---
title: Canonical Glossary of Terms and Symbols for the Maxwell Universe Research Program
subtitle: Operational Definitions for Energy, Flow, Fields, and Structure
author: An M. Rodriguez, Alex Mercer
date: 2026-01-16
one-sentence-summary: This document defines, exhaustively and operationally, the terms and symbols used throughout the Maxwell Universe program, fixing meanings and preventing hidden assumptions.
summary: We provide a complete glossary of terms and symbols used across the Maxwell Universe program. All definitions are operational and descriptive, not metaphysical. The glossary separates representation from dynamics, avoids particle or spacetime primitives, and fixes terminology to ensure consistency across documents. This glossary is intended to be canonical.
keywords: Maxwell theory, glossary, continuity equation, divergence-free fields, energy flow, electromagnetic foundations
---

## Summary

This document defines the meaning of all technical terms and symbols used in the
Maxwell Universe Research program.

Definitions are **operational**, **descriptive**, and **context-specific**. They
describe how quantities are used and related in the theory; they do not assert
what reality “is made of.”

No term implies "particles" or separate non-electromagnetic substances, forces,
etc.

This glossary is intended to be **canonical**.


## Fundamental Quantities

### Energy

A conserved physical quantity inferred from experimental regularities. In this
program, energy is treated operationally through its measurable density and
transport.

Energy is not assumed to be a substance, object, or material. However it it's
what is being transported, and whose transport makes everything happen.

If there is no "energy transport" (and thus, simply, "energy"), there is nothing
to describe.

It is positive by definition because "something" is always more than "nothing";
and also "something" is more than "a lack of", which is represented by negative
numbers. "Holes" being "something" is more about what is there around the empty
hole.

That negative values "can be achieved" depends on the initial conditions.


### Energy density

$\mathbf{u}(\mathbf{x},t)$

A nonnegative scalar field representing the amount of electromagnetic energy
associated with a region of space at a given time.

Energy density is a bookkeeping quantity. By itself, it does not encode motion,
direction, or causation.


### Energy flux

$\mathbf{S}(\mathbf{x},t)$

A vector field representing the local rate and direction of electromagnetic
energy transport through space.

$\mathbf{S}$ is part of a transport description. It does not imply a medium
or mechanical flow.


## Continuity and Transport

### Continuity equation

The relation

$$
\partial_t u + \nabla \cdot \mathbf{S} = 0
$$

which expresses local conservation of energy during continuous transport.

In this program, the continuity equation is treated as a **description of
observed energy transport through *space***, not as a metaphysical postulate.


### Continuity

The empirical observation that, when energy moves through space, changes in
energy density are accounted for by transport rather than unexplained creation
or destruction.

Continuity constrains allowed histories but does not specify dynamics.


### Transport

Spatial redistribution of energy over time.

Transport through space requires a spatial structure. Thus, purely algebraic or
purely temporal change can't produce transport by themselves.


### Flow

A descriptive term for continuous transport of a conserved quantity, represented
mathematically by a vector field.

“Flow” does not imply a fluid, medium, or substance.


## Kinematic vs Dynamic

### Kinematic

Constraints that restrict allowed configurations or histories without specifying
how evolution occurs.

Continuity is kinematic.


### Dynamic

Rules specifying how quantities evolve in time.

Dynamics are required to describe *how* transport happens, not merely *that* it
is conserved.


### Dynamical closure

A specification of time evolution that completes a kinematic description.

A closure answers the question: *how do allowed configurations change in time?*


### Minimal dynamical closure

The weakest evolution rule capable of describing observed behavior while
preserving imposed constraints.

“Minimal” means:
- no auxiliary fields,
- no nonlocal prescriptions,
- no higher-order structure than required.

It does not mean unique, complete, or final.


## Field Structure

### Vector field

A mathematical object assigning a direction and magnitude to each point in
space.

Vector fields are descriptive tools, not assumed physical substances.


### Divergence-free

A property of a vector field $\mathbf{F}$ satisfying

$$
\nabla \cdot \mathbf{F} = 0
$$

in a given region.

Divergence-free means there are no local sources or sinks.


