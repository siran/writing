---
title: Simplified Proposal - Longitudinal Delay of an Isolated Bright Interference Branch
date: 2026-04-22
---

# Simplified Proposal

## Abstract

This proposal tests whether an isolated bright interference branch in a
Mach-Zehnder interferometer propagates with the ordinary reference speed, or
with a reduced effective longitudinal transport speed.

The key physical point is that a Mach-Zehnder has two distinct phases:

1. a split phase, where one bright input beam becomes two bright arm beams
2. a recombination phase, where two coherent arm beams overlap and recover one
   two-beam flux before the ordinary output decomposition is written

These are not the same spatial operation run backward. The slowdown question
belongs to the recombination phase.

At a bright recombination point for two equal beams, the raw overlap fields
double, so the instantaneous energy density is four times the single-beam
density. But the conserved longitudinal flux feeding that point is only the sum
of the two beam fluxes. Under the loaded-branch reading,

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

So for equal beams on axis,

$$
J=2u_0c,
\qquad
u_{\mathrm{raw}}=4u_0,
\qquad
v_{\mathrm{eff}}=\frac{c}{2}.
$$

The standard output reading instead assigns the bright output density `2u_0`
and predicts no anomalous delay. The experiment is a direct time-of-flight test
between these two readings.

---

## 1. One-Page Statement

Start with one input beam entering a Mach-Zehnder. At the first beam splitter,
the beam is divided into two bright arm beams. Nothing unusual is being claimed
there. The split phase simply prepares two coherent branches.

The question appears at recombination. Two coherent arm beams overlap. At a
bright center, the electric and magnetic fields add before the density readout
is taken. Because energy density is quadratic in the fields, the raw overlap
density is larger than the density of either beam by itself.

For two equal beams at full bright overlap:

$$
u_{\mathrm{raw}}=4u_0.
$$

But the longitudinal flux feeding that bright region is only the sum of the two
incoming beam fluxes:

$$
J=2u_0c_z.
$$

If the isolated bright branch is treated as the transported branch, then the
effective longitudinal transport speed is

$$
v_{\mathrm{eff}}=\frac{J}{u_{\mathrm{raw}}}
=\frac{2u_0c_z}{4u_0}
=\frac{c_z}{2}.
$$

On axis, where `c_z=c`,

$$
v_{\mathrm{eff}}=\frac{c}{2}.
$$

So the experimental fork is:

- ordinary output reading:
  $$
  v_{\mathrm{bright}}=v_{\mathrm{ref}}
  $$
- loaded raw-overlap reading:
  $$
  v_{\mathrm{bright}}=\frac{v_{\mathrm{ref}}}{2}
  $$
  in the equal-beam on-axis limit

That prediction is large enough to be tested directly by modulation-delay
measurement.

---

## 2. Experimental Idea

Use a coherent source, modulate it, split it into two arms, and recombine the
arms so they form stable fringes. Then:

1. isolate one bright branch with an aperture
2. propagate that selected branch over distance `L`
3. propagate a matched reference beam over the same distance
4. compare delay slopes `d\tau/dL`

The standard output reading predicts equal slopes. The loaded-branch reading
predicts a larger slope for the bright branch.

For the equal-beam on-axis limit,

$$
\tau_{\mathrm{bright}}-\tau_{\mathrm{ref}}\approx \frac{L}{c}.
$$

So at `1 m` the extra delay is about `3.34 ns`, and at `10 m` it is about
`33.4 ns`.

---

## 3. Why the Split Phase Is Different

The first beam splitter and the recombination phase should not be described as
the same spatial process.

At the first beam splitter:

- one bright incident beam becomes two bright arm beams
- the purpose is to prepare coherent branches
- no loaded overlap is being claimed

At recombination:

- two arm beams meet coherently
- one recovered two-beam flux is present before the ordinary output
  decomposition is written
- the loaded-branch question is whether the isolated bright raw overlap itself
  transports as a branch

This is why the test belongs to the recombination phase, not to the initial
split.

---

## 4. Standard Output Reading

At a lossless 50/50 recombiner, the ordinary output fields are

$$
E_+=\frac{E_1+E_2}{\sqrt 2},
\qquad
E_-=\frac{E_1-E_2}{\sqrt 2},
$$

and likewise for the magnetic fields.

So for equal beams at a bright output point,

$$
u_+=2u_0,
\qquad
u_-=0.
$$

This reading predicts no anomalous delay:

$$
v_{\mathrm{bright}}=v_{\mathrm{ref}}.
$$

---

## 5. Loaded Raw-Overlap Reading

The loaded reading uses the same electromagnetic loading effect as dielectric
slowing, but now applied to full coherent overlap in vacuum. Each beam is
treated as the coherent response seen by the other. The overlap branch carries
the conserved two-beam flux on a higher local energy density, so

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

At equal-beam bright overlap,

$$
J=2u_0c_z,
\qquad
u_{\mathrm{raw}}=4u_0,
$$

therefore

$$
v_{\mathrm{eff}}=\frac{c_z}{2}.
$$

This is the tested claim.

---

## 6. Detailed Derivation

### 6.1 Instantaneous Bright-Point Density

No time averaging is needed for the basic bright-point argument.

At a full bright overlap point, take two equal coherent beams with instantaneous
fields

$$
E_1(t)=E_0(t),
\qquad
E_2(t)=E_0(t),
$$

and

$$
B_1(t)=B_0(t),
\qquad
B_2(t)=B_0(t).
$$

Then

$$
E_{\mathrm{raw}}(t)=E_1(t)+E_2(t)=2E_0(t),
$$

and

$$
B_{\mathrm{raw}}(t)=B_1(t)+B_2(t)=2B_0(t).
$$

The instantaneous electromagnetic energy density is

$$
u_{\mathrm{raw}}(t)
=
\frac{\varepsilon_0}{2}E_{\mathrm{raw}}(t)^2
+
\frac{1}{2\mu_0}B_{\mathrm{raw}}(t)^2.
$$

Substituting the doubled fields gives

$$
u_{\mathrm{raw}}(t)
=
4\left[
\frac{\varepsilon_0}{2}E_0(t)^2
+
\frac{1}{2\mu_0}B_0(t)^2
\right]
=4u_0(t).
$$

So the bright-point factor of four is already an instantaneous result.

### 6.2 Local Longitudinal Flux

For a freely propagating beam in vacuum, or more generally in a transparent
linear medium, the local longitudinal flux is

$$
J_{iz}=u_i c\cos\alpha_i,
$$

where `\alpha_i` is the local angle between the energy-flow direction and the
measurement axis.

For two equal beams with the same local longitudinal factor `c_z`,

$$
J=J_{1z}+J_{2z}=2u_0c_z.
$$

### 6.3 Loaded-Branch Speed

Combining the two previous results,

$$
v_{\mathrm{eff}}=\frac{J}{u_{\mathrm{raw}}}
=\frac{2u_0c_z}{4u_0}
=\frac{c_z}{2}.
$$

On axis,

$$
v_{\mathrm{eff}}=\frac{c}{2}.
$$

---

## 7. What the Experiment Decides

This experiment does not test whether energy is conserved. Energy conservation
is assumed throughout.

It tests which object should be treated as the transported branch after
recombination:

- the ordinary normalized output mode
- or the isolated raw bright overlap

If the measured delay matches the reference, the ordinary reading wins. If the
measured delay approaches the `c/2` prediction in the equal-beam limit, the
loaded-branch reading is supported.
