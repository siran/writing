---
title: The Physics of Energy Flow - Double Curl Closure and the Wave Equation
date: 2026-03-18
---


# 7. Double Curl Closure and the Wave Equation

Chapter 6 established that source-free energy flow must reorganize by curl if
it is to preserve its divergence-free structure. That identifies the admissible
local turn. The next question is what closed transport law follows from that
fact.

A single curl gives one local reorganization of the flow. To describe
transport, the update must close on the same flow through ordered
registrations. The minimal closure is therefore a second curl acting back on
the same field. Write

$$
\partial_t^2 \mathbf{F}
=
-c^2\,\nabla \times (\nabla \times \mathbf{F}),
\qquad
\nabla\cdot\mathbf{F}=0,
$$

with $c$ the propagation speed fixed by the closure.

Use the standard vector identity

$$
\nabla \times (\nabla \times \mathbf{F})
=
\nabla(\nabla\cdot\mathbf{F})-\nabla^2\mathbf{F}.
$$

In the source-free case,

$$
\nabla \cdot \mathbf{F} = 0,
$$

so the first term vanishes and we obtain

$$
\nabla \times (\nabla \times \mathbf{F}) = -\nabla^2 \mathbf{F}.
$$

Substituting this into the transport law gives

$$
\partial_t^2 \mathbf{F}
=
c^2\nabla^2 \mathbf{F}.
$$

So the transporting flow itself satisfies the vector wave equation

$$
\partial_t^2 \mathbf F-c^2\nabla^2\mathbf F=0,
\qquad
\nabla\cdot\mathbf F=0.
$$

The derivation is now explicit. Chapter 6 identified curl as the differential
form of source-free reorganization. Applying that rotational update twice gives
the minimal closed transport law for the same flow. In the source-free case,
double curl reduces to the Laplacian, and the wave equation follows directly.

Like every field relation in this book, this law is posed simultaneously for
all $\mathbf{r}$ in the extent. It does not track one tagged parcel of energy
through a pre-given background. It constrains how the whole organized flow can
reconfigure while remaining one continuous transport.

This wave equation does not yet impose a particular global closure. It permits
propagating organization in open space and standing organization on a closed
support. The next chapter uses exactly this point: once the same flow is
required to close on itself, only certain standing organizations remain
allowed.

Later, when one wants the conventional electromagnetic writing, the same
transport can be expressed in the familiar variables $\mathbf E$ and
$\mathbf B$, with energy flux written in Maxwell form as

$$
\mathbf{S}=\frac{1}{\mu_0}\,\mathbf{E}\times\mathbf{B}.
$$

That later resolution does not change the point established here. The
transporting object is the one source-free flow $\mathbf F$, and its local law
is the wave equation just derived.
