from __future__ import annotations

import argparse
import json
from math import isqrt
from pathlib import Path
from time import perf_counter

import matplotlib.pyplot as plt


CACHE_VERSION = 2
DEFAULT_CACHE = Path(".scripts/cache/era_order_cache.json")
DEFAULT_PLOT = Path(".scripts/cache/era_order_pi.png")


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


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = False
    sieve[1] = False
    for n in range(2, isqrt(limit) + 1):
        if not sieve[n]:
            continue
        start = n * n
        step = n
        sieve[start : limit + 1 : step] = [False] * (((limit - start) // step) + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def available_exponents(prime: int, era: int) -> list[int]:
    exponents: set[int] = set()
    base = prime
    f = 1
    while base <= era:
        for b in range(1, era + 1):
            exponents.add(f * b)
        f += 1
        base *= prime
    return sorted(exponents)


def available_prime_powers(prime: int, era: int) -> list[int]:
    return [prime**exponent for exponent in available_exponents(prime, era)]


def build_channels(era: int) -> dict[str, list[int]]:
    channels: dict[str, list[int]] = {}
    for prime in primes_up_to(era):
        channels[str(prime)] = available_prime_powers(prime, era)
    return channels


def build_admitted(channels: dict[str, list[int]]) -> list[int]:
    admitted = {1}
    for prime in sorted(int(key) for key in channels):
        prime_powers = channels[str(prime)]
        current = list(admitted)
        for base in current:
            for value in prime_powers:
                admitted.add(base * value)
    return sorted(admitted)


def new_state() -> dict:
    return {
        "version": CACHE_VERSION,
        "current_era": 1,
        "channels": {},
        "era_sets": {"1": [1]},
        "admitted": [1],
        "timings": {},
    }


def load_cache(cache_path: Path) -> dict:
    if not cache_path.exists():
        return new_state()

    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return new_state()

    if data.get("version") != CACHE_VERSION:
        return new_state()

    required = {"current_era", "channels", "era_sets", "admitted", "timings"}
    if not required.issubset(data):
        return new_state()

    if data["admitted"] != sorted(set(int(n) for n in data["admitted"])):
        return new_state()

    return data


def save_cache(cache_path: Path, state: dict) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(state), encoding="utf-8")


def extend_one_era(state: dict) -> tuple[dict, float]:
    next_era = int(state["current_era"]) + 1
    started = perf_counter()

    channels = build_channels(next_era)
    admitted = build_admitted(channels)

    previous_admitted = set(int(n) for n in state["admitted"])
    new_values = sorted(n for n in admitted if n not in previous_admitted)

    state["current_era"] = next_era
    state["channels"] = channels
    state["admitted"] = admitted
    state["era_sets"][str(next_era)] = new_values

    elapsed = perf_counter() - started
    state["timings"][str(next_era)] = elapsed
    return state, elapsed


def prime_count_curve(values: list[int]) -> tuple[list[int], list[int]]:
    x: list[int] = []
    y: list[int] = []
    count = 0
    for value in values:
        if is_prime(value):
            count += 1
        x.append(value)
        y.append(count)
    return x, y


def save_plot(state: dict, plot_path: Path) -> None:
    values = [int(n) for n in state["admitted"]]
    x, y = prime_count_curve(values)

    plot_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(9, 5.5))
    plt.step(x, y, where="post", linewidth=1.6, color="#0b5c7a")
    plt.scatter(x, y, s=8, color="#b03a2e")
    plt.xlabel("N")
    plt.ylabel("p(N)")
    plt.title(f"Prime count recovered from era-bounded admission through era {state['current_era']}")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(plot_path, dpi=160)
    plt.close()


def format_duration(seconds: float) -> str:
    if seconds < 1e-3:
        return f"{seconds * 1e6:.1f} us"
    if seconds < 1:
        return f"{seconds * 1e3:.1f} ms"
    return f"{seconds:.3f} s"


def summarize_era(era: int, values: list[int]) -> str:
    count = len(values)
    lo = values[0]
    hi = values[-1]
    if count <= 24:
        return f"era {era}: {values}"
    head = ", ".join(str(n) for n in values[:8])
    tail = ", ".join(str(n) for n in values[-5:])
    return (
        f"era {era}: {count} numbers, range {lo}..{hi} "
        f"[{head}, ..., {tail}]"
    )


def print_state_summary(state: dict) -> None:
    admitted = [int(n) for n in state["admitted"]]
    current_era = int(state["current_era"])
    print(f"Known through era {current_era}.")
    print(f"Admitted integers: {len(admitted)}")
    print(f"Range: {admitted[0]}..{admitted[-1]}")
    print()
    print("Known eras")
    for era_text in sorted(state["era_sets"], key=lambda item: int(item)):
        era = int(era_text)
        values = [int(n) for n in state["era_sets"][era_text]]
        print(summarize_era(era, values))


def describe_estimate(state: dict) -> str:
    current_era = int(state["current_era"])
    last_elapsed = state["timings"].get(str(current_era))
    if last_elapsed is None:
        return "No timing history yet for the next era."
    return (
        f"Last computed era ({current_era}) took about {format_duration(last_elapsed)}. "
        "The next era should be of the same order or slower."
    )


def ask_more_eras(state: dict) -> int:
    print()
    print(describe_estimate(state))
    answer = input("How many more eras should be computed? [0 to stop]: ").strip()
    if not answer:
        return 0
    extra_eras = max(0, int(answer))
    if extra_eras == 0:
        return 0

    current_era = int(state["current_era"])
    last_elapsed = state["timings"].get(str(current_era))
    if last_elapsed is not None:
        rough = extra_eras * last_elapsed
        print(f"Rough batch estimate from the last era: {format_duration(rough)}.")
    return extra_eras


def run_batch(state: dict, extra_eras: int) -> dict:
    for _ in range(extra_eras):
        next_era = int(state["current_era"]) + 1
        state, elapsed = extend_one_era(state)
        values = [int(n) for n in state["era_sets"][str(next_era)]]
        print()
        print(summarize_era(next_era, values))
        print(f"elapsed: {format_duration(elapsed)}")
    return state


def main() -> None:
    parser = argparse.ArgumentParser(description="Explore era-bounded integer generation.")
    parser.add_argument(
        "--cache-file",
        type=Path,
        default=DEFAULT_CACHE,
        help="JSON cache file for the era explorer",
    )
    parser.add_argument(
        "--plot-file",
        type=Path,
        default=DEFAULT_PLOT,
        help="image file for the saved p(N) plot",
    )
    parser.add_argument(
        "--add-eras",
        type=int,
        default=None,
        help="compute this many more eras and stop",
    )
    parser.add_argument(
        "--no-prompt",
        action="store_true",
        help="do not ask interactively; requires --add-eras for extensions",
    )
    args = parser.parse_args()

    state = load_cache(args.cache_file)
    save_plot(state, args.plot_file)
    print(f"Saved plot to {args.plot_file}.")
    print()
    print_state_summary(state)

    if args.no_prompt:
        if args.add_eras:
            state = run_batch(state, args.add_eras)
            save_cache(args.cache_file, state)
            save_plot(state, args.plot_file)
            print()
            print(f"Saved plot to {args.plot_file}.")
        return

    while True:
        extra_eras = args.add_eras if args.add_eras is not None else ask_more_eras(state)
        args.add_eras = None
        if extra_eras <= 0:
            break
        state = run_batch(state, extra_eras)
        save_cache(args.cache_file, state)
        save_plot(state, args.plot_file)
        print()
        print(f"Saved plot to {args.plot_file}.")
        print()
        print_state_summary(state)


if __name__ == "__main__":
    main()
