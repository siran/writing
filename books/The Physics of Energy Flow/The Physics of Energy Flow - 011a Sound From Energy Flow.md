---
title: The Physics of Energy Flow - Sound From Energy Flow
subtitle: Deriving the Acoustic Wave Equation from Source-Free Maxwell Transport
date: 2026-03-20
kind: chapter
part: Part I — Energy Flows
one-sentence-summary: The sound wave equation is not an independent mechanical law but the coarse-grained, longitudinal mode of the electromagnetic wave equation acting on a medium of organized toroidal closures, with propagation speed, dispersion, and dissipation all set by the electromagnetic structure of the medium.
summary: In a source-free Maxwell universe, matter is aggregate toroidal closures of electromagnetic energy flow. A perturbation in the arrangement of these closures propagates via their primary coupling — the axial charge interaction — and the continuum limit of that propagation is exactly the acoustic wave equation. The operator structure is inherited from the EM wave equation; the propagation speed is derived from the charge coupling stiffness and the trapped-energy mass density, both of which are electromagnetic quantities. Dissipation occurs when the driving frequency excites partial internal circulations that do not re-close into stable modes; below the internal resonance threshold, propagation is lossless and elastic. No mechanical postulate enters. Acoustics is recovered as a slow, longitudinal, coarse-grained regime of Maxwell transport.
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


# 11a. Sound From Energy Flow

Chapter 11 recovered Newton's second law as the integrated continuity equation
for momentum flux across the boundary of a stable bounded configuration. That
result applies to a single localized mode responding to an external organized
field. This chapter asks the next question: what happens when a large
collection of such modes — the bulk matter medium — is disturbed?

The answer is a wave. The wave equation that governs it is not a new
postulate. It is the coarse-grained, longitudinal mode of the electromagnetic
wave equation already in hand. Propagation speed, dispersion, and dissipation
all follow from the electromagnetic structure of the medium.


## The medium

Matter in a source-free Maxwell universe is aggregate toroidal closures of
electromagnetic energy flow (Ch 8, Ch 10). Each toroidal closure is
characterized by a winding pair $(m, n)$ — charge and spin as topological
invariants — and a scalar amplitude of trapped energy $E$. Its mass is

$$
M = E/c^2.
$$

Its exterior carries an axial charge field that falls as $1/r^2$, sustained by
the non-contractible through-hole flux of the $m$-winding.

A bulk material is a regular arrangement of $n_0$ such toroids per unit volume,
at equilibrium separation $d_0 \sim n_0^{-1/3}$. This equilibrium is set by the
balance of charge coupling between neighbors: at $d_0$ the net force on each
toroid from its neighbors vanishes.


## The perturbation

Displace the toroid centered at position $\mathbf{x}$ by a small vector
$\boldsymbol{\xi}(\mathbf{x}, t)$ from its equilibrium position. The restoring
force comes from the axial charge coupling.

The interaction energy between two toroidal axial charge fields at separation
$d$ is of the form

$$
U(d) \sim -\frac{Q^2}{d},
$$

where $Q$ is the through-hole flux strength fixed by the winding number $m$.
For a small displacement $\xi$ from equilibrium:

$$
U(d_0 + \xi) \approx U(d_0) + \tfrac{1}{2}\,U''(d_0)\,\xi^2,
$$

with restoring stiffness

$$
K_\text{local} = U''(d_0) \sim \frac{Q^2}{d_0^3} > 0.
$$

This is a purely electromagnetic quantity: $Q$ comes from the charge winding,
$d_0$ from the equilibrium of the same charge coupling.


## Continuum limit: the wave equation

Pass to the continuum. With $n_0$ toroids per unit volume:

$$
\rho = n_0\,M = \frac{n_0 E}{c^2}
\qquad\text{(mass density, from aggregate trapped EM energy)}
$$

$$
K = n_0\,K_\text{local}
\qquad\text{(bulk stiffness, from charge coupling between neighbors)}
$$

The equation of motion for the displacement field in the continuum limit is

$$
\rho\,\partial_t^2\,\boldsymbol{\xi} = K\,\nabla^2\boldsymbol{\xi}.
$$

This is a wave equation. The propagation speed is

$$
v_s = \sqrt{\frac{K}{\rho}}.
$$

Both $K$ and $\rho$ are derived from the electromagnetic structure of the
toroids. No mechanical postulate enters.

For the longitudinal (compressional) mode, set $p \propto \nabla \cdot
\boldsymbol{\xi}$ and take the divergence. The result is

$$
\partial_t^2 p - v_s^2\,\nabla^2 p = 0.
$$

This is the sound wave equation, recovered from Maxwell transport.


## The operator identity

