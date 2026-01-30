## Worked example 3: a helical trajectory on a torus with explicit $(m,n)$, explicit length $L_{m,n}$, and discrete frequency scales

This example makes the $(m,n)$ data operational.

We do not invoke “string postulates.” We use only:

- a torus as a closed surface supporting tangent flow,
- closure of a flow line as a periodicity condition,
- and the already-derived consequence that periodic domains enforce discrete
  mode spectra.

The central deliverables are:

- a concrete parametrization of a torus,
- a concrete curve class with winding numbers $(m,n)$,
- an explicit approximate formula for the curve length $L_{m,n}$,
- and the resulting mode frequencies $\omega_k(m,n)$ for perturbations on the
  closed path.

The point is to show exactly how integer winding forces discrete geometry, hence
discrete spectral structure.

---


## Torus geometry

Fix two radii:

- major radius $R$ (distance from center of hole to tube center),
- minor radius $r$ (radius of the tube).

Standard embedding of a torus in $\mathbb{R}^3$ uses angles $(\phi,\theta)$:

- $\phi$ is the toroidal angle (around the hole),
- $\theta$ is the poloidal angle (around the tube).

Define

$$
\mathbf{X}(\phi,\theta)=
\begin{pmatrix}
(R+r\cos\theta)\cos\phi\\
(R+r\cos\theta)\sin\phi\\
r\sin\theta
\end{pmatrix},
\qquad
(\phi,\theta)\in[0,2\pi)\times[0,2\pi).
$$

Compute tangent basis vectors:

$$
\partial_\phi \mathbf{X}=
\begin{pmatrix}
-(R+r\cos\theta)\sin\phi\\
\ \ (R+r\cos\theta)\cos\phi\\
0
\end{pmatrix},
\qquad
|\partial_\phi \mathbf{X}|=R+r\cos\theta,
$$

$$
\partial_\theta \mathbf{X}=
\begin{pmatrix}
- r\sin\theta\cos\phi\\
- r\sin\theta\sin\phi\\
\ \ r\cos\theta
\end{pmatrix},
\qquad
|\partial_\theta \mathbf{X}|=r.
$$

Also note orthogonality:

$$
\partial_\phi \mathbf{X}\cdot \partial_\theta \mathbf{X}=0.
$$

Thus the induced metric on the torus is

$$
ds^2 = (R+r\cos\theta)^2\,d\phi^2 + r^2\,d\theta^2.
$$

---


## A curve class with winding numbers $(m,n)$

A simple representative curve with toroidal winding $n$ and
poloidal winding $m$ is

$$
\phi(t)=nt,\qquad \theta(t)=mt,\qquad t\in[0,2\pi].
$$

Closure is automatic because at $t=2\pi$:

$$
\phi(2\pi)=2\pi n,\qquad \theta(2\pi)=2\pi m,
$$

so both angles return mod $2\pi$.

Thus $(m,n)\in\mathbb{Z}^2$ label the homotopy class of the curve.

This curve is not the most general torus-knot trajectory, but it is a clean
canonical representative for derivations.

---


## Exact arclength integral for this $(m,n)$ curve

Compute $ds$ along the curve using the metric.

We have

$$
d\phi = n\,dt,\qquad d\theta=m\,dt.
$$

So

$$
ds^2
=
(R+r\cos\theta)^2(n\,dt)^2 + r^2(m\,dt)^2.
$$

But $\theta(t)=mt$, so $\cos\theta=\cos(mt)$:

$$
ds
=
\sqrt{n^2(R+r\cos(mt))^2 + m^2 r^2}\,dt.
$$

Thus the total length is

$$
L_{m,n}=
\int_0^{2\pi}
\sqrt{n^2(R+r\cos(mt))^2 + m^2 r^2}\,dt.
$$

This is an explicit formula. It is generally not elementary because of the
$\cos(mt)$ inside the square root.

But it is already enough to show:

- $L_{m,n}$ depends on integers $(m,n)$,
- and thus any quantity depending on $L$ is discretized by
  topology.

Still, we can proceed further with useful approximations.

---


## Thin-torus approximation and explicit length estimate

Assume a thin torus:

$$
r \ll R.
$$

Then $R+r\cos(mt)\approx R$ to leading order, and we get

$$
ds \approx \sqrt{n^2R^2 + m^2 r^2}\,dt.
$$

This is constant in $t$, so

$$
L_{m,n}\approx \int_0^{2\pi}\sqrt{n^2R^2 + m^2 r^2}\,dt
=
2\pi\sqrt{n^2R^2 + m^2 r^2}.
$$

Equivalently,

$$
L_{m,n}\approx 2\pi\sqrt{(nR)^2 + (mr)^2}.
$$

This is the same “unrolled chart” intuition:

- around the torus: distance per turn $\sim 2\pi R$ (toroidal),
- around the tube: distance per turn $\sim 2\pi r$ (poloidal),
- total path behaves like hypotenuse of a rectangle scaled by $(n,m)$.

This shows explicitly how integers turn into geometric length.

---


## Effective forward speed on the torus

