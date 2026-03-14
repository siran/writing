---
title: The Physics of Energy Flow – Newton as Flux Accounting
date: 2026-03-11
---


# 12. Newton as Flux Accounting

Newton's second law is the integrated continuity law for momentum in a nearly
stable localized electromagnetic configuration.

Chapter 7 identified the energy flow with the Maxwell realization

$$
\mathbf{S}=\frac{1}{\mu_0}\,\mathbf{E}\times\mathbf{B}.
$$

The same transport therefore carries momentum. The electromagnetic momentum
density is

$$
\mathbf{g}=\frac{\mathbf{S}}{c^2}
=
\epsilon_0\,\mathbf{E}\times\mathbf{B}.
$$

To track how momentum moves through a surface, we use the Maxwell stress tensor:

$$
T_{ij}
=
\epsilon_0\left(E_iE_j-\frac{1}{2}\delta_{ij}\mathbf{E}^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j-\frac{1}{2}\delta_{ij}\mathbf{B}^2\right).
$$

Differentiate $\mathbf{g}$ in time and substitute Maxwell's equations. The
first result is

$$
\partial_t\mathbf{g}
=
\frac{1}{\mu_0}(\nabla\times\mathbf{B})\times\mathbf{B}
-
\epsilon_0\,\mathbf{E}\times(\nabla\times\mathbf{E}).
$$

Using the standard vector identity for $(\nabla\times\mathbf{A})\times
\mathbf{A}$ and the source-free conditions $\nabla\cdot\mathbf{E}=0$,
$\nabla\cdot\mathbf{B}=0$, this rearranges into the exact local momentum
continuity law

$$
\partial_t g_i + \partial_j T_{ij} = 0,
$$

or, in vector form,

$$
\partial_t\mathbf{g}+\nabla\cdot\mathbf{T}=0.
$$

This is the momentum analogue of Poynting's theorem. Momentum does not appear or
disappear. It changes only by flux through the boundary of a region.

Integrate over a localized region $K$ containing a nearly stable bounded
configuration:

$$
\mathbf{P}_K=\int_K \mathbf{g}\,d^3x.
$$

Then

$$
\frac{d}{dt}\mathbf{P}_K
=
-\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

The right-hand side is what later language calls force. It is the net rate at
which momentum crosses the boundary.

To connect this with motion of the object as a whole, define the energy in the
region and its center of energy:

$$
E_K=\int_K u\,d^3x,
\qquad
\mathbf{X}_K=\frac{1}{E_K}\int_K \mathbf{x}\,u\,d^3x.
$$

When boundary leakage is small and the mode remains coherent,

$$
E_K\,\dot{\mathbf{X}}_K \approx \int_K \mathbf{S}\,d^3x,
\qquad
\mathbf{P}_K \approx \frac{E_K}{c^2}\dot{\mathbf{X}}_K.
$$

For such a bounded configuration, define the effective inertial mass

$$
m_K := \frac{E_K}{c^2}.
$$

If the energy of the localized configuration is roughly constant, then

$$
m_K\,\ddot{\mathbf{X}}_K
\approx
-\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

This is Newton's second law in its effective form for a stable bounded mode:

$$
\mathbf{F}=\frac{d\mathbf{P}}{dt}.
$$

It describes momentum bookkeeping for a bounded region of field.

A mediating force field inserted between supposedly independent substrates does
not rescue their independence. If interaction is real, a common structure is
already present, and force is only the accounting of that coupling.

Particles are localized regions. Forces are boundary integrals. Newton's second
law is momentum continuity applied to a stable electromagnetic knot.
