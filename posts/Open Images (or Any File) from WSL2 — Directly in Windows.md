---
title: Open Images (or Any File) from WSL2 — Directly in Windows
subtitle: A small shell function to open files from WSL2 using native Windows apps
author: An M. Rodriguez
date: 2026-01-27
one-sentence-summary: Open images and any other files from the WSL2 terminal directly in their native Windows applications.
summary: >
  Working in WSL2 often breaks simple workflows like opening images or PDFs from the terminal.
  This article presents a minimal, reliable shell function that opens any file from WSL2
  using the default Windows application, avoiding common issues with explorer.exe,
  UNC paths, and fragile aliases.
keywords:
  - WSL2
  - Windows Subsystem for Linux
  - zsh
  - bash
  - Windows
  - productivity
  - developer tools
DOI:
---

![Opening a file from the WSL2 terminal using winopen, launching the native Windows viewer](https://siran.github.io/assets/writing/open-files-from-wsl2-terminal.png)


WSL2 is fantastic.

But the moment you try to open an image from the terminal, everything falls
apart.

You try:

```bash

explorer.exe image.png

```

Nothing happens. Or Explorer opens the wrong folder. Or Windows throws a cryptic
UNC-path error.

Let’s fix this **properly** — with one small, reliable function.


## TL;DR

To open **any file** from WSL2 in its *native* Windows app, add one small shell
function to your config file.

⚠️ **Limitation:** works on **real paths only** (no symbolic links).


## Quick Setup (60 seconds)

1. Open your shell config file:

   * ZSH → `~/.zshrc`
   * Bash → `~/.bashrc`

2. Paste this function:

```sh

winopen() { cmd.exe /c 'cd /d C:\ && start "" "'"$(wslpath -w "$1")"'"' }

```

3. Reload your shell:

```bash

source ~/.zshrc   # or: source ~/.bashrc

```

4. Open any file:

```bash

winopen image.png

```

Done.


## ZSH (manual)

Edit your config file:

```bash

vim ~/.zshrc

```

Add this one-liner anywhere:

```zsh

winopen() { cmd.exe /c 'cd /d C:\ && start "" "'"$(wslpath -w "$1")"'"' }

```


## Bash

The same function works in Bash.

Add it to `~/.bashrc`:

```bash

winopen() { cmd.exe /c 'cd /d C:\ && start "" "'"$(wslpath -w "$1")"'"' }

```


## macOS, Linux, BSD (for reference)

On Unix-like systems with a GUI, the equivalent is trivial:

```bash

open file.png        # macOS xdg-open file.png    # Linux desktop

```

WSL2 is special because it crosses OS boundaries.


## Use It

Reload your shell:

```bash

source ~/.zshrc   # or: source ~/.bashrc

```

Then:

```bash

winopen image.png
winopen file.pdf
winopen video.mp4

```

It opens instantly using the default Windows viewer.


## The Problem (What’s Actually Going On)

WSL2 runs Linux in a VM. That means:

* Your files live in a Linux filesystem
* Windows apps expect Windows paths
* `explorer.exe` is a **file manager**, not a file opener
* Windows apps often break when launched from UNC paths like
  `\\wsl.localhost\Ubuntu-22.04\...`

So even when a command *looks* correct, it often fails silently.

This is not user error. It’s impedance mismatch.


## Why `explorer.exe` Is the Wrong Tool

* `explorer.exe` opens folders, not files
* It does **not** reliably invoke file associations
* It behaves inconsistently from WSL
* It often opens Explorer instead of the viewer

That’s why images don’t open in Photos / Preview.


## The Correct Tool: `cmd.exe start`

On Windows, the canonical way to open a file with its default app is:

```cmd

start "" file.ext

```

This invokes **ShellExecute**, which respects file associations.

From WSL, two extra problems appear:

1. Windows inherits a **UNC working directory**
2. `start` has extremely fragile argument parsing

The function fixes both.


## Why This Works (No Hand-Waving)

* `wslpath -w` converts Linux paths to real Windows paths
* `cmd.exe /c start` invokes Windows file associations
* `cd /d C:\` avoids Windows failing on UNC working directories
* The empty `""` is required by `start` (window title)
* A **function**, not an alias, handles arguments correctly

This avoids every common WSL ↔ Windows failure mode.


## Can This Be an Alias?

Short answer: **don’t**.

Aliases:

* are text substitution
* don’t handle arguments safely
* break with nested quoting
* fail silently

Functions are the correct tool.

If you want muscle memory:

```bash

alias o=winopen

```

⚠️ Double-edged sword — `o *` will try to open *everything* 💣💥


## What Can It Open?

Anything Windows knows how to open:

* Images
* PDFs
* Videos
* Text files
* Archives
* Custom file types

No special cases.


## Final Thoughts

This function is tiny.

But it removes a constant friction point when working in WSL2: previewing
images, checking PDFs, opening generated files.

One command. Any file. Native Windows apps.

Honestly, this one made me smile when it finally clicked — fewer hacks, less
friction, and a smoother dev loop always feels good 😊

---

![ ](https://siran.github.io/assets/writing/100-vc.png)


*✅ 100% vibe-code certified 💯*

DOI:
