---
title: Introducing 'git snooze', a timed 'git stash'
subtitle: A timed git-stash that resets automatically
author: An M. Rodriguez
date: 2026-01-25
one-sentence-summary: git snooze lets you defer local Git changes for a fixed time, and forces them to come back so they can’t be forgotten.
summary: >
  git snooze is a small Git tool that temporarily hides local changes for a
  fixed number of days. Unlike git stash, snoozed changes automatically
  reappear after their deadline and warn you, making forgotten work impossible.
keywords: git, productivity, developer-tools, cli, workflow, vibe-coding
DOI:
---

**One-Sentence Summary.** git snooze lets you defer local Git changes for a fixed time, and forces them to come back so they can’t be forgotten.

**Abstract.** git snooze is a small Git tool that temporarily hides local changes for a fixed number of days. Unlike git stash, snoozed changes automatically reappear after their deadline and warn you, making forgotten work impossible.

**Keywords.** git, productivity, developer-tools, cli, workflow, vibe-coding

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
<li><a href="#like-git-stash-with-a-timer">Like git-stash with a timer</a>
</li>
<li><a href="#the-idea">The idea</a>
</li>
<li><a href="#what-is-git-snooze">What is git snooze?</a>
</li>
<li><a href="#how-it-works-briefly">How it works (briefly)</a>
</li>
<li><a href="#installation-30-seconds">Installation (30 seconds)</a>
</li>
<li><a href="#basic-usage">Basic usage</a>
</li>
<li><a href="#unsnoozing">Unsnoozing</a>
</li>
<li><a href="#seeing-whats-snoozed">Seeing what’s snoozed</a>
</li>
<li><a href="#automatic-reminders-the-important-part">Automatic reminders (the important part)</a>
</li>
<li><a href="#extra-safety">Extra safety</a>
</li>
<li><a href="#why-this-exists">Why this exists</a>
</li>
<li><a href="#source-license">Source & license</a>
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

![git snooze: git stash with a timer.](https://siran.github.io/assets/writing/git-snooze.png)


## Like git-stash with a timer

`git stash` is useful.

It’s also a graveyard.

People stash things “for later”… and later never comes.

Changes disappear. Context is lost. Work is forgotten.

That’s not a Git problem. That’s a **human workflow** problem.


## The idea

**What if stashed work had a timer?**

* Hide changes for *N* days
* Automatically bring them back
* Warn you when they reappear
* Never rely on memory

That’s `git snooze`.


## What is git snooze?

`git snooze` is a small Git-side tool for **time-based deferral of local
changes**.

Think of it as:

> **A timed alternative to `git stash` that resets automatically.**


### Core properties

* ⏱ Time-based (default: 4 days)
* 👀 Always visible (`git snooze -l`)
* ⚠ Automatically reappears
* 🧠 Impossible to forget
* 🏠 Local-only (no history, no remotes)


## How it works (briefly)

* **Tracked files** $\to$ hidden using `git update-index --skip-worktree`

* **Untracked files** $\to$ renamed to `*.Nd.snoozed.*` and ignored via
  `.gitignore`

* **State** $\to$ stored locally in `.git/snooze.db`

* **Automation** $\to$ a `pre-commit` hook runs `git snooze sweep` $\to$ expired
  snoozes are automatically undone $\to$ a warning is printed to stdout

No commits. No branches. No magic.


## Installation (30 seconds)


### Download link (raw script)

👉 **Download:**
**`https://gist.githubusercontent.com/siran/3640fd147e26c88ea9db0dbe01c15d6c/raw/git-snooze.py`**


### One-line install (recommended)


```sh

curl -fsSL
"https://gist.githubusercontent.com/siran/3640fd147e26c88ea9db0dbe01c15d6c/raw/git-snooze.py"
-o /tmp/git-snooze \ && python3 /tmp/git-snooze install --global \ && rm -f
/tmp/git-snooze

```

That’s it.

* Installs `git-snooze` to `~/.local/bin`
* Sets **one alias only**:

  ```

  git snooze → git-snooze

  ```


## Basic usage


### Snooze a file (default: 4 days)


```sh

git snooze notes.md

```



### Snooze for a specific duration


```sh

git snooze notes.md 7

```



### Snooze *everything* (stash-like, but timed)


```sh

git snooze all git snooze all 14

```



## Unsnoozing


### Unsnooze one file


```sh

git snooze -u notes.md

```



### Unsnooze everything immediately


```sh

git snooze -u all

```

Unsnoozing is **idempotent** and **index-authoritative**. Even if metadata is
missing, the index is always restored.


## Seeing what’s snoozed


```sh

git snooze -l

```

Output is grouped by **days remaining**, so you can see what’s about to
reappear.


## Automatic reminders (the important part)

On every commit:

* `git snooze sweep` runs automatically
* Expired snoozes are undone
* A warning is printed if anything wakes up

You **cannot accidentally forget** snoozed work.


## Extra safety

* The tool **refuses to snooze itself** unless forced
* `git snooze all` never breaks your setup
* `git snooze doctor --repair` can rebuild metadata if needed
* `git snooze uninstall` cleans up cleanly (and asks before deleting state)


## Why this exists

I kept losing work in `git stash`.

Not because Git is bad — but because **humans forget**.

`git snooze` doesn’t trust memory. It trusts **time**.

That’s the whole idea.


## Source & license

* Provided as-is, use at your own risk.
* Single-file script (Python 3.6+)
* Readable, hackable, local-only
* MIT-style, do what you want

👉 **Source / download:**
**[https://gist.githubusercontent.com/siran/3640fd147e26c88ea9db0dbe01c15d6c/raw/git-snooze.py](https://gist.githubusercontent.com/siran/3640fd147e26c88ea9db0dbe01c15d6c/raw/git-snooze.py)**

---

✅ 100% vibe-code "certified"! 💯

![git snooze -h](https://siran.github.io/assets/writing/image.png)