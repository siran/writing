#!/usr/bin/env python3

"""
Format Markdown in-place using numbertext-style wrapping plus spacing rules:
- Normalize blockquote spacing ("->" -> "> |", ">" -> "> ").
- Wrap paragraphs to 80 columns while preserving blockquote formatting.
- Keep image lines intact (no wrapping).
- Normalize blank lines between blocks:
  - 1 after headings and before blockquotes/images.
  - 2 after blockquotes/images and before new headings (except heading->heading).

Useful to use with Emerald's `emeraldwalk.runonsave`:
```
{
    "emeraldwalk.runonsave": {
        "commands": [
            {
                "match": ".*\\.md$",
                "cmd": "cd \"${workspaceFolder}\" && python3 .scripts/format_markdown_spacing.py \"${file}\""
            }
        ]
    }
}
```
"""

from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path


HEADING_RE = re.compile(r"^(\s*)(#{1,6})(\s+.*)$")
ARROW_LINE_RE = re.compile(r"^\s*(?:->|>)\s*")
IMAGE_LINE_RE = re.compile(r"^\s*!\[")
FOOTNOTE_DEF_RE = re.compile(r"^\s*\[\^[^\]]+\]:")
FOOTNOTE_PREFIX_RE = re.compile(r"^(\s*\[\^[^\]]+\]:)\s*(.*)$")
WRAP_WIDTH = 80


def split_blocks_with_implicit_breaks(lines: list[str]) -> list[tuple[str, list[str]]]:
    """
    Blocks: heading / blank / para.
    Implicit break:
      - if previous line starts with '->' or '>' and next line does NOT
      - if a run of image lines starts or ends
    """
    blocks: list[tuple[str, list[str]]] = []
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.strip() == "":
            j = i
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            blocks.append(("blank", lines[i:j]))
            i = j
            continue

        if HEADING_RE.match(line.rstrip("\n")):
            blocks.append(("heading", [line]))
            i += 1
            continue

        buf: list[str] = []
        prev_was_arrow = False
        prev_was_image = False

        while i < len(lines):
            cur = lines[i]
            if cur.strip() == "":
                break
            if HEADING_RE.match(cur.rstrip("\n")):
                break

            cur_is_arrow = bool(ARROW_LINE_RE.match(cur))
            cur_is_image = bool(IMAGE_LINE_RE.match(cur))

            if buf and prev_was_arrow and not cur_is_arrow:
                blocks.append(("para", buf))
                blocks.append(("blank", ["\n"]))
                buf = []
                prev_was_arrow = False
                prev_was_image = False
                continue

            if buf and (not prev_was_arrow) and cur_is_arrow:
                blocks.append(("para", buf))
                blocks.append(("blank", ["\n"]))
                buf = []
                prev_was_arrow = False
                prev_was_image = False
                continue

            if buf and prev_was_image and not cur_is_image:
                blocks.append(("para", buf))
                blocks.append(("blank", ["\n"]))
                buf = []
                prev_was_arrow = False
                prev_was_image = False
                continue

            if buf and (not prev_was_image) and cur_is_image:
                blocks.append(("para", buf))
                blocks.append(("blank", ["\n"]))
                buf = []
                prev_was_arrow = False
                prev_was_image = False
                continue

            buf.append(cur)
            prev_was_arrow = cur_is_arrow
            prev_was_image = cur_is_image
            i += 1

        if buf:
            blocks.append(("para", buf))

    return blocks


def is_blockquote_paragraph(blines: list[str]) -> bool:
    has_content = False
    for line in blines:
        if line.strip() == "":
            continue
        has_content = True
        if not ARROW_LINE_RE.match(line):
            return False
    return has_content


def is_image_paragraph(blines: list[str]) -> bool:
    has_content = False
    for line in blines:
        if line.strip() == "":
            continue
        has_content = True
        if not IMAGE_LINE_RE.match(line):
            return False
    return has_content


def is_footnote_block(paragraph: str) -> bool:
    """Return True if paragraph begins with a footnote definition like [^w1-4]:."""
    for line in paragraph.splitlines():
        if line.strip() == "":
            continue
        return bool(FOOTNOTE_DEF_RE.match(line))
    return False


def normalize_block_text(text: str) -> str:
    return text.rstrip("\n") + "\n"


def ensure_newline_before_blockquotes(text: str) -> str:
    out: list[str] = []
    line_has_text = False
    line_is_blockquote = False
    prev_line_was_blockquote = False
    i = 0

    def ensure_blank_line() -> None:
        nonlocal line_has_text, line_is_blockquote, prev_line_was_blockquote
        if not out:
            line_has_text = False
            line_is_blockquote = False
            prev_line_was_blockquote = False
            return
        while out and out[-1] in (" ", "\t"):
            out.pop()
        if not out:
            line_has_text = False
            line_is_blockquote = False
            prev_line_was_blockquote = False
            return
        if out[-1] != "\n":
            out.append("\n")
        if len(out) < 2 or out[-2] != "\n":
            out.append("\n")
        prev_line_was_blockquote = False
        line_has_text = False
        line_is_blockquote = False

    while i < len(text):
        ch = text[i]
        if ch == "\n":
            out.append(ch)
            prev_line_was_blockquote = line_is_blockquote
            line_has_text = False
            line_is_blockquote = False
            i += 1
            continue
        if text.startswith("->", i):
            m = re.match(r"->\s*", text[i:])
            adv = m.end() if m else 2
            if line_has_text or not prev_line_was_blockquote:
                ensure_blank_line()
            out.append("> | ")
            line_has_text = True
            line_is_blockquote = True
            i += adv
            continue
        if text.startswith(">", i):
            m = re.match(r">\s*", text[i:])
            adv = m.end() if m else 1
            if line_has_text or not prev_line_was_blockquote:
                ensure_blank_line()
            out.append("> ")
            line_has_text = True
            line_is_blockquote = True
            i += adv
            continue
        out.append(ch)
        if not ch.isspace():
            line_has_text = True
        i += 1

    return "".join(out)


