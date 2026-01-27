---
title: Open Images (or Any File) from WSL2 — Directly in Windows
subtitle: A small shell function to open files from WSL2 using native Windows apps
author: an
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

Open **any file** from WSL2 in its **native Windows app**.

```zsh
winopen() {
  cmd.exe /c 'cd /d C:\ && start "" "'"$(wslpath -w "$1")"'"'
}
```

Reload your shell, then:

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

Many guides suggest:

```bash
explorer.exe .
explorer.exe image.png
```

But:

* `explorer.exe` opens folders, not files
* It does **not** reliably invoke file associations
* It behaves inconsistently from WSL
* It often opens Explorer instead of the viewer

That’s why images don’t open in Preview / Photos.


## The Correct Tool: `cmd.exe start`

On Windows, the canonical way to open a file with its default app is:

```cmd
start "" file.ext
```

This invokes **ShellExecute**, which respects file associations.

But from WSL, there are two extra problems:

1. Windows inherits a **UNC working directory** from WSL
2. `start` has extremely fragile argument parsing

We must fix both.


## The Solution: One Small Function

Add this to your `.zshrc` or aliases file:

```zsh
winopen() {
  cmd.exe /c 'cd /d C:\ && start "" "'"$(wslpath -w "$1")"'"'
}
```

Reload:

```bash
source ~/.zshrc
```

Use it:

```bash
winopen screenshot.png
winopen report.pdf
winopen video.mp4
winopen notes.txt
```


## Why This Works (No Hand-Waving)

Fact by fact:

* `wslpath -w` converts Linux paths to real Windows paths
* `cmd.exe /c start` invokes Windows file associations
* `cd /d C:\` avoids Windows choking on UNC paths
* The empty `""` is required by `start` (window title)
* A **function**, not an alias, handles arguments correctly

This avoids every common WSL ↔ Windows failure mode.


## Can This Be an Alias?

Short answer: **don’t do it**.

Aliases:

* are text substitution
* don’t handle `$1` safely
* break with nested quoting
* fail silently across shells

Functions are the correct tool here.

If you want muscle memory:

```bash
alias o=winopen
```

Then:

```bash
o image.png
```


## What Can It Open?

Anything Windows knows how to open:

* Images → Photos / Preview
* PDFs → Browser / PDF viewer
* Videos → Media Player
* Text → Default editor
* Archives → Explorer
* Custom file types → Your associated app

No special cases.


## Final Thoughts

This function is small.

But it removes a constant friction point when working in WSL2: previewing
images, checking PDFs, opening generated files.

One command. Any file. Native Windows apps.

That’s how it should have worked from the start.

If you want:

* a Bash version
* auto-completion
* a PowerShell equivalent
* or a tiny GitHub utility

Just say the word.
