---
title: The Physics of Energy Flow - Moving Closure, Length Contraction, and Michelson-Morley
date: 2026-03-14
---

# 204. Moving Closure, Length Contraction, and Michelson-Morley

This appendix derives longitudinal contraction from the structure of a moving
self-sustained closure. The contraction is not inserted as a coordinate rule.
It is the geometric deformation required for one bounded transport mode to
remain coherent while drifting uniformly through an approximately uniform
region.

Throughout this appendix, let $k$ denote the local transport speed in that
region. The derivation assumes that $k$ is effectively constant over the size
of the apparatus during one run. More general backgrounds require path
integrals of the same local transport law.

## 204.1 Assumptions and Rest Closure

Fix an approximately uniform region in which the local transport speed is the
constant $k>0$.

Consider one bounded self-sustained mode. In its rest configuration there is no
distinguished drift direction. Choose one closure span of length $L_0$ along a
chosen axis, and one orthogonal closure span of the same length $L_0$.

The quantity $L_0$ is not introduced as an external ruler length. It is the
rest span of one internal closure of the mode.

One out-and-back closure across such a span has recurrence period

$$
T_0=\frac{2L_0}{k}.
$$

Now let the whole mode drift uniformly with speed $v$ along the $x$ direction,
with

$$
0\le v<k.
$$

We seek the moving longitudinal span $L_\parallel$ for which the drifting mode
remains one coherent closure.

## 204.2 Transverse Closure Under Drift

Consider a transverse closure across a span of length $L_0$, orthogonal to the
drift.

During one half-cycle of duration $\tau_\perp$, the receiving point of the mode
shifts longitudinally by $v\tau_\perp$. The transport still moves locally at
speed $k$, so the half-cycle geometry is

$$
(k\tau_\perp)^2=L_0^2+(v\tau_\perp)^2.
$$

Rearranging,

$$
(k^2-v^2)\tau_\perp^2=L_0^2.
$$

Therefore

$$
\tau_\perp=\frac{L_0}{\sqrt{k^2-v^2}},
$$

and the full transverse closure time is

$$
T_\perp=2\tau_\perp=\frac{2L_0}{\sqrt{k^2-v^2}}.
$$

## 204.3 Longitudinal Closure Under Drift

Let the longitudinal extent of the moving mode be $L_\parallel$. This is the
quantity to be determined.

For the forward half-cycle, the receiving boundary recedes at speed $v$, so

$$
\tau_+=\frac{L_\parallel}{k-v}.
$$

For the return half-cycle, the receiving boundary approaches at speed $v$, so

$$
\tau_-=\frac{L_\parallel}{k+v}.
$$

The full longitudinal closure time is therefore

$$
T_\parallel
=
\tau_+ + \tau_-
=
\frac{L_\parallel}{k-v}+\frac{L_\parallel}{k+v}
=
\frac{2kL_\parallel}{k^2-v^2}.
$$

## 204.4 Coherence of the Moving Closure

The drifting object is one self-sustained mode. Its transverse and longitudinal
closures cannot recur with different periods. If they did, then after one full
transverse recurrence and one full longitudinal recurrence the same moving mode
would assign different local states to what is supposed to be one coherent
configuration. The closure would fail to remain single-valued.

So the moving mode must satisfy

$$
T_\parallel = T_\perp.
$$

Substituting the expressions above gives

$$
\frac{2kL_\parallel}{k^2-v^2}
=
\frac{2L_0}{\sqrt{k^2-v^2}}.
$$

Solving for $L_\parallel$,

$$
L_\parallel
=
L_0\,\frac{\sqrt{k^2-v^2}}{k}
=
L_0\sqrt{1-\frac{v^2}{k^2}}.
$$

If we define

$$
\gamma=\frac{1}{\sqrt{1-v^2/k^2}},
$$

then

$$
L_\parallel=\frac{L_0}{\gamma}.
$$

This is the contraction of the moving closure along the drift direction.

## 204.5 Proposition

The previous computation proves the following statement.

> Let a bounded self-sustained closure drift uniformly through an
> approximately uniform region with local transport speed $k$. If the moving
> closure remains coherent, then its longitudinal span must be
>
> $$
> L_\parallel=L_0\sqrt{1-\frac{v^2}{k^2}}.
> $$

The conclusion is forced by coherence of the moving closure. It is not an
additional convention.

## 204.6 Structural Meaning

The contraction has not been imposed as a measurement convention. It has been
derived from one structural requirement only: the moving bounded mode must
remain one coherent closure.

So the meaning of the result is precise:

- a mode at rest closes with one recurrence structure
- a drifting mode must preserve that closure
- preserving that closure forces a longitudinal deformation

Length contraction appears here as the geometry required for moving closure,
not as an external postulate.

## 204.7 Michelson-Morley Consequence

Now consider a Michelson-Morley interferometer built from the same bounded
material closures and drifting uniformly through the same approximately uniform
region.

Let each arm have rest length $L_0$.

The arm transverse to the drift keeps that length geometrically, so its
round-trip transport time is

$$
T_\perp=\frac{2L_0}{\sqrt{k^2-v^2}}.
$$

The arm parallel to the drift contracts to

$$
L_\parallel=L_0\sqrt{1-\frac{v^2}{k^2}},
$$

so its round-trip transport time is

$$
T_\parallel
=
\frac{L_\parallel}{k-v}+\frac{L_\parallel}{k+v}
=
\frac{2kL_\parallel}{k^2-v^2}.
$$

Substituting the contracted length,

$$
T_\parallel
=
\frac{2kL_0\sqrt{1-v^2/k^2}}{k^2-v^2}
=
\frac{2L_0}{\sqrt{k^2-v^2}}
=
T_\perp.
$$

Therefore

$$
\Delta T = T_\parallel - T_\perp = 0.
$$

So a Michelson-Morley device is blind to uniform translational drift through a
region with uniform local transport speed $k$.

The null result does not arise because nothing moved. It arises because the
same transport closure that carries the signal also determines the moving
geometry of the device.

## 204.8 Scope

This appendix addresses uniform drift in an approximately uniform region. If
the surrounding transport conditions vary across the apparatus, then the local
speed $k$ must be replaced by the appropriate path-dependent transport speed.
The structural point remains the same: transport and geometry must be solved
together, because the bounded mode and the signal it carries are governed by
the same closure.
