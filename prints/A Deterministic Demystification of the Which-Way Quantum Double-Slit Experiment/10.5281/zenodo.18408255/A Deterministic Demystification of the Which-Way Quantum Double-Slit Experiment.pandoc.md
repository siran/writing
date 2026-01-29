---
title: A Deterministic Demystification of the Which-Way Quantum Double-Slit Experiment
subtitle: From Unitary Propagation to Interference Suppression
author: Maria Hart, An M. Rodriguez
date: 2026-01-28
one-sentence-summary: Which-way detection alters double-slit interference deterministically through interaction-induced phase evolution, without collapse, observers, or stochastic dynamics.
summary: >
  We present a first-principles, deterministic account of the quantum
  double-slit experiment with which-way detectors. Detectors are modeled as physical
  circuits possessing energetic barriers and therefore necessarily introduce localized
  interaction potentials. These interactions modify the action of electron paths and
  rotate the relative phase of each path. The continuous transition from interference to its
  suppression follows solely from unitary propagation. All probabilistic outcomes arise
  only from the quadratic mapping of the propagated state after propagation.
keywords:
  - quantum mechanics
  - double-slit experiment
  - which-way detection
  - determinism
  - propagator
  - path integral
  - phase evolution
doi: https://writing.preferredframe.com/doi/10.5281/zenodo.18408255
---

**One-Sentence Summary.** Which-way detection alters double-slit interference deterministically through interaction-induced phase evolution, without collapse, observers, or stochastic dynamics.

**Abstract.** We present a first-principles, deterministic account of the quantum double-slit experiment with which-way detectors. Detectors are modeled as physical circuits possessing energetic barriers and therefore necessarily introduce localized interaction potentials. These interactions modify the action of electron paths and rotate the relative phase of each path. The continuous transition from interference to its suppression follows solely from unitary propagation. All probabilistic outcomes arise only from the quadratic mapping of the propagated state after propagation.

**Keywords.** quantum mechanics, double-slit experiment, which-way detection, determinism, propagator, path integral, phase evolution

\begingroup
\setcounter{tocdepth}{1}
\renewcommand{\contentsname}{\centering Table of Contents}
\renewcommand{\numberline}[1]{#1.\hspace{0.6em}}
\setlength{\parskip}{0.35em}
\vspace{1.0\baselineskip}
\begin{center}\rule{0.35\linewidth}{0.4pt}\end{center}
\vspace{1.1\baselineskip}
\tableofcontents
\endgroup

```{=html}
<div class="toc">
<hr class="toc-divider" />
<div class="toc-title">Table of Contents</div>
<ul>
<li><a href="#determinism-in-quantum-dynamics">Determinism in Quantum Dynamics</a>
</li>
<li><a href="#the-double-slit-without-detectors">The Double-Slit **Without Detectors**</a>
</li>
<li><a href="#modeling-the-detector-as-a-circuit">Modeling the Detector as a Circuit</a>
</li>
<li><a href="#the-double-slit-with-detectors">The Double-Slit **With** Detectors</a>
</li>
<li><a href="#phase-evolution-induced-by-the-detector">Phase Evolution Induced by the Detector</a>
</li>
<li><a href="#continuous-suppression-of-interference">Continuous Suppression of Interference</a>
</li>
<li><a href="#no-measurement-postulate-required">No Measurement Postulate Required</a>
</li>
<li><a href="#conclusion">Conclusion</a>
</li>
<li><a href="#references">References</a>
</li>
</ul>
</div>
```


```{=latex}
\vspace{1.0\baselineskip}
\begin{center}\rule{0.35\linewidth}{0.4pt}\end{center}
\vspace{1.0\baselineskip}
```

```{=html}
<hr class="meta-divider" style="width:35%; margin:2rem auto; border:0; height:1px; background: rgba(0,0,0,0.35);" />
```

## Determinism in Quantum Dynamics

Quantum mechanics is probabilistic only at the level of outcome statistics. The
dynamical evolution of the quantum state, as governed by the Schrödinger
equation, is deterministic. This statement is independent of interpretational
preferences and concerns only the propagation of the quantum state.

Determinism of *evolution* is not a question.

The *evolution* of a quantum state $\psi(q,t)$ is governed
deterministically by the Schrödinger equation

$$
i\hbar \frac{\partial \psi}{\partial t}
=
\left(
-\frac{\hbar^2}{2m}\nabla^2 + \sum_{i} V_i(q,t)
\right)\psi
$$

This evolution is fully determined by the Hamiltonian —comprising the kinetic
term and the interaction potentials $V_i(q,t)$— together with the quantum
state $\psi$. No other consideration is necessary at the level of
propagation to calculate the probabilities at the screen.

In the present context, the Hamiltonian is not an independent or abstract
object. It is a compact representation of the interaction structure of the
system. All terms in the Hamiltonian arise from physical interactions between
the electron and its environment (including the detectors as part of the
environment).

In the absence of detectors, the Hamiltonian reduces to free propagation or to
interaction potentials common to all paths, which do not affect relative phases.

When detectors are present, additional slit-dependent interaction potentials are
introduced, modifying the Hamiltonian accordingly.


### The all-paths integral and *the propagator*

An equivalent formulation is provided by *the propagator*. The wavefunction at a
spacetime point $(x,T)$ is obtained by the action of the propagator on
the initial state,

$$
\psi(x,T)
=
\int dx_0\; K(x,T;x_0,0)\,\psi(x_0,0),
$$

where the propagator, $K$, is given by the path integral

$$
K(x,T;x_0,0)
=
\int_{q(0)=x_0}^{q(T)=x}\mathcal Dq\;
\exp\!\left(\frac{i}{\hbar}S[q]\right)
$$

with action

$$
S[q]=\int_0^T dt\left(\tfrac12 m\dot q^2 - \sum_i V_i(q,t)\right)
$$

The propagator contains the full dynamical content of the theory; all
interaction effects enter through its phase. Quantum mechanics is deterministic
at the level of propagation; probabilities arise only from the quadratic map
applied to the propagated state,

$$
P(x,T)=|\psi(x,T)|^2
$$


## The Double-Slit **Without Detectors**

An electron *quantum wave*, $\psi$, propagates from a source to a
screen through two slits.

In the absence of detectors, the propagation is governed by a single propagator
$K_0$, corresponding to free propagation or to interaction potentials
common to all paths.

The wavefunction at the screen point $x$ is obtained by propagating
the initial state through the two available spatial channels, "left slit" and
"right slit",

$$
\psi(x)
=
\psi_\text{left}(x)+\psi_\text{right}(x)
$$

where

$$
\psi_j(x)
=
\int dx_0\; K_0^{(j)}(x,T;x_0,0)\,\psi(x_0,0),
\qquad j=\text{left},\text{right}.
$$

Here $K_0^{(j)}$ denotes the restriction of the propagator to trajectories
passing through slit $j$. In what follows, the slits are labeled by
$j=1,2,\dots$.

Since "by construction" there is no distinction is between the slits, the
propagator is identical for both path classes.

The probability density at the screen is therefore

$$
P(x)
=
|\psi(x)|^2
=
|\psi_1|^2
+
|\psi_2|^2
+
2\,\mathrm{Re}\!\left(\psi_1\psi_2^*\right).
$$

The interference term arises from coherent phase relations generated by the
common propagator acting on the two spatially distinct path families.


## Modeling the Detector as a Circuit

A detector is not an abstract “observer”. **It is a physical device**, a circuit
of some kind.

By definition, a detector:

- is a circuit with at least two metastable macroscopic states (“triggered” and
  “not triggered”);

- contains an energetic barrier separating those states;

- and therefore requires an energy transfer to cross that barrier and register a
  detection event.

Consequently, the presence of a detector near a slit necessarily introduces a
localized interaction between the electron and the detector’s activation
circuit, independent of whether a macroscopic click ultimately occurs.

From the electron’s perspective, a detector defines a spatial region
$\Omega_d$ in which the electron may interact with the detector through an
interaction potential $V_d$, capable of deterministically triggering
when an energetic threshold is crossed.

Within the region $\Omega_d$, the detector is capable of coupling to the
particle and contributing an interaction term to the action. This interaction
produces an energetic imprint in the phase of the propagated wavefunction and
therefore affects the probability density $|\psi|^2$, regardless of the
final macroscopic state of the detector.


## The Double-Slit **With** Detectors

When detectors are placed near the slits, the electron propagates in the
presence of an enlarged interaction environment. It is important to emphasize
that the electron does not interact with only one detector or the other. Along
all trajectories, the electron interacts with the full detector environment.

Accordingly, the Hamiltonian contains interaction terms associated with both
detectors, described by localized interaction potentials $V_1(q,t)$ and
$V_2(q,t)$. These potentials are present for all paths; what distinguishes
the two slit contributions is not the presence or absence of an interaction, but
the relative weight with which these interaction potentials contribute along
different classes of trajectories.

In propagator language, the wavefunction at the screen point $x$ is
written as

$$
\psi(x,T) = \psi_1(x,T) + \psi_2(x,T),
$$

with each contribution obtained by propagating the initial state through the
corresponding spatial channel,

$$
\psi_j(x,T)
=
\int dx_0\; K_j(x,T;x_0,0)\,\psi(x_0,0),
\qquad j=1,2.
$$

The restricted propagators $K_j$ can be expressed as

$$
K_j(x,T;x_0,0)
=
\int_{q(0)=x_0}^{q(T)=x}\!\!\mathcal Dq\;
\exp\!\left[
\frac{i}{\hbar}
\int_0^T dt\left(
\tfrac12 m\dot q^2
- V_1(q,t)
- V_2(q,t)
\right)
\right],
$$

where the functional integral is restricted to trajectories belonging to
slit-class $j$. The interaction potentials $V_1$ and
$V_2$ are present for all paths; what distinguishes the two classes
is the relative contribution of these potentials along the corresponding
trajectories.

The physically relevant quantity controlling interference is the action
difference between the two slit contributions, which defines the relative phase
$\Delta\phi$:

$$
\Delta\phi
=
\frac{1}{\hbar}\int_0^T dt\,(V_1 - V_2).
$$


## Phase Evolution Induced by the Detector

Define the action increment associated with each detector interaction:

$$
\Delta S_j = -\int dt\,V_j(q,t).
$$

Only differences between these increments affect interference. The relative
phase is

$$
\Delta\phi
=
\frac{1}{\hbar}(\Delta S_2-\Delta S_1)
=
\frac{1}{\hbar}\int dt\,(V_1-V_2).
$$

The total amplitude is therefore

$$
\psi(x)
=
\psi_1^{(0)}(x)
+
e^{i\Delta\phi}\psi_2^{(0)}(x).
$$

Here the superscript $(0)$ in $\psi_j^{(0)}$ denotes the reference
amplitude computed for free propagation, or equivalently for symmetric
interactions that do not produce a relative phase.


### Recovering Double-Slit Pattern with Two Detectors

The probability density $P(x)$ of finding the electron in some point
in the screen calculated as:

$$
P(x)=|\psi(x)|^2
=
\left(\psi_1^{(0)}+e^{i\Delta\phi}\psi_2^{(0)}\right)
\left(\psi_1^{(0)*}+e^{-i\Delta\phi}\psi_2^{(0)*}\right)
$$

so

$$
P(x)
=
|\psi_1^{(0)}|^2
+
|\psi_2^{(0)}|^2
+
e^{-i\Delta\phi}\psi_1^{(0)}\psi_2^{(0)*}
+
e^{i\Delta\phi}\psi_1^{(0)*}\psi_2^{(0)}
$$

The last two terms are complex conjugates, hence

$$
P(x)
=
|\psi_1^{(0)}|^2
+
|\psi_2^{(0)}|^2
+
2\,\mathrm{Re}\!\left(
e^{i\Delta\phi}\psi_1^{(0)*}\psi_2^{(0)}
\right).
$$

If $V_1=V_2$, then $\Delta\phi=0$ and therefore

$$
P(x)
=
|\psi_1^{(0)}|^2
+
|\psi_2^{(0)}|^2
+
2\,\mathrm{Re}\!\left(
\psi_1^{(0)*}\psi_2^{(0)}
\right),
$$

which is precisely the full double-slit interference expression.


## Continuous Suppression of Interference

Recall the expression for the probability density $P(x)$ to detect the
electron at position $x$ on the screen:

$$
P(x)
=
|\psi_1^{(0)}|^2
+
|\psi_2^{(0)}|^2
+
2\,\mathrm{Re}\!\left(
\psi_1^{(0)}\psi_2^{(0)*} e^{i\Delta\phi}
\right)
$$

The probability density at a point on the screen depends on the relative phase
$\Delta\phi[V_1, V_2]$ through the rotation factor $e^{i\Delta\phi}$.

That is, the mere presence of a detector modifies the probability distribution
not by recording an outcome, but by altering the phase structure of the
propagated amplitudes.

When the two slits are energetically symmetric, such that $V_1 = V_2$, the
phase difference vanishes, $\Delta\phi = 0$, and the interference term
contributes maximally. In this case the familiar double-slit pattern is
recovered. The visibility of the interference pattern therefore directly
reflects the symmetry of the slit interactions.

When a detector is present near one or both slits, the corresponding interaction
potentials generally differ, $V_1 \neq V_2$. The resulting phase difference
modifies the interference term and alters the probability distribution at the
screen. This effect occurs independently of whether the detector ultimately
triggers.


### Detector triggers or does-not-trigger

To make the “triggers / does-not-trigger” point explicit, introduce a detector
outcome variable $r_j\in\{0,1\}$ for slit $j$, where
$r_j=1$ denotes a macroscopic firing event and $r_j=0$ denotes
no firing. Crucially, the interaction potential $V_j$ is present in
the Hamiltonian independently of the value of $r_j$; $r_j$
labels a detector outcome, not the existence of an interaction.

Accordingly, the screen amplitude must be written as an amplitude conditioned on
detector outcomes. In the simplest which-way arrangement (exactly one slit is
correlated with exactly one detector), the joint amplitude takes the form

$$
\Psi(x;r_1,r_2)=\psi_1(x)\,\delta_{r_1,1}\delta_{r_2,0}
+\psi_2(x)\,\delta_{r_1,0}\delta_{r_2,1},
$$

where $\delta$ is the Kronecker delta.

The expression describes a superposition of two propagation channels: the slit-1
contribution correlated with the detector-outcome channel $(r_1,r_2)=(1,0)$, and
the slit-2 contribution correlated with $(r_1,r_2)=(0,1)$.

The quantum wave functions $\psi_1(x)$ and $\psi_2(x)$ correspond to
the propagated waves computed at the screen, in position $x$, with
the interaction potentials, $V_1$ and $V_2$ included in
the action delta, $\Delta S_j = -\int dt\,V_j(q,t)$.

If one does not condition on the detector outcomes, the observed probability at
the screen is obtained by summing explicitly over all detector outcomes
$r_1,r_2\in\{0,1\}$:

$$
\begin{aligned}
P(x)
&=
\sum_{r_1,r_2} |\Psi(x;r_1,r_2)|^2 \\
&=
|\Psi(x;1,0)|^2
+
|\Psi(x;0,1)|^2
+
|\Psi(x;0,0)|^2
+
|\Psi(x;1,1)|^2.
\end{aligned}
$$

For typical which-way arrangements , only the outcomes $(r_1,r_2)=(1,0)$ and
$(0,1)$ contribute, with

$$
\Psi(x;1,0)=\psi_1(x), \qquad
\Psi(x;0,1)=\psi_2(x),
$$

while

$$
\Psi(x;0,0)=\Psi(x;1,1)=0.
$$

Therefore,

$$
P(x)
=
|\psi_1(x)|^2
+
|\psi_2(x)|^2.
$$

The cross term $\psi_1^*\psi_2$ is absent because the two slit contributions
occupy orthogonal detector-outcome channels (classically either one detector
fires, `none` or `both` cases are not typically considered).

This absence is independent of whether a detector fires; it follows from summing
over distinct outcomes rather than conditioning on one.

No interference term appears in this unconditional probability, because the two
slit contributions occupy disjoint detector-outcome channels $(r_1,r_2)=(1,0)$
and $(0,1)$.

This shows explicitly that the disappearance of interference is a deterministic
consequence of the interaction potentials associated with the detectors. The
interaction potentials $V_j$ are present during propagation
regardless of whether a macroscopic firing event occurs.


### Ideal scenarios

The above Kronecker-delta form represents an idealized which-way detector with
perfect efficiency and exclusive triggering. In general, non-ideal detector
response permits additional outcome channels. The most general two-slit form can
be written as

$$
\Psi(x;r_1,r_2)=\psi_1(x)\,a_{r_1,r_2}^{(1)}+\psi_2(x)\,a_{r_1,r_2}^{(2)},
$$

where $a_{r_1,r_2}^{(j)}$ is the detector response amplitude for outcome
$(r_1,r_2)$ conditioned on the slit-class $j$.

Summing over outcomes yields

$$
P(x)=\sum_{r_1,r_2}|\Psi(x;r_1,r_2)|^2
=|\psi_1|^2+|\psi_2|^2
+2\,\mathrm{Re}\!\left(\psi_1^*\psi_2\sum_{r_1,r_2} a_{r_1,r_2}^{(1)}a_{r_1,r_2}^{(2)*}\right).
$$

Thus the interference term is controlled by the overlap factor

$$
\Gamma=\sum_{r_1,r_2} a_{r_1,r_2}^{(1)}a_{r_1,r_2}^{(2)*}.
$$

Ideal which-way detection corresponds to $\Gamma=0$ (distinct outcome
channels); full interference corresponds to $\Gamma=1$ (indistinguishable
detector response).


### Atypical cases, or predictions of the mechanistic view

The mechanistic view of detectors as energetic thresholds opens the posibility
of *both* detectors firing and the electron be found in the screen.

If both detectors fire, the corresponding detector response implies that the
interaction experienced by the wave was effectively symmetric between the two
slit regions. In such a case, the relative phase difference vanishes and the
double-slit interference pattern is recovered.

Similarly, if neither detector fires and the electron is nevertheless detected
at the screen, the wavefunction must have evolved under the combined detector
potential into a configuration with negligible amplitude in the detector
regions. This evolution again corresponds to an effectively symmetric
interaction and therefore permits interference.

Detector outcomes label macroscopic response channels of the detector apparatus;
they do not identify microscopic trajectories. In particular, outcomes such as
$(r_1,r_2)=(1,1)$ or $(0,0)$ reflect how the detector circuitry
responds to the incident wave, not where the electron “was” in a particle sense.

When both detectors fire, the interaction potentials have coupled to wave
amplitude in both slit regions.


### Wave-Mechanical “Tunnel Effect”

It is instructive to note that, because the detector interaction potentials are
spatially extended and possess nontrivial spatial structure, the Schrödinger
equation admits solutions in which the electron wavefunction is strongly
suppressed —potentially vanishing— within the detector regions while remaining
finite at the screen. This behavior arises from wave interference under the
combined potential $V_1+V_2$ and does not rely on penetration of a
classically forbidden region.

Transmission to the screen without detector triggering is therefore a purely
wave-mechanical, deterministic effect. It reflects the fact that a wave —quantum
or electromagnetic— is defined over all allowed space and can develop nodal or
near-nodal regions as a consequence of its interaction with structured
potentials.


## No Measurement Postulate Required

At no stage does the description require:

- wavefunction collapse,
- stochastic dynamics,
- observer dependence,
- information-based causation, or
- interpretational assumptions.

The electron evolves deterministically under unitary propagation. Probabilities
arise only after applying the quadratic map to the propagated state.

The disappearance of interference is a consequence of deterministic phase
evolution under interaction. Nothing else is required.


## Conclusion

We have shown that, by following the deterministic evolution of an electron
traversing a double slit in the presence of which-way detectors, one can recover
continuously either the double-slit or the single-slit interference pattern
without appealing to observers, information-theoretic notions, or quantum
mysticism.

By treating the quantum wave as a literal wave evolving under electromagnetic
interaction potentials, we also uncover clear mechanistic explanations for
phenomena commonly described using tunneling or nonlocal transfer language. Such
effects arise from global wave propagation and interference under structured
interactions, and do not require stochastic jumps, collapse, or special
postulates beyond unitary quantum dynamics.


## References

1. C. Cohen-Tannoudji, B. Diu, F. Laloë, *Mécanique quantique*, Tomes I & II,
   Hermann, Paris.

2. R. P. Feynman, *QED: The Strange Theory of Light and Matter*, Princeton
   University Press, 1985.

3. J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley, 1998.

4. M. Schlosshauer, *Decoherence and the Quantum-to-Classical Transition*,
   Springer, 2007.