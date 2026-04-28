# Relation-Aware Addition

Ultrareal arithmetic overloads the symbol $+$ by the layer of its operands.

Lower-case symbols name inner magnitudes or inner states. Upper-case symbols
name visible ultrareal values:

$$
U=u^2,\qquad V=v^2,\qquad u,v\ge0.
$$

When lower-case inner states are added, ordinary inner-state addition is being
used:

$$
u+v.
$$

When upper-case ultrareals are added, the definition uses the joined inner
states:

$$
\boxed{
U+V := (u+v)^2
}
$$

This is the definition. If:

$$
X=U+V,
$$

then $X=x^2$ by definition, and the joined inner state is:

$$
x=u+v.
$$

Therefore:

$$
X=x^2=U+V=(u+v)^2.
$$

The operator is still $+$. The operands determine which layer is being used.

## Ordered Expansion

Expanding the defining square gives the interaction terms. If the inner-state
product distributes, then:

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

When the descriptor is being displayed, the same joined value may also be
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

Nor is there a need to assume that every larger joining is associative without
stating the inner-state algebra that makes it so. Commutativity and
associativity are common and useful in many applications, but they are not part
of the bare ultrareal definition.

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

The printed expression is the same, but the operands and relation are not the
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

Opposition can reduce a joined value. It cannot create a negative ultrareal
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
or otherwise structured relation data. The formal requirement is not that every
descriptor be commutative, scalar, or associative. The formal requirement is
admissibility: the joined value must remain an ultrareal.

The important order is:

$$
U+V := (u+v)^2
$$

first, and only then, when the inner-state product distributes:

$$
d(U,V):=uv+vu.
$$

Thus $d(U,V)$ is not an extra number placed beside addition. It is the
interaction term exposed by expanding the square of the joined inner states.

## Basic Laws

For fully aligned joining in a commutative and associative inner-state setting,
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
the joining. The many-term form makes that structure explicit.
