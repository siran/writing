---
title: The Physics of Energy Flow - Self-Refraction
date: 2026-03-26
---

# 7b. Self-Refraction

Chapter 7 recovered the source-free wave equation, and chapter 7a resolved the
one transporting field into two complementary transverse aspects. That still
does not yet say how the same field could bend its own path.

The point of this chapter is that no second substrate is needed. Distinct
portions of the same electromagnetic flow interact directly when they meet as
one common field. Two coherent sources interfere for exactly that reason. The
question is what that overlap does to transport.


## Coherent overlap

Write those two aspects in their conventional electromagnetic variables

$$
\mathbf E,
\qquad
\mathbf B.
$$

Write two coherent portions of the same field as

$$
\mathbf E_1,\ \mathbf B_1,
\qquad
\mathbf E_2,\ \mathbf B_2.
$$

When they overlap, the observables are computed from the total field,

$$
\mathbf E=\mathbf E_1+\mathbf E_2,
\qquad
\mathbf B=\mathbf B_1+\mathbf B_2.
$$

So the local energy density is

$$
u
=
\frac{\epsilon}{2}|\mathbf E|^2
+
\frac{1}{2\mu}|\mathbf B|^2
$$

that is,

$$
u
=
u_1+u_2
+
\epsilon\,\mathbf E_1\!\cdot\!\mathbf E_2
+
\frac{1}{\mu}\,\mathbf B_1\!\cdot\!\mathbf B_2.
$$

Likewise the energy flux is

$$
\mathbf S
=
\frac{1}{\mu}\,\mathbf E\times\mathbf B
$$

so

$$
\mathbf S
=
\mathbf S_1+\mathbf S_2
+
\frac{1}{\mu}\,\mathbf E_1\times\mathbf B_2
+
\frac{1}{\mu}\,\mathbf E_2\times\mathbf B_1.
$$

These cross terms are the interaction terms. They are not added by hand. They
appear because overlapping portions of the same field are read as one common
field.

For in-phase coherent overlap, the energy cross terms are non-null. The
overlap region is therefore more heavily loaded than either isolated portion.
In that sense, one region of the field acts for another as a denser
electromagnetic medium.

If the exact overlapping fields are kept, nothing further is needed. The
interaction is already present in the total-field observables written above.
There is no second additive law for energy. The addition law is linear at the
level of the fields, and the energy observable is quadratic in that total
field.

Energy is additive when the two portions occupy disjoint regions or orthogonal
transport modes. But once coherent portions occupy the same region in the same
mode, the quadratic observable need not split into separately additive parts.
That result can feel strange, but it is not peculiar to electromagnetism. It
is a standard fact of wave mechanics: amplitudes add, and the local load read
from their square can become large enough to produce effects not present in
either part taken alone.

The head-on case gives a simple exact example. If two equal coherent portions
move toward one another, then at a point where their electric sectors add one
has

$$
\mathbf E_2=\mathbf E_1,
\qquad
\mathbf B_2=-\mathbf B_1,
$$

so

$$
u=2u_1,
\qquad
\mathbf S=0.
$$

There the local loading doubles while the flux cancels. The total energy of
the two approaching regions remains

$$
E_{\mathrm{tot}}=E_A+E_B.
$$

The co-propagating recombination case must be read just as carefully. In
passive optics, take an ideal symmetric lossless 50/50 combiner and write its
two outputs as

$$
\mathbf E_\pm=\alpha(\mathbf E_A\pm \mathbf E_B),
\qquad
\mathbf B_\pm=\alpha(\mathbf B_A\pm \mathbf B_B).
$$

The coefficient is fixed by losslessness. If only input $A$ is present, then

$$
\mathbf E_+=\alpha\mathbf E_A,
\qquad
\mathbf E_-=\alpha\mathbf E_A,
$$

and likewise for $\mathbf B$. Each output therefore carries local loading

$$
u_\pm=\alpha^2 u_A.
$$

Since the combiner is lossless and splits symmetrically,

$$
u_+ + u_- = u_A,
$$

so

$$
2\alpha^2=1,
\qquad
\alpha=\frac{1}{\sqrt2}.
$$

Therefore

$$
\mathbf E_\pm=\frac{\mathbf E_A\pm \mathbf E_B}{\sqrt2},
\qquad
\mathbf B_\pm=\frac{\mathbf B_A\pm \mathbf B_B}{\sqrt2}.
$$

If the two inputs are equal and in phase, then

$$
\mathbf E_+=\sqrt2\,\mathbf E_A,
\qquad
\mathbf E_-=0,
$$

and likewise for $\mathbf B$. The bright output therefore carries

$$
u_+=2u_A,
\qquad
\mathbf S_+=2\mathbf S_A,
$$

while the dark output carries none. So passive recombination conserves the
total energy exactly. The apparent $4u$ paradox comes from treating two fully
overlapped non-orthogonal contributions as though they still carried the same
separately additive energies they had before recombination.

This is one reason interference has often been spoken of as though a quantum
of light could interfere only with itself. But the underlying mathematical
fact is more general and more ordinary: whenever wave amplitudes combine
coherently, the quadratic observables need not add term by term.

The overlap itself is the effect.


## Effective-medium summary

Sometimes one wants a local summary of that loaded overlap region without
tracking each contributing portion separately. Then it is convenient to write
the exact overlap phenomenologically as a local effective index

