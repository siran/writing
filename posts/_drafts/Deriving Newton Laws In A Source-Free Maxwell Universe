---
title: Deriving Newton and Maxwell Dynamics From Continuous, Divergence-Free Energy Transport
subtitle: Minimal kinematics, minimal closure, and when circulation becomes attracting
author: An M. Rodriguez, Alex Mercer
date: 2026-01-20
one-sentence-summary: From local conservation and source-free transport we obtain the solenoidal (curl) structure of admissible evolution laws; with dissipation plus topological constraints, circulation relaxes toward Beltrami states, and stable circulating packets admit Newton-like effective dynamics.
summary: We start from a nonnegative energy density u(x,t) and an energy flux S(x,t) obeying a local continuity equation. In source-free regions, ∇·S=0 constrains admissible transport but does not force closed streamlines in 3D. We then pose the closure problem: what local evolution laws preserve the solenoidal constraint? The minimal divergence-preserving differential operator is curl. Under additional symmetry/linearity/energy assumptions this yields Maxwell-type dynamics. Finally, we explain when circulation becomes attracting: not in reversible ideal transport, but under dissipative relaxation constrained by helicity/topology, where energy decays to force-free (Beltrami) states ∇×S = λS.
keywords: continuity equation, divergence-free flow, curl dynamics, Helmholtz-Hodge decomposition, Beltrami fields, helicity constraint, Taylor relaxation, Maxwell theory, effective Newton laws
---

# Overview

We build the theory in layers.

**Layer 0 (observational/empirical input).** Energy does not appear or disappear
locally without accounting, and it moves continuously through space.

**Layer 1 (kinematics).** This is encoded by a continuity equation relating
energy density u and energy flux S.

**Layer 2 (source-free structure).** In source-free regions, the flux field is
solenoidal: ∇·S=0.

**Layer 3 (closure).** Kinematics alone does not determine how S evolves. We
identify the minimal class of *local* evolution laws that preserve ∇·S=0.

**Layer 4 (attraction to circulation).** Divergence-free does *not* imply closed
streamlines in 3D. To make circulation an *attractor* one needs irreversibility
(dissipation) plus an invariant such as helicity/topology; then the flow relaxes
toward Beltrami states.

**Layer 5 (effective mechanics).** Stable circulating packets can be treated as
coherent structures with approximate conserved momentum, yielding Newton-like
effective equations under weak coupling.

The document is explicit about which claims follow from which assumptions.

---


# Part I — Kinematic Foundations (what is forced)

## 1. Energy and continuity

Assume:

- a nonnegative energy density \(u(x,t)\ge 0\),
- an energy flux \(S(x,t)\) (vector field),
- local accounting: energy changes only by transport across boundaries.

This is expressed by the local continuity equation \[ \partial_t u + \nabla\cdot
S = 0. \]

Interpretation: for any fixed control volume \(V\) with boundary \(\partial V\)
and outward normal \(n\), \[ \frac{d}{dt}\int_V u\,dV = -\int_{\partial V}
S\cdot n\,dA, \] obtained from the divergence theorem and the PDE.

This is bookkeeping, not dynamics.

---


## 2. Source-free structure

A **source-free region** is one where energy density can change only by flow,
not by local creation/destruction. In such a region, a common idealization is:
\[ \nabla\cdot S = 0. \]

Important:
- If also \(\partial_t u + \nabla\cdot S = 0\) holds, then in that region
  \(\partial_t u = 0\).
- So “∇·S=0” is best read as “flux has no local sinks/sources”; it does **not**,
  by itself, say the energy density is evolving.

We will use ∇·S=0 as a *structural constraint* on admissible transport fields,
and later impose a separate evolution law for S.

---


## 3. Flow lines: what divergence does and does not imply (3D)

### 3.1 Definition

Given a transport field \(S(x,t)\), a flow line at fixed time (or a trajectory
under a steady field) is an integral curve \(\gamma(t)\) satisfying \[
\dot{\gamma}(t) = S(\gamma(t)). \]


### 3.2 Interior “starts/ends” are not about divergence

If \(S\) is locally Lipschitz, solutions exist and are unique locally
(Picard–Lindelöf). In that setting, an integral curve cannot “start” or “end” at
a regular interior point; it extends at least for a short time forward and
backward. This is an ODE fact, not a divergence fact.
:contentReference[oaicite:0]{index=0}


### 3.3 Divergence-free does not force closed streamlines in 3D

Even if \(\nabla\cdot S=0\) and the domain is bounded, streamlines need not
close.

