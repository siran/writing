---
title: Project Note - Longitudinal Delay of an Isolated Interference Fringe
date: 2026-04-16
---

# Project Note

## Title

Longitudinal Delay of an Isolated Bright Interference Fringe


## Motivation

After two coherent beams are made to interfere, most naturally after a first
beam splitter in a Mach-Zehnder interferometer and with a small relative angle
at recombination, fringes appear on both output branches of the final beam
splitter. A bright fringe on one output corresponds to a dark fringe on the
other, as in the complementary cosine-squared and sine-squared decomposition.
The two outputs together recover the full input power.

At the raw overlap level, two equal coherent contributions can produce local
energy loading from 0 up to 4 times the loading of one contribution. The
measurement proposed here targets the central part of one bright fringe ridge
and compares its longitudinal delay against either of the two incident beams at
the final recombiner.


## Basic Idea

Two equal coherent beams are recombined at a small angle so that stable
straight fringes are formed. A narrow bright fringe ridge is then spatially
filtered and allowed to propagate forward as an isolated channel. Its
modulation or pulse delay is compared against one of the incident beams before
recombination, with matched carrier, modulation, and downstream path length.

The goal is not to measure fringe visibility. The goal is to measure the
forward propagation delay of one bright fringe channel.


## Hypothesis

For two equal coherent amplitudes, the local loading follows the square of
their sum. This gives a fringe density profile with bright ridges that are more
densely loaded than either incident beam alone.

Under the working hypothesis behind this project, the bright fringe ridge is
treated as a surviving loaded channel. If the same forward flux budget is
recovered on that denser ridge, then the effective forward advance of that
ridge should be reduced relative to one incident beam.

So the experimental question is:

- standard expectation: the isolated bright ridge shows the usual propagation
  delay for the chosen medium,
- loaded-branch hypothesis: the isolated bright ridge shows an additional
  forward delay relative to one incident beam.


## Mathematical Model

Let the two equal beams arriving at the final recombination region be written
as

$$
f_1(x,z,t)=A\,e^{i(kz-\omega t)}e^{+iqx/2},
\qquad
f_2(x,z,t)=A\,e^{i(kz-\omega t)}e^{-iqx/2},
$$

where:

- $A$ is the common complex amplitude,
- $q$ is the transverse fringe wave number set by the small crossing angle,
- each incident beam carries local density
  $$
  u := |A|^2.
  $$


### Raw Coherent Overlap

Before any final output-mode projection, the two-beam overlap is

$$
f_{\mathrm{raw}} = f_1 + f_2
=
2A\cos\!\left(\frac{qx}{2}\right)e^{i(kz-\omega t)}.
$$

So the raw overlap density is

$$
u_{\mathrm{raw}}(x)
=
|f_{\mathrm{raw}}|^2
=
4u\cos^2\!\left(\frac{qx}{2}\right).
$$

Therefore

$$
0 \le u_{\mathrm{raw}}(x) \le 4u.
$$

At a bright-fringe center

$$
x_n = \frac{2\pi n}{q},
$$

the raw overlap reaches

$$
u_{\mathrm{raw}}(x_n)=4u.
$$


### Bright-Core Region with Loading Above 3u

To isolate the strongest part of the fringe, one wants the neighborhood in
which the raw coherent loading remains above $3u$.

Write

$$
x = x_n + \Delta x.
$$

Then

$$
u_{\mathrm{raw}}(x)
=
4u\cos^2\!\left(\frac{q\Delta x}{2}\right).
$$

The condition

$$
u_{\mathrm{raw}}(x) > 3u
$$

is equivalent to

$$
4\cos^2\!\left(\frac{q\Delta x}{2}\right) > 3,
$$

that is,

$$
\cos^2\!\left(\frac{q\Delta x}{2}\right) > \frac{3}{4}.
$$

Hence

$$
\left|\frac{q\Delta x}{2}\right| < \frac{\pi}{6},
$$

so

