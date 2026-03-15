---
title: A Maxwell Universe - Mechanics and Self-Refraction
date: 2026-03-15
---


# Mechanics and Self-Refraction

In the preceding chapter, discreteness appeared not from particles or quantum
rules, but from continuity and topology. The electromagnetic field could close
on itself only in discrete global classes.

That result concerned internal organization. A further question immediately
follows. If such bounded configurations are to count as ordinary matter, how do
they move? How do they carry momentum, resist acceleration, and persist instead
of dispersing?

In a Maxwell Universe, these questions cannot be answered by importing
Newtonian particles or external containers. They must be answered by the field
itself.

This chapter does two things:

- it shows how mechanics emerges from electromagnetic energy and momentum
  balance,
- it sharpens the self-refraction principle so it no longer means a vague
  "effective medium," but the redirection of one organized part of the field by
  the transport geometry induced by the rest of that same field.


## Conservation Laws in a Maxwell Universe

The only fundamental entity is the organized electromagnetic field. In the
resolved Maxwell form, its source-free dynamics is

$$
\nabla\cdot\mathbf E=0,
\qquad
\nabla\cdot\mathbf B=0,
$$

$$
\nabla\times\mathbf E=-\partial_t\mathbf B,
\qquad
\nabla\times\mathbf B=\mu_0\varepsilon_0\,\partial_t\mathbf E.
$$

These equations are not added to a particle world. They are the resolved
two-aspect transport closure of the same continuous field.


### Energy and Momentum Are Already Field Properties

The local energy density is

$$
u=\frac12\left(\varepsilon_0|\mathbf E|^2+\mu_0^{-1}|\mathbf B|^2\right),
$$

and the energy flux is

$$
\mathbf S=\mu_0^{-1}\mathbf E\times\mathbf B.
$$

Momentum is not an extra ingredient. It is already present in the field:

$$
\mathbf g=\frac{\mathbf S}{c^2}=\varepsilon_0\,\mathbf E\times\mathbf B.
$$

The total momentum of a localized configuration in a region $V$ is therefore

$$
\mathbf P=\int_V \mathbf g\,d^3x.
$$

No independent mass parameter has yet been introduced.


### Local Balance Laws

Maxwell transport gives two exact local balance equations.

Energy continuity:

$$
\partial_t u+\nabla\cdot\mathbf S=0.
$$

Momentum continuity:

$$
\partial_t g_i-\partial_j T_{ij}=0,
$$

where the Maxwell stress tensor is

$$
T_{ij}
=
\varepsilon_0\left(E_iE_j-\frac12\delta_{ij}\mathbf E^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j-\frac12\delta_{ij}\mathbf B^2\right).
$$

Integrating the momentum law over a volume $V$ gives

$$
\frac{d\mathbf P}{dt}
=
\int_{\partial V}\mathbf T\cdot d\mathbf A.
$$

So momentum changes only when electromagnetic stress crosses the boundary.
Mechanics is already here. It is bookkeeping for transported field momentum.


### Center of Energy and Inertia

Let

$$
U=\int_V u\,d^3x
$$

be the total energy of a bounded configuration, and define its center of energy

$$
\mathbf R(t)=\frac{1}{U}\int_V \mathbf r\,u\,d^3x.
$$

For an isolated bounded mode, the boundary energy flux vanishes, so $U$ is
constant. Using

$$
\partial_t u=-\nabla\cdot\mathbf S,
$$

one obtains

$$
\frac{d}{dt}\int_V \mathbf r\,u\,d^3x
=
\int_V \mathbf S\,d^3x,
$$

hence

$$
\mathbf P
=
\frac{1}{c^2}\int_V \mathbf S\,d^3x
=
\frac{U}{c^2}\,\frac{d\mathbf R}{dt}.
$$

This is the exact center-of-energy identity.

It suggests the inertial mass of a bounded mode:

$$
m:=\frac{U}{c^2}.
$$

Then

$$
\mathbf P=m\,\dot{\mathbf R},
$$

and the boundary stress law becomes

$$
\mathbf F_{\mathrm{ext}}
:=
\frac{d\mathbf P}{dt}
=
\int_{\partial V}\mathbf T\cdot d\mathbf A.
$$

