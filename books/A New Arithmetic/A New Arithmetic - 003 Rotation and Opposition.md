# Rotation and Opposition

An ultrareal number is a positive square-form:

```text
U = u^2
```

with `u` real. But the inner value that exposes it can carry orientation.

The simplest orientation is sign:

```text
u
-u
```

Both expose the same ultrareal:

```text
u^2 = (-u)^2
```

So sign is not visible as a negative magnitude. It is visible only when inner values are joined.

## Opposition

If two inner values are opposed, their joined value is:

```text
u^2 + (-v)^2 := (u - v)^2
```

Expansion gives:

```text
(u - v)^2 = u^2 + v^2 - 2uv
```

The negative sign appears in the relation term. It does not create a negative ultrareal.

The special case of perfect opposition is cancellation:

```text
u^2 + (-u)^2 := (u - u)^2 = 0
```

The result is not less than zero. It is absence after opposition.

## Negative Values

A negative value requires a rotation out of the ultrareal layer:

```text
-U = (iu)^2
```

because:

```text
(iu)^2 = i^2 u^2 = -u^2
```

So a negative number is not a negative ultrareal. It is a rotated square-value.

The symbol `i` marks that rotation. It does not mean the positive value has disappeared. It means the square-value is returning through the inner layer from another direction:

```text
U = u^2
-U = (iu)^2
```

## Rotated Infinity

The same rule applies at infinity.

Positive infinity is the unbounded limit of positive square-forms:

```text
U = u^2
u -> infinity
U -> infinity
```

Negative infinity is not a different kind of negative substance. It is the same unbounded positive square-form seen through the rotated branch:

```text
-U = (iu)^2
u -> infinity
-U -> -infinity
```

So:

```text
-infinity = rotated infinity
```

In the ultrareal layer there is only positive unbounded value. The negative sign belongs to orientation.

## Euler's Rotation

Euler's identity gives the standard notation for this rotation:

```text
e^{i theta} = cos(theta) + i sin(theta)
```

This expression represents a point on the unit circle in the complex plane. Changing `theta` rotates the point.

At a quarter-turn:

```text
theta = pi/2
e^{i pi/2} = i
```

So:

```text
i = e^{i pi/2}
```

Squaring `i` doubles the rotation:

```text
i^2 = e^{i pi} = -1
```

Therefore:

```text
i = sqrt(-1)
```

more precisely:

```text
sqrt(-1) = +/- i
```

This is the arithmetic reason negative values can be understood as rotated positive square-values. The negative sign is a half-turn in value-space, produced by a quarter-turn in the inner square-root layer.

## General Rotation

Let the inner value be rotated:

```text
a = u e^{i theta}
```

Then:

```text
a^2 = u^2 e^{i 2theta}
```

The outer orientation is doubled. A quarter-turn of the inner value becomes a half-turn of the squared value:

```text
theta = pi/2
(u e^{i pi/2})^2 = -u^2
```

This is why `u^2` can be negative if `u` is not real. The negative square is not an ultrareal value; it is the result of rotating the inner value before squaring.

## Rotation-Aware Joining

If two inner values carry orientations,

```text
a = u e^{i alpha}
b = v e^{i beta}
```

then their positive joined value is:

```text
|a + b|^2
```

Expanded:

```text
|a + b|^2 = u^2 + v^2 + 2uv cos(alpha - beta)
```

The relation term depends on relative orientation.

Aligned joining:

```text
alpha - beta = 0
|a + b|^2 = (u + v)^2
```

Opposed joining:

```text
alpha - beta = pi
|a + b|^2 = (u - v)^2
```

Relation-erased joining:

```text
alpha - beta = pi/2
|a + b|^2 = u^2 + v^2
```

Ordinary addition is therefore not the whole operation. It is the case where the relation term is absent, canceled, or ignored.
