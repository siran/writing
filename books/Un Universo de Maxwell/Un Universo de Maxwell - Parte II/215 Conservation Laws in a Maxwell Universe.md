## Conservation Laws in a Maxwell Universe

In a Maxwell Universe, the electromagnetic field is the only fundamental entity.
There are no particles, no intrinsic masses, and no independent mechanical
postulates. All physical objects are structured, self-confined electromagnetic
field configurations evolving according to the source-free Maxwell equations,

$$
\nabla\cdot\vec{E}=0,\qquad
\nabla\cdot\vec{B}=0,\qquad
\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t},\qquad
\nabla\times\vec{B}=\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}.
$$

These four equations supply the entire dynamics. What we call “matter” is nothing
more than a persistent solution of these equations.

---


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

---


### Why Momentum Is Conserved

The conservation of momentum follows directly from Maxwell dynamics.
Differentiating the momentum density and using Maxwell’s equations yields the
local balance law

$$
\frac{\partial\vec{g}}{\partial t}+\nabla\cdot\mathbf{T}=0,
$$

where $\mathbf{T}$ is the Maxwell stress tensor,

$$
T_{ij}=\epsilon_0\!\left(E_iE_j+c^2B_iB_j
-\tfrac12\delta_{ij}(|\vec{E}|^2+c^2|\vec{B}|^2)\right).
$$

Integrating over a volume $V$ gives

$$
\frac{d\vec{P}}{dt}
=-\!\int_{\partial V}\mathbf{T}\cdot d\vec{A}.
$$

Momentum changes only when electromagnetic stress crosses the boundary. For a
self-confined configuration whose external fields cancel on $\partial V$, the
surface integral vanishes and $\vec{P}$ remains constant.

Momentum conservation is therefore not a postulate, but a consequence of
source-free Maxwell dynamics.

---


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
\vec{P}=U\,\frac{d\vec{R}}{dt}.
$$

If $\vec{P}$ is constant, then $d\vec{R}/dt$ is constant. A localized
electromagnetic configuration therefore moves at uniform velocity unless acted
upon by external electromagnetic stress.

This is inertia.

---


### Angular Momentum and Rotation

Electromagnetic fields also carry angular momentum. The angular-momentum density
is

$$
\vec{\ell}=\vec{r}\times\vec{g},
$$

and the total angular momentum is

$$
\vec{L}=\int_V \vec{r}\times(\epsilon_0\,\vec{E}\times\vec{B})\,d^3x.
$$

Its evolution obeys

$$
\frac{d\vec{L}}{dt}
=-\!\int_{\partial V}\vec{r}\times(\mathbf{T}\cdot d\vec{A}).
$$

Angular momentum is conserved whenever no torque crosses the boundary. A
self-confined electromagnetic configuration with internal circulation will
rotate indefinitely unless acted upon by an external stress.

Rotational inertia is the persistence of circulating field momentum.

---


### What a “Force” Is

In a Maxwell Universe, a force is not primitive. A push is simply an external
electromagnetic field overlapping a localized configuration. During the overlap,

$$
\vec{E}_{\text{tot}}=\vec{E}+\vec{E}_{\text{ext}},\qquad
\vec{B}_{\text{tot}}=\vec{B}+\vec{B}_{\text{ext}},
$$

and the momentum density becomes

$$
\vec{g}_{\text{tot}}=\epsilon_0\,\vec{E}_{\text{tot}}\times\vec{B}_{\text{tot}}.
$$

Momentum is redistributed through electromagnetic stress. After the interaction
ends, the configuration relaxes into a new steady state with a different total
momentum.

---


### Emergence of Newton’s Second Law

Define an effective inertial measure,

$$
m_{\text{eff}}=\frac{U}{c^2}.
$$

Since $\vec{P}=U\,\vec{v}$ with $\vec{v}=d\vec{R}/dt$, we have

$$
\vec{P}=m_{\text{eff}}\vec{v}.
$$

Differentiating and identifying stress-tensor flux as the external influence
yields

$$
\vec{F}_{\text{ext}}=m_{\text{eff}}\vec{a}.
$$

Newton’s second law is not fundamental. It is an identity expressing how
electromagnetic stress changes field momentum.

---


### What This Means

All classical mechanical behavior—translation, rotation, inertia, and
conservation laws—emerges directly from source-free Maxwell dynamics. No
particles, intrinsic masses, or auxiliary axioms are required.

In a Maxwell Universe, mechanics is not imposed on matter.
Mechanics is the natural behavior of structured electromagnetic fields.
