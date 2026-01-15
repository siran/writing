---
title: Defining Electromagnetic Fields from Continuity and Divergence-Free Structure
subtitle: What Can and Cannot Be Reconstructed from Energy Density and Energy Flow
author: An M. Rodriguez, Alex Mercer
date: 2026-01-17
keywords: Maxwell theory, continuity equation, divergence-free fields, Poynting vector, energy density, field reconstruction, circulation, topology
one-sentence-summary: Continuity and divergence-free structure force electromagnetic energy to be described by directional, circulating degrees of freedom; however, energy density and flux alone do not uniquely determine the electric and magnetic fields without additional relational data.
summary: We clarify the conceptual bridge between a field-only ontology of electromagnetic energy flow and the usual electric/magnetic field variables. We show rigorously that a scalar energy density alone cannot define propagation, but that a continuity equation for energy together with divergence-free structure in three dimensions forces directional transport and circulation. We then prove a reconstruction result: given an energy density u and an energy flux S satisfying the standard inequality |S| ≤ c u, one can always construct fields E and B that reproduce u and S (non-uniquely). The non-uniqueness is not a flaw; it matches the true degrees of freedom (polarization/duality). We conclude with a precise statement of what is implied by continuity and what requires the full Maxwell dynamical law.
---

# Defining Electromagnetic Fields from Continuity and Divergence-Free Structure

## Motivation

A recurring conceptual objection is:

If "electromagnetic energy" is the fundamental object, and energy density is a
scalar field, how do the vector fields $\mathbf{E}$ and $\mathbf{B}$
arise?

The objection is valid if one assumes the map

scalar $\to$ vectors

should be direct and instantaneous.

It is not.

The correct ordering is:

- scalar energy density $u(\mathbf{x},t)$ is an observable of a process,
- the process is constrained by continuity,
- continuity forces transport,
- transport forces directional structure,
- directional, divergence-free transport forces circulation,
- circulation admits a minimal vector description.

This document makes that chain explicit and states exactly what can be derived
from continuity and divergence-free structure, and what cannot.


## What is assumed (and what is not)

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

This bound is **not** a *postulate* about space or time or flow; it is an
operational, observed, fact about propagating electromagnetic disturbances:
there exists a maximal transport rate relating energy content to energy
throughput.

We do not assume particles, matter, constitutive media, quantum axioms, or any
mechanical primitive.

We do not derive Maxwell’s equations from continuity alone. We instead show what
continuity forces, and how $\mathbf{E}$ and $\mathbf{B}$ appear as a
minimal representation of that forced structure.


## Why a scalar field alone cannot encode propagation

A scalar field $u(\mathbf{x},t)$ at a single time slice is insufficient to
encode motion. Two snapshots, however, lets us define the "directional
structure" a scalar field must have in order to transport energy. Without energy
transport there is nothing to describe.

What comes is not only or just philosophy, it is a degrees-of-freedom statement:

- A scalar specifies magnitude,
- Transport requires magnitude and direction, and
- Direction can be encoded is vectorial language.

The continuity equation already check this requirements: it does not close on
$u$ alone; it involves a magnitude and direction of change,
$\mathbf{S}$, a scalar value everywhere. In essence, two scalar field, two
time slices.

Thus, the fundamental object in a continuity-based ontology is not
$u$ alone, but the pair $(u,\mathbf{S})$, i.e. a conserved flow.


## Divergence-free structure forces circulation in 3D

In three dimensions, divergence-free vector fields have a canonical geometric
feature: they admit circulation and vortex-like organization.

The mathematical statement is standard:

If a vector field $\mathbf{F}$ is divergence-free on a simply connected
region, then there exists a vector potential $\mathbf{A}$ such that

$$
\mathbf{F} = \nabla \times \mathbf{A}.
$$

This is not “electromagnetism”; it is a general theorem about solenoidal,
mathematical objects, fields. It says that divergence-free structure is
equivalent to curl structure, hence to circulation.

Therefore, any theory that insists on divergence-free structure as primitive is
already committed to circulation as a primitive mode of organization.

