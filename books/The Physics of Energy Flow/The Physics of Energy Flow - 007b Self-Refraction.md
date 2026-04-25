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


## Dielectric loading as the known case

The familiar laboratory form of this effect is dielectric slowing.

In ordinary electromagnetic notation, a probe field in a dielectric is read
together with the in-phase response of the medium. For a proportional response
with amplitude ratio $k$ in both transverse aspects, write

$$
\mathbf E_2 = k\mathbf E_1,
\qquad
\mathbf H_2 = k\mathbf H_1.
$$

Then

$$
\mathbf D
=
\varepsilon_0(\mathbf E_1+\mathbf E_2)
=
\varepsilon_0(1+k)\mathbf E_1
:=
\varepsilon_{\mathrm{eff}}\mathbf E_1,
$$

and

$$
\mathbf B
=
\mu_0(\mathbf H_1+\mathbf H_2)
=
\mu_0(1+k)\mathbf H_1
:=
\mu_{\mathrm{eff}}\mathbf H_1.
$$

The source-free wave speed of the loaded field is therefore

$$
c_{\mathrm{eff}}
=
\frac{1}{\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}}
=
\frac{1}{\sqrt{\varepsilon_0\mu_0(1+k)^2}}
=
\frac{c}{1+k}.
$$

This is the conventional two-aspect writing of the same compression rule. The
response field is not an extra primitive substrate; it is the in-phase
contribution that loads the transport. The coherent-overlap step below writes
the same rule for the case in which the in-phase response is supplied by another
phase-locked portion of the same transporting flow rather than by organized
matter.


## Coherent overlap and the amplitude-square form

The energy density at each point is expressed as the square of an
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

So the joined local energy density is

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

At first sight, both endpoints are surprising: coherent overlap seems to produce
a fourfold local energy density for free, while destructive overlap seems to erase the
joined energy altogether.

But in all cases energy is conserved, so these endpoints have to be interpreted
through continuity on the full overlap region, not by the local square-law
readout alone.

For two equal inputs, the incoming two-stream budget is still the original
$u_0 + u_0 = 2u_0$ before any particular recovery geometry is considered.


## Flux mismatch and the required slowdown

This is the physical reason the loaded branch cannot simply keep the original
advance rate.

In the laboratory version, let the original laser channel carry density
$2u$ and advance at $c$. Its flux is

$$
J_{\mathrm{in}} = 2u c.
$$

After a 50/50 split, the two arms carry

$$
2u c \longrightarrow u c + u c.
$$

The split changes the spatial distribution, not the available forward flux. The
total available flux remains

$$
J_{\mathrm{available}} = 2u c.
$$

At constructive recovery, the two coherent contributions add in amplitude. The
local bright density is therefore

$$
u_{\mathrm{bright}} = 4u.
$$

If that single bright recovery channel were assigned the unchanged advance
$c$, it would require

$$
J_{\mathrm{bright}} = u_{\mathrm{bright}}c = 4u c.
$$

But the laser only supplies $2u c$ into the two-arm recovery. There is
no second positive forward channel with $\mathbf S>0$ that can provide the
missing flux. The same input cannot feed a $4u$ branch moving at
$c$.

So the forbidden combination is precise:

$$
u_{\mathrm{bright}}=4u
\qquad\text{and}\qquad
c_{\mathrm{eff}}=c.
$$

At most one of those can survive as the description of a single positive
recovery channel. If the bright channel really recovers the $4u$
density, its advance must slow. If the channel is forced to advance at
$c$, then the laser cannot supply a sustained $4u$
recovery there; the density must fail to reach that value as a transported
channel, or the recovery must involve additional spatial redistribution outside
the selected branch.

Continuity therefore fixes the effective advance by

$$
J_{\mathrm{available}}
=
u_{\mathrm{bright}}c_{\mathrm{eff}},
$$

so

$$
2u c = 4u c_{\mathrm{eff}},
\qquad
c_{\mathrm{eff}} = \frac{c}{2}.
$$

The slowdown is not an added mechanism. It is the flux-density accounting of a
single positive recovery channel: the density increases locally while the
available flux does not.


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

In the constructive recovery geometry there is exactly one local positive
forward channel: the joined branch. There is no second local place where the
same branch has $\mathbf S>0$. The two inflows are therefore recovered on one
loaded branch over the same interval. The realized transport volume falls from
$2V_0$ to $V_0$ while the carried content remains
$2E$:

$$
\mu_{\mathrm{out}} = 2E,
\qquad
V_{\mathrm{out}} = V_0.
$$

Since in this case

$$
\mu_{\mathrm{out}} = \mu_{\mathrm{in}} = 2E,
\qquad
V_{\mathrm{out}} = V_0.
$$

