---
title: Foundation Equations and Forced Consequences in a Source-Free Maxwell Universe
subtitle: From Maxwell Dynamics to Continuity, Momentum, Inertia, Tension, and Topological Discretization
author: An M. Rodriguez, Alex Mercer
date: 2026-01-20
keywords: Maxwell theory, source-free electromagnetism, Poynting theorem, Maxwell stress tensor, momentum continuity, inertia, tension, torus winding, topology, reconstruction
one-sentence-summary: Starting from source-free Maxwell dynamics, we derive energy continuity, momentum continuity, effective inertia and tension for localized field configurations, and topological discretization on toroidal flow surfaces—without additional postulates.
summary: This document provides a step-by-step derivation chain for the Maxwell Universe program. We begin with the source-free Maxwell equations as the experimentally abstracted dynamical law. From these we derive Poynting’s theorem (energy continuity), then the momentum continuity equation with the Maxwell stress tensor (force as flux). We show how Newton-like laws arise for localized, self-sustaining electromagnetic configurations via integrated continuity identities. We then derive effective tension and inertial line density for thin flux tubes and show how toroidal organization forces integer winding numbers. Finally, we clarify what can be reconstructed from energy density and energy flux alone and what requires the full Maxwell evolution law.
---

# Scope and stance

This document does not introduce new primitives.

We assume only:

- a source-free region,
- continuous electromagnetic fields,
- and Maxwell’s vacuum dynamics as the experimentally abstracted transport law.

Everything else below is derived.

No particles are postulated. No “forces” are postulated. No independent
conservation axioms are postulated.


# Foundations

## Maxwell dynamics in a source-free region

In vacuum, the fields satisfy

$$
\nabla \cdot \mathbf{E} = 0,
\qquad
\nabla \cdot \mathbf{B} = 0,
$$

$$
\nabla \times \mathbf{E} = -\partial_t \mathbf{B},
\qquad
\nabla \times \mathbf{B} = \mu_0 \epsilon_0\,\partial_t \mathbf{E}.
$$

Define the constant

$$
c^2 = \frac{1}{\mu_0 \epsilon_0}.
$$

These four equations are the dynamical content we start from.


# Step 1: Energy continuity (Poynting theorem)

## Energy density and flux

Define electromagnetic energy density

$$
u
=
\frac{\epsilon_0}{2}\,|\mathbf{E}|^2
+
\frac{1}{2\mu_0}\,|\mathbf{B}|^2,
$$

and energy flux (Poynting vector)

$$
\mathbf{S}
=
\frac{1}{\mu_0}\,\mathbf{E}\times \mathbf{B}.
$$


## Derivation of local continuity

Take the dot product of Ampère–Maxwell with $\mathbf{E}$ and Faraday with
$\mathbf{B}/\mu_0$:

$$
\mathbf{E}\cdot(\nabla\times \mathbf{B})
=
\mu_0\epsilon_0\,\mathbf{E}\cdot \partial_t \mathbf{E},
$$

$$
\frac{1}{\mu_0}\mathbf{B}\cdot(\nabla\times \mathbf{E})
=
-\frac{1}{\mu_0}\mathbf{B}\cdot \partial_t \mathbf{B}.
$$

Subtract the second from the first and use the vector identity

$$
\nabla\cdot(\mathbf{E}\times \mathbf{B})
=
\mathbf{B}\cdot(\nabla\times \mathbf{E})
-
\mathbf{E}\cdot(\nabla\times \mathbf{B}),
$$

to obtain

$$
\partial_t
\left(
\frac{\epsilon_0}{2}|\mathbf{E}|^2
+
\frac{1}{2\mu_0}|\mathbf{B}|^2
\right)
+
\nabla\cdot
\left(
\frac{1}{\mu_0}\mathbf{E}\times \mathbf{B}
\right)
=0.
$$

That is,

$$
\partial_t u + \nabla\cdot \mathbf{S} = 0.
$$

Interpretation: this is a strict local bookkeeping identity implied by Maxwell
evolution. It says changes in field energy density are accounted for by flux
divergence.


# Step 2: Momentum continuity and force as flux

## Momentum density

Define electromagnetic momentum density

$$
\mathbf{g}
=
\epsilon_0\,\mathbf{E}\times \mathbf{B}.
$$

Using $\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times \mathbf{B}$ and
$c^2=1/(\mu_0\epsilon_0)$ gives the exact relation

