# pnpmd_preprocess.py

import re
import tempfile
from pathlib import Path
from typing import Optional, Tuple, Set, Dict, List

import yaml

from pnpmd_util import find_repo_root, load_map, die

# ---------- Protection of code, math ----------
_FENCE_RE = re.compile(r'(^|\n)(?P<f>```+|~~~+)[^\n]*\n.*?(\n(?P=f)[ \t]*\n|$)', re.DOTALL)
_INLINE_CODE_RE = re.compile(r'(?P<ticks>`+)(?P<body>[^`]*?)\1')
_MATH_BLOCK_RE = re.compile(r'(^|\n)\$\$[\s\S]*?\$\$(?=\s*(\n|$))', re.MULTILINE)
_INLINE_MATH_RE = re.compile(r'(?<!\$)\$(?!\$)(?:\\\$|[^$])+\$(?!\$)')


def _protect(text: str):
    blobs: List[str] = []

    def stash(m):
        i = len(blobs)
        blobs.append(m.group(0))
        return f"\u0000B{i}\u0000"

    text = _FENCE_RE.sub(stash, text)
    text = _INLINE_CODE_RE.sub(stash, text)
    text = _MATH_BLOCK_RE.sub(stash, text)
    text = _INLINE_MATH_RE.sub(stash, text)
    return text, blobs


def _unprotect(text: str, blobs: List[str]):
    return re.sub(r'\u0000B(\d+)\u0000', lambda mm: blobs[int(mm.group(1))], text)


# ---------- Unicode superscripts ----------
_SUPERSCRIPT_RE = re.compile(
    r'[\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079]+'
)
_SUPERSCRIPT_MAP = {
    "\u2070": "0",
    "\u00b9": "1",
    "\u00b2": "2",
    "\u00b3": "3",
    "\u2074": "4",
    "\u2075": "5",
    "\u2076": "6",
    "\u2077": "7",
    "\u2078": "8",
    "\u2079": "9",
}


def replace_unicode_superscripts(md: str) -> str:
    prot, blobs = _protect(md)

    def repl(m: re.Match) -> str:
        digits = "".join(_SUPERSCRIPT_MAP[ch] for ch in m.group(0))
        return f"^{digits}^"

    prot = _SUPERSCRIPT_RE.sub(repl, prot)
    return _unprotect(prot, blobs)


# ---------- Mapping ----------
def apply_mappings_safe(s: str, entries):
    prot, blobs = _protect(s)
    for lhs, rhs, is_regex in (e for e in entries if e[2]):
        rep = f"${rhs}$" if rhs.startswith("\\") else rhs
        prot = re.sub(lhs[1:-1], rep, prot, flags=re.DOTALL)
    for lhs, rhs, is_regex in (e for e in entries if not e[2]):
        rep = f"${rhs}$" if rhs.startswith("\\") else rhs
        prot = prot.replace(lhs, rep)
    return _unprotect(prot, blobs)


# ---------- % header ----------
_PERC_LINE = re.compile(r'^\s*%\s*(.*)\s*$')


def extract_yaml_front_matter(text: str):
    lines = text.splitlines()
    if not lines:
        return text, {}, []
    if lines[0].strip() != "---":
        return text, {}, []
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            end_idx = i
            break
    if end_idx is None:
        return text, {}, []
    yaml_text = "\n".join(lines[1:end_idx])
    try:
        data = yaml.safe_load(yaml_text) or {}
    except Exception:
        data = {}
    stripped = "\n".join(lines[end_idx + 1 :]).lstrip("\n")
    raw_head = lines[: end_idx + 1]
    return stripped, data, raw_head


def extract_percent_block(text: str):
    lines = text.splitlines()
    meta = {"title": None, "authors": [], "date": None}
    i = 0
    for j in range(min(3, len(lines))):
        m = _PERC_LINE.match(lines[j])
        if not m:
            break
        val = m.group(1).strip()
        if j == 0:
            meta["title"] = val or None
        elif j == 1:
            parts = [
                p.strip()
                for chunk in re.split(r'\band\b|,', val)
                for p in [chunk]
                if p.strip()
            ]
            meta["authors"] = parts
        elif j == 2:
            meta["date"] = val or None
        i += 1
    raw_head = lines[:i]
    stripped = "\n".join(lines[i:]).lstrip("\n") if i else text
    return stripped, meta, raw_head