The mean density on that loaded branch is

$$
\bar u_{\mathrm{out}}
=
\frac{\mu_{\mathrm{out}}}{V_{\mathrm{out}}}
=
\frac{2E}{V_0}
=
2\bar u_{\mathrm{in}}.
$$

This is the exact *compression* statement: the mean density doubles because the
same transported content is recovered on half the transport volume.


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

The correct conclusion is not that a sink has appeared. It is that this local
joined forward branch is absent. At the dark branch, $\mathbf S=0$ for the
surviving forward channel.

The incoming content is recovered only where the continuous pattern has positive
outgoing flux. In a spatial fringe, that recovery occurs at the neighboring
bright parts of the same pattern. If no joined branch is formed, the flows
separate again and recover the original two-branch distribution. The dark branch
itself is not a recovery channel; it is the local absence of the forward joined
branch.

This is also the place to distinguish the amplitude-like quantity from the
recovered density. The sign or phase can reverse in $f$, but the
recovered density

$$
u = |f|^2
$$

does not become negative. It can only vanish at a node and then reappear
elsewhere.

That spatial reappearance becomes explicit when the relative phase varies across
the overlap region. Let two equal contributions have the form

$$
f_1(x) = A e^{ikx},
\qquad
f_2(x) = A e^{-ikx}.
$$

Then

$$
f_{\mathrm{join}}(x)
=
f_1(x)+f_2(x)
=
2A\cos(kx),
$$

so the recovered density is

$$
u(x)
=
|f_{\mathrm{join}}(x)|^2
=
4|A|^2\cos^2(kx).
$$

Writing

$$
u_0 := |A|^2,
$$

this becomes

$$
u(x) = 4u_0\cos^2(kx).
$$

Therefore

$$
u(x)=0
\qquad
\text{at}
\qquad
x=\frac{(2n+1)\pi}{2k},
$$

while

$$
u(x)=4u_0
\qquad
\text{at}
\qquad
x=\frac{n\pi}{k}.
$$

The amplitude-like quantity $f_{\mathrm{join}}(x)$ changes sign across each node
because $\cos(kx)$ changes sign there. The density does not invert. It
vanishes at the node and reappears at separated antinodes.

Over one spatial period

$$
\lambda = \frac{2\pi}{k},
$$

the mean recovered density is

$$
\frac{1}{\lambda}\int_0^\lambda u(x)\,dx
=
\frac{1}{\lambda}\int_0^\lambda 4u_0\cos^2(kx)\,dx
=
2u_0.
$$

So the two-stream mean budget is recovered exactly, even though some points are
dark. The local zero is therefore not a sink. It is one part of a spatially
redistributed density pattern.

This example does not realize $\delta=\pi$ at every point. It shows the
generic case in which local destructive points are paired with local
constructive points, and the two-stream budget is recovered by spatial
redistribution.

In the second case, if no new local recompression occurs, the natural recovery
is simply

$$
u_0 + u_0 = 2u_0.
$$

So destructive overlap does not create a contradiction. It proves only that an
everywhere-dark joined branch has no positive recovery channel. If a finite
overlap region produced zero joined readout everywhere and no positive outgoing
flux anywhere in the continuing pattern, that region would act as a sink and
would therefore be forbidden.

To obtain a fresh `4u_0` readout after destructive overlap, the
transport must undergo a new constructive recombination into one branch.


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
of a branch that recovers two inflows on one realized transport volume over the
same interval.

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

That doubled mean density is the local compression statement. Equivalently, the
branch obeys the flux-density relation

$$
J = u\,c_{\mathrm{eff}},
$$

so when $J$ is fixed and $u$ rises, $c_{\mathrm{eff}}$
must fall. The effective advance is only a compact summary of the corresponding
lag on that loaded branch.

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
the forward joined branch vanishes in destructive overlap, there is no speed to
assign to that local branch. The positive recovery is read only in the nonzero
parts of the continuing pattern, or in the re-separated beams if no joined
branch is formed.


## Effective index

The effective index is therefore not a second mechanism. It is the compact way
to write that, on locally surviving loaded branches, more strongly superposed
regions lag more strongly than weakly loaded ones.


## Local bending

If different regions of a wavefront have different energy density, then they do not
advance equally.

- higher density implies lower $c_{\mathrm{eff}}$,
- lower density implies higher $c_{\mathrm{eff}}$.


So one side of the wavefront lags behind the other.

That lag bends the transport toward the more strongly loaded side.

This is refraction.

No external medium is required. The field bends because different parts of the
same flow are superposed and compressed by different amounts.


## Operational test

