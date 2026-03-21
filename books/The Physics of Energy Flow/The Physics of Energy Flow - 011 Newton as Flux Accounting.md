---
title: The Physics of Energy Flow - Newton as Flux Accounting
date: 2026-03-19
---


# 11. Newton as Flux Accounting

Newton's second law is the integrated continuity law for momentum in a bounded
region of directed energy flow.

Chapter 3 gave the continuity equation for energy density $u$. In the present
language of directed transport, that same statement is

$$
\partial_t u + \nabla\cdot \mathbf{F} = 0,
$$

where $\mathbf{F}$ is the directed energy-flow density.

Because energy flow carries momentum, define the momentum density by

$$
\mathbf{p}=\frac{\mathbf{F}}{c^2}.
$$

To describe how momentum crosses boundaries, introduce the stress tensor
$\mathbf{T}$. This is the momentum-flux density of the same flow. Its
component $T_{ij}$ is the $i$-component of momentum transferred across a
surface whose normal points in the $j$ direction.

The local momentum continuity law is then

$$
\partial_t p_i - \partial_j T_{ij} = 0,
$$

or, in tensor form,

$$
\partial_t \mathbf{p} - \nabla\cdot\mathbf{T}=0.
$$

Momentum does not appear or disappear. It changes only by flux through the
boundary of a region.

Now choose a bounded region $\Omega$ containing a nearly stable localized
configuration. Define its total momentum and total energy:

$$
\mathbf{P}_\Omega
=
\int_\Omega \mathbf{p}\,dV
=
\frac{1}{c^2}\int_\Omega \mathbf{F}\,dV,
$$

$$
E_\Omega=\int_\Omega u\,dV.
$$

Integrating the local momentum continuity law gives

$$
\frac{d}{dt}\mathbf{P}_\Omega
=
\int_{\partial\Omega}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

The right-hand side is what later language calls force. It is the net rate at
which momentum is transferred across the boundary into the localized region.

To connect this with motion of the bounded mode as a whole, define its center
of energy:

$$
\mathbf{X}_\Omega
=
\frac{1}{E_\Omega}\int_\Omega \mathbf{x}\,u\,dV.
$$

When boundary leakage is small and the mode remains coherent,

$$
E_\Omega\,\dot{\mathbf{X}}_\Omega
\approx
\int_\Omega \mathbf{F}\,dV,
$$

so

$$
\mathbf{P}_\Omega
\approx
\frac{E_\Omega}{c^2}\dot{\mathbf{X}}_\Omega.
$$

If the total energy of the bounded configuration is roughly constant, define

$$
m_\Omega := \frac{E_\Omega}{c^2}.
$$

Then

$$
m_\Omega\,\ddot{\mathbf{X}}_\Omega
\approx
\int_{\partial\Omega}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

This is Newton's second law in effective form for a stable bounded mode:

$$
\mathbf{F}_{\mathrm{ext}}=\frac{d\mathbf{P}_\Omega}{dt}.
$$

So Newton's law is not an independent primitive. It is momentum bookkeeping for
a bounded region of energy flow.

When the same transport is written in conventional electromagnetic variables,
$\mathbf{F}$ becomes the Poynting vector and $\mathbf{T}$ becomes the Maxwell
stress tensor. But the logic does not depend on that representation. The
content is already present in the flow language itself.


## The charge force

The $(m,n)$ tangential circulation on a toroid generates, on each enclosing
sphere $S_r$, a distribution of normal organized flow. Denote this distribution
$f(r, \Omega)$ where $\Omega = (\theta, \phi)$ labels direction on the sphere.
Expand in spherical harmonics:

$$
f(r, \Omega) = \sum_{l=0}^{\infty} \sum_{m=-l}^{l} a_{lm}(r)\,Y_l^m(\Omega),
\qquad
a_{lm}(r) = \oint_{S_r} f(r,\Omega)\,Y_l^{m*}(\Omega)\,d\Omega.
$$

**Monopole ($l = 0$).** The $Y_0^0 = 1/\sqrt{4\pi}$ component is the angular
average of $f$:

$$
a_{00}(r) = \frac{1}{\sqrt{4\pi}}\oint f\,d\Omega = \frac{Q}{\sqrt{4\pi}\,r^2},
$$

where $Q = \oint_{S_r} f\,dA$ is the total flux through $S_r$. The organized
flow is source-free between shells: no flux is created or destroyed as $r$
grows. Therefore $Q$ is the same for every enclosing sphere. The monopole
field is

