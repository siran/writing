---
title: Deriving Newton's Laws And Schroedinger's Equation In A Source-Free Maxwell Universe
subtitle: Newton laws and Schroedinger's equation from continuous energy flow
author: An M. Rodriguez, Alex Mercer, Anes Palma, Elias Thorne
date: 2026-01-26
one-sentence-summary: In source-free Maxwell theory, the same local continuity structure yields (i) global conservation laws and Newton-like motion for localized energy knots, and (ii) the Schrödinger equation as the narrow-band envelope limit of a toroidal standing mode, with $m$ and $\hbar$ emerging from the fundamental mode.
summary: We start from source-free Maxwell equations and derive the wave equation, then derive exact local continuity laws for energy, momentum, and angular momentum using the Poynting theorem and the Maxwell stress tensor. Integrating these identities yields global conservation statements. When electromagnetic energy is localized into a persistent circulating knot, its center-of-energy motion obeys Newton-like inertia and momentum-balance relations as flux bookkeeping, not as postulates. We then study a self-confined toroidal standing mode and isolate its forward-time narrow-band envelope via an analytic-signal projection. Keeping derivative terms exactly gives an envelope equation with a controlled remainder of order $(\Delta\omega/\omega_{11})^2$; discarding only that bounded term yields the Schrödinger equation. In this construction, $m=E_{11}/c^2$ and $\hbar=E_{11}/\omega_{11}$ are geometric properties of the fundamental toroidal mode.
keywords: Maxwell theory, source-free electromagnetism, continuity equation, Poynting theorem, Maxwell stress tensor, momentum conservation, angular momentum conservation, electromagnetic knots, toroidal standing modes, analytic signal, narrow-band limit, emergent inertia, emergent Planck constant, emergent quantum mechanics
license: CC BY 4.0
---

## Motivation

We want a document that does not assume:

- particles,
- mechanical “forces” as primitives,
- Newton’s laws as axioms,
- quantum postulates as axioms.

We assume only:

- source-free Maxwell dynamics

We show that:
- Newton-like mechanics for a localized object is integrated continuity
  bookkeeping,
- Schrödinger dynamics is the narrow-band envelope limit of Maxwell waves on a
  toroidal mode.


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

From this system we derive wave propagation. Taking the curl of Faraday’s law
and substituting the curl equation for $\mathbf{B}$ yields

$$
\nabla^2\mathbf{E}-\mu_0\epsilon_0\,\partial_t^2\mathbf{E}=0.
$$

An identical equation follows for $\mathbf{B}$.

From the coefficient of the time-derivative term, the wave speed is

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

$$
T_{ij}
=
\epsilon_0\left(E_iE_j - \frac{1}{2}\delta_{ij}\mathbf{E}^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j - \frac{1}{2}\delta_{ij}\mathbf{B}^2\right).
$$

$T_{ij}$ is the local momentum-flux bookkeeping of the field.


## Part I — Energy continuity is exact

### Poynting theorem

Start from:

$$
\nabla \times \mathbf{E} = -\partial_t \mathbf{B},
\qquad
\nabla \times \mathbf{B} = \mu_0\epsilon_0\,\partial_t \mathbf{E}.
$$

Use:

$$
\nabla\cdot(\mathbf{E}\times\mathbf{B})
=
\mathbf{B}\cdot(\nabla\times\mathbf{E})
-
\mathbf{E}\cdot(\nabla\times\mathbf{B}).
$$

Substitute Maxwell and rewrite as derivatives:

$$
\nabla\cdot\mathbf{S}=-\partial_t u,
\qquad\Rightarrow\qquad
\partial_t u + \nabla\cdot\mathbf{S} = 0.
$$


### Global energy conservation

Integrate over a fixed volume $V$ with boundary $\partial V$:

$$
\frac{d}{dt}\int_V u\,d^3x + \int_{\partial V}\mathbf{S}\cdot d\mathbf{A}=0.
$$

Define:

$$
U_V=\int_V u\,d^3x,
\qquad
\Phi_V=\int_{\partial V}\mathbf{S}\cdot d\mathbf{A},
$$

so:

$$
\frac{d}{dt}U_V=-\Phi_V.
$$