def _is_blank(val) -> bool:
    if val is None:
        return True
    if isinstance(val, str):
        return not val.strip()
    if isinstance(val, (list, tuple)):
        return all(_is_blank(v) for v in val)
    if isinstance(val, dict):
        return all(_is_blank(v) for v in val.values())
    return False


def _validate_percent_meta(meta: Dict, raw_head: List[str]) -> None:
    if len(raw_head) < 3:
        die("Pandoc % header must provide 3 lines: title, author, date.")
    if _is_blank(meta.get("title")):
        die("Pandoc % header missing title.")
    if _is_blank(meta.get("authors")):
        die("Pandoc % header missing author.")
    if _is_blank(meta.get("date")):
        die("Pandoc % header missing date.")


def _validate_yaml_meta(meta: Dict) -> None:
    title = meta.get("title")
    author = meta.get("author") or meta.get("authors")
    date = meta.get("date")
    if _is_blank(title):
        die("YAML front matter missing title.")
    if _is_blank(author):
        die("YAML front matter missing author.")
    if _is_blank(date):
        die("YAML front matter missing date.")


def _parse_author_list(val) -> List[str]:
    if not val:
        return []
    values = val if isinstance(val, list) else [val]
    out: List[str] = []
    for item in values:
        if item is None:
            continue
        if isinstance(item, str):
            parts = [
                p.strip()
                for chunk in re.split(r"\band\b|,", item)
                for p in [chunk]
                if p.strip()
            ]
            out.extend(parts)
        else:
            s = str(item).strip()
            if s:
                out.append(s)
    return out


# ---------- IDs, anchors ----------
_HDR_RE = re.compile(
    r'^(?P<hash>#{1,6})\s+(?P<title>.+?)(?:\s+\{(?P<attrs>[^}]*)\})?\s*$'
)
_ATTR_ID_RE = re.compile(r'(?:^|\s)#([A-Za-z0-9_:-]+)(?=\s|$)')
_LINK_LABEL_RE = re.compile(r'\[([^\]]+)\]\([^)]+\)')
_FORMAT_MARKER_RE = re.compile(r'[*_~`]+')


def _auto_slug(title: str) -> str:
    t = _LINK_LABEL_RE.sub(r'\1', title)
    t = _FORMAT_MARKER_RE.sub('', t)
    t = t.lower()
    t = re.sub(r'[^0-9a-zA-Z _-]+', '', t)
    t = t.strip().replace(' ', '-')
    t = re.sub(r'-{2,}', '-', t).strip('-')
    return t or 'x'


def collect_all_ids(md: str) -> Set[str]:
    ids: Set[str] = set()
    for ln in md.splitlines():
        m = _HDR_RE.match(ln)
        if m:
            title = m.group('title')
            attrs = m.group('attrs') or ''
            for mm in _ATTR_ID_RE.finditer(attrs):
                ids.add(mm.group(1))
            ids.add(_auto_slug(title))
        for mm in re.finditer(r'\{#([A-Za-z0-9_:-]+)\}', ln):
            ids.add(mm.group(1))
    return ids


_ATTR_BLOCK_RE = re.compile(r'\{#([A-Za-z0-9_:-]+)\}')
_BRACKETED_LABEL_ANCHOR_RE = re.compile(r'\[([^\]]+?)\]\s*\{#([A-Za-z0-9_:-]+)\}')
_EMPTY_SPAN_ANCHOR_RE = re.compile(r'\[\]\{#([A-Za-z0-9_-]+)\}')


