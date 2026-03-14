---
title: The Physics of Energy Flow - Double Curl Transport Law
date: 2026-03-11
---


# 7. Double Curl Transport Law

Chapter 6 established that the fundamental flow $\mathbf{F}$ must evolve by
curl if it is to preserve its divergence-free structure. That still leaves a
narrower question: what is the simplest curl-based law that makes transport
possible?

A single self-curl law,

$$
\partial_t \mathbf{F} = k\,\nabla \times \mathbf{F},
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
degrees of freedom of the same flow. The same local point serves as the
fulcrum for both turns, but the turns occur in different transverse
orientations. That difference is what makes them complementary rather than
redundant. Call these two aspects

$$
\mathbf{F}_{+}, \qquad \mathbf{F}_{-}.
$$

The minimal first-order local law that realizes this double turning is

$$
\partial_t \mathbf{F}_{+} = k\,\nabla \times \mathbf{F}_{-}, \qquad
\partial_t \mathbf{F}_{-} = -k\,\nabla \times \mathbf{F}_{+},
$$

with

$$
\nabla\cdot\mathbf{F}_{+}=0,\qquad
\nabla\cdot\mathbf{F}_{-}=0.
$$

Now each aspect changes by the curl of the other. This is the minimal real
closed transport law: no sources, no action at a distance, no extra fields,
and no higher-order operators.

Transport becomes legible only after the flow is resolved into these
complementary aspects, because the law acts on the pair as a whole. If we
write one complete local state as

$$
C = (\mathbf{F}_{+},\mathbf{F}_{-}),
$$

then one application of the law maps one configuration $C_1$ into another
configuration $C_2$. Repeated application therefore generates an ordered chain
of configurations:

$$
(\mathbf{F}_{+},\mathbf{F}_{-})_1,\;
(\mathbf{F}_{+},\mathbf{F}_{-})_2,\;
(\mathbf{F}_{+},\mathbf{F}_{-})_3,\;\dots
$$

That order is abstracted from the mapping itself. Only afterward is it
conveniently labeled by a parameter and written in differential form. In that
later form, the double rotation yields the wave equation for each aspect, as
shown in Appendix 203. For the present argument, the essential point is
simpler: one rotation recirculates, while two complementary rotations
transport.

This is the simplest transport law built from two complementary closed turns.
In its local ideal form it gives plane-wave transport: the same organized
advance repeated from point to point, without yet requiring helical closure.
One may picture the transverse frame as precessing about the local axis of
advance, so that the forward projection remains nonzero while the transverse
orientation oscillates. Helical and toroidal forms are global closures of the
same local geometry.

Only at this stage, after choosing conventional scale factors and absorbing
them into the electromagnetic normalization, are the two aspects named

$$
\mathbf{E} \equiv k_{+}\,\mathbf{F}_{+}, \qquad
\mathbf{B} \equiv k_{-}\,\mathbf{F}_{-}.
$$

They are not two substances. They are two complementary aspects of the same
organized flow $\mathbf{F}$. Their cross relation fixes the local direction of
transport:

$$
\mathbf{E}\cdot\mathbf{B}=0,\qquad
\mathbf{E}\times\mathbf{B}\parallel\mathbf{S}.
$$

The scale choices are then absorbed into the usual constitutive constants
$\varepsilon_0$ and $\mu_0$, and the energy flow can be written in Maxwell
form:

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
