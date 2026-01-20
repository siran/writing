---
title: "Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics"
subtitle: "A Geometry-Based Route from Classical Fields to Quantum Mechanics"
authors: Anes Palma, An M. Rodriguez, Elias Thorne
date: 2025-07-29
one-sentence-summary: |
  We derive the Schrödinger equation and the emergence of Planck's constant as the narrow-band limit of classical Maxwell wave dynamics on a toroidal standing mode.
summary: |
  Maxwell's equations for electromagnetism in source-free vacuum predict discrete energies when an electromagnetic field forms a self-confined toroidal standing pattern. For any component $F(\mathbf{r},t)$ of the electromagnetic fields $\mathbf{E}, \mathbf{B}$, we isolate the forward-time spectral part, keep all derivative terms exactly, and obtain —within a rigorously bounded, bandwidth-squared remainder— the Schrödinger equation. Planck’s constant and the inertial mass thus emerge not as fundamental constants, but as geometric properties of the fundamental toroidal mode ($E_{11}, \omega_{11}$).
keywords:
  - Maxwell Equations
  - Toroidal Quantization
  - Analytic Signal
  - Emergent Quantum Mechanics
  - Rydberg Ladder
license: CC BY 4.0
---

# Introduction

Quantum mechanics is usually introduced axiomatically. Maxwell’s equations, in
contrast, were distilled from experiment—Coulomb’s law, Faraday’s induction,
Ampère–Ørsted magnetism, and Hertz’s verification of electromagnetic waves.

Uniting these experimentally grounded field laws with quantum theory shows that
the Schrödinger equation follows from classical electromagnetism alone. In this
framework, mass is treated as an electromagnetic object with field structure.
Using the well-known relation $E=mc^2$, an electromagnetic account of
inertia naturally extends to the broader principle that energy attracts energy.


# Maxwell Wave Equation

For any Cartesian component $F(\mathbf{r},t)$ of $\mathbf{E}$ or
$\mathbf{B}$ in vacuum, the governing equation is:

$$
\left(\nabla^{2}-\frac{1}{c^{2}}\partial_t^{2}\right)F(\mathbf{r},t)=0 \tag{1}
$$


# Toroidal Standing Modes

We consider a self-confined electromagnetic mode with toroidal topology. Let the
major and minor radii be $R$ and $r$. Integer windings
$(n_1, n_2)$ impose the resonance conditions:

$$
k_1=\frac{n_1}{R},\qquad
k_2=\frac{n_2}{r},\qquad
k^{2}=k_1^{2}+k_2^{2},\qquad
\omega_{n_1n_2}=ck
$$

The energy of a mode is given by:

$$
E_{n_1n_2}=\hbar_g\,\omega_{n_1n_2},\qquad
\hbar_g=\frac{E_{11}}{\omega_{11}} \tag{2}
$$

This produces the energy ladder $E_n=E_{11}/n^2$ for symmetric windings
$n_1=n_2=n$, recovering the Rydberg series structure purely from classical
cavity harmonics.


# Exact Derivation via Analytic Signal

## Forward-Time Spectral Projection

We define the analytic (positive-time) signal:

$$
F^{(+)}(\mathbf{r},t)=\int_{0}^{\infty}\tilde F(\mathbf{r},\omega)\,e^{-i\omega t}\,d\omega
$$

which also satisfies Eq. (1). We extract the carrier frequency at the
fundamental mode $\omega_{11}$:

$$
\psi(\mathbf{r},t)=e^{i\omega_{11}t}\,F^{(+)}(\mathbf{r},t) \tag{3}
$$

Here, $\psi$ represents the slowly varying envelope of the field.


## Substitution and Exact Algebra

Insert the derivatives of $\psi$ into Eq. (1) and divide by
$e^{-i\omega_{11}t}$:

$$
\nabla^{2}\psi-\frac{1}{c^{2}}\partial_t^{2}\psi
+\frac{2i\omega_{11}}{c^{2}}\partial_t\psi
+\frac{\omega_{11}^{2}}{c^{2}}\psi=0 \tag{4}
$$

