---
title: The Physics of Energy Flow - Standing Waves and Discreteness
date: 2026-03-18
---

# 8. Standing Waves and Discreteness

Chapter 7 established that source-free energy flow satisfies the wave equation

$$
\partial_t^2 \mathbf F-c^2\nabla^2\mathbf F=0,
\qquad
\nabla\cdot\mathbf F=0.
$$

As a useful representation, each Cartesian component therefore satisfies

$$
\left(\nabla^2-\frac{1}{c^2}\partial_t^2\right)f=0.
$$

The wave equation permits both open propagating transport and organized, closed
closures. When a flow configuration refracts its own transport, curving its own
path through the field it generates, it can close on itself. Such a
self-refracting closure must be a shape that admits continuous nowhere-vanishing
tangential flow. A sphere does not: by the hairy ball theorem, no continuous
nowhere-vanishing tangential vector field exists on a sphere. The simplest
closed shape that can sustain such flow is a torus, a sphere with a smooth
through-hole. It has two independent non-contractible cycles, and the flow must
close in both directions at the same time.

A self-refracting flow closing toroidally yields integer modes and the
Rydberg-type $1/n^2$ scaling. Since hydrogen is matter, this is a first
serious clue that matter itself may be organized self-refracting closures of
energy flow.

For modes organized along the toroidal closure, those whose dominant structure
wraps the two cycles, the natural starting point is not a fixed Cartesian
component and not even fixed toroidal angles. Start with a closed centerline
$\gamma(s)$ parametrized by arclength $s\in[0,L)$, and around it choose a local
orthonormal frame $(\hat{\mathbf t},\hat{\boldsymbol\rho},\hat{\boldsymbol\theta})$,
where $\hat{\mathbf t}$ is tangent to the centerline and
$\hat{\boldsymbol\theta}$ is the turning direction around the local
cross-section. The transporting direction is then a helical tangent

$$
\hat{\mathbf f}
=
\cos\beta\,\hat{\mathbf t}
+
\sin\beta\,\hat{\boldsymbol\theta},
\qquad
\hat{\mathbf q}
=
-\sin\beta\,\hat{\mathbf t}
+
\cos\beta\,\hat{\boldsymbol\theta}.
$$

Here $\beta$ is the local winding angle. Unlike the later standing-wave labels,
it need not be fixed a priori: in a fuller self-refracting description it can
depend on the flow itself, just as the local cross-sectional radius and the
curvature of $\gamma$ can depend on the flow itself.

At the level needed to count allowed standing closures, take a thin nearly
uniform toroidal closure: the cross-sectional radius is approximately constant
$r$, the centerline length is approximately constant $L=2\pi R$, and the frame
varies slowly enough that the leading closure counting comes from the two
periodic directions themselves. Resolve the field by a scalar amplitude
$f(s,\theta,t)$ in this moving frame. Then, to leading order,

$$
\partial_t^2 f
=
c^2\left(
\partial_s^2 f
+
\frac{1}{r^2}\partial_\theta^2 f
\right),
$$

with lower-order curvature terms omitted because they do not change the integer
closure counting below.

Because the closure is self-consistent, the field must be periodic on both
cycles:

$$
f(s+L,\theta,t)=f(s,\theta,t),
\qquad
f(s,\theta+2\pi,t)=f(s,\theta,t).
$$

Now seek a separated standing mode

$$
f(s,\theta,t)=A\cos(ks)\cos(n\theta)\cos(\omega t).
$$

The periodicity conditions force

$$
kL=2\pi m,
\qquad
m,n\in\mathbb Z_{\ge 0}.
$$

These integers belong to the standing field on the two fundamental cycles of
the toroidal closure. Rationality enters at a different level: a single
helical streamline closes only when its slope returns after $m$ turns of one
cycle and $n$ of the other, so closed streamline winding is exactly the
statement that the ratio of the two cycle counts is rational.

Since $L=2\pi R$, this gives

$$
k=\frac{m}{R}.
$$

Substituting the standing mode into the wave equation yields

$$
\omega^2
=
c^2\left(k^2+\frac{n^2}{r^2}\right)
=
c^2\left(\frac{m^2}{R^2}+\frac{n^2}{r^2}\right).
$$

So the torus discretizes the transport immediately. The closed geometry permits
only integer mode numbers and therefore only discrete standing-wave frequencies.

If one prefers the more familiar angular coordinate around the major cycle,

$$
\phi = \frac{s}{R},
$$

then the same leading-order closure equation becomes

$$
\partial_t^2 f
=
c^2\left(
\frac{1}{R^2}\partial_\phi^2 f
+
\frac{1}{r^2}\partial_\theta^2 f
\right).
$$

The same result can be written as closure in wavelength form:

$$
m\lambda_s = L = 2\pi R,
\qquad
n\lambda_\theta = 2\pi r,
$$

for integers $m,n\in\mathbb Z_{>0}$. Equivalently,

$$
k_s=\frac{m}{R},
\qquad
k_\theta=\frac{n}{r}.
$$

So a bounded toroidal standing wave is not labeled by a continuous parameter,
but by an integer pair $(m,n)$, and its frequency is

$$
\omega_{mn}
=
c\sqrt{k_s^2+k_\theta^2}
=
c\sqrt{\frac{m^2}{R^2}+\frac{n^2}{r^2}}.
$$

So discreteness enters before any particle picture. Once the field is required
to close on itself in a toroidal closure, only certain standing-wave
organizations are allowed.

This is the right way to read the early quantum fact that hydrogen radiates in
discrete lines. The discreteness does not require an electron moving on
planet-like orbits. It requires only that bounded energy flow reorganize itself
between allowed standing-wave closures.

The observed Rydberg pattern can then be read as a special family of such
reorganizations. If a fixed toroidal closure is refined into an $N\times N$
standing-wave partition, the same total energy is distributed across
$N^2$ coherent cells. The characteristic energy per cell therefore
scales as

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

So discreteness begins as standing-wave closure of source-free energy flow in a
self-refracting toroidal configuration. Once that closure exists, its further
global aspects can be separated. The narrow-band envelope sector of the same
bounded mode appears as Schrodinger dynamics in the next chapter. The
through-hole character of that same toroidal standing wave appears as charge in
the chapter after that.
