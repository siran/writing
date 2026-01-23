---
title: Modal Electromagnetic Coupling Between Two Biological Antennas Near Criticality
subtitle: A Maxwellian Framework for Bias via Frequency Structure (WIP)
author: An M. Rodriguez, Alex Mercer, Alex Hankey (tbd), Elias Thorne
date: 2026-01-23
keywords: Maxwell theory, biological electromagnetism, modal coupling, frequency modulation, coherence, higher-order critical points, HOCP, bias, antenna theory, near-field, far-field, spectral structure, matched coupling, information
one-sentence-summary: Two extended biological current systems can couple through shared electromagnetic modes; frequency/phase structure selects the coupling channel, and near-critical regulatory dynamics can be biased by structured perturbations without violating Maxwell theory.
summary: We present a strict Maxwellian framework for how two biological systems (distributed current sources) can participate in a shared electromagnetic modal structure. The operative variable is frequency/phase structure: how energy is partitioned among joint modes and how phase relations persist, not “raw amplitude.” We show (i) how time-structured biological currents generate spectral and modal structure, (ii) how geometry and separation define shared modes, (iii) how modulation of currents shifts modal partition and phase, (iv) how a near-critical regulatory subsystem (HOCP-like) can act as a selective transducer of a particular modal channel, and (v) how this supports an information-theoretic view in which modulation and mode-partition can carry information independently of lexical content (e.g., tone/harmonics in voice). Two explicit toy examples are given: a line-of-centers standing-wave mode model and a deterministic critical-response model that makes “bias” precise without stochastic postulates.
---

# Modal Electromagnetic Coupling Between Two Biological Antennas Near Criticality

## Motivation

A recurring failure in discussions of long-range biological influence is the
fixation on *field strength* as if influence required mechanical force.

This is a category error.

In a linear field theory like Maxwell electromagnetism, the decisive question is
not “how big is the field,” but:

- Which modes are excited?
- How are their phases related?
- What part of the receiving system is actually coupled to those modes?
- Is the receiver operating near a critical point where small structured
  perturbations produce large regulatory consequences?

This document formalizes a minimal, source-free Maxwellian mechanism:

> Two extended biological current systems can couple through shared
> electromagnetic modes, and frequency/phase structure can bias near-critical
> regulatory dynamics in a receiving system.


Nothing nonlocal is assumed. No violations of causality occur. No “zero-energy
information” is required.

The aim is clarity: to state precisely what Maxwell theory permits and what it
logically implies can be done (given coupling), and what conditions are
necessary for an effect to be detectable.

---


## Assumptions

We assume only:

1. Classical electromagnetism in a source-free propagation region. “Source-free”
   here refers to the field in the region between bodies: outside the compact
   supports of biological currents, Maxwell’s vacuum equations hold. The
   biological systems themselves are treated as bounded current/charge
   distributions whose time-structure can be modulated within biological bounds
   (in frequency and spatiotemporal pattern).

2. Two localized biological current distributions (two bodies), each represented
   by charge/current sources confined to bounded regions:
   - region $\Omega_A$ with sources $(\rho_A,\mathbf{J}_A)$,
   - region $\Omega_B$ with sources $(\rho_B,\mathbf{J}_B)$.

3. Linearity and superposition. Fields from multiple sources add:

   $$
   \mathbf{E}=\mathbf{E}_A+\mathbf{E}_B,\qquad
   \mathbf{B}=\mathbf{B}_A+\mathbf{B}_B.
   $$

4. No constitutive medium is assumed for the propagation region (vacuum
   propagation law). Any biological tissue is part of source/receiver dynamics,
   not an external “dielectric background.” (If one adopts a Maxwell-universe
   ontology, “matter” itself is structured field; the coupling discussion below
   remains a discussion about field structure and boundary-like constraints.)

5. A near-critical receiver subsystem exists within $\Omega_B$ whose
   effective susceptibility to a particular perturbation channel is large
   (HOCP-like sensitivity). This is not Maxwell; it is the receiver’s internal
   regulatory physics.

No stochastic postulate is assumed. “Noise” refers only to unresolved
deterministic degrees of freedom in coarse descriptions.

---


## Maxwell equations and energy flow (baseline)

In the propagation region (outside the sources):

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

This continuity equation constrains bookkeeping; it does not choose which field
patterns exist. Patterns arise from source time-structure plus geometry.

---


