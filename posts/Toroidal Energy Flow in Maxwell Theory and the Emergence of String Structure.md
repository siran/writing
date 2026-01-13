---
title: Deriving String-Theoretic Structure in a Maxwell Universe
subtitle: Winding, Tension, and Stability from Electromagnetic Topology Alone
author: An M. Rodriguez, Alex Mercer
date: 2026-01-11
keywords: Maxwell theory, classical electrodynamics, Poynting flow, electromagnetic energy flow, electromagnetic topology, toroidal topology, torus knots, winding numbers, emergent strings, self-trapping, effective refractive index, field ontology
one-sentence-summary: When electromagnetic energy flow organizes on invariant tori, classical Maxwell theory produces integer winding numbers, tension, inertia, and discrete mode spectra stabilized by energy-dependent effective refraction.
summary: We show how linear, classical Maxwell theory admits toroidally organized energy flow whose closed trajectories are labeled by integer winding numbers. Localized electromagnetic energy flow defines an effective one-dimensional object with tension and inertia computed directly from field densities. Stability against dispersion arises because high electromagnetic energy density reduces the local effective speed of light, producing self-trapping through emergent refraction. Explicit null Maxwell solutions with torus-knot topology demonstrate that integer data $(m,n)$ are computable from conserved field integrals. String-theoretic structures thus emerge as effective descriptions of self-stabilizing electromagnetic topology.
---

![AI generated illustration of knotted trajectories on a toroidal surface.](https://siran.github.io/assets/writing/donut-knots.jpg)


## Summary

Maxwell theory admits electromagnetic energy flow configurations that are
closed, topologically nontrivial, and dynamically stable.

In a source-free Maxwell universe, electromagnetic energy can circulate on
invariant toroidal surfaces. Closure of these flows forces integer winding
numbers. Localization of energy along closed trajectories defines an effective
one-dimensional object with tension and inertia computed directly from field
densities. Periodicity enforces discrete mode spectra.

Stability against dispersion arises because high electromagnetic energy density
reduces the local effective speed of light, creating self-trapping through
emergent refraction.

In this setting, the defining structures of string theory—winding numbers,
tension, inertia, and discrete modes, are consequences of electromagnetic
topology and self-interaction within classical Maxwell theory.


## Goal

Demonstrate that:

1. Electromagnetic energy flow can form closed trajectories on tori.
2. Closure forces integer winding numbers $(m,n)$.
3. Localized energy flow defines a one-dimensional object with tension.
4. Maxwell momentum fixes the corresponding inertia.
5. High electromagnetic energy density reduces the local effective speed of
   light, producing self-trapping and spectral stability.
6. The integers $(m,n)$ are computable from conserved Maxwell
   integrals.


## Conclusions

- Integer winding is forced by toroidal topology.
- Tension and inertia follow from electromagnetic energy and momentum.
- Discrete spectra follow from periodicity combined with self-confinement.
- String-theoretic structure emerges as an effective description of
  electromagnetic topology stabilized by emergent refraction.


## Maxwell theory and energy transport

In vacuum, Maxwell’s equations are

$$
\nabla \cdot \mathbf{E} = 0, \qquad \nabla \cdot \mathbf{B} = 0,
$$

$$
\nabla \times \mathbf{E} = -\partial_t \mathbf{B}, \qquad
\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \, \partial_t \mathbf{E}.
$$

From these equations follows Poynting’s theorem,

$$
\partial_t u + \nabla \cdot \mathbf{S} = 0,
$$

with electromagnetic energy density and energy flux

$$
u = \frac{\epsilon_0}{2} \mathbf{E}^2 + \frac{1}{2\mu_0} \mathbf{B}^2,
\qquad
\mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B}.
$$

Energy transport is an intrinsic, conserved feature of the electromagnetic
field.

Define the instantaneous energy-flow velocity field wherever $u > 0$ as

$$
\mathbf{v} = \frac{\mathbf{S}}{u}.
$$

Integral curves of $\mathbf{v}$ describe the local flow of electromagnetic
energy at a fixed time slice.


## Toroidal organization and integer winding

Nothing in Maxwell theory restricts energy-flow lines to be open. Closed energy
circulation is dynamically allowed.

A torus $T^2$ is the simplest closed surface with two independent,
non-contractible cycles. On such a surface, any smooth, divergence-free tangent
flow is a linear flow in angular coordinates $(\theta,\phi)$.

A standard result from the theory of dynamical systems on $T^2$
states:

> A linear flow on a torus has closed trajectories if and only if the slope
> $d\theta/d\phi$ is rational.


Consequently, any closed energy-flow line on a torus is labeled by a unique
coprime integer pair

$$
(m,n) \in \mathbb{Z}^2,
$$

counting the number of windings around the two fundamental cycles.

These integers are enforced by periodicity and single-valuedness.


