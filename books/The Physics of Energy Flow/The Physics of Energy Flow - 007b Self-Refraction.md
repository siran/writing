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

Because the loading is positive, it can be written as the square of an
amplitude-like quantity:

$$
u = |f|^2.
$$

Let two coherent contributions of the same transporting flow be

$$
f_1,
\qquad
f_2.
$$

When they join, the amplitudes add first:

$$
f_{\mathrm{join}} = f_1 + f_2.
$$

So the joined local loading is

$$
u_{\mathrm{join}}
=
|f_{\mathrm{join}}|^2
=
|f_1+f_2|^2
=
|f_1|^2 + |f_2|^2 + 2|f_1||f_2|\cos\delta,
$$

where $\delta$ is the relative phase between the two flows,
$f_1$ and $f_2$.

Writing

$$
u_1 := |f_1|^2,
\qquad
u_2 := |f_2|^2,
$$

gives

$$
u_{\mathrm{join}} = u_1 + u_2 + 2\sqrt{u_1u_2}\cos\delta.
$$

For equal contributions,

$$
u_1 = u_2 = u_0,
$$

so

$$
u_{\mathrm{join}} = 2u_0(1+\cos\delta).
$$

Therefore

$$
0 \le u_{\mathrm{join}} \le 4u_0.
$$

In the "strongest" local case, the two contributions are in phase:

$$
\delta = 0.
$$

So the energy of the joined flow becomes

$$
u_{\mathrm{join}} = 4u_0.
$$

In the "weakest" local case, the two contributions are out of phase:

$$
\delta = \pi.
$$

And so the resulting energy is apparently gone,

$$
u_{\mathrm{join}} = 0.
$$

So two equal coherent contributions can range from full cancellation to a
fourfold local loading, with the exact $4u$ result at perfect phase
alignment.


## Apparent paradox

At first sight, this seems to contradict conservation.

If we picture the flow in conventional electromagnetic language, as was shown in
preceding sections, the energy flow F is an electromagnetic wave: one energy
flow whose two orthogonal aspects are conventionally called $\mathbf E$ and
$\mathbf B$.

Say two such energy flow waves carry the same transported energy content, and
there is a region in which these flows are joined. Since no additional energy
has been introduced, the result must reflect not the creation of new content but
a reorganization of how the same content is realized.

The bookkeeping is easier to picture with a concrete analogy. We can think of
the way energy is reorganized in double-curl transport as a chain of containers
carrying one unit of ordinary liquid (energy) passing to the next container.
Before joining, there are two containers carrying two units in total. After
overlapping coherently (same phase), there is one surviving chain of container
that must carry the double fluid content of the joined chains. If one container
normally carries one unit, then two units do not fit into one unchanged
container. The liquid would have to be compressed in order to fit.

That is the point of the support language below. When two beams join, the field
does not merely become stronger at the same place. The same transported content
is recovered on a smaller realized extent.


## Energy and support

The analogy above is only a picture. The actual explanation comes from
continuity.

The square form

$$
u = |f|^2
$$

does not explain why the joined flow becomes denser. It only makes the
interaction term visible and counts the local joined state once that state is
already given.

The physical explanation is simpler: if there are no primitive sources or
sinks, then whatever enters the overlap region must be accounted for by what
leaves it. If two inflows become one outflow, the same transported content must
be recovered on one surviving channel.

To write that bookkeeping explicitly, let $\Omega$ denote the realized support
of a transporting portion over a fixed interval $\Delta t$.

For a thin transport tube of cross section $A$ and realized length $L$, define
the geometric support by

$$
\Sigma(\Omega) := A L.
$$

Since transport proceeds at the fixed rate $c$,

$$
L = c\,\Delta t,
\qquad
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

This is the amount of transported energy recovered per unit realized support.


## Two inflows, one outflow

Before overlap, consider two equal inflows on disjoint supports
$\Omega_1$ and $\Omega_2$:

$$
\mu(\Omega_1)=\mu(\Omega_2)=E,
\qquad
\Sigma(\Omega_1)=\Sigma(\Omega_2)=\Sigma_0.
$$

So the total incoming content is

$$
\mu_{\mathrm{in}} = 2E,
$$

and the total incoming support is

$$
\Sigma_{\mathrm{initial}}
=
\Sigma(\Omega_1)+\Sigma(\Omega_2)
=
2\Sigma_0.
$$

Therefore the incoming mean density is

$$
\bar u_{\mathrm{initial}}
=
\frac{\mu_{\mathrm{in}}}{\Sigma_{\mathrm{initial}}}
=
\frac{2E}{2\Sigma_0}
=
\frac{E}{\Sigma_0}.
$$

Now let those two inflows be recovered on one surviving outflow over the same
interval. Then there is only one realized support left:

$$
\Sigma_{\mathrm{final}}
=
\Sigma_0
=
\frac{1}{2}\Sigma_{\mathrm{initial}}.
$$

But continuity forbids any loss of the transported content, so the outgoing
content must still be

$$
\mu_{\mathrm{out}} = 2E.
$$

Therefore the outgoing mean density is

$$
\bar u_{\mathrm{final}}
=
\frac{\mu_{\mathrm{out}}}{\Sigma_{\mathrm{final}}}
=
\frac{2E}{\Sigma_0}
=
\frac{4E}{\Sigma_{\mathrm{initial}}}
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

The mathematics above still explains nothing. It only counts what the joined
configuration looks like once written as a square.

The physical explanation is continuity:

- there are two equal inflows,
- there is one surviving outflow,
- no primitive source or sink may remove the difference,
- so the same total content must be recovered by compression on that one
  outflow.

