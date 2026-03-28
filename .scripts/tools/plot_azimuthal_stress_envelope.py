from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR / "data" / "azimuthal_stress_demo_disk.csv"
DEFAULT_OUTPUT_DIR = Path("reports") / "azimuthal-stress-envelope"
REQUIRED_COLUMNS = ("radius_kpc", "v_obs_kms", "v_bar_kms", "k_kms")


@dataclass
class GalaxySeries:
    name: str
    radius_kpc: np.ndarray
    v_obs_kms: np.ndarray
    v_bar_kms: np.ndarray
    k_kms: np.ndarray

    @property
    def delta_v2(self) -> np.ndarray:
        return self.v_obs_kms**2 - self.v_bar_kms**2

    @property
    def ratio(self) -> np.ndarray:
        return self.delta_v2 / (self.k_kms**2)

    @property
    def upper_speed_envelope(self) -> np.ndarray:
        return np.sqrt(np.maximum(self.v_bar_kms**2 + self.k_kms**2, 0.0))

    @property
    def inside_mask(self) -> np.ndarray:
        ratio = self.ratio
        return (ratio >= 0.0) & (ratio <= 1.0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Plot the azimuthal-stress envelope derived in TPOEF Part III from "
            "rotation-curve inputs."
        )
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        type=Path,
        help=(
            "CSV files with columns radius_kpc,v_obs_kms,v_bar_kms,k_kms and "
            "optional name."
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory where plots will be written. Default: {DEFAULT_OUTPUT_DIR}",
    )
    return parser.parse_args()


def read_series(path: Path) -> GalaxySeries:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path} has no header row")
        missing = [column for column in REQUIRED_COLUMNS if column not in reader.fieldnames]
        if missing:
            raise ValueError(f"{path} is missing required columns: {', '.join(missing)}")

        radius: list[float] = []
        v_obs: list[float] = []
        v_bar: list[float] = []
        k_values: list[float] = []
        names: list[str] = []

        for row_number, row in enumerate(reader, start=2):
            try:
                radius_value = float(row["radius_kpc"])
                v_obs_value = float(row["v_obs_kms"])
                v_bar_value = float(row["v_bar_kms"])
                k_value = float(row["k_kms"])
            except ValueError as exc:
                raise ValueError(f"{path}:{row_number} contains a non-numeric value") from exc

            if radius_value < 0:
                raise ValueError(f"{path}:{row_number} has negative radius_kpc")
            if v_obs_value < 0 or v_bar_value < 0:
                raise ValueError(f"{path}:{row_number} has negative speed data")
            if k_value <= 0:
                raise ValueError(f"{path}:{row_number} must have positive k_kms")

            radius.append(radius_value)
            v_obs.append(v_obs_value)
            v_bar.append(v_bar_value)
            k_values.append(k_value)
            name = (row.get("name") or "").strip()
            if name:
                names.append(name)

    if not radius:
        raise ValueError(f"{path} has no data rows")

    order = np.argsort(np.asarray(radius, dtype=float))
    series = GalaxySeries(
        name=names[0] if names else path.stem,
        radius_kpc=np.asarray(radius, dtype=float)[order],
        v_obs_kms=np.asarray(v_obs, dtype=float)[order],
        v_bar_kms=np.asarray(v_bar, dtype=float)[order],
        k_kms=np.asarray(k_values, dtype=float)[order],
    )
    return series


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "galaxy"


