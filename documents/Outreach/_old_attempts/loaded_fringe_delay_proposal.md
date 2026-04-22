% Experimental Proposal — Longitudinal Delay of an Isolated Loaded Interference Branch
% An M. Rodriguez
% 2026-04-21

# Experimental Proposal — Longitudinal Delay of an Isolated Loaded Interference Branch

## Abstract

This proposal tests whether a spatially isolated bright branch of a coherent interference pattern propagates with the standard vacuum speed $c$, or whether its effective longitudinal advance is reduced by coherent loading.

Two equal coherent beams are recombined with small crossing angle. Standard interference gives a local raw overlap density

$$
u_{\mathrm{raw}}(x)=4u_0\cos^2\!\left(\frac{qx}{2}\right),
$$

whose bright centers reach

$$
u_{\mathrm{raw,peak}}=4u_0.
$$

The total two-beam forward flux budget is

$$
J_{\mathrm{in},z}=2u_0c\cos\theta.
$$

The standard normalized output-channel reading assigns the bright output density $2u_0$ at a maximum and predicts no anomalous delay. The tested alternative is the loaded-branch reading: an isolated raw bright branch carries the same available two-beam flux on a higher local density. Then its effective longitudinal advance is

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

At a bright center this gives

$$
v_{\mathrm{peak}}
=
\frac{2u_0c\cos\theta}{4u_0}
=
\frac{c\cos\theta}{2}.
$$

For nearly collinear beams,

$$
v_{\mathrm{peak}}\approx \frac{c}{2}.
$$

The experiment therefore compares the measured delay of an isolated bright stripe against a reference beam over the same distance. The standard prediction is

$$
v_{\mathrm{stripe}}=v_{\mathrm{ref}},
$$

while the loaded-branch prediction is

$$
v_{\mathrm{stripe}}\approx \frac{v_{\mathrm{ref}}}{2}.
$$

The result is directly falsifiable.

---

# 1. Goal

Measure the longitudinal delay of the center of an isolated bright interference branch.

The experimental question is:

$$
\boxed{
\text{Does an isolated bright stripe propagate as a standard normalized optical output, or as a loaded raw-overlap branch?}
}
$$

The standard-optics expectation is

$$
v_{\mathrm{fringe}}=v_{\mathrm{ref}}
$$

within experimental error.

The loaded-branch expectation is

$$
v_{\mathrm{fringe}}<v_{\mathrm{ref}},
$$

with the bright-center prediction

$$
v_{\mathrm{fringe}}\approx \frac{c}{2}
$$

for nearly collinear equal beams in vacuum.

---

# 2. Definitions

Let each incoming coherent beam have amplitude-like field

$$
f_j=A_j e^{i\phi_j},
$$

with single-beam energy density

$$
u_0:=|A_j|^2.
$$

For equal beams,

$$
|A_1|=|A_2|=:A,
\qquad
u_0=|A|^2.
$$

Let the relative phase be

$$
\Delta\phi=\phi_1-\phi_2.
$$

The raw coherent overlap field is

$$
f_{\mathrm{raw}}=f_1+f_2.
$$

Its local density is

$$
u_{\mathrm{raw}}
=
|f_{\mathrm{raw}}|^2.
$$

The local energy flux budget along a chosen longitudinal direction is denoted by $J_z$. For a propagating single beam in vacuum,

$$
J_0=u_0c.
$$

If the beam crosses the $z$-axis at angle $\theta$, its longitudinal projected flux is

$$
J_{0,z}=u_0c\cos\theta.
$$

For two equal beams symmetrically crossing about $z$,

$$
J_{\mathrm{in},z}=2u_0c\cos\theta.
$$

---

# 3. Standard Coherent Overlap

Take two equal monochromatic contributions crossing symmetrically about the $z$-axis with half-angle $\theta$:

$$
f_1(x,z,t)
=
A e^{i(kx\sin\theta+kz\cos\theta-\omega t)},
$$

