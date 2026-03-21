---
title: Sound From Energy Flow
subtitle: Deriving the Acoustic Wave Equation from Source-Free Maxwell Transport
author: An M. Rodriguez
date: 2026-03-20
one-sentence-summary: The sound wave equation is not an independent mechanical law but the coarse-grained, longitudinal mode of the electromagnetic wave equation acting on a medium of organized toroidal closures, with propagation speed set entirely by the electromagnetic structure of the medium.
summary: In a source-free Maxwell universe, matter is aggregate toroidal closures of electromagnetic energy flow. A perturbation in the arrangement of these closures propagates via their primary coupling — the axial charge interaction — and the continuum limit of that propagation is exactly the acoustic wave equation. The operator structure is inherited from the EM wave equation; the propagation speed is derived from the charge coupling stiffness and the trapped-energy mass density, both of which are EM quantities. No mechanical postulate enters. Acoustics is recovered as a slow, longitudinal, coarse-grained regime of Maxwell transport.
keywords:
  - sound
  - acoustic wave equation
  - source-free Maxwell
  - energy flow
  - toroidal closure
  - charge coupling
  - coarse-graining
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
the non-contractible through-hole flux of the winding (Ch 10).

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

Newton's second law for the displacement field becomes, in the continuum limit,

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


## Dissipation

Sound dissipates. Source-free Maxwell transport is time-reversible. The tension
is resolved by the Entropy draft: dissipation occurs when a perturbation excites
partial circulations in the toroidal closures that do not re-close into stable
modes. Those open circulations — circulation that does not fold back on itself
— radiate outward as EM transport. What acoustics calls "thermal dissipation"
is, at the electromagnetic level, radiation from partial non-closing
circulations. The energy goes back into the EM field, not into a separate
thermal substance.


## What this closes

- The acoustic wave equation requires no independent mechanical postulate.
- The operator form $\partial_t^2 - v^2\,\nabla^2$ is universal because it
  comes from Maxwell; $v$ depends on the regime (fine-scale: $v = c$;
  coarse-grained medium: $v = v_s \ll c$).
- Propagation speed $v_s$ is derived from the charge coupling stiffness $K$
  and the mass density $\rho$, both EM quantities.
- $v_s \ll c$ is forced by medium stability, not assumed.
- Dissipation of sound = EM radiation from non-closing partial circulations,
  not an independent thermal mechanism.

Acoustics is a slow, longitudinal, coarse-grained regime of Maxwell transport.
No new ontology is introduced at any step.
