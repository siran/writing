% Longitudinal Delay of an Isolated Bright Interference Branch % An M. Rodriguez
% 2026-04-21


# Longitudinal Delay of an Isolated Bright Interference Branch

## Abstract

This proposal tests whether the bright center of a spatially isolated
interference stripe propagates with the same delay as an ordinary reference
beam, or whether its effective longitudinal advance is reduced by coherent
loading.

Two equal coherent beams are recombined at a small angle to produce stable
straight fringes. Standard interference gives a spatial redistribution of
density: bright regions exceed the two-beam mean while neighboring dark regions
fall below it, with the full fringe average conserving the two-beam budget. The
experiment isolates a narrow bright stripe and measures its modulation delay
over a known distance against a reference beam.

The standard expectation is that the selected bright stripe and the reference
beam have the same propagation speed, up to ordinary geometric and aperture
effects. The loaded-branch expectation is that a bright stripe carrying the
available two-beam flux on a higher local density must advance more slowly. For
equal beams at a bright center, the predicted speed is approximately half the
reference speed.

The experiment is therefore a direct time-of-flight test between two readings of
the same interference pattern: ordinary output transport and loaded raw-overlap
transport.

---


# 1. Goal

The goal is to measure the longitudinal delay of the center of an isolated
bright interference stripe.

The experimental question is:

$$
\boxed{
\text{Does an isolated bright stripe propagate like ordinary output light, or like a loaded raw-overlap branch?}
}
$$

The standard expectation is

$$
v_{\mathrm{stripe}}=v_{\mathrm{ref}}
$$

within experimental error.

The loaded-branch expectation is

$$
v_{\mathrm{stripe}}<v_{\mathrm{ref}},
$$

with the bright-center prediction

$$
v_{\mathrm{stripe}}\approx \frac{c}{2}
$$

for nearly collinear equal beams in vacuum.

---


# 2. Core Idea

Two equal coherent beams can overlap in phase. At a bright fringe center, their
amplitudes add before the energy-density readout is taken. Since the density
readout is quadratic, the raw local density at a bright center is four times the
single-beam density.

However, the incoming two-beam flux budget is only twice the single-beam flux.
The full interference pattern conserves energy by distributing density into
bright and dark regions. The proposed test asks what happens when only a narrow
bright region is selected and propagated as a channel.

If the selected bright stripe behaves like ordinary output light, it should
propagate with the same delay as a reference beam.

If instead the stripe behaves as a loaded branch, then the local speed is given
by

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

At a bright center,

$$
J=2u_0c,
\qquad
u=4u_0,
$$

so

$$
v_{\mathrm{eff}}=\frac{2u_0c}{4u_0}=\frac{c}{2}.
$$

The prediction is large, clean, and directly falsifiable.

---


# 3. Definitions

Let each incoming coherent beam have amplitude-like field

$$
f_j=A_j e^{i\phi_j}.
$$

For equal beams,

$$
|A_1|=|A_2|=:A.
$$

Define the single-beam density by

$$
u_0:=C|A|^2,
$$

where $C>0$ is the conventional proportionality factor between
squared field amplitude and energy density.

Let the relative phase be

$$
\Delta\phi=\phi_1-\phi_2.
$$

The raw coherent overlap field is

$$
f_{\mathrm{raw}}=f_1+f_2.
$$

The raw density is

$$
u_{\mathrm{raw}}=C|f_{\mathrm{raw}}|^2.
$$

For one freely propagating beam in vacuum, the flux magnitude is

$$
J_0=u_0c.
$$

If a beam travels at angle $\theta$ relative to the longitudinal
$z$-axis, its longitudinal projected flux is

$$
J_{0,z}=u_0c\cos\theta.
$$

For two equal symmetric beams,

$$
J_{\mathrm{in},z}=2u_0c\cos\theta.
$$

---


# 4. Derivation of the Raw Interference Density

This section derives the standard raw overlap density

