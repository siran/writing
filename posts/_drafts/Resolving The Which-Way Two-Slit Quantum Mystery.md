---
title: Resolving The Which-Way Two-Slit Quantum Mystery by Modeling Detectors as Potential Energy Trigger
subtitle: The Least-Energy Principle or “The Lazy Electron”
author: Julian Hart, An M. Rodriguez, Elias Thorne
date: 2026-01-24
one-sentence-summary: Interference disappears in which-way experiments because detector interaction introduces a deterministic energetic phase divergence that makes coherent superposition energetically inadmissible.
summary: >
  The two-slit which-way problem is commonly framed as a paradox involving
  measurement, information, or distinguishability. In this document, the phenomenon
  is analyzed using deterministic quantum wave evolution and explicit interaction energies.
  By treating detectors as physical devices that impart an energetic shift to the
  wavefunction, we show that the monitored path undergoes a deterministic phase
  "rotation". We introduce a Least-Energy Admissibility Principle,
  positing that the electron will not spontaneously expend the energy required to
  "rotate-back" into alignment. Consequently, the interference term dissolves because the two paths become effectively
  divergent energetic histories. Geometrically, if two lines start at the origin and one is rotated by even the slightest differential, they miss each other entirely at all subsequent points.
keywords:
  - double slit experiment
  - which-way detector
  - quantum interference
  - least energy principle
  - phase divergence
  - decoherence
---

# 1. Scope and motivation

The two-slit experiment with which-way detectors is often presented as a
conceptual puzzle: interference disappears when a detector is present, even if
the detector acts "non-destructively."

Standard accounts explain this using informational or measurement-based
language. While mathematically functional, such explanations obscure a more
direct physical mechanism: **a detector is an energetic object**.

This work revisits the problem using only:

- linear wave evolution,
- explicit interaction energies,
- and a physically motivated admissibility principle.

No appeal is made to observers, collapse postulates, or epistemic concepts like
"knowledge."

---


# 2. Minimal physical model

We consider:

- a single electron described by a wave,
- two spatial openings (left and right),
- a detection screen.

Downstream of the openings, the wave takes the linear form

$$
\psi(x) = \psi_L(x) + \psi_R(x),
$$

where $\psi_L$ and $\psi_R$ denote the contributions sourced by
the left and right openings respectively.

This decomposition follows directly from linearity and boundary conditions. No
interpretation beyond wave propagation is assumed.

---


# 3. Deterministic amplitudes and phases

Each contribution is written in amplitude–phase form:

$$
\psi_L(x) = a_L(x)\,e^{i\phi_L(x)}, \qquad
\psi_R(x) = a_R(x)\,e^{i\phi_R(x)},
$$

with:

- $a_L(x), a_R(x) \ge 0$ real-valued magnitudes,
- $\phi_L(x), \phi_R(x)$ real-valued phases.

Crucially, the phase $\phi$ represents the system's directional
alignment in the complex vector space.

---


# 4. Full interference expression

The observable intensity on the screen is defined as:

$$
I(x) := |\psi(x)|^2.
$$

Expanding explicitly,

$$
\begin{aligned}
I(x)
&= |\psi_L + \psi_R|^2 \\
&= a_L^2(x) + a_R^2(x)
+ 2 a_L(x)a_R(x)\cos\!\big(\Delta \phi(x)\big).
\end{aligned}
$$

The interference term is the cross-term proportional to $\cos(\Delta \phi)$.
Geometrically, this represents the scalar product (overlap) of the two state
vectors. For this term to exist, the vectors must not simply exist
simultaneously; they must be coincident.

---


# 5. Detectors as energetic triggers

A which-way detector is not a passive ghost; it is a physical potential
$V_{det}$. To "detect" the electron on the Left path, the device must
interact with it.

This interaction imparts a specific interaction energy $\Delta E$ to the
electron state $\psi_L$. We model this interaction not as an absorption,
but as a **torque** applied to the phase vector.

$$
\psi_L \xrightarrow{\text{Detector}} \psi_L' = \psi_L \cdot e^{i \Theta_{rot}}
$$

where $\Theta_{rot}$ is the deterministic rotation angle induced by the
interaction potential.

---


# 6. The Energetic Phase Rotation

In the absence of a detector, $\psi_L$ and $\psi_R$ evolve
symmetrically. Their phase vectors remain "parallel" (coincident) as they
propagate, effectively tracing the same line in phase space (an "I" shape).

When the detector is active, it applies an energetic torque to the Left path
only. This rotates the state vector $\psi_L$ relative to
$\psi_R$.

The magnitude of this rotation is irrelevant to the topology of the split. Even
the slightest differential rotation $\Theta_{rot} > 0$ ensures that the two
vectors, which originate from the same source, **miss each other entirely** at
all subsequent points.

Like two rays shooting from an origin, if their angles differ by even a fraction
of a degree, their intersection is restricted solely to the point of origin
($t=0$). For all $t > 0$, they are divergent (a "V" shape).

The interference term vanishes because the waves physically miss one another:

$$
\text{Overlap} \propto \langle \psi_L | \psi_R \rangle \rightarrow 0
$$

The paths have not been blocked; they have been **misaligned**.

---


# 7. Least-Energy Admissibility Principle

The central question is: Why doesn't the wave simply interfere anyway?

To restore the interference pattern, the system would need to force the
divergent Left vector back into alignment with the Right vector (closing the "V"
back into an "I"). In physical terms, this requires erasing the interaction
imprint.

However, rotating a state vector against the potential that twisted it requires
**Work** (Energy).

We introduce the **Least-Energy Admissibility Principle**:

> **The electron wavefunction will not spontaneously expend potential energy to
> "rotate-back" a phase asymmetry introduced by the environment.**


**The Geometric Analogy:** Two straight lines starting from the origin only
coincide if they are perfectly parallel. If one is rotated, they separate
immediately.

Because the electron is "lazy" (follows the path of least action), it refuses to
pay the energy cost required to force these divergent lines back together. The
states remain separate, and the interference term dissolves.

---


# 8. The “lazy electron” picture

Informally, the result may be summarized as follows:

**Rotation guarantees separation.**

A detector rotates the path. Any rotation creates a "miss." Fixing the miss
requires energy. The electron is broke.

Therefore, the electron cannot access the superposition state. It arrives as two
independent, divergent probabilities:

$$
I_{total} = |\psi_L|^2 + |\psi_R|^2
$$

It does not solve the expensive equation for vector addition; it settles for the
cheaper solution of scalar addition.

---


# 9. Conclusion

In order to be resolved, the which-way two-slit experiment does not require
interpretive constructs involving observers, information, or the abstract notion
of "indistinguishability."

When detectors are treated properly as energetic devices, the phenomenon follows
from ordinary wave mechanics combined with the Least-Energy Principle. The
detector rotates the phase, creating a geometric divergence; the electron is too
"lazy" to correct the angle. The mystery dissolves into a simple geometric
constraint.
