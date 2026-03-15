---
title: The Physics of Energy Flow - Lorentz Force as Boundary Stress Transfer
date: 2026-03-14
---

# 209. Lorentz Force as Boundary Stress Transfer

This appendix derives the Lorentz-force form as a consequence of momentum
continuity for a localized charged mode interacting with a background field.

The point is not to introduce a primitive force law. The point is to show that
the familiar Lorentz expression is the compact form taken by boundary momentum
transfer when a bounded charged configuration is described at scales larger
than its internal closure.

## 209.1 Effective Source Description of a Localized Mode

Fundamentally, the book treats all transport as source-free and continuous.
But once a bounded charged mode is viewed from scales large compared to its
internal toroidal closure, it admits an effective source description.

Write the self-field of the localized mode as

$$
\mathbf{E}_{\mathrm{self}},
\qquad
\mathbf{B}_{\mathrm{self}},
$$

and let

$$
\rho(\mathbf{r},t),
\qquad
\mathbf{J}(\mathbf{r},t)
$$

denote the effective charge and current densities of that coarse description.
They satisfy

$$
\nabla\cdot\mathbf{E}_{\mathrm{self}}=\frac{\rho}{\varepsilon_0},
$$

$$
\nabla\times\mathbf{B}_{\mathrm{self}}-\frac{1}{c^2}\partial_t\mathbf{E}_{\mathrm{self}}
=
\mu_0\mathbf{J},
$$

and

$$
\partial_t\rho+\nabla\cdot\mathbf{J}=0.
$$

This is not a second ontology. It is the effective large-scale description of a
bounded source-free closure whose far field has already been identified with
charge.

## 209.2 Local Momentum Continuity with Effective Sources

Let the total field be

$$
\mathbf{E}=\mathbf{E}_{\mathrm{self}}+\mathbf{E}_{\mathrm{ext}},
\qquad
\mathbf{B}=\mathbf{B}_{\mathrm{self}}+\mathbf{B}_{\mathrm{ext}},
$$

where the external fields satisfy the source-free Maxwell equations in the
neighborhood of the mode.

As in chapter 12, define

$$
\mathbf{g}=\varepsilon_0\,\mathbf{E}\times\mathbf{B},
$$

and the Maxwell stress tensor

$$
T_{ij}
=
\varepsilon_0\left(E_iE_j-\frac{1}{2}\delta_{ij}\mathbf{E}^2\right)
+
\frac{1}{\mu_0}\left(B_iB_j-\frac{1}{2}\delta_{ij}\mathbf{B}^2\right).
$$

Differentiate $\mathbf{g}$:

$$
\partial_t\mathbf{g}
=
\varepsilon_0\,\partial_t\mathbf{E}\times\mathbf{B}
+
\varepsilon_0\,\mathbf{E}\times\partial_t\mathbf{B}.
$$

Use the effective-source Maxwell equations:

$$
\varepsilon_0\,\partial_t\mathbf{E}
=
\frac{1}{\mu_0}\nabla\times\mathbf{B}-\mathbf{J},
\qquad
\partial_t\mathbf{B}=-\nabla\times\mathbf{E}.
$$

Then

$$
\partial_t\mathbf{g}
=
\frac{1}{\mu_0}(\nabla\times\mathbf{B})\times\mathbf{B}
- \mathbf{J}\times\mathbf{B}
- \varepsilon_0\,\mathbf{E}\times(\nabla\times\mathbf{E}).
$$

Now use the same vector identities as in chapter 12, but keep the source term
$\nabla\cdot\mathbf{E}=\rho/\varepsilon_0$ instead of setting it to zero. The
field terms rearrange into the divergence of the Maxwell stress tensor. The
result is the exact local balance law

$$
\partial_t g_i + \partial_j T_{ij}
=
-\rho E_i-(\mathbf{J}\times\mathbf{B})_i.
$$

Equivalently,

$$
\partial_t\mathbf{g}+\nabla\cdot\mathbf{T}
=
-\bigl(\rho\mathbf{E}+\mathbf{J}\times\mathbf{B}\bigr).
$$

So the Lorentz force density is not inserted by hand. It is the negative of the
field momentum loss plus stress outflow.

## 209.3 Exact Integrated Force on a Localized Mode

Let $K$ be a region containing the localized charged mode. Integrating the
local balance law gives

$$
\frac{d}{dt}\int_K \mathbf{g}\,dV
+
\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA
=
-\int_K \bigl(\rho\mathbf{E}+\mathbf{J}\times\mathbf{B}\bigr)\,dV.
$$

Therefore the exact force exerted on the localized mode is

$$
\mathbf{F}_K
=
\int_K \bigl(\rho\mathbf{E}+\mathbf{J}\times\mathbf{B}\bigr)\,dV
=
-\frac{d}{dt}\int_K \mathbf{g}\,dV
-\int_{\partial K}\mathbf{T}\cdot\mathbf{n}\,dA.
$$

This is the exact integrated Lorentz-force expression. In the language of this
book, it says that force on a bounded charged mode is boundary stress transfer
together with the change of field momentum stored in the surrounding region.

## 209.4 Separation of Self and External Contributions

Now separate the total field into self and external parts.

Because the stress tensor is quadratic in the fields,

