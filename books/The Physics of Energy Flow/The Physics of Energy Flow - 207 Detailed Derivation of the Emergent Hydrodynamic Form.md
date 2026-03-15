---
title: The Physics of Energy Flow - Detailed Derivation of the Emergent Hydrodynamic Form
date: 2026-03-14
---

# 207. Detailed Derivation of the Emergent Hydrodynamic Form

This appendix carries out, in the simplest uniform-region setting, the
derivation sketched in Appendix 206.

The result is exact up to the constitutive choice for the coarse-grained
stress. That last step is where Euler-like or Navier-Stokes-like behavior
enters.

## 207.1 Uniform-Region Assumptions

Work in a region where the local transport scale $k$ may be treated as
constant over the coarse-graining cell and over the time interval of interest.

In that region the already-derived electromagnetic transport quantities are

$$
u,
\qquad
\mathbf{S},
\qquad
\mathbf{g}=\frac{\mathbf{S}}{k^2},
\qquad
\partial_t \mathbf{g}-\nabla\cdot\mathbf{T}=0.
$$

The last equation is the exact local momentum continuity law already obtained
in chapter 12.

We now coarse-grain these quantities.

## 207.2 Averaging Operator

Let $\langle \cdot \rangle$ denote averaging over a cell large compared to
local closure structure and small compared to macroscopic variation.

Assume, in the usual continuum approximation, that averaging commutes with
space and time differentiation at the resolved scale:

$$
\langle \partial_t f\rangle = \partial_t \langle f\rangle,
\qquad
\langle \partial_i f\rangle = \partial_i \langle f\rangle.
$$

Then the exact local conservation laws average to

$$
\partial_t \langle u\rangle + \nabla\cdot\langle \mathbf{S}\rangle = 0,
$$

and

$$
\partial_t \langle \mathbf{g}\rangle - \nabla\cdot\langle \mathbf{T}\rangle = 0.
$$

These are still exact at the coarse-grained level. No constitutive assumption
has entered yet.

## 207.3 Effective Density and Velocity

Define the effective density by

$$
\rho := \frac{\langle u\rangle}{k^2}.
$$

Define the effective velocity by

$$
\rho \mathbf{v} := \langle \mathbf{g}\rangle
=
\frac{\langle \mathbf{S}\rangle}{k^2}.
$$

Equivalently,

$$
\mathbf{v}=\frac{\langle \mathbf{S}\rangle}{\langle u\rangle}.
$$

This is the coarse-grained transport velocity of the energy content of the
cell.

Now divide the averaged energy continuity equation by $k^2$:

$$
\partial_t \rho + \nabla\cdot(\rho \mathbf{v}) = 0.
$$

So the usual continuity equation of continuum mechanics appears immediately.

At this point nothing has been postulated beyond:

- local energy continuity,
- the already-derived relation $\mathbf{g}=\mathbf{S}/k^2$,
- coarse-graining in a region with uniform $k$.

## 207.4 Exact Coarse-Grained Momentum Equation

The averaged momentum equation is

$$
\partial_t(\rho \mathbf{v}) - \nabla\cdot\langle \mathbf{T}\rangle = 0.
$$

This still contains the full coarse-grained momentum-flux tensor

$$
\langle \mathbf{T}\rangle.
$$

To isolate the transported momentum of the mean motion, define the residual
stress tensor

$$
\boldsymbol{\Sigma}
:=
\rho\,\mathbf{v}\otimes\mathbf{v}-\langle \mathbf{T}\rangle.
$$

This is an exact definition, not an approximation. It says simply that the
total coarse-grained momentum flux is decomposed into:

- momentum carried by the mean motion,
- everything else.

Substituting gives the exact equation

$$
\partial_t(\rho \mathbf{v})
+
\nabla\cdot(\rho\,\mathbf{v}\otimes\mathbf{v})
-\nabla\cdot\boldsymbol{\Sigma}
=
0.
$$

This is already the hydrodynamic form. What remains is to parameterize
$\boldsymbol{\Sigma}$.

## 207.5 Pressure and Deviatoric Stress

Decompose the residual stress into isotropic and traceless parts:

$$
\boldsymbol{\Sigma}
=
p\,\mathbf{I} - \boldsymbol{\tau},
$$

where

$$
p := \frac{1}{3}\,\mathrm{tr}(\boldsymbol{\Sigma}),
$$

and

$$
\mathrm{tr}(\boldsymbol{\tau})=0.
$$

This gives

$$
\partial_t(\rho \mathbf{v})
+
\nabla\cdot(\rho\,\mathbf{v}\otimes\mathbf{v})
+
\nabla p
- \nabla\cdot\boldsymbol{\tau}
=
0.
$$

Equivalently,

