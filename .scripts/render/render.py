#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import shutil
import re
from pathlib import Path
from typing import Optional

from pnpmd_preprocess import prepare_preprocessed, replace_unicode_superscripts
from pnpmd_pandoc import render_pdf, render_html, render_epub
from pnpmd_book import render_book_yaml
from pnpmd_util import discover_md_in_cwd, die, print_pandoc_log


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


_FENCE_RE = re.compile(
    r'(^|\n)(?P<f>```+|~~~+)[^\n]*\n.*?(\n(?P=f)[ \t]*\n|$)', re.DOTALL
)
_INLINE_CODE_RE = re.compile(r'(?P<ticks>`+)(?P<body>[^`]*?)\1')
_MATH_BLOCK_RE = re.compile(r'(^|\n)\$\$[\s\S]*?\$\$(?=\s*(\n|$))', re.MULTILINE)
_INLINE_MATH_RE = re.compile(r'(?<!\$)\$(?!\$)(?:\\\$|[^$])+\$(?!\$)')

def _protect_blocks_and_code(text: str):
    blobs: list[str] = []

    def stash(m: re.Match) -> str:
        i = len(blobs)
        blobs.append(m.group(0))
        return f"\u0000B{i}\u0000"

    text = _FENCE_RE.sub(stash, text)
    text = _INLINE_CODE_RE.sub(stash, text)
    text = _MATH_BLOCK_RE.sub(stash, text)
    return text, blobs


def _unprotect(text: str, blobs: list[str]) -> str:
    return re.sub(r'\u0000B(\d+)\u0000', lambda mm: blobs[int(mm.group(1))], text)


def _inline_math_to_blocks_md(md: str) -> str:
    prot, blobs = _protect_blocks_and_code(md)

    def repl(m: re.Match) -> str:
        inner = m.group(0)[1:-1]
        return f"\n$$\n{inner}\n$$\n"

    prot = _INLINE_MATH_RE.sub(repl, prot)
    return _unprotect(prot, blobs)


def _blocks_pandoc_md_path(src: Path) -> Path:
    name = src.name
    if name.endswith(".blocks.pandoc.md"):
        return src
    if name.endswith(".pandoc.md"):
        base = name[:-len(".pandoc.md")]
    elif name.endswith(".md"):
        base = name[:-len(".md")]
    else:
        base = src.stem
    return src.with_name(f"{base}.blocks.pandoc.md")


def _blocks_html_path(blocks_pandoc_md: Path) -> Path:
    name = blocks_pandoc_md.name
    if name.endswith(".blocks.pandoc.md"):
        base = name[:-len(".blocks.pandoc.md")]
    else:
        base = blocks_pandoc_md.stem
    return blocks_pandoc_md.with_name(f"{base}.blocks.html")


def _render_blocks_html(
    blocks_pandoc_md: Path,
    *,
    meta_args: list[str],
    shift_args: list[str],
    common_args: list[str],
    timeout: int,
    css_path: Optional[Path],
    verbose: bool,
    html_embed_resources: bool,
) -> Optional[Path]:
    if not blocks_pandoc_md or not blocks_pandoc_md.exists():
        return None

    from tempfile import mkdtemp

    tmpdir = Path(mkdtemp(prefix="pnpmd_"))
    in_tmp = tmpdir / "in.md"
    in_tmp.write_text(blocks_pandoc_md.read_text(encoding="utf-8"), encoding="utf-8")

    css_local = None
    if css_path and css_path.exists():
        css_local = tmpdir / css_path.name
        css_local.write_text(css_path.read_text(encoding="utf-8"), encoding="utf-8")

    out_html = tmpdir / "out.html"
    html_log = tmpdir / "pandoc-html.log.json"
    rc = render_html(
        in_tmp,
        out_html,
        meta_args,
        shift_args,
        common_args,
        timeout,
        css_local,
        log_path=html_log,
        verbose=verbose,
        math_mode="webtex",
        embed_resources=html_embed_resources,
    )
    if verbose or rc != 0:
        print_pandoc_log(html_log, label="HTML Blocks")
    if rc != 0:
        die(f"Docker pandoc (HTML Blocks) failed (rc={rc})")

    blocks_html_path = _blocks_html_path(blocks_pandoc_md)
    shutil.copy2(out_html, blocks_html_path)
    if css_local:
        _inline_css(blocks_html_path, css_local)
    return blocks_html_path


