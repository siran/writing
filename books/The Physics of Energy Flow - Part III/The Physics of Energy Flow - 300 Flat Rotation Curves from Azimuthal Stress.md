---
title: "The Physics of Energy Flow - Flat Rotation Curves from Azimuthal Stress"
date: 2026-03-26
keywords: flat rotation curves, dark matter, lensing, azimuthal stress, hoop stress, momentum flux, energy flow, galaxy dynamics
one-sentence-summary: In an extended rotating galaxy, co-rotating closures leave a nonvanishing azimuthal second moment of momentum flux. Its hoop-stress term can supply the inward radial load behind flat rotation curves, and the same weak constitutive summary then yields the corresponding logarithmic lensing law.
summary: This note develops a dark-matter-like flat-curve regime from the exact coarse-grained momentum balance already recovered in The Physics of Energy Flow. The key correction is that a galaxy should not be reduced to the scalar monopole of randomly oriented closures. A rotating disk retains a coherent azimuthal second moment of transport. That second moment appears as an azimuthal stress component whose cylindrical divergence supplies inward radial loading. Under explicit outer-disk assumptions, the circular speed satisfies v_phi^2 approximately equal to Sigma_phiphi / rho. If the fraction of local energy stored in aligned unresolved azimuthal transport is slowly varying, the rotation curve is flat. The same recovered slow-mode radial load then fixes a logarithmic weak scalar, and under the same symmetric constitutive summary used in the gravity chapters a null probe is deflected by an angle Delta alpha = 2 pi v_f^2 / c^2 in the flat regime. The "dark halo" becomes the mass one would falsely infer by fitting a stress-supported disk with a monopole law. The note closes the flat-curve mechanism and its matching weak lensing only inside that constitutive class; it does not yet solve every phenomenon grouped under the dark-matter label.
---

# 300. Flat Rotation Curves from Azimuthal Stress

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

This text sits in Part III rather than in the main book or its technical
appendices because the galactic regime is not yet closed. What is developed
here is a serious candidate mechanism for the flat-curve regime, together with
the matching logarithmic weak-lensing law inside the same weak constitutive
closure already used in the gravity chapters. What is *not* yet recovered is
the full galactic microphysics that would make those outer-disk assumptions
follow automatically.


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

This point can be written directly. Let

$$
\mathbf A(R,z)=A_\phi(R,z)\,\hat{\mathbf e}_\phi
$$

be a purely azimuthal axisymmetric transport field. Then

$$
\nabla\cdot\mathbf A
=
\frac{1}{R}\partial_\phi A_\phi
=
0.
$$

So the first moment is divergence-free.

But now form its second moment:

$$
\mathbf Q:=\mathbf A\otimes\mathbf A.
$$

Its only nonzero component is

$$
Q_{\phi\phi}=A_\phi^2.
$$

Using the cylindrical divergence formula,

$$
\bigl(\nabla\cdot\mathbf Q\bigr)_R
=
\partial_R Q_{RR}
+
\frac{Q_{RR}-Q_{\phi\phi}}{R}
+
\partial_z Q_{Rz}
=
-\frac{A_\phi^2}{R}.
$$

So a purely azimuthal divergence-free flow still carries an inward radial load
through the divergence of its second moment. That is the exact mathematical
form of hoop stress.

This is the sense in which a vortex-like `(m,n)` organization can add pull
without adding source or sink: not through $\nabla\cdot\mathbf A$, but through
$\nabla\cdot(\mathbf A\otimes\mathbf A)$ and its coarse-grained stress
descendants.


### 2.1. Why the galactic excess is not a multipole tail

It is important not to confuse two different notions of "second moment."

A scalar multipole expansion of a compact source is one thing. The surviving
directional second moment of organized transport is another.

For a compact scalar exterior field, the far expansion has the form

$$
\eta(r,\Omega)
=
\frac{M_0}{r}
+
\frac{D_1(\Omega)}{r^2}
+
\frac{Q_2(\Omega)}{r^3}
+
\cdots
$$

where the angular factors encode dipole, quadrupole, and higher scalar
multipoles.

The corresponding radial loading scales as

$$
g_r \sim \partial_r \eta
\sim
\frac{1}{r^2},
\frac{1}{r^3},
\frac{1}{r^4},
\ldots
$$

and the circular-balance contribution of each finite compact multipole scales
as

$$
v_\phi^2
=
r\,g_r
\sim
\frac{1}{r},
\frac{1}{r^2},
\frac{1}{r^3},
\ldots
$$

