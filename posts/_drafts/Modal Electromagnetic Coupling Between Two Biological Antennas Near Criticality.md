---
title: Modal Electromagnetic Coupling Between Two Biological Antennas Near Criticality
subtitle: WIP - A Maxwellian Framework for Bias via Frequency Structure
author: An M. Rodriguez, Alex Mercer, Alex Hankey (tbd by him), Elias Thorne
date: 2026-01-23
keywords: Maxwell theory, biological electromagnetism, modal coupling, frequency modulation, coherence, higher-order critical points, HOCP, bias, antenna theory, near-field, far-field
one-sentence-summary: Two extended biological current systems can couple through shared electromagnetic modes; frequency/phase structure—rather than amplitude—selects the coupling channel, and near-critical regulatory dynamics can be biased by small structured perturbations without violating Maxwell theory.
summary: We present a strict Maxwellian framework for how two biological systems (treated as distributed current sources) can participate in a shared electromagnetic modal structure. The key variable is not field amplitude but the frequency/phase structure that selects which joint modes are occupied and how energy is partitioned among them. We show (i) how time-structured biological currents generate a modal spectrum, (ii) how geometry and separation define shared modes, (iii) how frequency modulation of sources shifts modal occupation and phase, and (iv) how a higher-order critical regulatory subsystem can act as a selective, high-gain transducer for perturbations in a specific mode. We include explicit derivations where needed and give two concrete toy examples: a 1D line-of-centers standing-wave mode and a coupled-oscillator/critical-response model that makes the “bias” notion precise without probabilistic postulates.
---

# Modal Electromagnetic Coupling Between Two Biological Antennas Near Criticality

## Motivation

A recurring failure in discussions of long-range biological influence is the
fixation on *field strength* as if influence required mechanical force.

This is a category error.

In a linear field theory like Maxwell electromagnetism, the decisive question is
not “how big is the field,” but:

- **Which modes are excited?**
- **How are their phases related?**
- **What part of the receiving system is actually coupled to those modes?**
- **Is the receiver operating near a critical point where small structured
  perturbations produce large regulatory consequences?**

This document formalizes a minimal, source-free Maxwellian mechanism:

> Two extended biological current systems can couple through shared
> electromagnetic modes, and frequency/phase structure can bias near-critical
> regulatory dynamics in a receiving system.


Nothing nonlocal is assumed. No violations of causality occur. No “zero-energy
information” is required.

The aim is clarity: to state precisely not only what Maxwell theory permits, but
it logically *implies* can be done, rigorously and without hand-waiving, and
what conditions are necessary for an effect to be detectable.


## Assumptions

We assume only:

1. **Classical electromagnetism in a source-free propagation region.**
   “Source-free” here means: there are no sources; biologogic systems are
   treated as current loops, that can be modulated between known, calculatable,
   biological, physical bounds, both in amplitude, frequency and "shape" (think
   of regulating flow on stomach vs throat, vs even singing, humming,..)

2. **Two localized biological current distributions** (two bodies), each
   represented by charge/current sources confined to bounded regions:
   - region $\Omega_A$ which "sources" the radiation profile
     $(\rho_A,\mathbf{J}_A)$
   - region $\Omega_B$ which "sources" the radiation profile
     $(\rho_B,\mathbf{J}_B)$

3. **Linearity and superposition.** Fields from multiple sources add:
   $$\mathbf{E}=\mathbf{E}_A+\mathbf{E}_B,\qquad \mathbf{B}=\mathbf{B}_A+\mathbf{B}_B.$$

4. **No constitutive medium is assumed** for the propagation region (vacuum
   propagation law). Any biological tissue is part of the sources and receiver
   dynamics, not an external “dielectric background.” Also, everything --
   "matter", in a modulation in the field: matter is a knot of energy flow, so
   this electromagnetic modes use them as transport medium... even diffusive
   media do not diffuse frequency structures...

5. **A near-critical receiver subsystem** exists within $\Omega_B$ whose
   effective susceptibility to a particular perturbation channel is large
   (HOCP-like sensitivity). This is not Maxwell; it is the receiver’s internal
   regulatory physics.

We do not assume any stochastic postulate, since Maxwell equations are fully
deterministic. Energy doesn't "escape" the system mysteriously. So, “noise” as
unresolved deterministic degrees of freedom can be disregarded.


## Maxwell equations and energy flow (baseline)

In the propagation region:

$$
\nabla\cdot \mathbf{E}=0,\qquad \nabla\cdot \mathbf{B}=0,
$$

