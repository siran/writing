---
title: The Physics of Energy Flow - Nested Transport and Hyperbolic Composition
date: 2026-03-13
---

# 202. Nested Transport and Hyperbolic Composition

The double-curl transport closure of chapter 7 determines the local transport
cone. Reapplying

$$
\nabla\times(\nabla\times\mathbf{F})
$$

acts again on field structure and raises the spatial operator. Nested transport
is a different question. It belongs to kinematics: how do successive bounded
transport increments compose when they occur in the same approximately uniform
region and therefore share the same local transport speed $k$?

To keep the discussion in one lab, consider motion along one spatial direction
$x$. Let $u$ denote the speed produced from rest by one standard transport
pulse in that region. If a body is already moving at speed $v$, let

$$
v \oplus u
$$

denote the speed measured in the same lab after applying that same standard
pulse again.

Because $k$ is the local transport speed singled out by the electromagnetic
closure, no transport process native to that region can push a mode outside the
admissible interval $|v|<k$. So the composition law must preserve that bound.
This already rules out Galilean additivity as an exact transport law, since

$$
v+u
$$

can exceed $k$ even when both $|v|<k$ and $|u|<k$ separately hold. The problem
is therefore not whether the bound survives composition, but what exact shape
the composition law must take once that bound is respected.

The composition operation $\oplus$ should satisfy four basic requirements:

- identity: $v\oplus 0 = v$ and $0\oplus u = u$
- associativity: successive standard pulses can be grouped arbitrarily
- oddness: reversing both directions reverses the result
- boundedness: if $|v|<k$ and $|u|<k$, then $|v\oplus u|<k$

The composition law can now be derived directly from the transport cone. In the
same approximately uniform region, the local transport speed $k$ picks out the
lines

$$
x = \pm kt,
$$

which bound the local transport cone. Writing the corresponding null
coordinates

$$
\xi = t + \frac{x}{k}, \qquad \chi = t - \frac{x}{k},
$$

any orientation-preserving linear map fixing those two directions takes the
form

$$
\xi' = a\,\xi, \qquad \chi' = b\,\chi,
$$

with $a,b>0$. For speed composition only the ratio matters, so write

$$
\lambda^2:=\frac{a}{b}.
$$

Now consider a line of constant speed $v$:

$$
x=vt.
$$

Along that line the null-coordinate ratio is

$$
R(v):=\frac{\xi}{\chi}
=
\frac{t+x/k}{t-x/k}
=
\frac{1+v/k}{1-v/k}
=
\frac{k+v}{k-v}.
$$

The rest line has $R(0)=1$. If one standard pulse from rest produces speed
$u$, then the corresponding cone-preserving map has

$$
R(u)=\lambda(u)^2.
$$

Applying that same pulse to a line already moving at speed $v$ multiplies the
same null ratio by the same factor:

$$
R(v\oplus u)=\lambda(u)^2R(v)=R(u)\,R(v).
$$

Therefore

$$
\frac{k+v\oplus u}{k-v\oplus u}
=
\frac{k+u}{k-u}\cdot\frac{k+v}{k-v}.
$$

Solving this relation gives

$$
\boxed{
v\oplus u
=
\frac{v+u}{1+vu/k^2}
}.
$$

This is the hyperbolic composition law forced by preservation of the same local
transport cone.

Only after this step is it useful to introduce an additive parameter. Taking
the logarithm of $R(v)$ gives

$$
\eta(v):=\frac12\ln\!\frac{k+v}{k-v}.
$$

Then

$$
\eta(v\oplus u)=\eta(v)+\eta(u).
$$

Equivalently,

$$
\eta(v)=\operatorname{artanh}\!\left(\frac{v}{k}\right),
\qquad
v=k\tanh\eta.
$$

So successive identical pulses add linearly in $\eta$, not in $v$. If one
pulse contributes $\eta_0$, then after $n$ identical pulses the lab speed is

$$
v_n=k\tanh(n\eta_0).
$$

So the distinction is exact:

- double curl organizes source-free transport locally
- repeated double curl changes field structure
- nested transport composes successive transport increments that preserve the
  same local bound $k$
- preserving that cone forces hyperbolic composition

The train-and-passenger image is therefore valid, but only at the kinematic
level. One transport process may be nested inside another. The resulting
composition is hyperbolic because the same local transport speed $k$ is
preserved at each step.
