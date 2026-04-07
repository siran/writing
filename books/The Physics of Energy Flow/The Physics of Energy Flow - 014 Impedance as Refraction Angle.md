---
title: The Physics of Energy Flow - Impedance as Refraction Angle
date: 2026-03-23
---

# 14. Impedance as Refraction Angle

The earlier chapters recovered source-free Maxwell transport from source-free
continuity and then used refraction to explain gravity-like bending. This
chapter extends that same logic into a more speculative direction. It asks how
the standard vacuum ratio between the two electromagnetic aspects should be
read if there is only one flow, and whether what is called impedance records
an angular organization of transport rather than a primitive split between two
substances.

If one flow is primary, its most unitary two-aspect reading is symmetric. In
that reference case the two aspects cycle one into the other in a one-to-one
relation. The natural orbit in the two-aspect plane is then circular. A
non-unit ratio is read here not as evidence for two different substances, but
as skew: the same flow is being resolved obliquely.

Let $a$ and $b$ be the major and minor semiaxes of that reading in the
two-aspect plane, and write the aspect skew as

$$
z := \frac{a}{b} \ge 1.
$$

For a circle seen in a plane tilted by angle $\theta$, the projected ellipse
satisfies

$$
\frac{b}{a} = \cos \theta,
\qquad
z = \sec \theta.
$$

Therefore

$$
\theta = \arccos\!\left(\frac{1}{z}\right).
$$

What standard electromagnetism calls vacuum impedance can then be read, in this
structural picture, as the observed skew:

$$
Z = \sqrt{\frac{\mu}{\epsilon}}.
$$

The claim is not that empty space dissipates motion as a material medium. The
claim is that the non-unit ratio records how a unitary flow is refracted as it
traverses a loaded energetic region. This is the same self-refraction
principle used earlier in the book: a higher energetic loading resists the same
flow and forces an angular change. In this reading, impedance is correctly read
as resistance, not by loss, but by refraction of one flow through a denser
region of the same field. The measured value is the trace of that refracting
resistance written into the two-aspect split.

A symmetric one-to-one relation would give

$$
z = 1
\qquad\Longrightarrow\qquad
\theta = 0.
$$

The observed non-unit ratio gives $\theta \neq 0$: the flow does not meet the
two-aspect plane orthogonally. It enters at an angle and is read as an ellipse
rather than a circle. The two-aspect split is therefore not primitive but
projected.

This can be written in Snell form. Let the exterior unskewed region have index
$n_1 = 1$, and let the loaded region have effective index $n_2 = z$. Standard
Snell law,

$$
n_1 \sin \theta_1 = n_2 \sin \theta_2,
$$

combined with

$$
\cos \theta = \frac{1}{z},
\qquad
\theta_2 = \arcsin\!\left(\frac{1}{z}\right),
$$

gives

$$
\sin \theta_1 = z \cdot \frac{1}{z} = 1,
$$

so

$$
\theta_1 = \frac{\pi}{2}.
$$

In this rough picture the unitary flow reaches the loaded region at grazing
incidence. The flow is tangent to the shell it traverses, not orthogonal to it.

The point of this chapter is not that the standard constants have been derived
in final form. The point is that what appears in standard language as
impedance can be read here as refraction angle and as the resistance
encountered by a unitary flow passing through a loaded region. If that reading
is right, the observed vacuum value need not be the only possible angular
reading. Other angles may exist as other organized transport relations. What
is not fixed here is whether changing that angle changes only the two-aspect
ratio or also the propagation speed, since $\mu$ and $\epsilon$ enter both the
ratio $\sqrt{\mu/\epsilon}$ and the speed $c=1/\sqrt{\mu\epsilon}$. The
chapter therefore opens a direction: transport may be reoriented even when the
full constant structure is not yet closed.


## Separating common loading from aspect skew

The two recovered coefficients enter transport in two independent combinations:

$$
v = \frac{1}{\sqrt{\mu\epsilon}},
\qquad
Z = \sqrt{\frac{\mu}{\epsilon}}.
$$

The product $\mu\epsilon$ fixes the common propagation lag. The ratio
$\mu/\epsilon$ fixes the skew between the two complementary aspects. So if the
skew is to be constrained by a toroidal integer pair, the clean place to write
that constraint is the ratio itself.

