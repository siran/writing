---
title: The Physics of Energy Flow - Minimal Propagating Closure of Source-Free Flow
date: 2026-03-13
---

# 203. Minimal Propagating Closure of Source-Free Flow

This appendix gives the mathematical step used structurally in chapter 7.

The result is the following.

> A single real first-order self-curl evolution of a divergence-free field does
> not produce neutral propagating transport. The minimal local propagating
> closure in this class requires two coupled divergence-free fields.

The point is not to postulate Maxwell's equations, but to show why they appear
as the minimal propagating closure of source-free rotational transport.

## 203.1 Source-Free Transport

Let

$$
\mathbf{F}(\mathbf{r},t)
$$

be a vector field on three-dimensional space.

Source-free transport means

$$
\nabla \cdot \mathbf{F} = 0.
$$

This expresses the absence of primitive beginnings or endings of the flow. If a
primitive start or end point were enclosed by a closed surface, the net flux
through that surface would not vanish. The source-free condition says that this
does not happen: the enclosed net flow remains identically zero.

## 203.2 Divergence Preservation Under Evolution

Assume a local first-order evolution relation

$$
\partial_t \mathbf{F} = \mathcal{D}(\mathbf{F}),
$$

where $\mathcal{D}$ is a spatial differential operator.

To preserve the source-free condition we require

$$
\nabla \cdot (\partial_t \mathbf{F}) = 0.
$$

Substituting the evolution relation gives

$$
\nabla \cdot \mathcal{D}(\mathbf{F}) = 0
$$

for every divergence-free field $\mathbf{F}$.

A natural local first-order differential operator with this property is curl,
since

$$
\nabla \cdot (\nabla \times \mathbf{A}) = 0
$$

for any vector field $\mathbf{A}$.

So a natural divergence-preserving self-update is

$$
\partial_t \mathbf{F} = k\,\nabla \times \mathbf{F}.
$$

We now examine whether this relation yields propagating transport.

## 203.3 Failure of the Single Self-Curl Relation

The simplest test is to differentiate the self-curl relation once more:

$$
\partial_t^2 \mathbf{F}
=
k\,\nabla\times(\partial_t\mathbf{F}).
$$

Substituting

$$
\partial_t \mathbf{F} = k\,\nabla \times \mathbf{F}
$$

gives

$$
\partial_t^2 \mathbf{F}
=
k^2\,\nabla\times(\nabla\times\mathbf{F}).
$$

Using the vector identity

$$
\nabla \times (\nabla \times \mathbf{F})
=
\nabla(\nabla\cdot\mathbf{F})-\nabla^2\mathbf{F},
$$

and the source-free condition

$$
\nabla\cdot\mathbf{F}=0,
$$

we obtain

$$
\partial_t^2 \mathbf{F}
=
-k^2\nabla^2\mathbf{F}.
$$

Equivalently,

$$
\partial_t^2 \mathbf{F} + k^2\nabla^2\mathbf{F}=0.
$$

This is not the neutral propagating wave equation, in which the second
temporal derivative term and the spatial Laplacian term appear with opposite
signs. Here both second-order terms enter with the same sign. A single
self-curl evolution therefore does not by itself furnish the propagating
closure we seek. It preserves turning, but it does not produce the neutral
propagating form.

There is also a direct obstruction to bodily transport.

Assume, for contradiction, that a nontrivial bounded closure could be carried
bodily by the single self-curl relation. Then there would exist a smooth
localized profile $\mathbf{G}$ and a constant drift velocity $\mathbf{v}$ such
that

$$
\mathbf{F}(\mathbf{r},t)=\mathbf{G}(\mathbf{r}-\mathbf{v}t).
$$

Differentiating gives

$$
\partial_t\mathbf{F}
=
-(\mathbf{v}\cdot\nabla)\mathbf{G},
\qquad
\partial_t^2\mathbf{F}
=
(\mathbf{v}\cdot\nabla)^2\mathbf{G}.
$$

Substituting this translating ansatz into

$$
\partial_t^2 \mathbf{F} + k^2\nabla^2\mathbf{F}=0
$$

gives

$$
(\mathbf{v}\cdot\nabla)^2\mathbf{G}+k^2\nabla^2\mathbf{G}=0.
$$

Now take the Euclidean inner product with $\mathbf{G}$ and integrate over all
space. Because $\mathbf{G}$ is localized, the boundary terms vanish under
integration by parts. Therefore

