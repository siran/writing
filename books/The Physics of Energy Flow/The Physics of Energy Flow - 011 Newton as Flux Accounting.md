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


## The charge force

Chapter 10 recovered charge as the signed shell reading of the net chiral
$(m,n)$ organization of a toroidal closure. Write that shell density for
closure $i$ as

$$
\sigma_i(r)=\frac{Q_i}{4\pi r^2},
$$

where $Q_i$ carries both the magnitude of the net chiral winding and its sign.
This is not a net flux through a closed sphere. It is the signed
shell-distributed reading of the organized closure.

The corresponding shell potential is the radial accumulation of that shell
density:

$$
\Phi_i(r)=\int_r^\infty \sigma_i(s)\,ds
=
\frac{Q_i}{4\pi r}.
$$

Now place two well-separated closures at distance $d$ between their centers of
energy. The interaction energy of closure 2 in the shell potential of closure 1
is

$$
U(d)=Q_2\,\Phi_1(d)=\frac{Q_1Q_2}{4\pi d}.
$$

The force is the radial derivative of that interaction energy:

$$
\mathbf{F}_{12}
=
-\nabla U
=
\frac{Q_1Q_2}{4\pi d^2}\,\hat{\mathbf{d}},
$$

where $\hat{\mathbf{d}}$ points from closure 1 to closure 2. If $Q_1Q_2>0$,
the force points outward and the closures repel. If $Q_1Q_2<0$, the force
points inward and they attract.

This is Coulomb's law in the present language. The $1/r^2$ force is the
derivative of a signed $1/r$ shell potential. The sign is fixed by the relative
handedness of the two net chiral windings. In the momentum-flux language of
this chapter, the same result is the effective boundary momentum transfer
between two separated localized modes.


## Two $1/r^2$ fields, two mechanisms

The charge force and the gravitational bending of the next chapter both carry
inverse-square dependence on distance. The shape is the same. The mechanism is
not.

Charge comes from a signed shell potential tied to the net chiral $(m,n)$
organization of a single closure. Its interaction strength depends on both the
source and the probe, because both carry a sign.

Gravity comes from the surviving scalar monopole of many positive closure
energies. There the sign information and oriented structure cancel in the
aggregate, while the positive energies add. The next chapter makes that
aggregate scalar derivation explicit and shows how it leads to universal
refraction.


## Summary

Particles are localized regions. Forces are boundary momentum fluxes.
Newton's second law is continuity applied to a stable knot of energy flow.
The Coulomb force is the derivative of a signed shell potential carried by the
net chiral winding of a localized closure. Gravity, by contrast, comes from the
scalar monopole of summed positive closure energies. Both produce $1/r^2$
fields. The mechanisms are distinct.
