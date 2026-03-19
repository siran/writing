---
title: Recomputing Michelson–Morley from Maxwellian Energy Transport
subtitle: Why the $c\pm v$ Round-Trip Argument Fails and How the Null Result Follows from Source-Free Maxwell
author: An M. Rodriguez, Alex Mercer
date: 2026-01-23
keywords: Michelson–Morley, Maxwell theory, interferometer, energy transport, wave operator invariance, velocity composition, Galilean addition, null result
one-sentence-summary: The Michelson–Morley $c\pm v$ timing argument assumes Galilean velocity addition, which is incompatible with source-free Maxwell transport; enforcing Maxwell-consistent transport forces hyperbolic velocity composition and yields equal arm round-trip times (null fringe shift) without extra geometric postulates.
summary: We derive, step-by-step, the correct kinematics for electromagnetic energy transport directly from source-free Maxwell equations. Maxwell implies a universal wave operator with transport rate $c$. Requiring that inertial coordinate descriptions preserve this wave operator forces the unique linear time–space mixing that yields hyperbolic velocity composition. We then recompute the Michelson–Morley interferometer timing, showing precisely where the naive $c\pm v$ argument assumes Galilean addition and why that assumption contradicts Maxwell transport. With Maxwell-consistent composition, the two arm round-trip times are equal in the ideal symmetric device, so the null result follows from Maxwellian transport itself.
---

# Recomputing Michelson–Morley from Maxwellian Energy Transport

## Motivation

The classic “ether wind” calculation is:

1. The laboratory moves at speed $v$ through a preferred medium.
2. Along the parallel arm, the outbound speed is $c-v$ and the return
   speed is $c+v$.
3. Along the transverse arm, the timing is different (a triangle argument).
4. Therefore, a fringe shift should appear.


Michelson–Morley found (ideally) no shift.

This document isolates the exact logical fault:

The $c\pm v$ calculation assumes Galilean velocity addition for a
process whose transport structure is fixed by source-free Maxwell theory.
Maxwell transport is not algebraic projectile transport; it is divergence-free,
curl-based propagation constrained by a universal wave operator. Under those
constraints, the correct composition is hyperbolic, not additive.

We proceed in three stages:

- derive the Maxwell wave operator and its invariant transport rate
  $c$,
- derive the unique inertial re-description compatible with that operator (and
  hence the velocity composition law),
- compute the Michelson–Morley timing using that Maxwell-consistent kinematics
  and identify the $c\pm v$ step as the incompatible assumption.


## What must be computed

A Michelson interferometer compares two round-trip travel times:

- $T_\parallel$: along an arm aligned with the laboratory’s velocity,
- $T_\perp$: along an arm perpendicular to it.


With equal arm lengths $L$ in the laboratory description, the
measured phase difference is proportional to

$$
\Delta T := T_\parallel - T_\perp.
$$

A nonzero $\Delta T$ yields a fringe shift. A null result corresponds to
$\Delta T=0$ (in the idealized symmetric instrument).


## Stage I: Maxwell fixes the propagation structure

### Source-free Maxwell equations

In vacuum (source-free region),

$$
\nabla\cdot\mathbf{E}=0,\qquad \nabla\cdot\mathbf{B}=0,
$$

$$
\nabla\times\mathbf{E}=-\partial_t\mathbf{B},\qquad
\nabla\times\mathbf{B}=\mu_0\epsilon_0\,\partial_t\mathbf{E}.
$$


### Maxwell implies a universal wave operator

Take curl of Faraday’s law and use the vector identity

$$
\nabla\times(\nabla\times\mathbf{E})=\nabla(\nabla\cdot\mathbf{E})-\nabla^2\mathbf{E}.
$$

Since $\nabla\cdot\mathbf{E}=0$,

$$
-\nabla^2\mathbf{E}=\nabla\times(-\partial_t\mathbf{B})
=-\partial_t(\nabla\times\mathbf{B})
=-\mu_0\epsilon_0\,\partial_t^2\mathbf{E}.
$$

Hence

$$
\partial_t^2\mathbf{E}=c^2\nabla^2\mathbf{E},\qquad
c:=\frac{1}{\sqrt{\mu_0\epsilon_0}}.
$$

Similarly,

$$
\partial_t^2\mathbf{B}=c^2\nabla^2\mathbf{B}.
$$

So field components satisfy the scalar wave operator

$$
\square_c := \partial_t^2 - c^2\nabla^2.
$$

Interpretation (transport-only): Maxwell theory enforces a distinguished causal
transport rate $c$ for electromagnetic disturbances. This is not a
statement about “space itself,” but about the structure of Maxwell propagation.


## Stage II: Maxwell-consistent velocity composition

