---
title: Modal Electromagnetic Coupling Between Biological Systems Near Criticality  
subtitle: A First-Principles Maxwellian Framework for Bias via Frequency Structure  
author: —  
date: —  
keywords: Maxwell theory, biological electromagnetism, spectral structure, modal coupling, receiver selectivity, criticality, bias, coherence, intuition, rhythm  
---

# 1. Introduction

Discussions of long-range biological influence often fail for a precise reason:
they implicitly treat the receiver as a **passive object** that must be pushed
by force or energy exceeding a noise floor.

Living systems are not passive.

They are **active dynamical systems** equipped with selective filters,
integration, adaptation, and high-gain regulatory regimes. In such systems,
influence is not primarily exerted by magnitude, but by **structure**.

This document derives—step by step, from Maxwell’s equations and elementary
dynamical systems theory—a mechanism by which two biological systems can
influence each other through ordinary electromagnetism via **frequency and phase
structure**, producing **deterministic bias** rather than mechanical force.

No nonlocality is assumed. No conservation laws are violated. No “energy-free
information” is invoked.

The core claim is narrow:

> Two biological systems, treated as extended current distributions, can couple
> through ordinary electromagnetic fields because time-structured currents
> generate frequency-structured fields, receivers are spectrally selective, and
> near-critical regulatory subsystems can convert small, coherent structured
> drives into large state biases.


---


# 2. Assumptions (Minimal and Explicit)

We assume only the following:

**A1. Maxwellian Electrodynamics** Electromagnetic fields obey Maxwell’s
equations in linear media. No exotic physics is introduced.

**A2. Distributed Biological Sources** A biological system is modeled as a
bounded region $\Omega$ containing charge and current densities
$(\rho(x,t), J(x,t))$.

**A3. Linearity of Field Propagation** For fixed environmental and material
conditions, the mapping from sources to fields is linear.

**A4. Selective Biological Reception** A receiver does not respond to total
field power, but through specific internal couplings (filters, templates,
projections).

**A5. Near-Critical Regulatory Subsystems** At least one receiver subsystem
operates near a dynamical transition where susceptibility to bias is large.

**A6. Adaptation and Novelty Sensitivity** Biological regulation suppresses
steady signals and emphasizes changes.

No stochastic postulates are required. “Noise” refers only to unresolved degrees
of freedom.

---


# 3. Maxwell with Sources: The Linear Map

Let a biological system generate charge and current densities $\rho(x,t)$
and $J(x,t)$.

Maxwell’s equations (general linear medium):

$$
\nabla\cdot D = \rho,\qquad \nabla\cdot B = 0
$$

$$
\nabla\times E = -\partial_t B,\qquad
\nabla\times H = J + \partial_t D
$$

with constitutive relations (linearized around operating point):

$$
D = \epsilon * E,\qquad B = \mu * H,\qquad J_{\text{cond}} = \sigma * E
$$

Here $*$ allows frequency dependence (dispersion, loss).

**Definition 1 (Maxwell Map).** For a fixed environment (space, objects, tissue
state), Maxwell’s equations define a linear operator:

$$
(E,B) = \mathcal{M}[\rho,J].
$$

**Implication.** Any change in biological current structure produces a
proportional change in the field structure. There is no threshold in Maxwell’s
equations.

---


# 4. Time Structure Implies Frequency Structure (Exact)

Any time-dependent current admits a Fourier representation:

$$
J(x,t) = \int_{-\infty}^{\infty} J(x,\omega)e^{-i\omega t}\,d\omega.
$$

This is not an approximation.

**Theorem 1 (Spectral Reweighting).** Any modulation of timing in
$J(x,t)$ redistributes energy across frequencies $J(x,\omega)$.

**Proof.** Direct consequence of Fourier decomposition. ∎

---


## 4.1 Multiplicative Modulation (Equalizer Interpretation)

If a physiological control variable $q(t)$ scales a current component:

$$
J(x,t) = q(t)\,J_0(x,t),
$$

then in frequency space:

$$
J(x,\omega) = \int \tilde q(\omega-\omega')\,J_0(x,\omega')\,d\omega'.
$$

**Implication.** Biological practice does not “add energy” by default; it
**reallocates spectral weight**. This is an exact mathematical statement.

---


# 5. Environment and Tissue as a Frequency-Selective Transform

Choose a receiver-side observable $y(t)$ (voltage, induced current,
field average, etc.).

By linearity:

$$
y(\omega) = H(\omega)\,s(\omega),
$$

where:
- $s(\omega)$ is the relevant emitted field component from the sender,
- $H(\omega)$ is the full transfer function: space + objects + tissue.

**Definition 2 (Coupling Function).** $H(\omega)$ encodes both magnitude
and phase. Tissue is part of the coupling path.

**Implication.** Phase relations are preserved and transformed, not destroyed.

---


# 6. Modal Expansion: Modes as Coordinates, Not Ontology

Select any set of field patterns $\{\phi_m(\omega)\}$ that efficiently represent
the environment’s response (near-field patterns, multipoles, guided paths,
etc.).

Then:

$$
s(\omega) = \sum_m a_m(\omega)\,\phi_m(\omega),
$$

and the receiver computes:

$$
y(\omega) = \sum_m g_m(\omega)\,a_m(\omega).
$$

**Definition 3 (Shared Mode).** A “shared mode” is any pattern $\phi_m$
that:
1. the sender can excite, and
2. the receiver can project onto.

No cavity is required. Standing waves are a special case.

---


# 7. Receiver Selectivity: Projection and Integration

A biological receiver does not measure $y(t)$ pointwise. It computes
**correlations**.

Let $r(t)$ be an internal template (rhythm, harmonic pattern,
envelope).

Define the coupling statistic:

$$
z = \int_0^T y(t)\,r(t)\,dt.
$$

**Theorem 2 (Coherent Accumulation).** If $y(t)$ is phase-aligned with
$r(t)$, then $z$ grows with $T$. If not,
contributions cancel.

**Implication.** Frequency and phase structure dominate detectability, not raw
amplitude.

---


## 7.1 Noise and Amplitude (Exact Role)

Let the input be:

$$
x(t) = y(t) + n(t),
$$

where $n(t)$ is unresolved background.

After projection:

$$
z = \int_0^T x(t)r(t)\,dt = z_s + z_n.
$$

- $z_s$ scales with coherent matched structure.
- $z_n$ partially cancels.

**Key point.** Amplitude sets **rate of accumulation**, not qualitative
detectability. Zero amplitude yields zero effect; excess amplitude saturates or
distorts.

---


