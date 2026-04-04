---
title: The Physics of Energy Flow - Self-Refraction
date: 2026-03-26
---

# 7b. Self-Refraction

Chapter 7 recovered source-free transport, and Chapter 7a resolved that
transport into two complementary transverse aspects. What remains is to
understand how a single field can bend its own path.

No second substrate is required. Distinct portions of the same transporting
field interact when they are realized on a common support. The question is how
this overlap modifies transport.


## Coherent overlap and quadratic loading

The local energy density is quadratic in the field. In the electromagnetic
writing recovered earlier, the local loading is of the form

$$
u \propto |\mathbf{E}|^2 + |\mathbf{B}|^2.
$$

So when two coherent contributions meet, the fields add first, and only then is
the local density evaluated.

If two equal contributions satisfy

$$
\mathbf{E}_2 = \mathbf{E}_1,
\qquad
\mathbf{B}_2 = \mathbf{B}_1,
$$

then the joined field is

$$
\mathbf{E}_{\mathrm{join}} = \mathbf{E}_1 + \mathbf{E}_2 = 2\mathbf{E}_1,
\qquad
\mathbf{B}_{\mathrm{join}} = \mathbf{B}_1 + \mathbf{B}_2 = 2\mathbf{B}_1.
$$

Therefore

$$
u_{\mathrm{join}}
=
|\mathbf{E}_{\mathrm{join}}|^2 + |\mathbf{B}_{\mathrm{join}}|^2
=
|2\mathbf{E}_1|^2 + |2\mathbf{B}_1|^2
=
4\big(|\mathbf{E}_1|^2 + |\mathbf{B}_1|^2\big).
$$

Hence

$$
u_{\mathrm{join}} = 4u_1.
$$

So two equal coherent contributions produce four times the local loading.


## Apparent paradox

At first sight, this seems to contradict conservation.

Two beams each carry the same transported content, and yet the joined beam is
described locally by a loading four times as large. No additional energy has
been introduced, so the result must reflect not the creation of new content but
a reorganization of how the same content is realized.

The resolution is that, in this framework, energy is not something contained in
a pre-given space. The realized extent of the field is part of what physically
exists. When two beams join, the field does not merely become stronger at the
same place. Its realized support also changes.


## Energy and support

Transport is described not only by what is carried, but by the support on which
it is carried.

Let $\Omega$ denote the realized support of a transporting portion over
a fixed interval $\Delta t$.

For a thin transport tube of cross section $A$ and realized length
$L$, define the geometric support by

$$
\Sigma(\Omega) := A L.
$$

Since transport proceeds at the fixed rate $c$,

$$
L = c\,\Delta t,
$$

so

$$
\Sigma(\Omega) = A c\,\Delta t.
$$

Let the transported content carried by that support be

$$
\mu(\Omega) := E.
$$

The mean support density is then

$$
\bar u(\Omega) := \frac{\mu(\Omega)}{\Sigma(\Omega)}.
$$

This is the amount of transported energy per unit realized support.


## Two independent beams

Before overlap, consider two equal beams on disjoint supports $\Omega_1$
and $\Omega_2$.

Each carries transported content

$$
\mu(\Omega_1)=\mu(\Omega_2)=E,
$$

and each has support

$$
\Sigma(\Omega_1)=\Sigma(\Omega_2)=\Sigma_0.
$$

The total initial support is therefore

$$
\Sigma_{\mathrm{initial}} = \Sigma(\Omega_1) + \Sigma(\Omega_2) = 2\Sigma_0,
$$

and the total transported content is

$$
\mu_{\mathrm{initial}} = \mu(\Omega_1)+\mu(\Omega_2)=2E.
$$

So the initial mean support density is

$$
\bar u_{\mathrm{initial}}
=
\frac{\mu_{\mathrm{initial}}}{\Sigma_{\mathrm{initial}}}
=
\frac{2E}{2\Sigma_0}
=
\frac{E}{\Sigma_0}.
$$


## Joining and support contraction

Now suppose the two beams are recovered on one common support
$\Omega_{\mathrm{final}}$.

The transported content is unchanged:

$$
\mu_{\mathrm{final}} = 2E.
$$

But the realized support is reduced:

$$
\Sigma_{\mathrm{final}} = \Sigma_0
=
\frac{1}{2}\Sigma_{\mathrm{initial}}.
$$

So the final mean support density is

$$
\bar u_{\mathrm{final}}
=
\frac{\mu_{\mathrm{final}}}{\Sigma_{\mathrm{final}}}
=
\frac{2E}{\Sigma_0}
=
2\bar u_{\mathrm{initial}}.
$$

Equivalently,

$$
\frac{2E}{\Sigma_{\mathrm{final}}}
=
\frac{2E}{\Sigma_{\mathrm{initial}}/2}
=
\frac{4E}{\Sigma_{\mathrm{initial}}},
\qquad
\Sigma_{\mathrm{final}}
=
\frac{1}{2}\Sigma_{\mathrm{initial}}.
$$

This is the exact support identity for the joined configuration.


## Resolution of the paradox

The fourfold local loading is now intelligible.

The same transported content is no longer realized on two disjoint supports. It
is recovered on one common support. That support contraction already doubles the
mean density:

$$
\bar u_{\mathrm{final}} = 2\bar u_{\mathrm{initial}}.
$$

The remaining factor of two comes from the two energy components.

So the full factor of four is not evidence of created energy. It is the local
expression of two simultaneous facts: twice the energy is transported on half
the realized support.

In this ontology, joining two beams makes the realized whole smaller by the
joined extent. The field is not being squeezed inside an unchanged container.
The realized extent of the field itself has been reduced.


## Effective advance

Transport along each realized path still proceeds at the local rate
$c$.

What changes is how much support is advanced over a fixed time interval.

Define the effective advance rate by

$$
c_{\mathrm{eff}} := \frac{\Sigma}{A\,\Delta t}.
$$

For the unloaded case,

$$
\Sigma_0 = A c\,\Delta t,
$$

so for a loaded support $\Sigma$ we obtain

$$
c_{\mathrm{eff}} = \frac{\Sigma}{\Sigma_0}\,c.
$$

Define the loading factor

$$
\lambda := \frac{\Sigma_0}{\Sigma}.
$$

Then

$$
c_{\mathrm{eff}} = \frac{c}{\lambda}.
$$

Since

$$
\bar u = \frac{\mu}{\Sigma},
\qquad
\bar u_0 = \frac{\mu}{\Sigma_0},
$$

it follows that

$$
\lambda = \frac{\bar u}{\bar u_0},
$$

and therefore

$$
c_{\mathrm{eff}} = c\,\frac{\bar u_0}{\bar u}.
$$


## Interpretation of effective speed

This result is exact and requires no additional mechanism.

The microscopic transport rate along each realized path remains
$c$.

But if the same transported content is recovered on less support, then less
support is advanced over the same time interval. That is what is measured as a
reduced effective speed.

So the point is not that more energy moves faster. It does not.

Rather:

- transported content increases relative to support,
- density increases,
- effective advance decreases.


If the mean support density doubles,

$$
\bar u = 2\bar u_0,
$$

then

$$
c_{\mathrm{eff}} = \frac{c}{2}.
$$

Thus higher loading corresponds to slower effective advance.


## Effective index

For compact writing, define an effective index by

$$
n_{\mathrm{eff}} := \frac{\bar u}{\bar u_0}.
$$

Then

$$
c_{\mathrm{eff}} = \frac{c}{n_{\mathrm{eff}}}.
$$

This does not introduce a new physical mechanism. It is only a summary of the
exact support-content bookkeeping:

- reduced support means higher density,
- higher density means lower effective advance.


## Local bending

If different regions of a wavefront have different loading, then they do not
advance equally.

- higher density implies lower $c_{\mathrm{eff}}$,
- lower density implies higher $c_{\mathrm{eff}}$.


So one side of the wavefront lags behind the other.

That lag bends the transport toward the more strongly loaded side.

This is refraction.

No external medium is required. The field bends because different parts of the
same flow carry different amounts of transported content per unit realized
support.


## Retarded self-overlap

In a self-interacting configuration, the overlap is not produced by two
independent laboratory beams. It is produced when a later portion of the same
flow enters a region already shaped by an earlier portion.

Let $\gamma(s)$ be a transport line. Then a point at $s$
interacts with earlier positions $s_{\mathrm{ret}}$ satisfying

$$
|\gamma(s)-\gamma(s_{\mathrm{ret}})| = c\,(t-t_{\mathrm{ret}}).
$$

For a harmonic field,

$$
E(s,t) = \Re\!\left[\widetilde E(s)e^{-i\omega t}\right],
$$

the retarded contribution is

$$
E_{\mathrm{ret}}(s,t)
=
\Re\!\left[\widetilde E(s_{\mathrm{ret}})e^{-i\omega t}e^{i\omega\tau}\right],
\qquad
\tau = t-t_{\mathrm{ret}}.
$$

So self-interaction appears as a phase-delayed contribution carried by the
earlier flow.

In coarse form, this may be summarized by writing

$$
D = \epsilon E_{\mathrm{loc}} + P_{\mathrm{self}},
\qquad
H = \frac{1}{\mu}B_{\mathrm{loc}} - M_{\mathrm{self}},
$$

with

$$
P_{\mathrm{self}} \approx \epsilon \chi_{e,\mathrm{eff}} E_{\mathrm{loc}},
\qquad
M_{\mathrm{self}} \approx \chi_{m,\mathrm{eff}} H.
$$

Then

$$
c_{\mathrm{eff}} = \frac{1}{\sqrt{\mu_{\mathrm{eff}}\epsilon_{\mathrm{eff}}}},
\qquad
n_{\mathrm{eff}} = \sqrt{(1+\chi_{e,\mathrm{eff}})(1+\chi_{m,\mathrm{eff}})}.
$$

This dielectric-style writing is only a coarse summary of the same retarded
support-loading effect.


## What this gives

This chapter establishes:

- coherent overlap produces quadratic local loading,
- the factor of four does not imply created energy,
- joining beams contracts realized support,
- support contraction raises density,
- raised density lowers effective advance,
- differential loading bends transport,
- self-refraction is retarded overlap of the same flow.


No second substrate is required.

The next step is global:

> when self-refraction is strong enough to close the path, what stable
> configurations are allowed?
