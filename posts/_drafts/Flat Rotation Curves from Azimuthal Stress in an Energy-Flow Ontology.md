---
title: "Flat Rotation Curves from Azimuthal Stress in an Energy-Flow Ontology"
date: 2026-03-26
keywords: flat rotation curves, dark matter, lensing, azimuthal stress, hoop stress, momentum flux, energy flow, galaxy dynamics
one-sentence-summary: In an extended rotating galaxy, co-rotating closures leave a nonvanishing azimuthal second moment of momentum flux. Its hoop-stress term supplies the inward radial load behind flat rotation curves, and the same weak constitutive summary yields the corresponding logarithmic lensing law.
summary: We derive a dark-matter-like flat-curve regime from the exact coarse-grained momentum balance already recovered in The Physics of Energy Flow. The key correction is that a galaxy should not be reduced to the scalar monopole of randomly oriented closures. A rotating disk retains a coherent azimuthal second moment of transport. That second moment appears as an azimuthal stress component whose cylindrical divergence supplies inward radial loading. Under explicit outer-disk assumptions, the circular speed satisfies v_phi^2 approximately equal to Sigma_phiphi / rho. If the fraction of local energy stored in aligned unresolved azimuthal transport is slowly varying, the rotation curve is flat. The same slow-mode radial load defines a logarithmic weak scalar, and under the same symmetric constitutive summary used in the gravity chapters a null probe is then deflected by an angle Delta alpha = 2 pi v_f^2 / c^2 in the flat regime. The "dark halo" becomes the mass one would falsely infer by fitting a stress-supported disk with a monopole law.
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


## 8. Direct source derivation of the weak scalar

The flat-curve derivation above concerns slow bounded transport. The missing
step is to derive the corresponding weak scalar directly from the galactic
source itself rather than infer it afterward from the slow-mode force law.

Appendix 216 already gives the weak interaction operator seen by a probe with
channel direction $\mathbf n$:

$$
\Lambda_n=u+\Pi_n,
\qquad
\Pi_n:=-n_in_jT_{ij}.
$$

Because the weak interaction energy is bilinear and symmetric between source
and probe, the same scalar must also appear on the source side. For a general
static source with local energy density $u_s$ and stress tensor $T^{(s)}_{ij}$,
define the source load density in the channel $\mathbf n$ by

$$
q_n
:=
u_s+\Pi_n^{(s)}
=
u_s-n_in_jT^{(s)}_{ij}.
$$

The weak scalar sourced by that channel is then