# 8. Why Timbre, Beats, and Tiny Spectral Changes Matter

Two signals can have identical total power:

$$
\int |S_1(\omega)|^2 d\omega = \int |S_2(\omega)|^2 d\omega,
$$

yet produce different $z$ because:

$$
\int S_1(\omega)R^*(\omega)\,d\omega \neq
\int S_2(\omega)R^*(\omega)\,d\omega.
$$

This is why:
- a bassoon differs from a trumpet,
- beats emerge from nearby frequencies,
- small harmonic shifts dominate perception.

A tuned receiver amplifies **structure**, not loudness.

---


# 9. Regulatory Dynamics and Near-Critical Bias

Let $X(t)$ be a regulatory variable in the receiver.

Model:

$$
\dot X = F(X;\mu) + \lambda z(t).
$$

Near a transition ($\mu \approx 0$), susceptibility is large.

**Toy Model (Pitchfork Bias).**

$$
\dot X = \mu X - X^3 + \lambda z.
$$

- Without $z$, multiple outcomes coexist.
- A small $z$ selects one branch.

**Interpretation.** The field does not push the system; it **tilts the
landscape**.

---


# 10. Adaptation and Novelty Detection

Biological systems suppress steady inputs.

Model:

$$
u(t) = z(t) - \langle z\rangle_{\text{recent}}.
$$

**Implication.** Repeated signals fade. Subtle changes stand out.

This explains why:
- “too much amplitude” is counterproductive,
- small spectral shifts are highly salient.

---


# 11. Shared Rhythm and Entrainment

Shared rhythm supplies a common template $r(t)$.

Effects:
1. Spectral alignment into narrow bands.
2. Phase stabilization.
3. Persistent coherent accumulation.

**Physical statement.** Shared music or rhythm increases effective coupling by
stabilizing the projection statistic $z$—not by increasing force.

---


# 12. Intuition as Non-Symbolic Information

The receiver variable $X$ evolves deterministically due to
$z(t)$.

But $z(t)$ is not linguistically encoded.

**Definition 4 (Intuition).** Intuition is causal influence via structured bias
without symbolic representation.

The information is real, operative, and structured—but not verbal.

---


# 13. Predictions (Falsifiable)

1. **Phase Scrambling Test** Hold power fixed; randomize phase → effect
   disappears.

2. **Coherence Beats Power** Weak matched signals outperform strong mismatched
   ones.

3. **Overload Nonlinearity** Excess amplitude reduces discrimination.

4. **Criticality Gate** Effects peak near transitions.

5. **Novelty Dependence** Repetition suppresses effects; controlled variation
   restores them.

6. **Shared Rhythm Enhancement** Entrainment increases coherence of
   $z$.

---


# 14. Summary (Single Statement)

Living systems are extended electromagnetic sources and selective receivers.
Maxwell’s equations map time-structured currents into frequency-structured
fields. Biological receivers extract information via projection and integration,
not power measurement. Near-critical regulatory subsystems convert small
coherent spectral biases into large deterministic state changes. Communication
occurs through structure, not force.

---

*End of Part I*


# Part II — Quantitative Bounds, Information, and Experiments

---


# 15. What “Information” Means Here (Pre-Shannon)

Before invoking Shannon, we define information operationally.

**Definition 5 (Operational Information).** Information is present if distinct
sender-controlled structures lead to reliably distinguishable receiver outcomes.

Formally:
- Sender selects among states \( J^{(1)}(t), J^{(2)}(t), \dots \)
- These produce receiver statistics \( z^{(1)}, z^{(2)}, \dots \)
- If the downstream regulatory variable \( X \) ends in different basins with
  high reliability, information has been transferred.

This definition:
- does **not** assume randomness,
- does **not** require symbols,
- does **not** require conscious decoding.

It is purely causal and dynamical.

---


# 16. Optional Shannon Layer (Upper Bound Only)

Once a receiver statistic \( z \) is defined, Shannon theory can be used **only
as a ceiling**, not as a claim of mechanism.

Assume:
- Receiver effectively listens in a band \( \mathcal{B} \) of width \( B \).
- Matched coherent variance: \( P_{\text{coh}} \).
- Unmatched residual variance: \( P_{\text{bg}} \).

Define:

$$
\mathrm{SNR} = \frac{P_{\text{coh}}}{P_{\text{bg}}}.
$$

Then the Shannon capacity bound is:

$$
C \le B \log_2(1+\mathrm{SNR}) \quad \text{bits/s}.
$$

**Interpretation in this framework:**
- \( B \) is set by receiver selectivity (template bandwidth).
- SNR is set by coherence, not raw power.
- Capacity can be very low (≪ 1 bit/s) and still matter near criticality.

This aligns with “bias channels”, not symbolic communication.

---


# 17. Slow vs Fast Biological Control Surfaces

## 17.1 Slow (Regulatory Bias Channels)

Examples:
- respiration rhythms,
- HRV bands,
- postural sway,
- slow vocal envelopes.

Typical bandwidths: \( B \sim 10^{-1} \) Hz.

Result:
- Very low information rates.
- High leverage due to critical gain.

These channels bias decisions, mood, readiness, coordination.

---


## 17.2 Fast (Spectral Control Surfaces)

Examples:
- vocal harmonics,
- rhythm microtiming,
- fine motor tremor patterns.

Typical bandwidths: \( B \sim 10^2–10^3 \) Hz.

Role:
- not direct EM transmission at that bandwidth,
- but **control of internal timing and coherence** that cascades down into
  slower regulatory channels.

Voice and music act as *spectral organizers*, not just acoustic carriers.

---


# 18. Why “Order of Magnitude” Is Secondary (But Not Zero)

Amplitude enters only through the matched statistic:

$$
z = \int y(t) r(t)\,dt.
$$

Key facts:
- Scaling amplitude scales accumulation speed.
- Coherence + integration can compensate for low amplitude.
- Saturation and adaptation impose upper limits.

Therefore:
- Order-of-magnitude estimates are relevant for feasibility,
- but **structure determines direction and selectivity**.

This is why tiny spectral differences dominate behavior in music, language
prosody, and affective communication.

---


# 19. Experimental Program (Clean and Decisive)

## 19.1 Define the Channel Explicitly

Choose:
- a receiver statistic \( z \),
- a template \( r(t) \),
- an integration window \( T \).

No vague “field strength” measurements.

---


## 19.2 Structural Manipulations (Key Tests)

1. **Phase Scrambling**
   - Preserve power spectrum.
   - Randomize phase relative to \( r(t) \).
   - Prediction: effect collapses.

