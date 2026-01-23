# Modal Electromagnetic Coupling Between Two Biological Antennas Near Criticality

## A Maxwellian Framework for Frequency-Based Bias

**Abstract**

We propose a mechanism for non-local correlation between biological systems that
relies neither on "paranormal" forces nor on high-amplitude signal transmission.
Instead, we treat biological systems as extended, time-varying current
distributions in a Maxwellian universe. We demonstrate that:
1.  **Transmission:** Biological currents act as Frequency Modulated (FM)
    transmitters, where information is encoded in the spectral structure
    (sidebands) rather than total power.
2.  **Coupling:** Two separated systems define a shared geometric boundary
    condition, supporting specific electromagnetic standing modes.
3.  **Reception:** A system operating near a Higher-Order Critical Point (HOCP)
    possesses infinite susceptibility to specific frequency perturbations,
    allowing it to be biased by minute changes in the modal structure of the
    field, regardless of the signal's energetic "weakness."

---


## 1. Introduction: The Amplitude Fallacy

Standard objections to biological field-coupling usually rest on the **Amplitude
Fallacy**: the assumption that for System A to influence System B, A must emit a
signal strong enough to overcome thermal noise ($kT$) at B via
energetic force.

This view treats the biological receiver as a passive rock that must be pushed.
However, living systems are active, far-from-equilibrium dynamical systems. If
System B is poised near a critical point, its susceptibility diverges. In this
regime, the relevant question is not *"How loud is the signal?"* but *"Does the
signal possess the correct frequency structure to couple to the order
parameter?"*

We present a rigorous derivation showing that **frequency structure** (driven by
physiological/neural modulation) governs the coupling, while **criticality**
governs the reception.

---


## 2. The Source: Biological Currents as FM Transmitters

A biological system (brain-spine-heart complex) is not a static charge
distribution. It is a collection of oscillating currents
$\mathbf{J}(\mathbf{x}, t)$.


### 2.1. Exact Spectral Decomposition

Let the current density in System A be $\mathbf{J}_A(\mathbf{x}, t)$. Since
biological processes are cyclic (heartbeat, respiration, neural firing), we
expand the current not as a DC flow, but as a carrier frequency modulated by
information (state/thought).

$$
\mathbf{J}_A(\mathbf{x}, t) = \mathbf{j}(\mathbf{x}) \cdot I(t)
$$

If the system has a basal rhythm $\omega_c$ (carrier) and is modulated by
a "thought" or physiological state signal $s(t)$, the current takes
the form of **Frequency Modulation (FM)** or Phase Modulation:

$$
I(t) = I_0 \cos\left( \omega_c t + \beta \int_0^t s(\tau) d\tau \right)
$$

Using the Bessel function expansion for sinusoidal modulation
($s(t) = \cos(\omega_m t)$), the spectral content splits into a carrier and
infinite sidebands:

$$
I(t) = I_0 \sum_{n=-\infty}^{\infty} J_n(\beta) \cos\left( (\omega_c + n\omega_m)t \right)
$$

**Physical Implication:** A change in the "thought" or state $s(t)$
does not necessarily change the total power ($I_0^2$). Instead, it
redistributes energy into specific **sideband frequencies**
$\omega_c \pm n\omega_m$. It is this *spectral fingerprint*, not the amplitude,
that propagates.

---


## 3. The Geometry: Modal Structure and Energy Scaling

Consider two biological antennas (current distributions) $A$ and
$B$ separated by a distance $r$. In a pure Maxwell
universe, these two objects define the boundary conditions for the space between
them.


### 3.1. The Interaction Modes

The electromagnetic field $\Psi$ (representing potentials or field
components) in the region must satisfy the wave equation:

$$
\nabla^2 \Psi - \frac{1}{c^2} \frac{\partial^2 \Psi}{\partial t^2} = 0
$$

The presence of Sources A and B implies that the solution space is spanned by a
set of "interaction modes" $\Phi_k(\mathbf{x})$. Following the Palma-Rodriguez
derivation, we denote the spatial component of a mode stretching between
$0$ (at A) and $r$ (at B) as:

$$
\Phi_k(\mathbf{x}; r) \propto f\left( \frac{k x}{r} \right)
$$


### 3.2. Energy Scaling

The energy stored in the spatial gradient of such a mode scales inversely with
separation. For a mode with amplitude coefficient $\alpha_k(t)$:

$$
W_k(r, t) \propto \frac{1}{r} [\alpha_k(t)]^2
$$

Crucially, $\alpha_k(t)$ is not arbitrary. It is driven by the spectral
overlap between the source current $\mathbf{J}_A$ and the mode shape
$\Phi_k$.

$$
\alpha_k(t) \propto \int_V \mathbf{J}_A(\mathbf{x}, t) \cdot \Phi_k(\mathbf{x}) \, d^3x
$$

Therefore, if the source current $\mathbf{J}_A$ shifts its frequency structure
(via FM), it excites a **different set of coefficients** $\alpha_k$. The
"message" is encoded in *which* modes are populated and their relative phase
relationships.

---


## 4. The Coupling: Interference and Coherence

We now compute the energy density at System B exactly. Maxwell's equations are
linear. The total field is the exact superposition of fields from A, fields from
B, and the environment:

$$
\mathbf{E}_{tot}(\mathbf{x}, t) = \mathbf{E}_A(\mathbf{x}, t) + \mathbf{E}_B(\mathbf{x}, t)
$$

The energy density $u$ (which drives thermodynamical forces)
depends on the square of the field:

$$
u(\mathbf{x}, t) = \frac{\epsilon_0}{2} | \mathbf{E}_A + \mathbf{E}_B |^2 = \frac{\epsilon_0}{2} \left( |\mathbf{E}_A|^2 + |\mathbf{E}_B|^2 + 2 \mathbf{E}_A \cdot \mathbf{E}_B \right)
$$


