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

These mixed terms are the interaction terms. If the two portions do not
overlap coherently, they are reduced and in general average out to zero.

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
If two ordinary fluid flows of similar cross-section are joined into an outlet
of similar cross-section, the fluid increases its speed at the outlet in order
to carry twice the incoming flow through the same section. But as earlier
chapters recovered, energy transport proceeds at the fixed rate $c$. In that
sense the exit speed is already controlled: the transport cannot simply move
faster to account for the added flow. Since energy is conserved, the remaining
way to carry more through the same realized section is greater energy density.

Let each isolated closure carry energy

$$
E
$$

on realized extent

$$
V,
$$

so

$$
u_{\mathrm{independent}}=\frac{E}{V}.
$$

The same point can be written directly in transport form. Through a local
section $A$ normal to the transport direction, the recovered power is

$$
P=u\,c\,A.
$$

This is the local transport capacity: area times speed times density. For one
isolated portion,

$$
P_1=u_{\mathrm{independent}}\,c\,A.
$$

If two equal portions are merged into one common section of the same area $A$,
then

$$
P_{\mathrm{final}}=P_1+P_2=2u_{\mathrm{independent}}\,c\,A.
$$

But the transport speed is still $c$ and the common section is still $A$, so

$$
P_{\mathrm{final}}=u_{\mathrm{merge}}\,c\,A
\qquad\Rightarrow\qquad
u_{\mathrm{merge}}=2u_{\mathrm{independent}}.
$$

So the merge by itself already gives the `2u` result. The exact local `4u`
law is the stronger overlap statement.

Now separate that exact local field readout from the bookkeeping of realized
extent. In this book, volume is not a primitive container. Organized energy
allows distance to be measured, and volume is the union of such measured
distances.

Before overlap, each realized extent $V_1,V_2$ carries the corresponding
energy $E_1,E_2$. For equal isolated closures,

$$
E_1=E_2=E,
\qquad
V_1=V_2=V,
\qquad
u_{\mathrm{independent}}=\frac{E_i}{V_i}.
$$

The initial total energy and volume are therefore

$$
E_{\mathrm{initial}}=E_1+E_2=2E,
\qquad
V_{\mathrm{initial}}=V_1+V_2=2V.
$$

So the initial mean realized density is

$$
\frac{E_{\mathrm{initial}}}{V_{\mathrm{initial}}}
=
\frac{2E}{2V}
=
u_{\mathrm{independent}}.
$$

After coherent overlap, the same total energy is realized on one common
extent,

$$
E_{\mathrm{final}}=2E,
\qquad
V_{\mathrm{final}}=V,
$$

so the merged mean density is

$$
\frac{E_{\mathrm{final}}}{V_{\mathrm{final}}}
=
\frac{2E}{V}
=
2u_{\mathrm{independent}}.
$$

This is the algebraic effect of the merge itself: two independent realized
extents become one common realized extent.

But the exact local field algebra above is stronger:

$$
u=4u_{\mathrm{independent}}.
$$

So the remaining bookkeeping question is simple: what realized volume carries
that `4u_{\mathrm{independent}}` readout? If that value is read as the
realized density of a bounded region carrying the full merged energy $2E$,
then conservation forces

$$
V_{\mathrm{occ}}
=
\frac{E_{\mathrm{final}}}{4u_{\mathrm{independent}}}
=
\frac{2E}{4E/V}
=
\frac{V}{2}.
$$

At the level of bookkeeping, this is analogous to an ideal pulley. A pulley
does not create work; it recovers greater force by reducing the distance
through which that force acts. Here too no new energy is created. The stronger
local loading is the same merged energy read on smaller extent.

So the strict derivation is this:

- the merge itself gives the mean density $2u_{\mathrm{independent}}$ on the common extent $V$,
- the exact local field algebra gives the stronger local readout $4u_{\mathrm{independent}}$,
- and if that stronger value is read as the realized density of a bounded
  region carrying the full merged energy, then the realized region
  must have measure $V/2$.

The algebra therefore fixes the concentration bookkeeping. What remains is the
physical reading of why the flow takes that smaller realized extent. The
proposed reading here is tangential closure stress in the same self-refracting
flow. Coherent overlap reinforces the closure-carrying tangential sectors, and
that reinforced closure is the proposed mechanism for the concentration just
derived.

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
