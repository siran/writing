---
title: Experimental Proposal - Longitudinal Delay of an Isolated Interference Fringe
date: 2026-04-16
---

# Experimental Proposal

## Goal

Measure the longitudinal delay of the center of an isolated bright fringe in a
Mach-Zehnder interferometer.


## Hypothesis being tested

Take one incident beam entering the first beam splitter with energy density
$2u$. Over a propagation interval $\Delta t$ and transverse area $A$, the
incident channel occupies volume

$$
V = A c \Delta t,
$$

so the incident energy and energy flux are

$$
E_{\mathrm{in}} = 2uV,\qquad J_{\mathrm{in}} = 2u c.
$$

At the first beam splitter, that one incident channel is divided into two arm
channels of the same volume $V$. The total energy is split equally, so each arm
carries

$$
E_1 = E_2 = uV,
$$

hence each arm has energy density $u$ and energy flux

$$
J_1 = J_2 = u c.
$$

Therefore

$$
2u c \longrightarrow u c + u c.
$$

So the first beam splitter is the decompression step: **one** incident channel
becomes **two** arm channels, the occupied propagation volume doubles, the
energy density in each arm drops from $2u$ to $u$, and the total energy flux is
unchanged.

Recombination is not the same spatial operation as the first beam splitter.
At BS1, one bright incident beam is divided into two bright arm channels. At
recombination, the two bright returned arm channels recover one coherent
output-channel energy flux, and that single recovered flux is then
distributed across the two output arms as

$$
u_+(x,y)=2u\cos^2\!\left(\frac{\Delta\phi(x,y)}{2}\right),\qquad
u_-(x,y)=2u\sin^2\!\left(\frac{\Delta\phi(x,y)}{2}\right),
$$

so

$$
u_+(x,y)+u_-(x,y)=2u.
$$

Thus the total returned arm energy flux is recovered as **one** conserved
output-channel energy flux, spatially distributed across the two output arms of
the Mach-Zehnder recombination:

$$
J_{\mathrm{out}} = 2u c.
$$

To describe the raw overlap corresponding to that same recovered output-channel
energy flux before expressing it in the complementary $\cos^2/\sin^2$ arm
decomposition, write the two returned arm amplitudes as

$$
a_1(x,y)=\sqrt{u}\,e^{i\phi_1(x,y)},\qquad
a_2(x,y)=\sqrt{u}\,e^{i\phi_2(x,y)},
$$

with

$$
\Delta\phi=\phi_1-\phi_2.
$$

Then the raw superposed amplitude is

$$
a_{\mathrm{raw}}=a_1+a_2,
$$

so the raw overlap energy density is

$$
u_{\mathrm{raw}}=|a_{\mathrm{raw}}|^2=|a_1+a_2|^2.
$$

Expanding,

$$
u_{\mathrm{raw}}
=|a_1|^2+|a_2|^2+a_1a_2^*+a_1^*a_2
=u+u+u e^{i\Delta\phi}+u e^{-i\Delta\phi}.
$$

Using

$$
e^{i\Delta\phi}+e^{-i\Delta\phi}=2\cos(\Delta\phi),
$$

this gives

$$
u_{\mathrm{raw}}(x,y)
=2u+2u\cos(\Delta\phi(x,y))
=4u\cos^2\!\left(\frac{\Delta\phi(x,y)}{2}\right).
$$

Therefore

$$
0 \le u_{\mathrm{raw}}(x,y) \le 4u.
$$

At a bright center, where $\Delta\phi=0$,

$$
u_{\mathrm{raw,peak}} = 4u.
$$

So the compression step is not the same spatial picture as the split step:

$$
2u \longrightarrow u+u
\qquad\text{at BS1,}
$$

$$
u+u \longrightarrow \text{one recovered output-channel flux}
\qquad\text{at recombination.}
$$

The first map sends one bright incident beam into two bright arm channels. The
second map does not produce two bright outputs of the same kind. Instead, the
returned arm flux is recovered as one coherent output-channel flux, and the raw
bright overlap reaches

$$
u_{\mathrm{raw,peak}}=4u.
$$

