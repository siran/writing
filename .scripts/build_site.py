#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import urllib.parse
import shutil
import re
import json
from pathlib import Path
from dataclasses import dataclass
from urllib.parse import urlparse, quote
from datetime import datetime, date, timezone
from zoneinfo import ZoneInfo

import yaml
from feedgen.feed import FeedGenerator

# ---------- config ----------
EXCLUDE_NAMES = {
    "site", "venv", ".venv", "env", ".env", "node_modules", ".git",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".cache",
    "Makefile", "index.html", "_staging", "pnpmd.map", "requirements.txt",
    "gpt5push.sh",
}

MIRROR_EXTS = {
    ".md",
    ".markdown",
    ".html",
    ".htm",
    ".yaml",
    ".yml",
    ".pandoc.md",
    ".txt",
}

MD_EXTS = {".md", ".markdown", ".pandoc.md"}

PREFERRED_JOURNAL = "Preferred Frame Writing"

# ---------- repo autodetect ----------

def _parse_remote(url: str) -> tuple[str | None, str | None]:
    try:
        if url.startswith("git@"):
            path = url.split(":", 1)[1]
        else:
            path = urllib.parse.urlparse(url).path.lstrip("/")
        if path.endswith(".git"):
            path = path[:-4]
        owner, repo = path.split("/", 1)
        return owner, repo
    except Exception:
        return None, None


def detect_repo_branch() -> tuple[str, str, str]:
    owner = os.getenv("SITE_OWNER")
    repo = os.getenv("SITE_REPO")
    branch = os.getenv("SITE_BRANCH")

    gh = os.getenv("GITHUB_REPOSITORY")
    if gh and "/" in gh:
        o, r = gh.split("/", 1)
        owner = owner or o
        repo = repo or r
    branch = branch or os.getenv("GITHUB_REF_NAME")

    if not (owner and repo):
        try:
            url = subprocess.check_output(
                ["git", "config", "--get", "remote.origin.url"],
                text=True,
                stderr=subprocess.DEVNULL,
            ).strip()
            o, r = _parse_remote(url)
            owner = owner or o
            repo = repo or r
        except Exception:
            pass

    if not branch:
        try:
            branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                text=True,
                stderr=subprocess.DEVNULL,
            ).strip()
        except Exception:
            branch = "main"

    if not owner:
        owner = "siran"
    if not repo:
        repo = Path.cwd().name

    return owner, repo, branch


OWNER, REPO, BRANCH = detect_repo_branch()

# ---------- paths ----------
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"
SRC = ROOT / ".scripts" / "src"

# ---------- base url ----------

def compute_base_url() -> str:
    env_base = os.getenv("BASE_URL")
    if env_base:
        return env_base.rstrip("/")

    if os.getenv("GITHUB_ACTIONS", "").lower() == "true":
        return f"https://{OWNER}.github.io/{REPO}"

    return "http://127.0.0.1:8000"


BASE_URL = compute_base_url()


def write_cname_if_custom(base_url: str) -> None:
    host = urlparse(base_url).hostname
    if not host:
        return
    if host.endswith(".github.io"):
        return
    if host in {"localhost", "127.0.0.1"}:
        return

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "CNAME").write_text(host + "\n", encoding="utf-8")

# ---------- helpers ----------

def rel(p: Path) -> Path:
    return p.relative_to(ROOT)


def rel_out(p: Path) -> Path:
    return p.relative_to(OUT)


