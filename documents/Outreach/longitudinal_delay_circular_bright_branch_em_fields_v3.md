---
title: "Longitudinal Delay of an Isolated Circular Bright Interference Branch"
subtitle: "A time-of-flight test of loaded raw-overlap transport in circular optical interference"
author: "An M. Rodriguez"
date: "2026-04-21"
one-sentence-summary: "This proposal tests whether an isolated bright region of a circular interference pattern propagates at the ordinary reference speed or at a reduced speed set by its higher coherent energy density."
summary: "Two coherent laser beams are recombined to produce circular fringes. Standard electromagnetic superposition gives bright regions where the electric and magnetic fields add and dark regions where they cancel, while the full pattern conserves the two-beam energy budget. The experiment isolates a bright circular region or annular ring and measures its modulation delay against a reference beam over the same longitudinal distance. Ordinary output transport predicts no delay difference. The loaded raw-overlap hypothesis predicts that if the bright region carries the conserved two-beam flux on a higher local energy density, its effective longitudinal advance is reduced according to v_eff = J/u. For equal local beam densities at a bright maximum on axis, the predicted speed is c/2."
keywords:
  - interference
  - circular fringes
  - Mach-Zehnder interferometer
  - Michelson interferometer
  - energy density
  - Poynting vector
  - coherent loading
  - dielectric analogy
  - speed of light
  - time-of-flight
---

# Longitudinal Delay of an Isolated Circular Bright Interference Branch

## Abstract

This proposal tests whether a spatially isolated bright region of a circular
interference pattern propagates with the same delay as an ordinary reference
beam, or whether its effective longitudinal advance is reduced by coherent
loading.

Two coherent laser beams are recombined so that their wavefronts produce
fringes. Standard interference gives a spatial redistribution of energy density:
bright rings exceed the two-beam mean while neighboring dark rings fall below
it, with the full pattern conserving the two-beam energy budget. The experiment
isolates a circular bright region, or a narrow annular bright ring, and measures
its modulation delay over a known longitudinal distance against a reference
beam.

The standard expectation is that the selected bright region and the reference
beam have the same propagation speed. The loaded-branch expectation is different
(in analogy with dielectrics): if the selected bright region carries the
available two-beam flux on a higher local energy density, then its effective
longitudinal advance must be slower. For equal local beam densities at a bright
maximum, the predicted speed is one half of the local available longitudinal
transport speed.

The experiment is therefore a direct time-of-flight test between ordinary output
transport and loaded raw-overlap transport.

---

# 1. Goal

Measure the longitudinal delay of an isolated bright region in a real circular
interference pattern.

The experimental question is:

$$
\boxed{
\text{Does an isolated circular bright region propagate like ordinary output light, or like a loaded raw-overlap branch?}
}
$$

The standard expectation is

$$
v_{\mathrm{bright}}=v_{\mathrm{ref}}
$$

within experimental error.

The loaded-branch expectation is

$$
v_{\mathrm{bright}}<v_{\mathrm{ref}}.
$$

For equal local beam densities at a bright maximum and equal local longitudinal
transport factors, the predicted result is

$$
v_{\mathrm{bright}}=\frac{v_{\mathrm{local}}}{2}.
$$

On the optical axis of two coaxial beams, where the local longitudinal transport
speed is $c$, this becomes

$$
v_{\mathrm{bright}}=\frac c2.
$$

---

# 2. Core Idea

Two coherent laser beams can overlap in phase. At a bright fringe, by the
superposition principle, their electric and magnetic field amplitudes add. Since
the electromagnetic energy density is quadratic in the fields, the raw local
energy density at an equal-beam bright maximum is four times the single-beam
energy density.

The recombined two-beam flux budget is the conserved flux of the two input
beams. After recombination, the full interference pattern conserves energy by
distributing density into bright and dark regions: a bright fringe in one
output corresponds symmetrically to a dark fringe in the other output.

The proposal applies the same standard electromagnetic loading logic used in
dielectric propagation to the case of two coherent beams fully overlapping in
vacuum. The beam splitter only prepares the geometry, direction, and relative
phase. At overlap, each beam is treated as a propagating electromagnetic field
that acts as the coherent response seen by the other. Under that reading, the
overlap is a loaded branch: the conserved two-beam longitudinal flux is carried
on a higher local energy density, so the effective longitudinal transport speed
follows from

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

At an equal-beam bright maximum on the optical axis,

$$
J=2u_0c,
\qquad
u=4u_0.
$$

Therefore

$$
v_{\mathrm{eff}}=\frac{2u_0c}{4u_0}=\frac c2.
$$

The prediction is large and directly falsifiable.

---

# 3. Beams and Coordinate Setup

Let the transverse coordinates on a plane normal to the nominal optical axis be

$$
(x,y),
$$

and define the radial coordinate

$$
\rho=\sqrt{x^2+y^2}.
$$

Circular fringes are described by a radial phase difference

$$
\Delta\phi(\rho),
$$

and radial single-beam energy-density profiles

$$
u_1(\rho),
\qquad
u_2(\rho).
$$

