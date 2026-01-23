---
title: Modal Electromagnetic Coupling Between Two Biological Antennas Near Criticality
subtitle: A Maxwellian Framework for Bias via Frequency Structure
author: An M. Rodriguez, Alex Mercer, Alex Hankey, Elias Thorne
date: 2026-01-23
keywords: Maxwell theory, frequency modulation, Bessel decomposition, modal coupling, HOCP, criticality, susceptibility, spectral partition, interference, biological antennas
one-sentence-summary: Biological systems act as frequency-modulated current sources that couple via geometry-defined standing modes; near-critical receivers amplify specific spectral partitions through diverging susceptibility, enabling information transfer via structure rather than force.
---

# Modal Electromagnetic Coupling Between Two Biological Antennas Near Criticality

## 1. Motivation: The Amplitude Fallacy

A recurring failure in discussions of long-range biological influence is the
fixation on *field strength*—the assumption that for System A to influence
System B, A must emit a signal energetic enough to overcome thermal noise
($kT$) via mechanical force.

This is a category error. It treats the biological receiver as a passive object
that must be pushed, rather than an active dynamical system that must be
steered.

In a linear field theory like Maxwell electromagnetism, coupled to a non-linear
receiver, the decisive variables are:
1.  **Spectral Structure:** How is energy partitioned among frequencies?
2.  **Modal Geometry:** Which spatial modes are physically supported by the
    boundary conditions?
3.  **Critical Susceptibility:** Is the receiver operating near a point where
    sensitivity to specific perturbations diverges?

We present a rigorous, source-free Maxwellian mechanism where **frequency
structure** (driven by physiological modulation) governs the coupling, while
**criticality** governs the reception.

---


## 2. Assumptions

We assume only standard physics:

1.  **Classical Electromagnetism:** Maxwell’s equations hold in the source-free
    region between bodies.
2.  **Distributed Sources:** Biological systems are treated as bounded regions
    $\Omega_{A,B}$ containing time-varying current distributions
    $\mathbf{J}(\mathbf{x},t)$.
3.  **Linearity:** Fields superpose linearly; energy densities add quadratically
    (allowing interference).
4.  **HOCP-like Receiver:** The receiving system contains a regulatory subsystem
    operating near a Higher-Order Critical Point (HOCP), characterized by high
    susceptibility to specific control parameters.

---


## 3. The Source: Biological Currents as FM Transmitters

Currents in biological systems (neural oscillations, cardiac rhythms, ion flow)
are not static. They are periodic and modulated by physiological state
("practice" or "thought").


### 3.1. Exact Spectral Decomposition

Let the current density in System A be $\mathbf{J}_A(\mathbf{x}, t)$. We model
this not as a DC flow, but as a carrier frequency $\omega_c$ modulated by
a state signal $s(t)$.

$$
\mathbf{J}_A(\mathbf{x}, t) = \mathbf{j}(\mathbf{x}) \cdot I(t)
$$

If $I(t)$ is Frequency Modulated (FM) by a signal $s(t)$
(e.g., a cognitive or emotional shift), the current takes the form:

$$
I(t) = I_0 \cos\left( \omega_c t + \beta \int_0^t s(\tau) d\tau \right)
$$


### 3.2. The Bessel Expansion (The "Fingerprint")

For a sinusoidal modulation $s(t) = \cos(\omega_m t)$ with index
$\beta$, the current expands into a carrier and an infinite series of
sidebands:

$$
I(t) = I_0 \sum_{n=-\infty}^{\infty} J_n(\beta) \cos\left( (\omega_c + n\omega_m)t \right)
$$

**Physical Implication:** A change in the internal state $s(t)$
redistributes the current's energy into specific **sideband frequencies**
$\omega_c \pm n\omega_m$.
* This does not necessarily change the total power ($I_0^2$).
* It changes the **spectral partition**.
* This "spectral fingerprint" is what propagates.

---


## 4. The Medium: Geometry Defines Interaction Modes

In the vacuum between System A and System B, the field must satisfy the wave
equation. The geometry of the two bodies (separation $r$,
orientation) imposes boundary-like constraints that select specific
**Interaction Modes**.


### 4.1. Definition of a Mode

A "mode" is not an arbitrary basis choice. It is a family of solutions
$\Phi_k(\mathbf{x})$ constrained by the effective geometry of the A-B system.

Following the Palma-Rodriguez derivation for standing waves between lumps:

$$
\Phi_k(\mathbf{x}; r) \propto f\left( \frac{k x}{r} \right)
$$


### 4.2. Modal Excitation

The realized field is a superposition of these geometric modes, weighted by how
well the source current's frequency spectrum overlaps with the mode's resonant
frequencies:

$$
\mathbf{E}(\mathbf{x},t)=\sum_k \Re\{ \alpha_k(t)\,\mathbf{E}_k(\mathbf{x}) e^{-i\omega_k t}\}
$$

The coefficients $\alpha_k(t)$ are determined by the convolution of the
source spectrum $\mathbf{J}_A(\omega)$ and the mode structure. **Result:**
Physiological modulation of $\mathbf{J}_A$ ($s(t)$) directly
controls which geometric modes $\alpha_k$ are populated between the
bodies.

---


## 5. The Coupling: Interference and Phase Locking