def load_text(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


@dataclass
class Item:
    name: str
    is_dir: bool
    mtime: float
    path: Path


def _asset_url(x) -> str:
    if not x:
        return ""
    if isinstance(x, str):
        return x.strip()
    if isinstance(x, dict):
        return (x.get("url") or x.get("href") or x.get("path") or "").strip()
    return ""


def _canonical_origin_from_provenance() -> str | None:
    try:
        prints_dir = ROOT / "prints"
        if not prints_dir.exists():
            return None

        for prov in prints_dir.glob("*/*/*/provenance.yaml"):
            try:
                data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
                u = (data.get("permalink") or "").strip()
                if not u:
                    site_block = (data.get("site") or {})
                    u = (
                        site_block.get("permalink")
                        or site_block.get("html_canonical")
                        or ""
                    ).strip()
                if u.startswith("http"):
                    p = urlparse(u)
                    if p.scheme and p.netloc:
                        return f"{p.scheme}://{p.netloc}"
            except Exception:
                continue
    except Exception:
        pass
    return None


def hidden_stems_from_provenance() -> set[str]:
    stems: set[str] = set()
    prints = ROOT / "prints"
    if not prints.exists():
        return stems

    for prov in prints.glob("*/*/*/provenance.yaml"):
        try:
            data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
            journal = (data.get("journal") or "").strip()
            if journal and journal != PREFERRED_JOURNAL:
                stems.add(prov.parent.parent.parent.name)
        except Exception:
            continue
    return stems

# ---------- templating ----------

def write_html(out_html: Path, body_html: str,
               head_extra: str = "", title: str = "") -> None:
    header = load_text(SRC / "header.html")
    footer = load_text(SRC / "footer.html")
    coda = load_text(SRC / "coda.html")

    doc = "".join(s for s in (header, body_html, footer) if s)

    if head_extra:
        charset = '<!DOCTYPE html><meta charset="UTF-8">'
        title_tag = f"<title>{title} - {PREFERRED_JOURNAL}</title>"
        if charset not in head_extra:
            head_extra = charset + "\n" + title_tag + "\n" + head_extra
        m = re.search(r"</head\s*>", doc, re.IGNORECASE)
        if m:
            doc = doc[:m.start()] + head_extra + doc[m.start():]
        else:
            doc = head_extra + doc

    ny = ZoneInfo("America/New_York")
    now = datetime.now(ny)
    offset = now.utcoffset()
    hrs = int(offset.total_seconds() // 3600) if offset else 0
    stamp = f"(built: {now.strftime('%Y-%m-%d %H:%M %Z')} UTC{hrs:+d})"

    if not doc.endswith("\n"):
        doc += "\n"
    doc += stamp
    if coda:
        doc += coda

    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(doc, encoding="utf-8")


def write_md_like_page(out_html: Path, md_body: str, head_extra: str = "") -> None:
    body = md_body.replace("&", "&amp;").replace("<", "&lt;")
    write_html(out_html, body, head_extra=head_extra)


def crumb_link(parts: list[str]) -> str:
    html = ['<nav class="breadcrumbs">', '<a href="/">🏠 Home</a>']
    base = ""
    for label in parts:
        base = base.rstrip("/") + "/" + quote(label)
        html.append(" / ")
        html.append(f'<a href="{base}/">📂 {label}</a>')
    html.append("</nav>")
    return "".join(html)

# ---------- dates ----------

def _to_datetime(obj) -> datetime | None:
    if isinstance(obj, datetime):
        return obj
    if isinstance(obj, date):
        return datetime.combine(obj, datetime.min.time())
    if isinstance(obj, str):
        s = obj.strip()
        for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
            try:
                return datetime.strptime(s, fmt)
            except Exception:
                pass
    return None


def month_year(d) -> str:
    dt = _to_datetime(d)
    if not dt:
        return str(d) if d is not None else ""
    return dt.strftime("%B %Y")


def scholar_date(x) -> str:
    if isinstance(x, datetime):
        return x.strftime("%Y/%m/%d")
    if isinstance(x, date):
        return x.strftime("%Y/%m/%d")
    if isinstance(x, str):
        x = x.strip()
        if not x:
            return ""
        if re.fullmatch(r"\d{4}-\d{2}-\d2", x):
            y, m, d = x.split("-")
            return f"{y}/{m}/{d}"
        if re.fullmatch(r"\d{4}-\d{2}", x):
            y, m = x.split("-")
            return f"{y}/{m}"
        if re.fullmatch(r"\d{4}", x):
            return x
        return x.replace("-", "/")
    return ""


def iso_date_str(x) -> str:
    if isinstance(x, datetime):
        return x.date().isoformat()
    if isinstance(x, date):
        return x.isoformat()
    if isinstance(x, str):
        return x.strip()
    return str(x) if x else ""


def extract_html_body(html_text: str) -> str:
    m_open = re.search(r"<body[^>]*>", html_text, flags=re.IGNORECASE | re.DOTALL)
    m_close = re.search(r"</body\s*>", html_text, flags=re.IGNORECASE | re.DOTALL)
    if m_open and m_close and m_close.start() > m_open.end():
        return html_text[m_open.end():m_close.start()]
    return html_text

# ---------- authors ----------

def _orcid_url(v: str) -> str:
    v = (v or "").strip()
    if not v:
        return ""
    if v.startswith("http"):
        return v
    m = re.search(r"(\d{4}-\d{4}-\d{4}-\d{3}[0-9Xx])", v)
    return f"https://orcid.org/{m.group(1).upper()}" if m else ""


def normalize_authors(auth_list):
    out = []
    for a in (auth_list or []):
        if isinstance(a, dict):
            nm = (a.get("name") or a.get("full_name") or "").strip()
            oc = _orcid_url(a.get("orcid") or a.get("id") or a.get("orcid_id") or "")
            em = (a.get("email") or "").strip()
        else:
            nm = str(a).strip()
            oc = ""
            em = ""
        if not nm or nm.lower() == "name":
            continue
        item = {"name": nm}
        if oc:
            item["orcid"] = oc
        if em:
            item["email"] = em
        out.append(item)
    return out


def fmt_author(a: dict) -> str:
    nm = a.get("name", "").strip()
    oc = _orcid_url(a.get("orcid", "").strip())
    if not nm:
        return ""
    if oc:
        return f'{nm} (<a href="{oc}">ORCID</a>)'
    return nm

# ---------- article helpers ----------

def _mirror_artifact_files(src: Path) -> None:
    for f in src.iterdir():
        if f.is_file() and f.suffix.lower() in MIRROR_EXTS:
            dst = OUT / rel(f)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst)


def _local_artifact_paths(src: Path, rec: dict) -> tuple[str | None, str | None, str | None]:
    md_name = rec["md_name"]
    html_name = rec["html_name"]
    pmd_name = rec["pmd_name"]

    def _mk_local(name: str | None) -> str | None:
        if not name:
            return None
        return "/" + (OUT / rel(src / name)).relative_to(OUT).as_posix()

    return _mk_local(md_name), _mk_local(html_name), _mk_local(pmd_name)


def _load_html_from_artifact(src: Path, html_name: str | None) -> str:
    if not html_name:
        return ""
    html_path = src / html_name
    if not html_path.exists():
        return ""
    try:
        return extract_html_body(html_path.read_text(encoding="utf-8"))
    except Exception:
        return ""


def _build_files_ul(local_html: str | None, local_md: str | None,
                    prov_path: Path, pdf_url: str | None) -> str:
    items = []
    prov_local = "/" + (OUT / rel(prov_path)).relative_to(OUT).as_posix()
    if local_html:
        items.append(f'<li><a href="{local_html}">{os.path.basename(local_html)}</a></li>')
    if local_md:
        items.append(f'<li><a href="{local_md}">{os.path.basename(local_md)}</a></li>')
    items.append(f'<li><a href="{prov_local}">provenance.yaml</a></li>')
    if pdf_url:
        items.append(f'<li><a href="{pdf_url}">PDF</a></li>')
    return "<ul>" + "".join(items) + "</ul>"


def _build_top_links(local_md: str | None, pdf_url: str | None,
                     local_pmd: str | None, latest_label: bool = False) -> str:
    links = []
    if local_md:
        label = "Markdown (latest)" if latest_label else "Markdown"
        links.append(f'<a href="{local_md}">{label}</a>')
    if pdf_url:
        label = "PDF (latest)" if latest_label else "PDF"
        links.append(f'<a href="{pdf_url}">{label}</a>')
    if local_pmd:
        links.append(f'<a href="{local_pmd}">Preprocessed MD</a>')
    return " · ".join(links)


def _build_article_ld(it: dict, page_url: str, pdf_url: str | None) -> dict:
    authors_ld = []
    for a in it["authors"]:
        nm = a.get("name", "").strip()
        oc = _orcid_url(a.get("orcid", "").strip())
        if not nm:
            continue
        ent = {"@type": "Person", "name": nm}
        if oc:
            ent["sameAs"] = [oc]
        authors_ld.append(ent)
    enc = []
    if pdf_url:
        enc.append({
            "@type": "MediaObject",
            "contentUrl": pdf_url,
            "encodingFormat": "application/pdf",
        })
    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": it["title"],
        "author": authors_ld or [{"@type": "Person", "name": "Unknown"}],
        "datePublished": iso_date_str(it["date"]),
        "isPartOf": {"@type": "Periodical", "name": "Preferred Frame"},
        "url": page_url,
    }
    if enc:
        article_ld["encoding"] = enc
    if it["doi"]:
        article_ld["sameAs"] = [f"https://doi.org/{it['doi'].split('/')[-1]}"]
    return article_ld


