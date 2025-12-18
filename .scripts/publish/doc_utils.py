# .scripts/doc_utils.py
import io
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from urllib.parse import urlparse

import yaml
import panflute as pf

from common import echo, die, run, format_long_date

# Ensure render helpers are importable (pnpmd_util lives under .scripts/render).
ROOT = Path(__file__).resolve().parents[2]
RENDER_DIR = ROOT / ".scripts" / "render"
if str(RENDER_DIR) not in sys.path:
    sys.path.append(str(RENDER_DIR))

from pnpmd_util import title_from_book_yaml


# ---- YAML dumper with nicer URL quoting ----

_URL_UNSAFE_CHARS = set(" \t()[]{}<>|\"'")


class PFYamlDumper(yaml.SafeDumper):
    # Disable anchors/aliases – always inline
    def ignore_aliases(self, data):
        return True


def _needs_double_quotes_for_url(s: str) -> bool:
    if "://" not in s:
        return False
    return any(c in _URL_UNSAFE_CHARS for c in s)


def _pf_represent_str(dumper: yaml.Dumper, data: str):
    style = '"' if _needs_double_quotes_for_url(data) else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


PFYamlDumper.add_representer(str, _pf_represent_str)


def dump_yaml(obj) -> str:
    return yaml.dump(
        obj,
        Dumper=PFYamlDumper,
        sort_keys=False,
        allow_unicode=True,
        width=1000,
        default_flow_style=False,
    )


# ---- markdown / PNPMD utils ----

def normalize_markdown_prose(md: str) -> str:
    if not md:
        return ""
    lines = md.replace("\r\n", "\n").split("\n")
    out: List[str] = []
    buf: List[str] = []

    def flush_buf():
        if buf:
            out.append(" ".join(x.strip() for x in buf if x.strip()))
            buf.clear()

    for line in lines:
        if not line.strip():
            flush_buf()
            out.append("")
        else:
            buf.append(line)
    flush_buf()
    return "\n".join(out).strip()


def replace_header_date(md_text: str, new_date_iso: str) -> str:
    lines = md_text.replace("\r\n", "\n").splitlines()
    long_date = format_long_date(new_date_iso)

    head_count = 0
    out: List[str] = []
    i = 0
    while i < len(lines) and lines[i].lstrip().startswith("%"):
        head_count += 1
        if head_count == 3:
            out.append(f"% {long_date}")
        else:
            out.append(lines[i])
        i += 1

    if head_count < 3:
        out.append(f"% {long_date}")

    out.extend(lines[i:])
    return "\n".join(out)


def _normalize_license_id(raw: str) -> str:
    """
    Normalize various license strings to a Zenodo-friendly identifier.
    Examples:
      "CC BY-NC-ND 4.0" -> "cc-by-nc-nd-4.0"
      "cc-by-nc-nd-4.0" -> "cc-by-nc-nd-4.0"
    """
    s = (raw or "").strip()
    if not s:
        return ""
    s = s.lower()
    s = s.replace("creative commons", "")
    s = re.sub(r"[\\s_]+", "-", s)
    s = s.strip("-")
    # Ensure cc- prefix
    if s and not s.startswith("cc-") and s.startswith("by-"):
        s = "cc-" + s
    return s


def detect_license(primary_md: Path, book_yaml: Optional[Path]) -> Optional[str]:
    """
    Attempt to detect a license/rights string from book.yml (preferred) or the
    Markdown front matter, then normalize it for Zenodo.
    """
    def _from_yaml(path: Path) -> Optional[str]:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            if isinstance(data, dict):
                for key in ("license", "licence", "rights"):
                    val = data.get(key)
                    if isinstance(val, str):
                        return val
        except Exception:
            return None
        return None

    candidates = []
    if book_yaml and book_yaml.exists():
        v = _from_yaml(book_yaml)
        if v:
            candidates.append(v)

    # front matter of markdown
    try:
        txt = primary_md.read_text(encoding="utf-8").replace("\\r\\n", "\\n")
        m = re.match(r"^---\\s*\\n(.*?)\\n---\\s*\\n", txt, flags=re.DOTALL)
        if m:
            fm = yaml.safe_load(m.group(1)) or {}
            if isinstance(fm, dict):
                for key in ("license", "licence", "rights"):
                    val = fm.get(key)
                    if isinstance(val, str):
                        candidates.append(val)
    except Exception:
        pass

    for c in candidates:
        norm = _normalize_license_id(c)
        if norm:
            return norm
    return None