$$
f_0(r) = a_{00}\,Y_0^0 = \frac{Q}{4\pi r^2}.
$$

Isotropic, $1/r^2$, independent of the toroid's orientation.

**Dipole ($l = 1$).** The oriented through-hole flux contributes at the next
order:

$$
a_{1m}(r) = \oint f\,Y_1^{m*}\,d\Omega \sim \frac{\mu_m}{r^3},
$$

where $\mu_m$ are the components of the magnetic moment $\boldsymbol{\mu} =
\mu\hat{a}$ (axial through-hole flux, oriented along $\hat{a}$). Since
$\oint Y_1^m\,d\Omega = 0$, the dipole carries zero net flux through any
enclosing sphere:

$$
\oint f_1\,dA = 0.
$$

The push (outward flux in one hemisphere) exactly cancels the pull (inward
flux in the other). What orients the dipole — the axis $\hat{a}$ — integrates
out. The tension that remains after this cancellation is solely in the $l=0$
term: $\oint f_0\,dA = Q$.

**Higher multipoles** ($l \geq 2$) fall as $r^{-(l+2)}$. At large $r$ the
monopole dominates:

$$
f(r, \Omega) = \frac{Q}{4\pi r^2} + O\!\left(\tfrac{1}{r^3}\right).
$$

**Gauss's law.** The monopole is the only term whose integral over $S_r$
survives:

$$
\oint_{S_r} f\,dA = Q \qquad \text{for all } r.
$$

The charge $Q = \sigma\,Q_0$ is signed by handedness $\sigma = \pm 1$.

**Coulomb force.** Place toroid 1 at the origin (charge $Q_1$) and toroid 2
at separation $d$ large compared to the toroid size. Toroid 2 sits in the
monopole field $f_1(d) = Q_1 / (4\pi d^2)$ of toroid 1. The same Gauss
argument applies to toroid 2: its charge $Q_2$ is the total flux of its own
organized field through any enclosing surface. The force is the momentum flux
of the combined monopole fields:

$$
\boxed{F = \frac{Q_1 Q_2}{4\pi d^2}.}
$$

$Q_1 Q_2 > 0$ (same handedness): repulsive. $Q_1 Q_2 < 0$: attractive. This
is Coulomb's law — not postulated, but derived from the spherical harmonic
decomposition of the divergence-free $(m,n)$ field. The $1/r^2$ fall is the
area spreading of a conserved flux. The sign is the handedness of the
circulation.


## Two $1/r^2$ fields, two mechanisms

The charge force $F = Q_1 Q_2 / 4\pi d^2$ and the gravitational bending
$\theta = 4GM/bc^2$ (Chapter 12) both carry inverse-square dependence on
separation. The shape is identical. The mechanism is not.

**Gravity is scalar refractive loading.** The mass aggregate modifies the
local propagation constants $\varepsilon_\text{eff} = \varepsilon_0(1+2\eta)$,
$\mu_\text{eff} = \mu_0(1+2\eta)$. The refractive index $n = 1 + 2\eta$ is a
scalar field over space. A probe of any composition satisfies the ray equation

$$
\frac{d}{ds}\!\left(n\,\frac{d\mathbf{r}}{ds}\right) = \nabla n,
$$

giving transverse bending

$$
\Delta\theta = \int_{-\infty}^{\infty} \nabla_\perp n\,dz = \frac{4GM}{bc^2}.
$$

The probe's charge $Q$, handedness $\sigma$, or internal winding structure
never enter. Gravity bends all energy flow identically because it modifies the
vacuum itself, not the organized field of the probe.

**The Coulomb force is a stress-tensor interaction.** The monopole charge
field of toroid 1,

$$
\mathbf{f}_1(\mathbf{r}) = \frac{Q_1}{4\pi r^2}\,\hat{\mathbf{r}},
$$

carries a momentum-flux tensor

$$
T_{ij}(\mathbf{f}_1) = f_{1,i}\,f_{1,j} - \tfrac{1}{2}\delta_{ij}\,|\mathbf{f}_1|^2.
$$

The force on toroid 2 (charge $Q_2$, position $\mathbf{x}_2$) is the integral
of the total-field stress tensor over a surface $\partial\Omega_2$ enclosing
only toroid 2:

$$
F_i^{(2)} = \oint_{\partial\Omega_2} T_{ij}(\mathbf{f}_\text{tot})\,n_j\,dA.
$$