$$
f_2(x,z,t)
=
A e^{i(-kx\sin\theta+kz\cos\theta-\omega t)}.
$$

Define

$$
q:=2k\sin\theta.
$$

Then

$$
f_{\mathrm{raw}}
=
f_1+f_2.
$$

Factor out the common longitudinal phase:

$$
f_{\mathrm{raw}}(x,z,t)
=
A e^{i(kz\cos\theta-\omega t)}
\left(
e^{ikx\sin\theta}+e^{-ikx\sin\theta}
\right).
$$

Using

$$
e^{ia}+e^{-ia}=2\cos a,
$$

we get

$$
f_{\mathrm{raw}}(x,z,t)
=
2A\cos(kx\sin\theta)
e^{i(kz\cos\theta-\omega t)}.
$$

Since

$$
kx\sin\theta=\frac{qx}{2},
$$

the raw density is

$$
u_{\mathrm{raw}}(x)
=
|f_{\mathrm{raw}}|^2
=
4|A|^2\cos^2\!\left(\frac{qx}{2}\right).
$$

Therefore

$$
\boxed{
u_{\mathrm{raw}}(x)
=
4u_0\cos^2\!\left(\frac{qx}{2}\right)
}
$$

and

$$
0\le u_{\mathrm{raw}}(x)\le 4u_0.
$$

Bright centers occur at

$$
\frac{qx}{2}=n\pi,
\qquad
n\in\mathbb Z,
$$

so

$$
x_n=\frac{2\pi n}{q}.
$$

At those points,

$$
u_{\mathrm{raw}}(x_n)=4u_0.
$$

Nodes occur at

$$
\frac{qx}{2}=\frac{(2n+1)\pi}{2},
$$

where

$$
u_{\mathrm{raw}}=0.
$$

The fringe period is

$$
\Lambda=\frac{2\pi}{q}
=
\frac{\lambda}{2\sin\theta}.
$$

For small $\theta$,

$$
\Lambda\approx \frac{\lambda}{2\theta}.
$$

---

# 4. Mean Density Budget

Over one fringe period,

$$
\langle u_{\mathrm{raw}}\rangle
=
\frac{1}{\Lambda}\int_0^\Lambda
4u_0\cos^2\!\left(\frac{qx}{2}\right)\,dx.
$$

Let

$$
y=\frac{qx}{2},
\qquad
dx=\frac{2}{q}dy.
$$

As $x$ runs from $0$ to $\Lambda=2\pi/q$, $y$ runs from $0$ to $\pi$. Therefore

$$
\langle u_{\mathrm{raw}}\rangle
=
\frac{1}{\Lambda}
4u_0
\frac{2}{q}
\int_0^\pi\cos^2y\,dy.
$$

Since

$$
\int_0^\pi\cos^2y\,dy=\frac{\pi}{2},
$$

we obtain

$$
\langle u_{\mathrm{raw}}\rangle
=
\frac{1}{\Lambda}
4u_0
\frac{2}{q}
\frac{\pi}{2}
=
\frac{1}{\Lambda}
\frac{4\pi u_0}{q}.
$$

Using

$$
\Lambda=\frac{2\pi}{q},
$$

this gives

$$
\boxed{
\langle u_{\mathrm{raw}}\rangle=2u_0.
}
$$

Thus the full fringe period recovers the two-beam density budget:

$$
u_0+u_0=2u_0.
$$

The density is not uniform. Some regions satisfy

$$
u_{\mathrm{raw}}>3u_0,
$$

while others satisfy

$$
u_{\mathrm{raw}}<u_0.
$$

Total energy is conserved over the full pattern, but the local density is redistributed.

---

# 5. Standard Normalized Output-Channel Reading

At a lossless 50/50 recombiner, the normalized output modes are

