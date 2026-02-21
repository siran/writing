## Worked example 2: a helical flux tube on a cylinder, with explicit $v_{\mathrm{eff}}$ and $m_{\mathrm{eff}}$

This example unifies three ingredients in one computation:

- local transport at the maximal rate along the flow line,
- geometry of a helical (non-straight) trajectory,
- momentum decomposition into translational and circulating parts.

It reproduces, as explicit formulas:

- the effective forward speed reduction,
- and an effective inertial mass measure associated with trapped circulation.

No relativity postulates are used. The only inputs are:

- a curve geometry in Euclidean space,
- local energy transport at speed $c$ along that curve,
- and the Maxwell kinematic relation between energy and momentum for such
  transport.


### Cylinder geometry and the helix

Consider a cylinder of radius $R$ with axis $\hat{\mathbf{z}}$.

Let a curve wrap around this cylinder with constant pitch. A convenient
parametrization uses arclength $s$ along the curve:

$$
\mathbf{X}(s) =
\begin{pmatrix}
R\cos(\kappa s)\\
R\sin(\kappa s)\\
\lambda s
\end{pmatrix}.
$$

Here:

- $\kappa$ controls how fast we wind azimuthally,
- $\lambda$ controls how fast we advance along $z$,
- and $s$ is arclength, so $|\partial_s\mathbf{X}(s)|=1$.

Compute the tangent:

$$
\partial_s\mathbf{X}(s)=
\begin{pmatrix}
- R\kappa \sin(\kappa s)\\
\ \ R\kappa \cos(\kappa s)\\
\lambda
\end{pmatrix}.
$$

Its squared norm is

$$
|\partial_s\mathbf{X}|^2 = (R\kappa)^2(\sin^2+\cos^2)+\lambda^2 = (R\kappa)^2+\lambda^2.
$$

Impose arclength normalization:

$$
(R\kappa)^2+\lambda^2=1.
$$

Define the (constant) pitch angle $\theta$ by

$$
\cos\theta = \hat{\mathbf{t}}\cdot \hat{\mathbf{z}},
\qquad
\hat{\mathbf{t}}=\partial_s\mathbf{X}.
$$

Since the $z$-component of $\partial_s\mathbf{X}$ is
$\lambda$, we have

$$
\cos\theta=\lambda,
\qquad
\sin\theta = R\kappa,
\qquad
\cos^2\theta+\sin^2\theta=1.
$$

So $\theta$ measures how much of the tangent is along $z$
versus around the cylinder.

---


## Local transport at speed $c$ along the helix

Assume electromagnetic energy propagates locally along the curve at speed
$c$. This is a kinematic assumption about local transport rate
along the flow line.

That means:

- in time $dt$, energy advances a distance $ds = c\,dt$ along
  the curve.

Thus,

$$
\frac{ds}{dt}=c.
$$

---


## Effective forward speed $v_{\mathrm{eff}}$

The forward displacement is the change in $z$:

$$
dz = \partial_s z\, ds = \lambda\, ds = \cos\theta\, ds.
$$

Divide by $dt$:

$$
\frac{dz}{dt} = \cos\theta\,\frac{ds}{dt} = \cos\theta\,c.
$$

Therefore the effective forward velocity is

$$
v_{\mathrm{eff}} = c\cos\theta.
$$

This is purely geometric: forward progress is reduced because part of the motion
is spent going around.

No “slowing” occurs along the path: the path-speed remains $c$.

---


## Unrolling the cylinder and deriving the same result

Unroll the cylinder surface to a plane.

One full azimuthal revolution corresponds to horizontal displacement
$2\pi R$. Suppose over one revolution the helix rises by
$\Delta z$.

Then the path length over one revolution is

$$
\Delta s = \sqrt{(2\pi R)^2 + (\Delta z)^2}.
$$

Local transport time is

$$
\Delta t = \frac{\Delta s}{c}.
$$

Effective forward speed is

$$
v_{\mathrm{eff}}=\frac{\Delta z}{\Delta t}
= \frac{\Delta z}{\Delta s/c}
= c\,\frac{\Delta z}{\sqrt{(2\pi R)^2 + (\Delta z)^2}}.
$$

Define $\theta$ by

$$
\cos\theta = \frac{\Delta z}{\Delta s},
$$

and the same formula appears:

$$
v_{\mathrm{eff}}=c\cos\theta.
$$

Thus, the reduction is exactly “geometric delay”: longer path for the same
forward span.

---


## Momentum content of a localized transported energy packet

Let the total electromagnetic energy in the tube be $E$.

For local light-like transport, the magnitude of momentum associated with energy
transport is

$$
P = \frac{E}{c}.
$$

This is the statement that energy transported at speed $c$ carries
momentum of magnitude $E/c$. In Maxwell language it is consistent
with $\mathbf{g}=\mathbf{S}/c^2$ and $|\mathbf{S}|=cu$.

The momentum vector points along the local direction of transport, i.e. along
the helix tangent.

---


## Decomposition into translational and circulating momentum

The direction $\hat{\mathbf{z}}$ defines “translation.” The orthogonal azimuthal
direction defines “circulation.”

