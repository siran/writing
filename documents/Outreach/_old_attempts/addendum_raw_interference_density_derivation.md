% Addendum — Rigorous Derivation of the Raw Interference Density
% An M. Rodriguez
% 2026-04-21

# Addendum — Rigorous Derivation of the Raw Interference Density

This addendum supplies two improvements to the proposal:

1. a revised prose-only abstract, avoiding equations and derivations;
2. a citeable appendix deriving the raw interference density step by step from standard wave interference.

The intended insertion point is near the beginning of the proposal, after the abstract and before the main theoretical fork.

---

# Revised Abstract

This proposal tests whether the bright center of a spatially isolated interference stripe propagates like an ordinary normalized optical output, or whether it behaves as a locally loaded branch whose effective longitudinal advance is reduced by its higher coherent energy density.

Two equal coherent beams are recombined at a small angle to produce stable straight fringes. Standard interference theory predicts a spatial redistribution of energy density: some regions become brighter than the two-beam mean while neighboring regions become darker, with total energy conserved over the full pattern. The proposed experiment isolates a narrow bright region and measures its modulation delay over a known longitudinal distance against a reference beam.

The standard expectation is that the isolated bright stripe propagates with the same delay as the reference beam, apart from ordinary geometric and aperture effects. The loaded-branch expectation is different: if the isolated bright region carries the available two-beam flux on a higher local density, then its effective advance must be slower. In the equal-beam bright-center limit, the predicted delay is approximately twice the reference delay.

The experiment is therefore a direct time-of-flight test between two readings of the same interference pattern: the standard normalized-output reading and the loaded raw-overlap branch reading.

---

# Suggested Abstract Sentence Replacement

Where the current abstract says:

> Standard interference gives a local raw overlap density
>
> $$
> u_{\mathrm{raw}}(x)=4u_0\cos^2\!\left(\frac{qx}{2}\right),
> $$

replace it with:

> Standard interference, derived explicitly in Appendix D below, gives a raw overlap pattern whose bright centers reach four times the single-beam density while the full fringe-period average remains equal to the two-beam budget.

This keeps the abstract as a summary and moves the derivation to a rigorous citeable section.

---

# Appendix D — Derivation of the Raw Interference Density from Standard Wave Theory

## D.1 Purpose

This appendix derives the raw interference density

$$
u_{\mathrm{raw}}(x)
=
4u_0\cos^2\!\left(\frac{qx}{2}\right)
$$

from standard linear wave interference.

The derivation uses only:

1. the source-free linear wave equation for a monochromatic field component,
2. linear superposition of two coherent equal-frequency solutions,
3. equal polarization,
4. the quadratic energy-density readout of the field amplitude.

No loaded-branch assumption is used in this appendix.

The loaded-branch hypothesis enters only later, when the proposal asks whether a selected bright region should propagate according to

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

---

## D.2 Source-Free Monochromatic Wave Component

In a source-free region, each Cartesian component of a transverse electromagnetic plane wave satisfies the scalar wave equation

$$
\nabla^2 f-\frac{1}{c^2}\partial_t^2 f=0.
$$

A monochromatic plane-wave solution can be written as

$$
f(\mathbf r,t)
=
A e^{i(\mathbf k\cdot\mathbf r-\omega t)},
$$

with dispersion relation

$$
\omega=c|\mathbf k|.
$$

The physical real field is the real part of this complex representation:

$$
f_{\mathrm{phys}}(\mathbf r,t)=\mathrm{Re}\,f(\mathbf r,t).
$$

The complex notation is only a bookkeeping device. Quadratic observables are computed from the appropriate time-averaged square of the physical field, or equivalently from the squared complex amplitude with a fixed normalization.

For this appendix, define the single-beam density by

$$
u_0:=C|A|^2,
$$

