---
title: A Maxwell Universe – Mechanics and Self-Refraction
date: 2025-12-31 20:15
---


## From Spectral Structure to Mechanics

In the preceding chapter, we showed that discrete spectral structure—exemplified
by the Rydberg series—arises naturally when electromagnetic fields are confined
by global continuity conditions. Discreteness emerged not from particles,
forces, or quantization rules, but from topology: the requirement that a field
defined on a compact configuration match itself after completing closed cycles.

At that stage, the discussion concerned only internal structure: how energy
redistributes within a self-confined electromagnetic configuration. Yet a
question remains unavoidable. If such configurations are to be identified with
ordinary matter, how do they move? How do they carry momentum, resist
acceleration, and obey the conservation laws that govern everyday mechanics?

The answer cannot be imported from Newtonian axioms or particle models, because
neither exists in a Maxwell Universe. If mechanics is to arise at all, it must
arise from electromagnetic field dynamics alone.

The purpose of the present chapter is to show that it does—inevitably.


## Conservation Laws in a Maxwell Universe

In a Maxwell Universe, the electromagnetic field is the only fundamental entity.
There are no particles, no intrinsic masses, and no independent mechanical
postulates. All physical objects are structured, self-confined electromagnetic
field configurations evolving according to the source-free Maxwell equations:

$$
\nabla\cdot\vec{E}=0,\qquad \nabla\cdot\vec{B}=0,
$$

$$
\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t},
\qquad
\nabla\times\vec{B}=\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}.
$$

These four equations supply the entire dynamics. What we call “matter” is
nothing more than a persistent solution of these equations.


### Energy and Momentum Are Field Properties

Maxwell’s theory assigns energy and momentum directly to fields. The local
electromagnetic energy density is

$$
u=\tfrac12\bigl(\epsilon_0|\vec{E}|^2+\mu_0^{-1}|\vec{B}|^2\bigr),
$$

and the flow of this energy is given by the Poynting vector,

$$
\vec{S}=\mu_0^{-1}\,\vec{E}\times\vec{B}.
$$

Momentum is not an added concept; it is already present in the field. The
momentum density is

$$
\vec{g}=\frac{\vec{S}}{c^2}=\epsilon_0\,\vec{E}\times\vec{B}.
$$

For any localized electromagnetic configuration occupying a region $V$, the
total momentum is therefore

$$
\vec{P}=\int_V \vec{g}\,d^3x.
$$

No mass parameter has been introduced.


### Why Momentum Is Conserved

The conservation of momentum follows directly from Maxwell dynamics.
Differentiating the momentum density and using Maxwell’s equations yields the
local balance law

$$
\frac{\partial\vec{g}}{\partial t}+\nabla\cdot\mathbf{T}=0,
$$

where $\mathbf{T}$ is the Maxwell stress tensor. Integrating over a volume $V$
gives

$$
\frac{d\vec{P}}{dt} = -\!\int_{\partial V}\mathbf{T}\cdot d\vec{A}.
$$

Momentum changes only when electromagnetic stress crosses the boundary. For a
self-confined configuration whose external fields cancel on $\partial V$, the
surface integral vanishes and $\vec{P}$ remains constant.

Momentum conservation is therefore not a postulate, but a consequence of
source-free Maxwell dynamics.


### Inertia Without Mass

Define the total electromagnetic energy in $V$,

$$
U=\int_V u\,d^3x,
$$

and the center of energy,

$$
\vec{R}(t)=\frac{1}{U}\int_V \vec{r}\,u\,d^3x.
$$

Electromagnetic field theory gives the exact relation

$$
\vec{P}=\frac{U}{c^{2}}\,\frac{d\vec{R}}{dt}.
$$

If $\vec{P}$ is constant, then $d\vec{R}/dt$ is constant. A localized
electromagnetic configuration therefore moves at uniform velocity unless acted
upon by external electromagnetic stress.

This is inertia.


### Emergence of Newton’s Second Law

From local energy conservation,

$$
\frac{\partial u}{\partial t}+\nabla\cdot\vec{S}=0,
$$

we define the enclosed energy of the self-sustaining electromagnetic
configuration $U(t)$ and its energy centroid $\vec{R}(t)$.

