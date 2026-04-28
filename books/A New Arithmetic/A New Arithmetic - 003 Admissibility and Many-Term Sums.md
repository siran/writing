# Admissibility and Many-Term Sums

Relation-aware addition must remain inside the ultrareal domain, the positive
real line with zero included:

$$
\mathbb U=[0,\infty).
$$

For two terms,

$$
U=u^2,\qquad V=v^2,
$$

the joined value is defined from the inner states:

$$
U+V=(u+v)^2.
$$

It is admissible when:

$$
(u+v)^2\in\mathbb U.
$$

If the inner-state product distributes, this can be read as the ordered
condition:

$$
u^2+uv+vu+v^2\in\mathbb U.
$$

This is the basic closure rule.

## Descriptor Admissibility

When the ordered cross terms are reduced by a scalar coefficient,

$$
d(U,V)=uv+vu\rightsquigarrow 2\kappa uv,
$$

the joined value becomes:

$$
U+V=u^2+v^2+2\kappa uv.
$$

In that reduction, the coefficient $\kappa$ is admissible for this joining when:

$$
u^2+v^2+2\kappa uv\ge0.
$$

Equivalently:

$$
U+V\in\mathbb U.
$$

## Bounded Opposition

In the bounded angular or field-alignment scale,

$$
-1\le \kappa\le1,
$$

closure is automatic:

$$
u^2+v^2+2\kappa uv\ge(u-v)^2\ge0.
$$

The smallest value occurs at complete opposition:

$$
\kappa=-1.
$$

Then:

$$
U+V=(u-v)^2.
$$

Thus opposition can cancel equal inner magnitudes to zero, but it cannot push a
joined ultrareal below zero while remaining in the bounded scale.

## Exact Cancellation

For nonzero ultrareals, exact cancellation in the bounded scale has only one
form.

Let:

$$
A=a^2,\qquad B=b^2,\qquad a,b>0.
$$

If:

$$
A+B=0,
$$

then:

$$
a^2+b^2+2\kappa ab=0.
$$

Solving for $\kappa$ gives:

$$
\kappa=-\frac{a^2+b^2}{2ab}.
$$

By the arithmetic-geometric mean inequality,

$$
\frac{a^2+b^2}{2ab}\ge1,
$$

with equality only when $a=b$. Therefore, inside $-1\le \kappa\le1$, exact
cancellation requires:

$$
a=b,\qquad \kappa=-1.
$$

Complete opposition is the only bounded relation that cancels two nonzero
ultrareals, and it cancels them only when their inner magnitudes are equal.

## Many-Term Addition

For many ultrareals,

$$
U_i=u_i^2,\qquad i=1,\ldots,n,
$$

the common commutative scalar reduction can be recorded by a coefficient table
$K=(\kappa_{ij})$. The same overloaded $+$ is used:

$$
\boxed{
U_1+\cdots+U_n
:=
\sum_i u_i^2
+2\sum_{i<j}\kappa_{ij}u_i u_j
}
$$

Before this scalar reduction, the many-term upper-case addition is simply:

$$
U_1+\cdots+U_n:=(u_1+\cdots+u_n)^2,
$$

with the expansion determined by the ordering, products, and parentheses of the
chosen inner-state algebra.

When the inner-state product is distributive and the order is explicit, the
pairwise interaction descriptors are:

$$
d(U_i,U_j):=u_i u_j+u_j u_i.
$$

The coefficient table is the common scalar reduction:

$$
d(U_i,U_j)\rightsquigarrow 2\kappa_{ij}u_i u_j.
$$

The diagonal entries are fixed:

$$
\kappa_{ii}=1.
$$

The off-diagonal entries record relations between distinct parts:

$$
\kappa_{ij}=\kappa_{ji}.
$$

In matrix form, with

$$
\mathbf u=(u_1,\ldots,u_n)^{\mathsf T},
$$

the joined value is:

$$
\mathbf u^{\mathsf T}K\mathbf u.
$$

The coefficient table is admissible for the given joining when:

$$
\mathbf u^{\mathsf T}K\mathbf u\ge0.
$$

It is admissible for every real inner state when:

$$
K\succeq0.
$$

It is admissible for every nonnegative ultrareal inner state when it is
copositive on the positive cone:

$$
\mathbf u\ge0
\quad\Longrightarrow\quad
\mathbf u^{\mathsf T}K\mathbf u\ge0.
$$

For a concrete sum, the state-specific condition is enough. For a whole class of
sums, the table itself must satisfy the appropriate positivity condition.

## Recovered Special Cases

Ordinary arithmetic is recovered when all off-diagonal relations vanish:

$$
\kappa_{ij}=0\qquad(i\ne j).
$$

Then:

$$
U_1+\cdots+U_n
=u_1^2+\cdots+u_n^2.
$$

Fully aligned addition is recovered when every off-diagonal relation is one:

$$
\kappa_{ij}=1\qquad(i\ne j).
$$

Then:

$$
U_1+\cdots+U_n=(u_1+\cdots+u_n)^2.
$$

The arithmetic point is simple: addition is not only a rule for collecting
visible values. It can also be a rule for joining inner magnitudes through an
admissible relation structure.