2. **Template Mismatch**
   - Change receiver filter slightly.
   - Prediction: sharp drop in response.

3. **Amplitude Overload**
   - Increase amplitude beyond linear range.
   - Prediction: degraded discrimination.

4. **Novelty Restoration**
   - Repeated identical signal → adaptation.
   - Introduce subtle structured change → response returns.

---


## 19.3 Criticality Gating

Measure effects:
- near known transitions (decision points, attentional shifts),
- vs far from transitions.

Prediction:
- coupling effects peak near critical regimes.

---


# 20. Conceptual Unification: Voice, Body, Intuition

### Voice

- Vocal apparatus is a spectral modulator.
- Meaning is carried in harmonic ratios, envelopes, timing.
- Loudness is secondary.


### Body Language

- Posture and movement modulate slow currents and boundary conditions.
- Acts directly on regulatory channels.
- Faster and more reliable than words.


### Intuition

- Result of deterministic bias in regulatory variables.
- Information without symbols.
- Felt as “direction” rather than proposition.

All three use the same mechanism: **structured modulation → selective projection
→ biased regulation**.

---


# 21. Limits of the Framework (Explicit)

This framework does **not** claim:
- arbitrary long-range communication,
- immunity to environmental disruption,
- violation of noise limits,
- consciousness transfer.

It **does** claim:
- structure-sensitive coupling is physically allowed,
- selectivity and criticality dramatically amplify relevance,
- amplitude alone is the wrong organizing variable.

---


# 22. Final Synthesis (Plain Language)

Living systems are not loudspeakers trying to shout across space. They are
musicians tuning instruments inside shared physics.

Maxwell’s equations carry structure. Biology selects structure. Critical
dynamics amplify structure.

What flows between bodies is not force. It is bias.

---


# Appendix A — Minimal Mathematical Chain

\[ J(x,t) \;\xrightarrow{\text{Fourier}}\; J(x,\omega)
\;\xrightarrow{\mathcal{M}}\; s(\omega) \;\xrightarrow{\text{modes}}\;
a_m(\omega) \;\xrightarrow{\text{projection}}\; z(t)
\;\xrightarrow{\text{critical dynamics}}\; X(t) \]

Every arrow is linear or well-characterized nonlinear dynamics. No arrow invokes
new physics.

---


# Appendix B — One-Sentence Theorem

**Theorem (Bias via Structure).** In a linear field theory coupled to a
selective, adaptive, near-critical receiver, small coherent spectral structures
can deterministically bias outcomes without requiring large energy transfer.

---

*End of Part II*


# Part III — Objections, Clarifications, and Deeper Structure

---


# 23. Common Objections and Precise Replies

This section addresses the most common objections, stated in their strongest
form, and resolved strictly within the framework already derived.

---


## Objection 1: “This is just saying weak signals plus nonlinear systems”

**Reply.** Not quite. The essential point is **which variable is weak**.

- It is *not* total field energy.
- It is *not* broadband amplitude.
- It is a **matched projection** \( z = \int y r \).

Two signals with identical total energy can produce opposite \(z\). That fact
cannot be reduced to “weak signal + nonlinearity”. It is a structural statement
about **representation and selectivity**.

---


## Objection 2: “This is just entrainment”

**Reply.** Entrainment is a special case.

Entrainment corresponds to:
- narrowband locking,
- long coherence time,
- shared phase reference.

The present framework includes entrainment, but also:
- bias without full locking,
- transient structure,
- envelope and sideband effects,
- phase relations that never fully synchronize.

Entrainment is the **limit** of strong coupling, not the mechanism itself.

---


## Objection 3: “Noise will wash everything out”

**Reply.** Noise washes out *unmatched* structure.

Matched structure survives integration:

\[ z_s \sim T,\qquad z_n \sim \sqrt{T}. \]

This is the same reason:
- weak radio signals are detectable,
- correlation receivers work,
- matched filters outperform power detectors.

The framework does not deny noise. It explains **how selectivity defeats it**.

---


## Objection 4: “This predicts telepathy”

**Reply.** No.

The framework predicts:
- low-rate bias,
- context dependence,
- sensitivity to state and criticality,
- fragility under mismatch.

Symbolic, arbitrary, long-distance communication is *not* implied.

The channel is **analog, contextual, and limited**.

---


## Objection 5: “Why isn’t this already obvious in experiments?”

**Reply.** Because most experiments measure:
- amplitude,
- averaged power,
- broadband effects,
- steady-state responses.

They do *not* measure:
- phase-aligned projections,
- novelty-gated responses,
- state-conditioned susceptibility,
- structure-preserving statistics.

The wrong observable kills the signal.

---


# 24. The Geometry–Spectrum Duality (Deep Clarification)

Frequency and geometry are not independent.

For any linear wave system:

- Geometry determines which spatial patterns persist.
- Time structure determines how those patterns are populated.

This is why:
- posture matters,
- orientation matters,
- distance changes which components survive,
- tissue shape alters phase relations.

In compact form:

\[ \text{Geometry} \;\Longleftrightarrow\; \text{Mode Support} \]

\[ \text{Time Modulation} \;\Longleftrightarrow\; \text{Spectral Partition} \]

The interaction is always their product.

---


# 25. Near-Field vs Far-Field (No Confusion)

At biological timescales and distances:

- Low frequencies → quasi-static, near-field dominated.
- Higher frequencies → mixed near/far-field behavior.

**Key correction:** The mechanism does *not* rely on propagating plane waves.

It relies on:
- field patterns that extend into space,
- phase-coherent components that survive projection,
- coupling through whatever field configuration exists.

Near-field coupling is still Maxwellian. Selectivity still applies.

---


# 26. Why “Modes” Are the Right Language (Even Without Cavities)

Even in open space, solutions of Maxwell’s equations can be decomposed into
orthogonal families (multipoles, vector spherical harmonics, guided patterns).

A mode is simply:

> a degree of freedom that evolves independently under linear dynamics.


Using modes:
- isolates what the receiver can actually sense,
- avoids misleading “total field” arguments,
- makes interference explicit.

Modes are bookkeeping, not metaphysics.

---


# 27. Deeper Mathematical View: Functional Composition

The full system can be written as a composition of maps:

1. **Source modulation**
\[ q(t) \mapsto J(x,t) \]

2. **Field propagation**
\[ J \mapsto (E,B) \]

3. **Receiver projection**
\[ (E,B) \mapsto z \]

4. **Regulatory dynamics**
\[ z \mapsto X \]

Each arrow is:
- well-defined,
- local,
- causal.

The nonlinearity appears only at the **receiver**, not in the field.

---