### Source-free

A description of regions where divergence-free structure holds.

“Source-free” does not deny the existence of localized structures in nature; it
denies primitive creation or destruction of energy at points.


### Circulation

Closed or looping transport of a divergence-free flow.

Circulation is a geometric property of transport, not a force or interaction.


## Differential Operators

### Gradient

$$
\nabla \phi
$$

A vector derived from a scalar field $\phi$.

Gradient-driven evolution generically creates or destroys divergence and cannot
serve as a general source-free transport description.


### Curl

$$
\nabla \times \mathbf{F}
$$

A vector operator in three dimensions measuring local circulation.

Curl-based evolution preserves divergence-free structure identically.


### Spatial differential operator

An operator involving derivatives with respect to spatial coordinates.

Spatial transport dynamics must involve spatial differential operators because
transport is spatial redistribution.


## Electromagnetic Fields

### Electric field

$$
\mathbf{E}
$$

A vector field paired with $\mathbf{B}$ (see below) used as part of a local
representation of electromagnetic energy transport and rotation.

$\mathbf{E}$ is not assumed fundamental; it is a representational variable.


### Magnetic field

$$
\mathbf{B}
$$

A vector field paired with $\mathbf{E}$ (see above) to represent rotational
aspects of electromagnetic energy transport.

$\mathbf{B}$ is not assumed fundamental.


### Maxwell electromagnetism

The curl-based dynamical system governing the coupled evolution of
$\mathbf{E}$ and $\mathbf{B}$.

In this program, Maxwell electromagnetism is understood as the **minimal
dynamical description** capable of transporting divergence-free energy flow
while respecting continuity.


## Representation

### Representation

A mapping from observable transport quantities (such as $u$ and
$\mathbf{S}$) to auxiliary fields (such as $\mathbf{E}$ and
$\mathbf{B}$).

Representations may be non-unique and need not determine dynamics.


### Reconstruction

The process of constructing fields $\mathbf{E}$ and $\mathbf{B}$ that
reproduce a given energy density $u$ and flux $\mathbf{S}$.

Reconstruction is generally non-unique.


### Polarization

Degrees of freedom not fixed by $u$ and $\mathbf{S}$ alone.

Polarization corresponds exactly to the non-uniqueness of reconstruction.


### Duality

Continuous transformations of $(\mathbf{E},\mathbf{B})$ that leave observable
quantities invariant.

Duality reflects representational freedom, not physical ambiguity.


## Geometry and Topology

### Topology

Global properties of field organization invariant under continuous deformation.

Topology constrains which configurations can change smoothly.


### Toroidal shell

A closed, surface-like with one hole, organization of energy flow supporting
persistent circulation.

Toroidal shells are membrane-like structures.


### Winding numbers

$$
(m,n)
$$

Integers labeling how a flow wraps around the independent cycles of a toroidal
surface.

$(m,n)$ characterize global flow organization, not local field values.


### Knot

A topologically nontrivial closed configuration of energy flow.

Knots cannot be undone by continuous deformation without reconnection.


## Dimensionality

### Three-dimensionality

The spatial dimensionality in which:
- curl maps vectors to vectors,
- divergence-free flows admit circulation,
- knotted structures exist.

Many stability features described in this program rely essentially on three
dimensions.


## Relation and Change

### Configuration

A spatial distribution of a quantity at a given time.


### Relation between configurations

The comparison between "snapshots" or "time slices" of configurations.

Flow is defined by relations between configurations, not by a single snapshot.


### Two snapshots define flow

A shorthand statement meaning:

A single scalar configuration does not encode transport. Directional transport
is defined by how scalar configurations change relative to each other under
continuity.


## Modeling and Ontology

### Model

A mathematical description of observed regularities.

Models do not assert ultimate ontology.


### Ontology

Claims about what exists fundamentally.

This program deliberately limits ontological commitments.


## Closing Summary

All terms in this glossary are defined operationally.

No term implies particles, substances, forces, or spacetime structure unless
explicitly stated.

The framework is descriptive, minimal, and grounded in observed continuity of
energy transport through space.