The two interfaces are therefore not symmetric as spatial decompositions:
BS1 yields two bright arm beams, whereas recombination yields one coherent
recovered output flux spatially distributed across the complementary
$\sin^2/\cos^2$ output arms.

The contradiction is not with energy conservation, which is assumed throughout.
It is with forcing the isolated bright branch to keep the unchanged
longitudinal speed $c$. If that bright branch were assigned speed $c$, then at
the bright center it would carry

$$
J_{\mathrm{bright}} = 4u c,
$$

while the available recovered output-channel energy flux is only

$$
J_{\mathrm{out}} = 2u c.
$$

Under this branch reading, conservation therefore requires

$$
4u\,c_{\mathrm{eff}} = 2u c,
$$

and hence

$$
c_{\mathrm{eff}} = \frac{c}{2}.
$$

Here $c_{\mathrm{eff}}$ is the effective longitudinal propagation speed.

In that plane-wave specialization, the fringes are straight ridges invariant in
$y$, not circular rings. So the exact control volume for that model
is a transverse strip. No approximation such as $\cos(\cdot)\approx 1$ or
$\sin(\cdot)\approx(\cdot)$ is used in the following integrals.

Take a symmetric strip window

$$
|x-x_0| \le \delta,
$$

with $0 \lt \delta \le \pi/q$, and let $h$ be the sampled stripe
height in the inert $y$ direction. If the raw bright profile were
transported unchanged at speed $c$, the implied exact strip
throughput would be

$$
\Phi_{\mathrm{peak}}^{\mathrm{strip}}(\delta;h)
:= h c \int_{x_0-\delta}^{x_0+\delta} u_{\mathrm{raw}}(x)\,dx.
$$

Using

$$
\cos^2\!\left(\frac{q(x-x_0)}{2}\right)=\frac{1+\cos(q(x-x_0))}{2},
$$

this becomes

$$
\Phi_{\mathrm{peak}}^{\mathrm{strip}}(\delta;h)
= 4u c h\left(\delta + \frac{\sin(q\delta)}{q}\right).
$$

Over the same strip, the available incoming two-beam throughput is exact because
in this model the incoming two-beam energy density is uniform and equal to
$2u$:

$$
\Phi_{\mathrm{in}}^{\mathrm{strip}}(\delta;h)
:= h \int_{x_0-\delta}^{x_0+\delta} 2u c\,dx
= 4u c h\,\delta.
$$

Therefore

$$
\Phi_{\mathrm{peak}}^{\mathrm{strip}}(\delta;h)
- \Phi_{\mathrm{in}}^{\mathrm{strip}}(\delta;h)
= \frac{4u c h}{q}\sin(q\delta).
$$

For every proper bright-core strip $0 \lt \delta \lt \pi/q$, we have
$0 \lt q\delta \lt \pi$, hence $\sin(q\delta)\gt 0$, so

$$
\Phi_{\mathrm{peak}}^{\mathrm{strip}}(\delta;h)
\gt \Phi_{\mathrm{in}}^{\mathrm{strip}}(\delta;h).
$$

So in the adopted straight-fringe geometry, any isolated symmetric strip around
the bright center would overcarry the available energy flux if the raw
$4u\cos^2$ profile were taken to move longitudinally at speed
$c$. The excess vanishes exactly only when the window expands to
the full bright-to-dark cell $\delta=\pi/q$.

If one instead prefers a circular aperture of radius $\rho$ centered
on the bright point, write $\xi:=x-x_0$. Then the exact disk throughput is

$$
\Phi_{\mathrm{peak}}^{\mathrm{disk}}(\rho)
:= c \iint_{(x-x_0)^2+y^2\le \rho^2} u_{\mathrm{raw}}(x)\,dA
= 8u c \int_{-\rho}^{\rho} \sqrt{\rho^2-\xi^2}\cos^2\!\left(\frac{q\xi}{2}\right)d\xi.
$$

Using $\cos^2(q\xi/2)=(1+\cos(q\xi))/2$, this becomes

$$
\Phi_{\mathrm{peak}}^{\mathrm{disk}}(\rho)
= 4u c \int_{-\rho}^{\rho} \sqrt{\rho^2-\xi^2}\,[1+\cos(q\xi)]\,d\xi.
$$