def _build_article_head(it: dict, page_url: str, pdf_url: str | None) -> str:
    head: list[str] = []
    head.append('<meta charset="UTF-8">')
    head.append(f'<link rel="canonical" href="{page_url}">')
    if pdf_url:
        head.append(f'<link rel="alternate" type="application/pdf" href="{pdf_url}">')
    head.append('<meta name="robots" content="index,follow">')
    if it["title"]:
        head.append(f'<meta name="citation_title" content="{it["title"]}">')
    for a in it["authors"]:
        nm = a.get("name", "")
        if nm:
            head.append(f'<meta name="citation_author" content="{nm}">')
    if it["date"]:
        head.append(
            f'<meta name="citation_publication_date" content="{scholar_date(it["date"])}">'
        )
    head.append('<meta name="citation_journal_title" content="Preferred Frame">')
    if pdf_url:
        head.append(f'<meta name="citation_pdf_url" content="{pdf_url}">')
    if it["doi"]:
        head.append(f'<meta name="citation_doi" content="{it["doi"]}">')

    desc = it["abstract"] or it["onesent"] or it["title"]
    if desc:
        head.append(f'<meta name="description" content="{desc}">')
        head.append(f'<meta property="og:description" content="{desc}">')

    head.append('<meta property="og:type" content="article">')
    head.append(f'<meta property="og:title" content="{it["title"]}">')
    head.append(f'<meta property="og:url" content="{page_url}">')

    article_ld = _build_article_ld(it, page_url, pdf_url)
    head.append(
        '<script type="application/ld+json">'
        + json.dumps(article_ld, ensure_ascii=False)
        + "</script>"
    )
    return "\n".join(head) + "\n"

