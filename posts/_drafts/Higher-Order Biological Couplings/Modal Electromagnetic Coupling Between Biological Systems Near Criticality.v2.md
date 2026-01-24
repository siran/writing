---
title: Modal Electromagnetic Coupling Between Biological Systems Near Criticality
subtitle: A First-Principles Maxwellian Framework for Bias via Frequency Structure
author: —
date: —
keywords: Maxwell theory, biological electromagnetism, spectral structure, modal coupling, receiver selectivity, criticality, bias, coherence, rhythm
one-sentence-summary: Ordinary Maxwell electrodynamics permits structure-mediated coupling between active biological systems via phase-coherent projection and near-critical amplification, producing bias without large energy transfer.
summary: We derive a conservative, falsifiable mechanism for long-range biological influence using only standard Maxwell electrodynamics plus explicit receiver selectivity and near-critical regulatory gain. The sender is modeled as a distributed current density; the environment implements a linear retarded map from sources to fields; the receiver computes a matched projection (correlation) onto an internal template, allowing coherent structure to accumulate while unmatched components cancel. Near a dynamical transition, small coherent projections bias macroscopic regulatory outcomes without requiring large net energy transfer. The framework sharply distinguishes conducted, quasi-static near-field, and radiative regimes; clarifies what is claimed and what is not; and proposes decisive experiments that hold power fixed while manipulating phase and geometry.
---

# Modal Electromagnetic Coupling Between Biological Systems Near Criticality

## Introduction

Discussions of long-range biological influence often fail for a precise reason:
they implicitly treat the receiver as a passive object that must be pushed by
force or energy exceeding a noise floor.

Living systems are not passive.

They are active dynamical systems with selective filters, integration, adaptation,
and high-gain regulatory regimes. In such systems, influence is not primarily
exerted by magnitude, but by structure.

This document derives—step by step, from standard Maxwell electrodynamics and
elementary dynamical-systems reasoning—a mechanism by which two biological systems
can influence each other through ordinary electromagnetism via frequency and phase
structure, producing deterministic bias rather than mechanical force.

No nonlocality is assumed. No conservation laws are violated. No “energy-free
information” is invoked.

The core claim is narrow:

Two biological systems, treated as extended current distributions, can couple
through ordinary electromagnetic fields because time-structured currents generate
frequency-structured fields; receivers are spectrally selective (they compute
structured projections, not power); and near-critical regulatory subsystems can
convert small coherent structured drives into large state biases.

## Assumptions (minimal and explicit)

We assume only:

A1. Maxwellian electrodynamics. Electromagnetic fields satisfy the standard
Maxwell equations with sources in ordinary media. No exotic physics is introduced.

A2. Distributed biological sources. A biological system occupies a bounded region
Ω and is modeled by charge and current densities ρ(x,t), J(x,t).

A3. Linearity of propagation. For a fixed environment and operating point, the map
from sources to fields is linear and retarded (causal).

A4. Selective biological reception. The receiver does not respond to total field
power. It responds through specific internal couplings (filters/templates/projections).

A5. Near-critical gain (state dependence). At least one receiver subsystem operates
near a dynamical transition (bifurcation/metastability boundary) where susceptibility
to small biases is large.

A6. Adaptation/novelty sensitivity. Biological regulation suppresses steady signals
and emphasizes changes. This is receiver dynamics, not field nonlinearity.

Important clarification: “No threshold in Maxwell” does not mean “effects are automatic.”
Maxwell’s equations are linear; biological receivers are not. Thresholds enter through
integration time, adaptation, saturation, and state (A4–A6).

## Maxwell with sources as a linear retarded map

Let a sender generate source densities ρ(x,t), J(x,t). Maxwell’s equations
(with a generic linear medium description) are:

\[
\nabla\cdot D = \rho,\qquad \nabla\cdot B = 0
\]

\[
\nabla\times E = -\partial_t B,\qquad
\nabla\times H = J + \partial_t D
\]

with linearized constitutive relations around an operating point (possibly
frequency-dependent and lossy):

\[
D = \epsilon * E,\qquad B = \mu * H,\qquad J_{\text{cond}} = \sigma * E
\]

Here “*” denotes a causal linear response (convolution in time).

Definition (Maxwell map). For a fixed environment (geometry, objects, tissue state),
Maxwell’s equations define a causal linear operator:

\[
(E,B) = \mathcal{M}[\rho,J].
\]