## Localized energy flow defines tension

Consider a closed energy-flow line $X(s)$ parameterized by arclength
$s \in [0,L]$. Assume the electromagnetic energy density is concentrated in a
thin tube surrounding this curve.

Define the line energy density by integrating the Maxwell energy density over a
transverse cross-section $\Sigma_s$:

$$
T = \int_{\Sigma_s} u \, d^2 x.
$$

The total electromagnetic energy contained in the tube is

$$
E = \int_0^L T \, ds = T L.
$$

This proportionality defines a tension $T$, interpreted as energy
per unit length.


## Inertia from Maxwell momentum

The electromagnetic momentum density is

$$
\mathbf{g} = \epsilon_0 \, \mathbf{E} \times \mathbf{B}
           = \frac{\mathbf{S}}{c^2},
\qquad
c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}.
$$

Projecting $\mathbf{g}$ along the unit tangent
$\hat{\mathbf{t}} = \partial_s X / |\partial_s X|$ and integrating over
$\Sigma_s$ yields the line momentum density

$$
p = \int_{\Sigma_s} \mathbf{g} \cdot \hat{\mathbf{t}} \, d^2 x.
$$

For null electromagnetic fields, defined by

$$
\mathbf{E} \cdot \mathbf{B} = 0, \qquad |\mathbf{E}| = c |\mathbf{B}|,
$$

one finds

$$
|\mathbf{S}| = c u.
$$

The effective inertial line density is therefore

$$
\mu = \frac{T}{c^2}.
$$

Tension and inertia are fixed by Maxwell field densities.


## Stability and discrete mode spectrum

A localized tube of electromagnetic energy in linear vacuum theory would
normally disperse. Electromagnetic superposition modifies the effective local
propagation speed in regions of high field energy density.

As shown in [@Rodriguez2026], linear superposition produces an effective
susceptibility $\chi(\mathbf{x})$ such that

$$
c_{\text{local}}(\mathbf{x}) = \frac{c_0}{\sqrt{1+\chi(\mathbf{x})}}.
$$

Regions of elevated energy density therefore correspond to regions of higher
effective refractive index. A toroidal energy tube creates an electromagnetic
waveguide through total internal reflection.

The same electromagnetic fields that define the object also generate the
refractive profile that confines it.

Let $\xi(s,t)$ describe small transverse perturbations of this
self-trapped structure. The leading-order effective dynamics yields

$$
\partial_t^2 \xi - c_{\text{local}}^2 \partial_s^2 \xi = 0.
$$

Closure of the curve enforces periodic boundary conditions

$$
\xi(s+L,t) = \xi(s,t).
$$

Fourier analysis on $S^1$ yields a discrete spectrum

$$
\omega_k = \frac{2\pi c_{\text{local}}}{L} |k|, \qquad k \in \mathbb{Z}.
$$


## Explicit Maxwell solutions with torus-knot topology

Exact vacuum Maxwell solutions constructed via the Bateman method exhibit nested
invariant tori and torus-knot field lines labeled by integers $(p,q)$.

For this family, conserved electromagnetic quantities are

$$
H_m = H_e = \frac{1}{p+q},
$$

$$
P_z = -\frac{p}{p+q}, \qquad L_z = \frac{q}{p+q}.
$$

The toroidal winding slope is

$$
\frac{p}{q} = -\frac{P_z}{L_z}.
$$

The integers are recovered from conserved integrals:

$$
p = -\frac{P_z}{H_m}, \qquad q = \frac{L_z}{H_m}.
$$


## What has been derived

From Maxwell theory alone:

- Closed one-dimensional electromagnetic excitations arise.
- Integer winding numbers $(m,n)$ are enforced by topology.
- Tension $T$ follows from energy density.
- Inertia $\mu = T/c^2$ follows from momentum density.
- A discrete oscillator spectrum is stabilized by self-trapping.
- Integer data are encoded in conserved field integrals.

These structures correspond to those normally postulated in string theory and
here arise as emergent properties of a classical Maxwell universe.


## Final statement

When electromagnetic energy flow organizes on invariant tori, Maxwell theory
produces string-theoretic structure as an emergent phenomenon.

Strings are not fundamental objects. They are effective descriptions of
electromagnetic topology stabilized by the field’s own energy density.

This follows directly from classical field theory.


## References

{#Rodriguez2026} Rodriguez, A. M. (2026). *Light speed as an emergent property
of electromagnetic superposition: Polarization without matter*. Preferred Frame.
https://writing.preferredframe.com/doi/10.5281/zenodo.18209801

Rodriguez, A. M., Mercer, A. (2026). *String Theory in AMU (chatgpt 5.2
conversation)*. Preferred Frame.
https://chatgpt.com/share/69658aaf-37a0-8007-ada8-959f4103d5cb
