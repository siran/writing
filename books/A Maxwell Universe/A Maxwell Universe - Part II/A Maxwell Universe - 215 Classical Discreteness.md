---
title: A Maxwell Universe – Classical Discreteness
date: 2025-12-31 18:04
---


## Sunlight

One of the greatest achievements of early quantum theory was predicting the
*discrete* energy levels of the hydrogen atom, known as the *Rydberg series*.

In 1704 Isaac Newton showed, using a prism, that all the colors of the rainbow
are contained in sunlight.

When doing the same experiment with a neon light, for example, or with hydrogen
-the most abundant element in the known universe- is it easily seen that neither
neon light nor hydrogen light contain all the colors as apparently did sunlight.

These very specific colors emitted by excited atoms constitute "the spectrum" of
the atom.


## Color is Energy

Here, color is not a representation of energy — it *is* energy, directly
perceived as visible light color; also called "electromagnetic frequency". If we
examine closely (not even too closely, naked eye is enough) the spectrum of
sunlight, it is readily evident that it is not "continuous", and that there are
gaps in the visible spectrum of light. These gaps in the spectrum, seen as
discrete integer numbers, is what gave rise to "quantum mechanics" that could
explain, with astonishg detail, many "discrete" features not explained by
classical "continuos" theories, like electromagnetism.

These "gaps" in the full spectrum of sunlight tell us what is the composition of
the sun, as every element has its particular "spectral signature".


## The Rydberg Series

Long before the internal structure of the atom was understood, experiments (like
the prism experiment done by Newton) showed that glowing hydrogen does not emit
a continuous rainbow of light. Instead, it emits light only at very specific,
sharply defined colors. These colors tell us the "energy levels" of the atom.

In 1888, a swedish physicist, Johannes Rydberg found that these colors —that is,
electromagnetic frequencies- follow a simple mathematical pattern involving
integers $n = 1, 2, 3, \dots$:

$$
E_n \propto \frac{1}{n^2}.
$$

In this context, energy is not an abstract quantity. It is what is directly
observed as color. Discreteness in energy is discreteness in color.

The standard explanation, developed in [] by Bohr and later Schrödinger, ties
this scaling to the electrostatic interaction between an electron and a proton
(the only known "components" of the hydrogen atom), reminiscent of a planetary
view. In this picture, larger $n$ corresponds to the electron being more excited
and thus occupying a higher orbit farther from the nucleus.

However, the formula itself contains no reference to distance, radius, or
geometry —only to the integer $n$.

More precisely, observed spectral lines correspond not to absolute energies
$E_n$, but to transitions between configurations. The emitted radiation carries
the energy difference:

$$
\Delta E \propto \frac{1}{m^2}-\frac{1}{n^2},
\qquad m>n.
$$


## The Geometry of Quantization

We interpret the $1/n^2$ factor not as a change in spatial size, but as a
reorganization of a fixed total energy into progressively finer internal
structure.

Imagine a flat rectangular sheet of paper. Draw one vertical line and one
horizontal line, each connecting opposite edges. They cross in the middle and
divide the sheet into $2\times2=4$ cells.

More generally, if we keep adding lines the sheet is then partitioned into

$$
n\times n = n^2
\text{ cells}.
$$

With no internal lines, the sheet corresponds to a ground configuration with
energy $E_1$.

As $n$ increases, the total area stays the same, but it is
subdivided into smaller and smaller regions.

If the total energy is conserved and distributed uniformly across the $n^2$
cells, the energy per cell scales as

$$
E_n \propto \frac{E_1}{n^2}.
$$

In this abstract but constrained way, the Rydberg scaling appears without
invoking particles, wavefunctions, operators, or force balance. Discrete levels
are simply discrete global subdivisions of a conserved quantity: energy.

The inverse-square law is therefore not accidental. It is the generic signature
of two independent closure counts acting on a conserved configuration.


## The Torus

To understand the physical basis of this grid, we must look at the topology of
confinement.

Return to the flat napkin. First, identify and glue together one pair of
opposite edges. The flat napkin becomes a tube. Lines that originally ended on
one edge now reappear continuously on the opposite edge.

<image>

Next, take this tube and identify its two circular ends. Gluing these ends
together produces a closed surface with no boundary—a **Torus**.

<image>

Any lines drawn on the original napkin become closed paths on the torus.
However, they form closed loops only if they match their own position when
crossing an identified edge. This requirement ensures global continuity of the
grid.

In a source-free Maxwell universe, electromagnetic fields on this surface must
satisfy these continuity conditions along the two independent cycles of the
torus: along the axis of the tube and around the ring.

This imposes a discretization condition on the wavelength. Along a closed loop
of length $L$, the field must satisfy:

$$
n \lambda = L.
$$

These are the same conditions that produce standing waves on a string, now
applied to a closed surface with two independent winding numbers.


## Energy Reorganization

In this view, the Rydberg series does not describe an electron moving to a
larger orbit in space. It describes the electromagnetic field reorganizing
itself into progressively finer standing-wave patterns.

These patterns are self-consistent knots of counter-propagating electromagnetic
energy flux, fixed by continuity rather than force balance.

Increasing $n$ corresponds to increasing the number of global windings on the
surface. More windings impose more nodes on the same conserved topology.

Transitions between levels are therefore related to the difference in **cell
sizes** (or effective tube widths) between two subdivisions. To move from level
$n$ to level $m$, the system must supply exactly the energy difference required
to "patch" the geometry from one tube width to another:

$$
\Delta E = E_1 \left( \frac{1}{n^2} - \frac{1}{m^2} \right).
$$

The photon is the packet of energy that facilitates this topological patching.

The ground state ($n=1$) is unique. It represents the configuration where the
torus is composed of a single coherent cell—the state where the flux tube is
pulled as tight as topologically possible. As we shall see, the geometric limit
of this "tightness" is what determines the coupling constant of the universe.


## Charge as Topology

Finally, we must account for the appearance of electric charge. In a source-free
universe,

$$
\nabla \cdot \mathbf{E} = 0
$$

everywhere. No electric field originates from a point. How, then, does a
particle appear to have charge?

Consider the standing wave on the torus. The field lines wrap around the two
independent cycles, characterized by the winding numbers $(m,n)$. These
windings represent closed circulations of electromagnetic energy.

<image>

At any local patch of the surface, the field lines entering and leaving balance
so that the net flux vanishes. However, the global circulation does not vanish.
The pair $(m,n)$ characterizes a vortex-like flow of energy along the two
directions of the torus.

Now, enclose this configuration within a spherical surface of radius $r$ much
larger than the torus itself.

The total electromagnetic circulation (the "topological charge") is a conserved
quantity fixed by the winding numbers. As this fixed quantity is projected
through a sphere whose area grows as $4\pi r^2$, the observed field intensity
necessarily falls off as:

$$
\text{Intensity} \propto \frac{1}{r^2}.
$$

This reproduces the phenomenology of charge.

In this view, charge is not a primitive substance added to the universe. It is
an effective, topological quantity: the far-field signature of closed
electromagnetic circulation. What we measure as Coulomb force is simply the
geometric dilution of this conserved topology over distance.


## Matter

In this framework, matter is not a substrate distinct from the field.

Matter is a self-sustained electromagnetic field configuration whose internal
couplings generate delayed response, confinement, and stability.

As we shall see, all effective material properties—mass, charge, inertia, and
spectral structure—are emergent consequences of source-free Maxwell dynamics in
a Maxwell Universe.
