---
title: The Physics of Energy Flow - Constitutive Origin of Background-Weighted Momentum
date: 2026-03-14
---

# 214. Constitutive Origin of Background-Weighted Momentum

Appendix 213 used the variable-background relation

$$
\mathbf{g}=\frac{\mathbf{S}}{k^2}
$$

as an adopted extension of the uniform-region momentum density.

This appendix derives that relation exactly for the specific constitutive
closure already used in the gravity chapters, once the resolved transport
momentum is taken to be the constitutive momentum density

$$
\mathbf{g}:=\mathbf{D}\times\mathbf{B}.
$$

With that choice, the relation used in appendix 213 follows identically inside
this constitutive class:

$$
\varepsilon(\mathbf{r},t)=\varepsilon_0\,\alpha(\mathbf{r},t),
\qquad
\mu(\mathbf{r},t)=\mu_0\,\alpha(\mathbf{r},t),
$$

with

$$
\alpha=\frac{c}{k}.
$$

It also derives the exact energy-exchange term for time-dependent background
and the leading background force for radiative transport in the geometric-optics
limit.

What it does **not** derive is the full exact background force for arbitrary
resolved field configurations. That remains open.

## 214.1 Symmetric Constitutive Closure

Take a source-free linear isotropic medium with constitutive relations

$$
\mathbf{D}=\varepsilon\,\mathbf{E},
\qquad
\mathbf{B}=\mu\,\mathbf{H},
$$

and assume the symmetric constitutive scaling

$$
\varepsilon=\varepsilon_0\,\alpha,
\qquad
\mu=\mu_0\,\alpha.
$$

Then the local transport speed is

$$
k=\frac{1}{\sqrt{\varepsilon\mu}}
=
\frac{1}{\sqrt{\varepsilon_0\mu_0}}\frac{1}{\alpha}
=
\frac{c}{\alpha}.
$$

The local impedance is

$$
Z=\sqrt{\frac{\mu}{\varepsilon}}
=
\sqrt{\frac{\mu_0}{\varepsilon_0}}
=
Z_0.
$$

So this closure changes the propagation speed while keeping the impedance
fixed.

## 214.2 Exact Momentum Density

The Poynting vector is

$$
\mathbf{S}=\mathbf{E}\times\mathbf{H}.
$$

Take the resolved transport momentum density to be

$$
\mathbf{g}:=\mathbf{D}\times\mathbf{B}.
$$

Under the symmetric closure,

$$
\mathbf{g}
=
(\varepsilon_0\alpha\mathbf{E})\times\mathbf{B}.
$$

Since

$$
\mathbf{H}=\frac{\mathbf{B}}{\mu}
=
\frac{\mathbf{B}}{\mu_0\alpha},
$$

we have

$$
\mathbf{S}
=
\mathbf{E}\times\mathbf{H}
=
\frac{1}{\mu_0\alpha}\,\mathbf{E}\times\mathbf{B}.
$$

Therefore

$$
\mathbf{E}\times\mathbf{B}
=
\mu_0\alpha\,\mathbf{S},
$$

and hence

$$
\mathbf{g}
=
\varepsilon_0\mu_0\alpha^2\,\mathbf{S}
=
\frac{\alpha^2}{c^2}\,\mathbf{S}.
$$

But

$$
\alpha=\frac{c}{k},
$$

so

$$
\frac{\alpha^2}{c^2}=\frac{1}{k^2}.
$$

Therefore

$$
\boxed{
\mathbf{g}=\frac{\mathbf{S}}{k^2}
}.
$$

This is exact for the adopted symmetric constitutive closure.

So appendix 213's background-weighted momentum density is not arbitrary inside
this constitutive class. It is exactly the constitutive momentum density
$\mathbf D\times\mathbf B$.

## 214.3 Exact Energy Density and Time-Dependent Exchange

The electromagnetic energy density is

$$
u
:=
\frac{1}{2}\bigl(\mathbf{E}\cdot\mathbf{D}+\mathbf{H}\cdot\mathbf{B}\bigr)
=
\frac{1}{2}\bigl(\varepsilon E^2+\mu H^2\bigr).
$$

Maxwell's equations in the source-free medium are

$$
\nabla\cdot\mathbf{D}=0,
\qquad
\nabla\cdot\mathbf{B}=0,
$$

$$
\nabla\times\mathbf{E}=-\partial_t\mathbf{B},
\qquad
\nabla\times\mathbf{H}=\partial_t\mathbf{D}.
$$

Take the scalar product of the second curl equation with $\mathbf E$ and of the
first with $\mathbf H$, then subtract:

$$
\mathbf E\cdot(\nabla\times\mathbf H)-\mathbf H\cdot(\nabla\times\mathbf E)
=
\mathbf E\cdot\partial_t\mathbf D+\mathbf H\cdot\partial_t\mathbf B.
$$

Using

$$
\nabla\cdot(\mathbf E\times\mathbf H)
=
\mathbf H\cdot(\nabla\times\mathbf E)-\mathbf E\cdot(\nabla\times\mathbf H),
$$

this becomes

$$
\partial_t u+\nabla\cdot\mathbf S
=
-\frac{1}{2}\bigl(E^2\,\partial_t\varepsilon+H^2\,\partial_t\mu\bigr).
$$

For the symmetric constitutive closure,

$$
\partial_t\varepsilon=\varepsilon_0\,\partial_t\alpha,
\qquad
\partial_t\mu=\mu_0\,\partial_t\alpha.
$$

