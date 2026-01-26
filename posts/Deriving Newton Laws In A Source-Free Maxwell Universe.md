---
title: Deriving Newton Laws In A Source-Free Maxwell Universe
subtitle: Newton laws from continuous energy flow
author: An M. Rodriguez, Alex Mercer
date: 2026-01-25
one-sentence-summary: In source-free Maxwell theory, local continuity identities imply global conservation of energy, momentum, and angular momentum; when energy is localized into a stable circulating knot, its integrated motion obeys Newton-like laws without postulating particles or forces.
summary: We derive, step by step, the conservation of energy, momentum, and angular momentum from source-free Maxwell theory, emphasizing that the basic “continuity equation” is the local statement underlying all of them. Using the Poynting theorem and the Maxwell stress tensor, we obtain local conservation laws, then integrate them to obtain global invariants. We then define a self-sustaining electromagnetic knot as a localized, persistent region of field energy and momentum, and show that its center-of-energy motion and momentum exchange obey Newton-like statements (inertia, action–reaction, and net-force laws) as consequences of flux balance—not as postulates.
keywords: Maxwell theory, source-free electromagnetism, continuity equation, Poynting theorem, Maxwell stress tensor, momentum conservation, angular momentum conservation, emergent inertia, field ontology
---

## Motivation

We want a document that does not assume:

- particles,
- mechanical “forces” as primitives,
- Newton’s laws as axioms.

We assume only:

- source-free Maxwell dynamics

We show that what looks like “Newtonian mechanics” for a localized object is the
integrated bookkeeping of field continuity.


## Assumptions and definitions

### Source-free Maxwell equations

In a source-free region:

$$
\nabla \cdot \mathbf{E} = 0,
\qquad
\nabla \cdot \mathbf{B} = 0,
$$

$$
\nabla \times \mathbf{E} = -\partial_t \mathbf{B},
\qquad
\nabla \times \mathbf{B} = \mu_0\epsilon_0\,\partial_t \mathbf{E}.
$$

From this system we can derive a wave equation for the electromagnetic fields.
Taking the curl of Faraday’s law and substituting the curl equation for
$\mathbf{B}$ yields

$$
\nabla^2\mathbf{E}-\mu_0\epsilon_0\,\partial_t^2\mathbf{E}=0.
$$

An identical equation follows for $\mathbf{B}$.

From the coefficient of the time-derivative term, we identify the wave
propagation speed:

$$
c=\frac{1}{\sqrt{\mu_0\epsilon_0}}.
$$


### Electromagnetic energy density and energy flux

$$
u = \frac{\epsilon_0}{2}\mathbf{E}^2 + \frac{1}{2\mu_0}\mathbf{B}^2,
\qquad
\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}.
$$


### Electromagnetic momentum density

$$
\mathbf{g} = \frac{\mathbf{S}}{c^2} = \epsilon_0\,\mathbf{E}\times\mathbf{B}.
$$


### Maxwell stress tensor

Define the stress tensor (one standard convention):

$$
T_{ij}
=
\epsilon_0\left(E_iE_j - \frac{1}{2}\delta_{ij}\mathbf{E}^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j - \frac{1}{2}\delta_{ij}\mathbf{B}^2\right).
$$

This tensor is the local momentum-flux bookkeeping of the field.


## Part I — Energy continuity is exact

### Poynting theorem

Start from:

$$
\nabla \times \mathbf{E} = -\partial_t \mathbf{B},
\qquad
\nabla \times \mathbf{B} = \mu_0\epsilon_0\,\partial_t \mathbf{E}.
$$

Use the identity:

$$
\nabla\cdot(\mathbf{E}\times\mathbf{B})
=
\mathbf{B}\cdot(\nabla\times\mathbf{E})
-
\mathbf{E}\cdot(\nabla\times\mathbf{B}).
$$

Substitute Maxwell:

$$
\nabla\cdot(\mathbf{E}\times\mathbf{B})
=
\mathbf{B}\cdot(-\partial_t\mathbf{B})
-
\mathbf{E}\cdot(\mu_0\epsilon_0\,\partial_t\mathbf{E}).
$$

Rewrite as time derivatives:

$$
\mathbf{B}\cdot\partial_t\mathbf{B}
=
\frac{1}{2}\partial_t(\mathbf{B}^2),
\qquad
\mathbf{E}\cdot\partial_t\mathbf{E}
=
\frac{1}{2}\partial_t(\mathbf{E}^2).
$$

So:

$$
\nabla\cdot(\mathbf{E}\times\mathbf{B})
=
-\frac{1}{2}\partial_t(\mathbf{B}^2)
-\frac{\mu_0\epsilon_0}{2}\partial_t(\mathbf{E}^2).
$$

Multiply by $1/\mu_0$:

$$
\nabla\cdot\mathbf{S}
=
-\partial_t\left(\frac{1}{2\mu_0}\mathbf{B}^2 + \frac{\epsilon_0}{2}\mathbf{E}^2\right)
=
-\partial_t u.
$$

