---
title: The Physics of Energy Flow - 222 Boundary Unloading by Superposition
date: 2026-03-17
---

# 222. Boundary Unloading by Superposition

Appendices 219 and 221 showed that a lower-loading region can act as a faster
transport corridor. The missing step is the unloading mechanism itself.

For passive source-free Maxwellian transport, that mechanism is already
available. It is the combination of:

- boundary determination of the passive interior,
- linear superposition of source-free fields,
- and the quadratic form of electromagnetic energy density.

So the fundamental point is not yet engineering. It is simply this: given
boundary control of a passive region, one can subtract as well as reinforce the
interior field.

## 222.1 Linear Dependence on Boundary Data

Let $\Omega$ be a passive bounded region with smooth closed boundary
$\partial\Omega$. Let $B$ denote the complete boundary transport data fed
through $\partial\Omega$ over the relevant causal interval.

For source-free linear Maxwellian transport, the interior resolved field
depends linearly on that boundary data. Writing

$$
\mathcal F[B] = (\mathbf E[B],\mathbf H[B]),
$$

linearity gives

$$
\mathcal F[B_1+B_2]=\mathcal F[B_1]+\mathcal F[B_2].
$$

Therefore boundary control can add or subtract admissible interior field
components.

This is the first fundamental fact.

## 222.2 Exact Energy Reduction of a Selected Component

Take any boundary-driven interior field component

$$
(\mathbf E_0,\mathbf H_0)
$$

in the target region.

Now choose a second boundary control that excites the same component with
opposite phase and relative amplitude $\lambda$, where

$$
0\le \lambda \le 1.
$$

That is,

$$
(\mathbf E_1,\mathbf H_1)
=
-\lambda(\mathbf E_0,\mathbf H_0).
$$

By superposition, the total field becomes

$$
(\mathbf E_\lambda,\mathbf H_\lambda)
=
(1-\lambda)(\mathbf E_0,\mathbf H_0).
$$

The electromagnetic energy density is

$$
u
=
\frac12\bigl(\varepsilon E^2+\mu H^2\bigr),
$$

and the Poynting flux is

$$
\mathbf S = \mathbf E\times\mathbf H.
$$

So for this same-mode subtraction,

$$
u_\lambda=(1-\lambda)^2u_0,
\qquad
\mathbf S_\lambda=(1-\lambda)^2\mathbf S_0.
$$

This reduction is exact. It is not heuristic. It follows from the quadratic
form of energy density and the bilinear form of flux.

At $\lambda=1$, the selected component is canceled completely.

## 222.3 Guided-Mode Version

In a tube or corridor geometry, let the dominant passive mode have the form

$$
(\mathbf E_0,\mathbf H_0)
=
A\,(\mathbf e,\mathbf h)(x_\perp)\,e^{i(\beta z-\omega t)}.
$$

If the boundary actuation injects the same mode with amplitude

$$
-\lambda A,
$$

then the resulting mode amplitude inside the target region is

$$
(1-\lambda)A.
$$

So the interior loading of that mode is reduced by the exact factor

$$
(1-\lambda)^2.
$$

This is the fundamental boundary-unloading mechanism for a transport corridor:
mode-wise subtraction by phase-opposed superposition.

The exact boundary pattern needed to realize the desired subtraction is the
engineering problem. The unloading mechanism itself is already forced by the
linearity of the passive interior.

## 222.4 Relation to Local Transport Speed

Appendices 214 and 219 work in the symmetric constitutive class

$$
\varepsilon=\varepsilon_0\alpha,
\qquad
\mu=\mu_0\alpha,
\qquad
k=\frac{c}{\alpha}.
$$

Within that class, lower local loading means larger local transport speed.
Therefore any boundary program that lowers the resolved background load in a
region raises the local transport speed there relative to the more heavily
loaded case.

That is the fundamental basis of a high-speed transport corridor.

The important limit is also clear. Exact cancellation of the selected carrier
component gives zero load in that component; it does not by itself provide a
working guide or an infinite-speed theorem. Corridor design therefore uses
controlled unloading, or unloading of a background component while preserving a
separate signal-bearing structure.

## 222.5 Final Statement

Given boundary control of a passive region, one can subtract admissible
Maxwellian modes as well as reinforce them. Because the field equations are
linear and the electromagnetic energy density is quadratic, phase-opposed
boundary control lowers interior energy exactly.

So the corridor idea does have a clean first-principles derivation:

- passive interior fields are boundary-determined,
- boundary-determined fields superpose linearly,
- opposite-phase excitation subtracts a selected interior mode,
- and that subtraction lowers the local loading that sets transport speed.

Appendix 221 then gives the corresponding lensing and guidance consequences
once such a loading profile has been engineered.