def wrap_paragraph(text: str, width: int = WRAP_WIDTH) -> str:
    lines = text.splitlines()
    out_lines: list[str] = []
    buffer: list[str] = []

    def flush_buffer() -> None:
        if not buffer:
            return
        m = re.match(r"^(\s*)", buffer[0])
        indent = m.group(1) if m else ""
        stripped = []
        for line in buffer:
            if line.startswith(indent):
                stripped.append(line[len(indent):].strip())
            else:
                stripped.append(line.strip())
        joined = " ".join(part for part in stripped if part != "")
        if joined:
            wrapper = textwrap.TextWrapper(
                width=width,
                initial_indent=indent,
                subsequent_indent=indent,
                break_long_words=False,
                break_on_hyphens=False,
            )
            out_lines.extend(wrapper.fill(joined).splitlines())
        buffer.clear()

    for line in lines:
        if line.strip() == "":
            flush_buffer()
            out_lines.append("")
            continue

        m = re.match(r"^(\s*)>\s*\|\s*(.*)$", line)
        if m:
            flush_buffer()
            indent, content = m.group(1), m.group(2).rstrip()
            if content:
                out_lines.append(f"{indent}> | {content}")
            else:
                out_lines.append(f"{indent}> |")
            continue

        m = re.match(r"^(\s*)>\s*(.*)$", line)
        if m:
            flush_buffer()
            indent, content = m.group(1), m.group(2).strip()
            prefix = f"{indent}> "
            wrapper = textwrap.TextWrapper(
                width=width,
                initial_indent=prefix,
                subsequent_indent=prefix,
                break_long_words=False,
                break_on_hyphens=False,
            )
            if content:
                out_lines.extend(wrapper.fill(content).splitlines())
            else:
                out_lines.append(prefix.rstrip())
            continue

        buffer.append(line)

    flush_buffer()
    return "\n".join(out_lines)


def wrap_footnote_block(text: str, width: int = WRAP_WIDTH) -> str:
    lines = text.splitlines()
    if not lines:
        return ""

    m = FOOTNOTE_PREFIX_RE.match(lines[0])
    if not m:
        return wrap_paragraph(text, width=width)

    prefix = m.group(1)
    parts = []
    if m.group(2).strip():
        parts.append(m.group(2).strip())
    for line in lines[1:]:
        if line.strip():
            parts.append(line.strip())
    content = " ".join(parts)

    if not content:
        return prefix

    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent=f"{prefix} ",
        subsequent_indent="",
        break_long_words=False,
        break_on_hyphens=False,
    )
    return wrapper.fill(content)


def format_paragraph(paragraph: str) -> str:
    trailing = len(paragraph) - len(paragraph.rstrip("\n"))
    core = paragraph.rstrip("\n")
    if not core:
        return "\n" * trailing

    if is_footnote_block(core):
        core = wrap_footnote_block(core)
        return core + ("\n" * trailing)

    core = ensure_newline_before_blockquotes(core)
    core = wrap_paragraph(core)
    return core + ("\n" * trailing)


def format_only(lines: list[str]) -> str:
    raw_blocks = split_blocks_with_implicit_breaks(lines)
    blocks: list[tuple[str, str]] = []
    gaps: list[int] = []
    gap_lines = 0

    for kind, blines in raw_blocks:
        if kind == "blank":
            gap_lines += len(blines)
            continue

        gaps.append(gap_lines)
        gap_lines = 0

        if kind == "heading":
            block_kind = "heading"
            text = blines[0]
        else:
            paragraph = "".join(blines)
            if is_image_paragraph(blines):
                block_kind = "image"
                text = paragraph
            else:
                block_kind = "blockquote" if is_blockquote_paragraph(blines) else "para"
                text = format_paragraph(paragraph)

        blocks.append((block_kind, normalize_block_text(text)))

    if not blocks:
        return "".join(lines)

    def required_blank_lines_between(prev_kind: str, next_kind: str) -> int:
        required = 1
        if prev_kind in ("blockquote", "image"):
            required = max(required, 2)
        if next_kind == "heading":
            required = max(required, 1 if prev_kind == "heading" else 2)
        return required

    out: list[str] = []
    leading_blank_lines = gaps[0] if gaps else 0
    if leading_blank_lines:
        out.append("\n" * leading_blank_lines)
    out.append(blocks[0][1])

    for idx in range(1, len(blocks)):
        prev_kind = blocks[idx - 1][0]
        next_kind = blocks[idx][0]
        required_blank_lines = required_blank_lines_between(prev_kind, next_kind)
        out.append("\n" * required_blank_lines)
        out.append(blocks[idx][1])

    if gap_lines:
        out.append("\n" * gap_lines)

    return "".join(out)


def main(path: Path) -> int:
    if not path.exists():
        return 0

    original_text = path.read_text(encoding="utf-8")
    lines = original_text.splitlines(keepends=True)

    new_text = format_only(lines)
    if new_text != original_text:
        path.write_text(new_text, encoding="utf-8")

    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit("Usage: format_markdown_spacing.py <path-to-markdown>")

    # Join args so unquoted paths containing spaces still work.
    path = Path(" ".join(args))
    if not path.exists():
        sys.exit(f"Path not found: {path}. If the file path has spaces, wrap it in quotes.")

    sys.exit(main(path))
