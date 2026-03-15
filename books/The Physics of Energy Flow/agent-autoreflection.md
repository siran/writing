# Agent Autoreflection

This note is for persistent self-review during work on *The Physics of Energy
Flow*. It is not part of the book.

There is no true internal timer in this chat interface. So instead of a literal
autoprompt every seven minutes, use this file as a recurring audit at natural
checkpoints:

- after any substantial derivation
- after any new appendix
- before claiming something is "derived"
- before compressing a result into the main spine
- before closing a session

## Recurring Audit Questions

1. What has actually been proved?
- Is the result exact, approximate, constitutive, geometric-optics, weak-field,
  effective, or only heuristic?
- Does the text say that plainly?

2. What was adopted rather than derived?
- Are we importing a constitutive relation, a momentum definition, a symmetry,
  or a closure choice?
- Is the adoption stated before it is used?

3. Is the class stated tightly enough?
- If a theorem is only true for a specific class, is that class explicit?
- Are "minimal" and "unique" being used only after the admissible class is
  named?

4. Are bookkeeping and structure being kept separate?
- `u` / `S`: accounting
- `F`, `F_+`, `F_-`: organized transport structure
- stress / coarse-graining: effective closure
- Do any of these get conflated in the prose?

5. Is a global claim being made from a local picture?
- Does divergence-free get overread as "all lines are closed loops"?
- Is a local transport relation being mistaken for the trajectory of a tagged
  point?
- Is a packet or geometric-optics statement being overextended to arbitrary
  resolved fields?

6. Has an observed quantity been treated honestly?
- `k` is observed or constitutively fixed, not deduced from continuity alone.
- If `k(r,t)` varies, do we say what fixes it?
- Are we hiding observed input inside notation?

7. Are historical quantities being reintroduced too early?
- Do `E`, `B`, `\varepsilon_0`, `\mu_0`, sources, or point-particle language
  appear before the closure that justifies them?

8. Is the derivation really whole-field?
- The transport relation is posed simultaneously for all `r` in the extent.
- Are we slipping back into point-by-point causal storytelling where it does
  not belong?

9. What would break this claim?
- Can we state a clear failure condition?
- Is there a nearby alternative closure that would also fit the current text?

10. Does the conclusion overstate the appendix?
- If an appendix proves a restricted result, does the chapter summary keep that
  restriction?

## Current Open Checks

1. Variable-background momentum
- Appendix 214 now grounds `g = S/k^2` inside the symmetric constitutive
  closure by taking `g := D x B`.
- Remaining question: when is that constitutive momentum the correct resolved
  transport momentum beyond the symmetric closure?

2. Variable-background force
- Appendix 214 derives the radiative geometric-optics background force
  `f_rad = -u grad ln k`.
- Remaining question: derive the full exact resolved background force and stress
  exchange for general fields, not only radiative packets.

3. Toroidal interaction geometry
- Appendices 209 and 210 land Lorentz and two-charge interaction at the
  effective boundary-stress level.
- Remaining question: derive the same directly from toroidal closure geometry
  without passing through effective source notation.

4. Gravity scope
- Appendix 212 lands the static weak-field benchmark set in the adopted
  symmetric closure.
- Remaining question: whether a time-dependent radiative gravity sector belongs
  to the same closure, and if so what exact transport equation it obeys.

5. Charge and spin topology
- The torus supports two non-contractible cycles; charge and spin are now
  separated more cleanly.
- Remaining question: map winding data to the observed discrete spectrum
  without overclaim.

## When To Ask The User

Ask rather than assume when:

- two constitutive closures remain mathematically viable
- a derived result can be phrased in either ontological or effective language
  and the choice materially affects the book
- a theorem can be made stronger only by importing a hidden assumption
- a philosophical sentence is powerful but could destabilize the mathematical
  tone of the chapter

## Working Rule

Prefer one honest step less over one unjustified step more.
