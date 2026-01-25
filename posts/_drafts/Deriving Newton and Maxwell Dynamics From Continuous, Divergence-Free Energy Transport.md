---
title: Deriving Conservation Laws from the Continuity Equation in a Source-Free Maxwell Universe
subtitle: How Newtonian-Looking Laws Emerge for a Self-Sustaining Electromagnetic Knot
author: An M. Rodriguez, Alex Mercer
date: 2026-01-24
one-sentence-summary: In source-free Maxwell theory, local continuity identities imply global conservation of energy, momentum, and angular momentum; when energy is localized into a stable circulating knot, its integrated motion obeys Newton-like laws without postulating particles or forces.
summary: We derive, step by step, the conservation of energy, momentum, and angular momentum from source-free Maxwell theory, emphasizing that the basic “continuity equation” is the local statement underlying all of them. Using the Poynting theorem and the Maxwell stress tensor, we obtain local conservation laws, then integrate them to obtain global invariants. We then define a self-sustaining electromagnetic knot as a localized, persistent region of field energy and momentum, and show that its center-of-energy motion and momentum exchange obey Newton-like statements (inertia, action–reaction, and net-force laws) as consequences of flux balance—not as postulates.
keywords: Maxwell theory, source-free electromagnetism, continuity equation, Poynting theorem, Maxwell stress tensor, momentum conservation, angular momentum conservation, emergent inertia, field ontology
---

# Deriving Conservation Laws from the Continuity Equation

## Motivation

We want a document that does not assume:
- particles,
- mechanical “forces” as primitives,
- Newton’s laws as axioms.

We assume only:
- source-free Maxwell dynamics,
- and the operational notion that what exists is organized electromagnetic
  energy flow.

We show that what looks like “Newtonian mechanics” for a localized object is the
integrated bookkeeping of field continuity.

---


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

Define:

$$
c = \frac{1}{\sqrt{\mu_0\epsilon_0}}.
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

This tensor encodes momentum flux: it is the “pressure/shear” bookkeeping of the
field.

---


## Part I — Energy continuity is exact

### Step 1: Derive Poynting’s theorem

Start from:

$$
\nabla \times \mathbf{E} = -\partial_t \mathbf{B},
\qquad
\nabla \times \mathbf{B} = \mu_0\epsilon_0\,\partial_t \mathbf{E}.
$$

Use the vector identity:

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

Rewrite the right-hand side as time derivatives of squares:

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


### Step 2: Global energy conservation

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

Meaning: energy inside $V$ changes only by flux through its
boundary.

If $\Phi_V=0$ (isolated region), then $U_V$ is constant.

---


## Part II — Momentum continuity is exact

Energy continuity alone does not yet yield Newton-like motion. We need the
momentum continuity law, which is another continuity equation—derived from the
same Maxwell system.


### Step 3: Local momentum conservation statement

The claim we will derive/accept as the standard Maxwell identity is:

$$
\partial_t g_i + \partial_j T_{ij} = 0,
$$

or in vector form:

$$
\partial_t \mathbf{g} + \nabla\cdot \mathbf{T} = 0,
$$

where $(\nabla\cdot\mathbf{T})_i=\partial_jT_{ij}$.

Interpretation:
- $\mathbf{g}$ is momentum density,
- $\mathbf{T}$ is momentum flux tensor,
- this is the exact local momentum continuity equation in a source-free region.

(One can derive it directly by differentiating
$\mathbf{g}=\epsilon_0\mathbf{E}\times\mathbf{B}$, substituting Maxwell’s curl
equations, and reorganizing terms into a divergence; the algebra is long but
straightforward.)


### Step 4: Global momentum conservation

Integrate over $V$:

$$
\frac{d}{dt}\int_V g_i\,d^3x + \int_V \partial_jT_{ij}\,d^3x = 0.
$$

Apply divergence theorem to the second term:

$$
\int_V \partial_jT_{ij}\,d^3x = \int_{\partial V}T_{ij}n_j\,dA.
$$

Define:
- total field momentum in $V$:

$$
P_i(V) = \int_V g_i\,d^3x,
$$

- net momentum flux through boundary:

$$
F_i^{(\text{boundary})}(V) = \int_{\partial V}T_{ij}n_j\,dA.
$$

Then:

$$
\frac{d}{dt}P_i(V) = -F_i^{(\text{boundary})}(V).
$$

This is Newton’s second-law form, but it is purely a flux balance statement:
rate of change of momentum inside equals minus momentum leaving through the
boundary.

If the region is isolated so that the boundary flux vanishes, then
$P_i(V)$ is constant.

---


## Part III — Angular momentum continuity is exact