**Counterexample (simple).** On a bounded domain \(D\subset\mathbb{R}^3\), take
\(S=(1,0,0)\). Then \(\nabla\cdot S=0\) and streamlines are straight lines
crossing the domain.

**Counterexample (chaotic bounded trajectories).** There exist smooth, steady,
divergence-free 3D flows with chaotic trajectories (streamline chaos), e.g.
ABC-type flows on a 3-torus. :contentReference[oaicite:1]{index=1}

So:

> **Claim (correct).**
> In 3D, “bounded + divergence-free + continuous” does **not** imply closed flow
> lines.
> Closure requires extra structure (symmetry, integrability, dissipation +
> constraints, etc.).


---


## 4. Helmholtz–Hodge structure of solenoidal transport

A key kinematic fact: under suitable smoothness and boundary/decay conditions, a
vector field decomposes into divergence-free and curl-free parts
(Helmholtz/Hodge). :contentReference[oaicite:2]{index=2}

On a simply connected region with appropriate boundary conditions, a
divergence-free field admits a vector potential \(A\) such that \[ \nabla\cdot
S=0 \quad\Rightarrow\quad S = \nabla\times A. \] This is representation, not
dynamics.

**Meaning.** Source-free transport is “purely solenoidal”: it can be expressed
as curl of something.

---


## 5. Local deformation: correct “stretch + rotate” statement

The correct linear-algebra object describing local deformation is the
**Jacobian** \(\nabla S\), a matrix field.

It has the unique decomposition \[ \nabla S = D + \Omega, \] where \[ D =
\frac12(\nabla S + \nabla S^{T}) \quad\text{(symmetric strain-rate)}, \] \[
\Omega = \frac12(\nabla S - \nabla S^{T}) \quad\text{(antisymmetric rotation)}.
\] The antisymmetric part corresponds to vorticity \(\omega=\nabla\times S\) (in
3D, \(\Omega\) is dual to \(\omega\)).

This is purely kinematic: it does not specify \(\partial_t S\).

---


# Part II — The Closure Problem (what evolution laws are compatible)

## 6. What “closure” means

Kinematics constrains accounting: \[ \partial_t u + \nabla\cdot S = 0. \] But it
does not specify how \(S\) changes.

A **local transport closure** postulates an evolution PDE for \(S\): \[
\partial_t S = \mathcal{D}(S, \nabla S, \nabla^2 S,\dots). \] “Local” here means
built from \(S\) and its spatial derivatives at the same point.

We ask:

> What local differential operators preserve the constraint \(\nabla\cdot S=0\)?


---


## 7. Minimal divergence-preserving operators

Take divergence of the evolution law: \[ \partial_t(\nabla\cdot S)=\nabla\cdot
\mathcal{D}(\cdots). \] To preserve \(\nabla\cdot S=0\) for all time, we need
\(\nabla\cdot \mathcal{D}=0\) whenever \(\nabla\cdot S=0\).


### 7.1 Gradient-driven evolution generally fails

If \(\partial_t S = \nabla \phi\), then \[ \partial_t(\nabla\cdot
S)=\nabla^2\phi, \] generically nonzero. So pure-gradient driving does not
preserve the constraint without special tuning.


### 7.2 Curl-driven evolution preserves divergence identically

If \[ \partial_t S = \nabla\times G \] for some (possibly field-dependent)
\(G\), then \[ \partial_t(\nabla\cdot S)=\nabla\cdot(\nabla\times G)=0 \]
identically (vector calculus identity).

So:

> **Minimal structural statement.**
> Any evolution law of pure curl form preserves the solenoidal constraint
> automatically.


This is the rigorous replacement for “rotation without creating sources”.

---


## 8. From “curl closure” to Maxwell-type dynamics (minimal assumptions)

A curl closure alone is not Maxwell. To reach Maxwell-like structure, add
standard minimality constraints:


### Assumption A (linearity near equilibrium)

For small disturbances, evolution is linear: \[ \partial_t S = \mathcal{L}S \]
for a linear differential operator \(\mathcal{L}\).


### Assumption B (isotropy and locality)

\(\mathcal{L}\) is built from ∇, and does not pick a preferred direction.


### Assumption C (preserve solenoidal constraint)

If \(\nabla\cdot S=0\) initially, it remains so.

Under these conditions, the lowest-order nontrivial possibility is a curl-type
operator: \[ \partial_t S = c\, \nabla\times S \] or, more generally, the
coupling of two solenoidal fields \(E,B\): \[ \partial_t B = -\nabla\times
E,\qquad \partial_t E = +c^2 \nabla\times B, \] with constraints \[ \nabla\cdot
B = 0,\qquad \nabla\cdot E = 0 \] in the source-free sector.

