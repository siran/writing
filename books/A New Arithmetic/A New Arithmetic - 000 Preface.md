# Preface: Ultrareal Numbers

So the first claim of this book is simple:

$$
1 + 1 \text{ is not necessarily only } 2.
$$

There is also an interaction term.

Far from claiming a finished new mathematics, this book claims a new way of
seeing numbers, and therefore a new arithmetic. Here we describe what we call
*ultrareal numbers*: numbers that are never negative.

More specifically, an ultrareal number $U$ has an "inner state"
$u$ whose visible value is written

$$
U = u^2
$$

An ultrareal number can then be more formally thought of as a positive
square-form.

The capital $U$ names the "visible value" or "observable value",
while the lower-case $u$ names the "inner state".

It is a state rather than merely a value because it can carry orientation,
phase, opposition, or other relation data before the visible value is evaluated.


## What is a number?

A number is not a concrete thing. It took humans a long time to abstract the
concept. Some languages still show that the abstraction is constructed rather
than automatic. The Piraha of the Brazilian Amazon have been described as using
*hoi* with falling tone, *hoi* with rising tone, and *aibaagi* or *baagi* for
roughly "one," "two," and "many," though later work argues these are relative
quantity words rather than exact numerals. The Munduruku, also in the Brazilian
Amazon, give another example: published numeral lists give *peng* for "one,"
*shepshep* for "two," and *ebapeng* for "three," while experimental work reports
that larger quantities move toward approximate expressions such as "some, not
many" and "many." Concepts such as color also evolved constructively through
language. Here the concern is numbers and what they are under this new
arithmetic.

Being not something concrete, a number can be understood as a numerical
*density* that when projected onto whatever we are referencing, the density
becomes realized in an instance.

The analogy comes straight from physics and the concept of electromagnetic
energy. In physics, when describing waves, energy is proportional to the square
of the amplitude. In ultrareal language, energy is the outer value, and
amplitude is the inner state:

$$
E = a^2
$$

When adding two waves, the amplitudes add first, as inner states in the
ultrareals. Two waves of amplitudes $a_1$ and $a_2$ have
energy:

$$
E=(a_1+a_2)^2
$$

This is the physical motivation for ultrareals. Energy-like quantities are
positive densities. If opposition is carried by phase, turn, or relation, then
the magnitude itself can remain in the positive real subset.

In this sense, numbers as we know them are densities. They are visible positive
values carried by actual instances. In ultrareal notation, a number appears as:

$$
N = n^2
$$

The capital $N$ is the visible number, or observable: the
instantiation of the idea of a number into something concrete. The lower-case
$n$ is its inner state.

The word *real* matters: ultrareals are only positive. What standard arithmetic
calls "negative" becomes a rotation, using Euler's identity.

The word *ultra* matters too. Ultrareals are not merely the usual real positive
numbers renamed. They keep track of something standard arithmetic does not
represent: the relation between numbers being added. So they are *more than*
real, hence *ultra*.

Also, *ultra* points beyond the usual negative extension of the number line. In
reality there are no negative things. There is no such thing as a negative apple
that gets added to a dozen after you eat one:

$$
12 + (-1) = 11
$$

The symbol $-1$, as in $-1 < 0$, does not map to the
ultrareals.

Standard arithmetic studies numbers as non-interacting. In that model, addition
behaves like the mathematical union of sets: the parts are placed together, and
the relation term is not part of the calculation. To describe the interaction
between numbers, introduce a descriptor $d(\cdot,\cdot)$ so that $d(U,V)=0$
recovers the usual non-interacting arithmetic,

$$
d(U,V) = 0
$$

Once relation is part of the arithmetic data, the operator $+$ is
overloaded. It is defined on the visible ultrareals, their inner states, and
their interaction descriptor:

$$
U = u^2,\qquad
V = v^2,\qquad
U + V = u^2 + v^2 + 2d(U,V)uv.
$$

When $d(U,V)=1$, this is just the binomial square identity:

$$
(u+v)^2 = u^2+v^2+2uv.
$$

The novelty is not the algebraic identity. The novelty is making explicit that
a handled number can be written as $N=n^2$, so the cross term becomes available
as relation data instead of being hidden by ordinary inventory arithmetic.

For ordinary angular alignment, the descriptor satisfies:

$$
-1 \le d(U,V) \le 1
$$

The descriptor is not a negative ultrareal. It is relation data. It can express
a degree of alignment, a degree of opposition, or another relation between the
inner states. At the endpoints, $d(U,V)=1$ means aligned and $d(U,V)=-1$ means
rotated into opposition. The descriptor can also encode hyperbolic, tangential,
weighted, or otherwise non-angular relations when those are the relations at
work.

For vector-like or phase-like quantities, it is often useful to write an angular
representation:

$$
d(U,V)=\cos\phi.
$$

The angle form is useful when the quantities carry orientation. It is not a
requirement on ultrareal quantities.

In this sense, addition in the ultrareals makes the parts whole through
interaction.

## No Negative Ultrareals

**There are no negative ultrareals.** There are opposing positive ultrareals:
two positive square-forms can meet through aligned or opposed inner states.
Opposition belongs to relation, orientation, or joining; it does not make the
positive square-form negative.

For a single ultrareal, the precise modulus statement is that it is
nonnegative, and positive except at zero:

$$
|U|=U=u^2\ge0,
\qquad
|U|=0 \Longleftrightarrow U=0.
$$

Because the form is a square, it is also natural to call the ultrareal layer
positive-definite in the square-form sense.

## Rotations and Phases of Number Densities

A minus-signed value is different from an opposing ultrareal. It is a rotated
square-value:

$$
-U = (iu)^2,
\qquad
i^2 = -1.
$$

The sign records a turn. In the complex-analytic toolset of standard calculus,
developed from Euler's notation, multiplication by $i$ is a quarter-turn of the
inner state, and squaring returns that turn as a half-turn in the visible value.
This uses the notation, mathematics, and operational calculus of standard
complex analysis. Ultrareals extend that calculus because the square-form is the
same.

If a relation is written in Euler form as $e^{i\phi}$, the $i\phi$ records the
turn of the inner state. The visible coefficient may be the projected descriptor
$d(U,V)=\cos\phi$, but the ultrareal magnitude remains positive.

The sign does not name an object in the ultrareal layer, nor remove the value
from numerical existence.

When the parts interact, the whole includes the interaction term.
