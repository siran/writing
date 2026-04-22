% Longitudinal Delay of an Isolated Circular Bright Interference Branch % An M.
Rodriguez % 2026-04-21


# Longitudinal Delay of an Isolated Circular Bright Interference Branch

## Abstract

This proposal tests whether a spatially isolated bright region of a circular
interference pattern propagates with the same delay as an ordinary reference
beam, or whether its effective longitudinal advance is reduced by coherent
loading.

Two coherent laser beams are recombined so that their wavefronts produce
fringes. Standard interference gives a spatial redistribution of density: bright
rings exceed the two-beam mean while neighboring dark rings fall below it, with
the full pattern conserving the two-beam energy budget. The experiment isolates
a circular bright region, or a narrow annular bright ring, and measures its
modulation delay over a known longitudinal distance against a reference beam.

The standard expectation is that the selected bright region and the reference
beam have the same propagation speed. The loaded-branch expectation is different
(in analogy with dielectrics): if the selected bright region carries the
available two-beam flux on a *higher local density*, then its effective
longitudinal advance must be slower. For equal local beam densities at a bright
maximum, the predicted speed is one half of the local available longitudinal
transport speed.

The experiment is therefore a direct time-of-flight test between ordinary output
transport and loaded raw-overlap transport.


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


# 2. Core Idea

Two coherent laser beams can overlap in phase. At a bright fringe, by
superposition principle, their amplitudes add. Since the *energy density*
readout is quadratic, the raw local *energy density* at an equal-beam bright
maximum is four times the single-beam *energy density*.

The incoming two-beam flux budget is equal to recombined the *single-beam* flux,
albeit the recombined beam is spatially distributed among the two output
channels of a MZ. The full interference pattern conserves energy by distributing
density into bright and dark regions -- a bright fringe on one arm corresponds
symmetrycally to a dark fringe in the other arm. The proposed test aims to
confirm the suspicion that to avoid energy conservation, denser energy
propagates more slowly. The inspiration comes from analyzing light speed inside
a dielectric material.

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


# 3. Beams and coordinates set up

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

and radial single-beam density profiles

$$
u_1(\rho),
\qquad
u_2(\rho).
$$


# 4. Beams interference

Let the two coherent scalar field amplitudes on the observation plane be written
as

$$
f_1(\rho,t)=A_1(\rho)e^{i\phi_1(\rho)}e^{-i\omega t},
$$

and

$$
f_2(\rho,t)=A_2(\rho)e^{i\phi_2(\rho)}e^{-i\omega t}.
$$

The raw superposed field is

$$
f_{\mathrm{raw}}(\rho,t)=f_1(\rho,t)+f_2(\rho,t).
$$

Define the single-beam densities by

$$
u_1(\rho):=C|A_1(\rho)|^2,
\qquad
u_2(\rho):=C|A_2(\rho)|^2,
$$

where $C>0$ is the conventional proportionality factor between
squared field amplitude and energy density.

Let

$$
\Delta\phi(\rho):=\phi_1(\rho)-\phi_2(\rho).
$$

Then

$$
u_{\mathrm{raw}}(\rho)
=
C|f_1+f_2|^2.
$$

Expand:

$$
|f_1+f_2|^2
=
|f_1|^2+|f_2|^2+f_1f_2^*+f_1^*f_2.
$$

Now

$$
f_1f_2^*
=
A_1A_2^*e^{i(\phi_1-\phi_2)},
$$

and if $A_1,A_2$ are taken as nonnegative real amplitudes after
extracting phase,

$$
f_1f_2^*
=
|A_1||A_2|e^{i\Delta\phi}.
$$

Similarly,

$$
f_1^*f_2
=
|A_1||A_2|e^{-i\Delta\phi}.
$$

Thus

$$
f_1f_2^*+f_1^*f_2
=
2|A_1||A_2|\cos\Delta\phi.
$$

Multiplying by $C$ gives

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

This identity is exact for coherent scalar amplitudes. It is the local
interference law.

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

Then

$$
u_{\mathrm{raw}}(\rho_b)
=
\left(
\sqrt{u_1(\rho_b)}
+
\sqrt{u_2(\rho_b)}
\right)^2.
$$

If the two beams are locally equal at that bright radius,

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

Then

$$
u_{\mathrm{raw}}(\rho_d)
=
\left(
\sqrt{u_1(\rho_d)}
-
\sqrt{u_2(\rho_d)}
\right)^2.
$$

If the two beams are locally equal there,

$$
u_{\mathrm{raw}}(\rho_d)=0.
$$


# 5. Exact Circular-Fringe Geometry from Real Wavefronts

Circular fringes occur when the phase difference is radial:

$$
\Delta\phi(x,y)=\Delta\phi(\rho).
$$

This may arise, for example, from two coherent beams with different wavefront
curvatures, from a Michelson-type circular-fringe geometry, or from any optical
arrangement where the measured phase difference is radial.

The analysis does not require a specific model of the laser beams. However, to
show the exact geometry explicitly, one may model each beam locally by a
spherical wavefront emitted from an effective coherent point on the optical
axis.

Let the effective origins be at axial positions $z=z_1$ and
$z=z_2$, and let the observation plane be $z=Z$. Define
exact path lengths

$$
R_1(\rho)=\sqrt{\rho^2+(Z-z_1)^2},
$$

and

$$
R_2(\rho)=\sqrt{\rho^2+(Z-z_2)^2}.
$$

The fields may be written as

$$
f_1(\rho,t)
=
A_1(\rho)e^{i(kR_1(\rho)-\omega t)},
$$

and

$$
f_2(\rho,t)
=
A_2(\rho)e^{i(kR_2(\rho)-\omega t+\phi_0)}.
$$

Then the exact radial phase difference is

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

No plane-wave approximation is used here. The square roots are retained exactly.

For real beams that are not exactly spherical, the same equations hold with the
measured phase functions $\phi_1(\rho)$ and $\phi_2(\rho)$. The experiment
only needs the actual radial phase difference and local densities, not an
idealized beam model.


# 6. Exact Area-Averaged Density for a Selected Circular Region

A detector or aperture samples a finite region, not a mathematical point.

Let $\Omega$ be the selected aperture region in the observation plane.
For a circular central bright spot,

$$
\Omega=\{(x,y):0\le \rho\le a\}.
$$

For a bright annular ring centered at radius $\rho_b$ with half-width
$w/2$,

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
assumption of constant density is used.


# 7. Exact Longitudinal Flux Budget for a Selected Circular Region

Let the longitudinal flux densities of the two individual beams be

$$
J_{1z}(\rho),
\qquad
J_{2z}(\rho).
$$

For freely propagating local transport, these may be written as

$$
J_{1z}(\rho)=u_1(\rho)c\cos\alpha_1(\rho),
$$

and

$$
J_{2z}(\rho)=u_2(\rho)c\cos\alpha_2(\rho),
$$

where $\alpha_i(\rho)$ is the local angle between the beam's energy-flow
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

For arbitrary real beams, $J_{iz}(\rho)$ can be measured or computed from the
local Poynting vector of each beam alone.

The exact available longitudinal flux through aperture $\Omega$ is

$$
\boxed{
\Phi_z(\Omega)
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
\Phi_z(\Omega)
=
2\pi\int_{\rho_-}^{\rho_+}
\left[
J_{1z}(\rho)+J_{2z}(\rho)
\right]\rho\,d\rho.
}
$$

This is the two-beam longitudinal budget available to the selected region.


# 8. Loaded-Branch Prediction for a Circular Aperture

The loaded-branch law is

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

For a finite aperture, the corresponding exact area-integrated prediction is

$$
\boxed{
v_{\Omega}
=
\frac{\Phi_z(\Omega)}
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

This is the exact circular-fringe loaded-branch prediction.

It is written entirely in terms of measurable beam quantities:

$$
u_1(\rho),\quad u_2(\rho),\quad \Delta\phi(\rho),\quad J_{1z}(\rho),\quad J_{2z}(\rho).
$$


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


# 10. Ordinary Output Transport

At a lossless 50/50 recombiner, the output fields are

$$
f_+
=
\frac{f_1+f_2}{\sqrt2},
\qquad
f_-
=
\frac{f_1-f_2}{\sqrt2}.
$$

The factor $1/\sqrt2$ is the lossless beam-splitter amplitude factor. It
ensures that the total output energy equals the total input energy.

The output densities are

$$
u_+
=
C|f_+|^2
=
\frac{C}{2}|f_1+f_2|^2,
$$

and

$$
u_-
=
C|f_-|^2
=
\frac{C}{2}|f_1-f_2|^2.
$$

Using the exact local interference identity,

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

Thus ordinary output transport assigns density $2u_0$ to the bright
output, not $4u_0$.

It therefore predicts no $c/2$ delay.


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
u_{\mathrm{raw}}=C|f_1+f_2|^2.
$$

At an equal-beam bright maximum,

$$
u_{\mathrm{raw}}=4u_0.
$$

The available two-beam flux is

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


# 12. Dielectric-Style Derivation of the Loaded-Branch Law

Matter is standing electromagnetic organization. Dielectric slowing is therefore
field-field interaction in a stable organized background. The fringe-delay test
asks whether the same loading rule appears in the simplest unbound case: two
coherent light fields overlapping in phase.


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


## 12.2 Coherent Response Field

Let a primary branch have field amplitude

$$
E_1.
$$

Let the coherent response field be proportional:

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

For two equal branches in phase, the available total flux is

$$
J_{\mathrm{available}}=2u_1c.
$$

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


# 13. Experimental Design

## 13.1 Apparatus

Minimum requirements:

- stable coherent laser source,
- amplitude modulation source,
- Michelson, Mach-Zehnder, or equivalent circular-fringe interferometer,
- controlled wavefront curvature or axial path geometry producing circular
  fringes,
- stable circular fringe pattern,
- circular aperture or annular slit selecting one bright region,
- reference beam path,
- equal downstream propagation length $L$ for reference and
  selected bright region,
- fast photodiodes,
- oscilloscope, lock-in amplifier, or phase-delay measurement system,
- variable path length or multiple known path lengths.


## 13.2 Procedure

1. Generate a coherent laser beam.
2. Apply sinusoidal amplitude modulation at angular frequency $\Omega$.
3. Split the beam into two equal arms.
4. Recombine the beams in a circular-fringe geometry.
5. Record the individual beam profiles $u_1(\rho)$ and $u_2(\rho)$ by
   blocking the other beam in turn.
6. Record the circular interference pattern to determine $\Delta\phi(\rho)$ or
   directly identify bright and dark radii.
7. Select a bright central spot or narrow bright annulus using a circular
   aperture or annular slit.
8. Let the selected bright region propagate over known distance
   $L$.
9. In parallel, propagate a reference beam over the same distance.
10. Detect both signals using matched photodiodes.
11. Measure the modulation phase delay of each channel relative to the common
    modulation source.
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

For an off-axis annular ring, replace $c$ by the exact local or
aperture-averaged longitudinal transport factor obtained from the flux integral:

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
interference. The selected beam should propagate at the ordinary reference
speed.

This checks that the aperture itself is not producing the predicted delay.


## 14.3 Off-Bright Sampling

Move the aperture from a bright ring to a lower-density region. The
loaded-branch prediction varies with sampled density:

$$
v_\Omega=
\frac{\Phi_z(\Omega)}
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

3. The exact available longitudinal flux through a selected circular or annular
   aperture is


   $$
   \Phi_z(\Omega)
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
   \frac{\Phi_z(\Omega)}
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

Let

$$
f_1(\rho,t)=A_1(\rho)e^{i(kR_1(\rho)-\omega t)},
$$

and

$$
f_2(\rho,t)=A_2(\rho)e^{i(kR_2(\rho)-\omega t+\phi_0)}.
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

The exact loaded-branch aperture prediction is

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

is standard.

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