## What “mode” means here (non-arbitrary)

A “mode” in this document is not a philosophical basis choice.

A “mode” means:

> A family of Maxwell solutions whose spatial structure is constrained by
> geometry and boundary-like conditions, with harmonic time dependence (or
> decomposable into harmonics).


In practice, such modes appear whenever there are:

- characteristic lengths (body size, separation distance),
- preferred orientations (dipole axis, spine direction),
- time scales (heart rhythm, neural oscillations, breathing),
- recurrent coupling or partial confinement (near-field storage, reflections,
  guided pathways, repeated interaction).

These define a *shared modal structure* between emitter and receiver.

---


## Step 1: time-structured biological currents imply spectral structure

Let a biological current distribution be $\mathbf{J}(\mathbf{x},t)$. This
generates fields via Maxwell theory with sources.

The exact statement needed is only:

- physiology/practice can modulate $\mathbf{J}$ in time.

Write the temporal Fourier transform:

$$
\mathbf{J}(\mathbf{x},t)=\int_{-\infty}^{\infty}\mathbf{J}(\mathbf{x},\omega)e^{-i\omega t}\,d\omega,
$$

$$
\mathbf{J}(\mathbf{x},\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathbf{J}(\mathbf{x},t)e^{i\omega t}\,dt.
$$

This is exact. It converts “time modulation” into “redistribution across
frequencies.”


### Multiplicative modulation yields convolution (exact)

If a control variable $q(t)$ modulates the current:

$$
\mathbf{J}(\mathbf{x},t)=q(t)\,\mathbf{J}_0(\mathbf{x},t),
$$

then in frequency space:

$$
\mathbf{J}(\mathbf{x},\omega)=\int \tilde q(\omega-\omega')\,\mathbf{J}_0(\mathbf{x},\omega')\,d\omega',
$$

where $\tilde q$ is the Fourier transform of $q$.

This is the exact mathematical content of “frequency modulation by practice”:
changing $q(t)$ changes spectral weight distribution, hence which
frequency channels are occupied.

---


## Step 2: fields superpose, but energy flow depends on phase structure

Superposition is linear:

$$
\mathbf{E}=\mathbf{E}_A+\mathbf{E}_B,\qquad \mathbf{B}=\mathbf{B}_A+\mathbf{B}_B.
$$

But observables like energy density are quadratic:

$$
u = \frac{\epsilon_0}{2}|\mathbf{E}_A+\mathbf{E}_B|^2
  + \frac{1}{2\mu_0}|\mathbf{B}_A+\mathbf{B}_B|^2.
$$

Expanding:

$$
|\mathbf{E}_A+\mathbf{E}_B|^2 = |\mathbf{E}_A|^2+|\mathbf{E}_B|^2
+2\,\mathbf{E}_A\cdot \mathbf{E}_B,
$$

(and similarly for $\mathbf{B}$).

The cross-terms encode relative phase. They vanish only when phases decorrelate
or average out. This is why “structure” matters: stable phase relations alter
energy flow patterns without introducing new physics.

---


## Step 3: the receiver responds through a selective coupling functional

A biological receiver does not respond to the entire field; it responds through
specific couplings.

A minimal physical coupling density is Lorentz force density:

$$
\mathbf{f}=\rho\mathbf{E}+\mathbf{J}\times\mathbf{B}.
$$

But regulatory effects typically arise through induced potentials, timing,
entrainment, and internal transduction. Abstractly, define a receiver observable
$Y(t)$ as a functional of the field restricted to $\Omega_B$:

$$
Y(t)=\mathcal{K}\bigl[\mathbf{E}(\cdot,t),\mathbf{B}(\cdot,t)\bigr].
$$

Here $\mathcal{K}$ represents geometry + internal transduction. “Mode
selectivity” is the statement that $\mathcal{K}$ has much larger response to
some time-structures than others (matched channels).

Near criticality, a subsystem can make $\mathcal{K}$ extremely selective.

---


## Step 4: from frequency structure to shared mode structure

We now connect frequency structure to *shared modes*.

The receiver’s coupling is not to “frequency in the abstract” but to frequency
*as realized in spatial field patterns* that actually exist between A and B.

The minimal conceptual bridge is:

1. A time-structured source generates a spectrum.
2. The environment + geometry defines a set of allowable spatial patterns at
   each frequency (solutions of Maxwell with those boundary-like constraints).
3. The realized field is the superposition of those patterns weighted by how the
   source projects onto them.

This is the same logic as cavity/waveguide physics: source projects onto modes.

---


## Example 1: line-of-centers standing-wave toy model

Take the line segment joining two localized sources, idealized as “nodes” at
$x=0$ and $x=r$.

A wave equation analogue on $[0,r]$ has standing modes:

$$
\phi_m(x,t)=a_m \sin\left(\frac{m\pi x}{r}\right)\cos(\omega_m t+\varphi_m),
$$

with

$$
\omega_m = c\frac{m\pi}{r}.
$$

This is not the full Maxwell field. It is a toy model that isolates one
essential point:

- geometry and separation define spatial patterns and frequency scales.

The *interaction channel* is not “amplitude,” but:

- which $m$ are populated,
- the phases $\varphi_m$,
- how the receiver couples to $\phi_m$.

In a full Maxwell setting, the spatial patterns are vector fields and the mode
spectrum depends on 3D geometry; the same logic holds.


### Modal partition as the meaningful variable

In any linear wave system with orthogonal modes, total energy partitions:

$$
W = \sum_m W_m.
$$

Changing the source time-structure changes the distribution across the
$W_m$. A receiver can detect changes in the partition (or in phase
relations) even if total energy is unchanged.

This is the “more information than words” point in physical terms.

---


## Step 5: Maxwell response maps source spectrum to field modal coefficients

In frequency space, Maxwell theory with sources gives a linear mapping from
$(\rho,\mathbf{J})$ to $(\mathbf{E},\mathbf{B})$:

$$
(\mathbf{E},\mathbf{B})(\omega)=\mathcal{L}(\omega)\,(\rho,\mathbf{J})(\omega),
$$

for a linear operator $\mathcal{L}(\omega)$ determined by Green’s functions and
the geometry/boundary constraints of the environment.

Now represent the field at each frequency as a sum over spatial mode patterns
$\{\mathbf{E}_m(\mathbf{x};\omega),\mathbf{B}_m(\mathbf{x};\omega)\}$:

$$
\mathbf{E}(\mathbf{x},\omega)=\sum_m c_m(\omega)\,\mathbf{E}_m(\mathbf{x};\omega),
$$

$$
\mathbf{B}(\mathbf{x},\omega)=\sum_m c_m(\omega)\,\mathbf{B}_m(\mathbf{x};\omega).
$$

The coefficients $c_m(\omega)$ are determined by how the sources project onto
those modes.

Time-domain fields follow by inverse transform. One convenient representation is
envelope form:

$$
\mathbf{E}(\mathbf{x},t)=\sum_m \Re\{ \alpha_m(t)\,\mathbf{E}_m(\mathbf{x}) e^{-i\omega_m t}\},
$$

$$
\mathbf{B}(\mathbf{x},t)=\sum_m \Re\{ \alpha_m(t)\,\mathbf{B}_m(\mathbf{x}) e^{-i\omega_m t}\}.
$$

The chain is exact in content:

$$
\text{practice/attention} \to \mathbf{J}_A(t)
\to \mathbf{J}_A(\omega)
\to c_m(\omega)
\to \alpha_m(t).
$$

The difficulty is computational (real geometry), not conceptual.

---


## Step 6: near-critical receiver converts modal shifts into deterministic bias

Let $x(t)$ denote a receiver regulatory variable. Model its evolution
as:

$$
\dot x = F(x) + \lambda\, y(t),
$$

where $y(t)$ is the EM drive channel induced by the field, and
$\lambda$ is a coupling constant determined by biology.

Let $y(t)$ be a projection onto a receiver-sensitive modal channel:

$$
y(t)=\langle \mathcal{K}, \mathbf{E}(\cdot,t),\mathbf{B}(\cdot,t)\rangle.
$$

Near criticality, effective susceptibility

$$
\chi_{\text{eff}}=\frac{\partial x}{\partial y}
$$

can become large. Operationally: small changes in $y$ select
different trajectories or outcomes.

If $\mathcal{K}$ is selective for a particular mode $m_*$, then:

$$
y(t)\approx \Re\{\alpha_{m_*}(t)e^{-i\omega_{m_*}t}\}.
$$

Thus:
- modulation of $\mathbf{J}_A(t)$ changes $\alpha_{m_*}(t)$,
- this changes $y(t)$,
- near criticality, this changes the receiver’s trajectory.

The result is deterministic: it is the integrated consequence of competing field
contributions and internal dynamics.

---


## Example 2: explicit deterministic critical selection model

Consider a pitchfork-like selection normal form:

$$
\dot x = \mu x - x^3 + \lambda y(t),
$$

with $\mu$ measuring distance to criticality.

For $\mu>0$ and $y=0$, equilibria are $x=\pm\sqrt{\mu}$
(degenerate branches).

A bias term $y$ breaks symmetry. For constant $y(t)=y_0$
equilibria satisfy:

$$
0=\mu x - x^3 + \lambda y_0.
$$

The sign and structure of $y_0$ selects the branch. If
$y_0$ is a demodulated component of $\alpha_{m_*}(t)$, then:

- changing modal structure changes the selected regulatory branch.

This is a deterministic statement: no randomness is required.

---


## Voice, tone, harmonics: information in spectral partition (beyond words)

A sustained note can carry information in the distribution of its frequency
components even if total radiated energy is held fixed.

In signal terms: different spectra can have the same total power. In physical
terms: different mode partitions can have the same total energy.

Let $s(t)$ be a signal (e.g., a vocal waveform, or any physiological
modulation waveform). Its power spectral density is $P(\omega)=|S(\omega)|^2$.

Two different signals $s_1,s_2$ can satisfy:

$$
\int |S_1(\omega)|^2\,d\omega = \int |S_2(\omega)|^2\,d\omega,
$$

while having different distributions $|S_1(\omega)|^2 \neq |S_2(\omega)|^2$.

This means: identical total energy, different spectral structure.

A receiver with mode-selective coupling $\mathcal{K}$ can respond differently
to these signals because $\mathcal{K}$ effectively weights frequencies and
phases.


### Information-theoretic framing (minimal)

If a sender chooses among distinct modulation states (distinct spectral
partitions or phase relations) and the receiver has a reliable way to map those
states to distinguishable internal responses, then a communication channel
exists.

In Shannon terms, the capacity depends on:

- how many distinguishable states can be produced by the sender (modulation
  repertoire),
- how selectively the receiver responds (matched coupling),
- how stable the shared modal structure is over time.

The physical point is prior to Shannon: Maxwell provides the carrier; modal
structure provides the alphabet; near-critical selectivity provides gain.

(Shannon analysis can be layered on once the state space and discrimination
mechanism are defined.)

---


## Why shared music can assist coupling (a physical statement)

Listening to the same structured sound piece can act as an external reference
that entrains:

- breathing rhythms,
- heart-rate variability patterns,
- neural oscillatory bands,
- vocal tract posture and muscle tension (even silently).

This can make internal current patterns more phase-structured relative to the
same template in both bodies, which increases the persistence of cross-terms and
stabilizes shared mode selection.

The role is not “power,” but “structure alignment.”

---


## What is allowed or logically implied (tight statement)

### Allowed / implied by Maxwell + coupling

- Time-structured currents generate frequency-structured fields.
- Geometry determines which spatial patterns (modes) are effectively supported.
- Source modulation reshapes spectral weight and hence modal coefficients.
- Receivers respond through specific couplings (functionals of the field).
- Near criticality, selective couplings can have large regulatory consequences.


### What remains empirical

- Whether the relevant shared modes exist with sufficient stability in real
  environments.
- Whether biological HOCP-like subsystems exist and couple to the right channels
  in the necessary way.
- Quantitative effect sizes and ranges.

---


## Minimal experimental posture (conceptual)

The decisive tests are structural:

- Do practice-induced physiological changes produce measurable changes in
  spectral/mode partition of emitted fields?
- Can a receiver’s near-critical subsystem be shown to respond selectively to a
  structured drive channel correlated with that partition?
- Does shared entrainment (shared rhythm/music) measurably increase coherence of
  relevant cross-terms or matched projections?

These tests target the actual claim: frequency-structural coupling and bias.

---


## Summary (single statement)

Two extended biological current systems can participate in a shared Maxwellian
modal structure. Practice and physiology modulate source currents, which
deterministically redistributes spectral weight across joint modes and alters
phase relations. A receiver with a near-critical regulatory subsystem can be
selectively sensitive to a particular modal channel, converting small modal
shifts into deterministic bias in regulatory evolution. The mechanism is
frequency-structural rather than force-based, and assumes no nonlocality and no
violations of causality.
