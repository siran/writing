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
same wave transport? The answer is forced by one simple invariant: if two
observers describe the same propagated pattern between the same shared events,
they must agree on how many wavelengths have passed.


## Isolated observers

Define an **isolated observer** as one describing a region in which the net
flux of $\mathbf{F}/c^2$ through any large closed surface vanishes. This is
the flow-language statement that no external transport organizes the region.

Two isolated observers in relative uniform motion, both describing the same
transport process, must be able to write the same source-free wave equation
with the same constant $c$. This is not a separate geometric postulate. It is
the statement that they describe one transport law rather than two different
unit rescalings. When the relative rate is $v=0$, the change of description
must reduce to the identity, so the transport constant must also agree:
$c_1=c_2=:c$.


## Shared phase count

In one spatial dimension, a right-moving monochromatic component has the form

$$
f(x,t)=A\cos(kx-\omega t),
\qquad
\omega = ck,
\qquad
\lambda = \frac{2\pi}{k}.
$$

Fix one crest at the shared origin event $(x,t)=(0,0)$. Between that event and
any later event $(x,t)$, the number of wavelengths transported is

$$
N_+ = \frac{kx-\omega t}{2\pi}
=
\frac{x-ct}{\lambda}.
$$

For the same right-moving component, the second observer writes

$$
N_+' = \frac{x'-ct'}{\lambda'}.
$$

Because it is the same transported pattern between the same shared events,

$$
N_+'=N_+.
$$

The wavelengths $\lambda$ and $\lambda'$ may differ, since different observers
can assign different Doppler-shifted wavelengths. Therefore the invariant count
implies not equality of the null coordinates themselves, but proportionality:

$$
x'-ct' = \alpha(v)\,(x-ct),
$$

where $\alpha(v)=\lambda'/\lambda$ depends only on the relative rate $v$.

The same argument for a left-moving monochromatic component gives

$$
x'+ct' = \beta(v)\,(x+ct).
$$

So the two null directions can scale differently, but the wavelength count
along each must be preserved.


## The unique re-description

Add and subtract the two null-coordinate relations:

$$
x' = \frac{\alpha+\beta}{2}\,x + \frac{c(\beta-\alpha)}{2}\,t,
$$

$$
t' = \frac{\beta-\alpha}{2c}\,x + \frac{\alpha+\beta}{2}\,t.
$$

So the change of description is already linear. The primed origin $x'=0$
therefore moves in the unprimed description at rate

$$
v = \frac{x}{t}
=
c\,\frac{\alpha-\beta}{\alpha+\beta}.
$$

Now use two symmetry requirements.

First, reversing the spatial direction exchanges right-moving and left-moving
transport, so

$$
\beta(v)=\alpha(-v).
$$

Second, the inverse transformation must have the same form with $v\mapsto -v$.
Applying the transformation and its inverse in succession must return the same
null coordinate, so

$$
\alpha(v)\alpha(-v)=1.
$$

Together these give

$$
\alpha(v)\beta(v)=1.
$$

Let $\beta=1/\alpha$. Then

$$
\frac{v}{c}
=
\frac{\alpha-\alpha^{-1}}{\alpha+\alpha^{-1}}
=
\frac{\alpha^2-1}{\alpha^2+1}.
$$

So

$$
\alpha^2 = \frac{1+v/c}{1-v/c},
\qquad
\beta^2 = \frac{1-v/c}{1+v/c}.
$$

Choose the orientation-preserving branch,

$$
\alpha = \sqrt{\frac{1+v/c}{1-v/c}},
\qquad
\beta = \sqrt{\frac{1-v/c}{1+v/c}}.
$$

Substituting into the linear form and writing

$$
\gamma := \frac{1}{\sqrt{1-v^2/c^2}},
$$

gives

$$
x' = \gamma(x-vt),
\qquad
t' = \gamma\!\left(t-\frac{v}{c^2}x\right),
\qquad
y' = y,
\quad
z' = z.
$$

This is the unique change-of-description consistent with preserving wavelength
count for both right-moving and left-moving Maxwell transport.
Because $x' \mp ct'$ are only rescaled copies of $x \mp ct$, the source-free
wave equation is preserved as well: the phase-count derivation and the
wave-operator derivation are the same statement written in two forms.


## Composed transport rate

Let a transport feature move at rate $u=dx/dt$ in the first description.
Differentiating the transformation gives

$$
u'
=
\frac{dx'}{dt'}
=
\frac{u-v}{1-\dfrac{uv}{c^2}}.
$$

This is the unique composition law consistent with the same transport process
being described by both observers.

In particular, if $u=c$,

$$
u' = \frac{c-v}{1-v/c}=c.
$$

So every isolated observer assigns the same rate $c$ to a propagating
wavefront.


## Michelson-Morley

The 1887 experiment compared round-trip travel times along two perpendicular
arms of equal rest length $L$. The classical $c\pm v$ prediction inserts
Galilean addition into the transport step. That step is not available here.

In the apparatus description, the transport law is the same in both directions,
and the propagation rate is $c$ along each arm. So both round-trip times are

$$
T = \frac{2L}{c},
\qquad
\Delta T := T_\parallel - T_\perp = 0.
$$

The null result is therefore not surprising. It is the direct consequence of
requiring two observers to preserve the same transported wavelength count of the
same source-free Maxwell process.