# 28. Why Language Feels Different from “Vibe”

Language:
- discrete,
- symbolic,
- error-tolerant,
- slow.

Spectral/structural channels:
- continuous,
- phase-sensitive,
- state-dependent,
- fast.

They coexist, but operate on different layers.

This is why:
- tone contradicts words,
- posture overrides speech,
- intuition precedes explanation.

The physics predicts this separation.

---


# 29. Limits and Failure Modes (Honest Accounting)

The coupling fails when:
- phase coherence is lost,
- receiver templates mismatch,
- adaptation fully suppresses novelty,
- system is far from criticality,
- environment scrambles structure faster than integration.

These are not edge cases. They are the **default**.

This is why effects are:
- subtle,
- context-dependent,
- hard to reproduce without control.

---


# 30. Why This Is Not Optional for Biology

Biology *must* exploit this regime because:

- energy budgets are tight,
- brute-force signaling is expensive,
- regulation requires sensitivity, not power.

Evolution favors:
- structure over force,
- bias over push,
- timing over magnitude.

This is not speculative. It is the only efficient option available.

---


# 31. Minimal Experimental Signature (One-Line Criterion)

If the framework is correct, then:

> Holding total power fixed, selectively altering spectral phase relations that
> preserve matched projections will preserve the effect; altering them to break
> the projection will destroy it.


This single criterion cleanly separates:
- structural coupling,
- from amplitude-based artifacts.

---


# 32. Condensed Core (For Publication)

1. Maxwell maps biological currents linearly to fields.
2. Biological modulation redistributes spectral weight.
3. Receivers perform selective projections, not power measurements.
4. Coherence accumulates; mismatch cancels.
5. Near-critical dynamics convert small biases into decisions.
6. Adaptation suppresses steady signals, enhances novelty.
7. Information flows as structure, not force.

---


# 33. Final Closing Statement

Nothing in this framework is exotic.

What is unusual is the **choice of observable**.

When biology is analyzed using:
- projections instead of amplitudes,
- structure instead of power,
- bias instead of force,

the apparent paradox disappears.

The physics is ordinary. The implication is that *listening matters more than
shouting*.

---

*End of Part III*


# Part IV — Formal Mathematical Appendix

*(Linear Operators, Projections, Critical Gain, and Limits)*

---


## A. Mathematical Objects and Spaces

We make all objects explicit.


### A.1 Source Space

Let the biological source be a bounded region \(\Omega_A \subset \mathbb{R}^3\).

Define the source vector: \[ S(t) \equiv (\rho(x,t), J(x,t)) \in \mathcal{S} \]

where \(\mathcal{S}\) is a suitable Hilbert space of square-integrable, causal
source distributions with compact support.

---


### A.2 Field Space

Let the electromagnetic field be: \[ F(t) \equiv (E(x,t), B(x,t)) \in
\mathcal{F} \]

with \(\mathcal{F}\) the Hilbert space of finite-energy Maxwell solutions in the
given medium.

---


### A.3 Receiver Observable Space

Let the receiver define a measurable scalar (or low-dimensional) observable: \[
y(t) \in \mathbb{R} \]

Examples:
- potential difference,
- induced loop current,
- averaged field component,
- demodulated envelope.

---


## B. Linear Maxwell Operator

### B.1 Definition

For fixed environment and material state, Maxwell’s equations define a linear
operator: \[ \mathcal{M} : \mathcal{S} \rightarrow \mathcal{F} \]

such that: \[ F(t) = \mathcal{M}[S(t)] \]

Linearity: \[ \mathcal{M}[\alpha S_1 + \beta S_2] = \alpha \mathcal{M}[S_1] +
\beta \mathcal{M}[S_2] \]

---


### B.2 Frequency Representation

Applying Fourier transform in time: \[ S(\omega) \mapsto F(\omega) \]

\[ F(\omega) = \mathcal{M}(\omega)\,S(\omega) \]

where \(\mathcal{M}(\omega)\) is a linear operator-valued transfer function
(Green operator).

---


## C. Modal Decomposition (General Case)

### C.1 Mode Definition

Let \(\{\Phi_m(\omega)\}\) be a complete orthonormal (or biorthogonal) basis for
the subspace of \(\mathcal{F}\) relevant to coupling.

Then: \[ F(\omega) = \sum_m a_m(\omega)\,\Phi_m(\omega) \]

with coefficients: \[ a_m(\omega) = \langle \Phi_m(\omega), F(\omega) \rangle \]

Modes may be:
- multipole fields,
- guided near-field patterns,
- resonant quasi-modes,
- tissue-shaped eigenpatterns.

No cavity assumption is required.

---


### C.2 Source-to-Mode Map

Combining operators: \[ a_m(\omega) = \langle \Phi_m(\omega),
\mathcal{M}(\omega) S(\omega) \rangle \]

This explicitly shows:
- how geometry selects modes,
- how spectral structure controls modal occupation.

---


## D. Receiver Projection as Functional

### D.1 Linear Functional

Define the receiver’s linear functional: \[ \mathcal{K} : \mathcal{F}
\rightarrow \mathbb{R} \]

such that: \[ y(t) = \mathcal{K}[F(t)] \]

In frequency domain: \[ y(\omega) = \sum_m g_m(\omega)\,a_m(\omega) \]

where: \[ g_m(\omega) = \mathcal{K}[\Phi_m(\omega)] \]

This is the exact meaning of “receiver selectivity”.

---


## E. Matched Projection and Integration

### E.1 Template Definition

Let \(r(t)\) be the receiver’s internal template.

Define the matched statistic: \[ z = \int_0^T y(t)\,r(t)\,dt \]

In frequency domain: \[ z = \int y(\omega)R^*(\omega)\,d\omega \]

---


### E.2 Optimality (Matched Filter Theorem)

Among all linear receivers, \(r(t)\) proportional to the expected signal
maximizes the signal-to-background ratio in \(z\).

This is standard detection theory and requires no stochastic assumptions beyond
finite variance.

---


## F. Noise and Scaling

Let: \[ y(t) = y_s(t) + n(t) \]

Then: \[ z = z_s + z_n \]

with: \[ z_s \sim \mathcal{O}(T), \qquad z_n \sim \mathcal{O}(\sqrt{T}) \]

for incoherent background.

**Result:** coherence accumulates linearly; noise accumulates sublinearly.

---


## G. Saturation and Nonlinearity

Let the receiver have a nonlinear response \(f(\cdot)\):

\[ \tilde y(t) = f(y(t)) \]

Linear regime: \[ f(y) \approx y \]

