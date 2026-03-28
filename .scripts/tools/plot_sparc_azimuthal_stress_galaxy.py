from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path

import matplotlib
import requests

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
BOOK_FIGURES_DIR = Path("books") / "The Physics of Energy Flow" / "figures"
SPARC_CACHE_DIR = SCRIPT_DIR / "data" / "sparc"
SPARC_URL = "https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt"
DEFAULT_GALAXIES = ("NGC3198",)
FIDUCIAL_ML_DISK = 0.5
FIDUCIAL_ML_BULGE = 0.7
TREFOIL_M = 3
TREFOIL_N = 2


@dataclass
class SparcGalaxy:
    identifier: str
    radius_kpc: np.ndarray
    v_obs_kms: np.ndarray
    v_obs_err_kms: np.ndarray
    v_gas_kms: np.ndarray
    v_disk_unit_ml_kms: np.ndarray
    v_bulge_unit_ml_kms: np.ndarray

    @property
    def display_name(self) -> str:
        match = re.fullmatch(r"([A-Z]+)(\d+)", self.identifier)
        if match:
            return f"{match.group(1)} {match.group(2)}"
        return self.identifier

    @property
    def v_bar2_visible(self) -> np.ndarray:
        gas_term = self.v_gas_kms * np.abs(self.v_gas_kms)
        disk_term = FIDUCIAL_ML_DISK * self.v_disk_unit_ml_kms**2
        bulge_term = FIDUCIAL_ML_BULGE * self.v_bulge_unit_ml_kms**2
        return np.maximum(gas_term + disk_term + bulge_term, 0.0)

    @property
    def v_bar_visible(self) -> np.ndarray:
        return np.sqrt(self.v_bar2_visible)

    @property
    def delta_v2(self) -> np.ndarray:
        return np.maximum(self.v_obs_kms**2 - self.v_bar2_visible, 0.0)

    @property
    def v_stress_required(self) -> np.ndarray:
        return np.sqrt(self.delta_v2)

    @property
    def trefoil32_fraction(self) -> float:
        numerator = 4.0 * TREFOIL_M**2
        denominator = numerator + TREFOIL_N**2
        return numerator / denominator

    @property
    def delta_v2_trefoil32(self) -> np.ndarray:
        return self.trefoil32_fraction * self.v_bar2_visible

    @property
    def v_stress_trefoil32(self) -> np.ndarray:
        return np.sqrt(self.delta_v2_trefoil32)

    @property
    def v_energy_flow_trefoil32(self) -> np.ndarray:
        return np.sqrt(self.v_bar2_visible + self.delta_v2_trefoil32)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Plot observed SPARC rotation curves against visible baryons and a "
            "baryonic-only trefoil energy-flow model for one or more galaxies."
        )
    )
    parser.add_argument(
        "galaxies",
        nargs="*",
        help="SPARC galaxy identifiers such as NGC3198 or DDO154.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=BOOK_FIGURES_DIR,
        help=f"Directory for the finished figure files. Default: {BOOK_FIGURES_DIR}",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=SPARC_CACHE_DIR,
        help=f"Directory used for cached SPARC tables and extracted CSV files. Default: {SPARC_CACHE_DIR}",
    )
    parser.add_argument(
        "--refresh-sparc",
        action="store_true",
        help="Redownload the SPARC machine-readable table even if a cache exists.",
    )
    return parser.parse_args()


def ensure_sparc_table(cache_path: Path, refresh: bool) -> Path:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.exists() and not refresh:
        return cache_path

    response = requests.get(SPARC_URL, timeout=30)
    response.raise_for_status()
    cache_path.write_text(response.text, encoding="utf-8")
    return cache_path


def parse_sparc_table(path: Path) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if len(raw_line) < 59:
            continue
        identifier = raw_line[0:11].strip()
        if not identifier:
            continue
        try:
            distance_mpc = float(raw_line[12:18])
            radius_kpc = float(raw_line[19:25])
            v_obs_kms = float(raw_line[26:32])
            v_obs_err_kms = float(raw_line[33:38])
            v_gas_kms = float(raw_line[39:45])
            v_disk_kms = float(raw_line[46:52])
            v_bulge_kms = float(raw_line[53:59])
        except ValueError:
            continue

        rows.append(
            {
                "identifier": identifier,
                "distance_mpc": distance_mpc,
                "radius_kpc": radius_kpc,
                "v_obs_kms": v_obs_kms,
                "v_obs_err_kms": v_obs_err_kms,
                "v_gas_kms": v_gas_kms,
                "v_disk_unit_ml_kms": v_disk_kms,
                "v_bulge_unit_ml_kms": v_bulge_kms,
            }
        )
    return rows