Write

$$
s := \sqrt{\mu\epsilon},
\qquad
r := \frac{\mu}{\epsilon}.
$$

Then

$$
\mu\epsilon = s^2,
\qquad
\frac{\mu}{\epsilon} = r.
$$

Multiply these two relations:

$$
\left(\mu\epsilon\right)\left(\frac{\mu}{\epsilon}\right)
=
s^2 r.
$$

The factor $\epsilon$ cancels, so

$$
\mu^2 = s^2 r.
$$

Taking the positive root gives

$$
\mu = s\sqrt{r}.
$$

Now divide the product relation by the ratio relation:

$$
\frac{\mu\epsilon}{\mu/\epsilon}
=
\frac{s^2}{r}.
$$

The factor $\mu$ cancels, so

$$
\epsilon^2 = \frac{s^2}{r}.
$$

Again taking the positive root gives

$$
\epsilon = \frac{s}{\sqrt{r}}.
$$

Therefore the pair can always be written as

$$
\mu = s\sqrt{r},
\qquad
\epsilon = \frac{s}{\sqrt{r}}.
$$

Now impose the literal toroidal ansatz

$$
r = \frac{m}{n},
\qquad
m,n \in \mathbb N.
$$

Then

$$
\mu = s\sqrt{\frac{m}{n}},
\qquad
\epsilon = s\sqrt{\frac{n}{m}}.
$$

The two observable transport combinations become

$$
v = \frac{1}{s},
\qquad
Z = \sqrt{\frac{m}{n}}.
$$

This separates the two roles cleanly.

- The common lag is carried by $s = \sqrt{\mu\epsilon}$.
- The aspect skew is carried by the toroidal ratio $m/n$.

The symmetric case is recovered when

$$
m=n,
$$

for which

$$
\mu = \epsilon = s,
\qquad
Z = 1.
$$

So the toroidal ratio does not need to set the common propagation speed. It can
change only the relative weighting of the two aspects while the common loading
scale $s$ remains fixed. Conversely, changing $s$ at fixed $m/n$ changes the
common refractive lag while preserving the same aspect skew.


## Extracting a rational core and a residual skew

The observed pair need not satisfy the toroidal ansatz exactly. In that case
one may still separate a rational core from a residual skew.

Let the observed coefficients be

$$
\mu_{\mathrm{obs}},
\qquad
\epsilon_{\mathrm{obs}},
$$

and write the observed skew as

$$
r_{\mathrm{obs}} := \frac{\mu_{\mathrm{obs}}}{\epsilon_{\mathrm{obs}}}.
$$

Choose a rational approximation

$$
\frac{m}{n}
$$

to that observed skew, and define the residual factor

$$
\rho
:=
\frac{r_{\mathrm{obs}}}{m/n}
=
\frac{n\,\mu_{\mathrm{obs}}}{m\,\epsilon_{\mathrm{obs}}}.
$$

Then

$$
r_{\mathrm{obs}} = \rho\,\frac{m}{n}.
$$

Let the common loading scale still be

$$
s := \sqrt{\mu_{\mathrm{obs}}\epsilon_{\mathrm{obs}}}.
$$

Substituting

$$
r = \rho\,\frac{m}{n}
$$

into the earlier decomposition gives

$$
\mu_{\mathrm{obs}}
=
s\sqrt{\rho\,\frac{m}{n}},
\qquad
\epsilon_{\mathrm{obs}}
=
s\sqrt{\frac{1}{\rho}\,\frac{n}{m}}.
$$

So the observed pair is separated into three pieces:

- the common loading scale $s$,
- the rational toroidal core $m/n$,
- the residual skew $\rho$.

If

$$
\rho = 1,
$$

then the observed ratio is exactly toroidal:

$$
\frac{\mu_{\mathrm{obs}}}{\epsilon_{\mathrm{obs}}} = \frac{m}{n}.
$$

If instead

$$
\rho \ne 1,
$$

then the ratio contains an exact rational core together with a non-rational
correction. In that case the toroidal integers describe only the leading skew,
not the full observed value.
