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

Chapter 7b derived the self-refraction principle: retarded portions of the
same flow alter the local transport law and bend later transport of that same
field. This chapter asks what follows once that bending becomes strong enough
to make the path close on itself.

Toroidal configurations are not exotic. They arise spontaneously whenever a
flow curls back on itself — smoke rings, vortex rings in water, incense
plumes disturbed by a hand. What is common to all these cases is that
toroidal geometry forms easily; what distinguishes them is whether the
resulting closure can self-sustain. Most such configurations dissipate. The
ones that persist are those whose self-refraction loading matches the
geometric curvature needed to maintain the closure (Appendix A0). This
chapter does not address the self-consistency of the closure. It asks only
what standing-wave organizations are allowed once a toroidal closure exists.

A self-refracting closure must be a shape that admits continuous
nowhere-vanishing tangential flow. A sphere does not: by the hairy ball
theorem, no continuous nowhere-vanishing tangential vector field exists on a
sphere. The simplest closed shape that can sustain such flow is a torus, a
sphere with a smooth through-hole. It has two independent non-contractible
cycles, and the flow must close in both directions at the same time.

As we shall see, a self-refracting flow closing toroidally yields integer modes
and the Rydberg-type $1/n^2$ scaling. Since hydrogen is matter, this is
a first serious clue that matter itself may be organized self-refracting
closures of energy flow.

For modes organized along the toroidal closure, those whose dominant structure
wraps the two cycles, the natural starting point is not a fixed Cartesian
component and not even fixed toroidal angles. Start with a closed centerline
$\gamma(s)$ parametrized by arclength $s\in[0,L)$, and around it
choose a local frame in which $\hat{\mathbf t}$ is tangent to the centerline
and $\hat{\boldsymbol\theta}$ is the turning direction around the local
cross-section. The transporting direction is then a helical tangent

$$
\hat{\mathbf f}
=
\cos\beta\,\hat{\mathbf t}
+
\sin\beta\,\hat{\boldsymbol\theta}.
$$

Here $\beta$ is the local winding angle, measured from the centerline tangent.
Chapter 7b already derived that local self-refraction fixes the bending angle
through

$$
\cos\beta=\frac{1}{n_{\mathrm{eff}}},
\qquad
\tan\beta=\sqrt{n_{\mathrm{eff}}^2-1}.
$$

This chapter needs only the geometric consequence: once self-refraction has
produced a toroidal closure, the winding can be treated as approximately
uniform. The self-consistent aspect ratio of such a closure is derived in
Appendix A0. The mode counting below does not depend on that ratio: the
integer conditions are topological and hold for any aspect ratio. The
separated wave equation used below omits curvature corrections that depend on
the aspect ratio; these corrections shift the exact mode frequencies but do
not change the integer counting (see Appendix A2 for the full toroidal
Laplacian).

Take a toroidal closure with cross-sectional radius $r$ and centerline length
$L=2\pi R$, with the winding angle $\beta$ approximately constant along a
closed streamline. If one such streamline winds $m$ times around the major
cycle and $n$ times around the minor cycle before returning to itself, then

$$
\Delta s = mL,
\qquad
\Delta\theta = 2\pi n.
$$

Since $\tan\beta$ is the ratio of transverse advance to longitudinal advance,

$$
\tan\beta
=
\frac{r\,\Delta\theta}{\Delta s}
=
\frac{nr}{mR}.
$$

So closure of a single helical streamline is exactly the statement that its
slope is rational: it returns only after integer counts on the two
non-contractible cycles.

Combining the geometric closure with the constitutive refraction relation gives

$$
\tan\beta=\frac{nr}{mR}=\sqrt{n_{\mathrm{eff}}^2-1},
$$

so equivalently

$$
\beta
=
\arctan\!\left(\frac{nr}{mR}\right)
=
\arccos\!\left(\frac{1}{n_{\mathrm{eff}}}\right),
$$

and

$$
n_{\mathrm{eff}}
=
\sqrt{1+\left(\frac{nr}{mR}\right)^2}.
$$

The standing field is a stronger condition than closure of one streamline. It
must be single-valued on both cycles of the toroidal closure. Resolve the field
by a scalar amplitude $f(s,\theta,t)$ in this moving frame. Then, to leading
order,

$$
\partial_t^2 f
=
c^2\left(
\partial_s^2 f
+
\frac{1}{r^2}\partial_\theta^2 f
\right),
$$

with curvature corrections omitted. These corrections, which depend on the
aspect ratio $r/R$, shift the exact mode frequencies but do not affect the
integer counting. The full toroidal wave equation with all curvature terms
retained is treated in Appendix A2.

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

The $\theta$-periodicity forces

$$
n\in\mathbb Z_{\ge 0},
$$

while the $s$-periodicity forces

$$
kL=2\pi m,
\qquad
m\in\mathbb Z_{\ge 0}.
$$

So the same pair of integers appears twice: first as the winding counts of a
closed helical streamline, and second as the phase counts of a standing field
that is single-valued on the two fundamental cycles.

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
