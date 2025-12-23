#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, subprocess, urllib.parse, shutil, re, json, io, sys, concurrent.futures
from pathlib import Path
from dataclasses import dataclass
from urllib.parse import urlparse, quote
from datetime import datetime, date, timezone
from zoneinfo import ZoneInfo
import yaml
from feedgen.feed import FeedGenerator

# ---------- config ----------
EXCLUDE_NAMES = {
    "site","venv",".venv","env",".env","node_modules",".git",
    "__pycache__", ".mypy_cache",".pytest_cache",".ruff_cache",".cache",
    "Makefile","index.html","_staging", "pnpmd.map", "requirements.txt",
    "gpt5push.sh",
    # Root pages that should be linked from nav but not listed in dir indexes
    "about.md",
    "about.md.html",
    "journals.md",
    "journals.md.html",
    "policies.md",
    "policies.md.html",
    "submissions.md",
    "submissions.md.html",
    "CNAME"
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
    ".css",
    ".pdf",
    ".epub",
}

MD_EXTS = {".md", ".markdown", ".pandoc.md"}

# ---------- Journal naming based on CNAME ----------
DEFAULT_JOURNAL = "Preferred Frame"
PREFERRED_JOURNAL = DEFAULT_JOURNAL

# ---------- repo autodetect ----------
def _parse_remote(url: str):
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