$$
u_{\mathrm{raw}}(x)
=
4u_0\cos^2\!\left(\frac{qx}{2}\right).
$$

No loaded-branch assumption is used here.


## 4.1 Source-Free Monochromatic Wave Component

In a source-free region, each Cartesian component of a transverse
electromagnetic plane wave satisfies the scalar wave equation

$$
\nabla^2 f-\frac{1}{c^2}\partial_t^2 f=0.
$$

A monochromatic plane-wave solution is

$$
f(\mathbf r,t)
=
A e^{i(\mathbf k\cdot\mathbf r-\omega t)},
$$

with dispersion relation

$$
\omega=c|\mathbf k|.
$$

The physical real field is the real part of this complex representation. The
complex expression is a compact way to track phase. Quadratic observables are
obtained from the squared amplitude with the chosen normalization.

Define

$$
u_0=C|A|^2.
$$


## 4.2 Two Symmetric Beams

Let two equal beams cross symmetrically about the $z$-axis in the
$x$-$z$ plane. Let $\theta$ be the half-angle
between each beam and the $z$-axis.

Then

$$
\mathbf k_1
=
k\sin\theta\,\hat{\mathbf x}
+
k\cos\theta\,\hat{\mathbf z},
$$

and

$$
\mathbf k_2
=
-k\sin\theta\,\hat{\mathbf x}
+
k\cos\theta\,\hat{\mathbf z}.
$$

Both beams have

$$
|\mathbf k_1|=|\mathbf k_2|=k,
\qquad
\omega=ck.
$$

The corresponding fields are

$$
f_1(x,z,t)
=
A e^{i(kx\sin\theta+kz\cos\theta-\omega t)},
$$

and

$$
f_2(x,z,t)
=
A e^{i(-kx\sin\theta+kz\cos\theta-\omega t)}.
$$

Define the transverse phase-gradient parameter

$$
q:=2k\sin\theta.
$$

The relative phase is

$$
\Delta\phi(x)
=
(\mathbf k_1-\mathbf k_2)\cdot\mathbf r
=
2k\sin\theta\,x
=
qx.
$$

Thus $q$ is the transverse spatial phase gradient.


## 4.3 Linear Superposition

Because the wave equation is linear,

$$
f_{\mathrm{raw}}=f_1+f_2
$$

is also a solution.

Substitute the two fields:

$$
f_{\mathrm{raw}}(x,z,t)
=
A e^{i(kx\sin\theta+kz\cos\theta-\omega t)}
+
A e^{i(-kx\sin\theta+kz\cos\theta-\omega t)}.
$$

Factor the common longitudinal and temporal phase:

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

with

$$
a=kx\sin\theta,
$$

gives

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

we obtain

$$
\boxed{
f_{\mathrm{raw}}(x,z,t)
=
2A\cos\!\left(\frac{qx}{2}\right)
e^{i(kz\cos\theta-\omega t)}.
}
$$


## 4.4 Quadratic Density Readout

The raw density is

$$
u_{\mathrm{raw}}(x)
=
C|f_{\mathrm{raw}}(x,z,t)|^2.
$$

Using the expression above,

$$
|f_{\mathrm{raw}}|^2
=
\left|
2A\cos\!\left(\frac{qx}{2}\right)
e^{i(kz\cos\theta-\omega t)}
\right|^2.
$$

The phase factor has unit magnitude:

$$
\left|e^{i(kz\cos\theta-\omega t)}\right|^2=1.
$$

Therefore

$$
|f_{\mathrm{raw}}|^2
=
4|A|^2\cos^2\!\left(\frac{qx}{2}\right).
$$

Multiplying by $C$ gives

$$
u_{\mathrm{raw}}(x)
=
4C|A|^2\cos^2\!\left(\frac{qx}{2}\right).
$$

Since

$$
u_0=C|A|^2,
$$

we get

$$
\boxed{
u_{\mathrm{raw}}(x)
=
4u_0\cos^2\!\left(\frac{qx}{2}\right).
}
$$