The electromagnetic wave equation is

$$
\partial_t^2 \mathbf{F} - c^2\,\nabla^2 \mathbf{F} = 0.
$$

The acoustic wave equation is

$$
\partial_t^2 p - v_s^2\,\nabla^2 p = 0.
$$

The operator $\partial_t^2 - v^2\,\nabla^2$ is the same at both scales. The
speed changes; the structure does not. The sound wave equation is not a new
law — it is the same operator acting on the density perturbation of a medium
whose constituents obey the fine-scale EM equation.


## Why $v_s \ll c$ is forced

$$
\frac{v_s^2}{c^2} = \frac{K}{\rho\,c^2} = \frac{K_\text{local}}{Mc^2}
\sim \frac{Q^2/d_0^3}{E}.
$$

The numerator $Q^2/d_0^3$ is the interaction energy gradient between
neighboring toroids — a near-field quantity. The denominator $E$ is the full
self-energy of a single toroid. For the medium to be stable — for toroids to
remain distinct, non-merging configurations — the inter-toroid coupling must be
much weaker than the toroid self-energy:

$$
\frac{Q^2}{d_0^3} \ll E \quad \Rightarrow \quad v_s \ll c.
$$

The inequality $v_s \ll c$ is not a parameter choice. It is the stability
condition of the medium.


## Dissipation and its disappearance

Dissipation of sound occurs when the driving perturbation excites partial
internal circulations within the toroidal closures that do not re-close into
stable modes. Those open circulations radiate outward as electromagnetic
transport — what macroscopic acoustics calls heat. The energy returns to the
electromagnetic field, not to a separate thermal substance.

Whether this happens depends on the frequency of the driving perturbation
relative to the internal mode structure of the toroids.

Each toroidal closure has a discrete set of natural internal frequencies
$\omega_0 < \omega_1 < \omega_2 < \cdots$, set by its winding numbers and
geometry (Ch 8). Three regimes follow:

**Sub-resonant regime, $\omega \ll \omega_0$.**
The perturbation is too slow to excite any internal circulation. The toroids
move as rigid bodies under the charge coupling, adiabatically tracking the
displacement field. No internal circulation is excited — partial or otherwise —
so no radiation escapes. Propagation is elastic and lossless.

**Resonant regime, $\omega = \omega_n$.**
The driving frequency matches a natural mode of the toroidal closure. The
perturbation couples into a complete standing wave inside the closure — a
circulation that does re-close. No partial open circulations arise, so no
radiation escapes from this coupling channel. The energy is absorbed into the
stable internal mode, not dissipated. This is absorption without radiation.

**Inter-resonance regime, $\omega_n < \omega < \omega_{n+1}$.**
The driving frequency lies between natural modes. The perturbation excites
partial circulations that cannot settle into a complete standing wave. These
open circulations radiate. This is the dissipative regime.

The structure is:

$$
\omega \ll \omega_0 : \quad \text{elastic, lossless propagation}
$$
$$
\omega = \omega_n : \quad \text{resonant absorption into stable modes}
$$
$$
\omega_n < \omega < \omega_{n+1} : \quad \text{dissipation by EM radiation}
$$

Sound has an acoustic band structure — transparent windows and absorbing peaks
— derived entirely from the internal electromagnetic mode structure of the
toroidal closures. No phonon postulate is needed.


## The coherent limit: superfluidity

The most extreme case: if all toroids in the medium occupy the same mode —
every winding aligned, every phase synchronized — then a perturbation either
couples to the collective mode coherently or does not couple at all. The
effective $\omega_0 \to 0$ and the entire acoustic spectrum falls in the
sub-resonant regime. Propagation is lossless at all frequencies.

This is the superfluid. Sound propagates without dissipation because the medium
has no partial-mode degrees of freedom to radiate into. Superfluidity is not a
separate phenomenon added to the framework. It is the limit of full toroidal
coherence, in which the dissipation mechanism is structurally absent.


## What this closes

Acoustics requires no postulates beyond source-free Maxwell transport:

- The acoustic wave equation has the same operator as the EM wave equation;
  only the speed changes, and that change is derived.
- Propagation speed $v_s = \sqrt{K/\rho}$ comes entirely from electromagnetic
  quantities ($K$ from charge coupling, $\rho$ from trapped-energy mass).
- $v_s \ll c$ is forced by medium stability.
- Dissipation is frequency-gated by the internal EM mode structure of the
  toroids: absent below $\omega_0$, absent at resonances, present between them.
- The coherent limit of the same structure recovers dissipation-free
  propagation — superfluidity — without additional postulates.

Acoustics is a slow, longitudinal, coarse-grained regime of Maxwell transport.
