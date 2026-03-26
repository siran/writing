---
title: The Physics of Energy Flow - Double Curl Closure and the Wave Equation
date: 2026-03-18
---


# 7. Double Curl Closure and the Wave Equation

Chapter 6 established that source-free energy flow must reorganize by curl if
it is to preserve its divergence-free structure. That identifies the admissible
local turn. The next question is what closed transport form follows from that
fact.

A single curl gives one local reorganization of the flow. But the flow is
present at every point, so the closure must remain within that same field
throughout the extent. The minimal closure is therefore a second curl of the
same field. Write

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

Substituting this into the expression above gives

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
form of source-free reorganization. Here energy is flowing at every point, and
that same field appears under curl twice. The identity

$$
\nabla \times (\nabla \times \mathbf{F})
=
\nabla(\nabla\cdot\mathbf{F})-\nabla^2\mathbf{F}
$$

together with

$$
\nabla\cdot\mathbf{F}=0
$$

leaves

$$
\nabla \times (\nabla \times \mathbf{F}) = -\nabla^2 \mathbf{F},
$$

so

$$
\partial_t^2 \mathbf{F}
=
-c^2\,\nabla \times (\nabla \times \mathbf{F})
=
c^2\nabla^2 \mathbf{F}.
$$

That is the wave equation just written.

Like every field relation in this book, this equation is posed simultaneously for
all $\mathbf{r}$ in the extent. It does not track one tagged parcel of energy
through a pre-given background. It constrains how the whole organized flow can
reconfigure while remaining one continuous transport.

This wave equation does not yet impose a particular global closure. It permits
propagating organization in open space and standing organization on a closed
support. The next chapter resolves this one transporting flow into two
complementary aspects, written later in the familiar variables
$\mathbf E$ and $\mathbf B$. The chapter after that derives the
self-refraction principle by which those two aspects bend the transport of the
same field. Only after that does the book ask what standing organizations
remain once that self-bending becomes strong enough to produce closure.

That later two-aspect resolution does not change the point established here.
The transporting object is still the one source-free flow $\mathbf F$, and its
local form is the wave equation just derived.