The $c\pm v$ argument assumes Galilean addition:

$$
u_{\text{total}} = u_{\text{signal}} \pm v.
$$

To test whether this is compatible with Maxwell transport, we derive the
composition law implied by Maxwell invariance.


### Inertial re-description principle (operator form)

Let $(t,\mathbf{x})$ and $(t',\mathbf{x}')$ be inertial coordinate descriptions
(straight uniform motion described as straight uniform motion). The minimal
Maxwell-invariance requirement is:

If a field component $\Phi$ satisfies

$$
(\partial_t^2-c^2\nabla^2)\Phi=0,
$$

then in primed variables it also satisfies

$$
(\partial_{t'}^2-c^2\nabla'^2)\Phi=0.
$$

Equivalently: the wave operator built from $c$ is preserved (up to
a nonzero constant factor), so that “Maxwell propagation with rate
$c$” is not an artifact of one particular inertial description.


### 1D derivation (relative motion along one axis)

Assume relative motion along $x$ and preserve transverse symmetry:

$$
y'=y,\qquad z'=z.
$$

Assume linearity of inertial mappings:

$$
x'=a\,x+b\,t,\qquad t'=d\,x+e\,t,
$$

with constants depending only on relative speed.

Apply the chain rule:

$$
\partial_x = a\,\partial_{x'}+d\,\partial_{t'},\qquad
\partial_t = b\,\partial_{x'}+e\,\partial_{t'}.
$$

Compute

$$
\partial_t^2-c^2\partial_x^2
= (b\partial_{x'}+e\partial_{t'})^2
- c^2(a\partial_{x'}+d\partial_{t'})^2.
$$

To preserve the operator’s form (up to a scalar factor), the mixed term must
vanish:

$$
be-c^2ad=0.
$$

The remaining coefficients must match the primed operator up to the same scalar
factor $\lambda\neq 0$:

$$
e^2-c^2d^2=\lambda,\qquad c^2a^2-b^2=\lambda c^2.
$$

Now identify the relative speed $v$ as the speed of the primed
origin ($x'=0$) as seen in unprimed coordinates:

$$
0=x'=a x+b t \quad\Rightarrow\quad x= -\frac{b}{a}t,
\qquad v := \frac{dx}{dt} = -\frac{b}{a}.
$$

So $b=-av$. From $be=c^2ad$,

$$
(-av)e=c^2ad \quad\Rightarrow\quad d=-\frac{ve}{c^2}.
$$

Substitute into $e^2-c^2d^2=\lambda$:

$$
e^2 - c^2\left(\frac{v^2e^2}{c^4}\right)=\lambda
\quad\Rightarrow\quad
e^2\left(1-\frac{v^2}{c^2}\right)=\lambda.
$$

Similarly from $c^2a^2-b^2=\lambda c^2$ with $b=-av$:

$$
c^2a^2-a^2v^2=\lambda c^2
\quad\Rightarrow\quad
a^2\left(1-\frac{v^2}{c^2}\right)=\lambda.
$$

Thus $a^2=e^2$. Choose the orientation-preserving branch
$a=e$. Fix the scaling by choosing $\lambda=1$ (so the inverse
has the same functional form). Define

$$
\gamma := \frac{1}{\sqrt{1-\frac{v^2}{c^2}}}.
$$

Then

$$
a=e=\gamma,\qquad b=-\gamma v,\qquad d=-\gamma\frac{v}{c^2}.
$$

So the unique Maxwell-invariant inertial transformation is

$$
x'=\gamma(x-vt),\qquad
t'=\gamma\left(t-\frac{v}{c^2}x\right),\qquad
y'=y,\ z'=z.
$$

This is not introduced as “spacetime geometry.” It is forced by invariance of
the Maxwell wave operator.


### Velocity composition (1D)

Let a trajectory have velocity $u=dx/dt$. Differentiate:

$$
dx'=\gamma(dx-v\,dt),\qquad
dt'=\gamma\left(dt-\frac{v}{c^2}dx\right).
$$

Hence the primed velocity is

$$
u' := \frac{dx'}{dt'}
=\frac{dx-v\,dt}{dt-\frac{v}{c^2}dx}
=\frac{u-v}{1-\frac{uv}{c^2}}.
$$

This is the Maxwell-implied composition law. It replaces the Galilean rule.

Immediate corollary (the key identity):

If $u=c$, then

$$
u'=\frac{c-v}{1-\frac{vc}{c^2}}
=\frac{c-v}{1-\frac{v}{c}}
=c.
$$

So Maxwell-consistent bookkeeping does not allow “$c\pm v$” as a
transformed signal speed. That expression is exactly the Galilean assumption.


### Full 3D composition (for completeness)

Let $\mathbf{v}$ be the relative velocity. Decompose any velocity
$\mathbf{u}$ into components parallel and perpendicular to $\mathbf{v}$:

$$
\mathbf{u}_\parallel := (\mathbf{u}\cdot\hat{\mathbf{v}})\hat{\mathbf{v}},
\qquad
\mathbf{u}_\perp := \mathbf{u}-\mathbf{u}_\parallel,
\qquad
\hat{\mathbf{v}}:=\frac{\mathbf{v}}{|\mathbf{v}|}.
$$

Then Maxwell-invariant boosts yield

$$
\mathbf{u}'
=\frac{\mathbf{u}_\perp/\gamma+\mathbf{u}_\parallel-\mathbf{v}}
{1-\frac{\mathbf{v}\cdot\mathbf{u}}{c^2}},
\qquad
\gamma=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}.
$$

Again, Galilean addition is not compatible with Maxwell invariance.


## Stage III: Michelson–Morley timing with Maxwell-consistent transport

We now recompute the interferometer round-trip times using only:

1. the device is symmetric in its own inertial description (arm lengths equal to
   $L$ in that description),
2. source-free Maxwell propagation in that description is governed by the wave
   operator $\square_c$ with transport rate $c$,
3. velocity composition is Maxwell-consistent (hyperbolic), not Galilean.


### The operational content of the interferometer

An interferometer does not measure “one-way speeds” directly. It measures a
relative phase accumulated on two closed optical paths. In ideal vacuum and
ideal optics, the relevant quantity is the round-trip time in the laboratory
description.

The laboratory description is the one in which:

- the beam splitter is at rest,
- the mirrors are at rest at fixed coordinate distances $L$ along
  the two arms.


In that description, the problem is:

Compute the time for a Maxwellian disturbance to go from the beam splitter to a
mirror at distance $L$ and return, along each arm.


### Maxwellian propagation in the laboratory description

By construction of the laboratory description and by Maxwell invariance (Stage
II), vacuum propagation in that inertial description is governed by the same
wave operator $\square_c$ and hence the same transport rate
$c$.

Therefore, in the laboratory description, the outbound travel time to a mirror
at distance $L$ is

$$
T_{\text{out}}=\frac{L}{c},
$$

and the return time is

$$
T_{\text{back}}=\frac{L}{c}.
$$

So for each arm,

$$
T_{\text{arm}} = T_{\text{out}}+T_{\text{back}}=\frac{2L}{c}.
$$

This is true for the parallel arm and the perpendicular arm because in the
laboratory description the mirror positions are fixed at the same distance
$L$ along their respective axes and the propagation law is
isotropic with rate $c$.

Hence

$$
T_\parallel=\frac{2L}{c},\qquad
T_\perp=\frac{2L}{c},
$$

and therefore

$$
\Delta T = T_\parallel - T_\perp = 0.
$$

This is the Michelson–Morley null result.


### Where the $c\pm v$ reasoning fails (exactly)

The $c\pm v$ derivation assumes that there exists a preferred frame in
which light propagates at $c$ and that, relative to a moving
laboratory, the light’s speed becomes $c\pm v$ along the arm due to
Galilean addition.

But Stage II shows that if Maxwell propagation has wave operator
$\square_c$ in one inertial description and you require it to retain the
same operator form in another inertial description, then the correct
transformation is Maxwell-hyperbolic and forces the identity

$$
c \mapsto c,
$$

not $c\pm v$.

Thus the $c\pm v$ step is not a “reasonable approximation.” It is an
incompatible kinematic premise: it assumes algebraic addition for a process
whose kinematics are fixed by Maxwell operator invariance.


## What Michelson–Morley actually tested (in this transport-first framing)

The interferometer tests whether electromagnetic propagation behaves as a
Galilean projectile in a moving apparatus description.

Source-free Maxwell propagation does not have that kinematics: its inertial
re-description is fixed by wave-operator invariance, and the corresponding
velocity composition is hyperbolic, preserving the transport rate
$c$.

In that sense, the null result is a direct confirmation of Maxwell-consistent
transport bookkeeping. It does not logically force a separate postulate of
“length contraction” as an independent axiom.


## Closing statement

The Michelson–Morley $c\pm v$ argument fails at a single, identifiable
point: the insertion of Galilean velocity addition for Maxwellian energy
transport.

Source-free Maxwell theory implies a wave operator with propagation rate
$c$ and, by requiring inertial form-invariance of that operator,
forces hyperbolic velocity composition. With that Maxwell-consistent kinematics,
the interferometer’s two round-trip times are equal in the ideal symmetric
device:

$$
T_\parallel=T_\perp=\frac{2L}{c},
\qquad
\Delta T=0.
$$

The null result follows from Maxwell transport itself.