$$
f_+(x)=\frac{f_1(x)+f_2(x)}{\sqrt 2},
\qquad
f_-(x)=\frac{f_1(x)-f_2(x)}{\sqrt 2}.
$$

For equal inputs,

$$
|f_1|^2=|f_2|^2=u_0.
$$

Then

$$
u_+(x)=|f_+(x)|^2
=
\frac{1}{2}|f_1+f_2|^2
=
2u_0\cos^2\!\left(\frac{qx}{2}\right),
$$

and

$$
u_-(x)=|f_-(x)|^2
=
\frac{1}{2}|f_1-f_2|^2
=
2u_0\sin^2\!\left(\frac{qx}{2}\right).
$$

Therefore

$$
\boxed{
u_+(x)+u_-(x)=2u_0
}
$$

pointwise.

At a bright center of the $+$ output,

$$
u_+=2u_0,
\qquad
u_-=0.
$$

In the standard normalized-channel reading, the bright output carries the full two-beam budget with density $2u_0$, so it can propagate at the usual longitudinal projected speed

$$
v=c\cos\theta
$$

without conservation conflict.

Thus standard optics predicts no extra longitudinal delay of the selected bright stripe beyond ordinary propagation and aperture effects.

---

# 6. Raw Loaded-Branch Reading

The tested alternative is not the normalized-channel reading.

The tested alternative is:

$$
\boxed{
\text{An isolated bright stripe is a surviving raw-overlap branch with density }u_{\mathrm{raw}}.
}
$$

On this reading, a bright-center branch has

$$
u_{\mathrm{raw,peak}}=4u_0.
$$

But the available two-beam longitudinal flux remains

$$
J_{\mathrm{in},z}=2u_0c\cos\theta.
$$

If the bright branch were assigned speed $c\cos\theta$, its local throughput would be

$$
J_{\mathrm{bright,naive}}
=
u_{\mathrm{raw,peak}}c\cos\theta
=
4u_0c\cos\theta.
$$

This is twice the available two-beam longitudinal flux:

$$
4u_0c\cos\theta
=
2J_{\mathrm{in},z}.
$$

Therefore, under the raw loaded-branch reading, conservation requires a reduced effective advance:

$$
J_{\mathrm{in},z}
=
u_{\mathrm{raw,peak}}v_{\mathrm{peak}}.
$$

Solving,

$$
v_{\mathrm{peak}}
=
\frac{J_{\mathrm{in},z}}{u_{\mathrm{raw,peak}}}
=
\frac{2u_0c\cos\theta}{4u_0}
=
\frac{c\cos\theta}{2}.
$$

Thus

$$
\boxed{
v_{\mathrm{peak}}=\frac{c\cos\theta}{2}
}
$$

and, for $\theta\ll 1$,

$$
\boxed{
v_{\mathrm{peak}}\approx \frac c2.
}
$$

This is the central experimental prediction.

---

# 7. Dielectric-Style Derivation of the Loaded-Branch Law

This section derives the same result using the dielectric analogy, read inside the energy-flow framework.

Matter is standing electromagnetic organization. Dielectric slowing is therefore field-field interaction in a stable organized background. The fringe-delay test asks whether the same loading rule appears in the simplest unbound case: two coherent light fields overlapping in phase.

## 7.1 Ordinary Dielectric Form

In a dielectric,

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P.
$$

For a linear response,

$$
\mathbf P=\varepsilon_0\chi_e\mathbf E.
$$

Therefore

$$
\mathbf D
=
\varepsilon_0(1+\chi_e)\mathbf E
=
\varepsilon_{\mathrm{eff}}\mathbf E,
$$

where

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+\chi_e).
$$

If the magnetic sector is similarly loaded,

$$
\mu_{\mathrm{eff}}=\mu_0(1+\chi_m),
$$

then the propagation speed is

$$
v
=
\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}.
$$

If the two sectors are symmetrically loaded,

$$
\chi_e=\chi_m=k,
$$