# ---- PNPMD parsing ----

ORCID_URL_RE = re.compile(r"https?://orcid\.org/(\d{4}-\d{4}-\d{4}-\d{3}[0-9Xx])")
ORCID_ID_RE = re.compile(r"\b(\d{4}-\d{4}-\d{4}-\d{3}[0-9Xx])\b", re.IGNORECASE)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s\"<>]+", re.IGNORECASE)


def _norm_orcid(s: str) -> str:
    return s.upper().replace(" ", "")


def _key(n: str) -> str:
    import unicodedata

    n = unicodedata.normalize("NFKC", n).lower()
    return " ".join(ch for ch in re.sub(r"[^0-9a-z. ]+", " ", n).split())


def _collect_section(doc: pf.Doc, title: str):
    blocks = list(doc.content)
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if isinstance(b, pf.Header) and pf.stringify(b).strip().lower() == title.lower():
            level = b.level
            j = i + 1
            out = []
            while j < len(blocks):
                if isinstance(blocks[j], pf.Header) and blocks[j].level <= level:
                    break
                out.append(blocks[j])
                j += 1
            return out
        i += 1
    return []


def _listish(blocks):
    for b in blocks:
        if isinstance(b, (pf.BulletList, pf.OrderedList)):
            for li in b.content:
                yield li
        elif isinstance(b, pf.ListItem):
            yield b
        elif isinstance(b, pf.Para):
            yield b


def _stringify_blocks(blocks) -> str:
    blks = list(blocks)
    if not blks:
        return ""
    return pf.stringify(pf.Div(*blks)).strip()


def _extract_about_authors(items) -> List[Dict[str, str]]:
    authors: List[Dict[str, str]] = []
    for it in items:
        text = pf.stringify(it).strip()
        if not text:
            continue
        name = text.split(",", 1)[0].strip()

        m_email = EMAIL_RE.search(text)
        email = m_email.group(0) if m_email else None

        m_orcid_url = ORCID_URL_RE.search(text)
        m_orcid_id = ORCID_ID_RE.search(text)
        orcid = None
        if m_orcid_url:
            orcid = _norm_orcid(m_orcid_url.group(1))
        elif m_orcid_id:
            orcid = _norm_orcid(m_orcid_id.group(1))

        entry: Dict[str, str] = {"name": name}
        if orcid:
            entry["orcid"] = orcid
        if email:
            entry["email"] = email
        authors.append(entry)
    return authors


