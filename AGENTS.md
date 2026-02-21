# AGENTS.md

## Shell Preference
- Prefer MSYS2/GNU shell commands by default.
- Execute commands through `C:\msys64\usr\bin\bash.exe -lc "<command>"` unless PowerShell is required.
- Prefer GNU tools (`rg`, `find`, `sed`, `awk`, `xargs`, `git`) over PowerShell cmdlets.
- Use POSIX paths inside bash (example: `/c/Users/an/Documents/src/siran/writing`).
- Use PowerShell only for Windows-specific tasks that cannot be done in bash.
- If PowerShell is required, state the reason briefly before running it.

## Command Reliability
- Prefer one mutation per command call for critical operations (add, commit, push, amend).
- Avoid long `&&` chains when quoting-sensitive values are involved.
- After each mutation, verify immediately with a read command (`git status -sb`, `git log -1`).
- Prefer non-interactive commands and explicit flags.
- For uncertain steps, run commands one by one instead of composing a single mega-command.

## Quoting and Paths
- In PowerShell, invoke Bash explicitly: `C:\msys64\usr\bin\bash.exe -lc '...'`.
- Use POSIX paths inside Bash (`/c/Users/an/...`), not Windows backslash paths.
- For filenames with spaces, either quote safely in Bash or escape spaces (`\ `).
- For commit messages with quotes/commas/special chars, use a message file + `git commit -F`.
- Avoid mixing PowerShell and Bash interpolation in the same argument string.
- If quoting becomes fragile, write a temp file (message/script), run command, then delete file.

## Aliases and Shell State
- Bash aliases require Bash context; PowerShell cannot resolve Bash aliases directly.
- Use `-lic` when invoking alias-heavy commands: `bash.exe -lic 'source ~/.bashrc; gst'`.
- `source ~/.bashrc` only affects that process; re-source in each one-shot command if needed.
- `!command` follows the session shell; use explicit Bash invocation for Bash aliases.
- The `no job control` warning in non-interactive Bash calls is expected and harmless.