So a neglected compact multipole tail can modify the angular structure of the
field, but it cannot sustain a flat outer curve. Every such term decays too
quickly.

A flat regime requires instead

$$
v_\phi(R)\approx v_f=\text{const.},
$$

so the required inward loading is

$$
g_R(R)\approx \frac{v_f^2}{R},
$$

which corresponds to a logarithmic effective scalar, not to any finite compact
scalar multipole tail.

That is why the galactic dark-matter effect should not be read here as the sum
of neglected higher terms in the scalar mass expansion of chapter 12. The
missing object is tensorial rather than scalar: the surviving azimuthal second
moment of organized transport. It enters through the stress tensor and its
cylindrical divergence, not as a scalar quadrupole correction to the monopole
field.


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

This is the coarse-grained form of the packet statement above: each unresolved
azimuthal transport element contributes its local energy density to the
azimuthal second moment, and those contributions add.

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


## 6. A built-in stress envelope

The same mechanism already supplies a lower and upper bound on what this
channel can explain. The derivation is step by step.

First, return to the exact radial balance from section 3:

$$
\rho\,\frac{v_\phi^2}{R}
=
-\partial_R \Sigma_{RR}
-
\frac{\Sigma_{RR}-\Sigma_{\phi\phi}}{R}
-
\partial_z \Sigma_{Rz}.
$$

Multiply by $R/\rho$ and regroup the terms:

$$
v_\phi^2
=
\left(
-\frac{R}{\rho}\partial_R \Sigma_{RR}
-\frac{\Sigma_{RR}}{\rho}
-\frac{R}{\rho}\partial_z \Sigma_{Rz}
\right)
+
\frac{\Sigma_{\phi\phi}}{\rho}.
$$

Define the non-azimuthal baseline by

$$
v_{\mathrm{base}}^2
:=
-\frac{R}{\rho}\partial_R \Sigma_{RR}
-\frac{\Sigma_{RR}}{\rho}
-\frac{R}{\rho}\partial_z \Sigma_{Rz}.
$$

Then the circular speed splits exactly as

$$
\boxed{
v_\phi^2 = v_{\mathrm{base}}^2 + \frac{\Sigma_{\phi\phi}}{\rho}.
}
$$

This is the key structural point. The full observed radial load

$$
\frac{v_\phi^2}{R}
$$

is not partly outside the stress description. It is exactly what the stress
tensor accounts for once all contributing terms are retained. The azimuthal
term is an additional surviving part of that same tensorial load, not a second
force laid on top from elsewhere.

So the excess above the non-azimuthal baseline is

$$
\boxed{
\Delta v_\phi^2
:=
v_\phi^2-v_{\mathrm{base}}^2
=
\frac{\Sigma_{\phi\phi}}{\rho}.
}
$$

Second, bound $\Sigma_{\phi\phi}$ from the unresolved transport itself. Inside
the same narrow-packet coarse-graining already used in section 5, resolve the
local unresolved transport into elements labeled by $a$, with local energy
densities $u_a$ and unit directions $\hat{\mathbf n}_a$. For each element, the
packet result gives the local momentum-flux tensor

$$
\mathbf Q^{(a)} \approx u_a\,\hat{\mathbf n}_a\otimes\hat{\mathbf n}_a.
$$

Its azimuthal component is therefore

$$
Q^{(a)}_{\phi\phi}
\approx
u_a\,(\hat{\mathbf n}_a\cdot\hat{\mathbf e}_\phi)^2.
$$

Coarse-graining over all unresolved elements gives

$$
\Sigma_{\phi\phi}
\approx
\sum_a u_a\,(\hat{\mathbf n}_a\cdot\hat{\mathbf e}_\phi)^2.
$$

Now

$$
0\le (\hat{\mathbf n}_a\cdot\hat{\mathbf e}_\phi)^2 \le 1
$$

for every element, so summing yields

$$
0
\le
\Sigma_{\phi\phi}
\le
\sum_a u_a.
$$

But the local coarse-grained energy density is just

$$
u=\sum_a u_a,
$$

so

$$
\boxed{
0\le \Sigma_{\phi\phi}\le u.
}
$$

Equivalently, the azimuthal fraction obeys

$$
\boxed{
0\le f:=\frac{\Sigma_{\phi\phi}}{u}\le 1.
}
$$

Third, convert that stress bound into a velocity-squared bound. Inside the same
constitutive class,

$$
\rho=\frac{u}{k^2},
\qquad
k=\frac{1}{\sqrt{\varepsilon\mu}}.
$$