This is the topological seed of toroidal shells and winding numbers: in 3D,
divergence-free structure naturally organizes into tubes and closed surfaces.


## What it means to “define the electromagnetic field”

There are two distinct tasks that often get conflated:

1. Representation: show that $(u,\mathbf{S})$ can be represented by fields
   $\mathbf{E},\mathbf{B}$.
2. Dynamics: show how $\mathbf{E},\mathbf{B}$ evolve.

Continuity addresses (1) partially and constrains (2), but does not uniquely fix
(2). For dynamics, one needs the full Maxwell evolution law.

This document focuses on (1): the representation problem.


## Reconstruction lemma: from $(u,\mathbf{S})$ to $(\mathbf{E},\mathbf{B})$

We now show that if $(u,\mathbf{S})$ obeys $|\mathbf{S}| \le c u$, then one can
construct $\mathbf{E}$ and $\mathbf{B}$ satisfying the standard
electromagnetic energy and flux relations.


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

Moreover, the pair $(\mathbf{E},\mathbf{B})$ is not unique: there is an infinite
family of solutions corresponding to polarization/duality degrees of freedom.


### Construction

Let $\hat{\mathbf{s}}$ be a unit vector in the direction of $\mathbf{S}$ if
$\mathbf{S}\neq 0$; if $\mathbf{S}=0$, pick any unit vector.

Choose any unit vector $\hat{\mathbf{e}}$ orthogonal to $\hat{\mathbf{s}}$.
Define $\hat{\mathbf{b}} := \hat{\mathbf{s}} \times \hat{\mathbf{e}}$ so that
$(\hat{\mathbf{e}},\hat{\mathbf{b}},\hat{\mathbf{s}})$ is a right-handed
orthonormal frame.

Now pick magnitudes $E:=|\mathbf{E}|$ and $B:=|\mathbf{B}|$ and set

$$
\mathbf{E} := E\,\hat{\mathbf{e}}, \qquad \mathbf{B} := B\,\hat{\mathbf{b}}.
$$

Then

$$
\mathbf{E}\times \mathbf{B} = EB\,\hat{\mathbf{s}}.
$$

So the flux condition becomes

$$
\frac{1}{\mu_0}EB = |\mathbf{S}|.
$$

The energy condition becomes

$$
u = \frac{\epsilon_0}{2}E^2 + \frac{1}{2\mu_0}B^2.
$$

Use $c^2 = 1/(\mu_0\epsilon_0)$ to write $B$ in terms of
$E$ from the flux equation:

$$
B = \frac{\mu_0|\mathbf{S}|}{E}.
$$

Substitute into the energy equation:

$$
u = \frac{\epsilon_0}{2}E^2 + \frac{1}{2\mu_0}\left(\frac{\mu_0|\mathbf{S}|}{E}\right)^2
= \frac{\epsilon_0}{2}E^2 + \frac{\mu_0}{2}\frac{|\mathbf{S}|^2}{E^2}.
$$

Multiply by $2/\epsilon_0$ and define $x:=E^2>0$:

$$
\frac{2u}{\epsilon_0} = x + \frac{|\mathbf{S}|^2}{c^2}\frac{1}{x}.
$$

This is a quadratic equation in $x$:

$$
x^2 - \frac{2u}{\epsilon_0}x + \frac{|\mathbf{S}|^2}{c^2} = 0.
$$

The discriminant is

$$
\Delta = \left(\frac{2u}{\epsilon_0}\right)^2 - 4\frac{|\mathbf{S}|^2}{c^2}
= 4\left(\frac{u^2}{\epsilon_0^2} - \frac{|\mathbf{S}|^2}{c^2}\right).
$$

By the assumed bound $|\mathbf{S}| \le c u$, we have $\Delta \ge 0$, so a
positive solution exists. Choose either root

$$
x = \frac{u}{\epsilon_0} \pm \sqrt{\frac{u^2}{\epsilon_0^2} - \frac{|\mathbf{S}|^2}{c^2}},
$$

and set $E=\sqrt{x}$, then define $B$ by
$B=\mu_0|\mathbf{S}|/E$.

