---
title: "Experimental Proposal -- Confirmation of a Dielectric Longitudinal Delay of a Bright Interference Fringe"
subtitle: "A dielectric-first derivation and time-of-flight test in a Mach-Zehnder interferometer"
author: "An M. Rodriguez"
date: "2026-04-22"
one-sentence-summary: "A bright interference fringe produced at Mach-Zehnder recombination carries increased constructive-interference energy density and therefore exhibits a dielectric longitudinal delay relative to an ordinary reference beam."
summary: "Electromagnetic propagation in a dielectric slows when the electric and magnetic response increases the effective permittivity and permeability. Full coherent superposition at Mach-Zehnder recombination has the same loading structure. The first beam splitter creates two bright arm beams, while recombination is a distinct phase in which two populated arm states meet and are redistributed across the two output ports. Each beam supplies the coherent response seen by the other, so equal-beam constructive interference doubles the fields, quadruples the instantaneous energy density at the bright center, and yields c_eff = c/2. The ordinary output reading instead assigns the bright output density 2u_0 and therefore gives no anomalous delay. Isolating a bright interference fringe and comparing its modulation delay against a matched reference beam over the same longitudinal distance gives a direct time-of-flight discrimination between the two readings."
keywords:
  - interference
  - Mach-Zehnder interferometer
  - dielectric slowing
  - dielectric longitudinal delay
  - constructive interference
  - energy density
  - bright interference fringe
  - time-of-flight
  - speed of light
---

# Experimental Proposal -- Confirmation of a Dielectric Longitudinal Delay of a Bright Interference Fringe

## Abstract

A dielectric slows light because the medium responds to the incident
electromagnetic wave with an in-phase polarization wave. Maxwell's equations
then describe the combined field — incident plus response — propagating at the
reduced speed

$$
c_{\mathrm{eff}}=\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}
=\frac{c}{n}.
$$

A dielectric is, at bottom, a coherent recombiner: one in-phase electromagnetic
wave riding alongside another.

At Mach-Zehnder recombination, the second arm beam is that in-phase response.
Both arms originate from the same coherent source, travel equal paths, and
arrive in phase at a bright point. Each beam is, for the other, the in-phase
electromagnetic addition that constitutes the dielectric loading. This is not
an analogy to the dielectric case — it is the dielectric mechanism, with the
second arm supplying the response sector instead of the medium.

The first beam splitter only prepares two coherent arm beams. The loading
question belongs to recombination, not to the initial split (see @sec:split).

Equal-beam constructive interference therefore doubles the fields, quadruples
the instantaneous energy density, and gives

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

The standard output reading assigns the bright output density $2u_0$ and
predicts no delay. The experiment is a direct time-of-flight test between these
two readings.

---

## Rationale

In a linear dielectric, an incident electromagnetic wave induces a response
electromagnetic wave in the medium. Maxwell electrodynamics is linear, so the
physical field is the sum of the incident and response sectors.

When that response is in phase with the incident wave, the fields add, the
local electromagnetic energy density increases, and the propagation speed is
reduced through the larger effective permittivity and permeability.

Constructive interference is that same mechanism. Two coherent beams add
linearly in phase: one sector carried together with a second in-phase
electromagnetic response sector. That is not a pattern that resembles a
dielectric — it is what a dielectric is. The longitudinal delay at
constructive interference is a dielectric delay.

This logic is one-sided. Constructive interference yields a denser surviving
bright fringe, while destructive interference depletes the field and in the
dark-limit cancels the fringe rather than producing a faster propagated one.

---

## Classic Dielectric Result

In a transparent linear dielectric,

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P,
$$

and

$$
\mathbf B=\mu_0(\mathbf H+\mathbf M).
$$

For a linear response,

$$
\mathbf P=\varepsilon_0\chi_e\mathbf E.
$$

and

$$
\mathbf M=\chi_m\mathbf H.
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

In a source-free region,

$$
\nabla\times \mathbf E=-\frac{\partial \mathbf B}{\partial t},
\qquad
\nabla\times \mathbf H=\frac{\partial \mathbf D}{\partial t}.
$$

Substituting the effective constitutive relations gives