This is the standard raw overlap density used in the proposal.

---


# 5. Equivalent Phase-Difference Derivation

The same result follows without specifying the crossing geometry.

Let

$$
f_1=Ae^{i\phi_1},
\qquad
f_2=Ae^{i\phi_2}.
$$

Then

$$
f_{\mathrm{raw}}=f_1+f_2.
$$

The raw density is

$$
u_{\mathrm{raw}}=C|f_1+f_2|^2.
$$

Expand:

$$
|f_1+f_2|^2
=
(f_1+f_2)(f_1^*+f_2^*).
$$

Thus

$$
|f_1+f_2|^2
=
|f_1|^2+|f_2|^2+f_1f_2^*+f_1^*f_2.
$$

Since

$$
|f_1|^2=|f_2|^2=|A|^2,
$$

and

$$
f_1f_2^*
=
|A|^2e^{i(\phi_1-\phi_2)},
$$

while

$$
f_1^*f_2
=
|A|^2e^{-i(\phi_1-\phi_2)},
$$

we have

$$
|f_1+f_2|^2
=
2|A|^2
+
|A|^2
\left(
e^{i\Delta\phi}
+
e^{-i\Delta\phi}
\right),
$$

where

$$
\Delta\phi:=\phi_1-\phi_2.
$$

Using

$$
e^{i\Delta\phi}+e^{-i\Delta\phi}=2\cos\Delta\phi,
$$

we get

$$
|f_1+f_2|^2
=
2|A|^2(1+\cos\Delta\phi).
$$

Using

$$
1+\cos\Delta\phi
=
2\cos^2\!\left(\frac{\Delta\phi}{2}\right),
$$

this becomes

$$
|f_1+f_2|^2
=
4|A|^2
\cos^2\!\left(\frac{\Delta\phi}{2}\right).
$$

Multiplying by $C$ gives

$$
u_{\mathrm{raw}}
=
4u_0
\cos^2\!\left(\frac{\Delta\phi}{2}\right).
$$

For the symmetric crossing geometry,

$$
\Delta\phi(x)=qx.
$$

Therefore

$$
\boxed{
u_{\mathrm{raw}}(x)
=
4u_0
\cos^2\!\left(\frac{qx}{2}\right).
}
$$

---


# 6. Bright Centers, Nodes, Bounds, and Fringe Period

Because

$$
0\le \cos^2\!\left(\frac{qx}{2}\right)\le 1,
$$

the raw density satisfies

$$
0\le u_{\mathrm{raw}}(x)\le 4u_0.
$$

Bright centers occur where

$$
\cos^2\!\left(\frac{qx}{2}\right)=1.
$$

This requires

$$
\frac{qx}{2}=n\pi,
\qquad
n\in\mathbb Z.
$$

Therefore

$$
x_n=\frac{2\pi n}{q}.
$$

At those points,

$$
u_{\mathrm{raw}}(x_n)=4u_0.
$$

Nodes occur where

$$
\cos^2\!\left(\frac{qx}{2}\right)=0.
$$

This requires

$$
\frac{qx}{2}
=
\frac{(2n+1)\pi}{2}.
$$

Thus

$$
x_n^{\mathrm{node}}
=
\frac{(2n+1)\pi}{q}.
$$

At those points,

$$
u_{\mathrm{raw}}=0.
$$

The fringe period $\Lambda$ is the smallest positive shift satisfying

$$
q(x+\Lambda)=qx+2\pi.
$$

Thus

$$
\Lambda=\frac{2\pi}{q}.
$$

Since

$$
q=2k\sin\theta,
\qquad
k=\frac{2\pi}{\lambda},
$$

we get

$$
\boxed{
\Lambda=\frac{\lambda}{2\sin\theta}.
}
$$

For small $\theta$,

$$
\Lambda\approx\frac{\lambda}{2\theta}.
$$

---


# 7. Full-Period Mean Density

