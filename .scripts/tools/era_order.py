from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import gcd, isqrt
from pathlib import Path


CACHE_VERSION = 1
DEFAULT_CACHE = Path(".scripts/cache/era_order_cache.json")


def power_cost(n: int) -> int:
    """Least generator ceiling needed to realize n as a^b with b >= 1."""
    best = n
    max_b = n.bit_length() + 1
    for b in range(2, max_b + 1):
        lo = 2
        hi = n
        while lo <= hi:
            mid = (lo + hi) // 2
            value = mid**b
            if value == n:
                best = min(best, max(mid, b))
                break
            if value < n:
                lo = mid + 1
            else:
                hi = mid - 1
    return best


def load_cache(cache_path: Path) -> list[int]:
    if not cache_path.exists():
        return [0, 1]

    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return [0, 1]

    if data.get("version") != CACHE_VERSION:
        return [0, 1]

    tau = data.get("tau")
    if not isinstance(tau, list) or len(tau) < 2:
        return [0, 1]

    if tau[0] != 0 or tau[1] != 1:
        return [0, 1]

    return [int(value) for value in tau]


def save_cache(cache_path: Path, tau: list[int]) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": CACHE_VERSION,
        "limit": len(tau) - 1,
        "tau": tau,
    }
    cache_path.write_text(json.dumps(payload), encoding="utf-8")


def ensure_tau(limit: int, cache_path: Path) -> tuple[list[int], str]:
    tau = load_cache(cache_path)
    cached_limit = len(tau) - 1

    if limit <= cached_limit:
        return tau[: limit + 1], f"Loaded cached eras through {cached_limit}."

    tau.extend([0] * (limit - cached_limit))
    start = max(2, cached_limit + 1)
    for n in range(start, limit + 1):
        best = power_cost(n)
        for a in range(2, isqrt(n) + 1):
            if n % a != 0:
                continue
            b = n // a
            if gcd(a, b) != 1:
                continue
            best = min(best, max(tau[a], tau[b]))
        tau[n] = best

    save_cache(cache_path, tau)
    return tau, f"Extended cache from {cached_limit} to {limit}."


def era_sets(tau: list[int]) -> dict[int, list[int]]:
    eras: dict[int, list[int]] = defaultdict(list)
    for n in range(1, len(tau)):
        eras[tau[n]].append(n)
    return dict(sorted(eras.items()))


def cumulative_sorted(tau: list[int], max_era: int) -> list[int]:
    return sorted(n for n in range(1, len(tau)) if tau[n] <= max_era)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


def prime_frontier_histogram(values: list[int], bin_size: int) -> list[tuple[int, int]]:
    bins: dict[int, int] = defaultdict(int)
    for n in values:
        if is_prime(n):
            bins[(n - 1) // bin_size] += 1
    return sorted((k * bin_size + 1, count) for k, count in bins.items())


def print_era(era: int, values: list[int]) -> None:
    print(f"era {era}: {values}")


def ask_continue(next_era: int, values: list[int], limit: int) -> bool:
    count = len(values)
    lo = values[0]
    hi = values[-1]
    answer = input(
        f"\nContinue to era {next_era}? "
        f"({count} numbers through {limit}, range {lo}..{hi}) [y/N]: "
    ).strip().lower()
    return answer in {"y", "yes"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute causal eras for integers.")
    parser.add_argument("--limit", type=int, default=1000, help="largest integer to compute")
    parser.add_argument(
        "--through-era",
        type=int,
        default=10,
        help="print eras through this level before prompting",
    )
    parser.add_argument(
        "--cache-file",
        type=Path,
        default=DEFAULT_CACHE,
        help="JSON cache file for tau values",
    )
    parser.add_argument(
        "--no-prompt",
        action="store_true",
        help="stop after --through-era instead of prompting to continue",
    )
    parser.add_argument(
        "--show-cumulative",
        action="store_true",
        help="print the cumulative sorted set through the last displayed era",
    )
    parser.add_argument(
        "--bin-size",
        type=int,
        default=100,
        help="prime histogram bin size; set to 0 to suppress histogram",
    )
    args = parser.parse_args()

    if args.limit < 1:
        raise ValueError("--limit must be at least 1")

    tau, cache_message = ensure_tau(args.limit, args.cache_file)
    eras = era_sets(tau)
    all_eras = sorted(eras)

    print(cache_message)
    print(f"Computed tau(n) for 1 <= n <= {args.limit}.")
    print()
    print("Era sets")

    displayed_era = 0
    stop_era = args.through_era
    for era in all_eras:
        if era > stop_era:
            break
        print_era(era, eras[era])
        displayed_era = era

    if not args.no_prompt:
        for era in all_eras:
            if era <= stop_era:
                continue
            if not ask_continue(era, eras[era], args.limit):
                break
            print_era(era, eras[era])
            displayed_era = era

    if displayed_era == 0:
        return

    values = cumulative_sorted(tau, displayed_era)

    if args.show_cumulative:
        print()
        print(f"Cumulative sorted values through era {displayed_era}:")
        print(values)

    if args.bin_size > 0:
        print()
        print(f"Prime histogram (bin size {args.bin_size}) through era {displayed_era}:")
        for start, count in prime_frontier_histogram(values, args.bin_size):
            end = start + args.bin_size - 1
            print(f"[{start:>5}, {end:>5}]  {count}")


if __name__ == "__main__":
    main()
