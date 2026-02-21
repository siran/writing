---
title: "You Like GNU, Not Linux"
description: "If you want bash, GNU tools, and a Unix workflow on Windows, you do not need WSL. MSYS2 UCRT64 is enough."
one-sentence-summary: For Windows-first developers who want Unix shell ergonomics, MSYS2 UCRT64 provides GNU tooling and package management with fewer cross-boundary headaches than defaulting to WSL.
summary: >
  This guide argues that many Windows-based workflows benefit more from MSYS2
  UCRT64 than from defaulting to WSL. It clarifies MSYS2/MSYS/MinGW/UCRT64
  terminology, compares MSYS2 against Git Bash, explains common path-translation
  pitfalls, and provides a concise pacman primer so developers can stay native
  while keeping a productive Unix-like shell environment.
keywords:
  - MSYS2
  - UCRT64
  - Git Bash
  - WSL
  - pacman
  - Windows development
  - GNU tools
tags: [windows, msys2, wsl, gnu, bash, git, vscode]
published: false
---

## TL;DR

If you

- want a shell environment with GNU's `bash`, `grep`,
  `sed`, `awk`, `fd`, `rg`, etc.
- do not compile Linux-targeted binaries
- do not need Linux containers locally


then WSL is extra operational complexity you do not need.

In many real setups, the friction is not coding; it is boundaries:

- networking surprises between host Windows and the Linux subsystem
- filesystem boundary issues when tools cross Windows paths and Linux paths


If you are not using Linux-specific syscalls, Linux GUI stacks, or Linux-target
runtime behavior, staying native on Windows with GNU tooling is the
simpler path.

Use **MSYS2 UCRT64** in Windows Terminal.

You keep:

- GNU tooling
- native Windows apps and performance
- one filesystem view
- no VM layer for daily workflow

### Fundamentals (`why` + `how`)

- `why`: Most people asking for "Linux" on Windows actually need GNU tooling
  and shell ergonomics, not Linux kernel behavior.
- `why`: For Windows-first work, one host OS and one filesystem removes common
  boundary failures.
- `how`: Run UCRT64 with inherited Windows environment variables:
  `C:\msys64\usr\bin\env.exe MSYSTEM=UCRT64 MSYS2_PATH_TYPE=inherit /usr/bin/bash -l -i`.
- `how`: Install and update with `pacman` (PACkage MANager): `pacman -Syu`,
  then install core tools from `mingw-w64-ucrt-x86_64-*` packages (`git`,
  `ripgrep`, `fd`, `rsync`, `python`, `make`).
- `how`: Use WSL only when you need Linux ABI fidelity, Linux containers, or
  Linux runtime semantics as a requirement.


## GNU Is Not the Linux Kernel

When many developers say, "I want Linux," what they mean is:

- `bash`
- forward-slash paths
- symlinks
- `grep`, `sed`, `awk`, `find`,
  `xargs`
- Git and a Unix-style CLI workflow


That is mostly **GNU userland ergonomics**, not a requirement for the Linux
kernel.

If your workflow does not require Linux ABI behavior, Linux-only syscalls, or
Linux container runtime behavior, MSYS2 covers the practical need with fewer
moving parts.


## Quick Decision Rule

Choose **MSYS2 UCRT64** when your main target is Windows and you want Unix-like
tools.

Choose **WSL** when you need to execute and validate Linux behavior itself.


## Where I Disagree with the Official Recommendation

The official MSYS2 docs suggest that if you mainly want Linux CLI tools, WSL is
the better choice:

- https://www.msys2.org/docs/what-is-msys2/


That recommendation is reasonable for Linux-parity-first workflows.

My claim is narrower and practical: if your host workflow is Windows-first and
you only need Unix shell ergonomics plus GNU tools, making WSL the default adds
avoidable boundaries (networking, path mapping, and cross-filesystem friction).
In that case, MSYS2 + native Windows tooling is simpler.


## Cygwin vs MSYS: Useful Mental Model

A concise framing from the Scoop wiki is:

- Cygwin focuses on Linux API compatibility
- MSYS focuses on POSIX-style scripting and shell workflow


Reference:

- https://github.com/ScoopInstaller/Scoop/wiki/Cygwin-and-MSYS-Comparison


