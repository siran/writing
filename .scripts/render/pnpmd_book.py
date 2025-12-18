# pnpmd_book.py

import re
import html
import shutil
from datetime import date
from pathlib import Path
from typing import Optional

import yaml

from pnpmd_util import title_from_book_yaml, die, run_visible, print_pandoc_log
from pnpmd_preprocess import prepare_preprocessed
from pnpmd_pandoc import render_pdf, render_html, render_epub


_H1_RE = re.compile(r"^\s*#\s+(.*)$")
_NON_ALNUM_RE = re.compile(r"[^0-9A-Za-z _-]+")
_SPACE_RE = re.compile(r"\s+")


def _extract_first_h1(body: str) -> tuple[Optional[str], str]:
    """
    Find the first level-1 heading ('# Title') in the body and return (title, body_without_that_heading).
    If no heading is found, returns (None, original_body).
    """
    lines = body.splitlines()
    title = None
    remove_idx = None
    for i, ln in enumerate(lines):
        m = _H1_RE.match(ln)
        if m:
            title = m.group(1).strip()
            remove_idx = i
            break
    if remove_idx is None:
        return None, body

    # Drop the heading line and a single following blank line (if present) to avoid duplicates.
    new_lines = lines[:remove_idx] + lines[remove_idx + 1 :]
    if remove_idx < len(new_lines) and new_lines[remove_idx].strip() == "":
        new_lines.pop(remove_idx)

    return title, "\n".join(new_lines)


def _slugify(text: str) -> str:
    """
    Generate a simple slug: lowercase, strip accents/punct, collapse spaces to '-'.
    """
    t = _NON_ALNUM_RE.sub("", text)
    t = _SPACE_RE.sub("-", t.strip())
    t = re.sub(r"-{2,}", "-", t).strip("-")
    return t.lower() or "x"


def _split_by_h1(body: str, default_title: str) -> list[tuple[str, str]]:
    """
    Split body into sections keyed by H1 headings. The heading line is removed
    from the section body. If no H1 is found, returns one section with the
    default_title and the entire body.
    """
    lines = body.splitlines()
    sections: list[tuple[str, str]] = []
    cur_title: Optional[str] = None
    cur_lines: list[str] = []

    for ln in lines:
        m = _H1_RE.match(ln)
        if m:
            if cur_title is not None:
                sections.append((cur_title, "\n".join(cur_lines).strip("\n")))
            cur_title = m.group(1).strip()
            cur_lines = []
            continue
        cur_lines.append(ln)

    if cur_title is None:
        cur_title = default_title
    sections.append((cur_title, "\n".join(cur_lines).strip("\n")))
    return sections


def _split_front_matter(text: str) -> tuple[Optional[str], str]:
    """
    Split a markdown file into (front_matter_text_or_None, body_text).

    Front matter is assumed to be a YAML block starting with '---' at the very
    top of the file and ending at the next line that is exactly '---'.
    """
    lines = text.splitlines()
    if not lines:
        return None, text
    if lines[0].strip() != "---":
        return None, text

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        # malformed, treat as no front matter
        return None, text

    meta_block = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1 :])
    body = body.lstrip("\n")
    return meta_block, body


def _title_from_front_matter(meta_block: str, base_title: str = "") -> Optional[str]:
    """
    Extract 'title: ...' from a YAML-like front matter block and optionally strip
    a leading '<base_title> - ' / '<base_title> – ' / '<base_title>: ' prefix.
    """
    m = re.search(r"^title\s*:\s*(.+)$", meta_block, re.MULTILINE)
    if not m:
        return None
    title = m.group(1).strip()
    # strip wrapping quotes
    if (title.startswith('"') and title.endswith('"')) or (
        title.startswith("'") and title.endswith("'")
    ):
        title = title[1:-1].strip()

    if base_title:
        # build a case-insensitive prefix pattern: ^<base_title>\s*[-–:]\s*
        pattern = re.compile(
            rf"^{re.escape(base_title)}\s*[-–:]\s*",
            re.IGNORECASE,
        )
        title = pattern.sub("", title, count=1).strip()

    return title or None


