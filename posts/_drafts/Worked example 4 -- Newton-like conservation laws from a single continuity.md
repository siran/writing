## Worked example 4: Newton-like conservation laws from a single continuity equation, for a localized self-sustaining energy knot

This example is deliberately concrete.

We assume only:

1. A nonnegative energy density $u(\mathbf{x},t)\ge 0$.
2. A local energy-flux vector field $\mathbf{S}(\mathbf{x},t)$.
3. A single continuity equation (energy bookkeeping under continuous transport):


$$
\partial_t u + \nabla\cdot \mathbf{S}=0.
$$

We do *not* assume Newton’s laws. We do *not* assume momentum conservation as an
axiom. We do *not* assume “force” as a primitive.

We show how the *form* of Newtonian-looking statements emerges as identities
once:

- you define a localized object as a region of concentrated energy,
- you track the motion of that region using its center-of-energy,
- and you interpret changes as flux across its boundary.


The key idea is: “laws of motion” are accounting identities for localized
conserved flow.

---


# 1. Localized object definition: an energy knot as a moving concentration

Let $V$ be a (possibly time-dependent) region enclosing a localized
concentration of energy (“knot”).

Define its total energy:

$$
E_V(t) := \int_V u(\mathbf{x},t)\,d^3x.
$$

To talk about “where it is,” define its center-of-energy:

$$
\mathbf{X}(t) := \frac{1}{E_V(t)}\int_V \mathbf{x}\,u(\mathbf{x},t)\,d^3x.
$$

This is purely definitional. It introduces no mechanics.

---


# 2. Energy change is boundary flux

Differentiate $E_V(t)$ in time.

If $V$ is fixed in space (for now):

$$
\frac{dE_V}{dt}=\int_V \partial_t u\,d^3x.
$$

Use continuity:

$$
\frac{dE_V}{dt}=-\int_V \nabla\cdot\mathbf{S}\,d^3x.
$$

Apply divergence theorem:

$$
\frac{dE_V}{dt}=-\oint_{\partial V}\mathbf{S}\cdot d\mathbf{A}.
$$

So: energy of the object changes only by energy crossing its boundary.

This is the first “conservation law” and it is not assumed beyond the single
continuity equation.

---


# 3. Velocity of the center-of-energy from continuity

Differentiate the numerator of $\mathbf{X}(t)$:

$$
\frac{d}{dt}\int_V \mathbf{x}\,u\,d^3x
=
\int_V \mathbf{x}\,\partial_t u\,d^3x
=
-\int_V \mathbf{x}\,\nabla\cdot\mathbf{S}\,d^3x.
$$

Now use the identity (componentwise):

$$
x_i\,\partial_j S_j = \partial_j(x_i S_j) - S_i.
$$

Integrate over $V$:

$$
-\int_V x_i\,\partial_j S_j\,d^3x
=
-\int_V \partial_j(x_i S_j)\,d^3x + \int_V S_i\,d^3x
=
-\oint_{\partial V} x_i\,\mathbf{S}\cdot d\mathbf{A} + \int_V S_i\,d^3x.
$$

Thus, in vector form:

$$
\frac{d}{dt}\int_V \mathbf{x}\,u\,d^3x
=
\int_V \mathbf{S}\,d^3x
-
\oint_{\partial V} \mathbf{x}\,(\mathbf{S}\cdot d\mathbf{A}).
$$

Now expand:

$$
\frac{d}{dt}\left(E_V \mathbf{X}\right)
=
\int_V \mathbf{S}\,d^3x
-
\oint_{\partial V} \mathbf{x}\,(\mathbf{S}\cdot d\mathbf{A}).
$$

Use product rule:

$$
E_V \dot{\mathbf{X}} + \dot{E}_V\,\mathbf{X}
=
\int_V \mathbf{S}\,d^3x
-
\oint_{\partial V} \mathbf{x}\,(\mathbf{S}\cdot d\mathbf{A}).
$$

Substitute $\dot{E}_V = -\oint_{\partial V}\mathbf{S}\cdot d\mathbf{A}$:

$$
E_V \dot{\mathbf{X}}
=
\int_V \mathbf{S}\,d^3x
-
\oint_{\partial V} (\mathbf{x}-\mathbf{X})\,(\mathbf{S}\cdot d\mathbf{A}).
$$

This is an exact identity derived from continuity alone.

Interpretation:

- $\int_V \mathbf{S}\,d^3x$ is the bulk transport tendency of energy within
  $V$.
- The boundary term corrects for energy leaking in/out at different positions
  relative to $\mathbf{X}$.


Now take the “closed object” regime:

Assume the knot is self-sustaining and well-separated so that there is
negligible net flux through $\partial V$:

$$
\oint_{\partial V}\mathbf{S}\cdot d\mathbf{A}\approx 0,
\qquad
\oint_{\partial V} (\mathbf{x}-\mathbf{X})(\mathbf{S}\cdot d\mathbf{A})\approx 0.
$$

Then the identity reduces to:

$$
E_V \dot{\mathbf{X}} \approx \int_V \mathbf{S}\,d^3x.
$$

So the center-of-energy velocity is:

$$
\dot{\mathbf{X}} \approx \frac{1}{E_V}\int_V \mathbf{S}\,d^3x.
$$

This is the Newtonian-looking statement “velocity is total flux divided by total
content,” but it is an identity from continuity plus localization.

No “inertia postulate” occurred.

---


# 4. Momentum as a derived bookkeeping variable

Define a derived “momentum-like” quantity:

$$
\mathbf{P}(t) := \frac{1}{c^2}\int_V \mathbf{S}\,d^3x.
$$

This is motivated by Maxwell kinematics (when applicable), but here it can be
taken as a definition: a rescaled integrated energy flux.

Combine with the previous relation:

$$
\dot{\mathbf{X}} \approx \frac{c^2}{E_V}\mathbf{P}.
$$

If the knot has approximately constant total energy $E_V\approx E$, define an
effective mass:

$$
m := \frac{E}{c^2}.
$$

Then:

$$
\mathbf{P} \approx m\,\dot{\mathbf{X}}.
$$

This is “$p=mv$” as an emergent relation: it is a definition of
$m$ from energy, plus the continuity-derived expression for
$\dot{\mathbf{X}}$.

Nothing mechanical has been assumed.

---


# 5. Acceleration arises from *flux exchange* across the boundary

Now differentiate $\mathbf{P}$:

$$
\dot{\mathbf{P}}=\frac{1}{c^2}\frac{d}{dt}\int_V \mathbf{S}\,d^3x
=
\frac{1}{c^2}\int_V \partial_t \mathbf{S}\,d^3x,
$$

if $V$ is fixed. (If $V$ moves with the knot, add the
standard Reynolds transport terms; the conclusion is the same: boundary flux
terms appear.)

At this stage, continuity alone does not tell you $\partial_t \mathbf{S}$. So
how do we proceed without “adding mechanics”?

The program’s move is:

- identify that *any* change of the knot’s net transport must come from exchange
  with the outside through its boundary,
- and therefore define “force” as the boundary flux of transport content.


To do this cleanly, introduce a symmetric second-rank flux object
$\mathbf{T}$ such that

$$
\partial_t\left(\frac{\mathbf{S}}{c^2}\right)+\nabla\cdot \mathbf{T}=0
$$

inside regions where there is no external exchange.

This is not a new postulate if you are in Maxwell theory: $\mathbf{T}$ is
the Maxwell stress tensor and the identity is a theorem. But even in a
continuity-first setting, the structural point is:

- if a conserved density exists, it has an associated flux.
- energy has density $u$ and flux $\mathbf{S}$.
- transport-content $\mathbf{S}/c^2$ plays the role of another density and
  therefore has a flux $\mathbf{T}$.


Assuming such a local balance law holds for the transport-content inside the
closed region, integrate:

$$
\frac{d}{dt}\int_V \frac{\mathbf{S}}{c^2}\,d^3x
=
-\int_V \nabla\cdot\mathbf{T}\,d^3x
=
-\oint_{\partial V}\mathbf{T}\cdot d\mathbf{A}.
$$

Thus:

$$
\dot{\mathbf{P}} = -\oint_{\partial V}\mathbf{T}\cdot d\mathbf{A}.
$$