# ---------- article pages ----------

def build_article_pages() -> None:
    """
    Build article/version/stem pages for any provenance.yaml that lives in:

        <base>/<stem>/<doi_prefix>/<doi_suffix>/provenance.yaml

    where <base> can be 'prints', 'documents', etc.
    """
    records: list[dict] = []

    for prov in ROOT.rglob("provenance.yaml"):
        rel_parent = prov.parent.relative_to(ROOT)
        parts = rel_parent.parts
        # need at least base/stem/prefix/suffix
        if len(parts) < 4:
            continue

        base = parts[0]
        stem = parts[-3]
        doi_prefix = parts[-2]
        doi_suffix = parts[-1]

        data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
        pf_block = data.get("parsed_from_pnpmd") or {}

        title = (data.get("title") or pf_block.get("title") or "") or ""
        abstract = (data.get("abstract") or pf_block.get("abstract") or "") or ""
        kws = (data.get("keywords") or pf_block.get("keywords") or []) or []
        onesent = (
            data.get("one_sentence_summary")
            or pf_block.get("one_sentence_summary")
            or pf_block.get("one_sentence")
            or ""
        )
        onesent = (onesent or "").strip()

        authors = normalize_authors(data.get("authors") or pf_block.get("authors"))

        date_norm = (
            data.get("publication_date")
            or data.get("creation_date")
            or pf_block.get("date")
            or ""
        )

        zenodo = data.get("zenodo") or {}
        doi = (data.get("doi") or zenodo.get("doi") or "") or ""
        concept = (data.get("concept_doi") or zenodo.get("concept_doi") or "") or ""

        permalink = (data.get("permalink") or "").strip()
        site_block = data.get("site") or {}
        html_canonical = (
            site_block.get("html_canonical")
            or site_block.get("permalink")
            or permalink
            or ""
        ).strip()

        assets = (data.get("assets") or {})
        canonical_assets = (data.get("canonical_assets") or {})
        artifacts = (data.get("artifacts") or {})

        md_name = artifacts.get("md") or artifacts.get("main")
        html_name = artifacts.get("html_name")
        pmd_name = artifacts.get("pandoc_md_name") or artifacts.get("pandoc_md")

        add_old = artifacts.get("additional") or {}
        if not html_name:
            html_name = add_old.get("html")
        if not pmd_name:
            pmd_name = add_old.get("pandoc_md")

        if not md_name and artifacts.get("md_url"):
            md_name = Path(artifacts["md_url"]).name
        if not html_name and artifacts.get("html_url"):
            html_name = Path(artifacts["html_url"]).name
        if not pmd_name and artifacts.get("pandoc_md_url"):
            pmd_name = Path(artifacts["pandoc_md_url"]).name

        assets_pdf = (
            artifacts.get("pdf_url")
            or _asset_url(assets.get("pdf"))
            or _asset_url(canonical_assets.get("pdf"))
            or ""
        )

        references_doi = data.get("references_doi") or pf_block.get("references_doi") or []
        if not isinstance(references_doi, list):
            references_doi = [references_doi]

        records.append(
            {
                "prov": prov,
                "base": base,
                "rel_parent": rel_parent,
                "stem": stem,
                "doi_prefix": doi_prefix,
                "doi_suffix": doi_suffix,
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "onesent": onesent,
                "kws": kws,
                "date": date_norm,
                "doi": doi,
                "concept": concept,
                "assets_pdf": assets_pdf,
                "md_name": md_name,
                "html_name": html_name,
                "pmd_name": pmd_name,
                "html_canonical": html_canonical,
                "references_doi": references_doi,
            }
        )

    if not records:
        return

    groups: dict[tuple[str, str], list[dict]] = {}
    for r in records:
        key = (r["base"], r["stem"])
        groups.setdefault(key, []).append(r)

    for (base, stem), items in groups.items():

        def sort_key(it: dict) -> datetime:
            dt = _to_datetime(it["date"])
            if dt:
                return dt
            return datetime.fromtimestamp(it["prov"].stat().st_mtime)

        versions = sorted(items, key=sort_key, reverse=True)
        latest = versions[0]

        # each VERSION page
        for it in versions:
            src = it["prov"].parent
            out_dir = OUT / it["rel_parent"]
            out_dir.mkdir(parents=True, exist_ok=True)

            _mirror_artifact_files(src)

            local_md, local_html, local_pmd = _local_artifact_paths(src, it)
            html_body = _load_html_from_artifact(src, it["html_name"])

            top_links = _build_top_links(local_md, it["assets_pdf"], local_pmd)
            breadcrumbs_html = crumb_link(
                [it["base"], it["stem"], it["doi_prefix"], it["doi_suffix"]]
            )

            files_ul = _build_files_ul(
                local_html, local_md, it["prov"], it["assets_pdf"]
            )

            display_authors = it["authors"]
            authors_html = ", ".join(
                filter(None, (fmt_author(a) for a in display_authors))
            )

            body_parts: list[str] = []
            body_parts.append("<main class='paper'>")
            body_parts.append(breadcrumbs_html)
            body_parts.append(f"<h1>{it['title']}</h1>")
            if authors_html:
                body_parts.append(f"<p class='authors'>{authors_html}</p>")
            body_parts.append(
                f"<p class='publine'>Preferred Frame — {month_year(it['date'])}</p>"
            )
            body_parts.append(f"<p class='links'>{top_links}</p>")

            if it["onesent"]:
                body_parts.append("<h2>One-Sentence Summary</h2>")
                body_parts.append(f"<p>{it['onesent']}</p>")

            if it["abstract"]:
                body_parts.append("<h2>Abstract</h2>")
                body_parts.append(f"<p>{it['abstract']}</p>")

            body_parts.append("<h2>Files</h2>")
            body_parts.append(files_ul)

            if html_body:
                body_parts.append("<h2>Article</h2>")
                body_parts.append(html_body)

            if it["references_doi"]:
                refs_items = []
                for ref_url in it["references_doi"]:
                    ref_url = (ref_url or "").strip()
                    if not ref_url:
                        continue
                    refs_items.append(f'<li><a href="{ref_url}">{ref_url}</a></li>')
                if refs_items:
                    body_parts.append("<h2>References (DOI)</h2>")
                    body_parts.append("<ul>" + "".join(refs_items) + "</ul>")

            body_parts.append("</main>")

            version_url = (
                f"{BASE_URL}/{it['base']}/{it['stem']}/"
                f"{it['doi_prefix']}/{it['doi_suffix']}/"
            )
            head_extra = _build_article_head(it, version_url, it["assets_pdf"])

            body_html = "\n".join(body_parts)
            write_html(out_dir / "index.html", body_html, head_extra=head_extra)

            # DOI alias only for prints, as before
            if it["base"] == "prints":
                alias_dir = (
                    OUT / "prints" / "doi" / it["doi_prefix"] / it["doi_suffix"]
                )
                alias_dir.mkdir(parents=True, exist_ok=True)
                write_html(alias_dir / "index.html", body_html, head_extra=head_extra)

        # STEM page (latest) – for all bases
        it = latest
        src = it["prov"].parent
        stem_out = OUT / it["base"] / it["stem"]
        stem_out.mkdir(parents=True, exist_ok=True)

        _mirror_artifact_files(src)

        local_md, local_html, local_pmd = _local_artifact_paths(src, it)
        html_body = _load_html_from_artifact(src, it["html_name"])

        breadcrumbs_stem = crumb_link([it["base"], it["stem"]])

        versions_list = []
        for v in versions:
            ver_url = (
                f"/{it['base']}/{it['stem']}/{v['doi_prefix']}/{v['doi_suffix']}/"
            )
            doi_disp = f"{v['doi_prefix']}/{v['doi_suffix']}"
            date_disp = v["date"] or ""
            versions_list.append(
                f"<li>{date_disp} — <a href='{ver_url}'>{doi_disp}</a></li>"
            )
        versions_ul = "<ul>" + "".join(versions_list) + "</ul>"

        files_ul = _build_files_ul(local_html, local_md, it["prov"], it["assets_pdf"])
        top_links = _build_top_links(
            local_md, it["assets_pdf"], local_pmd, latest_label=True
        )

        display_authors = it["authors"]
        authors_html = ", ".join(
            filter(None, (fmt_author(a) for a in display_authors))
        )

        body_parts = []
        body_parts.append("<main class='paper'>")
        body_parts.append(breadcrumbs_stem)
        body_parts.append(f"<h1>{it['title']}</h1>")
        if authors_html:
            body_parts.append(f"<p class='authors'>{authors_html}</p>")
        body_parts.append(
            f"<p class='publine'>Preferred Frame — {month_year(it['date'])}</p>"
        )
        body_parts.append(f"<p class='links'>{top_links}</p>")

        if versions_ul:
            body_parts.append("<h2>Versions</h2>")
            body_parts.append(versions_ul)

        body_parts.append("<h2>Files (latest)</h2>")
        body_parts.append(files_ul)

        if it["onesent"]:
            body_parts.append("<h2>One-Sentence Summary</h2>")
            body_parts.append(f"<p>{it['onesent']}</p>")

        if it["abstract"]:
            body_parts.append("<h2>Abstract</h2>")
            body_parts.append(f"<p>{it['abstract']}</p>")

        if html_body:
            body_parts.append("<h2>Article (latest)</h2>")
            body_parts.append(html_body)

        if it["references_doi"]:
            refs_items = []
            for ref_url in it["references_doi"]:
                ref_url = (ref_url or "").strip()
                if not ref_url:
                    continue
                refs_items.append(f'<li><a href="{ref_url}">{ref_url}</a></li>')
            if refs_items:
                body_parts.append("<h2>References (DOI)</h2>")
                body_parts.append("<ul>" + "".join(refs_items) + "</ul>")

        body_parts.append("</main>")

        stem_url = f"{BASE_URL}/{it['base']}/{it['stem']}/"
        head_extra = _build_article_head(it, stem_url, it["assets_pdf"])

        write_html(
            stem_out / "index.html",
            "\n".join(body_parts),
            head_extra=head_extra,
            title=it["title"],
        )

