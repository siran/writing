---
title: The Physics of Energy Flow - Uniqueness of the Maxwell Closure in the Stated Class
date: 2026-03-14
---

# 211. Uniqueness of the Maxwell Closure in the Stated Class

This appendix proves the uniqueness claim that chapter 7 can only suggest in
words.

The claim is not that Maxwell closure is unique among all imaginable local
relations whatsoever. The claim is narrower and precise:

> Within the class of real, linear, local, homogeneous, isotropic, first-order,
> purely differential, divergence-preserving two-field closures, every neutral
> isotropic transporting closure is equivalent, by a real linear recombination
> of the two fields, to the Maxwell pair
> $$
> \partial_t\mathbf{F}_{+}=k\,\nabla\times\mathbf{F}_{-},
> \qquad
> \partial_t\mathbf{F}_{-}=-k\,\nabla\times\mathbf{F}_{+}.
> $$

This is the exact sense in which the closure of chapter 7 is unique.

## 211.1 The Closure Class

Let

$$
\mathbf{F}_1(\mathbf{r},t),
\qquad
\mathbf{F}_2(\mathbf{r},t)
$$

be two real vector fields on $\mathbb{R}^3$, each constrained by

$$
\nabla\cdot\mathbf{F}_1=0,
\qquad
\nabla\cdot\mathbf{F}_2=0.
$$

We consider closures of the form

$$
\partial_t\mathbf{F}_a=\mathcal{L}_{ab}\mathbf{F}_b,
\qquad
a,b\in\{1,2\},
$$

with the following assumptions.

1. Real-linear:
   $\mathcal{L}$ is linear over the real numbers.

2. Local and homogeneous:
   $\mathcal{L}$ has constant coefficients and depends only on the value of the
   fields and their derivatives at the same point.

3. First-order in space:
   $\mathcal{L}$ contains at most one spatial derivative.

4. Purely differential:
   there is no algebraic zero-order mixing term. This restriction is
   intentional. Chapter 6 separated algebraic updates from spatial
   reorganization; the present theorem concerns the transporting closure class.

5. Isotropic:
   the closure is equivariant under proper spatial rotations.

6. Divergence-preserving:
   if $\nabla\cdot\mathbf{F}_a=0$ initially, then
   $\nabla\cdot(\partial_t\mathbf{F}_a)=0$.

The task is to classify all such closures and determine which of them yield
neutral isotropic transport.

## 211.2 Classification of All Closures in the Class

Because the closure is linear, local, homogeneous, first-order, and purely
differential, there exist constants $B_{abijk}$ such that

$$
(\partial_t\mathbf{F}_a)_i
=
B_{abijk}\,\partial_j(\mathbf{F}_b)_k.
$$

Isotropy under proper rotations means the tensor $B_{abijk}$ must satisfy

$$
R_{i\ell}\,B_{ab\ell mn}\,R_{jm}\,R_{kn}
=
B_{abijk}
$$

for every rotation matrix $R\in SO(3)$.

For fixed field indices $a,b$, this is the classification problem for an
isotropic rank-three tensor on Euclidean space. Up to a scalar multiple, the
only such tensor is the Levi-Civita symbol $\varepsilon_{ijk}$. Therefore

$$
B_{abijk}=M_{ab}\,\varepsilon_{ijk}
$$

for some real $2\times 2$ matrix $M=(M_{ab})$.

Hence every closure in the stated class has the form

$$
\partial_t\mathbf{F}_a
=
M_{ab}\,\nabla\times\mathbf{F}_b.
$$

Equivalently, if we write

$$
\mathbb{F}
:=
\begin{pmatrix}
\mathbf{F}_1\\
\mathbf{F}_2
\end{pmatrix},
$$

then

$$
\partial_t\mathbb{F}
=
M\,(\nabla\times)\mathbb{F},
$$

where $(\nabla\times)$ acts componentwise on the two fields.

This classification is exact.

## 211.3 Divergence Preservation

