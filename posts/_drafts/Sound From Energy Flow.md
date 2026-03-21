---
title: Sound From Energy Flow
subtitle: Deriving the Acoustic Wave Equation from Source-Free Maxwell Transport
author: An M. Rodriguez
date: 2026-03-20
one-sentence-summary: The sound wave equation is not an independent mechanical law but the coarse-grained, longitudinal mode of the electromagnetic wave equation acting on a medium of organized toroidal closures, with propagation speed, dispersion, and dissipation all set by the electromagnetic structure of the medium.
summary: In a source-free Maxwell universe, matter is aggregate toroidal closures of electromagnetic energy flow. A perturbation in the arrangement of these closures propagates via their primary coupling — the axial charge interaction — and the continuum limit of that propagation is exactly the acoustic wave equation. The operator structure is inherited from the EM wave equation; the propagation speed is derived from the charge coupling stiffness and the trapped-energy mass density, both of which are electromagnetic quantities. Dissipation occurs when the driving frequency excites partial internal circulations that do not re-close into stable modes; below the internal resonance threshold the propagation is lossless and elastic; in the fully coherent limit this recovers dissipation-free propagation — superfluidity — without additional postulates. No mechanical postulate enters at any step. Acoustics is recovered as a slow, longitudinal, coarse-grained regime of Maxwell transport.
keywords:
  - sound
  - acoustic wave equation
  - source-free Maxwell
  - energy flow
  - toroidal closure
  - charge coupling
  - dispersion
  - dissipation
  - superfluid
---


## Purpose

To show that the acoustic wave equation

$$
\partial_t^2 p - v_s^2\,\nabla^2 p = 0
$$

is not an independent postulate. It is the coarse-grained, longitudinal mode of
the electromagnetic wave equation

$$
\partial_t^2 \mathbf{F} - c^2\,\nabla^2 \mathbf{F} = 0
$$

acting on a medium whose constituents are organized electromagnetic closures.
No mechanical laws are introduced. The operator form, the propagation speed,
and the conditions under which $v_s \ll c$ all follow from source-free Maxwell
transport and the topology of self-sustaining configurations.


## The medium

In a source-free Maxwell universe, stable matter is aggregate toroidal closures
of electromagnetic energy flow. Each toroidal closure is characterized by a
winding pair $(m, n)$ — charge and spin as topological invariants — and a
scalar amplitude of trapped energy $E$. Its mass is

$$
M = E/c^2.
$$

Its exterior carries an axial charge field that falls as $1/r^2$, sustained by
the non-contractible through-hole flux of the winding.

A bulk material is a regular arrangement of $n$ such toroids per unit volume,
at equilibrium separation $d_0 \sim n^{-1/3}$.


## The perturbation

Displace the toroid centered at position $\mathbf{x}$ by a small vector
$\boldsymbol{\xi}(\mathbf{x}, t)$ from its equilibrium position. The restoring
force on it from its neighbors comes from the axial charge coupling.

The interaction energy between two toroidal axial charge fields at separation
$d$ is of the form

$$
U(d) \sim -\frac{Q^2}{d},
$$

where $Q$ is the through-hole flux strength fixed by the winding number $m$.
At equilibrium separation $d_0$, opposite-sign and same-sign contributions
balance. For a small displacement $\xi$ from equilibrium along the axis:

$$
U(d_0 + \xi) \approx U(d_0) + \tfrac{1}{2}\,U''(d_0)\,\xi^2,
$$

with

$$
U''(d_0) \sim \frac{Q^2}{d_0^3} > 0.
$$

The restoring stiffness per toroid is

$$
K_\text{local} \sim \frac{Q^2}{d_0^3}.
$$

This is a purely electromagnetic quantity: $Q$ is the axial winding flux, $d_0$
is the equilibrium spacing set by the balance of charge repulsion and spin
attraction between neighboring toroids.


## Continuum limit: the wave equation

Pass to the continuum. With $n$ toroids per unit volume:

$$
\rho = n\,M = \frac{nE}{c^2}
\qquad\text{(mass density, from aggregate trapped EM energy)}
$$

$$
K = n\,K_\text{local}
\qquad\text{(bulk stiffness, from charge coupling between neighbors)}
$$

The equation of motion for the displacement field becomes, in the continuum limit,

$$
\rho\,\partial_t^2\,\boldsymbol{\xi} = K\,\nabla^2\boldsymbol{\xi}.
$$

This is a wave equation. The propagation speed is

$$
\boxed{v_s = \sqrt{\frac{K}{\rho}}.}
$$

Both $K$ and $\rho$ are derived from the electromagnetic structure of the
toroids. No mechanical postulate enters.