$$
n_{\mathrm{eff}}>1,
\qquad
c_{\mathrm{eff}}=\frac{c}{n_{\mathrm{eff}}}.
$$

This does not replace the exact superposition above. It is only a compact
summary of the fact that the loaded overlap region advances more slowly than
an isolated portion would.


## Local bending

Once different sides of a local wavefront are loaded differently, they do not
advance at the same speed. The more heavily loaded side moves more slowly, so
the transport bends toward it. That is refraction.

Approximating the overlap region as a higher-index layer of the same field,
with exterior index $1$, and approximating the entering transport as locally
tangent to that layer, Snell's law gives

$$
\sin\theta_{\mathrm{in}}
=
n_{\mathrm{eff}}\sin\theta_{\mathrm{tr}},
\qquad
\theta_{\mathrm{in}}=\frac{\pi}{2},
$$

so

$$
\sin\theta_{\mathrm{tr}}=\frac{1}{n_{\mathrm{eff}}}.
$$

If $\beta$ denotes the complementary angle to the local tangent, then

$$
\beta=\frac{\pi}{2}-\theta_{\mathrm{tr}},
\qquad
\cos\beta=\frac{1}{n_{\mathrm{eff}}},
\qquad
\tan\beta=\sqrt{n_{\mathrm{eff}}^2-1}.
$$

This is the local self-refraction law: stronger coherent loading means larger
$n_{\mathrm{eff}}$, stronger bending, and larger departure from a straight
transport line.


## The retarded case

For a self-refracting closure, the overlap is not produced by two independent
laboratory sources. It is produced when a later portion of the same flow
enters a region already shaped by an earlier portion of that same flow.

Let $\gamma(s)$ describe a local transport line, parameterized by arclength
$s$. A local segment at position $s$ interacts causally with earlier source
positions $s_{\mathrm{ret}}$ on the same flow, related by

$$
\left|\gamma(s)-\gamma(s_{\mathrm{ret}})\right|
=
c\,(t-t_{\mathrm{ret}}).
$$

For a harmonic mode with period $T=2\pi/\omega$,

$$
E(s,t)=\Re\!\left[\widetilde E(s)e^{-i\omega t}\right],
\qquad
B(s,t)=\Re\!\left[\widetilde B(s)e^{-i\omega t}\right],
$$

the retarded contribution can be written as

$$
E_{\mathrm{ret}}(s,t)
=
E(s_{\mathrm{ret}},t_{\mathrm{ret}})
=
\Re\!\left[\widetilde E(s_{\mathrm{ret}})e^{-i\omega t}e^{\,i\omega\tau}\right],
\qquad
\tau=t-t_{\mathrm{ret}},
$$

and likewise for $B_{\mathrm{ret}}$. So the retarded self-action enters as a
phase lag $\omega\tau$ carried by earlier portions of the same flow.

The retarded case is therefore not the definition of self-interaction. It is
the closure-relevant causal specialization of the overlap principle already
derived above.

In the retarded case one may write the same coarse-grained summary more explicitly
as

$$
D
=
\epsilon E_{\mathrm{loc}} + P_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}],
\qquad
H
=
\frac{1}{\mu}B_{\mathrm{loc}} - M_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}].
$$

In the thin, nearly uniform, slowly varying regime, linearize the exact
retarded response against the local field:

$$
P_{\mathrm{self}}\approx \epsilon\,\chi_{e,\mathrm{eff}}\,E_{\mathrm{loc}},
\qquad
M_{\mathrm{self}}\approx \chi_{m,\mathrm{eff}}\,H.
$$

Then

$$
D \approx \epsilon_{\mathrm{eff}}E_{\mathrm{loc}},
\qquad
B_{\mathrm{loc}} \approx \mu_{\mathrm{eff}}H,
$$

with

$$
\epsilon_{\mathrm{eff}}=\epsilon(1+\chi_{e,\mathrm{eff}}),
\qquad
\mu_{\mathrm{eff}}=\mu(1+\chi_{m,\mathrm{eff}}).
$$

Therefore

$$
c_{\mathrm{eff}}
=
\frac{1}{\sqrt{\mu_{\mathrm{eff}}\epsilon_{\mathrm{eff}}}},
\qquad
n_{\mathrm{eff}}
=
\frac{c}{c_{\mathrm{eff}}}
=
\sqrt{\frac{\mu_{\mathrm{eff}}\epsilon_{\mathrm{eff}}}{\mu\epsilon}}
=
\sqrt{(1+\chi_{e,\mathrm{eff}})(1+\chi_{m,\mathrm{eff}})}.
$$

This recovers the same local refraction law, now written in the explicit
causal form relevant when the field bends back and meets its own earlier
transport.


## What This Does and Does Not Yet Give

This chapter derives the principle, not yet the global shape.

It shows:

- how coherent overlap of distinct portions of the same field produces
  non-null interaction terms in the observables,
- how that overlap is summarized phenomenologically by a local effective
  refractive index,
- how the closure-relevant retarded case fits inside that more general
  self-interaction picture and can be written in dielectric form,
- and how that loading bends transport by ordinary refraction.

It does **not** yet require closure.

The next chapter takes the next step:

> if self-refraction becomes strong enough to make the path close on itself,
> what global standing organizations are then allowed?