def prose_anchors_and_labels(md: str) -> Tuple[str, Dict[str, str]]:
    prot, blobs = _protect(md)
    out_lines: List[str] = []
    label_map: Dict[str, str] = {}
    for ln in prot.splitlines():
        if _HDR_RE.match(ln):
            out_lines.append(ln)
            continue
        for m in _BRACKETED_LABEL_ANCHOR_RE.finditer(ln):
            label = m.group(1)
            pid = m.group(2)
            if ":" in pid:
                continue
            label_map.setdefault(pid, label)

        def sub_attr(m):
            pid = m.group(1)
            if ":" in pid:
                return m.group(0)
            start = m.start()
            prefix = ln[:start]
            if re.search(r'\[\]\s*$', prefix):
                return m.group(0)
            if re.search(r'\]\s*$', prefix):
                return m.group(0)
            return f'[]{{#{pid}}}'

        ln2 = _ATTR_BLOCK_RE.sub(sub_attr, ln)
        out_lines.append(ln2)
    result = "\n".join(out_lines)
    return _unprotect(result, blobs), label_map


_DEST_NORM_RE = re.compile(
    r'\]\(\s*@(?:(sec|fig|eq|tbl):)?([A-Za-z0-9_-]+)\s*\)'
)


def normalize_link_destinations(md: str) -> str:
    prot, blobs = _protect(md)

    def repl(m):
        kind = m.group(1)
        ident = m.group(2)
        return f'](#{"%s:%s" % (kind, ident) if kind else ident})'

    prot = _DEST_NORM_RE.sub(repl, prot)
    return _unprotect(prot, blobs)


_AT_UNBRACKETED = re.compile(r'(?<![A-Za-z0-9._%+-])@(?P<id>[A-Za-z0-9_-]+)\b')
_AT_BRACKETED = re.compile(r'\[\s*@(?P<id>[A-Za-z0-9_-]+)\s*\]')


def rewrite_at_tokens(
    md: str,
    *,
    label_map: Dict[str, str],
    span_ids: Set[str],
    header_ids: Set[str],
) -> str:
    prot, blobs = _protect(md)
    outs: List[str] = []

    def keep(s: str) -> str:
        i = len(outs)
        outs.append(s)
        return f"\u0000L{i}\u0000"

    def make_link(ident: str, bracketed: bool) -> str:
        if ":" in ident:
            return f'@{ident}' if not bracketed else f'[@{ident}]'
        if ident in label_map:
            return f'[{label_map[ident]}](#{ident})'
        if ident in span_ids or ident in header_ids:
            return f'[@{ident}](#{ident})'
        return f'@{ident}' if not bracketed else f'[@{ident}]'

    prot = _AT_BRACKETED.sub(
        lambda m: keep(make_link(m.group('id'), True)), prot
    )
    prot = _AT_UNBRACKETED.sub(
        lambda m: keep(make_link(m.group('id'), False)), prot
    )
    prot = re.sub(r'\u0000L(\d+)\u0000', lambda mm: outs[int(mm.group(1))], prot)
    return _unprotect(prot, blobs)


_SEC_UNBR = re.compile(r'(?<![A-Za-z0-9._%+-])@sec:([A-Za-z0-9_-]+)\b')
_SEC_BRKT = re.compile(r'\[\s*@sec:([A-Za-z0-9_-]+)\s*\]')


def atsec_to_nameref(md: str) -> str:
    prot, blobs = _protect(md)
    prot = _SEC_BRKT.sub(
        lambda m: f"\\nameref{{sec:{m.group(1)}}}", prot
    )
    prot = _SEC_UNBR.sub(
        lambda m: f"\\nameref{{sec:{m.group(1)}}}", prot
    )
    return _unprotect(prot, blobs)


_BARE_HASH_RE = re.compile(r'(?<![#A-Za-z0-9_{(])#([A-Za-z0-9_:-]+)\b(?!\()')


def rewrite_hash_anchors(md: str) -> str:
    prot, blobs = _protect(md)

    def repl_line(ln: str) -> str:
        if _HDR_RE.match(ln):
            return ln
        return _BARE_HASH_RE.sub(lambda m: f'[](#{m.group(1)})', ln)

    new_lines = [repl_line(ln) for ln in prot.splitlines()]
    prot2 = "\n".join(new_lines)
    return _unprotect(prot2, blobs)


