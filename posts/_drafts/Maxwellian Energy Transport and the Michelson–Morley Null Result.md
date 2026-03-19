---
title: Maxwellian Energy Transport and the Michelson–Morley Null Result
subtitle: A First-Principles Derivation from Source-Free Maxwell Theory
author: —
date: —
---

# Maxwellian Energy Transport and the Michelson–Morley Null Result

## 0. Objective

We construct, from first principles, a logically complete derivation of:

1. The invariant propagation rate $c$ from source-free Maxwell
   theory.
2. The unique inertial coordinate transformations preserving Maxwellian
   propagation.
3. The induced hyperbolic velocity-composition law.
4. The correct computation of Michelson–Morley interferometer timing.
5. The null result as a direct consequence of Maxwell-consistent transport.


No geometric assumptions (length contraction, spacetime curvature, etc.) are
introduced. All results follow from the structure of Maxwell’s equations.

---


# Part I — Maxwell Theory Fixes a Universal Propagation Rate

## 1. Source-Free Maxwell Equations

In vacuum,

$$
\nabla \cdot \mathbf{E} = 0, \qquad
\nabla \cdot \mathbf{B} = 0,
$$

$$
\nabla \times \mathbf{E} = -\partial_t \mathbf{B}, \qquad
\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \, \partial_t \mathbf{E}.
$$

---


## 2. Derivation of the Wave Equation

Take the curl of Faraday’s law:

$$
\nabla \times (\nabla \times \mathbf{E})
= -\partial_t (\nabla \times \mathbf{B}).
$$

Using

$$
\nabla \times (\nabla \times \mathbf{E})
= \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E},
$$

and $\nabla \cdot \mathbf{E} = 0$:

$$
-\nabla^2 \mathbf{E}
= -\mu_0 \epsilon_0 \, \partial_t^2 \mathbf{E}.
$$

Thus:

$$
\partial_t^2 \mathbf{E} = c^2 \nabla^2 \mathbf{E},
\qquad
c := \frac{1}{\sqrt{\mu_0 \epsilon_0}}.
$$

Similarly,

$$
\partial_t^2 \mathbf{B} = c^2 \nabla^2 \mathbf{B}.
$$

---


## 3. The Maxwell Wave Operator

Define

$$
\square_c := \partial_t^2 - c^2 \nabla^2.
$$

Each field component satisfies

$$
\square_c \Phi = 0.
$$

Therefore:

- Maxwell theory fixes a universal transport rate $c$.
- Electromagnetic disturbances propagate along the characteristic structure
  defined by $\square_c$.
- $c$ is not an adjustable parameter; it is fixed by field
  dynamics.


---


# Part II — Inertial Re-Description and Operator Invariance

## 4. Minimal Invariance Requirement

Let $(t,\mathbf{x})$ and $(t',\mathbf{x}')$ be inertial coordinate systems.

Maxwell invariance requires:

$$
\square_c \Phi = 0
\quad \Longleftrightarrow \quad
\square_c' \Phi = 0.
$$

That is,

$$
\partial_t^2 - c^2 \nabla^2
\quad \text{and} \quad
\partial_{t'}^2 - c^2 \nabla'^2
$$

must represent the same operator up to scale.

This ensures that the propagation rate $c$ is not
coordinate-dependent.

---


## 5. Linear Structure of Inertial Transformations

Homogeneity and inertiality imply linear transformations.

Restrict first to motion along $x$:

$$
x' = a x + b t, \qquad
t' = d x + e t.
$$

Wave-operator invariance forces:

$$
x' = \gamma(x - v t),
$$

$$
t' = \gamma\left(t - \frac{v}{c^2} x \right),
$$

where

$$
\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}.
$$

This is uniquely determined by preserving $\square_c$.

No geometric assumptions were introduced.

---


# Part III — Velocity Composition from Maxwell Invariance

## 6. 1D Velocity Composition

Let $u = dx/dt$.

Differentiate:

$$
dx' = \gamma(dx - v dt),
$$

$$
dt' = \gamma\left(dt - \frac{v}{c^2} dx\right).
$$

Thus:

$$
u' = \frac{dx'}{dt'}
= \frac{u - v}{1 - \frac{uv}{c^2}}.
$$

This is hyperbolic composition.

---


## 7. 3D Velocity Composition

Decompose:

$$
\mathbf{u} = \mathbf{u}_\parallel + \mathbf{u}_\perp,
$$

with respect to $\mathbf{v}$.

Then:

$$
\mathbf{u}'
=
\frac{\mathbf{u}_\perp/\gamma + \mathbf{u}_\parallel - \mathbf{v}}
{1 - \frac{\mathbf{v} \cdot \mathbf{u}}{c^2}}.
$$

---


## 8. Critical Identity

If $|\mathbf{u}| = c$, then:

$$
|\mathbf{u}'| = c.
$$

Therefore:

Electromagnetic transport speed is invariant under inertial re-description.

This directly contradicts Galilean addition:

$$
u_{\text{Galilean}} = u \pm v.
$$

Galilean addition does not preserve $c$. Maxwell transport forbids
it.

---


# Part IV — The Logical Error in the Textbook Michelson–Morley Derivation

## 9. The Classical Assumption

Textbook reasoning assumes:

$$
c_{\text{effective}} = c \pm v.
$$

This presumes:

- Light behaves as a projectile.
- Velocities add algebraically.
- The apparatus moves through a medium.


But Maxwell theory already forbids additive composition.

Thus the $c \pm v$ assumption contradicts the field equations.

---


# Part V — Maxwell-Consistent Interferometer Timing

Let:

- $L$ be arm length in the laboratory,
- $v$ lab speed relative to hypothetical medium,
- $c$ Maxwell transport rate.


The interferometer measures:

$$
\Delta T = T_\parallel - T_\perp.
$$

---


## 10. Transport Principle

Electromagnetic disturbances propagate at invariant rate $c$.

Therefore:

- The signal transport rate is $c$ in all inertial descriptions.
- Timing must be computed from invariant propagation, not $c \pm v$.


---


## 11. Parallel Arm

Distance to mirror (lab frame):

$$
L.
$$

Transport rate:

$$
c.
$$

Outbound time:

$$
T_{\text{out}} = \frac{L}{c}.
$$

Return time:

$$
T_{\text{back}} = \frac{L}{c}.
$$

Thus:

$$
T_\parallel = \frac{2L}{c}.
$$

---


## 12. Perpendicular Arm

Same reasoning:

$$
T_\perp = \frac{2L}{c}.
$$

---


# Part VI — Null Result

Therefore:

$$
\Delta T = T_\parallel - T_\perp = 0.
$$

The Michelson–Morley null result follows directly from:

- Maxwell’s wave equation,
- invariance of the wave operator,
- hyperbolic velocity composition,
- invariance of $c$.


No length contraction was assumed. No geometric deformation was required.

---


# Part VII — Logical Structure of the Argument

1. Maxwell theory fixes a finite propagation rate $c$.
2. Inertial re-description must preserve the Maxwell operator.
3. This forces Lorentz-type transformations.
4. Differentiation yields hyperbolic velocity composition.
5. Hyperbolic composition preserves $c$.
6. Therefore light does not obey $c \pm v$.
7. The Michelson–Morley $c \pm v$ calculation is inconsistent with
   Maxwell.
8. Correct timing yields equal round-trip times.
9. The null result is expected.


---


# Final Statement

The Michelson–Morley experiment did not force length contraction.

It tested whether electromagnetic propagation obeys Galilean addition.

Maxwell theory predicts hyperbolic composition and invariant transport rate
$c$.

When timing is computed consistently with Maxwell transport,

$$
T_\parallel = T_\perp = \frac{2L}{c},
$$

and the null result follows as a direct mathematical consequence of the field
equations.
