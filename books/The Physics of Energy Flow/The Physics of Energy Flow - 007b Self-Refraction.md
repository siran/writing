---
title: The Physics of Energy Flow - Self-Refraction
date: 2026-03-26
---

# 7b. Self-Refraction

Chapter 7 recovered source-free transport, and Chapter 7a resolved that
transport into two complementary transverse aspects. What remains is to
understand how a single field can bend its own path.

No second substrate is required. Distinct portions of the same transporting
field interact when they are realized in a common overlap region. The question is how
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

the joined local readout becomes

$$
u_{\mathrm{join}} = 2u_0(1+\cos\delta).
$$

Therefore

$$
0 \le u_{\mathrm{join}} \le 4u_0.
$$

This is the local quadratic readout of the joined branch. It is not yet the
full continuity statement for the two-stream interaction.


## Pair budget and joined branch

To distinguish the conserved pair budget from the local joined readout, it is
useful to introduce the normalized sum and difference variables

$$
f_{+} := \frac{f_1+f_2}{\sqrt{2}},
\qquad
f_{-} := \frac{f_1-f_2}{\sqrt{2}}.
$$

Then exactly

$$
|f_{+}|^2 + |f_{-}|^2 = |f_1|^2 + |f_2|^2.
$$

For two equal inputs this becomes

$$
|f_{+}|^2 + |f_{-}|^2 = 2u_0.
$$

So the interacting pair always carries the same total budget $2u_0$. What
changes with phase is how that fixed budget is distributed between the joined
combination $f_{+}$ and the opposed combination $f_{-}$.

Since

$$
f_{\mathrm{join}} = f_1 + f_2 = \sqrt{2}\,f_{+},
$$

the local joined readout is

$$
u_{\mathrm{join}} = |f_{\mathrm{join}}|^2 = 2|f_{+}|^2.
$$

That is why the joined branch can read locally as $4u_0$ even though the
conserved pair budget is only $2u_0$.

This is only bookkeeping. It does not introduce a second substance. It only
keeps separate two questions that must not be conflated:

- how much energy the interacting pair carries in total,
- how much of that budget is read locally on the joined branch.


## Finite overlap region

The physical explanation starts from continuity on a finite overlap region
$\Omega$:

$$
\frac{d}{dt}\int_{\Omega} u\,dV
=
-\oint_{\partial\Omega}\mathbf J\cdot\mathbf n\,dS.
$$

No primitive source or sink is allowed. So whatever energy enters the overlap
region must either

- leave through some part of its boundary, or
- remain transiently stored inside the region.

Over a fixed interval $\Delta t$, let one thin inflow of cross section $A$
occupy the realized transport volume

$$
V_0 := A c\,\Delta t.
$$

If two equal inflows enter the overlap region, then before interaction the
incoming budget is

$$
\mu_{\mathrm{in}} = 2E,
\qquad
V_{\mathrm{in}} = 2V_0.
$$

So the incoming mean density is

$$
\bar u_{\mathrm{in}}
=
\frac{\mu_{\mathrm{in}}}{V_{\mathrm{in}}}
=
\frac{2E}{2V_0}
=
\frac{E}{V_0}.
$$


## Constructive recombination

If the two inflows are in phase,

$$
\delta = 0,
$$

then

$$
f_{+} = \sqrt{2}\,f_1,
\qquad
f_{-} = 0,
$$

and the joined local readout reaches

$$
u_{\mathrm{join}} = 4u_0.
$$

Now suppose the overlap region recovers the two inflows on one loaded branch
over the same interval. Then the realized transport volume falls from
$2V_0$ to $V_0$ while the carried content remains $2E$:

$$
\mu_{\mathrm{out}} = 2E,
\qquad
V_{\mathrm{out}} = V_0.
$$

Therefore the mean density on that loaded branch is

$$
\bar u_{\mathrm{out}}
=
\frac{\mu_{\mathrm{out}}}{V_{\mathrm{out}}}
=
\frac{2E}{V_0}
=
2\bar u_{\mathrm{in}}.
$$

This is the exact compression statement: the mean density doubles because the
same transported content is recovered on half the transport volume.

The stronger value

$$
u_{\mathrm{join}} = 4u_0
$$

is a local quadratic readout of that constructively recombined branch. It is
not the conserved pair budget itself.


## Destructive overlap

If instead the two inflows are out of phase,

$$
\delta = \pi,
$$

then

$$
f_{+} = 0,
\qquad
f_{-} = \sqrt{2}\,f_1,
$$

and the joined forward readout is

$$
u_{\mathrm{join}} = 0.
$$

This is not a sink. It means only that the joined branch vanishes. The pair
budget is still

$$
|f_{+}|^2 + |f_{-}|^2 = 2u_0.
$$

Continuity then forces the same incoming $2E$ to be recovered not on the
forward joined branch but elsewhere in the overlap geometry.

For a steady interaction there are only two possibilities:

- the flux leaves through other faces of the overlap region, that is, it is
  redirected,
- or the flows separate again after the overlap and recover the original
  two-branch distribution.

In the second case, if no new local recompression occurs, the natural recovery
is simply

$$
u_0 + u_0 = 2u_0.
$$

So destructive overlap does not produce a hidden `4u_0`. It removes the joined
branch and preserves the original pair budget. To obtain a fresh `4u_0`
readout, the transport must undergo a new constructive recombination into one
branch.


## What the square law does and does not do

The square form

$$
u = |f|^2
$$

does not create or remove energy. It does two precise jobs:

- it gives the local readout of the branch being sampled,
- it makes the phase-sensitive cross term explicit.

The continuity argument is separate. It tells us how the transported content is
recovered across the whole overlap region.


## Effective advance

Transport along each realized path still proceeds at the local rate $c$.

What changes is the lag of a loaded branch when compared with isolated
transport. Wherever two inflows are locally recovered on one branch, that
branch must carry the same content through less realized transport volume over
the same interval.

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

The microscopic transport rate along each realized path remains $c$.

But if two inflows are locally recovered on one loaded branch, then that branch
lags relative to the unloaded case. In coarse-grained language that lag is
written as a reduced effective advance.

So the point is not that more energy moves faster. It does not. The point is
that continuity forces the same total content through one locally surviving
branch.
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

This shortcut concerns the reinforcing branch. When the local sum vanishes, one
does not assign a negative effective advance to a non-existent forward branch;
one returns instead to the finite-region continuity statement above.

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
proportional-response idea. The response coefficient $k$ above is
the one-field analogue of the effective susceptibilities written here through
$\chi_{e,\mathrm{eff}}$ and $\chi_{m,\mathrm{eff}}$. The dielectric form
therefore does not introduce a different mechanism. It is the conventional
electromagnetic writing of the same retarded compression effect.


## What this gives

This chapter establishes:

- coherent overlap produces quadratic local loading,
- the local joined readout can range from $0$ to $4u_0$,
- the conserved two-stream budget remains $2u_0$,
- the square law counts the joined state but does not by itself explain it,
- continuity forbids assigning the difference to primitive sinks or sources,
- two inflows recovered on one outflow force compression of the same total
  content,
- that compression doubles the mean density,
- destructive overlap removes the joined branch without removing the pair
  budget, which must be redirected or later re-separated,
- reduced effective advance is the coarse-grained summary of that lag,
- the proportional-response form $f_2 = kf_1$ gives the direct local route
  to $c_{\mathrm{eff}}$ and closes onto the dielectric effective-medium writing,
- differential loading bends transport,
- self-refraction is retarded overlap of the same flow.


No second substrate is required.

The next step is global:

> when self-refraction is strong enough to close the path, what stable
> configurations are allowed?
