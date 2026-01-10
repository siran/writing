#!/usr/bin/env python3

"""
Format Markdown in-place using numbertext-style wrapping plus spacing rules:
- Leave YAML/TOML front matter untouched.
- Do not change content inside code fences, inline code, or math ($ / $$).
- Wrap paragraphs to 80 columns while preserving blockquote prefixes.
- Keep image lines intact (no wrapping).
- Normalize blank lines between blocks:
  - 2 before headings (except after front matter or another heading).
  - 1 after headings.
  - 2 after blockquotes/images.

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
from typing import Optional


HEADING_RE = re.compile(r"^(\s*)(#{1,6})(\s+.*)$")
ARROW_LINE_RE = re.compile(r"^\s*(?:->|>)\s*")
IMAGE_LINE_RE = re.compile(r"^\s*!\[")
FOOTNOTE_DEF_RE = re.compile(r"^\s*\[\^[^\]]+\]:")
FOOTNOTE_PREFIX_RE = re.compile(r"^(\s*\[\^[^\]]+\]:)\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^(\s*)([-*+]|[0-9]+[.)])(\s+|$)(.*)$")
FENCE_START_RE = re.compile(r"^\s*(`{3,}|~{3,})")
MATH_BLOCK_DELIM_RE = re.compile(r"^\s*\$\$\s*$")
WRAP_WIDTH = 80
FRONT_MATTER_DELIMS = ("---", "+++")
INLINE_TOKEN_PREFIX = "<<<CODEXSPAN"
INLINE_TOKEN_SUFFIX = ">>>"


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

        fence = is_fence_start(line)
        if fence:
            buf = [line]
            i += 1
            while i < len(lines):
                buf.append(lines[i])
                if is_fence_end(lines[i], fence):
                    i += 1
                    break
                i += 1
            blocks.append(("literal", buf))
            continue

        if MATH_BLOCK_DELIM_RE.match(line):
            buf = [line]
            i += 1
            while i < len(lines):
                buf.append(lines[i])
                if MATH_BLOCK_DELIM_RE.match(lines[i]):
                    i += 1
                    break
                i += 1
            blocks.append(("literal", buf))
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
            if is_fence_start(cur) or MATH_BLOCK_DELIM_RE.match(cur):
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


def inline_token(idx: int) -> str:
    return f"{INLINE_TOKEN_PREFIX}{idx}{INLINE_TOKEN_SUFFIX}"


def make_placeholder(idx: int, span: str) -> str:
    base = inline_token(idx)
    if len(base) >= len(span):
        return base
    return base + ("X" * (len(span) - len(base)))


def is_escaped(text: str, idx: int) -> bool:
    backslashes = 0
    i = idx - 1
    while i >= 0 and text[i] == "\\":
        backslashes += 1
        i -= 1
    return backslashes % 2 == 1


def protect_inline_spans(text: str) -> tuple[str, list[tuple[str, str]]]:
    replacements: list[tuple[str, str]] = []
    out: list[str] = []
    i = 0

    while i < len(text):
        ch = text[i]

        if ch == "`" and not is_escaped(text, i):
            run_len = 1
            while i + run_len < len(text) and text[i + run_len] == "`":
                run_len += 1
            j = i + run_len
            while j < len(text):
                if text[j] == "`" and not is_escaped(text, j):
                    if text.startswith("`" * run_len, j):
                        span = text[i : j + run_len]
                        token = make_placeholder(len(replacements), span)
                        out.append(token)
                        replacements.append((token, span))
                        i = j + run_len
                        break
                j += 1
            else:
                out.append(text[i : i + run_len])
                i += run_len
            continue

        if ch == "$" and not is_escaped(text, i):
            if text.startswith("$$", i):
                j = i + 2
                while j < len(text) - 1:
                    if text.startswith("$$", j) and not is_escaped(text, j):
                        span = text[i : j + 2]
                        token = make_placeholder(len(replacements), span)
                        out.append(token)
                        replacements.append((token, span))
                        i = j + 2
                        break
                    j += 1
                else:
                    out.append("$$")
                    i += 2
                continue

            j = i + 1
            while j < len(text):
                if text[j] == "$" and not is_escaped(text, j):
                    if not (j > 0 and text[j - 1] == "$") and not (
                        j + 1 < len(text) and text[j + 1] == "$"
                    ):
                        span = text[i : j + 1]
                        token = make_placeholder(len(replacements), span)
                        out.append(token)
                        replacements.append((token, span))
                        i = j + 1
                        break
                j += 1
            else:
                out.append(ch)
                i += 1
            continue

        out.append(ch)
        i += 1

    return "".join(out), replacements


def restore_inline_spans(text: str, replacements: list[tuple[str, str]]) -> str:
    for token, span in replacements:
        text = text.replace(token, span)
    return text


def is_fence_start(line: str) -> Optional[str]:
    match = FENCE_START_RE.match(line)
    return match.group(1) if match else None


def is_fence_end(line: str, fence: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith(fence)


def split_front_matter(lines: list[str]) -> tuple[list[str], list[str]]:
    if not lines:
        return [], lines

    first_line = lines[0].strip()
    if first_line not in FRONT_MATTER_DELIMS:
        return [], lines

    end_tokens = ("...", first_line) if first_line == "---" else (first_line,)
    for idx in range(1, len(lines)):
        if lines[idx].strip() in end_tokens:
            return lines[: idx + 1], lines[idx + 1 :]

    return [], lines


def wrap_paragraph(text: str, width: int = WRAP_WIDTH) -> str:
    lines = text.splitlines()
    out_lines: list[str] = []
    buffer: list[str] = []

    def wrap_prefixed(
        prefix: str, content: str, *, repeat_prefix: bool = True
    ) -> list[str]:
        content = content.strip()
        if not content:
            return [prefix.rstrip()]
        masked, replacements = protect_inline_spans(content)
        wrapper = textwrap.TextWrapper(
            width=width,
            initial_indent=prefix,
            subsequent_indent=prefix if repeat_prefix else (" " * len(prefix)),
            break_long_words=False,
            break_on_hyphens=False,
        )
        wrapped = wrapper.fill(masked)
        return restore_inline_spans(wrapped, replacements).splitlines()

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
            masked, replacements = protect_inline_spans(joined)
            wrapper = textwrap.TextWrapper(
                width=width,
                initial_indent=indent,
                subsequent_indent=indent,
                break_long_words=False,
                break_on_hyphens=False,
            )
            wrapped = wrapper.fill(masked)
            out_lines.extend(
                restore_inline_spans(wrapped, replacements).splitlines()
            )
        buffer.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "":
            flush_buffer()
            out_lines.append("")
            i += 1
            continue

        m = LIST_ITEM_RE.match(line)
        if m:
            flush_buffer()
            indent, marker, gap, content = m.groups()
            prefix = f"{indent}{marker}{gap}"
            content_indent_len = len(prefix)
            parts: list[str] = []
            if content.strip():
                parts.append(content.strip())
            i += 1
            while i < len(lines):
                next_line = lines[i]
                if next_line.strip() == "":
                    break
                if LIST_ITEM_RE.match(next_line):
                    break
                leading_ws = len(next_line) - len(next_line.lstrip(" \t"))
                if leading_ws < content_indent_len:
                    break
                continuation = next_line[content_indent_len:]
                if continuation.strip():
                    parts.append(continuation.strip())
                i += 1
            if parts:
                out_lines.extend(
                    wrap_prefixed(prefix, " ".join(parts), repeat_prefix=False)
                )
            else:
                out_lines.append(prefix.rstrip())
            continue

        m = re.match(r"^(\s*->\s*)(.*)$", line)
        if m:
            flush_buffer()
            prefix, content = m.groups()
            out_lines.extend(wrap_prefixed(prefix, content))
            i += 1
            continue

        m = re.match(r"^(\s*>\s*\|\s*)(.*)$", line)
        if m:
            flush_buffer()
            prefix, content = m.groups()
            out_lines.extend(wrap_prefixed(prefix, content))
            i += 1
            continue

        m = re.match(r"^(\s*>\s*)(.*)$", line)
        if m:
            flush_buffer()
            prefix, content = m.groups()
            out_lines.extend(wrap_prefixed(prefix, content))
            i += 1
            continue

        buffer.append(line)
        i += 1

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

    masked, replacements = protect_inline_spans(content)
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent=f"{prefix} ",
        subsequent_indent="",
        break_long_words=False,
        break_on_hyphens=False,
    )
    wrapped = wrapper.fill(masked)
    return restore_inline_spans(wrapped, replacements)


def format_paragraph(paragraph: str) -> str:
    trailing = len(paragraph) - len(paragraph.rstrip("\n"))
    core = paragraph.rstrip("\n")
    if not core:
        return "\n" * trailing

    if is_footnote_block(core):
        core = wrap_footnote_block(core)
        return core + ("\n" * trailing)

    core = wrap_paragraph(core)
    return core + ("\n" * trailing)


def format_only(lines: list[str], leading_context: Optional[str] = None) -> str:
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
        elif kind == "literal":
            block_kind = "literal"
            text = "".join(blines)
        else:
            paragraph = "".join(blines)
            if is_image_paragraph(blines):
                block_kind = "image"
                text = paragraph
            else:
                block_kind = "blockquote" if is_blockquote_paragraph(blines) else "para"
                text = format_paragraph(paragraph)

        if block_kind == "literal":
            blocks.append((block_kind, text))
        else:
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
    if leading_context == "front_matter" and blocks[0][0] == "heading":
        leading_blank_lines = 1
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
    front_matter: list[str] = []
    body_lines = lines
    if path.suffix.lower() == ".md":
        front_matter, body_lines = split_front_matter(lines)

    new_text = "".join(front_matter) + format_only(
        body_lines, leading_context="front_matter" if front_matter else None
    )
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
