# Properties of Ultrareals

An ultrareal number is a positive square-form:

$$
U = u^2
$$

with:

$$
u \ge 0
$$

The basic ultrareal domain is:

$$
UR = \{u^2 \mid u \ge 0\}
$$

The mathematics used here is already familiar: squares, norms, inner products,
Gram matrices, quadratic forms, and the law of cosines. The new move is to
stitch those pieces into a single number system: numbers are positive
density-values, addition carries relation data, and negative signs belong to
orientation, comparison, or bookkeeping rather than to ultrareal magnitude.

## Positive Square-Form

The modulus of every ultrareal is the value itself:

$$
|U| = U = u^2 \ge 0.
$$

It vanishes only at zero:

$$
|U|=0 \quad\Longleftrightarrow\quad U=0.
$$

In the square-form sense, this is positive definite: the value is never
negative, and only zero has zero modulus.

**There are no negative ultrareals.**

There are opposing positive ultrareals. Opposition belongs to relation,
orientation, or joining; it does not make the positive square-form negative.

The only zero-modulus ultrareal is zero:

$$
0 = 0^2
$$

## Square Representation

Every positive ordinary number can be represented as an ultrareal:

$$
X = x^2
$$

This does not make $X$ unreal. It gives $X$ an inner state $x$.

The distinction is:

$$
\begin{aligned}
\text{visible value:}\quad &X,\\
\text{inner state:}\quad &x.
\end{aligned}
$$

## Equality

Two ultrareals are equal when their positive square-forms are equal:

$$
u^2 = v^2
$$

Since the ultrareal layer uses $u \ge 0$ and $v \ge 0$, this also means:

$$
u = v
$$

If signs or rotations are introduced, they belong to the inner layer, not to the
ultrareal value itself.

## Zero

Zero is the additive identity:

$$
0^2 + u^2 = u^2
$$

for any interaction descriptor, because the relation term vanishes:

$$
2d(0^2,u^2)(0)u = 0
$$

## Relation-Aware Addition

The general two-term addition uses an overloaded $+$. The operator is aware of
the parts being added: the visible values and their inner states.

$$
U + V = u^2 + v^2 + 2d(U,V)uv
$$

where:

$$
U = u^2,\qquad V = v^2.
$$

The descriptor $d(U,V)$ records relation.

For angular or field-alignment relations, it is continuous over:

$$
-1 \le d(U,V) \le 1
$$

So relation-aware addition includes partial alignment, not only the three named
cases of alignment, orthogonality, and opposition.

The descriptor need not come from an angle. It encodes whatever relation data
the quantities require: alignment, opposition, hyperbolic relation, tangential
relation, weighting, or another structure. The only requirement is
admissibility: the resulting joined value must remain an ultrareal value.

If the quantities are vector-like or phase-like, and $d(U,V)$ does come from an
angle, then:

$$
d(U,V) = \cos(\theta)
$$

and:

$$
U + V = u^2 + v^2 + 2uv\cos(\theta)
$$

## Closure and Admissibility

For the angular range, closure is automatic:

$$
-1 \le d(U,V) \le 1
$$

the result remains ultrareal:

$$
u^2 + v^2 + 2d(U,V)uv \ge 0
$$

The smallest case is opposition:

$$
d(U,V) = -1
$$

which gives:

$$
(u - v)^2 \ge 0
$$

So relation-aware addition does not require negative ultrareals.

It requires opposing positive ultrareals when the descriptor records opposition.

This is the first admissibility rule:

$$
U + V \in UR
\quad\Longleftrightarrow\quad
u^2 + v^2 + 2d(U,V)uv \ge 0.
$$

Opposition can cancel a joined value down to zero. It cannot push an ultrareal
sum below zero and remain inside $UR$. In that sense, positivity behaves like an
effective hyperbolicity or boundary: relation can stretch, turn, or oppose, but
opposition cannot pass below zero without leaving the ultrareal layer or being
reinterpreted as rotation, phase, or bookkeeping outside the positive magnitude.

## Standard Arithmetic

Standard arithmetic is recovered when:

$$
d(U,V) = 0
$$

Then:

$$
U + V = u^2 + v^2
$$

So standard addition is the non-interaction case.

## Aligned Addition