then

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+k),
\qquad
\mu_{\mathrm{eff}}=\mu_0(1+k).
$$

Hence

$$
v
=
\frac{1}
{\sqrt{\varepsilon_0\mu_0(1+k)^2}}
=
\frac{c}{1+k}.
$$

Thus

$$
\boxed{
v_{\mathrm{eff}}=\frac{c}{1+k}.
}
$$

## 7.2 Coherent Response Field

Let a primary branch have field amplitude

$$
E_1.
$$

Let the coherent response field be proportional:

$$
E_2=kE_1,
\qquad
k\ge 0.
$$

Then the joined field is

$$
E_{\mathrm{tot}}
=
E_1+E_2
=
(1+k)E_1.
$$

Because the observable density is quadratic,

$$
u\propto E^2.
$$

Therefore

$$
u_{\mathrm{tot}}
\propto
E_{\mathrm{tot}}^2
=
(1+k)^2E_1^2.
$$

If

$$
u_1\propto E_1^2,
$$

then

$$
\boxed{
u_{\mathrm{tot}}=(1+k)^2u_1.
}
$$

For equal coherent contribution,

$$
k=1,
$$

so

$$
E_{\mathrm{tot}}=2E_1,
$$

and

$$
u_{\mathrm{tot}}=4u_1.
$$

The same amplitude-loading factor is

$$
n_{\mathrm{eff}}=1+k.
$$

Thus

$$
u_{\mathrm{tot}}=n_{\mathrm{eff}}^2u_1,
$$

and

$$
v_{\mathrm{eff}}=\frac{c}{n_{\mathrm{eff}}}.
$$

For $k=1$,

$$
n_{\mathrm{eff}}=2,
$$

so

$$
\boxed{
v_{\mathrm{eff}}=\frac c2.
}
$$

## 7.3 Flux Form of the Same Result

The same law can be written directly as

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

For one branch,

$$
J_1=u_1c.
$$

For two equal branches in phase, the available total flux is

$$
J_{\mathrm{available}}=2u_1c.
$$

The joined raw density is

$$
u_{\mathrm{joined}}=4u_1.
$$

Therefore

$$
v_{\mathrm{eff}}
=
\frac{J_{\mathrm{available}}}{u_{\mathrm{joined}}}
=
\frac{2u_1c}{4u_1}
=
\frac c2.
$$

This is the same result as the symmetric dielectric loading derivation.

The general proportional-response result is

$$
f_2=kf_1,
$$

so

$$
f_{\mathrm{tot}}=(1+k)f_1,
$$

$$
u_{\mathrm{tot}}=(1+k)^2u_1,
$$

and

$$
\boxed{
v_{\mathrm{eff}}=\frac{c}{1+k}.
}
$$

---

# 8. Spatially Varying Effective Advance Across a Fringe

For the raw overlap fringe,

$$
u_{\mathrm{raw}}(x)
=
4u_0\cos^2\!\left(\frac{qx}{2}\right).
$$

The available two-beam longitudinal flux is

$$
J_{\mathrm{in},z}=2u_0c\cos\theta.
$$

Applying the loaded-branch law locally gives

$$
v_{\mathrm{eff}}(x)
=
\frac{J_{\mathrm{in},z}}{u_{\mathrm{raw}}(x)}.
$$

Therefore

$$
v_{\mathrm{eff}}(x)
=
\frac{2u_0c\cos\theta}
{4u_0\cos^2(qx/2)}
=
\frac{c\cos\theta}
{2\cos^2(qx/2)}.
$$

So

$$
\boxed{
v_{\mathrm{eff}}(x)
=
\frac{c\cos\theta}
{2\cos^2(qx/2)}
}
$$

on open bright intervals where the raw branch survives.

At a bright center,

$$
\cos^2(qx/2)=1,
$$

so

$$
v_{\mathrm{eff,peak}}=\frac{c\cos\theta}{2}.
$$

