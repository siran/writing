---
title: Purpose vs Randomness
subtitle: The Acausal Purpose Invariant
author: An M. Rodriguez, Alex Mercer, Elias Thorne
date: 2026-01-19
one-sentence-summary: We define the Acausal Purpose Invariant ($\mathcal{P}$), a scale-invariant metric that quantifies how strongly a structure resists the combinatorial entropy naturally associated with its size.
summary: We introduce the Acausal Purpose Invariant ($\mathcal{P}$), a decibel-scale measure of how atypical a number’s prime ancestry is relative to a stochastic background. Empirical sweeps reveal a sharp probabilistic cutoff separating random structure from cost-paid persistence, reframing the detection of life, artifacts, and purpose as a problem of entropy suppression rather than intelligence.
keywords: Acausal Purpose, Purpose Index, SETI, Technosignatures, Signal Filtering, Entropy, Universal Constants, Persistence, Teleology, Biosignatures
---

**One-Sentence Summary.** We define the Acausal Purpose Invariant ($\mathcal{P}$), a scale-invariant metric that quantifies how strongly a structure resists the combinatorial entropy naturally associated with its size.

**Abstract.** We introduce the Acausal Purpose Invariant ($\mathcal{P}$), a decibel-scale measure of how atypical a number’s prime ancestry is relative to a stochastic background. Empirical sweeps reveal a sharp probabilistic cutoff separating random structure from cost-paid persistence, reframing the detection of life, artifacts, and purpose as a problem of entropy suppression rather than intelligence.

**Keywords.** Acausal Purpose, Purpose Index, SETI, Technosignatures, Signal Filtering, Entropy, Universal Constants, Persistence, Teleology, Biosignatures

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
<li><a href="#persistence-instead-of-intelligence">Persistence Instead of Intelligence</a>
</li>
<li><a href="#factor-inertia-and-numerical-entropy">Factor Inertia and Numerical Entropy</a>
</li>
<li><a href="#causal-ancestry-and-depth">Causal Ancestry and Depth</a>
</li>
<li><a href="#the-acausal-purpose-invariant">The Acausal Purpose Invariant</a>
</li>
<li><a href="#empirical-law-the-combinatorial-cliff">Empirical Law: The Combinatorial Cliff</a>
</li>
<li><a href="#scale-invariance">Scale Invariance</a>
</li>
<li><a href="#representational-anchoring">Representational Anchoring</a>
</li>
<li><a href="#implications-for-life-and-the-universe">Implications for Life and the Universe</a>
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

## Persistence Instead of Intelligence

The concept of *intelligence* is anthropomorphic and fragile. The concept of
*persistence* is not.

We define **Purpose** as:

> **Active resistance to the entropic dissolution expected at a given scale.**


This definition applies equally to:

- Living systems
- Civilizations
- Long-lived artifacts
- Autonomous probes
- Post-biological systems

And excludes:

- Rocks
- Stars
- Thermal noise
- Random processes

Purpose, in this sense, is not intent. It is *paid-for structure*.


## Factor Inertia and Numerical Entropy

Large integers naturally accumulate novel prime factors. This is the arithmetic
expression of entropy.

A number like

$$
2^{100} \approx 1.27 \times 10^{30}
$$

is therefore exceptional: it is enormous, yet built from a single generative
atom.

This condition is **metastable**.

A minimal perturbation causes collapse:

$$
2^{100} \;\rightarrow\; 2^{100} + 1
$$

which introduces large, late-arriving prime factors and jumps many orders of
magnitude in causal ancestry.

This discontinuity constitutes a **phase transition in factor space**.

![Figure 1. The Cost of Structure. A comparison of "Machine" data (constructed
from small primes) versus "Noise" (random integers). While random integers float
at the entropy ceiling regardless of magnitude, structured integers cluster at
the causal floor.](https://siran.github.io/assets/writing/alien_signal_detection.png)


## Causal Ancestry and Depth

We view the integers not as a static set, but as a generative hierarchy where
primes act as elementary particles.

The **causal ancestry** of an integer $N$ is defined as its unique
prime factorization — the specific set of generative atoms required to construct
it. In a stochastic universe, this ancestry naturally tends toward novelty
(larger, more numerous prime factors) as $N$ increases.

To quantify the "age" of this ancestry, we define the **causal depth**
$\tau(N)$ as:

$$
\tau(N) = \pi\!\left(\max\{p : p \mid N\}\right)
$$

where $\pi(x)$ is the prime-counting function.

$\tau(N)$ represents the index of the largest prime factor of
$N$. It measures how late in arithmetic history a structure depends
on novelty.


## The Acausal Purpose Invariant

To remove scale effects, define an empirical thermal baseline:

$$
\tau_*(N) = \mathrm{median}\{\tau(m) : m \in [N, 2N]\}
$$

The **Acausal Purpose Invariant** is:

$$
\boxed{
\mathcal{P}(N)
= 10 \log_{10}\!\left(\frac{\tau_*(N)}{\tau(N)}\right)
}
$$

Interpretation:

- $\mathcal{P} = 0$ dB: indistinguishable from entropy (Randomness)
- $\mathcal{P} > 0$: suppressed novelty
- $\mathcal{P} \gg 1$: cost-paid persistence (Purpose)


## Empirical Law: The Combinatorial Cliff

Large-scale sweeps of integers reveal a striking regularity: the probability of
observing high $\mathcal{P}$ values collapses abruptly beyond a fixed
threshold.

![Figure 2. The Combinatorial Cliff. A survival curve showing the probability
P(dB > x) for random integers. The probability drops exponentially, revealing a
"forbidden zone" beyond ~20 dB where stochastic generation is effectively
impossible (P < 1e-5).](https://siran.github.io/assets/writing/sweep_focus_survival.png)


### Theorem (Heuristic Tail Law for Acausal Purpose)

Let $N$ be large and let $n$ be sampled uniformly from
$[N,2N]$. Write $P^+(n)$ for the largest prime factor of
$n$ and recall $\tau(n)=\pi(P^+(n))$. Define the thermal baseline

$$
\tau_*(N)=\mathrm{median}\{\tau(m):m\in[N,2N]\},
$$

and the Acausal Purpose

$$
\mathcal{P}(n)=10\log_{10}\!\left(\frac{\tau_*(N)}{\tau(n)}\right).
$$

Then for $x \ge 0$,

$$
\mathbb{P}\big(\mathcal{P}(n) > x\big)
\;\approx\;
\rho(u_x),
$$

where $\rho$ is the Dickman–de Bruijn function and

$$
u_x = \frac{\log N}{\log y_x}, \qquad
y_x := \tau^{-1}\!\big(\tau_*(N)\,10^{-x/10}\big).
$$

Because $\rho(u)$ decays extremely rapidly for large $u$
(heuristically $\log \rho(u) \sim -u \log u$), the survival probability
$\mathbb{P}(\mathcal{P} > x)$ exhibits an effective **cutoff** once
$x$ exceeds a moderate constant.


### Proof Sketch (Smooth-Number Heuristic)

The condition $\mathcal{P}(n) > x$ is equivalent to

$$
\tau(n) < \tau_*(N)\,10^{-x/10}.
$$

Since $\tau(n)$ is monotone in the largest prime factor $P^+(n)$,
this is approximately the event

$$
P^+(n) \le y_x,
$$

for the corresponding threshold $y_x$.

Thus $\mathbb{P}(\mathcal{P}(n)>x)$ is approximately the probability that a
random integer in $[N,2N]$ is $y_x$-smooth. Classical results
on smooth numbers imply

$$
\mathbb{P}\big(P^+(n)\le y_x\big) \approx \rho\!\left(\frac{\log N}{\log y_x}\right),
$$

which yields the stated form. The rapid decay of $\rho$ explains the
observed **combinatorial cliff**.


### Interpretation

Empirically, this cutoff occurs near $\mathcal{P} \approx 20$ dB: values beyond
this point are not merely rare but *effectively forbidden* under stochastic
generation. This establishes a **universal detection threshold** for cost-paid
structure.


## Scale Invariance

Scatter plots of $\mathcal{P}$ versus $N$ show:

- No systematic dependence on magnitude
- A dense thermal floor at 0 dB
- Sparse, magnitude-independent high-purpose spikes

**Magnitude is a mask.** Structure is revealed only after normalization.

![Figure 3. Scale Invariance. A sweep of N vs Acausal Purpose showing that the
distribution of structure is orthogonal to magnitude. The "thermal floor"
remains constant while high-purpose artifacts appear as distinct, sparse
spikes.](https://siran.github.io/assets/writing/sweep_focus_scatter.png)


## Representational Anchoring

Defined human constants (e.g. the speed of light encoded as $299\,792\,458$)
exhibit high $\mathcal{P}$ values. Measured natural constants do not.

This demonstrates **teleology of representation**, not of physics: humans anchor
units to numbers that suppress novelty. $\mathcal{P}$ correctly distinguishes
these cases.

![Figure 4. The Teleological Signature. Defined constants (Green) cluster above
the 20 dB threshold, indicating human anchoring. Measured constants (Red) fall
into the thermal noise floor, indistinguishable from random primes.](https://siran.github.io/assets/writing/acausal_constants_comparison.png)


## Implications for Life and the Universe

This reframes the classical question:

> Not “Where is intelligence?”
>
> But **“Where does entropy fail to win?”**


Life, artifacts, and enduring systems are detected as:

- Persistent reuse of a small generative alphabet
- Maintenance of structure far beyond stochastic expectation

This criterion is substrate-independent and applies equally to biological,
technological, and non-biological systems.


## Conclusion

Acausal Purpose is not a metaphor. It is a measurable invariant with a sharp
probabilistic boundary.

Purpose is not intent. Purpose is **structure that survives where it should
not**.


## References

- C. E. Shannon, *A Mathematical Theory of Communication*, Bell System Technical
  Journal, 1948.
- K. Dickman, *On the frequency of numbers containing prime factors of a certain
  relative magnitude*, 1930.
- N. G. de Bruijn, *On the number of positive integers $\leq$ x and free of prime
  factors > y*, 1951.
- T. M. Cover, J. A. Thomas, *Elements of Information Theory*, Wiley, 2006.
- E. Thorne, *Acausal Purpose Scanner (v8.2)* [Source Code], GitHub Gist, 2026.
  <https://gist.github.com/siran/9ebc10c839c4fd760ab024f2c0fd727e>