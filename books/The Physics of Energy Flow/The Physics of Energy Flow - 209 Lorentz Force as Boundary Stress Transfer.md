---
title: The Physics of Energy Flow - Lorentz Force as Boundary Stress Transfer
date: 2026-03-15
---

# 209. Lorentz Force as Boundary Stress Transfer

This appendix derives the Lorentz-force form directly from the source-free
stress transfer of a compact toroidal charged mode.

No effective charge density or current density is introduced. The bounded mode
is a self-closing toroidal organization of one continuous field. The familiar
Lorentz formula appears as the exact point-mode limit of its interaction with a
smooth external Maxwell field.

For definiteness, take the compact mode to be an axisymmetric torus with equal
winding class $(m,m)$ and symmetry axis $\hat{\mathbf a}$. Nothing essential
depends on that simplifying choice. It only makes the geometric bookkeeping
cleaner. The leading interaction depends solely on the signed through-hole flux
class carried along the torus axis. All finer toroidal structure enters only
through higher multipoles.

## 209.1 Compact Toroidal Charged Modes

Let

$$
K_\varepsilon
$$

be a coherent toroidal charged mode of size $\varepsilon$, centered at the
worldline

$$
X(\tau),
$$

with proper time $\tau$.

Chapter 10 associated charge with the signed through-hole flux class across the
torus aperture. Write that class as the scalar

$$
q.
$$

In the instantaneous rest frame of the mode, choose Cartesian coordinates with
origin at the center of energy and let

$$
\mathbf r = R\,\mathbf n,
\qquad
|\mathbf n|=1.
$$

The compact toroidal mode is assumed to have the far-field behavior established
in chapter 10:

$$
\mathbf E_{\mathrm s}(\mathbf r)
=
\frac{q}{4\pi\varepsilon_0}\frac{\mathbf n}{R^2}
+
\mathbf e_{\mathrm{rem}}(\mathbf r),
$$

$$
\mathbf B_{\mathrm s}(\mathbf r)
=
\mathbf b_{\mathrm{rem}}(\mathbf r),
$$

with bounds

$$
|\mathbf e_{\mathrm{rem}}(\mathbf r)|
\le
C_E\frac{\varepsilon}{R^3},
\qquad
|\mathbf b_{\mathrm{rem}}(\mathbf r)|
\le
C_B\frac{\varepsilon}{R^3},
$$

for every

$$
R\ge 2\varepsilon.
$$

So the leading exterior field of the compact torus is the inverse-square
monopole term determined by the through-hole flux class, while all finer
toroidal structure decays at least one power faster.

Let the external Maxwell field be smooth near the mode center. On a sphere

$$
S_R:=\{\,\mathbf x : |\mathbf x-X(\tau)|=R\,\},
$$

write

$$
\mathbf E_{\mathrm e}(X(\tau)+R\mathbf n,\tau)
=
\mathbf E_0(\tau)+\mathbf E_1(R,\mathbf n,\tau),
$$

$$
\mathbf B_{\mathrm e}(X(\tau)+R\mathbf n,\tau)
=
\mathbf B_0(\tau)+\mathbf B_1(R,\mathbf n,\tau),
$$

with

$$
|\mathbf E_1(R,\mathbf n,\tau)|\le C'_E R,
\qquad
|\mathbf B_1(R,\mathbf n,\tau)|\le C'_B R.
$$

This is just the first-order smoothness expansion of the external field near
the mode center.

## 209.2 Exact Source-Free Interaction Balance

Let the total field be

$$
\mathbf E=\mathbf E_{\mathrm s}+\mathbf E_{\mathrm e},
\qquad
\mathbf B=\mathbf B_{\mathrm s}+\mathbf B_{\mathrm e}.
$$

Everywhere outside the compact toroidal core, the total field is source-free,
so the exact local momentum balance is

$$
\partial_t g_i - \partial_j T_{ij}=0,
$$