Overload regime: \[ f'(y) \rightarrow 0 \quad \text{or distortion terms appear}
\]

Hence excessive amplitude reduces effective selectivity.

---


## H. Regulatory Dynamics Near Criticality

### H.1 General Form

Let: \[ \dot X = F(X;\mu) + \lambda z(t) \]

Define susceptibility: \[ \chi = \frac{\partial X}{\partial z} \]

Near a bifurcation: \[ \chi \gg 1 \quad \text{(finite but large)} \]

---


### H.2 Pitchfork Normal Form

\[ \dot X = \mu X - X^3 + \lambda z \]

Equilibria: \[ X^* \approx \pm\sqrt{\mu} + \mathcal{O}(z) \]

Sign of \(z\) selects branch.

---


## I. Adaptation and Novelty Detection

Define a slow baseline: \[ \bar z(t) = \frac{1}{\tau}\int_{t-\tau}^t z(s)\,ds \]

Define effective drive: \[ u(t) = z(t) - \bar z(t) \]

This implements:
- steady-state suppression,
- sensitivity to change.

---


## J. Information Without Symbols

Define a finite set of sender states \(\{S_i\}\).

Define outcome map: \[ S_i \mapsto X_i(T) \]

If: \[ X_i(T) \neq X_j(T) \quad \text{for } i \neq j \]

with reliability \(> p\), then information exists.

No entropy or probability is required.

---


## K. Shannon Capacity (Optional Bound)

Given matched statistic variance: \[ \mathrm{SNR} =
\frac{\mathrm{Var}(z_s)}{\mathrm{Var}(z_n)} \]

Capacity bound: \[ C \le B \log_2(1+\mathrm{SNR}) \]

This is a ceiling, not a mechanism.

---


## L. Summary of the Formal Chain

\[ S(t) \;\xrightarrow{\mathcal{M}}\; F(t) \;\xrightarrow{\mathcal{K}}\; y(t)
\;\xrightarrow{\langle \cdot,r\rangle}\; z \;\xrightarrow{\text{critical
dynamics}}\; X \]

Every arrow is:
- causal,
- local,
- mathematically defined.

No hidden assumptions remain.

---


## M. Final Formal Statement

**Theorem (Maxwellian Bias via Structure).** Given a linear field theory, a
selective projection receiver, and a near-critical regulatory subsystem,
arbitrarily small but coherent spectral structures in the field can
deterministically bias macroscopic outcomes, subject only to finite integration
time and saturation limits.

---

*End of Part IV — Formal Appendix*


# Part V — Alternative Formulations of the Same Mechanism

*(Same Physics, Different Languages)*

This part shows that the mechanism you derived is
**representation-independent**. Nothing hinges on “modes”, “Shannon”, or even
explicit Maxwell notation. The same structure appears in multiple equivalent
formulations.

This matters because skeptics often attack *language*, not physics.

---


## V.1 Green–Function Formulation (No Modes, No Frequencies)

Start directly from Maxwell with sources.

For fixed environment and material state, the field at the receiver is:

$$
F(x,t)
=
\int G(x,x';t-t')\,S(x',t')\,dx'\,dt'
$$

where:
- \(S=(\rho,J)\) is the source,
- \(G\) is the retarded Green function.

This is exact.

Now define the receiver observable:

$$
y(t) = \int W(x)\cdot F(x,t)\,dx
$$

Insert the Green function:

$$
y(t) =
\int\!\!\int K(x',t-t')\,S(x',t')\,dx'\,dt'
$$

with:

$$
K = W * G
$$


### Interpretation

- \(K\) is the **effective coupling kernel**.
- If \(K\) oscillates or has memory, it *selects timing*.
- Phase structure emerges automatically.

**No frequency talk. No modes. Same result.**

---


## V.2 Control-Theoretic Formulation (Input–Output View)

Treat the sender as a control input \(u(t)\). Treat the receiver as a dynamical
system.


### Linear Front-End

\[ y(t) = (h * u)(t) \]

where \(h(t)\) is the impulse response.


### Nonlinear Regulator

\[ \dot X = F(X) + \lambda y(t) \]


### Key Control Insight

- The receiver is **not a gain block**.
- It is a **state-dependent amplifier**.
- Sensitivity depends on operating point.

This reframes everything as:

> *small structured control signals steering a nonlinear system.*


Which is textbook control theory.

---


## V.3 Phase-Space Geometry (No Fields at All)

Forget electromagnetism temporarily.

Let:
- \(u(t)\) be a continuous drive signal.
- \(X(t)\) be a regulatory state.

Define a phase portrait with multiple attractors.

Now ask:

> What minimal perturbation changes which basin is selected?


Answer:
- Not force.
- Not energy.
- **Direction in phase space.**

Electromagnetic structure merely supplies that direction.

This formulation shows:
- why “bias” is the correct word,
- why amplitude is secondary,
- why intuition feels directional, not forceful.

---


## V.4 Information Geometry (Beyond Shannon)

Define a family of receiver probability distributions over states \(X\):

\[ P(X | \theta) \]

where \(\theta\) parametrizes structured input (spectral phase, envelope, etc.).

Near criticality:
- Fisher information with respect to \(\theta\) becomes large.
- Small parameter changes become distinguishable.

So:

> *Criticality is an information-geometry amplifier.*


No bits. No entropy. Still rigorous.

---


## V.5 Thermodynamic Formulation (Free-Energy Landscape)

Let the regulatory system minimize an effective potential:

\[ V(X;\theta) \]

Structured electromagnetic input modulates \(\theta\).

Near a bifurcation:
- \(V\) is shallow.
- Tiny tilts select outcomes.

This is equivalent to:
- pitchfork dynamics,
- catastrophe theory,
- symmetry breaking.

The field does not “do work”. It **reshapes the landscape**.

---


## V.6 Bayesian Brain Interpretation (If One Insists)

Even in Bayesian language:

- The receiver has priors encoded in dynamics.
- Structured input updates effective likelihoods.
- Near criticality, posteriors flip sharply.

But crucially:
- The “likelihood” is **phase-structured**, not amplitude-based.
- Prediction error corresponds to **novel spectral mismatch**.

This explains intuition without mysticism.

---


## V.7 Signal-Manifold View (Equalizer Without Frequencies)

Represent signals as trajectories on a manifold \(\mathcal{M}\).

- Distance on \(\mathcal{M}\) measures *structural difference*.
- The receiver computes projections onto preferred directions.

Amplitude rescales trajectories. Structure changes direction.

Criticality amplifies directional differences.

---


## V.8 Why All These Are the Same Thing

All formulations share the same skeleton:

| Step | Abstract Form |
|----|----|
| Source | Structured drive |
| Medium | Linear operator |
| Receiver | Selective projection |
| Dynamics | Nonlinear, near-critical |
| Outcome | Biased selection |

Change the language. The math remains.

---


## V.9 When to Use Which Formulation

- **Green functions** → physicists, purists.
- **Control theory** → engineers.
- **Phase space** → dynamical systems.
- **Information geometry** → theorists.
- **Thermodynamics** → biologists.
- **Bayesian framing** → cognitive science.

If the effect disappears when language changes, it was never real. Here it
survives every translation.

---


## V.10 Final Meta-Statement

If someone says:

> “I don’t believe in modes / Shannon / criticality / intuition”


The correct reply is:

> “Fine. Pick any linear representation. The bias remains.”


Because the mechanism is **coordinate-free**.

---

*End of Part V — Alternative Formulations*


# Part VI — Experimental Proposals for Verification of the Phenomena

*(Clean, Structural, Falsifiable)*

This section proposes experiments that test **structure-based coupling**
directly. Each experiment is designed so that **amplitude is held constant**
while **spectral/phase structure is manipulated**. A positive result cannot be
explained by force, power, or generic entrainment alone.

---


## 1. Guiding Experimental Principle

**Principle.** If coupling is mediated by *structured projections* rather than
amplitude, then:

> Holding total power fixed, manipulations that preserve the matched projection
> preserve the effect; manipulations that destroy it eliminate the effect.


This is the invariant across all experiments.

---


## 2. Canonical Measurement Stack (Minimal)

Every experiment instantiates the same chain:

1. **Source control** A structured drive \( u(t) \) with fixed RMS amplitude.

2. **Propagation** Ordinary space + tissue. No shielding assumptions required.

3. **Receiver projection** A known or inferred template \( r(t) \).

4. **Regulatory readout** A near-critical observable \( X(t) \).

Nothing else is measured.

---


## 3. Experiment Class A — Phase vs Power Discrimination

### A1. Design

- Sender emits a signal with fixed power spectrum \( |S(\omega)|^2 \).
- Two conditions:
  - **Coherent:** phase aligned to receiver template.
  - **Scrambled:** random phase, same spectrum.


### A2. Observable

- Receiver statistic: \[ z = \int y(t) r(t)\,dt \]
- Downstream regulatory variable \( X \) (choice bias, timing shift, HRV
  inflection, etc.).


### A3. Prediction

- Coherent condition → systematic bias.
- Scrambled condition → null result.


### A4. Interpretation

A positive result falsifies amplitude-only explanations.

---


## 4. Experiment Class B — Template Rotation Test

### B1. Design

- Fix source signal.
- Modify receiver template slightly: \[ r(t) \rightarrow r_\theta(t) \] (small
  frequency shift, phase rotation, envelope skew).


### B2. Prediction

- Sharp drop in effect for small template mismatch.
- Nonlinear sensitivity near optimal match.


### B3. Interpretation

Confirms projection-based coupling.

---


## 5. Experiment Class C — Overload and Saturation

### C1. Design

- Gradually increase amplitude while keeping structure fixed.
- Measure discrimination performance.


### C2. Prediction

- Improvement up to linear range.
- Degradation past saturation.


### C3. Interpretation

Rules out monotonic “stronger is better” force models.

---


## 6. Experiment Class D — Novelty Gating

### D1. Design

- Repeated presentation of identical structured input.
- Introduce minimal structural variation at fixed power.


### D2. Prediction

- Response decays with repetition.
- Response rebounds with subtle variation.


### D3. Interpretation

Confirms adaptive suppression + structure sensitivity.

---


## 7. Experiment Class E — Criticality Dependence

### E1. Design

- Identify moments of natural or induced near-criticality:
  - decision boundaries,
  - attentional shifts,
  - bistable percepts,
  - motor initiation thresholds.


### E2. Prediction

- Coupling effects peak near transitions.
- Far from transitions → null or weak effects.


### E3. Interpretation

Separates bias-from-force mechanisms.

---


## 8. Experiment Class F — Shared Rhythm Amplification

### F1. Design

- Two conditions:
  - shared rhythmic reference (music, paced breathing),
  - no shared reference.
- Same source structure otherwise.


### F2. Prediction

- Increased coherence of \( z \) with shared rhythm.
- Larger downstream bias.


### F3. Interpretation

Demonstrates phase stabilization as the amplifier.

---


## 9. Experiment Class G — Spatial Geometry Sensitivity

### G1. Design

- Vary orientation, posture, relative position.
- Keep distance and amplitude fixed.


### G2. Prediction

- Strong geometry dependence.
- Sharp nulls for certain configurations.


### G3. Interpretation

Confirms modal / pattern selectivity.

---


## 10. Experiment Class H — Blind Structural Decoding

### H1. Design

- Sender selects among \( N \) structural states.
- Receiver classification based only on \( X \) outcomes.
- No feedback, no awareness.


### H2. Prediction

- Above-chance decoding for small \( N \).
- Failure when structure is destroyed.


### H3. Interpretation

Operational information transfer without symbols.

---


## 11. Control Experiments (Mandatory)

Every positive result must survive:

1. **Power-matched controls**
2. **Phase-scrambled controls**
3. **Template-mismatched controls**
4. **Distance/orientation nulls**
5. **Temporal reversal tests**
6. **Sham sender conditions**

Failure on any invalidates the claim.

---


## 12. Instrumentation Notes (Non-Exotic)

- No requirement for ultra-sensitive field meters.
- Measurement is at the **receiver output**, not the field.
- Field meters are optional diagnostics, not primary endpoints.

This is crucial: the effect lives in the *projection*, not the raw field.

---


## 13. Statistical Treatment (Minimal and Honest)

- No averaging over incompatible states.
- Condition on receiver state.
- Analyze effect sizes, not just p-values.
- Expect high variance and context dependence.

This is a feature, not a flaw.

---


## 14. Failure Modes to Expect

Expect null results when:
- receiver is far from criticality,
- adaptation dominates,
- phase coherence is unstable,
- templates are misidentified.

Null results do **not** falsify the framework unless controls are satisfied.

---


## 15. The One Decisive Experiment

If only one experiment were done, it should be this:

> Fix power. Preserve spectrum.
> Rotate phase continuously.
> Measure bias continuously.


A smooth, phase-dependent effect curve is the signature. No force-based model
predicts it.

---


## 16. What Would Falsify the Framework

The framework is wrong if:

- Effects scale only with power, not structure.
- Phase scrambling has no impact.
- Geometry has no effect.
- Criticality does not gate responses.
- Overload improves discrimination monotonically.

These are clean falsifiers.

---


## 17. Final Experimental Summary

You are not testing “energy transfer”. You are testing **whether structure
survives projection**.

If it does:
- coherence accumulates,
- bias appears,
- intuition becomes measurable.

If it does not:
- everything averages away.

---

*End of Part VI — Experimental Proposals*


# Part VII — Strongest Skeptical Rebuttals and Formal Answers

*(Steelman Objections, Not Strawmen)*

This section takes the **strongest possible skeptical positions**—the ones that
would be raised by competent physicists, neuroscientists, and engineers—and
answers them strictly within the framework already derived.

No appeal to authority. No handwaving. Only logic, equations, and
falsifiability.

---


## Rebuttal 1 — “This is just correlation plus confirmation bias”

### Skeptical claim

Observed effects are subjective, post-hoc, or selectively reported. No causal
mechanism is demonstrated.


### Formal answer

The framework predicts **directional asymmetries under controlled structural
manipulation**.

Specifically:
- Hold RMS amplitude fixed.
- Hold power spectrum fixed.
- Alter **phase relations only**.

If outcomes change **systematically and reversibly** with phase, correlation and
bias explanations fail, because:
- phase scrambling preserves energy,
- preserves expectation,
- preserves experimenter belief.

Only structural coupling predicts phase sensitivity.

**Decisive falsifier:** A null result under phase scrambling supports the model.
Persistence of effect under scrambling falsifies it.

---


## Rebuttal 2 — “Thermal noise (\(kT\)) dominates everything”

### Skeptical claim

Biological EM signals are far below thermal noise and therefore irrelevant.


### Formal answer

The \(kT\) argument applies to **energy thresholds**, not **matched
projections**.

The receiver does not ask:

> “Is this signal larger than \(kT\)?”


It asks: \[ z = \int y(t) r(t)\,dt \]

Thermal noise contributes incoherently to \(z\). Matched structure contributes
coherently.

Scaling: \[ z_s \sim T, \quad z_n \sim \sqrt{T} \]

Thus arbitrarily small coherent structure can dominate given:
- sufficient integration time,
- correct template,
- unsaturated receiver.

This is exactly how:
- radio astronomy,
- NMR,
- lock-in amplifiers,
- correlation spectroscopy

operate **below thermal noise**.

The argument against this would also invalidate those fields.

---


## Rebuttal 3 — “Biology has no such templates or matched filters”

### Skeptical claim

Living tissue cannot implement precise spectral or phase-selective operations.


### Formal answer

Biology is full of such operations:

- cochlear filtering (mechanical frequency decomposition),
- phase locking in auditory neurons,
- resonance in ion channels,
- rhythmic neural assemblies,
- adaptive gain control.

Templates do not need to be explicit or symbolic. They can be:
- distributed,
- approximate,
- adaptive.

The theory requires only **selectivity**, not precision.

---


## Rebuttal 4 — “You are smuggling in resonances without proof”

### Skeptical claim

Claims of resonance or modal coupling are unjustified in messy biological media.


### Formal answer

No resonance is required.

The minimal requirement is: \[ \langle r, y \rangle \neq 0 \]

Even broad, lossy, low-Q selectivity suffices if:
- integration time is long,
- critical gain is present.

Resonance is a *bonus*, not a premise.

---


## Rebuttal 5 — “This predicts arbitrary mind-to-mind communication”

### Skeptical claim

If this were real, people could transmit messages freely.


### Formal answer

The framework predicts the opposite:

- very low information rates,
- heavy context dependence,
- strong geometry and state gating,
- rapid degradation under mismatch.

Bias ≠ language.

Symbolic communication requires:
- discrete alphabets,
- error correction,
- wide bandwidth,
- deliberate encoding.

None are implied here.

---


## Rebuttal 6 — “Criticality is a buzzword”

### Skeptical claim

Criticality is invoked to excuse weak signals.


### Formal answer

Criticality is mathematically precise.

Near a bifurcation: \[ \chi = \frac{\partial X}{\partial z} \gg 1 \]

This is not rhetoric. It is standard dynamical systems theory.

The framework does **not** assume permanent criticality. It predicts:
- episodic sensitivity,
- state dependence,
- narrow windows of effect.

Which matches biological observation.

---


## Rebuttal 7 — “If this is real, why is it unreliable?”

### Skeptical claim

True physical effects should be robust and reproducible.


### Formal answer

Robustness depends on **control of the right variables**.

Here the relevant variables are:
- phase,
- geometry,
- internal state,
- novelty.

Ignoring any one collapses the effect.

Many real phenomena are unreliable when probed incorrectly:
- chaos,
- hysteresis,
- bifurcation delays,
- metastability.

Unreliability is a **signature** of state-dependent nonlinear systems.

---


## Rebuttal 8 — “Why not simpler explanations?”

### Skeptical claim

Psychology, suggestion, or social cues explain everything.


### Formal answer

Those explanations fail when:

- sender and receiver are blinded,
- no sensory channels are available,
- structure is manipulated below awareness,
- effects follow phase rather than expectation.

The proposed experiments explicitly enforce these constraints.

---


## Rebuttal 9 — “You are redefining ‘information’ to avoid rigor”

### Skeptical claim

Without Shannon entropy, claims of information are vague.


### Formal answer

Shannon information is about **coding under uncertainty**.

The present definition is **causal distinguishability**:

\[ S_i \rightarrow X_i \quad \text{with reliability} \]

This is sufficient and strictly weaker.

Shannon theory can be layered on later as an upper bound. It is not the
foundation.

---


## Rebuttal 10 — “This collapses into placebo”

### Skeptical claim

Effects arise from belief or expectation.


### Formal answer

Belief affects cognition, not:

- phase scrambling effects,
- geometry-dependent nulls,
- saturation curves,
- matched-filter optimality.

Placebo does not reverse sign under phase inversion. The model predicts sign
flips.

---


## Rebuttal 11 — “Why hasn’t physics already absorbed this?”

### Skeptical claim

If valid, it would already be mainstream.


### Formal answer

Physics already contains the tools:
- linear response,
- matched filtering,
- critical dynamics.

What is missing is **application to biological regulation**, not theory.

This is a domain-boundary problem, not a physics problem.

---


## Rebuttal 12 — “This is unfalsifiable”

### Skeptical claim

The framework is too flexible.


### Formal answer

The framework makes **hard predictions**:

- phase matters more than power,
- coherence beats amplitude,
- overload degrades performance,
- geometry creates sharp nulls,
- criticality gates effects.

