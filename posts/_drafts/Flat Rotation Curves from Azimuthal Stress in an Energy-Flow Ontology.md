---
title: "Flat Rotation Curves from Azimuthal Stress in an Energy-Flow Ontology"
date: 2026-03-26
keywords: flat rotation curves, dark matter, azimuthal stress, hoop stress, momentum flux, energy flow, galaxy dynamics
one-sentence-summary: In an extended rotating galaxy, co-rotating closures leave a nonvanishing azimuthal second moment of momentum flux. Its hoop-stress term supplies an inward radial load that can produce flat rotation curves without additional matter.
summary: We derive a dark-matter-like flat-curve regime from the exact coarse-grained momentum balance already recovered in The Physics of Energy Flow. The key correction is that a galaxy should not be reduced to the scalar monopole of randomly oriented closures. A rotating disk retains a coherent azimuthal second moment of transport. That second moment appears as an azimuthal stress component whose cylindrical divergence supplies inward radial loading. Under explicit outer-disk assumptions, the circular speed satisfies v_phi^2 ≈ Sigma_phiphi / rho. If the fraction of local energy stored in aligned unresolved azimuthal transport is slowly varying, the rotation curve is flat. The "dark halo" then becomes the mass one would falsely infer by fitting a stress-supported disk with a monopole law.
---

# Flat Rotation Curves from Azimuthal Stress in an Energy-Flow Ontology

## 1. The point of departure

Chapter 12 of *The Physics of Energy Flow* recovered the weak-field Newtonian
limit by summing the positive scalar energies of many closures and taking the
far field of a compact aggregate. That argument is correct for a roughly
compact, mixed, and orientation-averaged body.

A spiral galaxy is not such a body.

It is:

- extended rather than compact,
- axisymmetric rather than spherical,
- and rotating, so its closures need not be orientation-random.

The scalar monopole therefore cannot be the whole story. In a rotating disk,
the first moment of the organized flow may cancel while the second moment
survives. That surviving second moment is stress.

The dark-matter question is therefore recast as follows:

> can the flat outer rotation curves of galaxies arise from a surviving
> azimuthal stress of organized energy flow, rather than from additional
> unseen matter?

Under the assumptions stated below, the answer is yes at the level of the
rotation-curve problem itself.


## 2. Why the monopole average misses the galactic case

Let $\hat{\mathbf e}_\phi(\phi)$ denote the local azimuthal direction in the
galactic plane.

Around a full annulus,

$$
\int_0^{2\pi}\hat{\mathbf e}_\phi(\phi)\,d\phi = 0.
$$

So any vector sum of the azimuthal transport can vanish.

But the second moment does not vanish:

$$
\hat{\mathbf e}_\phi\otimes\hat{\mathbf e}_\phi \neq 0.
$$

This is the basic structural point. A rotating galaxy can have no net vector
flux around the annulus and still carry a nonzero azimuthal momentum-flux
tensor.

That is exactly what a monopole reduction throws away. The monopole keeps the
scalar energy and discards the directional part. A rotating disk keeps a
directional second moment, and that second moment contributes to radial
balance.


## 3. Exact coarse-grained momentum balance

Appendix 207 already recovered the exact coarse-grained momentum equation

$$
\partial_t(\rho\mathbf v)
+
\nabla\cdot(\rho\,\mathbf v\otimes\mathbf v)
-
\nabla\cdot\boldsymbol{\Sigma}
=
0,
$$

where

$$
\rho=\frac{\langle u\rangle}{k^2}
$$

is the effective inertial density,

$$
\rho\mathbf v=\left\langle \frac{\mathbf S}{k^2}\right\rangle
$$

is the mean transport momentum density, and $\boldsymbol{\Sigma}$ is the exact
residual stress tensor of the unresolved transport.

Take a steady axisymmetric disk in cylindrical coordinates $(R,\phi,z)$ with

$$
\partial_t=0,
\qquad
\partial_\phi=0,
\qquad
\mathbf v = v_\phi(R,z)\,\hat{\mathbf e}_\phi,
$$

and negligible mean radial or vertical drift:

$$
v_R=v_z=0.
$$

Then the radial component of the convective term is the usual centripetal term,

$$
\bigl[\nabla\cdot(\rho\,\mathbf v\otimes\mathbf v)\bigr]_R
=
-\rho\,\frac{v_\phi^2}{R}.
$$

So the exact radial balance is

$$
\rho\,\frac{v_\phi^2}{R}
=
-\bigl(\nabla\cdot\boldsymbol{\Sigma}\bigr)_R.
$$

For an axisymmetric stress tensor, the radial divergence is

$$
\bigl(\nabla\cdot\boldsymbol{\Sigma}\bigr)_R
=
\partial_R \Sigma_{RR}
+
\frac{\Sigma_{RR}-\Sigma_{\phi\phi}}{R}
+
\partial_z \Sigma_{Rz}.
$$

Therefore

$$
\rho\,\frac{v_\phi^2}{R}
=
-\partial_R \Sigma_{RR}
-
\frac{\Sigma_{RR}-\Sigma_{\phi\phi}}{R}
-
\partial_z \Sigma_{Rz}.
$$

This equation is exact. No dark matter has been inserted. No modified force law
has been inserted. Everything now depends on the structure of the unresolved
stress.


## 4. The azimuthal-stress regime

