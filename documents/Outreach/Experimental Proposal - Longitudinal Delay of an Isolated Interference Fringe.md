---
title: Experimental Proposal - Longitudinal Delay of an Isolated Interference Fringe
date: 2026-04-16
---

# Experimental Proposal

## Goal

Measure whether the center of a bright interference fringe propagates with a
different longitudinal delay than one of the incident beams that forms it.


## Tested Hypothesis

For a single beam of density $u$ advancing longitudinally at speed $c$, the
flux is

$$
J_0 = u\,c.
$$

For two equal incident beams, the total incoming budget is

$$
J_{\mathrm{in}} = 2u\,c.
$$

The tested hypothesis is not that brightness alone slows propagation. It is
that coherent overlap can compress the same incoming transport budget into
fewer effective longitudinal channels. If the bright surviving channel recovers
local loading $4u$, then the same incoming budget gives

$$
c_{\mathrm{eff}}
=
\frac{J_{\mathrm{in}}}{4u}
=
\frac{2u\,c}{4u}
=
\frac{c}{2}.
$$

Standard optics predicts no fringe-specific one-way speed change:

$$
v_{\mathrm{fringe}} = v_{\mathrm{ref}}
$$

within experimental error. The tested alternative is

$$
v_{\mathrm{fringe}} < v_{\mathrm{ref}}.
$$


## Standard Optical Interference Theory Applied to the Proposal

This section does six things:

1. defines the coordinate system and variables,
2. derives the interference amplitude pattern on the observation plane,
3. derives the transverse phase-gradient parameter $q(\theta)$ from the
   rejoining angle $\theta$,
4. derives the fringe width and the $>3u$ observation window,
5. states the one-way speed measurement by amplitude modulation,
6. leaves the channel-unavailability interpretation to Appendix A.


### Coordinate System and Carrier Fields

Let

$$
\mathbf{r}=x\hat{\mathbf{x}}+y\hat{\mathbf{y}}+z\hat{\mathbf{z}},
$$

where the interference geometry lies in the $x$-$z$ plane, $x$ is transverse
to the fringes, $z$ is longitudinal, and $y$ is inert in this symmetric
configuration.

Let the two carrier fields be

$$
f_1(\mathbf{r},t)=A_1(t)\,e^{-i(\mathbf{k}_1\cdot\mathbf{r}-\omega t)},
\qquad
f_2(\mathbf{r},t)=A_2(t)\,e^{-i(\mathbf{k}_2\cdot\mathbf{r}-\omega t)},
$$

with

$$
|\mathbf{k}_1|=|\mathbf{k}_2|=k=\frac{2\pi}{\lambda}.
$$

For a sinusoidal amplitude modulation driven by a function generator, take

$$
A_1(t)=A_2(t)=A_m\sin(\Omega t),
$$

where $A_m$ is the modulation amplitude and $\Omega$ is the modulation angular
frequency. The optical carrier angular frequency is $\omega$.


### Rejoining Angle and Interference Pattern

Let the two beams rejoin symmetrically with total crossing angle $\theta$. Then

$$
\mathbf{k}_1 =
k\sin\!\left(\frac{\theta}{2}\right)\hat{\mathbf{x}}
+
k\cos\!\left(\frac{\theta}{2}\right)\hat{\mathbf{z}},
\qquad
\mathbf{k}_2 =
-k\sin\!\left(\frac{\theta}{2}\right)\hat{\mathbf{x}}
+
k\cos\!\left(\frac{\theta}{2}\right)\hat{\mathbf{z}}.
$$

The relative phase is

$$
\Psi(\mathbf{r})
=
(\mathbf{k}_1-\mathbf{k}_2)\cdot\mathbf{r}
=
2k\sin\!\left(\frac{\theta}{2}\right)x.
$$

Define

$$
q(\theta):=2k\sin\!\left(\frac{\theta}{2}\right).
$$

Then

