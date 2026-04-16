---
title: Project Note - Longitudinal Delay of an Isolated Interference Fringe
date: 2026-04-16
---

# Project Note

## Title

Longitudinal Delay of an Isolated Bright Interference Fringe


## Motivation

This note outlines a short optical measurement project motivated by a simple
question: if two equal coherent beams overlap and create a stable fringe
pattern, does an isolated bright fringe ridge propagate with the same forward
delay as a matched lower-density single-beam reference, or does the higher
local density of the bright ridge produce an additional delay?


## Basic Idea

Two equal coherent beams are crossed at a small angle so that a stable fringe
pattern is formed. A narrow bright fringe ridge is then spatially filtered and
allowed to propagate forward as an isolated channel. Its modulation or pulse
delay is compared against a matched single-beam reference that carries the same
carrier and modulation but lower density.

The goal is not to measure fringe visibility. The goal is to measure the
forward propagation delay of one bright fringe channel.


## Hypothesis

For two equal coherent amplitudes, the local loading follows the square of
their sum. This gives a fringe density profile that ranges from dark points to
bright points with substantially higher local density than either beam alone.

Under the working hypothesis behind this project, the bright fringe ridge is
treated as a surviving loaded channel. If the same forward flux budget is
recovered on a denser ridge, then the effective forward advance of that ridge
should be reduced relative to a lower-density reference channel.

So the experimental question is:

- standard expectation: the isolated bright ridge shows the usual propagation
  delay for the chosen medium,
- loaded-branch hypothesis: the isolated bright ridge shows an additional
  forward delay.


## Proposed Geometry

1. Split a coherent laser beam into two equal beams.
2. Recombine them at a small angle to form stable straight fringes.
3. Select one bright fringe ridge using a slit or equivalent spatial filter.
4. Propagate that isolated ridge over a known forward distance.
5. In parallel, propagate a matched lower-density single-beam reference over
   the same distance.
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
- one matched lower-density reference channel.

That is the direct test of whether higher recovered density is accompanied by a
larger forward delay.


## Useful Controls

- vary the crossing angle while keeping downstream distance fixed
- compare bright-ridge delay against the unsplit beam
- compare bright-ridge delay against one single arm with matched power
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
- compare its delay against a matched lower-density reference.

That gives a direct experimental test of whether coherent density loading in an
isolated fringe channel affects longitudinal propagation delay.
