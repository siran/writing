---
title: Simplified Proposal - Longitudinal Delay of an Isolated Bright Interference Branch
date: 2026-04-22
---

# Simplified Proposal

## Abstract

This proposal begins from the standard result that light propagates more slowly
in a dielectric because a given longitudinal flux is carried on a larger total
energy density. In that form, the effective transport speed is

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

The proposal then asks whether the same loading effect appears when two
coherent beams fully overlap in the recombination phase of a Mach-Zehnder
interferometer. The first beam splitter only prepares two bright arm beams. The
slowdown question appears later, when those two beams recombine. These two
phases are not the same spatial operation run backward.

At a bright recombination point for two equal beams, the instantaneous overlap
fields double, so the raw energy density is four times the single-beam density.
But the conserved longitudinal flux feeding that point is only the sum of the
two beam fluxes. Under the loaded-branch reading,

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

## 1. Classic Dielectric Result

In a transparent linear dielectric, standard electromagnetism gives the
familiar reduced speed

$$
v_{\mathrm{dielectric}}=\frac{1}{\sqrt{\varepsilon\mu}}=\frac{c}{n}.
$$

The same result can be written in transport form:

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

Here `J` is the longitudinal energy flux and `u` is the total electromagnetic
energy density carried with the wave. The medium response increases the total
carried energy density, so the same through-flux corresponds to a smaller
transport speed. That is the standard starting point.

---

## 2. Same Logic at Coherent Overlap

This proposal asks whether the same loading effect appears when two coherent
beams fully overlap in vacuum during recombination.

At a full bright overlap point, the electric and magnetic fields add before the
energy-density readout is taken. For two equal beams,

$$
E_{\mathrm{raw}}=2E_0,
\qquad
B_{\mathrm{raw}}=2B_0.
$$

So the instantaneous raw energy density is

$$
u_{\mathrm{raw}}=4u_0.
$$

But the longitudinal flux feeding that bright point is only the sum of the two
beam fluxes:

$$
J=2u_0c_z.
$$

If the isolated bright branch is treated as the transported branch, then

$$
v_{\mathrm{eff}}=\frac{J}{u_{\mathrm{raw}}}
=\frac{2u_0c_z}{4u_0}
=\frac{c_z}{2}.
$$

On axis, where `c_z=c`,

$$
v_{\mathrm{eff}}=\frac{c}{2}.
$$

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

## 4. Experimental Fork

At a lossless 50/50 recombiner, the ordinary output fields are

$$
E_+=\frac{E_1+E_2}{\sqrt 2},
\qquad
E_-=\frac{E_1-E_2}{\sqrt 2},
$$

and likewise for the magnetic fields.

So for equal beams at a bright output point, the standard output reading gives

$$
u_+=2u_0,
\qquad
u_-=0.
$$

Therefore the two readings are:

- ordinary output reading:
  $$
  v_{\mathrm{bright}}=v_{\mathrm{ref}}
  $$
- loaded raw-overlap reading:
  $$
  v_{\mathrm{bright}}=\frac{v_{\mathrm{ref}}}{2}
  $$
  in the equal-beam on-axis limit

---

## 5. Experimental Idea

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

## 6. Detailed Derivation

### 6.1 Dielectric Speed in Standard Form

For a plane wave in a transparent linear dielectric,

$$
v=\frac{1}{\sqrt{\varepsilon\mu}}.
$$

This is the standard reduced propagation speed.

The same result can be written in transport form as

$$
v_{\mathrm{eff}}=\frac{J}{u},
$$

where `J` is longitudinal energy flux and `u` is the total carried
electromagnetic energy density.

### 6.2 Instantaneous Bright-Point Density

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

### 6.3 Local Longitudinal Flux

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

### 6.4 Loaded-Branch Speed

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
