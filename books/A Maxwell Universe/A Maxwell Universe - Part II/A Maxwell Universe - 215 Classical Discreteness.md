---
title: A Maxwell Universe – Classical Discreteness
date: 2025-12-31 18:04
---


## Sunlight

One of the greatest achievements of early quantum theory was predicting the
*discrete* energy levels of the hydrogen atom, known as the *Rydberg series*.

In 1704, Isaac Newton demonstrated, using a prism, that all the colors of the
rainbow are contained in sunlight. However, if one performs the same experiment
with a neon light, or with hydrogen—the most abundant element in the known
universe—it becomes readily evident that they do not emit a continuous spectrum.

Instead, they emit light only at very specific, sharply defined colors. These
gaps in the spectrum constitute the "spectral signature" of the element.


## Color is Energy

In this context, color is not merely a representation of energy—it *is* energy,
directly perceived as frequency. The discreteness of these colors was the
anomaly that gave rise to quantum mechanics, as classical electromagnetism (in
its continuous form) seemingly offered no explanation for why an atom should
radiate in steps rather than in a sweep.


## The Rydberg Series

Long before the internal structure of the atom was understood, the Swedish
physicist Johannes Rydberg (1888) found that these frequencies follow a simple
mathematical pattern involving integers $n = 1, 2, 3, \dots$:

$$
E_n \propto \frac{1}{n^2}.
$$

The standard explanation, developed later by Bohr and Schrödinger, ties this
scaling to the electrostatic interaction between an electron and a proton. In
that planetary picture, larger $n$ corresponds to the electron occupying an
orbit farther from the nucleus.

However, the formula itself contains no reference to distance, radius, or
geometry—only to the integer $n$.

More precisely, observed spectral lines correspond to transitions between
configurations. The emitted radiation carries the exact energy difference:

$$
\Delta E \propto \frac{1}{m^2}-\frac{1}{n^2}, \qquad m>n.
$$


## The Geometry of Quantization

We can interpret the $1/n^2$ factor not as a change in spatial size, but as a
reorganization of fixed total energy into progressively finer internal
structure.

Imagine a flat rectangular sheet. Draw one vertical line and one horizontal
line, each connecting opposite edges. They cross in the center, dividing the
sheet into $2\times2=4$ cells.

More generally, if we keep adding lines the sheet is then partitioned into:

$$
n\times n = n^2 \text{ cells}.
$$

With no internal lines ($n=1$), the sheet corresponds to a ground configuration
with energy $E_1$. As $n$ increases, the total area remains constant, but it is
subdivided into smaller and smaller regions.

If the total energy is conserved and distributed uniformly across the $n^2$
cells, the energy density per unit cell scales as:

$$
E_n \propto \frac{E_1}{n^2}.
$$

In this constrained view, the Rydberg scaling appears without invoking
particles, wavefunctions, or force balance. Discrete levels are simply discrete
global subdivisions of a conserved quantity: energy.


## The Torus

To understand the physical basis of this grid, we must look at the topology of
confinement.

Return to the flat sheet. First, identify and glue together one pair of opposite
edges. The sheet becomes a tube. Lines that originally ended on one edge now
reappear continuously on the opposite edge.

Next, take this tube and identify its two circular ends. Gluing these ends
together produces a closed surface with no boundary—a **Torus**.



Any lines drawn on the original sheet become closed paths on the torus. However,
they form closed loops only if they match their own position when crossing an
identified edge. This requirement ensures global continuity.

In a source-free Maxwell universe, electromagnetic fields on this surface must
satisfy these continuity conditions along the two independent cycles of the
torus: the poloidal (around the ring) and toroidal (along the tube) directions.

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
energy flux, fixed by continuity.

Increasing $n$ corresponds to increasing the number of global windings on the
surface. More windings impose more nodes on the same conserved topology.

Transitions between levels are therefore related to the difference in **cell
sizes** (or effective tube widths) between two subdivisions. To move from level
$n$ to level $m$, the system must supply exactly the energy difference required
to "patch" the geometry from one winding density to another:

$$
\Delta E = E_1 \left( \frac{1}{n^2} - \frac{1}{m^2} \right).
$$

The photon is the packet of energy that facilitates this topological patching.

The ground state ($n=1$) is unique. It represents the configuration where the
flux tube is pulled as tight as topologically possible. As we shall see, the
geometric limit of this "tightness" is what determines the coupling constant of
the universe.


## Charge as Topology

Finally, we must account for the appearance of electric charge. In a source-free
universe, $\nabla \cdot \mathbf{E} = 0$ everywhere. No electric field originates
from a point. How, then, does a particle appear to have charge?

Consider the standing wave on the torus. The field lines wrap around the two
independent cycles, characterized by winding numbers $(m,n)$. These windings
represent closed circulations of electromagnetic energy.

At any local patch of the surface, the field lines entering and leaving balance
so that the net flux vanishes. However, the global circulation -for example,
circulation tangent to the surface- does not vanish.

Now, enclose this configuration within a spherical surface of radius $r$ much
larger than the torus itself.

The total electromagnetic circulation (the "topological charge, $(m,n)$") is a
conserved quantity fixed by the winding numbers $m$ and $n$. This energy,
thought as a bulb turned-off (no radiation, no point source), is constant; so we
can think that it's energy is spread evenly around it. This energy, spread
accross the area of the sensor we use to measure it (the eye is a sensory organ,
"a sensor", as well) is what we measure as a $1/r^2$ dependence.


As this fixed quantity is projected
through a sphere whose area grows as $4\pi r^2$, the observed field intensity
necessarily falls off as:

$$
\text{Intensity} \propto \frac{1}{r^2}.
$$

This reproduces the phenomenology of charge.

In this view, charge is not a primitive substance added to the universe. It is
an effective, topological quantity: the far-field signature of closed
electromagnetic circulation.