No plane-wave approximation is required. No small-angle approximation is
required. The formulas below may be evaluated using the measured beam profiles
and measured phase difference.

Two planes are distinguished throughout the proposal. Sections 4--9 describe
the **overlap plane**, where the two returned fields are written as
$\mathbf E_1,\mathbf B_1$ and $\mathbf E_2,\mathbf B_2$ before assigning the
selected bright region to a transport law. Section 10 describes the
**beam-splitter output plane**, where the same two returned fields are resolved
into the ordinary lossless output combinations $(+)$ and $(-)$. The loaded
branch law is applied to the raw overlap reading; the ordinary-output section is
included as the standard comparison.

---

# 4. Beams Interference

This section derives the local interference energy density using ordinary
electric and magnetic fields, not a scalar shortcut.

Let the two coherent electromagnetic fields on the observation plane be

$$
\mathbf E_1(\rho,t),
\qquad
\mathbf B_1(\rho,t),
$$

and

$$
\mathbf E_2(\rho,t),
\qquad
\mathbf B_2(\rho,t).
$$

In a source-free linear region, Maxwell's equations allow superposition:

$$
\mathbf E_{\mathrm{raw}}=\mathbf E_1+\mathbf E_2,
\qquad
\mathbf B_{\mathrm{raw}}=\mathbf B_1+\mathbf B_2.
$$

The electromagnetic energy density is

$$
u_{\mathrm{raw}}
=
\frac{\varepsilon_0}{2}
|\mathbf E_{\mathrm{raw}}|^2
+
\frac{1}{2\mu_0}
|\mathbf B_{\mathrm{raw}}|^2.
$$

Substituting the superposed fields gives

$$
u_{\mathrm{raw}}
=
\frac{\varepsilon_0}{2}
|\mathbf E_1+\mathbf E_2|^2
+
\frac{1}{2\mu_0}
|\mathbf B_1+\mathbf B_2|^2.
$$

Expand both quadratic terms:

$$
|\mathbf E_1+\mathbf E_2|^2
=
|\mathbf E_1|^2+|\mathbf E_2|^2
+
2\mathbf E_1\cdot\mathbf E_2,
$$

and

$$
|\mathbf B_1+\mathbf B_2|^2
=
|\mathbf B_1|^2+|\mathbf B_2|^2
+
2\mathbf B_1\cdot\mathbf B_2.
$$

Therefore

$$
u_{\mathrm{raw}}
=
u_1+u_2
+
\varepsilon_0\mathbf E_1\cdot\mathbf E_2
+
\frac{1}{\mu_0}\mathbf B_1\cdot\mathbf B_2,
$$

where

$$
u_i
=
\frac{\varepsilon_0}{2}|\mathbf E_i|^2
+
\frac{1}{2\mu_0}|\mathbf B_i|^2.
$$

For two locally co-polarized coherent beams with the same frequency, the dot
products carry the relative phase. Write the local field amplitudes as

$$
\mathbf E_i(\rho,t)
=
\mathrm{Re}\!\left[
\widetilde{\mathbf E}_i(\rho)e^{-i\omega t}
\right],
$$

and

$$
\mathbf B_i(\rho,t)
=
\mathrm{Re}\!\left[
\widetilde{\mathbf B}_i(\rho)e^{-i\omega t}
\right].
$$

The time-averaged energy density is

$$
\langle u_{\mathrm{raw}}\rangle_t
=
\frac{\varepsilon_0}{4}
|\widetilde{\mathbf E}_1+\widetilde{\mathbf E}_2|^2
+
\frac{1}{4\mu_0}
|\widetilde{\mathbf B}_1+\widetilde{\mathbf B}_2|^2.
$$

For each individual beam,

$$
u_i
=
\frac{\varepsilon_0}{4}
|\widetilde{\mathbf E}_i|^2
+
\frac{1}{4\mu_0}
|\widetilde{\mathbf B}_i|^2.
$$

For a local null electromagnetic beam,

$$
|\widetilde{\mathbf B}_i|
=
\frac{|\widetilde{\mathbf E}_i|}{c},
$$

and the electric and magnetic contributions to the energy density are equal.
Thus

$$
u_i
=
\frac{\varepsilon_0}{2}
|\widetilde{\mathbf E}_i|^2
=
\frac{1}{2\mu_0}
|\widetilde{\mathbf B}_i|^2.
$$

Assume the two local fields have the same polarization and the same local
transport orientation, so the electric fields are parallel to one another and
the magnetic fields are parallel to one another. Let the relative phase be

$$
\Delta\phi(\rho)=\phi_1(\rho)-\phi_2(\rho).
$$

Then

$$
\widetilde{\mathbf E}_1\cdot\widetilde{\mathbf E}_2^*
=
|\widetilde{\mathbf E}_1|
|\widetilde{\mathbf E}_2|
e^{i\Delta\phi},
$$

and similarly for the magnetic fields. The time-averaged interference term is
the real part of this product, so it is proportional to

$$
\cos\Delta\phi(\rho).
$$

Therefore the exact local interference density for co-polarized coherent beams
is