Therefore:

$$
\partial_t u + \nabla\cdot\mathbf{S} = 0.
$$

This is local energy continuity.


### Global energy conservation

Integrate over a fixed volume $V$ with boundary $\partial V$:

$$
\frac{d}{dt}\int_V u\,d^3x + \int_V \nabla\cdot\mathbf{S}\,d^3x = 0.
$$

Use the divergence theorem:

$$
\int_V \nabla\cdot\mathbf{S}\,d^3x = \int_{\partial V}\mathbf{S}\cdot d\mathbf{A}.
$$

So:

$$
\frac{d}{dt}U_V = -\Phi_V,
$$

where:

$$
U_V = \int_V u\,d^3x,
\qquad
\Phi_V = \int_{\partial V}\mathbf{S}\cdot d\mathbf{A}.
$$

Energy inside $V$ changes only by flux through its boundary. If
$\Phi_V=0$, then $U_V$ is constant.


## Part II — Momentum continuity is exact

Energy continuity does not yet control motion. We also need momentum continuity,
derived from the same source-free Maxwell system.


### Local momentum continuity

Start from:

$$
\mathbf{g}=\epsilon_0\,\mathbf{E}\times\mathbf{B}.
$$

Differentiate:

$$
\partial_t\mathbf{g}
=
\epsilon_0\left(
\partial_t\mathbf{E}\times\mathbf{B}
+
\mathbf{E}\times\partial_t\mathbf{B}
\right).
$$

Substitute:

$$
\partial_t\mathbf{E}=\frac{1}{\mu_0\epsilon_0}\nabla\times\mathbf{B},
\qquad
\partial_t\mathbf{B}=-\nabla\times\mathbf{E}.
$$

Then:

$$
\partial_t\mathbf{g}
=
\frac{1}{\mu_0}(\nabla\times\mathbf{B})\times\mathbf{B}
-
\epsilon_0\,\mathbf{E}\times(\nabla\times\mathbf{E}).
$$

Use the identity:

$$
(\nabla\times\mathbf{A})\times\mathbf{A}
=
(\mathbf{A}\cdot\nabla)\mathbf{A}
-
\frac{1}{2}\nabla(\mathbf{A}^2)
+
\mathbf{A}(\nabla\cdot\mathbf{A}),
$$

and apply it to $\mathbf{E}$ and $\mathbf{B}$. Since
$\nabla\cdot\mathbf{E}=0$ and $\nabla\cdot\mathbf{B}=0$, this becomes:

$$
(\nabla\times\mathbf{A})\times\mathbf{A}
=
(\mathbf{A}\cdot\nabla)\mathbf{A}
-
\frac{1}{2}\nabla(\mathbf{A}^2).
$$

Thus:

$$
\partial_t\mathbf{g}
=
\frac{1}{\mu_0}\left((\mathbf{B}\cdot\nabla)\mathbf{B}-\frac{1}{2}\nabla(\mathbf{B}^2)\right)
-
\epsilon_0\left((\mathbf{E}\cdot\nabla)\mathbf{E}-\frac{1}{2}\nabla(\mathbf{E}^2)\right).
$$

Write components and regroup into a divergence. Using
$\partial_j(B_iB_j)=(\mathbf{B}\cdot\nabla)B_i$ and
$\partial_j(E_iE_j)=(\mathbf{E}\cdot\nabla)E_i$ (again by zero divergence), we
obtain:

$$
\partial_t g_i
=
-\partial_j\left[
\epsilon_0\left(E_iE_j-\frac{1}{2}\delta_{ij}\mathbf{E}^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j-\frac{1}{2}\delta_{ij}\mathbf{B}^2\right)
\right].
$$

Identify the bracketed term as $T_{ij}$. Then:

$$
\partial_t g_i + \partial_j T_{ij} = 0,
$$

or:

$$
\partial_t\mathbf{g}+\nabla\cdot\mathbf{T}=0.
$$

This is the exact local momentum continuity equation in a source-free region.


### Global momentum conservation

Integrate over $V$:

$$
\frac{d}{dt}\int_V g_i\,d^3x + \int_V \partial_jT_{ij}\,d^3x = 0.
$$

Apply the divergence theorem:

$$
\int_V \partial_jT_{ij}\,d^3x = \int_{\partial V}T_{ij}n_j\,dA.
$$

Define:

$$
P_i(V) = \int_V g_i\,d^3x,
\qquad
F_i^{(\text{boundary})}(V) = \int_{\partial V}T_{ij}n_j\,dA.
$$

Then:

$$
\frac{d}{dt}P_i(V) = -F_i^{(\text{boundary})}(V).
$$

This is a pure flux statement: momentum inside changes only by momentum crossing
the boundary. If the boundary flux vanishes, $P_i(V)$ is constant.


## Part III — Angular momentum continuity is exact

