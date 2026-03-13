---
title: The Physics of Energy Flow - Maxwell is Minimal
date: 2026-03-11
---


# 7. Maxwell is Minimal

Chapter 6 established that the fundamental flow $\mathbf{F}$ must evolve by
curl if it is to preserve its divergence-free structure. That still leaves a
narrower question: what is the simplest curl-based law that makes transport
possible?

A single self-curl law,

$$
\partial_t \mathbf{F} = c\,\nabla \times \mathbf{F},
$$

preserves source-free turning. But one local rotation only recirculates the
flow. It turns the structure around itself, but it does not yet carry energy
from one region into another. Transport requires a second, complementary
rotation. A point rotated once circulates. Rotated twice in a complementary
way, it advances.

A second step cannot be a gradient, because chapter 6 already showed that a
gradient update generically introduces divergence. The next admissible
possibility is therefore a second source-free rotation:

$$
\nabla \times (\nabla \times \mathbf{F}).
$$

In the source-free case,

$$
\nabla \cdot \mathbf{F} = 0
\qquad\Longrightarrow\qquad
\nabla \times (\nabla \times \mathbf{F}) = -\nabla^2 \mathbf{F}.
$$

Locally, a transporting configuration of $\mathbf{F}$ can therefore be
expressed by an axis of advance together with two complementary transverse
degrees of freedom of the same flow. Call these two aspects

$$
\mathbf{F}_{\circlearrowleft}, \qquad \mathbf{F}_{\circlearrowright}.
$$

These are not yet new fields. They are a local way of expressing the two
complementary rotational freedoms of $\mathbf{F}$.

The minimal first-order local law that realizes this double turning is

$$
\partial_t \mathbf{F}_{\circlearrowleft} = c\,\nabla \times \mathbf{F}_{\circlearrowright}, \qquad
\partial_t \mathbf{F}_{\circlearrowright} = -c\,\nabla \times \mathbf{F}_{\circlearrowleft},
$$

with

$$
\nabla\cdot\mathbf{F}_{\circlearrowleft}=0,\qquad
\nabla\cdot\mathbf{F}_{\circlearrowright}=0.
$$

Now each aspect changes by the curl of the other. This is the minimal real
closed transport law: no sources, no action at a distance, no extra fields,
and no higher-order operators.

At this point the two complementary aspects are recognized, up to the usual
unit convention, as the fields later called

$$
\mathbf{E} \equiv \mathbf{F}_{\circlearrowleft}, \qquad
\mathbf{B} \equiv \mathbf{F}_{\circlearrowright}.
$$

The contrast with a single self-curl field can be checked directly:

$$
\partial_t \mathbf{F} = c\,\nabla \times \mathbf{F}.
$$

Take a transverse Fourier mode

$$
\mathbf{F}(\mathbf{r},t)=\mathbf{A}\,e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)},
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
complementary aspects of the same organized flow $\mathbf{F}$. Their cross
relation fixes the local direction of transport:

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

Maxwell theory appears here as the minimal two-aspect closure of source-free
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
remain two transverse aspects of the same organized flow $\mathbf{F}$, whose
cross relation determines the direction of transport.