That distinction helps set expectations: use MSYS2 as a productivity layer on
Windows, not as a full Linux runtime replacement.


## What MSYS2, MSYS, MinGW, and UCRT64 Mean

The naming is confusing at first, but the model is simple once you separate the
layers:

- **MSYS2**: the overall distribution (package manager, shells, repos, tools)
- **MSYS**: the POSIX compatibility runtime (`msys-2.0.dll`) and packages that
  run through that layer
- **MinGW**: "Minimalist GNU for Windows", meaning native Windows binaries
- **UCRT64**: 64-bit MinGW environment linked against Microsoft's Universal C
  Runtime (UCRT)
- **MINGW64**: 64-bit MinGW environment with the older `msvcrt` runtime
  family


For most webdev, writing, and AI workflows on Windows, the safe default is:

- use **UCRT64** for day-to-day development tools


The low-level runtime details matter most when you debug ABI/runtime edge cases
or package binaries for distribution.


## MSYS2 vs Git Bash (Direct Answers)

### Is Git Bash enough?

For many people, yes.

If you only need Git plus a lightweight Unix-like shell, Git Bash is enough.

### What does MSYS2 add?

The big difference is the package ecosystem:

- Git Bash (Git for Windows) ships a curated toolset focused on Git workflows.
- MSYS2 gives you a full package manager, `pacman` (PACkage MANager), and
  large repositories for shell tools, compilers, runtimes, and utilities.

That makes MSYS2 better as a general-purpose dev environment, not just a Git
shell.

### Can `pacman` work in Git Bash?

Not as part of Git Bash itself.

`pacman` belongs to an MSYS2 installation (`C:\msys64`). If MSYS2 is installed,
you can invoke its binaries from many shells, but then you are managing MSYS2,
not extending Git Bash's own package set.

### Can I use UCRT64 in Git Bash?

Not directly.

UCRT64 is an MSYS2 environment/profile, not a mode inside Git Bash. To use
UCRT64 packages reliably, launch an MSYS2 UCRT64 shell (or a Windows Terminal
profile configured for `MSYSTEM=UCRT64` and `MSYS2_PATH_TYPE=inherit`).


## `pacman` (PACkage MANager) Primer (Teaser)

`pacman` (PACkage MANager) uses a repository-sync mental model. What other
tools call "install,"
`pacman` calls `--sync` (`-S`): you are synchronizing selected package state
from remote repositories to your local machine.

In that model, package changes are applied as a transaction:

- fetch package artifacts from repos
- apply package hooks/scripts so binaries work in the target environment
- update a local package registry/database

So yes, it feels more like open-source/VCS thinking than app-store language.

If you only learn a few commands, make them these:

```bash
# update package databases + installed packages
pacman -Syu

# search packages
pacman -Ss ripgrep

# sync/install package(s)
pacman -S --needed mingw-w64-ucrt-x86_64-ripgrep

# show package info
pacman -Si mingw-w64-ucrt-x86_64-ripgrep

# list files installed by a package
pacman -Ql mingw-w64-ucrt-x86_64-ripgrep

# find which package owns a file
pacman -Qo /ucrt64/bin/rg.exe

# remove a package and unneeded deps
pacman -Rns mingw-w64-ucrt-x86_64-ripgrep
```

Two practical notes:

- Prefer `mingw-w64-ucrt-x86_64-*` packages in the UCRT64 shell.
- Run full updates (`-Syu`) regularly instead of partial upgrades.

I will publish a dedicated deep dive on `pacman` workflows next.


## Install MSYS2 (UCRT64)

1. Install MSYS2 to:


```text
C:\msys64
```

2. Open **MSYS2 UCRT64**.


3. Update packages:


```bash
pacman -Syu
```

If it asks you to close and reopen the shell, do that, then run `pacman -Syu`
again until no further core update is pending.

4. Install core tools:


```bash
pacman -S --needed \
  mingw-w64-ucrt-x86_64-git \
  mingw-w64-ucrt-x86_64-ripgrep \
  mingw-w64-ucrt-x86_64-fd \
  mingw-w64-ucrt-x86_64-rsync \
  mingw-w64-ucrt-x86_64-python
```


## Run UCRT64 Inside Windows Terminal

Avoid launching `ucrt64.exe` directly if you want everything in Windows
Terminal tabs.