The full-period average is

$$
\langle u_{\mathrm{raw}}\rangle
=
\frac{1}{\Lambda}
\int_0^\Lambda
4u_0\cos^2\!\left(\frac{qx}{2}\right)dx.
$$

Let

$$
y=\frac{qx}{2},
\qquad
dx=\frac{2}{q}dy.
$$

When $x=0$,

$$
y=0.
$$

When $x=\Lambda=2\pi/q$,

$$
y=\pi.
$$

Therefore

$$
\langle u_{\mathrm{raw}}\rangle
=
\frac{4u_0}{\Lambda}
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
\frac{4u_0}{\Lambda}
\frac{2}{q}
\frac{\pi}{2}
=
\frac{4\pi u_0}{q\Lambda}.
$$

Using

$$
\Lambda=\frac{2\pi}{q},
$$

so that

$$
q\Lambda=2\pi,
$$

we find

$$
\boxed{
\langle u_{\mathrm{raw}}\rangle=2u_0.
}
$$

Thus the raw interference pattern conserves the two-beam density budget over a
complete fringe period:

$$
u_0+u_0=2u_0.
$$

The density is redistributed. It is not created.

---


# 8. Forward Flux Budget

Each incoming beam has flux magnitude

$$
J_0=u_0c.
$$

Since each beam makes angle $\theta$ with the $z$-axis, its
longitudinal projected flux is

$$
J_{0,z}=u_0c\cos\theta.
$$

For two equal symmetric beams,

$$
\boxed{
J_{\mathrm{in},z}=2u_0c\cos\theta.
}
$$

Dividing by the full-period mean density gives the mean longitudinal advance
rate of the full pattern:

$$
\frac{J_{\mathrm{in},z}}{\langle u_{\mathrm{raw}}\rangle}
=
\frac{2u_0c\cos\theta}{2u_0}
=
c\cos\theta.
$$

Therefore the full fringe-period average has the ordinary longitudinal projected
speed:

$$
\boxed{
v_{\mathrm{mean}}=c\cos\theta.
}
$$

No anomalous delay follows from standard interference alone. The anomalous
prediction enters only when a selected bright branch is assigned the raw local
density while carrying the available two-beam flux.

---


# 9. Ordinary Output Reading

At a lossless 50/50 recombiner, the output modes are

$$
f_+
=
\frac{f_1+f_2}{\sqrt2},
\qquad
f_-
=
\frac{f_1-f_2}{\sqrt2}.
$$

The factor $1/\sqrt2$ is the usual lossless beam-splitter amplitude
factor. It ensures that the total output energy equals the total input energy.

The corresponding densities are

$$
u_+
=
C|f_+|^2
=
\frac{C}{2}|f_1+f_2|^2,
$$

and

$$
u_-
=
C|f_-|^2
=
\frac{C}{2}|f_1-f_2|^2.
$$

Using the phase-difference result,

$$
C|f_1+f_2|^2
=
4u_0\cos^2\!\left(\frac{\Delta\phi}{2}\right),
$$

so

$$
u_+
=
2u_0\cos^2\!\left(\frac{\Delta\phi}{2}\right).
$$

Similarly,

$$
u_-
=
2u_0\sin^2\!\left(\frac{\Delta\phi}{2}\right).
$$

Therefore

$$
\boxed{
u_+(x)+u_-(x)=2u_0.
}
$$

At a bright center of the $+$ output,

$$
u_+=2u_0,
\qquad
u_-=0.
$$

So ordinary output transport assigns the bright output density $2u_0$,
not $4u_0$. It can therefore carry the two-beam budget at the usual
projected speed

$$
c\cos\theta
$$

without a conservation conflict.

This is the standard null prediction.

---


# 10. Loaded Raw-Overlap Branch Reading

The tested alternative is:

$$
\boxed{
\text{An isolated bright stripe propagates as a raw loaded branch with density }u_{\mathrm{raw}}.
}
$$

At a bright center,