The total momentum magnitude is $P=E/c$.

Its $z$-component is

$$
P_z = P\cos\theta = \frac{E}{c}\cos\theta.
$$

The orthogonal (azimuthal) component magnitude is

$$
P_\perp = P\sin\theta = \frac{E}{c}\sin\theta.
$$

Interpretation:

- $P_z$ contributes to net forward translation,
- $P_\perp$ is tied to circulation around the cylinder.

If the path is closed in the azimuthal direction, $P_\perp$ corresponds
to momentum that does not produce net displacement; it is “kinematically
trapped” in the closed direction.

---


## Effective inertial mass measure from trapped momentum

The program’s definition here is operational:

inertial mass is a measure of how much momentum content is not available for
translation.

A natural scalar measure is

$$
m_{\mathrm{eff}} := \frac{P_\perp}{c}.
$$

Substitute $P_\perp$:

$$
m_{\mathrm{eff}}
=
\frac{1}{c}\frac{E}{c}\sin\theta
=
\frac{E}{c^2}\sin\theta.
$$

So

$$
m_{\mathrm{eff}} = \frac{E}{c^2}\sin\theta,
\qquad
v_{\mathrm{eff}} = c\cos\theta.
$$

These two equations show the trade:

- as $\theta\to 0$, $v_{\mathrm{eff}}\to c$ and $m_{\mathrm{eff}}\to 0$,
- as $\theta\to \pi/2$, $v_{\mathrm{eff}}\to 0$ and $m_{\mathrm{eff}}\to E/c^2$.

The limiting case $\theta=\pi/2$ is pure circulation: motion without
translation.

---


## Energy-weighted generalization for variable pitch

If the pitch angle varies along a closed trajectory, replace constants by
averages.

Let the local pitch be $\theta(s)$, and let the energy per arclength be
$\varepsilon(s)$ so that $dE=\varepsilon(s)\,ds$ and
$E=\int_0^L \varepsilon(s)\,ds$.

Then the effective forward speed is energy-weighted:

$$
v_{\mathrm{eff}}
=
c\,\left\langle \cos\theta \right\rangle_E,
\qquad
\left\langle \cos\theta \right\rangle_E
:=
\frac{1}{E}\int_0^L \cos\theta(s)\,dE(s).
$$

Similarly,

$$
P_z = \frac{E}{c}\left\langle \cos\theta \right\rangle_E.
$$

A consistent trapped-momentum measure is then

$$
P_{\perp,\mathrm{eff}}
=
\sqrt{P^2 - P_z^2}
=
\frac{E}{c}\sqrt{1-\left\langle \cos\theta \right\rangle_E^2},
$$

and define

$$
m_{\mathrm{eff}}
=
\frac{P_{\perp,\mathrm{eff}}}{c}
=
\frac{E}{c^2}\sqrt{1-\left\langle \cos\theta \right\rangle_E^2}.
$$

This is the most general form compatible with:

- local transport at speed $c$ along the flow line,
- and the definition of translation as the $\hat{\mathbf{z}}$ direction.

---


## Connection to the thin-tube tension computation

From the previous worked example, thin-tube localization defines

$$
T = \int_{\Sigma_s} u\,dA,
\qquad
\mu = \frac{T}{c^2}.
$$

For a helix segment, the same definitions apply, but “translation” is now the
projection along $\hat{\mathbf{z}}$.

The point is:

- $T$ and $\mu$ are extracted from cross-sectional
  integrals of field energy,
- $v_{\mathrm{eff}}$ and $m_{\mathrm{eff}}$ are extracted from geometric
  projection of transport direction.

These are independent pieces of information about the same underlying localized
flow.

---


## Closing the conceptual loop between “delay” and “looping”

This worked example addresses the core tension:

- in some contexts effective slowing arises from phase-structured superposition,
- here effective slowing arises from geometric redistribution of motion.

Both can coexist without contradiction because they act on different aspects:

- phase-structured superposition changes how a total field evolves in time at a
  point,
- geometric looping changes how far transport advances in a chosen direction per
  unit time.

In both cases:
- local transport along the allowed path remains continuous,
- and the effective macroscopic propagation changes because “progress” is a
  projection of a richer process.

---


## Summary of the helix example

Given a localized electromagnetic energy packet of total energy $E$
transported locally at speed $c$ along a helical path of pitch
angle $\theta$:

1. Effective forward speed:

$$
v_{\mathrm{eff}} = c\cos\theta.
$$

2. Translational momentum:

$$
P_z = \frac{E}{c}\cos\theta.
$$

3. Circulating momentum:

$$
P_\perp = \frac{E}{c}\sin\theta.
$$

4. Effective inertial mass measure:

$$
m_{\mathrm{eff}} = \frac{E}{c^2}\sin\theta.
$$

5. Variable pitch generalization (energy-weighted):

$$
v_{\mathrm{eff}} = c\left\langle \cos\theta \right\rangle_E,
\qquad
m_{\mathrm{eff}} = \frac{E}{c^2}\sqrt{1-\left\langle \cos\theta \right\rangle_E^2}.
$$

No additional postulates appear. Everything is geometry plus Maxwell kinematics
of energy and momentum transport.