This is exactly the Maxwell curl-pair in vacuum (no charges/currents), and it
implies wave equations: \[ \partial_t^2 B = c^2 \nabla^2 B,\qquad \partial_t^2 E
= c^2 \nabla^2 E, \] using \(\nabla\times(\nabla\times B)=\nabla(\nabla\cdot
B)-\nabla^2B=-\nabla^2B\) when \(\nabla\cdot B=0\).

**Meaning.** The Maxwell curl structure is the simplest linear
solenoidal-preserving local closure that supports finite-speed propagation.

(Full electromagnetism with sources requires additional identifications: what
constitutes “charge/current” and how they enter the constraint equations.)

---


# Part III — When Circulation Becomes Attracting (what extra physics is needed)

## 9. Key point: ideal solenoidal transport is not generically attracting

If the evolution is time-reversible (as in ideal Euler-like transport),
“attractors” are not generic: trajectories can mix, filament, and wander without
converging. Chaotic advection in volume-preserving 3D flows is widely
documented. :contentReference[oaicite:3]{index=3}

So to make circulation *attracting*, you need **irreversibility**, i.e.
dissipation (or coarse-graining) plus at least one robust constraint that
prevents total decay to zero.

---


## 10. The mathematical object controlling “circulation content”: helicity

For a solenoidal field \(S\) with vector potential \(A\) (\(S=\nabla\times A\)),
define **helicity** \[ H[S] = \int_V A\cdot S \, dV. \] Helicity measures
linkage/twist of field lines (topological content). It is central in fluid and
MHD relaxation.

In ideal (non-dissipative) dynamics, helicity-like invariants can be conserved;
under weak dissipation, helicity can decay slower than energy, yielding
selective decay and relaxation.

(For magnetic fields this is standard: magnetic helicity is approximately
conserved during fast relaxation, motivating Taylor/Woltjer theory.)
:contentReference[oaicite:4]{index=4}

---


## 11. A rigorous “attractor mechanism”: energy minimization at fixed helicity

### 11.1 The constrained variational principle

Consider minimizing energy \[ E[S] = \frac12 \int_V |S|^2\, dV \] subject to
fixed helicity \(H[S]=H_0\) and \(\nabla\cdot S=0\), with appropriate boundary
conditions.

The Euler–Lagrange equation yields the **Beltrami (force-free) condition** \[
\nabla\times S = \lambda S \] for a scalar Lagrange multiplier \(\lambda\)
(constant in simple settings).

This is the “curl eigenfield” condition.

This is not folklore; it is a standard result in magnetic energy minimization
under helicity constraints and has rigorous modern treatments.
:contentReference[oaicite:5]{index=5}


### 11.2 Why this implies circulation

If \(\nabla\times S = \lambda S\) with \(\lambda\neq 0\), then \(S\) is
everywhere aligned with its curl. Such fields are maximally helical and
intrinsically swirling; they are the canonical mathematical embodiment of
persistent circulation.

---


## 12. Dynamics that actually converges to Beltrami states (a concrete model)

To turn the variational principle into an *attractor*, you need a dissipative
evolution that:

1) decreases energy \(E[S]\) monotonically,
2) preserves (approximately) helicity \(H[S]\),
3) respects \(\nabla\cdot S=0\).


### 12.1 Taylor relaxation (magnetic case; prototype)

Taylor’s theory posits rapid relaxation toward minimum energy at fixed helicity,
producing force-free equilibria (Beltrami fields). This is a canonical
“circulation becomes attracting” mechanism.
:contentReference[oaicite:6]{index=6}

**Physical meaning.** Small-scale reconnection/dissipation reduces energy while
conserving global helicity to leading order; the remaining constraint selects a
Beltrami state.


### 12.2 A generic constrained gradient flow

Abstractly, one may model relaxation as a projected gradient flow: \[ \partial_t
S = -\mathbb{P}\Big(\frac{\delta E}{\delta S} - \lambda\, \frac{\delta H}{\delta
S}\Big), \] where \(\mathbb{P}\) is the Leray projector onto divergence-free
fields (Hodge projection), and \(\lambda\) is chosen so that \(dH/dt=0\).

Since \(\delta E/\delta S = S\) and \(\delta H/\delta S = 2A\) (up to
gauge/boundary care), equilibria satisfy \[ S = \lambda A \quad\Rightarrow\quad
\nabla\times S = \lambda S, \] i.e. Beltrami.

This provides a mathematically clean template: “circulation attracts” because
the dynamics explicitly drives the system down the energy functional while
respecting a topological constraint.