At points where

$$
\cos^2(qx/2)=\frac12,
$$

the density equals the mean:

$$
u_{\mathrm{raw}}=2u_0,
$$

and

$$
v_{\mathrm{eff}}=c\cos\theta.
$$

At nodes,

$$
u_{\mathrm{raw}}=0,
$$

so the quotient is not interpreted as an infinite speed. Instead, the forward raw branch is absent there. Nodes are not surviving forward loaded branches.

Thus the loaded-branch law is meaningful only on selected nonzero bright intervals.

---

# 9. Exact Bright-Band Average

A real detector or slit samples a finite band around a bright center. Let the selected band be

$$
|x-x_n|\le a/2.
$$

Set

$$
\xi=x-x_n.
$$

Because $x_n$ is a bright center,

$$
u_{\mathrm{raw}}(\xi)
=
4u_0\cos^2\!\left(\frac{q\xi}{2}\right).
$$

The band-averaged density is

$$
\bar u_a
=
\frac{1}{a}\int_{-a/2}^{a/2}
4u_0\cos^2\!\left(\frac{q\xi}{2}\right)d\xi.
$$

Use

$$
\cos^2 y=\frac{1+\cos 2y}{2}.
$$

Here

$$
2y=q\xi.
$$

Thus

$$
\bar u_a
=
\frac{4u_0}{a}
\int_{-a/2}^{a/2}
\frac{1+\cos(q\xi)}{2}d\xi.
$$

So

$$
\bar u_a
=
\frac{2u_0}{a}
\left[
\int_{-a/2}^{a/2}1\,d\xi
+
\int_{-a/2}^{a/2}\cos(q\xi)\,d\xi
\right].
$$

The first integral is

$$
\int_{-a/2}^{a/2}1\,d\xi=a.
$$

The second is

$$
\int_{-a/2}^{a/2}\cos(q\xi)d\xi
=
\frac{2}{q}\sin\!\left(\frac{qa}{2}\right).
$$

Therefore

$$
\boxed{
\bar u_a
=
2u_0
\left[
1+
\frac{2}{qa}\sin\!\left(\frac{qa}{2}\right)
\right].
}
$$

The predicted band velocity is

$$
v_a
=
\frac{J_{\mathrm{in},z}}{\bar u_a}
=
\frac{2u_0c\cos\theta}
{
2u_0
\left[
1+
\frac{2}{qa}\sin(qa/2)
\right]
}.
$$

So

$$
\boxed{
v_a
=
\frac{c\cos\theta}
{
1+
\frac{2}{qa}\sin(qa/2)
}
}
$$

for a centered selected bright band of width $a$.

In the narrow-band limit,

$$
qa\ll 1,
$$

we have

$$
\sin(qa/2)\approx qa/2.
$$

Thus

$$
\frac{2}{qa}\sin(qa/2)\approx 1,
$$

and

$$
v_a\approx \frac{c\cos\theta}{2}.
$$

As the band widens to include a full bright-to-dark half-cell, the averaged density falls toward the two-beam mean and the predicted effective speed rises toward the standard mean value.

---

# 10. Practical Fringe Scale

The fringe period is

$$
\Lambda=\frac{\lambda}{2\sin\theta}.
$$

For a HeNe laser,

$$
\lambda=632.8\ \mathrm{nm}.
$$

If the half-angle is

$$
\theta=0.1\ \mathrm{mrad},
$$

then the total crossing angle is $0.2\ \mathrm{mrad}$ and

$$
\Lambda
\approx
\frac{632.8\times10^{-9}}
{2\times10^{-4}}
=
3.164\times10^{-3}\ \mathrm{m}.
$$

So

$$
\Lambda\approx 3.16\ \mathrm{mm}.
$$

The region satisfying

$$
u_{\mathrm{raw}}>3u_0
$$

obeys

