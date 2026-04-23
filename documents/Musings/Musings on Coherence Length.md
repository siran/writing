---
title: Musings on Coherence Length
author: "An M. Rodriguez <an@preferredframe.com>"
date: 2026-04-23
---

A stable laser has a coherence length of at least twenty centimeters.
Narrow-linewidth lasers reach tens of meters. Optical reference cavities reach
kilometers.

What is this length, physically?

It is the length over which an electromagnetic configuration remembers its own
phase. Over that length, the wave can interfere with itself: the field at one
point is phase-correlated with the field at another point further along the
same beam. Beyond it, the correlation decays, and the field no longer
recognizes its earlier self.

In a classical wave picture — no quantization — the coherent extent is the
natural unit of *one wave*: an extended object with a definite internal phase
structure and a soft boundary where that structure dissolves.

## The Dirac photon

Dirac wrote that each photon interferes only with itself. Within the
coherence length, that *self* is well-defined — the field knows its own
phase. Beyond it, *self* is no longer a useful label. The field is still
there, still oscillating, but its phase has drifted uncorrelated with what
came before.

The Dirac photon in this reading is not a point particle. It is the coherent
extent. A twenty-centimeter photon is not a strange object; it is just the
ordinary thing a laser produces.

Many such extents can share the same volume without interfering, provided
their phases are uncorrelated. For a milliwatt HeNe at 633 nm, a single
twenty-centimeter coherent region contains on the order of $10^{10}$ quantum
photons. They all ride inside one coherent extent, or in adjacent ones.
Counting quantum excitations and counting coherent extents are two different
accountings of the same electromagnetic field.

## The boundary

Is the boundary of coherence sharp?

No. The phase-correlation function decays — exponentially for a Lorentzian
lineshape, Gaussian for a Gaussian lineshape. At the 1/e point the correlation
is about 37%. At three coherence times it is about 5%. There is no edge, only
a halo that thins with distance.

So a coherent extent is cigar-shaped along its direction of travel, with a
transverse size set by the beam waist and a longitudinal size set by the
coherence length. The surfaces are soft — a statistical envelope, not a
membrane. The phase is defined inside, and becomes meaningless outside.

If you could stain the coherent region, it would look like a cigar of colored
smoke traveling at the speed of light along its long axis, with fuzzy ends
that trail off.

## Loading and decoherence

Any dielectric-like loading imposed by a coherent overlap lives inside this
cigar. Two beams derived from the same source that meet in a bright fringe
load each other's propagation only while they remain coherent. As the overlap
exits the coherent extent, the loading fades: the cross term
$\langle\mathbf{E}_1\cdot\mathbf{E}_2\rangle$ decays, $k_{\mathrm{eff}}$ drops
from one toward zero, and the effective refractive index slides from two back
toward one.

The bright fringe does not slam into a wall. It smoothly un-slows.

## Open questions

- The coherent extent has a soft spatial envelope. Does that envelope behave
  as a localized object in its own right — with its own response to
  perturbations — or only as a statistical label on field samples?

- Two partially-overlapping coherent regions with different phase histories:
  can they feel each other at their boundaries? Something like evanescent
  coherence?

- The ordinary laboratory laser routinely produces objects with macroscopic
  spatial extent, carrying phase-correlated structure, and behaving as single
  interfering units. This is ordinary classical physics, yet the usual
  particle intuition (photon as point) does not accommodate it.

- If the coherent extent is what *photon* labels in Dirac's sense, a single
  laboratory photon has a size one could walk around. The strangeness is not
  in the field; it is in the language.
