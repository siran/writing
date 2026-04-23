---
title: "Experimental Proposal -- Confirmation of a Dielectric Longitudinal Delay of a Bright Interference Fringe"
subtitle: "A dielectric-first derivation and two experimental tests in a Mach-Zehnder interferometer"
author: "An M. Rodriguez <an@preferredframe.com>, Leo Marchetti <leo@preferredframe.com>"
date: "2026-04-22"
one-sentence-summary: "At Mach-Zehnder recombination each arm beam is the in-phase electromagnetic response to the other, so the dielectric slowing mechanism applies directly and the bright fringe propagates at c/2."
summary: "Electromagnetic propagation in a dielectric slows because the medium's polarization response is an in-phase electromagnetic wave that loads the effective permittivity and permeability. At Mach-Zehnder recombination the second arm beam plays that role: both arms originate from the same coherent source and arrive in phase, making each beam the full-amplitude in-phase response to the other (k=1), which gives c_eff = c/2 by the standard dielectric formula. The ordinary output reading takes the routed output beam and predicts no delay. Two experiments discriminate the readings: refraction of the isolated bright fringe at a glass boundary — where the loaded reading predicts total internal reflection above the critical angle sin(theta_c) = n_g/2 ~ 0.75 — and time-of-flight along a propagation path."
keywords:
  - interference
  - Mach-Zehnder interferometer
  - dielectric slowing
  - dielectric longitudinal delay
  - constructive interference
  - energy density
  - bright interference fringe
  - refraction
  - Snell's law
  - total internal reflection
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

At equal-beam recombination, the arm amplitudes are equal, so each arm is the
full-amplitude in-phase response to the other: $k=1$. The dielectric formula
then gives directly

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

The ordinary reading takes the routed output beam and predicts no delay. The
experiment is a direct test between these two readings, and it reduces — in
the refraction version — to a binary outcome near the critical angle
$\theta_c\approx 48.6^\circ$.

---

## Introduction

In a linear dielectric, an incident electromagnetic wave induces an in-phase
polarization response. Maxwell's equations, applied to the combined field of
incident wave plus response, yield the reduced propagation speed $c/n$. The
dielectric index encodes, at bottom, the presence of a second in-phase
electromagnetic wave riding alongside the first.

This observation generalizes beyond bulk media. Any configuration that places a
second coherent in-phase electromagnetic wave alongside a probe wave should
produce the same reduced propagation speed, by the same Maxwell derivation.

A Mach-Zehnder interferometer at its recombination point is precisely such a
configuration. Both arm beams originate from the same coherent source, travel
equal paths, and arrive in phase at a bright point. Each beam is, from the
other's perspective, a full-amplitude in-phase electromagnetic response. The
mathematical structure matches the dielectric case exactly, with $k=1$, so the
reduced speed is $c_{\mathrm{eff}}=c/2$.

The ordinary output-mode analysis disagrees. It normalizes the recombined
field through the $1/\sqrt 2$ routing factor and treats the bright port as a
single beam propagating at $c$. This paper derives the loaded-fringe
prediction, frames the disagreement as a direct experimental fork, and
proposes two tests: refraction at a glass boundary (geometric) and
time-of-flight along a propagation path (temporal). The refraction test
reduces the discrimination to a binary outcome near the critical angle
$\theta_c\approx 48.6^\circ$, where the loaded reading predicts total internal
reflection and the ordinary reading predicts standard transmission.

The logic is one-sided. Constructive interference yields a denser in-phase
combined field; destructive interference depletes the field and, in the
dark-fringe limit, cancels it rather than producing anything faster. Only the
bright-fringe direction of the fork carries a substantive prediction.

---

## Theory

### The Dielectric Mechanism

Consider a region in which an electromagnetic probe wave
$(\mathbf E_1,\mathbf H_1)$ is accompanied by an in-phase response wave with
amplitude ratio $k\ge 0$,

$$
\mathbf E_2=k\,\mathbf E_1,
\qquad
\mathbf H_2=k\,\mathbf H_1.
$$

The sum fields enter Maxwell's equations through the constitutive relations

$$
\mathbf D=\varepsilon_0(\mathbf E_1+\mathbf E_2)=\varepsilon_0(1+k)\,\mathbf E_1
\equiv\varepsilon_{\mathrm{eff}}\,\mathbf E_1,
$$

