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

Write two coherent portions of the same transporting flow in the conventional
electromagnetic variables

$$
\mathbf E_1,\ \mathbf B_1,
\qquad
\mathbf E_2,\ \mathbf B_2.
$$

At one point of overlap, the total field is

$$
\mathbf E=\mathbf E_1+\mathbf E_2,
\qquad
\mathbf B=\mathbf B_1+\mathbf B_2,
$$

so the local energy density is

$$
u
=
\frac{\epsilon}{2}|\mathbf E|^2
+
\frac{1}{2\mu}|\mathbf B|^2
=
u_1+u_2
+
\epsilon\,\mathbf E_1\!\cdot\!\mathbf E_2
+
\frac{1}{\mu}\,\mathbf B_1\!\cdot\!\mathbf B_2.
$$

These mixed terms are the interaction terms. If the two portions do not overlap
coherently, they are reduced and in general average out to zero.

For the strongest local case, take the two portions to have the same local
transport direction, the same polarization, and zero relative phase. Then

$$
\mathbf E_2=\mathbf E_1,
\qquad
\mathbf B_2=\mathbf B_1,
$$

so

$$
\mathbf E=2\mathbf E_1,
\qquad
\mathbf B=2\mathbf B_1,
$$

and therefore

$$
u
=
\frac{\epsilon}{2}|2\mathbf E_1|^2
+
\frac{1}{2\mu}|2\mathbf B_1|^2
=
4u_1.
$$

This is the rigorous local `4u` result.

Interpretation is straightforward once the transport picture is kept in view.
Take one isolated transporting portion over one transport interval
$\Delta t$. If its realized cross-section is $A$, then its
realized length over that interval is

$$
\ell = c\,\Delta t,
$$

so its realized volume is

$$
V=A\ell.
$$

If that portion carries energy $E$, then

$$
u_{\mathrm{independent}}=\frac{E}{V}=\frac{E}{A\ell}.
$$

Now imagine two such equal portions. If one simply concatenates the two flux
tubes, the resulting tube has the same cross-section $A$ but double
the length $2\ell$. That is the ordinary fluid picture. To keep the
inflow and outflow equal over the same time window, the fluid resolves the
doubled content by increasing its speed through the outlet.

But as earlier chapters recovered, energy transport proceeds at the fixed rate
$c$. Since there are no sinks, the transported content entering and
leaving over the same interval must still match. If the speed cannot increase,
then the remaining degree of freedom is density. Under coherent overlap, the
two separate flows are recovered as one common coherent wave transport. Before
overlap there are two independent channels, each advancing one realized
wave-volume $V=A\ell$ over the interval $\Delta t$. After coherent overlap,
there is only one surviving channel. That single wave now carries the merged
content of the two previous waves. The transported content per surviving wave
therefore doubles while the propagation speed remains fixed at $c$. The same
merged content must therefore be carried through the same section and in the
same interval by becoming denser.

Let each isolated closure carry energy

$$
E
$$

on realized extent

$$
V_1=A\ell_1,
$$

so

$$
u_{\mathrm{independent}}=\frac{E}{A\ell_1}.
$$

Before coherent overlap, the two independent portions therefore carry total
energy

$$
E_{\mathrm{initial}}=E_1+E_2=2E
$$

on total realized volume

$$
V_{\mathrm{initial}}=V_1+V_2=A(\ell_1+\ell_2)=2A\ell,
$$

so the initial mean density is

$$
\frac{E_{\mathrm{initial}}}{V_{\mathrm{initial}}}
=
\frac{2E}{2A\ell}
=
u_{\mathrm{independent}}.
$$

After coherent merger, the two flows no longer travel on two independent paths.
The merged content is recovered on one common path of the same cross-section
$A$. Over the same interval $\Delta t$, that surviving path advances only one
realized wave-volume

$$
V_{\mathrm{final}}=A\ell,
$$

so the number of realized transport channels has fallen from two to one, while
the total transported energy remains $2E$. The ratio between the previous total
wave-volume and the surviving wave-volume is

$$
\frac{V_{\mathrm{initial}}}{V_{\mathrm{final}}}=2
$$

So the merged mean density is

$$
u_{\mathrm{merge}}
=
\frac{E_1+E_2}{V_{\mathrm{final}}}
=
\frac{2E}{A\ell}
=
2u_{\mathrm{independent}}.
$$

This is the first bookkeeping consequence of the merge: the two flows add, and
because they are recovered on one common realized path at fixed transport speed,
the merged flow is denser.


## Effective-medium summary

Sometimes one wants a local summary of that loaded overlap region without
tracking each contributing portion separately. Then it is convenient to write
the exact overlap phenomenologically as a local effective index

$$

n_{\mathrm{eff}}>1, \qquad c_{\mathrm{eff}}=\frac{c}{n_{\mathrm{eff}}}.

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

\sin\theta_{\mathrm{in}} = n_{\mathrm{eff}}\sin\theta_{\mathrm{tr}}, \qquad
\theta_{\mathrm{in}}=\frac{\pi}{2},

$$

so

$$

\sin\theta_{\mathrm{tr}}=\frac{1}{n_{\mathrm{eff}}}.

$$

If $\beta$ denotes the complementary angle to the local tangent, then

$$

\beta=\frac{\pi}{2}-\theta_{\mathrm{tr}}, \qquad
\cos\beta=\frac{1}{n_{\mathrm{eff}}}, \qquad
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

\left|\gamma(s)-\gamma(s_{\mathrm{ret}})\right| = c\,(t-t_{\mathrm{ret}}).

$$

For a harmonic mode with period $T=2\pi/\omega$,

$$

E(s,t)=\Re\!\left[\widetilde E(s)e^{-i\omega t}\right], \qquad
B(s,t)=\Re\!\left[\widetilde B(s)e^{-i\omega t}\right],

$$

the retarded contribution can be written as

$$

E_{\mathrm{ret}}(s,t) = E(s_{\mathrm{ret}},t_{\mathrm{ret}}) =
\Re\!\left[\widetilde E(s_{\mathrm{ret}})e^{-i\omega t}e^{\,i\omega\tau}\right],
\qquad \tau=t-t_{\mathrm{ret}},

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
P_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}], \qquad H =
\frac{1}{\mu}B_{\mathrm{loc}} -
M_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}].

$$

In the thin, nearly uniform, slowly varying regime, linearize the exact retarded
response against the local field:

$$

P_{\mathrm{self}}\approx \epsilon\,\chi_{e,\mathrm{eff}}\,E_{\mathrm{loc}},
\qquad M_{\mathrm{self}}\approx \chi_{m,\mathrm{eff}}\,H.

$$

Then

$$

D \approx \epsilon_{\mathrm{eff}}E_{\mathrm{loc}}, \qquad B_{\mathrm{loc}}
\approx \mu_{\mathrm{eff}}H,

$$

with

$$

\epsilon_{\mathrm{eff}}=\epsilon(1+\chi_{e,\mathrm{eff}}), \qquad
\mu_{\mathrm{eff}}=\mu(1+\chi_{m,\mathrm{eff}}).

$$

Therefore

$$

c_{\mathrm{eff}} = \frac{1}{\sqrt{\mu_{\mathrm{eff}}\epsilon_{\mathrm{eff}}}},
\qquad n_{\mathrm{eff}} = \frac{c}{c_{\mathrm{eff}}} =
\sqrt{\frac{\mu_{\mathrm{eff}}\epsilon_{\mathrm{eff}}}{\mu\epsilon}} =
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