def plot_series(series: GalaxySeries, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    ratio = series.ratio
    inside_mask = series.inside_mask
    outside_mask = ~inside_mask
    max_ratio = max(1.05, float(np.nanmax(ratio)) + 0.1)

    fig, (ax_speed, ax_ratio) = plt.subplots(
        2,
        1,
        figsize=(10.5, 8.0),
        sharex=True,
        gridspec_kw={"height_ratios": [3.0, 2.0]},
        constrained_layout=True,
    )

    fig.patch.set_facecolor("#fbf8f1")

    radius = series.radius_kpc
    upper = series.upper_speed_envelope

    ax_speed.set_facecolor("#fffdf8")
    ax_speed.fill_between(
        radius,
        series.v_bar_kms,
        upper,
        color="#f2d9a0",
        alpha=0.45,
        label=r"Envelope: $v_{\mathrm{bar}} \leq v_{\mathrm{obs}} \leq \sqrt{v_{\mathrm{bar}}^2+k^2}$",
    )
    ax_speed.plot(radius, series.v_bar_kms, color="#bf6d2f", linewidth=2.0, label=r"$v_{\mathrm{bar}}$")
    ax_speed.plot(radius, upper, color="#8f6f1f", linewidth=1.5, linestyle="--", label=r"$\sqrt{v_{\mathrm{bar}}^2+k^2}$")
    ax_speed.plot(radius, series.v_obs_kms, color="#145c6a", linewidth=2.4, marker="o", label=r"$v_{\mathrm{obs}}$")
    if np.any(outside_mask):
        ax_speed.scatter(
            radius[outside_mask],
            series.v_obs_kms[outside_mask],
            color="#a61e4d",
            s=48,
            zorder=5,
            label="Outside envelope",
        )
    ax_speed.set_ylabel("Speed [km/s]")
    ax_speed.set_title(f"{series.name}: azimuthal-stress envelope")
    ax_speed.grid(True, alpha=0.25)
    ax_speed.legend(loc="best", fontsize=9)

    ax_ratio.set_facecolor("#f8fbff")
    ax_ratio.axhspan(0.0, 1.0, color="#d9edf7", alpha=0.65, label=r"Admissible band: $0 \leq \Delta v_\phi^2/k^2 \leq 1$")
    ax_ratio.axhline(0.0, color="#4f6d7a", linewidth=1.0)
    ax_ratio.axhline(1.0, color="#4f6d7a", linewidth=1.0, linestyle="--")
    ax_ratio.plot(radius, ratio, color="#145c6a", linewidth=2.2, marker="o", label=r"$\Delta v_\phi^2/k^2$")
    ax_ratio.scatter(radius[inside_mask], ratio[inside_mask], color="#145c6a", s=28, zorder=4)
    if np.any(outside_mask):
        ax_ratio.scatter(radius[outside_mask], ratio[outside_mask], color="#a61e4d", s=42, zorder=5)
    ax_ratio.set_xlabel("Radius [kpc]")
    ax_ratio.set_ylabel(r"$\Delta v_\phi^2 / k^2$")
    ax_ratio.set_ylim(min(-0.1, float(np.nanmin(ratio)) - 0.1), max_ratio)
    ax_ratio.grid(True, alpha=0.25)
    ax_ratio.legend(loc="best", fontsize=9)

    inside_count = int(np.count_nonzero(inside_mask))
    total_count = int(radius.size)
    fig.suptitle(
        (
            f"{series.name} envelope diagnostic\n"
            f"inside={inside_count}/{total_count}, "
            f"ratio_min={float(np.nanmin(ratio)):.3f}, "
            f"ratio_max={float(np.nanmax(ratio)):.3f}"
        ),
        fontsize=13,
        color="#2a2a2a",
    )

    output_path = output_dir / f"{slugify(series.name)}-envelope.png"
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def print_summary(series: GalaxySeries, output_path: Path) -> None:
    ratio = series.ratio
    inside_count = int(np.count_nonzero(series.inside_mask))
    total_count = int(series.radius_kpc.size)
    print(f"{series.name}: {inside_count}/{total_count} points inside envelope")
    print(f"  ratio min/max: {float(np.min(ratio)):.3f} / {float(np.max(ratio)):.3f}")
    print(f"  plot: {output_path}")
    outside_mask = ~series.inside_mask
    if np.any(outside_mask):
        radii = ", ".join(f"{value:.2f}" for value in series.radius_kpc[outside_mask])
        print(f"  outside radii [kpc]: {radii}")


def main() -> int:
    args = parse_args()
    input_paths = args.inputs or [DEFAULT_INPUT]

    for input_path in input_paths:
        resolved = input_path if input_path.is_absolute() else Path.cwd() / input_path
        series = read_series(resolved)
        output_path = plot_series(series, args.output_dir)
        print_summary(series, output_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
