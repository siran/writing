---
title: The Physics of Energy Flow - Two-Aspect Origin of the Weak-Field Factor of Two
date: 2026-03-25
---

# 12a. Two-Aspect Origin of the Weak-Field Factor of Two

Chapter 12 summarized the weak-field interaction by the symmetric constitutive
writing

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+2\eta),
\qquad
\mu_{\mathrm{eff}}=\mu_0(1+2\eta).
$$

That summary is useful, but it is not the deepest explanation of the factor of
two. The deeper point is that the probe is a null Maxwell mode. It carries two
equal aspects, electric and magnetic, and a static toroidal closure must sample
both when it loads the probe along its axial transport line.

This chapter isolates exactly what is already forced by that fact and what
still remains open.

## 12a.1 Null Maxwell Modes Carry Two Equal Stress Sectors

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

This means the probe has no trapped rest component. Its transport is fully
carried along $\mathbf n$, so locally

$$
|\mathbf S|=ku.
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

## 12a.2 Consequence for the Leading Weak-Field Bending Term

Now consider a weak static bounded mass mode. The result above means that any
correct interaction cannot treat the probe as one channel only.

The remaining question is not whether there are two equal sectors. That is
already forced. The remaining question is how a static bounded closure samples
them.

The next chapter answers that directly. A static toroidal closure interacts
through its axial line, and because it is static it samples the two opposite
axial directions symmetrically. When that symmetric axial load is written in
terms of the probe transport data, it becomes

$$
u+\Pi_n.
$$

For a null Maxwell probe, $\Pi_n=u$, so the static closure sees

$$
u+\Pi_n=2u.
$$

That is the structural origin of the factor of two.

## 12a.3 Why Raw Vacuum Superposition Is Not Yet the Full Derivation

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

- it shows why a one-channel account gives only the Newtonian half-value,
- it shows why a null Maxwell probe carries the second equal sector,
- it prepares the axial-load derivation of the next chapter.

## 12a.4 Relation to the Weak-Field Summary

Chapter 12 summarized the weak interaction by the symmetric constitutive
modification

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
3. a static toroidal closure must sample both axial channels symmetrically,
4. the symmetric constitutive summary used in chapter 12 is the macroscopic
   encoding of that doubled axial interaction.

## 12a.5 What Still Remains Open

The next chapter completes the weak exterior factor-of-two derivation by doing
exactly that axial sampling step. What still remains open is not the factor of
two itself, but the full exact interaction beyond the weak exterior regime:

- finite-size corrections of the bounded mass closure,
- strong-field interaction,
- time-dependent and radiative sectors.

## 12a.6 Summary

For a null Maxwell probe:

$$
u_E=u_B=\frac{u}{2},
$$

and the electric and magnetic sectors contribute equally to the longitudinal
transport stress.

Therefore any admissible leading weak-field interaction term that treats the
two Maxwell aspects symmetrically must produce

$$
\text{full null interaction}
=
2\times\text{one-channel effect}.
$$

So the weak-field factor of two should not be explained by arbitrary
constitutive symmetry. It belongs more deeply to the two-aspect stress
structure of the probe itself and to the sign-symmetric axial loading by a
static toroidal closure.

The next chapter completes that weak exterior derivation directly from axial
transport.