$$
4u_0\cos^2\!\left(\frac{q\xi}{2}\right)>3u_0.
$$

Canceling $u_0$,

$$
\cos^2\!\left(\frac{q\xi}{2}\right)>\frac34.
$$

Thus

$$
\left|\frac{q\xi}{2}\right|<\frac{\pi}{6}.
$$

So

$$
|\xi|<\frac{\pi}{3q}.
$$

The full above-$3u_0$ width is therefore

$$
w_{>3u_0}
=
\frac{2\pi}{3q}
=
\frac{\Lambda}{3}.
$$

For $\Lambda\approx 3.16\ \mathrm{mm}$,

$$
w_{>3u_0}\approx 1.05\ \mathrm{mm}.
$$

A practical slit width is therefore

$$
a=0.25\ \mathrm{mm}
\quad\text{to}\quad
a=0.50\ \mathrm{mm},
$$

centered on a bright maximum.

---

# 11. Experimental Design

## 11.1 Apparatus

Minimum requirements:

- stable coherent laser source,
- amplitude modulation source,
- Mach-Zehnder or equivalent two-beam interferometer,
- controlled small recombination angle,
- stable straight fringes,
- spatial filter or slit selecting one bright ridge,
- reference beam path,
- equal downstream propagation length $L$ for reference and selected stripe,
- fast photodiodes,
- oscilloscope, lock-in amplifier, or phase-delay measurement system,
- variable path length or multiple known path lengths.

## 11.2 Procedure

1. Generate a coherent laser beam.
2. Apply sinusoidal amplitude modulation at angular frequency $\Omega$.
3. Split the beam into two equal arms.
4. Recombine the arms at small symmetric angle $\theta$.
5. Produce stable straight fringes.
6. Select the center of one bright fringe using a slit or spatial filter.
7. Allow the selected bright stripe to propagate over known distance $L$.
8. In parallel, propagate a reference beam over the same distance.
9. Detect both signals using matched photodiodes.
10. Measure the modulation phase delay of each channel relative to the common modulation source.
11. Repeat for several propagation lengths $L_i$.
12. Fit delay versus distance.

For each channel,

$$
\tau(L)=mL+b.
$$

Here $b$ is a fixed electronic and geometric offset. The slope is

$$
m=\frac{d\tau}{dL}.
$$

The measured speed is

$$
v=\frac{1}{m}.
$$

Thus

$$
v_{\mathrm{ref}}=\frac{1}{m_{\mathrm{ref}}},
\qquad
v_{\mathrm{stripe}}=\frac{1}{m_{\mathrm{stripe}}}.
$$

## 11.3 Predictions

Standard prediction:

$$
m_{\mathrm{stripe}}\approx m_{\mathrm{ref}},
$$

so

$$
v_{\mathrm{stripe}}\approx v_{\mathrm{ref}}.
$$

Loaded-branch prediction at a narrow bright center:

$$
v_{\mathrm{stripe}}\approx \frac{c\cos\theta}{2}.
$$

For small $\theta$,

$$
v_{\mathrm{stripe}}\approx \frac c2.
$$

Therefore

$$
m_{\mathrm{stripe}}\approx \frac{2}{c}
$$

while

$$
m_{\mathrm{ref}}\approx \frac{1}{c}.
$$

So

$$
\boxed{
m_{\mathrm{stripe}}\approx 2m_{\mathrm{ref}}.
}
$$

Equivalently, for equal propagation distance $L$,

$$
\boxed{
\tau_{\mathrm{stripe}}-\tau_{\mathrm{ref}}\approx \frac{L}{c}.
}
$$

For example, at

$$
L=1\ \mathrm{m},
$$

the predicted extra delay is

$$
\Delta\tau\approx \frac{1}{c}\approx 3.34\ \mathrm{ns}.
$$

At

$$
L=10\ \mathrm{m},
$$

the predicted extra delay is

$$
\Delta\tau\approx 33.4\ \mathrm{ns}.
$$

