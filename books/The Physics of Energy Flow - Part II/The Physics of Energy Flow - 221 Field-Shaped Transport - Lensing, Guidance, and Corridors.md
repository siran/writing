title: The Physics of Energy Flow - 221 Field-Shaped Transport - Lensing, Guidance, and Corridors
date: 2026-03-17
---

# 221. Field-Shaped Transport: Lensing, Guidance, and Corridors

Appendix 214 derived the radiative packet law in a static variable-speed
background:

$$
\dot{\mathbf x}=k(\mathbf x)\,\hat{\mathbf t},
\qquad
\frac{d\hat{\mathbf t}}{ds}=-\nabla_\perp\ln k.
$$

Appendix 219 used that law to show that lower loading can create a faster
transport corridor. The present appendix derives the corresponding lensing and
guidance consequences. Appendix 222 derives one fundamental way such unloading
can be produced: boundary subtraction of a selected passive mode.

The point is simple. Once a static field configuration creates a spatial
loading profile and therefore a spatial transport-speed profile

$$
k(\mathbf x),
$$

later Maxwellian transport is bent by that profile. Field-shaped transport
therefore acts as lens, guide, or corridor according to the geometry of $k$.

## 221.1 Static Field-Shaped Background

Within the symmetric constitutive class of appendix 214,

$$
\varepsilon=\varepsilon_0\alpha(\mathbf x),
\qquad
\mu=\mu_0\alpha(\mathbf x),
\qquad
k(\mathbf x)=\frac{c}{\alpha(\mathbf x)}.
$$

So a static organized electromagnetic loading profile is equivalently a static
transport-speed profile.

All the results below follow from that profile alone. No extra force law is
introduced.

## 221.2 Exact Ray Equation

For a narrow radiative packet, appendix 214 gives

$$
\dot{\mathbf p}=-U\,\nabla\ln k.
$$

Equivalently, with $\hat{\mathbf t}= \mathbf p/|\mathbf p|$ and arclength $s$,

$$
\frac{d\hat{\mathbf t}}{ds}=-\nabla_\perp\ln k.
$$

This is the exact transport-curvature law.

Its content is immediate:

- if $\nabla_\perp k$ points inward, rays bend inward,
- if $\nabla_\perp k$ points outward, rays bend outward,
- if $\nabla_\perp k=0$, the packet continues straight.

So lensing and guidance are not extra phenomena added afterward. They are the
direct geometric consequences of the field-shaped transport profile.

## 221.3 Axisymmetric Lensing

Take an axisymmetric static profile about the $z$ axis, and let

$$
r_\perp = \sqrt{x^2+y^2}
$$

denote the transverse radius.

For a ray nearly parallel to the axis, the paraxial approximation gives

$$
\frac{d^2\mathbf r_\perp}{dz^2}
=
-\nabla_\perp \ln k(\mathbf r_\perp,z).
$$

This is the lens equation of the present framework.

So:

- a profile with $k$ increasing away from the axis bends rays inward,
- a profile with $k$ decreasing away from the axis bends rays outward.

The first is focusing. The second is defocusing.

## 221.4 Paraxial Focusing and Defocusing

Expand near the axis.

### Focusing core

If the transport speed has a local minimum on the axis, write

$$
k(r_\perp)=k_0\!\left(1+\frac{\beta}{2}r_\perp^2\right)+O(r_\perp^4),
\qquad
\beta>0.
$$

Then

$$
\ln k(r_\perp)=\ln k_0+\frac{\beta}{2}r_\perp^2+O(r_\perp^4),
$$

so

$$
\nabla_\perp\ln k = \beta\,\mathbf r_\perp + O(r_\perp^3).
$$

Therefore the paraxial ray equation becomes

$$
\frac{d^2\mathbf r_\perp}{dz^2}+\beta\,\mathbf r_\perp=0.
$$

This is harmonic confinement. Rays oscillate about the axis. A low-speed core
is therefore a passive focusing guide.

### Defocusing core

If the transport speed has a local maximum on the axis, write

$$
k(r_\perp)=k_0\!\left(1-\frac{\beta}{2}r_\perp^2\right)+O(r_\perp^4),
\qquad
\beta>0.
$$

Then

$$
\ln k(r_\perp)=\ln k_0-\frac{\beta}{2}r_\perp^2+O(r_\perp^4),
$$

so

$$
\nabla_\perp\ln k = -\beta\,\mathbf r_\perp + O(r_\perp^3).
$$

Hence

$$
\frac{d^2\mathbf r_\perp}{dz^2}-\beta\,\mathbf r_\perp=0.
$$

This is exponential defocusing. A high-speed core does not passively trap
transport.

## 221.5 Passive Guides and Fast Corridors

The previous section separates two different design objectives.

### Passive guide

If the goal is passive focusing or confinement, the axis must be a local
minimum of $k$. Then transport is slower on axis but naturally guided.

### Fast corridor

If the goal is faster transit than through neighboring regions, the corridor
must have larger $k$ than those neighbors. Then transport through the core is
faster, but the core is not passively confining.

So a fast corridor and a passive guide are not the same object.

## 221.6 Engineered Guidance

A high-speed corridor can still be made useful. The point is simply that its
guidance is an engineering problem rather than an automatic consequence of the
speed contrast.

The necessary extra structure may come from:

- shaped boundaries,
- reflective or refractive sheaths,
- segmented lensing profiles,
- or active transduction along the path.

So the exact derived consequence is this:

- field-shaped loading profiles can lens transport,
- some profiles passively guide,
- some profiles maximize speed,
- and combining both requires designed structure.

## 221.7 Final Statement

Organized electromagnetic loading shapes the local transport-speed profile
$k(\mathbf x)$. Once that happens, later Maxwellian transport is bent by the
exact ray law

$$
\frac{d\hat{\mathbf t}}{ds}=-\nabla_\perp\ln k.
$$

This yields:

- field-shaped lenses,
- passive low-speed guides,
- and high-speed corridors whose routing requires engineering.

So lensing, guidance, and corridor transport are not external technologies
added to the framework. They are direct engineering consequences of taking the
transport ontology seriously.