Now use the exact identities

$$
\int_{-\rho}^{\rho} \sqrt{\rho^2-\xi^2}\,d\xi = \frac{\pi\rho^2}{2},
\qquad
\int_{-\rho}^{\rho} \sqrt{\rho^2-\xi^2}\cos(q\xi)\,d\xi
= \frac{\pi\rho}{q}J_1(q\rho),
$$

where $J_1$ is the Bessel function of the first kind. Therefore

$$
\Phi_{\mathrm{peak}}^{\mathrm{disk}}(\rho)
= 2\pi u c\,\rho^2 + \frac{4\pi u c\,\rho}{q}J_1(q\rho).
$$

Over the same disk, the available incoming throughput is

$$
\Phi_{\mathrm{in}}^{\mathrm{disk}}(\rho)
= 2u c\,(\pi \rho^2)
= 2\pi u c\,\rho^2.
$$

Therefore

$$
\Phi_{\mathrm{peak}}^{\mathrm{disk}}(\rho)
- \Phi_{\mathrm{in}}^{\mathrm{disk}}(\rho)
= \frac{4\pi u c\,\rho}{q}J_1(q\rho).
$$

Since $J_1(x)\gt 0$ for $0 \lt x \lt j_{1,1}\approx 3.8317$, every proper
bright-core disk with $0 \lt \rho \lt \pi/q$ also satisfies

$$
\Phi_{\mathrm{peak}}^{\mathrm{disk}}(\rho)
\gt \Phi_{\mathrm{in}}^{\mathrm{disk}}(\rho),
$$

because $\pi \lt j_{1,1}$. So the contradiction survives exact circular-aperture
integration as well.

This is the nonstandard step tested here: the isolated bright-core branch is
treated as the transported branch, with the complementary channel locally
unavailable. Appendix A states that channel-unavailability argument explicitly.

The pointwise center statement is the $\delta \to 0$ strip limit, or
equivalently the $\rho \to 0$ disk limit, of the same comparison. In the
plane-wave notation used here, the bright-center relations reduce to

$$
u_{\mathrm{raw,peak}} = 4u,\qquad
J_{\mathrm{out}} = 2u c,\qquad
c_{\mathrm{eff}} = \frac{2u c}{4u} = \frac{c}{2}.
$$


## Standard Optical Interference Theory Applied to the Proposal

This section does six things:

1. defines the coordinate system and variables,
2. derives the interference amplitude pattern on the observation plane,
3. derives the transverse phase-gradient parameter $q(\theta)$ from the
   rejoining angle $\theta$,
4. derives the fringe width and the above-$3u$ observation window,
5. states the one-way speed measurement by amplitude modulation,
6. leaves the channel-unavailability interpretation to Appendix A.


### Coordinate System and Carrier Fields

Let

$$ \mathbf{r}=x\hat{\mathbf{x}}+y\hat{\mathbf{y}}+z\hat{\mathbf{z}}, $$

where the interference geometry lies in the $x$-$z$
plane, $x$ is transverse to the fringes, $z$ is
longitudinal, and $y$ is inert in this symmetric configuration.

Let the two carrier fields be

$$ f_1(\mathbf{r},t)=A_1(t) e^{-i(\mathbf{k}_1\cdot\mathbf{r}-\omega t)}, \qquad f_2(\mathbf{r},t)=A_2(t) e^{-i(\mathbf{k}_2\cdot\mathbf{r}-\omega t)}, $$

with

$$ |\mathbf{k}_1|=|\mathbf{k}_2|=k=\frac{2\pi}{\lambda}. $$

For a sinusoidal amplitude modulation driven by a function generator, take

$$ A_1(t)=A_2(t)=A_m\sin(\Omega t), $$

where $A_m$ is the modulation amplitude and $\Omega$ is the
modulation angular frequency. The optical carrier angular frequency is
$\omega$.


### Rejoining Angle and Interference Pattern

Let the two beams rejoin symmetrically with total crossing angle
$\theta$. Then