# ---------- dir index ----------

def breadcrumbs(rel_dir: Path) -> str:
    depth = len(rel_dir.parts)
    to_root = "./" if depth == 0 else "../" * depth
    items = [f"[🏠 Home]({to_root})"]
    for i, part in enumerate(rel_dir.parts):
        up = "../" * (len(rel_dir.parts) - i - 1) or "./"
        items.append(f"/ [📂 {part}]({up})")
    return " ".join(items)


def format_dir_index(dir_abs: Path, items: list[Item]) -> str:
    rel_dir = rel(dir_abs) if dir_abs != ROOT else Path()
    title = rel_dir.name or f"{REPO} index"

    lines: list[str] = []
    lines.append(f"## {title}")
    lines.append("")
    lines.append(breadcrumbs(rel_dir))
    lines.append("")

    items_sorted = sorted(items, key=lambda e: (not e.is_dir, e.name.lower()))
    for it in items_sorted:
        if it.is_dir:
            href = (it.name + "/") if rel_dir.parts else (rel(it.path).as_posix() + "/")
            lines.append(f"- 📂 [{href}]({href})")
        else:
            p_rel = rel(it.path)
            mirrored = OUT / p_rel
            lines.append(f"- 📄 {it.name}")
            if mirrored.exists():
                url_local = "/" + mirrored.relative_to(OUT).as_posix()
                ext = it.path.suffix.lower()
                if ext in MD_EXTS:
                    gh_url = (
                        f"https://github.com/{OWNER}/{REPO}/blob/"
                        f"{BRANCH}/{p_rel.as_posix()}"
                    )
                    lines.append(
                        f"  - [open]({url_local}) · [open rendered]({gh_url})"
                    )
                else:
                    lines.append(f"  - [open]({url_local})")
    lines.append("")
    return "\n".join(lines)


