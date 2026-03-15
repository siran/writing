---
title: The Physics of Energy Flow - Two-Aspect Origin of the Weak-Field Factor of Two
date: 2026-03-15
---

# 215. Two-Aspect Origin of the Weak-Field Factor of Two

Chapter 13 and appendix 212 used a symmetric constitutive summary to recover
the weak-field light-bending value

$$
\theta=\frac{4GM}{bc^2}.
$$

That summary is useful, but it should not be mistaken for the deepest
explanation of the factor of two. The deeper point is that the probe is a null
Maxwell mode. It carries two equal aspects, electric and magnetic, and any
admissible first-order interaction with a static mass closure must couple to
both.

This appendix isolates exactly what is already forced by that fact and what
still remains open.

## 215.1 Null Maxwell Modes Carry Two Equal Stress Sectors

Take a narrow electromagnetic probe in a region that is approximately uniform
over one wavelength. Write its fields locally as

$$
\mathbf{E},
\qquad
\mathbf{B},
$$

with propagation direction $\mathbf{n}$ and local transport speed $k$.

For a null electromagnetic mode,

$$
\mathbf{n}\cdot\mathbf{E}=0,
\qquad
\mathbf{n}\cdot\mathbf{B}=0,
\qquad
\mathbf{B}=\frac{1}{k}\,\mathbf{n}\times\mathbf{E}.
$$

Its energy density splits into electric and magnetic pieces:

$$
u=u_E+u_B,
$$

$$
u_E=\frac{1}{2}\varepsilon E^2,
\qquad
u_B=\frac{1}{2\mu}B^2.
$$

If the local impedance is

$$
Z=\sqrt{\frac{\mu}{\varepsilon}},
$$

then

$$
|\mathbf{H}|=\frac{|\mathbf{E}|}{Z},
\qquad
\mathbf{B}=\mu\mathbf{H},
$$

and therefore

$$
u_B
=
\frac{1}{2}\mu H^2
=
\frac{1}{2}\mu\frac{E^2}{Z^2}
=
\frac{1}{2}\mu E^2\frac{\varepsilon}{\mu}
=
\frac{1}{2}\varepsilon E^2
=
u_E.
$$

So for any null Maxwell mode,

$$
\boxed{
u_E=u_B=\frac{u}{2}
}.
$$

Now split the Maxwell stress tensor into electric and magnetic pieces:

$$
T_{ij}=T^{(E)}_{ij}+T^{(B)}_{ij},
$$

with

$$
T^{(E)}_{ij}
=
\varepsilon\left(E_iE_j-\frac{1}{2}\delta_{ij}E^2\right),
$$

$$
T^{(B)}_{ij}
=
\frac{1}{\mu}\left(B_iB_j-\frac{1}{2}\delta_{ij}B^2\right).
$$

Choose local coordinates so the probe moves in the $+z$ direction. Then one
may take

$$
\mathbf{E}=(E,0,0),
\qquad
\mathbf{B}=\left(0,\frac{E}{k},0\right).
$$

The longitudinal momentum-flux component is $-T_{zz}$. For the electric part,

$$
-T^{(E)}_{zz}
=
\frac{1}{2}\varepsilon E^2
=
u_E.
$$

For the magnetic part,

$$
-T^{(B)}_{zz}
=
\frac{1}{2\mu}B^2
=
u_B.
$$

Hence

$$
\boxed{
-T_{zz}=u_E+u_B=u
},
$$

and the electric and magnetic sectors contribute equally to the longitudinal
transport stress of the probe.

That equality is exact. It does not depend on weak gravity. It is a structural
fact about null Maxwell transport.

## 215.2 Consequence for First-Order Bending

Now consider a weak static bounded mass mode. Suppose the first-order
interaction of that closure with the probe is:

1. linear to first order in the probe amplitude,
2. local on scales large compared to the probe wavelength,
3. isotropic at leading order in the background rest frame,
4. symmetric between the two Maxwell aspects of the probe.

Let

$$
\mathcal{L}_\perp
$$

denote the linear operator that sends the probe stress to its first-order
transverse momentum transfer density.

By linearity,

$$
\mathcal{L}_\perp[T]
=
\mathcal{L}_\perp[T^{(E)}]
+
\mathcal{L}_\perp[T^{(B)}].
$$

By two-aspect symmetry,

