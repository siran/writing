# Pythagorean Addition and Angles

Pythagoras appears naturally in ultrareal arithmetic.

The relation-aware addition rule is:

```text
u^2 +_{theta} v^2 = u^2 + v^2 + 2uv cos(theta)
```

The angle `theta` records how the inner values meet.

## Aligned Addition

When:

```text
theta = 0
```

we have:

```text
cos(0) = 1
```

so:

```text
u^2 +_{theta=0} v^2 = u^2 + v^2 + 2uv = (u + v)^2
```

This is aligned ultrareal addition.

## Orthogonal Addition

When:

```text
theta = pi/2
```

we have:

```text
cos(pi/2) = 0
```

so:

```text
u^2 +_{theta=pi/2} v^2 = u^2 + v^2
```

This is the Pythagorean case.

If:

```text
c^2 = u^2 + v^2
```

then:

```text
c = sqrt(u^2 + v^2)
```

So the Pythagorean theorem is standard arithmetic recovered as orthogonal ultrareal addition.

Standard addition is not the absence of structure. It is the case where the relation term vanishes.

## Opposed Addition

When:

```text
theta = pi
```

we have:

```text
cos(pi) = -1
```

so:

```text
u^2 +_{theta=pi} v^2 = u^2 + v^2 - 2uv = (u - v)^2
```

Opposition still produces a positive square-form.

If `u = v`, the result is:

```text
(u - u)^2 = 0
```

That is cancellation, not negative magnitude.

## The Law Of Cosines

The same formula recovers the law of cosines.

For joined inner values:

```text
|u + v e^{i theta}|^2
= u^2 + v^2 + 2uv cos(theta)
```

For the opposite side of a triangle, the conventional sign is:

```text
c^2 = u^2 + v^2 - 2uv cos(C)
```

The difference is orientation convention. The content is the same: the square-value depends on the relation between the inner values.

## Angle Addition

Euler's rotation rule also recovers the standard angle-addition formulas.

Rotations multiply:

```text
e^{i alpha} e^{i beta} = e^{i(alpha + beta)}
```

Using:

```text
e^{i theta} = cos(theta) + i sin(theta)
```

the left side becomes:

```text
(cos alpha + i sin alpha)(cos beta + i sin beta)
```

Expanding and collecting real and imaginary parts gives:

```text
cos(alpha + beta) = cos alpha cos beta - sin alpha sin beta
```

and:

```text
sin(alpha + beta) = sin alpha cos beta + cos alpha sin beta
```

So trigonometry is also relation arithmetic. It is the arithmetic of how inner values are oriented before the square-value is evaluated.

## Why This Matters

The Pythagorean theorem is often taught as a special geometric fact.

In ultrareal arithmetic, it becomes one case of a larger addition rule:

```text
relation term present:     u^2 + v^2 + 2uv cos(theta)
relation term zero:        u^2 + v^2
relation term negative:    u^2 + v^2 - 2uv
```

So Pythagoras is not outside the new arithmetic.

It is what standard arithmetic looks like when the inner values meet at right angle.
