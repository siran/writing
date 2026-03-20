---
title: The Physics of Energy Flow - Charge as Circulation
date: 2026-03-11
---


# 10. Charge as Circulation

Chapter 8 established that self-refracting flow can close on itself, and that
the simplest closed shape it can take is toroidal — a sphere with a
through-hole. The resulting closure has two independent non-contractible
cycles, two integer winding numbers $(m,n)$, and discrete standing-wave
frequencies. That chapter used the toroidal closure to account for discrete
energy levels and Rydberg-type scaling.

The same mode carries global aspects that chapter 8 did not yet name.
The most immediate is the through-hole flux threading the aperture. This
chapter names it, derives its $1/r^2$ exterior scaling, and shows it is
conserved by topology alone.

In source-free Maxwell dynamics, $\nabla \cdot \mathbf{E} = 0$ everywhere.
No electric field lines originate or terminate. Yet we observe a $1/r^2$
falloff in field intensity around what we call a "charged particle."

There is no contradiction. The toroidal mode of chapter 8, with winding
numbers $(m,n)$ characterizing the closed flow, carries a conserved
through-hole flux.

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
continuation we are measuring. Its sign and class are fixed by the discrete
closed circulation before any force law is written.

So the behavior classically attributed to an electric source is already
present inside the source-free theory once structured electromagnetic
configurations are admitted. If one prefers the later sourced Maxwell
notation, that source term is read here as an idealized summary of the same
toroidal closure, not as its primitive origin.


## Conservation of charge

The winding numbers $(m,n)$ that fix the through-hole flux class are
topological invariants. They count how many times the circulation wraps each
cycle of the torus. Continuous evolution cannot change an integer winding
count without the field passing through zero — a phase slip that would
require the toroidal mode to momentarily vanish at a point.

In source-free Maxwell dynamics, such a discontinuity cannot occur under
smooth evolution: the transport law is linear, the field is regular, and no
mechanism exists to force a zero crossing from within the source-free sector.
The winding class is therefore rigid under continuous source-free dynamics.

Charge conservation is thus not a separate axiom. It is a corollary of
topological rigidity: the same feature of the transport law that forces
integer quantization of the mode also prevents its class from changing.


## What remains

Charge is fully accounted for here: it is the exterior reading of a
conserved topological winding class, quantized by closure, conserved by
topological rigidity, scaling as $1/r^2$ by the spreading of non-contractible
$\mathbf{G}$-tubes in the non-simply-connected exterior.

The $(m,n)$ winding also encodes an orientational character — a handedness.
What we call spin is presumably this orientational structure, but the present
framework does not yet derive it. Applying the classical angular momentum
integral $\mathbf{L} = (1/c^2)\int \mathbf{r}\times\mathbf{F}\,dV$ to the
toroidal mode would import a mechanical formula rather than derive an
emergence. A proper account of spin from energy flow requires showing how the
rotating mode's intrinsic angular momentum per unit energy falls out of the
wave structure itself — the same way charge fell out of the winding topology.
That derivation belongs elsewhere.

Mass is similarly not introduced here. It is the total trapped energy of the
mode, $E/c^2$, developed in the preceding chapters.

Charge, spin, and mass are three independent characterizations of the toroidal
mode: a topological class, an orientational structure, and a scalar amplitude.
The interaction between charged configurations — momentum transfer across the
boundary between two toroidal modes — is the subject of the next chapter.