$$ \mathbf{k}_1 = k\sin\left(\frac{\theta}{2}\right)\hat{\mathbf{x}} + k\cos\left(\frac{\theta}{2}\right)\hat{\mathbf{z}}, \qquad \mathbf{k}_2 = -k\sin\left(\frac{\theta}{2}\right)\hat{\mathbf{x}} + k\cos\left(\frac{\theta}{2}\right)\hat{\mathbf{z}}. $$

The relative phase is

$$ \Psi(\mathbf{r}) = (\mathbf{k}_1-\mathbf{k}_2)\cdot\mathbf{r} = 2k\sin\left(\frac{\theta}{2}\right)x. $$

Define

$$ q(\theta):=2k\sin\left(\frac{\theta}{2}\right). $$

Then

$$ \Psi(\mathbf{r})=q(\theta)x. $$

Here $\theta$ is the geometric rejoining angle, while $q(\theta)$
is the transverse spatial phase gradient. They are not interchangeable:

$$ [\theta]=1, \qquad [q]=\mathrm{length}^{-1}. $$

At a fixed observation plane $z=z_0$, the raw superposed field is

$$ f_{\mathrm{raw}}(x,z_0,t) = f_1+f_2 = 2A_1(t)\cos\left(\frac{q(\theta)x}{2}\right) e^{-i(kz_0\cos(\theta/2)-\omega t)}. $$

Define the single-beam density

$$ u(t):=|A_1(t)|^2=|A_2(t)|^2. $$

Then the raw overlap density on the observation plane is

$$ u_{\mathrm{raw}}(x,t) = |f_{\mathrm{raw}}|^2 = 4u(t)\cos^2\left(\frac{q(\theta)x}{2}\right). $$

Therefore

$$ 0 \le u_{\mathrm{raw}}(x,t) \le 4u(t). $$

Bright-fringe centers satisfy

$$ x_n = \frac{2\pi n}{q(\theta)}, \qquad n\in\mathbb Z, $$

and at those points

$$ u_{\mathrm{raw}}(x_n,t)=4u(t). $$


### Complementary Output Branches

At the final 50/50 beam splitter, define the output channels

$$ f_+(x,t)=\frac{f_1(x,t)+f_2(x,t)}{\sqrt{2}}, \qquad f_-(x,t)=\frac{f_1(x,t)-f_2(x,t)}{\sqrt{2}}. $$

Their densities are

$$ u_+(x,t)=2u(t)\cos^2\left(\frac{q(\theta)x}{2}\right), \qquad u_-(x,t)=2u(t)\sin^2\left(\frac{q(\theta)x}{2}\right). $$

Hence

$$ u_+(x,t)+u_-(x,t)=2u(t). $$

So a bright fringe on one output corresponds to a dark fringe on the other, in
the standard complementary $\cos^2/\sin^2$ way.


### Fringe Width and Observation Window

To keep the sampled region above $3u(t)$, require

$$ u_{\mathrm{raw}}(x,t) \gt 3u(t). $$

Writing

$$ x=x_n+\Delta x, $$

gives

$$ 4u(t)\cos^2\left(\frac{q(\theta)\Delta x}{2}\right) \gt 3u(t), $$

so

$$ \cos^2\left(\frac{q(\theta)\Delta x}{2}\right) \gt \frac{3}{4}. $$

Therefore

$$ \left|\frac{q(\theta)\Delta x}{2}\right| \lt \frac{\pi}{6}, $$

hence

$$ |\Delta x| \lt \frac{\pi}{3q(\theta)}. $$

The fringe period is

$$ \Lambda = \frac{2\pi}{q(\theta)} = \frac{\lambda}{2\sin(\theta/2)} \approx \frac{\lambda}{\theta} \quad (\theta\ll 1). $$

So the full central width above $3u(t)$ is

$$ \frac{\Lambda}{3}. $$

For a HeNe laser,

$$ \lambda = 632.8 \mathrm{nm}. $$

If

$$ \theta = 0.2 \mathrm{mrad}, $$

then

$$ \Lambda \approx \frac{632.8\times10^{-9}}{2\times10^{-4}} \approx 3.16 \mathrm{mm}, $$

so the above-$3u(t)$ bright-core width is

