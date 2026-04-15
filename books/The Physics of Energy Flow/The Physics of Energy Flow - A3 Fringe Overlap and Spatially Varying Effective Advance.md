---
title: The Physics of Energy Flow - Appendix A3
date: 2026-04-14
kind: appendix
part: Appendices
summary: >
  Two equal coherent beams overlapping at a small angle produce a fringe
  density profile ranging from 0 to 4u relative to one beam, while the period
  average remains 2u. The forward flux budget is worked out explicitly. Under
  the loaded-branch law of Chapter 7b, this yields a candidate spatial profile
  for c_eff on the surviving bright parts of the fringe. The appendix states
  the exact measurement condition needed to turn that profile into an
  operational prediction.
keywords:
  - fringe overlap
  - effective advance
  - self-refraction
  - interference
  - spatial redistribution
---


# Appendix A3. Fringe Overlap and Spatially Varying Effective Advance

Chapter 7b derives an effective advance

$$
c_{\mathrm{eff}} = \frac{J}{u}
$$

for a loaded branch: the carried flux $J$ is preserved while the recovered
density $u$ rises.

This appendix works out the simplest spatial overlap geometry in which that
claim can be tested. The goal is to separate three statements cleanly:

1. what the density profile of a coherent fringe is,
2. what the forward flux budget is,
3. under what extra condition a spatially varying $c_{\mathrm{eff}}$ becomes
   an operational prediction.


## A3.1 Two Equal Beams Crossing Symmetrically

Let two equal monochromatic contributions cross symmetrically about the
$z$-axis with half-angle $\theta$:

$$
f_1(x,z,t)
=
A\,e^{\,i(kx\sin\theta + kz\cos\theta - \omega t)},
$$

$$
f_2(x,z,t)
=
A\,e^{\,i(-kx\sin\theta + kz\cos\theta - \omega t)}.
$$

Define

$$
u_0 := |A|^2,
\qquad
q := 2k\sin\theta.
$$

Then the summed field is

$$
f_{\mathrm{tot}}(x,z,t)
=
f_1 + f_2
=
2A\cos\!\left(\frac{qx}{2}\right)
e^{\,i(kz\cos\theta - \omega t)}.
$$

So the recovered density is

$$
u(x)
=
|f_{\mathrm{tot}}(x,z,t)|^2
=
4u_0\cos^2\!\left(\frac{qx}{2}\right).
$$

This gives the exact fringe range:

$$
0 \le u(x) \le 4u_0.
$$

The bright-fringe maxima occur at

$$
\frac{qx}{2} = n\pi,
$$

and the nodes occur at

$$
\frac{qx}{2} = \frac{(2n+1)\pi}{2}.
$$

The fringe period is

$$
\Lambda = \frac{2\pi}{q} = \frac{\lambda}{2\sin\theta}.
$$


## A3.2 Mean Density Budget

Over one fringe period,

$$
\langle u \rangle
:=
\frac{1}{\Lambda}\int_0^\Lambda u(x)\,dx
=
\frac{1}{\Lambda}\int_0^\Lambda
4u_0\cos^2\!\left(\frac{qx}{2}\right)\,dx
=
2u_0.
$$

So the density budget is exact:

- each incoming beam contributes mean density $u_0$,
- the overlapping pattern has mean density $2u_0$,
- local bright fringes are denser than the mean,
- local dark fringes are less dense than the mean,
- the full period average recovers the two-beam budget.

This is the clean spatial version of the Chapter 7b statement that coherent
overlap redistributes the same content into denser and sparser regions without
primitive sinks or sources.


## A3.3 Forward Flux Budget

Let each beam carry flux magnitude

$$
J_0 = u_0 c
$$

along its own direction.

Its forward projection on the $z$-axis is therefore

$$
J_{0,z} = J_0\cos\theta = u_0 c\cos\theta.
$$

For the two equal beams together, the total forward incoming flux density is

$$
J_{z,\mathrm{in}} = 2u_0 c\cos\theta.
$$

Dividing by the mean fringe density gives

$$
\frac{J_{z,\mathrm{in}}}{\langle u \rangle}
=
\frac{2u_0 c\cos\theta}{2u_0}
=
c\cos\theta.
$$

So on the full fringe average, the overlap advances forward at the geometric
projection of the original beam directions.

Nothing slower has yet been proved. Up to this point one has only shown:

- exact density redistribution,
- exact recovery of the two-beam mean budget,
- exact forward flux projection.


## A3.4 Candidate Local Effective Advance

Chapter 7b adds one more statement: if a surviving branch carries a fixed
carried flux while its recovered density rises, then its effective advance
drops according to

$$
c_{\mathrm{eff}} = \frac{J}{u}.
$$

Applying that branch law to the forward direction of the fringe profile gives
the candidate local summary

$$
c_{\mathrm{eff}}(x)
:=
\frac{J_{z,\mathrm{in}}}{u(x)}
=
\frac{2u_0 c\cos\theta}{4u_0\cos^2(qx/2)}
=
\frac{c\cos\theta}{2\cos^2(qx/2)}.
$$

At the center of a bright fringe,

$$
qx = 2n\pi,
$$

so

$$
c_{\mathrm{eff,peak}}
=
\frac{c\cos\theta}{2}.
$$

This is the direct spatial analogue of the Chapter 7b constructive
recombination result: the local bright region carries the same two-beam forward
flux, but at twice the mean density and four times the single-beam density.

At a node,

$$
u(x)=0,
$$