where

$$
\mathbf g=\varepsilon_0\,\mathbf E\times\mathbf B,
$$

and

$$
T_{ij}
=
\varepsilon_0\left(E_iE_j-\frac{1}{2}\delta_{ij}\mathbf E^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j-\frac{1}{2}\delta_{ij}\mathbf B^2\right).
$$

Decompose

$$
\mathbf g
=
\mathbf g_{\mathrm s}
+
\mathbf g_{\mathrm e}
+
\mathbf g_{\times},
$$

$$
\mathbf T
=
\mathbf T_{\mathrm s}
+
\mathbf T_{\mathrm e}
+
\mathbf T_{\times},
$$

where the cross terms are

$$
\mathbf g_{\times}
:=
\varepsilon_0\bigl(
\mathbf E_{\mathrm s}\times\mathbf B_{\mathrm e}
+
\mathbf E_{\mathrm e}\times\mathbf B_{\mathrm s}
\bigr),
$$

and

$$
(T_{\times})_{ij}
:=
\varepsilon_0\left(
E_{{\mathrm s}i}E_{{\mathrm e}j}
+
E_{{\mathrm e}i}E_{{\mathrm s}j}
-
\delta_{ij}\,\mathbf E_{\mathrm s}\cdot\mathbf E_{\mathrm e}
\right)
+
\frac{1}{\mu_0}\left(
B_{{\mathrm s}i}B_{{\mathrm e}j}
+
B_{{\mathrm e}i}B_{{\mathrm s}j}
-
\delta_{ij}\,\mathbf B_{\mathrm s}\cdot\mathbf B_{\mathrm e}
\right).
$$

Subtracting the self and external balances from the total balance gives the
exact cross-balance

$$
\partial_t(\mathbf g_{\times})_i
-
\partial_j(T_{\times})_{ij}
=
0.
$$

Integrating over the ball

$$
B_R:=\{\,\mathbf x : |\mathbf x-X(\tau)|\le R\,\}
$$

gives

$$
\frac{d}{dt}\int_{B_R}\mathbf g_{\times}\,dV
=
\int_{S_R}\mathbf T_{\times}\cdot\mathbf n\,dA.
$$

For the monist reading used in this book, the right-hand side is the exact rate
at which external stress transfers momentum into the compact closure across the
surrounding sphere.

Define therefore

$$
\mathbf F_R(\tau)
:=
\int_{S_R}\mathbf T_{\times}\cdot\mathbf n\,dA.
$$

The Lorentz force will be the exact limit of $\mathbf F_R$ as the mode is
shrunk to a point while the surrounding sphere shrinks with it but remains
outside the toroidal core.

## 209.3 Rest-Frame Compact-Mode Theorem

Choose an event on the worldline and work in the instantaneous rest frame of
the toroidal mode at that event.

Let

$$
\alpha(R):=\frac{q}{4\pi\varepsilon_0 R^2}.
$$

On $S_R$ write

$$
\mathbf E_{\mathrm s}
=
\alpha(R)\,\mathbf n + \mathbf e_{\mathrm{rem}},
$$

with

$$
|\mathbf e_{\mathrm{rem}}|\le C_E\frac{\varepsilon}{R^3},
\qquad
|\mathbf B_{\mathrm s}|\le C_B\frac{\varepsilon}{R^3}.
$$

The electric cross term on the sphere is

$$
\mathbf T_{\times}^{(E)}\cdot\mathbf n
=
\varepsilon_0\left[
(\mathbf E_{\mathrm s}\cdot\mathbf n)\mathbf E_{\mathrm e}
+
(\mathbf E_{\mathrm e}\cdot\mathbf n)\mathbf E_{\mathrm s}
-
(\mathbf E_{\mathrm s}\cdot\mathbf E_{\mathrm e})\mathbf n
\right].
$$

Substitute

