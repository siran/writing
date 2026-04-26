# Pythagorean Addition and Angles

Pythagoras appears naturally in ultrareal arithmetic.

The relation-aware addition rule is:

$$
U + V = u^2 + v^2 + 2uv\cos(\theta)
$$

where $U = u^2$ and $V = v^2$. The overloaded $+$ reads the parts being added;
the angle $\theta$ is one way to specify their interaction descriptor:

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

This is the Pythagorean case.

If:

$$
c^2 = u^2 + v^2
$$

then:

$$
c = \sqrt{u^2 + v^2}
$$

So the Pythagorean theorem is standard arithmetic recovered as orthogonal
ultrareal addition.

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

For joined inner values:

$$
|u + ve^{i\theta}|^2
= u^2 + v^2 + 2uv\cos(\theta)
$$

For the opposite side of a triangle, the conventional sign is:

$$
c^2 = u^2 + v^2 - 2uv\cos(C)
$$

The difference is orientation convention. The content is the same: the
square-value depends on the relation between the inner values.

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
values are oriented before the square-value is evaluated.

## Why This Matters

The Pythagorean theorem is often taught as a special geometric fact.

In ultrareal arithmetic, it becomes one case of a larger addition rule:

$$
\begin{aligned}
\text{relation term present:}\quad &u^2 + v^2 + 2uv\cos(\theta),\\
\text{relation term zero:}\quad &u^2 + v^2,\\
\text{relation term negative:}\quad &u^2 + v^2 - 2uv.
\end{aligned}
$$

So Pythagoras is not outside the new arithmetic.

It is what standard arithmetic looks like when the inner values meet at right
angle.
