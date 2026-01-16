---
title: Defining Electromagnetic Fields from Continuity and Divergence-Free Structure
subtitle: What Can and Cannot Be Reconstructed from Energy Density and Energy Flow
author: An M. Rodriguez, Alex Mercer
date: 2026-01-17
one-sentence-summary: Continuity and divergence-free structure force electromagnetic energy to be described by directional, circulating degrees of freedom; however, energy density and flux alone do not uniquely determine the electric and magnetic fields without additional relational data.
summary: We clarify the conceptual bridge between a field-only ontology of electromagnetic energy flow and the usual electric/magnetic field variables. We show rigorously that a scalar energy density alone cannot define propagation, but that a continuity equation for energy together with divergence-free structure in three dimensions forces directional transport and circulation. We then prove a reconstruction result: given an energy density u and an energy flux S satisfying the standard inequality |S| ≤ c u, one can always construct at least one pair of fields E and B that reproduce u and S (non-uniquely). The non-uniqueness is not a flaw; it matches the true degrees of freedom (polarization/duality). We conclude with a precise statement of what is implied by continuity and what requires the full Maxwell dynamical law.
keywords: Maxwell theory, continuity equation, divergence-free fields, Poynting vector, energy density, field reconstruction, circulation, topology
---

## Motivation

A recurring conceptual objection is:

If electromagnetic energy is taken as the fundamental object, and energy density
is a scalar field, how do the vector fields $\mathbf{E}$ and
$\mathbf{B}$ arise?

The objection is valid if one assumes the map

scalar $\to$ vectors

should be direct and instantaneous.

It is not.

The correct ordering is:

- scalar energy density $u(\mathbf{x},t)$ is an observable of a process,
- the process is constrained by continuity,
- continuity forces transport,
- transport forces directional structure,
- directional, divergence-free transport locally forces circulation,
- circulation admits a minimal vector description.

This document makes that chain explicit and states exactly what can be derived
from continuity and divergence-free structure.


## Assumptions

We assume a source-free region.

We assume that electromagnetic energy admits:

1. A nonnegative energy density $u(\mathbf{x},t) \ge 0$.

2. An energy flux $\mathbf{S}(\mathbf{x},t)$ satisfying a continuity equation

$$
\partial_t u + \nabla \cdot \mathbf{S} = 0.
$$

We also assume the usual empirical causal bound that energy flux does not exceed
the local maximal propagation speed $c$:

$$
|\mathbf{S}| \le c\,u.
$$

This means that energy cannot flow faster than the speed of electromagnetic
causality, $c$.

We do not assume particles, matter, constitutive media, quantum axioms, or any
mechanical primitive.

We do not derive Maxwell’s equations from continuity alone. We instead show what
continuity forces, and how $\mathbf{E}$ and $\mathbf{B}$ appear as a
minimal representation of that forced structure.


## Why a scalar field alone cannot encode propagation

A scalar field $u(\mathbf{x},t)$ at a single time slice is insufficient to
encode motion. Two snapshots, however, allow us to define the directional
structure a scalar field must have in order to transport energy. Without energy
transport there is nothing to describe.

This is not only philosophical; it is a degrees-of-freedom statement:

- A scalar specifies magnitude.
- Transport requires magnitude and direction.
- Direction is encoded in vectorial language.

The continuity equation already checks these requirements: it does not close on
$u$ alone; it involves a vector field defined everywhere,
$\mathbf{S}$.

Thus, the fundamental object in a continuity-based ontology is not
$u$ alone, but the pair $(u,\mathbf{S})$, i.e. a conserved flow.


## Divergence-free structure and circulation in 3D

In three dimensions, divergence-free vector fields have a canonical geometric
feature: they admit circulation and vortex-like organization.

The mathematical statement is standard:

If a vector field $\mathbf{F}$ is divergence-free on a simply connected
region, then there exists a vector potential $\mathbf{A}$ such that

$$
\mathbf{F} = \nabla \times \mathbf{A}.
$$

This is a general theorem about solenoidal fields. Locally, divergence-free
structure is equivalent to curl structure and hence to circulation. Globally,
the existence of nontrivial circulation depends on the topology of the domain.

This distinction underlies the appearance of toroidal shells and winding
numbers: in three dimensions, divergence-free structure naturally organizes into
tubes and closed surfaces when the topology permits it.


## What it means to define the electromagnetic field

There are two distinct tasks that must be separated:

1. Representation: showing that $(u,\mathbf{S})$ can be represented by fields
   $\mathbf{E}$ and $\mathbf{B}$.
2. Dynamics: specifying how $\mathbf{E}$ and $\mathbf{B}$ evolve in
   time.

Continuity addresses the first task partially and constrains the second, but
does not uniquely determine dynamics. This document focuses exclusively on the
representation problem.


## Reconstruction lemma: from $(u,\mathbf{S})$ to $(\mathbf{E},\mathbf{B})$

