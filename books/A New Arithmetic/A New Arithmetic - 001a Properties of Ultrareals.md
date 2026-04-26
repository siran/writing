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

## Positive Definiteness

The modulus of every ultrareal is positive definite:

$$
|U| = U = u^2 \ge 0.
$$

It vanishes only at zero:

$$
|U|=0 \quad\Longleftrightarrow\quad U=0.
$$

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

It is continuous over:

$$
-1 \le d(U,V) \le 1
$$

So relation-aware addition includes partial alignment, not only the three named
cases of alignment, orthogonality, and opposition.

The descriptor need not come from an angle. It is whatever relation data the
quantities require. If the quantities are vector-like or phase-like, and
$d(U,V)$ does come from an angle, then:

$$
d(U,V) = \cos(\theta)
$$

and:

$$
U + V = u^2 + v^2 + 2uv\cos(\theta)
$$

## Closure

For the continuous range:

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

## Many-Term Addition

For many terms, the relation-aware form is:

$$
(u_1 + u_2 + \cdots + u_n)^2
$$

Expanded:

$$
u_1^2 + u_2^2 + \cdots + u_n^2
+ 2\sum_{i<j} u_i u_j
$$

If the terms have different relations, the coefficients must be shown:

$$
u_1^2 + \cdots + u_n^2
+ 2\sum_{i<j} d_{ij} u_i u_j
$$

The descriptors $d_{ij}$ are part of the arithmetic data.

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
