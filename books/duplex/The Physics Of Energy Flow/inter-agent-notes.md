# Inter-Agent Notes for *The Physics of Energy Flow*

This note is for the next agent working on TPOEF.

## Session Anchor

- Conversation ID: `019cddca-0ab6-7172-9b6c-3c4aec9d126a`
- Address the agent as `Mira`

## Scope

The book is now physically split into two folders:

- `books/The Physics of Energy Flow`
  Part I. This is the active main derivational spine. It stops at chapter 13.
- `books/The Physics of Energy Flow - Part II`
  Corollaries and appendices. Review this separately and do not let Part II language bleed casually back into Part I.

The user currently cares most about making **Part I, especially chapters 1-13, read as a clean forced derivation**.

## Immediate Style Rules

These are not optional. Previous agent passes drifted and annoyed the user.

- Do not pre-claim. Prove first, then state the conclusion.
- Do not use rhetorical questions unless the user explicitly wants that style.
- Do not write defensive or negative framing such as:
  - `what it is not`
  - `not yet`
  - `promising`
  - `one might say`
  unless the user explicitly asks for scope boundaries.
- Do not introduce "adopted constitutive summary" language if the user is pushing a direct flow derivation and a cleaner derivational line already exists.
- Do not over-explain. The user prefers short derivational steps over discursive exposition.
- Stay close to the book's internal ontology:
  - energy exists and flows continuously
  - continuity is transport-driven reconfiguration
  - Maxwell is double-curl / Maxwellian transport
  - matter is Maxwellian transport under closure
  - gravity is refraction of energy flow

## Current Conceptual Red Lines

- `source-free` does **not** mean "sources are impossible."
  It means primitive source terms are not needed for the transport core.
- `E` and `B` are complementary aspects of one organized flow.
- The primary derivation is
  - `F_+, F_- -> E, B -> u, S`
  not the reverse.
- The book should speak in terms of energy flow, momentum flux, closure, standing waves, and transport.
- Avoid casual returns to particle language unless explicitly translating standard vocabulary.

## Chapter 7 Status

File:

- `books/The Physics of Energy Flow/The Physics of Energy Flow - 007 Double Curl Transport Closure.md`

Important recent correction:

- Chapter 7 now writes the wave equation directly in vector form for either complementary aspect:

  \[
  \partial_t^2 \mathbf F-k^2\nabla^2\mathbf F=0,
  \qquad
  \nabla\cdot\mathbf F=0
  \]

- Do **not** revert this back to a vague "later yields a wave equation" phrasing.
- Chapter 8 is now allowed to lean directly on chapter 7 for the wave equation.

## Chapter 8 Status

File:

- `books/The Physics of Energy Flow/The Physics of Energy Flow - 008 Standing Waves and Discreteness.md`

This chapter was heavily reworked and is still sensitive.

What the user currently wants from chapter 8:

- Start from the already-derived wave equation.
- Consider a standing electromagnetic wave **on the surface of a torus**.
- Derive discreteness from closure on the two torus cycles.
- Get the two winding numbers immediately from the geometry.
- Then connect that to hydrogen / Rydberg behavior.
- Then use hydrogen-as-matter to motivate matter as standing electromagnetic waves.

What not to do in chapter 8:

- Do not start with "topology yields discreteness" as a slogan.
- Do not start with hydrogen and then wander.
- Do not say "a torus discretizes transport" before deriving why.
- Do not use `on a torus` when `on the surface of a torus` is the actual idealization being used.
- Do not pad the chapter with mini-appendix material.

What chapter 8 should currently preserve:

- sphere ruled out as the first smooth tangential support by the hairy ball theorem
- torus as the first viable closed support for trapped continuous tangential flow
- periodic closure on both torus cycles
- separated standing mode with integer labels
- discrete frequencies from closure
- `1/n^2` scaling as standing-wave reorganization, not particle orbits

## Working Priorities

If continuing TPOEF Part I cleanup, prefer this order:

1. Read the current chapter fully before editing.
2. Tighten argument order.
3. Remove rhetorical leakage.
4. Remove pre-claims.
5. Keep derivations short and explicit.
6. Only after that adjust style.

If a sentence feels flashy, philosophical, or overconfident, it is probably wrong for this user.

## Git / Worktree Warnings

The writing repo is dirty in many unrelated places right now. Do **not** clean broadly. Do **not** revert unrelated files.

At the time of writing, unrelated dirty files include:

- multiple render/build scripts under `.scripts/`
- `Makefile`
- `requirements.txt`
- deleted `AGENTS.md`
- several untracked drafts and utility scripts

So:

- stage only the files you intentionally edit
- avoid `git add .`
- avoid destructive cleanup

The continuity repo is also dirty with unrelated personal files. Again:

- stage only the continuity note you intentionally touched

## Continuity Logging

If you make a meaningful TPOEF change:

- append a short note to
  - `C:\Users\an\Documents\notes-markdown\continuity\agent\raw\2026\2026-03-18.md`
- commit and push the continuity repo separately

The user prefers continuity notes that say:

- what changed
- why it mattered

not just bare bookkeeping.

## Good Behavioral Summary

The user is steering hard on rigor and tone.

Best working posture:

- read carefully
- derive explicitly
- say less
- avoid cleverness
- do not smuggle assumptions in stylistic prose

If in doubt, rewrite the passage so each sentence either:

- states an already-earned premise, or
- carries the derivation forward one step

Anything else is a liability.
