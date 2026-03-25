---
title: "Replicating pi(x) from Era Ordering with a Script"
subtitle: "A numerical probe of generational admissibility"
author: "An M. Rodriguez"
date: "2026-03-25"
one-sentence-summary: "A small script computes era-bounded integers, sorts the cumulative generated set, and bins the recovered primes to compare causal ordering with the usual prime-counting picture."
summary: "This note records a numerical experiment for the era-ordering idea. Integers are bounded to the earliest era in which their generators are available, with power formation treated as primitive and coprime recombination admitted afterward. A script computes the era function tau(n) up to a cutoff, caches prior runs, prints era sets through a chosen frontier, and bins the primes that survive in the cumulative generated set. The point is not to recover a smooth density but to watch a jagged prime-counting profile emerge from discrete generational admission."
keywords: "prime counting, pi(x), era ordering, natural numbers, generational admissibility, scripts"
---

# Replicating pi(x) from Era Ordering with a Script

The numerical question is simple: if integers are bounded to the earliest era
in which their generators are available, what does the cumulative admitted set
look like when it is sorted back into the usual order on `N`?

The script for this experiment now lives at
[`C:\Users\an\src\siran\writing\.scripts\tools\era_order.py`](C:\Users\an\src\siran\writing\.scripts\tools\era_order.py).

It now works era by era rather than through a fixed numerical cutoff. On each
run it:

1. loads the cached era state, if any;
2. saves a rolling `latest` image of the current `p(N)` plot;
3. reports the known eras and the size of the admitted set;
4. asks how many more eras to compute, together with a timing estimate based on
   the most recent era;
5. computes those eras, updates the cache, and saves both per-era snapshots and
   a refreshed `latest` plot;
6. can optionally save checkpoint plots during materialized eras.

When the admitted right endpoint becomes too large for ordinary floating-point
plotting, the script automatically switches the horizontal axis to `log10(N)`
so the plot does not fail on late eras.

It uses the current era rule:

$$
\tau(1)=1,
$$

and for $n>1$,

$$
\tau(n)
=
\min\left(
\kappa(n),
\min_{\substack{ab=n\\1<a<n\\\gcd(a,b)=1}}
\max(\tau(a),\tau(b))
\right),
$$

where $\kappa(n)$ is the least generator ceiling among power representations
$n=a^b$ with $b\ge 1$.

Example:

```powershell
python .scripts/tools/era_order.py
```

Optional:

```powershell
python .scripts/tools/era_order.py --checkpoint-every 50000
```

The working hypothesis is not that a smooth prime density is being derived.
Rather, the jagged prime-counting profile should emerge gradually as more
admitted points are added from successive eras.
