---
title: The Physics of Energy Flow – Curl Preserves Flow
date: 2026-03-11
---


# 6. Curl Preserves Flow

To preserve the source-free character of transport, local evolution must allow
the flow of energy without introducing primitive endpoints. We therefore ask
what kinds of local update can reorganize a flow while keeping it source-free.

A purely algebraic change, such as rescaling

$$
\mathbf{S} \mapsto \lambda \mathbf{S},
$$

can strengthen or weaken an existing flow, but it does not explain how the
flow turns or reorganizes in space.

To say this more precisely, take any region $V$ with closed boundary
$\partial V$. Gauss's theorem gives

$$
\int_V \nabla \cdot (\Delta \mathbf{S})\,dV
=
\oint_{\partial V} \Delta \mathbf{S} \cdot d\mathbf{A}.
$$

So divergence measures the net transport across a closed boundary. If it is
nonzero, more flow leaves than enters, or more enters than leaves. In that
case the transport behaves locally like a source or a sink. In the source-free
case it must therefore remain identically zero.

A gradient-type update does introduce spatial structure:

$$
\Delta \mathbf{S} = \nabla \phi.
$$

But then

$$
\nabla \cdot (\Delta \mathbf{S}) = \nabla^2 \phi,
$$

which is generally nonzero. Such an update can compress, expand, begin, or end
the transport. It does not preserve source-free reorganization.

The remaining possibility is local turning. In three dimensions, take

$$
\mathbf{A} = \left(0,0,\frac{x^2+y^2}{2}\right).
$$

Then

$$
\nabla \times \mathbf{A} = (y,-x,0),
$$

which circles around the $z$-axis. The flow bends continuously without
starting or stopping, and

$$
\nabla \cdot (y,-x,0) = 0.
$$

This is not a special case. For any vector field $\mathbf{A}$,

$$
\nabla \cdot (\nabla \times \mathbf{A}) = 0.
$$

Curl therefore preserves source-free structure identically. It is the
differential form of source-free reorganization: continuous turning, with no
tearing and no start or end points introduced by the evolution itself.

The next question is whether one self-turning field is enough for stable
propagation.