def copy_static() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ["submit.html"]:
        src = SRC / name
        if src.exists():
            dst = OUT / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

# ---------- sitemap & robots ----------

def _url_from_out_path(p: Path) -> str:
    rp = rel_out(p).as_posix()
    if rp == "index.html":
        return f"{BASE_URL}/"
    if rp.endswith("/index.html"):
        return f"{BASE_URL}/" + rp[:-10]
    if p.suffix.lower() == ".html" and p.parent == OUT:
        return f"{BASE_URL}/" + rp
    return ""


def build_sitemap_and_robots() -> None:
    origin = (
        os.getenv("BASE_URL")
        or _canonical_origin_from_provenance()
        or BASE_URL
    ).rstrip("/")

    def _remap_origin(loc: str) -> str:
        try:
            p = urlparse(loc)
            return f"{origin}{p.path}"
        except Exception:
            return loc

    urls: list[tuple[str, str]] = []
    for path in OUT.rglob("*.html"):
        if path.name.startswith("."):
            continue
        loc = _url_from_out_path(path)
        if not loc:
            continue
        loc = _remap_origin(loc)
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        lastmod = mtime.strftime("%Y-%m-%dT%H:%M:%SZ")
        urls.append((loc, lastmod))

    seen: dict[str, str] = {}
    for loc, lastmod in urls:
        if (loc not in seen) or (lastmod > seen[loc]):
            seen[loc] = lastmod

    items = []
    for loc, lastmod in sorted(seen.items()):
        items.append(
            "  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            "    <changefreq>weekly</changefreq>\n"
            "    <priority>0.6</priority>\n"
            "  </url>"
        )

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(items)
        + "\n</urlset>\n"
    )
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    robots = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {origin}/sitemap.xml\n"
    )
    (OUT / "robots.txt").write_text(robots, encoding="utf-8")

