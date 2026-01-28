---
title: A Deterministic Demystification of the Which-Way Quantum Double-Slit Experiment
subtitle: Interference as Phase Evolution Under Slit-Dependent Interaction Potentials
author: Jean Pierre
date: 2026-01-28
one-sentence-summary: Which-way detection alters double-slit interference deterministically through interaction-induced phase evolution, without collapse, observers, or stochastic dynamics.
summary: >
  This document presents a first-principles, deterministic account of the quantum
  double-slit experiment with which-way detectors. Detectors are treated as physical
  circuits possessing energetic barriers and therefore necessarily introduce localized
  interaction potentials. These interactions modify the action of electron paths and
  rotate their relative phases. The continuous transition from interference to its
  suppression follows solely from unitary dynamics and deterministic phase evolution.
  All probabilistic outcomes arise only from the final modulus squared.
keywords:
  - quantum mechanics
  - double-slit experiment
  - which-way detection
  - determinism
  - path integral
  - phase evolution
  - decoherence
doi: null
---

## 1. Determinism in Quantum Dynamics

Quantum mechanics is probabilistic only at the level of outcome statistics. Its
underlying dynamics is deterministic.

The evolution of a quantum state is governed by the Schrödinger equation

$$
i\hbar \frac{\partial \psi}{\partial t}
=
\left(
-\frac{\hbar^2}{2m}\nabla^2 + V
\right)\psi,
$$

or equivalently by the path-integral formulation

$$
\mathcal A
=
\int \mathcal Dq(t)\;
\exp\!\left(\frac{i}{\hbar}S[q]\right),
\qquad
S[q]=\int dt\left(\tfrac12 m\dot q^2 - V(q,t)\right).
$$

No randomness enters at the level of dynamics.

---


## 2. The Double-Slit Without Detectors

An electron propagates from a source to a screen through two slits. The
amplitude at a screen point $x$ is

$$
\psi(x)=\psi_1(x)+\psi_2(x),
$$

with

$$
\psi_j(x)=
\int_{\text{paths through slit }j}\!\!\mathcal Dq\;
\exp\!\left[
\frac{i}{\hbar}
\int dt\Big(\tfrac12 m\dot q^2 - V_0(q)\Big)
\right],
\qquad j=1,2.
$$

The probability density is

$$
P(x)=|\psi(x)|^2
=
|\psi_1|^2+|\psi_2|^2
+
2\,\mathrm{Re}\!\left(\psi_1\psi_2^*\right).
$$

The interference term arises from coherent phase relations between the two
families of paths.

---


## 3. What a Detector Is (Physically)

A detector is not an abstract observer. It is a physical device.

By definition, a detector:

- is a circuit with at least two metastable macroscopic states ("triggered" and
  "not triggered"),
- must contain an energetic barrier separating those states (to avoid continuous
  firing),
- and thus, requires an energy transfer to cross that barrier and register a
  detection event.

Consequently, the presence of a detector near a slit necessarily introduces a
localized interaction between the electron/photon/"quantum entity" and the
detector's activation circuit, independent of whether a macroscopic click
ultimately occurs. In a way, a detector looks to the electron like a barrier
that takes energetic effort to overcome; this is independent of the detector
firing. And so, a detectorless slit looks energetically costless.

In this picture, then, the electron wave deterministically traverses both slits,
and each slit leaves its own energetic fingerprint in the phase of the electron,
as seen in its phase -- a rotation.


### Scope and Modeling Assumptions

All detector degrees of freedom are treated implicitly through slit-dependent
interaction potentials. This involves no loss of generality: any microscopic
detector model with additional degrees of freedom can be integrated out,
yielding an effective action (or influence functional) acting on the electron
alone. The resulting phase functional is equivalent to the suppression of
interference obtained in standard decoherence treatments, expressed here
entirely in Lagrangian and path-integral language. Only unitary dynamics of the
full system are assumed.

---


## 4. Slit-Dependent Interaction Potentials

Let the detector near slit $j$ introduce a localized interaction
potential $V_j(q,t)$. The amplitudes become

$$
\psi_j(x)=
\int_{\text{paths via slit }j}\!\!\mathcal Dq\;
\exp\!\left[
\frac{i}{\hbar}
\int dt\Big(
\tfrac12 m\dot q^2
- V_0(q)
- V_j(q,t)
\Big)
\right].
$$

All detector physics enters solely through $V_j$.

---


## 5. Phase Evolution Induced by the Detector

Define the action difference between the two slit families:

$$
\Delta S
=
S_1-S_2
=
-\int dt\,(V_1 - V_2).
$$

The corresponding relative phase is

$$
\Delta\phi
=
\frac{\Delta S}{\hbar}.
$$

The total amplitude at the screen can therefore be written as

$$
\psi(x)
=
\psi_1^{(0)}(x)
+
e^{i\Delta\phi}\psi_2^{(0)}(x),
$$

