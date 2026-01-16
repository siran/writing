---
title: Defining Electromagnetic Fields from Continuity and Divergence-Free Structure
subtitle: Two snapshots of a single scalar field define flow
author: An M. Rodriguez, Alex Mercer
date: 2026-01-16
one-sentence-summary: Continuity and divergence-free structure force electromagnetic energy to be described by directional, circulating degrees of freedom; however, energy density and flux alone do not uniquely determine the electric and magnetic fields without additional relational data.
summary: "We clarify the conceptual bridge between a field-only ontology of electromagnetic energy flow and the usual electric and magnetic field variables. We show rigorously that a single scalar energy density does not define propagation, but that the relation between scalar configurations at different times, constrained by continuity, forces the introduction of directional transport. We prove a reconstruction result: given an energy density u and an energy flux S satisfying |S| <= c u, one can always construct at least one pair of fields E and B that reproduce u and S. The non-uniqueness of this reconstruction matches the true physical degrees of freedom identified as polarization. We conclude with a precise statement of what is implied by continuity and what requires the full Maxwell dynamical law."
keywords: Maxwell theory, continuity equation, divergence-free fields, Poynting vector, energy density, field reconstruction, circulation, topology
---

**One-Sentence Summary.** Continuity and divergence-free structure force electromagnetic energy to be described by directional, circulating degrees of freedom; however, energy density and flux alone do not uniquely determine the electric and magnetic fields without additional relational data.

**Abstract.** We clarify the conceptual bridge between a field-only ontology of electromagnetic energy flow and the usual electric and magnetic field variables. We show rigorously that a single scalar energy density does not define propagation, but that the relation between scalar configurations at different times, constrained by continuity, forces the introduction of directional transport. We prove a reconstruction result: given an energy density u and an energy flux S satisfying |S| <= c u, one can always construct at least one pair of fields E and B that reproduce u and S. The non-uniqueness of this reconstruction matches the true physical degrees of freedom identified as polarization. We conclude with a precise statement of what is implied by continuity and what requires the full Maxwell dynamical law.

**Keywords.** Maxwell theory, continuity equation, divergence-free fields, Poynting vector, energy density, field reconstruction, circulation, topology

\begingroup
\setcounter{tocdepth}{1}
\renewcommand{\contentsname}{\centering Table of Contents}
\renewcommand{\numberline}[1]{#1.\hspace{0.6em}}
\setlength{\parskip}{0.35em}
\vspace{1.0\baselineskip}
\begin{center}\rule{0.35\linewidth}{0.4pt}\end{center}
\vspace{1.1\baselineskip}
\tableofcontents
\endgroup

```{=html}
<div class="toc">
<hr class="toc-divider" />
<div class="toc-title">Table of Contents</div>
<ul>
<li><a href="#motivation">Motivation</a>
</li>
<li><a href="#assumptions">Assumptions</a>
</li>
<li><a href="#why-a-scalar-field-alone-cannot-encode-propagation">Why a scalar field alone cannot encode propagation</a>
</li>
<li><a href="#divergence-free-structure-and-circulation-in-3d">Divergence-free structure and circulation in 3D</a>
</li>
<li><a href="#what-it-means-to-define-the-electromagnetic-field">What it means to define the electromagnetic field</a>
</li>
<li><a href="#reconstruction-lemma-from-umathbfs-to-mathbfemathbfb">Reconstruction lemma: from $(u,\mathbf{S})$ to $(\mathbf{E},\mathbf{B})$</a>
</li>
<li><a href="#why-orthogonal-coupling-appears">Why orthogonal coupling appears</a>
</li>
<li><a href="#where-toroidal-winding-numbers-mn-enter">Where toroidal winding numbers $(m,n)$ enter</a>
</li>
<li><a href="#conclusions">Conclusions</a>
</li>
<li><a href="#closing-statement">Closing statement</a>
</li>
</ul>
</div>
```


```{=latex}
\vspace{1.0\baselineskip}
\begin{center}\rule{0.35\linewidth}{0.4pt}\end{center}
\vspace{1.0\baselineskip}
```

```{=html}
<hr class="meta-divider" style="width:35%; margin:2rem auto; border:0; height:1px; background: rgba(0,0,0,0.35);" />
```

## Motivation

A recurring conceptual objection is:

If electromagnetic energy is taken as primary, and energy density is a scalar
field, how do vector fields such as $\mathbf{E}$ and $\mathbf{B}$ arise?

The objection is valid if one assumes that vectors must be extracted directly
from a single scalar configuration. They cannot.

A single scalar field does not define flow. Flow is defined by the **relation
between scalar configurations at different times under continuity**.

This distinction is central and non-negotiable.

The correct ordering is:

- a scalar energy density $u(\mathbf{x},t)$ is an observable of a process,
- continuity relates changes of that observable across time,
- the relation between two scalar configurations requires directional transport,
- directional transport is necessarily described in vectorial language.

Thus, vectors do not arise from scalars by inspection. They arise from **change
under constraint**.

This document makes that chain explicit and states precisely what can be
reconstructed from energy density and energy flow alone.


## Assumptions

We assume a source-free region.

We assume that electromagnetic energy admits:

1. A nonnegative energy density $u(\mathbf{x},t) \ge 0$.
2. An energy flux $\mathbf{S}(\mathbf{x},t)$ satisfying a continuity description

   $$
   \partial_t u + \nabla \cdot \mathbf{S} = 0.
   $$

This equation expresses the observed fact that when energy moves through space,
it does so continuously: changes in density are accounted for by transport.

We also assume the empirically observed causal bound

   $$
   |\mathbf{S}| \le c\,u,
   $$

which states that the rate of energy transport does not exceed the maximal
observed propagation rate. This is an operational fact about how energy is seen
to move through space, not a restriction on the possible ways transport may be
organized or described.

We do not assume particles, matter, constitutive media, quantum axioms, or
mechanical primitives.

We do not derive Maxwell’s dynamical equations from continuity alone. We instead
establish what continuity and divergence-free structure *force*, and what
additional structure is required to describe evolution.


## Why a scalar field alone cannot encode propagation

A scalar field $u(\mathbf{x},t)$ at a single time slice contains no information
about direction. It specifies magnitude only.

Two scalar snapshots, however, allow us to define transport. Given
$u(\mathbf{x},t_1)$ and $u(\mathbf{x},t_2)$, continuity requires that
differences between them be explained by motion through space.

That motion cannot be described without direction.

Thus, the continuity equation does not close on $u$ alone. It
introduces $\mathbf{S}$ as a necessary relational quantity. The pair
$(u,\mathbf{S})$ is the minimal description of conserved flow.

Vectors are therefore not additional structure. They are the minimal language
required to describe change consistently.


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

The integers $(m,n)$ do not define the electric or magnetic fields
pointwise.

They characterize the global organization of a particular energy flow: how that
flow wraps, closes, and circulates on a toroidal surface.

The fields $\mathbf{E}$ and $\mathbf{B}$ are a different kind of
description. They provide a local, differential account of how energy is
transported and rotated through space.

These are not competing structures. They are complementary descriptions of the
same underlying process.

In the same way that energy and frequency describe the same electromagnetic
phenomenon from different perspectives, $(m,n)$ describe the global
pattern of a flow, while $(\mathbf{E},\mathbf{B})$ describe its local transport.


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