Therefore

$$
0\le \frac{\Sigma_{\phi\phi}}{\rho}\le \frac{u}{\rho}=k^2,
$$

that is,

$$
\boxed{
0\le \Delta v_\phi^2 = \frac{\Sigma_{\phi\phi}}{\rho}\le k^2.
}
$$

This is the envelope expression.

If one uses an observational baryonic baseline $v_{\mathrm{bar}}^2$ to
represent the same non-azimuthal contribution, then the observable excess

$$
\Delta v_\phi^2:=v_{\mathrm{obs}}^2-v_{\mathrm{bar}}^2
$$

should satisfy the same envelope:

$$
\boxed{
0\le \Delta v_\phi^2 \le k^2.
}
$$

So the structural test is immediate. If the galactic dark-matter cases really
come from this azimuthal-stress channel, they should fall inside that
envelope. A case requiring

$$
\Delta v_\phi^2 > k^2
$$

would lie outside the capacity of this mechanism.


### 6.1. Coherent interaction term from aligned baryonic closures

The envelope above only bounds what the azimuthal-stress channel can supply.
To connect that bound directly to the coherent-overlap logic of the
self-refraction chapters, now write the interaction term as an averaged product
term.

Let the resolved co-rotating baryonic families be labeled by $I$, with local
positive azimuthal amplitudes

$$
A_I(R,z)\ge 0.
$$

Choose local oscillatory representatives

$$
f_I(t;R,z)
:=
\sqrt{2}\,A_I(R,z)\cos\bigl(\omega t+\phi_I(R,z)\bigr).
$$

Then each family contributes the diagonal average

$$
\langle f_I^2\rangle = A_I^2.
$$

Therefore the time-averaged square of the summed local family field is

$$
\left\langle \left(\sum_I f_I\right)^2 \right\rangle
=
\sum_I A_I^2
+
2\sum_{I<J}A_IA_J\,C_{IJ},
$$

where the pair correlators are

$$
C_{IJ}(R,z)
:=
\left\langle \cos\bigl(\phi_I-\phi_J\bigr)\right\rangle.
$$

This is the exact averaged-product form of the coherent interaction term. The
ordinary baryonic addition keeps only the diagonal piece and drops the positive
product term.

The local `4u` result is the two-family maximal case of this same formula. If

$$
A_1=A_2=\sqrt{u},
\qquad
C_{12}=1,
$$

then

$$
\left\langle (f_1+f_2)^2\right\rangle
=
u+u+2u
=
4u.
$$

So the galactic interaction term is the coarse-grained many-family descendant
of the same coherent-overlap rule.

Now define the diagonal family energy content by

$$
U_I:=A_I^2.
$$

The ordinary baryonic baseline then keeps only the diagonal contribution:

$$
V_N^2=\sum_I U_I=\sum_I A_I^2.
$$

If the resolved families contribute coherently to the aligned azimuthal second
moment, the corresponding coarse-grained energy-flow curve is

$$
V_{\mathrm{EF}}^2
=
V_N^2
+
2\sum_{I<J}A_IA_J\,C_{IJ}.
$$

In the constructive aligned sector,

$$
0\le C_{IJ}\le 1.
$$

So the coherent excess above the diagonal baryonic baseline is

$$
\Delta v_{\mathrm{coh}}^2
\approx
2\sum_{I<J}A_IA_J\,C_{IJ}.
$$

Because each correlator lies between zero and one, the resolved-family
coherent term obeys the exact coarse bounds

$$
\boxed{
0
\le
\Delta v_{\mathrm{coh}}^2
\le
2\sum_{I<J}A_IA_J.
}
$$

Equivalently,

$$
\boxed{
V_N^2
\le
V_{\mathrm{EF}}^2
\le
\left(\sum_I A_I\right)^2.
}
$$

So the diagonal Newtonian curve is the lower bound, while the fully coherent
resolved-family sum is the upper bound. No detailed knot shape is needed for
this step. The local `4u` principle enters in exactly the right place: it is
the maximal two-family value of the same averaged product term.

For the resolved SPARC families gas, disk, and bulge, take

$$
A_g:=\sqrt{\max(V_g|V_g|,0)},
\qquad
A_d:=\sqrt{\Upsilon_d}\,V_d,
\qquad
A_b:=\sqrt{\Upsilon_b}\,V_b,
$$

with the SPARC fiducial values

$$
\Upsilon_d=0.5,
\qquad
\Upsilon_b=0.7.
$$

