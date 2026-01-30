## Worked example: a thin toroidal flux tube with explicit $T$, $\mu$, and a discrete mode spectrum

This example is deliberately minimal.

It does not attempt to solve the full Maxwell initial-value problem for a
self-trapped toroidal knot (that belongs to the explicit-solution documents).
Instead it shows, with explicit computations, how the program’s derived
quantities are extracted from a localized field configuration once such a
configuration exists.

The goal is to compute, step by step:

- the tension (line energy density) $T$,
- the inertial line density $\mu$,
- and the discrete spectrum of small excitations on a closed loop.

Nothing is postulated beyond:
- source-free Maxwell kinematics in vacuum,
- thin-tube localization,
- and periodicity around the loop.


### Geometry of the tube

Let the tube be centered on a circle of major radius $R$ in the
plane $z=0$.

Parameterize the centerline by arclength $s$:

$$
s\in[0,L],\qquad L=2\pi R,
$$

with unit tangent $\hat{\mathbf{t}}(s)$ along the loop.

At each $s$, define a cross-section $\Sigma_s$ orthogonal to
$\hat{\mathbf{t}}(s)$ with local polar coordinates $(\rho,\alpha)$, where
$\rho$ is the distance from the centerline within the cross-section.

Assume thin-tube localization:

$$
a \ll R,
$$

where $a$ is the characteristic tube radius.


### A concrete localized energy density profile

Assume the electromagnetic energy density is concentrated near the centerline
with a Gaussian radial profile:

$$
u(\rho) = u_0\,e^{-\rho^2/a^2}.
$$

Here $u_0$ is the peak energy density on the centerline.

This is not a Maxwell solution by itself. It is an ansatz for a localized energy
profile. The extraction of $T$ and $\mu$ from
$u$ is purely geometric and uses only the derived continuity
structure.

---


## Tension $T$ (energy per unit length)

By definition, the line energy density (tension) is the cross-sectional integral

$$
T = \int_{\Sigma_s} u\,dA.
$$

In polar coordinates on the cross-section:

$$
dA=\rho\,d\rho\,d\alpha,
\qquad
\rho\in[0,\infty),\ \alpha\in[0,2\pi).
$$

Compute:

$$
T
=
\int_0^{2\pi}\int_0^\infty u_0 e^{-\rho^2/a^2}\,\rho\,d\rho\,d\alpha.
$$

First integrate over $\alpha$:

$$
T
=
2\pi u_0\int_0^\infty e^{-\rho^2/a^2}\,\rho\,d\rho.
$$

Let $y=\rho^2/a^2$, so $dy=(2\rho/a^2)d\rho$ and $\rho\,d\rho=(a^2/2)\,dy$:

$$
T
=
2\pi u_0\frac{a^2}{2}\int_0^\infty e^{-y}\,dy
=
\pi u_0 a^2.
$$

So for this profile,

$$
T=\pi u_0 a^2.
$$

This is an explicit, measurable relation:

- larger tube radius increases $T$ linearly in cross-sectional area
  scale,
- larger central energy density increases $T$ proportionally.

---


## Total energy $E$

For approximately uniform $T$ along the loop, total energy is

$$
E = \int_0^L T\,ds = TL.
$$

With $L=2\pi R$ and $T=\pi u_0 a^2$:

$$
E = (\pi u_0 a^2)(2\pi R)=2\pi^2 u_0 a^2 R.
$$

---


## Inertial line density $\mu$

From the Maxwell momentum density relation

$$
\mathbf{g}=\frac{\mathbf{S}}{c^2},
$$

and the null-transport identity (maximal local transport)

$$
|\mathbf{S}|=c\,u,
$$

we get

$$
|\mathbf{g}|=\frac{u}{c}.
$$

For a thin tube whose energy flow is tangent to the loop, the momentum density
vector is approximately aligned with $\hat{\mathbf{t}}(s)$, so the line momentum
density is

$$
p
=
\int_{\Sigma_s}\mathbf{g}\cdot\hat{\mathbf{t}}\,dA
\approx
\int_{\Sigma_s}\frac{u}{c}\,dA
=
\frac{1}{c}\int_{\Sigma_s}u\,dA
=
\frac{T}{c}.
$$

The effective inertial line density is defined by the relation between line
momentum density and effective translation velocity when needed. In the program
we use the identity consistent with energy–momentum bookkeeping:

$$
\mu = \frac{T}{c^2}.
$$

Thus here,

$$
\mu=\frac{\pi u_0 a^2}{c^2}.
$$

This is the precise sense in which “mass per unit length” follows from energy
localization.

---


## Small transverse excitation spectrum on the closed loop

Now define a small transverse displacement field $\xi(s,t)$ describing
small deformations of the tube relative to its equilibrium centerline.

