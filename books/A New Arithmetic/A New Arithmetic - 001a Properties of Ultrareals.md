# Properties of Ultrareals

An ultrareal number is a positive square-form:

```text
U = u^2
```

with:

```text
u >= 0
```

The basic ultrareal domain is:

```text
UR = {u^2 | u >= 0}
```

## Positive Definiteness

Every ultrareal is nonnegative:

```text
U >= 0
```

There are no negative ultrareals.

The only ultrareal that is neither positive nor negative is zero:

```text
0 = 0^2
```

## Square Representation

Every positive ordinary number can be represented as an ultrareal:

```text
X = x^2
```

This does not make `X` unreal. It gives `X` an inner value `x`.

The distinction is:

```text
visible value:  X
inner value:    x
```

## Equality

Two ultrareals are equal when their positive square-forms are equal:

```text
u^2 = v^2
```

Since the ultrareal layer uses `u >= 0` and `v >= 0`, this also means:

```text
u = v
```

If signs or rotations are introduced, they belong to the inner layer, not to the ultrareal value itself.

## Zero

Zero is the additive identity:

```text
0^2 + u^2 = u^2
```

for any interaction descriptor, because the relation term vanishes:

```text
2d(0^2,u^2)(0)u = 0
```

## Relation-Aware Addition

The general two-term addition uses an overloaded `+`. The operator is aware of the parts being added: the visible values and their inner values.

```text
U + V = u^2 + v^2 + 2d(U,V)uv
```

where:

```text
U = u^2
V = v^2
```

The descriptor `d(U,V)` records relation.

It is continuous over:

```text
-1 <= d(U,V) <= 1
```

So relation-aware addition includes partial alignment, not only the three named
cases of alignment, orthogonality, and opposition.

If `d(U,V)` comes from an angle, then:

```text
d(U,V) = cos(theta)
```

and:

```text
U + V = u^2 + v^2 + 2uv cos(theta)
```

## Closure

For the continuous range:

```text
-1 <= d(U,V) <= 1
```

the result remains ultrareal:

```text
u^2 + v^2 + 2d(U,V)uv >= 0
```

The smallest case is opposition:

```text
d(U,V) = -1
```

which gives:

```text
(u - v)^2 >= 0
```

So relation-aware addition does not require negative ultrareals.

## Standard Arithmetic

Standard arithmetic is recovered when:

```text
d(U,V) = 0
```

Then:

```text
U + V = u^2 + v^2
```

So standard addition is the non-interaction case.

## Aligned Addition

Aligned ultrareal addition is:

```text
d(U,V) = 1
U + V = (u + v)^2
```

This operation is commutative:

```text
u^2 + v^2 = v^2 + u^2
```

and associative:

```text
(u^2 + v^2) + w^2 = u^2 + (v^2 + w^2)
```

because both sides equal:

```text
(u + v + w)^2
```

## Many-Term Addition

For many terms, the relation-aware form is:

```text
(u_1 + u_2 + ... + u_n)^2
```

Expanded:

```text
u_1^2 + u_2^2 + ... + u_n^2
+ 2 sum_{i<j} u_i u_j
```

If the terms have different relations, the coefficients must be shown:

```text
u_1^2 + ... + u_n^2
+ 2 sum_{i<j} d_ij u_i u_j
```

The descriptors `d_ij` are part of the arithmetic data.

## Multiplication

Ultrareal multiplication is inherited from the inner values:

```text
u^2 *_UR v^2 = (uv)^2
```

The multiplicative identity is:

```text
1 = 1^2
```

For aligned addition, multiplication distributes:

```text
u^2 *_UR (v^2 + w^2)
= (uv)^2 + (uw)^2
```

## No Negative Inverses Inside UR

Except for zero, no ultrareal has an additive inverse inside `UR`.

There is no positive square-form `V` such that:

```text
U + V = 0
```

for positive `U`, unless the cancellation is carried by inner opposition:

```text
(u - u)^2 = 0
```

Negativity belongs to rotation or opposition in the inner layer, not to ultrareal magnitude.
