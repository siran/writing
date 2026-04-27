# Relation-Aware Addition

Ultrareal arithmetic distinguishes visible value from inner magnitude:

$$
U=u^2,\qquad V=v^2,\qquad u,v\ge0.
$$

Once the inner magnitudes are available, addition can include the relation
between the parts. The two-term relation-aware sum is:

$$
\boxed{
U\oplus_d V:=u^2+v^2+2duv
}
$$

The descriptor $d$ is not an ultrareal number. It is relation data for this
joining.

The operator $\oplus_d$ is used here to keep the formal structure visible. When
the descriptor is fixed by context, one may write a plain plus sign as a
shorthand, but the descriptor is part of the operation.

## The Recovered Ordinary Case

Ordinary addition of visible values is recovered when the relation descriptor is
zero:

$$
d=0.
$$

Then:

$$
U\oplus_0 V=u^2+v^2.
$$

This is the arithmetic of non-interacting parts. The quantities are counted
together, but no cross term is included.

For unit values:

$$
1\oplus_0 1=1+1=2.
$$

## Aligned Addition

Aligned addition is the case:

$$
d=1.
$$

Then:

$$
U\oplus_1 V=u^2+v^2+2uv=(u+v)^2.
$$

For unit values:

$$
1\oplus_1 1=(1+1)^2=4.
$$

This is why the opening claim is precise:

$$
1+1 \text{ is not necessarily only } 2.
$$

The result depends on the operation. Non-interacting unit values recover $2$.
Aligned unit values produce $4$.

## Opposed Addition

Opposed addition is the case:

$$
d=-1.
$$

Then:

$$
U\oplus_{-1} V=u^2+v^2-2uv=(u-v)^2.
$$

Opposition can reduce a joined value. It cannot create a negative ultrareal
inside this bounded relation scale.

If $u=v$, complete opposition gives:

$$
U\oplus_{-1}U=0.
$$

This is cancellation to the zero boundary, not passage into negative
ultrareal value.

## The Descriptor

The descriptor records the relation required by the quantities being joined.
In the simplest bounded scale:

$$
-1\le d\le1.
$$

The endpoints have clear meanings:

$$
d=1 \quad\text{aligned},\qquad
d=0 \quad\text{non-interacting},\qquad
d=-1 \quad\text{opposed}.
$$

Other descriptor systems are possible. A descriptor may encode angular,
hyperbolic, weighted, tangential, or otherwise structured relation data. The
formal requirement is not that every descriptor be angular. The formal
requirement is admissibility: the joined value must remain an ultrareal.

## Basic Laws In The Fixed-Descriptor Cases

For the recovered ordinary case, $\oplus_0$ is ordinary addition of visible
values:

$$
U\oplus_0 V=U+V.
$$

It is commutative and associative because ordinary addition is commutative and
associative.

For fully aligned joining, the operation is also commutative and associative:

$$
U\oplus_1 V=(u+v)^2=(v+u)^2=V\oplus_1 U.
$$

For three aligned terms:

$$
(U\oplus_1 V)\oplus_1 W
=U\oplus_1(V\oplus_1 W)
=(u+v+w)^2.
$$

For general relation-aware addition, associativity is not a property of a
single two-term descriptor alone. It belongs to the whole relation structure
among all parts. That structure is made explicit by the many-term form.
