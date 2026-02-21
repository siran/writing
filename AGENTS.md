# AGENTS.md

## Shell Preference
- Prefer MSYS2/GNU shell commands by default.
- Execute commands through `C:\msys64\usr\bin\bash.exe -lc "<command>"` unless PowerShell is required.
- Prefer GNU tools (`rg`, `find`, `sed`, `awk`, `xargs`, `git`) over PowerShell cmdlets.
- Use POSIX paths inside bash (example: `/c/Users/an/Documents/src/siran/writing`).
- Use PowerShell only for Windows-specific tasks that cannot be done in bash.
- If PowerShell is required, state the reason briefly before running it.
