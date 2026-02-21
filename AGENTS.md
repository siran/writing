# AGENTS.md

## Shell Preference
- Prefer MSYS2/GNU shell commands by default.
- Execute commands through `C:\msys64\usr\bin\bash.exe -lc "<command>"` unless PowerShell is required.
- Prefer GNU tools (`rg`, `find`, `sed`, `awk`, `xargs`, `git`) over PowerShell cmdlets.
- Use POSIX paths inside bash (example: `/c/Users/an/Documents/src/siran/writing`).
- Use PowerShell only for Windows-specific tasks that cannot be done in bash.
- If PowerShell is required, state the reason briefly before running it.

## Why Commands Get Mangled
- The usual failure mode is two-stage parsing: PowerShell parses first, Bash parses second.
- This is not an MSYS2 bug. It is cross-shell quoting/interpolation complexity.
- Treat every command as crossing two parsers unless running directly inside a Bash terminal.

## Actionable Rules
- Prefer one mutation per command call for critical operations (`add`, `commit`, `amend`, `push`).
- Verify after each mutation with a read command (`git status -sb`, `git log -1`).
- Use Bash login shell for normal commands: `bash.exe -lc`.
- Use interactive Bash only when aliases are required: `bash.exe -lic 'source ~/.bashrc; <alias>'`.
- If quoting is fragile, use a temp file (for commit message or script) and then execute it.
- Avoid very long `&&` chains when values include quotes, regex, or spaces.

## Safe Patterns
- Basic command:
  `C:\msys64\usr\bin\bash.exe -lc "cd /c/Users/an/Documents/src/siran/writing && git status -sb"`
- Regex search (keep regex in single quotes inside Bash):
  `C:\msys64\usr\bin\bash.exe -lc "cd /c/Users/an/Documents/src/siran/writing && rg -n 'printf|escape|interpolation' AGENTS.md"`
- File with spaces:
  `C:\msys64\usr\bin\bash.exe -lc "cd /c/Users/an/Documents/src/siran/writing && sed -n '1,200p' posts/_drafts/WSL\ Was\ Optional\ -\ Codex\ and\ Git\ on\ MSYS2.md"`
- Alias execution:
  `C:\msys64\usr\bin\bash.exe -lic 'source ~/.bashrc; gst'`

## Git Commit Message Guidance
- For simple messages, use direct `-m`.
- For complex messages (quotes/commas/symbols), use message file + `git commit -F`.
- Avoid multi-layer `printf` escaping for commit messages unless absolutely necessary.

## Fallback Strategy
- If a grep/rg/sed command gets mangled by quoting, read the file directly (`sed -n` or `cat`) and answer from exact contents.
- Prefer correctness and reliability over compact one-liners.