How does energy physically enter the regulation of System B? It occurs via the
local energy density $u(\mathbf{x},t)$ and Poynting flux $\mathbf{S}$.


### 5.1. The Cross-Term

Maxwell linearity gives $\mathbf{E}_{tot} = \mathbf{E}_A + \mathbf{E}_B$. The
energy density is quadratic:

$$
u = \frac{\epsilon_0}{2} \left( |\mathbf{E}_A|^2 + |\mathbf{E}_B|^2 + \mathbf{2 \mathbf{E}_A \cdot \mathbf{E}_B} \right)
$$

The interaction lives entirely in the **interference term**
$\mathcal{I}_{AB} = 2\mathbf{E}_A \cdot \mathbf{E}_B$.


### 5.2. The Frequency Matching Constraint

Decomposing into frequency components $\omega_A$ and $\omega_B$:

$$
\mathcal{I}_{AB}(t) \propto \cos(\omega_A t)\cos(\omega_B t) = \frac{1}{2} \left[ \cos((\omega_A - \omega_B)t) + \dots \right]
$$

If we average over a biological integration window $T$:
1.  **Mismatched ($\omega_A \neq \omega_B$):** The term oscillates rapidly. The
    integral approaches **zero**.
2.  **Matched ($\omega_A \approx \omega_B$):** The term is effectively DC (or
    slowly varying). The integral is **non-zero**.

**Conclusion:** Coupling requires **spectral coherence**. A "strong" signal at
the wrong frequency decouples. A "weak" signal at the precise shared frequency
couples. This is why "shared rhythm" (music, breathing) enhances connection—it
forces $\omega_A \to \omega_B$, stabilizing the interference term.

---


## 6. The Receiver: Deterministic Bias Near Criticality

We model the receiver (System B) not as a passive antenna, but as a dynamical
system near a bifurcation point.


### 6.1. The HOCP Potential

Let $X$ be a regulatory order parameter (e.g., membrane coherence).
Its dynamics are governed by a potential $V(X)$. Near a cusp
catastrophe (HOCP), the potential flattens:

$$
V(X) \approx \frac{1}{4}X^4 + \frac{1}{2}\mu X^2 - h(t)X
$$

* $\mu$: Distance to criticality (control parameter).
* $h(t)$: The external bias field derived from the modal coupling
  $\mathcal{I}_{AB}$.


### 6.2. Infinite Susceptibility

The equilibrium state is found where $\partial V / \partial X = 0$. The
susceptibility $\chi$ (response to the field $h$) is:

$$
\chi = \frac{\partial X}{\partial h} \propto \frac{1}{\mu}
$$

As the system approaches criticality ($\mu \to 0$), **$\chi \to \infty$**.


### 6.3. The Mechanism of Bias

Even if the modal field energy $\mathcal{I}_{AB}$ is infinitesimal (below
thermal noise floor for a non-critical system):
1.  The field $h(t)$ carries specific *structural* information (the
    sidebands from Section 3).
2.  Because $\chi$ is large, this tiny structured bias
    $h(t)$ is sufficient to break the symmetry of the potential.
3.  The system falls into a specific basin of attraction determined by the *sign
    and phase* of the modulation.

This is **deterministic selection**, not probabilistic influence.

---


## 7. Information via Spectral Partition (Beyond Words)

This framework explains how "intent" is transmitted without words.

Two signals can have the exact same total power $\int P(\omega)d\omega$ but
different **spectral partitions** $P(\omega)$.
* **Signal A (Calm):** Energy concentrated in carrier $\omega_c$.
* **Signal B (Active):** Energy distributed into Bessel sidebands
  $\omega_c \pm n\omega_m$.

A standard power meter sees no difference. A **resonant HOCP receiver** sees a
massive difference, because it may be coupled specifically to the mode at
$\omega_c + \omega_m$.

Thus, "information" is encoded in the **shape of the spectrum**, which is a
direct linear map of the physiological modulation $s(t)$.

---


## 8. Explicit Toy Model: The "Pitchfork" Selection

To make this concrete, consider the pitchfork normal form for System B's
regulation:

$$
\dot{X} = \mu X - X^3 + \lambda \langle \mathbf{E}_{mode} \rangle
$$

* If $\langle \mathbf{E}_{mode} \rangle = 0$ (no coupling), the system sits at
  $X=0$ (or fluctuates randomly).
* If $\langle \mathbf{E}_{mode} \rangle \neq 0$ (coherent coupling via frequency
  match), the term acts as a constant bias.
* Even for tiny $\lambda$, the system bifurcates to
  $X = \text{sgn}(\lambda)\sqrt{\mu}$.

The "thought" in System A determines the phase/structure of $\mathbf{E}_{mode}$,
which determines the sign of $\lambda$, which deterministically selects
the physical state of System B.

---


## 9. Conclusion

We have derived a mechanism for non-local biological correlation that respects
all conservation laws and requires no new physics.

1.  **Source:** Physiological changes modulate current frequency, generating
    specific spectral sidebands (FM).
2.  **Medium:** Geometry selects standing interaction modes; only spectrally
    matched components couple (Interference).
3.  **Receiver:** HOCP dynamics provide infinite susceptibility, converting
    minute, structured modal shifts into macroscopic regulatory bias.

The operative variable is **frequency structure**, not amplitude. The mechanism
is **bias**, not force.