That is the only physical doubling in the argument. The same transported
content that had been realized on two inflows is now realized on one outflow,
so the mean density must double:

$$
\bar u_{\mathrm{final}} = 2\bar u_{\mathrm{initial}}.
$$

The square form

$$
u = |f|^2
$$

does not add a second mechanism. It only makes the interaction term visible and
counts the local joined state. In the perfectly aligned case that local
counting reaches the exact endpoint

$$
u_{\mathrm{join}} = 4u_0.
$$

So the full `4u` result is not evidence of created energy. It is the local
reading of one compressed superposed outflow that must account for what had
previously been carried on two inflows.

In the glass picture, the same two units once carried by two glasses are now
recovered on one surviving glass. In the field language, the realized extent
itself has been reduced.


## Effective advance

Transport along each realized path still proceeds at the local rate
$c$.

What changes is the lag of the joined outflow when compared with isolated
transport. Over the same interval, one loaded outflow now replaces what had
previously been two independent inflows.

If one wants a compact summary of that lag without carrying the full inflow and
outflow bookkeeping every time, it is convenient to write an effective advance
rate

$$
c_{\mathrm{eff}} < c
$$

and a corresponding effective index

$$
n_{\mathrm{eff}} := \frac{c}{c_{\mathrm{eff}}} > 1.
$$

This is not the explanation of the effect. It is only the compact language for
the lag produced by continuity under superposition.

One convenient local summary is to use the density ratio

$$
n_{\mathrm{eff}} := \frac{\bar u}{\bar u_0},
\qquad
c_{\mathrm{eff}} = \frac{c}{n_{\mathrm{eff}}}.
$$

When the mean density doubles,

$$
\bar u = 2\bar u_0,
$$

this summary reads

$$
c_{\mathrm{eff}} = \frac{c}{2}.
$$


## Interpretation of effective speed

The microscopic transport rate along each realized path remains
$c$.

But if two inflows are recovered on one outflow, then the joined pattern lags
relative to the unloaded case. In coarse-grained language that lag is written
as a reduced effective advance.

So the point is not that more energy moves faster. It does not. The point is
that continuity forces the same total content through one surviving channel.
That compression is what the reduced effective advance is summarizing.


## Effective index

The effective index is therefore not a second mechanism. It is the compact way
to write that more strongly superposed regions lag more strongly than weakly
loaded ones.


## Proportional background response

There is also a direct local route to the same effective advance.

Treat the second contribution not as a second independent substance but as the
background response induced by the first. In the same way one writes

$$
P = \chi E,
$$

write the reinforcing response of the same flow as

$$
f_2 = k f_1,
\qquad
k \ge 0.
$$

Then the joined flow is

$$
f_{\mathrm{tot}}
=
f_1 + f_2
=
(1+k)f_1.
$$

So the joined local loading is

$$
u_{\mathrm{tot}}
=
|f_{\mathrm{tot}}|^2
=
|1+k|^2 |f_1|^2
=
(1+k)^2 u_1.
$$

In the reinforcing case it is therefore natural to write

$$
n_{\mathrm{eff}} := 1+k.
$$

Then

$$
u_{\mathrm{tot}} = n_{\mathrm{eff}}^2 u_1.
$$

Continuity then gives the matching lag statement: if one surviving outflow must
recover what is now loaded by the factor $n_{\mathrm{eff}}$, the effective
advance is

$$
c_{\mathrm{eff}} = \frac{c}{n_{\mathrm{eff}}}.
$$

So the proportional-response shortcut closes the same circle:

$$
f_2 = kf_1
\quad\Longrightarrow\quad
f_{\mathrm{tot}} = (1+k)f_1
\quad\Longrightarrow\quad
u_{\mathrm{tot}} = (1+k)^2u_1
\quad\Longrightarrow\quad
c_{\mathrm{eff}} = \frac{c}{1+k}.
$$

For the equal-contribution case,

$$
k = 1,
$$

so

$$
f_{\mathrm{tot}} = 2f_1,
\qquad
u_{\mathrm{tot}} = 4u_1,
\qquad
c_{\mathrm{eff}} = \frac{c}{2}.
$$

This is the easiest local route from superposition to the effective-medium
summary.


## Local bending

If different regions of a wavefront have different loading, then they do not
advance equally.

- higher density implies lower $c_{\mathrm{eff}}$,
- lower density implies higher $c_{\mathrm{eff}}$.


So one side of the wavefront lags behind the other.

That lag bends the transport toward the more strongly loaded side.

This is refraction.

No external medium is required. The field bends because different parts of the
same flow are superposed and compressed by different amounts.


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

This dielectric-style writing is the conventional two-aspect version of the same
proportional-response idea. The response coefficient $k$ above is the
one-field analogue of the effective susceptibilities written here through
$\chi_{e,\mathrm{eff}}$ and $\chi_{m,\mathrm{eff}}$. The dielectric form
therefore does not introduce a different mechanism. It is the conventional
electromagnetic writing of the same retarded compression effect.


## What this gives

This chapter establishes:

- coherent overlap produces quadratic local loading,
- the square law counts the joined state but does not by itself explain it,
- continuity forbids assigning the difference to primitive sinks or sources,
- two inflows recovered on one outflow force compression of the same total
  content,
- that compression doubles the mean density,
- reduced effective advance is the coarse-grained summary of that lag,
- the proportional-response form $f_2 = kf_1$ gives the direct local route to
  $c_{\mathrm{eff}}$ and closes onto the dielectric effective-medium writing,
- differential loading bends transport,
- self-refraction is retarded overlap of the same flow.


No second substrate is required.

The next step is global:

> when self-refraction is strong enough to close the path, what stable
> configurations are allowed?