$$
\Psi(\mathbf{r})=q(\theta)x.
$$

Here $\theta$ is the geometric rejoining angle, while $q(\theta)$ is the
transverse spatial phase gradient. They are not interchangeable:

$$
[\theta]=1,
\qquad
[q]=\mathrm{length}^{-1}.
$$

At a fixed observation plane $z=z_0$, the raw superposed field is

$$
f_{\mathrm{raw}}(x,z_0,t)
=
f_1+f_2
=
2A_1(t)\cos\!\left(\frac{q(\theta)x}{2}\right)
e^{-i(kz_0\cos(\theta/2)-\omega t)}.
$$

Define the single-beam density

$$
u(t):=|A_1(t)|^2=|A_2(t)|^2.
$$

Then the raw overlap density on the observation plane is

$$
u_{\mathrm{raw}}(x,t)
=
|f_{\mathrm{raw}}|^2
=
4u(t)\cos^2\!\left(\frac{q(\theta)x}{2}\right).
$$

Therefore

$$
0 \le u_{\mathrm{raw}}(x,t) \le 4u(t).
$$

Bright-fringe centers satisfy

$$
x_n = \frac{2\pi n}{q(\theta)},
\qquad
n\in\mathbb Z,
$$

and at those points

$$
u_{\mathrm{raw}}(x_n,t)=4u(t).
$$


### Complementary Output Branches

At the final 50/50 beam splitter, define the output channels

$$
f_+(x,t)=\frac{f_1(x,t)+f_2(x,t)}{\sqrt2},
\qquad
f_-(x,t)=\frac{f_1(x,t)-f_2(x,t)}{\sqrt2}.
$$

Their densities are

$$
u_+(x,t)=2u(t)\cos^2\!\left(\frac{q(\theta)x}{2}\right),
\qquad
u_-(x,t)=2u(t)\sin^2\!\left(\frac{q(\theta)x}{2}\right).
$$

Hence

$$
u_+(x,t)+u_-(x,t)=2u(t).
$$

So a bright fringe on one output corresponds to a dark fringe on the other, in
the standard complementary $\cos^2/\sin^2$ way.


### Fringe Width and Observation Window

To keep the sampled region above $3u(t)$, require

$$
u_{\mathrm{raw}}(x,t) > 3u(t).
$$

Writing

$$
x=x_n+\Delta x,
$$

gives

$$
4u(t)\cos^2\!\left(\frac{q(\theta)\Delta x}{2}\right) > 3u(t),
$$

so

$$
\cos^2\!\left(\frac{q(\theta)\Delta x}{2}\right) > \frac{3}{4}.
$$

Therefore

$$
\left|\frac{q(\theta)\Delta x}{2}\right| < \frac{\pi}{6},
$$

hence

$$
|\Delta x| < \frac{\pi}{3q(\theta)}.
$$

The fringe period is

$$
\Lambda = \frac{2\pi}{q(\theta)}
=
\frac{\lambda}{2\sin(\theta/2)}
\approx
\frac{\lambda}{\theta}
\quad
(\theta\ll 1).
$$

So the full central width above $3u(t)$ is

$$
\frac{\Lambda}{3}.
$$

For a HeNe laser,

$$
\lambda = 632.8\,\mathrm{nm}.
$$

If

$$
\theta = 0.2\,\mathrm{mrad},
$$

then

$$
\Lambda
\approx
\frac{632.8\times10^{-9}}{2\times10^{-4}}
\approx
3.16\,\mathrm{mm},
$$

so the $>3u(t)$ bright-core width is

$$
\frac{\Lambda}{3} \approx 1.05\,\mathrm{mm}.
$$

If a detector or slit centered on the bright maximum has active width $a$, the
worst-case sampled loading is

$$
u_{\mathrm{edge}}(t)
=
4u(t)\cos^2\!\left(\frac{\pi a}{2\Lambda}\right).
$$

For the same HeNe example:

- if $a=0.25\,\mathrm{mm}$, then $u_{\mathrm{edge}}(t)\approx 3.94u(t)$;
- if $a=0.50\,\mathrm{mm}$, then $u_{\mathrm{edge}}(t)\approx 3.76u(t)$.

So a practical observation window is

$$
0.25\,\mathrm{mm}\;\text{to}\;0.50\,\mathrm{mm},
$$

centered on the bright-fringe maximum.


### One-Way Speed Measurement by Amplitude Modulation

1. Split a coherent amplitude-modulated laser beam into two equal beams.
2. Recombine them at a small angle in a Mach-Zehnder interferometer.
3. Use one output branch, where stable straight fringes are visible.
4. Spatially isolate the center of one bright fringe ridge.
5. Propagate that bright ridge over a known distance $L$.
6. In parallel, propagate one incident beam as a reference over the same
   distance.
7. Measure each channel delay $\tau$ relative to the common modulation signal.

For each channel, record

$$
(L_1,\tau_1),\ (L_2,\tau_2),\ (L_3,\tau_3),\ \ldots
$$

and fit

$$
\tau(L)=mL+b.
$$

Here $b$ is the fixed zero-length offset. The local slope estimates are

$$
m_i=\frac{\delta\tau_i}{\delta L_i},
$$

and the regression returns the mean slope

$$
\langle m\rangle \approx \frac{d\tau}{dL}.
$$

Since

$$
\tau = \frac{L}{v},
$$

the speed is

$$
v=\frac{1}{\langle m\rangle}.
$$

Thus

$$
v_{\mathrm{ref}}=\frac{1}{\langle m_{\mathrm{ref}}\rangle},
\qquad
v_{\mathrm{fringe}}=\frac{1}{\langle m_{\mathrm{fringe}}\rangle}.
$$


## Experimental Question

The standard-optics expectation is

$$
v_{\mathrm{fringe}}=v_{\mathrm{ref}}
$$

within experimental error. The tested alternative is

$$
v_{\mathrm{fringe}}<v_{\mathrm{ref}}.
$$


## Appendix A. Channel Energetic Unavailability

This appendix states the nonstandard transport interpretation used by the
proposal.

Let the two available output-channel amplitudes be

$$
c_+ := \frac{a+b}{\sqrt2},
\qquad
c_- := \frac{a-b}{\sqrt2},
$$

with channel energies

$$
u_+ := |c_+|^2,
\qquad
u_- := |c_-|^2.
$$

Then

$$
u_+ + u_-
=
\frac{|a+b|^2 + |a-b|^2}{2}
=
|a|^2 + |b|^2.
$$

So the total budget is conserved exactly.

Now take equal-energy opposite-sign inputs:

$$
b=-a.
$$

Then

$$
c_+ = \frac{a+(-a)}{\sqrt2}=0,
\qquad
c_- = \frac{a-(-a)}{\sqrt2}=\sqrt2\,a.
$$

Therefore

$$
u_+ = 0,
\qquad
u_- = 2|a|^2.
$$

This proves the precise claim used by the proposal:

- the cancelled channel is energetically unavailable,
- its energetic budget is not destroyed,
- the full positive budget is recovered in the complementary surviving channel.

In this interpretation, a dark fringe is a self-cancelled local recovery
channel, and the complementary bright fringe is the surviving compressed
channel.


## Minimum Requirements

- stable coherent source
- Mach-Zehnder interferometer
- controlled small crossing angle at recombination
- stable fringe pattern
- spatial filter for one bright ridge
- common amplitude modulation source
- oscilloscope or phase-delay readout
- variable path length


## Summary

The proposal:

1. derives the standard interference field and fringe scale,
2. fixes a practical HeNe fringe width and observation window,
3. measures one-way delay by amplitude modulation,
4. compares the standard null expectation to the tested alternative,
5. places the channel energetic unavailability argument in Appendix A.