def _build_html_toc(md: str, depth: int) -> str:
    """
    Build an HTML TOC (unordered list) up to the given depth using the
    normalized heading IDs we generate during preprocessing.
    """
    items: list[tuple[int, str, str]] = []
    for ln in md.splitlines():
        m = _HDR_RE.match(ln)
        if not m:
            continue
        lvl = len(m.group('hash'))
        if lvl > depth:
            continue
        raw_title = m.group('title').strip()
        attrs = m.group('attrs') or ""

        # Skip unlisted/auxiliary headings (e.g., injected TOC page).
        if ".unlisted" in attrs.split() or re.search(r"\.unlisted\b", attrs):
            continue

        # If a heading line contains an inline empty span with id ([]{#id}),
        # strip it from the display text and prefer that id.
        span_id = None
        span_match = re.search(r'\[\]\s*\{#([^\}]+)\}', raw_title)
        if span_match:
            span_id = span_match.group(1)
            raw_title = re.sub(r'\s*\[\]\s*\{#([^\}]+)\}\s*', '', raw_title).strip()

        anchor = None
        for mm in _ATTR_ID_RE.finditer(attrs):
            anchor = mm.group(1)
        if not anchor and span_id:
            anchor = span_id
        anchor = anchor or _auto_slug(raw_title)

        items.append((lvl, raw_title, anchor))

    if not items:
        return ""

    html: list[str] = []
    prev_level = 0
    first = True
    for lvl, title, anchor in items:
        while prev_level < lvl:
            html.append("<ul>")
            prev_level += 1
        while prev_level > lvl:
            html.append("</li></ul>")
            prev_level -= 1
        if not first:
            html.append("</li>")
        html.append(f'<li><a href="#{anchor}">{title}</a>')
        first = False

    html.append("</li>")
    while prev_level > 0:
        html.append("</ul>")
        prev_level -= 1

    return "\n".join(html)


# ---------- TOC, heading spacing ----------
_TOC_MARK_RE = re.compile(r'^\s*\[\[TOC\]\]\s*$', re.MULTILINE)
_TOC_LATEX_RE = re.compile(r'^\s*\\TOC\s*$', re.MULTILINE)
_ATTR_ID_RE = re.compile(r'(?:^|\s)#([A-Za-z0-9_:-]+)(?=\s|$)')


def insert_toc_after_keywords_content(md: str) -> str:
    if _TOC_MARK_RE.search(md) or _TOC_LATEX_RE.search(md):
        return md
    lines = md.splitlines()
    start_idx = None
    lvl = None
    for i, ln in enumerate(lines):
        m = _HDR_RE.match(ln)
        if not m:
            continue
        title = m.group('title').strip()
        if title.lower().startswith('keywords'):
            start_idx = i
            lvl = len(m.group('hash'))
            break
    if start_idx is None:
        return md
    end = len(lines)
    for j in range(start_idx + 1, len(lines)):
        m = _HDR_RE.match(lines[j])
        if m and len(m.group('hash')) <= lvl:
            end = j
            break
    lines.insert(end, "")
    lines.insert(end + 1, "\n[[TOC]]\n")
    lines.insert(end + 2, "")
    return "\n".join(lines)


def replace_toc_marker(md: str, toc_depth: int, shift: int = 0) -> Tuple[str, bool]:
    touched = False
    latex_td = max(0, toc_depth)
    html_td = max(0, toc_depth - shift)
    html_toc = _build_html_toc(md, html_td)
    toc_block = (
        "\\begingroup\n"
        f"\\setcounter{{tocdepth}}{{{latex_td}}}\n"
        "\\renewcommand{\\contentsname}{}\n"
        "\\setlength{\\parskip}{0.35em}\n"
        "\\tableofcontents\n"
        "\\endgroup"
    )
    if html_toc:
        toc_block += (
            "\n\n```{=html}\n"
            "<div class=\"toc\">\n"
            f"{html_toc}\n"
            "</div>\n"
            "```\n"
        )
    if _TOC_MARK_RE.search(md):
        md = _TOC_MARK_RE.sub(lambda m: f'\n{toc_block}\n', md)
        touched = True
    if _TOC_LATEX_RE.search(md):
        md = _TOC_LATEX_RE.sub(lambda m: f'\n{toc_block}\n', md)
        touched = True
    if touched:
        return md, True
    return md, False


