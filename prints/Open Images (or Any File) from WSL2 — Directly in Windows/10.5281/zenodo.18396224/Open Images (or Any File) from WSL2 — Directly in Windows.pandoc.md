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
DOI: https://writing.preferredframe.com/doi/10.5281/zenodo.18396224
---

**One-Sentence Summary.** Open images and any other files from the WSL2 terminal directly in their native Windows applications.

**Abstract.** Working in WSL2 often breaks simple workflows like opening images or PDFs from the terminal. This article presents a minimal, reliable shell function that opens any file from WSL2 using Windows Explorer, avoiding common issues with UNC paths and unreliable direct application launches.

**Keywords.** WSL2, Windows Subsystem for Linux, zsh, bash, Windows, productivity, developer tools

\begingroup
\setcounter{tocdepth}{1}
\renewcommand{\contentsname}{\centering Table of Contents}
\renewcommand{\numberline}[1]{#1.\hspace{0.6em}}
\setlength{\parskip}{0.35em}
\vspace{1.0\baselineskip}
\begin{center}\rule{0.35\linewidth}{0.4pt}\end{center}
\vspace{1.1\baselineskip}
\tableofcontents
\endgroup

```{=html}
<div class="toc">
<hr class="toc-divider" />
<div class="toc-title">Table of Contents</div>
<ul>
<li><a href="#tldr">TL;DR</a>
</li>
<li><a href="#quick-setup-60-seconds">Quick Setup (60 seconds)</a>
</li>
<li><a href="#zsh-manual">ZSH (manual)</a>
</li>
<li><a href="#bash">Bash</a>
</li>
<li><a href="#macos-linux-bsd-for-reference">macOS, Linux, BSD (for reference)</a>
</li>
<li><a href="#use-it">Use It</a>
</li>
<li><a href="#the-problem-whats-actually-going-on">The Problem (What’s Actually Going On)</a>
</li>
<li><a href="#why-explorer-is-the-right-tool">Why Explorer Is the Right Tool</a>
</li>
<li><a href="#the-correct-mental-model">The Correct Mental Model</a>
</li>
<li><a href="#recommendation">Recommendation</a>
</li>
<li><a href="#final-thoughts">Final Thoughts</a>
</li>
</ul>
</div>
```


```{=latex}
\vspace{1.0\baselineskip}
\begin{center}\rule{0.35\linewidth}{0.4pt}\end{center}
\vspace{1.0\baselineskip}
```

```{=html}
<hr class="meta-divider" style="width:35%; margin:2rem auto; border:0; height:1px; background: rgba(0,0,0,0.35);" />
```

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

   * ZSH $\to$ `~/.zshrc`
   * Bash $\to$ `~/.bashrc`

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