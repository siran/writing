---
title: The Physics of Energy Flow - Charge as Circulation
date: 2026-03-11
---


# 10. Charge as Circulation

Electric charge is the exterior reading of conserved topological
winding: the torus's $(m,n)$ circulation sustains a divergence-free
exterior continuation that appears on growing enclosing shells as
matched inward and outward normal-to-shell currents whose magnitude
falls as $1/r^2$.

In source-free Maxwell dynamics, $\nabla \cdot \mathbf{E} = 0$ everywhere.
No electric field lines originate or terminate. Yet we observe a $1/r^2$
falloff in field intensity around what we call a "charged particle."

There is no contradiction. Consider a toroidal energy configuration with a
fixed total circulation, with winding numbers $(m, n)$ characterizing the
closed flow. The total is conserved.

A torus has a distinguished aperture. Choose a spanning surface $\Sigma$
across that aperture. The closed circulation carries a signed through-hole
flux

$$
\Phi_\Sigma=\int_\Sigma \mathbf{S}\cdot d\mathbf{A}.
$$

This is not a source or sink. It is the oriented through-hole moment of the
closed circulation. Its sign reverses with handedness.

Because the circulation closes in integer winding classes, this through-hole
flux is not arbitrary. For a stable toroidal mode it comes in discrete classes
set by the winding itself.

To see how the exterior continuation acquires inverse-square scaling, take a
small open patch of the torus surface and follow the nested open patches
generated outward from it. The local $(m,n)$ transport is tangential on the
torus patch, so on every such patch Stokes' theorem gives

$$
\int_{\Sigma_r} (\nabla \times \mathbf{F})\cdot \mathbf{n}\, dA
=
\oint_{\partial \Sigma_r} \mathbf{F}\cdot d\mathbf{l}.
$$

This ties the normal continuation on the patch directly to the tangential
circulation. Now let

$$
\mathbf G:=\nabla\times\mathbf F.
$$

Since

$$
\nabla\cdot\mathbf G=\nabla\cdot(\nabla\times\mathbf F)=0,
$$

the normal continuation itself is divergence-free. Build a thin tube between
two corresponding open patches $\Sigma_{r_1}$ and $\Sigma_{r_2}$, with side
walls everywhere tangent to $\mathbf G$. The divergence theorem then gives

$$
\int_{\Sigma_{r_2}} \mathbf G\cdot \mathbf n\, dA
-
\int_{\Sigma_{r_1}} \mathbf G\cdot \mathbf n\, dA
=
0.
$$

So the same winding sector carries the same signed normal continuation as it is
taken outward. Denote that sector strength by

$$
J_\perp:=\int_{\Sigma_r} \mathbf G\cdot \mathbf n\, dA.
$$

On large enclosing shells, corresponding patches scale like

$$
A(\Sigma_r)\propto r^2.
$$

So the shell-normal continuation carried by that sector must scale as

$$
|j_\perp(r)| \propto \frac{|J_\perp|}{A(\Sigma_r)} \propto \frac{1}{r^2}.
$$

Across a full closed shell these sectors occur in matched inward and outward
patches, so the signed total still balances to zero. But the magnitude of each
normal-to-shell sector falls as $1/r^2$.

This yields the inverse-square far-field scaling without any primitive source.
Charge is the name we give to the conserved oriented quantity whose exterior
continuation we are measuring. In this sense, charge is quantized before any
force law is written: its sign and class are fixed by the discrete closed
circulation.
So the behavior classically attributed to an electric source is already
present inside the source-free theory once structured electromagnetic
configurations are admitted.

If one prefers the later sourced Maxwell notation, that source term can be
read here as an idealized or effective summary of the same toroidal closure,
not as the primitive origin of the field.

Within a toroidal mode, charge and spin are read from the same closure but
from different global quantities. Charge measures the signed through-hole
flux, while spin measures the angular momentum of the closed circulation about
the mode's center.

Opposite charge signs correspond to opposite senses of winding, equivalently to
opposite signs of the through-hole flux. The present chapter identifies the
geometric far-field character of charge. The detailed interaction between such
configurations belongs later, when momentum transfer and flux accounting are
made explicit.