$$
u_{\mathrm{raw,peak}}=4u_0.
$$

But the available two-beam longitudinal flux is still

$$
J_{\mathrm{in},z}=2u_0c\cos\theta.
$$

If the bright branch were assigned speed $c\cos\theta$, its local throughput
would be

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

Therefore, under the loaded raw-overlap reading, conservation requires a reduced
effective advance:

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
v_{\mathrm{peak}}=\frac{c\cos\theta}{2}.
}
$$

For $\theta\ll1$,

$$
\boxed{
v_{\mathrm{peak}}\approx\frac c2.
}
$$

This is the central experimental prediction.

---


# 11. Dielectric-Style Derivation of the Loaded-Branch Law

Matter is standing electromagnetic organization. Dielectric slowing is therefore
field-field interaction in a stable organized background. The fringe-delay test
asks whether the same loading rule appears in the simplest unbound case: two
coherent light fields overlapping in phase.


## 11.1 Ordinary Dielectric Form

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

For symmetric electric and magnetic loading,

$$
\chi_e=\chi_m=k,
$$

so

$$
\varepsilon_{\mathrm{eff}}=\varepsilon_0(1+k),
\qquad
\mu_{\mathrm{eff}}=\mu_0(1+k).
$$

Then

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


## 11.2 Coherent Response Field

Let a primary branch have electric field amplitude

$$
E_1.
$$

Let the coherent response field be proportional:

$$
E_2=kE_1,
\qquad
k\ge0.
$$

Then

$$
E_{\mathrm{tot}}
=
E_1+E_2
=
(1+k)E_1.
$$

Because the density readout is quadratic,

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

The corresponding amplitude-loading factor is

$$
n_{\mathrm{eff}}=1+k.
$$

Therefore

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


## 11.3 Flux Form of the Same Result

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


# 12. Spatially Varying Effective Advance Across a Fringe

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

Thus

$$
v_{\mathrm{eff}}(x)
=
\frac{2u_0c\cos\theta}
{4u_0\cos^2(qx/2)}
=
\frac{c\cos\theta}
{2\cos^2(qx/2)}.
$$

Therefore

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

the density equals the mean,

$$
u_{\mathrm{raw}}=2u_0,
$$

and

$$
v_{\mathrm{eff}}=c\cos\theta.
$$

At nodes,

$$
u_{\mathrm{raw}}=0.
$$

The quotient is not interpreted as an infinite speed. A node is not a surviving
forward loaded branch.

---


# 13. Exact Finite-Band Prediction

A real slit samples a finite band around a bright center. Let the selected band
be

$$
|x-x_n|\le \frac a2.
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

The second integral is

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

Thus

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

In the narrow-band limit,

$$
qa\ll1,
$$

we have

$$
\sin(qa/2)\approx qa/2.
$$

So

$$
\frac{2}{qa}\sin(qa/2)\approx1,
$$

and

$$
v_a\approx\frac{c\cos\theta}{2}.
$$

As the band widens, the sampled density falls toward the two-beam mean and the
predicted speed rises toward the ordinary mean value.

---


# 14. Practical Fringe Scale

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
\Lambda\approx3.16\ \mathrm{mm}.
$$

The region satisfying

$$
u_{\mathrm{raw}}>3u_0
$$

obeys

$$
4u_0\cos^2\!\left(\frac{q\xi}{2}\right)>3u_0.
$$

Canceling $u_0$ gives

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

The full above-$3u_0$ width is

$$
w_{>3u_0}
=
\frac{2\pi}{3q}
=
\frac{\Lambda}{3}.
$$

For

$$
\Lambda\approx3.16\ \mathrm{mm},
$$

we get

$$
w_{>3u_0}\approx1.05\ \mathrm{mm}.
$$

A practical slit width is therefore

$$
a=0.25\ \mathrm{mm}
\quad\text{to}\quad
a=0.50\ \mathrm{mm},
$$

centered on a bright maximum.

---


