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

## 209.4 Moving Aperture Transport

The rest-frame theorem gives the monopole coupling of the toroidal charge class
to a smooth electric load. To get the moving magnetic term, one should not
jump immediately to a covariant ansatz. The torus itself already tells us what
has to be sampled: a moving aperture of one common field.

Let

$$
\Sigma_\varepsilon(t)
$$

be a spanning surface across the torus aperture, transported with the compact
mode, and let

$$
\mathbf u(\mathbf y,t)
$$

be the local velocity of the material point

$$
\mathbf y\in \Sigma_\varepsilon(t).
$$

For any moving surface, Maxwell-Faraday transport gives

$$
\frac{d}{dt}\int_{\Sigma_\varepsilon(t)}\mathbf B_{\mathrm e}\cdot d\mathbf A
=
-\oint_{\partial\Sigma_\varepsilon(t)}
\bigl(
\mathbf E_{\mathrm e}
+
\mathbf u\times \mathbf B_{\mathrm e}
\bigr)\cdot d\boldsymbol\ell.
$$

So the local field sampled by a moving aperture is not

$$
\mathbf E_{\mathrm e}
$$

alone, but

$$
\mathbf E_{\mathrm e}+\mathbf u\times\mathbf B_{\mathrm e}.
$$

This is the transport meaning of the magnetic term.

For a rigidly drifting compact torus, decompose

$$
\mathbf u(\mathbf y,t)=\mathbf v(t)+\mathbf u_{\mathrm{int}}(\mathbf y,t),
$$

where

$$
\mathbf v(t)=\dot{\mathbf X}(t)
$$

is the drift of the torus center and

$$
\mathbf u_{\mathrm{int}}
$$

is the internal helical traversal of the closure.

Define the aperture average of a field over $\Sigma_\varepsilon(t)$ by

$$
\langle \mathbf W\rangle_{\Sigma_\varepsilon(t)}
:=
\frac{1}{A(\Sigma_\varepsilon(t))}
\int_{\Sigma_\varepsilon(t)}\mathbf W\,dA.
$$

Because the external field is smooth on the compact scale,

$$
\langle \mathbf E_{\mathrm e}\rangle_{\Sigma_\varepsilon(t)}
=
\mathbf E_{\mathrm e}(\mathbf X(t),t)+O(\varepsilon),
$$

$$
\langle \mathbf B_{\mathrm e}\rangle_{\Sigma_\varepsilon(t)}
=
\mathbf B_{\mathrm e}(\mathbf X(t),t)+O(\varepsilon).
$$

For the equal-winding axisymmetric torus, the internal traversal has no
monopole average across the aperture:

$$
\langle \mathbf u_{\mathrm{int}}\rangle_{\Sigma_\varepsilon(t)}=0.
$$

Geometrically, opposite points of the aperture carry opposite tangential
traversal velocities, so the internal helical motion cancels at monopole
order. It affects only higher multipoles.

Therefore

$$
\left\langle
\mathbf E_{\mathrm e}
+
\mathbf u\times\mathbf B_{\mathrm e}
\right\rangle_{\Sigma_\varepsilon(t)}
=
\mathbf E_{\mathrm e}(\mathbf X(t),t)
+
\mathbf v(t)\times\mathbf B_{\mathrm e}(\mathbf X(t),t)
+
O(\varepsilon).
$$

The moving compact torus therefore samples the smooth external field through
the effective transport load

$$
\boxed{
\mathbf L_{\mathrm{mov}}
=
\mathbf E_{\mathrm e}(\mathbf X(t),t)
+
\mathbf v(t)\times\mathbf B_{\mathrm e}(\mathbf X(t),t)
}.
$$

## 209.5 Compact Moving-Mode Theorem

Section 209.3 proved that the compact toroidal charge class couples at
monopole order by

$$
q\times(\text{smooth load sampled across the aperture}).
$$

For a static torus, that sampled load is

$$
\mathbf E_{\mathrm e}(X).
$$

For a translating torus, section 209.4 shows that the sampled load is

$$
\mathbf L_{\mathrm{mov}}
=
\mathbf E_{\mathrm e}(\mathbf X(t),t)
+
\mathbf v(t)\times\mathbf B_{\mathrm e}(\mathbf X(t),t).
$$

Therefore, in the same compact two-scale limit,

$$
\boxed{
\mathbf F
=
q\,\mathbf L_{\mathrm{mov}}
=
q\bigl(
\mathbf E_{\mathrm e}
+
\mathbf v\times\mathbf B_{\mathrm e}
\bigr)
}.
$$

This is the Lorentz-force form at compact toroidal monopole order.

The associated power law follows immediately:

$$
\frac{dE}{dt}
=
\mathbf F\cdot\mathbf v
=
q\,\mathbf E_{\mathrm e}\cdot\mathbf v,
$$

because

$$
(\mathbf v\times\mathbf B_{\mathrm e})\cdot\mathbf v=0.
$$

So the magnetic part redirects transport but does no work.

## 209.6 What the Derivation Used

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
5. Maxwell-Faraday transport for a moving aperture,
6. cancellation of the internal helical traversal at monopole order for an
   axisymmetric compact torus.

No effective source density was needed.

The role of the equal-winding $(m,m)$ torus was only to give a clean axis and a
clean aperture-flux class. The Lorentz law depends only on the resulting scalar
$q$ at monopole order. All finer toroidal geometry survives only in higher
multipole corrections beyond the point-mode limit.

## 209.7 Interpretation

Within this framework, the Lorentz force is not a primitive rule about a
particle being pushed by an external field.

It is the compact expression of one exact statement:

- a charged body is a bounded toroidal closure of one common field,
- its signed through-hole flux class determines the monopole coefficient $q$,
- external stress transfers momentum across a shrinking sphere around that
  closure,
- the moving aperture samples the same field through
  $$
  \mathbf E_{\mathrm e}+\mathbf v\times\mathbf B_{\mathrm e},
  $$
- internal helical traversal cancels at monopole order, leaving only the drift
  correction.

So the Lorentz law is not imported. It is the point-mode limit of toroidal
boundary stress transfer together with moving-aperture transport.

## 209.8 Summary

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

For a moving compact torus, the transported aperture samples the smooth
external field through

$$
\mathbf E_{\mathrm e}+\mathbf v\times\mathbf B_{\mathrm e}.
$$

Therefore the compact toroidal monopole force is

$$
\frac{d\mathbf p}{dt}
=
q\bigl(\mathbf E_{\mathrm e}+\mathbf v\times\mathbf B_{\mathrm e}\bigr).
$$

Thus the Lorentz-force form is derived here directly from first principles at
compact toroidal monopole order: compact toroidal charge, exact source-free
stress transfer, and moving-aperture transport of one common electromagnetic
substrate.