If $\Phi_V=0$, then $U_V$ is constant.


## Part II — Momentum continuity is exact

### Local momentum continuity

Start from:

$$
\mathbf{g}=\epsilon_0\,\mathbf{E}\times\mathbf{B}.
$$

Differentiate and substitute Maxwell:

$$
\partial_t\mathbf{g}
=
\frac{1}{\mu_0}(\nabla\times\mathbf{B})\times\mathbf{B}
-
\epsilon_0\,\mathbf{E}\times(\nabla\times\mathbf{E}).
$$

Use:

$$
(\nabla\times\mathbf{A})\times\mathbf{A}
=
(\mathbf{A}\cdot\nabla)\mathbf{A}
-
\frac{1}{2}\nabla(\mathbf{A}^2)
+
\mathbf{A}(\nabla\cdot\mathbf{A}),
$$

and $\nabla\cdot\mathbf{E}=0$, $\nabla\cdot\mathbf{B}=0$, giving

$$
(\nabla\times\mathbf{A})\times\mathbf{A}
=
(\mathbf{A}\cdot\nabla)\mathbf{A}
-
\frac{1}{2}\nabla(\mathbf{A}^2).
$$

So:

$$
\partial_t\mathbf{g}
=
\frac{1}{\mu_0}\left((\mathbf{B}\cdot\nabla)\mathbf{B}-\frac{1}{2}\nabla(\mathbf{B}^2)\right)
-
\epsilon_0\left((\mathbf{E}\cdot\nabla)\mathbf{E}-\frac{1}{2}\nabla(\mathbf{E}^2)\right).
$$

In components, using $\partial_j(B_iB_j)=(\mathbf{B}\cdot\nabla)B_i$ and
$\partial_j(E_iE_j)=(\mathbf{E}\cdot\nabla)E_i$, this becomes:

$$
\partial_t g_i
=
-\partial_j\left[
\epsilon_0\left(E_iE_j-\frac{1}{2}\delta_{ij}\mathbf{E}^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j-\frac{1}{2}\delta_{ij}\mathbf{B}^2\right)
\right].
$$

With the definition of $T_{ij}$:

$$
\partial_t g_i + \partial_j T_{ij} = 0,
\qquad\text{equivalently}\qquad
\partial_t\mathbf{g}+\nabla\cdot\mathbf{T}=0.
$$


### Global momentum conservation

Integrate over $V$:

$$
\frac{d}{dt}\int_V g_i\,d^3x + \int_{\partial V}T_{ij}n_j\,dA=0.
$$

Define:

$$
P_i(V)=\int_V g_i\,d^3x,
\qquad
F_i^{(\text{boundary})}(V)=\int_{\partial V}T_{ij}n_j\,dA,
$$

so:

$$
\frac{d}{dt}P_i(V)=-F_i^{(\text{boundary})}(V).
$$


## Part III — Angular momentum continuity is exact

### Angular momentum density and flux

$$
\boldsymbol{\ell}=\mathbf{x}\times\mathbf{g},
\qquad
\mathbf{L}(V)=\int_V \mathbf{x}\times\mathbf{g}\,d^3x.
$$

Using momentum continuity, angular momentum changes only by torque flux:

$$
\frac{d}{dt}\mathbf{L}(V)
=
-\int_{\partial V}(\mathbf{x}\times(\mathbf{T}\cdot\mathbf{n}))\,dA.
$$


## Part IV — Newton-like laws for a localized electromagnetic knot

### Localized, persistent energy region

Let $K(t)$ be a moving region such that energy is concentrated inside
it and boundary flux is small.

$$
E_K = \int_{K(t)} u\,d^3x,
\qquad
\mathbf{P}_K = \int_{K(t)} \mathbf{g}\,d^3x.
$$


### Center of energy and emergent inertial mass

$$
\mathbf{X}_K = \frac{1}{E_K}\int_{K(t)} \mathbf{x}\,u\,d^3x.
$$

When boundary terms are negligible:

$$
E_K\,\dot{\mathbf{X}}_K \approx \int_K \mathbf{S}\,d^3x,
\qquad
\mathbf{P}_K \approx \frac{E_K}{c^2}\dot{\mathbf{X}}_K.
$$

