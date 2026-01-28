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
\int dt\Big(\tfrac12 m\dot q^2 \Big)
\right],
\qquad j=1,2.
$$

Here the electron is taken to be free between source, slits, and screen; any
potential common to both slits contributes equally to all paths and is therefore
irrelevant to interference.

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
- is a circuit with at least two metastable macroscopic states (“triggered” and
  “not triggered”),
- must contain an energetic barrier separating those states, in order to avoid
  continuous firing,
- and therefore requires an energy transfer to cross that barrier and register a
  detection event.

Consequently, the presence of a detector near a slit necessarily introduces a
deterministic interaction between the electron and the detector’s circuit,
independent of whether a macroscopic click ultimately occurs.

From the electron’s perspective, a detector constitutes an energetic influence
that must be overcome. A detectorless slit, by contrast, is energetically
costless.

In this picture, the electron wave deterministically traverses both slits, and
each slit imprints its own energetic signature on the electron through a phase
shift determined by the interaction.


### Scope and Modeling Assumptions

All detector degrees of freedom are treated implicitly through slit-dependent
interaction potentials. This involves no loss of generality: any microscopic
detector model with additional degrees of freedom can be integrated out,
yielding an effective action happening on the electron alone. The resulting
phase functional is equivalent to the suppression of interference obtained in
standard decoherence treatments, expressed here entirely in Lagrangian and
path-integral language. Only unitary dynamics of the full system are assumed.

---


## 4. Slit-Dependent Interaction Potentials

Let the detector near slit $j$ introduce a localized interaction
potential $V_j(q,t)$. Any potential common to both slits has been omitted,
as it contributes equally to all paths and does not affect relative phases.

The amplitudes become

$$
\psi_j(x)=
\int_{\text{paths via slit }j}\!\!\mathcal Dq\;
\exp\!\left[
\frac{i}{\hbar}
\int dt\Big(
\tfrac12 m\dot q^2
- V_j(q,t)
\Big)
\right].
$$

All detector physics enters solely through the slit-dependent potentials
$V_j$.

---


## 5. Phase Evolution Induced by the Detector

Define the action increment associated with each detector interaction:

$$
\Delta S_j = -\int dt\,V_j(q,t).
$$

Only differences between these action increments affect interference. The
relative phase between the two slit contributions is

$$
\Delta\phi
=
\frac{1}{\hbar}(\Delta S_2-\Delta S_1)
=
\frac{1}{\hbar}\int dt\,(V_1-V_2).
$$

The total amplitude at the screen can therefore be written as

$$
\psi(x)
=
\psi_1^{(0)}(x)
+
e^{i\Delta\phi}\psi_2^{(0)}(x),
$$

where $\psi_j^{(0)}$ denote the detectorless slit amplitudes.

If the two detectors are energetically identical, $V_1=V_2$, then
$\Delta\phi=0$ and full double-slit interference is recovered.

---


## 6. Continuous Suppression of Interference

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

As the detector interaction strength is increased, the phase difference
$\Delta\phi$ becomes dependent on the class of paths contributing to the
amplitude. The cross term then ceases to contribute to the final probability
distribution, yielding

$$
P(x)\;\rightarrow\;
|\psi_1^{(0)}|^2+|\psi_2^{(0)}|^2.
$$

The interference pattern is continuously deformed into the single-slit envelope.
No discontinuity or additional postulate is involved.

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
