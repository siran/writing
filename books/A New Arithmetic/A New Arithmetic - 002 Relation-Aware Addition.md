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

This is the definition. Since $X=x^2$, adding upper-case ultrareals means
squaring the joined lower-case inner states. The operator is still $+$. The
operands determine which layer is being used.

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

## Commutative Reduction

In the common commutative scalar case:

$$
uv=vu.
$$

Then the ordered expansion reduces to:

$$
U+V=u^2+v^2+2uv.
$$

This is the fully aligned case.

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

## Descriptor Reduction

In many common cases, the interaction descriptor can be summarized by a scalar
coefficient $\kappa$:

$$
d(U,V)=uv+vu\rightsquigarrow 2\kappa uv.
$$

Then the same upper-case addition has the scalar reduction:

$$
U+V=u^2+v^2+2\kappa uv.
$$

The descriptor $d(U,V)$ is not an ultrareal number. It is relation data for this
joining. The coefficient $\kappa$ is a normalized scalar summary of that
descriptor when such a summary is available.

The standard coefficient values are:

$$
\kappa=1 \quad\text{aligned},\qquad
\kappa=0 \quad\text{non-interacting},\qquad
\kappa=-1 \quad\text{opposed}.
$$

When $\kappa=0$:

$$
U+V=u^2+v^2.
$$

This is the recovered ordinary case: the cross terms vanish.

When $\kappa=-1$:

$$
U+V=u^2+v^2-2uv=(u-v)^2.
$$

Opposition can reduce a joined value. It cannot create a negative ultrareal
inside this bounded relation scale.

If $u=v$, complete opposition gives:

$$
U+U=0
\qquad(\kappa=-1).
$$

This is cancellation to the zero boundary, not passage into negative
ultrareal value.

## Coefficients Are Reductions

An interaction descriptor may encode angular, hyperbolic, weighted, tangential,
or otherwise structured relation data. The formal requirement is not that every
descriptor reduce to a scalar coefficient. The formal requirement is
admissibility: the joined value must remain an ultrareal.

The important order is:

$$
U+V := (u+v)^2
$$

first, and only then, when the inner-state algebra permits it:

$$
d(U,V)=uv+vu \rightsquigarrow 2\kappa uv.
$$

Thus $2\kappa uv$ is not the definition of addition. It is a common scalar form
of the interaction descriptor.

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
