---
title: The Physics of Energy Flow - Two-Charge Interaction as Cross-Stress Transfer
date: 2026-03-14
---

# 210. Two-Charge Interaction as Cross-Stress Transfer

This appendix derives the exact interaction formula for two localized charged
modes at the effective-source level and then recovers the Coulomb law in the
static point-mode idealization.

The point is the same as in appendix 209. No primitive action-at-a-distance is
introduced. The interaction is the momentum transferred through the organized
field between two bounded closures.

## 210.1 Two Localized Charged Modes

Let two disjoint bounded regions

$$
K_1,\qquad K_2
$$

contain two localized charged modes.

At scales large compared to their internal toroidal closure, represent them by
effective charge and current densities

$$
\rho_1,\ \mathbf{J}_1,
\qquad
\rho_2,\ \mathbf{J}_2.
$$

Let their corresponding fields be

$$
(\mathbf{E}_1,\mathbf{B}_1),
\qquad
(\mathbf{E}_2,\mathbf{B}_2),
$$

so that each pair satisfies

$$
\nabla\cdot\mathbf{E}_a=\frac{\rho_a}{\varepsilon_0},
$$

$$
\nabla\times\mathbf{B}_a-\frac{1}{c^2}\partial_t\mathbf{E}_a
=
\mu_0\mathbf{J}_a,
$$

$$
\partial_t\rho_a+\nabla\cdot\mathbf{J}_a=0,
\qquad a=1,2.
$$

The total field is

$$
\mathbf{E}=\mathbf{E}_1+\mathbf{E}_2,
\qquad
\mathbf{B}=\mathbf{B}_1+\mathbf{B}_2.
$$

## 210.2 Exact Local Cross-Interaction Balance

At the effective-source level, the local momentum balance is

$$
\partial_t\mathbf{g}-\nabla\cdot\mathbf{T}
=
-\bigl(\rho\mathbf{E}+\mathbf{J}\times\mathbf{B}\bigr),
$$

with

$$
\mathbf{g}=\varepsilon_0\,\mathbf{E}\times\mathbf{B},
$$

and

$$
T_{ij}
=
\varepsilon_0\left(E_iE_j-\frac{1}{2}\delta_{ij}\mathbf{E}^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j-\frac{1}{2}\delta_{ij}\mathbf{B}^2\right).
$$

Apply that law once to the total field and once to each mode separately, then
subtract the two self-balance laws from the total balance law.

Define the cross field-momentum density

$$
\mathbf{g}_{\times}
:=
\varepsilon_0\bigl(\mathbf{E}_1\times\mathbf{B}_2
+
\mathbf{E}_2\times\mathbf{B}_1\bigr),
$$

and the cross Maxwell stress tensor

$$
(T_{\times})_{ij}
:=
\varepsilon_0\left(E_{1i}E_{2j}+E_{2i}E_{1j}
-\delta_{ij}\,\mathbf{E}_1\cdot\mathbf{E}_2\right)
+
\frac{1}{\mu_0}\left(B_{1i}B_{2j}+B_{2i}B_{1j}
-\delta_{ij}\,\mathbf{B}_1\cdot\mathbf{B}_2\right).
$$

Then the exact local cross-interaction balance is

$$
\partial_t\mathbf{g}_{\times}
-\nabla\cdot\mathbf{T}_{\times}
=
-\bigl(
\rho_1\mathbf{E}_2+\mathbf{J}_1\times\mathbf{B}_2
+
\rho_2\mathbf{E}_1+\mathbf{J}_2\times\mathbf{B}_1
\bigr).
$$

This is the exact local momentum balance for the interaction between the two
modes.

Nothing has been approximated. The right-hand side is the mutual force density,
and the left-hand side is the change of cross field momentum together with the
cross stress transmitted through boundaries.

## 210.3 Exact Force on One Mode Due to the Other

Let $V_1$ be any region containing $K_1$ but not $K_2$. Inside $V_1$ we have

$$
\rho_2=0,
\qquad
\mathbf{J}_2=0.
$$

Integrating the cross-interaction balance over $V_1$ gives

$$
\frac{d}{dt}\int_{V_1}\mathbf{g}_{\times}\,dV
-\int_{\partial V_1}\mathbf{T}_{\times}\cdot\mathbf{n}\,dA
=
-\int_{V_1}
\bigl(\rho_1\mathbf{E}_2+\mathbf{J}_1\times\mathbf{B}_2\bigr)\,dV.
$$

Therefore the exact force exerted by mode 2 on mode 1 is

$$
\mathbf{F}_{1\leftarrow 2}
:=
\int_{V_1}
\bigl(\rho_1\mathbf{E}_2+\mathbf{J}_1\times\mathbf{B}_2\bigr)\,dV
$$

