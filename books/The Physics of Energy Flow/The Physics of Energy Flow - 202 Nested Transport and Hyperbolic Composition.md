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
field operator. The question is this: if one transport process is nested inside
another, and both respect the same invariant transport speed $k$, what is the
resulting law of composition?

For clarity, consider one spatial direction $x$. The invariant transport speed
$k$ means that the distinguished transport lines are

$$
x = \pm kt.
$$

These are the boundaries of the transport cone. Any admissible change of frame
must preserve them.

Assume two frames are related by uniform relative motion along $x$. Because the
transport background is homogeneous, the change of coordinates must be linear.
Instead of $(t,x)$, write the null coordinates

$$
u = t + \frac{x}{k}, \qquad w = t - \frac{x}{k}.
$$

Then the transport lines are simply

$$
u = 0 \qquad\text{or}\qquad w = 0.
$$

Preserving the transport cone means preserving these null directions. So the
most general admissible linear transformation is

$$
u' = \lambda u, \qquad w' = \lambda^{-1} w,
$$

for some positive constant $\lambda$.

Returning to $(t,x)$ coordinates gives

$$
t' = \frac{u'+w'}{2}
=
\frac{\lambda+\lambda^{-1}}{2}\,t
+ \frac{\lambda-\lambda^{-1}}{2k}\,x,
$$

and

$$
x' = \frac{k(u'-w')}{2}
=
\frac{k(\lambda-\lambda^{-1})}{2}\,t
+ \frac{\lambda+\lambda^{-1}}{2}\,x.
$$

Now choose the sign convention so that the primed origin moves with speed $v$
in the unprimed frame. Writing

$$
\lambda = e^{-\eta},
$$

we have

$$
\frac{\lambda+\lambda^{-1}}{2} = \cosh \eta, \qquad
\frac{\lambda-\lambda^{-1}}{2} = -\sinh \eta.
$$

Therefore

$$
t' = \cosh\eta\,t - \frac{\sinh\eta}{k}\,x,
$$

$$
x' = -k\sinh\eta\,t + \cosh\eta\,x.
$$

If $x'=0$, then the primed origin satisfies

$$
x = k\tanh\eta \, t.
$$

So the relative speed is

$$
v = k\tanh\eta.
$$

This is the hyperbolic parametrization of velocity.

Now compose two such frame changes, with parameters $\eta_1$ and $\eta_2$. In
null coordinates,

$$
u'' = e^{-\eta_2}u' = e^{-(\eta_1+\eta_2)}u,
$$

$$
w'' = e^{\eta_2}w' = e^{\eta_1+\eta_2}w.
$$

So the parameters add:

$$
\eta_{\mathrm{tot}} = \eta_1 + \eta_2.
$$

Since

$$
v = k\tanh\eta,
$$

the composed speed is

$$
v_{\mathrm{tot}}
=
k\tanh(\eta_1+\eta_2)
=
\frac{v_1+v_2}{1+v_1v_2/k^2}.
$$

This is the hyperbolic composition law.

So the distinction is exact:

- double curl organizes source-free transport locally
- repeated double curl changes field structure
- nested transport composes moving frames that preserve the same transport cone
- preserving that cone forces hyperbolic composition

The train-and-passenger image is therefore valid, but only at the kinematic
level. One transport process may be nested inside another. The resulting
composition is hyperbolic because the same invariant transport speed $k$ is
preserved at each level.