def _pandoc_doc(md_text: str) -> pf.Doc:
    proc = subprocess.run(
        ["pandoc", "-f", "markdown+tex_math_dollars", "-t", "json"],
        input=md_text.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    ast = json.loads(proc.stdout)
    return pf.load(io.StringIO(json.dumps(ast)))


def parse_pnpmd(md_text: str) -> Dict:
    doc = _pandoc_doc(md_text)
    meta = doc.get_metadata()

    def _meta_str(x):
        return x if isinstance(x, str) else pf.stringify(x) if x is not None else ""

    def _split_header_authors(s: str) -> List[str]:
        parts = re.split(r"\s+\band\b\s+|;", s)
        if len(parts) == 1:
            parts = re.split(r",(?![^()]*\))", s)
        return [p.strip() for p in parts if p.strip()]

    title = _meta_str(meta.get("title", ""))
    pub_date = _meta_str(meta.get("date", ""))

    raw_auth = meta.get("author")
    if isinstance(raw_auth, list):
        if len(raw_auth) == 1 and isinstance(raw_auth[0], str):
            header_authors = _split_header_authors(raw_auth[0])
        else:
            header_authors = [_meta_str(a) for a in raw_auth]
    elif isinstance(raw_auth, str):
        header_authors = _split_header_authors(raw_auth)
    else:
        header_authors = []

    one_sentence = _stringify_blocks(_collect_section(doc, "One-Sentence Summary")).strip()
    abstract = _stringify_blocks(_collect_section(doc, "Abstract")).strip()
    kb_text = _stringify_blocks(_collect_section(doc, "Keywords"))
    about_blocks = _collect_section(doc, "About Author(s)")
    refs_blocks = _collect_section(doc, "References")

    first_line = next((ln.strip() for ln in kb_text.splitlines() if ln.strip()), "")
    keywords = [k.strip() for k in first_line.split(",") if k.strip()] if first_line else []

    about_items = list(_listish(about_blocks))
    about_parsed = _extract_about_authors(about_items)
    about_index = {_key(a["name"]): a for a in about_parsed}

    merged: List[Dict[str, str]] = []

    if header_authors:
        for nm in header_authors:
            k = _key(nm)
            if k in about_index:
                e = dict(about_index[k])
                e["name"] = nm
                merged.append(e)
            else:
                merged.append({"name": nm})
    else:
        merged = list(about_parsed)

    refs_text = _stringify_blocks(refs_blocks)
    ref_dois = sorted({m.group(0).rstrip(".,);:]") for m in DOI_RE.finditer(refs_text)})
    reference_doi_urls = [f"https://doi.org/{d}" for d in ref_dois]

    full_text = pf.stringify(doc)
    global_orcids = sorted(
        {_norm_orcid(m.group(1)) for m in ORCID_URL_RE.finditer(full_text)}
        | {_norm_orcid(m.group(1)) for m in ORCID_ID_RE.finditer(full_text)}
    )
    if global_orcids and all("orcid" not in a for a in merged) and merged:
        merged[0]["orcid"] = global_orcids[0]

    return {
        "title": title,
        "date": pub_date,
        "one_sentence": one_sentence,
        "abstract": abstract,
        "keywords": keywords,
        "authors": merged,
        "reference_doi_urls": reference_doi_urls,
    }


# ---- site layout ----

def compute_site_base_url(site_repo: Path) -> str:
    candidates = [
        site_repo / "site" / "CNAME",
        site_repo / "CNAME",
    ]
    for p in candidates:
        if p.exists():
            raw = p.read_text(encoding="utf-8").splitlines()
            if not raw:
                continue
            v = raw[0].strip()
            if not v:
                continue
            if v.startswith("http://") or v.startswith("https://"):
                return v.rstrip("/")
            return "https://" + v.rstrip("/")

    v = os.environ.get("BASE_URL")
    if v:
        return v.rstrip("/")

    return "http://127.0.0.1:8000"


def infer_journal_from_site_base(site_base: str) -> str:
    try:
        host = (urlparse(site_base).hostname or "").lower()
    except Exception:
        host = ""
    if "writing.preferredframe.com" in host or host.startswith("writing."):
        return "Preferred Frame Writing"
    if "preprints.preferredframe.com" in host or host.startswith("preprints."):
        return "Preferred Frame Pre-Prints"
    return "Preferred Frame"


# ---- staging render (with book mode support) ----

def render_in_staging(
    site_repo: Path,
    subjournal: str,
    src_md: Path,
    publication_date_iso: str,
    book_yaml: Optional[Path] = None,
    render_args: Optional[List[str]] = None,
) -> Tuple[Path, Path, Path, Path, Optional[Path]]:
    """
    Stage and render the main PNPMD .md, and optionally a book .yml (book mode).

    Returns:
        staging_dir, staged_md, staged_pdf, staged_html, staged_epub (or None)
    """
    stem = src_md.stem
    staging = site_repo / subjournal / "_staging" / stem
    staging.mkdir(parents=True, exist_ok=True)

    base_render_args = list(render_args or [])

    script_dir = Path(__file__).resolve().parent
    render_py = script_dir.parent / "render" / "render.py"
    if not render_py.exists():
        die(f"render.py not found at expected location: {render_py}")

    # ---- Book mode ----
    if book_yaml is not None:
        book_dir = book_yaml.parent
        echo(f"+ copy book dir {book_dir} -> {staging}")
        for p in book_dir.iterdir():
            if p.is_file():
                shutil.copy2(p, staging / p.name)

        dst_yaml = staging / book_yaml.name
        run(
            [sys.executable, str(render_py), "--all", "--epub", *base_render_args, str(dst_yaml)],
            cwd=staging,
            check=True,
        )

        base_title = title_from_book_yaml(dst_yaml)
        human_md = staging / f"{base_title}.md"
        pandoc_md = staging / f"{base_title}.pandoc.md"

        pdf_src = pandoc_md.with_suffix(".pdf")  # e.g., .pandoc.pdf
        html_src = pandoc_md.with_suffix(".html")
        epub_src = pandoc_md.with_suffix(".epub")

        pdf_dst = staging / f"{base_title}.pdf"
        html_dst = staging / f"{base_title}.html"
        epub_dst = staging / f"{base_title}.epub"

        # Rename pandoc outputs to user-friendly names.
        if pdf_src.exists():
            pdf_src.rename(pdf_dst)
        if html_src.exists():
            html_src.rename(html_dst)
        if epub_src.exists():
            epub_src.rename(epub_dst)

        for p in (human_md, pdf_dst, html_dst, pandoc_md):
            if not p.exists():
                die(f"Expected artifact missing after render: {p}")
        staged_epub = epub_dst if epub_dst.exists() else None

        return staging, human_md, pdf_dst, html_dst, staged_epub

    # ---- main PNPMD .md ----
    dst_md = staging / src_md.name
    echo(f"+ copy {src_md} -> {dst_md}")
    shutil.copy2(src_md, dst_md)

    md_text = dst_md.read_text(encoding="utf-8")
    md_text = replace_header_date(md_text, publication_date_iso)
    dst_md.write_text(md_text, encoding="utf-8")

    run(
        [sys.executable, str(render_py), "--all", *base_render_args, str(dst_md)],
        cwd=staging,
        check=True,
    )

    dst_pdf = dst_md.with_suffix(".pdf")
    dst_html = dst_md.with_suffix(".html")
    dst_pmd = dst_md.with_suffix(".pandoc.md")
    for p in (dst_pdf, dst_html, dst_pmd):
        if not p.exists():
            die(f"Expected artifact missing after render: {p}")

    return staging, dst_md, dst_pdf, dst_html, None


# ---- provenance ----

def write_provenance(
    dst_dir: Path,
    dst_md: Path,
    dst_pdf: Path,
    dst_html: Path,
    dst_pmd: Path,
    dst_epub: Optional[Path],
    src_origin: str,
    src_commit: str,
    title: str,
    creators: List[Dict],
    parsed: Dict,
    publication_date: str,
    publication_year: str,
    doi: str,
    concept_doi: Optional[str],
    assets_pdf_url: str,
    assets_epub_url: Optional[str],
    site_html_url: str,
    site_md_url: str,
    site_pandoc_md_url: str,
    version_permalink: str,
    zenodo_metadata: Dict,
    journal_name: str,
    subjournal: str,
    change_log: Optional[str] = None,
    publication_type: str = "article",
) -> Path:

    artifacts: Dict[str, str] = {
        "md": dst_md.name,
        "md_url": site_md_url,
        "pandoc_md_name": dst_pmd.name,
        "pandoc_md_url": site_pandoc_md_url,
        "pdf_name": dst_pdf.name,
        "pdf_url": assets_pdf_url,
        "html_name": dst_html.name,
        "html_url": site_html_url,
        "primary": "md",
    }
    if dst_epub is not None and assets_epub_url:
        artifacts["epub_name"] = dst_epub.name
        artifacts["epub_url"] = assets_epub_url

    prov = {
        "journal": journal_name,
        "subjournal": subjournal,
        "publication_type": publication_type,
        "title": title,
        "doi": doi,
        "concept_doi": concept_doi,
        "permalink": version_permalink,
        "publication_date": publication_date,
        "publication_year": publication_year,
        "keywords": parsed["keywords"],
        "one_sentence_summary": normalize_markdown_prose(parsed["one_sentence"]),
        "abstract": normalize_markdown_prose(parsed["abstract"]),
        "authors": creators,
        "references_doi": parsed["reference_doi_urls"],
        "zenodo_metadata": zenodo_metadata,
        "change_log": change_log or "",
        "source": {
            "repo_origin": src_origin,
            "commit": src_commit,
            "filename": dst_md.name,
        },
        "artifacts": artifacts,
    }

    prov_path = dst_dir / "provenance.yaml"
    echo(f"+ write {prov_path}")
    prov_path.write_text(dump_yaml(prov), encoding="utf-8")
    return prov_path


# ---- provenance discovery ----

def find_latest_provenance_for_stem(
    site_repo: Path, subjournal: str, stem: str
) -> Tuple[Optional[Path], Optional[Dict]]:
    base = site_repo / subjournal / stem
    if not base.exists():
        return None, None

    provs: List[Tuple[Path, Dict]] = []
    for p in base.rglob("provenance.yaml"):
        try:
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            provs.append((p, data))
        except Exception:
            continue

    if not provs:
        return None, None

    def prov_key(item):
        p, d = item
        return (d.get("publication_date", ""), str(p))

    provs.sort(key=prov_key)
    return provs[-1]