$$
\nabla\times \mathbf E=-\mu_{\mathrm{eff}}\frac{\partial \mathbf H}{\partial t},
\qquad
\nabla\times \mathbf H=\varepsilon_{\mathrm{eff}}\frac{\partial \mathbf E}{\partial t}.
$$

Taking the curl of the first equation, and using the second together with
$\nabla\cdot\mathbf E=0$, gives the wave equation

$$
\nabla^2\mathbf E-\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}
\frac{\partial^2\mathbf E}{\partial t^2}=0.
$$

Therefore the propagation speed is

$$
c_{\mathrm{eff}}=\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}.
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

## Recombination as a Dielectric

A dielectric slows light because the medium's polarization response is an
in-phase electromagnetic wave riding alongside the incident wave. The physical
content of the dielectric result is this: an in-phase electromagnetic response
sector accompanying a wave reduces the propagation speed. The permittivity and
permeability merely parametrize how large that response is.

At Mach-Zehnder recombination, the second arm beam is that response sector.
Both arms come from the same coherent source and arrive in phase at a bright
point. Each beam is, from the other's perspective, an in-phase electromagnetic
addition. The medium's polarization current and the second arm beam are two
physical realizations of the same coherent in-phase response. The reduced-speed
result is not transferred by analogy — it applies directly, because the
mechanism is the same.

Writing the second beam as the response sector proportional to the first,

$$
\mathbf E_2=k\mathbf E_1,
\qquad
\mathbf H_2=k\mathbf H_1,
$$

and defining, abbreviating *coherent* by the subscript $\mathrm{coh}$,

$$
\mathbf D_{\mathrm{coh}}
=\varepsilon_0(\mathbf E_1+\mathbf E_2),
\qquad
\mathbf B_{\mathrm{coh}}
=\mu_0(\mathbf H_1+\mathbf H_2).
$$

Then

$$
\mathbf D_{\mathrm{coh}}
=\varepsilon_0(1+k)\mathbf E_1
=\varepsilon_{\mathrm{coh}}\mathbf E_1,
$$

with

$$
\varepsilon_{\mathrm{coh}}=\varepsilon_0(1+k),
$$

and likewise

$$
\mathbf B_{\mathrm{coh}}
=\mu_0(1+k)\mathbf H_1
=\mu_{\mathrm{coh}}\mathbf H_1,
$$

with

$$
\mu_{\mathrm{coh}}=\mu_0(1+k).
$$

The same source-free Maxwell form then becomes

$$
\nabla\times \mathbf E_1
=-\frac{\partial \mathbf B_{\mathrm{coh}}}{\partial t},
\qquad
\nabla\times \mathbf H_1
=\frac{\partial \mathbf D_{\mathrm{coh}}}{\partial t}.
$$

So

$$
\nabla\times \mathbf E_1
=-\mu_{\mathrm{coh}}\frac{\partial \mathbf H_1}{\partial t},
\qquad
\nabla\times \mathbf H_1
=\varepsilon_{\mathrm{coh}}\frac{\partial \mathbf E_1}{\partial t}.
$$

Taking the curl again gives

$$
\nabla^2\mathbf E_1-\varepsilon_{\mathrm{coh}}\mu_{\mathrm{coh}}
\frac{\partial^2\mathbf E_1}{\partial t^2}=0,
$$

therefore

$$
c_{\mathrm{eff}}
=\frac{1}{\sqrt{\varepsilon_{\mathrm{coh}}\mu_{\mathrm{coh}}}}
=\frac{1}{\sqrt{\varepsilon_0\mu_0(1+k)^2}}
=\frac{c}{1+k}.
$$

For equal beams at constructive interference,

$$
k=1,
$$

so

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

At the bright center of the fringe, where the interference is constructive,
the total fields are

$$
\mathbf E_{\mathrm{tot}}=2\mathbf E_1,
\qquad
\mathbf H_{\mathrm{tot}}=2\mathbf H_1,
$$

and the instantaneous energy density there is

$$
u_{\mathrm{tot}}=4u_1.
$$

More generally, across the fringe profile one may write

$$
u(x)=4u_1\cos^2\!\left(\frac{\Delta\phi(x)}{2}\right),
$$

so the factor $4$ is the bright-center value of the full spatial dependence.

That is the tested coherent-overlap result.

---

## Why the Split Phase Is Different {#sec:split}

