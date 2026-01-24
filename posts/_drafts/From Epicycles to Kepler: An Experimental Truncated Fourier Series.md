---
title: "From Epicycles to Kepler: An Experimental Truncated Fourier Series"
subtitle: "Similar Cyclic Representational Idea in Both Minds"
author: "Alexandre Moreau, An M. Rodriguez"
date: "2026-01-24"
one-sentence-summary: "Ptolemaic epicycles constitute a truncated harmonic representation of periodic orbital motion, whose infinite limit recovers Keplerian dynamics."
summary: "This document presents a rigorous mathematical derivation showing that the classical epicyclic model of planetary motion is structurally equivalent to a truncated Fourier expansion of a periodic trajectory. By reparametrizing Keplerian motion using the mean anomaly, we demonstrate that elliptical orbits admit a complete harmonic decomposition, with epicycles corresponding to individual Fourier modes. The historical distinction between Ptolemy and Kepler is reframed as one of formal completeness rather than representational principle."
keywords: "epicycles, Fourier series, Keplerian motion, harmonic decomposition, celestial mechanics, mathematical astronomy"
---

# 1. Objective and scope

We formalize the claim:

> Adding circular motions (epiciclos) progressively improves the approximation
> of a periodic planetary trajectory.


Mathematically, this is the statement that a periodic planar motion can be
approximated arbitrarily well by finite sums of uniform circular motions. This
claim depends only on periodicity and regularity, not on heliocentrism or
geocentrism.

---


# 2. Mathematical setting

We work in the complex plane $\mathbb C \simeq \mathbb R^2$.

A uniform circular motion of radius $R$ and angular frequency
$\omega$ is

$$
z(t)=R\,e^{i(\omega t+\phi)}.
$$

A general **epicyclic model** with finitely many cycles is

$$
z_N(t)=c_0+\sum_{k=1}^{N} c_k e^{i\omega_k t}, \qquad c_k\in\mathbb C.
$$

This expression captures the full geometric content of the Ptolemaic
construction.

---


# 3. Periodicity and angular parametrization

Let $z(t)$ be a bounded planar motion with fundamental period
$T$.

Define the angular variable

$$
\theta := \frac{2\pi}{T}t \in \mathbb T:=\mathbb R/2\pi\mathbb Z.
$$

Then $z(t)=z(\theta)$ where $z:\mathbb T\to\mathbb C$ is
$2\pi$-periodic.

---


# 4. Fourier decomposition of periodic motion

If $z\in L^2(\mathbb T)$, it admits the Fourier expansion

$$
z(\theta)=\sum_{k\in\mathbb Z} \hat z_k e^{ik\theta},
\qquad
\hat z_k=\frac{1}{2\pi}\int_0^{2\pi} z(\theta)e^{-ik\theta}\,d\theta.
$$

The partial sums

$$
z_N(\theta)=\sum_{|k|\le N} \hat z_k e^{ik\theta}
$$

satisfy

$$
\|z-z_N\|_{L^2}\xrightarrow[N\to\infty]{}0
$$

by completeness of the trigonometric system [1].

**Interpretation.** Each term $\hat z_k e^{ik\theta}$ represents a uniform
circular motion. Hence a truncated Fourier series is exactly an epicyclic model.

---


# 5. Keplerian motion as a periodic function

Consider planar Keplerian motion with semi-major axis $a>0$,
eccentricity $e\in[0,1)$, and mean motion $n>0$.

Define the mean anomaly

$$
M:=nt.
$$

The eccentric anomaly $E(M)$ satisfies Kepler’s equation

$$
M=E-e\sin E.
$$

With the focus at the origin, the position is

$$
z(M)=a(\cos E-e)+i\,a\sqrt{1-e^2}\sin E.
$$

---


# 6. Regularity of the Kepler map

Since

$$
\frac{dM}{dE}=1-e\cos E>0 \quad (e<1),
$$

the implicit function theorem ensures that $E(M)$ exists, is unique,
and is $C^\infty$ and $2\pi$-periodic.

Consequently,

$$
z(M)\in C^\infty(\mathbb T)\subset L^2(\mathbb T).
$$

---


# 7. Harmonic expansion of Keplerian motion

Because $z(M)\in L^2(\mathbb T)$, it admits a Fourier series

$$
z(M)=\sum_{k\in\mathbb Z} c_k e^{ikM},
$$

with convergence in $L^2$. Smoothness implies rapid decay of
$|c_k|$ and uniform convergence.

The coefficients $c_k$ can be written explicitly using Fourier–Bessel
expansions involving Bessel functions $J_k(ke)$ [2,3].

---


# 8. Truncation and approximation by epiciclos

Define the truncated approximation

$$
z_N(M)=\sum_{|k|\le N} c_k e^{ikM}.
$$

Then

$$
\|z-z_N\|_{L^2}^2=\sum_{|k|>N}|c_k|^2 \xrightarrow[N\to\infty]{}0.
$$

Thus, increasing the number of cycles (epiciclos) strictly improves the
approximation in a well-defined norm.

---


# 9. Structural equivalence

We may state precisely:

> The Ptolemaic epicyclic construction is mathematically equivalent to a
> truncated Fourier representation of a periodic orbital motion.


Keplerian motion corresponds to the infinite-harmonic limit of this
representation, with coefficients fixed by dynamical laws rather than empirical
adjustment.

The distinction is epistemic, not structural:
- Empirical fitting of coefficients versus analytic determination.
- Finite truncation versus infinite completion.

---


# 10. Conclusion

1. The intuition that adding cycles improves accuracy is mathematically correct.
2. Fourier analysis proves and formalizes this intuition.
3. Keplerian motion lies in the closure of the space spanned by epicycles.
4. Following the Ptolemaic construction and abstracting it rigorously leads
   naturally to Keplerian motion.

The representational idea is the same; only the mathematical language evolved.

---


# References

[1] J. Fourier, *Théorie analytique de la chaleur*. Paris: Firmin Didot, 1822.
DOI: 10.3931/e-rara-8845

[2] J. L. Lagrange, “Sur l’altération des moyens mouvements des planètes,”
*Mémoires de l’Académie Royale des Sciences de Berlin*, 1781. DOI:
10.3931/e-rara-14297

[3] V. I. Arnold, *Mathematical Methods of Classical Mechanics*. Springer, 1978.
DOI: 10.1007/978-1-4757-1693-1

[4] O. Neugebauer, *A History of Ancient Mathematical Astronomy*. Springer,
1975. DOI: 10.1007/978-3-642-61981-8
