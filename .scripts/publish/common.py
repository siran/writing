# .scripts/common.py
import sys
import subprocess
from pathlib import Path
from datetime import date
from typing import List, Optional


def echo(msg: str):
    print(msg, flush=True)


def die(msg: str, code: int = 1):
    echo(f"ERROR: {msg}")
    sys.exit(code)


def run(cmd: List[str], cwd: Optional[Path] = None, check: bool = True) -> str:
    echo("+ " + " ".join(str(x) for x in cmd))
    p = subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    out = p.stdout
    if out:
        print(out, end="" if out.endswith("\n") else "\n")
    print()
    if check and p.returncode != 0:
        die(f"command failed with exit code {p.returncode}", p.returncode)
    return out


def format_long_date(d: date | str) -> str:
    """Return 'January 25, 2025'. Accepts date or ISO 'YYYY-MM-DD'."""
    if isinstance(d, str):
        d = date.fromisoformat(d)
    try:
        return d.strftime("%B %-d, %Y")
    except ValueError:
        # Windows
        return d.strftime("%B %#d, %Y")
