---
title: The Physics of Energy Flow - Appendix A1
date: 2026-04-11
kind: appendix
part: Appendices
summary: >
  A rigorous proof that the exterior curl-flux of a net-chiral toroidal closure
  is isotropically distributed on large enclosing shells. The uniform
  distribution is shown to be the unique minimum of the exterior shell energy
  under fixed total flux, with the restoring force derived from the
  self-refraction principle. Topological protection of the winding numbers is
  then shown to elevate this minimum from local to global stability.
keywords:
  - toroidal closure
  - exterior curl flux
  - isotropy
  - energy minimum
  - topological protection
  - winding number
  - self-refraction
---

# Appendix A1. Isotropy of the Exterior Shell as a Topologically Protected Energy Minimum

Chapter 10 asserts that the exterior curl-flux of a net-chiral toroidal closure
is distributed isotropically over large enclosing shells, so that its surface
density falls as $1/r^2$. This appendix proves that claim in three steps.

1. A non-uniform flux distribution on an enclosing shell creates a restoring
   force, derived directly from the self-refraction principle of Chapter 7b.

2. The uniform distribution is the unique minimum of the exterior shell energy
   subject to fixed total flux, by a direct variational argument.

3. The winding numbers $(m,n)$ are topological invariants of the source-free
   flow. Their rigidity prevents any source-free perturbation from moving the
   closure out of its $(m,n)$ sector, so the energy minimum is globally stable.


## A1.1 Setup and Notation

Let $\mathcal{T}$ denote a toroidal closure with net chiral winding $(m,n)$.
From the divergence-of-curl argument of Chapter 10, the total organized curl
flux

$$
\Phi_{(m,n)} := \int_{S_r} (\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}\,dA
$$

is the same for every enclosing shell $S_r$ of radius $r$ centered on the
closure, and is nonzero when the net chiral winding is nonzero.

Write the flux density per unit solid angle on $S_r$ as $\phi(\hat{\mathbf{r}},r)$,
defined by

$$
(\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}\big|_{S_r}
=
\frac{\phi(\hat{\mathbf{r}},r)}{r^2},
$$

so that the conservation law reads

$$
\int_{S^2} \phi(\hat{\mathbf{r}},r)\,d\Omega = \Phi_{(m,n)},
\qquad \forall r > r_0,
$$

where $r_0$ is a radius enclosing $\mathcal{T}$ and $d\Omega$ is the standard
solid-angle measure on the unit sphere.

From the amplitude-squared relation of Chapter 7a, the local exterior energy
density on $S_r$ is proportional to the square of the local field amplitude.
The organized $(m,n)$ sector carries amplitude proportional to the curl flux per
unit area, so

$$
u_{(m,n)}(\hat{\mathbf{r}},r)
=
\kappa\,\frac{\phi(\hat{\mathbf{r}},r)^2}{r^4},
$$

for a positive constant $\kappa$ fixed by the normalization of the two-aspect
split. The total organized exterior energy on the shell is therefore

$$
U_r
=
\int_{S^2} u_{(m,n)}\,r^2\,d\Omega
=
\frac{\kappa}{r^2}
\int_{S^2} \phi(\hat{\mathbf{r}},r)^2\,d\Omega.
$$


## A1.2 Non-uniform Flux Produces a Restoring Force

Suppose $\phi$ is not constant on $S_r$. Define its tangential gradient on
$S_r$ by $\nabla_\perp\phi$. By the self-refraction principle of Chapter 7b,
a region of higher local energy density loads the flow more strongly, producing
a lower effective advance rate:

$$
c_\mathrm{eff}(\hat{\mathbf{r}},r)
=
\frac{c}{n_\mathrm{eff}(\hat{\mathbf{r}},r)},
\qquad
n_\mathrm{eff} \propto \phi(\hat{\mathbf{r}},r).
$$

A tangential gradient of $c_\mathrm{eff}$ bends transport toward the more
strongly loaded side. The transverse refractive force per unit volume exerted on
the exterior flow is (Chapter 12, ray equation)

