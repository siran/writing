# Joined Addition

The central operation is joined addition.

Ordinary addition begins from separated objects:

```text
one thing + one thing = two things
```

Joined addition begins from the situation created when those things are actually together.

This matters because addition has often been mistaken for union. But union is union. It says the parts are in one set. It does not say what the parts do to one another.

Joined addition asks for the new condition created by the joining.

If

```text
U = u^2
V = v^2
```

then, in the aligned case, the overloaded operator `+` can read both the visible values and their inner values:

```text
U + V := (u + v)^2
```

Equivalently, in square-form notation:

```text
u^2 + v^2 := (u + v)^2
```

This is the defining axiom of aligned ultrareal addition.

Expanded into old notation:

```text
(u + v)^2 = u^2 + v^2 + 2uv
```

The first two terms are what ordinary inventory would keep. The last term is the relation term.

## Standard Arithmetic As A Special Case

Standard arithmetic is not discarded. It is recovered as the special case of non-interacting things.

In standard arithmetic:

```text
U + V
```

means that `U` and `V` are counted together while their relation is ignored, absent, canceled, or irrelevant.

In ultrareal arithmetic, the fuller joined form uses an interaction descriptor:

```text
U + V := u^2 + v^2 + 2d(U,V)uv
```

The aligned ultrareal case has:

```text
d(U,V) = 1
```

The standard case has:

```text
d(U,V) = 0
```

The relation term is then zero because the operation deliberately studies units as non-interacting:

```text
u^2 + v^2 + 2(0)uv = u^2 + v^2
```

This makes standard arithmetic an object of study inside the larger system. It is the arithmetic of indifferent units: useful, precise, and limited.

The ultrareal question is different:

```text
what happens when the units are not indifferent?
```

## Zero

Zero remains the additive identity:

```text
0^2 + u^2 = (0 + u)^2 = u^2
```

## Commutativity

Joined addition is commutative:

```text
u^2 + v^2 = (u + v)^2 = (v + u)^2 = v^2 + u^2
```

The order of joining does not change the joined value.

## Associativity

Joined addition is associative:

```text
(u^2 + v^2) + w^2
= (u + v)^2 + w^2
= (u + v + w)^2
```

and

```text
u^2 + (v^2 + w^2)
= u^2 + (v + w)^2
= (u + v + w)^2
```

So:

```text
(u^2 + v^2) + w^2 = u^2 + (v^2 + w^2)
```

## Many Terms

For many joined ultrareals:

```text
u_1^2 + u_2^2 + ... + u_n^2
= (u_1 + u_2 + ... + u_n)^2
```

Expanded:

```text
(u_1 + ... + u_n)^2
= u_1^2 + ... + u_n^2
  + 2 sum_{i<j} u_i u_j
```

Every pair contributes a relation term.

## Repeated Unit

The joined sum of `n` unit ultrareals is:

```text
1 + 1 + ... + 1 = n^2
```

So:

```text
1 + 1 = 4
1 + 1 + 1 = 9
1 + 1 + 1 + 1 = 16
```

Classical counting gives the arithmetic of separated units. Joined addition gives the arithmetic of units brought into one situation.

## Relation Is The Point

The formula above is the simplest case: aligned joining, where the relation term is positive.

Daily life also shows damaging or canceling relations. A rotten apple added to a bag increases the inventory count, but may reduce the value of the bag. That is not a failure of arithmetic. It is evidence that inventory and relation are different layers.

The next step is therefore to let the inner values carry opposition and rotation.
