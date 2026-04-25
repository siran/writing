---
title: The Physics of Energy Flow - Appendix A2
date: 2026-04-11
kind: appendix
part: Appendices
summary: >
  The full scalar wave equation on a toroidal domain, with all curvature
  corrections retained. The Laplacian on a torus of major radius R and minor
  radius r is derived in toroidal coordinates. The curvature terms that
  Chapter 8 omits are identified and their effect on the mode spectrum is
  characterized. The integer mode counting is shown to be independent of the
  aspect ratio, while the exact frequencies receive aspect-dependent
  corrections.
keywords:
  - toroidal Laplacian
  - curvature corrections
  - mode spectrum
  - aspect ratio
  - wave equation
---

> TO BE READ: rough AI draft pending detailed human review.


# Appendix A2. Wave Equation on a Toroidal Domain

Chapter 8 writes the wave equation on a toroidal closure in the separated form

$$
\partial_t^2 f
=
c^2\left(
\partial_s^2 f + \frac{1}{r^2}\partial_\theta^2 f
\right),
$$

with curvature corrections omitted. This appendix derives the full Laplacian on
a torus, identifies the omitted terms, and shows that the integer mode counting
is exact while the mode frequencies receive aspect-dependent corrections.


## A2.1 Toroidal Coordinates

Parametrize the torus by three coordinates $(\phi, \theta, \rho)$:

- $\phi \in [0, 2\pi)$: angle around the major cycle (centerline),
- $\theta \in [0, 2\pi)$: angle around the minor cycle (cross-section),
- $\rho \in [0, r]$: radial distance from the tube center.

A point in space is

$$
\mathbf{x}(\phi, \theta, \rho)
=
\bigl((R + \rho\cos\theta)\cos\phi,\;
(R + \rho\cos\theta)\sin\phi,\;
\rho\sin\theta\bigr).
$$

Define

$$
\eta(\theta, \rho) := R + \rho\cos\theta.
$$

This is the distance from the symmetry axis to the point $(\phi,\theta,\rho)$.
On the tube surface ($\rho = r$), $\eta$ varies from $R - r$ on the inner
equator ($\theta = \pi$) to $R + r$ on the outer equator ($\theta = 0$).


## A2.2 Metric and Scale Factors

The scale factors of the toroidal coordinate system are

$$
h_\phi = \eta = R + \rho\cos\theta,
\qquad
h_\theta = \rho,
\qquad
h_\rho = 1.
$$

The volume element is

$$
dV = h_\phi\,h_\theta\,h_\rho\;d\phi\,d\theta\,d\rho
=
\eta\,\rho\;d\phi\,d\theta\,d\rho.
$$


## A2.3 The Laplacian

The Laplacian in orthogonal curvilinear coordinates is

$$
\nabla^2 f
=
\frac{1}{h_\phi h_\theta h_\rho}
\left[
\frac{\partial}{\partial\phi}\!\left(\frac{h_\theta h_\rho}{h_\phi}\frac{\partial f}{\partial\phi}\right)
+
\frac{\partial}{\partial\theta}\!\left(\frac{h_\phi h_\rho}{h_\theta}\frac{\partial f}{\partial\theta}\right)
+
\frac{\partial}{\partial\rho}\!\left(\frac{h_\phi h_\theta}{h_\rho}\frac{\partial f}{\partial\rho}\right)
\right].
$$

Substituting the scale factors:

$$
\nabla^2 f
=
\frac{1}{\eta\rho}
\left[
\frac{\partial}{\partial\phi}\!\left(\frac{\rho}{\eta}\frac{\partial f}{\partial\phi}\right)
+
\frac{\partial}{\partial\theta}\!\left(\eta\frac{\partial f}{\partial\theta}\right)
+
\rho\frac{\partial}{\partial\rho}\!\left(\eta\frac{\partial f}{\partial\rho}\right)
\right].
$$


### Surface Laplacian

For a field confined to the tube surface ($\rho = r$, no radial dependence),
the radial term is dropped and the surface Laplacian is

$$
\nabla^2_{\mathrm{surf}} f
=
\frac{1}{\eta\,r}
\left[
\frac{\partial}{\partial\phi}\!\left(\frac{r}{\eta}\frac{\partial f}{\partial\phi}\right)
+
\frac{\partial}{\partial\theta}\!\left(\eta\frac{\partial f}{\partial\theta}\right)
\right],
$$

where now $\eta = R + r\cos\theta$.

Expanding the derivatives:

$$
\nabla^2_{\mathrm{surf}} f
=
\frac{1}{\eta^2}\frac{\partial^2 f}{\partial\phi^2}
+
\frac{1}{r^2}\frac{\partial^2 f}{\partial\theta^2}
-
\frac{\sin\theta}{r\,\eta}\frac{\partial f}{\partial\theta}.
$$

