---
title: "Gravitational Lensing in a Maxwell Universe: Recovering the Factor of 2 from Flux Continuity"
subtitle: "Deriving the 1.75 arcsecond deflection using Vector Flux rather than Scalar Mass"
author: An M. Rodriguez, Alex Mercer
date: 2026-01-17
keywords: gravitational lensing, Eddington number, dielectric gravity, Maxwell equations, Poynting vector, flux vs mass, continuity equation
one-sentence-summary: We demonstrate that the discrepancy between Newtonian (0.875'') and Relativistic (1.75'') light bending predictions arises from treating light as averaged mass rather than instantaneous flux; preserving the vector nature of propagation in a dielectric vacuum naturally recovers the missing factor of 2.
summary: Standard semi-classical derivations of light bending treat photons as "massive particles" with effective mass E/c^2, yielding a deflection of 0.875 arcseconds—exactly half the observed value. General Relativity corrects this by invoking spatial curvature. We propose an alternative resolution within classical field theory. By treating gravity as a dielectric variation in the vacuum, and—crucially—coupling the gradient to the instantaneous energy flux S rather than the time-averaged energy density u, we show that the averaging penalty (1/2) inherent to massive matter does not apply to free radiation. This vector-flux coupling naturally yields the full 1.75 arcsecond deflection derived from Maxwell’s equations and continuity alone.
---

## The Problem: The Newtonian Deficit

It is well known that treating light as a projectile with mass $m = E/c^2$
falling in a gravitational field yields a deflection angle of:

$$
\theta_{\text{Newton}} = \frac{2GM}{Rc^2} \approx 0.875 \text{ arcseconds (at Solar limb)}.
$$

Observation confirms the value is twice this:

$$
\theta_{\text{Observed}} \approx 1.75 \text{ arcseconds}.
$$

General Relativity resolves this by attributing half the bending to time
dilation (the Newtonian part) and half to spatial curvature.

In a **Maxwell Universe**, where there is no spatial curvature, we must explain
this factor of 2 through electrodynamics.


## Gravity as a Dielectric Gradient

As established in *Gravity as a Dielectric* (Rodriguez, 2025), we model the
gravitational potential $\Phi$ as an increase in the electromagnetic
density of the vacuum, creating an effective refractive index $n(\mathbf{r})$.

$$
c(\mathbf{r}) = \frac{c_0}{n(\mathbf{r})}.
$$

The standard assumption is that refractive index scales linearly with the
potential energy density:

$$
n(\mathbf{r}) \approx 1 + \frac{|\Phi|}{c^2} = 1 + \frac{GM}{rc^2}.
$$

Applying Fermat’s Principle (or Snell’s Law) to this refractive profile yields:

$$
\theta = \int_{-\infty}^{\infty} \nabla_\perp n \, dz = \frac{2GM}{Rc^2}.
$$

This reproduces the Newtonian result (0.875''). The model appears to fail.


## The Error: Averaging the Flux

The failure arises from a hidden assumption: treating the electromagnetic wave
as a "particle" of mass.

Mass, in the Maxwell Universe, is **Geometric Inertia**—a consequence of
trapped, circulating energy. As derived in *Geometric Inertia* (2026), effective
mass $m$ is related to total energy $E$ by the average
forward propagation:

$$
m = \frac{E}{c^2} \langle \sin^2 \psi \rangle,
$$

where $\psi$ is the pitch angle of the flow. For a trapped particle
(virialized knot), the energy is equipartitioned between circulation and
translation.

**Averaging Penalty:** When we define the "mass equivalent" of energy, we are
effectively taking a time-average of a dynamic wave. This introduces a factor of
**1/2**.

The Newtonian calculation implicitly treats light as "matter moving at
$c$." It applies the coupling rules of averaged matter to raw
radiation.


## The Correction: Flux Continuity

Light is not matter. It is pure, untrapped flux.

In Maxwell theory, the primary ontological object is the **Poynting Vector
$\mathbf{S}$**, not the scalar mass.

When a wave propagates through a dielectric gradient, the bending is driven by
the **instantaneous wavefront**, not the time-averaged energy envelope.


### The Symmetry Argument

1.  **Massive Matter (Scalar Average):** Gravity acts on the trapped energy. The
    trapped energy is the "Sine" component of the flow. Due to the virial
    symmetry of the knot, only **half** the total field energy contributes to
    the inertial interaction in any single vector direction.
    $$\text{Coupling}_{\text{Matter}} \propto \frac{1}{2}$$

2.  **Free Radiation (Vector Flux):** Gravity (the dielectric gradient) acts on
    the flow $\mathbf{S}$. The flow is the "Cosine" component. For free
    radiation, $\cos(0) = 1$. The flow is fully aligned. There is no
    circulation, no averaging, and no "sine" component to dilute the
    interaction. $$\text{Coupling}_{\text{Flux}} \propto 1$$


### The Ratio

The ratio of the coupling strength of **Raw Flux** (Light) to **Averaged Mass**
(Matter) is:

$$
\frac{\text{Flux Coupling}}{\text{Mass Coupling}} = \frac{1}{1/2} = 2.
$$


## Result: The Eddington Number

If the Newtonian prediction (based on mass equivalence) is $\theta_{N}$,
then the Maxwell prediction (based on flux continuity) must be:

$$
\theta_{\text{Maxwell}} = 2 \times \theta_{N}.
$$

Substituting the Newtonian value:

$$
\theta_{\text{Maxwell}} = 2 \times \left( \frac{2GM}{Rc^2} \right) = \frac{4GM}{Rc^2}.
$$

$$
\theta_{\text{Maxwell}} \approx 1.75 \text{ arcseconds}.
$$


## Conclusion

The "missing" bending angle in classical gravity is not a failure of Euclidean
geometry, but a failure of the "mass-energy equivalence" heuristic.

- **Matter** is time-averaged field energy (mass).
- **Light** is instantaneous field flux.

Treating light as mass incorrectly applies a 1/2 averaging penalty. Treating
light as flux recovers the full interaction strength.

The Maxwell Universe accurately predicts the 1.75 arcsecond deflection of
starlight assuming only:
1.  Maxwell's Equations.
2.  Continuity of Energy.
3.  Gravity as a dielectric modification of vacuum density.

No curved spacetime is required.