Any consistent violation falsifies it.

That is falsifiability.

---


## Rebuttal 13 — “This is just rebranding known facts”

### Skeptical claim

Nothing new is added.


### Formal answer

What is new is:
- the **unified chain** from Maxwell → projection → regulation,
- the insistence on **structural observables**,
- the prediction of **bias without force**.

Reframing is not trivial when it changes what is measured.

---


## Rebuttal 14 — “This invites pseudoscience”

### Skeptical claim

Such ideas attract unfounded claims.


### Formal answer

Pseudoscience avoids:
- explicit operators,
- falsifiable predictions,
- null conditions.

This framework demands them.

The cure for misuse is rigor, not silence.

---


## Rebuttal 15 — “Show me the one thing I should test”

### Skeptical demand

Give a single decisive test.


### Answer

Here it is:

> Fix amplitude.
> Fix spectrum.
> Continuously rotate phase.
> Measure bias.


A smooth, reversible phase-dependent curve settles the question.

---


## Final Skeptical Synthesis

Every serious objection reduces to one of three claims:

1. **Structure cannot survive noise** → false for matched filters.
2. **Biology cannot implement selectivity** → contradicted by physiology.
3. **Weak signals cannot matter** → false near criticality.

None invalidate the framework.

---


## Closing Statement (For Skeptics)

If this mechanism is wrong, it will fail **cleanly** under controlled structural
manipulations.

If it is right, it will appear **only** when structure is respected and
everything else is stripped away.

Either way, the experiments decide.

---

*End of Part VII — Skeptical Rebuttals*


# Part VIII — One-Page Axiomatic / Manifesto-Style Summary

*(Structure Over Force)*

---


## Axioms

**Axiom 1 — Living systems are electromagnetic systems.** All biological
activity involves moving charges and currents. These generate electromagnetic
fields governed by Maxwell’s equations.

---

**Axiom 2 — Maxwell’s equations are linear.** For fixed environments,
electromagnetic fields depend linearly on sources. Structure in the source
produces structure in the field.

---

**Axiom 3 — Time structure is frequency structure.** Any modulation of
biological timing redistributes spectral and phase content. This is exact and
unavoidable.

---

**Axiom 4 — Receivers are selective, not passive.** Biological systems do not
measure total power. They respond through specific projections, filters, and
templates.

---

**Axiom 5 — Coherence accumulates, mismatch cancels.** Phase-aligned structure
builds under integration. Unmatched structure averages away, even if
energetically larger.

---

**Axiom 6 — Amplitude controls rate, not meaning.** Amplitude sets how fast
evidence accumulates. Structure determines *what* accumulates.

---

**Axiom 7 — Biological regulation is nonlinear and adaptive.** Steady inputs are
suppressed. Changes are emphasized. Excess input saturates and degrades
selectivity.

---

**Axiom 8 — Near criticality, small biases matter.** When a regulatory subsystem
is near a transition, tiny structured drives can deterministically select
outcomes.

---

**Axiom 9 — Information need not be symbolic.** If distinct structures reliably
bias outcomes, information has been transferred, even without words or
awareness.

---

**Axiom 10 — Geometry matters.** Orientation, posture, distance, and tissue
shape determine which patterns couple. Power alone predicts nothing.

---


## The Chain (Irreducible)

\[ \text{Structured currents} \;\rightarrow\; \text{Structured fields}
\;\rightarrow\; \text{Selective projection} \;\rightarrow\; \text{Coherent
accumulation} \;\rightarrow\; \text{Critical bias} \]

Every arrow is causal, local, and well-defined.

---


## What This Explains (Cleanly)

- Why **tone** matters more than loudness
- Why **rhythm** synchronizes bodies
- Why **timbre** carries meaning
- Why **intuition** precedes explanation
- Why **posture** communicates faster than speech
- Why **subtle changes** outweigh brute force

---


## What This Rejects

- That influence requires large energy transfer
- That thermal noise forbids structure
- That biology is a power detector
- That “weak” signals are irrelevant
- That communication must be symbolic

---


## The Central Claim (One Sentence)

> Living systems influence each other not by pushing harder, but by aligning
> structure where sensitivity is high.


---


## The Decisive Test (One Line)

> Hold power fixed.
> Preserve spectrum.
> Rotate phase.
> Watch bias follow structure.


---


## If This Is Wrong

- Phase will not matter.
- Geometry will not matter.
- Criticality will not gate effects.
- Overload will only help.

The framework dies cleanly.

---


## If This Is Right

- Effects will be subtle, contextual, and directional.
- Shared rhythm will amplify coupling.
- Intuition will become measurable.
- Force-based language will fail.

---


## Final Manifesto

Biology does not shout. It listens.

Physics does not forbid this. It explains it.

What we measure determines what we believe. Measure structure.

---

*End of Part VIII — Axiomatic Summary*


# Abstract

Living biological systems are extended electromagnetic current distributions.
Their activity is inherently time-structured, and therefore frequency- and
phase-structured. Classical Maxwell electrodynamics maps this structure linearly
into surrounding electromagnetic fields, preserving spectral and phase
relationships. Biological receivers, however, do not respond to total field
power; they respond selectively through projections, integration, adaptation,
and nonlinear regulation.

Here we present a first-principles Maxwellian framework showing how two
biological systems can influence one another through ordinary electromagnetic
fields via **structure rather than force**. The decisive variables are spectral
partition, phase coherence, geometry, and receiver state—not raw amplitude.
Receiver selectivity is formalized as a projection (matched correlation) onto
specific field patterns, causing coherent structure to accumulate while
unmatched components cancel, even in noisy environments. Amplitude controls the
rate of accumulation but not its qualitative effect, and excessive amplitude
degrades coupling through saturation and adaptation.

Crucially, when a receiver subsystem operates near a dynamical transition
(criticality), small structured electromagnetic drives act as deterministic
biases that select regulatory outcomes without requiring significant energy
transfer. This mechanism explains how subtle frequency and phase differences
(timbre, rhythm, posture, tone) can strongly influence behavior, coordination,
and intuition without symbolic encoding or conscious awareness.

The framework yields clean, falsifiable predictions: effects depend sharply on
phase and geometry, survive power-matched phase scrambling controls, peak near
critical transitions, degrade under overload, and are amplified by shared
rhythmic references. No nonlocality, new physics, or violations of conservation
laws are invoked. The results reposition biological electromagnetic interaction
as a problem of **selective listening and critical bias**, rather than signal
strength, and provide a unified physical basis for non-symbolic communication,
intuition, and coordination in living systems.