We now show that if $(u,\mathbf{S})$ obeys $|\mathbf{S}| \le c u$, then one can
always construct at least one pair of fields $\mathbf{E}$ and
$\mathbf{B}$ satisfying the standard electromagnetic energy and flux
relations.


### Lemma (existence, non-uniqueness)

Given scalar $u>0$ and vector $\mathbf{S}$ with
$|\mathbf{S}| \le c u$, there exist vectors $\mathbf{E}$ and
$\mathbf{B}$ such that

$$
u = \frac{\epsilon_0}{2}|\mathbf{E}|^2 + \frac{1}{2\mu_0}|\mathbf{B}|^2,
$$

$$
\mathbf{S} = \frac{1}{\mu_0}\,\mathbf{E}\times \mathbf{B}.
$$

The pair $(\mathbf{E},\mathbf{B})$ is not unique. There is an infinite family of
solutions corresponding to polarization and duality degrees of freedom.


### Construction

Let $\hat{\mathbf{s}}$ be a unit vector in the direction of $\mathbf{S}$ if
$\mathbf{S}\neq 0$; if $\mathbf{S}=0$, choose any unit vector.

Choose a unit vector $\hat{\mathbf{e}}$ orthogonal to $\hat{\mathbf{s}}$ and
define $\hat{\mathbf{b}} := \hat{\mathbf{s}} \times \hat{\mathbf{e}}$, forming a
right-handed orthonormal frame.

Define

$$
\mathbf{E} := E\,\hat{\mathbf{e}}, \qquad \mathbf{B} := B\,\hat{\mathbf{b}}.
$$

Then

$$
\mathbf{E}\times \mathbf{B} = EB\,\hat{\mathbf{s}}.
$$

Imposing the flux condition yields

$$
\frac{1}{\mu_0}EB = |\mathbf{S}|.
$$

The energy condition gives

$$
u = \frac{\epsilon_0}{2}E^2 + \frac{1}{2\mu_0}B^2.
$$

Using $c^2 = 1/(\mu_0\epsilon_0)$ and eliminating $B$ leads to a
quadratic equation for $E^2$ with real solutions whenever
$|\mathbf{S}| \le c u$. Choosing either root completes the construction.


### Interpretation

- The inequality $|\mathbf{S}| \le c u$ is exactly the condition required for
  reconstruction.
- The choice of transverse frame corresponds to polarization freedom.
- Continuous duality rotations leave $(u,\mathbf{S})$ invariant.

Thus, $(u,\mathbf{S})$ underdetermines $(\mathbf{E},\mathbf{B})$ by exactly two
local degrees of freedom. This matches the two missing local degrees of freedom
identified as polarization.


## Why orthogonal coupling appears

The frequent question “why does one generate the other orthogonally?” should be
recast as:

Why does divergence-free propagation require rotational coupling?

The minimal structural answer is:

- To propagate while remaining divergence-free, degrees of freedom must rotate
  into one another. In three dimensions, this rotation is encoded by curl.

- Maxwell evolution uses curl operators, which are sufficient to transport
  divergence-free structure without creating sources or sinks.

Continuity alone does not fix this evolution uniquely; curl dynamics is a
minimal realization of divergence-free propagation.

In this sense, electric and magnetic fields are names for the two interlocked
rotational aspects of a single propagating, divergence-free energy flow.


## Where toroidal winding numbers $(m,n)$ enter

The reconstruction above is local. Toroidal winding numbers are global.

On an invariant torus $T^2$, a smooth source-free tangent flow
decomposes into windings around the two fundamental cycles. For example, a
linear flow of rational slope on $T^2$ closes after $(m,n)$
windings, enforcing discrete circulation classes.

In a flow-first ontology:

- $(m,n)$ classify the global organization of energy transport on the
  torus,
- while $(\mathbf{E},\mathbf{B})$ provide a local representation of that same
  organization.

The integers $(m,n)$ constrain which global field configurations are
possible, not the local reconstruction itself.


## Conclusions

- A scalar energy density alone cannot encode propagation.
- Continuity forces directional transport and hence vector structure.
- Divergence-free structure locally forces circulation in three dimensions.
- Given $(u,\mathbf{S})$ with $|\mathbf{S}|\le c u$, one can construct
  $\mathbf{E}$ and $\mathbf{B}$ reproducing the same energy and flux.
- The reconstruction is necessarily non-unique, matching polarization degrees of
  freedom.


## Closing statement

A scalar energy observable does not generate electromagnetic vector fields by
itself. The evolution of energy under continuity forces transport, and transport
forces directional, circulating structure in three dimensions.

Electric and magnetic fields provide a minimal local representation of this
structure while reproducing the observable pair $(u,\mathbf{S})$.

This provides a precise conceptual bridge between a flow-first Maxwell ontology
and the standard $(\mathbf{E},\mathbf{B})$ description.
