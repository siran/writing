---
title: The Physics of Energy Flow - Axial Interaction of a Static Mass Closure with a Null Probe
date: 2026-03-25
---

# 12b. Axial Interaction of a Static Mass Closure with a Null Probe

Chapter 12a established that a null Maxwell probe carries two equal stress
sectors. That alone explains why a one-channel account gives only half the
full bending, but it does not yet say how a static bounded mass closure
samples those two sectors.

This chapter derives that missing step directly from axial transport.

The key geometric point is simple. A compact toroidal closure interacts
through its axial line. For a static closure there is no preferred sign along
that line, so the leading weak exterior interaction must sample the probe
through both axial directions equally. When that symmetric axial load is
written in terms of the probe's energy-momentum tensor, it is exactly

$$
u+\Pi_n,
$$

where $u$ is the probe energy density and $\Pi_n$ is its longitudinal momentum
flux. For a slow bounded mode this reduces to $u$. For a null Maxwell probe it
becomes $2u$. The weak-field factor of two therefore follows from axial
transport itself, not from a later adjustment.

## 12b.1 Probe Transport Data

Work in the rest frame of the static bounded mass closure.

For a narrow probe packet, write its local energy density, momentum density,
and spatial stress as

$$
u,
\qquad
\mathbf g,
\qquad
T_{ij},
$$

with

$$
\mathbf g=\frac{\mathbf S}{c^2}.
$$

Introduce the corresponding energy-momentum tensor

$$
\Theta^{00}=u,
\qquad
\Theta^{0i}=c\,g_i,
\qquad
\Theta^{ij}=-T_{ij}.
$$

Let

$$
\mathbf n
$$

be the local transport direction of the narrow probe, with

$$
|\mathbf n|=1.
$$

Define the longitudinal momentum-flux density by

$$
\Pi_n:=-n_in_jT_{ij}.
$$

For a null Maxwell probe, chapter 12a gives

$$
\Pi_n=u.
$$

Equivalently,

$$
|\mathbf S|=cu,
$$

so the probe carries no trapped rest component. It is transport all the way
through.

## 12b.2 The Two Axial Channels of a Static Closure

At a point outside a static toroidal closure, the leading interaction is
carried along the local axial line. Because the closure is static, that line
has no preferred sign. It therefore presents two opposite transport channels,
forward and backward along $\mathbf n$.

Introduce the two null axial directions

$$
k_+^\mu:=(1,\mathbf n),
\qquad
k_-^\mu:=(1,-\mathbf n).
$$

Their loads against the probe energy-momentum tensor are

$$
\Theta_{\mu\nu}k_+^\mu k_+^\nu,
\qquad
\Theta_{\mu\nu}k_-^\mu k_-^\nu.
$$

The sign-symmetric axial load seen by the static closure is therefore

$$
\Lambda_n
:=
\frac{1}{2}\Theta_{\mu\nu}k_+^\mu k_+^\nu
+
\frac{1}{2}\Theta_{\mu\nu}k_-^\mu k_-^\nu.
$$

Expanding in the closure rest frame gives

$$
\Theta_{\mu\nu}k_+^\mu k_+^\nu
=
u+2c\,\mathbf g\cdot\mathbf n+\Pi_n,
$$

$$
\Theta_{\mu\nu}k_-^\mu k_-^\nu
=
u-2c\,\mathbf g\cdot\mathbf n+\Pi_n.
$$

Adding and dividing by two, the mixed momentum terms cancel exactly:

$$
\boxed{
\Lambda_n=u+\Pi_n
}.
$$

This identity is exact. No weak-field approximation has been used yet.

It says that a static closure samples two things at once:

- occupancy of the axial line by energy density,
- directed loading of that line by longitudinal momentum flux.

That is the flow-theoretic origin of the doubling.

## 12b.3 Slow Modes and Null Modes

For a slowly moving bounded probe, the longitudinal momentum flux is smaller by
order $v^2/c^2$, so in the strict slow-mode limit

$$
\Pi_n=o(u),
$$

and therefore

$$
\Lambda_n=u+o(u).
$$

So a slow bounded mode loads the static closure essentially by its stored
energy density alone.

For a null Maxwell probe, chapter 12a gives

$$
\Pi_n=u,
$$

hence

$$
\boxed{
\Lambda_n=2u
}.
$$

So the same static closure sees twice the axial load from a null probe that it
would see from a one-channel or slow-mode treatment of the same energy.

This is the exact weak-field factor-of-two point.

## 12b.4 Axial Interaction Potential of a Static Mass Closure

Let the static mass closure generate the exterior strength

$$
\eta(\mathbf r):=\frac{GM}{rc^2},
\qquad
r=|\mathbf r|.
$$

In the weak exterior regime, the leading local interaction must be:

1. local on the scale of the packet,
2. linear in the probe transport data,
3. sign-symmetric under $\mathbf n\mapsto -\mathbf n$ because the closure is
   static,
4. normalized so that the strict slow-mode limit reproduces Newtonian
   attraction.

Under these conditions, the unique axial scalar carried by the probe is

$$
\Lambda_n=u+\Pi_n.
$$

Therefore the leading local interaction energy density is