(Implementation details depend on domain and boundary conditions; the Hodge
decomposition framework organizes this cleanly.
:contentReference[oaicite:7]{index=7})

---


## 13. Summary: formal conditions for circulation to be attracting (3D)

Circulation is not forced by ∇·S=0. It becomes attracting when:

1) **Dissipation / irreversibility exists** so that some norm (typically energy)
   decreases.

2) **A nontrivial invariant survives dissipation** e.g. helicity/topological
   linkage decays much more slowly than energy.

3) **The evolution respects solenoidal constraint** so the system stays in the
   divergence-free manifold.

4) **The constrained minimum is nontrivial** so the system cannot relax to the
   zero field without violating the invariant.

Then the long-time state is a Beltrami / force-free / curl-eigenfield
configuration: \[ \nabla\times S = \lambda S, \] which is a mathematically
precise “persistent circulation” state.

---


# Part IV — Effective Newtonian Dynamics of Coherent Circulating Packets (what must be assumed)

## 14. From fields to “objects”: coherent structures

To get Newton-like behavior, one must introduce a controlled approximation:

> There exist long-lived, localized, approximately stable circulating
> configurations of the transport field.


This is not automatic; it is an empirical/dynamical claim about the existence of
coherent structures (vortices, solitons, knotted tubes, etc.) in the chosen
closure.

Under such conditions, one can define effective conserved quantities by
integrating densities over the packet.

---


## 15. Momentum balance from flux (field-theoretic form)

The clean way to derive Newton-like laws is via a local momentum continuity
equation: \[ \partial_t p + \nabla\cdot \Pi = 0, \] where \(p\) is momentum
density and \(\Pi\) is a momentum-flux (stress) tensor.

Integrating over a volume \(V\): \[ \frac{d}{dt} \int_V p\, dV = -
\int_{\partial V} \Pi\, n \, dA. \] This is the rigorous content behind “force
equals momentum flux”.

For a localized packet, define total momentum \[ P = \int_{\text{packet}} p\,
dV. \] Then external flux through the packet boundary changes \(P\): \[
\frac{dP}{dt} = F_{\text{net}}, \] which is Newton’s second law in integral
form.

Newton’s third law appears when two packets exchange momentum through their
shared flux: the total momentum is conserved if the combined system has no net
boundary flux.

**Note.** To make this explicit you must specify the underlying closure enough
to define \(p\) and \(\Pi\). In electromagnetism this is standard via the
stress-energy tensor; in fluids via Reynolds/Cauchy stress.

So “Newton emerges” is best stated as:

> If the closed field theory admits localized long-lived structures and a
> conserved stress-energy, then their collective-coordinate dynamics obeys
> Newton-like momentum balance at leading order.


---


# Closing Statement (clean and correct)

From continuity and source-free structure alone, we obtain:

- a strict accounting identity (continuity),
- a solenoidal constraint in source-free regions (∇·S=0),
- a kinematic representation \(S=\nabla\times A\) under standard conditions,
- and a sharp correction: in 3D, ∇·S=0 does **not** force closed streamlines.

To get dynamics, we must choose a closure. The minimal local
divergence-preserving operator is curl, and the simplest linear
solenoidal-preserving propagation closure yields Maxwell-type curl dynamics in
the source-free sector.

To make circulation *attracting* in 3D, we must add irreversibility plus a
robust constraint such as helicity/topology. Under such conditions, energy
minimization at fixed helicity drives relaxation toward Beltrami states
\(\nabla\times S=\lambda S\), which are precise mathematical models of
persistent circulation. :contentReference[oaicite:8]{index=8}

Finally, if the resulting field theory supports stable localized circulating
packets and a conserved momentum flux, their slow collective motion obeys
Newton-like momentum balance.

---


# References (primary pointers)

- Picard–Lindelöf existence/uniqueness for ODE integral curves.
  :contentReference[oaicite:9]{index=9}
- Helmholtz/Hodge decomposition and solenoidal projection.
  :contentReference[oaicite:10]{index=10}
- 3D divergence-free flows with chaotic trajectories (ABC flows).
  :contentReference[oaicite:11]{index=11}
- Chaotic advection review. :contentReference[oaicite:12]{index=12}
- Magnetic/Beltrami energy minimizers under helicity constraint (rigorous).
  :contentReference[oaicite:13]{index=13}
- Taylor relaxation / helicity-constrained relaxation to force-free states.
  :contentReference[oaicite:14]{index=14}
- Helicity’s role and inverse cascade context.
  :contentReference[oaicite:15]{index=15}
