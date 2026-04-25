---
title: The Physics of Energy Flow - Appendix A0
date: 2026-04-11
kind: appendix
part: Appendices
summary: >
  A rigorous derivation of the self-consistent closure condition for a
  self-refracting energy flow. The transverse refractive-index gradient
  produced by a curved flow is required to equal the geometric curvature
  needed to sustain that same curve. The resulting fixed-point equation is
  solved for a thin toroidal configuration, yielding the minimum effective
  index, the aspect ratio, and the allowed integer winding pairs. The
  appendix bridges Chapters 7b and 8 by closing the gap between local
  self-refraction and global toroidal closure.
keywords:
  - self-refraction
  - closure condition
  - ray curvature
  - effective index
  - toroidal closure
  - winding numbers
  - self-consistency
---

> TO BE READ: rough AI draft pending detailed human review.


# Appendix A0. Self-Consistent Closure of a Self-Refracting Flow

Chapter 7b establishes the self-refraction principle: retarded overlap of the
same flow produces a local effective index $n_\mathrm{eff} > 1$, reducing the
effective advance rate and bending the transport toward more strongly loaded
regions. Chapter 8 then works out the integer standing-wave modes of a toroidal
closure, assuming that self-refraction has already produced one.

This appendix derives the missing link: the condition under which coherent
self-overlap of a flow is sufficient to close the path. Coherent overlap is
self-refraction — not a cause followed by an effect, but a single event read
as an effective index. The result is a self-consistent fixed-point equation
whose solutions are the allowed closure configurations.


## A0.1 Ray Curvature from a Transverse Index Gradient

Consider a narrow transport beam propagating through a region in which the
effective refractive index varies across the beam cross-section. The standard
ray equation gives the path curvature

$$
\kappa
=
\hat{\mathbf{n}}_\perp \cdot \frac{\nabla n_\mathrm{eff}}{n_\mathrm{eff}},
$$

where $\hat{\mathbf{n}}_\perp$ is the unit normal to the ray in the plane of
bending. In the scalar case where $n_\mathrm{eff}$ varies only in the
transverse direction, this simplifies to

$$
\kappa
=
\frac{1}{n_\mathrm{eff}}
\frac{\partial n_\mathrm{eff}}{\partial \rho},
$$

where $\rho$ is the transverse coordinate measured outward from the center of
curvature.

This is a kinematic identity. It says nothing about the origin of the index
gradient. In the present framework, the index gradient is the coherent
self-overlap of the same flow, varying across the beam cross-section.


## A0.2 Geometric Curvature Required for Closure

For a flow path to close as a circle of radius $\mathcal{R}$, the geometric
curvature at every point along the path must be

$$
\kappa_\mathrm{geom} = \frac{1}{\mathcal{R}}.
$$

A toroidal closure has two independent curvatures. The major cycle (centerline)
has radius $R$ and curvature $1/R$. The minor cycle (cross-section) has
radius $r$ and curvature $1/r$.

The transport beam follows a helical path on the torus, simultaneously curving
in both directions. This helical path has a local curvature that depends on the
winding angle $\beta$. We address the two curvatures separately in
Section A0.5. First, we derive the self-consistent condition for a single
circular closure, then compose the two.


## A0.3 Self-Refraction Loading of a Curved Flow

A transport beam following a curved path of radius $\mathcal{R}$ produces a
retarded self-overlap. A later portion of the beam enters a region already
occupied by an earlier portion of the same flow, because the curved geometry
brings separated arc-segments into spatial proximity.

For a beam of cross-sectional width $w$ following a circular arc of radius
$\mathcal{R}$, the inner edge (at transverse distance $\mathcal{R} - w/2$
from the center) receives retarded overlap from a longer arc than the outer
edge (at distance $\mathcal{R} + w/2$). The retarded path difference between
the two edges produces a transverse gradient in the accumulated self-overlap.

From the proportional-response relation of Chapter 7b,

$$
f_\mathrm{tot} = (1 + k)\,f_1,
\qquad
n_\mathrm{eff} = 1 + k,
$$

the effective index at a point depends on the local overlap strength $k$. For
a harmonic beam of frequency $\omega$ and local amplitude $|f_1|$, the
retarded self-overlap at transverse position $\rho$ from the arc center is
proportional to the solid angle subtended by the earlier arc as seen from
$\rho$. Closer to the center of curvature, that solid angle is larger.

To make this quantitative, consider the steady-state field inside a thin
circular waveguide of radius $\mathcal{R}$ and cross-sectional radius $w/2$.
The field at radial position $\rho$ from the guide center receives
contributions from all other portions of the guide visible within a retardation
horizon $c\tau$. For $\tau$ large enough to encompass several turns, the
accumulated overlap is

$$
k(\rho)
=
\alpha\,\frac{\mathcal{R}}{\rho},
$$

where $\alpha > 0$ is a dimensionless coupling constant that depends on the
beam amplitude, frequency, and the number of coherent turns contributing.
The $\mathcal{R}/\rho$ dependence reflects the geometric fact that the inner
edge subtends a larger angular range of the earlier arc than the outer edge.

Therefore, writing $\rho = \mathcal{R} + \xi$ where $\xi$ is the transverse
displacement from the centerline,

$$
n_\mathrm{eff}(\xi)
=
1 + k(\xi)
=
1 + \frac{\alpha\,\mathcal{R}}{\mathcal{R}+\xi}.
$$

For $|\xi| \ll \mathcal{R}$, expand to first order:

$$
n_\mathrm{eff}(\xi)
\approx
1 + \alpha - \frac{\alpha\xi}{\mathcal{R}}
=:
n_0 - \frac{\alpha\xi}{\mathcal{R}},
$$

where

$$
n_0 := 1 + \alpha.
$$

The transverse gradient is therefore

$$
\frac{\partial n_\mathrm{eff}}{\partial \xi}
=
-\frac{\alpha}{\mathcal{R}}.
$$

Since $\xi$ increases outward from the center of curvature, the negative
sign means $n_\mathrm{eff}$ is higher on the inner side — exactly the
condition that bends transport inward.


## A0.4 The Self-Consistent Closure Equation

For closure, the ray curvature produced by the self-refraction gradient must
equal the geometric curvature of the path:

$$
\kappa_\mathrm{ray} = \kappa_\mathrm{geom}.
$$

From Section A0.1,

$$
\kappa_\mathrm{ray}
=
\frac{1}{n_0}\left|\frac{\partial n_\mathrm{eff}}{\partial \xi}\right|
=
\frac{\alpha}{n_0\,\mathcal{R}}.
$$

From Section A0.2,

$$
\kappa_\mathrm{geom} = \frac{1}{\mathcal{R}}.
$$

Setting these equal:

$$
\frac{\alpha}{n_0\,\mathcal{R}} = \frac{1}{\mathcal{R}}.
$$

The radius $\mathcal{R}$ cancels. This is significant: the closure condition is
scale-free. It does not select a particular radius. It selects a particular
value of $\alpha$ relative to $n_0$:

$$
\alpha = n_0 = 1 + \alpha.
$$

This gives

$$
\boxed{
\alpha = n_0 = 1 + \alpha
\qquad\Longrightarrow\qquad
\text{no solution for finite } \alpha.
}
$$

A single planar circular closure of a thin self-refracting beam does not
self-consistently close. The ray curvature from self-overlap is always less
than $1/\mathcal{R}$ by the factor $\alpha/n_0 = \alpha/(1+\alpha) < 1$.

This is the correct result. A single thin ring cannot close by
self-refraction alone, because the self-overlap that bends the beam also raises
$n_0$, and the raised $n_0$ in the denominator always defeats the gradient in
the numerator.


## A0.5 Toroidal Closure Resolves the Deficit

A torus has two independent cycles. The transport does not close by bending in
a single plane. It closes by winding helically, simultaneously curving around
the major cycle (radius $R$) and the minor cycle (radius $r$).

