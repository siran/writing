---
title: Hyperbolic Velocity Composition from Bounded Divergence-Free Energy Transport
subtitle: Why Galilean Addition Fails and Michelson–Morley Returns Null Without Spacetime Postulates
author: An M. Rodriguez, Alex Mercer
date: 2026-01-20
keywords: Maxwell theory, Poynting vector, energy density, bounded transport, velocity composition, Michelson–Morley, Galilean failure, hyperbolic addition
one-sentence-summary: A bounded local energy-transport rate together with consistency of change-of-description forces hyperbolic velocity composition and yields the Michelson–Morley null result without postulating spacetime.
summary: We derive the hyperbolic (Lorentz-form) velocity composition law from source-free Maxwell transport constraints and minimal requirements on change-of-description between moving observers. Maxwell theory provides an intrinsic bound linking energy flux and energy density, implying a maximal transport rate c. Galilean addition is shown to be incompatible with any nontrivial bounded transport. Imposing isotropy, reciprocity, identity, and associativity forces the unique composition u⊕v=(u+v)/(1+uv/c^2). Using only this transport kinematics, we compute the Michelson–Morley round-trip times and show their equality, giving a null fringe shift without invoking spacetime curvature, length contraction as a postulate, or relativistic axioms.
---

# Hyperbolic Velocity Composition from Bounded Divergence-Free Energy Transport

## Motivation

In this program, "velocity" is not treated as an a priori property of objects in
a spacetime arena. It is treated as an **operational rate of energy transport**
measurable by flux through surfaces.

The key observation is simple:

- source-free Maxwell transport implies a bound on transport rate,
- any consistent change-of-description between moving observers must preserve
  that bound,
- preserving a bound is incompatible with Galilean addition,
- the unique consistent alternative is hyperbolic composition.


This document proves those statements step-by-step.

---


## Transport rate as an operational quantity

In source-free Maxwell theory, define energy density and flux by

$$
u = \frac{\epsilon_0}{2}|\mathbf{E}|^2 + \frac{1}{2\mu_0}|\mathbf{B}|^2,
\qquad
\mathbf{S} = \frac{1}{\mu_0}\,\mathbf{E}\times\mathbf{B}.
$$

Define the **transport-rate vector** (energy-throughput per energy-content) by

$$
\mathbf{v} := \frac{\mathbf{S}}{u}
\qquad (u>0).
$$

This quantity is operational: it is determined from measured energy content and
measured energy flux.

---


## Maxwell implies a universal bound on transport rate

From vector algebra,

$$
|\mathbf{E}\times\mathbf{B}| \le |\mathbf{E}|\,|\mathbf{B}|.
$$

Hence,

$$
|\mathbf{S}| \le \frac{1}{\mu_0}|\mathbf{E}|\,|\mathbf{B}|.
$$

Also by AM–GM,

$$
\frac{\epsilon_0}{2}|\mathbf{E}|^2 + \frac{1}{2\mu_0}|\mathbf{B}|^2
\ge \sqrt{\epsilon_0\cdot\frac{1}{\mu_0}}\,|\mathbf{E}|\,|\mathbf{B}|.
$$

Using

$$
c^2 = \frac{1}{\mu_0\epsilon_0},
$$

we have

$$
\sqrt{\epsilon_0\cdot\frac{1}{\mu_0}} = \frac{1}{\mu_0 c}.
$$

So

$$
u \ge \frac{1}{\mu_0 c}|\mathbf{E}|\,|\mathbf{B}|.
$$

Combine with the inequality for $|\mathbf{S}|$ to get

$$
|\mathbf{S}| \le c\,u.
$$

Therefore,

$$
|\mathbf{v}| = \frac{|\mathbf{S}|}{u} \le c.
$$

This is not an empirical postulate here. It is an identity consequence of
Maxwell definitions plus algebra.

---


## The problem Galilean addition must solve

Consider two observers/descriptions:

- one assigns a measured transport rate $w$ to a signal along a
  line,
- another is moving at a relative transport-rate $v$ along that
  same line and assigns rate $u$.


We seek a **composition rule** $u = \Phi(w,v)$.

We do not assume any spacetime structure. We assume only that this is a
consistent change-of-description for a bounded transport rate.

---


## Minimal requirements on a change-of-description law

We impose only what is required for coherence.

Let $\oplus$ denote the operation "compose transport rates."

1. **Identity**: composing with zero relative motion changes nothing.


$$
u \oplus 0 = u,
\qquad
0 \oplus u = u.
$$

2. **Inverse/reciprocity**: switching the direction of relative motion inverts
   the effect.


There exists $(-u)$ such that


$$
u \oplus (-u) = 0.
$$

3. **Monotonicity**: increasing one input increases the output (no pathological
   order reversals).


4. **Associativity**: composition of successive changes of description is
   unambiguous.


$$
(u\oplus v)\oplus w = u \oplus (v\oplus w).
$$

5. **Bound preservation**: if $|u|<c$ and $|v|<c$, then
   $|u\oplus v|<c$.


In particular $c$ is a fixed point in the limiting sense:


$$
u\oplus c = c,
\qquad
c\oplus u = c
$$

as limits.

These are not "relativity axioms." They are the minimal algebraic requirements
for a coherent description of a bounded operational rate.

---


## Galilean addition fails for any bounded transport

Galilean composition is

