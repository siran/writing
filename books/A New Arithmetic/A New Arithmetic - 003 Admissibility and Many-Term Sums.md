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

the positive-ultrareal reading gives:

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

When the ordered cross terms are written as the descriptor,

$$
d(U,V)=uv+vu,
$$

the joined value becomes:

$$
U+V=u^2+d(U,V)+v^2.
$$

In scalar cases, the descriptor is admissible for this joining when:

$$
u^2+d(U,V)+v^2\ge0.
$$

Equivalently:

$$
U+V\in\mathbb U.
$$

## Bounded Opposition

In the bounded angular or field-alignment scale, the descriptor satisfies:

$$
-2uv\le d(U,V)\le 2uv.
$$

Closure is automatic:

$$
u^2+d(U,V)+v^2\ge(u-v)^2\ge0.
$$

The smallest value occurs at complete opposition:

$$
d(U,V)=-2uv.
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
a^2+d(A,B)+b^2=0.
$$

Solving for the descriptor gives:

$$
d(A,B)=-(a^2+b^2).
$$

By the arithmetic-geometric mean inequality,

$$
a^2+b^2\ge2ab,
$$

with equality only when $a=b$. Therefore, inside the bounded descriptor scale
$-2ab\le d(A,B)\le2ab$, exact cancellation requires:

$$
a=b,\qquad d(A,B)=-2ab.
$$

Complete opposition is the only bounded relation that cancels two nonzero
ultrareals, and it cancels them only when their inner magnitudes are equal.

## Many-Term Addition

For many ultrareals,

$$
U_i=u_i^2,\qquad i=1,\ldots,n,
$$

the pairwise descriptor table $D=(d_{ij})$ records the interaction terms. The
same overloaded $+$ is used:

$$
\boxed{
U_1+\cdots+U_n
:=
\sum_i u_i^2
+\sum_{i<j}d_{ij}
}
$$

Before this scalar reduction, the many-term upper-case addition is simply:

$$
U_1+\cdots+U_n:=(u_1+\cdots+u_n)^2,
$$

with the expansion determined by the ordering, products, and parentheses of the
chosen inner-state algebra.

When the inner-state product is distributive and the order is explicit, the
pairwise descriptors are:

$$
d_{ij}=d(U_i,U_j):=u_i u_j+u_j u_i.
$$

There is no separate interaction descriptor on the diagonal in this sum. The
visible square terms are already present as $u_i^2$. The off-diagonal entries
record interactions between distinct parts:

$$
d_{ij}=d_{ji}
$$

In matrix form, with

$$
\mathbf u=(u_1,\ldots,u_n)^{\mathsf T},
$$

the joined value is:

$$
\sum_i u_i^2+\sum_{i<j}d_{ij}.
$$

The descriptor table is admissible for the given joining when:

$$
\sum_i u_i^2+\sum_{i<j}d_{ij}\ge0.
$$

In the common scalar matrix representation, this may be rewritten as a quadratic
form $\mathbf u^{\mathsf T}K\mathbf u$. That representation is admissible for
every real inner state when:

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
d_{ij}=0\qquad(i\ne j).
$$

Then:

$$
U_1+\cdots+U_n
=u_1^2+\cdots+u_n^2.
$$

Fully aligned addition is recovered when every off-diagonal descriptor is the
commutative scalar descriptor:

$$
d_{ij}=2u_i u_j\qquad(i\ne j).
$$

Then:

$$
U_1+\cdots+U_n=(u_1+\cdots+u_n)^2.
$$

The arithmetic point is simple: addition is not only a rule for collecting
visible values. It can also be a rule for joining inner magnitudes through an
admissible relation structure.