This is large enough to test with ordinary fast photodiodes and phase-sensitive electronics.

---

# 12. Controls

## 12.1 Reference Beam

The reference beam should have:

- the same carrier frequency,
- the same modulation frequency,
- the same optical components where possible,
- the same downstream length $L$,
- similar detector electronics.

## 12.2 Single-Beam Slit Control

Send only one beam through the same slit geometry, with no interference. The selected beam should propagate at the ordinary reference speed.

This control checks that the slit itself is not producing the predicted delay.

## 12.3 Off-Bright Sampling

Move the slit away from the bright center. The loaded-branch prediction varies with sampled density:

$$
v_a
=
\frac{J}{\bar u_a}.
$$

Thus lower-density bands should show smaller delay.

The standard prediction remains no density-dependent delay.

## 12.4 Fringe-Period Averaging

Open the aperture to collect an entire fringe period. The average density returns to

$$
\langle u\rangle=2u_0.
$$

The loaded-branch anomaly should disappear under full-period collection.

This distinguishes local branch loading from ordinary total-power conservation.

## 12.5 Power Scaling

The prediction depends on coherent loading ratio, not absolute power, in the proportional regime. Therefore reducing both beam powers equally should reduce signal amplitude but not change the predicted velocity ratio.

If the delay depends strongly on absolute optical power, thermal, detector, or nonlinear-medium effects must be suspected.

---

# 13. Interpretation of Outcomes

## 13.1 Null Result

If

$$
v_{\mathrm{stripe}}=v_{\mathrm{ref}}
$$

within experimental error, then the isolated stripe behaves as a standard propagated optical mode. The raw local $4u_0$ density does not act as a loaded branch with reduced effective advance.

This would support the normalized-output reading.

## 13.2 Positive Result

If

$$
v_{\mathrm{stripe}}\approx \frac{v_{\mathrm{ref}}}{2}
$$

for a narrow bright-center stripe, and if the effect tracks the sampled density as predicted, then the loaded-branch law is supported.

The result would indicate that coherent local density loading changes the effective longitudinal advance of a surviving branch.

## 13.3 Intermediate Result

If

$$
v_{\mathrm{ref}}>v_{\mathrm{stripe}}>\frac{v_{\mathrm{ref}}}{2},
$$

then the selected stripe may not remain a pure raw bright branch. Partial mixing, diffraction, finite aperture averaging, imperfect visibility, or incomplete branch isolation may be contributing.

In that case the measured velocity should be compared against the finite-band prediction

$$
v_a
=
\frac{c\cos\theta}
{
1+
\frac{2}{qa}\sin(qa/2)
}.
$$

---

# 14. Core Theoretical Fork

The full interference pattern conserves energy in both readings.

The disagreement is not about whether energy is conserved. It is about how a selected bright region transports energy.

## Standard Reading

The recombiner produces normalized output modes:

$$
u_+(x)+u_-(x)=2u_0.
$$

At a bright center,

$$
u_+=2u_0.
$$

No speed reduction is required.

## Loaded-Branch Reading

The isolated branch is identified with the raw overlap density:

$$
u_{\mathrm{raw,peak}}=4u_0.
$$

The available two-beam flux is

$$
J=2u_0c\cos\theta.
$$

Therefore

$$
v_{\mathrm{peak}}=\frac{J}{u_{\mathrm{raw,peak}}}
=
\frac{c\cos\theta}{2}.
$$

The experiment tests which reading describes the propagation of an isolated bright stripe.

---

# 15. Summary

The proposal establishes:

1. Two equal coherent beams produce the raw density profile

   $$
   u_{\mathrm{raw}}(x)=4u_0\cos^2\!\left(\frac{qx}{2}\right).
   $$

2. The full fringe average is

   $$
   \langle u_{\mathrm{raw}}\rangle=2u_0,
   $$

   so total energy is conserved over a full period.

