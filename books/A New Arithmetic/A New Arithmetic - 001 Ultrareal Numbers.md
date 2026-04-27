# Ultrareal Numbers

An ultrareal number is a positive square-form:

$$
U=u^2,\qquad u\ge0.
$$

The number is $U$. Its inner magnitude, or natural inner state, is $u$.

The ultrareal domain is:

$$
\mathbb U=\{u^2\mid u\in\mathbb R_{\ge0}\}=[0,\infty).
$$

The map from inner magnitude to visible value is:

$$
q:\mathbb R_{\ge0}\to\mathbb U,\qquad q(u)=u^2.
$$

Because the inner magnitude is constrained by $u\ge0$, this representation is
unique. For every $U\in\mathbb U$ there is exactly one natural inner state:

$$
u=\sqrt U.
$$

## Value And Inner Magnitude

The notation separates two roles:

$$
\begin{aligned}
\text{visible value:}\quad &U,\\
\text{inner magnitude:}\quad &u.
\end{aligned}
$$

The visible value is the square-value handled by arithmetic. The inner magnitude
is the root through which relation terms are formed.

This separation is the structural move of the book. Ordinary arithmetic normally
works directly with visible values. Ultrareal arithmetic keeps the inner
magnitude available, so a joined value can include terms that depend on how the
parts meet.

## Positivity

Every ultrareal is nonnegative:

$$
U=u^2\ge0.
$$

Its modulus is the value itself:

$$
|U|=U.
$$

It vanishes only at zero:

$$
|U|=0\quad\Longleftrightarrow\quad U=0.
$$

In this square-form sense, the ultrareal layer is positive definite: no member
of $\mathbb U$ is below zero, and only zero has zero modulus.

## Equality

Two ultrareals are equal exactly when their visible square-forms are equal:

$$
U=V
\quad\Longleftrightarrow\quad
u^2=v^2.
$$

Since $u,v\ge0$, this is equivalent to equality of their natural inner states:

$$
U=V
\quad\Longleftrightarrow\quad
u=v.
$$

## Zero

Zero is the ultrareal whose inner magnitude is zero:

$$
0=0^2.
$$

It is the additive identity for ordinary visible addition and for every
relation-aware joining, because any relation term containing its inner magnitude
vanishes.

## No Negative Ultrareals

There are no negative ultrareals.

Let $U$ be a nonzero ultrareal:

$$
U=u^2,\qquad u>0.
$$

For every allowed inner magnitude $r\in\mathbb R_{\ge0}$,

$$
r^2\ge0.
$$

Therefore no allowed inner magnitude can produce $-U$, because $-U<0$ in
ordinary signed notation. The symbol $-U$ may still be useful as ordinary
notation, but it is not a member of $\mathbb U$.

The conclusion is:

$$
\mathbb U=[0,\infty),\qquad
\mathbb U\cap(-\infty,0)=\varnothing.
$$

Signs belong to presentation, comparison, direction, cancellation, or relation.
They do not name negative ultrareal values.

## Oriented Presentations

A lone ultrareal does not require orientation. Its natural inner state is $u$.

In problems where orientation matters, one may introduce an oriented inner
presentation:

$$
z=ue^{i\alpha}.
$$

This is not a new ultrareal value. It is a presentation of the same inner
magnitude with an added orientation parameter. The ultrareal value recovered
from this presentation is:

$$
z\bar z
=(ue^{i\alpha})(ue^{-i\alpha})
=u^2.
$$

Thus self-orientation cancels in a single ultrareal. Relative orientation
matters only when two or more inner states are joined.