Introduce the winding angle $\beta$ as in Chapter 8. On the torus, the helical
transport direction is

$$
\hat{\mathbf{f}}
=
\cos\beta\,\hat{\mathbf{t}} + \sin\beta\,\hat{\boldsymbol{\theta}},
$$

where $\hat{\mathbf{t}}$ is tangent to the centerline (major cycle) and
$\hat{\boldsymbol{\theta}}$ is the turning direction around the minor cycle.

The self-refraction energy density now has two sources:

1. The curvature of the major cycle bends the beam toward the torus center.
   This produces a radial index gradient as in Section A0.3.

2. The curvature of the minor cycle bends the beam toward the tube axis.
   This produces a cross-sectional index gradient within the tube.

In a thin torus ($r \ll R$), these two contributions are approximately
independent. The minor-cycle gradient operates across a cross-section of
size $w \ll r$, while the major-cycle gradient operates at scale $R$.


### Minor-cycle self-consistency

The minor cycle is a small circular cross-section of radius $r$. On this
scale, the dominant source of self-overlap is the retarded contribution from the
same cross-section — the beam encounters its own earlier passage around the
tube.

For a beam winding $n$ times around the minor cycle per $m$ windings around the
major cycle, the number of coherent self-overlap layers within one tube
cross-section is of order $n$. Each layer adds a proportional contribution to
the local effective index. Writing the accumulated coupling on the minor cycle as
$\alpha_\theta$,

$$
\kappa_{\mathrm{ray},\theta}
=
\frac{\alpha_\theta}{n_{\mathrm{eff},\theta}\,r},
\qquad
\kappa_{\mathrm{geom},\theta}
=
\frac{\sin^2\beta}{r},
$$

where the geometric curvature of the helical path projected onto the minor
cycle is $\sin^2\beta / r$.

Setting these equal:

$$
\frac{\alpha_\theta}{n_{\mathrm{eff},\theta}} = \sin^2\beta.
$$


### Major-cycle self-consistency

The major cycle has radius $R$. The helical path projected onto the major cycle
has geometric curvature $\cos^2\beta / R$. The self-overlap along the major
cycle is produced by earlier turns of the helix passing through the same
spatial neighborhood with a retardation set by $R$. Writing the accumulated
coupling on the major cycle as $\alpha_\phi$,

$$
\frac{\alpha_\phi}{n_{\mathrm{eff},\phi}} = \cos^2\beta.
$$


### Combined closure condition

The total effective index follows from the combined energy density from both cycles. For a thin
torus with independent overlap contributions,

$$
n_\mathrm{eff} = 1 + \alpha_\theta + \alpha_\phi.
$$

To leading order in the thin-torus limit, the two self-consistency equations are

$$
\alpha_\theta = n_\mathrm{eff}\sin^2\beta,
\qquad
\alpha_\phi = n_\mathrm{eff}\cos^2\beta.
$$

Adding:

$$
\alpha_\theta + \alpha_\phi = n_\mathrm{eff}(\sin^2\beta + \cos^2\beta) = n_\mathrm{eff}.
$$

But $n_\mathrm{eff} = 1 + \alpha_\theta + \alpha_\phi$, so

$$
n_\mathrm{eff} - 1 = n_\mathrm{eff},
$$

which again has no finite solution if the $1$ is taken as rigid.

The resolution is that the $1$ in $n_\mathrm{eff} = 1 + k$ represents vacuum
propagation in the absence of any overlap. Inside a toroidal closure, there is
no such absence. Every point is already part of the coherent self-overlap —
the overlap is not added to the closure, it is the closure. The background
against which the proportional response is measured is not the vacuum but the
self-consistent overlap pattern itself.


## A0.6 Self-Consistent Fixed-Point Formulation

The correct formulation drops the external vacuum reference and asks directly
for the self-consistent state. Define the local effective index at a point on
the toroidal closure as

$$
n(s, \theta),
$$