$$ \frac{\Lambda}{3} \approx 1.05 \mathrm{mm}. $$

If a detector or slit centered on the bright maximum has active width
$a$, the worst-case sampled energy density is

$$ u_{\mathrm{edge}}(t) = 4u(t)\cos^2\left(\frac{\pi a}{2\Lambda}\right). $$

For the same HeNe example:

- if $a=0.25 \mathrm{mm}$, then $u_{\mathrm{edge}}(t)\approx 3.94u(t)$;
- if $a=0.50 \mathrm{mm}$, then $u_{\mathrm{edge}}(t)\approx 3.76u(t)$.


So a practical observation window is

$$ 0.25 \mathrm{mm} \text{to} 0.50 \mathrm{mm}, $$

centered on the bright-fringe maximum.


### One-Way Speed Measurement by Amplitude Modulation

1. Split a coherent amplitude-modulated laser beam into two equal beams.
2. Recombine them at a small angle in a Mach-Zehnder interferometer.
3. Use one output branch, where stable straight fringes are visible.
4. Spatially isolate the center of one bright fringe ridge.
5. Propagate that bright ridge over a known distance $L$.
6. In parallel, propagate one incident beam as a reference over the same
   distance.
7. Measure each channel delay $\tau$ relative to the common modulation
   signal.


For each channel, record

$$ (L_1,\tau_1),\ (L_2,\tau_2),\ (L_3,\tau_3),\ \ldots $$

and fit

$$ \tau(L)=mL+b. $$

Here $b$ is the fixed zero-length offset. The local slope estimates
are

$$ m_i=\frac{\delta\tau_i}{\delta L_i}, $$

and the regression returns the mean slope

$$ \langle m\rangle \approx \frac{d\tau}{dL}. $$

Since

$$ \tau = \frac{L}{v}, $$

the speed is

$$ v=\frac{1}{\langle m\rangle}. $$

Thus

$$ v_{\mathrm{ref}}=\frac{1}{\langle m_{\mathrm{ref}}\rangle}, \qquad v_{\mathrm{fringe}}=\frac{1}{\langle m_{\mathrm{fringe}}\rangle}. $$


## Experimental Question

The standard-optics expectation is

$$ v_{\mathrm{fringe}}=v_{\mathrm{ref}} $$

within experimental error. The tested alternative is

$$ v_{\mathrm{fringe}} \lt v_{\mathrm{ref}}. $$


## Appendix A. Channel Energetic Unavailability

This appendix states the nonstandard transport interpretation used by the
proposal.

Let the two available output-channel amplitudes be

$$ c_+ := \frac{a+b}{\sqrt{2}}, \qquad c_- := \frac{a-b}{\sqrt{2}}, $$

with channel energies

$$ u_+ := |c_+|^2, \qquad u_- := |c_-|^2. $$

Then

$$ u_+ + u_- = \frac{|a+b|^2 + |a-b|^2}{2} = |a|^2 + |b|^2. $$

So the total energy is conserved exactly.

Now take equal-energy opposite-sign inputs:

$$ b=-a. $$

Then

$$ c_+ = \frac{a+(-a)}{\sqrt{2}}=0, \qquad c_- = \frac{a-(-a)}{\sqrt{2}}=\sqrt{2} a. $$

Therefore

$$ u_+ = 0, \qquad u_- = 2|a|^2. $$

This proves the precise claim used by the proposal:

- the cancelled channel is energetically unavailable,
- its energy is not destroyed,
- the full positive energy is recovered in the complementary surviving channel.


This proves exact channel reduction, but not yet reduced propagation speed.

If the surviving branch is read as the normalized Mach-Zehnder bright output,
then its density is only $2|a|^2$ and it can carry the full two-beam
energy flux at speed $c$ with no contradiction. The proposal's
tested step is the stronger identification used in the main hypothesis block:
the transported branch is the raw bright-overlap peak of density
$4|a|^2$. Under that identification, letting it advance at speed
$c$ would imply a carried flux larger than the available incoming
energy flux, so reduced effective longitudinal propagation speed
$c_{\mathrm{eff}}$ is required by conservation.

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