def normalize_heading_spacing(md: str) -> str:
    prot, blobs = _protect(md)
    lines = prot.splitlines()
    out: List[str] = []
    for i, ln in enumerate(lines):
        if _HDR_RE.match(ln):
            if len(out) >= 1 and out[-1].strip() != "":
                out.append("")
            if len(out) >= 2 and out[-2].strip() != "":
                out.append("")
            out.append(ln)
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                out.append("")
        else:
            out.append(ln)
    return _unprotect("\n".join(out), blobs)


def _min_heading_level(md: str) -> Optional[int]:
    lvl = None
    for ln in md.splitlines():
        m = _HDR_RE.match(ln)
        if not m:
            continue
        n = len(m.group('hash'))
        lvl = n if lvl is None else min(lvl, n)
    return lvl


def _normalize_heading_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.strip().lower()).strip()


def _has_heading(md: str, target: str) -> bool:
    norm_target = _normalize_heading_title(target)
    for ln in md.splitlines():
        m = _HDR_RE.match(ln)
        if not m:
            continue
        norm_title = _normalize_heading_title(m.group("title"))
        if norm_title == norm_target or norm_title.startswith(norm_target + " "):
            return True
    return False


def _yaml_text(meta: Dict, *keys: str) -> str:
    for key in keys:
        if key in meta:
            val = meta.get(key)
            if val is None:
                continue
            if isinstance(val, list):
                parts = [str(v).strip() for v in val if str(v).strip()]
                if parts:
                    return ", ".join(parts)
                continue
            text = str(val).strip()
            if text:
                return text
    return ""


def _inject_title_page_meta(body: str, yaml_meta: Dict) -> str:
    if not yaml_meta:
        return body

    one_sentence = _yaml_text(
        yaml_meta,
        "one-sentence-summary",
        "one_sentence_summary",
        "one_sentence",
        "oss",
    )
    abstract = _yaml_text(yaml_meta, "abstract", "summary")
    keywords = _yaml_text(yaml_meta, "keywords", "keyword")

    blocks: List[str] = []
    if one_sentence and not _has_heading(body, "One-Sentence Summary"):
        blocks.append(f"**One-Sentence Summary.** {one_sentence}")
    if abstract and not _has_heading(body, "Abstract"):
        blocks.append(f"**Abstract.** {abstract}")
    if keywords and not _has_heading(body, "Keywords"):
        blocks.append(f"**Keywords.** {keywords}")

    if not blocks:
        return body

    injected = "\n\n".join(blocks) + "\n\n"
    if not (_TOC_MARK_RE.search(body) or _TOC_LATEX_RE.search(body)):
        injected += "[[TOC]]\n\n"
    return injected + body


