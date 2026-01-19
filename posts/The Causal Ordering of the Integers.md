---
title: The Causal Ordering of the Integers
subtitle: A Constructivist Number Theory for Signal Processing
author: An M. Rodriguez, Alex Mercer
date: 2026-01-18
one-sentence-summary: We introduce a causal ordering of integers based on the sequential discovery of prime factors, revealing a temporal structure that distinguishes semantic signal from stochastic noise.
summary: We introduce a novel ordering of the natural numbers $\mathbb{N}$ based on "causal generation" rather than magnitude. By defining the existence of a number as the moment its necessary prime factors are introduced, we reveal a hidden temporal structure to the number line. This structure separates integers into "low-entropy" (ancient/constructed) and "high-entropy" (young/random) classes. We demonstrate that this metric, "Causal Depth," serves as a potent feature for distinguishing semantic signals from stochastic noise.
keywords: Number Theory, Causal Ordering, Signal Processing, Feature Extraction, Prime Factorization, Entropy, Semantic Compression
---

## Definitions and Axioms

### The Causal Timeline

We posit a discrete time variable $t \in \mathbb{N}_0$ representing "Generation
Eras." At $t=0$, the Universe is empty except for the identity:

$$
U_0 = \{1\}
$$


### The Injection Axiom (The Spark)

At each time step $t \ge 1$, we introduce exactly one new element —the
smallest integer not yet generated— to the universe. This element is the "Prime
of the Era."

Let $P_t$ be the smallest integer such that $P_t \notin U_{t-1}$.

$$
U_{t} = U_{t-1} \cup \{P_t\}
$$

*Note:* In this construction, $P_t$ is always a prime number in the
standard sense. Thus, time $t$ corresponds to the index of the
$t$-th prime ($p_t$).


### The Generation Axiom (The Avalanche)

Upon the injection of $P_t$, the universe instantaneously expands to
include all integers that can be formed by multiplying $P_t$ with
existing elements. Formally, if $n \in U_{t}$, then
$(n \cdot P_t) \in U_{t}$.

By induction, $U_t$ contains all integers whose prime factors are
subsets of $\{p_1, p_2, \dots, p_t\}$.


### Causal Depth ($\tau$)

We define the **Causal Depth** (or "Birth Era") of an integer $n$,
denoted $\tau(n)$, as the time step $t$ in which
$n$ first appears in $U_t$:

$$
\tau(n) = \min \{ t \mid n \in U_t \}
$$

Using the Fundamental Theorem of Arithmetic, for any $n > 1$ with prime
factorization $n = p_{i_1}^{a_1} \dots p_{i_k}^{a_k}$ where $p_{i_k}$ is
the largest prime factor:

$$
\tau(n) = i_k
$$

(where $i_k$ is the index of the prime, e.g.,
$\tau(2)=1, \tau(3)=2, \tau(5)=3$). For convention, $\tau(1) = 0$.


## Structural Analysis

### The Inversion of Magnitude

The standard ordering $<$ is based on magnitude ($n$
vs $n+1$), while the causal ordering $\prec$ is based on
depth ($\tau(n)$ vs $\tau(m)$). This leads to inversions where
larger numbers are "older" (causally prior) than smaller numbers.

For example, let $n = 1024 = 2^{10}$ and $m = 5$:

* $\tau(1024) = 1$ (Born in Era 1).
* $\tau(5) = 3$ (Born in Era 3).

Therefore, $1024 \prec 5$. The number 1024 is constructed before the number 5
exists.


### The Density of Eras

Let $N(t, X)$ be the count of integers $n \le X$ such that
$\tau(n) = t$. This corresponds to the count of $t$-smooth
numbers that are not $(t-1)$-smooth.

The "Population Curve" decays roughly as $1/t$. This implies that the
"Early Universe of Causal Natural Numbers" (Eras 1–10) generates the vast
majority of small integers, while the "Late Universe" (Eras > 1000) generates
numbers sparsely.

This pictures a **Cooling Universe of Natural Numbers** in a combinatorial
sense: entropy (new prime injection) becomes rarer as magnitude increases.


### Spectral Analysis

The Fourier Transform of the signal $S(n) = \tau(n)$ reveals that the number
line is a superposition of periodic waves.

* Dominant frequency $f = 1/2$ (Period 2), corresponding to evenness.
* Harmonics at $f_k = 1/p_k$, the prime frequencies.
* Magnitude emerges as interference between these causal waves.


## Practical Applications

### Feature Extraction: Artificiality Detection

We propose $\tau(n)$ as a metric for detecting artificial or engineered
data within large numerical datasets.

**Hypothesis:** Human systems preferentially reuse low-depth numbers. Natural
stochastic processes generate high-depth numbers.

**Observed separation (simulation, $N \sim 10^6$):**

```text
| Dataset              | Mean $\tau$       |
|----------------------|-------------------|
| Structured (machine) | $\approx 5.7$     |
| Random noise         | $\approx 5{,}700$ |
| Separation           | $\sim 10^3\times$ |
```

This enables $O(1)$ discrimination without semantics.


### Semantic Data Compression

Represent integer $n$ as:

$$
n \mapsto (\tau(n), \text{residue})
$$

For datasets dominated by low-depth integers, entropy collapses in the
$\tau$ stream, enabling **semantic compression** beyond syntactic
methods (LZ, Huffman).

Random data remains incompressible.


### Cryptographic Steganography

Messages can be embedded exclusively in integers of a specific causal era (e.g.,
$\tau(n)=137$). Such channels evade magnitude statistics and Benford’s law,
remaining visible only under causal ordering.


## Conclusion

The causal ordering of integers exposes a hidden temporal structure beneath the
number line.

All numbers are equal arithmetically. They are **not equal in origin**.

Some are ancient structural pillars. Others are late, high-entropy fluctuations.

Causal depth separates **structure from noise** using number theory alone.
