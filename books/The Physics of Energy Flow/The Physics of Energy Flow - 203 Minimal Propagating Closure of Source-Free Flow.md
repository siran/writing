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

This expresses the absence of primitive beginnings or endings of the flow.

## 203.2 Divergence Preservation Under Evolution

Assume a local first-order evolution law

$$
\partial_t \mathbf{F} = \mathcal{D}(\mathbf{F}),
$$

where $\mathcal{D}$ is a spatial differential operator.

To preserve the source-free condition we require

$$
\nabla \cdot (\partial_t \mathbf{F}) = 0.
$$

Substituting the evolution law gives

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

We now examine whether this law yields propagating transport.

## 203.3 Dynamics of the Single Self-Curl Law

Consider plane-wave modes

$$
\mathbf{F}(\mathbf{r},t)
=
\mathbf{f}\,e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)}.
$$

Because $\nabla\cdot\mathbf{F}=0$, the amplitude must satisfy

$$
\mathbf{k}\cdot\mathbf{f}=0.
$$

Substituting into

$$
\partial_t \mathbf{F} = k\,\nabla \times \mathbf{F}
$$

gives

$$
-i\omega\mathbf{f}
=
ik(\mathbf{k}\times\mathbf{f}).
$$

Rearranging,

$$
\omega\mathbf{f}
=
-k(\mathbf{k}\times\mathbf{f}).
$$

On the transverse plane, the operator $\mathbf{k}\times$ has eigenvalues

$$
\pm i|\mathbf{k}|.
$$

Therefore

$$
\omega = \pm i\,k|\mathbf{k}|.
$$

The time dependence becomes

$$
e^{-i\omega t} = e^{\pm k|\mathbf{k}|t}.
$$

So the modes either grow or decay exponentially.

A single self-curl evolution therefore does not produce neutral wave
propagation. It generates unstable rotational modes.

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

- a single divergence-preserving self-curl evolution does not yield neutral
  propagating solutions
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
- a single self-curl evolution produces unstable rotational modes
- two coupled curl evolutions yield neutral wave propagation
- the resulting equations coincide with the source-free Maxwell system

Maxwell dynamics therefore appears here as the minimal propagating closure of
source-free rotational transport.