$$
\mathbf B=\mu_0(\mathbf H_1+\mathbf H_2)=\mu_0(1+k)\,\mathbf H_1
\equiv\mu_{\mathrm{eff}}\,\mathbf H_1.
$$

In a source-free region,

$$
\nabla\times\mathbf E_1=-\frac{\partial\mathbf B}{\partial t}
=-\mu_{\mathrm{eff}}\frac{\partial\mathbf H_1}{\partial t},
$$

$$
\nabla\times\mathbf H_1=\frac{\partial\mathbf D}{\partial t}
=\varepsilon_{\mathrm{eff}}\frac{\partial\mathbf E_1}{\partial t}.
$$

Taking the curl of the first equation and using $\nabla\cdot\mathbf E_1=0$
gives the wave equation

$$
\nabla^2\mathbf E_1
-\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}
\frac{\partial^2\mathbf E_1}{\partial t^2}=0,
$$

so the combined field propagates at

$$
c_{\mathrm{eff}}
=\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}
=\frac{1}{\sqrt{\varepsilon_0\mu_0(1+k)^2}}
=\frac{c}{1+k}.
$$

This result depends only on the existence of an in-phase electromagnetic
response with amplitude ratio $k$. It does not depend on the physical origin
of that response.

### Two Physical Realizations

**Linear dielectric.** In a transparent linear dielectric, $\mathbf E_2$ is the
electromagnetic field of the medium's polarization response, and the amplitude
ratio is the electric susceptibility, $k=\chi_e$ (analogously $\chi_m$ for the
magnetic response). The standard reduced-speed formula $c/n$ follows with
$n=\sqrt{(1+\chi_e)(1+\chi_m)}$.

**Mach-Zehnder recombination.** At the recombination point of a Mach-Zehnder
interferometer, $\mathbf E_2$ is the second arm beam. Both arms originate from
the same coherent source, travel equal paths, and arrive in phase at a bright
point. Each beam is, from the other's perspective, a full-amplitude in-phase
electromagnetic response. At full constructive interference
$\mathbf E_2=\mathbf E_1$, so $k=1$ without further substitution, and

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

The physical realizations differ — medium polarization versus free-propagating
beam — but the mathematical structure, and therefore the predicted propagation
speed, is identical. The dielectric result is not transferred by analogy; it
applies directly, because the mechanism is the same.

### Why the Split Phase Is Different {#sec:split}

The split and recombination use the same physical element (a 50/50 beam
splitter) but are not the same operation.

The split takes one beam and produces two equal beams from it. Its purpose is
to prepare coherent arm beams; no loaded interference fringe is formed.

Recombination takes two coherent equal beams and concentrates them into a
single signal distributed across two output channels. The bright channel
receives the constructive-interference fringe; the dark channel receives
nothing. Together they account for the full input energy — the fringe profile
$\cos^2+\sin^2=1$ sums to unity.

The dielectric loading question belongs to recombination, where two in-phase
equal beams combine, not to the split.

---

## Proposed Experiments

### The Two Readings

Each arm carries amplitude $E_0$ (energy density $u$). At recombination the
two coherent equal beams combine: the bright fringe has amplitude $2E_0$ and
energy density $4u$; the dark fringe has $0$. The fringe profile
$\cos^2+\sin^2=1$ distributes the full input energy across the two output
channels.

The dielectric loading applies to the combined field at the bright fringe.
With $k=1$ the dielectric result gives $c_{\mathrm{eff}}=c/2$ (see
@sec:energy-flux for the full energy and routing accounting).

The two readings differ in the phase velocity assigned to the bright fringe:

- ordinary output reading: $v_{\mathrm{bright}}=c$
- loaded-fringe reading: $v_{\mathrm{bright}}=c/2$

Two experiments can probe this phase velocity: refraction at a glass boundary
(geometric) and time-of-flight along a propagation path (temporal). Both
access the same underlying wavevector magnitude
$|k|=n_{\mathrm{eff}}\,\omega/c$ in the overlap region; they are not
independent confirmations but complementary observation channels.

### Refraction Test

The simplest test to discriminate the two readings is geometric. Snell's law at a boundary
between two media,

