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

To state the overlap principle without changing ontology, use one local
amplitude of the transporting flow. Write that local amplitude as

$$
a(\mathbf r,t),
$$

normalized so that the observable local energy density is

$$
u=|a|^2.
$$

So the observable is quadratic in amplitude. Equivalently, $\sqrt{u}$ is an
amplitude scale, not a second density.

Now let two coherent portions of the same transporting flow contribute local
amplitudes

$$
a_1,
\qquad
a_2
$$

to the same transport channel.

Geometric crossing alone is not yet the strongest overlap. For substantial
coherent loading, the two portions must share a common local transport channel:
support overlap, compatible polarization, a definite phase relation, and a
nonzero common projection of the transport directions. If the local transport
directions fail to overlap coherently, the mixed term is reduced and in general
averages out to zero rather than building one merged loaded region.

In the aligned case, write the relative phase as $\Delta$ and the total local
amplitude as

$$
a=a_1+e^{i\Delta}a_2.
$$

Then

$$
u
=
|a|^2
=
|a_1|^2+|a_2|^2+2|a_1||a_2|\cos\Delta.
$$

Writing

$$
u_1:=|a_1|^2,
\qquad
u_2:=|a_2|^2,
$$

gives

$$
u=u_1+u_2+2\sqrt{u_1u_2}\cos\Delta.
$$

Under coherent overlap, if $\Delta=0$ and $u_1=u_2=u_0$, then

$$
u=(\sqrt{u_0}+\sqrt{u_0})^2=4u_0.
$$

This is the rigorous local `4u` result.

Now separate that exact local field readout from the energy bookkeeping of the
merged flow. Treat the overlapping objects not as two unrelated infinite waves
but as two equal closed portions of flow. Let each isolated closure carry

$$
E
$$

on occupied extent

$$
V,
$$

so

$$
u_0=\frac{E}{V}.
$$

Before overlap, the two closures occupy separate extents, so the total realized
energy and occupied extent are

$$
E_{\mathrm{initial}}=E_1+E_2=2E,
\qquad
V_{\mathrm{initial}}=V_1+V_2=2V.
$$

Therefore the mean occupied density before overlap is

$$
\frac{E_{\mathrm{initial}}}{V_{\mathrm{initial}}}
=
\frac{2E}{2V}
=
u_0.
$$

After coherent overlap, the same total energy is realized on one common extent

$$
V_{\mathrm{final}}=V,
\qquad
E_{\mathrm{final}}=2E,
$$

so the mean merged density is

$$
\frac{E_{\mathrm{final}}}{V_{\mathrm{final}}}
=
\frac{2E}{V}
=
2u_0.
$$

This is the algebraic effect of the merge itself: the second occupied extent no
longer enters the bookkeeping.

But the exact local amplitude algebra above is stronger:

$$
u=4u_0.
$$

So the next question is: in what occupied volume is that `4u_0` realized? If
that value is read as the realized density of a bounded occupied region
carrying the full merged energy $2E$, then conservation forces

$$
V_{\mathrm{occ}}
=
\frac{E_{\mathrm{final}}}{4u_0}
=
\frac{2E}{4E/V}
=
\frac{V}{2}.
$$

So the strict derivation is this:

- the merge itself gives the mean density $2u_0$ on the common extent $V$,
- the exact local amplitude algebra gives the stronger readout $4u_0$,
- and if that stronger value is read as the realized density of a bounded
  occupied region carrying the full merged energy, then the occupied region
  must have measure $V/2$.

What algebra alone does not supply is the dynamical agent that would make the
realized occupied region take that smaller value. The proposed agent here is
the tangential closure stress of the same self-refracting flow. Coherent
overlap reinforces the closure-carrying tangential sectors, and that
reinforced closure is the proposed physical reading of the algebraic
concentration just derived.

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
summary of the fact that the loaded overlap region advances more slowly than an
isolated portion would.


## Local bending

Once different sides of a local wavefront are loaded differently, they do not
advance at the same speed. The more heavily loaded side moves more slowly, so
the transport bends toward it. That is refraction.

Approximating the overlap region as a higher-index layer of the same field, with
exterior index $1$, and approximating the entering transport as
locally tangent to that layer, Snell's law gives

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
laboratory sources. It is produced when a later portion of the same flow enters
a region already shaped by an earlier portion of that same flow.

Let $\gamma(s)$ describe a local transport line, parameterized by arclength
$s$. A local segment at position $s$ interacts
causally with earlier source positions $s_{\mathrm{ret}}$ on the same flow,
related by

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

The retarded case is therefore not the definition of self-interaction. It is the
closure-relevant causal specialization of the overlap principle already derived
above.

In the retarded case one may write the same coarse-grained summary more
explicitly as

$$
D
=
\epsilon E_{\mathrm{loc}} + P_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}],
\qquad
H
=
\frac{1}{\mu}B_{\mathrm{loc}} - M_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}].
$$

In the thin, nearly uniform, slowly varying regime, linearize the exact retarded
response against the local field:

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

This recovers the same local refraction law, now written in the explicit causal
form relevant when the field bends back and meets its own earlier transport.


## What This Does and Does Not Yet Give

This chapter derives the principle, not yet the global shape.

It shows:

- how coherent overlap of distinct portions of the same field produces non-null
  interaction terms in the observables,
- how that overlap is summarized phenomenologically by a local effective
  refractive index,
- how the closure-relevant retarded case fits inside that more general
  self-interaction picture and can be written in dielectric form,
- and how that loading bends transport by ordinary refraction.


It does **not** yet require closure.

The next chapter takes the next step:

> if self-refraction becomes strong enough to make the path close on itself,
> what global standing organizations are then allowed?