For any real matrix $M$,

$$
\nabla\cdot\bigl(M_{ab}\,\nabla\times\mathbf{F}_b\bigr)
=
M_{ab}\,\nabla\cdot(\nabla\times\mathbf{F}_b)=0.
$$

So every closure in the classified form preserves the divergence-free
condition identically.

Thus the classification problem is reduced to the field-space matrix $M$.

## 211.4 Second-Order Consequence

Differentiate once more in time:

$$
\partial_t^2\mathbf{F}_a
=
M_{ab}\,\nabla\times(\partial_t\mathbf{F}_b).
$$

Substitute the closure again:

$$
\partial_t^2\mathbf{F}_a
=
M_{ab}\,\nabla\times\bigl(M_{bc}\,\nabla\times\mathbf{F}_c\bigr)
=
(M^2)_{ac}\,\nabla\times(\nabla\times\mathbf{F}_c).
$$

Because each field is source-free,

$$
\nabla\times(\nabla\times\mathbf{F}_c)
=
\nabla(\nabla\cdot\mathbf{F}_c)-\nabla^2\mathbf{F}_c
=
-\nabla^2\mathbf{F}_c.
$$

Hence

$$
\partial_t^2\mathbf{F}_a
=
-(M^2)_{ac}\,\nabla^2\mathbf{F}_c.
$$

In block form,

$$
\partial_t^2\mathbb{F}
=
-M^2\,\nabla^2\mathbb{F}.
$$

So the entire second-order transport content of the closure is encoded by the
matrix $-M^2$.

## 211.5 Criterion for Neutral Isotropic Transport

In the present appendix, neutral isotropic transport means the following:

there exists a real field-space change of variables

$$
\mathbb{G}=P^{-1}\mathbb{F},
\qquad
P\in GL(2,\mathbb{R}),
$$

and a positive constant $k$ such that each transformed field satisfies the same
wave equation

$$
\partial_t^2\mathbf{G}_1-k^2\nabla^2\mathbf{G}_1=0,
\qquad
\partial_t^2\mathbf{G}_2-k^2\nabla^2\mathbf{G}_2=0.
$$

Because $P$ is constant, it commutes with $\partial_t$ and $\nabla^2$. So the
second-order equation becomes

$$
\partial_t^2\mathbb{G}
=
-P^{-1}M^2P\,\nabla^2\mathbb{G}.
$$

Therefore neutral isotropic transport holds if and only if

$$
-P^{-1}M^2P=k^2I.
$$

Since the identity is invariant under similarity, this is equivalent to

$$
M^2=-k^2I.
$$

So the transport criterion is exact:

> A closure in the stated class yields neutral isotropic transport with one
> common speed $k$ if and only if its field-space matrix satisfies
> $M^2=-k^2I$.

## 211.6 Reduction to the Canonical Maxwell Pair

We now classify all real $2\times 2$ matrices satisfying

$$
M^2=-k^2I,
\qquad
k>0.
$$

Let $\mathbf{e}\in\mathbb{R}^2$ be any nonzero vector.

The vectors $\mathbf{e}$ and $M\mathbf{e}$ are linearly independent. For if
they were dependent, we would have

$$
M\mathbf{e}=\lambda\mathbf{e}
$$

for some real $\lambda$, and then

$$
M^2\mathbf{e}=\lambda^2\mathbf{e},
$$

which would imply

$$
\lambda^2=-k^2,
$$

impossible over the real numbers.

So the vectors

$$
\mathbf{e}_1:=\mathbf{e},
\qquad
\mathbf{e}_2:=-\frac{1}{k}M\mathbf{e}
$$

form a basis of $\mathbb{R}^2$.

In this basis,

$$
M\mathbf{e}_1
=
k\,\mathbf{e}_2,
$$

and

$$
M\mathbf{e}_2
=
-\frac{1}{k}M^2\mathbf{e}
=
-\frac{1}{k}(-k^2)\mathbf{e}
=
-k\,\mathbf{e}_1.
$$

