# pnpmd_pandoc.py

import os
import time
from pathlib import Path
from typing import List, Optional

from pnpmd_util import run_visible


_PANDOC_IMAGE = os.environ.get("PNPMD_PANDOC_IMAGE", "pandoc/extra:3.1")
_MATHJAX_URL = os.environ.get(
    "PNPMD_MATHJAX_URL",
    "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js",
)
_WEBTEX_URL = os.environ.get("PNPMD_WEBTEX_URL", "")
_IMAGE_READY = False


def _ensure_image(image: str, retries: int = 2, delay: float = 2.0) -> int:
    """
    Pre-pull the docker image with a couple of retries so transient registry
    errors don't abort the run.
    """
    global _IMAGE_READY
    if _IMAGE_READY:
        return 0
    last_rc = 0
    for attempt in range(retries + 1):
        last_rc = run_visible(["docker", "pull", image])
        if last_rc == 0:
            _IMAGE_READY = True
            return 0
        time.sleep(delay * (attempt + 1))
    return last_rc


def render_pdf(
    in_tmp: Path,
    out_tmp: Path,
    meta_args: List[str],
    shift_args: List[str],
    common_args: List[str],
    timeout: int,
    log_path: Optional[Path] = None,
    verbose: bool = False,
    extra_args: Optional[List[str]] = None,
) -> int:
    log_args: List[str] = [f"--log={log_path.name}"] if log_path else []
    verbose_args: List[str] = ["--verbose"] if verbose else []
    extra_args = extra_args or []
    header_args: List[str] = []
    try:
        numbering_header = in_tmp.parent / "section-numbering.tex"
        numbering_header.write_text(
            (
                "\\usepackage{titling}\n"
                "\\makeatletter\n"
                "\\renewcommand{\\@seccntformat}[1]{\\csname the#1\\endcsname.\\quad}\n"
                "\\renewcommand{\\numberline}[1]{#1.\\hspace{0.6em}}\n"
                "\\@ifundefined{subtitle}{\n"
                "  \\newcommand{\\subtitle}[1]{%\n"
                "    \\posttitle{%\n"
                "      \\par\\end{center}\n"
                "      \\vspace{1.0\\baselineskip}\n"
                "      \\begin{center}\\large#1\\end{center}\n"
                "      \\vskip0.5em}%\n"
                "  }\n"
                "}{\n"
                "  \\renewcommand{\\subtitle}[1]{%\n"
                "    \\posttitle{%\n"
                "      \\par\\end{center}\n"
                "      \\vspace{1.0\\baselineskip}\n"
                "      \\begin{center}\\large#1\\end{center}\n"
                "      \\vskip0.5em}%\n"
                "  }\n"
                "}\n"
                "\\makeatother\n"
            ),
            encoding="utf-8",
        )
        header_args = ["--include-in-header", numbering_header.name]
    except Exception:
        header_args = []

    rc = _ensure_image(_PANDOC_IMAGE)
    if rc != 0:
        return rc

    cmd = [
        "docker",
        "run",
        "--rm",
        "--mount",
        f"type=bind,source={str(in_tmp.parent)},target=/data",
        "-w",
        "/data",
        _PANDOC_IMAGE,
        "--standalone",
        *log_args,
        *verbose_args,
        *extra_args,
        *common_args,
        *shift_args,
        *meta_args,
        *header_args,
        "--filter",
        "pandoc-crossref",
        "in.md",
        "-o",
        out_tmp.name,
    ]
    return run_visible(cmd, timeout=timeout)


