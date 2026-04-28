# Term-Type-Aware Addition

Ultrareal arithmetic uses one addition operation,
$+(\cdot,\cdot)$, read through the terms supplied to it.

Lower-case symbols name inner magnitudes, inner states, or presentations of
inner states when relation data is present. Upper-case symbols name visible
ultrareal values:

$$
U=u^2,\qquad V=v^2,\qquad u,v\ge0.
$$

For natural scalar inner states, lower-case addition is ordinary inner-state
addition:

$$
+(u,v)=u+v.
$$

When upper-case ultrareals are added, the result is the ultrareal determined by
the corresponding lower-case sum. Since $U=u^2$ and $V=v^2$:

$$
+(U,V)=U+V=(+(u,v))^2.
$$

In the natural scalar case:

$$
+(U,V)=U+V=(u+v)^2.
$$

Thus the printed sign is the same. The term type determines how the operation
is read.

## Closure Of Ultrareal Addition

The natural scalar upper-case sum must remain inside $\mathbb U$.

Let:

$$
U,V\in\mathbb U,\qquad U=u^2,\qquad V=v^2.
$$

Then:

$$
u,v\in\mathbb R_{\ge0}.
$$

The nonnegative reals are closed under ordinary addition, so the inner-state
sum:

$$
x=+(u,v)=u+v
$$

also lies in the nonnegative reals:

$$
x\in\mathbb R_{\ge0}.
$$

By the definition of an ultrareal number, $x^2\in\mathbb U$. Call this
ultrareal $X$:

$$
X=x^2.
$$

This proves that adding two ultrareals gives another ultrareal. Since
$+(U,V)$ is the ultrareal determined by $+(u,v)$:

$$
+(U,V)=U+V=X.
$$

Therefore:

$$
U+V=X=x^2=(u+v)^2.
$$

Nothing new is being added to the square-form. The upper-case result follows
from the lower-case sum and the definition $U=u^2$.

The operator is still $+$. The operands determine which layer is being used.

## Ordered Expansion

Expanding this square gives the interaction terms. If the inner-state product
distributes, then:

$$
(u+v)^2=(u+v)(u+v)=u^2+uv+vu+v^2.
$$

The middle terms are ordered. They are the interaction descriptor:

$$
d(U,V):=uv+vu.
$$

Thus:

$$
U+V=u^2+d(U,V)+v^2.
$$

When the descriptor is being displayed, the same sum may also be
written:

$$
U\,d\,V:=uu+uv+vu+vv.
$$

Equivalently:

$$
U\,d\,V=U+V=u^2+d(U,V)+v^2.
$$

The symbol $d$ in this notation marks that the interaction descriptor is being
included.

In general, there is no need to assume:

$$
uv=vu.
$$

Nor is there a need to assume that every many-term expression is associative
without stating the inner-state algebra that makes it so. Commutativity and
associativity are available when the arithmetic of the particular case supplies
them, but they are not imposed by the bare ultrareal definition.

## Standard Arithmetic

Standard arithmetic is recovered when the descriptor vanishes:

$$
d(U,V)=0.
$$

Then:

$$
U+V=u^2+v^2.
$$

This is the non-interaction case. The visible values are counted together, and
no interaction term remains.

This is not a second addition operation. It is the same upper-case sum read
with zero relation data.

For unit values in this case:

$$
1+1=2.
$$

## Aligned Scalar Case

In the common commutative scalar case:

$$
uv=vu.
$$

Full alignment gives:

$$
d(U,V)=uv+vu=2uv.
$$

Then:

$$
U+V=u^2+v^2+2uv=(u+v)^2.
$$

For unit values in the aligned case:

$$
1+1=(1+1)^2=4.
$$

This is why the opening claim is precise:

$$
1+1 \text{ is not necessarily only } 2.
$$

The printed expression is the same, but the term data and relation are not the
same. Separated visible units recover $2$. Aligned unit magnitudes produce $4$.

## Opposed Scalar Case

Complete opposition in the same scalar setting gives:

$$
d(U,V)=-2uv.
$$

Then:

$$
U+V=u^2+v^2-2uv=(u-v)^2.
$$

Opposition can reduce a sum. It cannot create a negative ultrareal
inside this bounded relation scale.

If $u=v$, complete opposition gives:

$$
U+U=0
\qquad(d(U,U)=-2u^2).
$$

This is cancellation to the zero boundary, not passage into negative
ultrareal value.

## Descriptor Structure

An interaction descriptor may encode angular, hyperbolic, weighted, tangential,
or otherwise structured relation data. It need not be commutative, scalar, or
associative in advance. The formal requirement is admissibility: the result
must remain an ultrareal.

The important order in the natural scalar case is the closure proof:

$$
u,v\in\mathbb R_{\ge0}
\quad\Longrightarrow\quad
x=u+v\in\mathbb R_{\ge0}
\quad\Longrightarrow\quad
X=x^2\in\mathbb U.
$$

Then the upper-case sum can be written:

$$
U+V=X=(u+v)^2.
$$

Only then, when the inner-state product distributes:

$$
d(U,V):=uv+vu.
$$

Thus $d(U,V)$ is not an extra number placed beside addition. It is the
interaction term exposed by expanding the square of the added inner states.

## Basic Laws

For fully aligned addition in a commutative and associative inner-state setting,
addition has the familiar laws:

$$
U+V=(u+v)^2=(v+u)^2=V+U.
$$

For three aligned terms:

$$
(U+V)+W
=U+(V+W)
=(u+v+w)^2.
$$

Without those properties, ordering and parentheses remain part of the data of
the expression. The many-term form makes that structure explicit.