def detect_repo_branch():
    owner = os.getenv("SITE_OWNER")
    repo  = os.getenv("SITE_REPO")
    branch= os.getenv("SITE_BRANCH")

    gh = os.getenv("GITHUB_REPOSITORY")
    if gh and "/" in gh:
        o, r = gh.split("/", 1)
        owner = owner or o
        repo  = repo  or r
    branch = branch or os.getenv("GITHUB_REF_NAME")

    if not (owner and repo):
        try:
            url = subprocess.check_output(
                ["git","config","--get","remote.origin.url"],
                text=True, stderr=subprocess.DEVNULL
            ).strip()
            o, r = _parse_remote(url)
            owner = owner or o
            repo  = repo  or r
        except Exception:
            pass
    if not branch:
        try:
            branch = subprocess.check_output(
                ["git","rev-parse","--abbrev-ref","HEAD"],
                text=True, stderr=subprocess.DEVNULL
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
ROOT = Path(__file__).resolve().parents[2]
OUT  = ROOT / "site"
SRC  = ROOT / ".scripts" / "src"

# ---------- .gitignore handling ----------
def load_gitignored_paths() -> set[Path]:
    try:
        out = subprocess.check_output(
            ["git", "ls-files", "-i", "--exclude-standard", "--others", "--directory"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return set()
    paths: set[Path] = set()
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        p = (ROOT / line.rstrip("/")).resolve()
        paths.add(p)
    return paths

GITIGNORED_PATHS = load_gitignored_paths()

def is_gitignored(path: Path) -> bool:
    p = path.resolve()
    for ign in GITIGNORED_PATHS:
        try:
            p.relative_to(ign)
            return True
        except ValueError:
            continue
    return False

# ---------- base url ----------
def compute_base_url() -> str:
    v = os.getenv("BASE_URL")
    if v:
        return v.rstrip("/")
    if os.getenv("GITHUB_ACTIONS", "").lower() == "true":
        return f"https://{OWNER}.github.io/{REPO}"
    return "http://127.0.0.1:8000"

BASE_URL = compute_base_url()

def write_cname_if_custom(base_url: str) -> None:
    root_cname = ROOT / "CNAME"
    if root_cname.exists():
        OUT.mkdir(parents=True, exist_ok=True)
        shutil.copy2(root_cname, OUT / "CNAME")
        return

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
    text = p.read_text(encoding="utf-8")

    # remove exactly one trailing newline
    if text.endswith("\n"):
        return text[:-1]
    return text

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


def _local_artifact_url(src_dir: Path, name: str | None) -> str:
    if not name:
        return ""
    # Artifacts may be generated only under OUT (staging), so compute the OUT path.
    out_path = OUT / rel(src_dir) / name
    return f"/{rel_out(out_path).as_posix()}"

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
                    u = (site_block.get("permalink") or site_block.get("html_canonical") or "").strip()
                if u.startswith("http"):
                    p = urlparse(u)
                    if p.scheme and p.netloc:
                        return f"{p.scheme}://{p.netloc}"
            except Exception:
                continue
    except Exception:
        pass
    return None

def iter_provenance_files():
    for top in ROOT.iterdir():
        if not top.is_dir():
            continue
        if top == OUT:
            continue
        if top.name in EXCLUDE_NAMES:
            continue
        if top.name.startswith(".") and top.name != ".well-known":
            continue
        for prov in top.glob("**/provenance.yaml"):
            if is_gitignored(prov):
                continue
            yield prov

def hidden_stems_from_provenance() -> set[tuple[str, str]]:
    stems_with_pref: set[tuple[str, str]] = set()
    stems_with_nonpref: set[tuple[str, str]] = set()

    for prov in iter_provenance_files():
        try:
            data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
        except Exception:
            continue

        j = (data.get("journal") or "").strip()
        rel_parts = rel(prov).parts
        if len(rel_parts) < 2:
            continue
        top, stem = rel_parts[0], rel_parts[1]
        key = (top, stem)

        if not j:
            continue
        if j == PREFERRED_JOURNAL:
            stems_with_pref.add(key)
        else:
            stems_with_nonpref.add(key)

    return {k for k in stems_with_nonpref if k not in stems_with_pref}

def _origin_from_cname() -> str | None:
    for base in (ROOT, OUT):
        cname = base / "CNAME"
        if not cname.exists():
            continue
        try:
            first_line = cname.read_text(encoding="utf-8").splitlines()[0].strip()
        except Exception:
            continue
        if not first_line:
            continue
        return f"https://{first_line}"
    return None

def _current_origin() -> str:
    return (
        _origin_from_cname()
        or _canonical_origin_from_provenance()
        or os.getenv("BASE_URL")
        or BASE_URL
    ).rstrip("/")

# ---------- templating ----------
def write_html(out_html: Path, body_html: str, head_extra: str = "", title: str = ""):
    # All pages (including *.md.html mirrors) get header + breadcrumb (for mirrors)
    # + body + footer + coda.
    header = load_text(SRC / "header.html")
    footer = load_text(SRC / "footer.html")
    coda   = load_text(SRC / "coda.html")

    rel_html = rel_out(out_html).as_posix()
    is_md_html = rel_html.endswith(".md.html")
    breadcrumb_html = ""
    if is_md_html:
        # Use same crumb_link style as article pages, based on path without trailing .html
        rel_no_html = re.sub(r"\.html$", "", rel_html)
        parts = list(Path(rel_no_html).parts)
        if parts and parts[-1] == "index":
            parts = parts[:-1]
        breadcrumb_html = crumb_link(parts)

    body_block = body_html
    if is_md_html:
        body_block = f'<div class="md-container">\n{body_block}\n</div>\n'

    doc = "".join(
        s for s in (
            header,
            breadcrumb_html + "\n" if breadcrumb_html else "",
            body_block,
            footer,
        ) if s
    )

    # NOTE: head_extra injection is currently disabled. Re-enable this block
    # if per-page <title>/<meta> should be injected again.
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

def render_markdown_file(src: Path, dst_html: Path, title: str):
    md = src.read_text(encoding="utf-8")
    # Replace YAML front matter with a Markdown H1 so mirrors show the title, not raw YAML.
    m_front = re.match(r"^---\s*\n(.*?)\n---\s*\n", md, flags=re.DOTALL)
    if m_front:
        front = m_front.group(1)
        title_val = None
        m_title = re.search(r"^title\s*:\s*(.+)$", front, flags=re.MULTILINE)
        if m_title:
            title_val = m_title.group(1).strip().strip('"\'')
        # Remove front matter
        md = md[m_front.end():]
        if title_val:
            md = f"# {title_val}\n\n" + md
    # Human-first: embed the markdown body as-is (styled by the site chrome).
    body_html = md

    rel_html = dst_html.relative_to(OUT).as_posix()
    origin = _current_origin()
    page_url = f"{origin}/{rel_html}"
    head = [
        '<meta charset="utf-8">',
        f'<link rel="canonical" href="{page_url}">',
        f'<meta name="description" content="Rendered Markdown view for {title}">',
    ]
    head_extra = "\n".join(head) + "\n"

    write_html(dst_html, body_html, head_extra=head_extra, title=title)

def render_md_formats(src_in_site: Path, rel_path: Path, *, do_pdf: bool, do_epub: bool):
    """
    Render PDF/EPUB for a mirrored Markdown file (already under OUT) using render.py.
    Outputs are written next to the mirrored file in OUT.
    """
    if not (do_pdf or do_epub):
        return

    render_py = ROOT / ".scripts" / "render" / "render.py"
    if not render_py.exists():
        print(f"[DEBUG] render.py not found at {render_py}; skipping md formats for {rel_path}")
        return

    cmd = [sys.executable, str(render_py)]
    if do_pdf:
        cmd.append("--pdf")
    if do_epub:
        cmd.append("--epub")
    cmd.append(src_in_site.name)

    proc = subprocess.run(
        cmd,
        cwd=src_in_site.parent,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    out = proc.stdout or ""
    if out:
        print(out, end="" if out.endswith("\n") else "\n")
    if proc.returncode != 0:
        print(f"[DEBUG] WARNING: md render failed (rc={proc.returncode}) for {rel_path}; continuing")

def _render_single_book(
    book_dir: Path,
    meta_name: str,
    render_py: Path,
    *,
    include_epub: bool = True,
    include_pdf: bool = True,
    include_html: bool = True,
) -> tuple[Path, int, str]:
    """
    Render a single book directory with render.py.

    include_pdf/include_html/include_epub request those formats. include_html=False
    will skip both PDF/HTML renders and just run preprocessing to emit concatenated
    .md/.pandoc.md files. By default we ask for PDF+HTML+EPUB; on PDF failure we
    retry HTML-only so concatenated outputs still exist.
    """
    cmd = [sys.executable, str(render_py)]

    if include_pdf and include_html:
        cmd.append("--all")  # PDF+HTML
    elif include_pdf:
        cmd.append("--pdf")
    elif include_html:
        cmd.append("--html")

    if include_epub and (include_html or include_pdf):
        cmd.append("--epub")

    cmd.extend(
        [
            "--omit-numbering",
            "--toc-depth",
            "1",
            meta_name,
        ]
    )

    proc = subprocess.run(
        cmd,
        cwd=book_dir,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    out = proc.stdout or ""

    # If PDF+HTML failed (likely due to PDF), retry HTML-only (no EPUB) so the
    # build keeps going and concatenated outputs exist.
    if include_pdf and proc.returncode != 0:
        out += (
            ("\n" if out and not out.endswith("\n") else "")
            + "[DEBUG] PDF+HTML render failed; retrying HTML-only without EPUB\n"
        )
        fallback_cmd = [sys.executable, str(render_py)]
        if include_html:
            fallback_cmd.append("--html")
        fallback_cmd.extend(
            [
                "--omit-numbering",
                "--toc-depth",
                "1",
                meta_name,
            ]
        )
        proc2 = subprocess.run(
            fallback_cmd,
            cwd=book_dir,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        out += proc2.stdout or ""
        return book_dir, proc2.returncode, out

    return book_dir, proc.returncode, out

def render_book_dirs(
    skip_epub: bool = False,
    include_pdf: bool = True,
    include_html: bool = True,
    max_workers: int | None = None,
    base_dir: Path | None = None,
):
    """
    Find directories that declare a book.yml/book.yaml and render them before
    mirroring the tree into site(). By default renders PDF+HTML+EPUB.

    skip_epub=True renders without EPUB. include_pdf=True attempts PDF+HTML
    (still skipping EPUB if skip_epub is set), and on failure falls back to
    HTML-only so the build can continue. include_html=False will only run the
    preprocessing step to emit concatenated .md/.pandoc.md files. max_workers
    limits parallelism; default uses min(4, number of books).
    """
    base = base_dir or ROOT
    skip_gitignore = base == OUT
    include_epub = not skip_epub
    import yaml as _yaml

    render_py = ROOT / ".scripts" / "render" / "render.py"
    if not render_py.exists():
        print(f"[DEBUG] render.py not found at {render_py}; skipping book renders")
        return

    seen: set[Path] = set()
    candidates: list[Path] = []
    for ext in ("book.yml", "book.yaml"):
        candidates.extend(base.rglob(ext))

    for meta in candidates:
        try:
            meta_rel = meta.relative_to(base)
        except Exception:
            continue

        # Skip gitignored, OUT/, excluded, or hidden paths
        if not skip_gitignore and is_gitignored(meta):
            continue
        parts = meta_rel.parts
        if not parts:
            continue
        if parts[0] in EXCLUDE_NAMES:
            continue
        if any(p.startswith(".") and p != ".well-known" for p in parts):
            continue

        book_dir = meta.parent
        if book_dir in seen:
            continue
        seen.add(book_dir)

        try:
            rel_root = rel(book_dir)
        except Exception:
            rel_root = book_dir
        print(f"[DEBUG] Queued book render: {rel_root} ({meta.name})")

    book_dirs = list(seen)
    if not book_dirs:
        return

    workers = max_workers or min(4, len(book_dirs))
    if not include_html and not include_pdf and not include_epub:
        mode = "preprocess only (no HTML/PDF/EPUB)"
    elif include_pdf and include_epub:
        mode = "HTML+PDF+EPUB"
    elif include_pdf:
        mode = "HTML+PDF (no EPUB)"
    elif include_epub:
        mode = "HTML+EPUB"
    else:
        mode = "HTML only"
    print(
        f"[DEBUG] Rendering {len(book_dirs)} book(s) ({mode}) with {workers} worker(s) "
        f"from base={base}"
    )

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futures = []
        for book_dir in book_dirs:
            meta_name = None
            for ext in ("book.yml", "book.yaml"):
                if (book_dir / ext).exists():
                    meta_name = ext
                    break
            if not meta_name:
                continue
            futures.append(
                ex.submit(
                    _render_single_book,
                    book_dir,
                    meta_name,
                    render_py,
                    include_epub=include_epub,
                    include_pdf=include_pdf,
                    include_html=include_html,
                )
            )

        for fut in concurrent.futures.as_completed(futures):
            book_dir, rc, out = fut.result()
            if out:
                print(out, end="" if out.endswith("\n") else "\n")
            if rc != 0:
                print(
                    f"[DEBUG] WARNING: book render failed (rc={rc}) "
                    f"for {rel(book_dir)}; continuing build"
                )
            # After render, ensure every .md (including combined book .md) has a .md.html wrapper.
            try:
                for md_file in book_dir.glob("*.md"):
                    render_markdown_file(md_file, md_file.with_suffix(md_file.suffix + ".html"), title=md_file.stem)
            except Exception:
                pass

def build_simple_page_from_md(src_name: str, slug: str, title: str):
    src_md = ROOT / src_name
    if not src_md.exists():
        return
    dst_html = OUT / slug / "index.html"
    render_markdown_file(src_md, dst_html, title)

def write_md_like_page(out_html: Path, md_body: str, title: str | None = None):
    body = md_body.replace("&", "&amp;").replace("<", "&lt;")

    rel_html = rel_out(out_html).as_posix()
    origin = _current_origin()
    page_url = f"{origin}/{rel_html}"

    t = title or ""
    head = [
        '<meta charset="utf-8">',
        f'<link rel="canonical" href="{page_url}">',
        '<meta name="robots" content="index,follow">',
        f'<meta name="description" content="{t}">',
    ]
    head_extra = "\n".join(head) + "\n"

    write_html(out_html, body, head_extra=head_extra, title=t or "Index")

def crumb_link(parts: list[str]) -> str:
    html = ['<nav class="breadcrumbs">']
    html.append('<a href="/">🏠 Home</a>')
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
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", x):
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

def fmt_author(a):
    nm = a.get("name", "").strip()
    oc = _orcid_url(a.get("orcid", "").strip())
    if not nm:
        return ""
    if oc:
        return f'{nm} (<a href="{oc}">ORCID</a>)'
    return nm

# ---------- article pages ----------
def build_article_pages():
    origin = _current_origin()

    records = []
    for prov in iter_provenance_files():
        try:
            data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
        except Exception:
            continue

        rel_parts = rel(prov).parts
        if len(rel_parts) < 4:
            continue

        top = rel_parts[0]
        stem = rel_parts[1]
        doi_prefix = rel_parts[2]
        doi_suffix = rel_parts[3]

        journal = (data.get("journal") or "").strip()

        pf_block = data.get("parsed_from_pnpmd") or {}

        title    = (data.get("title") or pf_block.get("title") or "") or ""
        abstract = (data.get("abstract") or pf_block.get("abstract") or "") or ""
        kws      = (data.get("keywords") or pf_block.get("keywords") or []) or []
        onesent  = (
            data.get("one_sentence_summary")
            or pf_block.get("one_sentence_summary")
            or pf_block.get("one_sentence")
            or ""
        )
        onesent = (onesent or "").strip()

        authors  = normalize_authors(data.get("authors") or pf_block.get("authors"))

        date_norm = (
            data.get("publication_date")
            or data.get("creation_date")
            or pf_block.get("date")
            or ""
        )

        zenodo = data.get("zenodo") or {}
        doi     = (data.get("doi") or zenodo.get("doi") or "") or ""
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

        md_name   = (artifacts.get("md") or artifacts.get("main") or None)
        html_name = (artifacts.get("html_name") or None)
        pmd_name  = (artifacts.get("pandoc_md_name") or artifacts.get("pandoc_md") or None)
        pdf_name  = (artifacts.get("pdf_name") or artifacts.get("pdf") or None)
        epub_name = (artifacts.get("epub_name") or artifacts.get("epub") or None)
        add_old   = artifacts.get("additional") or {}
        if not html_name:
            html_name = add_old.get("html")
        if not pmd_name:
            pmd_name  = add_old.get("pandoc_md")
        if not pdf_name:
            pdf_name = add_old.get("pdf")
        if not epub_name:
            epub_name = add_old.get("epub")

        if not md_name and artifacts.get("md_url"):
            md_name = Path(artifacts["md_url"]).name
        if not html_name and artifacts.get("html_url"):
            html_name = Path(artifacts["html_url"]).name
        if not pmd_name and artifacts.get("pandoc_md_url"):
            pmd_name = Path(artifacts["pandoc_md_url"]).name
        if not pdf_name and artifacts.get("pdf_url"):
            pdf_name = Path(artifacts["pdf_url"]).name
        if not epub_name and artifacts.get("epub_url"):
            epub_name = Path(artifacts["epub_url"]).name

        assets_pdf = (
            artifacts.get("pdf_url")
            or _asset_url(assets.get("pdf"))
            or _asset_url(canonical_assets.get("pdf"))
            or ""
        )
        assets_epub = (
            artifacts.get("epub_url")
            or _asset_url(assets.get("epub"))
            or _asset_url(canonical_assets.get("epub"))
            or ""
        )

        references_doi = data.get("references_doi") or pf_block.get("references_doi") or []
        if not isinstance(references_doi, list):
            references_doi = [references_doi]

        records.append({
            "prov": prov, "top": top, "stem": stem,
            "doi_prefix": doi_prefix, "doi_suffix": doi_suffix,
            "title": title, "authors": authors,
            "abstract": abstract, "onesent": onesent,
            "kws": kws,
            "date": date_norm, "doi": doi, "concept": concept,
            "assets_pdf": assets_pdf,
            "assets_epub": assets_epub,
            "md_name": md_name, "html_name": html_name, "pmd_name": pmd_name,
            "pdf_name": pdf_name, "epub_name": epub_name,
            "html_canonical": html_canonical,
            "references_doi": references_doi,
            "journal": journal,
        })

        json.dumps(records, indent=2, default=str)

    if not records:
        return

    # group by (top-level folder, stem)
    groups: dict[tuple[str, str], list[dict]] = {}
    for r in records:
        key = (r["top"], r["stem"])
        groups.setdefault(key, []).append(r)

    for (top, stem), items in groups.items():
        def sort_key(it):
            dt = _to_datetime(it["date"])
            return dt or datetime.fromtimestamp(it["prov"].stat().st_mtime)

        versions = sorted(items, key=sort_key, reverse=True)
        latest = versions[0]

        # --- each VERSION page ---
        for it in versions:
            src = it["prov"].parent
            out_dir = OUT / top / stem / it["doi_prefix"] / it["doi_suffix"]
            out_dir.mkdir(parents=True, exist_ok=True)

            for f in src.iterdir():
                if not f.is_file():
                    continue
                # Mirror assets and all rendered outputs; also mirror the parent stem dir (for DOI alias).
                if f.suffix.lower() in MIRROR_EXTS or f.name.endswith(".md.html"):
                    dst = OUT / rel(f)
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, dst)

            local_md   = f"/{(OUT/rel(src/it['md_name'])).relative_to(OUT).as_posix()}" if it["md_name"] else None
            local_html = f"/{(OUT/rel(src/it['html_name'])).relative_to(OUT).as_posix()}" if it["html_name"] else None
            local_pmd  = f"/{(OUT/rel(src/it['pmd_name'])).relative_to(OUT).as_posix()}" if it["pmd_name"] else None
            local_pdf  = _local_artifact_url(src, it.get("pdf_name"))
            local_epub = _local_artifact_url(src, it.get("epub_name"))
            pdf_link = it.get("assets_pdf") or local_pdf or ""
            epub_link = it.get("assets_epub") or local_epub or ""

            html_body = ""
            if it["html_name"] and (src/it["html_name"]).exists():
                try:
                    htxt = (src/it["html_name"]).read_text(encoding="utf-8")
                    html_body = extract_html_body(htxt)
                except Exception:
                    html_body = ""

            top_links = []
            if local_md:
                top_links.append(f'<a href="{local_md}">Markdown</a>')
            if pdf_link:
                top_links.append(f'<a href="{pdf_link}">PDF</a>')
            if epub_link:
                top_links.append(f'<a href="{epub_link}">EPUB</a>')
            if local_pmd:
                top_links.append(f'<a href="{local_pmd}">Preprocessed MD</a>')

            share_html = ""
            doi_clean = (it["doi"] or "").replace(" ", "")
            doi_fallback = ""
            if it["doi_prefix"] and it["doi_suffix"]:
                doi_fallback = f"{it['doi_prefix']}/{it['doi_suffix']}"
            if doi_clean or doi_fallback:
                doi_value = doi_clean or doi_fallback
                doi_url = f"https://doi.org/{doi_value}"
                origin = _current_origin()
                doi_alias = f"{origin}/{top}/doi/{it['doi_prefix']}/{it['doi_suffix']}"
                share_html = (
                    "<div class=\"share\"><strong>Share as:</strong><br>"
                    f'<a href="{doi_alias}">{doi_alias}</a><br>'
                    f'<a href="{doi_url}">{doi_url}</a>'
                    "</div>"
                )

            breadcrumbs = crumb_link([top, stem, it["doi_prefix"], it["doi_suffix"]])
            files_list = []
            prov_local = f"/{(OUT/rel(it['prov'])).relative_to(OUT).as_posix()}"
            if local_html:
                files_list.append(f'<li><a href="{local_html}">{it["html_name"]}</a></li>')
            if local_md:
                files_list.append(f'<li><a href="{local_md}">{it["md_name"]}</a></li>')
            files_list.append(f'<li><a href="{prov_local}">provenance.yaml</a></li>')
            if pdf_link:
                files_list.append(f'<li><a href="{pdf_link}">PDF</a></li>')
            if epub_link:
                files_list.append(f'<li><a href="{epub_link}">EPUB</a></li>')
            files_ul = "<ul>" + "".join(files_list) + "</ul>"

            display_authors = it["authors"]
            authors_html = ", ".join(filter(None, (fmt_author(a) for a in display_authors)))

            body = []
            body.append(breadcrumbs)
            body.append("<main class='paper'>")
            body.append(f"<h1>{it['title']}</h1>")
            if authors_html:
                body.append(f"<p class='authors'>{authors_html}</p>")
            body.append(f"<p class='publine'>{PREFERRED_JOURNAL} — {month_year(it['date'])}</p>")
            body.append("<p class='links'>" + " · ".join(top_links) + "</p>")
            if share_html:
                body.append(share_html)

            if it["onesent"]:
                body.append("<h2>One-Sentence Summary</h2>")
                body.append(f"<p>{it['onesent']}</p>")

            if it["abstract"]:
                body.append("<h2>Abstract</h2>")
                body.append(f"<p>{it['abstract']}</p>")

            body.append("<h2>Files</h2>")
            body.append(files_ul)

            if html_body:
                body.append("<h2>Article</h2>")
                body.append(html_body)

            if it["references_doi"]:
                body.append("<h2>References (DOI)</h2>")
                refs_items = []
                for ref_url in it["references_doi"]:
                    ref_url = (ref_url or "").strip()
                    if not ref_url:
                        continue
                    refs_items.append(f'<li><a href="{ref_url}">{ref_url}</a></li>')
                if refs_items:
                    body.append("<ul>" + "".join(refs_items) + "</ul>")

            body.append("</main>")

            stem_seg = quote(stem, safe="")
            version_url = f"{origin}/{top}/{stem_seg}/{it['doi_prefix']}/{it['doi_suffix']}/"

            head = []
            head.append('<meta charset="utf-8">')
            head.append(f'<link rel="canonical" href="{version_url}">')
            if pdf_link:
                head.append(f'<link rel="alternate" type="application/pdf" href="{pdf_link}">')
            if epub_link:
                head.append(f'<link rel="alternate" type="application/epub+zip" href="{epub_link}">')
            head.append('<meta name="robots" content="index,follow">')
            if it["title"]:
                head.append(f'<meta name="citation_title" content="{it["title"]}">')
            for a in display_authors:
                nm = a.get("name", "")
                if nm:
                    head.append(f'<meta name="citation_author" content="{nm}">')
            if it["date"]:
                head.append(f'<meta name="citation_publication_date" content="{scholar_date(it["date"])}">')
            head.append(f'<meta name="citation_journal_title" content="{PREFERRED_JOURNAL}">')
            if pdf_link:
                head.append(f'<meta name="citation_pdf_url" content="{pdf_link}">')
            if it["doi"]:
                head.append(f'<meta name="citation_doi" content="{it["doi"]}">')
            desc = it["abstract"] or it["onesent"] or it["title"]
            if desc:
                head.append(f'<meta name="description" content="{desc}">')
                head.append(f'<meta property="og:description" content="{desc}">')
            head.append('<meta property="og:type" content="article">')
            head.append(f'<meta property="og:title" content="{it["title"]}">')
            head.append(f'<meta property="og:url" content="{version_url}">')

            authors_ld = []
            for a in display_authors:
                nm = a.get("name", "").strip()
                oc = _orcid_url(a.get("orcid", "").strip())
                if not nm:
                    continue
                ent = {"@type": "Person", "name": nm}
                if oc:
                    ent["sameAs"] = [oc]
                authors_ld.append(ent)
            enc = []
            if pdf_link:
                enc.append({
                    "@type": "MediaObject",
                    "contentUrl": pdf_link,
                    "encodingFormat": "application/pdf",
                })
            if epub_link:
                enc.append({
                    "@type": "MediaObject",
                    "contentUrl": epub_link,
                    "encodingFormat": "application/epub+zip",
                })
            article_ld = {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": it["title"],
                "author": authors_ld or [{"@type": "Person", "name": "Unknown"}],
                "datePublished": iso_date_str(it["date"]),
                "isPartOf": {"@type": "Periodical", "name": PREFERRED_JOURNAL},
                "url": version_url,
            }
            if enc:
                article_ld["encoding"] = enc
            if it["doi"]:
                article_ld["sameAs"] = [f"https://doi.org/{it['doi'].split('/')[-1]}"]
            head.append(
                '<script type="application/ld+json">'
                + json.dumps(article_ld, ensure_ascii=False)
                + "</script>"
            )
            head_extra = "\n".join(head) + "\n"
            body_html = "\n".join(body)

            write_html(out_dir/"index.html", body_html, head_extra=head_extra, title=it["title"])

            # DOI aliases live under the same top-level (prints/doi or documents/doi)
            alias_dir = OUT / top / "doi" / it["doi_prefix"] / it["doi_suffix"]
            alias_dir.mkdir(parents=True, exist_ok=True)
            write_html(alias_dir/"index.html", body_html, head_extra=head_extra, title=it["title"])

            mirror_dir = OUT / rel(src)
            mirror_dir.mkdir(parents=True, exist_ok=True)
            write_html(mirror_dir/"index.html", body_html, head_extra=head_extra, title=it["title"])

        # --- STEM page (latest) ---
        it = latest
        src = it["prov"].parent
        stem_out = OUT / top / stem
        stem_out.mkdir(parents=True, exist_ok=True)

        for f in src.iterdir():
            if f.is_file() and f.suffix.lower() in MIRROR_EXTS:
                dst = OUT / rel(f)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dst)

        local_md   = f"/{(OUT/rel(src/it['md_name'])).relative_to(OUT).as_posix()}" if it["md_name"] else None
        local_html = f"/{(OUT/rel(src/it['html_name'])).relative_to(OUT).as_posix()}" if it["html_name"] else None
        local_pmd  = f"/{(OUT/rel(src/it['pmd_name'])).relative_to(OUT).as_posix()}" if it["pmd_name"] else None
        local_pdf  = _local_artifact_url(src, it.get("pdf_name"))
        local_epub = _local_artifact_url(src, it.get("epub_name"))
        pdf_link = it.get("assets_pdf") or local_pdf or ""
        epub_link = it.get("assets_epub") or local_epub or ""

        html_body = ""
        if it["html_name"] and (src/it["html_name"]).exists():
            try:
                htxt = (src/it["html_name"]).read_text(encoding="utf-8")
                html_body = extract_html_body(htxt)
            except Exception:
                html_body = ""

        breadcrumbs = crumb_link([top, stem])

        # Only treat records with the SAME concept DOI as versions
        same_family = []
        for v in versions:
            if it["concept"] and v["concept"] == it["concept"]:
                same_family.append(v)
            elif not it["concept"] and not v["concept"]:
                same_family.append(v)

        versions_list = []
        for v in same_family:
            ver_url  = f"/{top}/{stem}/{v['doi_prefix']}/{v['doi_suffix']}/"
            doi_disp = f"{v['doi_prefix']}/{v['doi_suffix']}"
            date_disp = v["date"] or ""
            versions_list.append(f"<li>{date_disp} — <a href='{ver_url}'>{doi_disp}</a></li>")
        versions_ul = "<ul>" + "".join(versions_list) + "</ul>" if versions_list else ""

        files_list = []
        prov_local = f"/{(OUT/rel(it['prov'])).relative_to(OUT).as_posix()}"
        if local_html:
            files_list.append(f'<li><a href="{local_html}">{it["html_name"]}</a></li>')
        if local_md:
            files_list.append(f'<li><a href="{local_md}">{it["md_name"]}</a></li>')
        files_list.append(f'<li><a href="{prov_local}">provenance.yaml</a></li>')
        if pdf_link:
            files_list.append(f'<li><a href="{pdf_link}">PDF</a></li>')
        if epub_link:
            files_list.append(f'<li><a href="{epub_link}">EPUB</a></li>')
        files_ul = "<ul>" + "".join(files_list) + "</ul>"

        top_links = []
        if local_md:
            top_links.append(f'<a href="{local_md}">Markdown (latest)</a>')
        if pdf_link:
            top_links.append(f'<a href="{pdf_link}">PDF (latest)</a>')
        if epub_link:
            top_links.append(f'<a href="{epub_link}">EPUB (latest)</a>')
        if local_pmd:
            top_links.append(f'<a href="{local_pmd}">Preprocessed MD</a>')

        share_html = ""
        doi_clean = (it["doi"] or "").replace(" ", "")
        doi_fallback = ""
        if it["doi_prefix"] and it["doi_suffix"]:
            doi_fallback = f"{it['doi_prefix']}/{it['doi_suffix']}"
        if doi_clean or doi_fallback:
            doi_value = doi_clean or doi_fallback
            doi_url = f"https://doi.org/{doi_value}"
            origin = _current_origin()
            doi_alias = f"{origin}/{top}/doi/{it['doi_prefix']}/{it['doi_suffix']}"
            share_html = (
                "<div class=\"share\"><strong>Share as:</strong><br>"
                f'<a href="{doi_alias}">{doi_alias}</a><br>'
                f'<a href="{doi_url}">{doi_url}</a>'
                "</div>"
            )

        display_authors = it["authors"]
        authors_html = ", ".join(filter(None, (fmt_author(a) for a in display_authors)))

        body = []
        body.append(breadcrumbs)
        body.append("<main class='paper'>")
        body.append(f"<h1>{it['title']}</h1>")
        if authors_html:
            body.append(f"<p class='authors'>{authors_html}</p>")
        body.append(f"<p class='publine'>{PREFERRED_JOURNAL} — {month_year(it['date'])}</p>")
        body.append("<p class='links'>" + " · ".join(top_links) + "</p>")
        if share_html:
            body.append(share_html)
        if versions_ul:
            body.append("<h2>Versions</h2>")
            body.append(versions_ul)
        body.append("<h2>Files (latest)</h2>")
        body.append(files_ul)

        if it["onesent"]:
            body.append("<h2>One-Sentence Summary</h2>")
            body.append(f"<p>{it['onesent']}</p>")

        if it["abstract"]:
            body.append("<h2>Abstract</h2>")
            body.append(f"<p>{it['abstract']}</p>")

        if html_body:
            body.append("<h2>Article (latest)</h2>")
            body.append(html_body)

        if it["references_doi"]:
            body.append("<h2>References (DOI)</h2>")
            refs_items = []
            for ref_url in it["references_doi"]:
                ref_url = (ref_url or "").strip()
                if not ref_url:
                    continue
                refs_items.append(f'<li><a href="{ref_url}">{ref_url}</a></li>')
            if refs_items:
                body.append("<ul>" + "".join(refs_items) + "</ul>")
        body.append("</main>")

        stem_seg = quote(stem, safe="")
        stem_url = f"{origin}/{top}/{stem_seg}/"
        head = []
        head.append('<meta charset="utf-8">')
        head.append(f'<link rel="canonical" href="{stem_url}">')
        if pdf_link:
            head.append(f'<link rel="alternate" type="application/pdf" href="{pdf_link}">')
        if epub_link:
            head.append(f'<link rel="alternate" type="application/epub+zip" href="{epub_link}">')
        head.append('<meta name="robots" content="index,follow">')
        if it["title"]:
            head.append(f'<meta name="citation_title" content="{it["title"]}">')
        for a in display_authors:
            nm = a.get("name", "")
            if nm:
                head.append(f'<meta name="citation_author" content="{nm}">')
        if it["date"]:
            head.append(f'<meta name="citation_publication_date" content="{scholar_date(it["date"])}">')
        head.append(f'<meta name="citation_journal_title" content="{PREFERRED_JOURNAL}">')
        if pdf_link:
            head.append(f'<meta name="citation_pdf_url" content="{pdf_link}">')
        if it["doi"]:
            head.append(f'<meta name="citation_doi" content="{it["doi"]}">')
        desc = it["abstract"] or it["onesent"] or it["title"]
        if desc:
            head.append(f'<meta name="description" content="{desc}">')
            head.append(f'<meta property="og:description" content="{desc}">')
        head.append('<meta property="og:type" content="article">')
        head.append(f'<meta property="og:title" content="{it["title"]}">')
        head.append(f'<meta property="og:url" content="{stem_url}">')

        authors_ld = []
        for a in display_authors:
            nm = a.get("name", "").strip()
            oc = _orcid_url(a.get("orcid", "").strip())
            if not nm:
                continue
            ent = {"@type": "Person", "name": nm}
            if oc:
                ent["sameAs"] = [oc]
            authors_ld.append(ent)
        enc = []
        if pdf_link:
            enc.append({
                "@type": "MediaObject",
                "contentUrl": pdf_link,
                "encodingFormat": "application/pdf",
            })
        if epub_link:
            enc.append({
                "@type": "MediaObject",
                "contentUrl": epub_link,
                "encodingFormat": "application/epub+zip",
            })
        article_ld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": it["title"],
            "author": authors_ld or [{"@type": "Person", "name": "Unknown"}],
            "datePublished": iso_date_str(it["date"]),
            "isPartOf": {"@type": "Periodical", "name": PREFERRED_JOURNAL},
            "url": stem_url,
        }
        if enc:
            article_ld["encoding"] = enc
        if it["doi"]:
            article_ld["sameAs"] = [f"https://doi.org/{it['doi'].split('/')[-1]}"]
        head.append(
            '<script type="application/ld+json">'
            + json.dumps(article_ld, ensure_ascii=False)
            + "</script>"
        )
        head_extra = "\n".join(head) + "\n"

        write_html(stem_out/"index.html", "\n".join(body), head_extra=head_extra, title=it["title"])

# ---------- dir index ----------
def breadcrumbs(rel_dir: Path) -> str:
    depth = len(rel_dir.parts)
    to_root = "./" if depth == 0 else "../"*depth
    items = [f"[/   ]({to_root})"]
    for i, part in enumerate(rel_dir.parts):
        up = "../"*(len(rel_dir.parts)-i-1) or "./"
        items.append(f"[📂 {part} /]({up})")
    return " ".join(items)

def _format_dir_index_common(rel_dir: Path, items: list[Item], *, use_root_links: bool) -> tuple[str, str]:
    """
    Shared index formatter.

    use_root_links=False => paths are relative to OUT (mirrored tree).
    """
    title = (rel_dir.name or f"{REPO} index")

    lines = []
    lines.append(breadcrumbs(rel_dir))
    lines.append("")

    items_sorted = sorted(items, key=lambda e: (not e.is_dir, e.name.lower()))
    for it in items_sorted:
        if it.is_dir:
            href_rel = rel(it.path) if use_root_links else rel_out(it.path)
            href = (it.name + "/") if rel_dir.parts else (href_rel.as_posix() + "/")
            href = quote(href, safe="/:@-._~")
            lines.append(f"- 📂 [{it.name}]({href})")
        else:
            p_rel = rel(it.path) if use_root_links else rel_out(it.path)
            ext = it.path.suffix.lower()

            if ext in MD_EXTS:
                # rendered file lives at: OUT / <p_rel>.html
                rendered = (OUT / p_rel).with_suffix(p_rel.suffix + ".html")
                mirrored = OUT / p_rel
                rel_url = rel_out(mirrored).as_posix()
                url_local_raw = "/" + quote(rel_url, safe="/:@-._~")
                # assume it exists; if it doesn't, that's a build bug
                rel_rendered = rel_out(rendered).as_posix()
                url_local = "/" + quote(rel_rendered, safe="/:@-._~")

                gh_path = quote(p_rel.as_posix(), safe="/:@-._~")
                gh_url = None
                if use_root_links and (ROOT / p_rel).exists():
                    gh_url = (
                        f"https://github.com/{OWNER}/{REPO}/blob/"
                        f"{BRANCH}/{gh_path}"
                    )

                gh_block = f" [[GH]({gh_url})]" if gh_url else ""
                lines.append(f"- 📄 [{it.name}]({url_local}) ([[Raw]({url_local_raw})]{gh_block})")
            else:
                mirrored = OUT / p_rel
                if mirrored.exists():
                    rel_url = rel_out(mirrored).as_posix()
                    url_local = "/" + quote(rel_url, safe="/:@-._~")
                    lines.append(f"- 📄 [{it.name}]({url_local})")
                else:
                    # file exists in repo but wasn't mirrored (should not happen)
                    lines.append(f"- 📄 {it.name}")

    lines.append("")
    return title, "\n".join(lines)

def format_dir_index(dir_abs: Path, items: list[Item]) -> tuple[str, str]:
    rel_dir = rel(dir_abs) if dir_abs != ROOT else Path()
    return _format_dir_index_common(rel_dir, items, use_root_links=True)

def format_dir_index_out(dir_abs: Path, items: list[Item]) -> tuple[str, str]:
    rel_dir = rel_out(dir_abs) if dir_abs != OUT else Path()
    return _format_dir_index_common(rel_dir, items, use_root_links=False)

def _book_artifact_hide_names(dir_abs: Path) -> set[str]:
    if not ((dir_abs / "book.yml").exists() or (dir_abs / "book.yaml").exists()):
        return set()
    hidden = {"book-style.css"}
    suffix = ".pandoc.md"
    for p in dir_abs.glob(f"*{suffix}"):
        base = p.name[:-len(suffix)]
        hidden.add(p.name)
        hidden.add(f"{base}.pandoc.md.html")
    return hidden

def build_out_indexes(hidden_stems: set[tuple[str, str]]):
    for dirpath, dirnames, filenames in os.walk(OUT):
        d = Path(dirpath)
        rel_parts = rel_out(d).parts if d != OUT else ()
        in_hidden = (
            len(rel_parts) >= 2 and (rel_parts[0], rel_parts[1]) in hidden_stems
        )
        hide_names = _book_artifact_hide_names(d)
        # prune hidden dirs
        keep = []
        for dd in list(dirnames):
            if dd.startswith(".") and dd != ".well-known":
                continue
            child = d / dd
            child_rel_parts = rel_out(child).parts
            if len(child_rel_parts) >= 2 and (child_rel_parts[0], child_rel_parts[1]) in hidden_stems:
                continue
            if (child/"pyvenv.cfg").exists():
                continue
            keep.append(dd)
        dirnames[:] = keep

        items: list[Item] = []
        for sub in sorted([d/nn for nn in dirnames], key=lambda x: x.name.lower()):
            items.append(Item(name=sub.name, is_dir=True, mtime=sub.stat().st_mtime, path=sub))
        for fname in sorted(filenames, key=lambda x: x.lower()):
            if fname.startswith("."):
                continue
            p = d / fname
            if p.name in EXCLUDE_NAMES:
                continue
            lower_name = p.name.lower()
            if lower_name.endswith(".md.html") or lower_name.endswith(".markdown.html"):
                continue
            if p.name in hide_names:
                continue
            items.append(Item(name=p.name, is_dir=False, mtime=p.stat().st_mtime, path=p))

        out_html = d / "index.html"
        if in_hidden:
            continue
        title, md_body = format_dir_index_out(d, items)
        write_md_like_page(out_html, md_body, title=title)

def copy_static():
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
    suf = p.suffix.lower()

    if suf == ".html":
        if rp == "index.html":
            path = "/"
        elif rp.endswith("/index.html"):
            path = "/" + rp[:-10]
        else:
            path = "/" + rp
    elif suf == ".md":
        path = "/" + rp
    else:
        return ""

    return quote(path, safe="/:@-._~")

def build_sitemap_and_robots():
    origin = _current_origin()

    urls = []
    for path in OUT.rglob("*"):
        if path.name.startswith("."):
            continue
        if path.suffix.lower() not in {".html", ".md"}:
            continue

        rel_url = _url_from_out_path(path)
        if not rel_url:
            continue

        loc = origin + rel_url
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        lastmod = mtime.strftime("%Y-%m-%dT%H:%M:%SZ")
        urls.append((loc, lastmod))

    seen = {}
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
        + "\n".join(items) + "\n</urlset>\n"
    )
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    robots = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {origin}/sitemap.xml\n"
    )
    (OUT / "robots.txt").write_text(robots, encoding="utf-8")

# ---------- RSS ----------
def build_rss_feed():
    origin = _current_origin()

    by_stem = {}
    for prov in iter_provenance_files():
        try:
            data = yaml.safe_load(prov.read_text(encoding="utf-8")) or {}
        except Exception:
            continue

        journal = (data.get("journal") or "").strip()
        if journal and journal != PREFERRED_JOURNAL:
            continue

        rel_parts = rel(prov).parts
        if len(rel_parts) < 2:
            continue
        top  = rel_parts[0]
        stem = rel_parts[1]

        pf_block = data.get("parsed_from_pnpmd") or {}
        title    = (data.get("title") or pf_block.get("title") or stem)
        authors  = normalize_authors(data.get("authors") or pf_block.get("authors"))
        abstract = (data.get("abstract") or pf_block.get("abstract") or "")
        onesent  = (
            data.get("one_sentence_summary")
            or pf_block.get("one_sentence_summary")
            or pf_block.get("one_sentence")
            or ""
        )
        date_norm= (data.get("publication_date") or data.get("creation_date") or pf_block.get("date") or None)
        doi      = (data.get("doi") or (data.get("zenodo") or {}).get("doi") or "")

        permalink = (data.get("permalink") or "").strip()
        if permalink and permalink.startswith("http"):
            item_url = permalink.rstrip("/")
        else:
            item_url = f"{origin}/{quote(top, safe='')}/{quote(stem, safe='')}/"

        dt = _to_datetime(date_norm) or datetime.fromtimestamp(prov.stat().st_mtime)
        keep = by_stem.get((top, stem))
        if not keep or dt > keep["date"]:
            by_stem[(top, stem)] = {
                "stem": stem,
                "top": top,
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "onesent": onesent,
                "date": dt,
                "url": item_url,
                "doi": doi,
            }

    if not by_stem:
        return

    fg = FeedGenerator()
    fg.load_extension("podcast")
    fg.title(f"{PREFERRED_JOURNAL} — Publications")
    fg.link(href=origin + "/", rel="alternate")
    fg.link(href=origin + "/rss.xml", rel="self")
    fg.description(f"Latest publications from {PREFERRED_JOURNAL}")
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
            fe.link(href=f'https://doi.org/{it["doi"].split("/")[-1]}', rel="related")

    rss_xml = fg.rss_str(pretty=True).decode("utf-8")
    (OUT / "rss.xml").write_text(rss_xml, encoding="utf-8")

# ---------- build ----------
def main():
    import argparse

    ap = argparse.ArgumentParser(description="Build static site")
    ap.add_argument(
        "--skip-books",
        action="store_true",
        help="Only concatenate book.yml/book.yaml (no PDF/EPUB/HTML renders).",
    )
    ap.add_argument(
        "--skip-pdf",
        action="store_true",
        help="Skip generating PDFs (books and individual Markdown files).",
    )
    ap.add_argument(
        "--skip-epub",
        action="store_true",
        help="Skip generating EPUBs (books and individual Markdown files).",
    )
    ap.add_argument(
        "--book-workers",
        type=int,
        default=None,
        help="Max parallel workers for book renders (default: min(4, #books)).",
    )
    args = ap.parse_args()

    global PREFERRED_JOURNAL
    PREFERRED_JOURNAL = _compute_preferred_journal()

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/".nojekyll").write_text("", encoding="utf-8")
    write_cname_if_custom(BASE_URL)

    print(f"[DEBUG] ROOT: {ROOT}")
    print(f"[DEBUG] OUT:  {OUT}")
    print(f"[DEBUG] SRC:  {SRC}")
    print(f"[DEBUG] BASE_URL: {BASE_URL}")
    print(f"[DEBUG] gitignored paths: {len(GITIGNORED_PATHS)}")

    site_src = SRC / "site"
    print(f"[DEBUG] site_src: {site_src} (exists={site_src.exists()})")

    if site_src.exists():
        for src_path in site_src.rglob("*"):
            if not src_path.is_file():
                continue
            rel_path = src_path.relative_to(site_src)
            print(f"[DEBUG] site asset found: {rel_path}")
            if src_path.suffix.lower() == ".md":
                dst_md = OUT / rel_path
                dst_md.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dst_md)
                dst_rel = rel_path.with_suffix(rel_path.suffix + ".html")
                dst_path = OUT / dst_rel
                print(f"[DEBUG]   MD (site) -> {dst_rel}")
                render_markdown_file(dst_md, dst_path, title=rel_path.stem)
            else:
                dst_path = OUT / rel_path
                print(f"[DEBUG]   COPY -> {rel_path} → {dst_path.relative_to(OUT)}")
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dst_path)
    else:
        print("[DEBUG] WARNING: site_src does not exist; no site/ assets copied")

    build_article_pages()

    hidden_stems = hidden_stems_from_provenance()

    for dirpath, dirnames, filenames in os.walk(ROOT):
        d = Path(dirpath)

        if is_gitignored(d):
            dirnames.clear()
            continue

        if d == OUT:
            dirnames.clear()
            continue

        if dirpath != str(ROOT):
            first = Path(dirpath).relative_to(ROOT).parts[0]
            if first in EXCLUDE_NAMES:
                dirnames.clear()
                continue
            if (Path(dirpath)/"pyvenv.cfg").exists():
                dirnames.clear()
                continue

        keep=[]
        for dd in list(dirnames):
            child = Path(dirpath) / dd
            if is_gitignored(child):
                continue
            if dd in EXCLUDE_NAMES:
                continue
            if dd.startswith(".") and dd != ".well-known":
                continue
            if (Path(dirpath)/dd/"pyvenv.cfg").exists():
                continue
            keep.append(dd)
        dirnames[:] = keep

        for fname in filenames:
            p = d / fname
            if fname.startswith("."):
                continue
            if is_gitignored(p):
                continue

            if d == ROOT and fname == "index.html":
                continue

            dst = OUT / rel(p)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst)

            if p.suffix.lower() == ".md":
                rendered_dst = dst.with_suffix(dst.suffix + ".html")
                render_markdown_file(p, rendered_dst, title=p.stem)

    copy_static()
    # Render books from the mirrored copies under OUT to avoid touching source.
    book_include_pdf = not (args.skip_pdf or args.skip_books)
    book_include_epub = not (args.skip_epub or args.skip_books)
    book_include_html = not args.skip_books
    render_book_dirs(
        skip_epub=not book_include_epub,
        include_pdf=book_include_pdf,
        include_html=book_include_html,
        max_workers=args.book_workers,
        base_dir=OUT,
    )

    # Build directory indexes based on the final OUT tree (includes rendered books).
    build_out_indexes(hidden_stems)

    build_sitemap_and_robots()
    build_rss_feed()

def _compute_preferred_journal() -> str:
    """
    Determine journal name from canonical origin (host).

    Mapping:
      writing.preferredframe.com   → Preferred Frame Writing
      preprints.preferredframe.com → Preferred Frame Pre-Prints
      preferredframe.com (root)    → Preferred Frame
    """
    from urllib.parse import urlparse

    host = ""
    try:
        # read exactly the same origin logic used everywhere else
        from __main__ import _current_origin  # safe because resolved after import
        origin = _current_origin()
        host = (urlparse(origin).hostname or "").lower()
    except Exception:
        return DEFAULT_JOURNAL

    if host.startswith("writing."):
        return "Preferred Frame Writing"
    if host.startswith("preprints."):
        return "Preferred Frame Pre-Prints"
    return DEFAULT_JOURNAL

if __name__ == "__main__":
    main()