3. Bright centers have

   $$
   u_{\mathrm{raw,peak}}=4u_0.
   $$

4. The two-beam longitudinal flux budget is

   $$
   J_{\mathrm{in},z}=2u_0c\cos\theta.
   $$

5. The loaded-branch law is

   $$
   v_{\mathrm{eff}}=\frac{J}{u}.
   $$

6. Therefore the bright-center prediction is

   $$
   v_{\mathrm{peak}}
   =
   \frac{2u_0c\cos\theta}{4u_0}
   =
   \frac{c\cos\theta}{2}.
   $$

7. The dielectric-style proportional response gives the same result:

   $$
   E_2=kE_1
   \Rightarrow
   E_{\mathrm{tot}}=(1+k)E_1
   \Rightarrow
   u_{\mathrm{tot}}=(1+k)^2u_1
   \Rightarrow
   v_{\mathrm{eff}}=\frac{c}{1+k}.
   $$

   For $k=1$,

   $$
   v_{\mathrm{eff}}=\frac c2.
   $$

8. A longitudinal delay measurement of an isolated bright stripe directly distinguishes the two models.

The decisive experimental signature is

$$
\boxed{
m_{\mathrm{stripe}}\approx 2m_{\mathrm{ref}}
}
$$

for a narrow bright-center stripe, where $m=d\tau/dL$ is the measured delay slope.

If observed, the result supports the loaded-branch interpretation of coherent energy flow. If not observed, the standard normalized-output reading is favored.

---

# Appendix A — Finite Band Prediction

For a centered slit of width $a$ around a bright maximum,

$$
\bar u_a
=
2u_0
\left[
1+
\frac{2}{qa}\sin\!\left(\frac{qa}{2}\right)
\right].
$$

Therefore

$$
v_a
=
\frac{2u_0c\cos\theta}{\bar u_a}.
$$

So

$$
\boxed{
v_a
=
\frac{c\cos\theta}
{
1+
\frac{2}{qa}\sin(qa/2)
}
}.
$$

Limits:

For $qa\ll 1$,

$$
v_a\to \frac{c\cos\theta}{2}.
$$

For wider averaging, the sampled density decreases and $v_a$ increases toward the mean-pattern value.

---

# Appendix B — Above-$3u_0$ Bright-Core Width

The above-$3u_0$ condition is

$$
4u_0\cos^2\!\left(\frac{q\xi}{2}\right)>3u_0.
$$

Thus

$$
\cos^2\!\left(\frac{q\xi}{2}\right)>\frac34.
$$

So

$$
\left|\frac{q\xi}{2}\right|<\frac{\pi}{6}.
$$

Therefore

$$
|\xi|<\frac{\pi}{3q}.
$$

The full width is

$$
w_{>3u_0}=\frac{2\pi}{3q}.
$$

Since

$$
\Lambda=\frac{2\pi}{q},
$$

we get

$$
\boxed{
w_{>3u_0}=\frac{\Lambda}{3}.
}
$$

For $\Lambda\approx 3.16\ \mathrm{mm}$,

$$
w_{>3u_0}\approx 1.05\ \mathrm{mm}.
$$

A slit width of

$$
0.25\ \mathrm{mm}\le a\le 0.50\ \mathrm{mm}
$$

therefore samples the high-density bright core while avoiding neighboring lower-density regions.

---

# Appendix C — Status of the Claim

The standard interference formulas alone prove the density pattern and the conserved average. They do not by themselves prove reduced speed.

The reduced speed follows from the additional loaded-branch transport law

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

This is the law tested by the experiment.

Thus the proposal is not merely a reinterpretation of a screen fringe. It is a direct time-of-flight test between two alternatives:

$$
\boxed{
\text{standard normalized output channel}
}
$$

versus

$$
\boxed{
\text{raw loaded branch with }v_{\mathrm{eff}}=J/u.
}
$$
