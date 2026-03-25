from __future__ import annotations

import argparse
from bisect import bisect_right
from functools import lru_cache
from heapq import nlargest
from math import isqrt


def smallest_prime_factors(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for n in range(2, isqrt(limit) + 1):
        if spf[n] != n:
            continue
        start = n * n
        step = n
        for k in range(start, limit + 1, step):
            if spf[k] == k:
                spf[k] = n
    return spf


def primes_from_spf(spf: list[int]) -> list[int]:
    return [n for n in range(2, len(spf)) if spf[n] == n]


def factorize(n: int, spf: list[int]) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        factors.append((p, e))
    return factors


@lru_cache(maxsize=None)
def divisors(n: int) -> tuple[int, ...]:
    out: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d != 0:
            continue
        out.append(d)
        if d * d != n:
            out.append(n // d)
    out.sort()
    return tuple(out)


@lru_cache(maxsize=None)
def prime_power_era(prime: int, exponent: int) -> int:
    best = prime**exponent
    for power in divisors(exponent):
        base = prime ** (exponent // power)
        best = min(best, max(base, power))
    return best


def tau_from_factors(factors: list[tuple[int, int]]) -> int:
    if not factors:
        return 1
    return max(prime_power_era(prime, exponent) for prime, exponent in factors)


def tau_up_to(limit: int, spf: list[int]) -> list[int]:
    tau = [0] * (limit + 1)
    tau[1] = 1
    for n in range(2, limit + 1):
        tau[n] = tau_from_factors(factorize(n, spf))
    return tau


def slow_power_cost(n: int) -> int:
    best = n
    max_b = n.bit_length() + 1
    for power in range(2, max_b + 1):
        lo = 2
        hi = n
        while lo <= hi:
            mid = (lo + hi) // 2
            value = mid**power
            if value == n:
                best = min(best, max(mid, power))
                break
            if value < n:
                lo = mid + 1
            else:
                hi = mid - 1
    return best


def slow_tau_up_to(limit: int) -> list[int]:
    tau = [0] * (limit + 1)
    tau[1] = 1
    for n in range(2, limit + 1):
        best = slow_power_cost(n)
        for a in range(2, isqrt(n) + 1):
            if n % a != 0:
                continue
            b = n // a
            if gcd(a, b) != 1:
                continue
            best = min(best, max(tau[a], tau[b]))
        tau[n] = best
    return tau


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def format_factorization(factors: list[tuple[int, int]]) -> str:
    parts = []
    for prime, exponent in factors:
        if exponent == 1:
            parts.append(str(prime))
        else:
            parts.append(f"{prime}^{exponent}")
    return " * ".join(parts)


def candidate_bound(n: int, tau_n: int) -> int:
    return min(isqrt(n), tau_n)


def prime_count(primes: list[int], bound: int) -> int:
    return bisect_right(primes, bound)


def stats_for_number(n: int, factors: list[tuple[int, int]], tau_n: int, primes: list[int]) -> dict[str, object]:
    sqrt_n = isqrt(n)
    naive = prime_count(primes, sqrt_n)
    bound = candidate_bound(n, tau_n)
    filtered = prime_count(primes, bound)
    reduction = 0.0 if naive == 0 else 1.0 - (filtered / naive)
    return {
        "n": n,
        "factors": factors,
        "tau": tau_n,
        "sqrt": sqrt_n,
        "naive": naive,
        "bound": bound,
        "filtered": filtered,
        "reduction": reduction,
    }


def is_prime_factorization(factors: list[tuple[int, int]]) -> bool:
    return len(factors) == 1 and factors[0][1] == 1


def is_semiprime_factorization(factors: list[tuple[int, int]]) -> bool:
    return sum(exponent for _, exponent in factors) == 2


def top_reductions(limit: int, spf: list[int], tau: list[int], primes: list[int], top_k: int) -> list[dict[str, object]]:
    rows = []
    for n in range(4, limit + 1):
        factors = factorize(n, spf)
        if is_prime_factorization(factors):
            continue
        rows.append(stats_for_number(n, factors, tau[n], primes))
    return nlargest(top_k, rows, key=lambda row: (row["reduction"], row["n"]))


def semiprime_examples(limit: int, spf: list[int], tau: list[int], primes: list[int], top_k: int) -> list[dict[str, object]]:
    rows = []
    for n in range(4, limit + 1):
        factors = factorize(n, spf)
        if not is_semiprime_factorization(factors):
            continue
        rows.append(stats_for_number(n, factors, tau[n], primes))
    rows.sort(key=lambda row: (row["n"], row["reduction"]))
    return rows[-top_k:]


def print_rows(title: str, rows: list[dict[str, object]]) -> None:
    print()
    print(title)
    for row in rows:
        factor_text = format_factorization(row["factors"])
        reduction_pct = 100.0 * float(row["reduction"])
        print(
            f"n={row['n']}, factors={factor_text}, tau={row['tau']}, "
            f"sqrt(n)={row['sqrt']}, pi(sqrt(n))={row['naive']}, "
            f"pi(min(tau,sqrt))={row['filtered']}, reduction={reduction_pct:.1f}%"
        )


def parse_numbers(raw: str | None) -> list[int]:
    if not raw:
        return []
    return [int(part.strip()) for part in raw.split(",") if part.strip()]


def default_demo_numbers(limit: int) -> list[int]:
    candidates = [
        216,
        20736,
        65536,
        531441,
        720720,
        99991 * 2,
        1009 * 1013,
        101 * 103,
    ]
    return [n for n in candidates if n <= limit]


def verify_fast_tau(verify_limit: int, tau: list[int]) -> None:
    slow = slow_tau_up_to(verify_limit)
    for n in range(1, verify_limit + 1):
        if slow[n] != tau[n]:
            raise ValueError(f"Fast tau mismatch at n={n}: {tau[n]} != {slow[n]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Probe factorization heuristics from era bounds.")
    parser.add_argument("--limit", type=int, default=200_000, help="largest integer to analyze")
    parser.add_argument("--top-k", type=int, default=12, help="how many strongest reductions to print")
    parser.add_argument(
        "--numbers",
        type=str,
        default="",
        help="comma-separated list of specific integers to inspect",
    )
    parser.add_argument(
        "--verify-limit",
        type=int,
        default=0,
        help="cross-check the fast tau formula against the slow recursive definition up to this bound",
    )
    args = parser.parse_args()

    spf = smallest_prime_factors(args.limit)
    primes = primes_from_spf(spf)
    tau = tau_up_to(args.limit, spf)

    if args.verify_limit > 0:
        verify_fast_tau(min(args.verify_limit, args.limit), tau)
        print(f"Verified fast tau against the slow recursive definition through {min(args.verify_limit, args.limit)}.")

    demo_numbers = parse_numbers(args.numbers) or default_demo_numbers(args.limit)
    demo_rows = []
    for n in demo_numbers:
        factors = factorize(n, spf)
        demo_rows.append(stats_for_number(n, factors, tau[n], primes))

    print(f"Computed exact era data through {args.limit}.")
    print_rows("Selected examples", demo_rows)
    print_rows(
        f"Top {args.top_k} candidate-prime reductions among composites through {args.limit}",
        top_reductions(args.limit, spf, tau, primes, args.top_k),
    )
    print_rows(
        f"Semiprime contrast cases near {args.limit}",
        semiprime_examples(args.limit, spf, tau, primes, min(args.top_k, 8)),
    )


if __name__ == "__main__":
    main()
