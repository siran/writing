---
title: The Physics of Energy Flow - Two Complementary Aspects of Flow
date: 2026-03-26
---

# 7a. Two Complementary Aspects of Flow

Chapter 7 recovered one source-free transporting field

$$
\mathbf F
$$

obeying the wave equation. To connect that one field with the conventional
electromagnetic writing, we now resolve its local transport into two
complementary transverse aspects.

The point is not to replace one substrate by two. The point is to show that
the local transport data of one flow can be written as a pair of orthogonal
aspects whose conventional names are $\mathbf E$ and $\mathbf B$.


## Local transport data

At each point, let

$$
u(\mathbf r,t)>0,
\qquad
\mathbf S(\mathbf r,t)
$$

denote the local energy density and energy flux of the one transporting field.

Because the flow transports energy at speed at most $c$, the local transport
data satisfy the bound

$$
|\mathbf S|\le cu.
$$

Equality holds for purely propagating transport. Strict inequality allows
locally retained or standing content.


## Orthogonal two-aspect resolution

If $\mathbf S\neq 0$, define the local transport direction

$$
\hat{\mathbf s}:=\frac{\mathbf S}{|\mathbf S|}.
$$

If $\mathbf S=0$, choose any unit vector $\hat{\mathbf s}$.

Now choose any unit vector $\hat{\mathbf e}$ orthogonal to $\hat{\mathbf s}$,
and define

$$
\hat{\mathbf b}:=\hat{\mathbf s}\times\hat{\mathbf e}.
$$

Then

$$
(\hat{\mathbf e},\hat{\mathbf b},\hat{\mathbf s})
$$

is a right-handed orthonormal frame.

Resolve the one transporting flow into two transverse aspects

$$
\mathbf F_+ := X\,\hat{\mathbf e},
\qquad
\mathbf F_- := Y\,\hat{\mathbf b},
$$

with nonnegative magnitudes $X,Y$ still to be chosen.

We require this pair to reproduce the local transport data by

$$
u=\frac{|\mathbf F_+|^2+|\mathbf F_-|^2}{2},
$$

and

$$
\mathbf S = c\,\mathbf F_+\times\mathbf F_-.
$$

Since

$$
\hat{\mathbf e}\times\hat{\mathbf b}=\hat{\mathbf s},
$$

these become the scalar conditions

$$
X^2+Y^2=2u,
\qquad
XY=\frac{|\mathbf S|}{c}.
$$


## Existence

Set

$$
\rho:=\frac{|\mathbf S|}{cu}.
$$

By the transport bound,

$$
0\le \rho\le 1.
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
X^2+Y^2=2u,
$$

and

$$
XY
=
2u\cos\theta\sin\theta
=
u\sin(2\theta)
=
\frac{|\mathbf S|}{c}.
$$

So the pair

$$
\mathbf F_+=\sqrt{2u}\cos\theta\,\hat{\mathbf e},
\qquad
\mathbf F_-=\sqrt{2u}\sin\theta\,\hat{\mathbf b}
$$

reproduces the given local transport data exactly.

Therefore every admissible local transport state of the one field can be
written as a pair of orthogonal transverse aspects.


## Conventional electromagnetic writing

Now define the conventional fields by the rescalings

$$
\mathbf F_+ := \sqrt{\varepsilon_0}\,\mathbf E,
\qquad
\mathbf F_- := \frac{\mathbf B}{\sqrt{\mu_0}}.
$$

Then

$$
u
=
\frac{|\mathbf F_+|^2+|\mathbf F_-|^2}{2}
=
\frac{\varepsilon_0}{2}|\mathbf E|^2
+
\frac{1}{2\mu_0}|\mathbf B|^2,
$$

and, since

$$
c=\frac{1}{\sqrt{\varepsilon_0\mu_0}},
$$

also

$$
\mathbf S
=
c\,\mathbf F_+\times\mathbf F_-
=
\frac{1}{\mu_0}\,\mathbf E\times\mathbf B.
$$

So the usual Maxwell writing is recovered as the conventional normalization of
the two complementary aspects of one flow.


## Interpretation

The two-aspect split is not unique. Rotating the transverse pair

$$
(\hat{\mathbf e},\hat{\mathbf b})
$$

about $\hat{\mathbf s}$ changes the local representation while preserving the
same local transport data.

What is fixed is the structure:

- one transporting field,
- one local propagation direction,
- two orthogonal transverse aspects,
- one common energy density and flux.

This is why the book treats $\mathbf E$ and $\mathbf B$ as complementary
aspects of one organized flow rather than as two substances.


## Next Step

The two-aspect resolution is local. It says how one transporting field is
written at a point.

The next chapter asks what happens when distinct portions of those same two
aspects meet and interact as one common field. For a self-refracting closure,
the most important concrete case is retarded self-action, where earlier
portions of the flow act back on later portions. That is the self-refraction
principle.
