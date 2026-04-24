---
title: The Experiment Nobody Did
subtitle: A bright interference fringe, a glass slab, and a question a century of interferometry never asked.
author: An M. Rodriguez, Leo Marchetti
date: 2026-04-23
one-sentence-summary: Two coherent beams meeting in phase form a bright fringe whose propagation speed is universally assumed to be c -- but the specific experiment that would test it has apparently never been done.
summary: Standard optics treats a bright Mach-Zehnder fringe as a combined field that propagates at the speed of light, because Maxwell's equations in vacuum are linear and two plane waves superpose without slowing. Yet a dielectric slows light precisely because a second in-phase electromagnetic wave (the polarization response) rides alongside the incident one -- exactly the configuration of two equal coherent arms meeting at a bright fringe. Written literally, that would give c_eff = c/2. A refraction test at a glass boundary near the critical angle is a binary discriminator: either the bright fringe transmits, or it undergoes total internal reflection. Across precision interferometry -- LIGO, Mach-Zehnder metrology, fiber gyroscopes, Fizeau, Michelson-Morley -- no experiment appears to have set up this specific test and looked. The assumption goes through because Maxwell is taken as linear, not because anyone checked.
keywords:
  - interference
  - Mach-Zehnder
  - dielectric slowing
  - refraction
  - critical angle
  - experimental physics
  - coherent superposition
  - Dirac dictum
doi:
---

Ask a physics student what happens when two coherent laser beams meet in phase
at a bright interference fringe, and you'll get a confident answer: the fields
add, the bright fringe has four times the energy density of one arm, and it
propagates at the speed of light.

The first two are boringly true. The third is a guess.

## The dielectric mechanism, honestly

A dielectric slows light because the medium's polarization response is an
in-phase electromagnetic wave riding alongside the incident wave. Maxwell's
equations then describe the combined field — incident plus response —
propagating at the reduced speed

$$
c_\text{eff} = \frac{1}{\sqrt{\varepsilon_\text{eff}\mu_\text{eff}}} = \frac{c}{n}.
$$

The dielectric index $n$ encodes, at bottom, the presence of a second in-phase
electromagnetic wave.

At a Mach-Zehnder recombination, the second arm beam *is* an in-phase
electromagnetic wave riding alongside the first. Both arms come from the same
coherent source, travel equal paths, and arrive in phase at a bright point.
Same mathematical structure. Same Maxwell derivation. For equal beams in full
constructive interference, the amplitude ratio $k = 1$, and the formula gives
$c_\text{eff} = c/2$.

Standard optics says no: Maxwell in vacuum is linear, two plane waves
superpose, the combined field still satisfies the vacuum wave equation with
phase velocity $c$. No dielectric loading without matter.

Which reading is right?

## The experiment

Set up a Mach-Zehnder. Isolate one bright fringe with an aperture. Shine it at
a glass slab ($n_g \approx 1.5$) at oblique incidence $\theta_i$. Compare the
refraction angle against a matched reference beam taken straight from the
laser.

Two predictions:

- **Ordinary** ($n_\text{eff} = 1$): standard refraction, identical to the
  reference. $\sin\theta_r = \sin\theta_i / n_g$.
- **Loaded** ($n_\text{eff} = 2$): the bright fringe behaves like a beam
  leaving a denser medium. $\sin\theta_r = (2/n_g) \sin\theta_i$, and there's
  a critical angle at $\sin\theta_c = n_g/2 = 0.75$, so $\theta_c \approx
  48.6^\circ$.

Above the critical angle, the loaded reading predicts total internal
reflection — no transmitted beam. The ordinary reading predicts standard
transmission. Binary outcome. Glass slab, a CCD, a reference beam. No
nanosecond timing required.

## The surprise

I went looking for this experiment. Across LIGO, Mach-Zehnder metrology, fiber
gyroscopes, slow-light demonstrations, Fizeau, Michelson-Morley, light-by-light
scattering in stressed QED vacuum. All of them measure something else.

Precision interferometers measure *intensity at the output port* — a
photodetector sits right at the recombiner. They read the phase between arms.
None of them deliberately propagate a bright fringe over distance, or send it
into a glass boundary at oblique incidence, and compare.

Every undergraduate textbook assumes the bright fringe propagates at $c$,
because Maxwell in vacuum is linear. Nobody built a setup whose output would
be different under the two readings and checked.

## Why this is worth a Friday afternoon

The test is cheap. The prediction is binary. The gap in the literature is
real.

If the loaded reading wins, the consequences are large: coherent superposition
by itself loads Maxwell's equations, independent of matter, and the program of
treating refraction as a linear-optical phenomenon needs revisiting.

If the ordinary reading wins, we tighten the empirical case for vacuum
linearity against a mechanism that, until tested, was only reached by
assumption.

A hundred years of interferometry, and a question nobody asked.
