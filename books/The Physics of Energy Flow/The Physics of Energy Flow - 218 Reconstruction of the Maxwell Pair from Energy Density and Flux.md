---
title: The Physics of Energy Flow - Reconstruction of the Maxwell Pair from Energy Density and Flux
date: 2026-03-17
---

# 218. Reconstruction of the Maxwell Pair from Energy Density and Flux

The main text derives the transport core first and identifies the two
complementary aspects $\mathbf E$ and $\mathbf B$ with the two transporting
aspects $\mathbf F_+$ and $\mathbf F_-$. This appendix does not replace that
derivation. It proves only the local converse: once a local energy density and
energy flux are given, and once they obey the transport bound, one can
reconstruct at least one Maxwell pair that reproduces them.

This is a representation theorem, not a dynamical one. It shows what the local
observables $(u,\mathbf S)$ are sufficient to encode. It does not by itself
determine how the fields evolve. That still belongs to Maxwellian transport.

## 218.1 Problem

Suppose a pointwise energy density and flux are given:

$$
u(\mathbf r,t) > 0,
\qquad
\mathbf S(\mathbf r,t).
$$

Assume the transport bound

$$
|\mathbf S| \le c\,u.
$$

We ask whether there exist vectors $\mathbf E$ and $\mathbf B$ such that

$$
u
=
\frac{\varepsilon_0}{2}|\mathbf E|^2
+
\frac{1}{2\mu_0}|\mathbf B|^2,
$$

and

$$
\mathbf S
=
\frac{1}{\mu_0}\,\mathbf E\times\mathbf B.
$$

The answer is yes.

## 218.2 Reconstruction Theorem

For every pair $(u,\mathbf S)$ with $u>0$ and $|\mathbf S|\le cu$, there exists
at least one pair $(\mathbf E,\mathbf B)$ satisfying

$$
u
=
\frac{\varepsilon_0}{2}|\mathbf E|^2
+
\frac{1}{2\mu_0}|\mathbf B|^2,
$$

$$
\mathbf S
=
\frac{1}{\mu_0}\,\mathbf E\times\mathbf B.
$$

Moreover, the reconstruction is not unique.

## 218.3 Construction

If $\mathbf S\neq 0$, let

$$
\hat{\mathbf s}:=\frac{\mathbf S}{|\mathbf S|}.
$$

If $\mathbf S=0$, choose any unit vector $\hat{\mathbf s}$.

Choose any unit vector $\hat{\mathbf e}$ orthogonal to $\hat{\mathbf s}$, and
define

$$
\hat{\mathbf b}:=\hat{\mathbf s}\times\hat{\mathbf e}.
$$

Then $(\hat{\mathbf e},\hat{\mathbf b},\hat{\mathbf s})$ is a right-handed
orthonormal frame.

Now define

$$
\mathbf E := E\,\hat{\mathbf e},
\qquad
\mathbf B := B\,\hat{\mathbf b},
$$

with scalars $E,B\ge 0$ to be chosen.

Because

$$
\hat{\mathbf e}\times\hat{\mathbf b}=\hat{\mathbf s},
$$

we have

$$
\mathbf E\times\mathbf B = EB\,\hat{\mathbf s}.
$$

So the flux condition becomes

$$
\frac{1}{\mu_0}EB = |\mathbf S|.
$$

The energy condition becomes

$$
u
=
\frac{\varepsilon_0}{2}E^2
+
\frac{1}{2\mu_0}B^2.
$$

It is convenient to rescale:

$$
X:=\sqrt{\varepsilon_0}\,E,
\qquad
Y:=\frac{B}{\sqrt{\mu_0}}.
$$

Then the two conditions become

$$
u=\frac{X^2+Y^2}{2},
$$

and, since

$$
c^2=\frac{1}{\mu_0\varepsilon_0},
$$

also

$$
|\mathbf S| = c\,X\,Y.
$$

So it is enough to find nonnegative $X,Y$ such that

