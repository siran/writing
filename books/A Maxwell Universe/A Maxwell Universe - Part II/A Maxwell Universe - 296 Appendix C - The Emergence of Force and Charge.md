---
title: A Maxwell Universe – Appendix C: The Emergence of Force and Charge
date: 2026-01-01 15:34
---


# Appendix C: The Emergence of Force and Charge

In the main text, we asserted that the Lorentz Force and Electric Charge are not
fundamental axioms, but emergent properties of a source-free Maxwell field. This
appendix provides the formal derivation of these second-order effects.


## 1. Deriving the Lorentz Force from Momentum Balance

In standard electrodynamics, the Lorentz force
$\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$ is an axiom. In a
Maxwell Universe, it is a theorem derived from the **Conservation of
Electromagnetic Momentum**.

We define "Force" on a particle not as an external push, but as the rate of
change of the momentum contained within the knot configuration.

$$
\mathbf{F}_{knot} \equiv \frac{d\mathbf{P}_{knot}}{dt}
$$

This is governed by the momentum continuity equation. The change in momentum
within a volume $V$ is equal to the momentum flowing in through the surface
minus the rate of change of the background field momentum:

$$
\frac{d\mathbf{P}_{mech}}{dt}
= \oint_{\partial V} \mathbf{T} \cdot d\mathbf{a}
- \frac{d}{dt} \int_V \epsilon_0 \mu_0 (\mathbf{S}) \, d^3x
$$

where $\mathbf{S} = \mathbf{E} \times \mathbf{H}$ is the Poynting vector and
$\mathbf{T}$ is the Maxwell Stress Tensor.


### Step 1: Isolating the Interaction

We decompose the field into the Knot field ($\mathbf{E}_k, \mathbf{H}_k$) and
the Background field ($\mathbf{E}_0, \mathbf{H}_0$).
The Stress Tensor is quadratic. The self-terms integrate to zero for a stable
particle, and the background terms integrate to zero as they pass through. The
net driving force comes entirely from the **Interaction Tensor**:

$$
T_{ij}^{int}
= \epsilon_0 (E_{k,i} E_{0,j} + E_{0,i} E_{k,j}
- \delta_{ij} \mathbf{E}_k \cdot \mathbf{E}_0) + \dots
$$


### Step 2: The Electrostatic Term ($q\mathbf{E}$)

Consider the knot in its own rest frame ($\mathbf{v}=0$).
We calculate the stress exerted by the background electric field $\mathbf{E}_0$
on the knot. The force is the surface integral of the interaction stress:

$$
\mathbf{F}_{static} = \oint_{\partial V} \mathbf{T}^{int} \cdot d\mathbf{a}
$$

Using the Divergence Theorem, we convert this surface integral into a volume
integral of the divergence of the tensor. Using the vector identity

$$
\nabla \cdot (\mathbf{E}_k \mathbf{E}_0)
= (\nabla \cdot \mathbf{E}_k)\mathbf{E}_0
+ (\mathbf{E}_k \cdot \nabla)\mathbf{E}_0$,
$$

and assuming the background field $\mathbf{E}_0$ is constant across the small
volume of the knot (so $\nabla \mathbf{E}_0 \approx 0$):

$$
\mathbf{F}_{static} \approx \mathbf{E}_0 \int_V (\nabla \cdot \mathbf{E}_k) \, d^3x
$$

Strictly speaking, in a source-free theory, $\nabla \cdot \mathbf{E}_k = 0$
everywhere. However, as defined in Section 2, the particle possesses a
**Time-Averaged Vorticity Magnitude** which behaves macroscopically as an
effective density $\rho_{eff}$.

Thus, the volume integral recovers the effective charge:

$$
\mathbf{F}_{static} \approx \mathbf{E}_0 \int \rho_{eff} dV = q \mathbf{E}_0
$$

This confirms that the "Electric Force" is the pressure of the background field acting on the effective density of the knot.


### Step 3: The Magnetic Term ($\mathbf{v} \times \mathbf{B}$)

This emergent term arises strictly from motion.
If the knot moves with velocity $\mathbf{v}$ through a background magnetic
field $\mathbf{B}_0$, the momentum balance changes. The rate of change of
momentum density includes a **convective term**:

$$
\frac{d\mathbf{P}}{dt} = \frac{\partial \mathbf{P}}{\partial t} + (\mathbf{v} \cdot \nabla)\mathbf{P}
$$