A Mach-Zehnder has two distinct phases.

At the first beam splitter:

- one bright incident beam becomes two bright arm beams
- the purpose is to prepare coherent arm beams
- no loaded constructive-interference fringe is being claimed

At recombination:

- two arm beams meet coherently
- the fields add or subtract before the ordinary output decomposition is written
- the loaded-fringe question is whether the bright raw overlap itself propagates
  with the reduced speed above

Mathematically, the same 50/50 beam-splitter matrix can describe both
interfaces, but the occupied input states are different. If

$$
\binom{b_1}{b_2}
=
\frac{1}{\sqrt 2}
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
\binom{a_1}{a_2},
$$

then the split phase starts from one populated input port,

$$
\binom{a_1}{a_2}=\binom{A}{0},
$$

so

$$
\binom{b_1}{b_2}
=
\binom{A/\sqrt 2}{A/\sqrt 2},
$$

which gives two bright arm beams. Recombination starts instead from two
populated arm inputs,

$$
\binom{a_1}{a_2}=\binom{A}{A},
$$

so

$$
\binom{b_1}{b_2}
=
\binom{\sqrt 2\,A}{0},
$$

which gives one bright output and one dark output. The optical element is the
same, but the populated states are different, so the split and recombination
phases are not the same spatial decomposition.

This also explains why recombination still produces two spatially distributed
output arms rather than a single merged beam. The recombiner is a two-port
linear map: it sends the two incoming arm fields into the sum and difference
output channels. Those channels emerge in different spatial directions, so the
recovered field is written across two output arms even when one of them is dark
at a bright point.

So the slowdown question belongs to recombination, not to the initial split.

---

## Experimental Fork

At a "lossless" 50/50 recombiner, the ordinary output fields are

$$
\mathbf E_+=\frac{\mathbf E_1+\mathbf E_2}{\sqrt 2},
\qquad
\mathbf E_-=\frac{\mathbf E_1-\mathbf E_2}{\sqrt 2},
$$

and likewise for the magnetic fields.

Here "lossless" means the splitter is modeled as conserving total optical
energy, so all energy is accounted for across the two output arms. Small real
losses do not change the core result being tested, and in a well-aligned setup
they are negligible compared with the claimed factor-of-two speed difference.

The factor $1/\sqrt 2$ appears because the splitter divides the incoming energy
into two equal beams. Energy density is a positive quadratic quantity in the
field *amplitudes*, so halving the energy means scaling the field amplitudes by
$1/\sqrt 2$, not by $1/2$. The same factor is written on both the electric and
magnetic fields because they are modeled as vector fields and enter the
electromagnetic energy density quadratically.

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

## Experimental Idea

Use a coherent source, modulate it, split it into two arms, and recombine the
arms so they form stable fringes. Then:

1. isolate one bright interference fringe with an aperture
2. propagate that selected fringe over distance $L$
3. propagate a matched reference beam over the same distance
4. compare delay slopes $d\tau/dL$

The standard output reading predicts equal slopes. The loaded-fringe reading
predicts a larger slope for the bright fringe.

For the equal-beam limit,

$$
\tau_{\mathrm{bright}}-\tau_{\mathrm{ref}}\approx \frac{L}{c}.
$$

So at $1\,\mathrm{m}$ the extra delay is about $3.34\,\mathrm{ns}$, and at
$10\,\mathrm{m}$ it is about $33.4\,\mathrm{ns}$.

---

## Detailed Derivation

### Dielectric Derivation

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

For symmetric loading $\chi_e=\chi_m=k$,

$$
c_{\mathrm{eff}}=\frac{c}{1+k}.
$$

### Instantaneous Constructive-Interference Derivation

No time averaging is needed for the basic bright-point argument.

At a full constructive-interference point for equal beams,

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

### Coherent-Response Form

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

For equal beams at constructive interference, $k=1$, hence

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

---

## What the Experiment Decides

This experiment tests which object should be treated as the propagating fringe
after recombination:

- the ordinary normalized output mode
- or the isolated raw constructive-interference fringe

If the measured delay matches the reference, the ordinary reading wins. If the
measured delay approaches the $c/2$ prediction in the equal-beam limit, the
loaded-fringe reading is supported.
