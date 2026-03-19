---
title: A Pre-Wave, Pre-Lorentz, Flat-Space Explanation of the Michelson–Morley Null Result
subtitle: Curl-Based Energy Transport Versus Galilean Carriage
author: An M. Rodriguez, Alex Mercer
date: 2026-01-20
one-sentence-summary: The Michelson–Morley null result follows directly from divergence-free curl-based energy transport in flat space and does not require spacetime curvature or an ether.
summary: We derive the Michelson–Morley null result from first principles using only source-free Maxwell theory, the continuity equation, and divergence-free curl-based transport. We show explicitly that the classical ether prediction arises from imposing Galilean velocity addition on electromagnetic propagation. That assumption is incompatible with curl-based transport closure. The null result therefore selects curl-based transport over Galilean carriage, without invoking spacetime curvature, ether media, or geometric deformation of space itself.
keywords: Michelson–Morley, Maxwell theory, divergence-free flow, curl transport, Galilean addition, flat space, energy continuity
---

# A Pre-Wave, Pre-Lorentz, Flat-Space Explanation of the Michelson–Morley Null Result

## 1. Motivation

The Michelson–Morley experiment is historically interpreted as evidence against
an ether and in favor of relativistic kinematics.

We present a different derivation.

We assume:

- flat three-dimensional space,
- source-free Maxwell theory,
- local energy continuity,
- divergence-free curl-based transport.


We do **not** assume:

- spacetime curvature,
- geometric deformation of space,
- rods that contract by hypothesis,
- time dilation postulates.


We show that the null result follows because electromagnetic propagation is not
Galilean carriage of a signal through a background, but divergence-free
curl-based transport with intrinsic closure.

The experiment selects the correct transport law.


## 2. Source-free Maxwell structure

In vacuum:

$$
\nabla \cdot \mathbf{E} = 0,
\qquad
\nabla \cdot \mathbf{B} = 0,
$$

$$
\nabla \times \mathbf{E} = -\partial_t \mathbf{B},
\qquad
\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \,\partial_t \mathbf{E}.
$$

Define the electromagnetic energy density:

$$
u = \frac{\epsilon_0}{2} |\mathbf{E}|^2
  + \frac{1}{2\mu_0} |\mathbf{B}|^2,
$$

and the Poynting vector:

$$
\mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B}.
$$

From these equations follows the continuity relation:

$$
\partial_t u + \nabla \cdot \mathbf{S} = 0.
$$

This is local energy bookkeeping.

Define the local transport velocity:

$$
\mathbf{v} = \frac{\mathbf{S}}{u}.
$$

One proves directly from the field algebra:

$$
|\mathbf{S}| \le c u,
\qquad
c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}.
$$

Radiative configurations satisfy:

$$
|\mathbf{S}| = c u.
$$

Thus propagation at speed $c$ is not assumed. It is an algebraic
property of curl-based divergence-free transport.


## 3. What Galilean drift assumes

The classical ether prediction assumes:

- light travels at speed $c$ relative to the ether,
- the laboratory moves at velocity $\mathbf{V}$ through that ether,
- velocities add linearly.


Thus the effective signal velocity in the lab frame is:

$$
\mathbf{v}_{\text{eff}} = \mathbf{v} + \mathbf{V}.
$$

This is equivalent to replacing the time derivative with the convective
derivative:

$$
D_t = \partial_t + \mathbf{V} \cdot \nabla.
$$

Apply this to the continuity equation:

$$
D_t u + \nabla \cdot \mathbf{S} = 0.
$$

This implies:

$$
\partial_t u + \nabla \cdot (\mathbf{S} + u\mathbf{V}) = 0.
$$

So Galilean drift modifies the flux:

$$
\mathbf{S}_{\text{eff}} = \mathbf{S} + u\mathbf{V}.
$$

Thus:

$$
\mathbf{v}_{\text{eff}} = \frac{\mathbf{S}}{u} + \mathbf{V}.
$$

This is the mathematical content of ether drift.


## 4. Why Galilean drift is incompatible with curl transport

Curl-based evolution has the structural form:

$$
\partial_t \mathbf{F} = \nabla \times \mathbf{G}.
$$

Taking divergence:

$$
\partial_t (\nabla \cdot \mathbf{F}) = \nabla \cdot (\nabla \times \mathbf{G}) = 0.
$$

Divergence-free structure is preserved identically.

But if we replace $\partial_t$ with $D_t$:

$$
D_t \mathbf{F} = \nabla \times \mathbf{G},
$$

we introduce convective contributions.

These modify the closure of the system unless additional compensating terms are
introduced.

In other words:

- Galilean drift is not a neutral coordinate change.
- It modifies the intrinsic transport law.
- It changes flux closure unless one alters the dynamics.


Therefore the ether prediction assumes a transport mechanism that is not
compatible with divergence-free curl closure unless further structure is
imposed.


## 5. Michelson–Morley interferometer calculation

Consider an interferometer with two orthogonal arms of equal length
$L$.

Under Galilean drift:

Parallel arm travel time:

$$
t_\parallel
= \frac{L}{c - V}
+ \frac{L}{c + V}
= \frac{2L c}{c^2 - V^2}.
$$

Perpendicular arm travel time:

$$
t_\perp
= \frac{2L}{\sqrt{c^2 - V^2}}.
$$

Expand for $V \ll c$:

$$
t_\parallel
\approx \frac{2L}{c}
\left(1 + \frac{V^2}{c^2}\right),
$$

$$
t_\perp
\approx \frac{2L}{c}
\left(1 + \frac{1}{2}\frac{V^2}{c^2}\right).
$$

Difference:

$$
\Delta t
\approx \frac{L}{c} \frac{V^2}{c^2}.
$$

This predicts a fringe shift.

Experimentally:

$$
\Delta t = 0.
$$


## 6. Flat-space explanation of the null result

The null result does not require curved space.

It requires rejecting Galilean addition for electromagnetic transport.

Under source-free Maxwell evolution:

- propagation is curl-based,
- the transport bound $|\mathbf{S}| \le cu$ is intrinsic,
- radiation saturates the bound independent of laboratory motion.


There is no additive drift term in the transport law.

Therefore:

- round-trip propagation time depends only on arm length,
- not on orientation relative to uniform motion,
- not on drift velocity.


The null result follows from preserving curl-based closure.


## 7. Where hyperbolic kinematics appears

If one demands:

- the same transport law holds in any uniformly moving laboratory,
- no convective correction is added,


then linear velocity addition cannot hold for electromagnetic transport.

The algebra that preserves the intrinsic transport bound leads to hyperbolic
velocity composition.

This hyperbolicity is not a property of space.

It is the algebra required to preserve curl-based transport closure.


## 8. Interpretation without geometric deformation

No deformation of space is required.

No spacetime curvature is required.

What changes between uniformly moving laboratories is the decomposition of
transport into components.

Bodies made of electromagnetic energy maintain their structure through internal
transport.

Changing laboratory description changes how that transport decomposes into
“forward” and “circulating” components.

Hyperbolic-looking effects arise from transport algebra, not from geometry.


## 9. Final conclusion

The Michelson–Morley null result is not evidence of curved space.

It is evidence that electromagnetic propagation is not Galilean carriage.

Source-free Maxwell theory describes divergence-free curl-based transport with
intrinsic continuity closure and a maximal transport rate.

Galilean drift modifies the flux structure and therefore predicts an effect that
does not occur.

The null result selects curl-based transport over additive carriage.

Flat space is sufficient.

The correction is kinematic, not geometric.