# 15. Experimental Design

## 15.1 Apparatus

Minimum requirements:

- stable coherent laser source,
- amplitude modulation source,
- Mach-Zehnder or equivalent two-beam interferometer,
- controlled small recombination angle,
- stable straight fringes,
- spatial filter or slit selecting one bright ridge,
- reference beam path,
- equal downstream propagation length $L$ for reference and
  selected stripe,
- fast photodiodes,
- oscilloscope, lock-in amplifier, or phase-delay measurement system,
- variable path length or multiple known path lengths.


## 15.2 Procedure

1. Generate a coherent laser beam.
2. Apply sinusoidal amplitude modulation at angular frequency $\Omega$.
3. Split the beam into two equal arms.
4. Recombine the arms at small symmetric angle $\theta$.
5. Produce stable straight fringes.
6. Select the center of one bright fringe using a slit or spatial filter.
7. Let the selected bright stripe propagate over known distance
   $L$.
8. In parallel, propagate a reference beam over the same distance.
9. Detect both signals using matched photodiodes.
10. Measure the modulation phase delay of each channel relative to the common
    modulation source.
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


## 15.3 Predictions

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
v_{\mathrm{stripe}}\approx\frac{c\cos\theta}{2}.
$$

For small $\theta$,

$$
v_{\mathrm{stripe}}\approx\frac c2.
$$

Therefore

$$
m_{\mathrm{stripe}}\approx\frac{2}{c},
$$

while

$$
m_{\mathrm{ref}}\approx\frac{1}{c}.
$$

So

$$
\boxed{
m_{\mathrm{stripe}}\approx2m_{\mathrm{ref}}.
}
$$

Equivalently, for equal propagation distance $L$,

$$
\boxed{
\tau_{\mathrm{stripe}}-\tau_{\mathrm{ref}}\approx\frac{L}{c}.
}
$$

At

$$
L=1\ \mathrm{m},
$$

the predicted extra delay is

$$
\Delta\tau\approx3.34\ \mathrm{ns}.
$$

At

$$
L=10\ \mathrm{m},
$$

the predicted extra delay is

$$
\Delta\tau\approx33.4\ \mathrm{ns}.
$$

This is large enough to test with ordinary fast photodiodes and phase-sensitive
electronics.

---


# 16. Controls

## 16.1 Reference Beam

The reference beam should have:

- the same carrier frequency,
- the same modulation frequency,
- the same optical components where possible,
- the same downstream length $L$,
- similar detector electronics.


## 16.2 Single-Beam Slit Control

Send only one beam through the same slit geometry, with no interference. The
selected beam should propagate at the ordinary reference speed.

This checks that the slit itself is not producing the predicted delay.


## 16.3 Off-Bright Sampling

Move the slit away from the bright center. The loaded-branch prediction varies
with sampled density:

$$
v_a
=
\frac{J}{\bar u_a}.
$$

Thus lower-density bands should show smaller delay.

The standard prediction remains no density-dependent delay.


## 16.4 Fringe-Period Averaging

Open the aperture to collect an entire fringe period. The average density
returns to

$$
\langle u_{\mathrm{raw}}\rangle=2u_0.
$$

The loaded-branch anomaly should disappear under full-period collection.

This distinguishes local branch loading from ordinary total-power conservation.


## 16.5 Power Scaling

The prediction depends on coherent loading ratio, not absolute power, in the
proportional regime. Reducing both beam powers equally should reduce signal
amplitude but not change the predicted velocity ratio.

If the delay depends strongly on absolute optical power, thermal, detector, or
nonlinear-medium effects must be suspected.

---


# 17. Interpretation of Outcomes

## 17.1 Null Result

If

$$
v_{\mathrm{stripe}}=v_{\mathrm{ref}}
$$

within experimental error, then the isolated stripe behaves as ordinary
propagated output light. The raw local $4u_0$ density does not act as
a loaded branch with reduced effective advance.


## 17.2 Positive Result