Implication. Any change in source structure produces a proportional change in the field
structure at the receiver. There is no *field-theory* threshold; detectability is a
receiver question.

## Three coupling regimes (do not conflate them)

Biological coupling can occur through distinct Maxwell regimes:

1) Conducted coupling: currents/voltages transmitted through physical contact,
shared conductive paths, or common “ground-like” structures. This is often the
dominant channel in experimental artifacts.

2) Quasi-static near-field coupling: low-frequency electric and magnetic fields
extend into space without forming propagating plane waves. E and B are not locked as
in far-field radiation; geometry dominates.

3) Radiative far-field coupling: propagating waves where E and B are approximately
transverse and coupled as in standard radiation.

This framework does not require far-field radiation to be strong. Most biologically
relevant timescales suggest quasi-static and conducted pathways are primary unless
distance and frequency make radiation relevant.

## Time structure implies frequency structure (exact)

Any time-dependent current admits a Fourier representation:

\[
J(x,t) = \int_{-\infty}^{\infty} J(x,\omega)e^{-i\omega t}\,d\omega.
\]

This is an identity, not an approximation.

Theorem (spectral reweighting). Any modulation of timing in J(x,t) redistributes
energy across frequencies J(x,ω).

Proof. This is the Fourier transform property of multiplication/convolution. ∎

### Multiplicative modulation (equalizer interpretation)

If a physiological control variable q(t) scales a current component:

\[
J(x,t) = q(t)\,J_0(x,t),
\]

then in frequency space:

\[
J(x,\omega) = \int \tilde q(\omega-\omega')\,J_0(x,\omega')\,d\omega'.
\]

Implication. Many biological actions do not “add new energy by default”; they reallocate
spectral weight and phase organization under a fixed energy budget. This is a statement
about signal structure, not about violating conservation.

## Environment + tissue as a frequency- and phase-selective transform

Choose a receiver-side scalar observable y(t): induced loop current, voltage difference,
averaged field component, demodulated envelope, etc.

By linearity (for fixed receiver configuration):

\[
y(\omega) = H(\omega)\,s(\omega),
\]

where s(ω) is the relevant emitted field component at the receiver location, and H(ω)
is the full transfer function: space + objects + tissue + measurement coupling. H(ω)
encodes magnitude and phase.

Implication. Phase relations are transformed, not automatically destroyed. Whether they
survive is an empirical question about H(ω) and the receiver’s projection.

## What actually couples (the four-line chain)

To prevent misreadings, here is the entire mechanism in one place.

1) Sender chooses between structured source states \(J_A^{(i)}(t)\).

2) The environment produces receiver input \(y_B^{(i)}(t)\) via Maxwell:
\(J_A^{(i)} \mapsto (E,B) \mapsto y_B^{(i)}\) (linear, causal).

3) Receiver computes a matched projection (correlation) onto a template r(t) over a
window T:

\[
z^{(i)} = \int_0^T y_B^{(i)}(t)\,r(t)\,dt.
\]

4) A near-critical regulatory subsystem maps z(t) into a macroscopic state X(T).
Distinct \(J_A^{(i)}\) can yield distinguishable X(T) with nonzero reliability.

This is bias via structure. Not force via amplitude.

## Modal expansion (modes as coordinates, not ontology)

Pick any set of field patterns {φ_m(ω)} that efficiently represent the environment’s
response (multipoles, near-field patterns, guided patterns, eigenfunctions of a chosen
operator, etc.). Then:

\[
s(\omega) = \sum_m a_m(\omega)\,\phi_m(\omega),
\qquad
y(\omega) = \sum_m g_m(\omega)\,a_m(\omega).
\]

Definition (shared mode). A “shared mode” is any pattern φ_m that the sender can excite
and the receiver can project onto. No cavity is implied. “Mode” here is a coordinate
choice in a linear decomposition.

## Receiver selectivity: projection and integration

A biological receiver does not measure y(t) pointwise. It integrates structured
correlations.

Let r(t) be an internal template (rhythm, envelope, harmonic pattern, phase reference).
Define:

\[
z = \int_0^T y(t)\,r(t)\,dt.
\]

Theorem (coherent accumulation). If y(t) is phase-aligned with r(t), contributions add
coherently and z grows with T. If not, contributions partially cancel.

This is the basis of matched filtering and correlation detection. It is a statement about
projection, not about “mystery sensitivity.”

### Noise enters, but the observable matters

Let x(t) = y(t) + n(t) be receiver input including unresolved background. Then:

\[
z = \int_0^T x(t) r(t)\,dt = z_s + z_n.
\]

Unmatched background contributes incoherently; matched structure contributes coherently.
Amplitude sets accumulation rate; structure sets the sign and selectivity of z.

## Near-critical regulatory bias

Let X(t) be a regulatory variable in the receiver. Model:

\[
\dot X = F(X;\mu) + \lambda z(t).
\]

Operational meaning of “near-critical.” The system is near-critical when small perturbations
measurably change: switching probability between metastable states, variance, correlation
time, or basin selection near a bifurcation.

Toy normal form (pitchfork bias):

\[
\dot X = \mu X - X^3 + \lambda z.
\]

When μ is small and positive, multiple outcomes coexist. A small z tilts selection toward
one branch. The field does not “push”; it biases.

## Adaptation and novelty detection

Biological systems suppress steady inputs. A minimal form:

\[
u(t) = z(t) - \langle z\rangle_{\text{recent}}.
\]

Implications.

- Repeated identical signals fade.
- Small structured changes can dominate.
- Excess amplitude can be counterproductive because it saturates and reduces discrimination.

## What “information” means here (operational, pre-Shannon)

Definition (operational information). Information is present if distinct sender-controlled
structures lead to reliably distinguishable receiver outcomes.

Sender selects among states \(J^{(1)}(t),J^{(2)}(t),\dots\). These produce receiver outcomes
\(X^{(1)}(T),X^{(2)}(T),\dots\). If outcomes differ with reliability above chance under controls,
information has been transferred in the causal sense.

This does not require symbols, entropy, or conscious decoding.

Optional: Shannon capacity can be used only as a ceiling once a specific statistical model is
adopted, but it is not the mechanism.

## Quantitative feasibility bounds (placeholder, required)

This framework is not a claim of unlimited range or robustness.

Feasibility is constrained by:

- geometry and distance (which patterns survive to the receiver),
- bandwidth and coherence time (how long phase relations remain usable),
- integration window T (how long the receiver can accumulate),
- adaptation timescales (which structures are suppressed),
- saturation limits (when large inputs degrade selectivity),
- environmental scrambling (time-varying H(ω) and motion).

Any concrete application must estimate:

- expected receiver input amplitude in the relevant regime (conducted / near-field / far-field),
- expected coherence time relative to T,
- receiver susceptibility near transitions.

This document supplies the mechanism; feasibility requires numbers and experiments.

## Predictions (falsifiable)

All tests are designed to hold power fixed while manipulating structure.

1) Phase scrambling test: preserve power spectrum; scramble phase relative to template → effect collapses.

2) Template mismatch: small mismatch in receiver template or coupling path → sharp drop.

3) Coherence beats power: weak matched structure can outperform strong mismatched structure.

4) Overload: beyond linear range, increasing amplitude reduces discrimination.

5) Criticality gate: effects peak near transitions; far from transitions they weaken.

6) Novelty dependence: repetition suppresses effects; controlled variation restores them.

7) Geometry sensitivity: orientation/posture/placement yields sharp nulls and maxima.

## Limits (explicit)

This framework does not claim:

- arbitrary long-range symbolic communication,
- immunity to environmental disruption,
- violation of causal propagation,
- consciousness transfer.

It does claim:

- structure-sensitive coupling is physically allowed under ordinary Maxwell electrodynamics,
- receiver selectivity and criticality can make small structured drives behaviorally relevant,
- amplitude-only measurement is the wrong observable for this channel.

## Closing statement

The physics here is ordinary.

What is unusual is the choice of observable: projection and structure, not amplitude and power.

Living systems influence each other not by pushing harder, but by aligning structure
where sensitivity is high. If this is wrong, phase- and geometry-controlled experiments
will falsify it cleanly. If it is right, it will appear only when structure is respected
and receiver state is controlled.

---

# Appendix — Minimal formal chain

\[
(\rho,J)_A(t)
\;\xrightarrow{\text{Fourier}}\;
(\rho,J)_A(\omega)
\;\xrightarrow{\mathcal{M}(\omega)}\;
(E,B)(\omega)
\;\xrightarrow{\mathcal{K}}\;
y_B(\omega)
\;\xrightarrow{\langle \cdot, r\rangle_T}\;
z(t)
\;\xrightarrow{\text{near-critical dynamics}}\;
X(T).
\]

Each arrow is causal and defined. No new physics is introduced.