We derive the effective wave equation for $\xi$ using only:

- the loop is a 1D periodic domain,
- there is a tension $T$ resisting deformation,
- and an inertial line density $\mu$.

This is not “importing mechanics.” It is using definitions already derived from
the field: $T$ and $\mu$ come from $u$ and
$\mathbf{S}$.


### Energy functional for small deformations

For small deformations, the leading-order deformation energy on a taut loop has
the form

$$
U[\xi] = \frac{T}{2}\int_0^L |\partial_s\xi|^2\,ds.
$$

Interpretation: gradients along the loop increase length locally;
$T$ weights that cost.

The kinetic energy is

$$
K[\xi] = \frac{\mu}{2}\int_0^L |\partial_t\xi|^2\,ds.
$$

The action is

$$
\mathcal{A}[\xi] = \int (K-U)\,dt.
$$

Varying $\xi$ gives the Euler–Lagrange equation

$$
\mu\,\partial_t^2\xi - T\,\partial_s^2\xi = 0.
$$

Divide by $\mu$ and use $\mu=T/c^2$:

$$
\partial_t^2\xi - c^2\,\partial_s^2\xi = 0.
$$

This is the linear wave equation on a circle of length $L$.


### Periodic boundary condition

Closure of the loop enforces

$$
\xi(s+L,t)=\xi(s,t).
$$


### Fourier modes and discrete spectrum

Expand in Fourier modes:

$$
\xi(s,t)=\sum_{k\in\mathbb{Z}} \xi_k(t)\,e^{i 2\pi k s/L}.
$$

Substitute into the wave equation:

$$
\ddot{\xi}_k(t) + \omega_k^2\,\xi_k(t)=0,
$$

with

$$
\omega_k = \frac{2\pi c}{L}|k| = \frac{c}{R}|k|.
$$

So the loop has a discrete set of normal mode frequencies

$$
\omega_k = \frac{c}{R}|k|,
\qquad
k\in\mathbb{Z}.
$$

This discreteness is forced by topology: the domain is a circle.

No quantization rule has been introduced. This is classical mode discreteness.

---


## Where winding numbers enter in this example

The example above computed $T$, $\mu$, and
$\omega_k$ assuming only:

- the object is a closed loop,
- energy flow is localized in a tube.

To incorporate toroidal winding integers $(m,n)$, one moves from a
single loop to a loop constrained to lie on a torus surface $T^2$ and
be homotopically labeled.

Operationally, the loop class is fixed by its winding around the two cycles:

$$
(m,n)\in\mathbb{Z}^2.
$$

Then:

- the total length $L$ becomes a function of $(m,n)$ and
  the torus geometry,
- and therefore the mode spectrum scales accordingly.

For a standard torus with major radius $R$ and minor radius
$r$, a simple model for the length of a curve winding
$m$ times poloidally and $n$ times toroidally is

$$
L_{m,n}\approx \sqrt{(2\pi n R)^2 + (2\pi m r)^2}.
$$

This is the same “unrolled torus” geometry used in the geometric inertia
document. The frequency set becomes

$$
\omega_k(m,n)=\frac{2\pi c}{L_{m,n}}|k|.
$$

The forced discreteness then has two layers:

- global topological discreteness from $(m,n)$,
- internal Fourier discreteness from $k$ on the closed loop.

---


## Summary of the worked extraction

Given a thin, localized toroidal tube with energy density profile
$u(\rho)=u_0 e^{-\rho^2/a^2}$ on a loop of radius $R$:

1. Tension (line energy density):

$$
T=\pi u_0 a^2.
$$

2. Total energy:

$$
E=2\pi^2 u_0 a^2 R.
$$

3. Inertial line density:

$$
\mu=\frac{\pi u_0 a^2}{c^2}.
$$

4. Small transverse excitation spectrum:

$$
\omega_k=\frac{c}{R}|k|,\qquad k\in\mathbb{Z}.
$$

5. With torus winding constraints $(m,n)$ on a torus of radii
   $(R,r)$:

$$
L_{m,n}\approx \sqrt{(2\pi n R)^2 + (2\pi m r)^2},
\qquad
\omega_k(m,n)=\frac{2\pi c}{L_{m,n}}|k|.
$$

What has been used:
- Maxwell-derived definitions of $u,\mathbf{S}$ and the identity
  $\mathbf{g}=\mathbf{S}/c^2$,
- localization to define a 1D effective object,
- periodicity to enforce discrete modes,
- and torus topology to enforce integer winding.

What has not been used:
- particles,
- external forces,
- quantization axioms,
- spacetime postulates.

This is the minimal worked template for extracting “string-like” effective
parameters from a localized Maxwell configuration.