$$
\nabla\times \mathbf{E}=-\partial_t \mathbf{B},\qquad
\nabla\times \mathbf{B}=\mu_0\epsilon_0\,\partial_t \mathbf{E}.
$$

Energy density $u$ and Poynting flux $\mathbf{S}$ are:

$$
u=\frac{\epsilon_0}{2}|\mathbf{E}|^2+\frac{1}{2\mu_0}|\mathbf{B}|^2,\qquad
\mathbf{S}=\frac{1}{\mu_0}\mathbf{E}\times \mathbf{B}.
$$

Energy continuity (Poynting theorem) in vacuum:

$$
\partial_t u+\nabla\cdot \mathbf{S}=0.
$$

This is bookkeeping. It does not choose which modes exist; boundary conditions
and sources do.


## What “mode” means here (non-arbitrary)

A “mode” in this document is not a philosophical basis choice.

A “mode” means:

> A solution family to Maxwell’s equations whose spatial structure is fixed by
> geometry and boundary-like constraints, and whose time dependence is harmonic
> (or decomposable into harmonics).


In practice, modes appear whenever:

- there are characteristic lengths (body size, separation distance),
- there are preferred orientations (dipole axes, spine direction),
- there are time scales (heart rhythm, neural oscillations),
- the environment supports standing or quasi-standing patterns (near-field
  reactive storage, partial reflections, recurrent coupling).

These define a *shared modal structure* between emitter and receiver.


## Step 1: biological currents are time-structured sources

A time-varying current distribution $\mathbf{J}(\mathbf{x},t)$ generates
electromagnetic radiation.

We do not need to guess microscopic details. We only need the fact:

- physiology and practice modulate $\mathbf{J}$ in time.

Write the source current as a sum of temporal components (Fourier decomposition
in time):

$$
\mathbf{J}(\mathbf{x},t)=\int_{-\infty}^{\infty}\mathbf{J}(\mathbf{x},\omega)e^{-i\omega t}\,d\omega,
$$

where

