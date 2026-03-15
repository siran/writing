---
title: The Physics of Energy Flow - Variable-Background Emergent Hydrodynamic Form
date: 2026-03-14
---

# 213. Variable-Background Emergent Hydrodynamic Form

Appendix 207 derived the emergent hydrodynamic form in an approximately uniform
region, where the local transport scale $k$ could be treated as constant. This
appendix extends that derivation to the case in which

$$
k=k(\mathbf{r},t)
$$

varies across the resolved continuum.

The balance-law structure derived here is exact once two variable-background
ingredients are adopted:

- the matched constitutive relation
  $$
  \mathbf{g}=\frac{\mathbf{S}}{k^2},
  $$
- the residual background momentum-exchange term
  $$
  \mathbf{f}_{\mathrm{bg}}.
  $$

What is not yet derived here is the substrate-specific closure that fixes those
objects from the underlying transport. The novelty is that once $k$ varies, one
must distinguish carefully between:

- conserved coarse-grained energy,
- effective inertial density,
- momentum exchange with the varying background.

## 213.1 Local Variables in a Varying Background

Let

$$
\beta(\mathbf{r},t):=\frac{1}{k(\mathbf{r},t)^2}.
$$

At the resolved scale, keep the local energy density and energy flux

$$
u,
\qquad
\mathbf{S},
$$

with exact local energy continuity

$$
\partial_t u+\nabla\cdot\mathbf{S}=0.
$$

Adopt, as the variable-background extension of the uniform-region relation, the
local momentum density

$$
\mathbf{g}:=\beta\,\mathbf{S}=\frac{\mathbf{S}}{k^2}.
$$

When the background varies, the resolved subsystem need not be momentum-closed
by itself. Define the exact background-exchange density

$$
\mathbf{f}_{\mathrm{bg}}(\mathbf{r},t)
$$

by the local balance law

$$
\partial_t\mathbf{g}+\nabla\cdot\mathbf{T}
=
\mathbf{f}_{\mathrm{bg}}.
$$

This is not a new force law. It is the exact residual bookkeeping term once
$\mathbf{g}$ and $\mathbf{T}$ are specified: whatever momentum is not balanced
by the resolved stress transport is, by definition, momentum exchanged with the
unresolved background constitutive organization.

In a uniform region,

$$
\nabla k=0,
\qquad
\partial_t k=0,
\qquad
\mathbf{f}_{\mathrm{bg}}=0,
$$

and the derivation of appendix 207 is recovered.

## 213.2 Coarse-Graining in a Variable Background

Let $\langle\cdot\rangle$ again denote averaging over a cell large compared to
local closure structure and small compared to resolved macroscopic variation.

Assume, at the resolved scale, that averaging commutes with differentiation:

$$
\langle\partial_t f\rangle=\partial_t\langle f\rangle,
\qquad
\langle\partial_i f\rangle=\partial_i\langle f\rangle.
$$

Then the exact coarse-grained energy balance is still

$$
\partial_t\langle u\rangle+\nabla\cdot\langle\mathbf{S}\rangle=0.
$$

This remains source-free. Energy itself is still only redistributed.

The effective momentum balance is

$$
\partial_t\langle\mathbf{g}\rangle
+
\nabla\cdot\langle\mathbf{T}\rangle
=
\langle\mathbf{f}_{\mathrm{bg}}\rangle.
$$

So the background enters through momentum exchange, not through failure of
energy continuity.

## 213.3 Two Densities: Energy Density and Effective Inertial Density

When $k$ varies, it is no longer enough to write

$$
\rho=\frac{\langle u\rangle}{k^2}
$$

with one constant $k$ pulled out of the cell.

The exact effective inertial density is instead

$$
\rho:=\langle \beta u\rangle
=
\left\langle \frac{u}{k^2}\right\rangle.
$$

This should be distinguished from the coarse-grained stored-energy density

$$
\bar u:=\langle u\rangle.
$$

Only $\bar u$ obeys a source-free continuity equation. The quantity $\rho$ is
an effective inertial density, and when $k$ varies it does not satisfy a
source-free continuity law by itself.

Define the coarse-grained momentum density by

$$
\rho\mathbf{v}:=\langle\mathbf{g}\rangle
=
\left\langle\frac{\mathbf{S}}{k^2}\right\rangle.
$$

In a slowly varying background, where $k$ changes little across the cell, this
reduces to

$$
\rho
\approx
\frac{\bar u}{k(\mathbf{X},t)^2},
\qquad
\rho\mathbf{v}
\approx
\frac{\langle\mathbf{S}\rangle}{k(\mathbf{X},t)^2},
$$

so that

$$
\mathbf{v}\approx\frac{\langle\mathbf{S}\rangle}{\langle u\rangle}.
$$

Thus the transport velocity remains the ratio of coarse-grained energy flux to
coarse-grained energy density, but the effective inertial density now carries
the background weighting.

## 213.4 Exact Variable-Background Continuity Equation

Differentiate $\rho=\langle\beta u\rangle$:

$$
\partial_t\rho
=
\left\langle \beta\,\partial_t u+u\,\partial_t\beta\right\rangle.
$$

Also,

$$
\nabla\cdot(\rho\mathbf{v})
=
\nabla\cdot\langle\beta\mathbf{S}\rangle
=
\left\langle \beta\,\nabla\cdot\mathbf{S}+\mathbf{S}\cdot\nabla\beta\right\rangle.
$$

Add the two expressions and use $\partial_t u+\nabla\cdot\mathbf{S}=0$:

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf{v})
=
\left\langle
u\,\partial_t\beta+\mathbf{S}\cdot\nabla\beta
\right\rangle.
$$

Define the exact variable-background source term

$$
\sigma_k
:=
\left\langle
u\,\partial_t\beta+\mathbf{S}\cdot\nabla\beta
\right\rangle.
$$

Then

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf{v})=\sigma_k.
$$

This is the exact balance law for the effective inertial density once
$\rho=\langle u/k^2\rangle$ has been adopted.

Now write it directly in terms of $k$. Since

$$
\beta=k^{-2},
$$

we have

$$
\partial_t\beta=-2\beta\,\partial_t\ln k,
\qquad
\nabla\beta=-2\beta\,\nabla\ln k.
$$

So

$$
\sigma_k
=
-2\left\langle
\beta\left(u\,\partial_t\ln k+\mathbf{S}\cdot\nabla\ln k\right)
\right\rangle.
$$

In a slowly varying resolved cell, this becomes

$$
\sigma_k
\approx
-2\rho\left(\partial_t+ \mathbf{v}\cdot\nabla\right)\ln k.
$$

Therefore the continuity equation becomes

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf{v})
\approx
-2\rho\,D_t\ln k,
$$

where

$$
D_t:=\partial_t+\mathbf{v}\cdot\nabla.
$$

This equation says something precise:

> when a transported configuration moves into a region where the local
> transport scale decreases, the same coarse-grained energy corresponds to a
> larger effective inertial density.

So the variable-$k$ medium modifies inertia even before any constitutive stress
assumption is made.

## 213.5 Exact Coarse-Grained Momentum Equation

The coarse-grained momentum balance is

$$
\partial_t(\rho\mathbf{v})
+
\nabla\cdot\langle\mathbf{T}\rangle
=
\mathbf{f},
$$

where

$$
\mathbf{f}:=\langle\mathbf{f}_{\mathrm{bg}}\rangle.
$$

Define, exactly as before, the residual stress tensor

$$
\boldsymbol{\Sigma}
:=
\langle\mathbf{T}\rangle-\rho\,\mathbf{v}\otimes\mathbf{v}.
$$

Then

$$
\partial_t(\rho\mathbf{v})
+
\nabla\cdot(\rho\,\mathbf{v}\otimes\mathbf{v})
+
\nabla\cdot\boldsymbol{\Sigma}
=
\mathbf{f}.
$$

Decompose

$$
\boldsymbol{\Sigma}=p\,\mathbf{I}-\boldsymbol{\tau},
$$

with

$$
p:=\frac{1}{3}\operatorname{tr}(\boldsymbol{\Sigma}),
\qquad
\operatorname{tr}(\boldsymbol{\tau})=0.
$$

Then the exact variable-background momentum equation is

$$
\partial_t(\rho\mathbf{v})
+
\nabla\cdot(\rho\,\mathbf{v}\otimes\mathbf{v})
=
-\nabla p+\nabla\cdot\boldsymbol{\tau}+\mathbf{f}.
$$

## 213.6 Convective Form with Variable Background

Expand the left-hand side:

$$
\partial_t(\rho\mathbf{v})
+
\nabla\cdot(\rho\,\mathbf{v}\otimes\mathbf{v})
=
\rho\left(\partial_t\mathbf{v}+(\mathbf{v}\cdot\nabla)\mathbf{v}\right)
+
\mathbf{v}\left(\partial_t\rho+\nabla\cdot(\rho\mathbf{v})\right).
$$

Using the exact variable-background continuity equation,

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf{v})=\sigma_k,
$$

we obtain

$$
\rho\left(\partial_t\mathbf{v}+(\mathbf{v}\cdot\nabla)\mathbf{v}\right)
=
-\nabla p+\nabla\cdot\boldsymbol{\tau}+\mathbf{f}-\mathbf{v}\,\sigma_k.
$$

This is the exact convective form in a variable background.

In the slowly varying resolved approximation,

$$
\rho D_t\mathbf{v}
\approx
-\nabla p+\nabla\cdot\boldsymbol{\tau}
+
\mathbf{f}
+
2\rho\,\mathbf{v}\,D_t\ln k.
$$

So the variable background enters in two distinct ways:

- through the explicit momentum-exchange term $\mathbf{f}$,
- through the density-conversion term encoded by $\sigma_k$.

These two effects should not be conflated.

## 213.7 Static Background Example

If the background is static, then

$$
\partial_t k=0,
$$

and the continuity source reduces to

$$
\sigma_k
=
\langle \mathbf{S}\cdot\nabla\beta\rangle
\approx
-2\rho\,\mathbf{v}\cdot\nabla\ln k.
$$

