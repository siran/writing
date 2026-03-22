---
title: The Physics of Energy Flow - Charge as Circulation
date: 2026-03-21
---

# 10. Charge as Circulation

Chapter 8 established that self-refracting flow can close on itself, and that
the simplest closed shape it can take is toroidal — a sphere with a through-hole
sustains continuous nowhere-vanishing tangential flow in two independent
directions, while a plain sphere does not. The resulting closure has two
independent non-contractible cycles, two integer winding numbers
$(m,n)$, and discrete standing-wave frequencies.

This chapter asks what this mode looks like from the outside.


## The organized shell

Take a small patch $\Sigma$ on the toroidal closure. Along the boundary
$\partial\Sigma$, the $(m,n)$ winding gives a nonzero tangential circulation
of the flow. Stokes' theorem then gives

$$
\oint_{\partial\Sigma}\mathbf{F}\cdot d\mathbf{l}
=
\int_{\Sigma}(\nabla\times\mathbf{F})\cdot\mathbf{n}\,dA.
$$

So the tangential $(m,n)$ circulation on the closure is not confined to the
surface itself. It is accompanied by a normal curl through the patch. This is
the local reason the organized toroidal flow has an exterior continuation.

Now choose two corresponding patches, $\Sigma_1$ and $\Sigma_2$, on two
neighboring enclosing shells, and connect their boundaries by a thin tube
whose sidewall is tangent to the continuation. For that tube volume $V$,

$$
\int_V \nabla\cdot(\nabla\times\mathbf{F})\,dV = 0,
$$

because the divergence of a curl vanishes identically. Since no component of
the continuation crosses the sidewall, the normal curl through the two end
patches must match:

$$
\int_{\Sigma_1}(\nabla\times\mathbf{F})\cdot\mathbf{n}\,dA
=
\int_{\Sigma_2}(\nabla\times\mathbf{F})\cdot\mathbf{n}\,dA.
$$

The same organized sector therefore continues from shell to shell without
primitive creation or loss. What changes outward is not the total organized
shell content, but the area across which it is distributed.

Let $E_{(m,n)}$ denote the total organized shell energy carried by that
continuation. On an enclosing shell at radius $r$, the isotropic shell reading
of that same organized total is spread over area $4\pi r^2$. Its shell density
is therefore

$$
\frac{E_{(m,n)}}{4\pi r^2} \propto \frac{1}{r^2}.
$$

This is what charge is: the exterior reading of the organized $(m,n)$
energy of the toroidal closure, distributed over shells of increasing area.


## Sign and quantization

The $(m,n)$ flow on the closure has a handedness — the circulation runs
one way or the other around each cycle. This handedness is the sign of the
charge: a global orientation of the $(m,n)$ flow on the shells,
readable on any enclosing shell, not a local property of the torus surface.

The winding numbers are integers. The charge class is therefore discrete and
does not take arbitrary values. The torus is the simplest topological example of
a self-sustaining closure, but topology admits more complex configurations —
trefoils and other knotted closures — each carrying its own winding class. Which
configuration corresponds to the minimum stable self-sustaining mode, and
therefore to elementary charge, is not determined at this level of analysis.

Whether same-sign closures repel and opposite-sign closures attract is not
established here. It requires deriving the interaction law between two such
organized shell readings — the task of the next chapter.


## Net chirality is required

A toroidal geometry alone does not guarantee a net charge or magnetic moment.
Counter-propagating windings — equal $(m,n)$ and $(-m,-n)$ flows on the same
toroid — carry energy but cancel both the net handedness and the net axial
flux. Such a closure has $Q = 0$ and $\boldsymbol{\mu} = 0$: it contributes
to gravity (its scalar energy remains) but carries no charge and no magnetic
moment. Net charge and net axial flux both require a net chiral winding —
a definite excess of one handedness over the other.


## The axial through-hole flux is magnetic

Separately from the shell energy picture, the toroidal closure has a
distinguished aperture. The through-hole carries an oriented axial flux — a
directed quantity set by the winding before any exterior measurement is made.
This axial flux is the magnetic moment of the closure: oriented along the hole
axis, reversing sign with handedness.

It is not charge. The shell energy density is isotropic on enclosing shells. The
axial flux is not — it is directed along the hole axis. These are two
independent exterior properties of the same mode: the organized shell energy
(charge) and the axial through-hole structure (magnetic moment).


## What remains

Three things characterize the toroidal mode from the outside:

- **Charge**: the organized $(m,n)$ surface energy density on shells,
  $E_{(m,n)}/4\pi r^2$, signed by circulation handedness, quantized by integer
  winding.
- **Magnetic moment**: the axial through-hole flux, oriented along the hole
  axis, independent of the shell energy reading.
- **Mass**: the scalar amplitude $E/c^2$ of total closure energy. For a
  single toroid this is small. For large aggregates of toroids with random
  orientations, the $(m,n)$ structure averages out and what remains is
  the unstructured scalar energy $NE/c^2$ spread isotropically over
  shells — also $1/r^2$, unsigned, always attractive. That is gravity.


The primary interaction between two simple toroidal closures is through their
charge shells — the organized $(m,n)$ energy densities meeting across
the exterior. The next chapter derives Coulomb's law from the signed shell
potential of two such modes.