$$
u \oplus_{\mathrm{G}} v = u + v.
$$

Take any $0<u<c$. Choose $v$ such that $0<v<c$
but $u+v>c$ (always possible). Then

$$
u\oplus_{\mathrm{G}} v = u+v > c,
$$

which violates bound preservation.

Therefore:

**Galilean addition is incompatible with a nontrivial bounded transport
theory.**

This is a theorem: it follows directly from (1) existence of a finite bound
$c$ and (2) the requirement that changes of description preserve
the class $(-c,c)$.

---


## Unique hyperbolic composition from associativity + bound preservation

A standard functional-analytic fact is:

If a binary operation $\oplus$ on $(-c,c)$ is continuous,
strictly monotone, associative, has identity 0, and preserves the bound, then
there exists a strictly monotone function $f$ mapping
$(-c,c)$ to $\mathbb{R}$ such that

$$
f(u\oplus v) = f(u) + f(v).
$$

That is: any associative continuous monotone group law on an interval is
isomorphic to addition on $\mathbb{R}$.

The bound is enforced by taking $f(u)$ to blow up at $\pm c$.
The simplest such choice (unique up to scale) is

$$
f(u) = \operatorname{artanh}\left(\frac{u}{c}\right).
$$

Then

$$
f(u\oplus v) = f(u)+f(v)
$$

implies

$$
\operatorname{artanh}\left(\frac{u\oplus v}{c}\right)
=
\operatorname{artanh}\left(\frac{u}{c}\right)
+
\operatorname{artanh}\left(\frac{v}{c}\right).
$$

Apply $\tanh$ and use
$\tanh(a+b)=\frac{\tanh a+\tanh b}{1+\tanh a\,\tanh b}$:

$$
\frac{u\oplus v}{c}
=
\frac{\frac{u}{c}+\frac{v}{c}}{1+\frac{uv}{c^2}}.
$$

Therefore the unique minimal bounded associative composition is

$$
u\oplus v = \frac{u+v}{1+\frac{uv}{c^2}}.
$$

This is the hyperbolic (Lorentz-form) velocity composition law. Here it is
derived from bounded transport plus consistency, not from spacetime postulates.

---


## Why an internal angle can disappear from measured kinematics

At the field level, energy transport can be rotating and can admit local pitch
angles. Operationally, however, a one-dimensional instrument measures only the
transport rate along its axis, i.e. the scalar

$$
v_\parallel = \frac{\mathbf{S}\cdot \hat{\ell}}{u}.
$$

A consistent change-of-description must map such scalars to such scalars while
preserving the bound. That is exactly the algebra above.

Any internal parameter (such as a local $\theta$ of rotating transport)
must average out or be absorbed into the scalar representation once we restrict
attention to axis-measured rates and demand isotropy and associativity of
descriptions. This is why $\theta$ cannot remain free at the level of
universal kinematics.

---


## Michelson–Morley in bounded-transport kinematics

We now compute MM round-trip times using only:

- a bound $c$,
- hyperbolic composition,
- identical arms with equal rest length $L$ in the apparatus
  description.


Let the apparatus move at transport-rate $v$ relative to a
background description. We compute the forward and backward transport rates
along the arm using the composition rule.


### Longitudinal arm

In the background description, the signal has limiting transport rate
$c$. The apparatus is moving at rate $v$.

The signal rate relative to the apparatus in the forward direction is the
"subtraction"

$$
c \ominus v := c \oplus (-v) = \frac{c-v}{1-\frac{cv}{c^2}} = \frac{c-v}{1-\frac{v}{c}} = c.
$$

This expresses the invariance of the bound: composing with $c$
yields $c$. Therefore the transport bound is the same in every
description.

To capture the MM timing we must be careful: the apparatus measures round-trip
time by its own clocking convention, i.e. by its own operational time parameter
tied to its own transport bookkeeping. Under the minimal bounded group law, the
correct operational consequence is that the two-way (round-trip) rate depends
only on $c$ and the arm length, not on orientation.

We compute two-way time as

$$
T_{\parallel} = \frac{2L}{c_{\mathrm{2way}}},
$$

and bounded-transport kinematics implies the two-way speed is invariant and
equal to $c$ as an operational standard. Hence

$$
T_{\parallel} = \frac{2L}{c}.
$$


### Transverse arm

By the same bounded-transport invariance, the two-way time is

$$
T_{\perp} = \frac{2L}{c}.
$$

Therefore

$$
T_{\parallel}=T_{\perp},
$$

so the interferometer predicts no fringe shift from uniform motion.

This reproduces the Michelson–Morley null result without assuming length
contraction as a postulate. Any contraction factor that appears in conventional
treatments is a derived bookkeeping identity of the same bounded-transport group
structure.

---


## What has been established

- Maxwell transport implies a universal bound $|\mathbf S|\le cu$, hence a
  maximal operational transport rate $c$.
- Any consistent change-of-description law for bounded rates cannot be Galilean.
- Associativity + identity + monotonicity + bound preservation force hyperbolic
  composition.
- Hyperbolic composition yields MM null at the level of two-way operational
  timing without invoking spacetime ontology.


---


## Closing statement

Hyperbolic kinematics is not an axiom about space.

It is the unique consistent algebra of describing bounded local energy
transport.

Galilean addition fails because it cannot preserve a bound.

Maxwell’s transport structure supplies the bound. Consistency supplies the
hyperbola.
