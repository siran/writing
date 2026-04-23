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

The input laser carries intensity $2u$. The first beam splitter produces two
arm beams of amplitude $E_0$ and intensity $u$ each. At recombination, the two
equal arm amplitudes add in phase: $E_0 + E_0 = 2E_0$, intensity $4u$ at the
bright fringe. Each arm is the equal-amplitude in-phase response to the other
($k=1$), so

$$
c_{\mathrm{eff}}=\frac{c}{2}.
$$

The recombiner routes this $4u$ overlap into the output ports: bright port
carries $2u$, dark port $0$, recovering the input laser energy. The ordinary
reading reports a $2u$ output beam propagating at $c$ and predicts no delay.
The experiment is a direct time-of-flight test between these two readings.

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

The input laser carries intensity $2u$. After the first beam splitter, each
arm has amplitude $E_0$ and intensity $u$, where $u\propto E_0^2$. At
recombination the two equal arms arrive in phase; each is the equal-amplitude
in-phase response to the other, so $k=1$ without any further substitution.

Writing the response amplitude as $k$ times the first arm,

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

At the bright center, with $k=1$ and arm amplitude $E_0$ (intensity $u$),

$$
\mathbf E_{\mathrm{tot}}=2E_0,
\qquad
\mathbf H_{\mathrm{tot}}=2H_0,
$$

and the instantaneous energy density is

$$
u_{\mathrm{tot}}=4u.
$$

This is twice the input laser intensity $2u$ and four times each arm intensity
$u$. Energy is conserved: the dark fringe carries $0$, so the spatial
redistribution accounts for the full input. Across the fringe profile,

$$
u(x)=4u\cos^2\!\left(\frac{\Delta\phi(x)}{2}\right),
$$

averaging to $2u$ over a full fringe period, as required.

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

Each arm carries amplitude $E_0$ (intensity $u$). The raw overlap at the
recombination region is

$$
\mathbf E_{\mathrm{overlap}}=\mathbf E_1+\mathbf E_2=2E_0,
\qquad
u_{\mathrm{overlap}}=4u.
$$

This is the loaded object — the field that the dielectric mechanism acts on.

The recombiner then routes the overlap into two output spatial modes. For a
lossless 50/50 recombiner the output fields are

$$
\mathbf E_+=\frac{\mathbf E_1+\mathbf E_2}{\sqrt 2}=\sqrt{2}\,E_0,
\qquad
\mathbf E_-=\frac{\mathbf E_1-\mathbf E_2}{\sqrt 2}=0,
$$

and likewise for the magnetic fields. The $1/\sqrt{2}$ here is the recombiner's
routing factor, distinct from the $1/\sqrt{2}$ that already reduced the arm
amplitudes at the initial split. Together they return the full input laser
energy to the bright port:

$$
u_+=2u,
\qquad
u_-=0.
$$

The ordinary reading starts from the $2u$ output beam and finds no anomalous
delay. The loaded-fringe reading starts from the $4u$ raw overlap and predicts
$c/2$. The experimental fork is:

- ordinary output reading: $v_{\mathrm{bright}}=c$, no extra delay
- loaded raw-overlap reading: $v_{\mathrm{bright}}=c/2$, extra delay $L/c$ over distance $L$

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

No time averaging is needed. Each arm beam has amplitude $E_0$ and intensity
$u$. At a full constructive-interference point,

$$
\mathbf E_1(t)=E_0(t),
\qquad
\mathbf E_2(t)=E_0(t),
\qquad
\mathbf B_1(t)=B_0(t),
\qquad
\mathbf B_2(t)=B_0(t).
$$

The total field is

$$
\mathbf E_{\mathrm{tot}}(t)=2E_0(t),
\qquad
\mathbf B_{\mathrm{tot}}(t)=2B_0(t).
$$

The instantaneous electromagnetic energy density is

$$
u_{\mathrm{tot}}(t)
=
\frac{\varepsilon_0}{2}\lvert \mathbf E_{\mathrm{tot}}(t)\rvert^2
+
\frac{1}{2\mu_0}\lvert \mathbf B_{\mathrm{tot}}(t)\rvert^2
= 4u.
$$

The factor of four is instantaneous and exact: amplitude doubles, intensity
quadruples. The input laser was $2u$; the bright fringe peak is $4u$; the dark
fringe is $0$; the spatial average is $2u$. Energy is conserved.

### Coherent-Response Form

Each arm has amplitude $E_0$ (intensity $u$). The second arm is the response
sector with $k=1$:

$$
\mathbf E_2=\mathbf E_1=E_0,
\qquad
\mathbf B_2=\mathbf B_1=B_0.
$$

Total field:

$$
\mathbf E_{\mathrm{tot}}=(1+k)E_0=2E_0,
\qquad
u_{\mathrm{tot}}=(1+k)^2u=4u.
$$

The dielectric loading gives

$$
c_{\mathrm{eff}}=\frac{c}{1+k}=\frac{c}{2}.
$$

The $2u$ laser, split to $u$ per arm, recombines to a $4u$ bright fringe
propagating at $c/2$. The recombiner routes that fringe to a $2u$ output port
at $c$. The experiment distinguishes which propagation speed is physical.

---

## What the Experiment Decides

This experiment tests which object should be treated as the propagating fringe
after recombination:

- the ordinary normalized output mode
- or the isolated raw constructive-interference fringe

If the measured delay matches the reference, the ordinary reading wins. If the
measured delay approaches the $c/2$ prediction in the equal-beam limit, the
loaded-fringe reading is supported.