$$
\mathbf{g}=\frac{\mathbf{S}}{c^2}.
$$


## Maxwell stress tensor

Define the Maxwell stress tensor $\mathbf{T}$ with components

$$
T_{ij}
=
\epsilon_0
\left(
E_i E_j
-\frac{1}{2}\delta_{ij}|\mathbf{E}|^2
\right)
+
\frac{1}{\mu_0}
\left(
B_i B_j
-\frac{1}{2}\delta_{ij}|\mathbf{B}|^2
\right).
$$


## Local momentum balance (source-free)

A standard computation using Maxwell’s equations and vector identities yields

$$
\partial_t \mathbf{g} + \nabla\cdot \mathbf{T} = \mathbf{0}.
$$

This is the momentum continuity equation for the field in a source-free region.

Interpretation: momentum changes in a region are accounted for by stress flux
across the boundary.


## Integrated form (force as momentum flux)

Let $V$ be a fixed volume with boundary $\partial V$ and
outward normal $\mathbf{n}$.

Integrate and apply the divergence theorem:

$$
\frac{d}{dt}\int_V \mathbf{g}\,dV
=
-\int_{\partial V} \mathbf{T}\,\mathbf{n}\,dA.
$$

The right-hand side is the net momentum flux through the boundary.

This is the precise origin of “force” in this program:

- “force on a subsystem” is not postulated,
- it is defined as the boundary flux of momentum.


# Step 3: Newton-like laws for localized electromagnetic configurations

We now extract mechanics from the continuity identities.


## Localized configuration (“knot” or “object”)

Assume a field configuration whose energy and momentum are concentrated in a
bounded region that moves without dispersing appreciably over the time interval
of interest.

Define total energy and momentum:

$$
E(t)=\int_{\mathbb{R}^3} u(\mathbf{x},t)\,dV,
\qquad
\mathbf{P}(t)=\int_{\mathbb{R}^3} \mathbf{g}(\mathbf{x},t)\,dV.
$$

From the continuity equations, if the flux vanishes sufficiently fast at
infinity (localized configuration), then

$$
\frac{dE}{dt}=0,
\qquad
\frac{d\mathbf{P}}{dt}=\mathbf{0}.
$$

This is conservation of energy and momentum as a derived property of source-free
Maxwell evolution plus localization.


## Center-of-energy trajectory

Define the center-of-energy position

$$
\mathbf{R}(t)
=
\frac{1}{E}\int_{\mathbb{R}^3}\mathbf{x}\,u(\mathbf{x},t)\,dV.
$$

Differentiate and use energy continuity
$\partial_t u = -\nabla\cdot \mathbf{S}$:

$$
\frac{d\mathbf{R}}{dt}
=
\frac{1}{E}\int_{\mathbb{R}^3}\mathbf{S}(\mathbf{x},t)\,\frac{dV}{c^2}
=
\frac{1}{E}\int_{\mathbb{R}^3}\mathbf{g}(\mathbf{x},t)\,dV
=
\frac{\mathbf{P}}{E}.
$$

Thus, for a localized source-free configuration,

$$
\frac{d\mathbf{R}}{dt}=\frac{\mathbf{P}}{E},
\qquad
\frac{d^2\mathbf{R}}{dt^2}= \mathbf{0}.
$$

This is inertial motion: constant center-of-energy velocity follows from derived
momentum conservation.


## “Force” and interaction

If the configuration is not isolated because other field structure crosses the
boundary of a chosen region $V$, then

$$
\frac{d}{dt}\int_V \mathbf{g}\,dV
=
-\int_{\partial V} \mathbf{T}\,\mathbf{n}\,dA,
$$

so changes in subsystem momentum are caused by stress flux across its boundary.

No additional force law is required. Interaction is momentum exchange through
the field.


# Step 4: Effective tension and inertia of a thin flux tube

Assume a configuration whose energy is concentrated in a thin tube around a
smooth closed curve $X(s)$, with arclength parameter $s\in[0,L]$.

Let $\Sigma_s$ be a small cross-section transverse to the tube at position
$s$.


## Tension (energy per unit length)

Define line energy density

$$
T
=
\int_{\Sigma_s} u\,dA.
$$

Then total energy in the tube is

$$
E = \int_0^L T\,ds.
$$

If $T$ is approximately constant along the tube,

$$
E = T L.
$$

This defines the effective tension: it is not assumed; it is energy localization
per unit length.


## Inertial line density