$$
|\Delta x| < \frac{\pi}{3q}.
$$

If the fringe period is

$$
\Lambda = \frac{2\pi}{q},
$$

then the bright-core condition is

$$
|\Delta x| < \frac{\Lambda}{6}.
$$

So the central region of each bright fringe contains a stripe of full width

$$
\frac{\Lambda}{3}
$$

on which the raw coherent loading stays strictly above $3u$.


### Complementary Mach-Zehnder Outputs

If the same two fields are projected through the final 50/50 beam splitter of
a slightly misaligned Mach-Zehnder interferometer, the observable output modes
are the normalized combinations

$$
f_+(x)=\frac{f_1(x)+f_2(x)}{\sqrt2},
\qquad
f_-(x)=\frac{f_1(x)-f_2(x)}{\sqrt2}.
$$

This gives

$$
f_+(x)=\sqrt2\,A\cos\!\left(\frac{qx}{2}\right)e^{i(kz-\omega t)},
$$

$$
f_-(x)=i\sqrt2\,A\sin\!\left(\frac{qx}{2}\right)e^{i(kz-\omega t)}.
$$

Therefore the two output densities are

$$
u_+(x)=2u\cos^2\!\left(\frac{qx}{2}\right),
\qquad
u_-(x)=2u\sin^2\!\left(\frac{qx}{2}\right).
$$

These are complementary:

$$
u_+(x)+u_-(x)=2u.
$$

So:

- a bright fringe on one output corresponds to a dark fringe on the other,
- the two outputs together recover the full incident two-beam power,
- the raw coherent loading is described by $u_{\mathrm{raw}}(x)$,
- the observable output branches are described by the complementary
  $u_+(x)$ and $u_-(x)$ profiles.

The proposed measurement targets the central part of a bright fringe ridge,
where the raw overlap loading is maximal and where the branch selected from one
output is most naturally associated with the strongest coherent loading.


## Proposed Geometry

1. Split a coherent laser beam into two equal beams.
2. Recombine them at a small angle to form stable straight fringes.
3. Select one bright fringe ridge using a slit or equivalent spatial filter.
4. Propagate that isolated ridge over a known forward distance.
5. In parallel, propagate one incident beam as a matched reference over the
   same distance.
6. Compare the two arrival times using amplitude modulation or pulse timing.


## Measurement

The cleanest readout is longitudinal delay:

- modulate both channels in the same way,
- send both through equal downstream lengths,
- measure the phase delay or pulse delay at the outputs.

Possible realizations:

- free-space propagation over equal lengths,
- propagation through a tube or cell,
- propagation through a medium such as water or gas, if desired.


## Minimum Experimental Requirements

- stable coherent source
- interferometric splitting and recombination
- controlled small crossing angle
- stable fringe pattern
- spatial filtering of one bright ridge
- matched reference channel
- modulation source or pulsed source
- time-delay or phase-delay detection


## Why the Comparison Matters

A screen at one fixed plane only shows the fringe pattern. It does not measure
the forward travel time of one bright ridge. The required comparison is instead
between:

- one isolated bright fringe channel, and
- one matched incident-beam reference channel.

That is the direct test of whether higher recovered density is accompanied by a
larger forward delay.


## Useful Controls

- vary the crossing angle while keeping downstream distance fixed
- compare bright-ridge delay against either incident beam
- compare bright-ridge delay against the unsplit beam
- repeat in air and in a simple medium
- check whether any measured delay scales with fringe brightness or geometry


## Expected Value of the Project

This project is useful even if the result is null.

- If no additional delay is observed, that places a clean constraint on the
  loaded-branch hypothesis.
- If a reproducible excess delay is observed, that would justify a more careful
  follow-up study.


## Summary

The proposed measurement is simple in form:

- create a stable fringe pattern,
- isolate one bright fringe ridge,
- propagate it forward,
- compare its delay against an incident-beam reference.

That gives a direct experimental test of whether coherent density loading in an
isolated fringe channel affects longitudinal propagation delay.
