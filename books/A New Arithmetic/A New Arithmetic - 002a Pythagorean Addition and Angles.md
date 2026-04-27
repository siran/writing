# Pythagorean Addition and Angles

Pythagoras appears naturally in ultrareal arithmetic.

The relation-aware addition rule is:

$$
U + V = u^2 + v^2 + 2uv\cos(\theta)
$$

where $U = u^2$ and $V = v^2$. The overloaded $+$ reads the parts being added.
For vector-like or phase-like quantities, the angle $\theta$ is one way to
specify their interaction descriptor:

$$
d(U,V) = \cos(\theta)
$$

## Aligned Addition

When:

$$
\theta = 0
$$

we have:

$$
\cos(0) = 1
$$

so:

$$
U + V = u^2 + v^2 + 2uv = (u + v)^2
$$

This is aligned ultrareal addition.

## Orthogonal Addition

When:

$$
\theta = \frac{\pi}{2}
$$

we have:

$$
\cos\left(\frac{\pi}{2}\right) = 0
$$

so:

$$
U + V = u^2 + v^2
$$

This is the zero-relation form.

If:

$$
c^2 = u^2 + v^2
$$

then:

$$
c = \sqrt{u^2 + v^2}
$$

So the Pythagorean theorem has the same algebraic form as standard arithmetic:
the relation term is zero. When the descriptor is angular, that zero-relation
condition is orthogonality.

Standard addition is not the absence of structure. It is the case where the
relation term vanishes.

## Opposed Addition

When:

$$
\theta = \pi
$$

we have:

$$
\cos(\pi) = -1
$$

so:

$$
U + V = u^2 + v^2 - 2uv = (u - v)^2
$$

Opposition still produces a positive square-form.

If $u = v$, the result is:

$$
(u - u)^2 = 0
$$

That is cancellation, not negative magnitude.

## The Law Of Cosines

The same formula recovers the law of cosines.

For joined inner states:

$$
|u + ve^{i\theta}|^2
= u^2 + v^2 + 2uv\cos(\theta)
$$

For the opposite side of a triangle, the conventional sign is:

$$
c^2 = u^2 + v^2 - 2uv\cos(C)
$$

The difference is orientation convention. The content is the same: the
square-value depends on the relation between the inner states.

## Angle Addition

Euler's rotation rule also recovers the standard angle-addition formulas.

Rotations multiply:

$$
e^{i\alpha}e^{i\beta} = e^{i(\alpha + \beta)}
$$

Using:

$$
e^{i\theta} = \cos(\theta) + i\sin(\theta)
$$

the left side becomes:

$$
(\cos\alpha + i\sin\alpha)(\cos\beta + i\sin\beta)
$$

Expanding and collecting real and imaginary parts gives:

$$
\cos(\alpha + \beta)
= \cos\alpha\cos\beta - \sin\alpha\sin\beta
$$

and:

$$
\sin(\alpha + \beta)
= \sin\alpha\cos\beta + \cos\alpha\sin\beta
$$

So trigonometry is also relation arithmetic. It is the arithmetic of how inner
states are oriented before the square-value is evaluated.

## Why This Matters

The Pythagorean theorem is often taught as a standalone geometric fact. In
ultrareal arithmetic, the recovered special case is non-interaction:

$$
d(U,V)=0.
$$

When the descriptor is angular, non-interaction is represented by a right
angle:

$$
\cos\left(\frac{\pi}{2}\right)=0.
$$

So Pythagoras is not a separate arithmetic. It is the geometric face of the
same zero-relation condition that recovers standard addition.