# ---------- RSS ----------

def build_rss_feed() -> None:
    origin = (
        os.getenv("BASE_URL")
        or _canonical_origin_from_provenance()
        or BASE_URL
    ).rstrip("/")

    prints = ROOT / "prints"
    if not prints.exists():
        return

    by_stem: dict[str, dict] = {}

    for prov in prints.glob("*/*/*/provenance.yaml"):
        try:
            data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
        except Exception:
            continue

        stem = prov.parent.parent.parent.name
        pf_block = data.get("parsed_from_pnpmd") or {}

        title = (data.get("title") or pf_block.get("title") or stem)
        authors = normalize_authors(data.get("authors") or pf_block.get("authors"))
        abstract = (data.get("abstract") or pf_block.get("abstract") or "")
        onesent = (
            data.get("one_sentence_summary")
            or pf_block.get("one_sentence_summary")
            or pf_block.get("one_sentence")
            or ""
        )
        date_norm = (
            data.get("publication_date")
            or data.get("creation_date")
            or pf_block.get("date")
            or None
        )
        doi = (data.get("doi") or (data.get("zenodo") or {}).get("doi") or "")

        permalink = (data.get("permalink") or "").strip()
        if permalink and permalink.startswith("http"):
            item_url = permalink.rstrip("/")
        else:
            item_url = f"{origin}/prints/{stem}/"

        dt = _to_datetime(date_norm) or datetime.fromtimestamp(prov.stat().st_mtime)
        keep = by_stem.get(stem)
        if not keep or dt > keep["date"]:
            by_stem[stem] = {
                "stem": stem,
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "onesent": onesent,
                "date": dt,
                "url": item_url,
                "doi": doi,
            }

    fg = FeedGenerator()
    fg.load_extension("podcast")
    fg.title("Preferred Frame — Publications")
    fg.link(href=origin + "/", rel="alternate")
    fg.link(href=origin + "/rss.xml", rel="self")
    fg.description("Latest publications from Preferred Frame")
    fg.language("en")

    items = sorted(by_stem.values(), key=lambda x: x["date"], reverse=True)
    for it in items:
        fe = fg.add_entry()
        fe.id(it["url"])
        fe.link(href=it["url"])
        fe.title(it["title"])
        desc = it["abstract"] or it["onesent"]
        if desc:
            fe.description(desc)
        for a in it["authors"]:
            nm = a.get("name", "").strip()
            if nm:
                fe.author({"name": nm})
        fe.pubDate(it["date"].astimezone(timezone.utc))
        if it["doi"]:
            fe.link(
                href=f'https://doi.org/{it["doi"].split("/")[-1]}',
                rel="related",
            )

    rss_xml = fg.rss_str(pretty=True).decode("utf-8")
    (OUT / "rss.xml").write_text(rss_xml, encoding="utf-8")