So

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf{v})
\approx
-2\rho\,\mathbf{v}\cdot\nabla\ln k.
$$

If, in addition, the background momentum exchange is potential-like, write

$$
\mathbf{f}=-\rho\,\nabla\Phi_k.
$$

Then

$$
\rho D_t\mathbf{v}
\approx
-\nabla p+\nabla\cdot\boldsymbol{\tau}
-\rho\,\nabla\Phi_k
+
2\rho\,\mathbf{v}\,\mathbf{v}\cdot\nabla\ln k.
$$

For the gravity closure of appendix 212, the weak-field metric gave

$$
g_{tt}=\frac{k}{c}+O(\eta^2),
$$

so the corresponding slow-mode potential is

$$
\Phi_k
:=
\frac{c^2}{2}\ln\frac{k}{c}.
$$

Since

$$
k=c(1-2\eta)+O(\eta^2),
$$

we obtain

$$
\Phi_k
=
-c^2\eta+O(\eta^2)
=
-\frac{GM}{r}+O(\eta^2),
$$

and therefore

$$
-\nabla\Phi_k
=
-\frac{GM}{r^2}\,\hat{\mathbf r}+O(\eta^2),
$$

which is the Newtonian gravitational acceleration.

So the variable-background hydrodynamic form contains the gravity closure of
appendix 212 as one special constitutive case.

## 213.8 Euler-like and Navier-Stokes-like Limits in Variable Background

The exact equations above reduce to the familiar forms once the unresolved
stress is closed.

### Euler-like limit

If

$$
\boldsymbol{\tau}=0,
$$

then

$$
\rho D_t\mathbf{v}
=
-\nabla p+\mathbf{f}-\mathbf{v}\sigma_k.
$$

This is the variable-background Euler form.

### Navier-Stokes-like limit

If the deviatoric stress is approximated by the Newtonian constitutive form

$$
\boldsymbol{\tau}
=
\eta_v\left(\nabla\mathbf{v}+(\nabla\mathbf{v})^{\mathsf T}
-\frac{2}{3}(\nabla\cdot\mathbf{v})\mathbf{I}\right)
+
\zeta_v(\nabla\cdot\mathbf{v})\mathbf{I},
$$

then

$$
\rho D_t\mathbf{v}
=
-\nabla p+\nabla\cdot\boldsymbol{\tau}
+
\mathbf{f}
-\mathbf{v}\sigma_k.
$$

This is the variable-background Navier-Stokes-like form.

Compared with the uniform-region case, the new terms are exactly those tied to

- background momentum exchange,
- variation of the local transport scale.

## 213.9 What Is Exact and What Is Not

Up to the introduction of the constitutive form of $\boldsymbol{\tau}$, the
derivation is exact once

- the variable-background momentum relation
  $$
  \mathbf{g}=\frac{\mathbf{S}}{k^2}
  $$
  is adopted,
- the background-exchange term

$$
\mathbf{f}_{\mathrm{bg}}
$$

is defined as the exact residual momentum exchange with the unresolved
background.

So the exact conclusions are:

- coarse-grained energy density remains conserved,
- effective inertial density obeys a balance law with a conversion term when
  $k$ varies,
- the convective momentum equation acquires both an explicit background force
  term and a density-conversion term.

What remains constitutive is:

- the local momentum relation $\mathbf{g}=\mathbf{S}/k^2$ for a genuinely
  variable background, unless it is separately derived from the chosen
  constitutive closure,
- the exact resolved form of $\mathbf{f}_{\mathrm{bg}}$ for a chosen
  background closure,
- the constitutive closure of the deviatoric stress.

## 213.10 Summary

When the local transport scale varies,

$$
k=k(\mathbf{r},t),
$$

the exact coarse-grained effective inertial density is

$$
\rho=\left\langle\frac{u}{k^2}\right\rangle,
$$

and the exact momentum density is

$$
\rho\mathbf{v}
=
\left\langle\frac{\mathbf{S}}{k^2}\right\rangle.
$$

They satisfy

$$
\partial_t\rho+\nabla\cdot(\rho\mathbf{v})=\sigma_k,
$$

with

$$
\sigma_k
=
\left\langle
u\,\partial_t(k^{-2})+\mathbf{S}\cdot\nabla(k^{-2})
\right\rangle,
$$

and

$$
\rho D_t\mathbf{v}
=
-\nabla p+\nabla\cdot\boldsymbol{\tau}
+
\mathbf{f}
-\mathbf{v}\sigma_k.
$$

Thus the variable-background hydrodynamic limit is no longer just the
uniform-region Euler/Navier-Stokes form with $k(\mathbf r,t)$ inserted by hand.

It has a definite new structure:

- energy continuity remains source-free,
- effective inertia is background-weighted,
- background variation creates density-conversion terms,
- momentum exchange with the background enters explicitly.

This is a consistent variable-background extension of appendix 207 within the
adopted matched constitutive relation $\mathbf{g}=\mathbf{S}/k^2$.