Create a profile with:

```text
C:\msys64\usr\bin\env.exe MSYSTEM=UCRT64 MSYS2_PATH_TYPE=inherit /usr/bin/bash -l -i
```

This keeps Windows environment variables (including `PATH`) available inside
the shell.

If you want the shell to keep the current working directory, add
`CHERE_INVOKING=1`.

Recommended starting directory:

```text
%USERPROFILE%
```


## Why It Can Feel Like "Another Windows" at First

This confusion is common. On first install, MSYS2 often opens its own terminal
window (`mintty`), and its Unix-style paths (`/c/...`) can look
like a separate system.

It is still native Windows underneath:

- same files on NTFS
- same Windows apps
- same host OS


Using MSYS2 through Windows Terminal removes most of that "separate world"
feeling.


## Real Path Translation Pitfalls (and Fixes)

In MSYS-style shells, arguments that look like Unix paths can be rewritten
before being passed to native Windows executables. Sometimes that helps.
Sometimes it breaks your command in subtle ways.


### Example 1: Docker bind mounts

This common command can fail or mount incorrectly when argument conversion
interferes:

```bash
docker run --rm -v "$PWD":/app -w /app python:3.12 python app.py
```

Safer options:

```bash
docker run --rm -v "$(pwd -W):/app" -w /app python:3.12 python app.py
```

or:

```bash
MSYS2_ARG_CONV_EXCL='*' docker run --rm -v "$PWD:/app" -w /app python:3.12 python app.py
```


### Example 2: Passing literal Unix paths to native Python

If you run Windows Python from an MSYS shell:

```bash
python -c "import sys; print(sys.argv[1])" /tmp/cache
```

the argument may arrive as a rewritten Windows path, not the literal
`/tmp/...` string you typed. If your script needs literal Unix-like text,
disable conversion for that command or escape that argument pattern.


### Example 3: Colon-separated arguments

Any argument that combines paths with `:` can be interpreted as a
path-list-like value and rewritten unexpectedly. Container volume specs and some
CLI flags are the most common casualties.

Fix patterns:

- pass explicit Windows paths when calling native Windows CLIs
- use `pwd -W` / `cygpath -w` at boundaries
- disable conversion only where needed via `MSYS2_ARG_CONV_EXCL`


These are compatibility boundaries, not "MSYS2 is broken" issues. Once you know
where they are, the workflow is stable.


## Keep One Home Directory

If you want `~` to map to your Windows profile:

Edit:

```text
C:\msys64\etc\nsswitch.conf
```

Set:

```text
db_home: windows
```

Restart terminal and verify:

```bash
echo "$HOME"
```

Expected pattern:

```text
/c/Users/yourname
```

Then your dotfiles are naturally in:

```text
C:\Users\yourname
```

Before removing `/home/yourname`, verify everything works and your dotfiles are
migrated.


## VS Code Integration (`code .`)

Use a dedicated UCRT64 profile in VS Code so every integrated terminal opens in
the correct environment.

In `settings.json`, set:

```json
"terminal.integrated.profiles.windows": {
  "MSYS2": {
    "path": "C:\\msys64\\usr\\bin\\env.exe",
    "args": [
      "MSYSTEM=UCRT64",
      "MSYS2_PATH_TYPE=inherit",
      "CHERE_INVOKING=1",
      "/usr/bin/bash",
      "-l",
      "-i"
    ],
    "cwd": "${workspaceFolder}"
  }
},
"terminal.integrated.defaultProfile.windows": "MSYS2"
```

`MSYS2_PATH_TYPE=inherit` carries Windows `PATH` into the shell, and
`CHERE_INVOKING=1` preserves the working directory from VS Code.

Then:

```bash
code .
```

This opens native Windows VS Code in the current folder.


## Stable Git Branch in Bash Prompt

Avoid expensive command substitution directly in `PS1` on every
redraw.

```bash
git_branch() {
  local b
  b=$(git symbolic-ref --quiet --short HEAD 2>/dev/null) || { GIT_BRANCH=""; return; }
  GIT_BRANCH=" ($b)"
}

PROMPT_COMMAND="git_branch"
PS1='\n\u@\h \[\e[35m\]$MSYSTEM\[\e[0m\] \[\e[33m\]\w\[\e[0m\]${GIT_BRANCH}\n\$ '
```