def render_html(
    in_tmp: Path,
    out_tmp: Path,
    meta_args: List[str],
    shift_args: List[str],
    common_args: List[str],
    timeout: int,
    css_path: Optional[Path] = None,
    log_path: Optional[Path] = None,
    verbose: bool = False,
    *,
    math_mode: str = "mathjax",
    embed_resources: bool = False,
    webtex_url: Optional[str] = None,
) -> int:
    css_args: List[str] = []
    if css_path and css_path.exists():
        css_args = ["--css", css_path.name]
    header_args: List[str] = []
    try:
        numbering_header = in_tmp.parent / "section-numbering.html"
        numbering_header.write_text(
            (
                "<style>\n"
                ".header-section-number::after,\n"
                ".toc-section-number::after {\n"
                "  content: \". \";\n"
                "}\n"
                ".toc ul {\n"
                "  list-style: none;\n"
                "  padding-left: 0;\n"
                "  margin-left: 0;\n"
                "  counter-reset: item;\n"
                "}\n"
                ".toc li {\n"
                "  margin: 0.4em 0;\n"
                "  padding-left: 2.6em;\n"
                "  position: relative;\n"
                "  counter-increment: item;\n"
                "}\n"
                ".toc li::before {\n"
                "  content: counters(item, \".\") \".\";\n"
                "  position: absolute;\n"
                "  left: 0;\n"
                "  color: #666;\n"
                "  width: 2.2em;\n"
                "  text-align: right;\n"
                "}\n"
                ".toc-title {\n"
                "  display: block;\n"
                "  font-weight: 700;\n"
                "  font-size: 1.1em;\n"
                "  margin: 0.5em 0 0.4em;\n"
                "  text-align: center;\n"
                "}\n"
                ".toc-divider {\n"
                "  width: 35%;\n"
                "  margin: 3.2em auto 2.8em;\n"
                "  border: 0;\n"
                "  height: 1px;\n"
                "  background: rgba(0,0,0,0.25);\n"
                "}\n"
                ".toc a {\n"
                "  text-decoration: none;\n"
                "  color: inherit;\n"
                "  border-bottom: 1px solid transparent;\n"
                "}\n"
                ".toc a:hover {\n"
                "  border-bottom-color: #1f5fbf;\n"
                "}\n"
                ".heading-anchor {\n"
                "  margin-left: 0.35em;\n"
                "  text-decoration: none;\n"
                "  opacity: 0;\n"
                "  font-size: 0.85em;\n"
                "  color: inherit;\n"
                "  transition: opacity 0.15s ease;\n"
                "}\n"
                ".heading-anchor::after {\n"
                "  content: \"\\1F517\";\n"
                "}\n"
                "h1:hover .heading-anchor,\n"
                "h2:hover .heading-anchor,\n"
                "h3:hover .heading-anchor,\n"
                "h4:hover .heading-anchor,\n"
                "h5:hover .heading-anchor,\n"
                "h6:hover .heading-anchor,\n"
                ".heading-anchor:focus {\n"
                "  opacity: 1;\n"
                "}\n"
                ".heading-anchor:hover {\n"
                "  text-decoration: none;\n"
                "}\n"
                "</style>\n"
                "<script>\n"
                "(function () {\n"
                "  function slugify(text) {\n"
                "    return (text || \"\")\n"
                "      .toLowerCase()\n"
                "      .replace(/[^0-9a-zA-Z _-]+/g, \"\")\n"
                "      .trim()\n"
                "      .replace(/\\s+/g, \"-\")\n"
                "      .replace(/-+/g, \"-\")\n"
                "      .replace(/^-+|-+$/g, \"\") || \"section\";\n"
                "  }\n"
                "  function headingText(el) {\n"
                "    var clone = el.cloneNode(true);\n"
                "    var drop = clone.querySelectorAll(\".heading-anchor, .header-section-number\");\n"
                "    for (var i = 0; i < drop.length; i++) {\n"
                "      if (drop[i].parentNode) {\n"
                "        drop[i].parentNode.removeChild(drop[i]);\n"
                "      }\n"
                "    }\n"
                "    return (clone.textContent || \"\").trim();\n"
                "  }\n"
                "  function ensureId(el, used) {\n"
                "    var id = el.getAttribute(\"id\") || \"\";\n"
                "    if (id) {\n"
                "      used[id] = true;\n"
                "      return id;\n"
                "    }\n"
                "    var base = slugify(headingText(el));\n"
                "    var cand = base;\n"
                "    var i = 1;\n"
                "    while (!cand || document.getElementById(cand) || used[cand]) {\n"
                "      cand = base + \"-\" + i;\n"
                "      i += 1;\n"
                "    }\n"
                "    el.setAttribute(\"id\", cand);\n"
                "    used[cand] = true;\n"
                "    return cand;\n"
                "  }\n"
                "  function addAnchors(root) {\n"
                "    if (!root) {\n"
                "      return;\n"
                "    }\n"
                "    var headings = root.querySelectorAll(\"h1, h2, h3, h4, h5, h6\");\n"
                "    var used = {};\n"
                "    for (var i = 0; i < headings.length; i++) {\n"
                "      var h = headings[i];\n"
                "      if (h.querySelector(\"a.heading-anchor\")) {\n"
                "        continue;\n"
                "      }\n"
                "      var id = ensureId(h, used);\n"
                "      var a = document.createElement(\"a\");\n"
                "      a.className = \"heading-anchor\";\n"
                "      a.href = \"#\" + id;\n"
                "      a.setAttribute(\"aria-label\", \"Link to this section\");\n"
                "      a.setAttribute(\"title\", \"Link to this section\");\n"
                "      h.appendChild(a);\n"
                "    }\n"
                "  }\n"
                "  function run() {\n"
                "    addAnchors(document.body);\n"
                "  }\n"
                "  if (document.readyState === \"loading\") {\n"
                "    document.addEventListener(\"DOMContentLoaded\", run);\n"
                "  } else {\n"
                "    run();\n"
                "  }\n"
                "})();\n"
                "</script>\n"
            ),
            encoding="utf-8",
        )
        header_args = ["--include-in-header", numbering_header.name]
    except Exception:
        header_args = []
    math_args: List[str] = []
    mode = (math_mode or "mathjax").strip().lower()
    if mode == "mathjax":
        if _MATHJAX_URL:
            header_path = in_tmp.parent / "mathjax-config.html"
            header_path.write_text(
                (
                    "<script>\n"
                    "window.MathJax = {\n"
                    "  tex: {\n"
                    "    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],\n"
                    "    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]\n"
                    "  },\n"
                    "  options: {\n"
                    "    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']\n"
                    "  },\n"
                    "  svg: {\n"
                    "    fontCache: 'global'\n"
                    "  }\n"
                    "};\n"
                    "</script>\n"
                ),
                encoding="utf-8",
            )
            math_args = [
                "--include-in-header",
                header_path.name,
                f"--mathjax={_MATHJAX_URL}",
            ]
    elif mode == "webtex":
        url = webtex_url or _WEBTEX_URL
        if url:
            math_args = [f"--webtex={url}"]
        else:
            math_args = ["--webtex"]
    elif mode == "mathml":
        math_args = ["--mathml"]
    elif mode == "katex":
        math_args = ["--katex"]
    log_args: List[str] = [f"--log={log_path.name}"] if log_path else []
    verbose_args: List[str] = ["--verbose"] if verbose else []
    embed_args: List[str] = ["--embed-resources"] if embed_resources else []

    rc = _ensure_image(_PANDOC_IMAGE)
    if rc != 0:
        return rc

    cmd = [
        "docker",
        "run",
        "--rm",
        "--mount",
        f"type=bind,source={str(in_tmp.parent)},target=/data",
        "-w",
        "/data",
        _PANDOC_IMAGE,
        "--standalone",
        *log_args,
        *verbose_args,
        *embed_args,
        *common_args,
        *shift_args,
        *meta_args,
        *css_args,
        *header_args,
        *math_args,
        "--filter",
        "pandoc-crossref",
        "in.md",
        "-t",
        "html5",
        "-o",
        out_tmp.name,
    ]
    return run_visible(cmd, timeout=timeout)