$$
\partial_t(\rho \mathbf{v})
+
\nabla\cdot(\rho\,\mathbf{v}\otimes\mathbf{v})
=
-\nabla p + \nabla\cdot\boldsymbol{\tau}.
$$

This is the exact coarse-grained momentum balance once the residual stress is
split into isotropic and traceless parts.

## 207.6 Convective Form

Use the continuity equation

$$
\partial_t \rho + \nabla\cdot(\rho \mathbf{v})=0
$$

to rewrite the momentum equation in convective form.

Expand

$$
\partial_t(\rho \mathbf{v})+\nabla\cdot(\rho\,\mathbf{v}\otimes\mathbf{v})
=
\rho\left(\partial_t\mathbf{v}+(\mathbf{v}\cdot\nabla)\mathbf{v}\right)
+
\mathbf{v}\left(\partial_t\rho+\nabla\cdot(\rho\mathbf{v})\right).
$$

The second term vanishes by continuity, so

$$
\rho\left(\partial_t\mathbf{v}+(\mathbf{v}\cdot\nabla)\mathbf{v}\right)
=
-\nabla p + \nabla\cdot\boldsymbol{\tau}.
$$

This is the standard continuum momentum equation, still exact up to the form
of $\boldsymbol{\tau}$.

## 207.7 Euler and Navier-Stokes-like Limits

At this stage the derivation branches according to constitutive closure.

### Euler-like limit

If the deviatoric stress is neglected,

$$
\boldsymbol{\tau}=0,
$$

then

$$
\rho\left(\partial_t\mathbf{v}+(\mathbf{v}\cdot\nabla)\mathbf{v}\right)
=
-\nabla p.
$$

This is the Euler form.

### Navier-Stokes-like limit

If the unresolved stress is approximated by the Newtonian constitutive form

$$
\boldsymbol{\tau}
=
\eta\left(\nabla\mathbf{v}+(\nabla\mathbf{v})^{\mathsf T}
-\frac{2}{3}(\nabla\cdot\mathbf{v})\mathbf{I}\right)
+
\zeta(\nabla\cdot\mathbf{v})\mathbf{I},
$$

then

$$
\rho\left(\partial_t\mathbf{v}+(\mathbf{v}\cdot\nabla)\mathbf{v}\right)
=
-\nabla p
+
\nabla\cdot\boldsymbol{\tau}.
$$

This is the compressible Navier-Stokes form.

In the incompressible limit

$$
\nabla\cdot\mathbf{v}=0,
\qquad
\rho=\text{const.},
$$

it reduces to

$$
\rho\left(\partial_t\mathbf{v}+(\mathbf{v}\cdot\nabla)\mathbf{v}\right)
=
-\nabla p + \eta \nabla^2\mathbf{v}.
$$

So the familiar hydrodynamic equations arise as constitutive limits of the
coarse-grained momentum balance.

## 207.8 What Is Exact and What Is Not

Up to the introduction of $\boldsymbol{\Sigma}$, everything in this appendix is
an exact rewriting of:

- local energy continuity,
- local momentum continuity,
- coarse-grained definitions of density and velocity.

The first constitutive choice enters only when one asks how the unresolved
stress should depend on the resolved fields.

So the exact conclusion is:

> the present program already yields the exact hydrodynamic conservation form.

The further statement

> the effective stress is Newtonian and therefore Navier-Stokes

is an additional closure hypothesis. It is plausible, but it is not automatic.

## 207.9 Physical Interpretation

This derivation matters because it says where fluid behavior would come from in
the present ontology.

- The effective density is coarse-grained stored energy divided by the local
  transport scale squared.

- The effective velocity is coarse-grained energy transport divided by
  coarse-grained stored energy.

- Pressure and viscosity are not primitive substances or forces. They are
  summaries of unresolved local closure and transport encoded in
  $\boldsymbol{\Sigma}$.

So if Navier-Stokes-like dynamics is correct at macroscopic scales, it appears
here as an emergent continuum limit of the same energy substrate, not as a
separate ontology.

## 207.10 Summary

In a region with approximately uniform local transport scale $k$, the already
derived conservation laws imply:

$$
\partial_t \rho + \nabla\cdot(\rho \mathbf{v})=0,
$$

and

$$
\rho\left(\partial_t\mathbf{v}+(\mathbf{v}\cdot\nabla)\mathbf{v}\right)
=
-\nabla p + \nabla\cdot\boldsymbol{\tau},
$$

with $\rho$, $\mathbf{v}$, $p$, and $\boldsymbol{\tau}$ defined by exact
coarse-graining identities up to the final constitutive closure.

Thus the book does not merely point toward hydrodynamics in the abstract. It
already contains the detailed route by which Euler-like and Navier-Stokes-like
equations emerge from continuity, momentum flux, and coarse-graining of the
same underlying transport substrate. Appendix 213 then extends the same
derivation to variable background.