Then the resolved-family correlator band becomes

$$
\boxed{
V_N^2(R)
\le
V_{\mathrm{EF}}^2(R)
\le
\bigl(A_g(R)+A_d(R)+A_b(R)\bigr)^2.
}
$$

and the maximum resolved coherent excess is

$$
\boxed{
\Delta v_{\mathrm{coh,max}}^2(R)
=
2\bigl(A_gA_d+A_gA_b+A_dA_b\bigr).
}
$$

If one compresses the three resolved pair correlators into a single effective
correlator

$$
C_{\mathrm{eff}}(R),
$$

then

$$
\boxed{
V_{\mathrm{EF}}^2(R)
=
V_N^2(R)
+
2\,C_{\mathrm{eff}}(R)\bigl(A_gA_d+A_gA_b+A_dA_b\bigr).
}
$$

and the observed galaxy defines the required effective correlator

$$
\boxed{
C_{\mathrm{req}}(R)
:=
\frac{v_{\mathrm{obs}}^2(R)-V_N^2(R)}
{2\bigl(A_gA_d+A_gA_b+A_dA_b\bigr)}.
}
$$

Whenever

$$
0\le C_{\mathrm{req}}(R)\le 1,
$$

the observed excess can be recovered inside the resolved gas-disk-bulge
correlator band alone. If instead

$$
C_{\mathrm{req}}(R)>1,
$$

then the resolved families undercount the full positive cross term, and finer
baryonic decomposition or additional unresolved baryonic families must still
contribute.

### 6.2. Internal winding channels lift the coarse resolved-family band

The previous band still treats each resolved visible family as though it were a
single coherent channel. That is too restrictive.

A visible family can itself contain several coherent winding sectors. Write

$$
A_I^2(R)=\sum_k A_{Ik}^2(R),
$$

where the index `k` labels the active winding channels carried by resolved
family `I`.

Then the full constructive energy-flow curve is

$$
V_{\mathrm{EF}}^2(R)
=
\sum_{I,k}A_{Ik}^2(R)
+
2\sum_{(I,k)<(J,\ell)}A_{Ik}(R)A_{J\ell}(R)\,C_{Ik,J\ell}(R).
$$

This matters for two reasons.

First, same-family coherent products now appear automatically through the terms
with fixed `I` and different winding labels `k\neq \ell`. So the coarse
resolved-family denominator no longer collapses merely because only one visible
family dominates at some radius.

Second, the visible coarse amplitudes still control the constructive envelope.
By Cauchy,

$$
\sum_k A_{Ik}(R)
\le
\sqrt{N_I(R)}\,A_I(R),
$$

where `N_I(R)` is the number of active winding channels carried by resolved
family `I` at that radius.

Therefore

$$
V_{\mathrm{EF}}^2(R)
\le
\left(\sum_I\sum_k A_{Ik}(R)\right)^2
\le
\left(\sum_I \sqrt{N_I(R)}\,A_I(R)\right)^2.
$$

If one common ceiling `N_\ast(R)` bounds the active winding multiplicity of the
visible families,

$$
N_I(R)\le N_\ast(R)
\qquad
\text{for all }I,
$$

then

$$
\boxed{
V_{\mathrm{EF}}^2(R)
\le
N_\ast(R)\bigl(A_g(R)+A_d(R)+A_b(R)\bigr)^2.
}
$$

This is the rigorous winding-channel lift of the coarse baryonic ceiling.

The coarse resolved-family band corresponds to

$$
N_\ast=1.
$$

If each visible family carries at most one dominant conjugate pair, for
example `(m,n)` together with `(n,m)`, then

$$
N_\ast=2,
$$

and the constructive ceiling becomes

$$
\boxed{
V_{\mathrm{EF}}^2(R)
\le
2\bigl(A_g(R)+A_d(R)+A_b(R)\bigr)^2.
}
$$

So a preferred conjugate winding pair does not merely change interpretation. It
strictly raises the admissible baryonic ceiling and restores same-family
coherent products that the coarse resolved-family formula omits.

The observed galaxy then defines the required common winding ceiling

$$
\boxed{
N_{\ast,\mathrm{req}}(R)
:=
\frac{v_{\mathrm{obs}}^2(R)}
\bigl(A_g(R)+A_d(R)+A_b(R)\bigr)^2.
}
$$

Whenever

$$
N_{\ast,\mathrm{req}}(R)\le 1,
$$

the observed point lies inside the coarse one-channel ceiling. Whenever

$$
1 < N_{\ast,\mathrm{req}}(R)\le 2,
$$

a single dominant conjugate pair per visible family is enough. If instead

$$
N_{\ast,\mathrm{req}}(R)>2,
$$

then even that is not enough, and more active winding sectors, finer baryonic
decomposition, or additional unresolved baryonic families must still
contribute.


### 6.3. What the observations give, and what the ontology changes

Nothing in this argument rejects the astronomical observations themselves.

The observations give resolved baryonic organization:

- surface-brightness profiles,
- colors and spectra,
- gas tracers,
- and the rotation field.

What standard practice then does is reduce that observed organization to a
scalar baryonic mass profile and assume that this scalar profile is the whole
dynamically relevant object.

In symbols, the usual ontological reduction is

$$
\text{observed baryonic light/tracers}
\;\longrightarrow\;
\rho_{\mathrm{bar}}(R)
\;\longrightarrow\;
\text{gravity from scalar mass alone}.
$$

This text keeps the observational first step but rejects the last reduction as
ontologically incomplete for an extended rotating galaxy.

The observed baryonic profile still gives the diagonal content:

$$
V_N^2(R)=\sum_I A_I^2(R).
$$

But the same observed baryonic organization can also carry a surviving
directional second moment, and that second moment contributes through the
correlator term

$$
\Delta v_{\mathrm{coh}}^2(R)
=
2\sum_{I<J}A_I(R)A_J(R)\,C_{IJ}(R).
$$

So the collective dynamical object recovered from the observations is not just
a scalar mass density. It is

$$
\text{diagonal baryonic content}
+
\text{surviving correlator/stress structure}.
$$

That is the ontological correction. The data are not discarded. What changes
is the dynamical reading of those data.

This is also why the galactic excess need not imply either additional unseen
matter or an error in the observed baryonic profile. It can arise because a
structured rotating baryonic system is being forced into a scalar-only
gravitational reading. In that misreading, the correlator/stress contribution
has nowhere to appear except as fictitious missing mass.


## 7. Flat curves

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


## 8. Why the standard dark-halo inference appears

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


## 9. Null-probe lensing from the same outer-disk regime

Adopt the same weak constitutive summary already recovered in the gravity
chapters for null probes:

$$
n=1+2\eta,
\qquad
k=\frac{c}{1+2\eta}.
$$

The slow radial load in the flat outer regime is

$$
a_R(R)=-\frac{v_f^2}{R}.
$$

Appendix 213 gives the slow-mode potential

$$
\Phi_k=-c^2\eta.
$$

Therefore the radial acceleration is

$$
a_R=-\partial_R\Phi_k=c^2\,\partial_R\eta_{\mathrm{gal}}.
$$

Substituting the flat-curve load gives

$$
\partial_R\eta_{\mathrm{gal}}=-\frac{v_f^2}{c^2R},
$$

so

$$
\boxed{
\eta_{\mathrm{gal}}(R)
=
\eta_0-\frac{v_f^2}{c^2}\ln\!\frac{R}{R_0},
}
$$

up to an irrelevant additive constant.

Therefore the corresponding refractive index is

$$
n(R)
=
1+2\eta_0-\frac{2v_f^2}{c^2}\ln\!\frac{R}{R_0}.
$$

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

The sign is inward. Using the same weak-ray law as chapter 12, the deflection
magnitude is

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
- and it is recovered without adding a dark halo once the galaxy is treated as
  a stress-supported disk rather than as a compact scalar monopole.


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
- the relation, if any, between this stress mechanism and the baryonic
  Tully-Fisher law,
- a direct derivation of the weak scalar $\eta_{\mathrm{gal}}$ from the full
  axisymmetric source stress, rather than inferring it from the slow-mode
  radial load,
- the non-ideal corrections from finite disk thickness, disk truncation,
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

So the completed galactic attraction must coincide with what is observed, and
in this framework that completed load is read as stress-tensor structure all
the way through: the non-azimuthal baseline plus the surviving azimuthal term.

Under the explicit outer-disk assumptions above,

$$
v_\phi^2 \approx \frac{\Sigma_{\phi\phi}}{\rho}\approx f\,k^2,
\qquad
\Delta\alpha \approx \frac{2\pi v_f^2}{c^2},
$$

so a slowly varying azimuthal transport fraction produces a flat rotation
curve, and the same weak constitutive summary yields the matching
logarithmic-regime lensing strength.

At that level, the missing mass is not missing matter. It is missing stress.
