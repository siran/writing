---
title: The Physics of Energy Flow - Weak Interaction Operator for a Static Mass Closure
date: 2026-03-15
---

# 216. Weak Interaction Operator for a Static Mass Closure

Appendix 215 identified the structural source of the weak-field factor of two:
a null Maxwell probe carries two equal stress sectors. What remained open was
to state, in exact local form, what kind of interaction operator a static
bounded mass closure can exert on a narrow passing probe.

This appendix does that at the leading weak-field level. It isolates the first
nontrivial term in the exact interaction operator, fixes one coefficient from
the Newtonian slow-mode limit, and isolates the one remaining coefficient that
must be determined from the detailed closure of the mass mode itself.

The point is not yet to claim the final gravity derivation is complete. The
point is to reduce the exact gravity problem to one sharp mathematical
question in its weak-field regime.

## 216.1 Setup

Let a bounded static mass mode be centered at the origin. In the weak-field
regime, write its strength as

$$
\eta(r):=\frac{GM}{rc^2},
\qquad
\eta\ll 1.
$$

Consider a narrow probe packet whose support is small compared to the length
scale on which $\eta$ varies. Let

$$
\mathbf{n}
$$

be its local propagation direction, with

$$
|\mathbf{n}|=1.
$$

Write the probe energy density as

$$
u=T^{00},
$$

and define its longitudinal momentum-flux density by

$$
\Pi_n:=-n_in_jT_{ij}.
$$

For a null Maxwell probe, appendix 215 proved

$$
\Pi_n=u.
$$

For a slowly moving bounded probe, $\Pi_n$ is of higher order in $v/c$ and
vanishes in the strict slow-mode limit.

## 216.2 The General Leading Interaction Class

Assume the interaction between the static mass closure and the narrow probe is
expanded in the weak-field parameter and retained through its leading
nontrivial term. At that order the interaction is:

1. local on the scale of the packet,
2. linear in the probe variables,
3. retained only through leading weak-field order in $\eta$ and its gradient,
4. static, parity-even, and spherically symmetric in the rest frame of the mass
   closure.

Because the packet is narrow compared to the background scale, internal probe
gradients contribute only at higher order in the expansion and are not part of
the leading interaction class.

At leading order, the only background scalar is $\eta(r)$ and the only
background vector is

$$
\nabla\eta.
$$

For the probe, the only zeroth-derivative scalars relevant to a narrow packet
are

$$
u,
\qquad
\Pi_n.
$$

The only available vectors at this order are therefore

$$
u\,\nabla\eta,
\qquad
\Pi_n\,\nabla\eta,
\qquad
u\,(\mathbf n\cdot\nabla\eta)\mathbf n,
\qquad
\Pi_n\,(\mathbf n\cdot\nabla\eta)\mathbf n.
$$

No pseudovector term is allowed, because the mass closure is static and
spherically symmetric and introduces no handedness.

Hence the most general leading weak-field local force density has the form

$$
\mathbf f
=
-A\,u\,\nabla\eta
-B\,\Pi_n\,\nabla\eta
-C\,u\,(\mathbf n\cdot\nabla\eta)\mathbf n
-D\,\Pi_n\,(\mathbf n\cdot\nabla\eta)\mathbf n,
$$

for dimensionless coefficients

$$
A,\ B,\ C,\ D.
$$

This is the full leading weak-field interaction class under the stated
assumptions.

## 216.3 Transverse Bending Depends on Two Coefficients Only

For deflection, only the part perpendicular to $\mathbf n$ matters. Define the
transverse projector

$$
P_\perp:=I-\mathbf n\otimes\mathbf n.
$$

Then

$$
\nabla_\perp\eta:=P_\perp\nabla\eta
=
\nabla\eta-(\mathbf n\cdot\nabla\eta)\mathbf n.
$$

Applying $P_\perp$ to the general interaction law removes the longitudinal
terms:

$$
\mathbf f_\perp
=
P_\perp\mathbf f
=
-A\,u\,\nabla_\perp\eta
-B\,\Pi_n\,\nabla_\perp\eta.
$$

So the bending problem depends only on

$$
A,\qquad B.
$$

The coefficients $C$ and $D$ affect only longitudinal transport bookkeeping,
not the leading weak-field deflection angle.

## 216.4 Newtonian Calibration Fixes $A=1$

Take a slowly moving bounded probe. In the strict slow-mode limit,

$$
\Pi_n=o(u),
$$

so the leading transverse force density becomes

$$
\mathbf f_\perp=-A\,u\,\nabla_\perp\eta.
$$

Integrating over the packet gives