$$
\mathcal{L}_\perp[T^{(E)}]
=
\mathcal{L}_\perp[T^{(B)}].
$$

Therefore

$$
\boxed{
\mathcal{L}_\perp[T]
=
2\,\mathcal{L}_\perp[T^{(E)}]
=
2\,\mathcal{L}_\perp[T^{(B)}]
}.
$$

So a one-channel treatment captures only half the first-order transverse
interaction of a null Maxwell probe.

Within the stated interaction class, this is the structural origin of the familiar
factor of two:

- a scalar or one-channel model sees only one half,
- a null electromagnetic probe carries two equal stress channels,
- any admissible first-order interaction must act on both.

## 215.3 Why Raw Vacuum Superposition Is Not Yet the Full Derivation

Write the total fields as linear superposition of background and probe:

$$
\mathbf{E}=\mathbf{E}_1+\mathbf{E}_2,
\qquad
\mathbf{B}=\mathbf{B}_1+\mathbf{B}_2.
$$

Then the cross part of the Maxwell stress tensor is

$$
(T_\times)_{ij}
=
\varepsilon_0\left(E_{1i}E_{2j}+E_{2i}E_{1j}
-\delta_{ij}\mathbf{E}_1\cdot\mathbf{E}_2\right)
+
\frac{1}{\mu_0}\left(B_{1i}B_{2j}+B_{2i}B_{1j}
-\delta_{ij}\mathbf{B}_1\cdot\mathbf{B}_2\right).
$$

This identity is exact, but by itself it does not complete the weak-field
gravity derivation.

There are two reasons.

First, if the background is modeled as purely static and electric at leading
order, then

$$
\mathbf{B}_1\approx 0,
$$

so the explicit magnetic part of the raw cross stress vanishes at that order.
The second half of the factor of two is therefore not sitting in the formula as
an extra $B_1B_2$ term waiting to be read off.

Second, linear Maxwell superposition in vacuum does not make one source-free
solution bend another. The missing object is the actual interaction law by
which the bounded mass closure and the passing null probe reorganize one common
field.

So the exact role of the argument above is not to claim that raw vacuum
superposition already gives the full interaction law. Its role is sharper:

- it shows what any correct first-order interaction law must do,
- it shows why a one-channel account gives only the Newtonian half-value,
- it shows why the full electromagnetic interaction must double that result.

## 215.4 Relation to Chapter 13 and Appendix 212

Chapter 13 and appendix 212 summarized the weak interaction by the
symmetric constitutive modification

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+2\eta),
\qquad
\mu_{\mathrm{eff}}=\mu_0(1+2\eta).
$$

That summary should now be read more carefully.

It is not the deepest explanation of the factor of two. Rather, it is the
macroscopic summary of an interaction law that must, if it is correct, act
equally on the two stress sectors of a null Maxwell probe.

So the logical order is:

1. a null electromagnetic probe carries two equal stress sectors,
2. a one-channel theory gives only half the effect,
3. the full first-order interaction must couple to both,
4. the symmetric constitutive summary used in chapter 13 is the macroscopic
   encoding of that doubled interaction.

## 215.5 What Still Remains Open

The remaining task is not to guess the factor of two. Within the stated
interaction class, that part is already fixed by the two-aspect structure of the
probe.

The remaining task is to derive the actual interaction operator of a localized
massive closure and to show that it yields the full weak-field interaction
law.

In particular, a complete derivation should:

- start from a bounded mass mode and a passing null probe,
- compute the first-order interaction of the bounded mass closure with the
  passing probe,
- integrate the resulting transverse momentum transfer along the probe path,
- recover
  $$
  \theta=\frac{4GM}{bc^2}
  $$
  without treating the symmetric constitutive form as explanatory input.

That is the sharper gravity target inside the present framework.

## 215.6 Summary

For a null Maxwell probe:

$$
u_E=u_B=\frac{u}{2},
$$

and the electric and magnetic sectors contribute equally to the longitudinal
transport stress.

Therefore any admissible first-order interaction law that treats the two
Maxwell aspects symmetrically must produce

$$
\text{full null interaction}
=
2\times\text{one-channel effect}.
$$

So the weak-field factor of two should not be explained by arbitrary
constitutive symmetry. It belongs more deeply to the two-aspect stress
structure of the probe itself.

What remains open is the exact interaction derivation that turns this
structural fact into the full light-bending law.