Define the right-hand side as the net external action on the knot:

$$
\mathbf{F}_{\mathrm{ext}} := -\oint_{\partial V}\mathbf{T}\cdot d\mathbf{A}.
$$

Then we have:

$$
\dot{\mathbf{P}} = \mathbf{F}_{\mathrm{ext}}.
$$

This is Newton’s “second law” in its most honest form:

- it is not a postulate about forces,
- it is a definition of force as boundary flux of transport-content,
- and it becomes a theorem once $\mathbf{T}$ is specified (in Maxwell, it
  is).


If additionally $\mathbf{P}\approx m\dot{\mathbf{X}}$ and $m$ is
constant, then:

$$
m\,\ddot{\mathbf{X}} = \mathbf{F}_{\mathrm{ext}}.
$$

So “$F=ma$” is a derived identity: acceleration is caused by net
boundary flux of stress-like transport.

---


# 6. Newton’s third law as action–reaction from flux continuity

Consider two disjoint localized knots in volumes $V_1$ and
$V_2$. Let $V=V_1\cup V_2$ enclose both.

If the combined region is closed (no net flux through its outer boundary), then:

$$
\dot{\mathbf{P}}_{\mathrm{total}} = 0.
$$

But

$$
\mathbf{P}_{\mathrm{total}} = \mathbf{P}_1+\mathbf{P}_2,
\qquad
\dot{\mathbf{P}}_1=\mathbf{F}_{2\to 1},\quad \dot{\mathbf{P}}_2=\mathbf{F}_{1\to 2}
$$

where each $\mathbf{F}$ is defined by the stress flux across the respective
boundaries.

Then

$$
0=\dot{\mathbf{P}}_1+\dot{\mathbf{P}}_2=\mathbf{F}_{2\to 1}+\mathbf{F}_{1\to 2}.
$$

So

$$
\mathbf{F}_{2\to 1}=-\mathbf{F}_{1\to 2}.
$$

This is Newton’s third law, obtained from:

- closure of the combined region,
- and the fact that changes can only be mediated by boundary exchanges.


No separate “third law axiom” is needed.

---


# 7. Newton’s first law as the closed-knot limit

If a knot is fully isolated so that the stress flux across its boundary
vanishes:

$$
\oint_{\partial V}\mathbf{T}\cdot d\mathbf{A}=0,
$$

then

$$
\dot{\mathbf{P}}=0.
$$

If $m$ is constant and $\mathbf{P}=m\dot{\mathbf{X}}$, then:

$$
\ddot{\mathbf{X}}=0.
$$

This is inertia as the no-exchange limit.

So “an object in motion stays in motion” is the statement:

- if no boundary exchange occurs, integrated transport-content stays constant.

---


# 8. What has and has not been assumed

### What was assumed

- The continuity equation for energy (observed continuous transport accounting).
- The existence of localized concentrations (knots) so one can define
  $E_V$ and $\mathbf{X}$.
- For the Newton 2/3 pieces: the existence of a flux $\mathbf{T}$ for the
  transport-content density $\mathbf{S}/c^2$.


### What was not assumed

- No primitive mass.
- No primitive momentum.
- No primitive force.
- No primitive Newton laws.


Mass, momentum, force appear as *derived bookkeeping constructs* for localized
continuous transport.


### Where Maxwell enters

If one now specializes to source-free Maxwell theory, then:

- $u$ and $\mathbf{S}$ are given by field expressions,
- $\mathbf{T}$ is the Maxwell stress tensor,
- and the balance law for $\mathbf{S}/c^2$ is a theorem of Maxwell equations.


So in a Maxwell universe, the above “Newton identities” are not just structural
possibilities; they become explicit field-theoretic consequences.

---


# 9. The core message of this worked example

Newton-like mechanics is not an independent layer.

For localized, self-sustaining concentrations of continuously transported
energy:

- “inertia” is the persistence of integrated flux content under zero boundary
  exchange,
- “force” is the net boundary flux of stress-like transport,
- “action–reaction” is closure of the combined region,
- “mass” is $E/c^2$ once local transport is tied to a maximal rate.


Everything is continuity plus localization plus boundary accounting.