$$
\mathbf E_{\mathrm s}=\alpha\mathbf n+\mathbf e_{\mathrm{rem}},
\qquad
\mathbf E_{\mathrm e}=\mathbf E_0+\mathbf E_1.
$$

The leading terms simplify exactly:

$$
\varepsilon_0\left[
(\alpha\mathbf n\cdot\mathbf n)\mathbf E_0
+
(\mathbf E_0\cdot\mathbf n)\alpha\mathbf n
-
(\alpha\mathbf n\cdot\mathbf E_0)\mathbf n
\right]
=
\varepsilon_0\,\alpha\,\mathbf E_0.
$$

So

$$
\mathbf T_{\times}^{(E)}\cdot\mathbf n
=
\frac{q}{4\pi R^2}\,\mathbf E_0
+
\mathbf R_E(R,\mathbf n),
$$

where the remainder satisfies

$$
|\mathbf R_E(R,\mathbf n)|
\le
C_1\frac{|q|}{R^2}\,R
+
C_2\frac{\varepsilon}{R^3}.
$$

Therefore

$$
\int_{S_R}\mathbf T_{\times}^{(E)}\cdot\mathbf n\,dA
=
q\,\mathbf E_0
+
O(R)
+
O\!\left(\frac{\varepsilon}{R}\right).
$$

For the magnetic cross term,

$$
\mathbf T_{\times}^{(B)}\cdot\mathbf n
=
\frac{1}{\mu_0}\left[
(\mathbf B_{\mathrm s}\cdot\mathbf n)\mathbf B_{\mathrm e}
+
(\mathbf B_{\mathrm e}\cdot\mathbf n)\mathbf B_{\mathrm s}
-
(\mathbf B_{\mathrm s}\cdot\mathbf B_{\mathrm e})\mathbf n
\right],
$$

so

$$
\left|
\int_{S_R}\mathbf T_{\times}^{(B)}\cdot\mathbf n\,dA
\right|
\le
C_3\,R^2\sup_{S_R}|\mathbf B_{\mathrm s}|\,\sup_{S_R}|\mathbf B_{\mathrm e}|
=
O\!\left(\frac{\varepsilon}{R}\right).
$$

Hence

$$
\mathbf F_R
=
q\,\mathbf E_0
+
O(R)
+
O\!\left(\frac{\varepsilon}{R}\right).
$$

Take a two-scale limit in which

$$
\varepsilon\to 0,
\qquad
R\to 0,
\qquad
\frac{\varepsilon}{R}\to 0.
$$

Then

$$
\boxed{
\lim_{\varepsilon\to 0}\mathbf F_R
=
q\,\mathbf E_0
}.
$$

So a compact toroidal charged mode at rest experiences exactly the electric
force

$$
\mathbf F_{\mathrm{rest}}=q\,\mathbf E_{\mathrm e}(X).
$$

No magnetic term appears in the rest frame, because the static toroidal mode
has no magnetic monopole part. The toroidal details affect only the discarded
higher multipoles.

## 209.4 Exact Covariant Extension

The previous sections used only source-free stress continuity and the compact
toroidal asymptotics of chapter 10. To pass from the instantaneous rest frame
to an arbitrary inertial frame, use the transport covariance already developed
earlier in the book.

Let

$$
U^\mu
$$

be the four-velocity of the compact toroidal mode, and let

$$
F^{\mu\nu}_{\mathrm e}
$$

be the external field tensor, with convention

$$
F^{0i}=-\frac{E_i}{c},
\qquad
F^{i0}=\frac{E_i}{c},
\qquad
F^{ij}=-\varepsilon^{ijk}B_k.
$$

In the instantaneous rest frame, the theorem above gives the four-force

$$
f'^\mu=(0,q\mathbf E').
$$

Now ask for the exact covariant extension that is:

1. linear in the external field,
2. linear in the charge class $q$,
3. orthogonal to $U^\mu$,
4. equal to $(0,q\mathbf E')$ in the rest frame.

At a point, the only covariant vectors linear in $F^{\mu\nu}_{\mathrm e}$ and
$U^\mu$ are

$$
F^{\mu\nu}_{\mathrm e}U_\nu,
\qquad
{}^\star\!F^{\mu\nu}_{\mathrm e}U_\nu.
$$

The dual term is excluded, because in the rest frame it would couple the
toroidal electric charge class to the magnetic field instead of the electric
field. That would contradict the rest-frame theorem just proved.

Therefore the unique exact covariant extension is

$$
\boxed{
f^\mu
=
q\,F^{\mu\nu}_{\mathrm e}U_\nu
}.
$$

Write

$$
U^\mu=\gamma(c,\mathbf v).
$$

Then

$$
f^0
=
\gamma\,\frac{q}{c}\,\mathbf E\cdot\mathbf v,
$$

and

$$
f^i
=
\gamma\,q\bigl(\mathbf E+\mathbf v\times\mathbf B\bigr)^i.
$$

Since

$$
f^\mu=\frac{dP^\mu}{d\tau},
\qquad
\frac{dP^i}{d\tau}
=
\gamma\,\frac{dp^i}{dt},
$$

it follows that

$$
\boxed{
\frac{d\mathbf p}{dt}
=
q\bigl(\mathbf E+\mathbf v\times\mathbf B\bigr)
}.
$$

This is exactly the Lorentz force law.

The temporal component gives the power law

$$
\frac{dE}{dt}
=
q\,\mathbf E\cdot\mathbf v.
$$

So the full relativistic force-energy relation is recovered at the same time.

## 209.5 What the Derivation Used

The argument used only the following ingredients:

1. source-free Maxwell stress continuity,
2. the toroidal charge interpretation of chapter 10,
3. the compact-mode far-field asymptotic
   $$
   \mathbf E_{\mathrm s}
   =
   \frac{q}{4\pi\varepsilon_0}\frac{\mathbf n}{R^2}
   +
   O\!\left(\frac{\varepsilon}{R^3}\right),
   $$
4. smoothness of the external field near the mode center,
5. transport covariance already established elsewhere in the book.

No effective source density was needed.

The role of the equal-winding $(m,m)$ torus was only to give a clean axis and a
clean aperture-flux class. The Lorentz law depends only on the resulting scalar
$q$ at monopole order. All finer toroidal geometry survives only in higher
multipole corrections beyond the point-mode limit.

## 209.6 Interpretation

Within this framework, the Lorentz force is not a primitive rule about a
particle being pushed by an external field.

It is the compact expression of one exact statement:

- a charged body is a bounded toroidal closure of one common field,
- its signed through-hole flux class determines the monopole coefficient $q$,
- external stress transfers momentum across a shrinking sphere around that
  closure,
- transport covariance turns the rest-frame electric result into the exact
  moving-frame Lorentz form.

So the Lorentz law is not imported. It is the point-mode limit of toroidal
boundary stress transfer.

## 209.7 Summary

For a compact toroidal charged mode, the exact source-free cross-stress
transfer across a sphere $S_R$ is

$$
\mathbf F_R
=
\int_{S_R}\mathbf T_{\times}\cdot\mathbf n\,dA.
$$

In the instantaneous rest frame, the compact-mode limit gives

$$
\lim_{\varepsilon\to 0}\mathbf F_R
=
q\,\mathbf E_{\mathrm e}(X).
$$

Transport covariance then forces the unique exact extension

$$
f^\mu=q\,F^{\mu\nu}_{\mathrm e}U_\nu,
$$

whose spatial part is

$$
\frac{d\mathbf p}{dt}
=
q\bigl(\mathbf E+\mathbf v\times\mathbf B\bigr).
$$

Thus the Lorentz-force form is derived here directly from first principles:
compact toroidal charge, exact source-free stress transfer, and covariant
transport of one common electromagnetic substrate.