so the quotient above ceases to be meaningful as a branch speed. The forward
branch does not survive there. The node is therefore not assigned an infinite
speed; it is simply not a surviving forward branch.

The local formula is meaningful only on open bright intervals between nodes.


## A3.5 What Is and Is Not Predicted

This appendix proves the following:

- the raw coherent fringe has an exact density profile from $0$ to $4u_0$,
- the fringe-period mean density is exactly $2u_0$,
- the total forward flux projection is exactly $2u_0 c\cos\theta$,
- if the Chapter 7b loaded-branch law is applied locally to the surviving
  bright parts of the fringe, the bright-fringe center carries the candidate
  effective advance
  $$
  c_{\mathrm{eff,peak}} = \frac{c\cos\theta}{2}.
  $$

It does *not* by itself prove that an unconstrained free-space fringe will
already yield that value in an ordinary time-of-flight measurement.

The reason is simple: a free fringe is a spatially extended redistribution
pattern. Near the nodes, the forward branch disappears, and lateral
redistribution remains part of the full transport geometry.

So a direct measurement of spatially varying $c_{\mathrm{eff}}$ requires an
extra operational condition.


## A3.6 Measurement Condition

To measure a difference in effective advance along the forward distance of a
fringe, the experiment must do more than simply create the interference
pattern. It must also isolate a surviving bright stripe as a propagating
channel over a finite forward distance.

The minimum conditions are:

1. two equal coherent beams produce a stable fringe pattern,
2. a narrow bright region is selected around a fringe center,
3. that selected region propagates forward over distance $L$ with negligible
   mixing with neighboring fringes,
4. a modulation or pulse delay is measured against a reference.

Under those conditions, the Chapter 7b branch law predicts a larger delay for
the denser bright channel than for the two-beam mean pattern.

If the selected bright stripe remains centered at a fringe maximum, the vacuum
prediction is

$$
v_{\mathrm{peak}} = \frac{c\cos\theta}{2},
\qquad
t_{\mathrm{peak}} = \frac{2L}{c\cos\theta}.
$$

If that same loaded stripe then enters a medium of ordinary refractive index
$n$, and if the medium lag multiplies the branch lag, the propagated speed is

$$
v_{\mathrm{peak,med}} = \frac{c\cos\theta}{2n},
\qquad
t_{\mathrm{peak,med}} = \frac{2nL}{c\cos\theta}.
$$

These are not generic interference formulas. They are the direct experimental
predictions of the loaded-branch reading of Chapter 7b.


## A3.6a Longitudinal Bright-Stripe Measurement

The cleanest measurement is therefore longitudinal rather than transverse.

Choose a bright-fringe center

$$
x_n = \frac{2n\pi}{q},
$$

place a narrow spatial filter around that ridge, and let only that bright
stripe propagate forward.

If the stripe remains centered on the same bright ridge over a forward path
length $L$, then the measured delay is the delay of one surviving loaded
channel, not merely the static readout of a screen pattern.

The experimental comparison is then:

1. one reference beam with the same carrier and modulation,
2. one isolated bright stripe taken from the coherent overlap region,
3. equal downstream path length $L$ for both channels,
4. phase or pulse-delay comparison at the outputs.

If the Chapter 7b branch law is correct, the bright-stripe channel must arrive
later than the reference channel.

In vacuum, the reference time is

$$
t_{\mathrm{ref}} = \frac{L}{c},
$$

while the bright-stripe prediction at a fringe center is

$$
t_{\mathrm{peak}} = \frac{2L}{c\cos\theta}.
$$

In a medium of ordinary refractive index $n$, the corresponding comparison is

$$
t_{\mathrm{ref,med}} = \frac{nL}{c},
\qquad
t_{\mathrm{peak,med}} = \frac{2nL}{c\cos\theta}.
$$

For nearly collinear beams,

$$
\cos\theta \approx 1,
$$

so the predicted medium speed approaches

$$
v_{\mathrm{peak,med}} \approx \frac{c}{2n}.
$$

That is the direct operational form of the earlier water-tube intuition: once a
bright fringe is isolated and propagated as a channel, the test is no longer
"does a screen show fringes?" but rather "does the denser channel acquire the
larger forward delay predicted by the loaded-branch law?"


## A3.7 Relation to a Misaligned Mach-Zehnder

A slightly misaligned Mach-Zehnder is a practical way to realize the same
transverse phase variation in a controlled apparatus.

If the two fields reaching the final recombiner have equal magnitude and phase
difference

$$
\Delta\phi(x)=qx+\phi_0,
$$

then the normalized output modes are

$$
f_\pm(x)=\frac{f_1(x)\pm f_2(x)}{\sqrt2},
$$

with

$$
u_{\mathrm{arm}} := |f_1|^2 = |f_2|^2,
$$

with densities

$$
u_\pm(x)=u_{\mathrm{arm}}\bigl(1\pm\cos\Delta\phi(x)\bigr)
$$

that is,

$$
u_+(x)=2u_{\mathrm{arm}}\cos^2\!\frac{\Delta\phi(x)}{2},
\qquad
u_-(x)=2u_{\mathrm{arm}}\sin^2\!\frac{\Delta\phi(x)}{2}.
$$

Therefore

$$
u_+(x)+u_-(x)=2u_{\mathrm{arm}}
$$

pointwise.

So the misaligned Mach-Zehnder gives the complementary two-output version of
the same redistribution picture: where one output is bright, the other is dark,
and together they recover the full incoming budget.

The direct $0$ to $4u_0$ profile of Sections A3.1-A3.4 is the raw overlap
picture before that normalized two-output projection is imposed.
