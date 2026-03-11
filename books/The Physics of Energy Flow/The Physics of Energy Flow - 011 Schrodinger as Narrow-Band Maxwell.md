---
title: The Physics of Energy Flow – Schrödinger as Narrow-Band Maxwell
date: 2026-03-11
---


# 11. Schrödinger as Narrow-Band Maxwell

**Claim.** The Schrödinger equation is not a new postulate of quantum
mechanics. It is a controlled approximation of Maxwell transport, valid when
the frequency bandwidth of the field configuration is small relative to its
central frequency.

Each component of the Maxwell field satisfies the wave equation:

$$
\left( \nabla^2 - \frac{1}{c^2} \partial_t^2 \right) F = 0.
$$

Consider a solution dominated by a narrow band of frequencies around a
central frequency $\omega_0$, with fractional bandwidth $\varepsilon =
\Delta\omega / \omega_0 \ll 1$. Write the field as a slowly varying
envelope $\psi(\mathbf{x}, t)$ modulating a carrier:

$$
F(\mathbf{x}, t) = \psi(\mathbf{x}, t) \, e^{i(\mathbf{k}_0 \cdot \mathbf{x} - \omega_0 t)}.
$$

Substituting into the wave equation and retaining terms to leading order in
$\varepsilon$ yields:

$$
i\hbar \, \partial_t \psi = -\frac{\hbar^2}{2m} \nabla^2 \psi + O(\varepsilon^2).
$$

The Schrödinger equation emerges as the envelope equation. $\hbar$ and $m$
are not fundamental constants introduced by hand; they encode the central
frequency and the geometry of the stable mode: $\hbar \propto \omega_0$ and
$m = \hbar \omega_0 / c^2$.

Quantum mechanics, in this view, is the physics of *slowly varying
envelopes* of electromagnetic energy. Its characteristic strangeness —
superposition, interference, uncertainty — is inherited directly from the
wave nature of Maxwell dynamics, not from a separate quantum layer of
reality.

---

*Source: Deriving the Schrödinger Equation from Source-Free Maxwell
Dynamics*
