---
title: The Physics of Energy Flow - Self-Refraction
date: 2026-03-26
---

# 7b. Self-Refraction

Chapter 7 recovered the source-free wave equation, and chapter 7a resolved the
one transporting field into two complementary transverse aspects. That still
does not yet say how the same field could bend its own path.

The point of this chapter is that no second substrate is needed. One portion
of the same electromagnetic flow can alter the local transport law seen by a
later portion of that flow through retarded self-action. That is the
self-refraction principle.


## Retarded self-action of one flow on itself

Write those two aspects in their conventional electromagnetic variables

$$
\mathbf E,
\qquad
\mathbf B.
$$

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


## Constitutive writing

In ordinary media, one electromagnetic field modifies the local transport of
another through polarization and magnetization. Here the same mathematics is
used, but the response is produced by delayed portions of the same flow:

$$
D
=
\epsilon E_{\mathrm{loc}} + P_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}],
\qquad
H
=
\frac{1}{\mu}B_{\mathrm{loc}} - M_{\mathrm{self}}[E_{\mathrm{ret}},B_{\mathrm{ret}}].
$$

Nothing in this step assumes a closed path. It says only that the same flow
can act back on its later transport through its retarded fields.

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

So delayed portions of the same flow can increase the local refractive index
and lower the local transport speed.


## Local bending

Once different sides of a local wavefront are loaded differently, they do not
advance at the same speed. The more heavily self-loaded side moves more
slowly, so the transport bends toward it. That is refraction.

Approximating the local overlap region as a higher-index layer of the same
field, with exterior index $1$, and approximating the entering transport as
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

This is the local self-refraction law: stronger delayed self-loading means
larger $n_{\mathrm{eff}}$, stronger bending, and larger departure from a
straight transport line.


## What This Does and Does Not Yet Give

This chapter derives the principle, not yet the global shape.

It shows:

- how one portion of the electromagnetic flow can act back on a later portion
  of the same flow,
- how that retarded self-action can be written as a constitutive loading of the
  same field,
- and how that loading bends transport by ordinary refraction.

It does **not** yet require closure.

The next chapter takes the next step:

> if self-refraction becomes strong enough to make the path close on itself,
> what global standing organizations are then allowed?
