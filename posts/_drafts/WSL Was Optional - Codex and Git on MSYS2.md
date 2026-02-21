---
title: "WSL Was Optional: Codex and Git on MSYS2"
description: "A practical migration note: keep GNU workflows on Windows with MSYS2, and run Codex + Git without needing WSL."
one-sentence-summary: If your day-to-day workflow is Windows-first, you can run Codex and Git with MSYS2 Bash aliases and skip WSL.
summary: >
  This note documents a real migration from WSL habits to an MSYS2-first setup.
  The key point is simple: Codex command execution on Windows is often PowerShell
  by default, so Bash aliases fail unless you explicitly invoke MSYS2 Bash.
  Once commands are run through `bash -lic` and `~/.bashrc` is sourced,
  Git aliases such as `gst` work normally, and the workflow remains native.
keywords:
  - Codex
  - MSYS2
  - WSL
  - Git
  - Bash aliases
  - Windows
tags: [windows, msys2, codex, git, bash, wsl]
published: false
date: 2026-02-21
---

## TL;DR

WSL is useful, but not mandatory for a GNU-like workflow on Windows.

If your work is Windows-first, this is enough:

- MSYS2 installed (`C:\msys64`)
- Git + GNU tools in Bash
- Codex commands explicitly executed via MSYS2 Bash

The reliable pattern is:

```powershell
C:\msys64\usr\bin\bash.exe -lic 'source ~/.bashrc; gst'
```

## What Actually Happened

I kept trying commands like:

```powershell
gst
source ~/.bashrc
```

and got errors.

The reason was not "Git is broken" and not "aliases are wrong."
The reason was shell mismatch:

- Codex was executing in PowerShell
- `gst` and `source` were Bash-level aliases/builtins

So PowerShell could not resolve them.

## The Fix

Run the command in MSYS2 Bash directly, and source your shell config in that same invocation:

```powershell
C:\msys64\usr\bin\bash.exe -lic 'source ~/.bashrc; gst'
```

This works because:

- `-l` starts a login shell
- `-i` enables interactive behavior (alias expansion)
- `-c` runs the command string
- `source ~/.bashrc` loads fresh aliases before running `gst`

You may see:

```text
bash: cannot set terminal process group (-1): Inappropriate ioctl for device
bash: no job control in this shell
```

That warning is normal in non-interactive command runners and does not prevent alias execution.

## Why This Is Good Enough for Many Workflows

If you are not targeting Linux ABI behavior, Linux containers, or Linux-only runtime semantics, WSL may be extra complexity:

- extra boundary layer
- cross-filesystem path friction
- occasional shell-context confusion

MSYS2 keeps everything native to Windows while preserving GNU ergonomics.

## Practical Setup Pattern

I now keep aliases in a dedicated include file and source it from `~/.bashrc`:

```bash
# ~/.bashrc
if [ -f "$HOME/.bash_aliases_git_plugin.sh" ]; then
  . "$HOME/.bash_aliases_git_plugin.sh"
fi
```

Then Codex commands can use:

```powershell
!C:\msys64\usr\bin\bash.exe -lic 'source ~/.bashrc; gst'
!C:\msys64\usr\bin\bash.exe -lic 'source ~/.bashrc; gapa'
!C:\msys64\usr\bin\bash.exe -lic 'source ~/.bashrc; grst'
```

## Important Clarification

If Codex is running with PowerShell as its default session shell, `!command` runs in PowerShell by default.

So this:

```powershell
!gst
```

will fail unless `gst` is a real Windows command on PATH.

This:

```powershell
!C:\msys64\usr\bin\bash.exe -lic 'source ~/.bashrc; gst'
```

is the explicit cross-shell bridge.

## Final Note

WSL is still excellent. This is not anti-WSL.
This is just a practical decision:

"I wanted GNU tools, not a Linux VM boundary in daily flow."

For that goal, MSYS2 plus explicit Bash invocation in Codex was enough.
