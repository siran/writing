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
) -> int:
    css_args: List[str] = []
    if css_path and css_path.exists():
        css_args = ["--css", css_path.name]
    mathjax_args: List[str] = []
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
        mathjax_args = [
            "--include-in-header",
            header_path.name,
            f"--mathjax={_MATHJAX_URL}",
        ]
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
        *mathjax_args,
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
