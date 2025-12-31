---
title: A Maxwell Universe – Part II — content map
date: 2025-12-31 15:23
---


## Part II content map

Rydberg $\to$ discreteness from global continuity
- Standing-wave closure on non-contractible cycles forces integer labels.
- $1/n^2$ scaling is energy reorganization under fixed total energy.

Torus $\to$ minimal topology that supports two independent closure integers
- Two fundamental cycles $\Rightarrow$ two winding numbers $(m,n)$.
- Topology supplies the counting; no particles required.

Tube $\to$ concrete carrier for winding and phase closure
- A flux tube (waveguide) is the geometric object that winds on the torus.
- “Knot” means the tube’s energy-flow lines close globally.

Self-refraction $\to$ existence of bounded, persistent solutions (stability)
- No sources, no material medium: confinement must be internal.
- Stability = closed (or time-averaged closed) Poynting flux through $\partial V$:
  $$
  \left\langle \oint_{\partial V}\vec S\cdot d\vec A \right\rangle_T = 0.
  $$
- Mechanism: linear superposition + phase structure $\Rightarrow$ cross-terms in
  $\vec S$ redirect energy flow into recurrent paths.

Conservation laws $\to$ momentum and torque as field integrals (no mechanics postulates)
- Energy density and flux:
  $$
  u=\tfrac12(\epsilon_0|\vec E|^2+\mu_0^{-1}|\vec B|^2),\qquad
  \vec S=\mu_0^{-1}\vec E\times\vec B.
  $$
- Momentum density and total momentum:
  $$
  \vec g=\frac{\vec S}{c^2},\qquad
  \vec P=\int_V \vec g\,d^3x.
  $$
- Stress tensor gives exact balance:
  $$
  \frac{\partial \vec g}{\partial t}+\nabla\cdot \mathbf T = 0
  \quad\Rightarrow\quad
  \frac{d\vec P}{dt}=-\int_{\partial V}\mathbf T\cdot d\vec A.
  $$

Newton/classical mechanics $\to$ emergence as center-of-energy kinematics
- From local energy conservation:
  $$
  \frac{\partial u}{\partial t}+\nabla\cdot \vec S=0,
  $$
  derive the exact identity for a bounded configuration with vanishing net flux:
  $$
  \vec P=\frac{U}{c^2}\frac{d\vec R}{dt},
  \qquad
  U=\int_V u\,d^3x,\qquad
  \vec R=\frac{1}{U}\int_V \vec r\,u\,d^3x.
  $$
- Sub-luminal motion is automatic via $c|\vec P|\le U$:
  $$
  \vec v:=\frac{d\vec R}{dt}=\frac{c^2\vec P}{U},\qquad |\vec v|\le c.
  $$
- Define inertial mass as enclosed field energy:
  $$
  m:=\frac{U}{c^2}.
  $$
- General momentum-balance (variable enclosed energy allowed):
  $$
  \vec F_{\rm ext}:=\frac{d\vec P}{dt}
  =\frac{1}{c^2}\frac{dU}{dt}\,\vec v + m\,\vec a,
  \qquad
  \vec a=\frac{d\vec v}{dt}.
  $$
- Newton’s $\,\vec F=m\vec a\,$ is the closed, self-sustained special case
  ($dU/dt=0$), i.e. no net power flux across $\partial V$.

Impedance $\to$ the boundary-coupling invariant left in Maxwell theory
- Vacuum impedance is fixed:
  $$
  Z_0=\sqrt{\frac{\mu_0}{\epsilon_0}}=\mu_0 c=\frac{1}{\epsilon_0 c}.
  $$
- A bounded configuration must have an intrinsic impedance $Z_{\rm knot}$
  determined by its geometry (waveguide/flux-tube structure).

Fine structure $\alpha$ $\to$ mismatch ratio between vacuum and intrinsic impedance
- Using $\alpha=e^2/(4\pi\epsilon_0\hbar c)$ and $Z_0=1/(\epsilon_0 c)$:
  $$
  \alpha=\frac{Z_0}{2R_K},
  \qquad
  R_K=\frac{h}{e^2}=\frac{Z_0}{2\alpha}.
  $$
- Maxwell-universe claim must therefore amount to:
  $$
  Z_{\rm knot}=R_K,
  \qquad\Rightarrow\qquad
  \alpha=\frac{Z_0}{2Z_{\rm knot}}.
  $$

Reflection/TIR analogy $\to$ boundary-condition interpretation (not extra physics)
- Large mismatch $Z_{\rm knot}\gg Z_0$ implies weak transmission to vacuum.
- The boundary behaves as a high-reflectivity interface for circulating energy,
  an impedance statement analogous to total internal reflection in optics.