Define:

$$
m_K:=\frac{E_K}{c^2}.
$$


### Momentum balance as the net-force law

$$
\frac{d}{dt}\mathbf{P}_K
=
-\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA
=:\mathbf{F}_K.
$$

If $E_K$ is roughly constant:

$$
m_K\,\ddot{\mathbf{X}}_K \approx \mathbf{F}_K.
$$


## Part V — Schrödinger dynamics as a narrow-band Maxwell envelope

### Maxwell wave equation for a field component

For any Cartesian component $F(\mathbf{r},t)$ of $\mathbf{E}$ or
$\mathbf{B}$:

$$
\left(\nabla^{2}-\frac{1}{c^{2}}\partial_t^{2}\right)F(\mathbf{r},t)=0.
$$


### Toroidal standing modes

Take a toroidal topology with radii $R$ and $r$.
Integer windings $(n_1,n_2)$ give

$$
k_1=\frac{n_1}{R},
\qquad
k_2=\frac{n_2}{r},
\qquad
k^{2}=k_1^{2}+k_2^{2},
\qquad
\omega_{n_1n_2}=ck.
$$

Define the fundamental mode $(1,1)$ with $(E_{11},\omega_{11})$ and

$$
\hbar=\frac{E_{11}}{\omega_{11}},
\qquad
m=\frac{E_{11}}{c^{2}}.
$$


### Forward-time spectral projection and envelope

Define the analytic (positive-frequency) signal:

$$
F^{(+)}(\mathbf{r},t)=\int_{0}^{\infty}\tilde F(\mathbf{r},\omega)\,e^{-i\omega t}\,d\omega.
$$

Extract the carrier at $\omega_{11}$:

$$
\psi(\mathbf{r},t)=e^{i\omega_{11}t}\,F^{(+)}(\mathbf{r},t).
$$


### Exact envelope equation and controlled remainder

Substitution into the wave equation yields:

$$
\nabla^{2}\psi-\frac{1}{c^{2}}\partial_t^{2}\psi
+\frac{2i\omega_{11}}{c^{2}}\partial_t\psi
+\frac{\omega_{11}^{2}}{c^{2}}\psi=0.
$$

Rearrange:

$$
i\partial_t\psi=-\frac{c^{2}}{2\omega_{11}}\nabla^{2}\psi
+\frac{1}{2\omega_{11}c^{2}}\partial_t^{2}\psi.
$$

If the envelope has RMS bandwidth $\Delta\omega$ with
$\epsilon=\Delta\omega/\omega_{11}\ll1$, then the last term is bounded by
$O(\epsilon^2)$ in norm.

Dropping only this controlled term gives:

$$
i\partial_t\psi=-\frac{c^{2}}{2\omega_{11}}\nabla^{2}\psi+O(\epsilon^{2}).
$$

Using $\hbar=E_{11}/\omega_{11}$ and $m=E_{11}/c^2$ turns the coefficient into
$\hbar/(2m)$, yielding:

$$
i\hbar\,\partial_t\psi=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi+O(\epsilon^{2}).
$$


## Scope

### Derived from source-free Maxwell structure

- energy continuity: $$\partial_t u + \nabla\cdot\mathbf{S}=0$$
- momentum continuity: $$\partial_t \mathbf{g} + \nabla\cdot\mathbf{T}=0$$
- angular momentum flux balance
- Newton-like motion of localized energy knots as integrated flux bookkeeping
- Schrödinger dynamics as a narrow-band envelope limit with controlled
  $O(\epsilon^2)$ remainder
- emergent $m$ and $\hbar$ from $(E_{11},\omega_{11})$


### Not claimed here

- existence and stability of knots for arbitrary initial data,
- uniqueness of the toroidal mode or its formation mechanism,
- full quantum measurement theory.

These are separate questions.


## Closing statement

In a source-free Maxwell universe, continuity laws are identities, not
postulates. When energy localizes into a persistent knot, its coarse motion
follows from flux balance and looks Newtonian. When a toroidal mode is
narrow-band, its envelope obeys Schrödinger dynamics up to a controlled
$O(\epsilon^2)$ correction.