def build_galaxy(rows: list[dict[str, float | str]], identifier: str) -> SparcGalaxy:
    normalized = identifier.strip().upper().replace(" ", "")
    matched = [row for row in rows if str(row["identifier"]).upper().replace(" ", "") == normalized]
    if not matched:
        raise ValueError(f"Galaxy {identifier} not found in SPARC mass models")

    radius = np.asarray([float(row["radius_kpc"]) for row in matched], dtype=float)
    order = np.argsort(radius)
    return SparcGalaxy(
        identifier=str(matched[0]["identifier"]),
        radius_kpc=radius[order],
        v_obs_kms=np.asarray([float(row["v_obs_kms"]) for row in matched], dtype=float)[order],
        v_obs_err_kms=np.asarray([float(row["v_obs_err_kms"]) for row in matched], dtype=float)[order],
        v_gas_kms=np.asarray([float(row["v_gas_kms"]) for row in matched], dtype=float)[order],
        v_disk_unit_ml_kms=np.asarray([float(row["v_disk_unit_ml_kms"]) for row in matched], dtype=float)[order],
        v_bulge_unit_ml_kms=np.asarray([float(row["v_bulge_unit_ml_kms"]) for row in matched], dtype=float)[order],
    )


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "galaxy"


def export_extracted_csv(galaxy: SparcGalaxy, data_dir: Path) -> Path:
    data_dir.mkdir(parents=True, exist_ok=True)
    output_path = data_dir / f"{slugify(galaxy.display_name)}-sparc-visible-baryons.csv"
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "name",
                "radius_kpc",
                "v_obs_kms",
                "v_obs_err_kms",
                "v_gas_kms",
                "v_disk_unit_ml_kms",
                "v_bulge_unit_ml_kms",
                "v_bar_visible_kms",
                "v_stress_trefoil32_kms",
                "v_energy_flow_trefoil32_kms",
                "v_stress_required_kms",
                "trefoil32_fraction",
                "delta_v2_kms2",
            ]
        )
        for values in zip(
            galaxy.radius_kpc,
            galaxy.v_obs_kms,
            galaxy.v_obs_err_kms,
            galaxy.v_gas_kms,
            galaxy.v_disk_unit_ml_kms,
            galaxy.v_bulge_unit_ml_kms,
            galaxy.v_bar_visible,
            galaxy.v_stress_trefoil32,
            galaxy.v_energy_flow_trefoil32,
            galaxy.v_stress_required,
            galaxy.delta_v2,
            strict=True,
        ):
            writer.writerow(
                [
                    galaxy.display_name,
                    *[f"{value:.6f}" for value in values[:-1]],
                    f"{galaxy.trefoil32_fraction:.6f}",
                    f"{values[-1]:.6f}",
                ]
            )
    return output_path


