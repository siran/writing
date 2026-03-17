---
title: The Physics of Energy Flow – Mass as Trapped Energy
date: 2026-03-11
---


# 9. Mass as Trapped Energy

Mass is what confined energy becomes when part of its momentum is trapped in
closed circulation and no longer available for straight translation.

Consider a localized flow whose energy moves along a smooth closed trajectory
$X(s)$, parameterized by arclength $s$. Locally, the propagation speed is still
$c$. Choose a macroscopic direction of motion $\hat{\mathbf{z}}$, and let
$\hat{\mathbf{t}}(s)$ be the unit tangent to the flow. Define the local pitch
angle by

$$
\cos\theta(s)=\hat{\mathbf{t}}(s)\cdot\hat{\mathbf{z}}.
$$

Over a segment $ds$, the forward displacement is

$$
dz=\cos\theta(s)\,ds,
$$

while the elapsed time is

$$
dt=\frac{ds}{c}.
$$

So the local forward speed is

$$
v_{\text{forward}}(s)=\frac{dz}{dt}=c\cos\theta(s).
$$

Over one full circuit of length $L$, the effective forward speed is therefore

$$
v_{\text{eff}}
=
c\,\left\langle\cos\theta\right\rangle,
$$

where

$$
\left\langle\cos\theta\right\rangle
:=
\frac{1}{L}\int_0^L \cos\theta(s)\,ds.
$$

If the path were everywhere straight, $\langle\cos\theta\rangle=1$ and the
energy would simply propagate at $c$. But once the trajectory has persistent
transverse winding, part of the motion is no longer available for forward
translation.

Electromagnetic energy of total energy $E$ carries momentum of magnitude

$$
P=\frac{E}{c}.
$$

Only the component aligned with $\hat{\mathbf{z}}$ contributes to forward
motion. Integrating around the loop gives

$$
P_z=\frac{E}{c}\left\langle\cos\theta\right\rangle.
$$

The rest is trapped in closed transverse circulation:

$$
P_{\perp,\text{eff}}
:=
\sqrt{P^2-P_z^2}
=
\frac{E}{c}\sqrt{1-\left\langle\cos\theta\right\rangle^2}.
$$

This trapped momentum is the reason the configuration resists redirection. To
change the macroscopic motion of the object, one must reorient the circulating
momentum throughout the whole closed path, not merely push a point.

That is inertia. Its measure is

$$
m_{\text{eff}}
:=
\frac{P_{\perp,\text{eff}}}{c}
=
\frac{E}{c^2}\sqrt{1-\left\langle\cos\theta\right\rangle^2}.
$$

In the rest frame of the confined configuration, the net translational momentum
vanishes, so $\langle\cos\theta\rangle=0$. Then

$$
m=\frac{E_0}{c^2},
$$

where $E_0$ is the rest energy of the closed mode.

In this framework, this states what mass is: the energy trapped in
circulation, measured in the frame where the closed flow has no net
translation.

Why does the energy not simply straighten its path and eliminate its mass?
Because the circulation is topologically closed. Once winding exists, removing
it would require reconnection of the flow itself. Mass is kinematic delay
locked in by topology.

Unconfined propagation carries momentum $p=E/c$ but no inertial rest mass.
Mass appears when topology confines part of the momentum into persistent
circulation.

If that confined circulation is concentrated in a thin closed tube, the same
trapped load defines an effective one-dimensional description. Energy per unit
length becomes line tension, and the corresponding inertial line density is
that tension divided by $c^2$. Appendix 217 develops that effective string
description directly from the bounded Maxwellian mode.

Appendix 220 sharpens the same point one step further: matter is a persistent
closed causal loop of Maxwellian transport. Its mass is the trapped load of
that loop.