def _is_fdn_md(src: Path) -> bool:
    return src.name.lower().endswith(".fdn.md")


def _pdf_extra_args(src: Path) -> list[str]:
    if not _is_fdn_md(src):
        return []
    return ["--pdf-engine=xelatex"]

def _print_wrote(items: list[tuple[str, Optional[Path]]]) -> None:
    for label, path in items:
        if path:
            print(f"✅ Wrote {label}: {path}")


def render(
    path: str | None = None,
    *,
    timeout: int = 0,
    omit_toc: bool = False,
    omit_numbering: bool = False,
    as_is: bool = False,
    make_pdf: bool = True,
    make_html: bool = True,
    make_epub: bool = False,
    toc_depth: int = 2,
    shift_headings: Optional[int] = None,
    auto_shift: bool = True,
    number_offset: Optional[str] = None,
    epub_chapter_level: Optional[int] = None,
    verbose: bool = False,
    html_math: str = "mathjax",
    html_embed_resources: bool = False,
    blocks: bool = False,
) -> tuple[Optional[Path], Optional[Path]]:
    """
    Main render entrypoint.

    Returns: (pdf_path or None, html_path or None)
    """
    effective_epub_level = epub_chapter_level
    if make_epub and effective_epub_level is None:
        effective_epub_level = 1
    epub_split_args: list[str] = []
    if make_epub and effective_epub_level is not None:
        epub_split_args = ["--split-level", str(effective_epub_level)]
    epub_extra_args = epub_split_args + (["--toc"] if make_epub else [])

    src = (Path(path) if path else discover_md_in_cwd()).expanduser()
    src = src.resolve(strict=False)
    if not src.exists():
        die(f"Missing source: {src}")

    # --- Book mode (YAML metadata) ---
    if src.suffix.lower() in (".yml", ".yaml"):
        pdf_path, html_path = render_book_yaml(
            src,
            timeout=timeout,
            omit_toc=omit_toc,
            omit_numbering=omit_numbering,
            make_pdf=make_pdf,
            make_html=make_html,
            make_epub=make_epub,
            toc_depth=toc_depth,
            shift_headings=shift_headings,
            auto_shift=auto_shift,
            number_offset=number_offset,
            epub_chapter_level=effective_epub_level,
            verbose=verbose,
            html_math=html_math,
            html_embed_resources=html_embed_resources,
        )
        if blocks:
            print("[WARN] --blocks is not supported for book mode.")
        return pdf_path, html_path

    # --- Normal (single .md) mode ---
    if as_is:
        from tempfile import mkdtemp

        tmpdir = Path(mkdtemp(prefix="pnpmd_"))
        in_tmp = tmpdir / "in.md"
        text = src.read_text(encoding="utf-8")
        if _is_fdn_md(src):
            text = replace_unicode_superscripts(text)
        in_tmp.write_text(text, encoding="utf-8")

        reader = "markdown+tex_math_dollars+raw_tex"
        if _is_fdn_md(src):
            reader += "+superscript"

        toc_flag: list[str] = [] if omit_toc else ["--toc"]
        numbering_flag: list[str] = [] if omit_numbering else ["--number-sections"]
        if number_offset is not None and not omit_numbering:
            numbering_flag += ["--number-offset", number_offset]

        toc_opts: list[str] = []
        if not omit_toc:
            toc_opts.append(f"--toc-depth={toc_depth}")

        shift_args: list[str] = []
        if shift_headings is not None:
            shift_args = ["--shift-heading-level-by", str(shift_headings)]

        common_args = toc_opts + numbering_flag + toc_flag + ["-f", reader]
        pdf_extra_args = _pdf_extra_args(src)

        pdf_path = src.with_suffix(".pdf") if make_pdf else None
        html_path = src.with_suffix(".html") if make_html else None
        epub_path = src.with_suffix(".epub") if make_epub else None

        blocks_pandoc_md: Optional[Path] = None
        blocks_html_path: Optional[Path] = None
        if blocks:
            blocks_pandoc_md = _blocks_pandoc_md_path(src)
            blocks_text = _inline_math_to_blocks_md(text)
            blocks_pandoc_md.write_text(blocks_text, encoding="utf-8")

        if make_pdf:
            out_pdf = tmpdir / "out.pdf"
            pdf_log = tmpdir / "pandoc-pdf.log.json"
            rc = render_pdf(
                in_tmp,
                out_pdf,
                [],
                shift_args,
                common_args,
                timeout,
                log_path=pdf_log,
                verbose=verbose,
                extra_args=pdf_extra_args,
            )
            if verbose or rc != 0:
                print_pandoc_log(pdf_log, label="PDF")
            if rc != 0:
                die(f"Docker pandoc (PDF) failed (rc={rc})")
            shutil.copy2(out_pdf, pdf_path)
            if not pdf_path.exists():
                die(f"Expected PDF output missing: {pdf_path}")

        if make_html:
            out_html = tmpdir / "out.html"
            html_log = tmpdir / "pandoc-html.log.json"
            rc = render_html(
                in_tmp,
                out_html,
                [],
                shift_args,
                common_args,
                timeout,
                log_path=html_log,
                verbose=verbose,
                math_mode=html_math,
                embed_resources=html_embed_resources,
            )
            if verbose or rc != 0:
                print_pandoc_log(html_log, label="HTML")
            if rc != 0:
                die(f"Docker pandoc (HTML) failed (rc={rc})")
            shutil.copy2(out_html, html_path)
            if not html_path.exists():
                die(f"Expected HTML output missing: {html_path}")
            if blocks and blocks_pandoc_md:
                blocks_html_path = _render_blocks_html(
                    blocks_pandoc_md,
                    meta_args=[],
                    shift_args=shift_args,
                    common_args=common_args,
                    timeout=timeout,
                    css_path=None,
                    verbose=verbose,
                    html_embed_resources=html_embed_resources,
                )

        if make_epub:
            out_epub = tmpdir / "out.epub"
            epub_log = tmpdir / "pandoc-epub.log.json"
            rc = render_epub(
                in_tmp,
                out_epub,
                [],
                shift_args,
                common_args,
                timeout,
                log_path=epub_log,
                verbose=verbose,
                extra_args=epub_extra_args,
            )
            if verbose or rc != 0:
                print_pandoc_log(epub_log, label="EPUB")
            if rc != 0:
                die(f"Docker pandoc (EPUB) failed (rc={rc})")
            shutil.copy2(out_epub, epub_path)
            if not epub_path.exists():
                die(f"Expected EPUB output missing: {epub_path}")

        _print_wrote(
            [
                ("PDF", pdf_path if make_pdf else None),
                ("HTML", html_path if make_html else None),
                ("Blocks Pandoc MD", blocks_pandoc_md if blocks else None),
                ("HTML Blocks", blocks_html_path if blocks else None),
                ("EPUB", epub_path if make_epub else None),
            ]
        )

        return (
            pdf_path.resolve() if pdf_path else None,
            html_path.resolve() if html_path else None,
        )

    # Preprocessed path
    (
        in_tmp,
        final_pandoc_md,
        meta_args,
        shift_args,
        common_args,
        css_path,
    ) = prepare_preprocessed(
        src,
        omit_toc=omit_toc,
        omit_numbering=omit_numbering,
        toc_depth=toc_depth,
        shift_headings=shift_headings,
        auto_shift=auto_shift,
        number_offset=number_offset,
        epub_chapter_level=effective_epub_level,
        include_css=False,
    )
    pdf_extra_args = _pdf_extra_args(src)

    pdf_path = src.with_suffix(".pdf") if make_pdf else None
    html_path = src.with_suffix(".html") if make_html else None
    epub_path = src.with_suffix(".epub") if make_epub else None
    blocks_pandoc_md: Optional[Path] = None
    blocks_html_path: Optional[Path] = None
    if blocks:
        blocks_pandoc_md = _blocks_pandoc_md_path(final_pandoc_md)
        blocks_src_text = final_pandoc_md.read_text(encoding="utf-8")
        blocks_pandoc_md.write_text(
            _inline_math_to_blocks_md(blocks_src_text), encoding="utf-8"
        )

    if make_pdf:
        out_pdf = in_tmp.parent / "out.pdf"
        pdf_log = in_tmp.parent / "pandoc-pdf.log.json"
        rc = render_pdf(
            in_tmp,
            out_pdf,
            meta_args,
            shift_args,
            common_args,
            timeout,
            log_path=pdf_log,
            verbose=verbose,
            extra_args=pdf_extra_args,
        )
        if verbose or rc != 0:
            print_pandoc_log(pdf_log, label="PDF")
        if rc != 0:
            die(f"Docker pandoc (PDF) failed (rc={rc})")
        shutil.copy2(out_pdf, pdf_path)
        if not pdf_path.exists():
            die(f"Expected PDF output missing: {pdf_path}")

    if make_html:
        out_html = in_tmp.parent / "out.html"
        html_log = in_tmp.parent / "pandoc-html.log.json"
        rc = render_html(
            in_tmp,
            out_html,
            meta_args,
            shift_args,
            common_args,
            timeout,
            css_path,
            log_path=html_log,
            verbose=verbose,
            math_mode=html_math,
            embed_resources=html_embed_resources,
        )
        if verbose or rc != 0:
            print_pandoc_log(html_log, label="HTML")
        if rc != 0:
            die(f"Docker pandoc (HTML) failed (rc={rc})")
        shutil.copy2(out_html, html_path)
        if not html_path.exists():
            die(f"Expected HTML output missing: {html_path}")
        _inline_css(html_path, css_path)
        if blocks and blocks_pandoc_md:
            blocks_html_path = _render_blocks_html(
                blocks_pandoc_md,
                meta_args=meta_args,
                shift_args=shift_args,
                common_args=common_args,
                timeout=timeout,
                css_path=css_path,
                verbose=verbose,
                html_embed_resources=html_embed_resources,
            )
        if css_path and css_path.exists():
            try:
                shutil.copy2(css_path, html_path.parent / css_path.name)
            except Exception:
                print(f"[WARN] could not copy CSS to {html_path.parent}")

    if make_epub:
        out_epub = in_tmp.parent / "out.epub"
        epub_log = in_tmp.parent / "pandoc-epub.log.json"
        rc = render_epub(
            in_tmp,
            out_epub,
            meta_args,
            shift_args,
            common_args,
            timeout,
            css_path,
            log_path=epub_log,
            verbose=verbose,
            extra_args=epub_extra_args,
        )
        if verbose or rc != 0:
            print_pandoc_log(epub_log, label="EPUB")
        if rc != 0:
            die(f"Docker pandoc (EPUB) failed (rc={rc})")
        shutil.copy2(out_epub, epub_path)
        if not epub_path.exists():
            die(f"Expected EPUB output missing: {epub_path}")

    _print_wrote(
        [
            ("PDF", pdf_path if make_pdf else None),
            ("HTML", html_path if make_html else None),
            ("Blocks Pandoc MD", blocks_pandoc_md if blocks else None),
            ("HTML Blocks", blocks_html_path if blocks else None),
            ("EPUB", epub_path if make_epub else None),
            ("Pandoc MD", final_pandoc_md),
        ]
    )

    return (
        pdf_path.resolve() if pdf_path else None,
        html_path.resolve() if html_path else None,
    )


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="PNPMD → PDF/HTML/EPUB (Pandoc + crossref; TOC after Keywords; spacing; link/anchor sugar)."
    )
    ap.add_argument(
        "file",
        nargs="?",
        help="Markdown or YAML (book) file; if omitted, exactly one .md in CWD is required.",
    )
    ap.add_argument(
        "--timeout", type=int, default=0, help="Timeout seconds (0=no timeout)."
    )
    ap.add_argument(
        "--omit-toc",
        action="store_true",
        help="Do not include a table of contents in the final outputs.",
    )
    ap.add_argument(
        "--omit-numbering",
        action="store_true",
        help="Disable section numbering in the final outputs.",
    )
    ap.add_argument(
        "--as-is",
        action="store_true",
        help="Bypass preprocessing and pass the original Markdown directly to Pandoc.",
    )
    ap.add_argument("--toc-depth", type=int, default=2, help="TOC depth for pandoc.")
    ap.add_argument(
        "--shift-headings",
        type=int,
        help="Explicit pandoc --shift-heading-level-by value (overrides auto in preprocessed mode).",
    )
    ap.add_argument(
        "--no-auto-shift",
        action="store_true",
        help="Disable automatic heading-level shifting in preprocessed mode.",
    )
    ap.add_argument(
        "--number-offset",
        type=str,
        help="Value for pandoc --number-offset (e.g. '0', '1', '1.2').",
    )
    ap.add_argument(
        "--epub-chapter-level",
        type=int,
        help="Heading level for EPUB splitting (pandoc --split-level, default 1); also enables pandoc TOC for EPUB.",
    )
    ap.add_argument(
        "--verbose",
        action="store_true",
        help="Print pandoc logs (and extra pandoc verbosity) to help debug failures.",
    )
    ap.add_argument(
        "--html-math",
        choices=["mathjax", "webtex", "mathml", "katex"],
        default="mathjax",
        help="Math rendering mode for HTML output.",
    )
    ap.add_argument(
        "--html-embed-resources",
        action="store_true",
        help="Embed external resources into HTML (useful with --html-math=webtex).",
    )
    ap.add_argument(
        "--math-images",
        action="store_true",
        help="Render HTML math as images and embed resources (alias for --html-math=webtex --html-embed-resources).",
    )
    ap.add_argument(
        "--blocks",
        action="store_true",
        help="Also write .blocks.pandoc.md and .blocks.html with inline math rewritten as $$...$$.",
    )

    g = ap.add_mutually_exclusive_group()
    g.add_argument("--pdf", action="store_true", help="Render PDF only.")
    g.add_argument("--html", action="store_true", help="Render HTML only.")
    ap.add_argument(
        "--epub",
        action="store_true",
        help="Also render EPUB in addition to PDF/HTML selection.",
    )
    g.add_argument(
        "--all", action="store_true", help="Render both PDF and HTML (default)."
    )

    args = ap.parse_args(argv)

    try:
        make_pdf = args.pdf or args.all
        make_html = args.html or args.all
        make_epub = args.epub

        html_math = args.html_math
        html_embed_resources = args.html_embed_resources
        if args.math_images:
            html_math = "webtex"
            html_embed_resources = True

        render(
            args.file,
            timeout=args.timeout,
            omit_toc=args.omit_toc,
            omit_numbering=args.omit_numbering,
            as_is=args.as_is,
            make_pdf=make_pdf,
            make_html=make_html,
            make_epub=make_epub,
            toc_depth=args.toc_depth,
            shift_headings=args.shift_headings,
            auto_shift=not args.no_auto_shift,
            number_offset=args.number_offset,
            epub_chapter_level=args.epub_chapter_level,
            verbose=args.verbose,
            html_math=html_math,
            html_embed_resources=html_embed_resources,
            blocks=args.blocks,
        )
    except SystemExit:
        raise
    except Exception as e:
        die(str(e))


if __name__ == "__main__":
    main()