$$
\int \mathbf{G}\cdot(\mathbf{v}\cdot\nabla)^2\mathbf{G}\,dV
=
-\int \left|(\mathbf{v}\cdot\nabla)\mathbf{G}\right|^2\,dV
$$

and

$$
\int \mathbf{G}\cdot\nabla^2\mathbf{G}\,dV
=
-\int |\nabla\mathbf{G}|^2\,dV.
$$

So

$$
\int \left|(\mathbf{v}\cdot\nabla)\mathbf{G}\right|^2\,dV
+
k^2\int |\nabla\mathbf{G}|^2\,dV
=
0.
$$

Both integrands are nonnegative. Hence both integrals must vanish:

$$
(\mathbf{v}\cdot\nabla)\mathbf{G}=0,
\qquad
\nabla\mathbf{G}=0.
$$

So $\mathbf{G}$ is constant. Since $\mathbf{G}$ is localized, that constant
must be zero. Therefore the only localized rigidly translating solution of the
single self-curl relation is the trivial one.

This proves the point needed in the main text: a single self-curl update can
turn a structure, but it cannot carry a nontrivial bounded closure bodily from
one region to another.

## 203.4 Coupled Curl Evolution

Now introduce two divergence-free fields

$$
\mathbf{F}_+, \qquad \mathbf{F}_-.
$$

Consider the coupled evolution

$$
\partial_t \mathbf{F}_+ = k\,\nabla \times \mathbf{F}_-
$$

$$
\partial_t \mathbf{F}_- = -k\,\nabla \times \mathbf{F}_+.
$$

Taking a time derivative of the first equation,

$$
\partial_t^2 \mathbf{F}_+
=
k\,\nabla \times (\partial_t \mathbf{F}_-).
$$

Substituting the second equation,

$$
\partial_t^2 \mathbf{F}_+
=
-k^2\,\nabla \times (\nabla \times \mathbf{F}_+).
$$

Using the vector identity

$$
\nabla \times (\nabla \times \mathbf{F})
=
\nabla(\nabla\cdot\mathbf{F})-\nabla^2\mathbf{F},
$$

and the divergence-free condition

$$
\nabla\cdot\mathbf{F}_+ = 0,
$$

we obtain

$$
\partial_t^2 \mathbf{F}_+
=
k^2\nabla^2\mathbf{F}_+.
$$

Thus $\mathbf{F}_+$ satisfies the wave equation

$$
\partial_t^2\mathbf{F}_+ - k^2\nabla^2\mathbf{F}_+ = 0.
$$

The same derivation holds for $\mathbf{F}_-$.

## 203.5 Minimal Propagating Closure

The analysis shows:

- a single divergence-preserving self-curl evolution makes the temporal and
  spatial second-order terms enter with the same sign, not the neutral
  propagating form
- two coupled curl evolutions do yield neutral wave propagation

So the minimal propagating closure in this class is

$$
\partial_t \mathbf{F}_+ = k\,\nabla \times \mathbf{F}_-
$$

$$
\partial_t \mathbf{F}_- = -k\,\nabla \times \mathbf{F}_+.
$$

These equations preserve

$$
\nabla\cdot\mathbf{F}_+ = 0,\qquad
\nabla\cdot\mathbf{F}_- = 0.
$$

## 203.6 Electromagnetic Normalization

Now define

$$
\mathbf{E} \equiv \mathbf{F}_+,\qquad
\mathbf{B} \equiv \mathbf{F}_-/k.
$$

Then the coupled equations become

$$
\partial_t \mathbf{E} = k^2\nabla \times \mathbf{B}
$$

$$
\partial_t \mathbf{B} = -\nabla \times \mathbf{E}.
$$

With conventional constants absorbed into the normalization of $k$, these
correspond to the source-free Maxwell equations.

## 203.7 Interpretation

The two fields are not independent substances.

They are two complementary transverse aspects of the same organized source-free
transport. Their mutual curl coupling yields the minimal propagating structure
compatible with divergence-free flow.

## 203.8 Summary

Starting from divergence-free transport:

- curl preserves the source-free condition
- a single self-curl evolution makes the temporal and spatial second-order
  terms enter with the same sign, not the neutral propagating form
- two coupled curl evolutions yield neutral wave propagation
- the resulting equations coincide with the source-free Maxwell system

Maxwell dynamics therefore appears here as the minimal propagating closure of
source-free rotational transport.