$$
\mathbf{T}
=
\mathbf{T}_{\mathrm{self}}
+
\mathbf{T}_{\mathrm{ext}}
+
\mathbf{T}_{\mathrm{cross}}.
$$

The external field alone is source-free in the neighborhood of the mode, so it
does not push on the mode by itself. The self-field describes internal
stresses of the mode. The net externally induced force is carried by the cross
terms, equivalently by evaluating the integrated Lorentz density against the
external field:

$$
\mathbf{F}^{\mathrm{ext}}_K
=
\int_K \bigl(\rho\mathbf{E}_{\mathrm{ext}}
+
\mathbf{J}\times\mathbf{B}_{\mathrm{ext}}\bigr)\,dV.
$$

This is exact at the level of the effective localized description.

## 209.5 Compact-Mode Limit

Assume now that the external fields vary only weakly across the support of the
localized mode. Let $\mathbf{X}(t)$ denote the center of the mode. Then

$$
\mathbf{E}_{\mathrm{ext}}(\mathbf{r},t)
=
\mathbf{E}_{\mathrm{ext}}(\mathbf{X},t)
+
O\!\left(\ell\,\nabla\mathbf{E}_{\mathrm{ext}}\right),
$$

and similarly for $\mathbf{B}_{\mathrm{ext}}$, where $\ell$ is the size of the
mode.

Substituting into the exact integrated force gives

$$
\mathbf{F}^{\mathrm{ext}}_K
=
\left(\int_K \rho\,dV\right)\mathbf{E}_{\mathrm{ext}}(\mathbf{X},t)
+
\left(\int_K \mathbf{J}\,dV\right)\times\mathbf{B}_{\mathrm{ext}}(\mathbf{X},t)
+
O(\ell\nabla\mathbf{E}_{\mathrm{ext}},\,\ell\nabla\mathbf{B}_{\mathrm{ext}}).
$$

Define the total charge

$$
q:=\int_K \rho\,dV.
$$

To evaluate the current integral, use charge continuity. Componentwise,

$$
\frac{d}{dt}\int_K x_i\rho\,dV
=
\int_K x_i\partial_t\rho\,dV
=
-\int_K x_i\partial_j J_j\,dV.
$$

Integrating by parts and using compact support of the mode gives

$$
\frac{d}{dt}\int_K x_i\rho\,dV
=
\int_K J_i\,dV.
$$

Define the center of charge

$$
\mathbf{X}_q
:=
\frac{1}{q}\int_K \mathbf{x}\,\rho\,dV.
$$

Then

$$
\int_K \mathbf{J}\,dV = q\,\dot{\mathbf{X}}_q.
$$

If the charged mode moves coherently so that its center of charge moves with
velocity

$$
\mathbf{v}:=\dot{\mathbf{X}}_q,
$$

then

$$
\mathbf{F}^{\mathrm{ext}}_K
=
q\,\mathbf{E}_{\mathrm{ext}}(\mathbf{X},t)
+
q\,\mathbf{v}\times\mathbf{B}_{\mathrm{ext}}(\mathbf{X},t)
+
O(\ell\nabla\mathbf{E}_{\mathrm{ext}},\,\ell\nabla\mathbf{B}_{\mathrm{ext}}).
$$

In the point-mode idealization, or in a truly uniform external field, the
correction terms vanish and we obtain exactly

$$
\mathbf{F}
=
q\bigl(\mathbf{E}+\mathbf{v}\times\mathbf{B}\bigr).
$$

This is the Lorentz force law.

## 209.6 Interpretation

Within this framework, the Lorentz law is not a primitive rule about particles
being pushed by fields.

It is the compact expression of a deeper statement:

- the mode is a bounded organized closure of the same energy substrate,
- its effective charge is the large-scale summary of that closure,
- the surrounding field transfers momentum through boundary stress,
- the familiar force expression is the integrated form of that transfer.

So the Lorentz force is not outside the continuity program. It is one of its
effective consequences.

## 209.7 Relation to Charge as Toroidal Flux

Chapter 10 identified charge with the signed through-hole flux class of a
toroidal mode. The present appendix uses the corresponding large-scale
effective source description of that same object.

So the logical order is:

1. the bounded mode is fundamentally source-free,
2. at large scales it is represented by effective $\rho$ and $\mathbf{J}$,
3. momentum continuity then yields the Lorentz force law.

This is why the derivation belongs here. It connects the topological charge
picture to the standard dynamical force formula without abandoning the monist
ontology.

## 209.8 Summary

The exact local momentum balance with effective sources is

$$
\partial_t\mathbf{g}+\nabla\cdot\mathbf{T}
=
-\bigl(\rho\mathbf{E}+\mathbf{J}\times\mathbf{B}\bigr).
$$

Integrating over a localized charged mode gives the exact force formula

$$
\mathbf{F}_K
=
\int_K \bigl(\rho\mathbf{E}+\mathbf{J}\times\mathbf{B}\bigr)\,dV.
$$

For a compact coherent mode in a slowly varying external field, this reduces to

$$
\mathbf{F}
=
q\bigl(\mathbf{E}+\mathbf{v}\times\mathbf{B}\bigr).
$$

Thus the Lorentz-force form is derived here as boundary stress transfer and
field-momentum bookkeeping for a localized charged closure.
