---
title: Canonical Glossary of Terms and Symbols for the Maxwell Universe Research Program
subtitle: Operational Definitions for Energy, Flow, Fields, and Structure
author: An M. Rodriguez, Alex Mercer
date: 2026-01-16
one-sentence-summary: This document defines, exhaustively and operationally, the terms and symbols used throughout the Maxwell Universe Research Program, fixing meanings and preventing hidden assumptions.
summary: We provide a complete glossary of terms and symbols used across the Maxwell Universe Research Program. All definitions are operational and descriptive, not metaphysical. The glossary separates representation from dynamics, avoids particle or spacetime primitives, and fixes terminology to ensure consistency across documents. This glossary is intended to be canonical.
keywords: Maxwell theory, glossary, continuity equation, divergence-free fields, energy flow, electromagnetic foundations
---

**One-Sentence Summary.** This document defines, exhaustively and operationally, the terms and symbols used throughout the Maxwell Universe Research Program, fixing meanings and preventing hidden assumptions.

**Abstract.** We provide a complete glossary of terms and symbols used across the Maxwell Universe Research Program. All definitions are operational and descriptive, not metaphysical. The glossary separates representation from dynamics, avoids particle or spacetime primitives, and fixes terminology to ensure consistency across documents. This glossary is intended to be canonical.

**Keywords.** Maxwell theory, glossary, continuity equation, divergence-free fields, energy flow, electromagnetic foundations

\begingroup
\setcounter{tocdepth}{2}
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
<li><a href="#summary">Summary</a>
</li>
<li><a href="#fundamental-quantities">Fundamental Quantities</a>
<ul>
</li>
<li><a href="#energy">Energy</a>
</li>
<li><a href="#energy-density">Energy density</a>
</li>
<li><a href="#energy-flux">Energy flux</a>
</li></ul>
</li>
<li><a href="#continuity-and-transport">Continuity and Transport</a>
<ul>
</li>
<li><a href="#continuity-equation">Continuity equation</a>
</li>
<li><a href="#continuity">Continuity</a>
</li>
<li><a href="#transport">Transport</a>
</li>
<li><a href="#flow">Flow</a>
</li></ul>
</li>
<li><a href="#kinematic-vs-dynamic">Kinematic vs Dynamic</a>
<ul>
</li>
<li><a href="#kinematic">Kinematic</a>
</li>
<li><a href="#dynamic">Dynamic</a>
</li>
<li><a href="#dynamical-closure">Dynamical closure</a>
</li>
<li><a href="#minimal-dynamical-closure">Minimal dynamical closure</a>
</li></ul>
</li>
<li><a href="#field-structure">Field Structure</a>
<ul>
</li>
<li><a href="#vector-field">Vector field</a>
</li>
<li><a href="#divergence-free">Divergence-free</a>
</li>
<li><a href="#source-free">Source-free</a>
</li>
<li><a href="#circulation">Circulation</a>
</li></ul>
</li>
<li><a href="#differential-operators">Differential Operators</a>
<ul>
</li>
<li><a href="#gradient">Gradient</a>
</li>
<li><a href="#curl">Curl</a>
</li>
<li><a href="#spatial-differential-operator">Spatial differential operator</a>
</li></ul>
</li>
<li><a href="#electromagnetic-fields">Electromagnetic Fields</a>
<ul>
</li>
<li><a href="#electric-field">Electric field</a>
</li>
<li><a href="#magnetic-field">Magnetic field</a>
</li>
<li><a href="#maxwell-electromagnetism">Maxwell electromagnetism</a>
</li></ul>
</li>
<li><a href="#representation">Representation</a>
<ul>
</li>
<li><a href="#representation">Representation</a>
</li>
<li><a href="#reconstruction">Reconstruction</a>
</li>
<li><a href="#polarization">Polarization</a>
</li>
<li><a href="#duality">Duality</a>
</li></ul>
</li>
<li><a href="#geometry-and-topology">Geometry and Topology</a>
<ul>
</li>
<li><a href="#topology">Topology</a>
</li>
<li><a href="#toroidal-shell">Toroidal shell</a>
</li>
<li><a href="#winding-numbers">Winding numbers</a>
</li>
<li><a href="#knot">Knot</a>
</li></ul>
</li>
<li><a href="#dimensionality">Dimensionality</a>
<ul>
</li>
<li><a href="#three-dimensionality">Three-dimensionality</a>
</li></ul>
</li>
<li><a href="#relation-and-change">Relation and Change</a>
<ul>
</li>
<li><a href="#configuration">Configuration</a>
</li>
<li><a href="#relation-between-configurations">Relation between configurations</a>
</li>
<li><a href="#two-snapshots-define-flow">Two snapshots define flow</a>
</li></ul>
</li>
<li><a href="#modeling-and-ontology">Modeling and Ontology</a>
<ul>
</li>
<li><a href="#model">Model</a>
</li>
<li><a href="#ontology">Ontology</a>
</li></ul>
</li>
<li><a href="#closing-summary">Closing Summary</a>
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

