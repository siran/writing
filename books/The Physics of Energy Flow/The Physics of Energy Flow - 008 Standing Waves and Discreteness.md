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
To see what sets it, use the ordinary $E/B$ representation and let one portion
of the flow act on a neighboring portion through its retarded field. Write the
local field on a small segment of the closure as
$\left(E_{\mathrm{loc}},B_{\mathrm{loc}}\right)$, and let
$\left(E_{\mathrm{ret}},B_{\mathrm{ret}}\right)$ denote the retarded field at
that segment produced by neighboring segments of the same closure. The exact
causal bookkeeping can then be written in constitutive form as

$$
D
=
\epsilon E_{\mathrm{loc}} + P_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}],
\qquad
H
=
\frac{1}{\mu}B_{\mathrm{loc}} - M_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}].
$$

That is the same mathematical role played by polarization and magnetization in
ordinary media, except that here the response is produced by delayed portions
of the same flow. No scalar energy density is used to compute this interaction:
the primary objects are the retarded electric and magnetic fields themselves.

In the thin nearly uniform, slowly varying regime used in this chapter,
linearize that exact retarded response against the local field and write

$$
P_{\mathrm{self}}\approx \epsilon\,\chi_{e,\mathrm{eff}}\,E_{\mathrm{loc}},
\qquad
M_{\mathrm{self}}\approx \chi_{m,\mathrm{eff}}\,H.
$$

Here $\chi_{e,\mathrm{eff}}$ and $\chi_{m,\mathrm{eff}}$ are local
approximations to the underlying retarded response functionals.

Then

$$
D \approx \epsilon_{\mathrm{eff}}E_{\mathrm{loc}},
\qquad
B_{\mathrm{loc}} \approx \mu_{\mathrm{eff}}H,
$$

with

$$
\epsilon_{\mathrm{eff}}=\epsilon(1+\chi_{e,\mathrm{eff}}),
\qquad
\mu_{\mathrm{eff}}=\mu(1+\chi_{m,\mathrm{eff}}).
$$

Therefore

$$
c_{\mathrm{eff}}
=
\frac{1}{\sqrt{\mu_{\mathrm{eff}}\epsilon_{\mathrm{eff}}}},
\qquad
n_{\mathrm{eff}}
=
\frac{c}{c_{\mathrm{eff}}}
=
\sqrt{\frac{\mu_{\mathrm{eff}}\epsilon_{\mathrm{eff}}}{\mu\epsilon}}
=
\sqrt{(1+\chi_{e,\mathrm{eff}})(1+\chi_{m,\mathrm{eff}})}.
$$

Approximating the local overlap region as a higher-index layer of the same
field, with exterior index $1$, and approximating the entering transport as
locally tangent to that layer, Snell's law, with angles measured from the local
normal, gives

$$
\sin\theta_{\mathrm{in}}
=
n_{\mathrm{eff}}\sin\theta_{\mathrm{tr}},
\qquad
\theta_{\mathrm{in}}=\frac{\pi}{2},
$$

so

$$
\sin\theta_{\mathrm{tr}}=\frac{1}{n_{\mathrm{eff}}}.
$$

Since $\beta$ is the complementary angle to the centerline tangent,

$$
\beta=\frac{\pi}{2}-\theta_{\mathrm{tr}},
\qquad
\cos\beta=\frac{1}{n_{\mathrm{eff}}},
\qquad
\tan\beta=\sqrt{n_{\mathrm{eff}}^2-1}.
$$

This chapter needs only the geometric consequence: once self-refraction has
produced a thin nearly uniform toroidal closure, the winding can be treated as
approximately uniform.

At the level needed to count allowed standing closures, take a thin nearly
uniform toroidal closure: the cross-sectional radius is approximately constant
$r$, the centerline length is approximately constant
$L=2\pi R$, and the winding angle $\beta$ is approximately constant along a
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