def _extract_cover_image(yaml_text: str) -> Optional[str]:
    """
    Extract 'cover-image: ...' from book.yml (scalar, one-line value).
    Returns the raw value (URL or path) or None if not present.
    """
    m = re.search(r"^cover-image\s*:\s*(.+)$", yaml_text, re.MULTILINE)
    if not m:
        return None
    val = m.group(1).strip()
    # strip simple quotes
    if (val.startswith('"') and val.endswith('"')) or (
        val.startswith("'") and val.endswith("'")
    ):
        val = val[1:-1].strip()
    return val or None


def _extract_yaml_scalar(yaml_text: str, key: str) -> Optional[str]:
    """
    Extract a simple scalar value from a YAML-looking block: 'key: value'.
    Returns the unquoted value or None if missing. Uses YAML parsing first so
    escape sequences (e.g., '\n') are interpreted as actual newlines.
    """
    try:
        docs = list(yaml.safe_load_all(yaml_text))
        data = docs[0] if docs else {}
        if isinstance(data, dict) and key in data:
            val = data.get(key)
            if val is None:
                return None
            return str(val).strip()
    except Exception:
        pass

    m = re.search(rf"^{re.escape(key)}\s*:\s*(.+)$", yaml_text, re.MULTILINE)
    if not m:
        return None
    val = m.group(1).strip()
    if (val.startswith('"') and val.endswith('"')) or (
        val.startswith("'") and val.endswith("'")
    ):
        val = val[1:-1].strip()
    return val or None


def _latex_escape(text: str) -> str:
    """
    Minimal LaTeX escaping for common special characters.
    """
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    out = text
    for old, new in replacements.items():
        out = out.replace(old, new)
    return out


def _subtitle_segments(text: str) -> list[tuple[str, int]]:
    """
    Split subtitle into (line_text, blank_lines_before) tuples.
    Leading/trailing newlines are ignored. Blank lines only add spacing before
    subsequent text (never after the last line).
    """
    normalized = text.replace("\r\n", "\n").strip("\n")
    if not normalized:
        return []

    segments: list[tuple[str, int]] = []
    blank_run = 0
    for ln in normalized.split("\n"):
        stripped = ln.strip()
        if stripped == "":
            if segments:
                blank_run += 1
            continue
        segments.append((stripped, blank_run))
        blank_run = 0
    return segments


def _normalize_human_md_spacing(text: str) -> str:
    """
    Ensure two blank lines before each heading and one blank line after,
    and wrap images with blank lines.
    """
    lines = text.replace("\r\n", "\n").splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        is_heading = bool(re.match(r"^\s*#{1,6}\s", ln))
        is_image = bool(re.match(r"!\[.*\]\([^)]*\)", ln.strip()))

        if is_heading:
            # ensure two blank lines before
            blanks = 0
            j = len(out) - 1
            while j >= 0 and out[j].strip() == "":
                blanks += 1
                j -= 1
            while blanks < 2:
                out.append("")
                blanks += 1
            out.append(ln.strip())
            # ensure one blank line after
            if i + 1 >= len(lines) or lines[i + 1].strip() != "":
                out.append("")
            i += 1
            continue

        if is_image:
            if not out or out[-1].strip() != "":
                out.append("")
            out.append(ln.strip())
            if i + 1 >= len(lines) or lines[i + 1].strip() != "":
                out.append("")
            i += 1
            continue

        out.append(ln)
        i += 1

    return "\n".join(out).strip("\n") + "\n"


_HDR_SIMPLE_RE = re.compile(r"^(?P<hash>#{1,6})\s+(?P<title>.+)$")
_ID_TRAIL_RE = re.compile(r"\s*\{#([^\}]+)\}\s*$")