### 4.1. The Interference Term

The coupling lives entirely in the cross-term (interference term):

$$
\mathcal{I}_{AB}(\mathbf{x}, t) = \epsilon_0 \mathbf{E}_A(\mathbf{x}, t) \cdot \mathbf{E}_B(\mathbf{x}, t)
$$

Let us decompose the fields into their frequency components. Let
$\mathbf{E}_A \sim \cos(\omega_A t)$ and $\mathbf{E}_B \sim \cos(\omega_B t)$.

$$
\mathcal{I}_{AB} \propto \cos(\omega_A t)\cos(\omega_B t) = \frac{1}{2} \left[ \cos((\omega_A - \omega_B)t) + \cos((\omega_A + \omega_B)t) \right]
$$


### 4.2. The Necessity of Frequency Matching

If we average over a biological integration time $T$ (e.g., a
neural integration window):

1.  **If $\omega_A \neq \omega_B$:** The term $\cos((\omega_A - \omega_B)t)$
    oscillates and averages to **zero**. There is effectively no coupling.
2.  **If $\omega_A \approx \omega_B$:** The difference frequency is near zero
    (DC). The average is **non-zero**.

**Conclusion:** Coupling is strictly a function of **spectral overlap**. High
amplitude at the wrong frequency yields zero coupling. Low amplitude at the
precise shared frequency yields non-zero coupling.

This explains why "thoughts" (which modulate the frequency spectrum) determine
connectivity. A specific modulation creates specific sidebands; if the receiver
is sensitive to those specific sidebands, the "channel" opens.

---


## 5. The Receiver: HOCP and Sensitivity to Bias

How does a "weak" electromagnetic mode affect a macroscopic biological system?


### 5.1. System Dynamics Near Criticality

Let System B be described by an order parameter $X$ (e.g., membrane
potential coherence, neural firing rate) governed by a potential
$V(X)$.

$$
\frac{dX}{dt} = -\frac{\partial V}{\partial X} + \xi(t) \quad (\text{noise})
$$

Near a Higher-Order Critical Point (HOCP), the potential flattens. For example,
near a cusp catastrophe:

$$
V(X) \approx \frac{1}{4}X^4 + \frac{1}{2}a X^2 + b X
$$

At the critical point ($a \to 0, b \to 0$), the restoring force
$-\partial V/\partial X$ vanishes. The system becomes massless in the coordinate
$X$.


### 5.2. Susceptibility to Modal Fields

We treat the incoming modal energy $\mathcal{I}_{AB}$ as a perturbation field
$h(t)$ acting on $X$.

The susceptibility $\chi$ is defined as the response of the order
parameter to the field:

$$
\chi = \frac{\partial \langle X \rangle}{\partial h}
$$

In mean-field theory, near criticality ($a \to 0$):

$$
\chi \sim |a|^{-\gamma}
$$

As $a \to 0$, **$\chi \to \infty$**.

**Step-by-Step Mechanism:**
1.  System A modulates its current $\mathbf{J}_A$ (Thought).
2.  This generates a specific spectral sideband structure in the field.
3.  This field creates a non-zero interference term $\mathcal{I}_{AB}$ at System
    B *only* if frequencies match.
4.  This term acts as a bias field $h(t)$ on System B.
5.  Because System B is at an HOCP, its infinite susceptibility amplifies this
    microscopic bias, causing a macroscopic shift in state (bifurcation).

---


## 6. Illustrative Examples

### Example 1: The "Silent" Carrier vs. The Modulated Signal

Consider two people sitting quietly.
* **State 1 (No Rapport):** Their "carriers" (heart/respiration rates) are
  mismatched ($\omega_A \neq \omega_B$).
    * $\langle \mathbf{E}_A \cdot \mathbf{E}_B \rangle = 0$.
    * No coupling.
* **State 2 (Synchronization):** They synchronize breathing or listen to the
  same complex music.
    * $\omega_A \to \omega_B$. The carriers lock.
    * The "channel" is established (non-zero interference term).
* **State 3 (Transmission):** Person A engages in a specific cognitive task
  (modulation).
    * This generates sidebands at $\omega_A \pm \delta$.
    * Because $\omega_A \approx \omega_B$, these sidebands fall within the
      critical bandwidth of Person B.
    * Person B's HOCP amplifies this specific modulation, resulting in a "sense"
      of Person A's state.


### Example 2: Music as Geometry Stabilization

Why does complex sound facilitate this? A complex sound wave impinging on both A
and B drives their currents $\mathbf{J}_A$ and $\mathbf{J}_B$ externally.

$$
\mathbf{J}_{A,B}(t) \approx \mathbf{J}_{internal} + \chi_{mech} \mathbf{F}_{sound}(t)
$$

This forces a shared spectral baseline. It removes the "frequency mismatch"
barrier, ensuring that the cross-term $\mathbf{E}_A \cdot \mathbf{E}_B$ is
non-vanishing. The music acts as a "carrier wave" that enables the subtle
modulation of "thought" to ride across the gap.

---


## 7. Conclusion

We have derived a mechanism for biological coupling that requires no new
physics.

1.  **No New Force:** The interaction is purely electromagnetic (Maxwell).
2.  **No Action-at-a-Distance:** Coupling is mediated by standing wave modes
    defined by the geometry of the intervening space.
3.  **No "Strong" Signals:** The mechanism relies on **Frequency Modulation** to
    establish coherence and **Critical Susceptibility** (HOCP) to amplify the
    signal.

The interaction is not a transfer of power (joules), but a transfer of
**structural information** (frequency/phase) that biases the decoherence of a
critical system.