### Angular momentum density and flux

Define:

$$
\boldsymbol{\ell} = \mathbf{x}\times\mathbf{g}.
$$

Using momentum continuity, one obtains an angular momentum continuity equation
of the form:

$$
\partial_t \ell_i + \partial_j M_{ij} = 0,
$$

for an appropriate flux tensor $M_{ij}$ built from $T_{ij}$.

Integrated form:

$$
\frac{d}{dt}\mathbf{L}(V)
=
-\int_{\partial V}(\mathbf{x}\times(\mathbf{T}\cdot\mathbf{n}))\,dA,
$$

where:

$$
\mathbf{L}(V)=\int_V \mathbf{x}\times\mathbf{g}\,d^3x.
$$

Angular momentum changes only by torque flux through the boundary.


## Part IV — Newton-like laws for a localized electromagnetic knot

Now we define what we mean by “object” without particles.


### A localized, persistent energy region

Let $K(t)$ be a moving region in space such that:
- most of the energy is concentrated inside it,
- its boundary is chosen so that flux across it is negligible compared to
  internal circulation,
- it persists over times long compared to its internal circulation timescale.

Define its total energy and momentum:

$$
E_K = \int_{K(t)} u\,d^3x,
\qquad
\mathbf{P}_K = \int_{K(t)} \mathbf{g}\,d^3x.
$$

If boundary fluxes are negligible, then $E_K$ and $\mathbf{P}_K$
are approximately conserved. This is “self-sustaining knot” in operational
terms.


### Center of energy

Define:

$$
\mathbf{X}_K = \frac{1}{E_K}\int_{K(t)} \mathbf{x}\,u\,d^3x.
$$

Differentiate in time using energy continuity (with boundary terms tracked):

$$
\frac{d}{dt}\left(\int_{K} \mathbf{x}\,u\,d^3x\right)
=
\int_{K}\mathbf{S}\,d^3x
\;+\;\text{boundary terms}.
$$

When boundary terms are negligible:

$$
E_K\,\dot{\mathbf{X}}_K \approx \int_{K}\mathbf{S}\,d^3x.
$$

Using $\mathbf{g}=\mathbf{S}/c^2$:

$$
\mathbf{P}_K \approx \frac{E_K}{c^2}\,\dot{\mathbf{X}}_K.
$$

Define the emergent inertial mass:

$$
m_K := \frac{E_K}{c^2}.
$$


### Inertia

If the knot is isolated so that boundary momentum flux vanishes:

$$
\frac{d}{dt}\mathbf{P}_K = 0.
$$

If additionally $E_K$ is constant, then $\dot{\mathbf{X}}_K$ is
constant. An isolated knot moves at constant center-of-energy velocity.


### Net-force law as boundary stress balance

Integrate momentum continuity over $K$:

$$
\frac{d}{dt}\mathbf{P}_K
=
-\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

Define the effective force as net momentum flux across the boundary:

$$
\mathbf{F}_K := -\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

Then:

$$
\frac{d}{dt}\mathbf{P}_K = \mathbf{F}_K.
$$

With $\mathbf{P}_K \approx m_K\dot{\mathbf{X}}_K$ (when $E_K$ is
roughly constant):

$$
m_K\,\ddot{\mathbf{X}}_K \approx \mathbf{F}_K.
$$


### Action–reaction as internal flux cancellation

Consider two disjoint localized regions $K_1$ and $K_2$
whose union lies in a larger region $V$ with no net boundary flux:

$$
\int_{\partial V}\mathbf{T}\cdot\mathbf{n}\,dA = 0.
$$

Then total momentum in $V$ is constant:

$$
\frac{d}{dt}(\mathbf{P}_{K_1} + \mathbf{P}_{K_2} + \mathbf{P}_{\text{outside}}) = 0.
$$

With the outside contribution negligible or included in the partition, momentum
lost by one region is gained by the other. Equal-and-opposite “forces” are the
same internal stress flux counted on two sides of the same interface.


## Scope

### Derived from source-free Maxwell structure

- local energy continuity: $$\partial_t u + \nabla\cdot\mathbf{S}=0$$
- local momentum continuity: $$\partial_t \mathbf{g} + \nabla\cdot\mathbf{T}=0$$
- angular momentum continuity in flux form
- global conservation laws as boundary-flux statements
- Newton-like motion of localized knots as integrated flux balances


### Not claimed here

- that a knot must exist for all initial data,
- that Maxwell alone guarantees stability of knots,
- that discrete spectra follow from this document alone.

These are separate questions.


## Closing statement

In a source-free Maxwell universe, conservation laws are not extra axioms. They
are continuity statements.

When electromagnetic energy organizes into a localized, persistent knot, its
large-scale motion is governed by the same bookkeeping: momentum changes only by
stress flux, and isolated knots therefore move inertially.

Newtonian mechanics appears as the boundary accounting of continuous field
transport.
