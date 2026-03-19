---
title: The Physics of Energy Flow - Newton as Flux Accounting
date: 2026-03-19
---


# 11. Newton as Flux Accounting

Newton's second law is the integrated continuity law for momentum in a bounded
region of directed energy flow.

Chapter 3 gave the continuity equation for energy density $u$. In the present
language of directed transport, that same statement is

$$
\partial_t u + \nabla\cdot \mathbf{F} = 0,
$$

where $\mathbf{F}$ is the directed energy-flow density.

Because energy flow carries momentum, define the momentum density by

$$
\mathbf{p}=\frac{\mathbf{F}}{c^2}.
$$

To describe how momentum crosses boundaries, introduce the stress tensor
$\mathbf{T}$. This is the momentum-flux density of the same flow. Its
component $T_{ij}$ is the $i$-component of momentum transferred across a
surface whose normal points in the $j$ direction.

The local momentum continuity law is then

$$
\partial_t p_i - \partial_j T_{ij} = 0,
$$

or, in tensor form,

$$
\partial_t \mathbf{p} - \nabla\cdot\mathbf{T}=0.
$$

Momentum does not appear or disappear. It changes only by flux through the
boundary of a region.

Now choose a bounded region $\Omega$ containing a nearly stable localized
configuration. Define its total momentum and total energy:

$$
\mathbf{P}_\Omega
=
\int_\Omega \mathbf{p}\,dV
=
\frac{1}{c^2}\int_\Omega \mathbf{F}\,dV,
$$

$$
E_\Omega=\int_\Omega u\,dV.
$$

Integrating the local momentum continuity law gives

$$
\frac{d}{dt}\mathbf{P}_\Omega
=
\int_{\partial\Omega}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

The right-hand side is what later language calls force. It is the net rate at
which momentum is transferred across the boundary into the localized region.

To connect this with motion of the bounded mode as a whole, define its center
of energy:

$$
\mathbf{X}_\Omega
=
\frac{1}{E_\Omega}\int_\Omega \mathbf{x}\,u\,dV.
$$

When boundary leakage is small and the mode remains coherent,

$$
E_\Omega\,\dot{\mathbf{X}}_\Omega
\approx
\int_\Omega \mathbf{F}\,dV,
$$

so

$$
\mathbf{P}_\Omega
\approx
\frac{E_\Omega}{c^2}\dot{\mathbf{X}}_\Omega.
$$

If the total energy of the bounded configuration is roughly constant, define

$$
m_\Omega := \frac{E_\Omega}{c^2}.
$$

Then

$$
m_\Omega\,\ddot{\mathbf{X}}_\Omega
\approx
\int_{\partial\Omega}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

This is Newton's second law in effective form for a stable bounded mode:

$$
\mathbf{F}_{\mathrm{ext}}=\frac{d\mathbf{P}_\Omega}{dt}.
$$

So Newton's law is not an independent primitive. It is momentum bookkeeping for
a bounded region of energy flow.

When the same transport is written in conventional electromagnetic variables,
$\mathbf{F}$ becomes the Poynting vector and $\mathbf{T}$ becomes the Maxwell
stress tensor. But the logic does not depend on that representation. The
content is already present in the flow language itself.

Particles are localized regions. Forces are boundary momentum fluxes.
Newton's second law is continuity applied to a stable knot of energy flow.
