---
title: The Physics of Energy Flow - Effective String Structure from Bounded Maxwellian Transport
date: 2026-03-17
---

# 217. Effective String Structure from Bounded Maxwellian Transport

The earlier chapters already derived the transport core. Once one further step
is admitted, namely that Maxwellian transport can organize into a bounded
toroidal mode, the structures usually postulated in string descriptions follow
directly.

This appendix proves the exact part of that statement. It does not assume a
fundamental string ontology. It shows that a bounded thin-tube Maxwellian mode
already carries:

- integer winding data,
- line tension,
- inertial line density,
- a self-trapping condition,
- and a discrete closed-mode spectrum.

In that precise sense, string-theoretic structure is an effective description
of bounded electromagnetic topology.

## 217.1 Geometric Setup

Let

$$
X : \mathbb{R}/L\mathbb{Z} \to \mathbb{R}^3
$$

be a smooth closed curve parameterized by arclength $s$, so

$$
|X'(s)| = 1,
\qquad
\tau(s) := X'(s).
$$

For sufficiently small $\varepsilon > 0$, let $N_\varepsilon(X)$ be the thin
tube about $X$, and let $\Sigma_\varepsilon(s)$ denote the transverse
cross-section orthogonal to $\tau(s)$ at $X(s)$.

Assume a bounded Maxwellian mode is concentrated in that tube. Write its
energy density and flux as

$$
u_\varepsilon(x,t),
\qquad
S_\varepsilon(x,t).
$$

Assume further that the transporting part of the mode is tangent to the tube,
so in the thin-tube limit

$$
S_\varepsilon(x,t)
=
k\,u_\varepsilon(x,t)\,\tau(s)
+ O(\varepsilon),
$$

where $k$ is the local transport speed of the background region. In vacuum,
$k=c$.

## 217.2 Integer Winding

Suppose the thin tube lies on an invariant torus. A torus has two independent
non-contractible cycles. Any closed tangent transport line on that torus is
therefore labeled by an integer pair

$$
(m,n) \in \mathbb{Z}^2,
$$

counting its windings about those two cycles.

This is the same topological statement established in chapter 8. The present
point is only that, once the bounded mode is reduced to a thin closed tube,
those integers are already the winding numbers of an effective string.

## 217.3 Line Energy and Tension

Define the line energy density of the tube by integrating the energy density
over each transverse section:

$$
\mathcal{T}_\varepsilon(s,t)
:=
\int_{\Sigma_\varepsilon(s)} u_\varepsilon(x,t)\,dA.
$$

The total energy contained in the tube is then

$$
E_\varepsilon(t)
=
\int_0^L \mathcal{T}_\varepsilon(s,t)\,ds.
$$

In the effective one-dimensional description, energy per unit length is
exactly the string tension. So define

$$
\mathcal{T}(s,t)
:=
\lim_{\varepsilon\to 0}\mathcal{T}_\varepsilon(s,t).
$$

If the closed mode is approximately uniform along the tube, then

$$
\mathcal{T}(s,t) = \mathcal{T},
$$

and therefore

$$
E = \mathcal{T} L.
$$

So the effective tension is not postulated. It is the line reduction of the
Maxwellian energy density.

## 217.4 Line Momentum and Inertial Density

Define the momentum density by

$$
g_\varepsilon := \frac{S_\varepsilon}{k^2}.
$$

Its tangential line density is

$$
\mathcal{P}_\varepsilon(s,t)
:=
\int_{\Sigma_\varepsilon(s)} g_\varepsilon(x,t)\cdot\tau(s)\,dA.
$$

Using the tangential transport relation from section 217.1,

$$
g_\varepsilon(x,t)\cdot\tau(s)
=
\frac{u_\varepsilon(x,t)}{k}
+ O(\varepsilon),
$$

so

$$
\mathcal{P}_\varepsilon(s,t)
=
\frac{1}{k}\mathcal{T}_\varepsilon(s,t)
+ O(\varepsilon).
$$

Passing to the thin-tube limit gives

$$
\mathcal{P}(s,t)=\frac{\mathcal{T}(s,t)}{k}.
$$

The corresponding inertial line density is therefore

$$
\mu(s,t)
:=
\frac{\mathcal{P}(s,t)}{k}
=
\frac{\mathcal{T}(s,t)}{k^2}.
$$

In vacuum,

$$
\mu = \frac{\mathcal{T}}{c^2}.
$$

So the effective inertial density is also not postulated. It is fixed by the
Maxwellian momentum density of the bounded mode.

## 217.5 Small Disturbances of the Closed Tube

Now consider a small transverse displacement

$$
\xi(s,t)
$$

of the effective line. Assume the unperturbed closed mode is uniform enough
that $\mathcal{T}$ and $\mu$ may be treated as constants to leading order.

Take a short segment $[s,s+ds]$. The tension vectors at its endpoints are

$$
\mathcal{T}\,\partial_s(X+\xi)(s,t),
\qquad
\mathcal{T}\,\partial_s(X+\xi)(s+ds,t).
$$