$$
n_1\sin\theta_i=n_2\sin\theta_r,
$$

is tangential-wavevector conservation: $|k|_{\mathrm{tangential}}$ is preserved
at the boundary, and $|k|=n\,\omega/c$. The refraction angle therefore reads
off the wavevector magnitude of the incident wave. The testable content of the
$c_{\mathrm{eff}}=c/2$ claim is that the combined field at the bright fringe
carries $|k|=2\omega/c$ in the overlap region, which at a boundary with glass
of index $n_g$ bends the beam to

$$
\sin\theta_r=\frac{2}{n_g}\sin\theta_i,
$$

twice the ordinary prediction.

**Setup.** Arrange the Mach-Zehnder so the two arm beams are collinear at the
recombiner output. Isolate one bright fringe with an aperture and let it
propagate toward a glass slab ($n_g\approx 1.5$) at oblique incidence $\theta_i$.
A reference beam taken directly from the laser is sent to the same slab at the
same $\theta_i$ for standard-refraction comparison.

The two arm beams remain spatially coincident within the apertured beam, so
each is still the in-phase response to the other and the dielectric loading
argument persists as long as they propagate together.

**Predictions.**

- *Ordinary reading* ($n_{\mathrm{eff}}=1$): standard refraction, identical to
  the reference, $\sin\theta_r=\sin\theta_i/n_g$.
- *Loaded-fringe reading* ($n_{\mathrm{eff}}=2$):
  $\sin\theta_r=(2/n_g)\sin\theta_i=(4/3)\sin\theta_i$.

For the loaded reading a critical angle appears at

$$
\sin\theta_c=\frac{n_g}{n_{\mathrm{eff}}}=0.75,
\qquad
\theta_c\approx 48.6^\circ.
$$

Above that incidence angle the loaded reading predicts total internal
reflection — no transmitted beam — while the ordinary reading still predicts
standard transmission.

At $\theta_i\gtrsim 49^\circ$ the experiment reduces to a binary discriminator:
either the bright fringe transmits into the glass or it does not. No timing
measurement is required.

### Time-of-Flight Test

If the refraction test is positive, a direct temporal confirmation is to
propagate the fringe and measure its group delay.

Use a coherent source, modulate it, split it into two arms, and recombine the
arms so they form stable fringes. Then:

1. isolate one bright interference fringe with an aperture
2. propagate that selected fringe over distance $L$
3. propagate a matched reference beam over the same distance
4. compare delay slopes $d\tau/dL$

The ordinary reading predicts equal slopes. The loaded-fringe reading predicts
a larger slope for the bright fringe.

For the equal-beam limit,

$$
\tau_{\mathrm{bright}}-\tau_{\mathrm{ref}}\approx \frac{L}{c}.
$$

So at $1\,\mathrm{m}$ the extra delay is about $3.34\,\mathrm{ns}$, and at
$10\,\mathrm{m}$ it is about $33.4\,\mathrm{ns}$.

---

## Discussion: Energy and Flux Accounting {#sec:energy-flux}

The dielectric argument above establishes $c_{\mathrm{eff}}=c/2$ from the
loading structure alone. The following energy and flux calculations are
consistency checks, not the primary argument.

Throughout this document $u$ denotes energy density (J/m³), not intensity
(W/m²); the two are related by $I=u\,v$ where $v$ is the propagation speed,
and they differ between the two readings.

**Energy density at the bright center.** With $k=1$ and arm amplitude $E_0$
(energy density $u$),

$$
\mathbf E_{\mathrm{tot}}=2E_0,
\qquad
\mathbf H_{\mathrm{tot}}=2H_0,
$$

and the instantaneous energy density is

$$
u_{\mathrm{tot}}=4u.
$$

This is twice the input laser energy density $2u$ and four times each arm's
energy density $u$. Across the fringe profile,

$$
u(x)=4u\cos^2\!\left(\frac{\Delta\phi(x)}{2}\right),
$$

averaging to $2u$ over a full fringe period. The dark fringe carries $0$, so
the spatial redistribution accounts for the full input energy.

**Instantaneous derivation.** No time averaging is needed. At a full
constructive-interference point, $\mathbf E_1(t)=\mathbf E_2(t)=E_0(t)$ and
$\mathbf B_1(t)=\mathbf B_2(t)=B_0(t)$, so
$\mathbf E_{\mathrm{tot}}(t)=2E_0(t)$, $\mathbf B_{\mathrm{tot}}(t)=2B_0(t)$, and