where $C>0$ contains the conventional electromagnetic normalization. For example, in the usual time-averaged electric-field convention, $C$ would contain factors such as $\varepsilon_0/2$ together with the magnetic contribution. Its exact value is not needed, because all ratios below are independent of $C$.

---

## D.3 Geometry of Two Symmetric Beams

Let the two equal beams cross symmetrically about the longitudinal $z$-axis in the $x$-$z$ plane.

Let the half-angle between each beam and the $z$-axis be $\theta$.

Then the wave vectors are

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

Both have the same magnitude:

$$
|\mathbf k_1|=|\mathbf k_2|=k.
$$

Thus both have the same angular frequency

$$
\omega=ck.
$$

Assume equal polarization and equal amplitude. Then the two complex field contributions may be written as

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

Then the relative phase between the two beams at fixed $z$ and $t$ is

$$
\Delta\phi(x)
=
(\mathbf k_1-\mathbf k_2)\cdot\mathbf r
=
2k\sin\theta\,x
=
qx.
$$

So $q$ is the transverse spatial phase gradient.

---

## D.4 Linear Superposition of the Fields

Because the source-free wave equation is linear, the sum of two solutions is also a solution:

$$
f_{\mathrm{raw}}=f_1+f_2.
$$

Substituting the two fields,

$$
f_{\mathrm{raw}}(x,z,t)
=
A e^{i(kx\sin\theta+kz\cos\theta-\omega t)}
+
A e^{i(-kx\sin\theta+kz\cos\theta-\omega t)}.
$$

Factor out the common longitudinal and temporal phase:

$$
f_{\mathrm{raw}}(x,z,t)
=
A e^{i(kz\cos\theta-\omega t)}
\left(
e^{ikx\sin\theta}+e^{-ikx\sin\theta}
\right).
$$

Use the identity

$$
e^{ia}+e^{-ia}=2\cos a.
$$

With

$$
a=kx\sin\theta,
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

this becomes

$$
\boxed{
f_{\mathrm{raw}}(x,z,t)
=
2A\cos\!\left(\frac{qx}{2}\right)
e^{i(kz\cos\theta-\omega t)}.
}
$$

This is the standard two-beam interference field before normalized beam-splitter output projection.

---

## D.5 Quadratic Density Readout

The raw density is proportional to the squared magnitude of the raw field amplitude:

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

The complex phase has unit magnitude:

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

we obtain

$$
\boxed{
u_{\mathrm{raw}}(x)
=
4u_0\cos^2\!\left(\frac{qx}{2}\right).
}
$$

This is the claimed raw overlap density.

---

## D.6 Equivalent Phase-Difference Derivation

The same result can be derived without specifying the crossing geometry.

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

The density is

$$
u_{\mathrm{raw}}
=
C|f_1+f_2|^2.
$$

Expand:

$$
|f_1+f_2|^2
=
(f_1+f_2)(f_1^*+f_2^*).
$$

Therefore

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
|A|^2 e^{i(\phi_1-\phi_2)},
$$

while

$$
f_1^*f_2
=
|A|^2 e^{-i(\phi_1-\phi_2)},
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

Thus

$$
\boxed{
u_{\mathrm{raw}}(x)
=
4u_0
\cos^2\!\left(\frac{qx}{2}\right).
}
$$

---

## D.7 Bright Centers, Nodes, and Bounds

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
\qquad n\in\mathbb Z.
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

So

$$
\boxed{
\Lambda=\frac{2\pi}{q}.
}
$$

Since

$$
q=2k\sin\theta
$$

and

$$
k=\frac{2\pi}{\lambda},
$$

we get

$$
\Lambda
=
\frac{2\pi}{2k\sin\theta}
=
\frac{\pi}{k\sin\theta}
=
\frac{\lambda}{2\sin\theta}.
$$

Thus

$$
\boxed{
\Lambda=\frac{\lambda}{2\sin\theta}.
}
$$

For small $\theta$,

$$
\sin\theta\approx\theta,
$$

so