def _build_md_toc(text: str, depth: int) -> str:
    """
    Build a Markdown TOC up to the given depth from headings in text.
    """
    lines = []
    for ln in text.splitlines():
        m = _HDR_SIMPLE_RE.match(ln)
        if not m:
            continue
        lvl = len(m.group("hash"))
        if lvl > depth:
            continue
        raw_title = m.group("title").strip()
        hid = None
        # Strip trailing {#id}
        raw_clean = _ID_TRAIL_RE.sub("", raw_title).strip()
        indent = "  " * (lvl - 1)
        lines.append(f"{indent}- {raw_clean}")
    return "\n".join(lines) + ("\n" if lines else "")


def _inline_css(html_path: Path, css_path: Optional[Path]) -> None:
    """
    Inline CSS content into the generated HTML so the file is standalone.
    Removes link tags pointing to the CSS file.
    """
    if not css_path or not css_path.exists() or not html_path.exists():
        return
    try:
        html_txt = html_path.read_text(encoding="utf-8")
        css_txt = css_path.read_text(encoding="utf-8")
    except Exception:
        return

    style_block = "<style>\n" + css_txt + "\n</style>\n"
    html_txt = re.sub(
        rf'<link[^>]+href=["\']{re.escape(css_path.name)}["\'][^>]*>\s*',
        "",
        html_txt,
        flags=re.IGNORECASE,
    )
    if "</head>" in html_txt:
        html_txt = html_txt.replace("</head>", style_block + "</head>", 1)
    else:
        html_txt = style_block + html_txt

    html_path.write_text(html_txt, encoding="utf-8")


def _ensure_header_packages(path: Path, packages: list[str]) -> None:
    """
    Ensure the YAML front matter declares header-includes with the given LaTeX
    packages. Adds header-includes if missing.
    """
    if not path.exists():
        return

    txt = path.read_text(encoding="utf-8")
    lines = txt.splitlines()
    if not lines or lines[0].strip() != "---":
        return

    header_end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            header_end = i
            break
    if header_end is None:
        return

    hi_idx = None
    for i in range(1, header_end):
        if lines[i].lstrip().startswith("header-includes"):
            hi_idx = i
            break

    if hi_idx is None:
        insert_pos = header_end
        lines.insert(insert_pos, "header-includes:")
        insert_pos += 1
        for pkg in packages:
            lines.insert(insert_pos, f"  - '{pkg}'")
            insert_pos += 1
        header_end += 1 + len(packages)
    else:
        existing = set()
        j = hi_idx + 1
        while j < header_end and lines[j].startswith("  -"):
            existing.add(lines[j].split(None, 1)[1].strip().strip("'\""))
            j += 1
        insert_pos = j
        added = 0
        for pkg in packages:
            if pkg not in existing:
                lines.insert(insert_pos, f"  - '{pkg}'")
                insert_pos += 1
                added += 1
        header_end += added

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# def _strip_conflicting_keys(yaml_text: str) -> str:
#     """
#     Remove keys that may cause weird template output like 'truetrue'
#     when printed by the HTML template (e.g. booleans).

#     We strip:
#       - autoSectionLabels
#       - autoSectionLabelsDepth
#       - linkReferences
#     """
#     lines = yaml_text.replace("\r\n", "\n").splitlines()
#     out: list[str] = []
#     skip = {"autosectionlabels", "autosectionlabelsdepth", "linkreferences"}

#     for line in lines:
#         raw = line.lstrip()
#         if not raw or raw.startswith("#"):
#             out.append(line)
#             continue
#         key = raw.split(":", 1)[0].strip()
#         if key.lower() in skip:
#             continue
#         out.append(line)

#     return "\n".join(out)


def _normalize_book_yaml_as_front_matter(yaml_text: str) -> str:
    """
    Ensure book.yml content becomes a valid top-level YAML metadata block
    with explicit '---' ... '---' delimiters, after stripping conflicting keys.
    """
    # yaml_text = _strip_conflicting_keys(yaml_text)
    lines = yaml_text.replace("\r\n", "\n").splitlines()

    if not lines:
        return "---\n---\n\n"

    # case 1: already starts with '---'
    if lines[0].strip() == "---":
        has_closing = any(line.strip() == "---" for line in lines[1:])
        if not has_closing:
            lines.append("---")
        return "\n".join(lines) + "\n\n"

    # case 2: no leading '---' => wrap in a block
    return "---\n" + "\n".join(lines) + "\n---\n\n"


