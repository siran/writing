# Multiplication and Powers

The previous chapter defined term-type-aware addition. Before the angular and
exponential tools used in later chapters can rest on a rigorous foundation,
scalar multiplication must be defined.

## Multiplication

Let $U=u^2$ and $V=v^2$ be ultrareals with scalar natural inner states. Their
product is:

$$
U \cdot V = (uv)^2.
$$

The inner magnitude of a product is the product of the inner magnitudes. Since
$u,v\ge0$, the product $uv\ge0$, so $(uv)^2\in\mathbb U$. Multiplication is
closed.

In the ordinary scalar case, multiplication is commutative:

$$
U\cdot V=(uv)^2=(vu)^2=V\cdot U.
$$

In the ordinary scalar case, multiplication is associative:

Let $W=w^2$. Then:

$$
(U\cdot V)\cdot W=((uv)w)^2=(u(vw))^2=U\cdot(V\cdot W).
$$

Multiplicative identity:

The ultrareal $1=1^2$ satisfies:

$$
1\cdot U=(1\cdot u)^2=u^2=U.
$$

Absorption at zero:

$$
0\cdot U=(0\cdot u)^2=0.
$$

## Distributivity

Whether multiplication distributes over addition depends on what the relevant
addition does to inner magnitudes.

For the natural scalar ultrareal addition $U+V=(u+v)^2$, the inner magnitude of
a sum is the sum of inner magnitudes. Under this term-type rule the proof
proceeds at the inner magnitude layer.

The inner magnitude of $V+W$ is $v+w$.

Therefore the inner magnitude of $U\cdot(V+W)$ is:

$$
u\cdot(v+w)=uv+uw.
$$

The inner magnitude of $U\cdot V$ is $uv$.
The inner magnitude of $U\cdot W$ is $uw$.
The inner magnitude of $(U\cdot V)+(U\cdot W)$ is:

$$
uv+uw.
$$

Both sides square the same inner magnitude. Therefore, for the natural scalar
addition:

$$
U\cdot(V+W)=U\cdot V+U\cdot W.
$$

For a general descriptor $d$, the inner magnitude of $V+W$ is
$\sqrt{v^2+d(V,W)+w^2}$, which is not $v+w$ unless $d(V,W)=2vw$. In that
case, the inner magnitude of $U\cdot(V+W)$ is
$u\sqrt{v^2+d(V,W)+w^2}$, and the inner magnitude of $U\cdot V+U\cdot W$
depends on $d(UV,UW)$. Equality requires:

$$
d(UV,UW)=U\cdot d(V,W).
$$

Here $U\cdot d(V,W)$ is ordinary scalar scaling of the descriptor by the
visible value $U=u^2$. This is a compatibility condition on the descriptor. It
holds for the angular descriptor $d(V,W)=2vw\cos\Delta$ when the angle
$\Delta$ is preserved under scaling by $U$. It is not automatic and should not
be assumed without verification for a given $d$.

## Integer Powers

For $U=u^2$ and a nonnegative integer $n$, define:

$$
U^n=(u^n)^2.
$$

The inner magnitude of $U^n$ is $u^n$. Since $u\ge0$, $u^n\ge0$ for all
$n\ge0$, so $U^n\in\mathbb U$.

Base cases: $U^0=(u^0)^2=1$ and $U^1=u^2=U$.

**Power law:**

$$
U^n\cdot U^m=(u^n)^2\cdot(u^m)^2=(u^n\cdot u^m)^2=(u^{n+m})^2=U^{n+m}.
$$

**Power of a product:**

$$
(U\cdot V)^n=((uv)^2)^n=((uv)^n)^2=((u^n)(v^n))^2=U^n\cdot V^n.
$$

## Two Exponential Layers

Integer powers being defined, a power series in $U$ is now meaningful:

$$
\sum_{n=0}^{\infty}a_n U^n=\sum_{n=0}^{\infty}a_n(u^n)^2,
$$

provided the series converges. Applied to the standard exponential
coefficients:

$$
e^U=\sum_{n=0}^{\infty}\frac{U^n}{n!}=\sum_{n=0}^{\infty}\frac{u^{2n}}{n!}=e^{u^2}.
$$

This is the value-layer exponential: the standard real exponential evaluated at
the visible value. Its output is an ultrareal.

A second exponential lives at the presentation layer. If the symbol $i$ is
adjoined with $i^2=-1$, the power series may be evaluated at a purely imaginary
argument $i\theta$:

$$
e^{i\theta}=\sum_{n=0}^{\infty}\frac{(i\theta)^n}{n!}.
$$

This series converges absolutely for every real $\theta$. Its value is a
complex number of modulus one. It is not an ultrareal. It is an orientation — a
unit presentation carrying direction without inner magnitude other than one.

The two exponentials belong to different layers:

$$
\begin{aligned}
\text{value layer:}\quad &e^U=e^{u^2},\qquad U\in\mathbb U,\\
\text{presentation layer:}\quad &e^{i\theta}=\cos\theta+i\sin\theta,\qquad\theta\in\mathbb R.
\end{aligned}
$$

The derivation of Euler's formula — that $e^{i\theta}=\cos\theta+i\sin\theta$
— is given in Chapter 004. Multiplication of ultrareals is not required for
that derivation. What is required is multiplication under the power series with
the single rule $i^2=-1$. That rule was introduced as the definition of the
adjoined symbol, not as a consequence of ultrareal arithmetic.