> **Why this term matters:**
> Think of this difference like watching a river.
> * The partial derivative $\frac{\partial \mathbf{P}}{\partial t}$ is the
>   change measured by a **stationary sensor** on the riverbank (Eulerian view).
> * The convective term $(\mathbf{v} \cdot \nabla)\mathbf{P}$ accounts for the
>   fact that the water itself is moving.
>
> Since our "particle" is not a fixed point in space but a moving configuration
> of field energy, we cannot just watch a fixed coordinate; we must follow the
> flow. The total change in momentum must account for the transport of the knot
> through the field.


The motion of the knot pushes its electric field profile $\mathbf{E}_k$ through
the background $\mathbf{B}_0$. Using the relation between spatial gradients and
time derivatives for a moving wave
($\frac{\partial}{\partial t} = -\mathbf{v} \cdot \nabla$):


> **Derivation of the identity:**
> This comes from the definition of a rigid shape moving through space.
> Consider a field profile $F(x)$ moving with velocity $v$. The value at any
> point is given by $F(x - vt)$.
> Applying the chain rule:
> * Time slope: $\frac{\partial F}{\partial t} = F' \cdot (-v)$
> * Space slope: $\nabla F = F' \cdot (1)$
>
> Therefore, for any traveling wave structure, time variation is simply spatial
> variation scaled by velocity: $\frac{\partial}{\partial t} = -\mathbf{v} \cdot \nabla$.


Substituting this into the Maxwell-Faraday law, the interaction yields a net
momentum flux perpendicular to both velocity and field:

$$
\mathbf{F}_{mag} = q (\mathbf{v} \times \mathbf{B}_0)
$$

The "magnetic force" is simply the momentum transfer required for the electric
geometry of the knot to translate through the magnetic geometry of the
background.


## 2. Deriving Effective Charge from Field Vorticity

Standard theory defines charge via divergence ($\nabla \cdot \mathbf{E}$). In a
source-free Maxwell Universe, $\nabla \cdot \mathbf{E} = 0$ everywhere, so the
net vector flux through any closed surface is zero.

However, the **amount of electromagnetic activity** is not zero. We define
"Charge" as the **Time-Averaged Magnitude** of the field curls.


### 2.1 The Local Vorticity Vector

We define the local **Vorticity Vector** $\mathbf{C}$ as the curl of the
electric field:

$$
\mathbf{C}(\mathbf{x}, t) = \nabla \times \mathbf{E}(\mathbf{x}, t)
$$

This vector describes the instantaneous "spin" or circulation of the field.


### 2.2 The Problem of Vector Cancellation

If we simply integrate the vector $\mathbf{C}$ over the volume of the knot, the
result is zero. Because the knot is a standing wave, for every clockwise curl,
there is a counter-clockwise curl elsewhere (or at a different phase of the
cycle). The *net* directional circulation vanishes, just as the net current in
an AC circuit is zero.


### 2.3 The Scalar Magnitude (AC Analogy)

However, a washing machine full of turbulent water has zero net flow but
non-zero **Agitation**. An AC circuit has zero net current but non-zero
**Power**.

To measure the physical "substance" of the knot, we must measure the
**Magnitude** of the agitation, regardless of direction. We define the
**Vorticity Density** $\Omega$ as the time-averaged magnitude of the curl:

$$
\Omega(\mathbf{x}) = \langle |\nabla \times \mathbf{E}(\mathbf{x}, t)| \rangle_t
$$

This scalar field $\Omega(\mathbf{x})$ represents the raw amount of
electromagnetic "twist" or turbulence at any point.


### 2.4 The Total Integrated Vorticity

We define the intrinsic "strength" of the particle as the volume integral of
this density:

$$
\Gamma_{total} = \int_{Knot} \Omega(\mathbf{x}) \, d^3x
$$

Since

$$\nabla \times \mathbf{E}
= -\frac{\partial \mathbf{B}}{\partial t}$, $\Gamma_{total}
$$

is directly proportional to the total **Oscillation Energy** trapped in the standing wave.


### 2.5 The Measured Charge $q$

An observer measures the knot from a distance $r$. The total amount of agitation
$\Gamma_{total}$ is conserved. As this agitation projects outwards, it
distributes over the surface area of the shell ($4\pi r^2$).

The instrument (a voltmeter) measures the **Time-Averaged Intensity** of the
field impact on its sensor.
Since the total integrated magnitude $\Gamma_{total}$ is distributed over the
growing sphere, the **Surface Density of Vorticity Magnitude** decays as:

$$
\sigma_{\Omega}(r) = \frac{\Gamma_{total}}{4\pi r^2}
$$

We define the observable **Charge** $q$ as the coefficient of this projection:

$$
q \equiv k \cdot \Gamma_{total}
$$

Thus, the inverse-square law $E \propto q/r^2$ is not due to a point source
divergence. It is the geometric dilution of the **Total Vorticity Magnitude**
of the knot spread over the surface area of the universe.