$$
\boxed{
u_{\mathrm{raw}}(\rho)
=
u_1(\rho)+u_2(\rho)
+
2\sqrt{u_1(\rho)u_2(\rho)}
\cos\Delta\phi(\rho).
}
$$

This is the electromagnetic interference identity in energy-density form.

At a bright radius $\rho_b$,

$$
\Delta\phi(\rho_b)=2\pi N,
\qquad
N\in\mathbb Z,
$$

so

$$
\cos\Delta\phi(\rho_b)=1.
$$

Thus

$$
u_{\mathrm{raw}}(\rho_b)
=
\left(
\sqrt{u_1(\rho_b)}
+
\sqrt{u_2(\rho_b)}
\right)^2.
$$

If the local densities are equal,

$$
u_1(\rho_b)=u_2(\rho_b)=u_0(\rho_b),
$$

then

$$
\boxed{
u_{\mathrm{raw}}(\rho_b)=4u_0(\rho_b).
}
$$

At a dark radius $\rho_d$,

$$
\Delta\phi(\rho_d)=(2N+1)\pi,
$$

so

$$
\cos\Delta\phi(\rho_d)=-1.
$$

Thus

$$
u_{\mathrm{raw}}(\rho_d)
=
\left(
\sqrt{u_1(\rho_d)}
-
\sqrt{u_2(\rho_d)}
\right)^2.
$$

If the local densities are equal there,

$$
u_{\mathrm{raw}}(\rho_d)=0.
$$

This derivation uses only Maxwell superposition and the standard quadratic
electromagnetic energy density.

---

# 5. Exact Circular-Fringe Geometry from Real Wavefronts

Circular fringes occur when the phase difference is radial:

$$
\Delta\phi(x,y)=\Delta\phi(\rho).
$$

This may arise from two coherent beams with different wavefront curvatures,
from a Michelson-type circular-fringe geometry, or from any optical arrangement
where the measured phase difference is radial.

The analysis does not require a specific model of the laser beams. However, to
write one exact circular geometry explicitly, model each beam locally by a
spherical wavefront emitted from an effective coherent point on the optical
axis.

Let the effective origins be at axial positions $z=z_1$ and $z=z_2$, and let
the observation plane be $z=Z$. Define exact path lengths

$$
R_1(\rho)=\sqrt{\rho^2+(Z-z_1)^2},
$$

and

$$
R_2(\rho)=\sqrt{\rho^2+(Z-z_2)^2}.
$$

The phase difference is

$$
\boxed{
\Delta\phi(\rho)
=
k\left[R_1(\rho)-R_2(\rho)\right]-\phi_0.
}
$$

Bright rings satisfy

$$
\Delta\phi(\rho_b)=2\pi N,
$$

that is,

$$
k\left[R_1(\rho_b)-R_2(\rho_b)\right]-\phi_0=2\pi N.
$$

Dark rings satisfy

$$
\Delta\phi(\rho_d)=(2N+1)\pi.
$$

No plane-wave approximation is used. The square roots are retained exactly.

For real beams that are not exactly spherical, the same equations hold with the
measured phase functions $\phi_1(\rho)$ and $\phi_2(\rho)$. The experiment only
needs the actual radial phase difference and local densities.

---

# 6. Exact Area-Averaged Density for a Selected Circular Region

A detector or aperture samples a finite region, not a mathematical point.

Let $\Omega$ be the selected aperture region in the observation plane. For a
circular central bright spot,

$$
\Omega=\{(x,y):0\le \rho\le a\}.
$$

For a bright annular ring centered at radius $\rho_b$ with half-width $w/2$,

$$
\Omega=\{(x,y):\rho_b-w/2\le \rho\le \rho_b+w/2\}.
$$

The aperture area is

$$
A_\Omega=\int_\Omega dA.
$$

Because

$$
dA=\rho\,d\rho\,d\varphi,
$$

a radial aperture gives

$$
A_\Omega=2\pi\int_{\rho_-}^{\rho_+}\rho\,d\rho
=
\pi(\rho_+^2-\rho_-^2),
$$

where

$$
\rho_- \le \rho \le \rho_+.
$$

The exact aperture-averaged raw density is

$$
\boxed{
\bar u_{\mathrm{raw}}(\Omega)
=
\frac{1}{A_\Omega}
\int_\Omega u_{\mathrm{raw}}(\rho)\,dA.
}
$$

Using radial symmetry,

$$
\boxed{
\bar u_{\mathrm{raw}}(\Omega)
=
\frac{2\pi}{A_\Omega}
\int_{\rho_-}^{\rho_+}
\left[
u_1(\rho)+u_2(\rho)
+
2\sqrt{u_1(\rho)u_2(\rho)}
\cos\Delta\phi(\rho)
\right]
\rho\,d\rho.
}
$$

This expression is exact for the measured circular fringe pattern.

No small-angle approximation is used. No plane-wave approximation is used. No
constant-density approximation is used.

---

# 7. Input-Branch Longitudinal Flux Budget for the Loaded-Branch Test

This section defines the flux used by the tested loaded-branch law. It is not
claimed to be the full standard post-overlap Poynting flux of the superposed
field through the aperture.

In standard electromagnetism, the Poynting vector of the raw superposed field is

$$
\mathbf S_{\mathrm{raw}}
=
\frac{1}{\mu_0}
(\mathbf E_1+\mathbf E_2)\times(\mathbf B_1+\mathbf B_2).
$$

Expanding,

$$
\mathbf S_{\mathrm{raw}}
=
\mathbf S_1+\mathbf S_2
+
\frac{1}{\mu_0}
\left(
\mathbf E_1\times\mathbf B_2
+
\mathbf E_2\times\mathbf B_1
\right),
$$

where

$$
\mathbf S_i=\frac{1}{\mu_0}\mathbf E_i\times\mathbf B_i.
$$

Thus the standard post-overlap Poynting flux contains interference cross terms.
Those cross terms are part of the ordinary-output reading discussed in Section
10.

The loaded-branch test uses a different bookkeeping quantity: the conserved
two-input longitudinal flux assigned to the selected branch. Define the
individual input-branch longitudinal flux densities as

$$
J_{1z}(\rho),
\qquad
J_{2z}(\rho).
$$

They are obtained from each beam separately, before forming the raw overlap
Poynting vector. For time-harmonic fields,

$$
\langle\mathbf S_i\rangle_t
=
\frac{1}{2\mu_0}
\mathrm{Re}
\left(
\widetilde{\mathbf E}_i\times\widetilde{\mathbf B}_i^*
\right),
$$

and

$$
J_{iz}(\rho)
=
\langle\mathbf S_i(\rho)\rangle_t\cdot\hat{\mathbf z}.
$$

For local freely propagating transport,

$$
J_{iz}(\rho)=u_i(\rho)c\cos\alpha_i(\rho),
$$

where $\alpha_i(\rho)$ is the local angle between beam $i$'s energy-flow
direction and the $z$-axis.

For exact spherical wavefronts,

$$
\cos\alpha_i(\rho)
=
\frac{Z-z_i}{R_i(\rho)}.
$$

Thus

$$
J_{iz}(\rho)
=
u_i(\rho)c\frac{Z-z_i}{R_i(\rho)}.
$$

The conserved two-input longitudinal flux assigned to aperture $\Omega$ is

$$
\boxed{
\Phi_{\mathrm{in},z}(\Omega)
=
\int_\Omega
\left[
J_{1z}(\rho)+J_{2z}(\rho)
\right]dA.
}
$$

For a radial aperture,

$$
\boxed{
\Phi_{\mathrm{in},z}(\Omega)
=
2\pi\int_{\rho_-}^{\rho_+}
\left[
J_{1z}(\rho)+J_{2z}(\rho)
\right]\rho\,d\rho.
}
$$

This is the flux budget used in the loaded raw-overlap law

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

The ordinary-output comparison instead uses the full lossless output-mode
decomposition of Section 10.

---

# 8. Loaded-Branch Prediction for a Circular Aperture

The loaded-branch law is

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

For a finite aperture, the corresponding area-integrated loaded-branch prediction is

$$
\boxed{
v_{\Omega}
=
\frac{\Phi_{\mathrm{in},z}(\Omega)}
{
\int_\Omega u_{\mathrm{raw}}(\rho)\,dA
}.
}
$$

Using the formulas above,

$$
\boxed{
v_{\Omega}
=
\frac{
2\pi\int_{\rho_-}^{\rho_+}
\left[
J_{1z}(\rho)+J_{2z}(\rho)
\right]\rho\,d\rho
}
{
2\pi\int_{\rho_-}^{\rho_+}
\left[
u_1(\rho)+u_2(\rho)
+
2\sqrt{u_1(\rho)u_2(\rho)}
\cos\Delta\phi(\rho)
\right]\rho\,d\rho
}.
}
$$

The factor $2\pi$ cancels:

$$
\boxed{
v_{\Omega}
=
\frac{
\int_{\rho_-}^{\rho_+}
\left[
J_{1z}(\rho)+J_{2z}(\rho)
\right]\rho\,d\rho
}
{
\int_{\rho_-}^{\rho_+}
\left[
u_1(\rho)+u_2(\rho)
+
2\sqrt{u_1(\rho)u_2(\rho)}
\cos\Delta\phi(\rho)
\right]\rho\,d\rho
}.
}
$$

This is the circular-fringe loaded-branch prediction using the conserved two-input flux budget.

It is written entirely in terms of measurable beam quantities:

$$
u_1(\rho),\quad u_2(\rho),\quad \Delta\phi(\rho),\quad J_{1z}(\rho),\quad J_{2z}(\rho).
$$

---

# 9. Local Bright-Maximum Limit

At a bright radius $\rho_b$,

$$
\cos\Delta\phi(\rho_b)=1.
$$

The local raw density is

$$
u_{\mathrm{raw}}(\rho_b)
=
\left[
\sqrt{u_1(\rho_b)}
+
\sqrt{u_2(\rho_b)}
\right]^2.
$$

The local available longitudinal flux is

$$
J_z(\rho_b)
=
J_{1z}(\rho_b)+J_{2z}(\rho_b).
$$

The local loaded-branch speed is therefore

$$
\boxed{
v_{\mathrm{bright}}(\rho_b)
=
\frac{
J_{1z}(\rho_b)+J_{2z}(\rho_b)
}
{
\left[
\sqrt{u_1(\rho_b)}
+
\sqrt{u_2(\rho_b)}
\right]^2
}.
}
$$

If the two local densities are equal,

$$
u_1(\rho_b)=u_2(\rho_b)=u_0(\rho_b),
$$

then

$$
u_{\mathrm{raw}}(\rho_b)=4u_0(\rho_b).
$$

If the two local longitudinal transport factors are equal,

$$
J_{1z}(\rho_b)=u_0(\rho_b)c_z(\rho_b),
$$

and

$$
J_{2z}(\rho_b)=u_0(\rho_b)c_z(\rho_b),
$$

then

$$
J_z(\rho_b)=2u_0(\rho_b)c_z(\rho_b).
$$

Therefore

$$
v_{\mathrm{bright}}(\rho_b)
=
\frac{2u_0(\rho_b)c_z(\rho_b)}
{4u_0(\rho_b)}
=
\frac{c_z(\rho_b)}{2}.
$$

Thus

$$
\boxed{
v_{\mathrm{bright}}(\rho_b)=\frac{c_z(\rho_b)}{2}.
}
$$

On the optical axis of coaxial beams,

$$
c_z(0)=c,
$$

so

$$
\boxed{
v_{\mathrm{bright}}(0)=\frac c2.
}
$$

For an off-axis ring in an exact spherical-wave geometry,

$$
c_z(\rho_b)
=
c\frac{Z-z_i}{R_i(\rho_b)}
$$

when the two beams have equal local transport factors. Hence the exact off-axis
prediction is

$$
\boxed{
v_{\mathrm{bright}}(\rho_b)
=
\frac c2
\frac{Z-z_i}{R_i(\rho_b)}
}
$$

in the equal-symmetric case.

If the two beams have different local longitudinal factors, the exact
equal-density formula is instead

$$
\boxed{
v_{\mathrm{bright}}(\rho_b)
=
\frac c4
\left[
\cos\alpha_1(\rho_b)+\cos\alpha_2(\rho_b)
\right].
}
$$

No approximation is involved in this expression.

---

# 10. Ordinary Output Transport

At a lossless 50/50 recombiner, the output fields are

$$
\mathbf E_+
=
\frac{\mathbf E_1+\mathbf E_2}{\sqrt2},
\qquad
\mathbf B_+
=
\frac{\mathbf B_1+\mathbf B_2}{\sqrt2},
$$

and

$$
\mathbf E_-
=
\frac{\mathbf E_1-\mathbf E_2}{\sqrt2},
\qquad
\mathbf B_-
=
\frac{\mathbf B_1-\mathbf B_2}{\sqrt2}.
$$

The factor $1/\sqrt2$ is the lossless beam-splitter amplitude factor. It
ensures that the total output energy equals the total input energy.

The output energy densities are

$$
u_+
=
\frac12
\left[
u_1+u_2
+
2\sqrt{u_1u_2}\cos\Delta\phi
\right],
$$

and

$$
u_-
=
\frac12
\left[
u_1+u_2
-
2\sqrt{u_1u_2}\cos\Delta\phi
\right].
$$

Therefore

$$
\boxed{
u_+(\rho)+u_-(\rho)=u_1(\rho)+u_2(\rho).
}
$$

At an equal-beam bright maximum,

$$
u_+=2u_0,
\qquad
u_-=0.
$$

Thus ordinary output transport assigns energy density $2u_0$ to the bright
output, not $4u_0$.

It therefore predicts no $c/2$ delay.

---

# 11. Theoretical Fork

Both readings conserve energy.

The disagreement is not about energy conservation. It is about how a selected
bright region transports energy.

## 11.1 Ordinary Output Transport

The recombiner output densities satisfy

$$
u_+(\rho)+u_-(\rho)=u_1(\rho)+u_2(\rho).
$$

At an equal-beam bright maximum,

$$
u_+=2u_0.
$$

No reduced speed is required.

## 11.2 Loaded Raw-Overlap Transport

The selected bright region is identified with the raw overlap density:

$$
u_{\mathrm{raw}}
=
\frac{\varepsilon_0}{2}
|\mathbf E_1+\mathbf E_2|^2
+
\frac{1}{2\mu_0}
|\mathbf B_1+\mathbf B_2|^2.
$$

At an equal-beam bright maximum,

$$
u_{\mathrm{raw}}=4u_0.
$$

The conserved two-beam flux assigned to the selected region is

$$
J=2u_0c_z.
$$

Therefore

$$
v_{\mathrm{bright}}
=
\frac{J}{u_{\mathrm{raw}}}
=
\frac{2u_0c_z}{4u_0}
=
\frac{c_z}{2}.
$$

The experiment tests which reading describes the propagation of an isolated
circular bright region.

---

# 12. Dielectric-Style Derivation of the Loaded-Branch Law

Standard dielectric slowing is the template used here. In dielectric
propagation, electromagnetic transport is slowed by field interaction with a
response field carried by matter. The fringe-delay test applies that same
electromagnetic loading logic to the simplest unbound case: two coherent light
fields fully overlapping in vacuum.

The beam splitter itself is not the loading mechanism. It only prepares the
returned beams with the required direction and relative phase. At recombination,
the two beams are treated strictly as propagating electric and magnetic fields.
Under that reading, each beam acts as the coherent response field seen by the
other. If that overlap is carried as a single loaded branch, the slowdown
follows from the same dielectric-style transport rule.

## 12.1 Ordinary Dielectric Form

In a dielectric,

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P.
$$

For a linear response,

$$
\mathbf P=\varepsilon_0\chi_e\mathbf E.
$$

Therefore

$$
\mathbf D
=
\varepsilon_0(1+\chi_e)\mathbf E
=
\varepsilon_{\mathrm{eff}}\mathbf E.
$$

Thus

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+\chi_e).
$$

If the magnetic sector is similarly loaded,

$$
\mu_{\mathrm{eff}}=\mu_0(1+\chi_m),
$$

then

$$
v
=
\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}.
$$

For symmetric electric and magnetic loading,

$$
\chi_e=\chi_m=k,
$$

so

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+k),
\qquad
\mu_{\mathrm{eff}}=\mu_0(1+k).
$$

Then

$$
v
=
\frac{1}
{\sqrt{\varepsilon_0\mu_0(1+k)^2}}
=
\frac{c}{1+k}.
$$

Thus

$$
\boxed{
v_{\mathrm{eff}}=\frac{c}{1+k}.
}
$$

## 12.2 Mutual Coherent Response Fields

Let one beam have electric field amplitude

$$
E_1.
$$

Let the coherent response field supplied by the other beam be proportional:

$$
E_2=kE_1,
\qquad
k\ge0.
$$

Then

$$
E_{\mathrm{tot}}
=
E_1+E_2
=
(1+k)E_1.
$$

Because the density readout is quadratic,

$$
u\propto E^2.
$$

Therefore

$$
u_{\mathrm{tot}}
\propto
E_{\mathrm{tot}}^2
=
(1+k)^2E_1^2.
$$

If

$$
u_1\propto E_1^2,
$$

then

$$
\boxed{
u_{\mathrm{tot}}=(1+k)^2u_1.
}
$$

For equal coherent contribution,

$$
k=1,
$$

so

$$
E_{\mathrm{tot}}=2E_1,
$$

and

$$
u_{\mathrm{tot}}=4u_1.
$$

The corresponding amplitude-loading factor is

$$
n_{\mathrm{eff}}=1+k.
$$

Therefore

$$
u_{\mathrm{tot}}=n_{\mathrm{eff}}^2u_1,
$$

and

$$
v_{\mathrm{eff}}=\frac{c}{n_{\mathrm{eff}}}.
$$

For $k=1$,

$$
n_{\mathrm{eff}}=2,
$$

so

$$
\boxed{
v_{\mathrm{eff}}=\frac c2.
}
$$

## 12.3 Flux Form

The same law is

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

For one branch,

$$
J_1=u_1c.
$$

For two equal branches in phase, the conserved available flux is

$$
J_{\mathrm{available}}=2u_1c,
$$

which is the same two-branch flux present before recombination.

The joined raw density is

$$
u_{\mathrm{joined}}=4u_1.
$$

Therefore

$$
v_{\mathrm{eff}}
=
\frac{J_{\mathrm{available}}}{u_{\mathrm{joined}}}
=
\frac{2u_1c}{4u_1}
=
\frac c2.
$$

The general proportional-response result is

$$
f_2=kf_1,
$$

so

$$
f_{\mathrm{tot}}=(1+k)f_1,
$$

$$
u_{\mathrm{tot}}=(1+k)^2u_1,
$$

and

$$
\boxed{
v_{\mathrm{eff}}=\frac{c}{1+k}.
}
$$

---

# 13. Experimental Design

## 13.1 Apparatus

Minimum requirements:

- stable coherent laser source,
- amplitude modulation source,
- Michelson, Mach-Zehnder, or equivalent circular-fringe interferometer,
- controlled wavefront curvature or axial path geometry producing circular fringes,
- stable circular fringe pattern,
- circular aperture or annular slit selecting one bright region,
- reference beam path,
- equal downstream propagation length $L$ for reference and selected bright region,
- fast photodiodes,
- oscilloscope, lock-in amplifier, or phase-delay measurement system,
- variable path length or multiple known path lengths.

## 13.2 Procedure

1. Generate a coherent laser beam.
2. Apply sinusoidal amplitude modulation at angular frequency $\Omega$.
3. Split the beam into two equal arms.
4. Recombine the beams in a circular-fringe geometry.
5. Record the individual beam profiles $u_1(\rho)$ and $u_2(\rho)$ by blocking the other beam in turn.
6. Record the circular interference pattern to determine $\Delta\phi(\rho)$ or directly identify bright and dark radii.
7. Select a bright central spot or narrow bright annulus using a circular aperture or annular slit.
8. Let the selected bright region propagate over known distance $L$.
9. In parallel, propagate a reference beam over the same distance.
10. Detect both signals using matched photodiodes.
11. Measure the modulation phase delay of each channel relative to the common modulation source.
12. Repeat for several propagation lengths $L_i$.
13. Fit delay versus distance.

For each channel,

$$
\tau(L)=mL+b.
$$

Here $b$ is a fixed electronic and geometric offset.

The slope is

$$
m=\frac{d\tau}{dL}.
$$

The measured speed is

$$
v=\frac{1}{m}.
$$

Thus

$$
v_{\mathrm{ref}}=\frac{1}{m_{\mathrm{ref}}},
\qquad
v_{\mathrm{bright}}=\frac{1}{m_{\mathrm{bright}}}.
$$

## 13.3 Predictions

Standard prediction:

$$
m_{\mathrm{bright}}\approx m_{\mathrm{ref}},
$$

so

$$
v_{\mathrm{bright}}\approx v_{\mathrm{ref}}.
$$

Loaded-branch prediction for an equal-beam bright center on axis:

$$
v_{\mathrm{bright}}\approx\frac c2.
$$

Thus

$$
m_{\mathrm{bright}}\approx\frac{2}{c},
$$

while

$$
m_{\mathrm{ref}}\approx\frac{1}{c}.
$$

So

$$
\boxed{
m_{\mathrm{bright}}\approx2m_{\mathrm{ref}}.
}
$$

Equivalently, for equal propagation distance $L$,

$$
\boxed{
\tau_{\mathrm{bright}}-\tau_{\mathrm{ref}}\approx\frac{L}{c}.
}
$$

At

$$
L=1\ \mathrm{m},
$$

the predicted extra delay is

$$
\Delta\tau\approx3.34\ \mathrm{ns}.
$$

At

$$
L=10\ \mathrm{m},
$$

the predicted extra delay is

$$
\Delta\tau\approx33.4\ \mathrm{ns}.
$$

For an off-axis annular ring, replace $c$ by the local or aperture-averaged
longitudinal transport factor obtained from the input-branch flux integral:

$$
v_\Omega
=
\frac{
\int_{\rho_-}^{\rho_+}
\left[
J_{1z}(\rho)+J_{2z}(\rho)
\right]\rho\,d\rho
}
{
\int_{\rho_-}^{\rho_+}
u_{\mathrm{raw}}(\rho)\rho\,d\rho
}.
$$

---

# 14. Controls

## 14.1 Reference Beam

The reference beam should have:

- the same carrier frequency,
- the same modulation frequency,
- the same optical components where possible,
- the same downstream length $L$,
- similar detector electronics.

## 14.2 Single-Beam Aperture Control

Send only one beam through the same circular aperture or annular slit, with no
interference. The selected beam should propagate at the ordinary reference speed.

This checks that the aperture itself is not producing the predicted delay.

## 14.3 Off-Bright Sampling

Move the aperture from a bright ring to a lower-density region. The loaded-branch
prediction varies with sampled density:

$$
v_\Omega=
\frac{\Phi_{\mathrm{in},z}(\Omega)}
{\int_\Omega u_{\mathrm{raw}}\,dA}.
$$

Lower-density regions should show smaller delay.

The standard prediction remains no density-dependent delay.

## 14.4 Full-Fringe Averaging

Open the aperture to collect a complete bright-dark radial cell, or a
sufficiently large balanced region. The sampled density approaches the two-beam
budget.

The loaded-branch anomaly should weaken or disappear under full-pattern
averaging.

This distinguishes local branch loading from ordinary total-power conservation.

## 14.5 Power Scaling

The prediction depends on coherent loading ratio, not absolute power, in the
proportional regime. Reducing both beam powers equally should reduce signal
amplitude but not change the predicted velocity ratio.

If the delay depends strongly on absolute optical power, thermal, detector, or
nonlinear-medium effects must be suspected.

---

# 15. Interpretation of Outcomes

## 15.1 Null Result

If

$$
v_{\mathrm{bright}}=v_{\mathrm{ref}}
$$

within experimental error, then the isolated bright region behaves as ordinary
propagated output light. The raw local high density does not act as a loaded
branch with reduced effective advance.

## 15.2 Positive Result

If

$$
v_{\mathrm{bright}}\approx\frac{v_{\mathrm{ref}}}{2}
$$

for an equal-beam bright center on axis, and if the effect tracks the sampled
density as predicted, then the loaded-branch law is supported.

The result would indicate that coherent local density loading changes the
effective longitudinal advance of a surviving branch.

## 15.3 Intermediate Result

If

$$
v_{\mathrm{ref}}>v_{\mathrm{bright}}>\frac{v_{\mathrm{ref}}}{2},
$$

then the selected region may not remain a pure raw bright branch. Partial
mixing, diffraction, finite aperture averaging, imperfect visibility, unequal
local densities, or incomplete branch isolation may contribute.

In that case the measured velocity should be compared against the exact aperture
prediction