The laboratory test is direct because ordinary interference already gives the
density profile. A flux detector placed at a screen measures the flux of the
superposed fields arriving at that point.

For two equal coherent beams crossing symmetrically about the $z$
direction, write

$$
f_1(x,z,t)
=
A e^{i(kx\sin\theta+kz\cos\theta-\omega t)},
$$

$$
f_2(x,z,t)
=
A e^{i(-kx\sin\theta+kz\cos\theta-\omega t)}.
$$

With

$$
u_0 := |A|^2,
\qquad
q := 2k\sin\theta,
$$

the joined readout is

$$
u(x)
=
|f_1+f_2|^2
=
4u_0\cos^2\!\left(\frac{qx}{2}\right).
$$

The bright centers therefore have

$$
u_{\mathrm{bright}} = 4u_0,
$$

while the period average remains

$$
\langle u\rangle = 2u_0.
$$

The forward incoming flux density is

$$
J_{z,\mathrm{in}} = 2u_0 c\cos\theta.
$$

On the full fringe average this gives the ordinary projected advance
$c\cos\theta$. But if a narrow bright stripe is isolated and propagated as
the surviving positive channel, the loaded-branch law gives

$$
c_{\mathrm{eff,bright}}
=
\frac{J_{z,\mathrm{in}}}{u_{\mathrm{bright}}}
=
\frac{2u_0 c\cos\theta}{4u_0}
=
\frac{c\cos\theta}{2}.
$$

For nearly collinear beams this is $c/2$.

The experiment is therefore not "does a screen show a $4u_0$ bright
fringe?" That part is ordinary interference. The experiment is:

> Does an isolated bright stripe, once selected as the surviving positive
> channel, acquire the larger longitudinal delay implied by
> $c_{\mathrm{eff}}=J/u$?


Equivalently, the experiment asks which part of the forbidden pair fails. Either
the isolated bright channel keeps the $4u_0$ density and slows, or a
channel that advances at the ordinary speed cannot sustain the $4u_0$
density as an isolated transported branch.

One implementation is a delay measurement:

1. form a stable two-beam fringe pattern,
2. isolate a narrow region around a bright center,
3. propagate that selected stripe over a known length $L$,
4. propagate a matched reference beam over the same length,
5. compare modulation or pulse delay.


The reference prediction is

$$
t_{\mathrm{ref}}=\frac{L}{c},
$$

while the bright-stripe prediction for $\theta\ll1$ is

$$
t_{\mathrm{bright}}\approx\frac{2L}{c}.
$$

So the extra delay is

$$
\Delta t
\approx
\frac{L}{c},
$$

about $3.34\,\mathrm{ns}$ per meter.

A geometric version sends the selected bright stripe to a glass boundary. If the
bright branch carries effective index $n_{\mathrm{eff}}=2$, Snell's law at a
boundary with glass index $n_g\approx1.5$ gives

$$
n_{\mathrm{eff}}\sin\theta_i=n_g\sin\theta_r.
$$

The loaded branch then has a critical angle

$$
\sin\theta_c=\frac{n_g}{n_{\mathrm{eff}}}\approx0.75,
\qquad
\theta_c\approx48.6^\circ.
$$

Above that incidence angle the selected bright stripe should not transmit into
the glass, while an ordinary reference beam at the same angle should still
transmit. That is the clean refraction form of the same loaded-branch claim.

Opening the aperture to average over a full fringe period should erase the
loaded-branch signature, because the measured density returns to the two-beam
mean $2u_0$. The prediction belongs to the isolated bright channel,
not to the unselected fringe pattern as a whole.


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

- coherent overlap concentrates local energy density as the square of the joined amplitude,
- the local joined readout can range from $0$ to $4u_0$,
- the conserved two-stream budget remains $2u_0$,
- the square law counts the joined state but does not by itself explain it,
- continuity forbids assigning the difference to primitive sinks or sources,
- where two constructive inflows recover as one local positive branch,
  continuity forces compression of the same total content,
- that constructive one-branch recovery doubles the mean density,
- spatially varying phase produces nodes where the density vanishes and
  antinodes where it reappears more densely,
- a dark branch has no positive flux channel; recovery is read only where the
  continuing pattern has $\mathbf S>0$,
- reduced effective advance is the coarse-grained summary of that loaded-branch
  lag,
- the dielectric/proportional-response form $f_2=kf_1$ gives the direct
  local route to $c_{\mathrm{eff}}$,
- differential energy density bends transport,
- an isolated bright stripe gives a direct delay or refraction test of the
  loaded-branch law,
- self-refraction is retarded overlap of the same flow.


No second substrate is required.

The next step is global:

> when self-refraction is strong enough to close the path, what stable
> configurations are allowed?