In the outer disk, suppose the unresolved transport is dominated by aligned
azimuthal circulation. Then the residual stress is anisotropic, with

$$
\Sigma_{\phi\phi}
\gg
\Sigma_{RR},
\qquad
\Sigma_{\phi\phi}
\gg
R\,|\partial_R\Sigma_{RR}|,
\qquad
\Sigma_{\phi\phi}
\gg
R\,|\partial_z\Sigma_{Rz}|.
$$

Under these explicit assumptions, the radial balance reduces to

$$
\rho\,\frac{v_\phi^2}{R}
\approx
\frac{\Sigma_{\phi\phi}}{R},
$$

so

$$
\boxed{
v_\phi^2 \approx \frac{\Sigma_{\phi\phi}}{\rho}.
}
$$

This is the key equation.

Flat rotation curves therefore do not require an additional scalar mass
distribution if the outer galaxy carries a residual azimuthal stress whose
ratio to the effective inertial density is approximately constant.


## 5. Why $\Sigma_{\phi\phi}$ can survive

Appendix 216 already gives the local transport-stress magnitude of a narrow
null Maxwell packet. If $\mathbf n$ is the packet direction, then the
longitudinal momentum-flux density is

$$
\Pi_n = -n_i n_j T_{ij} = u.
$$

So a narrow transport element moving in the azimuthal direction carries a
positive azimuthal transport-stress magnitude equal to its energy density.

For a coarse-grained ensemble of co-rotating closures, let

$$
u_\phi(R,z)
$$

be the part of the local energy density stored in unresolved azimuthal
transport. Then the corresponding leading residual stress is

$$
\Sigma_{\phi\phi}\approx u_\phi.
$$

Inside the same constitutive class already used in the gravity appendices,

$$
\rho = \frac{u}{k^2},
$$

so if a fraction

$$
f(R,z):=\frac{u_\phi(R,z)}{u(R,z)}
$$

of the local coarse-grained energy sits in aligned unresolved azimuthal
transport, then

$$
\Sigma_{\phi\phi}\approx f\,u = f\,\rho\,k^2.
$$

Substituting into the outer-disk balance gives

$$
\boxed{
v_\phi^2 \approx f\,k^2.
}
$$

This is the strongest compact form of the result.


## 6. Flat curves

Equation

$$
v_\phi^2 \approx f\,k^2
$$

shows immediately how a plateau arises.

If, over the outer galactic regime,

$$
f(R,z)\approx f_0,
\qquad
k(R,z)\approx k_0,
$$

with both varying only slowly, then

$$
v_\phi(R)\approx \sqrt{f_0}\,k_0 = \text{const.}
$$

The rotation curve is flat.

The ontology is then clear:

- the inward radial load is supplied by the cylindrical divergence of a
  surviving azimuthal stress,
- that stress comes from unresolved co-rotating organized transport,
- and the apparent dark halo is the scalar mass one would falsely infer by
  fitting that stress-supported motion with a monopole law.


## 7. Why the standard dark-halo inference appears

Observers often translate the measured circular speed into an inferred enclosed
mass by the spherical Newtonian relation

$$
M_{\mathrm{inf}}(R)=\frac{R\,v_\phi^2(R)}{G}.
$$

If $v_\phi(R)$ is flat, this gives

$$
M_{\mathrm{inf}}(R)\propto R,
$$

which is then read as evidence for a massive unseen halo.

In the present ontology, that linear growth is not necessarily the profile of
an unseen scalar mass. It is the scalar mass one would back-fit to motion that
is actually supported by anisotropic azimuthal stress:

$$
M_{\mathrm{inf}}(R)
\approx
\frac{R}{G}\,\frac{\Sigma_{\phi\phi}(R)}{\rho(R)}.
$$

So the "dark matter" can be, at the level of flat rotation curves, a stress
misread as mass.


## 8. What this does and does not explain

This derivation explains the original flat-curve trigger of the dark-matter
problem inside the energy-flow ontology:

- no additional matter is required,
- no empirical force-law modification is required,
- the effect is produced by the exact coarse-grained momentum equation already
  recovered from source-free transport.

But it does **not** yet explain everything commonly grouped under the dark
matter label.

Still open are:

- a constitutive derivation of the plateau fraction $f_0$ from the microphysics
  of galactic closures,
- the relation, if any, between this stress mechanism and the baryonic
  Tully-Fisher law,
- and the corresponding lensing calculation.

So the present result should be read narrowly and exactly:

> flat galactic rotation curves can be recovered, in this ontology, from the
> surviving azimuthal stress of organized co-rotating transport in an extended
> axisymmetric disk.


## 9. Final statement

The correct collective object for a rotating galaxy is not the scalar monopole
of a compact random aggregate. It is the stress tensor of an extended organized
disk.

The vector part of the azimuthal transport can cancel around the galaxy. The
second moment does not. That surviving second moment is an azimuthal stress,
and its cylindrical hoop-stress term supplies the inward radial loading needed
for circular motion.

Under the explicit outer-disk assumptions above,

$$
v_\phi^2 \approx \frac{\Sigma_{\phi\phi}}{\rho}\approx f\,k^2,
$$

so a slowly varying azimuthal transport fraction produces a flat rotation
curve.

At that level, the missing mass is not missing matter. It is missing stress.