For the longitudinal mode, take the divergence $p \propto \nabla \cdot
\boldsymbol{\xi}$. This gives

$$
\partial_t^2 p - v_s^2\,\nabla^2 p = 0.
$$

This is the sound wave equation, recovered from EM.


## The operator identity

The electromagnetic wave equation:

$$
\partial_t^2 \mathbf{F} - c^2\,\nabla^2 \mathbf{F} = 0
$$

The acoustic wave equation:

$$
\partial_t^2 p - v_s^2\,\nabla^2 p = 0
$$

Same operator $\partial_t^2 - v^2\,\nabla^2$; different speed. This is not a
coincidence. The sound wave equation is the coarse-grained version of the EM
wave equation: the operator structure is inherited, and only the speed changes.
The change in speed is itself derived from the EM constitution of the medium.


## Why $v_s \ll c$ is forced

$$
\frac{v_s^2}{c^2} = \frac{K}{\rho\,c^2} = \frac{K_\text{local}}{M c^2}
= \frac{Q^2 / d_0^3}{E}.
$$

$Q^2/d_0^3$ is the interaction energy gradient between neighboring toroids —
a near-field quantity set by the charge coupling at separation $d_0$. $E$ is
the full self-energy of a single toroid. For the medium to be stable (toroids
not merging, not dissolving), the coupling energy between neighbors must be much
less than the self-energy of each toroid. Therefore

$$
\frac{Q^2}{d_0^3} \ll E \quad \Rightarrow \quad v_s \ll c.
$$

The inequality $v_s \ll c$ is not a parameter choice. It is forced by the
stability of the medium: a bulk material of toroidal closures must have
inter-toroid coupling weaker than toroid self-energy, or it would not be a
stable arrangement of distinct closures at all.


## Dissipation and its disappearance

Dissipation occurs when the driving perturbation excites partial internal
circulations within the toroidal closures that do not re-close into stable
modes. Those open circulations — circulation that does not fold back on itself
— radiate outward as electromagnetic transport. What acoustics calls thermal
dissipation is, at the electromagnetic level, radiation from partial
non-closing circulations. The energy returns to the EM field, not to a
separate thermal substance.

Whether this happens depends on the driving frequency relative to the internal
mode structure of the toroids. Each toroidal closure has a discrete set of
natural internal frequencies $\omega_0 < \omega_1 < \omega_2 < \cdots$, set by
its winding numbers and geometry. Three regimes follow.

**Sub-resonant, $\omega \ll \omega_0$.**
The perturbation is too slow to excite any internal circulation. The toroids
move as rigid bodies, adiabatically tracking the displacement field. No
partial circulations arise. Propagation is elastic and lossless.

**Resonant, $\omega = \omega_n$.**
The driving frequency matches a natural mode. The perturbation couples into a
complete standing wave inside the closure — a circulation that does re-close.
No open circulations arise. Energy is absorbed into the stable internal mode,
not dissipated as radiation.

**Inter-resonance, $\omega_n < \omega < \omega_{n+1}$.**
The driving frequency lies between natural modes. Partial circulations are
excited that cannot settle into a complete standing wave. These radiate. This
is the dissipative regime.

Sound therefore has an acoustic band structure — transparent windows and
absorbing peaks — derived entirely from the internal electromagnetic mode
structure of the toroidal closures. No phonon postulate is needed.

**The coherent limit: superfluidity.**
If all toroids in the medium occupy the same mode — every winding aligned,
every phase synchronized — a perturbation either couples to the collective mode
coherently or does not couple at all. The effective $\omega_0 \to 0$ and the
entire acoustic spectrum falls in the sub-resonant regime. Propagation is
lossless at all frequencies. This is the superfluid: not a separate phenomenon
added to the framework, but the limit of full toroidal coherence in which the
dissipation mechanism is structurally absent.


## What this closes

- The acoustic wave equation requires no independent mechanical postulate.
- The operator $\partial_t^2 - v^2\,\nabla^2$ is the same at all scales;
  only $v$ changes, and that change is derived from the EM constitution of
  the medium.
- Propagation speed $v_s = \sqrt{K/\rho}$ is set entirely by charge coupling
  stiffness and trapped-energy mass density — both EM quantities.
- $v_s \ll c$ is forced by medium stability, not assumed.
- Dissipation is frequency-gated by the internal EM mode structure of the
  toroids: absent below $\omega_0$, absent at resonances, present between them.
- Superfluidity is the fully coherent limit of the same structure.

Acoustics is a slow, longitudinal, coarse-grained regime of Maxwell transport.
No new ontology is introduced at any step.