The three terms have clear geometric meanings:

1. $\dfrac{1}{\eta^2}\dfrac{\partial^2 f}{\partial\phi^2}$: variation around
   the major cycle, weighted by the local circumferential distance $\eta$
   from the symmetry axis.

2. $\dfrac{1}{r^2}\dfrac{\partial^2 f}{\partial\theta^2}$: variation around
   the minor cycle, as in the flat approximation.

3. $-\dfrac{\sin\theta}{r\,\eta}\dfrac{\partial f}{\partial\theta}$: the
   curvature correction. It couples the minor-cycle derivative to the
   position on the cross-section.


## A2.4 What Chapter 8 Drops

Chapter 8 replaces $\eta = R + r\cos\theta$ by its mean value $R$, giving

$$
\nabla^2_{\mathrm{flat}} f
\approx
\frac{1}{R^2}\frac{\partial^2 f}{\partial\phi^2}
+
\frac{1}{r^2}\frac{\partial^2 f}{\partial\theta^2}.
$$

This amounts to two approximations:

**Approximation 1.** In the major-cycle term,

$$
\frac{1}{\eta^2} \to \frac{1}{R^2}.
$$

The fractional error is

$$
\frac{1}{\eta^2} - \frac{1}{R^2}
=
\frac{1}{R^2}\left(\frac{1}{(1+\epsilon\cos\theta)^2} - 1\right),
\qquad
\epsilon := \frac{r}{R}.
$$

For $\epsilon \ll 1$ (thin torus), the correction is $O(\epsilon)$. For
$\epsilon \sim 1$ (fat torus, as Appendix A0 shows is the self-consistent
regime), the correction is $O(1)$ and cannot be neglected.

**Approximation 2.** The curvature correction term

$$
-\frac{\sin\theta}{r\,\eta}\frac{\partial f}{\partial\theta}
$$

is dropped entirely. This term is first order in the minor-cycle derivative
and couples the angular position on the cross-section to the transport around
the torus. It vanishes identically at $\theta = 0$ (outer equator) and
$\theta = \pi$ (inner equator), and is maximal at $\theta = \pi/2$ and
$3\pi/2$.


## A2.5 Full Surface Wave Equation

The full scalar wave equation on the toroidal surface is

$$
\partial_t^2 f
=
c^2\left(
\frac{1}{\eta^2}\frac{\partial^2 f}{\partial\phi^2}
+
\frac{1}{r^2}\frac{\partial^2 f}{\partial\theta^2}
-
\frac{\sin\theta}{r\,\eta}\frac{\partial f}{\partial\theta}
\right),
$$

with $\eta = R + r\cos\theta$.


## A2.6 Mode Structure with Curvature Corrections

Seek separated solutions of the form

$$
f(\phi,\theta,t) = e^{im\phi}\,\Theta(\theta)\,e^{-i\omega t}.
$$

The $\phi$-periodicity enforces $m \in \mathbb{Z}$, exactly as in Chapter 8.
This integer condition is independent of the curvature corrections.

Substituting into the full surface wave equation gives the ordinary
differential equation for $\Theta(\theta)$:

$$
\frac{\omega^2}{c^2}\,\Theta
=
-\frac{m^2}{\eta^2}\,\Theta
+
\frac{1}{r^2}\,\Theta''
-
\frac{\sin\theta}{r\,\eta}\,\Theta',
$$

where primes denote $d/d\theta$ and $\eta = R + r\cos\theta$.

Rearranging:

$$
\Theta''
-
\frac{r\sin\theta}{\eta}\,\Theta'
+
r^2\left(\frac{\omega^2}{c^2} + \frac{m^2}{\eta^2}\right)\Theta
= 0.
$$

This is a Hill-type equation: a second-order ODE with periodic coefficients
(period $2\pi$ in $\theta$). The $\theta$-periodicity of $\Theta$ enforces
a discrete spectrum of allowed $\omega$ values for each $m$.

In the flat approximation ($\eta \to R$, curvature term dropped), this reduces
to

$$
\Theta'' + \left(\frac{r^2\omega^2}{c^2} + \frac{m^2 r^2}{R^2}\right)\Theta = 0,
$$

which has the constant-coefficient solutions $\Theta = e^{in\theta}$ with
$n \in \mathbb{Z}$ and

$$
\omega^2 = c^2\left(\frac{m^2}{R^2} + \frac{n^2}{r^2}\right),
$$

recovering Chapter 8.


### Structure of the corrections

Write $\epsilon = r/R$ and expand the Hill equation to first order in
$\epsilon$. The coefficients become

$$
\frac{r\sin\theta}{\eta}
=
\epsilon\sin\theta\,(1 + O(\epsilon)),
$$

$$
\frac{m^2}{\eta^2}
=
\frac{m^2}{R^2}(1 - 2\epsilon\cos\theta + O(\epsilon^2)).
$$

At first order, the curvature correction couples the $n$-th Fourier mode of
$\Theta$ to its neighbors $n \pm 1$. The leading effect is a frequency shift
proportional to $\epsilon$:

$$
\omega_{mn}^2
=
c^2\left(\frac{m^2}{R^2}+\frac{n^2}{r^2}\right)
\left(1 + O(\epsilon)\right).
$$

More precisely, the first-order correction to $\omega_{mn}^2$ from standard
perturbation theory of Hill's equation is

$$
\delta\omega_{mn}^2
=
-\frac{c^2 m^2}{R^2}\,\epsilon\,\langle\cos\theta\rangle_{n}
+
O(\epsilon^2),
$$

where $\langle\cos\theta\rangle_n$ is the diagonal matrix element of
$\cos\theta$ in the $n$-th Fourier mode. Since $\cos\theta$ connects $n$ to
$n \pm 1$, the diagonal element vanishes:

$$
\langle n|\cos\theta|n\rangle
=
\frac{1}{2\pi}\int_0^{2\pi} e^{-in\theta}\cos\theta\,e^{in\theta}\,d\theta
= 0.
$$

Therefore the first-order frequency correction vanishes:

$$
\delta\omega_{mn}^2 = O(\epsilon^2).
$$

The leading correction to the mode frequencies is second order in $\epsilon$.


## A2.7 What the Curvature Terms Do and Do Not Change

**What is unchanged:**

1. The integer $m$ is enforced by $\phi$-periodicity. This is exact for any
   $\epsilon$.

2. The integer $n$ is enforced by $\theta$-periodicity. The Hill equation has
   a discrete Floquet spectrum; the periodicity condition selects integer
   Fourier indices regardless of $\epsilon$.

3. The mode-counting rule — one integer pair $(m,n)$ per allowed standing
   wave — holds for all aspect ratios.

**What changes:**

1. The exact mode frequencies receive corrections of order $\epsilon^2$
   relative to the flat-torus values. For a fat torus ($\epsilon \sim 1$),
   these corrections are $O(1)$ and the flat formula is quantitatively wrong,
   even though it is qualitatively correct.

2. The curvature correction couples neighboring Fourier modes in $\theta$,
   meaning the exact eigenmodes of the full equation are not pure
   $e^{in\theta}$ but superpositions with small admixtures of $e^{i(n\pm 1)\theta}$,
   $e^{i(n\pm 2)\theta}$, etc. The leading admixture is $O(\epsilon)$.

3. For a fat torus, the mode shapes are distorted: energy density is higher on
   the outer equator ($\theta = 0$) than on the inner equator
   ($\theta = \pi$), because the outer equator has larger $\eta$ and therefore
   a longer path around the major cycle.


## A2.8 Implications for the Self-Consistent Closure

Appendix A0 shows that the self-consistent closure has aspect ratio

$$
\frac{r}{mR} = \frac{\sqrt{n^2-1}}{n},
$$

which for the minimum closure ($m = 1$, $n = 2$) gives $\epsilon = r/R =
\sqrt{3}/2 \approx 0.87$. In this regime, the flat-torus frequency formula
of Chapter 8 is a qualitative guide but not a quantitative prediction.

Computing the exact spectrum of the minimum closure requires solving the full
Hill equation of Section A2.6 at $\epsilon = \sqrt{3}/2$. This is a numerical
exercise that does not change the topological structure of the spectrum (one
mode per integer pair) but does change the quantitative spacing between
levels.

For higher $m$ at fixed $n$, or for closures confined by external energy density
to $\epsilon \ll 1$, the flat-torus formula is quantitatively accurate to
$O(\epsilon^2)$.


## A2.9 Summary

1. The full Laplacian on a toroidal surface contains a position-dependent
   major-cycle term $1/\eta^2$ and a curvature correction
   $-(\sin\theta)/(r\eta)\,\partial_\theta$.

2. Chapter 8 drops both by replacing $\eta \to R$. The resulting flat-torus
   equation is exact in the limit $r/R \to 0$.

3. The integer mode counting $(m, n)$ is topological: it is enforced by
   periodicity in $\phi$ and $\theta$ and holds for all aspect ratios.

4. The first-order frequency correction vanishes. The leading correction to
   the mode frequencies is $O(\epsilon^2)$ where $\epsilon = r/R$.

5. For the self-consistent minimum closure ($\epsilon \approx 0.87$), the
   corrections are large and the exact spectrum requires numerical solution
   of the Hill equation.

6. The qualitative picture of Chapter 8 — discrete integer modes, Rydberg-type
   scaling from standing-wave partitions — is robust. The curvature terms
   change the exact frequencies, not the counting.