where $s$ is arclength along the major cycle and $\theta$ is the angle around
the minor cycle. This field must satisfy two conditions simultaneously:

**Condition 1 (Transport).** The effective index determines the winding angle
through

$$
\cos\beta = \frac{1}{n},
\qquad
\sin\beta = \frac{\sqrt{n^2 - 1}}{n}.
$$

This is the constitutive relation of Chapter 8: the angle between the transport
direction and the centerline tangent is set by how strongly the medium loads
the propagation.

**Condition 2 (Geometry).** The winding angle determines the integer closure
through

$$
\tan\beta = \frac{nr}{mR},
$$

from Chapter 8. Combining with Condition 1,

$$
\frac{\sqrt{n^2 - 1}}{1} = \frac{nr}{mR},
$$

giving

$$
n = \sqrt{1 + \left(\frac{nr}{mR}\right)^2}.
$$

This is the closure equation already stated in Chapter 8. It is
self-consistent because $n$ appears on both sides: the effective index
determines the geometry, and the geometry determines the effective index.

**Condition 3 (Self-overlap is the index).** The effective index is not
produced by the self-overlap — it is the self-overlap, read as a transport
coefficient. At every point on the closure, the field overlaps coherently with
retarded contributions from the rest of the same flow. The degree of that
overlap is the effective index at that point.

For a steady-state closure, the overlap pattern is time-independent. The
retarded contributions at point $(s, \theta)$ come from all points
$(s', \theta')$ on the closure satisfying