$$
\Lambda\approx\frac{\lambda}{2\theta}.
$$

---

## D.8 Full-Period Mean Density

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

Thus

$$
\langle u_{\mathrm{raw}}\rangle
=
\frac{4u_0}{\Lambda}
\frac{2}{q}
\int_0^\pi\cos^2y\,dy.
$$

Using

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

Since

$$
\Lambda=\frac{2\pi}{q},
$$

we have

$$
q\Lambda=2\pi.
$$

Therefore

$$
\langle u_{\mathrm{raw}}\rangle
=
\frac{4\pi u_0}{2\pi}
=
2u_0.
$$

So

$$
\boxed{
\langle u_{\mathrm{raw}}\rangle=2u_0.
}
$$

This proves that the raw interference pattern conserves the two-beam density budget over a complete fringe period:

$$
u_0+u_0=2u_0.
$$

The local density is redistributed, not created.

---

## D.9 Forward Flux Budget

Each incoming beam has flux magnitude

$$
J_0=u_0c.
$$

Since each beam makes angle $\theta$ with the $z$-axis, its longitudinal projected flux is

$$
J_{0,z}=u_0c\cos\theta.
$$

For two equal symmetric beams,

$$
\boxed{
J_{\mathrm{in},z}=2u_0c\cos\theta.
}
$$

Dividing by the full-period mean density gives the mean longitudinal advance rate of the full interference pattern:

$$
\frac{J_{\mathrm{in},z}}{\langle u_{\mathrm{raw}}\rangle}
=
\frac{2u_0c\cos\theta}{2u_0}
=
c\cos\theta.
$$

Thus the full fringe-period average has the ordinary longitudinal projected speed:

$$
\boxed{
v_{\mathrm{mean}}=c\cos\theta.
}
$$

No anomalous delay follows from standard interference alone.

The anomalous prediction arises only if a selected bright branch is assigned the raw local density $u_{\mathrm{raw}}$ while carrying the available two-beam flux.

---

## D.10 Relation to Normalized Beam-Splitter Outputs

At a lossless 50/50 recombiner, the normalized output modes are

$$
f_+
=
\frac{f_1+f_2}{\sqrt2},
\qquad
f_-
=
\frac{f_1-f_2}{\sqrt2}.
$$

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

From the previous derivation,

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
u_+ + u_- = 2u_0.
}
$$

At a bright center of the $+$ output,

$$
u_+=2u_0,
\qquad
u_-=0.
$$

So the standard normalized-output channel has peak density $2u_0$, not $4u_0$.

This is the precise theoretical fork:

- the normalized-output reading assigns the bright output density $2u_0$;
- the raw loaded-branch reading assigns the isolated bright branch density $4u_0$.

Only the second reading predicts the reduced bright-center speed

$$
v_{\mathrm{peak}}
=
\frac{2u_0c\cos\theta}{4u_0}
=
\frac{c\cos\theta}{2}.
$$

---

## D.11 What This Appendix Proves

This appendix proves the standard interference identities:

$$
u_{\mathrm{raw}}(x)
=
4u_0\cos^2\!\left(\frac{qx}{2}\right),
$$

$$
0\le u_{\mathrm{raw}}\le 4u_0,
$$

$$
\langle u_{\mathrm{raw}}\rangle=2u_0,
$$

and

$$
J_{\mathrm{in},z}=2u_0c\cos\theta.
$$

It also proves that the standard normalized recombiner outputs satisfy

$$
u_+(x)+u_-(x)=2u_0.
$$

It does not assume or prove the loaded-branch transport law

$$
v_{\mathrm{eff}}=\frac{J}{u}.
$$

That law is the tested hypothesis of the proposal.

The experiment is therefore cleanly separated:

1. standard interference supplies the raw density pattern;
2. the loaded-branch law supplies the anomalous delay prediction;
3. the measurement decides whether the isolated bright stripe follows the standard normalized-output reading or the raw loaded-branch reading.