$$
\mathbf{J}(\mathbf{x},\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathbf{J}(\mathbf{x},t)e^{i\omega t}\,dt.
$$

This is exact.

Now the key point: **modulating physiology modulates spectral weight**. For
example, if a physiological control variable $q(t)$ modulates the
current:

$$
\mathbf{J}(\mathbf{x},t)=q(t)\,\mathbf{J}_0(\mathbf{x},t),
$$

then the spectrum is a convolution:

$$
\mathbf{J}(\mathbf{x},\omega) = \int \tilde q(\omega-\omega')\,\mathbf{J}_0(\mathbf{x},\omega')\,d\omega',
$$

where $\tilde q$ is the Fourier transform of $q$.

This is the core “frequency modulation” mechanism in strict terms:
- changing $q(t)$ changes the distribution of energy across
  frequencies.

No amplitude language is needed. What changes is *spectral structure*.


## Step 2: Maxwell is linear, but observables depend on the total field

Superposition is a statement about fields:
$$\mathbf{E}=\mathbf{E}_A+\mathbf{E}_B.$$

But the energy density is quadratic:

$$
u = \frac{\epsilon_0}{2}|\mathbf{E}_A+\mathbf{E}_B|^2 + \frac{1}{2\mu_0}|\mathbf{B}_A+\mathbf{B}_B|^2.
$$

Expanding:

$$
|\mathbf{E}_A+\mathbf{E}_B|^2 = |\mathbf{E}_A|^2+|\mathbf{E}_B|^2+2\,\mathbf{E}_A\cdot \mathbf{E}_B,
$$

and similarly for $\mathbf{B}$.

The cross-terms encode **phase relations**. They vanish only when phases average
out.

Thus:
- linearity does not mean “no interaction” at the level of energy flow.
- it means fields add, and the *pattern* can change because quadratic
  observables include cross-terms.

This is why frequency/phase structure matters.


## Step 3: the receiver sees a *filtered projection* of the field

A biological receiver does not respond to “the field everywhere.” It responds
through specific coupling channels.

At the simplest Maxwellian level, charges and currents respond via Lorentz force
density:

$$
\mathbf{f}=\rho\mathbf{E}+\mathbf{J}\times\mathbf{B}.
$$

But in a regulatory subsystem, the relevant quantity is often some *functional*
of the fields over a region (e.g., induced potential differences, timing of
threshold crossings, phase-locking of endogenous oscillators).

Abstractly: define a receiver observable $Y(t)$ as a functional of the
field restricted to $\Omega_B$:

$$
Y(t)=\mathcal{K}\bigl[\mathbf{E}(\cdot,t),\mathbf{B}(\cdot,t)\bigr].
$$

The operator $\mathcal{K}$ encodes biological coupling geometry and internal
transduction.

This is where “mode selectivity” enters:
- $\mathcal{K}$ behaves like a filter or matched detector for certain time
  structures.

A near-critical subsystem can make $\mathcal{K}$ extremely sensitive to a
narrow structured channel.


## Step 4: shared modal structure between two sources

Now we formalize the “shared mode” idea in the simplest possible setting.


### Example 1 (one-dimensional line-of-centers standing mode)

Consider the line segment joining two localized sources, idealized as “nodes” at
positions $x=0$ (source A) and $x=r$ (source B).

A simple wave equation analogue on $[0,r]$ has standing modes:

$$
\phi_m(x,t)=a_m \sin\left(\frac{m\pi x}{r}\right)\cos(\omega_m t+\varphi_m),
$$

with

$$
\omega_m = c\frac{m\pi}{r}.
$$

This is not the full Maxwell field; it is a controlled toy model capturing a
real point:
- geometry and separation define discrete spatial patterns and frequencies.

Now connect it to fields:

In Maxwell, a similar role is played by field patterns that are recurrently
reinforced by source geometry, near-field storage, and partial reflections in
the environment.

The exact modal structure in real 3D is more complicated, but the logic is the
same:
- shared geometry defines families of patterns with well-defined frequency
  content.

The key variable is not “how big is $a_m$,” but:
- which $m$ are present,
- how their phases $\varphi_m$ align,
- how the receiver’s coupling operator $\mathcal{K}$ projects onto these
  modes.


### Modal energy partition

In any linear wave system with orthogonal modes, total energy decomposes as:

$$
W = \sum_m W_m,
$$

with each $W_m$ determined by modal amplitude and geometry.

This is the structural point:
- changing the source’s temporal structure changes how energy is distributed
  among the $W_m$.
- the receiver can be sensitive to *changes in modal partition* even when total
  emitted energy does not change.

That is “frequency-based transport” in the sense you mean.


## Step 5: frequency modulation as redistribution of modal occupation

Let the emitted field in a shared region be expanded in a set of
geometry-defined mode fields
$\{\mathbf{E}_m(\mathbf{x}),\mathbf{B}_m(\mathbf{x})\}$:

$$
\mathbf{E}(\mathbf{x},t)=\sum_m \Re\{ \alpha_m(t)\,\mathbf{E}_m(\mathbf{x}) e^{-i\omega_m t}\},
$$

$$
\mathbf{B}(\mathbf{x},t)=\sum_m \Re\{ \alpha_m(t)\,\mathbf{B}_m(\mathbf{x}) e^{-i\omega_m t}\}.
$$

Here:
- $\omega_m$ are mode frequencies determined by geometry and environment.
- $\alpha_m(t)$ are slowly varying complex envelopes (exactly: any
  sufficiently regular signal can be represented this way).

Now how does a source modulate $\alpha_m(t)$?

Because the source current has spectral content. In the frequency domain,
Maxwell’s equations yield linear response:

$$
(\mathbf{E},\mathbf{B})(\omega) = \mathcal{L}(\omega)\,(\rho,\mathbf{J})(\omega),
$$

for a linear operator $\mathcal{L}(\omega)$ determined by Green’s functions and
boundary conditions.

Therefore:
- changing $\mathbf{J}_A(\omega)$ changes the coefficients with which modes are
  excited.
- a time modulation in physiology changes $\mathbf{J}_A(\omega)$, hence changes
  $\alpha_m$.

This is an exact chain:

$$
\text{practice/attention} \to \mathbf{J}_A(t) \to \mathbf{J}_A(\omega) \to \{\alpha_m\}.
$$

No approximation is required in principle; the only complication is that
$\mathcal{L}$ is hard to compute in real geometry.


## Step 6: how a near-critical receiver converts modal shifts into bias

We now define “bias” precisely without probabilistic postulates.

Let $x(t)$ denote a regulatory variable in the receiver (in
$\Omega_B$). Let its dynamics be:

$$
\dot x = F(x) + \lambda\, y(t),
$$

where:
- $F$ is the internal regulatory law,
- $y(t)$ is the electromagnetically induced drive channel,
- $\lambda$ is a coupling constant determined by biology.

Assume $y(t)$ is a projection of the fields onto a receiver-sensitive
mode channel:

$$
y(t) = \langle \mathcal{K}, \mathbf{E}(\cdot,t),\mathbf{B}(\cdot,t)\rangle.
$$

Near criticality, the system has a sharp response: small changes in
$y(t)$ shift outcomes.

A generic way to encode “critical sensitivity” is that the effective
susceptibility

$$
\chi_{\text{eff}} = \frac{\partial x}{\partial y}
$$

becomes large in some operating regime.

In HOCP language: the regulatory manifold has near-degenerate directions where
small perturbations select one branch.

In this document we do not need HOCP microphysics; we only need the operational
fact:
- near a critical point, the receiver’s response to a specific drive channel is
  high.

Now connect to modes:

If

$$
y(t) \approx \Re\{\alpha_{m_*}(t)e^{-i\omega_{m_*}t}\},
$$

because $\mathcal{K}$ is selective for mode $m_*$, then:

- changing $\alpha_{m_*}(t)$ changes $y(t)$,
- near criticality, small changes in $y$ alter the trajectory of
  $x(t)$,
- that altered trajectory is what we call *bias*.

This is deterministic: the “drift” is the integrated result of coupled dynamics.


## Example 2 (explicit critical-response toy model)

Consider a normal form for a pitchfork-like critical selection:

$$
\dot x = \mu x - x^3 + \lambda y(t),
$$

where:
- $\mu$ measures distance to criticality ($\mu\approx 0$ is
  critical),
- $y(t)$ is the EM drive channel.

When $\mu>0$ and $y=0$, equilibria are $x=\pm\sqrt{\mu}$
(degenerate branches). A small $y$ breaks symmetry and selects one
branch.

In steady drive $y(t)=y_0$: equilibria satisfy

$$
0=\mu x - x^3 + \lambda y_0.
$$

For small $y_0$, the selected equilibrium shifts. The sign of
$y_0$ chooses which branch is favored.

Now if $y_0$ is the time-average of a mode envelope $\alpha_{m_*}(t)$
(or a demodulated component of it), then:

> a small change in modal occupation/phase can select a different regulatory
> branch.


No probability is needed. This is a deterministic bifurcation selection.

This is the exact mathematical sense of “bias near criticality.”


## Why shared rhythm and music matter (mode selection, not amplitude)

A shared external rhythm (breathing together, synchronized pulse, listening to a
complex but common sound structure) can act as a *reference* that stabilizes and
aligns internal current modulations.

Maxwellian translation:
- the sources’ currents become more phase-structured and spectrally organized
  relative to a common template.

This has two consequences:

1. **Mode alignment:** the set of excited modes $\{\omega_m\}$ becomes more
   similar between A and B.
2. **Phase coherence:** cross-terms like $\mathbf{E}_A\cdot \mathbf{E}_B$ become
   persistent rather than averaging out.

Thus, shared practice is not “sending energy.” It is **synchronizing the
spectral/mode structure that defines the coupling channel.**


## What is allowed or logically rigorously implied

### Allowed by Maxwell theory

- Two biological current systems radiate fields.
- Fields superpose.
- Quadratic observables (energy flow, induced drive channels) contain
  phase-dependent cross-terms.
- Source modulation changes spectral content, hence modal occupation.
- A selective receiver can respond strongly to a narrow structured channel.
- Near criticality, small structured perturbations can select outcomes.

None of this violates Maxwell theory.


## Minimal experimental posture (conceptual)

If one were to test this framework in a controlled way, the relevant observables
are not “force” or “motion,” but:

- spectral changes in emitted fields correlated with practice,
- phase-coherence measures between two systems,
- receiver-side changes specifically near critical regulatory regimes,
- demodulated signatures that track mode envelopes $\alpha_m(t)$.

The key prediction is modal/phase structure dependence:
- effects track shared time-structure more than raw field magnitude.


## Summary (single statement)

Maxwell theory supplies a linear, local field substrate in which extended
time-varying biological currents generate frequency-structured radiation.
Geometry and separation define shared electromagnetic mode families; physiology
and practice modulate the spectral distribution across those modes. A receiver
operating near a higher-order critical point can be selectively sensitive to
perturbations in a specific mode channel, converting small changes in modal
occupation/phase into deterministic bias in regulatory trajectories. The
mechanism is frequency-structural, not force-based, and requires no nonlocality
or violations of causality.