## Summary

This document defines the meaning of all technical terms and symbols used in the
Maxwell Universe Research Program.

Definitions are operational, descriptive, and context-specific. They describe
how quantities are used and related in the theory; they do not assert what
reality “is made of.”

No term implies particles, separate substances, or non-electromagnetic forces.

This glossary is intended to be canonical.


## Fundamental Quantities


### Energy

A conserved physical quantity inferred from experimental regularities. In this
program, energy is treated operationally through its measurable density and
transport.

Energy is not assumed to be a substance or object. It is what is transported,
and its transport is what gives rise to observable physical phenomena.

If there is no energy transport, there is nothing to describe.

Energy is positive by definition as a measure of presence relative to absence.
Negative values, when used, represent differences relative to a chosen reference
configuration.


### Energy density

$u(\mathbf{x},t)$

A nonnegative scalar field representing the amount of electromagnetic energy
associated with a region of space at a given time.

Energy density is a bookkeeping quantity. By itself, it does not encode motion,
direction, or causation.


### Energy flux

$\mathbf{S}(\mathbf{x},t)$

A vector field representing the local rate and direction of electromagnetic
energy transport through space.

$\mathbf{S}$ describes how energy moves. It does not imply a mechanical
fluid or particle substrate distinct from the field itself. In this program, the
electromagnetic field is the continuous medium of energy transport.


## Continuity and Transport


### Continuity equation


$$
\partial_t u + \nabla \cdot \mathbf{S} = 0
$$

A relation expressing local conservation of energy during continuous transport.

In this program, the continuity equation is treated as a description of observed
energy transport through space, not as a metaphysical postulate.


### Continuity

The empirical observation that, when energy moves through space, changes in
energy density are accounted for by transport rather than unexplained creation
or destruction.

Continuity constrains allowed histories but does not specify dynamics.


### Transport

Spatial redistribution of energy over time.

Transport through space requires spatial structure. Purely algebraic or purely
temporal change cannot, by itself, produce transport.


### Flow

A descriptive term for continuous transport of a conserved quantity, represented
mathematically by a vector field.

Flow refers to organized energy transport. It does not imply particles or a
separate mechanical medium; the field itself carries the flow.


## Kinematic vs Dynamic


### Kinematic

Constraints that restrict allowed configurations or histories without specifying
how evolution occurs.

Continuity is kinematic.


### Dynamic

Rules specifying how quantities evolve in time.

Dynamics describe how transport and reconfiguration occur.


### Dynamical closure

A specification of time evolution that completes a kinematic description.

A closure answers the question: how do allowed configurations change in time?


### Minimal dynamical closure

The weakest evolution rule capable of describing observed behavior while
preserving imposed constraints.

Minimal means:
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

Source-free does not deny the existence of localized structures in nature; it
denies primitive creation or destruction at points.


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

Transport is spatial redistribution and therefore requires spatial derivatives.


## Electromagnetic Fields


### Electric field

$\mathbf{E}$

A vector field used, together with $\mathbf{B}$, as part of a local
representation of electromagnetic energy transport and rotation.

$\mathbf{E}$ is representational, not assumed fundamental.


### Magnetic field

$\mathbf{B}$

A vector field paired with $\mathbf{E}$ to represent rotational aspects of
electromagnetic energy transport.

$\mathbf{B}$ is representational, not assumed fundamental.


### Maxwell electromagnetism

The curl-based dynamical system governing the coupled evolution of
$\mathbf{E}$ and $\mathbf{B}$.

In this program, Maxwell electromagnetism is understood as the minimal dynamical
description capable of transporting divergence-free energy flow while respecting
continuity.


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

A closed, surface-like organization of energy flow supporting persistent
circulation.

Toroidal shells are membrane-like structures.


### Winding numbers

$(m,n)$

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

The comparison between scalar configurations at different times.

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

The electromagnetic field is treated as the continuous medium of energy
transport. No additional substrate is assumed.

The framework is descriptive, minimal, and grounded in observed continuity of
energy transport through space.