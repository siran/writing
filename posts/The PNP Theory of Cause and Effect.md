---
title: "The PNP Theory of Cause and Effect"
subtitle: "Causality from Topological Persistence in Scalar Fields"
authors: Fred Nedrock, Leera Vale, Max Freet, An M. Rodriguez
date: 2025-08-14
one-sentence-summary: |
  Causality emerges in the PNP framework because a topologically non-trivial scalar field configuration cannot remain static without violating stress–energy conservation, forcing ordered evolution.
summary: |
  We derive causality from first principles within the Point–Not–Point (PNP) framework. At its core lies the topological irreducibility of the fundamental $(1)$ mode: the simplest closed oscillation of a scalar field $U$ exhibiting a $\pi$ phase inversion, or "bounce." This $\mathbb{Z}_2$ invariant enforces loop persistence and forbids extinction without a phase slip. We explicitly ground this mode in the discrete solution space of source-free Maxwell dynamics (the toroidal hydrogenic spectrum). From this physically motivated topology, we prove that such a mode cannot remain static, formalizing cause–effect not as a postulate, but as the inevitable action of the field propagator on a persistent topological sector.
keywords:
  - PNP Framework
  - Topological Persistence
  - Causal Geometry
  - Scalar Field Theory
  - Z2 Invariant
  - Emergent Time
license: CC BY 4.0
---

# Introduction

In standard formulations of physics, causality is assumed as a primitive
ordering of events—time exists, and things move through it. In the
Point–Not–Point (PNP) framework, we invert this relationship. We propose that
causality emerges from **Topology**: specifically, from the requirement that a
non-trivial field configuration must evolve to maintain its structural
integrity.

We show that a minimally nontrivial loop of the scalar field $U$
(the fundamental "Entity") persists under evolution. We prove that such a mode
cannot remain static without violating local momentum conservation. Time here is
not assumed as a background ordering, but emerges as the parameter labeling
successive configurations required to preserve topology. Thus, cause–effect is
the temporal manifestation of topological persistence.


# The PNP Framework and the Fundamental Mode

Let $U: \mathcal{M} \to \mathbb{R}$ be a real scalar energy field. We define the
complex envelope $A(\mathbf{x},t)$ as a local phase–amplitude decomposition of
the oscillatory solutions of $U$:

$$
A(\mathbf{x},t) = \rho(\mathbf{x},t)\,e^{i\phi(\mathbf{x},t)}, \qquad \rho \ge 0, \ \phi \in \mathbb{R} \pmod{2\pi}
$$

*Note: The complex envelope $A$ is a bookkeeping device for local
oscillatory structure in a real scalar field; no additional $U(1)$
degrees of freedom are introduced.*


## The Physical Origin of the $(1)$ Mode

The topological object central to this theory—the **$(1)$ mode**—is
not an arbitrary mathematical postulate. It is the abstraction of the
fundamental standing-wave solution to Maxwell's equations on a toroidal
manifold.

As demonstrated in the derivation of the Schrödinger equation from source-free
electromagnetism [1], the imposition of single-valuedness on a toroidal field
configuration yields a discrete spectrum of modes labeled by integer winding
numbers $(m, n)$. For the symmetric case ($m = n$), the energy
of these modes scales as $E \propto 1/n^2$, reproducing the Rydberg series
characteristic of bound atomic states (Hydrogen) without invoking point charges.

The **$(1)$ mode** corresponds to the ground state ($n=1$)
of this physical hierarchy. It represents the "simplest knot" compatible with
the wave equation—a closed loop of energy with a $\pi$ phase twist.
While higher $n$ modes describe excited states, the
$(1)$ mode represents the irreducible topological obstruction that
defines the entity's existence. By focusing on the $(1)$ mode, we are
not inventing a shape; we are analyzing the topological properties of the most
fundamental stable structure allowed by classical field dynamics.


## Topological Sectors and the $(n)$ Notation

We denote topological sectors by $(n)$ with $n \in \mathbb{N}$,
representing the winding number of the phase around the core.

The $(1)$ mode is defined geometrically as a closed loop
$C$ encircling a core such that one traversal advances the phase
$\phi$ by $\pi$ (a Möbius-like twist).  This requires two
traversals to return to the initial state.

The holonomy along $C$ is:

$$
H(C) = \exp\!\left(i\oint_C \nabla\phi \cdot d\mathbf{l}\right) \in \{+1, -1\}
$$

This defines the discrete $\mathbb{Z}_2$ index $\nu$ (Parity):

$$
\nu = \frac{1 - H(C)}{2} = n \pmod 2
$$

* $\nu=0$: Trivial topology (Even $n$).
* $\nu=1$: Non-trivial topology (Odd $n$, including the
  fundamental $(1)$ mode).

