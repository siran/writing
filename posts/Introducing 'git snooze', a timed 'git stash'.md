---
title: Introducing 'git snooze', a timed 'git stash'
subtitle: A timed git-stash that resets automatically
author: Jean Pierre
date: 2026-01-25
one-sentence-summary: git snooze lets you defer local Git changes for a fixed time, and forces them to come back so they can’t be forgotten.
summary: >
  git snooze is a small Git tool that temporarily hides local changes for a
  fixed number of days. Unlike git stash, snoozed changes automatically
  reappear after their deadline and warn you, making forgotten work impossible.
keywords: git, productivity, developer-tools, cli, workflow
DOI:
---

## Like git-stash with a timer

`git stash` is useful.

It’s also a graveyard.

People stash things “for later”… and later never comes.

Changes disappear. Context is lost. Work is forgotten.

That’s not a Git problem. That’s a **human workflow** problem.

---


## The idea

**What if stashed work had a timer?**

* Hide changes for *N* days
* Automatically bring them back
* Warn you when they reappear
* Never rely on memory

That’s `git snooze`.

---


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

---


## How it works (briefly)

* **Tracked files** → hidden using `git update-index --skip-worktree`

* **Untracked files** → renamed to `*.Nd.snoozed.*` and ignored via
  `.gitignore`

* **State** → stored locally in `.git/snooze.db`

* **Automation** → a `pre-commit` hook runs `git snooze sweep` → expired
  snoozes are automatically undone → a warning is printed to stdout

No commits. No branches. No magic.

---


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

---


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

---


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

---


## Seeing what’s snoozed

```sh

git snooze -l

```

Output is grouped by **days remaining**, so you can see what’s about to
reappear.

---


## Automatic reminders (the important part)

On every commit:

* `git snooze sweep` runs automatically
* Expired snoozes are undone
* A warning is printed if anything wakes up

You **cannot accidentally forget** snoozed work.

---


## Extra safety

* The tool **refuses to snooze itself** unless forced
* `git snooze all` never breaks your setup
* `git snooze doctor --repair` can rebuild metadata if needed
* `git snooze uninstall` cleans up cleanly (and asks before deleting state)

---


## Why this exists

I kept losing work in `git stash`.

Not because Git is bad — but because **humans forget**.

`git snooze` doesn’t trust memory. It trusts **time**.

That’s the whole idea.

---


## Source & license

* Provided as-is, use at your own risk.
* Single-file script (Python 3.6+)
* Readable, hackable, local-only
* MIT-style, do what you want

👉 **Source / download:**
**[https://gist.githubusercontent.com/siran/3640fd147e26c88ea9db0dbe01c15d6c/raw/git-snooze.py](https://gist.githubusercontent.com/siran/3640fd147e26c88ea9db0dbe01c15d6c/raw/git-snooze.py)**

---

✅ 100% vibe-coded "certified"! 💯

DOI:
