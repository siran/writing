---
title: "Gravitational Lensing in a Maxwell Universe: Recovering the Factor of 2 from Electromagnetic Constitutive Symmetry"
subtitle: "Why a Full Electromagnetic Medium Gives 1.75 Arcseconds"
author: An M. Rodriguez, Alex Mercer
date: 2026-01-17
keywords: gravitational lensing, dielectric gravity, refractive index, constitutive symmetry, permittivity, permeability, Maxwell universe
one-sentence-summary: The Newtonian half-value for light bending arises from treating the gravitational background as an electric-only medium. In a Maxwell universe the background is electromagnetic, so both permittivity and permeability shift together, yielding the full 1.75 arcsecond deflection.
summary: A dielectric analogy that modifies only the electric response of the vacuum yields the Newtonian bending angle, 0.875 arcseconds at the solar limb. That is only half an electromagnetic medium. In a Maxwell universe the background responsible for gravity is itself electromagnetic energy, so the constitutive response must be symmetric: both permittivity and permeability change together. This preserves the local impedance of vacuum while lowering the local propagation speed. The resulting refractive index is n(r)=1+2GM/(rc^2), and the weak-field ray integral gives the full deflection angle 4GM/(bc^2), equal to 1.75 arcseconds at the solar limb.
---

## The problem

The classical projectile treatment of light gives the well-known half-value:

$$
\theta_{\text{Newton}} = \frac{2GM}{bc^2}.
$$

At the solar limb this is about

$$
\theta_{\text{Newton}} \approx 0.875 \text{ arcseconds}.
$$

Observation gives twice this:

$$
\theta_{\text{obs}} \approx 1.75 \text{ arcseconds}.
$$

In a Maxwell universe, where gravity is interpreted as refraction rather than
spacetime curvature, the question is direct:

**what refractive profile gives the observed value, and why?**


## The half-result comes from a half-medium

The standard dielectric-style argument treats the gravitational background as an
effective change in permittivity only:

$$
\varepsilon_{\text{eff}}(r)=\varepsilon_0\bigl(1+2\eta(r)\bigr),\qquad
\mu_{\text{eff}}(r)=\mu_0,
$$

with

$$
\eta(r)=\frac{GM}{rc^2}\ll 1.
$$

The resulting refractive index is

$$
n(r)=\sqrt{\frac{\varepsilon_{\text{eff}}\mu_{\text{eff}}}
{\varepsilon_0\mu_0}}
=\sqrt{1+2\eta}
\approx 1+\eta
=1+\frac{GM}{rc^2}.
$$

Using the weak-deflection ray integral,

$$
\theta \approx \int_{-\infty}^{\infty}\nabla_\perp n\,dz,
$$

this gives

$$
\theta = \frac{2GM}{bc^2}.
$$

That is the Newtonian half-value.

The result is not wrong. The model is incomplete. It perturbs only one
constitutive channel of an electromagnetic medium.


## Gravity acts through a full electromagnetic background

In this framework, the background around a massive body is not inert matter. It
is organized electromagnetic energy. A passing wave does not encounter an
electric-only response. It encounters a full electromagnetic response.

That matters because light propagation depends on both constitutive coefficients:

$$
c_{\text{local}} = \frac{1}{\sqrt{\varepsilon_{\text{eff}}\mu_{\text{eff}}}},
\qquad
n = \sqrt{\frac{\varepsilon_{\text{eff}}\mu_{\text{eff}}}
{\varepsilon_0\mu_0}}.
$$

If the background is itself electromagnetic, there is no reason to privilege
the electric channel and ignore the magnetic one. In the Maxwell closure,
$\mathbf{E}$ and $\mathbf{B}$ are complementary aspects of one organized flow,
not separate substances. An electric-only perturbation would split what the
theory has already identified as inseparable.

The weak-field constitutive law must therefore be symmetric:

$$
\varepsilon_{\text{eff}}(r)=\varepsilon_0\bigl(1+2\eta(r)\bigr),
\qquad
\mu_{\text{eff}}(r)=\mu_0\bigl(1+2\eta(r)\bigr),
$$

with the same

$$
\eta(r)=\frac{GM}{rc^2}.
$$


## Why the symmetry is physically required

This symmetric choice does two things at once.

First, it reflects the ontology. The background is electromagnetic energy, not a
purely electric dielectric.

Second, it preserves the local vacuum impedance:

$$
Z_{\text{eff}}=\sqrt{\frac{\mu_{\text{eff}}}{\varepsilon_{\text{eff}}}}
=\sqrt{\frac{\mu_0}{\varepsilon_0}}
= Z_0.
$$

So the background changes propagation speed without introducing an arbitrary
electric-magnetic mismatch. The medium bends rays by delay, not by inventing a
new polarization asymmetry.


## The full weak-field refractive index

With both channels modified equally,

$$
n(r)=\sqrt{(1+2\eta)(1+2\eta)} = 1+2\eta + O(\eta^2).
$$

Therefore

$$
n(r)\approx 1+\frac{2GM}{rc^2}.
$$

This is the full electromagnetic refractive profile.

Compared with the electric-only half-medium, the first-order index shift is
doubled.


## Weak-field bending calculation

Let a ray pass the gravitating body with impact parameter $b$, and use the
straight-line approximation

$$
r=\sqrt{b^2+z^2}.
$$

Then

$$
n(r)=1+\frac{2GM}{c^2\sqrt{b^2+z^2}}.
$$

The transverse gradient is

$$
\frac{\partial n}{\partial b}
= -\frac{2GM}{c^2}\frac{b}{(b^2+z^2)^{3/2}}.
$$

The total deflection magnitude is

$$
\theta
= \int_{-\infty}^{\infty}\left|\frac{\partial n}{\partial b}\right|dz
= \frac{2GM}{c^2}\int_{-\infty}^{\infty}
\frac{b\,dz}{(b^2+z^2)^{3/2}}.
$$

Using

$$
\int_{-\infty}^{\infty}\frac{b\,dz}{(b^2+z^2)^{3/2}} = \frac{2}{b},
$$

we obtain

$$
\theta = \frac{4GM}{bc^2}.
$$

This is exactly the observed weak-field result.


## Solar-limb value

For a ray grazing the Sun, $b=R_\odot$, so

$$
\theta_\odot = \frac{4GM_\odot}{R_\odot c^2}
\approx 8.48\times10^{-6}\ \text{rad}
\approx 1.75 \text{ arcseconds}.
$$


## Interpretation

The factor of 2 does not require curved spacetime. It requires that the
gravitational background be treated as what it is in this framework:

- electromagnetic,
- source-free,
- and therefore symmetric in its electric and magnetic response.

The Newtonian half-value is the bending produced by a one-channel constitutive
model. The full value comes from the full electromagnetic medium.

This is also why the earlier flux-versus-mass intuition was pointing in the
right direction. Light is not averaged trapped matter. It is directed
electromagnetic transport. But the exact coefficient is not fixed by that
intuition alone. It is fixed by the constitutive symmetry forced by the
electromagnetic character of the background.


## Conclusion

In a Maxwell universe, gravity is refraction produced by organized background
electromagnetic energy.

If that background is modeled as electric-only, one recovers the Newtonian
half-value:

$$
\theta = \frac{2GM}{bc^2}.
$$

If it is modeled as a full electromagnetic medium, with symmetric weak-field
changes in both permittivity and permeability, one obtains

$$
\theta = \frac{4GM}{bc^2}.
$$

At the solar limb this is 1.75 arcseconds.

The factor of 2 is not evidence that space itself is curved. It is evidence
that gravity acts through the full electromagnetic constitutive structure of the
vacuum.