For a closed mode with constant $U$,

$$
\mathbf F_{\mathrm{ext}}=m\,\ddot{\mathbf R}.
$$

So inertia and Newtonian-looking mechanics are not primitive axioms. They are
compact descriptions of electromagnetic energy and momentum bookkeeping for a
bounded closure.


## Why a Bounded Mode Can Exist

Mechanics explains how a bounded configuration moves if it already exists. It
does not yet explain why such a configuration does not simply disperse.

The answer cannot be an external box or a material background, because neither
exists in a Maxwell Universe. The closure must persist by the field's own
transport.

Here the distinction between local reorganization and transport matters.

- A single curl reorganizes locally.
- A doubled curl transports.

An open transporting pattern is not yet matter. A material mode is transport
folded back onto itself so that the transport closure remains bounded.

That folded transport is what AMU Part II calls **self-refraction**.


## Self-Refraction

The phrase should now be read precisely.

Self-refraction does **not** mean:

- propagation through a second medium,
- a delayed secondary field added on top of the first,
- a modification of Maxwell's equations.

It means:

> one organized part of the field redirects another part of the same field
> because the total transport geometry is determined by the whole configuration
> at once.

The field does not travel through something else. The field is the thing that
sets the transport conditions.


### Why Superposition Is Already Interaction

Write a bounded configuration as a sum of coherent components:

$$
\mathbf E=\sum_k \mathbf E_k,
\qquad
\mathbf B=\sum_k \mathbf B_k.
$$

Then the Poynting vector is

$$
\mathbf S
=
\frac{1}{\mu_0}\sum_{k,\ell}\mathbf E_k\times\mathbf B_\ell.
$$

The Maxwell stress is likewise quadratic:

$$
T_{ij}
=
\varepsilon_0\left(E_iE_j-\frac12\delta_{ij}\mathbf E^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j-\frac12\delta_{ij}\mathbf B^2\right).
$$

So when coherent parts of the same bounded mode overlap, cross terms appear in
both energy transport and momentum transport.

Those cross terms are not optional corrections. They are the exact
redistribution terms of the total field. They redirect energy flow and stress
across the entire extent at once.

That is the rigorous content of "the field interacts with itself."


### Self-Refraction as Same-Substrate Redirection

Because the transport relation is imposed simultaneously for all points in the
extent, self-refraction is not the path of a tagged bit of substance through a
pre-existing medium.

It is the whole-field statement that one region of the closure changes the
transport geometry seen by neighboring regions of that same closure.

In a toroidal or helical mode:

- one part of the circulation loads the axial path,
- another part carries the transport around the closure,
- the transported energy is continuously redirected back into the bounded mode
  instead of leaking away.

So a knot is not "light trapped in a box." It is transport whose own geometry
keeps turning subsequent transport back into the closure.

This is why the phrase `self-refraction` is worth keeping. It names the fact
that the field is both the transported thing and the thing that shapes the path
of that transport.


## Stability as Identity

A bounded electromagnetic mode persists when dispersion is balanced by this
same-substrate redirection.

The mode exists because:

- transport is real,
- transport can close on itself,
- the closure redirects later transport back into the same organized pattern.

The identity of the object is therefore not a separate substance hidden behind
the field. The identity **is** the persistent closure.

Matter, on this view, is electromagnetic transport maintained by its own
self-refraction.


## Summary

Mechanics emerges from the exact field balances

$$
\partial_t u+\nabla\cdot\mathbf S=0,
\qquad
\partial_t g_i-\partial_jT_{ij}=0.
$$

For a bounded mode,

$$
\mathbf P=\frac{U}{c^2}\dot{\mathbf R},
\qquad
m=\frac{U}{c^2},
$$

so inertia and Newton-like motion are compact descriptions of electromagnetic
energy and momentum transport.

Stability requires more: not merely local turning, but transporting closure
folded back onto itself.

That folded transport is self-refraction. It is not a second medium and not a
secondary field. It is the exact redirection of one organized part of the field
by the transport geometry induced by the rest of that same field.
