---
title: The Physics of Energy Flow - Self-Refraction
date: 2026-03-26
---

# 7b. Self-Refraction

Chapter 7 recovered source-free transport, and Chapter 7a resolved that
transport into two complementary transverse aspects. What remains is to
understand how a single field can bend its own path.

No second substrate is required. Distinct portions of the same transporting
field interact when they are realized in a common overlap region. The question
is how this overlap modifies transport.


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

At first sight, both endpoints are surprising: coherent overlap seems to
produce a fourfold local loading for free, while destructive overlap seems to
erase the joined energy altogether.

But in all cases energy is conserved, so these endpoints have to be interpreted
through continuity on the full overlap region, not by the local square-law
readout alone.

For two equal inputs, the incoming two-stream budget is still the original
$u_0 + u_0 = 2u_0$ before any particular recovery geometry is considered.


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


Over a fixed interval $\Delta t$, let one thin inflow of cross section
$A$ occupy the realized transport volume

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

then the joined local readout reaches

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

is the local quadratic readout of that constructively recombined branch. It is
not a statement that the conserved transported budget itself has become `4u_0`.


## Destructive overlap

If instead the two inflows are out of phase,

$$
\delta = \pi,
$$

then the joined local readout reaches

$$
u_{\mathrm{join}} = 0.
$$

This needs interpretation. The continuity equation tells us that the incoming
energy cannot simply disappear, but the joined forward branch now contributes no
local readout.

The correct conclusion is not that a sink has appeared. It is that the joined
forward branch is not the channel on which the incoming content is recovered.

For a finite overlap region, continuity leaves only two possibilities:

- the incoming content exits through other parts of the boundary, that is, it
  is redirected,
- or the flows separate again after the overlap and recover the original
  two-branch distribution.

In the second case, if no new local recompression occurs, the natural recovery
is simply

$$
u_0 + u_0 = 2u_0.
$$

So destructive overlap does not create a contradiction and does not prove that
no real overlap region is possible. It proves only that an everywhere-dark
joined branch cannot itself be the full recovery geometry. If a finite overlap
region produced zero joined readout and no redirected or re-separated exit, that
region would act as a sink and would therefore be forbidden.

To obtain a fresh `4u_0` readout after destructive overlap, the transport must
undergo a new constructive recombination into one branch.


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

Transport along each realized path still proceeds at the local rate
$c$.

What changes is not the microscopic transport speed but the coarse-grained lag
of a branch that must recover two inflows on one realized transport volume over
the same interval.

In the constructive case above, the loaded branch carries

$$
\mu_{\mathrm{out}} = 2E
$$

on

$$
V_{\mathrm{out}} = V_0,
$$

whereas the same total transported content had previously been distributed over

$$
V_{\mathrm{in}} = 2V_0.
$$

Equivalently,

$$
\bar u_{\mathrm{out}} = 2\bar u_{\mathrm{in}}.
$$

That doubled mean density is the local compression statement. The effective
advance is only a compact summary of the corresponding lag on that loaded
branch.

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

On a locally surviving loaded branch, a convenient summary is

$$
n_{\mathrm{eff}} := \frac{\bar u_{\mathrm{out}}}{\bar u_{\mathrm{in}}},
\qquad
c_{\mathrm{eff}} = \frac{c}{n_{\mathrm{eff}}}.
$$

So in the constructively recombined case,

$$
\bar u_{\mathrm{out}} = 2\bar u_{\mathrm{in}}
\qquad\Longrightarrow\qquad
c_{\mathrm{eff}} = \frac{c}{2}.
$$

This summary applies only to a branch that actually survives the overlap. When
the forward joined branch vanishes in destructive overlap, one returns instead
to the finite-region continuity statement and the redirected or re-separated
recovery geometry.


## Effective index

The effective index is therefore not a second mechanism. It is the compact way
to write that, on locally surviving loaded branches, more strongly superposed
regions lag more strongly than weakly loaded ones.


## Proportional background response

There is also a direct local route to the same effective advance on the
reinforcing branch.

Treat the second contribution not as a second independent substance but as the
background response induced by the first. In the same way one writes

$$
P = \chi E,
$$

one may write the reinforcing response of the same flow as

$$
f_2 = k f_1,
\qquad
k \ge 0.
$$

This shortcut concerns only the reinforcing branch. When the local sum vanishes,
one does not assign a negative effective advance to a non-existent forward
branch; one returns instead to the finite-region continuity statement above.

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
- where two inflows are locally recovered on one outflow, continuity forces
  compression of the same total content,
- that constructive one-branch recovery doubles the mean density,
- destructive overlap removes the joined branch without removing the pair
  budget, which must be redirected or later re-separated,
- reduced effective advance is the coarse-grained summary of that loaded-branch
  lag,
- the proportional-response form $f_2 = kf_1$ gives the direct local route
  to $c_{\mathrm{eff}}$ and closes onto the dielectric effective-medium writing,
- differential loading bends transport,
- self-refraction is retarded overlap of the same flow.


No second substrate is required.

The next step is global:

> when self-refraction is strong enough to close the path, what stable
> configurations are allowed?