Therefore the matrix of $M$ in the basis $(\mathbf{e}_1,\mathbf{e}_2)$ is

$$
\begin{pmatrix}
0 & -k\\
k & 0
\end{pmatrix}.
$$

After exchanging the two basis vectors if desired, this becomes the canonical
matrix

$$
J_k
:=
\begin{pmatrix}
0 & k\\
-k & 0
\end{pmatrix}.
$$

So there exists a real invertible matrix $P$ such that

$$
P^{-1}MP=J_k.
$$

Now set

$$
\begin{pmatrix}
\mathbf{F}_{+}\\
\mathbf{F}_{-}
\end{pmatrix}
:=
P^{-1}
\begin{pmatrix}
\mathbf{F}_1\\
\mathbf{F}_2
\end{pmatrix}.
$$

Then the closure becomes

$$
\partial_t
\begin{pmatrix}
\mathbf{F}_{+}\\
\mathbf{F}_{-}
\end{pmatrix}
=
\begin{pmatrix}
0 & k\\
-k & 0
\end{pmatrix}
(\nabla\times)
\begin{pmatrix}
\mathbf{F}_{+}\\
\mathbf{F}_{-}
\end{pmatrix},
$$

that is,

$$
\partial_t\mathbf{F}_{+}=k\,\nabla\times\mathbf{F}_{-},
\qquad
\partial_t\mathbf{F}_{-}=-k\,\nabla\times\mathbf{F}_{+}.
$$

This is exactly the canonical Maxwell closure of chapter 7.

We have therefore proved:

> Every neutral isotropic transporting closure in the stated class is
> equivalent, by a real linear recombination of the two fields, to the Maxwell
> pair.

That is the promised uniqueness theorem.

## 211.7 Corollary: No One-Field Real Closure in This Class Transports

For a one-field closure in the same class, the matrix $M$ is just a real scalar
$m$, so the condition for neutral isotropic transport would be

$$
m^2=-k^2,
$$

which has no real solution.

So within the same class:

- one real field cannot furnish neutral isotropic transport,
- two real fields are necessary,
- and once two are admitted, the transporting closure is unique up to real
  field recombination.

This corollary places appendix 203 and the present appendix in one chain:

- appendix 203 proved the minimality claim constructively,
- appendix 211 proves the uniqueness claim in the stated class.

## 211.8 Scope of the Theorem

The theorem is exact, but its scope is the class stated at the beginning.

It does not address:

- nonlinear closures,
- anisotropic media,
- higher-order spatial operators,
- closures with explicit zero-order algebraic mixing,
- closures with more than two independent fields,
- nonlocal closures.

So the theorem should be read correctly:

- not as a proof that Maxwell is unique among all conceivable mathematical
  structures,
- but as a proof that Maxwell is unique inside the exact closure class
  singled out by chapters 6 and 7.

That is already a strong result.

## 211.9 Summary

Within the real, linear, local, homogeneous, isotropic, first-order, purely
differential, divergence-preserving two-field class:

1. every closure has the form
   $$
   \partial_t\mathbb{F}=M(\nabla\times)\mathbb{F}
   $$
   for a real $2\times 2$ matrix $M$,
2. its second-order consequence is
   $$
   \partial_t^2\mathbb{F}=-M^2\nabla^2\mathbb{F},
   $$
3. neutral isotropic transport with speed $k$ occurs if and only if
   $$
   M^2=-k^2I,
   $$
4. every such matrix is real-similar to
   $$
   \begin{pmatrix}
   0 & k\\
   -k & 0
   \end{pmatrix},
   $$
5. therefore the closure is equivalent to
   $$
   \partial_t\mathbf{F}_{+}=k\,\nabla\times\mathbf{F}_{-},
   \qquad
   \partial_t\mathbf{F}_{-}=-k\,\nabla\times\mathbf{F}_{+}.
   $$

Thus Maxwell closure is unique in the stated class.