def render_epub(
    in_tmp: Path,
    out_tmp: Path,
    meta_args: List[str],
    shift_args: List[str],
    common_args: List[str],
    timeout: int,
    css_path: Optional[Path] = None,
    extra_args: Optional[List[str]] = None,
    log_path: Optional[Path] = None,
    verbose: bool = False,
) -> int:
    css_args: List[str] = []
    if css_path and css_path.exists():
        css_args = ["--css", css_path.name]
    extra_css_args: List[str] = []
    try:
        numbering_css = in_tmp.parent / "section-numbering.css"
        numbering_css.write_text(
            (
                ".header-section-number::after,\n"
                ".toc-section-number::after {\n"
                "  content: \". \";\n"
                "}\n"
            ),
            encoding="utf-8",
        )
        extra_css_args = ["--css", numbering_css.name]
    except Exception:
        extra_css_args = []
    extra_args = extra_args or []
    log_args: List[str] = [f"--log={log_path.name}"] if log_path else []
    verbose_args: List[str] = ["--verbose"] if verbose else []

    rc = _ensure_image(_PANDOC_IMAGE)
    if rc != 0:
        return rc

    cmd = [
        "docker",
        "run",
        "--rm",
        "--mount",
        f"type=bind,source={str(in_tmp.parent)},target=/data",
        "-w",
        "/data",
        _PANDOC_IMAGE,
        "--standalone",
        *log_args,
        *verbose_args,
        *common_args,
        *shift_args,
        *meta_args,
        *css_args,
        *extra_css_args,
        *extra_args,
        "--filter",
        "pandoc-crossref",
        "in.md",
        "-t",
        "epub3",
        "-o",
        out_tmp.name,
    ]
    return run_visible(cmd, timeout=timeout)
