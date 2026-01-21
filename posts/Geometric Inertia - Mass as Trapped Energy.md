---
title: "Geometric Inertia: Mass as Trapped Energy"
subtitle: A First-Principles Derivation from Maxwell Topology
author: An M. Rodriguez, Alex Mercer
date: 2026-01-14
keywords: geometric delay, helical path, effective velocity, emergent mass, Maxwell topology, classical derivation, energy circulation
one-sentence-summary: When electromagnetic energy follows a non-straight, closed trajectory while locally propagating at light speed, geometric delay produces subluminal effective motion and inertial mass.
summary: We derive subluminal velocity and inertial mass from first principles using only geometry and Maxwell kinematics. Electromagnetic energy always propagates locally at speed $c$, but if constrained to follow a helical or knotted trajectory, it must traverse a longer path to achieve the same forward displacement. This geometric delay reduces the effective forward speed. Momentum circulating in closed transverse directions does not contribute to translation and manifests as inertial mass. No constitutive medium, polarization response, or relativistic postulates are assumed. Mass emerges as a measure of trapped electromagnetic momentum.
DOI: https://writing.preferredframe.com/doi/10.5281/zenodo.18249230
---

![AI generated illustration of knotted trajectories on a toroidal surface.](https://siran.github.io/assets/writing/unrolled-cylinder.png)


## The geometry of constrained motion

Consider a localized tube of electromagnetic energy whose energy flow follows a
smooth space curve $X(s)$, parameterized by arclength
$s$.

Assume only the following:

1. Electromagnetic energy propagates locally at speed $c$ along the
   curve.
2. The curve is smooth and closed.
3. No material medium or external forces are present.

The question is purely kinematic:

**What is the effective forward speed of such a structure?**


## Unrolling the geometry

Choose a fixed spatial direction $\hat{\mathbf{z}}$, interpreted as the
macroscopic direction of motion of the object.

Let $\hat{\mathbf{t}}(s) = dX/ds$ be the unit tangent vector to the energy flow.
Define the local pitch angle $\theta(s)$ by

$$
\cos\theta(s) = \hat{\mathbf{t}}(s)\cdot \hat{\mathbf{z}}.
$$

Over an infinitesimal segment $ds$:

- The forward displacement is

  $$
  dz = \cos\theta(s)\,ds.
  $$

- Since the energy propagates along the curve at speed $c$, the
  elapsed time is

  $$
  dt = \frac{ds}{c}.
  $$

Therefore, the instantaneous forward velocity associated with that segment is

$$
v_{\text{forward}}(s) = \frac{dz}{dt} = c\cos\theta(s).
$$


## Effective forward speed

Let the total length of the closed trajectory be $L$.

The total traversal time is

$$
T = \int_0^L \frac{ds}{c} = \frac{L}{c},
$$

and the net forward displacement over one cycle is

$$
Z = \int_0^L \cos\theta(s)\,ds.
$$

Define the effective forward speed as net displacement divided by total time:

$$
v_{\text{eff}} = \frac{Z}{T}
= c\,\left\langle \cos\theta \right\rangle,
$$

where the arclength average is

$$
\left\langle \cos\theta \right\rangle
:= \frac{1}{L}\int_0^L \cos\theta(s)\,ds.
$$


### Result: Subluminal motion from geometry

Since $|\cos\theta(s)| \le 1$ pointwise, it follows that

$$
|v_{\text{eff}}| \le c,
$$

with strict inequality whenever the trajectory has nonzero transverse winding
over a set of nonzero measure.

The local propagation speed remains exactly $c$ everywhere. The
reduction in forward speed is purely geometric.


## Momentum decomposition and inertia

Electromagnetic energy carries momentum. For a localized packet of energy
$E$ whose local transport occurs at speed $c$, the
magnitude of the total momentum is

$$
P = \frac{E}{c}.
$$

The momentum vector is tangent to the energy flow at each point. Only its
component along $\hat{\mathbf{z}}$ contributes to forward translation.


## Forward momentum

An energy element $dE$ carries momentum magnitude $dP = dE/c$
directed along $\hat{\mathbf{t}}(s)$. Its forward component is

$$
dP_z = \frac{dE}{c}\cos\theta(s).
$$

If the energy per arclength is uniform, $dE = (E/L)\,ds$, then integrating
around the loop gives

$$
P_z = \frac{E}{c}\left\langle \cos\theta \right\rangle.
$$

This is the momentum responsible for macroscopic translation.


## Trapped momentum

The remaining momentum does not contribute to forward motion. It circulates in
closed transverse directions.

Define the effective transverse momentum as

$$
P_{\perp,\text{eff}} := \sqrt{P^2 - P_z^2}.
$$

Substituting $P = E/c$ yields

$$
P_{\perp,\text{eff}}
= \frac{E}{c}\sqrt{1-\left\langle \cos\theta \right\rangle^2}.
$$

This momentum is dynamically present but kinematically trapped.


## Definition of inertial mass

We define the inertial mass as the measure of resistance to acceleration arising
from momentum that does not contribute to translation.

Accordingly,

$$
m_{\text{eff}} := \frac{P_{\perp,\text{eff}}}{c}.
$$

Thus,

$$
m_{\text{eff}}
= \frac{E}{c^2}\sqrt{1-\left\langle \cos\theta \right\rangle^2}.
$$


### Result: Mass from circulation

- If the trajectory is everywhere straight, then $\langle\cos\theta\rangle = 1$,
  so $m_{\text{eff}} = 0$ and $v_{\text{eff}} = c$.
- If the trajectory has persistent transverse winding, then
  $|\langle\cos\theta\rangle| < 1$, so $m_{\text{eff}} > 0$ and
  $|v_{\text{eff}}| < c$.

Mass arises as a consequence of trapped electromagnetic momentum.


## Energy-weighted generalization

If the energy density varies along the curve, replace arclength averages with
energy-weighted averages.

Define

$$
\left\langle \cos\theta \right\rangle_E
:= \frac{1}{E}\int_0^L \cos\theta(s)\,dE(s).
$$

Then

$$
v_{\text{eff}} = c\left\langle \cos\theta \right\rangle_E,
$$

$$
m_{\text{eff}}
= \frac{E}{c^2}
\sqrt{1-\left\langle \cos\theta \right\rangle_E^2}.
$$

This is the most general form consistent with light-like local transport
constrained to a closed trajectory.


## Topological stability

Why does the energy not simply straighten its path and eliminate its mass?

Because the trajectory is topologically constrained.

Closed electromagnetic flux tubes may form knots characterized by integer
winding numbers $(m,n)$. These integers cannot change continuously.
Eliminating the transverse circulation would require a discontinuous
reconnection of field lines.

Therefore, once circulation exists, the associated inertial mass is locked in by
topology.


## Final conclusion

Using only:

1. The local propagation of electromagnetic energy at speed $c$,
2. Euclidean geometry of curved paths,
3. Conservation of energy and momentum,
4. Topological stability of closed trajectories,

we have derived:

- Subluminal effective motion from path geometry,
- Inertial mass from circulating electromagnetic momentum,
- The existence of a frame in which the net translational momentum vanishes (a
  "rest frame" for the object) while intrinsic circulation persists.

without introducing matter, constitutive media, or relativistic postulates.

Mass is not a fundamental property of matter.

**Mass is electromagnetic energy constrained to circulate rather than
translate.**


## Notes

This work complements earlier derivations of emergent refraction and
electromagnetic topology in a Maxwell universe, but remains kinematically
self-contained.


## Suggested References

Rodriguez, A. M. (2026). *Light speed as an emergent property of electromagnetic
superposition: Polarization without matter*. Preferred Frame.
https://writing.preferredframe.com/doi/10.5281/zenodo.18209801

Rodriguez, A. M., Mercer, A. (2026). *String Theory Derivation in a Maxwell
Universe*. Preferred Frame.
https://writing.preferredframe.com/doi/10.5281/zenodo.425370
