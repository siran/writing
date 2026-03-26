---
title: The Physics of Energy Flow - Two Observers, One Transport
date: 2026-03-19
---


# 13. Two Observers, One Transport

Chapter 7 established that source-free energy flow satisfies the wave equation

$$
\partial_t^2 \mathbf{F} - c^2 \nabla^2 \mathbf{F} = 0,
\qquad
\nabla\cdot\mathbf{F} = 0.
$$

The same transport process can be described by different observers in relative
motion. This chapter asks: what change-of-description is consistent with that
same wave equation? The answer forces a particular kinematics — not as a
postulate, but as an algebraic consequence of preserving the transport law.


## Isolated observers

Define an **isolated observer** as one describing a region in which the net
flux of $\mathbf{F}/c^2$ through any large closed surface vanishes. This is
the flow-language statement that no external transport organizes the region.

Two isolated observers in relative uniform motion, both describing the same
transport process, must be able to write the same wave operator with the same
constant $c$. This is the only requirement imposed. It is not a statement about
geometry or space. It is the statement that two descriptions of the same
transport process agree on the transport law.

The equality of that constant is not a second postulate. It is the normalization
implicit in saying that the observers describe the same law rather than two
different rescalings of units. If one wrote $c_1$ and $c_2$ instead, the linear
invariance algebra would determine only their ratio as part of the relative
normalization of space and time. Requiring that the change of description reduce
to the identity when the relative rate is $v=0$ removes that ambiguity: at
$v=0$ the map must be $x'=x$, $t'=t$, so the two operator constants must agree,
$c_1=c_2=:c$.


## The transport bound

For propagating solutions of the wave equation — organized wavefronts moving
at rate $c$ — energy density and energy flux satisfy

$$
|\mathbf{F}| = c\,u.
$$

For general configurations (superpositions of modes propagating in different
directions), the net flux is bounded:

$$
|\mathbf{F}| \leq c\,u.
$$

Define the operational transport rate by

$$
\mathbf{v} := \frac{\mathbf{F}}{u}
\qquad (u > 0).
$$

Then $|\mathbf{v}| \leq c$. This bound is not postulated. It is an identity
consequence of the wave-equation structure established in Chapter 7.


## Galilean addition violates the bound

Galilean composition assigns

$$
u \oplus_G v = u + v.
$$

For any $0 < u < c$ and $0 < v < c$ with $u + v > c$ — always achievable —
Galilean composition gives $u \oplus_G v > c$, violating the bound above.

Therefore: **Galilean addition is incompatible with source-free Maxwell
transport.** This is a theorem. It follows from the existence of the bound
and the requirement that a change-of-description preserve it.

We now derive the unique linear re-description that does preserve that same
transport law.


## The wave operator forces the unique re-description

Let two isolated observers be in relative uniform translation at rate $v$
along the $x$-axis. Assume the change-of-description is differentiable.
Homogeneity of space and time means its Jacobian cannot depend on $x$ or $t$:
otherwise the same local transport experiment, shifted to a different location
or time, would transform by a different law. A differentiable map with constant
Jacobian is affine. Choosing the origins to coincide at one event removes the
additive constants, so the map is linear. Uniform relative translation along
the $x$-axis and transverse symmetry then leave only $x$-$t$ mixing:
$y' = y$, $z' = z$. Write the most general linear form:

$$
x' = a x + b t,
\qquad
t' = d x + e t.
$$

Derivatives transform by the chain rule:

$$
\partial_x = a\,\partial_{x'} + d\,\partial_{t'},
\qquad
\partial_t = b\,\partial_{x'} + e\,\partial_{t'}.
$$

Impose wave-operator invariance in 1+1 dimensions:

$$
\partial_t^2 - c^2 \partial_x^2
=
\lambda\!\left(\partial_{t'}^2 - c^2 \partial_{x'}^2\right),
\qquad \lambda \neq 0.
$$

Expanding the left side and collecting by differential operator:

- Cross-term must vanish: $be = c^2 a d$.
- Coefficient of $\partial_{t'}^2$: $e^2 - c^2 d^2 = \lambda$.
- Coefficient of $\partial_{x'}^2$: $b^2 - c^2 a^2 = -\lambda c^2$.

The primed origin $x' = 0$ satisfies $ax + bt = 0$, so the relative rate is
$v = -b/a$, giving $b = -av$. From the cross-term condition: $d = -ve/c^2$.
Substituting into the coefficient equations:

$$
e^2\!\left(1 - \frac{v^2}{c^2}\right) = \lambda,
\qquad
a^2\!\left(1 - \frac{v^2}{c^2}\right) = \lambda.
$$

So $a^2 = e^2$. Choosing the orientation-preserving branch and $\lambda = 1$
so that the inverse transformation takes the same form:

$$
a = e = \gamma
:= \frac{1}{\sqrt{1 - v^2/c^2}},
\qquad
b = -\gamma v,
\qquad
d = -\frac{\gamma v}{c^2}.
$$

The unique linear change-of-description consistent with Maxwell transport is
therefore

$$
x' = \gamma(x - vt),
\qquad
t' = \gamma\!\left(t - \frac{v}{c^2}\,x\right),
\qquad
y' = y,
\quad
z' = z.
$$

This is not assumed. It is the only linear map that preserves the wave
operator. Note that $\gamma$ requires $|v| < c$: a relative translation rate
at or above $c$ would prevent any wavefront emitted by one observer from
reaching the other — no closed measurement is possible.


## Composed transport rate

Let a transport feature move at rate $u = dx/dt$ in the first description.
Differentiating the transformation gives

$$
u'
= \frac{dx'}{dt'}
= \frac{u - v}{1 - \dfrac{uv}{c^2}}.
$$

This is the unique composition law consistent with Maxwell transport. It is
not postulated; it is a corollary of the operator invariance above.

In particular, if $u = c$:

$$
u' = \frac{c - v}{1 - v/c} = c.
$$

The transport bound is absolute: every isolated observer assigns the same rate
$c$ to a propagating wavefront. No composition of rates below $c$ reaches or
exceeds $c$.


## Michelson–Morley

The 1887 experiment compared round-trip travel times along two perpendicular
arms of equal rest length $L$. The classic analysis assumed Galilean
composition: outbound rate $c - v$ and return rate $c + v$ along the arm
aligned with the laboratory's motion, producing unequal arm times and a
predicted fringe shift.

That step is not available here. The composition law derived above gives the
transport rate as $c$ in all directions in the apparatus description — the one
in which the wave operator holds with that same constant. Both arms give

$$
T = \frac{2L}{c},
\qquad
\Delta T := T_\parallel - T_\perp = 0.
$$

The null result is not a surprise requiring additional hypotheses. It is the
only answer consistent with Maxwell transport. The $c \pm v$ argument inserts
Galilean addition at exactly one step; that step contradicts the operator
invariance derived in this chapter. The null result closes the argument.
