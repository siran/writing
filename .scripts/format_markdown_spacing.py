#!/usr/bin/env python3

"""
Normalize Markdown spacing:
- Ensure TWO line before headings.
- Ensure ONE blank line after headings.
- Surround images lines, blockquotes and citations with TWO blank lines.
- Leave fenced code blocks untouched.

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

import sys
from pathlib import Path


def is_fence(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def format_lines(lines: list[str]) -> list[str]:
    formatted: list[str] = []
    in_code_block = False
    i = 0

    def ensure_two_blank_before() -> None:
        # Remove trailing blank lines, then add exactly two (if not at start).
        while formatted and formatted[-1].strip() == "":
            formatted.pop()
        if formatted:
            formatted.append("")
            formatted.append("")

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if is_fence(line):
            in_code_block = not in_code_block
            formatted.append(line)
            i += 1
            continue

        if in_code_block:
            formatted.append(line)
            i += 1
            continue

        is_heading = stripped.startswith("#")
        is_image = stripped.startswith("![")
        is_quote = stripped.startswith(">")

        if is_heading:
            ensure_two_blank_before()
            formatted.append(line)
            i += 1

            while i < len(lines) and lines[i].strip() == "":
                i += 1
            if i < len(lines):
                formatted.append("")
            continue

        if is_image or is_quote:
            ensure_two_blank_before()

            current_is_quote = is_quote
            current_is_image = is_image

            while i < len(lines):
                candidate = lines[i]
                candidate_stripped = candidate.strip()
                if is_fence(candidate):
                    break

                if current_is_quote and not candidate_stripped.startswith(">"):
                    break
                if current_is_image and not candidate_stripped.startswith("!["):
                    break

                formatted.append(candidate)
                i += 1

            while i < len(lines) and lines[i].strip() == "":
                i += 1
            if i < len(lines):
                formatted.append("")
                formatted.append("")

            continue

        formatted.append(line)
        i += 1

    return formatted


def main(path: Path) -> int:
    if not path.exists():
        return 0

    original_text = path.read_text(encoding="utf-8")
    lines = original_text.splitlines()

    new_lines = format_lines(lines)
    new_text = "\n".join(new_lines)
    if not new_text.endswith("\n"):
        new_text += "\n"

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