We now define “forward” as the toroidal direction (increasing $\phi$).
This is the natural macroscopic direction for an energy flow circulating around
the hole.

Along the curve, the $\phi$-motion per $dt$ is
$d\phi=n\,dt$. The physical toroidal arc element is $(R+r\cos\theta)\,d\phi$.

In the thin approximation, this is approximately $R\,d\phi$. So the
physical toroidal displacement over $dt$ is approximately:

$$
d\ell_{\text{tor}} \approx R\,d\phi = Rn\,dt.
$$

Meanwhile the arclength travelled is approximately:

$$
ds \approx \sqrt{n^2R^2 + m^2 r^2}\,dt.
$$

So the projection factor is

$$
\frac{d\ell_{\text{tor}}}{ds}
\approx
\frac{Rn}{\sqrt{n^2R^2 + m^2 r^2}}.
$$

If local transport along the path is at speed $c$:

$$
\frac{ds}{dt}=c,
$$

then the effective toroidal transport speed is

$$
v_{\text{tor}}(m,n)
=
\frac{d\ell_{\text{tor}}}{dt}
=
\frac{d\ell_{\text{tor}}}{ds}\frac{ds}{dt}
\approx
c\frac{Rn}{\sqrt{n^2R^2 + m^2 r^2}}.
$$

Thus

$$
v_{\text{tor}}(m,n)
\approx
\frac{c}{\sqrt{1+\left(\frac{mr}{nR}\right)^2}}.
$$

This is the torus analogue of the helix result $v=c\cos\theta$, with

$$
\cos\theta_{\mathrm{eff}}(m,n)
=
\frac{Rn}{\sqrt{n^2R^2 + m^2r^2}}.
$$

So winding in the poloidal direction forces a reduction in effective toroidal
transport.

---


## Discrete mode spectrum on the closed trajectory

Now treat the flow line as a 1D closed domain of length $L_{m,n}$.

Small transverse excitations $\xi(s,t)$ satisfy, at leading order,

$$
\partial_t^2\xi - c^2\partial_s^2\xi = 0,
$$

with periodicity

$$
\xi(s+L_{m,n},t)=\xi(s,t).
$$

Therefore Fourier modes are

$$
\xi(s,t)=\sum_{k\in\mathbb{Z}}\xi_k(t)\,e^{i2\pi ks/L_{m,n}},
$$

and the normal frequencies are

$$
\omega_k(m,n)=\frac{2\pi c}{L_{m,n}}|k|.
$$

Using the thin-torus length approximation gives a fully explicit scale:

$$
\omega_k(m,n)
\approx
\frac{2\pi c}{2\pi\sqrt{n^2R^2+m^2r^2}}|k|
=
\frac{c}{\sqrt{n^2R^2+m^2r^2}}|k|.
$$

Thus the frequency scale is discretized by:

- $k\in\mathbb{Z}$ from periodicity on a loop,
- $(m,n)\in\mathbb{Z}^2$ from topological closure class on the torus.

This is the precise mechanism behind “discreteness from topology” in the
program.

Nothing quantum has been assumed.

---


## Where “tension” and “inertia” enter here

From the thin-tube extraction:

$$
T=\int_{\Sigma_s} u\,dA,
\qquad
\mu=\frac{T}{c^2}.
$$

On any closed trajectory the same holds.

So for a torus-wound tube:

- $T$ depends on the cross-sectional energy profile,
- $\mu$ follows,
- and the closed length $L_{m,n}$ fixes the discrete mode spacings.

Thus the object is characterized by:

- local quantities: $T$, $\mu$,
- global quantities: $(m,n)$, $L_{m,n}$,
- and internal spectrum: $\omega_k(m,n)$.

All are computed from localization plus topology.

---


## Summary of the torus winding worked example

1. Torus embedding yields metric:

$$
ds^2=(R+r\cos\theta)^2d\phi^2 + r^2d\theta^2.
$$

2. Canonical winding curve:

$$
\phi(t)=nt,\qquad \theta(t)=mt,\qquad t\in[0,2\pi].
$$

3. Exact length:

$$
L_{m,n}=
\int_0^{2\pi}
\sqrt{n^2(R+r\cos(mt))^2 + m^2 r^2}\,dt.
$$

4. Thin-torus explicit approximation:

$$
L_{m,n}\approx 2\pi\sqrt{n^2R^2+m^2r^2}.
$$

5. Effective toroidal transport speed (projection):

$$
v_{\text{tor}}(m,n)
\approx
c\frac{Rn}{\sqrt{n^2R^2+m^2r^2}}
=
\frac{c}{\sqrt{1+\left(\frac{mr}{nR}\right)^2}}.
$$

6. Discrete mode spectrum on the closed trajectory:

$$
\omega_k(m,n)=\frac{2\pi c}{L_{m,n}}|k|
\approx
\frac{c}{\sqrt{n^2R^2+m^2r^2}}|k|.
$$

This is the explicit bridge from:
- divergence-free closed flow on a torus
to
- integer winding
to
- discrete geometrical length
to
- discrete mode spectrum.