Decompose $T(\mathbf{f}_\text{tot}) = T(\mathbf{f}_1) + T(\mathbf{f}_2) +
T^\text{cross}$.

- $T(\mathbf{f}_1)$ is divergence-free in $\Omega_2$ (the source of
  $\mathbf{f}_1$ lies outside); by Gauss its surface integral over
  $\partial\Omega_2$ vanishes.
- $T(\mathbf{f}_2)$ is the self-stress of toroid 2; it integrates to zero by
  internal momentum conservation.

Only the cross term survives:

$$
T_{ij}^\text{cross} =
f_{1,i}\,f_{2,j} + f_{2,i}\,f_{1,j} - \delta_{ij}(\mathbf{f}_1\cdot\mathbf{f}_2).
$$

Since $\mathbf{f}_1$ is slowly varying over $\partial\Omega_2$ (toroid size
$\ll d$), it can be pulled outside the integral:

$$
F_i^{(2)}
=
\oint_{\partial\Omega_2} T_{ij}^\text{cross}\,n_j\,dA
\approx
[f_1]_i(\mathbf{x}_2)\oint_{\partial\Omega_2}\mathbf{f}_2\cdot\hat{\mathbf{n}}\,dA
=
[f_1]_i(\mathbf{x}_2)\cdot Q_2,
$$

where the last step uses Gauss's law for $\mathbf{f}_2$:
$\oint \mathbf{f}_2\cdot\hat{\mathbf{n}}\,dA = Q_2$.
Therefore

$$
\mathbf{F}^{(2)}
= Q_2\,\mathbf{f}_1(\mathbf{x}_2)
= \frac{Q_1 Q_2}{4\pi d^2}\,\hat{\mathbf{d}}.
$$

The sign of the force is $Q_1 Q_2 = \sigma_1\sigma_2 Q_0^2$: same handedness
repels, opposite handedness attracts. It is a vector coupling between two
organized fields, not a scalar loading of the vacuum.

**Why gravity cannot repel.** Since $\eta = GM/rc^2$ with $M = NE/c^2 > 0$,
the gradient $\nabla n$ always points inward. No property of the probe
can flip its sign.

**The ray bending integral.** Consider a ray traveling along $z$ with
impact parameter $b$, so $r^2 = b^2 + z^2$ to leading order. With
$n(r) = 1 + 2GM/rc^2$,

$$
\nabla n = -\frac{2GM}{c^2 r^2}\,\hat{\mathbf{r}}
= -\frac{2GM}{c^2}\,\frac{b\,\hat{\mathbf{b}} + z\,\hat{\mathbf{z}}}{(b^2+z^2)^{3/2}}.
$$

The transverse (perpendicular to $\hat{\mathbf{z}}$) component governs the
bending. Since $n \approx 1$ in the weak-field limit, the ray equation
$d(n\,d\mathbf{r}/ds)/ds = \nabla n$ gives

$$
\frac{d\alpha}{dz} \approx (\nabla n)_\perp
= -\frac{2GM\,b}{c^2\,(b^2+z^2)^{3/2}}.
$$

Integrating along the unperturbed ray:

$$
\Delta\alpha
= \int_{-\infty}^{\infty} (\nabla n)_\perp\,dz
= -\frac{2GM\,b}{c^2}
  \int_{-\infty}^{\infty} \frac{dz}{(b^2+z^2)^{3/2}}.
$$

The integral evaluates by the substitution $z = b\tan\varphi$:

$$
\int_{-\infty}^{\infty}\frac{dz}{(b^2+z^2)^{3/2}}
= \frac{1}{b^2}\int_{-\pi/2}^{\pi/2}\cos\varphi\,d\varphi
= \frac{2}{b^2}.
$$

Therefore

$$
\Delta\alpha = -\frac{4GM}{c^2 b}\,\hat{\mathbf{b}},
$$

directed toward the mass. The probe's charge, handedness, and internal
winding structure are absent from every line of this calculation.


## Summary

Particles are localized regions. Forces are boundary momentum fluxes.
Newton's second law is continuity applied to a stable knot of energy flow.
The Coulomb force is the stress-tensor cross-coupling of two organized charge
fields — a vector interaction whose sign is set by relative handedness.
Gravity is a scalar refractive loading of the vacuum — probe-independent and
always attractive. Both produce $1/r^2$ fields. The mechanisms are distinct.