$$
v_{\Omega}
=
\frac{
\int_{\rho_-}^{\rho_+}
\left[
J_{1z}(\rho)+J_{2z}(\rho)
\right]\rho\,d\rho
}
{
\int_{\rho_-}^{\rho_+}
\left[
u_1(\rho)+u_2(\rho)
+
2\sqrt{u_1(\rho)u_2(\rho)}
\cos\Delta\phi(\rho)
\right]\rho\,d\rho
}.
$$

---

# 16. Summary

This proposal establishes:

1. For real circular fringes, the exact raw density is

   $$
   u_{\mathrm{raw}}(\rho)
   =
   u_1(\rho)+u_2(\rho)
   +
   2\sqrt{u_1(\rho)u_2(\rho)}
   \cos\Delta\phi(\rho).
   $$

2. At an equal-beam bright maximum,

   $$
   u_{\mathrm{raw}}=4u_0.
   $$

3. The exact conserved longitudinal flux through a selected circular or annular aperture is

   $$
   \Phi_{\mathrm{in},z}(\Omega)
   =
   \int_\Omega
   \left[
   J_{1z}+J_{2z}
   \right]dA.
   $$

4. The loaded-branch prediction for the selected region is

   $$
   v_{\Omega}
   =
   \frac{\Phi_{\mathrm{in},z}(\Omega)}
   {\int_\Omega u_{\mathrm{raw}}\,dA}.
   $$

5. At an equal-beam bright center with equal local longitudinal transport,

   $$
   v_{\mathrm{bright}}=\frac{c_z}{2}.
   $$

6. On axis, where $c_z=c$,

   $$
   v_{\mathrm{bright}}=\frac c2.
   $$

7. The dielectric-style proportional response gives the same result:

   $$
   E_2=kE_1
   \Rightarrow
   E_{\mathrm{tot}}=(1+k)E_1
   \Rightarrow
   u_{\mathrm{tot}}=(1+k)^2u_1
   \Rightarrow
   v_{\mathrm{eff}}=\frac{c}{1+k}.
   $$

   For $k=1$,

   $$
   v_{\mathrm{eff}}=\frac c2.
   $$

The decisive experimental signature is

$$
\boxed{
m_{\mathrm{bright}}\approx2m_{\mathrm{ref}}
}
$$

for an equal-beam on-axis bright center, where $m=d\tau/dL$ is the measured
delay slope.

---

# Appendix A — Exact Spherical-Wave Circular Rings

This appendix gives the explicit no-approximation circular-ring formula for two
effective spherical wavefronts.

Let

$$
R_1(\rho)=\sqrt{\rho^2+a_1^2},
$$

and

$$
R_2(\rho)=\sqrt{\rho^2+a_2^2},
$$

where

$$
a_i=Z-z_i.
$$

Then

$$
\Delta\phi(\rho)
=
k[R_1(\rho)-R_2(\rho)]-\phi_0.
$$

The raw density is

$$
u_{\mathrm{raw}}(\rho)
=
u_1(\rho)+u_2(\rho)
+
2\sqrt{u_1(\rho)u_2(\rho)}
\cos\!\left(k[R_1(\rho)-R_2(\rho)]-\phi_0\right).
$$

Bright rings obey

$$
k[R_1(\rho_b)-R_2(\rho_b)]-\phi_0=2\pi N.
$$

Dark rings obey

$$
k[R_1(\rho_d)-R_2(\rho_d)]-\phi_0=(2N+1)\pi.
$$

The local longitudinal transport factors are

$$
\cos\alpha_i(\rho)=\frac{a_i}{R_i(\rho)}.
$$

Therefore

$$
J_{iz}(\rho)=u_i(\rho)c\frac{a_i}{R_i(\rho)}.
$$

The loaded-branch aperture prediction, using the conserved two-input flux budget, is

$$
v_{\Omega}
=
\frac{
\int_{\rho_-}^{\rho_+}
\left[
u_1(\rho)c\frac{a_1}{R_1(\rho)}
+
u_2(\rho)c\frac{a_2}{R_2(\rho)}
\right]\rho\,d\rho
}
{
\int_{\rho_-}^{\rho_+}
\left[
u_1(\rho)+u_2(\rho)
+
2\sqrt{u_1(\rho)u_2(\rho)}
\cos\!\left(k[R_1(\rho)-R_2(\rho)]-\phi_0\right)
\right]\rho\,d\rho
}.
$$

No plane-wave approximation is used. No small-angle approximation is used. No
constant-density approximation is used.

---

# Appendix B — Status of the Claim

The interference identity

$$
u_{\mathrm{raw}}(\rho)
=
u_1(\rho)+u_2(\rho)
+
2\sqrt{u_1(\rho)u_2(\rho)}
\cos\Delta\phi(\rho)
$$

is standard electromagnetic interference.

The circular-fringe phase condition

$$
\Delta\phi(\rho)=2\pi N
$$

for bright rings is standard.

The reduced speed does not follow from these standard identities alone.

The reduced speed follows from the tested loaded-branch transport law

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

Thus the proposal is a direct time-of-flight test between:

$$
\boxed{
\text{ordinary output transport}
}
$$

and

$$
\boxed{
\text{loaded raw-overlap transport with }v_{\mathrm{eff}}=J/u.
}
$$