def write_caption(galaxy: SparcGalaxy, output_dir: Path, image_filename: str) -> Path:
    caption_path = output_dir / f"{slugify(galaxy.display_name)}-observed-newtonian-and-trefoil32-energy-flow.md"
    caption = f"""# {galaxy.display_name}: Observed Rotation, Newtonian Baryons, and a Trefoil-Based Energy-Flow Curve

This figure is meant to be read in two steps.

The top panel shows three curves for the same galaxy.

- The dark points are the directly observed circular speed `V_obs(R)` from the SPARC mass-model table.
- The orange curve is the Newtonian visible-baryonic prediction `V_N(R)`, built from the SPARC gas, disk, and bulge components using the fiducial stellar mass-to-light choices quoted in the SPARC paper: `Upsilon_disk = 0.5` and `Upsilon_bulge = 0.7` at 3.6 um.
- The blue-green curve is the trefoil-based energy-flow calculation `V_EF,32(R)`, obtained from the baryons alone by assuming each baryonic closure is a coherent `(3,2)` trefoil flow.

The construction is stepwise.

1. Recover the visible-baryonic Newtonian curve from the SPARC gas, disk, and bulge pieces:

```text
V_N^2(R) = V_gas(R)|V_gas(R)| + 0.5 V_disk^2(R) + 0.7 V_bulge^2(R).
```

2. Assume each baryonic closure is a `(3,2)` trefoil with toroidal winding `m=3` and poloidal winding `n=2`.

3. Assume the azimuthal stress is carried by the toroidal winding, and that coherent same-base overlap strengthens that toroidal loading by the `4u` rule. This weights the toroidal contribution by `4m^2` while the poloidal contribution remains `n^2`.

4. Normalize that split to get the coherent azimuthal fraction

```text
f_32 = (4 m^2) / (4 m^2 + n^2) = 36 / 40 = 0.9.
```

5. Use that fraction to define the baryonic-only stress completion

```text
V_stress,32^2(R) = f_32 V_N^2(R),
```

and then recover the completed trefoil energy-flow curve

```text
V_EF,32^2(R) = V_N^2(R) + V_stress,32^2(R) = (1 + f_32) V_N^2(R).
```

This is not the observed gap inserted back into the curve. It is a baryonic-only trefoil ansatz built from the visible baryons together with the `(3,2)` and coherent-`4u` assumptions.

The bottom panel compares two different completion terms:

```text
V_stress,32(R) = sqrt(f_32) V_N(R)
```

from the baryonic-only trefoil model, and

```text
V_stress,req(R) = sqrt(max(V_obs^2(R) - V_N^2(R), 0))
```

required by the observed gap.

So the lower panel is the actual test. If the trefoil/coherence ansatz is sufficient, the blue model-completion curve should track the gray required-completion curve. If it stays below it, the baryonic trefoil ansatz underestimates the stress completion that the galaxy requires.

For NGC 3198, that is exactly what this first test shows: the `(3,2)` trefoil curve improves on the Newtonian baryonic curve, but it still sits below the observed outer rotation and below the required completion through most of the disk. So the construction is now honest and baryonic-only, but the present `(3,2)` plus coherent-`4u` weighting is not yet sufficient by itself.

In the language of the book, the required gap still represents the local excess `Delta v_phi^2(R)` that must be supplied by organized azimuthal stress if no extra unseen matter is added. By the envelope derivation in the azimuthal-stress note, that same quantity must satisfy

```text
Delta v_phi^2(R) <= k^2(R).
```

Data source:
- SPARC machine-readable mass models: https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt
- SPARC paper: Lelli, McGaugh, and Schombert (2016), https://astroweb.case.edu/ssm/papers/AJv152n157.pdf

Local extracted data file:
- `.scripts/tools/data/sparc/{slugify(galaxy.display_name)}-sparc-visible-baryons.csv`

Figure file: `{image_filename}`
"""
    caption_path.write_text(caption, encoding="utf-8")
    return caption_path