**Physically, the $(1)$ mode traps the essence of a "continuous
bounce."** The field flows through the core, inverts phase, and re-emerges,
effectively reflecting off its own nodal structure without ever encountering a
hard boundary; a self-referential flow.

Crucially, $\nu$ is a topological invariant. It cannot change
continuously; it can only change via a **Phase Slip** (where $\rho \to 0$ at
a point on $C$), effectively breaking the loop.


# Field Dynamics and Stress–Energy

The source-free PNP equation of motion is given by the vanishing of the exterior
derivative of the dual:

$$
d(\star dU) = 0
$$

With a Lagrangian density $\mathcal{L}(U, \nabla U)$, the stress–energy tensor
is:

$$
T_{\mu\nu} = \nabla_\mu U\,\nabla_\nu U - g_{\mu\nu}\,\mathcal{L}, \qquad \nabla_\mu T^{\mu\nu} = 0
$$

*Note: No specific form of $\mathcal{L}$ is required for this argument beyond
locality, positivity of energy density, and the existence of a conserved
stress–energy tensor.*

We define the Energy Density ($u$) and Flux ($J^\mu$)
relative to a local time vector $t^\nu$:

$$
u = T^{00}, \qquad J^\mu = T^\mu{}_\nu\,t^\nu
$$


# Derivation of Causality

We now prove that "Time" is the byproduct of the $(1)$ mode's
necessary self-perpetuation.


## Sector Decomposition

The configuration space decomposes into disjoint sectors labeled by
$\nu$. The evolution generated by $d(\star dU)=0$ preserves sector
labels except at singularities (Phase Slips). Therefore, a persistent entity
satisfies:

$$
\nu(t+\Delta t) = \nu(t) = 1
$$


## Persistence Forbids Stasis (The Proof)

Assume, for the sake of contradiction, that the field is static:
$\Phi(t+\Delta t) = \Phi(t)$ for all $t$. This implies
$\partial_t U = 0$ everywhere on the loop, which means the momentum flux density
(energy flow) $T^{0i}$ must vanish.

However, for a loop with $\pi$-twist topology (the $(1)$
mode), the phase gradient $\nabla \phi$ is non-zero and twisted. This implies
nonzero spatial stress components ($T^{ij} \neq 0$). A static configuration
with non-zero internal stress requires external support to maintain force
balance ($\partial_j T^{ij} \neq 0$ without flow).

In a source-free vacuum, no such external force exists. Therefore, a static
$(1)$ mode violates local momentum balance. **Topology alone does not
generate motion; rather, the incompatibility between nontrivial topology and
static force balance in a source-free field enforces evolution.**

**Conclusion:** To maintain the $(1)$ mode (Persistence), the field
**cannot be static**.

$$
\Phi(t+\Delta t) \neq \Phi(t)
$$

Unlike conventional instabilities which depend on parameters, the instability of
a static $(1)$ mode is topologically protected.


## Propagator Form of Cause–Effect

Let $\mathcal{P}_{\Delta t}$ be the evolution operator. On the persistent
sector:

$$
\Phi(t+\Delta t) = \mathcal{P}_{\Delta t}\,\Phi(t)
$$

"Cause" is the state $\Phi(t)$. "Effect" is the state $\Phi(t+\Delta t)$.
The link between them is not an axiom, but the **Propagator of Topological
Persistence**. The effect is simply the next necessary configuration to prevent
the loop from breaking.


# Force from Stress–Flow

We can extend this to interactions. From $\nabla_\mu T^{\mu\nu}=0$ in a
stationary, spherically symmetric flow:

$$
\partial_r T^{rr} + \frac{2}{r}\big(T^{rr} - T^{\theta}{}_{\theta}\big) = 0
$$

For tangentially dominated energy transport (a spinning torus),
$T^{rr} \approx -u(r)$. The induced radial acceleration on test configurations
is:

$$
a_r(r) \propto -\partial_r T^{rr}(r) \approx \partial_r u(r)
$$

For configurations whose energy density exhibits vortex-like decay
($u(r) \sim 1/r$), this yields $a_r \sim -1/r^2$. Thus, this framework suggests
a gravitation-like interaction arising from the **Organization of Energy Flow**,
without the need to postulate intrinsic mass.


# Conclusion

In the PNP framework, we do not need to postulate that "Time Flows" or "Gravity
Attracts."

1.  **Causality** is the result of **Topological Persistence** (the
    $(1)$ mode implies $\partial_t \Phi \neq 0$).
2.  **Force** is the result of **Stress-Energy Conservation**
    ($\nabla_\mu T^{\mu\nu} = 0$).

Reality is a self-driving machine: it moves because it is topologically
forbidden from standing still.


# References

1.  **Palma, A., Rodriguez, A. M., Thorne, E.** (2025). *Deriving the
    Schrödinger Equation from Source-Free Maxwell Dynamics*. Preferred Frame
    Lab. https://writing.preferredframe.com/doi/10.5281/zenodo.18316984