$$
u_{\mathrm{tot}}(t)
=
\frac{\varepsilon_0}{2}\lvert \mathbf E_{\mathrm{tot}}(t)\rvert^2
+
\frac{1}{2\mu_0}\lvert \mathbf B_{\mathrm{tot}}(t)\rvert^2
=4u.
$$

The factor of four is instantaneous and exact: amplitude doubles, energy
density quadruples.

**Output routing.** The recombiner maps the overlap into two output spatial
modes. For a lossless 50/50 recombiner,

$$
\mathbf E_+=\frac{\mathbf E_1+\mathbf E_2}{\sqrt 2}=\sqrt{2}\,E_0,
\qquad
\mathbf E_-=\frac{\mathbf E_1-\mathbf E_2}{\sqrt 2}=0,
$$

and likewise for the magnetic fields. The $1/\sqrt 2$ routing factor, combined
with the $1/\sqrt 2$ that already reduced the arm amplitudes at the initial
split, returns the full input energy to the bright port:

$$
u_+=2u,
\qquad
u_-=0.
$$

The ordinary reading starts from this $2u$ output and finds no anomalous
refraction or delay. The loaded-fringe reading starts from the $4u$ raw
overlap and predicts $c/2$. These energy-accounting relations are consistent
with both readings; they do not by themselves decide which propagation speed
is physical. That discrimination is what the refraction and time-of-flight
experiments provide.

---

## Possible Applications (if confirmed)

If the loaded-fringe reading is confirmed, the relative phase between the two
arm beams becomes a continuous control parameter for the refraction behavior
at a glass boundary. Three distinct regimes emerge, all reachable at the same
fixed incidence angle $\theta_i\gtrsim\theta_c$ by tuning phase alone.

1. **No coherent loading** — arms in quadrature ($\Delta\phi=\pi/2$) or one
   arm blocked. The in-phase response vanishes, so $k_{\mathrm{eff}}=0$ and
   $n_{\mathrm{eff}}=1$. The output refracts at the standard Snell angle,
   identical to a reference beam.

2. **Partial loading** — intermediate phase ($0<\Delta\phi<\pi/2$). The
   in-phase response is partial, so $0<k_{\mathrm{eff}}<1$ and
   $1<n_{\mathrm{eff}}<2$. The refraction angle tracks the phase continuously.

3. **Full in-phase loading** — arms in phase ($\Delta\phi=0$), $k=1$,
   $n_{\mathrm{eff}}=2$. For $\theta_i>\theta_c\approx 48.6^\circ$ the boundary
   rejects the bright fringe into total internal reflection. An evanescent
   wave penetrates a sub-wavelength depth into the glass, available for
   frustrated-TIR coupling at a second nearby interface.

A single glass surface, controlled by a single quantity (relative phase),
therefore provides three complementary device primitives:

- **a binary optical switch** (transmission ↔ TIR) with no carrier injection,
  thermal control, or moving parts — only phase
- **a continuous beam-steerer** with refraction angle tracking phase
- **a phase-gated evanescent coupler** for waveguide interconnect near $\theta_c$

Each is linear, fast, low-power, and compatible with standard coherent-light
platforms. The shared physics is that the glass boundary senses the phase
velocity of the combined field, and that phase velocity is tunable through
coherent superposition. Applications span optical computing, photonic signal
routing, and coherent interconnect.

---

## Conclusion

The experiments test which object should be treated as the propagating fringe
after recombination:

- the ordinary normalized output mode, with $n_{\mathrm{eff}}=1$
- or the isolated raw constructive-interference fringe, with $n_{\mathrm{eff}}=2$

For the refraction test, if the bright fringe transmits into the glass at
$\theta_i\gtrsim 49^\circ$ together with the reference, the ordinary reading wins.
If the bright fringe undergoes total internal reflection while the reference
still transmits, the loaded-fringe reading is supported.

For the time-of-flight test, if the measured delay matches the reference, the
ordinary reading wins. If the delay approaches the $c/2$ prediction in the
equal-beam limit, the loaded-fringe reading is supported.
