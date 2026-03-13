---
title: The Physics of Energy Flow – Curl Preserves Flow
date: 2026-03-11
---


# 6. Curl Preserves Flow

To preserve the source-free character of transport, the local evolution law
must turn a flow without introducing primitive endpoints. Curl does this
identically.

Not every local update has that property. If the change were described by a
gradient field,

$$
\partial \mathbf{S} = \nabla \phi,
$$

then its divergence would be

$$
\nabla \cdot (\partial \mathbf{S}) = \nabla^2 \phi,
$$

which is generally nonzero. Such an update can compress, expand, begin, or end
the transport. It does not preserve a source-free structure.

For any vector field $\mathbf{A}$,

$$
\nabla \cdot (\nabla \times \mathbf{A}) = 0.
$$

This is an identity, not a special case. It does not depend on whether
$\mathbf{A}$ is linear or nonlinear. Curl turns a flow without creating
endpoints.

Curl is therefore the differential form of source-free reorganization:
continuous turning, with no tearing and no start or end points introduced by
the evolution itself. The next question is whether one self-turning field is
enough for stable propagation.