Also,

$$
u
=
\frac{\alpha}{2}\bigl(\varepsilon_0E^2+\mu_0H^2\bigr).
$$

So the right-hand side becomes

$$
-\frac{1}{2}\bigl(\varepsilon_0E^2+\mu_0H^2\bigr)\partial_t\alpha
=
-\frac{u}{\alpha}\,\partial_t\alpha.
$$

Therefore

$$
\partial_t u+\nabla\cdot\mathbf S
=
-u\,\partial_t\ln\alpha.
$$

Since $\alpha=c/k$,

$$
\partial_t\ln\alpha=-\partial_t\ln k,
$$

and hence

$$
\boxed{
\partial_t u+\nabla\cdot\mathbf S
=
u\,\partial_t\ln k
}.
$$

This is the exact energy balance for the time-dependent symmetric constitutive
closure.

Consequences:

- if the background is static, $\partial_t k=0$, then energy continuity is
  source-free;
- if the background varies in time, the resolved field exchanges energy with
  the constitutive background at the exact rate $u\,\partial_t\ln k$.

So a time-dependent background already breaks the stronger claim that the
resolved subsystem always has source-free energy continuity.

## 214.4 Radiative Packet Dynamics in Geometric Optics

To derive the leading background force for transport itself, restrict to the
geometric-optics regime of a narrow radiative packet.

The local dispersion relation is

$$
\omega(\mathbf{r},\mathbf{q},t)=k(\mathbf{r},t)\,|\mathbf{q}|.
$$

Treat this as the packet Hamiltonian

$$
H(\mathbf{r},\mathbf{p},t)=k(\mathbf{r},t)\,|\mathbf{p}|.
$$

Hamilton's equations are

$$
\dot{\mathbf{r}}=\nabla_{\mathbf p}H
=
k\,\frac{\mathbf p}{|\mathbf p|},
$$

$$
\dot{\mathbf p}=-\nabla_{\mathbf r}H
=
-|\mathbf p|\,\nabla k.
$$

The packet energy is

$$
U=H=k|\mathbf p|,
$$

so

$$
|\mathbf p|=\frac{U}{k}.
$$

Therefore

$$
\boxed{
\dot{\mathbf p}
=
-\frac{U}{k}\,\nabla k
=
-U\,\nabla\ln k
}.
$$

This is the leading force on a radiative packet due to spatial variation of the
local transport speed.

Likewise the energy changes as

$$
\dot U=\partial_t H=|\mathbf p|\,\partial_t k=\frac{U}{k}\partial_t k,
$$

so

$$
\boxed{
\dot U=U\,\partial_t\ln k
}.
$$

This is exactly the packet version of the local energy-exchange law derived
above.

## 214.5 Radiative Background Force Density

For a narrow radiative packet with local energy density $u$ and negligible
internal stress compared to the background gradient scale, the geometric-optics
force density is

$$
\boxed{
\mathbf{f}_{\mathrm{rad}}
=
-u\,\nabla\ln k
}.
$$

Equivalently, using $\mathbf g=\mathbf S/k^2$ and $|\mathbf S|=uk$ for pure
radiation,

$$
\mathbf{f}_{\mathrm{rad}}
=
-k\,|\mathbf g|\,\nabla\ln k.
$$

This formula is not the full exact background force for arbitrary resolved
field configurations. It is the leading transport-force density for radiative
packets in the geometric-optics limit.

So the situation is now clear:

- exact constitutive result:
  $$
  \mathbf g=\mathbf S/k^2,
  $$
- exact time-dependent energy exchange:
  $$
  \partial_t u+\nabla\cdot\mathbf S=u\,\partial_t\ln k,
  $$
- leading radiative background force:
  $$
  \mathbf f_{\mathrm{rad}}=-u\,\nabla\ln k.
  $$

## 214.6 Relation to Appendices 212 and 213

Appendix 212 used the same symmetric constitutive closure to derive the static
weak-field metric and the corresponding benchmark observables.

Appendix 213 used

$$
\mathbf g=\frac{\mathbf S}{k^2}
$$

as the adopted variable-background momentum relation inside the hydrodynamic
balance-law extension.

The present appendix now clarifies the scope:

- that momentum relation is exact inside the symmetric constitutive closure,
- the time-dependent energy source term is also exact there,
- but the full exact resolved background force density is still not known for
  arbitrary field configurations,
- only its radiative geometric-optics form has been derived here.

## 214.7 Summary

For the symmetric constitutive closure

$$
\varepsilon=\varepsilon_0\,\frac{c}{k},
\qquad
\mu=\mu_0\,\frac{c}{k},
$$

the exact field momentum density is

$$
\mathbf g=\mathbf D\times\mathbf B=\frac{\mathbf S}{k^2}.
$$

The exact energy balance is

$$
\partial_t u+\nabla\cdot\mathbf S=u\,\partial_t\ln k.
$$

So:

- static background: source-free energy continuity for the resolved field,
- time-dependent background: exact energy exchange with the constitutive
  background.

For radiative packets in geometric optics, the background force is

$$
\mathbf f_{\mathrm{rad}}=-u\,\nabla\ln k.
$$

This provides the constitutive origin of the background-weighted momentum used
in appendix 213 and identifies the next real open problem:

> derive the full exact background force and stress exchange for general
> variable-background field configurations, not only for radiative transport.
