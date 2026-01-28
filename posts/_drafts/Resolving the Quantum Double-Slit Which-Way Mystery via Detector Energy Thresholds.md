---
title: Resolving the Quantum Double-Slit Which-Way Problem via Partial Interference and Detector Coupling
subtitle: A Mechanistic Account Without Observation or Collapse
author: Julian Hart, An M. Rodriguez, Elias Thorne
date: 2026-01-27
one-sentence-summary: Interference in which-way experiments disappears continuously, not mysteriously, due to detector-induced distinguishability quantified by Hilbert-space overlap.
keywords:
  - double slit experiment
  - which-way detection
  - partial interference
  - decoherence
  - detector coupling
---

# 1. What needs explaining

In the double-slit experiment, single particles produce an interference pattern.
When a which-way detector is introduced, interference visibility decreases or
vanishes, even if the detector does not macroscopically fire.

This effect is often explained using abstract notions such as observation,
information, or wavefunction collapse. These explanations obscure the underlying
physical mechanism.

Here we show that no such concepts are required. The phenomenon follows directly
from standard quantum mechanics once detector coupling and partial interference
are treated correctly.

---


# 2. Interference as Hilbert-space overlap

Let the particle state be a coherent superposition of two paths: \[ |\psi\rangle
= |\psi_L\rangle + |\psi_R\rangle \]

The probability density on the detection screen is: \[ |\psi|^2 = |\psi_L|^2 +
|\psi_R|^2
+ 2\,\Re\!\left(\psi_L^*\psi_R\right)
\]

The interference term depends on the **overlap** between the two path
amplitudes. Interference does not require the states to be identical, only that
their inner product be nonzero.

Interference strength is therefore **continuous**, not binary.

---


# 3. Phase shifts do not destroy interference

A relative phase shift, \[ |\psi\rangle = |\psi_L\rangle +
e^{i\phi}|\psi_R\rangle, \] does not reduce interference visibility. It only
shifts fringe positions.

Thus, phase rotation alone cannot explain the disappearance of interference in
which-way experiments.

---


# 4. What a detector physically does

A detector is a physical system that interacts with the particle. Crucially, it
becomes **correlated** with the particle’s path.

After interaction, the joint state is: \[ |\Psi\rangle =
|\psi_L\rangle|D_L\rangle
+ |\psi_R\rangle|D_R\rangle
\]

Here, \(|D_L\rangle\) and \(|D_R\rangle\) are detector states correlated with
each path. No assumption of macroscopic triggering or classical thresholds is
required.

---


# 5. Partial interference and visibility

The observable probability distribution is obtained by tracing over detector
degrees of freedom: \[ P(x) = |\psi_L|^2 + |\psi_R|^2
+ 2\,\Re\!\left(\psi_L^*\psi_R\langle D_L|D_R\rangle\right)
\]

Define the visibility factor: \[ V = |\langle D_L|D_R\rangle| \in [0,1] \]

- \(V = 1\): detector states identical → full interference
- \(0 < V < 1\): partial distinguishability → partial interference
- \(V = 0\): detector states orthogonal → no interference

This continuous behavior matches experimental results.

---


# 6. Which-way information without energy exchange

The loss of interference does not require net energy transfer. Which-way
information can be acquired through entanglement alone, as demonstrated in
quantum nondemolition and cavity-based experiments.

Therefore, interference loss is not governed by energy minimization, but by
state distinguishability.

---


# 7. No collapse, no observer, no paradox

The disappearance of interference is not caused by:
- observation,
- consciousness,
- knowledge,
- or wavefunction collapse.

It is caused by **entanglement with uncontrolled degrees of freedom** and the
resulting suppression of off-diagonal terms in the reduced density matrix.

The process is unitary and reversible in principle.

---


# 8. Interpretation

The double-slit which-way experiment demonstrates a single principle:

> Interference exists exactly to the degree that alternative paths remain
> indistinguishable in Hilbert space.


This statement is quantitative, testable, and free of metaphysical assumptions.

---


# 9. Conclusion

The which-way problem contains no mystery.

Interference disappears because:
1. Detectors couple to the particle.
2. Coupling correlates path and detector states.
3. Path distinguishability suppresses interference continuously.

The phenomenon is fully explained within standard quantum mechanics, without
appeal to observation, collapse, or interpretation-dependent language.

---


# References

- B.-G. Englert, *Fringe Visibility and Which-Way Information*, Phys. Rev. Lett.
  77, 2154 (1996).
- W. H. Zurek, *Decoherence and the Transition from Quantum to Classical*, Rev.
  Mod. Phys. 75, 715 (2003).
- M. O. Scully, B.-G. Englert, H. Walther, *Quantum Optical Tests of
  Complementarity*, Nature 351, 111 (1991).