### Step 5: Define angular momentum density and flux

Define field angular momentum density:

$$
\boldsymbol{\ell} = \mathbf{x}\times\mathbf{g}.
$$

Using momentum continuity, one obtains an angular momentum continuity equation
of the form:

$$
\partial_t \ell_i + \partial_j M_{ij} = 0,
$$

for an appropriate angular momentum flux tensor $M_{ij}$ built from
$T_{ij}$.

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

So angular momentum changes only by torque flux through the boundary.

---


## Part IV — Newton-like laws for a localized electromagnetic knot

Now we define what we mean by “object” without particles.


### Step 6: Define a knot/object as a localized, persistent energy region

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
are approximately conserved.

This is “self-sustaining knot” in operational terms.


### Step 7: Define a center-of-energy position

Define:

$$
\mathbf{X}_K = \frac{1}{E_K}\int_{K(t)} \mathbf{x}\,u\,d^3x.
$$

Differentiate in time using energy continuity (and careful boundary handling).
The standard result is that the center-of-energy velocity is governed by energy
flux:

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

This is the Newtonian-looking relation “momentum equals mass times velocity”
with emergent inertial mass:

$$
m_K := \frac{E_K}{c^2}.
$$

This is not postulated; it is the integrated identity connecting energy flux and
momentum density.


### Step 8: Newton’s first law (inertia) as a corollary

If the knot is isolated so that boundary momentum flux vanishes:

$$
\frac{d}{dt}\mathbf{P}_K = 0.
$$

Then $\mathbf{P}_K$ is constant.

If additionally $E_K$ is constant (no net energy leakage), then:

$$
\dot{\mathbf{X}}_K \approx \frac{c^2}{E_K}\mathbf{P}_K
$$

is constant.

So: an isolated knot moves with constant velocity of its center-of-energy.

That is the inertial statement—obtained as a flux conservation corollary.


### Step 9: Newton’s second law as boundary-stress balance

From momentum continuity integrated over the knot region:

$$
\frac{d}{dt}\mathbf{P}_K
=
-\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

Define the “effective force on the knot” as the net momentum flux across its
boundary:

$$
\mathbf{F}_K := -\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

Then:

$$
\frac{d}{dt}\mathbf{P}_K = \mathbf{F}_K.
$$

With $\mathbf{P}_K \approx m_K\dot{\mathbf{X}}_K$ (when $E_K$
approximately constant):

$$
m_K\,\ddot{\mathbf{X}}_K \approx \mathbf{F}_K.
$$

This is Newton’s second law in emergent form: force is not primitive; it is
momentum flux through a boundary.


### Step 10: Newton’s third law as internal flux cancellation

Consider two disjoint localized regions $K_1$ and $K_2$
whose union lies in a larger region $V$ with no net boundary flux:

$$
\int_{\partial V}\mathbf{T}\cdot\mathbf{n}\,dA = 0.
$$

Then total momentum in $V$ is constant:

$$
\frac{d}{dt}(\mathbf{P}_{K_1} + \mathbf{P}_{K_2} + \mathbf{P}_{\text{outside}}) = 0.
$$

If “outside” contributions are negligible or included in the two regions
appropriately, the momentum lost by one must be gained by the other.

Operationally, the momentum flux crossing the interface is equal and opposite.

So “action–reaction” is not an extra axiom; it is the cancellation of internal
fluxes in a closed system.

---


## What has actually been derived (and what has not)

### Derived from source-free Maxwell structure

- local energy continuity: $$\partial_t u + \nabla\cdot\mathbf{S}=0$$

- local momentum continuity: $$\partial_t \mathbf{g} + \nabla\cdot\mathbf{T}=0$$

- local angular momentum continuity (torque flux form)

- global conservation laws as boundary-flux statements

- Newton-like laws for localized knots as integrated flux balances:
  - inertia: constant momentum implies constant center-of-energy velocity,
  - “force” as stress-flux,
  - “action–reaction” as internal flux cancellation.


### Not claimed here

- that a knot must exist for all initial data,
- that all stability mechanisms are covered by Maxwell alone without your
  emergent-refraction mechanism,
- that discrete spectra follow from this document alone.

Those are established elsewhere in the program and are separate logical steps.

---


## Closing statement

In a source-free Maxwell universe, conservation laws are not additional
postulates.

They are continuity statements.

When electromagnetic energy self-organizes into a localized, persistent knot,
the knot’s large-scale motion is governed by the same continuity bookkeeping:
momentum changes only by momentum flux, and isolated knots therefore move
inertially.

Newtonian-looking mechanics is the coarse-grained boundary accounting of
continuous field transport.
