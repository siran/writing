---
title: Light Speed as an Emergent Property of Electromagnetic Superposition
subtitle: "Polarization Without Matter: A Field-Only Interpretation of Refraction"
author: An M. Rodriguez
date: 2026-01-10 13:20
keywords: Maxwell theory, electromagnetic superposition, polarization, linear response, refraction, phase delay, energy density, effective refractive index, variable light speed, field ontology
one-sentence-summary: Light slows because electromagnetic waves interfere with phase-delayed secondary electromagnetic fields, making the effective speed of light an emergent, local property of electromagnetic superposition rather than a universal constant.
summary: Polarization is treated as a secondary electromagnetic field rather than a property of matter. Within linear Maxwell theory and linear response, overlapping electromagnetic waves generate phase-delayed secondary fields whose superposition alters phase evolution and yields an effective refractive index. Electromagnetic waves therefore interact through the total field configuration they jointly create, and the effective local speed of light depends on the electromagnetic energy density of the environment. Refraction emerges as a consequence of field superposition and delayed response, without invoking particles, atoms, or nonlinear modifications of Maxwell’s equations.
doi: https://writing.preferredframe.com/doi/10.5281/zenodo.18209801/
---

## Summary

Electromagnetic waves interact through the total field they jointly create.
Polarization is an electromagnetic field, not a material property. Phase-delayed
secondary fields modify phase evolution. An effective, local light speed emerges
from the electromagnetic energy density itself, as fields interfere pointwise.


### Goal

Explain, mathematically and with an explicit ontological justification, how
linear Maxwell theory allows electromagnetic waves to superpose and interact
through the total field, and how an effective local propagation speed can arise
from that total-field interaction.


### Corollary

The maximum propagation speed of electromagnetic disturbances is
$c_0$, with

$$
c_0 = \frac{1}{\sqrt{\mu_0 \epsilon_0}}.
$$

However, $c_0$ need not take the same effective value everywhere in
the universe. When electromagnetic waves propagate in a linear, nontrivial
electromagnetic environment, the total field gives rise to an effective
susceptibility $\chi(\mathbf{x})$.

The effective local propagation speed is then

$$
c_{\text{local}}(\mathbf{x}) = \frac{c_0}{\sqrt{1+\chi(\mathbf{x})}},
$$

and therefore depends on the local electromagnetic energy density through the
induced effective $\chi$.

As a result, the effective speed of light varies from place to place, tracking
spatial variations in electromagnetic field energy density across the universe.


## Derivation

### 1. Maxwell theory and superposition

In source-free regions, Maxwell’s equations are

$$
\nabla\cdot\mathbf{E}=0,\qquad \nabla\cdot\mathbf{B}=0,
$$

$$
\nabla\times\mathbf{E}=-\partial_t\mathbf{B},\qquad
\nabla\times\mathbf{B}=\mu_0\epsilon_0\,\partial_t\mathbf{E}.
$$

These equations are linear: if $(\mathbf{E}_1,\mathbf{B}_1)$ and
$(\mathbf{E}_2,\mathbf{B}_2)$ are solutions, then their sum is also a solution.

Linearity applies to the field equations themselves and does not constrain how
physical observables are constructed from the fields.


### 2. Quadratic field observables

The electromagnetic energy density is

$$
u=\frac{\epsilon_0}{2}\left(\mathbf{E}^2+c^2\mathbf{B}^2\right).
$$

For a superposed field $\mathbf{E}=\mathbf{E}_1+\mathbf{E}_2$,

$$
u=u_1+u_2+u_{12},
$$

with

$$
u_{12}=\epsilon_0\left(\mathbf{E}_1\cdot\mathbf{E}_2+c^2\mathbf{B}_1\cdot\mathbf{B}_2\right).
$$

Thus, overlapping waves produce cross terms in energy density and momentum flow.
This constitutes a physical interaction at the level of observables.


### 3. Polarization written purely as fields

In macroscopic electrodynamics,

$$
\mathbf{D}=\epsilon_0\mathbf{E}+\mathbf{P},
$$

with linear response

$$
\mathbf{P}=\epsilon_0\chi\,\mathbf{E}.
$$

Maxwell’s equations do not specify the origin of $\mathbf{P}$. Formally,
$\mathbf{P}$ is an additional electromagnetic field proportional to
$\mathbf{E}$.

Interpreted this way:
- $\mathbf{P}$ is a secondary electromagnetic field.
- The relation $\mathbf{P}=\epsilon_0\chi\mathbf{E}$ is a linear field–field
  coupling.
- No ontological distinction between “matter” and “electromagnetic field” is
  required.


### 4. Phase delay and effective propagation

In realistic linear response, proportionality is causal:

$$
\mathbf{P}(t)=\epsilon_0\int_{-\infty}^{t}\chi(t-t')\,\mathbf{E}(t')\,dt'.
$$

In frequency space,

$$
\mathbf{P}(\omega)=\epsilon_0\chi(\omega)\mathbf{E}(\omega).
$$

The secondary field associated with $\mathbf{P}$ is phase-delayed relative
to the primary field. The total field is the superposition of the incident
electromagnetic wave and the delayed secondary electromagnetic wave, producing a
shifted phase evolution.


### 5. Emergence of an effective refractive index

With

$$
\mathbf{D}=\epsilon(\omega)\mathbf{E},\qquad
\epsilon(\omega)=\epsilon_0\left[1+\chi(\omega)\right],
$$

Maxwell’s equations yield the wave equation

$$
\nabla^2\mathbf{E}-\mu_0\epsilon(\omega)\partial_t^2\mathbf{E}=0.
$$

Plane-wave solutions satisfy

$$
k^2=\mu_0\epsilon(\omega)\omega^2,
$$

so the phase velocity is

$$
v_p(\omega)=\frac{1}{\sqrt{\mu_0\epsilon(\omega)}}=\frac{c_0}{n(\omega)},\qquad
n(\omega)=\sqrt{1+\chi(\omega)}.
$$

The reduction in propagation speed follows directly from interference with a
phase-delayed secondary electromagnetic field.


### 6. Two-wave interaction

Let

$$
\mathbf{E}=\mathbf{E}_1+\mathbf{E}_2.
$$

By linearity,

$$
\mathbf{P}=\epsilon_0\chi(\mathbf{E}_1+\mathbf{E}_2)
          =\epsilon_0\chi\mathbf{E}_1+\epsilon_0\chi\mathbf{E}_2.
$$

Each wave generates a secondary electromagnetic field, and both contribute to
the total response. Each wave therefore propagates in an environment determined
by the combined electromagnetic configuration.


### 7. Local effective light speed

The local electromagnetic energy density is

$$
u(\mathbf{x})=\frac{\epsilon_0}{2}\left(\langle\mathbf{E}^2\rangle+c^2\langle\mathbf{B}^2\rangle\right).
$$

The effective refractive index is

$$
n(\mathbf{x})=\sqrt{1+\chi(\mathbf{x})},
$$

and the local propagation speed is

$$
c_{\text{local}}(\mathbf{x})=\frac{c_0}{n(\mathbf{x})}.
$$


### 8. Consequence

Different regions of the universe, characterized by different electromagnetic
field configurations and energy densities, exhibit different effective
propagation speeds. Maxwell’s equations remain unchanged. The result follows
solely from superposition, linear response, and a field-only interpretation of
polarization.

---

DOI: https://writing.preferredframe.com/doi/10.5281/zenodo.18209801/
