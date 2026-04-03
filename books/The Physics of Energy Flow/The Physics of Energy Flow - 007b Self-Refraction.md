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
one common field. The question is what that overlap does to transport.


## Coherent overlap

Because the local loading is positive, write it as the square of a local
amplitude-like quantity:

$$
u = |f|^2.
$$

Let two coherent portions of the same transporting flow contribute amplitudes

$$
f_1,
\qquad
f_2
$$

to one common transport channel. Then the combined amplitude is

$$
f = f_1 + f_2,
$$

so the local loading is

$$
u
=
|f_1+f_2|^2
=
|f_1|^2+|f_2|^2+2|f_1||f_2|\cos\Delta.
$$

Writing

$$
u_1 := |f_1|^2,
\qquad
u_2 := |f_2|^2,
$$

gives

$$
u = u_1 + u_2 + 2\sqrt{u_1u_2}\cos\Delta.
$$

The mixed term is the interaction term. If the two portions do not overlap
coherently, it is reduced and in general averages out to zero.

For the strongest local case, take equal amplitudes in the same local transport
direction with zero relative phase. Then

$$
f_2 = f_1,
\qquad
\Delta = 0,
$$

so

$$
u
=
|2f_1|^2
=
4u_1.
$$

This is the rigorous local `4u` result.


## The joined-channel picture

The transport bookkeeping is easiest to see by thinking of two conveyor belts
that join into one. The picture is only about carried content and realized path
length, not about a second material substance.

Take one isolated transporting portion over one transport interval
$\Delta t$. If its realized cross-section is $A$, then its realized
length over that interval is

$$
\ell = c\,\Delta t.
$$

If that portion carries energy $E$, then its realized wave-volume is

$$
V = A\ell,
$$

and its mean density is

$$
u_{\mathrm{independent}} = \frac{E}{A\ell}.
$$

Now imagine two such equal channels. Before they join, the total transported
energy is

$$
E_{\mathrm{initial}} = E_1 + E_2 = 2E,
$$

and the total realized wave-volume over the same interval is

$$
V_{\mathrm{initial}} = A\ell + A\ell = 2A\ell.
$$

So the initial mean density is still

$$
\frac{E_{\mathrm{initial}}}{V_{\mathrm{initial}}}
=
\frac{2E}{2A\ell}
=
u_{\mathrm{independent}}.
$$

Now let the two channels join into one common channel of the same
cross-section $A$. Because transport along that joined channel still
proceeds at the fixed rate $c$, the surviving channel advances only one
realized length $\ell$ during the same interval $\Delta t$. Its
realized wave-volume is therefore

$$
V_{\mathrm{join}} = A\ell.
$$

But it must now carry the merged content of both prior channels:

$$
E_{\mathrm{join}} = 2E.
$$

So the mean density on the joined channel is

$$
u_{\mathrm{join}}
=
\frac{E_{\mathrm{join}}}{V_{\mathrm{join}}}
=
\frac{2E}{A\ell}
=
2u_{\mathrm{independent}}.
$$

This is the clean `2u` result. Nothing has been created. The same transported
content is now recovered on one surviving channel rather than on two.


## Relation to the exact `4u` result

The joined-channel result and the exact coherent-overlap result are not rivals.
They refer to two different parts of the same event.

The joined-channel bookkeeping says:

- two equal carried contents $E$ become $2E$ on one realized channel,
- the surviving channel still advances at the fixed rate $c$,
- so the mean density on that surviving channel doubles.


That gives the clean transport result

$$
u_{\mathrm{join}} = 2u_{\mathrm{independent}}.
$$

The stronger local result

$$
u = 4u_1
$$

belongs to the coherent field overlap itself. Once the two equal contributions
share one common channel and remain phase-aligned, amplitudes add before the
observable is squared. That gives the second factor of two.

So the interpretation is:

- channel merger gives one factor of $2$,
- coherent quadratic loading gives the second factor of $2$,
- together they yield the exact local `4u` overlap result.


If coherence is lost, the second factor is reduced and can average away. The
joined-channel factor does not depend on that phase alignment.


## Effective-medium summary

Sometimes one wants a compact local summary of the loaded overlap region without
tracking each contributing portion separately. Then it is convenient to write
the exact overlap phenomenologically as a local effective index

$$
n_{\mathrm{eff}} > 1,
\qquad
c_{\mathrm{eff}} = \frac{c}{n_{\mathrm{eff}}}.
$$

This does not replace the exact superposition or the joined-channel
bookkeeping above. Nor does it say that the underlying transport ceases to move
locally at $c$. It says only that the loaded region, treated as one
effective channel, advances more slowly as a pattern than an isolated portion
would. That is the coarse-grained meaning of $c_{\mathrm{eff}}$.


