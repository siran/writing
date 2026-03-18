---
title: The Physics of Energy Flow - Standing Waves and Discreteness
date: 2026-03-18
---


# 8. Standing Waves and Discreteness

Chapter 7 established Maxwellian transport as the minimal two-aspect closure of
source-free flow. In that closure, each Cartesian component of the transporting
field satisfies the wave equation

$$
\left(\nabla^2-\frac{1}{c^2}\partial_t^2\right)f=0.
$$

We now consider a bounded standing electromagnetic wave on the surface of a
torus. In the
thin-support idealization developed below, that construction yields allowed
integer modes and the Rydberg-type $1/n^2$ scaling. Since hydrogen is matter,
this is a first serious clue that matter itself may be standing
electromagnetic waves.

To make that idea precise, we need a closed support on which energy flow can be
trapped continuously. A sphere cannot sustain a continuous nowhere-vanishing
tangential flow, by the hairy ball theorem. The simplest closed support to
consider next is therefore the surface of a torus. It has two independent
non-contractible cycles, so closure must hold in two independent directions at
once.

In the thin-support idealization, use angular coordinates $(\phi,\theta)$ on
the torus, where $\phi$ runs around the major cycle of radius $R$ and
$\theta$ around the minor cycle of radius $r$. Restrict attention to one
Cartesian component $f$ of the transporting field. The wave equation on that
support becomes

$$
\partial_t^2 f
=
c^2\left(
\frac{1}{R^2}\partial_\phi^2 f
+
\frac{1}{r^2}\partial_\theta^2 f
\right).
$$

Because the support is closed, the field must be periodic on both cycles:

$$
f(\phi+2\pi,\theta,t)=f(\phi,\theta,t),
\qquad
f(\phi,\theta+2\pi,t)=f(\phi,\theta,t).
$$

Now seek a separated standing mode

$$
f(\phi,\theta,t)=A\cos(m\phi)\cos(n\theta)\cos(\omega t).
$$

The periodicity conditions force the mode numbers to be integers
$m,n\in\mathbb Z_{\ge 0}$. Substituting this form into the wave equation gives

$$
\omega^2
=
c^2\left(\frac{m^2}{R^2}+\frac{n^2}{r^2}\right).
$$

So the torus discretizes the transport immediately. The closed geometry permits
only integer mode numbers and therefore only discrete standing-wave
frequencies.

The same result can be written as closure in wavelength form:

$$
m\lambda_\phi = 2\pi R,
\qquad
n\lambda_\theta = 2\pi r,
$$

for integers $m,n\in\mathbb Z_{>0}$. Equivalently,

$$
k_\phi=\frac{m}{R},
\qquad
k_\theta=\frac{n}{r}.
$$

So a bounded toroidal standing wave is not labeled by a continuous parameter,
but by an integer pair $(m,n)$, and its frequency is

$$
\omega_{mn}
=
c\sqrt{k_\phi^2+k_\theta^2}
=
c\sqrt{\frac{m^2}{R^2}+\frac{n^2}{r^2}}.
$$

So discreteness enters before any particle picture. Once the field is required
to close on itself on a torus, only certain standing-wave organizations are
allowed.

This is the right way to read the early quantum fact that hydrogen radiates in
discrete lines. The discreteness does not require an electron moving on
planet-like orbits. It requires only that bounded electromagnetic transport
reorganize itself between allowed standing-wave closures.

The observed Rydberg pattern can then be read as a special family of such
reorganizations. If a fixed toroidal support is refined into an $N\times N$
standing-wave partition, the same total energy is distributed across $N^2$
coherent cells. The characteristic energy per cell therefore scales as

$$
E_N \propto \frac{E_1}{N^2}.
$$

Transitions between two such allowed organizations then have the form

$$
\Delta E \propto \frac{1}{p^2}-\frac{1}{q^2},
\qquad p>q.
$$

The integers are not mysterious labels imposed from outside. They are the
counting numbers of the standing-wave closure itself.

So discreteness begins as standing-wave closure of Maxwellian transport on a
closed support. Once that bounded standing wave exists, its further global
aspects can be separated. The trapped load of the closed circulation appears as
mass in the next chapter. The through-hole character of that same toroidal
standing wave appears as charge in the chapter after that.