$$
=
\frac{d}{dt}\int_{V_1}\mathbf{g}_{\times}\,dV
+
\int_{\partial V_1}\mathbf{T}_{\times}\cdot\mathbf{n}\,dA.
$$

Similarly, if $V_2$ contains $K_2$ but not $K_1$, then

$$
\mathbf{F}_{2\leftarrow 1}
=
\int_{V_2}
\bigl(\rho_2\mathbf{E}_1+\mathbf{J}_2\times\mathbf{B}_1\bigr)\,dV
$$

$$
=
\frac{d}{dt}\int_{V_2}\mathbf{g}_{\times}\,dV
+
\int_{\partial V_2}\mathbf{T}_{\times}\cdot\mathbf{n}\,dA.
$$

These formulas are exact. They say that the interaction between the two modes
is carried entirely by cross stress and cross field momentum.

## 210.4 Total Momentum Exchange and Action-Reaction

Assume both modes are localized so that the fields decay sufficiently fast at
spatial infinity. Integrating the cross-interaction balance over all space
gives

$$
\mathbf{F}_{1\leftarrow 2}+\mathbf{F}_{2\leftarrow 1}
=
-\frac{d}{dt}\int_{\mathbb{R}^3}\mathbf{g}_{\times}\,dV,
$$

because the boundary term at infinity vanishes.

So the sum of the mechanical forces on the two modes is not generally zero by
itself. It is balanced by the time variation of the momentum stored in the
interaction field between them.

Only when the cross field momentum is stationary do we obtain

$$
\mathbf{F}_{1\leftarrow 2}=-\mathbf{F}_{2\leftarrow 1}.
$$

Thus even the action-reaction question is resolved here by momentum continuity,
not by primitive pairwise postulate.

## 210.5 Compact-Mode Limit

Assume the second mode is small compared to its distance from the first, and
that the fields $(\mathbf{E}_2,\mathbf{B}_2)$ vary slowly across $K_1$.

Let $\mathbf{X}_1(t)$ denote the center of charge of mode 1:

$$
\mathbf{X}_1
:=
\frac{1}{q_1}\int_{K_1}\mathbf{x}\,\rho_1\,dV,
\qquad
q_1:=\int_{K_1}\rho_1\,dV.
$$

Expand the external field of mode 2 about $\mathbf{X}_1$:

$$
\mathbf{E}_2(\mathbf{r},t)
=
\mathbf{E}_2(\mathbf{X}_1,t)
+
(\mathbf{r}-\mathbf{X}_1)\cdot\nabla\mathbf{E}_2(\mathbf{X}_1,t)
+
O(\ell_1^2\nabla^2\mathbf{E}_2),
$$

and similarly for $\mathbf{B}_2$, where $\ell_1$ is the size of the first
mode.

Because $\mathbf{X}_1$ is the center of charge,

$$
\int_{K_1}(\mathbf{r}-\mathbf{X}_1)\,\rho_1(\mathbf{r},t)\,dV=0.
$$

Substituting into the exact force formula gives

$$
\mathbf{F}_{1\leftarrow 2}
=
q_1\,\mathbf{E}_2(\mathbf{X}_1,t)
+
\left(\int_{K_1}\mathbf{J}_1\,dV\right)\times\mathbf{B}_2(\mathbf{X}_1,t)
+
O(\ell_1^2\nabla^2\mathbf{E}_2,\ \ell_1\nabla\mathbf{B}_2).
$$

By the same continuity argument used in appendix 209,

$$
\int_{K_1}\mathbf{J}_1\,dV=q_1\,\dot{\mathbf{X}}_1.
$$

Define

$$
\mathbf{v}_1:=\dot{\mathbf{X}}_1.
$$

Then

$$
\mathbf{F}_{1\leftarrow 2}
=
q_1\bigl(
\mathbf{E}_2(\mathbf{X}_1,t)
+
\mathbf{v}_1\times\mathbf{B}_2(\mathbf{X}_1,t)
\bigr)
+
O(\ell_1^2\nabla^2\mathbf{E}_2,\ \ell_1\nabla\mathbf{B}_2).
$$

The same argument gives

$$
\mathbf{F}_{2\leftarrow 1}
=
q_2\bigl(
\mathbf{E}_1(\mathbf{X}_2,t)
+
\mathbf{v}_2\times\mathbf{B}_1(\mathbf{X}_2,t)
\bigr)
+
O(\ell_2^2\nabla^2\mathbf{E}_1,\ \ell_2\nabla\mathbf{B}_1).
$$

So the two-charge interaction law is already present in exact form at the
localized-mode level, and reduces in the compact limit to the Lorentz force of
each mode in the field generated by the other.

## 210.6 Static Point-Mode Idealization and Coulomb Law

Now take the static point-mode idealization:

$$
\rho_1(\mathbf{r})=q_1\,\delta(\mathbf{r}-\mathbf{X}_1),
\qquad
\rho_2(\mathbf{r})=q_2\,\delta(\mathbf{r}-\mathbf{X}_2),
$$

with

$$
\mathbf{J}_1=\mathbf{J}_2=0.
$$

Then

$$
\mathbf{B}_1=\mathbf{B}_2=0,
$$

and each electric field is static and curl-free away from its source:

$$
\nabla\times\mathbf{E}_a=0.
$$

Therefore

$$
\mathbf{E}_a=-\nabla\phi_a,
$$

with

$$
\nabla^2\phi_a
=
-\frac{q_a}{\varepsilon_0}\,\delta(\mathbf{r}-\mathbf{X}_a).
$$

The unique solution vanishing at spatial infinity is

$$
\phi_a(\mathbf{r})
=
\frac{q_a}{4\pi\varepsilon_0\,|\mathbf{r}-\mathbf{X}_a|},
$$

so

$$
\mathbf{E}_a(\mathbf{r})
=
\frac{q_a}{4\pi\varepsilon_0}
\frac{\mathbf{r}-\mathbf{X}_a}{|\mathbf{r}-\mathbf{X}_a|^3}.
$$

Hence

$$
\mathbf{F}_{1\leftarrow 2}
=
q_1\,\mathbf{E}_2(\mathbf{X}_1)
=
\frac{q_1q_2}{4\pi\varepsilon_0}
\frac{\mathbf{X}_1-\mathbf{X}_2}{|\mathbf{X}_1-\mathbf{X}_2|^3}.
$$

Similarly,

$$
\mathbf{F}_{2\leftarrow 1}
=
\frac{q_1q_2}{4\pi\varepsilon_0}
\frac{\mathbf{X}_2-\mathbf{X}_1}{|\mathbf{X}_2-\mathbf{X}_1|^3}
=
-\mathbf{F}_{1\leftarrow 2}.
$$

This is exactly the Coulomb interaction law.

The sign of the interaction is carried by the product $q_1q_2$:

- if $q_1q_2>0$, the force is repulsive,
- if $q_1q_2<0$, the force is attractive.

In the language of chapter 10, that sign is the large-scale summary of the
relative orientation of the two through-hole flux classes.

## 210.7 Moving Configurations

For moving compact modes, the exact force law remains

$$
\mathbf{F}_{1\leftarrow 2}
=
\int_{V_1}
\bigl(\rho_1\mathbf{E}_2+\mathbf{J}_1\times\mathbf{B}_2\bigr)\,dV,
$$

and similarly for mode 2.

So magnetic interaction is not an extra mechanism. It is the current part of
the same cross-stress transfer.

In the compact-mode limit this becomes

$$
\mathbf{F}_{1\leftarrow 2}
\approx
q_1\bigl(\mathbf{E}_2(\mathbf{X}_1,t)+\mathbf{v}_1\times\mathbf{B}_2(\mathbf{X}_1,t)\bigr),
$$

which is the moving two-charge interaction written in localized form.

## 210.8 Interpretation

The exact two-charge interaction law is therefore:

- fundamentally, cross momentum transfer through one common field,
- effectively, the force of one localized mode against the field generated by
  the other,
- in the static point-mode idealization, exactly Coulomb.

So chapter 10 can now be read more sharply:

- charge sign is tied to the oriented through-hole flux class of a toroidal
  mode,
- effective charge density is the large-scale summary of that class,
- interaction follows from cross stress transfer between such modes.

## 210.9 Summary

For two localized charged modes, the exact local cross-interaction balance is

$$
\partial_t\mathbf{g}_{\times}
-\nabla\cdot\mathbf{T}_{\times}
=
-\bigl(
\rho_1\mathbf{E}_2+\mathbf{J}_1\times\mathbf{B}_2
+
\rho_2\mathbf{E}_1+\mathbf{J}_2\times\mathbf{B}_1
\bigr).
$$

Integrating around one mode gives the exact force exerted by the other:

$$
\mathbf{F}_{1\leftarrow 2}
=
\int_{V_1}
\bigl(\rho_1\mathbf{E}_2+\mathbf{J}_1\times\mathbf{B}_2\bigr)\,dV.
$$

In the compact-mode limit this reduces to the localized Lorentz form, and in
the static point-mode idealization it becomes exactly

$$
\mathbf{F}_{1\leftarrow 2}
=
\frac{q_1q_2}{4\pi\varepsilon_0}
\frac{\mathbf{X}_1-\mathbf{X}_2}{|\mathbf{X}_1-\mathbf{X}_2|^3}.
$$

Thus the Coulomb interaction is derived here as the static point-mode limit of
cross-stress transfer between two localized charged closures.
