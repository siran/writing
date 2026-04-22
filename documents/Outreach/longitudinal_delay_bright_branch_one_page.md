---
title: Simplified Proposal - Longitudinal Delay of an Isolated Bright Interference Branch
date: 2026-04-22
---

# Simplified Proposal

## Abstract

This proposal begins from the standard result that light propagates more slowly
in a transparent dielectric. In the usual electromagnetic description, the
electric and magnetic response of the medium increases the effective
permittivity and permeability, so the propagation speed becomes

$$
c_{\mathrm{eff}}=\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}
=\frac{c}{n}.
$$

The proposal then asks whether the same kind of slowdown appears when two
coherent beams fully overlap in the recombination phase of a Mach-Zehnder
interferometer. The first beam splitter only prepares two bright arm beams. The
question appears later, when those beams recombine. These are not the same
spatial operation run backward.

If each overlapping beam is treated as the coherent electromagnetic response
seen by the other, then equal-beam bright overlap doubles the fields, quadruples
the instantaneous energy density, and gives the same reduced-speed result

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

The standard output reading instead assigns the bright output density `2u_0`
and predicts no anomalous delay. The experiment is therefore a direct
time-of-flight test between these two readings.

---

## 1. Classic Dielectric Result

In a transparent linear dielectric,

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P,
$$

and for a linear response,

$$
\mathbf P=\varepsilon_0\chi_e\mathbf E.
$$

Therefore

$$
\mathbf D=\varepsilon_0(1+\chi_e)\mathbf E
=\varepsilon_{\mathrm{eff}}\mathbf E,
$$

so

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+\chi_e).
$$

If the magnetic sector is likewise loaded,

$$
\mu_{\mathrm{eff}}=\mu_0(1+\chi_m).
$$

Then the propagation speed is

$$
c_{\mathrm{eff}}
=\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}.
$$

For symmetric electric and magnetic loading,

$$
\chi_e=\chi_m=k,
$$

so

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+k),
\qquad
\mu_{\mathrm{eff}}=\mu_0(1+k),
$$

and therefore

$$
c_{\mathrm{eff}}
=\frac{1}{\sqrt{\varepsilon_0\mu_0(1+k)^2}}
=\frac{c}{1+k}.
$$

This is the standard reduced-speed result.

---

## 2. Same Structure at Coherent Overlap

The proposal asks whether the same electromagnetic loading structure appears
when two coherent beams fully overlap in vacuum during recombination.

Let one beam have fields

$$
\mathbf E_1,\qquad \mathbf B_1,
$$

and let the second beam act as a coherent response field proportional to the
first:

$$
\mathbf E_2=k\mathbf E_1,
\qquad
\mathbf B_2=k\mathbf B_1.
$$

Then the total overlap fields are

$$
\mathbf E_{\mathrm{tot}}=(1+k)\mathbf E_1,
\qquad
\mathbf B_{\mathrm{tot}}=(1+k)\mathbf B_1.
$$

Because electromagnetic energy density is quadratic in the fields, the overlap
density scales as

$$
u_{\mathrm{tot}}=(1+k)^2u_1.
$$

If the same loading rule as in the dielectric case is applied, then

$$
c_{\mathrm{eff}}=\frac{c}{1+k}.
$$

For equal coherent overlap,

$$
k=1,
$$

so

$$
\mathbf E_{\mathrm{tot}}=2\mathbf E_1,
\qquad
\mathbf B_{\mathrm{tot}}=2\mathbf B_1,
$$

and

$$
u_{\mathrm{tot}}=4u_1.
$$

Therefore

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

That is the simple claim being tested.

---

## 3. Why the Split Phase Is Different

A Mach-Zehnder has two distinct phases.

At the first beam splitter:

- one bright incident beam becomes two bright arm beams
- the purpose is to prepare coherent branches
- no loaded overlap is being claimed

At recombination:

- two arm beams meet coherently
- the fields add or subtract before the ordinary output decomposition is written
- the loaded-branch question is whether the bright raw overlap itself propagates
  with the reduced speed above

So the slowdown question belongs to recombination, not to the initial split.

---

## 4. Experimental Fork

At a lossless 50/50 recombiner, the ordinary output fields are

$$
\mathbf E_+=\frac{\mathbf E_1+\mathbf E_2}{\sqrt 2},
\qquad
\mathbf E_-=\frac{\mathbf E_1-\mathbf E_2}{\sqrt 2},
$$

and likewise for the magnetic fields.

For equal beams at a bright output point, the standard output reading gives

$$
u_+=2u_0,
\qquad
u_-=0.
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
  in the equal-beam limit

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

For the equal-beam limit,

$$
\tau_{\mathrm{bright}}-\tau_{\mathrm{ref}}\approx \frac{L}{c}.
$$

So at `1 m` the extra delay is about `3.34 ns`, and at `10 m` it is about
`33.4 ns`.

---

## 6. Detailed Derivation

### 6.1 Dielectric Derivation

Start from

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P,
\qquad
\mathbf P=\varepsilon_0\chi_e\mathbf E.
$$

Then

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+\chi_e).
$$

If the magnetic sector is likewise loaded,

$$
\mu_{\mathrm{eff}}=\mu_0(1+\chi_m).
$$

So

$$
c_{\mathrm{eff}}=\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}.
$$

For symmetric loading `\chi_e=\chi_m=k`,

$$
c_{\mathrm{eff}}=\frac{c}{1+k}.
$$

### 6.2 Instantaneous Overlap Derivation

No time averaging is needed for the basic bright-point argument.

At a full bright overlap point for equal beams,

$$
\mathbf E_1(t)=\mathbf E_0(t),
\qquad
\mathbf E_2(t)=\mathbf E_0(t),
$$

and

$$
\mathbf B_1(t)=\mathbf B_0(t),
\qquad
\mathbf B_2(t)=\mathbf B_0(t).
$$

Then

$$
\mathbf E_{\mathrm{tot}}(t)=2\mathbf E_0(t),
\qquad
\mathbf B_{\mathrm{tot}}(t)=2\mathbf B_0(t).
$$

The instantaneous electromagnetic energy density is

$$
u_{\mathrm{tot}}(t)
=
\frac{\varepsilon_0}{2}\lvert \mathbf E_{\mathrm{tot}}(t)\rvert^2
+
\frac{1}{2\mu_0}\lvert \mathbf B_{\mathrm{tot}}(t)\rvert^2.
$$

Substituting the doubled fields gives

$$
u_{\mathrm{tot}}(t)=4u_0(t).
$$

So the bright-point factor of four is already an instantaneous result.

### 6.3 Coherent-Response Form

Write the second beam as a coherent response field proportional to the first:

$$
\mathbf E_2=k\mathbf E_1,
\qquad
\mathbf B_2=k\mathbf B_1.
$$

Then

$$
\mathbf E_{\mathrm{tot}}=(1+k)\mathbf E_1,
\qquad
\mathbf B_{\mathrm{tot}}=(1+k)\mathbf B_1,
$$

so

$$
u_{\mathrm{tot}}=(1+k)^2u_1.
$$

Applying the same reduced-speed structure as in the dielectric case gives

$$
c_{\mathrm{eff}}=\frac{c}{1+k}.
$$

For equal overlap, `k=1`, hence

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

---

## 7. What the Experiment Decides

This experiment tests which object should be treated as the propagating branch
after recombination:

- the ordinary normalized output mode
- or the isolated raw bright overlap

If the measured delay matches the reference, the ordinary reading wins. If the
measured delay approaches the `c/2` prediction in the equal-beam limit, the
loaded-branch reading is supported.
