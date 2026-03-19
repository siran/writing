---
title: The Physics of Energy Flow - Double Curl Transport Closure
date: 2026-03-11
---


# 7. Double Curl Transport Closure

Chapter 6 established that the fundamental flow $\mathbf{F}$ must evolve by
curl if it is to preserve its divergence-free structure. That still leaves a
narrower question: what is the simplest curl-based closure that makes transport
possible?

A single self-curl relation,

$$
\partial_t \mathbf{F} = k\,\nabla \times \mathbf{F},
$$

preserves source-free turning. Appendix 203 proves the precise limitation:
single curl reorganizes locally, but it does not bodily carry a nontrivial
bounded closure from one region into another. Transport requires a second,
complementary rotation.

A second step cannot be a gradient, because chapter 6 already showed that a
gradient update generically introduces divergence. The next admissible
possibility is therefore a second source-free rotation:

$$
\nabla \times (\nabla \times \mathbf{F}).
$$

To see what this means, use the standard vector identity

$$
\nabla \times (\nabla \times \mathbf{F})
=
\nabla(\nabla\cdot\mathbf{F})-\nabla^2\mathbf{F}.
$$

So in the source-free case,

$$
\nabla \cdot \mathbf{F} = 0,
$$

the first term vanishes and we obtain

$$
\nabla \times (\nabla \times \mathbf{F}) = -\nabla^2 \mathbf{F}.
$$

So a double curl of a source-free flow reduces exactly to minus the spatial
Laplacian of the field. This is the step from which the wave equation for the
transporting aspects follows directly.

Locally, a transporting configuration of $\mathbf{F}$ can therefore be
expressed by an axis of advance together with two complementary transverse
degrees of freedom of the same flow. The same local point serves as the
fulcrum for both turns, but the turns occur in different transverse
orientations. That difference is what makes them complementary rather than
redundant. Call these two aspects

$$
\mathbf{F}_{+}, \qquad \mathbf{F}_{-}.
$$

The minimal first-order local relation that realizes this double turning is

$$
\partial_t \mathbf{F}_{+} = k\,\nabla \times \mathbf{F}_{-}, \qquad
\partial_t \mathbf{F}_{-} = -k\,\nabla \times \mathbf{F}_{+},
$$

with

$$
\nabla\cdot\mathbf{F}_{+}=0,\qquad
\nabla\cdot\mathbf{F}_{-}=0.
$$

Now differentiate one of the two equations in time and substitute the other:

$$
\partial_t^2 \mathbf{F}_{+}
=
k\,\nabla\times(\partial_t\mathbf{F}_{-})
=
-k^2\nabla\times(\nabla\times\mathbf{F}_{+}).
$$

Because $\nabla\cdot\mathbf{F}_{+}=0$, the curl-curl identity gives

$$
\partial_t^2 \mathbf{F}_{+}=k^2\nabla^2\mathbf{F}_{+}.
$$

Exactly the same step gives

$$
\partial_t^2 \mathbf{F}_{-}=k^2\nabla^2\mathbf{F}_{-}.
$$

So for either complementary aspect $\mathbf F\in\{\mathbf F_+,\mathbf F_-\}$,
the transport law already has the direct vector wave form

$$
\partial_t^2 \mathbf F-k^2\nabla^2\mathbf F=0,
\qquad
\nabla\cdot\mathbf F=0.
$$

Now each aspect changes by the curl of the other. This is the minimal real
closed transport relation: no primitive source terms, no action at a distance,
no extra fields, and no higher-order operators.

Like every field relation in this book, this coupled update is posed
simultaneously for all $\mathbf{r}$ in the extent. It does not describe the
path of one individually tagged point. It describes how the whole organized
flow reorganizes at once.

Transport becomes legible only after the flow is resolved into these
complementary aspects, because the coupled update acts on the pair as a whole.
If we
write one complete local state as

$$
C = (\mathbf{F}_{+},\mathbf{F}_{-}),
$$

then one application of the coupled update maps one configuration $C_1$ into another
configuration $C_2$. Repeated application therefore generates an ordered chain
of configurations:

$$
(\mathbf{F}_{+},\mathbf{F}_{-})_1,\;
(\mathbf{F}_{+},\mathbf{F}_{-})_2,\;
(\mathbf{F}_{+},\mathbf{F}_{-})_3,\;\dots
$$

That order is abstracted from the mapping itself. Only afterward is it
conveniently labeled by a parameter and written in differential form. The
wave equation already follows from the coupled closure just written. For the
present argument, the essential point is simpler: single curl reorganizes
locally; doubled curl transports.

This is the simplest transport closure built from two complementary closed
turns.
We will refer to it interchangeably as double-curl transport or Maxwellian
transport.

In its local ideal form it gives the plane-wave idealization of transport: the
same organized advance repeated from point to point, without yet requiring
helical closure. Such an idealization already picks out a local axis of
advance, but because it extends everywhere it does not yet describe a bounded
from-here-to-there transfer. One may picture the transverse frame as
precessing about that local axis, so that the forward projection remains
nonzero while the transverse orientation oscillates. Helical and toroidal
forms are global closures of the same local geometry.

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

The primary identification remains the one just made:

$$
\mathbf E \equiv k_+ \mathbf F_+,
\qquad
\mathbf B \equiv k_- \mathbf F_-.
$$

Appendix 218 only proves the converse representation statement: once a local
energy density $u>0$ and energy flux $\mathbf{S}$ are known, and once they
satisfy the transport bound

$$
|\mathbf{S}| \le c\,u,
$$

one can construct at least one pair $(\mathbf{E},\mathbf{B})$ reproducing
those same observables in Maxwell form. This does not replace the derivation
from $\mathbf F_+$ and $\mathbf F_-$. It shows only that the already-derived
two-aspect transport admits a local Maxwell representation in terms of the
observable pair $(u,\mathbf S)$. The reconstruction is not unique. The
remaining freedom is the local polarization or duality freedom of the
two-aspect transport.

Maxwell theory appears here as the minimal two-aspect closure of rotational
transport without primitive source terms. In this sense, Maxwellian transport
is precisely the double-curl transport closure written in conventional
electromagnetic normalization.

Minimal does not mean unique. It means the weakest local closure that actually
propagates source-free flow. Appendix 211 proves the corresponding uniqueness
statement in the exact class used here: real, local, homogeneous, isotropic,
first-order, purely differential, divergence-preserving two-field closures.

The vacuum Maxwell equations are symmetric under the duality rotation

$$
\mathbf{E} \to c\mathbf{B}, \qquad c\mathbf{B} \to -\mathbf{E}.
$$

This reflects the complementary status of the two fields within one transport
relation. The symmetry does not collapse
$\mathbf{E}$ and $\mathbf{B}$ into a single field, and it does not erase
their distinct roles in a given solution. In a propagating configuration they
remain two transverse aspects of the same organized flow $\mathbf{F}$, whose
cross relation determines the direction of transport.
