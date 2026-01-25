---
title: Deriving Newton and Maxwell Dynamics From Continuous, Divergence-Free Energy Transport
subtitle: No axioms, no postulates
author: An M. Rodriguez, Alex Mercer
date: 2026-01-20
one-sentence-summary: Newtonian and Maxwellian dynamics arise as consequences of continuous, divergence-free energy transport, without independent postulates.
summary: We show that assuming only continuous, local energy transport without sources forces two results. First, curl-based evolution is the minimal dynamical closure, yielding Maxwell electromagnetism. Second, stable circulating energy configurations behave as inertial objects whose momentum balance obeys Newtonian laws. No separate axioms for force, mass, or fields are introduced.
keywords: continuity equation, divergence-free flow, curl dynamics, Maxwell theory, Newton laws, minimal dynamics
---

# Overview

This document derives, in a rigorous and step-by-step manner, Newtonian and
Maxwellian dynamics from two empirically grounded observations:

- energy is not observed to appear or disappear spontaneously in space,
- energy is observed to move continuously through space.

From these facts —expressed as continuous, local, divergence-free energy
transport— we derive:

1. Maxwell electromagnetism as the minimal dynamics of divergence-free flow.
2. Newtonian mechanics as the effective description of stable circulating
   energy.

No axioms are assumed. The usual axioms of force, mass, or fields, are instead
derived from the two observations above.


# Part I — Kinematic Foundations

## Energy and continuity

We assume only:

- a nonnegative energy density u(x,t),
- an energy flux S(x,t),
- a continuity description of transport,

∂_t u + ∇·S = 0.

This equation expresses the observed fact that changes in energy density are
accounted for by transport of such energy through space.


## Source-free structure

In regions without primitive creation or destruction of energy,

∇·S = 0.

This condition expresses the fact that we are modeling a space where for energy
to move from one place to another it has to displace continuously through space,
rather than poping-up into existence elsewhere, or, in other words,
"teleporting" itself to another location.

**We are not forbidding this behavior from happening, we are just modeling when
it does *not* happen because that is what is observed in our shared everyday
existence.**

Surprinsingly, Newton's 3 laws and Maxwell's 4 laws for electromagnegtism follow
from this observation. Even perhaps most surprinsingly is that we finally
*define* inertia -- from the continuity equation.


## Closure of flow lines

The transport field S defines flow lines as integral curves γ(t) satisfying

γ̇(t) = S(γ(t)).

**If a flow line were to begin or end at an interior point, that point would act
as a source or sink, implying nonzero divergence.**

Therefore:

In a bounded source-free region, continuous transport forces flow lines to close
on themselves.

In the language of linear algebra (vectors, matrices, ...), *transport* can be
seen as a continuous transformation from one state into another. To *transform*
one vector into another, we change it's length and rotate. We do this for all
vectors in the vector field $F$, that represents energy trasport,
or *flow*.

So a change in F implies a streching and a rotation of the field. From geometric
algebra, we can write:

$$
\delta_t F = \nabla \cdot F + \nabla \cross F
$$

Closed flow is not an assumption. It is a consequence of continuity and the
absence of divergence.


## Circulation as a forced consequence

Closed flow lines represent persistent circulation.

Thus, we can conclude that:

  - divergence-free transport generically organizes into circulating patterns,
    and

  - circulation is enforced by continuity.


# Part II — Maxwell Dynamics

## The closure problem

The continuity description constrains accounting ("how much" flow) but does not
specify a description of "how" transport evolves.

To describe how energy flow rearranges spatially we need to figure out the
dynamics of the flow.


## General form of transport evolution

Consider a divergence-free vector field F(x,t).

By definition, any local transport law must involve spatial derivatives. That
is, we must specify that changes of a quantity *in space*. This is expressed
with differential language:

∂_t F = D(F).

In other words: the field's change in time happen because the field changes
*continuously*, divergence-free, in space.


## Failure of gradient-driven evolution

If evolution is gradient-driven,

∂_t F = ∇φ,

then

∂_t(∇·F) = ∇²φ,

which is generically nonzero.

Gradient-driven evolution creates or destroys divergence and therefore cannot
describe source-free transport.


## Curl as the minimal divergence-preserving operator

If evolution is curl-driven,

∂_t F = ∇×G,

then

∂_t(∇·F) = 0

identically.

Curl-based evolution preserves divergence-free structure and redistributes flow
by rotating existing flow lines without creating or destroying them.

---


## Emergence of Maxwell dynamics

Maxwell’s equations are precisely of this curl-based form. Electric and magnetic
components rotate into one another, preserving divergence-free structure by
construction.

Maxwell dynamics is therefore not postulated. It is the minimal evolution law
compatible with continuous, source-free transport.

---


# Part III — Newtonian Dynamics

## Circulating energy as inertial structure

Closed circulation traps momentum. Momentum stored in circulation does not
contribute to net translation but resists changes in motion.

This resistance is inertia.

---


## Definition of mass

In this framework, inertial mass measures the amount of momentum bound in
persistent circulation.

Mass is not a primitive substance. It is a dynamical property of stable energy
flow.

---


## Newton’s First Law

A stable circulating configuration maintains its state of motion unless acted
upon by external transport imbalance.

This is persistence of circulation under divergence-free transport.

---


## Newton’s Second Law

External transport imbalance changes total momentum according to the rate of
momentum flux across a boundary.

Force is defined as momentum flow, yielding

F = dP/dt.

---


## Newton’s Third Law

Momentum conservation follows directly from continuity: momentum exchanged
between subsystems is equal and opposite.

Action and reaction are bookkeeping identities of transport.

---


# Closing Statement

From continuity and divergence-free transport alone:

- curl-based evolution is forced, yielding Maxwell dynamics,
- stable circulation yields inertia and Newtonian motion.

No axioms for force, mass, or fields are required.

What appears as mechanics and electromagnetism is the geometry of energy in
motion.