$$
\boxed{
w_{\mathrm{int}}=-\eta\,\Lambda_n
=
-\eta\,(u+\Pi_n)
}.
$$

This is not an arbitrary fit. The overall unit is already fixed by the
definition of $\eta$ through the Newtonian slow-mode limit. The only question
was what scalar of the probe a static axial closure must sample. The answer is
the symmetric two-channel load $\Lambda_n$.

For a narrow packet centered at $\mathbf X(t)$, with support small compared to
the background scale, we may treat $\eta$ as constant across the packet to
leading order:

$$
U_{\mathrm{int}}(t)
=
\int w_{\mathrm{int}}\,dV
=
-\eta(\mathbf X(t))
\int \Lambda_n\,dV.
$$

Define the total axial load of the packet by

$$
L_n:=\int \Lambda_n\,dV.
$$

Then

$$
U_{\mathrm{int}}(t)=-\eta(\mathbf X(t))\,L_n.
$$

## 12b.5 Exact Weak-Field Bending of a Null Probe

For a null Maxwell probe,

$$
\Lambda_n=2u,
$$

so

$$
L_n=2U,
\qquad
U:=\int u\,dV.
$$

Hence

$$
U_{\mathrm{int}}(t)
=
-2U\,\eta(\mathbf X(t)).
$$

The transverse force on the packet is the negative gradient of the interaction
energy:

$$
\mathbf F_\perp
:=
-\nabla_\perp U_{\mathrm{int}}
=
2U\,\nabla_\perp\eta.
$$

Because

$$
\eta(r)=\frac{GM}{rc^2},
$$

the vector $\nabla\eta$ points inward, so the force is attractive.

The momentum magnitude of the null packet is

$$
P=\frac{U}{c}.
$$

Therefore the infinitesimal change of direction is

$$
d\theta
=
\frac{|\mathbf F_\perp|}{P}\,dt
=
2c\,|\nabla_\perp\eta|\,dt.
$$

Along the unperturbed straight path,

$$
dt=\frac{dz}{c},
$$

so

$$
d\theta
=
2|\nabla_\perp\eta|\,dz.
$$

Take the ray to pass the mass with impact parameter $b$. Then

$$
r(z)=\sqrt{b^2+z^2},
$$

and

$$
|\nabla_\perp\eta|
=
\frac{GM\,b}{c^2(b^2+z^2)^{3/2}}.
$$

Hence

$$
\theta
=
2\int_{-\infty}^{\infty}
\frac{GM\,b}{c^2(b^2+z^2)^{3/2}}\,dz
=
\frac{2GM\,b}{c^2}
\int_{-\infty}^{\infty}\frac{2\,dz}{(b^2+z^2)^{3/2}}.
$$

Using

$$
\int_{-\infty}^{\infty}\frac{dz}{(b^2+z^2)^{3/2}}
=
\frac{2}{b^2},
$$

we obtain

$$
\boxed{
\theta=\frac{4GM}{bc^2}
}.
$$

So the full weak-field light-bending value is recovered here directly from the
axial two-channel loading of a null Maxwell probe.

## 12b.6 Relation to the Newtonian Half-Value

If one keeps only the slow-mode channel, one uses

$$
\Lambda_n\approx u
$$

instead of

$$
\Lambda_n=u+\Pi_n.
$$

Then the interaction energy would be

$$
U_{\mathrm{int}}^{\mathrm{one\ channel}}
=
-U\,\eta,
$$

and the same calculation would give

$$
\theta_{\mathrm{one\ channel}}
=
\frac{2GM}{bc^2}.
$$

So the Newtonian half-value is not mysterious. It is simply the result of
counting only one axial loading channel of the probe.

The full null value appears when the static closure is allowed to sample the
probe through both axial directions, as a toroidal same-substrate interaction
must.

## 12b.7 What Is and Is Not Completed Here

The factor of two is no longer an arbitrary constitutive choice, and it is no
longer hidden in an undetermined coefficient. It has been derived from:

1. the two-channel axial interaction of a static closure,
2. the exact identity
   $$
   \Lambda_n=u+\Pi_n,
   $$
3. the null Maxwell property
   $$
   \Pi_n=u.
   $$

What remains open is not the factor of two itself. What remains open is the
full exact interaction beyond the weak exterior regime:

- finite-size corrections of the bounded mass closure,
- strong-field interaction,
- time-dependent and radiative sectors.

## 12b.8 Summary

For a narrow probe with transport direction $\mathbf n$, the sign-symmetric
axial load seen by a static closure is

$$
\Lambda_n
=
\frac{1}{2}\Theta_{\mu\nu}k_+^\mu k_+^\nu
+
\frac{1}{2}\Theta_{\mu\nu}k_-^\mu k_-^\nu
=
u+\Pi_n.
$$

For a slow bounded mode, this reduces to

$$
\Lambda_n\approx u.
$$

For a null Maxwell probe,

$$
\Lambda_n=2u.
$$

Therefore the weak exterior interaction energy is

$$
U_{\mathrm{int}}=-\eta L_n,
$$

and the resulting null deflection is exactly

$$
\theta=\frac{4GM}{bc^2}.
$$

So the weak-field factor of two is recovered here from first principles of
flow: a static toroidal closure samples both axial transport channels of the
passing null probe.