def render_book_yaml(
    src: Path,
    *,
    timeout: int = 0,
    omit_toc: bool = False,
    omit_numbering: bool = False,
    make_pdf: bool = True,
    make_html: bool = True,
    make_epub: bool = False,
    toc_depth: int = 2,
    shift_headings: Optional[int] = None,
    auto_shift: bool = True,
    number_offset: Optional[str] = None,
    epub_chapter_level: Optional[int] = None,
    verbose: bool = False,
) -> tuple[Optional[Path], Optional[Path]]:
    """
    Book mode:
      - src is a *.yml / *.yaml book metadata file
      - collect all *.md in that directory (alphabetically)
      - build one big <Title>.md with:
          * book.yml as a single YAML metadata block (properly delimited, without
            conflicting keys like autoSectionLabels/linkReferences)
          * for each chapter .md:
              - strip its own front matter
              - inject '# <chapter title>' from that front matter (or filename)
              - append body
      - produce <Title>.pdf / <Title>.html / <Title>.epub
    """
    if not src.exists():
        die(f"Missing source: {src}")

    book_dir = src.parent
    base = title = title_from_book_yaml(src)

    print(f"Book mode: metadata={src.name}  title={title!r}  base={base}")

    human_md_path = book_dir / f"{base}.md"
    pandoc_md_path = book_dir / f"{base}.pandoc.md"

    md_files = sorted(
        p
        for p in book_dir.iterdir()
        if p.is_file()
        and p.suffix.lower() == ".md"
        and p.name != f"{base}.md"
        and p.name != f"{base}.pandoc.md"
    )
    if not md_files:
        die(f"No .md files found in {book_dir}")

    # 1) book-level YAML front matter (from book.yml), normalized and cleaned
    raw_yaml_text = src.read_text(encoding="utf-8")
    cover_value = _extract_cover_image(raw_yaml_text)
    yaml_block = _normalize_book_yaml_as_front_matter(raw_yaml_text)

    title_text = _extract_yaml_scalar(raw_yaml_text, "title") or title
    author_text = _extract_yaml_scalar(raw_yaml_text, "author") or ""
    date_text = _extract_yaml_scalar(raw_yaml_text, "date") or date.today().isoformat()

    with human_md_path.open("w", encoding="utf-8") as fh, pandoc_md_path.open(
        "w", encoding="utf-8"
    ) as fp:
        # Human-friendly header (pandoc percent style) without YAML
        fh.write(f"% {title_text}\n% {author_text}\n% {date_text}\n\n")

        # Pandoc input keeps full YAML metadata/front matter.
        fp.write(yaml_block)

        # 2) each chapter .md becomes '# title' + body (front matter stripped)
        for p in md_files:
            chapter_raw = p.read_text(encoding="utf-8").replace("\r\n", "\n")
            meta_block, body = _split_front_matter(chapter_raw)

            chapter_title: Optional[str] = None
            if meta_block is not None:
                chapter_title = _title_from_front_matter(meta_block, base)
            if not chapter_title:
                chapter_title = p.stem

            sections = _split_by_h1(body, chapter_title)

            for sec_title, sec_body in sections:
                latex_title = _latex_escape(sec_title)
                is_ack = "acknowledgment" in sec_title.lower() or "acknowledgement" in sec_title.lower()
                is_toc = sec_title.strip().lower() in {"table of contents", "contents"}
                hid = _slugify(sec_title)

                body_stripped = sec_body.strip()

                # ----- Write pandoc/LaTeX version -----
                if is_ack:
                    latex_body = (
                        _latex_escape(body_stripped)
                        .replace("\n\n", "\\par\n\\vspace{0.6em}\n")
                        .replace("\n", " ")
                    )
                    title_block = (
                        "```{=latex}\n"
                        "\\clearpage\n"
                        "\\thispagestyle{empty}\n"
                        "\\vspace*{0.30\\textheight}\n"
                        "\\begin{center}\n"
                        f"{{\\bfseries\\Large {latex_title}}}\\par\n"
                        "\\vspace{2.2em}\n"
                        f"{{\\itshape {latex_body}}}\\par\n"
                        "\\end{center}\n"
                        "\\clearpage\n"
                        "```\n\n"
                    )
                    fp.write(title_block)
                    # For HTML/EPUB emit a page break and a real heading/body so split-level works,
                    # but hide that heading from LaTeX (PDF already has the styled page above).
                    fp.write("```{=html}\n<div class=\"page-break\"></div>\n```\n\n")
                    fp.write("```{=latex}\n\\iffalse\n```\n")
                    fp.write(f"# {sec_title} {{#{hid} .chapter .unlisted}}\n\n")
                    if body_stripped:
                        fp.write(f"*{body_stripped}*\n\n")
                    fp.write("```{=latex}\n\\fi\n```\n\n")
                elif is_toc:
                    title_block = (
                        "```{=latex}\n"
                        "\\clearpage\n"
                        "\\thispagestyle{empty}\n"
                        "\\begin{center}\n"
                        "\\vspace*{0.11\\textheight}\n"
                        "{\\bfseries\\fontsize{24pt}{32pt}\\selectfont Table of Contents}\\par\n"
                        "\\end{center}\n"
                        "\\vspace{1.0em}\n"
                        "\\noindent{\\color[gray]{0.65}\\rule{\\textwidth}{0.6pt}}\n"
                        "\\color{black}\n"
                        "\\vspace{2.0em}\n"
                        "```\n\n"
                    )
                    fp.write(title_block)
                    fp.write("```{=html}\n<div class=\"page-break\"></div>\n```\n\n")
                    fp.write("```{=latex}\n\\iffalse\n```\n")
                    fp.write(f"# Table of Contents {{#{hid} .chapter .unlisted}}\n\n")
                    fp.write("[[TOC]]\n\n")
                    fp.write("```{=latex}\n\\fi\n```\n\n")
                else:
                    title_block = (
                        "```{=latex}\n"
                        "\\clearpage\n"
                        "\\thispagestyle{empty}\n"
                        "\\begin{center}\n"
                        "\\vspace*{0.28\\textheight}\n"
                        "{\\begingroup\\setlength{\\baselineskip}{2.1\\baselineskip}\n"
                        f"{{\\bfseries\\fontsize{{26pt}}{{52pt}}\\selectfont {latex_title}}}\\par\n"
                        "\\endgroup}\n"
                        "\\end{center}\n"
                        "\\clearpage\n"
                        "```\n\n"
                    )
                    fp.write(title_block)
                    fp.write("```{=latex}\n\\vspace*{0.18\\textheight}\n```\n")
                    is_part_heading = sec_title.strip().lower().startswith("part ")
                    hid = _slugify(sec_title)
                    if is_part_heading:
                        heading_line = f"# {sec_title} {{#{hid}}}"
                    else:
                        heading_line = f"# {sec_title} {{#{hid} .chapter}}"
                    fp.write(f"{heading_line}\n\n")
                    fp.write(body_stripped + "\n\n")

                # ----- Write human-readable version (no LaTeX) -----
                is_part_heading = sec_title.strip().lower().startswith("part ")
                hid = _slugify(sec_title)
                if is_ack:
                    fh.write(f"# {sec_title}\n\n")
                    if body_stripped:
                        fh.write(f"*{body_stripped}*\n\n")
                elif is_toc:
                    fh.write("# Table of Contents\n\n[[TOC]]\n\n")
                else:
                    if is_part_heading:
                        heading_line = f"# {sec_title}"
                    else:
                        heading_line = f"# {sec_title}"
                    fh.write(f"{heading_line}\n\n")
                    fh.write(body_stripped + "\n\n")

    # Normalize spacing in the human-readable markdown.
    try:
        human_text = human_md_path.read_text(encoding="utf-8")
        human_text = _normalize_human_md_spacing(human_text)
        # Replace [[TOC]] with a Markdown TOC up to the requested toc_depth.
        if "[[TOC]]" in human_text:
            toc_md = _build_md_toc(human_text, toc_depth)
            human_text = human_text.replace("[[TOC]]", toc_md)
        human_md_path.write_text(human_text, encoding="utf-8")
    except Exception:
        pass

    print(f"✅ Built combined markdown {human_md_path} (pandoc input {pandoc_md_path})")

    effective_epub_level = epub_chapter_level
    if make_epub and effective_epub_level is None:
        effective_epub_level = 1
    epub_split_args: list[str] = []
    if make_epub and effective_epub_level is not None:
        epub_split_args = ["--split-level", str(effective_epub_level)]
    # Rely on EPUB nav document for the TOC (no explicit --toc).
    epub_extra_args = epub_split_args

    (
        in_tmp,
        final_pandoc_md,
        meta_args,
        shift_args,
        common_args,
        css_path,
    ) = prepare_preprocessed(
        pandoc_md_path,
        omit_toc=omit_toc,
        omit_numbering=omit_numbering,
        toc_depth=toc_depth,
        shift_headings=shift_headings,
        auto_shift=auto_shift,
        number_offset=number_offset,
        epub_chapter_level=effective_epub_level,
    )

    # If cover-image was specified in book.yml, ensure a local copy exists in
    # the tmp dir (where pandoc runs) and rewrite the metadata to point to it.
    local_name: Optional[str] = None
    if cover_value:
        tmpdir = in_tmp.parent

        cv = cover_value
        strip_cover = False

        try:
            if cv.startswith("http://") or cv.startswith("https://"):
                # Download via curl to tmpdir/cover.ext
                from urllib.parse import urlparse

                parsed = urlparse(cv)
                ext = Path(parsed.path).suffix or ".jpg"
                dest = tmpdir / ("cover" + ext)
                rc = run_visible(["curl", "-L", "-o", str(dest), cv])
                if rc != 0:
                    print(f"[WARN] cover-image fetch failed (rc={rc}); skipping cover: {cv}")
                    strip_cover = True
                elif dest.exists():
                    local_name = dest.name
                else:
                    print(f"[WARN] cover-image missing after download; skipping cover: {cv}")
                    strip_cover = True
            else:
                # Treat as filesystem path (absolute or relative to book_dir)
                src_img = Path(cv)
                if not src_img.is_absolute():
                    src_img = book_dir / src_img
                if not src_img.exists():
                    print(f"[WARN] cover-image not found; skipping cover: {src_img}")
                    strip_cover = True
                else:
                    dest = tmpdir / src_img.name
                    shutil.copy2(src_img, dest)
                    local_name = dest.name
        except Exception as e:
            print(f"[WARN] cover-image processing failed; skipping cover: {e}")
            strip_cover = True

        # Rewrite the cover-image metadata in in_tmp YAML to point to local_name
        if local_name:
            text = in_tmp.read_text(encoding="utf-8")
            lines = text.splitlines()
            if lines and lines[0].strip() == "---":
                # Walk inside the front matter until the closing '---'
                for i in range(1, len(lines)):
                    if lines[i].strip() == "---":
                        break
                    stripped = lines[i].lstrip()
                    if stripped.startswith("cover-image"):
                        indent = lines[i][: len(lines[i]) - len(stripped)]
                        lines[i] = f"{indent}cover-image: {local_name}"
                        break
                text = "\n".join(lines)
                in_tmp.write_text(text, encoding="utf-8")
        elif strip_cover:
            # Strip the cover-image entry from the YAML block so pandoc won't fail.
            text = in_tmp.read_text(encoding="utf-8")
            lines = text.splitlines()
            if lines and lines[0].strip() == "---":
                header_end = None
                for i in range(1, len(lines)):
                    if lines[i].strip() == "---":
                        header_end = i
                        break
                if header_end is not None:
                    kept: list[str] = []
                    for i, line in enumerate(lines):
                        if 0 < i < header_end and line.lstrip().startswith("cover-image"):
                            continue
                        kept.append(line)
                    text = "\n".join(kept)
                    in_tmp.write_text(text, encoding="utf-8")

    # Ensure LaTeX packages needed for the cover/title pages are available.
    _ensure_header_packages(
        in_tmp, ["\\usepackage{geometry}", "\\usepackage{graphicx}", "\\usepackage{xcolor}"]
    )

    # Cache common metadata once so it can be reused below.
    title_text = _extract_yaml_scalar(raw_yaml_text, "title") or title
    subtitle_text = _extract_yaml_scalar(raw_yaml_text, "subtitle")
    author_text = _extract_yaml_scalar(raw_yaml_text, "author")
    publisher_text = _extract_yaml_scalar(raw_yaml_text, "publisher")

    # Inject a full-page cover (if present) plus a centered title/subtitle/author page
    # at the very start of the document. This uses the local cover file downloaded
    # into the temp directory so PDF creation works offline.
    def _inject_frontmatter_pages(path: Path, cover_filename: Optional[str]) -> None:
        if not path.exists():
            return

        ltitle = _latex_escape(title_text) if title_text else ""
        lsubtitle = _latex_escape(subtitle_text) if subtitle_text else None
        lauthor = _latex_escape(author_text) if author_text else None
        subtitle_segments = _subtitle_segments(lsubtitle) if lsubtitle else []
        html_cover_src = cover_value or None

        cover_block = ""
        if cover_filename:
            cover_block = (
                "```{=latex}\n"
                "\\clearpage\n"
                "\\thispagestyle{empty}\n"
                "\\newgeometry{margin=0pt}\n"
                "\\noindent\n"
                f"\\includegraphics[width=\\paperwidth,height=\\paperheight]{{{cover_filename}}}\n"
                "\\restoregeometry\n"
                "\\clearpage\n"
                "```\n\n"
            )

        title_lines = [
            "```{=latex}",
            "\\clearpage",
            "\\thispagestyle{empty}",
            "\\begin{center}",
            "\\vspace*{0.25\\textheight}",
        ]
        if ltitle:
            title_lines.append(
                "{\\begingroup\\setlength{\\baselineskip}{1.8\\baselineskip}\n"
                f"{{\\bfseries\\fontsize{{28pt}}{{56pt}}\\selectfont {ltitle}}}\\par\n"
                "\\endgroup}"
            )
        if subtitle_segments:
            title_lines.append("\\vspace{1.6em}")
            for idx, (seg, blanks) in enumerate(subtitle_segments):
                gap = blanks + (1 if idx > 0 else 0)
                for _ in range(gap):
                    title_lines.append("\\vspace{1.1em}")
                title_lines.append(
                    f"{{\\normalfont\\fontsize{{18pt}}{{26pt}}\\selectfont {seg}}}\\par"
                )
        if lauthor:
            title_lines += [
                "\\vspace{3.25em}",
                f"{{\\Large\\bfseries {lauthor}}}\\par",
            ]
        title_lines += [
            "\\end{center}",
            "\\clearpage",
            "```",
            "",
            "",
        ]
        title_block = "\n".join(title_lines)

        html_title_parts: list[str] = []
        if html_cover_src:
            html_title_parts.append(
                f'<div class="title-cover"><img src="{html.escape(html_cover_src)}" alt="Cover image" /></div>'
            )
        if title_text:
            html_title_parts.append(f'<h1 class="book-title">{html.escape(title_text)}</h1>')
        if subtitle_text:
            html_title_parts.append(f'<div class="subtitle">{html.escape(subtitle_text)}</div>')
        if author_text:
            html_title_parts.append(f'<div class="book-author">{html.escape(author_text)}</div>')
        html_block = ""
        if html_title_parts:
            html_block = (
                "```{=html}\n"
                '<div class="title-page">\n'
                + "\n".join(html_title_parts)
                + "\n</div>\n"
                '<div class="page-break"></div>\n'
                "```\n\n"
            )

        txt = path.read_text(encoding="utf-8")
        lines = txt.splitlines()
        header_end = None
        if lines and lines[0].strip() == "---":
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    header_end = i
                    break

        if header_end is not None:
            head = "\n".join(lines[: header_end + 1])
            body = "\n".join(lines[header_end + 1 :]).lstrip("\n")
        else:
            head = ""
            body = txt.lstrip("\n")

        new_txt = (
            (head + "\n\n" if head else "")
            + cover_block
            + title_block
            + html_block
            + body
        )
        path.write_text(new_txt, encoding="utf-8")

    _inject_frontmatter_pages(in_tmp, local_name)

    pdf_path = pandoc_md_path.with_suffix(".pdf") if make_pdf else None
    html_path = pandoc_md_path.with_suffix(".html") if make_html else None
    epub_path = pandoc_md_path.with_suffix(".epub") if make_epub else None

    if make_pdf:
        out_pdf = in_tmp.parent / "out.pdf"
        pdf_log = in_tmp.parent / "pandoc-pdf.log.json"
        pdf_extras = ["-V", "title=", "-V", "subtitle=", "-V", "author="]
        rc = render_pdf(
            in_tmp,
            out_pdf,
            meta_args,
            shift_args,
            common_args,
            timeout,
            log_path=pdf_log,
            verbose=verbose,
            extra_args=pdf_extras,
        )
        if verbose or rc != 0:
            print_pandoc_log(pdf_log, label="PDF")
        if rc != 0:
            die(f"Docker pandoc (PDF) failed (rc={rc})")
        shutil.copy2(out_pdf, pdf_path)

    # Suppress pandoc's auto title block for HTML/EPUB (use our injected title page),
    # while keeping metadata via title-meta/pagetitle/author-meta.
    meta_overrides: list[str] = []
    if title_text:
        meta_overrides += ["-M", f"title-meta={title_text}", "-M", f"pagetitle={title_text}"]
    if author_text:
        meta_overrides += ["-M", f"author-meta={author_text}"]
    if publisher_text:
        meta_overrides += ["-M", f"publisher={publisher_text}"]

    if make_html:
        out_html = in_tmp.parent / "out.html"
        html_log = in_tmp.parent / "pandoc-html.log.json"
        rc = render_html(
            in_tmp,
            out_html,
            meta_args + meta_overrides,
            shift_args,
            common_args,
            timeout,
            css_path,
            log_path=html_log,
            verbose=verbose,
        )
        if verbose or rc != 0:
            print_pandoc_log(html_log, label="HTML")
        if rc != 0:
            die(f"Docker pandoc (HTML) failed (rc={rc})")
        shutil.copy2(out_html, html_path)
        _inline_css(html_path, css_path)

    if make_epub:
        # Use the same input for EPUB so headings (including TOC/Ack) split pages consistently.
        epub_in = in_tmp

        out_epub = in_tmp.parent / "out.epub"
        epub_log = in_tmp.parent / "pandoc-epub.log.json"
        rc = render_epub(
            epub_in,
            out_epub,
            meta_args + meta_overrides,
            shift_args,
            common_args,
            timeout,
            css_path,
            extra_args=epub_extra_args,
            log_path=epub_log,
            verbose=verbose,
        )
        if verbose or rc != 0:
            print_pandoc_log(epub_log, label="EPUB")
        if rc != 0:
            die(f"Docker pandoc (EPUB) failed (rc={rc})")
        shutil.copy2(out_epub, epub_path)

    if css_path and css_path.exists():
        dest_css = book_dir / css_path.name
        try:
            shutil.copy2(css_path, dest_css)
        except Exception:
            print(f"[WARN] could not copy CSS to {dest_css}")

    wrote = [
        str(p)
        for p in [pdf_path, html_path, epub_path, human_md_path, final_pandoc_md]
        if p
    ]
    print("✅ Wrote " + ", ".join(wrote))

    return (
        pdf_path.resolve() if pdf_path else None,
        html_path.resolve() if html_path else None,
    )