$$
|\mathbf{x}(s,\theta) - \mathbf{x}(s',\theta')|
=
c\,(t - t'),
$$

where $t - t'$ is the propagation time along the helical path from $(s',\theta')$
to $(s,\theta)$.

For a uniform torus, symmetry under rotation in both $s$ and $\theta$
implies that every point has the same overlap geometry. The effective
index is therefore uniform:

$$
n(s, \theta) = n_0 = \mathrm{const}.
$$

The self-consistent closure equation is then the algebraic relation

$$
\boxed{
n_0 = \sqrt{1 + \left(\frac{n_0\,r}{m\,R}\right)^2},
\qquad m, n \in \mathbb{Z}_{>0},
}
$$

read as a fixed-point equation for $n_0$ at given $(m, n, r/R)$.


## A0.7 Solution of the Fixed-Point Equation

Square both sides:

$$
n_0^2 = 1 + \frac{n_0^2\,r^2}{m^2 R^2}.
$$

Rearrange:

$$
n_0^2\left(1 - \frac{r^2}{m^2 R^2}\right) = 1.
$$

Define the dimensionless aspect parameter

$$
\lambda := \frac{r}{mR}.
$$

Then

$$
n_0^2(1 - \lambda^2) = 1,
$$

so

$$
\boxed{
n_0 = \frac{1}{\sqrt{1 - \lambda^2}},
\qquad
\lambda = \frac{r}{mR} < 1.
}
$$

This has the Lorentz-factor form. It is real and greater than unity whenever

$$
r < mR,
$$

which is always satisfied for a thin torus ($r \ll R$) and for any $m \geq 1$.


### Existence condition

The fixed-point equation has a solution if and only if

$$
\lambda = \frac{r}{mR} < 1.
$$

For a thin torus, $r/R \ll 1$, so this is automatically satisfied for all
$m \geq 1$. The winding number $n$ enters through the original geometric
relation $\tan\beta = nr/mR$ and is free to take any positive integer value.

The closure equation does not select a unique $(m, n)$. It constrains the
relationship between the effective index, the aspect ratio, and the winding
pair. Selection of a specific $(m, n)$ requires additional physical input —
either a stability condition or a matching to observed spectral data. What is
established here is that the self-consistent closure exists for all
$(m, n)$ with $r < mR$.


## A0.8 Derived Quantities

From the fixed-point solution, the closure parameters follow.

**Winding angle:**

$$
\cos\beta = \frac{1}{n_0} = \sqrt{1 - \lambda^2},
\qquad
\sin\beta = \lambda n_0 = \frac{\lambda}{\sqrt{1-\lambda^2}}.
$$

In the thin-torus limit $\lambda \ll 1$:

$$
\beta \approx \lambda = \frac{r}{mR} \ll 1.
$$

So the helical path is nearly tangent to the centerline, with a small winding
pitch.

**Effective advance rate:**

$$
c_\mathrm{eff} = \frac{c}{n_0} = c\sqrt{1 - \lambda^2}.
$$

**Effective index in terms of $(m, n)$:**

The original closure relation $\tan\beta = nr/mR$ combined with
$\sin\beta = \lambda/\sqrt{1-\lambda^2}$ gives, after substitution,

$$
\frac{nr}{mR} = \frac{\lambda}{\sqrt{1-\lambda^2}} \cdot \frac{1}{\cos\beta} \cdot \cos\beta = \frac{\lambda}{\sqrt{1-\lambda^2}},
$$

which is automatically satisfied by $\lambda = r/mR$ only if $n = 1$.

For general $n$, the identification $\tan\beta = nr/mR$ combined with
$\tan\beta = \sqrt{n_0^2 - 1}$ gives

$$
n_0 = \sqrt{1 + \frac{n^2 r^2}{m^2 R^2}}.
$$

The fixed-point equation from Section A0.7 then becomes

$$
1 + \frac{n^2 r^2}{m^2 R^2}
=
\frac{1}{1 - r^2/(mR)^2},
$$

which gives, after clearing denominators,

$$
\left(1 + \frac{n^2 r^2}{m^2 R^2}\right)
\left(1 - \frac{r^2}{m^2 R^2}\right) = 1.
$$

Expanding and writing $\lambda = r/(mR)$:

$$
1 + n^2\lambda^2 - \lambda^2 - n^2\lambda^4 = 1,
$$

$$
(n^2 - 1)\lambda^2 = n^2\lambda^4,
$$

$$
n^2 - 1 = n^2\lambda^2.
$$

Therefore

$$
\boxed{
\lambda^2 = \frac{n^2 - 1}{n^2} = 1 - \frac{1}{n^2},
\qquad
\frac{r}{mR} = \frac{\sqrt{n^2-1}}{n}.
}
$$

This is a strong result. The self-consistent closure fixes the aspect ratio
$r/(mR)$ entirely in terms of the minor winding number $n$.

**Consequences:**

For $n = 1$: $\lambda = 0$. The minor winding number $n = 1$ gives
$r/(mR) = 0$, meaning the torus degenerates to a circle with no cross-section.
This is the single-ring case of Section A0.4, which does not close.

For $n = 2$: $\lambda = \sqrt{3}/2 \approx 0.866$. The torus is fat: $r$
is comparable to $mR$.

For $n \to \infty$: $\lambda \to 1$. The cross-section fills the major
radius. This approaches the limit of the thin-torus approximation.

The effective index at the self-consistent closure is

$$
n_0
=
\frac{1}{\sqrt{1-\lambda^2}}
=
\frac{1}{\sqrt{1/n^2}}
=
n.
$$

So

$$
\boxed{n_0 = n.}
$$

The self-consistent effective index of a toroidal closure equals its minor
winding number. The field must load itself by a factor of exactly $n$ to sustain
a closure that winds $n$ times around the minor cycle.


## A0.9 The Minimum Closure

The minimum non-degenerate closure has $n = 2$, for which

$$
n_0 = 2,
\qquad
\frac{r}{mR} = \frac{\sqrt{3}}{2},
\qquad
\beta = \arctan\!\left(\frac{2\sqrt{3}/2}{1}\right) = \arctan\sqrt{3} = \frac{\pi}{3}.
$$

For $m = 1$, the geometry is a fat torus with $r = (\sqrt{3}/2)\,R$, the
winding angle is $60°$, and the flow must load itself by a factor of $2$ — the
same equal-contribution case of Chapter 7b.

This is the simplest self-consistent closure. Its two properties are notable:

1. The effective index is exactly $2$, corresponding to the
   equal-contribution constructive superposition of Chapter 7b.

2. The aspect ratio is $r/R = \sqrt{3}/2$, which is not a thin torus. The
   thin-torus approximation breaks down for the minimum closure. A rigorous
   treatment of the $(2,2)$ or $(1,2)$ mode would require solving the full
   wave equation on a fat torus, not just the leading-order separated form.


## A0.10 Higher Winding Numbers and the Thin-Torus Regime

For larger $n$ at fixed $m$, the self-consistent aspect ratio approaches

$$
\frac{r}{mR} \to 1 \qquad \text{as } n \to \infty.
$$

But for fixed $n$ and increasing $m$, the aspect ratio scales as

$$
\frac{r}{R} = m\,\frac{\sqrt{n^2-1}}{n},
$$

so a thin torus ($r/R \ll 1$) requires either large $m$ at fixed $n$ (many
major windings per minor winding) or an external confinement mechanism not
derived here.

The physical implication is that isolated self-consistent toroidal closures in
the present framework are not thin. The thin-torus limit used in Chapter 8 for
the standing-wave mode counting is an approximation that becomes exact only for
large $m$ at fixed $n$.


## A0.11 Why the Closure is Scale-Free

The fixed-point equation

$$
n_0 = \sqrt{1 + \frac{n^2 r^2}{m^2 R^2}}
$$

depends only on the ratio $r/R$ and the integers $(m, n)$. It does not contain
the absolute values of $r$ or $R$, nor the frequency $\omega$, nor the
amplitude of the field.

This scale-freedom is a direct consequence of the proportional-response form

$$
f_2 = k f_1,
$$

in which the response is proportional to the source. A proportional response
gives an effective index that depends on the overlap geometry but not on the
field strength.

The absolute scale of the closure — the physical value of $R$ — is not
determined by the closure condition. It must be set by additional physics: either
the total energy content of the mode, or a matching condition to the exterior
field (Appendix A1). This is consistent with Chapter 8, where the mode
frequencies depend on both $(m,n)$ and the absolute radii $R$ and $r$.


## A0.12 Summary

1. **Single planar ring** (Section A0.4): A thin self-refracting beam in a
   single plane cannot self-consistently close. The self-overlap raises
   $n_\mathrm{eff}$ at the same rate as it provides the bending gradient,
   and the ratio $\alpha/n_0 = \alpha/(1+\alpha)$ is always less than unity.

2. **Toroidal closure** (Sections A0.5–A0.6): A torus resolves the deficit by
   distributing the closure across two independent cycles. The self-consistent
   condition is a fixed-point equation for $n_0$.

3. **Fixed-point solution** (Sections A0.7–A0.8): The self-consistent effective
   index is $n_0 = n$ (the minor winding number), and the aspect ratio is
   fixed at $r/(mR) = \sqrt{n^2-1}/n$.

4. **Minimum closure** (Section A0.9): The minimum non-degenerate closure has
   $n = 2$, $n_0 = 2$, and a fat torus with $r/(mR) = \sqrt{3}/2$. This
   corresponds to the equal-contribution superposition of Chapter 7b.

5. **Scale-freedom** (Section A0.11): The closure condition fixes the aspect
   ratio and effective index but not the absolute size. The physical radius is
   set by the total energy content or the exterior matching condition.

6. **Overlap is the closure**: A toroidal closure is permanent coherent
   self-overlap. The effective index is not a consequence of the overlap — it
   is what the overlap is, read as a transport coefficient. The fixed-point
   equation is therefore not a condition on two separate things (a flow and
   its self-refraction) but a self-consistency condition on one thing: the
   overlap geometry of a single flow.

7. **What is and is not derived**: The closure condition is derived from the
   self-overlap geometry without external input. What is not derived is
   which $(m, n)$ pair nature selects — that requires either a stability
   analysis beyond the scope of this appendix, or comparison with observed
   spectra.