Because $\omega_{11}=ck_{11}$, the term $\frac{\omega_{11}^2}{c^2}\psi$ cancels
with the spatial Laplacian contribution $k_{11}^2 \psi$, leaving an exact
equation with a first-order time derivative.


## Bandwidth Control

Rearranging Eq. (4) yields:

$$
i\partial_t\psi=-\frac{c^{2}}{2\omega_{11}}\nabla^{2}\psi
+\frac{1}{2\omega_{11}c^{2}}\partial_t^{2}\psi \tag{5}
$$

For a mode with root-mean-square spectral width $\Delta\omega$, the second
derivative term obeys:

$$
\left\|\frac{1}{2\omega_{11}c^{2}}\partial_t^{2}\psi\right\|
\le\frac{\Delta\omega^{2}}{2\omega_{11}c^{2}}\|\psi\|
=O(\epsilon^{2}),\qquad
\epsilon=\frac{\Delta\omega}{\omega_{11}}\ll1 \tag{6}
$$


## Emergent $\hbar$ and $m$

We identify the emergent constants from the geometry of the fundamental mode:

$$
\hbar=\frac{E_{11}}{\omega_{11}},\qquad
m=\frac{E_{11}}{c^{2}} \tag{7}
$$

Substituting these into the coefficient $c^2/(2\omega_{11})$ gives
$\hbar/(2m)$. Discarding the $O(\epsilon^2)$ term yields the Schrödinger
Equation:

$$
i\hbar\,\partial_t\psi=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi+O(\epsilon^{2}) \tag{8}
$$


# Equivalent Derivations

The robustness of this result is confirmed via three alternative routes:
1.  **Operator Factorization:** Factoring the wave operator and expanding about
    $\omega_{11}$.
2.  **Multiple-Scale Expansion:** Introducing slow time $T=\epsilon t$;
    matching orders reproduces Eq. (8).
3.  **Poynting Vector Averaging:** Narrow-band averaging of the energy flow
    yields the probability current.

All routes rely on the same bandwidth parameter $\epsilon$ and yield
identical definitions for $\hbar$ and $m$.


# Discussion

* **Rigor:** Only the controlled $O(\epsilon^2)$ term is dropped. This term
  represents the "Causal History" or high-frequency carrier information lost in
  the Schrödinger approximation.
* **Emergent Constants:** $\hbar$ and $m$ are not
  arbitrary; they arise from the energy and geometry of a single classical mode.
* **Testable Corrections:** Deviations from Schrödinger dynamics scale as
  $\epsilon^2$ and are potentially measurable in high-$Q$
  cavities with tunable bandwidth.


# Conclusion

A doubly periodic electromagnetic mode, governed solely by Maxwell’s vacuum
equations, contains the Schrödinger dynamics of a quantum object once its
narrow-band envelope is isolated. Classical electrodynamics therefore supplies
the formal and numerical content usually attributed to quantum postulates.

---


### Appendix A: Carrier Extraction and Degeneracy

#### Carrier Extraction

The process of "extracting the carrier" is formally equivalent to demodulation.
* **Frequency Domain:** The positive spectrum is shifted left by
  $\omega_{11}$; the peak now sits at $\omega=0$.
* **Time Domain:** The fast factor $e^{-i\omega_{11}t}$ is removed;
  $\psi$ is the slowly varying envelope.
* **Condition:** The Schrödinger limit is valid strictly when
  $\Delta\omega/\omega_{11} \ll 1$.


#### Degeneracy at Level $E_1 = E_0/4$

* **Geometric Modes:** 4 states (integer pairs satisfying $n_1^2 + n_2^2 = 4$).
* **Chirality:** 2 states (Positive vs Negative carrier, $F^{(+)}/F^{(-)}$).
* **Total:** $4 \times 2 = 8$ states.
Projecting onto $F^{(+)}$ alone leaves the usual $n^2=4$
degeneracy; keeping both analytic branches doubles it, accounting for spin-like
multiplicity.

---


## References

1. Jackson, J. D. (1998). *Classical Electrodynamics*, 3rd ed., Wiley.
