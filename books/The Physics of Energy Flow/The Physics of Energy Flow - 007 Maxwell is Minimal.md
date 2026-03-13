---
title: The Physics of Energy Flow - Maxwell is Minimal
date: 2026-03-11
---


# 7. Maxwell is Minimal

Chapter 6 established that source-free flow must evolve by curl if it is to
preserve its divergence-free structure. That still leaves a narrower question:
what is the simplest curl-based law that makes transport possible?

The first attempt is a single self-curl field:

$$
\partial_t \mathbf{Q} = c\,\nabla \times \mathbf{Q}.
$$

This preserves source-free turning identically. But preservation is not
enough. One field turning itself still recirculates locally. It does not yet
show how energy is carried from one region into another.

Take a transverse Fourier mode

$$
\mathbf{Q}(\mathbf{r},t)=\mathbf{A}\,e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)},
\qquad
\mathbf{k}\cdot\mathbf{A}=0.
$$

Substitution gives

$$
-i\omega\,\mathbf{A}=ic\,\mathbf{k}\times\mathbf{A}.
$$

On the transverse plane, $\mathbf{k}\times$ acts as a quarter-turn operator.
Its eigenvalues are $\pm i|\mathbf{k}|$. Therefore

$$
\omega = \pm i\,c|\mathbf{k}|.
$$

The modes grow or decay instead of remaining neutral. A single real curl field
turns, but it does not sustain transport.

To obtain transport, the turning must be complementary. One field must rotate
another:

$$
\partial_t \mathbf{E} = c\,\nabla \times \mathbf{B}, \qquad
\partial_t \mathbf{B} = -c\,\nabla \times \mathbf{E},
$$

with

$$
\nabla\cdot\mathbf{E}=0,\qquad \nabla\cdot\mathbf{B}=0.
$$

Now each field changes by the curl of the other.
This is the minimal real closed transport law: no sources, no action at a
distance, no extra fields, and no higher-order operators.

Apply $\partial_t$ once more. For $\mathbf{E}$,

$$
\partial_t^2\mathbf{E}
=
c\,\nabla\times(\partial_t\mathbf{B})
=
-c^2\,\nabla\times\nabla\times\mathbf{E}.
$$

Using

$$
\nabla\times\nabla\times\mathbf{E}
=
\nabla(\nabla\cdot\mathbf{E})-\nabla^2\mathbf{E},
$$

and $\nabla\cdot\mathbf{E}=0$, we obtain

$$
\partial_t^2\mathbf{E}=c^2\nabla^2\mathbf{E}.
$$

The same argument gives

$$
\partial_t^2\mathbf{B}=c^2\nabla^2\mathbf{B}.
$$

So the double rotation does more than preserve source-free turning. It carries
the transport forward, and in doing so it yields the wave equation:

$$
\omega^2=c^2|\mathbf{k}|^2.
$$

$\mathbf{E}$ and $\mathbf{B}$ are not two substances. They are two
complementary rotational aspects of one organized flow. Their cross relation
fixes the local direction of transport:

$$
\mathbf{E}\cdot\mathbf{B}=0,\qquad
\mathbf{E}\times\mathbf{B}\parallel\mathbf{S}.
$$

The two fields form a rotating transverse frame whose mutual twist advances the
flow. Locally the geometry is a double rotation. Globally the same motif
appears in helical and toroidal closure.

Only at this stage can the energy flow be written in Maxwell form:

$$
\mathbf{S}=\frac{1}{\mu_0}\,\mathbf{E}\times\mathbf{B}.
$$

Maxwell theory appears here as the minimal two-field closure of source-free
rotational transport.

Minimal does not mean unique. It means the weakest local closure that actually
propagates source-free flow.

The vacuum Maxwell equations are symmetric under the duality rotation

$$
\mathbf{E} \to c\mathbf{B}, \qquad c\mathbf{B} \to -\mathbf{E}.
$$

This reflects the complementary status of the two fields within one transport
law. The symmetry does not collapse
$\mathbf{E}$ and $\mathbf{B}$ into a single field, and it does not erase
their distinct roles in a given solution. In a propagating configuration they
remain two transverse aspects of one organized flow, whose cross relation
determines the direction of transport.
