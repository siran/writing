---
title: The Physics of Energy Flow - Nested Transport and Hyperbolic Composition
date: 2026-03-13
---

# 202. Nested Transport and Hyperbolic Composition

The double-curl transport closure of chapter 7 should not be composed with itself
naively. Applying

$$
\nabla\times(\nabla\times\mathbf{F})
$$

again acts on field structure. It produces a higher spatial operator. It does
not by itself describe one transport riding on another.

Nested transport belongs to kinematics, not to repeated application of the
field operator. For a given approximately uniform region, let $k$ denote the
local transport speed singled out there by the electromagnetic closure. The
question is this: if one transport process is nested inside another, and both
are described within a region where the same local $k$ applies, what is the
resulting relation of composition?

To keep the discussion in one lab, consider motion along one spatial direction
$x$. Let $u$ denote the speed produced from rest by one standard transport
pulse in that region. If a body is already moving at speed $v$, let

$$
v \oplus u
$$

denote the speed measured in the same lab after applying that same standard
pulse again.

The composition operation $\oplus$ should satisfy four basic requirements:

- identity: $v\oplus 0 = v$ and $0\oplus u = u$
- associativity: successive standard pulses can be grouped arbitrarily
- oddness: reversing both directions reverses the result
- boundedness: if $|v|<k$ and $|u|<k$, then $|v\oplus u|<k$

For any smooth one-dimensional associative composition law, there exists a
monotone parameter $\eta=\phi(v)$ that turns composition into addition:

$$
\phi(v\oplus u)=\phi(v)+\phi(u).
$$

Because the admissible speeds are bounded by $\pm k$, this additive parameter
must diverge as $v\to\pm k$. A convenient odd smooth choice, normalized at the
origin, is

$$
\eta=\phi(v)=\operatorname{artanh}\!\left(\frac{v}{k}\right).
$$

So

$$
v = k\tanh\eta.
$$

This is the hyperbolic parametrization of speed. Successive identical pulses do
not add linearly in $v$. They add linearly in $\eta$.

If one pulse contributes $\eta_0$, then after $n$ identical pulses the lab
speed is

$$
v_n = k\tanh(n\eta_0).
$$

More generally, if

$$
v_1 = k\tanh\eta_1,
\qquad
v_2 = k\tanh\eta_2,
$$

then

$$
v_1\oplus v_2
=
k\tanh(\eta_1+\eta_2)
=
\frac{v_1+v_2}{1+v_1v_2/k^2}.
$$

This is the hyperbolic composition relation.

The same result can be written in the more compressed coordinate language. In
the same approximately uniform region, the local transport speed $k$ picks out
the lines

$$
x = \pm kt,
$$

which bound the local transport cone. Writing the null coordinates

$$
u = t + \frac{x}{k}, \qquad w = t - \frac{x}{k},
$$

any linear map preserving those directions takes the form

$$
u' = \lambda u, \qquad w' = \lambda^{-1} w.
$$

Writing $\lambda=e^{-\eta}$ recovers the same additive parameter $\eta$ and
therefore the same hyperbolic composition rule above.

So the distinction is exact:

- double curl organizes source-free transport locally
- repeated double curl changes field structure
- nested transport composes successive transport increments that preserve the
  same local bound $k$
- preserving that cone forces hyperbolic composition

The train-and-passenger image is therefore valid, but only at the kinematic
level. One transport process may be nested inside another. The resulting
composition is hyperbolic because the same local transport speed $k$ is
preserved at each step.