def plot_galaxy(galaxy: SparcGalaxy, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{slugify(galaxy.display_name)}-observed-newtonian-and-trefoil32-energy-flow.png"
    output_path = output_dir / filename

    fig, (ax_top, ax_bottom) = plt.subplots(
        2,
        1,
        figsize=(11.0, 8.3),
        sharex=True,
        gridspec_kw={"height_ratios": [3.2, 2.1]},
    )

    fig.patch.set_facecolor("#f8f4ec")
    radius = galaxy.radius_kpc
    v_bar = galaxy.v_bar_visible
    v_stress_model = galaxy.v_stress_trefoil32
    v_stress_required = galaxy.v_stress_required
    v_energy_flow = galaxy.v_energy_flow_trefoil32

    ax_top.set_facecolor("#fffdf9")
    ax_top.fill_between(radius, v_bar, v_energy_flow, color="#cfe6d8", alpha=0.35)
    ax_top.errorbar(
        radius,
        galaxy.v_obs_kms,
        yerr=galaxy.v_obs_err_kms,
        fmt="o",
        color="#143d59",
        ecolor="#90a4ae",
        elinewidth=1.0,
        capsize=2.5,
        markersize=4.6,
        label="Observed rotation",
    )
    ax_top.plot(radius, v_bar, color="#c26d1a", linewidth=2.4, label="Newtonian baryonic prediction")
    ax_top.plot(
        radius,
        v_energy_flow,
        color="#2f6b5f",
        linewidth=2.7,
        label="Trefoil (3,2) energy-flow model",
    )
    ax_top.fill_between(radius, 0.0, v_bar, color="#efcf9f", alpha=0.18)
    ax_top.set_ylabel("Circular speed [km/s]")
    ax_top.grid(True, alpha=0.25)
    ax_top.legend(loc="best", fontsize=10)

    ax_bottom.set_facecolor("#fbfdff")
    ax_bottom.plot(
        radius,
        v_stress_model,
        color="#2f6b8a",
        linewidth=2.5,
        label=r"Trefoil model completion $\sqrt{f_{32}}\,V_N$",
    )
    ax_bottom.plot(
        radius,
        v_stress_required,
        color="#3e3e3e",
        linewidth=1.9,
        linestyle="--",
        label=r"Completion required by observation $\sqrt{V_{\mathrm{obs}}^2 - V_N^2}$",
    )
    ax_bottom.fill_between(radius, 0.0, v_stress_model, color="#c4dceb", alpha=0.40)
    ax_bottom.set_xlabel("Galactocentric radius [kpc]")
    ax_bottom.set_ylabel("Stress completion [km/s]")
    ax_bottom.set_title(
        "Model stress completion versus the completion required by the data",
        fontsize=11.5,
    )
    ax_bottom.grid(True, alpha=0.25)
    ax_bottom.legend(loc="best", fontsize=10)

    formula_text = (
        r"$f_{32} = \frac{4m^2}{4m^2+n^2} = 0.9$" "\n"
        r"$V_{\mathrm{EF},32}^2 = (1+f_{32})V_N^2$"
    )
    ax_bottom.text(
        0.98,
        0.97,
        formula_text,
        transform=ax_bottom.transAxes,
        ha="right",
        va="top",
        fontsize=11,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "#ffffff", "edgecolor": "#c9d6df"},
    )

    fig.suptitle(f"{galaxy.display_name} from visible baryons", fontsize=15, color="#1f1f1f", y=0.98)
    fig.text(
        0.5,
        0.955,
        "Observed, Newtonian baryons, and a baryonic-only `(3,2)` trefoil model with coherent `4u` weighting",
        ha="center",
        va="top",
        fontsize=10.0,
        color="#3a3a3a",
    )

    fig.tight_layout(rect=[0.03, 0.04, 0.97, 0.90])
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def print_summary(galaxy: SparcGalaxy, image_path: Path, csv_path: Path, caption_path: Path) -> None:
    print(galaxy.display_name)
    print(f"  radii: {galaxy.radius_kpc.size}")
    print(f"  observed peak [km/s]: {float(np.max(galaxy.v_obs_kms)):.2f}")
    print(f"  Newtonian peak [km/s]: {float(np.max(galaxy.v_bar_visible)):.2f}")
    print(f"  trefoil model peak [km/s]: {float(np.max(galaxy.v_energy_flow_trefoil32)):.2f}")
    print(f"  trefoil model completion peak [km/s]: {float(np.max(galaxy.v_stress_trefoil32)):.2f}")
    print(f"  required completion peak [km/s]: {float(np.max(galaxy.v_stress_required)):.2f}")
    print(f"  figure: {image_path}")
    print(f"  extracted data: {csv_path}")
    print(f"  caption: {caption_path}")


def main() -> int:
    args = parse_args()
    galaxy_ids = args.galaxies or list(DEFAULT_GALAXIES)
    sparc_path = ensure_sparc_table(args.data_dir / Path(SPARC_URL).name, args.refresh_sparc)
    rows = parse_sparc_table(sparc_path)

    for galaxy_id in galaxy_ids:
        galaxy = build_galaxy(rows, galaxy_id)
        csv_path = export_extracted_csv(galaxy, args.data_dir)
        image_path = plot_galaxy(galaxy, args.output_dir)
        caption_path = write_caption(galaxy, args.output_dir, image_path.name)
        print_summary(galaxy, image_path, csv_path, caption_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
