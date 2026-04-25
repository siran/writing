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