This constructs $\mathbf{E}$ and $\mathbf{B}$ satisfying the desired
relations.


### Interpretation

- The inequality $|\mathbf{S}| \le c u$ is exactly the condition that makes the
  reconstruction possible.
- The choice of $\hat{\mathbf{e}}$ orthogonal to $\hat{\mathbf{s}}$ is a free
  polarization choice.
- The choice of sign in the quadratic solution is another branch freedom.
- More generally, one can rotate $(\mathbf{E},\mathbf{B})$ by a continuous
  duality transformation without changing $(u,\mathbf{S})$.

So the mapping $(u,\mathbf{S}) \mapsto (\mathbf{E},\mathbf{B})$ exists but is
not unique, as it should not be: $(u,\mathbf{S})$ contains fewer degrees of
freedom than $(\mathbf{E},\mathbf{B})$.


## Why non-uniqueness is not a defect

At a point in space-time, $(u,\mathbf{S})$ provides:

- 1 scalar degree of freedom (magnitude),
- 3 flux components (direction + magnitude),

for a total of 4 real numbers.

But $(\mathbf{E},\mathbf{B})$ provides 6 real numbers.

Therefore, 2 local degrees of freedom cannot be determined from $(u,\mathbf{S})$
alone. This is exactly what polarization is.

So when one says:

“fields arise from energy flow,”

the correct content is:

- energy flow determines the transported energy and its direction,
- polarization is additional relational structure not contained in
  $u$ alone, and not fully contained in $\mathbf{S}$ alone.

This is consistent with the lived content of electromagnetism: one may know the
energy and flux of a wave packet without knowing its polarization state.


## Why “orthogonal generation” appears

The frequent question “why does one generate the other orthogonally?” should be
recast as:

Why does divergence-free propagation *require* rotational coupling?

The minimal answer is:

- To propagate while remaining divergence-free, a field’s degrees of freedom
  must rotate into each other. Rotation in 3D is encoded by curl.
- Maxwell evolution is built from curl operators, hence it enforces rotational
  coupling between the two transverse degrees of freedom of propagation.

This is a structural statement: curl dynamics is the generic way to move a
divergence-free pattern without creating sources or sinks.

In this sense, “electric” and “magnetic” are names for the two interlocked
rotational aspects of a single propagating, divergence-free energy flow.


## Where toroidal winding numbers $(m,n)$ enter

The reconstruction above is local. Toroidal winding numbers are global.

On an invariant torus $T^2$, any smooth, source-free tangent flow
decomposes into windings around the two fundamental cycles. Closure forces the
slope to be rational, giving coprime integers $(m,n)$.

In a flow-first ontology:

- $(m,n)$ classify the global organization of energy transport on the
  torus,
- while $(\mathbf{E},\mathbf{B})$ provide a local representation of that same
  organization.

The role of $(m,n)$ is not to define $\mathbf{E}$ and
$\mathbf{B}$ pointwise, but to define the global circulation constraints
that $\mathbf{E}$ and $\mathbf{B}$ must satisfy when representing the
flow.


## What is proved, and what is not

What has been proven here:

- A scalar energy density alone cannot encode propagation.
- Continuity forces directional transport and hence vector structure.
- Divergence-free structure locally forces circulation in three dimensions.
- Given $(u,\mathbf{S})$ with $|\mathbf{S}|\le c u$, one can construct
  $\mathbf{E}$ and $\mathbf{B}$ reproducing the same energy and flux.
- The reconstruction is necessarily non-unique, matching polarization degrees of
  freedom.

What has not not proven *here*:

- Maxwell’s dynamical evolution equations derived from continuity alone.

Those belong to dynamics and solution classification, not to representation.


## Closing statement

A scalar energy observable does not generate electromagnetic vector fields by
itself. The *evolution* of energy under continuity forces transport, and
transport forces directional, circulating structure in three dimensions.

Electric and magnetic fields are the minimal local variables that represent this
structure while reproducing the observable pair $(u,\mathbf{S})$.

This is the precise conceptual bridge between a flow-first Maxwell ontology and
the standard $(\mathbf{E},\mathbf{B})$ description.
