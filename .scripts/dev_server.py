#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import subprocess
import sys
import threading
import time
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE = ROOT / "site"
WATCH_DIRS = [
    ROOT / ".scripts",
    ROOT / "books",
    ROOT / "documents",
    ROOT / "posts",
    ROOT / "prints",
    ROOT / "reports",
]
WATCH_FILES = [
    ROOT / "Makefile",
    ROOT / "CNAME",
    ROOT / "pnpmd.map",
    ROOT / "requirements.txt",
]
WATCH_SUFFIXES = {
    ".css",
    ".html",
    ".htm",
    ".map",
    ".markdown",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}
# Dotfiles that act as build-control markers (no extension in pathlib terms).
WATCH_DOTFILES = {".pdf"}
SKIP_DIRS = {
    ".git",
    ".pnpmd",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "env",
    "node_modules",
    "site",
    "venv",
}


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


def _iter_watch_files() -> list[Path]:
    paths: list[Path] = []
    for file_path in WATCH_FILES:
        if file_path.exists():
            paths.append(file_path)
    for root_dir in WATCH_DIRS:
        if not root_dir.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root_dir):
            dirnames[:] = [
                name for name in dirnames
                if name not in SKIP_DIRS and not name.startswith(".")
            ]
            base = Path(dirpath)
            for name in filenames:
                path = base / name
                if name in WATCH_DOTFILES or path.suffix.lower() in WATCH_SUFFIXES:
                    paths.append(path)
    return paths


def _snapshot() -> dict[str, tuple[int, int]]:
    snap: dict[str, tuple[int, int]] = {}
    for path in _iter_watch_files():
        try:
            stat = path.stat()
        except OSError:
            continue
        snap[str(path)] = (
            getattr(stat, "st_mtime_ns", int(stat.st_mtime * 1_000_000_000)),
            stat.st_size,
        )
    return snap


def _run_build(command: list[str]) -> bool:
    print("+", " ".join(command), flush=True)
    proc = subprocess.run(command, cwd=ROOT)
    return proc.returncode == 0


def _watch_loop(command: list[str], interval: float) -> None:
    previous = _snapshot()
    while True:
        time.sleep(interval)
        current = _snapshot()
        if current == previous:
            continue
        previous = current
        print("[watch] change detected; rebuilding...", flush=True)
        ok = _run_build(command)
        print("[watch] build ok" if ok else "[watch] build failed", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description="Static dev server with no-cache headers.")
    ap.add_argument("--root", default=str(DEFAULT_SITE), help="Directory to serve.")
    ap.add_argument("--port", type=int, default=8000, help="Port to serve on.")
    ap.add_argument("--watch", action="store_true", help="Rebuild when source files change.")
    ap.add_argument("--interval", type=float, default=1.0, help="Watch poll interval in seconds.")
    ap.add_argument(
        "--build-mode",
        choices=("fast", "books", "full"),
        default="fast",
        help="Build mode to use with --watch.",
    )
    args = ap.parse_args()

    site_root = Path(args.root).resolve()
    if not site_root.exists():
        site_root.mkdir(parents=True, exist_ok=True)

    build_command = [
        sys.executable,
        str(ROOT / ".scripts" / "build_site" / "build_site.py"),
    ]
    if args.build_mode in {"fast", "books"}:
        build_command.extend(["--skip-pdf", "--skip-epub"])
    else:
        pass

    if args.watch:
        watcher = threading.Thread(
            target=_watch_loop,
            args=(build_command, args.interval),
            daemon=True,
        )
        watcher.start()

    handler = partial(NoCacheHandler, directory=str(site_root))
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    print(f"[serve] http://127.0.0.1:{args.port} -> {site_root}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        return 0
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
