---
title: The Physics of Energy Flow – Interaction as Phase Accumulation
date: 2026-03-11
---


# 11a. Interaction as Phase Accumulation

Chapter 11 derived the free Schrödinger equation as the narrow-band envelope of
a stable Maxwell mode. Interaction enters when that envelope propagates through
a structured background.

In the envelope description, such a background appears as a local potential:

$$
i\hbar\,\partial_t\psi
=
\left(
-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r},t)
\right)\psi.
$$

$V$ is not a new substance or a new causal layer. It is a compact summary of
how the background changes the phase accumulated by the envelope during
propagation.

The propagator makes this explicit:

$$
K(x,T;x_0,0)
=
\int\mathcal Dq\;
\exp\!\left[
\frac{i}{\hbar}\int_0^T dt
\left(
\frac{1}{2}m\dot q^2 - V(q,t)
\right)
\right].
$$

All interaction enters through the action in the exponential. The background
does not destroy the wave. It rotates its phase.

This is especially clear in the double-slit case. If two spatial channels
experience different interaction backgrounds, represented by $V_1$ and $V_2$,
the physically relevant quantity is the action difference between them:

$$
\Delta\phi
=
\frac{1}{\hbar}\int_0^T dt\,(V_1-V_2).
$$

The total amplitude at the screen is then

$$
\psi(x)
=
\psi_1^{(0)}(x)
+
e^{i\Delta\phi}\psi_2^{(0)}(x),
$$

where $\psi_j^{(0)}$ is the reference amplitude for free or symmetric
propagation.

If $V_1 = V_2$, then $\Delta\phi = 0$ and the full interference pattern is
recovered. If the two backgrounds differ, the relative phase changes and the
pattern changes with it. What disappears is not wave character, but coherent
phase relation.

This closes the loop left open in chapter 11. The potential term in
Schrödinger's equation does not introduce a separate ontology. It summarizes
background interaction in the same wave-envelope dynamics.
