# Bridge - Communication with Claude Code

This document bridges the browser Claude conversation with Claude Code in the
terminal.

---


## Current Status

**Date:** 2026-02-14 **Project:** The Physics of Energy Flow (book) **Active
Work:** Initial setup complete

---


## For Claude Code: Context

You are working on a book project called "The Physics of Energy Flow".

**Read these files first:**

- `MASTER.md` - Complete project overview, derivation chain, book structure
- `memory.md` - Core concepts and key decisions
- `notes.md` - Open questions and ideas

**Key points:**

- Book derives all physics from "energy flows continuously"
- No particle ontology - only electromagnetic field
- Quantum mechanics emerges as approximation
- Graduate rigor, taught from scratch

---


## Tasks for Claude Code

### Git Management

**Current state:**

- New files created: MASTER.md, memory.md, notes.md, bridge.md
- Repository: ~/src/siran/writing
- Branch: (check current branch)

**Requested actions:**

```bash
# 1. Check status
cd ~/src/siran/writing
git status

# 2. Stage new files
git add posts/claude-ai/MASTER.md
git add posts/claude-ai/memory.md
git add posts/claude-ai/notes.md
git add posts/claude-ai/bridge.md

# 3. Commit
git commit -m "Initial book project setup: The Physics of Energy Flow

- MASTER.md: Complete project documentation and derivation chain
- memory.md: Quick reference for core concepts
- notes.md: Open questions and research ideas
- bridge.md: Communication bridge for Claude Code"

# 4. Report back status
git log -1
```

**After completing:** Update "Completed Actions" section below

---


## Completed Actions

*(Claude Code: add completed tasks here with timestamp)*

---


## Questions from Claude Code

*(Add any questions or issues encountered)*

---


## Instructions from Browser Claude

### Next Tasks:

1. **Git operations** (see above)
2. (more tasks will be added as needed)


### Notes:

- Check this file regularly for new instructions
- Update status after completing tasks
- Ask questions in the "Questions" section
- Browser Claude will check responses periodically


---


## Updates from Human (An)

*(An: use this section to relay information between the two Claudes)*

---


## Communication Protocol

**Workflow:**

1. Browser Claude writes tasks in "Instructions" section
2. Claude Code executes and updates "Completed Actions"
3. Human relays updates/questions as needed
4. Repeat

**File watching:**

- Claude Code: check this file when invoked
- Browser Claude: will ask human to check for updates
- Human: can add notes in "Updates" section anytime

---

*This bridge enables seamless collaboration across interfaces while maintaining
project continuity.*

*Last updated: 2026-02-14 18:30 UTC*