## Symlinks on Windows

Enable Developer Mode in Windows:

- Settings -> Privacy & Security -> For Developers -> Developer Mode


Then symlinks work as expected:

```bash
ln -s target_path link_name
```


## When You Actually Need WSL

Use WSL when you need one or more of these:

- Linux-native container workflows
- Linux ABI / glibc compatibility testing
- Linux filesystem and permission semantics as runtime requirements
- CI parity where target is Linux and subtle behavior matters


## Recommended Architecture for This Use Case

- Windows Terminal
- MSYS2 UCRT64
- Windows Python
- Native Windows VS Code
- one Git toolchain kept consistent
- dotfiles in `%USERPROFILE%`


Single host OS, fewer boundaries, less operational friction.


## Filenames, Filesystems, and Cross-Boundary Reality

One practical lesson from moving between WSL and native Windows:

- Linux filesystems (for example, ext4) allow filenames that Windows NTFS
  forbids.

Windows forbids these characters in filenames:

```text
< > : " / \ | ? *
```

Linux allows most of them.

If you create files inside WSL's ext4 (for example,
`chapter: introduction.md` or `question?.md`), everything works there. The
problem appears later:

- you clone or move that repository onto NTFS
- Git tries to materialize those filenames
- checkout fails or produces confusing errors

The issue is not Git. It is filesystem semantics.

If your repository is public and intended for cross-platform cloning, you
should:

- avoid Windows-illegal characters in filenames
- avoid trailing dots or spaces in names
- prefer portable ASCII for critical paths

This is not ideological. It is operational.

### Why MSYS2 Helps Here

When working directly on NTFS through MSYS2 UCRT64:

- invalid filenames fail immediately
- you see the constraint early
- your repository stays Windows-portable by construction

By contrast, WSL ext4 lets you create names that later break on Windows.

If your primary deployment target is Windows (or mixed teams), staying native
avoids this silent portability trap.


## Practical `pacman` Packages for Daily Workflow

If you use MSYS2 UCRT64 as your main environment, these packages are pragmatic
defaults.

Always prefer the `mingw-w64-ucrt-x86_64-*` prefix inside the UCRT64 shell.

### Core CLI Tools

```bash
pacman -S --needed \
  mingw-w64-ucrt-x86_64-git \
  mingw-w64-ucrt-x86_64-ripgrep \
  mingw-w64-ucrt-x86_64-fd \
  mingw-w64-ucrt-x86_64-rsync
```

- `ripgrep` (`rg`) is the default search tool for this workflow
- `fd` is a modern replacement for `find` in many workflows
- `rsync` is useful for controlled file synchronization and mirroring

### Python

```bash
pacman -S --needed mingw-w64-ucrt-x86_64-python
```

This gives you native Windows Python built via MinGW/UCRT without crossing
into WSL.

### Man Pages (Long-Form Documentation)

MSYS2 does not always install man pages by default.

Install:

```bash
pacman -S man-db man-pages
```

Then:

```bash
man rsync
man bash
man pacman
```

For many tools installed via `mingw-w64-ucrt-*`, man pages are available too.
This restores the classic Unix long-form documentation model.


## Recommended Baseline Install Set

For a productive Windows-first GNU environment:

```bash
pacman -Syu

pacman -S --needed \
  mingw-w64-ucrt-x86_64-git \
  mingw-w64-ucrt-x86_64-ripgrep \
  mingw-w64-ucrt-x86_64-fd \
  mingw-w64-ucrt-x86_64-rsync \
  mingw-w64-ucrt-x86_64-python \
  mingw-w64-ucrt-x86_64-make \
  man-db man-pages
```

Update regularly:

```bash
pacman -Syu
```

Avoid partial upgrades.


## Refined Position

If you need Linux ABI fidelity, containers, or glibc runtime semantics, use
WSL.

If you want:

- GNU tooling
- one filesystem
- native Windows performance
- fewer boundary surprises
- portable filenames by default

then MSYS2 UCRT64 is the simpler architecture.


## Conclusion

If your goal is a fast Unix-like development workflow on Windows, you do not
need a full Linux runtime.

You want GNU tooling and shell ergonomics.

MSYS2 UCRT64 gives you that while staying native.