$$
\boxed{
\eta_n(\mathbf x)
=
\frac{G}{c^4}
\int
\frac{q_n(\mathbf x')}{|\mathbf x-\mathbf x'|}\,d^3x'.
}
$$

This is the natural source-side extension of appendix 216 inside the same weak
bilinear interaction class. It is not yet a claim about the full exact
strong-field kernel.

For a compact mixed aggregate, the directional part averages away and this
reduces to the scalar monopole of chapter 12.

For the rotating galactic disk, the relevant slow bounded transport is
azimuthal. Take therefore

$$
\mathbf n=\hat{\mathbf e}_\phi.
$$

In the same coarse-grained notation as above,

$$
q_\phi
=
u+\Pi_\phi
\approx
u+\Sigma_{\phi\phi}.
$$

Here the approximation is the same outer-disk coarse-graining already used in
sections 3 through 6: the surviving source-side directional load is the
unresolved azimuthal second moment.

In the outer azimuthal-stress regime,

$$
\Sigma_{\phi\phi}\approx f\,u,
$$

so

$$
q_\phi\approx (1+f)\,u=(1+f)\rho k^2.
$$

Now pass to the thin-disk approximation and define the corresponding surface
load density

$$
q_{\Sigma,\phi}(R):=\int_{-\infty}^{\infty}q_\phi(R,z)\,dz.
$$

The flat outer regime is scale-free: over that range there is no preferred
radius. The unique axisymmetric surface profile with that property is

$$
\boxed{
q_{\Sigma,\phi}(R)=\frac{Q_0}{R},
}
$$

where $Q_0$ is the constant source load per logarithmic annulus.

Use the standard axisymmetric Hankel representation for a thin sheet:

$$
\eta_{\mathrm{gal}}(R,z)
=
\frac{2\pi G}{c^4}
\int_0^\infty
S(k)\,J_0(kR)\,e^{-k|z|}\,dk,
$$

with

$$
S(k)
:=
\int_0^\infty q_{\Sigma,\phi}(R')\,J_0(kR')\,R'\,dR'.
$$

Substituting $q_{\Sigma,\phi}(R')=Q_0/R'$ gives

$$
S(k)
=
Q_0\int_0^\infty J_0(kR')\,dR'
=
\frac{Q_0}{k}.
$$

Therefore on the midplane,

$$
\eta_{\mathrm{gal}}(R,0)
=
\frac{2\pi GQ_0}{c^4}
\int_0^\infty \frac{J_0(kR)}{k}\,dk.
$$

Using

$$
\int_0^\infty \frac{J_0(kR)}{k}\,dk
=
\text{const.}-\ln R,
$$

we obtain

$$
\boxed{
\eta_{\mathrm{gal}}(R)
=
\eta_0
-\frac{2\pi GQ_0}{c^4}\ln\!\frac{R}{R_0},
}
$$

with $\eta_0$ an irrelevant additive constant.

Differentiate:

$$
\partial_R\eta_{\mathrm{gal}}
=
-\frac{2\pi GQ_0}{c^4R}.
$$

Appendix 213 gives the slow-mode potential

$$
\Phi_k=-c^2\eta,
$$

so the radial acceleration is

$$
a_R
=
-\partial_R\Phi_k
=
c^2\partial_R\eta_{\mathrm{gal}}
=
-\frac{2\pi GQ_0}{c^2R}.
$$

Hence the circular-speed law is

$$
\boxed{
v_f^2=\frac{2\pi GQ_0}{c^2},
}
$$

and therefore

$$
\boxed{
\eta_{\mathrm{gal}}(R)
=
\eta_0-\frac{v_f^2}{c^2}\ln\!\frac{R}{R_0}.
}
$$

This is the direct source derivation that was missing: the logarithmic weak
scalar is generated by the scale-free azimuthal source load of the disk itself,
not backed out afterward from the observed slow-mode force law.


## 9. Null-probe lensing from the same source-derived scalar

Adopt the same weak constitutive summary already recovered in the gravity
chapters for null probes:

$$
n=1+2\eta,
\qquad
k=\frac{c}{1+2\eta}.
$$

Using the source-derived scalar above,

$$
n(R)
=
n_0-\frac{2v_f^2}{c^2}\ln\!\frac{R}{R_0},
$$

where the constant part $n_0:=1+2\eta_0$ plays no role in bending.

Take a null probe with impact parameter $b$ in the scale-free outer regime,
and write

$$
R^2=b^2+z^2
$$

along the unperturbed path. Then

$$
\partial_\perp n
=
-\frac{2v_f^2}{c^2}\,\frac{b}{b^2+z^2}.
$$

Using the same weak-ray law as chapter 12, the inward deflection magnitude is

$$
\Delta\alpha
=
\int_{-\infty}^{\infty}\bigl|\partial_\perp n\bigr|\,dz
=
\frac{2v_f^2}{c^2}
\int_{-\infty}^{\infty}\frac{b\,dz}{b^2+z^2}
=
\frac{2v_f^2}{c^2}
\left[\arctan\!\frac{z}{b}\right]_{-\infty}^{\infty}.
$$

Therefore

$$
\boxed{
\Delta\alpha
=
\frac{2\pi v_f^2}{c^2}.
}
$$

This is the characteristic logarithmic-lens result of the flat regime:

- it is determined by the same plateau speed $v_f$ that governs the rotation
  curve,
- it is independent of impact parameter inside the scale-free regime,
- and it is recovered from the same source-derived weak scalar once the galaxy
  is treated as a stress-supported disk rather than as a compact scalar
  monopole.


## 10. What this does and does not explain

This derivation explains the original flat-curve trigger of the dark-matter
problem inside the energy-flow ontology, together with the corresponding
logarithmic lensing law of the same regime:

- no additional matter is required,
- no empirical force-law modification is required,
- the effect is produced by the exact coarse-grained momentum equation already
  recovered from source-free transport,
- and the null deflection follows from the same weak constitutive summary
  already used in the gravity chapters.

But it does **not** yet explain everything commonly grouped under the dark
matter label.

Still open are:

- a constitutive derivation of the plateau fraction $f_0$ from the microphysics
  of galactic closures,
- a derivation of the scale-free outer source profile
  $q_{\Sigma,\phi}(R)=Q_0/R$ from that same microphysics, rather than taking
  scale-freedom as the macroscopic outer-disk assumption,
- the relation, if any, between this stress mechanism and the baryonic
  Tully-Fisher law,
- and the non-ideal corrections from finite disk thickness, disk truncation,
  and non-axisymmetric structure.

So the present result should be read narrowly and exactly:

> flat galactic rotation curves, together with the corresponding logarithmic
> lensing law of the same outer regime, can be recovered in this ontology from
> the surviving azimuthal stress of organized co-rotating transport in an
> extended axisymmetric disk.


## 11. Final statement

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
\qquad
\eta_{\mathrm{gal}}(R)
\approx
\eta_0-\frac{v_f^2}{c^2}\ln\!\frac{R}{R_0},
\qquad
\Delta\alpha \approx \frac{2\pi v_f^2}{c^2},
$$

so a slowly varying azimuthal transport fraction produces a flat rotation
curve, the corresponding scale-free source load produces the logarithmic weak
scalar, and the same weak constitutive summary yields the matching
logarithmic-regime lensing strength.

At that level, the missing mass is not missing matter. It is missing stress.