# ---------- build ----------

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    write_cname_if_custom(BASE_URL)

    print(f"[DEBUG] ROOT: {ROOT}")
    print(f"[DEBUG] OUT:  {OUT}")
    print(f"[DEBUG] SRC:  {SRC}")
    print(f"[DEBUG] BASE_URL: {BASE_URL}")

    # static assets from .scripts/src/site/
    site_src = SRC / "site"
    print(f"[DEBUG] site_src: {site_src} (exists={site_src.exists()})")
    if site_src.exists():
        for src_path in site_src.rglob("*"):
            if not src_path.is_file():
                continue
            rel_path = src_path.relative_to(site_src)

            if src_path.suffix.lower() == ".md":
                # about.md -> about.md.html, wrapped in header/footer/coda
                dst_rel = rel_path.with_suffix(rel_path.suffix + ".html")
                dst_path = OUT / dst_rel
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                md_body = src_path.read_text(encoding="utf-8")
                print(f"[DEBUG] site MD -> {dst_rel}")
                write_html(dst_path, md_body, head_extra="", title=rel_path.stem)
            else:
                dst_path = OUT / rel_path
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dst_path)
                print(f"[DEBUG] site COPY -> {rel_path} -> {dst_path.relative_to(OUT)}")
    else:
        print("[DEBUG] WARNING: site_src does not exist; no site/ assets copied")

    # build article pages for any provenance.yaml
    build_article_pages()

    hidden_stems = hidden_stems_from_provenance()

    for dirpath, dirnames, filenames in os.walk(ROOT):
        d = Path(dirpath)

        # never descend into OUT itself
        if d == OUT:
            dirnames.clear()
            continue

        # hide foreign-journal stems under prints
        parts = d.relative_to(ROOT).parts if d != ROOT else ()
        if "prints" in parts:
            i = parts.index("prints")
            if len(parts) >= i + 2 and parts[i + 1] in hidden_stems:
                dirnames.clear()
                continue

        # prune child dirs
        kept_dirs: list[str] = []
        for dd in list(dirnames):
            child = d / dd
            if dd in EXCLUDE_NAMES:
                continue
            if dd.startswith(".") and dd != ".well-known":
                continue
            if (child / "pyvenv.cfg").exists():
                continue
            if d == ROOT / "prints" and dd in hidden_stems:
                continue
            kept_dirs.append(dd)
        dirnames[:] = kept_dirs

        # mirror all non-excluded files
        for fname in filenames:
            if fname.startswith("."):
                continue
            if fname in EXCLUDE_NAMES:
                continue
            if (d / "pyvenv.cfg").exists():
                continue
            p = d / fname
            dst = OUT / rel(p)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst)

        # build dir index if absent
        out_html = OUT / "index.html" if d == ROOT else OUT / rel(d) / "index.html"
        if out_html.exists():
            continue

        items: list[Item] = []

        # dirs
        for dd in sorted(dirnames, key=str.lower):
            p = d / dd
            items.append(
                Item(
                    name=dd,
                    is_dir=True,
                    mtime=p.stat().st_mtime,
                    path=p,
                )
            )

        # files
        for fname in sorted(filenames, key=str.lower):
            if fname.startswith("."):
                continue
            if fname in EXCLUDE_NAMES:
                continue
            p = d / fname
            items.append(
                Item(
                    name=fname,
                    is_dir=False,
                    mtime=p.stat().st_mtime,
                    path=p,
                )
            )

        md_body = format_dir_index(d, items)
        write_md_like_page(out_html, md_body)

    copy_static()
    build_sitemap_and_robots()
    build_rss_feed()


if __name__ == "__main__":
    main()