where $\psi_j^{(0)}$ are the amplitudes in the absence of detector
interaction.

The probability density is

$$
P(x)
=
|\psi_1|^2
+
|\psi_2|^2
+
2\,\mathrm{Re}\!\left(
\psi_1^{(0)}\psi_2^{(0)*} e^{i\Delta\phi}
\right).
$$

The cross term depends entirely on the deterministic phase shift generated by
$V_1 - V_2$.

---


## 6. Continuous Suppression of Interference

The presence of a detector introduces a slit-dependent interaction potential
$V_1 - V_2$. This interaction modifies the relative phase between the two
slit contributions.

The amplitude at the screen is

$$
\psi(x)=\psi_1^{(0)}(x)+e^{i\Delta\phi}\psi_2^{(0)}(x),
\qquad
\Delta\phi=\frac{1}{\hbar}\int dt\,(V_1-V_2).
$$


### Derivation of the relative phase from first principles

Denoting by $q(t)$ a continuous spacetime trajectory of the electron,
with boundary condition $q(T)=x$ at the screen, the probability
amplitude at $x$ can be written as

$$
\psi(x)=\int_{q(T)=x} \mathcal Dq\;
\exp\!\left[
\frac{i}{\hbar}
\int_{0}^{T} dt\Big(
\tfrac12 m\dot q^2 - V_0(q) - V(q,t)
\Big)
\right],
$$

where the functional integral runs over all trajectories $q(t)$
originating at the source and terminating at the screen point $x$.
No restriction is placed on the intermediate path; each trajectory contributes a
phase determined by the action accumulated along it.

Assume the detector produces a slit-localized interaction, so that along any
path passing through slit $j$ the interaction term equals
$V_j(q,t)$, and outside the detector region it vanishes. Then the
amplitude decomposes as a sum over the two disjoint classes of paths:

$$
\psi(x)=\psi_1(x)+\psi_2(x),
$$

with

$$
\psi_j(x)=\int_{\text{paths via slit }j}\mathcal Dq\;
\exp\!\left[
\frac{i}{\hbar}
\int dt\Big(
\tfrac12 m\dot q^2 - V_0(q) - V_j(q,t)
\Big)
\right].
$$

Define the corresponding detectorless amplitudes

$$
\psi_j^{(0)}(x)=\int_{\text{paths via slit }j}\mathcal Dq\;
\exp\!\left[
\frac{i}{\hbar}
\int dt\Big(
\tfrac12 m\dot q^2 - V_0(q)
\Big)
\right].
$$

If, within each slit class, the detector interaction contributes an additive
action increment

$$
\Delta S_j = -\int dt\,V_j(q,t),
$$

then each $\psi_j$ factors as

$$
\psi_j(x)=e^{\frac{i}{\hbar}\Delta S_j}\,\psi_j^{(0)}(x).
$$

Therefore the total amplitude can be written as

$$
\psi(x)=\psi_1^{(0)}(x)+e^{i\Delta\phi}\psi_2^{(0)}(x),
\qquad
\Delta\phi=\frac{1}{\hbar}(\Delta S_2-\Delta S_1)
=\frac{1}{\hbar}\int dt\,(V_1-V_2).
$$


### Probability density

The corresponding probability density is

$$
P(x)
=
|\psi_1^{(0)}|^2
+
|\psi_2^{(0)}|^2
+
2\,\mathrm{Re}\!\left(
\psi_1^{(0)}\psi_2^{(0)*} e^{i\Delta\phi}
\right).
$$

As the interaction strength is increased, the phase difference $\Delta\phi$
becomes path-dependent. The cross term then ceases to contribute to the final
probability distribution, yielding

$$
P(x)\;\rightarrow\;
|\psi_1^{(0)}|^2+|\psi_2^{(0)}|^2.
$$

The interference pattern is therefore continuously deformed into the single-slit
envelope. No discontinuity or additional postulate is involved.

---


## 7. No Measurement Postulate Required

At no stage does the description require:

- wavefunction collapse,
- stochastic dynamics,
- observer dependence,
- information-based causation,
- paradoxes or interpretational assumptions.

The electron evolves deterministically under a Hamiltonian modified by physical
interaction potentials. Probabilities arise only after taking the modulus
squared of the resulting amplitude and summing over unobserved degrees of
freedom.

The disappearance of interference is a consequence of deterministic phase
evolution under interaction. Nothing else is required.

---


## 8. Conclusion

The which-way quantum double-slit experiment is an ordinary interference problem
governed by deterministic dynamics.

Which-way detectors:
- introduce unavoidable interaction potentials,
- rotate the relative phase of path amplitudes,
- suppress interference continuously via action differences.

The disappearance of interference is not a mystery. It is a consequence of phase
evolution under interaction.

Nothing more is required.