Differentiating the numerator of the centroid definition:

$$
\frac{d}{dt}\int_V \vec{r}\,u\,d^3x
=\int_V \vec{r}\,\frac{\partial u}{\partial t}\,d^3x
=-\int_V \vec{r}\,\nabla\cdot\vec{S}\,d^3x.
$$

Using the vector identity
$\nabla\cdot(\vec{r}\,\vec{S})=\vec{S}+\vec{r}\,\nabla\cdot\vec{S}$, we rewrite
the integral and apply the divergence theorem:

$$
\frac{d}{dt}\int_V \vec{r}\,u\,d^3x
=\int_V \vec{S}\,d^3x-\oint_{\partial V} \vec{r}\,(\vec{S}\cdot d\vec{A}).
$$

For a self-confined configuration (no net energy flux across $\partial V$), the surface term vanishes. Using $\vec{P} = (1/c^2) \int \vec{S} d^3x$, we obtain:

$$
\frac{d}{dt}\int_V \vec{r}\,u\,d^3x=c^2\vec{P}.
$$

Finally, differentiating $\vec{R}$ gives the center-of-energy identity:

$$
\boxed{\;\vec{P}=\frac{U}{c^{2}}\,\frac{d\vec{R}}{dt}\;}
$$

Thus the translational velocity of the configuration is not an assumption but a ratio of conserved field integrals.

Define the inertial mass of the bounded configuration by

$$
m=\frac{U}{c^{2}}.
$$

Differentiating $\vec{P}$ yields the general momentum-balance law:

$$
\vec{F}_{\text{ext}} =\frac{d\vec{P}}{dt} =\frac{1}{c^{2}}\frac{dU}{dt}\,\vec{v} +m\,\vec{a}.
$$

For a closed, self-sustained configuration where $dU/dt=0$, the motion of the center of energy obeys identically:

$$
\vec{F}_{\text{ext}}=m\,\vec{a}.
$$

Inertia is therefore the persistence of field momentum. Mechanics is the natural behavior of structured electromagnetic fields.


## Self-Refraction and Electromagnetic Stability

In the preceding analysis, we treated a localized electromagnetic configuration
as a given. We must now explain why such a configuration can exist at all, given
the tendency of electromagnetic waves to disperse.

In a Maxwell Universe, there is no container and no material substrate. Any mechanism of confinement must arise from the field’s own dynamics. We call this mechanism **self-refraction**.


### Self-Generated Electromagnetic Environment

Refraction does not require matter; it requires a phase-delayed electromagnetic response. In a Maxwell Universe, this response arises from the field configuration itself.

A self-sustained electromagnetic structure continuously generates secondary electromagnetic fields through its internal dynamics. These secondary fields are phase-delayed relative to the primary energy flow. An electromagnetic wave propagating within such a configuration therefore propagates through an electromagnetic environment created by the configuration itself.

The configuration acts as its own effective medium.


### Self-Refraction

In a Maxwell Universe, refraction is expected to happen without matter; it requires relative phase structure within the electromagnetic field that redirects energy flow through interference.

No modification of Maxwell’s equations is required. The equations remain linear and source-free everywhere. The apparent bending of energy flow arises from interference between components of a single self-consistent Maxwell solution.

Writing the total field as a superposition
$\vec{E}=\sum \vec{E}_k$ and $\vec{B}=\sum \vec{B}_k$, the Poynting vector becomes:

$$
\vec{S} =\frac{1}{\mu_0}\sum_{k,\ell}\vec{E}_k\times\vec{B}_\ell .
$$

The cross terms encode the redistribution of electromagnetic energy and momentum
that continuously redirects propagation, producing closed circulation without
invoking nonlinearity or an external medium.


### Stability as Identity

A self-sustained electromagnetic configuration persists because its own fields generate the delayed response required to redirect subsequent propagation. The configuration exists not despite dispersion, but because dispersion is exactly balanced by self-refraction.

Matter, in this view, is not light trapped by an external medium.
Matter is electromagnetic energy whose own self-generated field structure continuously refracts it into closed, self-consistent circulation.