Subtracting and keeping the leading transverse term yields the net transverse
force

$$
dF_\perp
=
\mathcal{T}\,\partial_s^2 \xi(s,t)\,ds.
$$

The inertial mass of that segment is

$$
dm = \mu\,ds,
$$

so momentum balance gives

$$
\mu\,\partial_t^2 \xi
=
\mathcal{T}\,\partial_s^2 \xi.
$$

Using

$$
\mu=\frac{\mathcal{T}}{k^2},
$$

we obtain

$$
\partial_t^2 \xi - k^2 \partial_s^2 \xi = 0.
$$

So the effective one-dimensional disturbance speed is exactly the underlying
Maxwellian transport speed.

## 217.6 Self-Trapping Condition

Appendix 214 already derived the geometric-optics transport law in a static
background speed field $k(x)$. For a narrow radiative packet with Hamiltonian

$$
H(x,p)=k(x)\,|p|,
$$

Hamilton's equations are

$$
\dot{x}=k\,\frac{p}{|p|},
\qquad
\dot{p}=-|p|\,\nabla k.
$$

Let

$$
\hat{\mathbf t}:=\frac{p}{|p|}
$$

be the unit transport tangent. Then

$$
\dot{x}=k\,\hat{\mathbf t}.
$$

Write

$$
p=|p|\,\hat{\mathbf t}.
$$

Differentiating gives

$$
\dot{p}=\dot{|p|}\,\hat{\mathbf t}+|p|\,\dot{\hat{\mathbf t}}.
$$

Project this orthogonally to $\hat{\mathbf t}$. Since the tangential part drops
out,

$$
|p|\,\dot{\hat{\mathbf t}}
=
-|p|\,\nabla_\perp k,
$$

where

$$
\nabla_\perp k
:=
\nabla k-(\hat{\mathbf t}\cdot\nabla k)\hat{\mathbf t}
$$

is the transverse gradient. Therefore

$$
\dot{\hat{\mathbf t}}=-\nabla_\perp k.
$$

Now parametrize the ray by arclength $s$. Since

$$
\dot{x}=k\,\hat{\mathbf t},
$$

we have

$$
\frac{ds}{dt}=k.
$$

Hence

$$
\frac{d\hat{\mathbf t}}{ds}
=
\frac{\dot{\hat{\mathbf t}}}{k}
=
-\nabla_\perp \ln k.
$$

But for a curve with curvature $\kappa$ and principal normal $N$,

$$
\frac{d\hat{\mathbf t}}{ds}=\kappa N.
$$

So the exact trapping condition is

$$
\boxed{
\kappa N=-\nabla_\perp \ln k
}.
$$

This equation is the clean transport statement of self-refraction. A narrow
transport branch remains trapped on a curved support exactly when the inward
transverse gradient of the local transport speed supplies the required
curvature of the ray.

For a circular orbit of radius $R$ in a radially symmetric static profile
$k(r)$, the curvature is $\kappa=1/R$ and the condition reduces to

$$
\frac{1}{R}
=
\frac{1}{k(R)}\frac{dk}{dr}(R).
$$

So a closed circular transport line is self-trapped precisely when the outward
increase of $k$ balances the inward bending required by the orbit.

In a self-trapped bounded Maxwellian mode, that profile is not imposed from
outside. It is generated by the same total trapped load of the closure itself.
The field is both the transported thing and the thing that shapes the
transport path.

## 217.7 Closed-Mode Spectrum

Because the support is closed,

$$
\xi(s+L,t)=\xi(s,t).
$$

Expand in Fourier modes,

$$
\xi(s,t)=\sum_{n\in\mathbb{Z}} a_n(t)\,e^{i2\pi ns/L}.
$$

Substituting into the line equation gives

$$
\ddot{a}_n + \omega_n^2 a_n = 0,
$$

with

$$
\omega_n = \frac{2\pi k}{L}|n|.
$$

So the closed Maxwellian tube carries a discrete oscillator spectrum.

The reason is exactly the same as in chapter 8: closure forces periodic
matching. The effective string equation only makes that spectral consequence
explicit.

## 217.8 What Has Been Derived

From bounded Maxwellian transport on a thin closed toroidal support, the
following effective string data are forced:

- winding numbers $(m,n)$ from toroidal topology,
- line tension $\mathcal{T}$ from energy density,
- inertial line density $\mu = \mathcal{T}/k^2$ from momentum density,
- the exact self-trapping condition
  $$
  \kappa N=-\nabla_\perp \ln k,
  $$
- and discrete mode frequencies
  $$
  \omega_n = \frac{2\pi k}{L}|n|.
  $$

These are precisely the structures usually introduced axiomatically in a
string description.

## 217.9 Final Statement

String structure is not primitive here. It is the effective one-dimensional
description of a bounded Maxwellian mode.

The deeper object is the electromagnetic closure itself. The string appears
when that closure is reduced to its thin-tube, closed-line, periodic support.