## Local bending

Once different sides of a local wavefront are loaded differently, they do not
advance at the same effective rate. The more heavily loaded side has larger
$n_{\mathrm{eff}}$, smaller $c_{\mathrm{eff}}$, and therefore lags. The
transport bends toward it. That is refraction.

Approximating the overlap region as a higher-index layer of the same field, with
exterior index $1$, and approximating the entering transport as
locally tangent to that layer, Snell's law gives

$$
\sin\theta_{\mathrm{in}} = n_{\mathrm{eff}}\sin\theta_{\mathrm{tr}},
\qquad
\theta_{\mathrm{in}} = \frac{\pi}{2},
$$

so

$$
\sin\theta_{\mathrm{tr}} = \frac{1}{n_{\mathrm{eff}}}.
$$

If $\beta$ denotes the complementary angle to the local tangent, then

$$
\beta = \frac{\pi}{2}-\theta_{\mathrm{tr}},
\qquad
\cos\beta = \frac{1}{n_{\mathrm{eff}}},
\qquad
\tan\beta = \sqrt{n_{\mathrm{eff}}^2-1}.
$$

This is the local self-refraction law: stronger loading means larger
$n_{\mathrm{eff}}$, stronger bending, and larger departure from a straight
transport line.


## The retarded case

For a self-refracting closure, the overlap is not produced by two independent
laboratory sources. It is produced when a later portion of the same flow enters
a region already shaped by an earlier portion of that same flow.

Let $\gamma(s)$ describe a local transport line, parameterized by arclength
$s$. A local segment at position $s$ interacts causally with earlier
source positions $s_{\mathrm{ret}}$ on the same flow, related by

$$
\left|\gamma(s)-\gamma(s_{\mathrm{ret}})\right| = c\,(t-t_{\mathrm{ret}}).
$$

For a harmonic mode with period $T=2\pi/\omega$,

$$
E(s,t) = \Re\!\left[\widetilde E(s)e^{-i\omega t}\right],
\qquad
B(s,t) = \Re\!\left[\widetilde B(s)e^{-i\omega t}\right],
$$

the retarded contribution can be written as

$$
E_{\mathrm{ret}}(s,t)
=
E(s_{\mathrm{ret}},t_{\mathrm{ret}})
=
\Re\!\left[\widetilde E(s_{\mathrm{ret}})e^{-i\omega t}e^{\,i\omega\tau}\right],
\qquad
\tau = t-t_{\mathrm{ret}},
$$

and likewise for $B_{\mathrm{ret}}$. So the retarded self-action enters as a
phase lag $\omega\tau$ carried by earlier portions of the same flow.

The retarded case is therefore not the definition of self-interaction. It is the
closure-relevant causal specialization of the overlap principle already derived
above.

In the retarded case one may write the same coarse-grained summary more
explicitly as

$$
D = \epsilon E_{\mathrm{loc}} +
P_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}],
\qquad
H = \frac{1}{\mu}B_{\mathrm{loc}} -
M_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}].
$$

In the thin, nearly uniform, slowly varying regime, linearize the exact retarded
response against the local field:

$$
P_{\mathrm{self}} \approx \epsilon\,\chi_{e,\mathrm{eff}}\,E_{\mathrm{loc}},
\qquad
M_{\mathrm{self}} \approx \chi_{m,\mathrm{eff}}\,H.
$$

Then

$$
D \approx \epsilon_{\mathrm{eff}}E_{\mathrm{loc}},
\qquad
B_{\mathrm{loc}} \approx \mu_{\mathrm{eff}}H,
$$

with

$$
\epsilon_{\mathrm{eff}} = \epsilon(1+\chi_{e,\mathrm{eff}}),
\qquad
\mu_{\mathrm{eff}} = \mu(1+\chi_{m,\mathrm{eff}}).
$$

Therefore

$$
c_{\mathrm{eff}} = \frac{1}{\sqrt{\mu_{\mathrm{eff}}\epsilon_{\mathrm{eff}}}},
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
- how joining two equal transport channels into one same-speed channel gives the
  clean `2u` density increase,
- how the exact coherent case gives the stronger local `4u` result,
- how that loading is summarized phenomenologically by a local effective
  refractive index,
- how the closure-relevant retarded case fits inside that more general
  self-interaction picture and can be written in dielectric form,
- and how that loading bends transport by ordinary refraction.


It does **not** yet require closure.

The next chapter takes the next step:

> if self-refraction becomes strong enough to make the path close on itself,
> what global standing organizations are then allowed?