Using $\mathbf{g}=\mathbf{S}/c^2$, the line momentum density along the local
tangent direction $\hat{\mathbf{t}}(s)$ is

$$
p(s)=\int_{\Sigma_s} \mathbf{g}\cdot \hat{\mathbf{t}}\,dA.
$$

In null-like transport inside the tube (energy flow locally at the maximal
rate), one has the identity

$$
|\mathbf{S}| = c\,u
\quad\Rightarrow\quad
|\mathbf{g}| = \frac{u}{c}.
$$

Under the same thin-tube localization, this yields the effective inertial line
density

$$
\mu = \frac{T}{c^2}.
$$

This is the clean field-theoretic origin of “mass density” for a one-dimensional
effective object.


# Step 5: Toroidal organization forces integer winding

Assume the energy-flow lines lie on an invariant toroidal surface
$T^2$ and form a smooth tangent flow.

A torus has two independent non-contractible cycles.

Closed flow lines must wind around both cycles by integers. The resulting
winding data are coprime integers

$$
(m,n)\in\mathbb{Z}^2.
$$

Interpretation:

- the pair $(m,n)$ is not inserted,
- it is forced by global single-valuedness and closure on $T^2$.

This is the topological origin of discrete classes of configurations.


# Step 6: Discrete modes from periodicity

A closed tube has a circular arclength domain $s\sim s+L$.

Any small perturbation variable $\xi(s,t)$ on the tube that satisfies a
linear wave equation on the circle has Fourier modes:

Assume

$$
\partial_t^2 \xi - v^2\,\partial_s^2 \xi = 0,
\qquad
\xi(s+L,t)=\xi(s,t).
$$

Then expand

$$
\xi(s,t)=\sum_{k\in\mathbb{Z}} a_k e^{i(2\pi k s/L)} f_k(t),
$$

and obtain the discrete frequency set

$$
\omega_k = \frac{2\pi v}{L}|k|.
$$

Discreteness is forced by topology (periodicity), not by quantization axioms.

In the program, the remaining question is the origin of confinement and
stability of the tube; in the trilogy this is tied to emergent refraction and
self-trapping.


# Step 7: What can be reconstructed from energy density and flux

There are two distinct questions:

- Representation: given transport observables, can we represent them with
  fields?
- Dynamics: how do the fields evolve?


## Reconstruction statement (representation)

Given a scalar energy density $u>0$ and a flux $\mathbf{S}$
satisfying

$$
|\mathbf{S}|\le c\,u,
$$

one can construct at least one pair of fields $(\mathbf{E},\mathbf{B})$ such
that

$$
u
=
\frac{\epsilon_0}{2}|\mathbf{E}|^2
+
\frac{1}{2\mu_0}|\mathbf{B}|^2,
$$

$$
\mathbf{S}=\frac{1}{\mu_0}\mathbf{E}\times \mathbf{B}.
$$

The construction is not unique. The two missing local degrees of freedom
correspond to polarization (duality freedom).


## What requires Maxwell dynamics

Reconstruction does not determine how the configuration evolves.

The evolution law that preserves divergence-free structure and yields the above
continuity identities is Maxwell curl dynamics.


# What has been derived (no added postulates)

From source-free Maxwell evolution plus localization/topology assumptions stated
explicitly, we derived:

- energy continuity,
- momentum continuity and stress flux,
- inertial motion of center-of-energy for isolated configurations,
- interaction as momentum exchange through boundary stress,
- effective tension and inertial line density for thin tubes,
- integer winding on toroidal organization,
- discrete mode spectra on closed loops,
- and the precise boundary between representation and dynamics.


# References

Include the program documents here (DOIs to be inserted by editor):

- Light speed as an emergent property of electromagnetic superposition:
  Polarization without matter. DOI: [TO INSERT]
- String Theory Derivation in a Maxwell Universe. DOI: [TO INSERT]
- Geometric Inertia: Mass as Trapped Energy. DOI: [TO INSERT]
- Defining Electromagnetic Fields from Continuity and Divergence-Free Structure.
  DOI: [TO INSERT]
- Maxwell Electromagnetism as the Minimal Dynamics of Divergence-Free Energy
  Flow. DOI: [TO INSERT]
- Canonical Glossary of Terms and Symbols for the Maxwell Universe Research
  Program. DOI: [TO INSERT]
- The Maxwell Universe Research Program — A Logical Map. DOI: [TO INSERT]
