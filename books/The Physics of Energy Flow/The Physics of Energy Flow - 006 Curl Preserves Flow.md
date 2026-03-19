---
title: The Physics of Energy Flow – Curl Preserves Flow
date: 2026-03-11
---

# 6. Curl Preserves Flow

Recall the continuous energy flow field, $\mathbf{F}(\mathbf{r})$, whose
ordered bookkeeping between registrations was written in earlier chapters as
$\mathbf{S}(\mathbf{r};1,2)$.

To preserve the source-free character of the transport seen in experiments,
local evolution must allow the flow of energy without introducing primitive
endpoints. We therefore ask what kinds of local update can reorganize
$\mathbf{F}$ while maintaining its source-free nature.

To express more precisely the idea of accounting for flow across a boundary,
take any region $V$ with closed boundary $\partial V$. Gauss's
theorem gives

$$
\int_V \nabla \cdot (\Delta \mathbf{F})\,dV
=
\oint_{\partial V} \Delta \mathbf{F} \cdot d\mathbf{A}.
$$

This says that divergence measures the net transport across a closed boundary.
In the source-free case, every such boundary must give zero net flow. No
separate charges, masses, sources, or sinks are inserted into the accounting:
there is only energy being transported. The divergence must therefore remain
identically zero.

A purely algebraic change, such as rescaling

$$
\mathbf{F} \mapsto \lambda \mathbf{F},
$$

can strengthen or weaken what is already there, but it does not explain how the
flow turns or reorganizes in space in more complex ways. Furthermore, it leaves
zeros where they are and adds no new spatial structure.

If the evolution of $\mathbf{F}$ is written as the gradient of some field
$\phi$,

$$
\Delta \mathbf{F} = \nabla \phi.
$$

then, taking the divergence $\nabla \cdot$,

$$
\nabla \cdot (\Delta \mathbf{F}) = \nabla^2 \phi,
$$

which is generally nonzero.

Such an update can compress, expand, begin, or end the transport. It does not
preserve source-free reorganization.

What does preserve the source-free condition identically is a rotation.

For any vector field $\mathbf{A}$, we can express source-free evolution of
$\mathbf{F}$ as

$$
\Delta \mathbf{F} = \nabla \times \mathbf{A}
\qquad\Longrightarrow\qquad
\nabla \cdot (\Delta \mathbf{F}) = 0.
$$

To make this explicit, in three dimensions, write

$$
\mathbf{A} = (A_x,A_y,A_z).
$$

Then, by definition,

$$
\nabla \times \mathbf{A}
=
(
\partial_y A_z - \partial_z A_y,\;
\partial_z A_x - \partial_x A_z,\;
\partial_x A_y - \partial_y A_x
),
$$

and therefore

$$
\nabla \cdot (\Delta \mathbf{F})
=
\partial_x\partial_y A_z - \partial_x\partial_z A_y
+ \partial_y\partial_z A_x - \partial_y\partial_x A_z
+ \partial_z\partial_x A_y - \partial_z\partial_y A_x
= 0.
$$

The mixed derivatives cancel pairwise. That is why curl preserves the
source-free condition identically.

Curl therefore preserves source-free structure identically. It is the
differential form of source-free reorganization: continuous turning, with no
tearing and no start or end points introduced by the evolution itself.