# ---------- Core entry ----------
def prepare_preprocessed(
    src: Path,
    *,
    omit_toc: bool,
    omit_numbering: bool,
    toc_depth: int = 2,
    shift_headings: Optional[int] = None,
    auto_shift: bool = True,
    number_offset: Optional[str] = None,
    epub_chapter_level: Optional[int] = None,
    include_css: bool = True,
) -> Tuple[Path, Path, List[str], List[str], List[str], Optional[Path]]:
    """
    Returns:
      in_tmp, final_pandoc_md, meta_args, shift_args, common_args, css_path
    """
    repo = find_repo_root(src.parent)
    entries = load_map(repo / "pnpmd.map")
    print(f"Using map: {repo / 'pnpmd.map'}  (rules={len(entries)})")

    raw = src.read_text(encoding="utf-8").replace("\r\n", "\n")

    body_wo_yaml, yaml_meta, yaml_head = extract_yaml_front_matter(raw)
    mapped = apply_mappings_safe(body_wo_yaml, entries)
    stripped, meta, raw_head = extract_percent_block(mapped)

    use_percent = len(raw_head) > 0
    use_yaml = not use_percent

    if use_percent:
        _validate_percent_meta(meta, raw_head)
        yaml_head = []
    else:
        if not yaml_head:
            die("Missing required metadata: add a 3-line % header or YAML front matter.")
        _validate_yaml_meta(yaml_meta or {})
    header_and_inline_ids = collect_all_ids(stripped)

    body, label_map = prose_anchors_and_labels(stripped)
    body = normalize_link_destinations(body)
    span_ids = set(_EMPTY_SPAN_ANCHOR_RE.findall(body))
    body = rewrite_at_tokens(
        body, label_map=label_map, span_ids=span_ids, header_ids=header_and_inline_ids
    )
    body = atsec_to_nameref(body)
    body = rewrite_hash_anchors(body)
    body = normalize_heading_spacing(body)
    body = _inject_title_page_meta(body, yaml_meta)
    if src.name.lower().endswith(".fdn.md"):
        body = replace_unicode_superscripts(body)

    keep_parts = []
    if use_yaml and yaml_head:
        keep_parts.append("\n".join(yaml_head))
    if use_percent and raw_head:
        keep_parts.append("\n".join(raw_head))
    keep_head = "\n".join(keep_parts) + ("\n\n" if keep_parts else "")

    body2 = body
    has_toc_marker = False
    if not omit_toc:
        body2 = insert_toc_after_keywords_content(body2)

    shift_preview = 0
    if shift_headings is not None:
        shift_preview = shift_headings
    elif auto_shift:
        mhl = _min_heading_level(body2)
        if mhl and mhl > 1:
            shift_preview = 1 - mhl

    if not omit_toc:
        body2, has_toc_marker = replace_toc_marker(body2, toc_depth, shift_preview)

    tmpdir = Path(tempfile.mkdtemp(prefix="pnpmd_"))
    in_tmp = tmpdir / "in.md"
    text_for_pandoc = keep_head + (body2 if not omit_toc else body)
    in_tmp.write_text(text_for_pandoc, encoding="utf-8")

    if src.name.endswith(".pandoc.md"):
        final_pandoc_md = src
    else:
        final_pandoc_md = src.with_suffix(".pandoc.md")
    # Persist exactly what we feed to pandoc (with TOC replacement when enabled)
    # so debug/served .pandoc.md matches the actual render input.
    final_pandoc_md.write_text(text_for_pandoc, encoding="utf-8")

    css_path = None
    css_src = repo / ".scripts" / "render" / "book-style.css"
    if include_css and css_src.exists():
        css_path = tmpdir / css_src.name
        css_path.write_text(css_src.read_text(encoding="utf-8"), encoding="utf-8")

    meta_args: List[str] = []
    if use_percent:
        if meta.get("title"):
            meta_args += ["-M", f"title={meta['title']}"]
        for a in meta.get("authors", []):
            meta_args += ["-M", f"author={a}"]
        if meta.get("date"):
            meta_args += ["-M", f"date={meta['date']}"]
    else:
        title = yaml_meta.get("title")
        subtitle = yaml_meta.get("subtitle")
        authors = _parse_author_list(
            yaml_meta.get("author") or yaml_meta.get("authors")
        )
        date_val = yaml_meta.get("date")
        if title is not None:
            meta_args += ["-M", f"title={str(title).strip()}"]
        if subtitle is not None:
            meta_args += ["-M", f"subtitle={str(subtitle).strip()}"]
        for a in authors:
            meta_args += ["-M", f"author={a}"]
        if date_val is not None:
            meta_args += ["-M", f"date={str(date_val).strip()}"]

    # heading shift: explicit > auto > 0
    if shift_headings is not None or auto_shift:
        shift = shift_preview
    else:
        shift = 0
    shift_args = ["--shift-heading-level-by", str(shift)] if shift != 0 else []

    reader = "markdown+yaml_metadata_block+tex_math_dollars+raw_tex"
    if src.name.lower().endswith(".fdn.md"):
        reader += "+superscript"
    toc_flag: List[str] = [] if (omit_toc or has_toc_marker) else ["--toc"]
    numbering_flag: List[str] = [] if omit_numbering else ["--number-sections"]
    if number_offset is not None and not omit_numbering:
        numbering_flag += ["--number-offset", number_offset]

    toc_opts: List[str] = []
    if not omit_toc:
        toc_opts.append(f"--toc-depth={toc_depth}")

    common_args = toc_opts + numbering_flag + toc_flag + ["-f", reader]

    return in_tmp, final_pandoc_md, meta_args, shift_args, common_args, css_path
