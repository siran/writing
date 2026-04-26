# Preface: Ultrareal Numbers

So the first claim of this book is simple:

$$
1 + 1 \text{ is not necessarily only } 2.
$$

There is also an interaction term.

This book describes ultrareal numbers: numbers that are never negative.

More specifically, an ultrareal number is a positive square-form:

$$
U = u^2
$$

The capital $U$ names the visible value. The lower-case $u$ names the inner value.

## What is a number?

A number is not a concrete thing. It took humans a long time to abstract the
concept; some counting systems still distinguish only a few quantities before
reaching "many." Concepts such as color also evolved constructively through
language. Here the concern is numbers and what they are under this new
arithmetic.

Being not something concrete, a number can be understood as a numerical
*density*: when projected onto whatever we are referencing, the density becomes
realized in an instance.

The analogy comes straight from physics and the concept of electromagnetic
energy. In physics, when describing waves, energy is proportional to the square
of the amplitude. In ultrareal language, energy is the outer value, and
amplitude is the inner value:

$$
E = a^2
$$

When adding two waves, the amplitudes add first, as inner values in the
ultrareals. Two waves of amplitudes $a_1$ and $a_2$ have energy:

$$
E=(a_1+a_2)^2
$$

In this sense, Numbers as we know them are densities. They are visible positive
values carried by actual instances. In ultrareal notation, a Number appears as:

$$
N = n^2
$$

The capital $N$ is the visible number, or observable: the instantiation of the
idea of a number into something concrete. The lower-case $n$ is its inner value.

The word *real* matters: ultrareals are only positive. What standard arithmetic
calls "negative" becomes a rotation, using Euler's identity.

The word *ultra* matters too. Ultrareals are not merely the usual real numbers
renamed. They keep track of something standard arithmetic does not represent:
the relation between numbers being added. So they are *more than* real, hence
*ultra*.

Also, *ultra* points beyond the usual negative extension of the number line. In
reality there are no negative things. There is no such thing as a negative apple
that gets added to a dozen after you eat one:

$$
12 + (-1) = 11
$$

The symbol $-1$, as in $-1 < 0$, does not map to the ultrareals.

Standard arithmetic studies numbers as non-interacting. In that model, addition
behaves like the mathematical union of sets: the parts are placed together, and
the relation term is not part of the calculation. Ultrareal arithmetic treats
that as the special case:

$$
d(U,V) = 0
$$

Once relation is part of the arithmetic data, the operator $+$ is overloaded.
It is defined on the visible ultrareals, their inner values, and their
interaction descriptor:

$$
U = u^2,\qquad
V = v^2,\qquad
U + V = u^2 + v^2 + 2d(U,V)uv.
$$

with:

$$
-1 \le d(U,V) \le 1
$$

This descriptor is continuous. It works like alignment in fields: the values
between $-1$ and $1$ are partial alignments, not separate kinds of addition.

The important endpoint and midpoint cases are:

$$
\begin{aligned}
d(U,V) &= 1 &&\text{aligned joining},\\
d(U,V) &= 0 &&\text{non-interaction},\\
d(U,V) &=-1 &&\text{opposition}.
\end{aligned}
$$

So:

$$
\begin{aligned}
\text{aligned:}\quad &U + V = (u + v)^2,\\
\text{standard:}\quad &U + V = u^2 + v^2,\\
\text{opposed:}\quad &U + V = (u - v)^2.
\end{aligned}
$$

The aligned case shows the interaction term directly:

$$
(u + v)^2 = u^2 + v^2 + 2uv
$$

In this sense, addition makes the parts whole through interaction.

The same distinction clarifies negative numbers. There are no negative
ultrareals. A negative value is a rotated square-value:

$$
-U = (iu)^2,
\qquad
i^2 = -1.
$$

The sign records rotation, opposition, cancellation, or comparison. It does not
name a negative object in the ultrareal layer.

The opening claim can now be stated by cases:

$$
\begin{aligned}
d(1,1) &= 0 &&\text{gives } 1 + 1 = 2,\\
d(1,1) &= 1 &&\text{gives } 1 + 1 = 4,\\
d(1,1) &=-1 &&\text{gives } 1 + 1 = 0.
\end{aligned}
$$

When the parts interact, the whole includes the interaction term.