$$
\mathbf{f}_\perp = \nabla_\perp n_\mathrm{eff}
\propto
\nabla_\perp\phi.
$$

This force acts on the vortex tubes constituting the exterior continuation of
$\mathcal{T}$. A nonzero $\nabla_\perp\phi$ therefore drives tangential
redistribution of flux on $S_r$. The force vanishes if and only if

$$
\nabla_\perp\phi = 0
\qquad\text{on }S_r,
$$

that is, when $\phi$ is constant over $S_r$.

The direction of the force is toward regions of higher $\phi$, so it moves flux
away from depleted sectors and toward enriched ones. This is a restoring force
toward uniformity, not away from it.


## A1.3 Uniform Distribution is the Unique Energy Minimum

**Proposition.** Among all non-negative functions $\phi: S^2 \to \mathbb{R}_{\geq 0}$
satisfying

$$
\int_{S^2} \phi\,d\Omega = \Phi_{(m,n)} =: C > 0,
$$

the functional

$$
I[\phi] := \int_{S^2} \phi^2\,d\Omega
$$

attains its minimum uniquely at

$$
\phi_* = \frac{C}{4\pi} = \mathrm{const}.
$$

**Proof.** Write $\phi = \phi_* + \delta\phi$, where
$\phi_* = C/4\pi$ and $\int_{S^2}\delta\phi\,d\Omega = 0$. Then

$$
I[\phi]
=
\int_{S^2}(\phi_*+\delta\phi)^2\,d\Omega
=
4\pi\phi_*^2 + 2\phi_*\underbrace{\int_{S^2}\delta\phi\,d\Omega}_{=\,0}
+ \int_{S^2}(\delta\phi)^2\,d\Omega.
$$

Since $(\delta\phi)^2 \geq 0$ pointwise, with equality if and only if
$\delta\phi = 0$ identically,

$$
I[\phi] \geq 4\pi\phi_*^2 = \frac{C^2}{4\pi} = I[\phi_*],
$$

with equality if and only if $\phi = \phi_*$ almost everywhere on $S^2$.
$\square$

**Remark.** This is equivalent to the Cauchy-Schwarz inequality

$$
C^2
=
\left(\int_{S^2}\phi\,d\Omega\right)^2
\leq
\left(\int_{S^2} 1^2\,d\Omega\right)\!\left(\int_{S^2}\phi^2\,d\Omega\right)
=
4\pi\,I[\phi],
$$

with equality iff $\phi$ is proportional to $1$, i.e., constant. Both proofs
are elementary and reach the same strict minimum.

**Consequence.** The total exterior shell energy $U_r \propto I[\phi]/r^2$ is
minimized uniquely when $\phi$ is uniform over $S_r$. Any non-uniform
distribution carries strictly higher exterior energy and, by Section A1.2, is
subject to a restoring force. Uniform flux is therefore a critical point, and
the proposition shows it is a strict minimum, not a saddle.


## A1.4 Topological Protection: Local Minimum is Global Minimum

The argument so far establishes that uniform flux is a strict local minimum of
$U_r$ within the space of flux distributions satisfying fixed total $C$. It
remains to rule out escape to a lower-energy configuration in a different
winding class.

**Definition.** The winding numbers of the $(m,n)$ flow on $\mathcal{T}$ are

$$
m = \frac{1}{2\pi}\oint_{\gamma_1} d\varphi,
\qquad
n = \frac{1}{2\pi}\oint_{\gamma_2} d\theta,
$$

where $\gamma_1$ and $\gamma_2$ are the two independent non-contractible cycles
of the torus, and $\varphi$, $\theta$ are the respective phase angles of the
flow around each cycle. Because the flow is continuous and single-valued on
each cycle, $m$ and $n$ are integers.

**Lemma.** Under any continuous source-free deformation of $\mathcal{T}$, the
winding numbers $m$ and $n$ are preserved.

**Proof.** The winding number $m$ is the degree of the map
$\gamma_1 \to S^1$ defined by the phase of the flow amplitude $f$ around
$\gamma_1$. This degree is a homotopy invariant: it cannot change under a
continuous deformation of the map. A deformation of the map corresponds here
to a continuous source-free evolution of the flow.

