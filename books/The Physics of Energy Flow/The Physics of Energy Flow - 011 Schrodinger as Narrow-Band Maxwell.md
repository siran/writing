---
title: The Physics of Energy Flow - Schrodinger as Narrow-Band Maxwell
date: 2026-03-11
---


# 11. Schrodinger as Narrow-Band Maxwell

The Schrodinger equation appears here as a controlled envelope limit of
double-curl or Maxwellian transport. Chapters 8 and 9 already gave two things
needed for that
limit: discrete stable modes and an emergent mass scale. The remaining task is
to describe slow modulation of one such mode.

Each Cartesian component $f(\mathbf{r},t)$ of $\mathbf{E}$ or $\mathbf{B}$
satisfies the vacuum wave equation:

$$
\left(\nabla^2-\frac{1}{c^2}\partial_t^2\right)f=0.
$$

Select the positive-frequency part of the field near a stable carrier frequency
$\omega_0$, and demodulate the carrier:

$$
\psi(\mathbf{r},t)=e^{i\omega_0 t}f^{(+)}(\mathbf{r},t).
$$

The field is narrow-band when

$$
\varepsilon = \frac{\Delta\omega}{\omega_0}\ll 1,
$$

so the envelope $\psi$ varies slowly compared with the carrier. After
separating the carrier and the base-mode contribution, and using the fact that
the carrier already satisfies the dispersion relation of the underlying stable
mode, the exact envelope identity is

$$
i\partial_t\psi
=
-\frac{c^2}{2\omega_0}\nabla^2\psi
+\frac{1}{2\omega_0 c^2}\partial_t^2\psi.
$$

The last term is the difference between exact Maxwellian transport and the
Schrodinger limit. For spectral width $\Delta\omega$, it is controlled by

$$
\left\|\frac{1}{2\omega_0 c^2}\partial_t^2\psi\right\|
\le
\frac{\Delta\omega^2}{2\omega_0 c^2}\|\psi\|
=
O(\varepsilon^2)\|\psi\|.
$$

So, to leading order in the narrow-band parameter,

$$
i\partial_t\psi
=
-\frac{c^2}{2\omega_0}\nabla^2\psi
+O(\varepsilon^2).
$$

Now define the emergent constants from the carrier mode itself:

$$
\hbar=\frac{E_0}{\omega_0},\qquad
m=\frac{E_0}{c^2},
$$

where $E_0$ is the rest energy of the underlying stable mode. Then

$$
\frac{c^2}{2\omega_0}=\frac{\hbar}{2m}.
$$

Multiplying by $\hbar$ gives

$$
i\hbar\,\partial_t\psi
=
-\frac{\hbar^2}{2m}\nabla^2\psi
+O(\varepsilon^2).
$$

This is the free Schrodinger equation. It arises as the narrow-band envelope
equation of a stable Maxwell mode.

The interaction case uses the same ontology. In structured backgrounds, the
envelope accumulates additional region-dependent phase. The double-slit
treatment later represents such interaction regions by localized potentials
$V_j$ that rotate the relative phase of the propagation channels. The
potential term is therefore a summary of background interaction in the same
envelope dynamics. This chapter, however, derives only the free narrow-band
case.

Superposition, interference, and uncertainty enter because the envelope remains
a wave field. Quantum mechanics is the effective theory of slowly varying
Maxwell envelopes.