Aligned ultrareal addition is:

$$
d(U,V) = 1,\qquad U + V = (u + v)^2
$$

This operation is commutative:

$$
u^2 + v^2 = v^2 + u^2
$$

and associative:

$$
(u^2 + v^2) + w^2 = u^2 + (v^2 + w^2)
$$

because both sides equal:

$$
(u + v + w)^2
$$

## Many-Term Addition as a Quadratic Form

This is the rigorous core of the number system.

Let:

$$
U_i = u_i^2
$$

and collect the inner states into:

$$
\mathbf u =
\begin{bmatrix}
u_1\\
\vdots\\
u_n
\end{bmatrix}.
$$

Let $D$ be the relation matrix:

$$
D_{ii}=1,
\qquad
D_{ij}=d_{ij}.
$$

Then the relation-aware joined value is:

$$
U_1+\cdots+U_n
:=
\mathbf u^{\mathsf T}D\mathbf u.
$$

Expanded:

$$
\mathbf u^{\mathsf T}D\mathbf u
=
\sum_i u_i^2
+ 2\sum_{i<j}d_{ij}u_i u_j.
$$

The descriptors $d_{ij}$ are part of the arithmetic data. Ordinary arithmetic
is the diagonal case:

$$
D=I,
\qquad
\mathbf u^{\mathsf T}I\mathbf u
=
\sum_i u_i^2.
$$

Aligned joined addition is the all-ones relation matrix:

$$
D_{ij}=1
\quad\Longrightarrow\quad
\mathbf u^{\mathsf T}D\mathbf u
=
(u_1+\cdots+u_n)^2.
$$

Angular or phase-like relations give Gram matrices:

$$
d_{ij}=\cos(\theta_i-\theta_j).
$$

A Gram matrix is positive semidefinite, so the joined value is automatically
nonnegative:

$$
\mathbf u^{\mathsf T}D\mathbf u \ge 0.
$$

For hyperbolic, tangential, weighted, or otherwise non-angular relations, the
same rule applies: the descriptor may be used if the resulting relation matrix
is admissible. For a whole class of signed or rotated inner states, the clean
condition is:

$$
D \succeq 0.
$$

If the intended domain is only nonnegative inner magnitudes, the matching
whole-class condition is copositivity on the positive cone:

$$
\mathbf u \ge 0
\quad\Longrightarrow\quad
\mathbf u^{\mathsf T}D\mathbf u \ge 0.
$$

For a single concrete joining, or for a restricted positive domain, the weaker
state-specific condition is enough:

$$
\mathbf u^{\mathsf T}D\mathbf u \ge 0.
$$

This is the formal version of "you cannot oppose beyond zero." A proposed
relation that makes the joined density negative is not an ultrareal sum.

## Immediate Identities and Novelties

The identities are familiar, but their placement is different.

Standard arithmetic is recovered as the identity relation matrix:

$$
D=I.
$$

Pythagorean addition is recovered as orthogonal relation:

$$
d_{ij}=0.
$$

Aligned repeated units recover square growth:

$$
\underbrace{1+\cdots+1}_{n\text{ aligned units}}=n^2.
$$

Opposition becomes a zero-boundary relation rather than a negative object:

$$
u^2+(-u)^2=(u-u)^2=0.
$$

The novelty is therefore not a new binomial identity. It is the organization of
positive magnitudes, relation descriptors, rotations, cancellations, and
ordinary arithmetic inside one operational calculus of density-values.

## Multiplication

Ultrareal multiplication is inherited from the inner states:

$$
u^2 \times_{\mathrm{UR}} v^2 = (uv)^2
$$

The multiplicative identity is:

$$
1 = 1^2
$$

For aligned addition, multiplication distributes:

$$
u^2 \times_{\mathrm{UR}} (v^2 + w^2)
= (uv)^2 + (uw)^2
$$

## No Negative Inverses Inside UR

Except for zero, no ultrareal has an additive inverse inside $UR$.

There is no positive square-form $V$ such that:

$$
U + V = 0
$$

for positive $U$, unless the cancellation is carried by inner opposition:

$$
(u - u)^2 = 0
$$

Signs, rotation, and opposition belong to the inner layer or to relation, not to
ultrareal magnitude.
