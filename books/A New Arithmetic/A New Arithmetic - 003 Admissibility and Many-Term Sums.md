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

the joined value is:

$$
U+V=u^2+v^2+2duv.
$$

The descriptor $d$ is admissible for this joining when:

$$
u^2+v^2+2duv\ge0.
$$

Equivalently:

$$
U+V\in\mathbb U.
$$

This is the basic closure rule.

## Bounded Opposition

In the bounded angular or field-alignment scale,

$$
-1\le d\le1,
$$

closure is automatic:

$$
u^2+v^2+2duv\ge(u-v)^2\ge0.
$$

The smallest value occurs at complete opposition:

$$
d=-1.
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
a^2+b^2+2dab=0.
$$

Solving for $d$ gives:

$$
d=-\frac{a^2+b^2}{2ab}.
$$

By the arithmetic-geometric mean inequality,

$$
\frac{a^2+b^2}{2ab}\ge1,
$$

with equality only when $a=b$. Therefore, inside $-1\le d\le1$, exact
cancellation requires:

$$
a=b,\qquad d=-1.
$$

Complete opposition is the only bounded relation that cancels two nonzero
ultrareals, and it cancels them only when their inner magnitudes are equal.

## Many-Term Addition

For many ultrareals,

$$
U_i=u_i^2,\qquad i=1,\ldots,n,
$$

relation-aware addition is determined by a relation table $D=(d_{ij})$. The
same overloaded $+$ is used:

$$
\boxed{
U_1+\cdots+U_n
:=
\sum_i u_i^2
+2\sum_{i<j}d_{ij}u_i u_j
}
$$

The diagonal entries are fixed:

$$
d_{ii}=1.
$$

The off-diagonal entries record relations between distinct parts:

$$
d_{ij}=d_{ji}.
$$

In matrix form, with

$$
\mathbf u=(u_1,\ldots,u_n)^{\mathsf T},
$$

the joined value is:

$$
\mathbf u^{\mathsf T}D\mathbf u.
$$

The relation table is admissible for the given joining when:

$$
\mathbf u^{\mathsf T}D\mathbf u\ge0.
$$

It is admissible for every real inner state when:

$$
D\succeq0.
$$

It is admissible for every nonnegative ultrareal inner state when it is
copositive on the positive cone:

$$
\mathbf u\ge0
\quad\Longrightarrow\quad
\mathbf u^{\mathsf T}D\mathbf u\ge0.
$$

For a concrete sum, the state-specific condition is enough. For a whole class of
sums, the table itself must satisfy the appropriate positivity condition.

## Recovered Special Cases

Ordinary arithmetic is recovered when all off-diagonal relations vanish:

$$
d_{ij}=0\qquad(i\ne j).
$$

Then:

$$
U_1+\cdots+U_n
=u_1^2+\cdots+u_n^2.
$$

Fully aligned addition is recovered when every off-diagonal relation is one:

$$
d_{ij}=1\qquad(i\ne j).
$$

Then:

$$
U_1+\cdots+U_n=(u_1+\cdots+u_n)^2.
$$

The arithmetic point is simple: addition is not only a rule for collecting
visible values. It can also be a rule for joining inner magnitudes through an
admissible relation structure.