If

$$
v_{\mathrm{stripe}}\approx\frac{v_{\mathrm{ref}}}{2}
$$

for a narrow bright-center stripe, and if the effect tracks the sampled density
as predicted, then the loaded-branch law is supported.

The result would indicate that coherent local density loading changes the
effective longitudinal advance of a surviving branch.


## 17.3 Intermediate Result

If

$$
v_{\mathrm{ref}}>v_{\mathrm{stripe}}>\frac{v_{\mathrm{ref}}}{2},
$$

then the selected stripe may not remain a pure raw bright branch. Partial
mixing, diffraction, finite aperture averaging, imperfect visibility, or
incomplete branch isolation may contribute.

In that case the measured velocity should be compared against the finite-band
prediction

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


# 18. Theoretical Fork

Both readings conserve total energy.

The disagreement is not about energy conservation. It is about how a selected
bright region transports energy.


## 18.1 Ordinary Output Transport

The recombiner output densities satisfy

$$
u_+(x)+u_-(x)=2u_0.
$$

At a bright center,

$$
u_+=2u_0.
$$

No speed reduction is required.


## 18.2 Loaded Raw-Overlap Transport

The selected bright stripe is identified with the raw overlap density:

$$
u_{\mathrm{raw,peak}}=4u_0.
$$

The available two-beam flux is

$$
J=2u_0c\cos\theta.
$$

Therefore

$$
v_{\mathrm{peak}}
=
\frac{J}{u_{\mathrm{raw,peak}}}
=
\frac{c\cos\theta}{2}.
$$

The experiment tests which reading describes the propagation of an isolated
bright stripe.

---


# 19. Summary

This proposal establishes:

1. Two equal coherent beams produce the raw density profile


   $$
   u_{\mathrm{raw}}(x)=4u_0\cos^2\!\left(\frac{qx}{2}\right).
   $$

2. The full fringe average is


   $$
   \langle u_{\mathrm{raw}}\rangle=2u_0,
   $$

   so the two-beam budget is conserved over a full period.

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

8. A longitudinal delay measurement of an isolated bright stripe directly
   distinguishes the two models.


The decisive experimental signature is

$$
\boxed{
m_{\mathrm{stripe}}\approx2m_{\mathrm{ref}}
}
$$

for a narrow bright-center stripe, where $m=d\tau/dL$ is the measured delay
slope.

---


# Appendix A — Compact Derivation of the Bright-Core Width

The above-$3u_0$ condition is

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

For $\Lambda\approx3.16\ \mathrm{mm}$,

$$
w_{>3u_0}\approx1.05\ \mathrm{mm}.
$$

A slit width of

$$
0.25\ \mathrm{mm}\le a\le0.50\ \mathrm{mm}
$$

samples the high-density bright core while avoiding neighboring low-density
regions.

---


# Appendix B — Finite-Band Velocity Formula

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

For $qa\ll1$,

$$
v_a\to\frac{c\cos\theta}{2}.
$$

For wider averaging, the sampled density decreases and $v_a$
increases toward the mean-pattern value.

---


# Appendix C — Status of the Claim

The derivations of the interference pattern, fringe average, output densities,
and longitudinal flux budget are standard wave calculations.

They prove:

$$
u_{\mathrm{raw}}(x)
=
4u_0\cos^2\!\left(\frac{qx}{2}\right),
$$

$$
\langle u_{\mathrm{raw}}\rangle=2u_0,
$$

and

$$
J_{\mathrm{in},z}=2u_0c\cos\theta.
$$

They do not by themselves prove reduced speed.

The reduced speed follows from the tested loaded-branch transport law

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

Thus the proposal is not merely a reinterpretation of a screen fringe. It is a
direct time-of-flight test between two alternatives:

$$
\boxed{
\text{ordinary output transport}
}
$$

and

$$
\boxed{
\text{loaded raw-overlap transport with }v_{\mathrm{eff}}=J/u.
}
$$
