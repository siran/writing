# What We Want To Calculate

The aim of this book is not to make arithmetic vague.

It is to make clear what arithmetic is calculating.

Standard arithmetic calculates a simplified case where units do not interact. In that case, addition behaves like mathematical union: the parts are placed together, and the relation between them is not calculated.

```text
d(U,V) = 0
```

Ultrareal arithmetic asks what changes when the relation is not zero.

## The Basic Objects

We begin with Numbers as positive density-values:

```text
N = n^2
```

A Number is the visible value we handle. Its inner value is the lower-case term whose square gives that visible value.

For two Numbers:

```text
U = u^2
V = v^2
```

The visible values are `U` and `V`.

The inner values are `u` and `v`.

## The Basic Question

The central question is:

```text
what is the value of U with V?
```

Not merely:

```text
how many units are present?
```

but:

```text
what does their relation contribute?
```

## The Relation Term

The general two-term calculation uses the overloaded operator `+`:

```text
U + V = u^2 + v^2 + 2d(U,V)uv
```

where `d(U,V)` records the relation between the parts being added. The operator is defined on the operands `U = u^2` and `V = v^2`, and it uses the inner values `u` and `v`.

Important cases:

```text
d(U,V) =  1   aligned joining
d(U,V) =  0   non-interaction or orthogonality
d(U,V) = -1   opposition
```

So:

```text
aligned:        U + V = (u + v)^2
standard:       U + V = u^2 + v^2
opposed:        U + V = (u - v)^2
```

## What This Lets Us Calculate

This framework lets us calculate:

```text
standard arithmetic as non-interaction
joined addition as aligned interaction
opposition and cancellation
Pythagorean addition
angle-dependent addition
trigonometric addition laws
repeated units
split-and-rejoin cases
rotated negative values
rotated infinity
```

The point is not that every situation uses the same interaction descriptor.

The point is that ordinary arithmetic uses the case `d(U,V) = 0`.

Ultrareal arithmetic makes the relation visible.