$$
\mathbf F_\perp=-A\,U\,\nabla_\perp\eta,
\qquad
U:=\int u\,dV.
$$

For a bounded mode of total energy $U$, chapter 9 and chapter 12 identify the
effective inertial mass as

$$
m=\frac{U}{c^2}.
$$

The Newtonian potential of the central mass is

$$
\Phi(r)=-\frac{GM}{r}=-c^2\eta(r),
$$

so the Newtonian force is

$$
\mathbf F_{\mathrm N}
=
-m\,\nabla\Phi
=
-\frac{U}{c^2}\,\nabla(-c^2\eta)
=
-U\,\nabla\eta.
$$

Therefore the slow-mode limit fixes

$$
\boxed{
A=1
}.
$$

So the general transverse interaction law reduces to

$$
\boxed{
\mathbf f_\perp
=
-\bigl(u+B\Pi_n\bigr)\nabla_\perp\eta
}.
$$

## 216.5 Null Maxwell Probe

For a null Maxwell probe, appendix 215 gives

$$
\Pi_n=u.
$$

Therefore

$$
\mathbf f_\perp
=
-(1+B)\,u\,\nabla_\perp\eta.
$$

Integrating over the packet,

$$
\mathbf F_\perp
=
-(1+B)\,U\,\nabla_\perp\eta.
$$

Since the packet momentum magnitude is

$$
P=\frac{U}{c},
$$

the change in direction is

$$
d\theta
=
\frac{|\mathbf F_\perp|}{P}\,dt
=
\frac{c}{U}(1+B)\,U\,|\nabla_\perp\eta|\,dt.
$$

Along the unperturbed straight path,

$$
dt=\frac{dz}{c},
$$

so

$$
d\theta=(1+B)\,|\nabla_\perp\eta|\,dz.
$$

Hence the total weak deflection is

$$
\theta=(1+B)\int_{-\infty}^{\infty}|\nabla_\perp\eta|\,dz.
$$

For

$$
\eta(r)=\frac{GM}{c^2\sqrt{b^2+z^2}},
$$

one has

$$
|\nabla_\perp\eta|
=
\frac{GM\,b}{c^2(b^2+z^2)^{3/2}},
$$

and therefore

$$
\int_{-\infty}^{\infty}|\nabla_\perp\eta|\,dz
=
\frac{2GM}{bc^2}.
$$

So the general weak bending formula in the stated interaction class is

$$
\boxed{
\theta=(1+B)\frac{2GM}{bc^2}
}.
$$

This isolates the exact role of the remaining coefficient:

- if $B=0$, one gets the Newtonian half-value,
- if $B=1$, one gets the full null value
  $$
  \theta=\frac{4GM}{bc^2}.
  $$

## 216.6 Interpretation of $B$

In the leading weak-field truncation, the coefficient $B$ measures how
strongly the static mass closure couples to the longitudinal momentum flux of
the probe, in addition to its stored energy density.

So the remaining gravity question is no longer vague. It is:

> for a bounded static mass closure of the common electromagnetic substrate,
> what is the coefficient $B$ in the weak interaction operator?

The same-substrate reading suggests the natural candidate

$$
B=1,
$$

because the probe's stored energy and carried momentum flux are not different
substances. They are two aspects of the same organized transport.

But that value should still be derived from the detailed interaction of the
mass closure with the probe, not merely preferred philosophically.

## 216.7 What Has Been Reduced

Before this appendix, the open gravity step could be described only loosely as
"derive the interaction."

Now the open step is reduced to one coefficient in one explicit operator class.

The following are already fixed:

- the admissible leading local interaction class,
- the Newtonian calibration
  $$
  A=1,
  $$
- the null Maxwell identity
  $$
  \Pi_n=u,
  $$
- the resulting deflection formula
  $$
  \theta=(1+B)\frac{2GM}{bc^2}.
  $$

What remains is only this:

- derive the coefficient $B$ from the detailed same-substrate interaction of a
  bounded mass closure with a null Maxwell probe.

## 216.8 Summary

For a static spherical mass closure and a narrow probe, the most general
leading transverse interaction law is

$$
\mathbf f_\perp
=
-\bigl(Au+B\Pi_n\bigr)\nabla_\perp\eta.
$$

The Newtonian slow-mode limit fixes

$$
A=1.
$$

For a null Maxwell probe,

$$
\Pi_n=u,
$$

so

$$
\theta=(1+B)\frac{2GM}{bc^2}.
$$

Therefore the full weak-field light-bending value is obtained exactly when

$$
B=1.
$$

The gravity program is thus reduced to a sharp remaining task:

> derive $B=1$ from the detailed interaction of the bounded mass closure and
> the passing null Maxwell probe.
