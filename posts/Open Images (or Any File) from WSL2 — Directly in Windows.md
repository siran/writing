---
title: Open Images (or Any File) from WSL2 — Directly in Windows
subtitle: A small shell function to open files from WSL2 using native Windows apps
author: An M. Rodriguez
date: 2026-01-27
one-sentence-summary: Open images and any other files from the WSL2 terminal directly in their native Windows applications.
summary: >
  Working in WSL2 often breaks simple workflows like opening images or PDFs from the terminal.
  This article presents a minimal, reliable shell function that opens any file from WSL2
  using Windows Explorer, avoiding common issues with UNC paths
  and unreliable direct application launches.
keywords:
  - WSL2
  - Windows Subsystem for Linux
  - zsh
  - bash
  - Windows
  - productivity
  - developer tools
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

To open **any file** from WSL2 in its Windows environment, add one small shell
function to your config file.

⚠️ **Limitation:** this works on **real paths only** (no symbolic links).


## Quick Setup (60 seconds)

1. Open your shell config file:

   * ZSH → `~/.zshrc`
   * Bash → `~/.bashrc`

2. Paste this function:

```sh
winopen() {
  explorer.exe "$(wslpath -w "$(realpath "$1")")"
}
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
winopen() {
  explorer.exe "$(wslpath -w "$(realpath "$1")")"
}
```


## Bash

The same function works in Bash.

Add it to `~/.bashrc`:

```bash
winopen() {
  explorer.exe "$(wslpath -w "$(realpath "$1")")"
}
```


## macOS, Linux, BSD (for reference)

On Unix-like systems with a GUI, the equivalent is trivial:

```bash
open file.png        # macOS
xdg-open file.png    # Linux desktop
```

WSL2 is special because it crosses OS boundaries.


## Use It

Reload your shell:

```bash
source ~/.zshrc   # or source ~/.bashrc
```

Then:

```bash
winopen image.png
winopen file.pdf
winopen video.mp4
```

Windows Explorer opens at the correct location.

Select the file. Hit **Enter**.

The file opens using the default Windows application.


## The Problem (What’s Actually Going On)

WSL2 runs Linux in a VM. That means:

* Your files live in a Linux filesystem
* Windows apps expect Windows paths
* Windows sees WSL files as UNC paths like
  `\\wsl.localhost\Ubuntu-22.04\home\username\...`
* Many Windows applications handle UNC paths inconsistently

So even when a command *looks* correct, it often fails silently.

This is not user error. It’s impedance mismatch.


## Why Explorer Is the Right Tool

Windows Explorer:

* Fully supports UNC paths
* Is designed to browse network locations
* Reliably dispatches files via default associations
* Does not suffer from viewer-specific UNC bugs

Explorer is the stable bridge between WSL and Windows.


## The Correct Mental Model

WSL–Windows integration has multiple layers:

| Goal                    | Tool             | Reliability |
| ----------------------- | ---------------- | ----------- |
| Browse WSL files        | Windows Explorer | ✅ Always    |
| Open via Enter          | Explorer         | ✅ Always    |
| Open directly in app    | App-dependent    | ⚠️          |
| Guaranteed native paths | `/mnt/c`         | ✅           |

Once you use the right layer, the problem disappears.


## Recommendation

* Use **Explorer** for anything under `/home/...`
* Let Explorer handle UNC paths
* Hit **Enter** to open files
* Store files on `/mnt/c` only if you need guaranteed direct app
  launches

Simple. Honest. Reliable.


## Final Thoughts

This function is tiny.

But it removes a constant friction point when working in WSL2: previewing
images, checking PDFs, opening generated files.

One command. Any file. Native Windows apps.

Honestly, this one made me smile when it finally clicked — fewer hacks, less
friction, and a smoother dev loop always feels good 😊

* * *

![ ](https://siran.github.io/assets/writing/100pc-vibe-coded.png)


*✅ 100% vibe-code certified 💯*

DOI:
