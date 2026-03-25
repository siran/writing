from __future__ import annotations

import argparse
import json
from math import isqrt, log10
from pathlib import Path
from time import perf_counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


CACHE_VERSION = 3
DEFAULT_CACHE = Path(".scripts/cache/era_order_cache.json")
DEFAULT_LATEST_PLOT = Path(".scripts/cache/era_order_latest.png")
DEFAULT_PLOT_DIR = Path(".scripts/cache/era_order_plots")
DEFAULT_DENSE_XMAX = None
MATERIALIZE_LIMIT = 100_000
MAX_LINEAR_PLOT_INT = 10**300
GLOBAL_LOG10_THRESHOLD = 10**6


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


def full_channels(era: int) -> dict[str, list[int]]:
    return {str(prime): available_prime_powers(prime, era) for prime in primes_up_to(era)}


def channel_product_count(channels: dict[str, list[int]]) -> int:
    total = 1
    for values in channels.values():
        total *= 1 + len(values)
    return total


def channel_max_product(channels: dict[str, list[int]]) -> int:
    total = 1
    for values in channels.values():
        if values:
            total *= values[-1]
    return total


def diff_channels(
    old_channels: dict[str, list[int]],
    new_channels: dict[str, list[int]],
) -> dict[str, list[int]]:
    delta: dict[str, list[int]] = {}
    for prime_text, new_values in new_channels.items():
        old_set = set(old_channels.get(prime_text, []))
        delta_values = [value for value in new_values if value not in old_set]
        if delta_values:
            delta[prime_text] = delta_values
    return delta


def min_new_value(delta_channels: dict[str, list[int]]) -> int:
    return min(values[0] for values in delta_channels.values())


def materialize_delta_values(
    old_channels: dict[str, list[int]],
    new_channels: dict[str, list[int]],
    checkpoint_every: int = 0,
    checkpoint_callback=None,
) -> list[int]:
    primes = sorted(int(key) for key in new_channels)
    delta_sets = {
        prime: set(diff_channels(old_channels, new_channels).get(str(prime), []))
        for prime in primes
    }
    values: list[int] = []
    processed = 0
    current_max = 1

    def walk(index: int, product: int, used_new: bool) -> None:
        nonlocal processed, current_max
        if index == len(primes):
            if used_new:
                values.append(product)
                processed += 1
                current_max = max(current_max, product)
                if (
                    checkpoint_every > 0
                    and checkpoint_callback is not None
                    and processed % checkpoint_every == 0
                ):
                    checkpoint_callback(processed, current_max)
            return

        prime = primes[index]
        prime_text = str(prime)
        walk(index + 1, product, used_new)
        for value in new_channels[prime_text]:
            walk(index + 1, product * value, used_new or (value in delta_sets[prime]))

    walk(0, 1, False)
    values.sort()
    return values


def format_duration(seconds: float) -> str:
    if seconds < 1e-3:
        return f"{seconds * 1e6:.1f} us"
    if seconds < 1:
        return f"{seconds * 1e3:.1f} ms"
    return f"{seconds:.3f} s"


def summarize_head_tail(values: list[int]) -> tuple[list[int], list[int]]:
    if len(values) <= 13:
        return values, values
    return values[:8], values[-5:]


def era_summary_from_values(era: int, values: list[int]) -> dict[str, object]:
    head, tail = summarize_head_tail(values)
    return {
        "era": era,
        "count": len(values),
        "min": values[0],
        "max": values[-1],
        "head": head,
        "tail": tail,
        "materialized": True,
    }


def era_summary_from_channels(
    era: int,
    old_channels: dict[str, list[int]],
    new_channels: dict[str, list[int]],
    checkpoint_every: int = 0,
    checkpoint_callback=None,
) -> dict[str, object]:
    old_count = channel_product_count(old_channels)
    new_count = channel_product_count(new_channels)
    delta_channels = diff_channels(old_channels, new_channels)
    count = new_count - old_count
    summary = {
        "era": era,
        "count": count,
        "min": min_new_value(delta_channels),
        "max": channel_max_product(new_channels),
        "head": [],
        "tail": [],
        "materialized": False,
    }

    if count <= MATERIALIZE_LIMIT:
        values = materialize_delta_values(
            old_channels,
            new_channels,
            checkpoint_every=checkpoint_every,
            checkpoint_callback=checkpoint_callback,
        )
        summary = era_summary_from_values(era, values)
    return summary


def new_state() -> dict:
    return {
        "version": CACHE_VERSION,
        "current_era": 1,
        "channels": {},
        "era_summaries": {
            "1": {
                "era": 1,
                "count": 1,
                "min": 1,
                "max": 1,
                "head": [1],
                "tail": [1],
                "materialized": True,
            }
        },
        "admitted_count": 1,
        "max_admitted": 1,
        "primes": [],
        "timings": {},
    }


def migrate_v2(data: dict) -> dict:
    current_era = int(data.get("current_era", 1))
    era_summaries: dict[str, dict[str, object]] = {}
    for era_text, values in data.get("era_sets", {}).items():
        int_values = sorted(int(n) for n in values)
        era_summaries[str(era_text)] = era_summary_from_values(int(era_text), int_values)

    admitted = sorted(int(n) for n in data.get("admitted", [1]))
    return {
        "version": CACHE_VERSION,
        "current_era": current_era,
        "channels": data.get("channels", {}),
        "era_summaries": era_summaries or new_state()["era_summaries"],
        "admitted_count": len(admitted),
        "max_admitted": admitted[-1] if admitted else 1,
        "primes": primes_up_to(current_era),
        "timings": data.get("timings", {}),
    }


def load_cache(cache_path: Path) -> dict:
    if not cache_path.exists():
        return new_state()

    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return new_state()

    version = data.get("version")
    if version == 2:
        return migrate_v2(data)
    if version != CACHE_VERSION:
        return new_state()

    required = {
        "current_era",
        "channels",
        "era_summaries",
        "admitted_count",
        "max_admitted",
        "primes",
        "timings",
    }
    if not required.issubset(data):
        return new_state()
    return data


def save_cache(cache_path: Path, state: dict) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(state), encoding="utf-8")


def preview_next_era(state: dict) -> dict[str, object]:
    next_era = int(state["current_era"]) + 1
    old_channels = {key: [int(v) for v in values] for key, values in state["channels"].items()}
    new_channels = full_channels(next_era)
    return era_summary_from_channels(next_era, old_channels, new_channels)


def extend_one_era(
    state: dict,
    checkpoint_every: int = 0,
    checkpoint_callback=None,
) -> tuple[dict, dict[str, object], float]:
    next_era = int(state["current_era"]) + 1
    old_channels = {key: [int(v) for v in values] for key, values in state["channels"].items()}

    started = perf_counter()
    new_channels = full_channels(next_era)
    summary = era_summary_from_channels(
        next_era,
        old_channels,
        new_channels,
        checkpoint_every=checkpoint_every,
        checkpoint_callback=checkpoint_callback,
    )
    elapsed = perf_counter() - started

    state["current_era"] = next_era
    state["channels"] = new_channels
    state["era_summaries"][str(next_era)] = summary
    state["admitted_count"] = channel_product_count(new_channels)
    state["max_admitted"] = channel_max_product(new_channels)
    state["primes"] = primes_up_to(next_era)
    state["timings"][str(next_era)] = elapsed
    return state, summary, elapsed


def plot_points(state: dict) -> tuple[list[int], list[int]]:
    primes = [int(p) for p in state["primes"]]
    max_admitted = int(state["max_admitted"])
    x = [1]
    y = [0]
    for count, prime in enumerate(primes, start=1):
        x.append(prime)
        y.append(count)
    if max_admitted > x[-1]:
        x.append(max_admitted)
        y.append(len(primes))
    return x, y


def dense_plot_limit(state: dict, dense_xmax: int | None) -> int:
    if dense_xmax is None:
        return max(1, int(state["current_era"]))
    return max(1, dense_xmax)


def dense_local_points(state: dict, dense_xmax: int) -> tuple[list[int], list[int]]:
    primes = [int(p) for p in state["primes"]]
    x = list(range(1, dense_xmax + 1))
    y: list[int] = []
    count = 0
    prime_index = 0
    while prime_index < len(primes) and primes[prime_index] < 1:
        prime_index += 1
    for value in x:
        while prime_index < len(primes) and primes[prime_index] <= value:
            count += 1
            prime_index += 1
        y.append(count)
    return x, y


def log10_bigint(n: int) -> float:
    if n <= 0:
        raise ValueError("log10_bigint requires a positive integer")
    if n <= MAX_LINEAR_PLOT_INT:
        return log10(n)
    bits = n.bit_length()
    keep = 53
    shift = max(0, bits - keep)
    mantissa = n >> shift
    return log10(mantissa) + shift * log10(2)


def save_plot(state: dict, plot_path: Path, dense_xmax: int | None) -> None:
    x_dense, y_dense = dense_local_points(state, dense_plot_limit(state, dense_xmax))
    x_global, y_global = plot_points(state)
    use_log10 = any(value > MAX_LINEAR_PLOT_INT for value in x_global) or int(
        state["max_admitted"]
    ) > GLOBAL_LOG10_THRESHOLD
    x_global_plot = [log10_bigint(value) for value in x_global] if use_log10 else x_global
    plot_path.parent.mkdir(parents=True, exist_ok=True)
    fig, (ax_top, ax_bottom) = plt.subplots(
        2,
        1,
        figsize=(9, 7.5),
        gridspec_kw={"height_ratios": [3, 2]},
    )
    fig.suptitle(f"Era-truncated prime counting through era {state['current_era']}")

    ax_top.step(x_dense, y_dense, where="post", linewidth=1.6, color="#0b5c7a")
    if len(x_dense) <= 2_000:
        ax_top.scatter(x_dense, y_dense, s=12, color="#0b5c7a")
    ax_top.set_xlabel("x")
    ax_top.set_ylabel("pi_E(x)")
    ax_top.set_title(f"Dense local staircase on 1..{x_dense[-1]}")
    ax_top.grid(alpha=0.25)

    ax_bottom.step(x_global_plot, y_global, where="post", linewidth=1.8, color="#b03a2e")
    if use_log10:
        ax_bottom.set_xlabel("log10(N)")
        ax_bottom.set_title("Global frontier of pi_E(N) (log10 scale on N)")
    else:
        ax_bottom.set_xlabel("N")
        ax_bottom.set_title("Global frontier of pi_E(N)")
    ax_bottom.set_ylabel("pi_E(N)")
    ax_bottom.grid(alpha=0.25)

    fig.tight_layout()
    fig.savefig(plot_path, dpi=160)
    plt.close(fig)


def save_plot_set(
    state: dict,
    latest_plot: Path,
    plot_dir: Path,
    tag: str,
    dense_xmax: int | None,
) -> None:
    save_plot(state, latest_plot, dense_xmax)
    plot_dir.mkdir(parents=True, exist_ok=True)
    save_plot(state, plot_dir / tag, dense_xmax)


def checkpoint_callback_factory(
    state: dict,
    next_era: int,
    latest_plot: Path,
    plot_dir: Path,
    dense_xmax: int | None,
):
    base_count = int(state["admitted_count"])
    base_max = int(state["max_admitted"])
    base_primes = [int(p) for p in state["primes"]]

    def callback(processed: int, current_max: int) -> None:
        preview = {
            **state,
            "current_era": next_era,
            "admitted_count": base_count + processed,
            "max_admitted": max(base_max, current_max),
            "primes": base_primes,
        }
        tag = f"era-{next_era:04d}-checkpoint-{processed:08d}.png"
        save_plot_set(preview, latest_plot, plot_dir, tag, dense_xmax)

    return callback


def format_summary(summary: dict[str, object]) -> str:
    era = int(summary["era"])
    count = int(summary["count"])
    lo = int(summary["min"])
    hi = int(summary["max"])
    if summary.get("materialized"):
        head = [int(n) for n in summary["head"]]
        tail = [int(n) for n in summary["tail"]]
        if head == tail:
            return f"era {era}: {head}"
        head_text = ", ".join(str(n) for n in head)
        tail_text = ", ".join(str(n) for n in tail)
        return f"era {era}: {count} numbers, range {lo}..{hi} [{head_text}, ..., {tail_text}]"
    return f"era {era}: {count} numbers, range {lo}..{hi}"


def print_state_summary(state: dict) -> None:
    current_era = int(state["current_era"])
    print(f"Known through era {current_era}.")
    print(f"Admitted integers: {int(state['admitted_count'])}")
    print(f"Range: 1..{int(state['max_admitted'])}")
    print()
    print("Known eras")
    for era_text in sorted(state["era_summaries"], key=lambda item: int(item)):
        print(format_summary(state["era_summaries"][era_text]))


def describe_estimate(state: dict, next_summary: dict[str, object]) -> str:
    current_era = int(state["current_era"])
    last_elapsed = state["timings"].get(str(current_era))
    next_count = int(next_summary["count"])
    if last_elapsed is None:
        return (
            f"Next era {int(next_summary['era'])} has {next_count} numbers "
            f"in range {int(next_summary['min'])}..{int(next_summary['max'])}."
        )
    last_summary = state["era_summaries"].get(str(current_era), {})
    last_count = int(last_summary.get("count", 1))
    scaled = last_elapsed * max(1.0, next_count / max(1, last_count))
    return (
        f"Next era {int(next_summary['era'])} has {next_count} numbers "
        f"in range {int(next_summary['min'])}..{int(next_summary['max'])}. "
        f"Last era took {format_duration(last_elapsed)}; scaled estimate for the next era is about {format_duration(scaled)}."
    )


def ask_more_eras(state: dict) -> int:
    next_summary = preview_next_era(state)
    print()
    print(describe_estimate(state, next_summary))
    answer = input("How many more eras should be computed? [0 to stop]: ").strip()
    if not answer:
        return 0
    extra_eras = max(0, int(answer))
    if extra_eras == 0:
        return 0

    last_elapsed = state["timings"].get(str(int(state["current_era"])))
    if last_elapsed is not None:
        rough = extra_eras * last_elapsed
        print(f"Very rough batch floor from the last era: {format_duration(rough)}.")
    return extra_eras


def run_batch(
    state: dict,
    extra_eras: int,
    cache_file: Path,
    latest_plot: Path,
    plot_dir: Path,
    checkpoint_every: int,
    dense_xmax: int | None,
) -> dict:
    for _ in range(extra_eras):
        next_era = int(state["current_era"]) + 1
        checkpoint_callback = None
        if checkpoint_every > 0:
            checkpoint_callback = checkpoint_callback_factory(
                state,
                next_era,
                latest_plot,
                plot_dir,
                dense_xmax,
            )
        state, summary, elapsed = extend_one_era(
            state,
            checkpoint_every=checkpoint_every,
            checkpoint_callback=checkpoint_callback,
        )
        save_cache(cache_file, state)
        save_plot_set(state, latest_plot, plot_dir, f"era-{next_era:04d}.png", dense_xmax)
        print()
        print(format_summary(summary))
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
        "--latest-plot",
        type=Path,
        default=DEFAULT_LATEST_PLOT,
        help="rolling latest plot image",
    )
    parser.add_argument(
        "--plot-dir",
        type=Path,
        default=DEFAULT_PLOT_DIR,
        help="directory for per-era plot snapshots",
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
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=0,
        help="save checkpoint plots every so many newly materialized values within an era",
    )
    parser.add_argument(
        "--dense-xmax",
        type=int,
        default=DEFAULT_DENSE_XMAX,
        help="pointwise staircase window for the dense local plot; defaults to the current era",
    )
    args = parser.parse_args()

    state = load_cache(args.cache_file)
    save_plot_set(
        state,
        args.latest_plot,
        args.plot_dir,
        f"era-{int(state['current_era']):04d}.png",
        args.dense_xmax,
    )
    print(f"Saved plots to {args.latest_plot} and {args.plot_dir}.")
    print()
    print_state_summary(state)

    if args.no_prompt:
        if args.add_eras:
            state = run_batch(
                state,
                args.add_eras,
                args.cache_file,
                args.latest_plot,
                args.plot_dir,
                args.checkpoint_every,
                args.dense_xmax,
            )
            print()
            print(f"Saved plots to {args.latest_plot} and {args.plot_dir}.")
        return

    while True:
        extra_eras = args.add_eras if args.add_eras is not None else ask_more_eras(state)
        args.add_eras = None
        if extra_eras <= 0:
            break
        state = run_batch(
            state,
            extra_eras,
            args.cache_file,
            args.latest_plot,
            args.plot_dir,
            args.checkpoint_every,
            args.dense_xmax,
        )
        print()
        print(f"Saved plots to {args.latest_plot} and {args.plot_dir}.")
        print()
        print_state_summary(state)


if __name__ == "__main__":
    main()
