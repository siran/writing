# Properties of Ultrareals

An ultrareal number is a positive square-form:

$$
U = u^2
$$

The basic ultrareal domain is the set of visible square-values:

$$
UR = \{u^2 \mid u\in\mathbb R_{\ge0}\}=[0,\infty).
$$

The value $U$ is nonnegative, and the inner magnitude $u$ is nonnegative. The
full inner state is $ue^{i\phi}$. The unrotated case has $\phi=0$. Orientation,
opposition, and return are carried by changing $\phi$, not by introducing a
negative inner magnitude.

The mathematics touched here is already familiar. For the full theory of
squares, norms, inner products, quadratic forms, matrices, and the law of
cosines, the reader should go to the books written by masters of those fields.
This book is not trying to replace them.

The aim here is narrower: to look at a small shiny angle where geometry,
physics, linear algebra, number theory, and basic algebra meet. Each field sees
part of the picture. Ultrareals gather those views into a single arithmetic
language: numbers are positive density-values, addition carries relation data,
and negative signs belong to orientation, comparison, or bookkeeping rather than
to ultrareal magnitude.

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

This does not make $X$ unreal. It gives $X$ an inner magnitude $x$.

The distinction is:

$$
\begin{aligned}
\text{visible value:}\quad &X,\\
\text{inner magnitude:}\quad &x.
\end{aligned}
$$

## Equality

Two ultrareals are equal when their positive square-forms are equal:

$$
u^2 = v^2
$$

Since the inner magnitudes satisfy $u\ge0$ and $v\ge0$, equality also means:

$$
u = v
$$

If rotations are introduced, they belong to the inner layer, not to the
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
the parts being added: the visible values and their inner magnitudes.

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

So relation-aware addition includes every degree of partial relation inside the
chosen scale. The special recovered case is non-interaction, where the
descriptor is zero and the relation term vanishes.

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

and the result remains ultrareal:

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

For two nonzero ultrareals, exact cancellation inside the angular or
field-alignment scale has only one form. Let:

$$
A=a^2,\qquad B=b^2.
$$

Then:

$$
A+B=a^2+b^2+2d(A,B)ab.
$$

If $A+B=0$, then:

$$
d(A,B)=-\frac{a^2+b^2}{2ab}.
$$

But in the bounded opposition scale $-1\le d(A,B)\le1$, the right side can
reach the scale only when $a=b$. Therefore cancellation inside $UR$ requires:

$$
a=b,\qquad d(A,B)=-1.
$$

Complete opposition then reduces the joined value to:

$$
A+B=(a-b)^2.
$$

Zero is not negative existence. It is equal positive magnitude joined in
complete opposition.

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

## Many-Term Addition as Relation Arithmetic

This is the rigorous core of the number system.

Let:

$$
U_i = u_i^2
$$

For many terms, relation-aware addition is:

$$
\boxed{
U_1+\cdots+U_n
:=
\sum_i u_i^2
+ 2\sum_{i<j}d_{ij}u_i u_j
}
$$

The coefficients $d_{ij}$ form a table of relations between the parts:

$$
\begin{array}{c|cccc}
 & U_1 & U_2 & \cdots & U_n\\
\hline
U_1 & 1 & d_{12} & \cdots & d_{1n}\\
U_2 & d_{21} & 1 & \cdots & d_{2n}\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
U_n & d_{n1} & d_{n2} & \cdots & 1
\end{array}
$$

The diagonal entries are $1$ because each term is fully itself. The off-diagonal
entries are the interaction descriptors.

Ordinary arithmetic is recovered when every off-diagonal relation is zero:

$$
d_{ij}=0
\quad (i\ne j).
$$

Then:

$$
U_1+\cdots+U_n
=
u_1^2+\cdots+u_n^2.
$$

Aligned joined addition is recovered when every relation is $1$:

$$
d_{ij}=1
\quad\Longrightarrow\quad
U_1+\cdots+U_n=(u_1+\cdots+u_n)^2.
$$

Opposed relations subtract from the joined value through the relation term, but
the admissibility rule remains:

$$
U_1+\cdots+U_n \ge 0.
$$

In angular or phase-like cases one common choice is:

$$
d_{ij}=\cos(\theta_i-\theta_j).
$$

This is the law-of-cosines pattern generalized to many terms.

Readers who know linear algebra will recognize the same expression as a
quadratic form:

$$
\mathbf u^{\mathsf T}D\mathbf u.
$$

Angular relation tables are Gram matrices, which automatically keep the joined
value nonnegative. In that language, a whole class of signed or rotated inner
states is safely admissible when:

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

That is useful language, but it is not the center of the book. The arithmetic
point is simpler: the relation table is part of addition, and the joined value
must remain a positive density.

This is the formal version of "you cannot oppose beyond zero." A proposed
relation that makes the joined density negative is not an ultrareal sum.

## Immediate Identities and Novelties

The identities are familiar, but their placement is different. The important
recovered special case is non-interaction.

Standard arithmetic is recovered as the identity relation matrix:

$$
D=I.
$$

What geometry calls Pythagorean addition is the same zero-relation condition
when the descriptor is angular:

$$
d_{ij}=0.
$$

Aligned repeated units recover square growth:

$$
\underbrace{1+\cdots+1}_{n\text{ aligned units}}=n^2.
$$

Opposition becomes a zero-boundary relation rather than a negative object:

$$
|u+ue^{i\pi}|^2=0.
$$

The novelty is therefore not a new binomial identity. It is the organization of
positive magnitudes, relation descriptors, rotations, cancellations, and
ordinary arithmetic inside one operational arithmetic of density-values.

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