$$
X^2+Y^2=2u,
\qquad
XY=\frac{|\mathbf S|}{c}.
$$

## 218.4 Existence

Set

$$
\rho := \frac{|\mathbf S|}{c\,u}.
$$

By assumption,

$$
0\le \rho \le 1.
$$

Choose an angle $\theta\in[0,\pi/4]$ such that

$$
\sin(2\theta)=\rho.
$$

Now define

$$
X:=\sqrt{2u}\,\cos\theta,
\qquad
Y:=\sqrt{2u}\,\sin\theta.
$$

Then

$$
\frac{X^2+Y^2}{2}
=
\frac{2u(\cos^2\theta+\sin^2\theta)}{2}
=
u,
$$

and

$$
cXY
=
c(2u\cos\theta\sin\theta)
=
cu\sin(2\theta)
=
|\mathbf S|.
$$

So the reconstructed pair

$$
\mathbf E = \frac{X}{\sqrt{\varepsilon_0}}\,\hat{\mathbf e},
\qquad
\mathbf B = \sqrt{\mu_0}\,Y\,\hat{\mathbf b}
$$

satisfies the required relations exactly.

Thus the reconstruction exists for every $(u,\mathbf S)$ satisfying
$|\mathbf S|\le cu$.

## 218.5 Why the Bound Is Sharp

The same inequality is also necessary.

For any vectors $\mathbf E,\mathbf B$,

$$
|\mathbf S|
=
\frac{1}{\mu_0}|\mathbf E\times\mathbf B|
\le
\frac{1}{\mu_0}|\mathbf E|\,|\mathbf B|.
$$

Using the arithmetic-geometric mean inequality,

$$
\frac{1}{\mu_0}|\mathbf E|\,|\mathbf B|
\le
\frac{c}{2}\left(
\varepsilon_0|\mathbf E|^2+\frac{1}{\mu_0}|\mathbf B|^2
\right)
=
cu.
$$

So any Maxwell pair must satisfy

$$
|\mathbf S|\le cu.
$$

The bound is therefore not an extra decoration. It is exactly the condition
under which the local observables admit Maxwell representation.

## 218.6 Non-Uniqueness

The reconstruction is not unique.

First, the choice of transverse unit vector $\hat{\mathbf e}$ is arbitrary up
to rotation in the plane orthogonal to $\hat{\mathbf s}$. That already gives a
continuous family of solutions.

Second, even after one pair $(\mathbf E,\mathbf B)$ is fixed, the duality
rotation

$$
\mathbf E'=\mathbf E\cos\phi + c\,\mathbf B\sin\phi,
$$

$$
c\,\mathbf B'=-\mathbf E\sin\phi + c\,\mathbf B\cos\phi
$$

leaves both $u$ and $\mathbf S$ unchanged.

So $(u,\mathbf S)$ do not determine $(\mathbf E,\mathbf B)$ uniquely. The
underdetermination is exactly the local polarization or duality freedom of the
two-aspect transport.

## 218.7 What This Does and Does Not Determine

The pair $(u,\mathbf S)$ determines:

- whether a Maxwell reconstruction exists,
- one local transport direction $\hat{\mathbf s}$ when $\mathbf S\neq 0$,
- and the scalar load split consistent with the transport bound.

It does not determine:

- a unique polarization frame,
- a unique duality phase,
- or the dynamical evolution of the reconstructed fields.

Those missing pieces are not flaws in the reconstruction. They are precisely
what requires the full Maxwellian transport closure of chapter 7.

## 218.8 Final Statement

The Maxwell pair is not an arbitrary superstructure placed on top of energy
density and flux. Its primary origin in this book is still the double-curl
transport closure. The present appendix says only that whenever the local
observables satisfy

$$
|\mathbf S|\le cu,
$$

they already admit at least one exact Maxwell representation.

the already-derived two-aspect transport admits at least one local Maxwell
representation whose scalar and vector observables are $u$ and $\mathbf S$.
What the representation alone cannot do is fix the evolution. That is the role
of Maxwellian transport.