The only way $m$ can change is if the map $\gamma_1 \to S^1$ becomes
discontinuous at some instant — that is, if the flow amplitude $|f|$ vanishes
somewhere on $\gamma_1$, destroying the phase. But $|f|^2 = u > 0$ everywhere
on the closure, because a zero of $|f|$ on $\mathcal{T}$ is a local sink,
forbidden by source-free continuity. Therefore $|f| > 0$ at all times, the
phase map is everywhere defined and continuous, and $m$ cannot change.
The identical argument applies to $n$. $\square$

**Theorem.** The uniform-flux equilibrium of the $(m,n)$ closure is globally
stable: no source-free perturbation of any amplitude can move the system to a
configuration with different winding numbers.

**Proof.** By the Lemma, any source-free evolution preserves $(m,n)$.
Any configuration reachable from the $(m,n)$ equilibrium under source-free
dynamics therefore belongs to the same winding class. Within that class,
Section A1.3 shows the uniform-flux distribution is the unique minimum of
$U_r$. The system cannot exit the $(m,n)$ class, and within that class the
equilibrium is the unique minimum. $\square$

**Remark.** The distinction between local and global stability is resolved
entirely by topology. Without topological protection, one would need to check
whether the closure can tunnel through a zero-amplitude configuration to reach
a lower-energy winding class. The source-free constraint forbids that
configuration from arising. The winding is frozen, and the energy minimum is
therefore global.


## A1.5 Exterior Shell Density

From the uniform flux $\phi_* = C/4\pi = \Phi_{(m,n)}/4\pi$ and the
energy-density relation of Section A1.1, the exterior organized energy density
on $S_r$ is

$$
u_{(m,n)}(r)
=
\kappa\,\frac{\phi_*^2}{r^4}
=
\frac{\kappa\,\Phi_{(m,n)}^2}{16\pi^2 r^4}.
$$

The total organized energy on $S_r$ is

$$
U_r
=
4\pi r^2\cdot u_{(m,n)}(r)
=
\frac{\kappa\,\Phi_{(m,n)}^2}{4\pi r^2}.
$$

Writing $Q^2 := \kappa\,\Phi_{(m,n)}^2/4\pi$, the shell energy density is

$$
\boxed{
u_{(m,n)}(r) = \frac{Q^2}{4\pi r^4},
\qquad
\sigma(r) := \frac{U_r}{4\pi r^2} = \frac{Q^2}{(4\pi)^2 r^4}.
}
$$

The shell density falls as $1/r^4$ in energy and as $1/r^2$ in the amplitude
(field-strength) reading. It is isotropic — independent of $\hat{\mathbf{r}}$ —
by the result of Section A1.3, and that isotropy is globally stable by
Section A1.4.

The quantity $Q$, proportional to $\Phi_{(m,n)}$, is signed by the handedness
of the net chiral winding and is an integer multiple of its elementary value.
This is the exterior scalar that Chapter 11 identifies with charge.


## A1.6 Summary

The three steps of this appendix establish:

1. **Restoring force** (Section A1.2). A non-uniform flux distribution on an
   enclosing shell creates a tangential self-refraction force proportional to
   $\nabla_\perp\phi$, driving flux toward uniformity.

2. **Strict energy minimum** (Section A1.3). Among all distributions with
   fixed total flux $C$, the uniform distribution $\phi = C/4\pi$ uniquely
   minimizes the exterior shell energy. Any deviation raises the energy
   strictly.

3. **Global stability by topology** (Section A1.4). The winding numbers
   $(m,n)$ are homotopy invariants of the source-free flow. They cannot change
   under any continuous source-free evolution because a change would require a
   zero of $|f|$ on the closure, which is a sink and is forbidden. The energy
   minimum is therefore global, not merely local.

Together these three steps ground the isotropy assertion of Chapter 10 as a
derived result rather than an assumption, and identify the $1/r^2$ shell
density as the necessary exterior form of a topologically stable net-chiral
toroidal closure.
