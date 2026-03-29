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
    def gas_signed_term(self) -> np.ndarray:
        return self.v_gas_kms * np.abs(self.v_gas_kms)

    @property
    def gas_positive_amplitude(self) -> np.ndarray:
        return np.sqrt(np.maximum(self.gas_signed_term, 0.0))

    @property
    def disk_visible_amplitude(self) -> np.ndarray:
        return np.sqrt(FIDUCIAL_ML_DISK) * self.v_disk_unit_ml_kms

    @property
    def bulge_visible_amplitude(self) -> np.ndarray:
        return np.sqrt(FIDUCIAL_ML_BULGE) * self.v_bulge_unit_ml_kms

    @property
    def v_bar2_visible(self) -> np.ndarray:
        return np.maximum(
            self.gas_signed_term + self.disk_visible_amplitude**2 + self.bulge_visible_amplitude**2,
            0.0,
        )

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
    def delta_v2_coherence_upper_bound(self) -> np.ndarray:
        cross_sum = (
            self.gas_positive_amplitude * self.disk_visible_amplitude
            + self.gas_positive_amplitude * self.bulge_visible_amplitude
            + self.disk_visible_amplitude * self.bulge_visible_amplitude
        )
        return 2.0 * cross_sum

    @property
    def v_energy_flow_correlator_upper_bound(self) -> np.ndarray:
        return np.sqrt(self.v_bar2_visible + self.delta_v2_coherence_upper_bound)

    @property
    def a_sum_visible(self) -> np.ndarray:
        return self.gas_positive_amplitude + self.disk_visible_amplitude + self.bulge_visible_amplitude

    @property
    def v_energy_flow_one_channel_upper_bound(self) -> np.ndarray:
        return self.a_sum_visible

    @property
    def v_energy_flow_two_channel_upper_bound(self) -> np.ndarray:
        return np.sqrt(2.0) * self.a_sum_visible

    @property
    def n_winding_req(self) -> np.ndarray:
        denominator = self.a_sum_visible**2
        values = np.full_like(denominator, np.nan, dtype=float)
        mask = denominator > 1e-9
        values[mask] = self.v_obs_kms[mask] ** 2 / denominator[mask]
        values[~mask] = 0.0
        return values

    @property
    def c_req(self) -> np.ndarray:
        denominator = self.delta_v2_coherence_upper_bound
        values = np.full_like(denominator, np.nan, dtype=float)
        mask = denominator > 1e-9
        values[mask] = self.delta_v2[mask] / denominator[mask]
        values[~mask] = 0.0
        return values

    @property
    def v_energy_flow_correlator_accounted(self) -> np.ndarray:
        return np.sqrt(self.v_bar2_visible + self.delta_v2_coherence_upper_bound * self.c_req)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Plot observed SPARC rotation curves against visible baryons and a "
            "resolved baryonic coherence band for one or more galaxies."
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
                "a_g_coherent_kms",
                "a_d_coherent_kms",
                "a_b_coherent_kms",
                "a_sum_coherent_kms",
                "v_bar_visible_kms",
                "v_energy_flow_one_channel_upper_bound_kms",
                "v_energy_flow_two_channel_upper_bound_kms",
                "v_energy_flow_correlator_upper_bound_kms",
                "v_energy_flow_correlator_accounted_kms",
                "v_stress_required_kms",
                "n_winding_req",
                "c_req",
                "delta_v2_coherence_upper_bound_kms2",
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
            galaxy.gas_positive_amplitude,
            galaxy.disk_visible_amplitude,
            galaxy.bulge_visible_amplitude,
            galaxy.a_sum_visible,
            galaxy.v_bar_visible,
            galaxy.v_energy_flow_one_channel_upper_bound,
            galaxy.v_energy_flow_two_channel_upper_bound,
            galaxy.v_energy_flow_correlator_upper_bound,
            galaxy.v_energy_flow_correlator_accounted,
            galaxy.v_stress_required,
            galaxy.n_winding_req,
            galaxy.c_req,
            galaxy.delta_v2_coherence_upper_bound,
            galaxy.delta_v2,
            strict=True,
        ):
            writer.writerow(
                [
                    galaxy.display_name,
                    *[f"{value:.6f}" for value in values[:-1]],
                    f"{values[-1]:.6f}",
                ]
            )
    return output_path


def write_caption(galaxy: SparcGalaxy, output_dir: Path, image_filename: str) -> Path:
    caption_path = output_dir / f"{slugify(galaxy.display_name)}-observed-newtonian-and-winding-channel-band.md"
    caption = f"""# {galaxy.display_name}: Observed Rotation, Newtonian Baryons, and the Winding-Channel Band

This figure is meant to be read in two steps.

The top panel shows four curves for the same galaxy.

- The dark points are the directly observed circular speed `V_obs(R)` from the SPARC mass-model table.
- The orange curve is the Newtonian visible-baryonic prediction `V_N(R)`, built from the SPARC gas, disk, and bulge components using the fiducial stellar mass-to-light choices quoted in the SPARC paper: `Upsilon_disk = 0.5` and `Upsilon_bulge = 0.7` at 3.6 um.
- The blue curve is the one-channel baryonic ceiling `V_1(R) = A_g(R) + A_d(R) + A_b(R)`.
- The green curve is the conjugate-pair ceiling `V_2(R) = sqrt(2)[A_g(R) + A_d(R) + A_b(R)]`.

The construction is stepwise.

1. Recover the visible-baryonic Newtonian curve from the SPARC gas, disk, and bulge pieces:

```text
V_N^2(R) = V_gas(R)|V_gas(R)| + 0.5 V_disk^2(R) + 0.7 V_bulge^2(R).
```

2. Convert the resolved SPARC families into positive coherent amplitudes:

```text
A_g(R) = sqrt(max(V_g(R)|V_g(R)|, 0)),
A_d(R) = sqrt(0.5) V_disk(R),
A_b(R) = sqrt(0.7) V_bulge(R).
```

3. At resolved-family level, the ordinary baryonic curve keeps only the diagonal part

```text
V_N^2(R) = A_g^2(R) + A_d^2(R) + A_b^2(R).
```

4. Allow coherent pair loading between the resolved families:

```text
V_EF^2(R) = V_N^2(R) + 2[C_gd(R) A_g(R)A_d(R) + C_gb(R) A_g(R)A_b(R) + C_db(R) A_d(R)A_b(R)],
```

with `0 <= C_ij(R) <= 1`.

5. That gives the coarse one-channel ceiling

```text
V_EF^2(R) <= [A_g(R) + A_d(R) + A_b(R)]^2.
```

6. To allow a preferred winding sector inside a visible family, split each resolved family into internal winding channels `k`:

```text
A_I^2(R) = sum_k A_Ik^2(R).
```

Then the full constructive envelope is

```text
V_EF^2(R) <= [sum_I sum_k A_Ik(R)]^2.
```

By Cauchy,

```text
sum_k A_Ik(R) <= sqrt(N_I) A_I(R),
```

where `N_I` is the number of active winding channels carried by resolved family `I`.

7. If one common ceiling `N_*` bounds the active winding channels of the visible families, then

```text
V_EF^2(R) <= N_* [A_g(R) + A_d(R) + A_b(R)]^2.
```

So the two plotted baryonic ceilings are

```text
V_1(R) = A_g(R) + A_d(R) + A_b(R),
V_2(R) = sqrt(2)[A_g(R) + A_d(R) + A_b(R)].
```

The first is the one-channel ceiling. The second is the first winding lift: each visible family carries at most one conjugate pair, such as `(m,n)` and `(n,m)`.

The bottom panel then asks how large a common winding ceiling would be needed to cover the observed galaxy. Define

```text
N_req(R) = V_obs^2(R) / [A_g(R) + A_d(R) + A_b(R)]^2.
```

If `N_req(R) <= 1`, the observed point fits inside the one-channel ceiling. If `1 < N_req(R) <= 2`, the one-channel ceiling is too low but a dominant conjugate pair per visible family is enough. If `N_req(R) > 2`, then even that is not enough, so additional winding channels, finer baryonic decomposition, or additional unresolved baryonic families must still contribute.

In the plot, very large values of `N_req` are clipped only for readability.

For NGC 3198, this is exactly what the figure shows. The one-channel ceiling already tracks the inner rise shape far better than the Newtonian baryonic curve, which means the omitted coherent product term is pointed in the right direction. The conjugate-pair ceiling lifts that band further and covers more of the galaxy, including part of the mid-disk. But much of the outer disk still requires `N_req(R) > 2`, so a single winning `(m,n)/(n,m)` pair is not enough by itself.

This is the clean reason to move from resolved families to resolved families plus internal winding channels. The old coarse band threw away same-family coherent products. The winding-channel refinement puts them back in the only rigorous way available at this stage: as a finite-channel constructive bound.

Data sources:
- SPARC machine-readable mass models: https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt
- SPARC paper: Lelli, McGaugh, and Schombert (2016), https://astroweb.case.edu/ssm/papers/AJv152n157.pdf

Local extracted data file:
- `.scripts/tools/data/sparc/{slugify(galaxy.display_name)}-sparc-visible-baryons.csv`

Figure file: `{image_filename}`
"""
    caption_path.write_text(caption, encoding="utf-8")
    return caption_path


def write_accounting_caption(galaxy: SparcGalaxy, output_dir: Path, image_filename: str) -> Path:
    caption_path = output_dir / f"{slugify(galaxy.display_name)}-observed-newtonian-and-correlator-accounting.md"
    caption = f"""# {galaxy.display_name}: Observed Rotation, Newtonian Baryons, and Correlator Accounting of the Excess

This figure is the accounting companion to the resolved correlator band.

The top panel shows three curves:

- The dark points are the directly observed SPARC rotation curve `V_obs(R)`.
- The orange curve is the Newtonian visible-baryonic prediction `V_N(R)`.
- The blue-green curve is the correlator-accounted excess curve `V_corr,acc(R)`.

The construction uses the same resolved baryonic amplitudes

```text
A_g(R) = sqrt(max(V_g(R)|V_g(R)|, 0)),
A_d(R) = sqrt(0.5) V_disk(R),
A_b(R) = sqrt(0.7) V_bulge(R),
```

and the same resolved-family cross budget

```text
Delta V_coh,max^2(R) = 2[A_g(R)A_d(R) + A_g(R)A_b(R) + A_d(R)A_b(R)].
```

Define the required effective correlator by

```text
C_req(R) = [max(V_obs^2(R) - V_N^2(R), 0)] / Delta V_coh,max^2(R).
```

Then the accounted correlator curve is

```text
V_corr,acc^2(R) = V_N^2(R) + 2 C_req(R)[A_g(R)A_d(R) + A_g(R)A_b(R) + A_d(R)A_b(R)].
```

So in every radius where the observed rotation lies above the Newtonian baryonic curve, the excess is written exactly as a baryonic correlator term. Where the observed point dips below the Newtonian curve, the correlator term is set to zero, because the dark-matter question concerns the positive excess above the baryonic baseline.

This is not a prediction. It is an exact accounting statement: the observed galactic excess can be represented as a correlator term built from the resolved baryonic amplitudes.

The bottom panel plots the same `C_req(R)` profile. The green band `0 <= C_req <= 1` is the resolved-family correlator band. Values above `1` mean the resolved gas-disk-bulge families alone are not enough, so finer baryonic decomposition or additional unresolved baryonic families must still contribute.

For NGC 3198, the accounting plot shows two things at once:

- the observed excess really can be written in correlator form,
- but the required correlator rises above the simple resolved-family band across most of the outer disk.

So the explanation accounts for the observations structurally, while the present gas-disk-bulge truncation remains too coarse to make the correlator fully internal without further baryonic subdivision.

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
    filename = f"{slugify(galaxy.display_name)}-observed-newtonian-and-winding-channel-band.png"
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
    v_one_channel = galaxy.v_energy_flow_one_channel_upper_bound
    v_two_channel = galaxy.v_energy_flow_two_channel_upper_bound
    n_req = galaxy.n_winding_req

    ax_top.set_facecolor("#fffdf9")
    ax_top.fill_between(radius, v_one_channel, v_two_channel, color="#cfe6d8", alpha=0.35)
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
        v_one_channel,
        color="#2f6b8a",
        linewidth=2.4,
        label="One-channel upper bound",
    )
    ax_top.plot(
        radius,
        v_two_channel,
        color="#2f6b5f",
        linewidth=2.7,
        label="Conjugate-pair upper bound",
    )
    ax_top.fill_between(radius, 0.0, v_bar, color="#efcf9f", alpha=0.18)
    ax_top.set_ylabel("Circular speed [km/s]")
    ax_top.grid(True, alpha=0.25)
    ax_top.legend(loc="best", fontsize=10)

    ax_bottom.set_facecolor("#fbfdff")
    ax_bottom.axhspan(
        0.0,
        1.0,
        color="#dbeaf6",
        alpha=0.65,
        label=r"One-channel band $0 \leq N_{\ast,\mathrm{req}} \leq 1$",
    )
    ax_bottom.axhspan(
        1.0,
        2.0,
        color="#d9efe3",
        alpha=0.65,
        label=r"Conjugate-pair band $1 < N_{\ast,\mathrm{req}} \leq 2$",
    )
    clipped_n = np.minimum(n_req, 6.0)
    ax_bottom.plot(
        radius,
        clipped_n,
        color="#2f6b8a",
        linewidth=2.5,
        label=r"Required common winding ceiling $N_{\ast,\mathrm{req}}$",
    )
    overflow_mask = n_req > 6.0
    if np.any(overflow_mask):
        ax_bottom.scatter(
            radius[overflow_mask],
            np.full(np.count_nonzero(overflow_mask), 6.0),
            marker="^",
            s=48,
            color="#2f6b8a",
            label=r"$N_{\ast,\mathrm{req}}>6$ (clipped)",
            zorder=5,
        )
    ax_bottom.set_xlabel("Galactocentric radius [kpc]")
    ax_bottom.set_ylabel(r"Required winding ceiling $N_{\ast,\mathrm{req}}$")
    ax_bottom.set_title(
        "Required common winding ceiling versus the one-channel and conjugate-pair bands",
        fontsize=11.5,
    )
    ax_bottom.grid(True, alpha=0.25)
    ax_bottom.legend(loc="best", fontsize=10)
    ax_bottom.set_ylim(0.0, 6.05)

    formula_text = (
        r"$V_{\mathrm{EF}}^2 \leq N_{\ast}(A_g+A_d+A_b)^2$" "\n"
        r"$N_{\ast,\mathrm{req}} = \frac{V_{\mathrm{obs}}^2}{(A_g+A_d+A_b)^2}$"
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
        "Observed rotation, Newtonian baryons, and the winding-channel lift of the baryonic ceiling",
        ha="center",
        va="top",
        fontsize=10.0,
        color="#3a3a3a",
    )

    fig.tight_layout(rect=[0.03, 0.04, 0.97, 0.90])
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def plot_accounting_galaxy(galaxy: SparcGalaxy, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{slugify(galaxy.display_name)}-observed-newtonian-and-correlator-accounting.png"
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
    v_accounted = galaxy.v_energy_flow_correlator_accounted
    c_req = galaxy.c_req

    ax_top.set_facecolor("#fffdf9")
    ax_top.fill_between(radius, v_bar, v_accounted, color="#cfe6d8", alpha=0.35)
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
        v_accounted,
        color="#2f6b5f",
        linewidth=2.7,
        label="Correlator-accounted excess",
    )
    ax_top.fill_between(radius, 0.0, v_bar, color="#efcf9f", alpha=0.18)
    ax_top.set_ylabel("Circular speed [km/s]")
    ax_top.grid(True, alpha=0.25)
    ax_top.legend(loc="best", fontsize=10)

    ax_bottom.set_facecolor("#fbfdff")
    ax_bottom.axhspan(
        0.0,
        1.0,
        color="#d9efe3",
        alpha=0.65,
        label=r"Resolved-family band $0 \leq C_{\mathrm{eff}} \leq 1$",
    )
    clipped_c = np.minimum(c_req, 5.0)
    ax_bottom.plot(
        radius,
        clipped_c,
        color="#2f6b8a",
        linewidth=2.5,
        label=r"Required correlator $C_{\mathrm{req}}$",
    )
    overflow_mask = c_req > 5.0
    if np.any(overflow_mask):
        ax_bottom.scatter(
            radius[overflow_mask],
            np.full(np.count_nonzero(overflow_mask), 5.0),
            marker="^",
            s=48,
            color="#2f6b8a",
            label=r"$C_{\mathrm{req}}>5$ (clipped)",
            zorder=5,
        )
    ax_bottom.set_xlabel("Galactocentric radius [kpc]")
    ax_bottom.set_ylabel(r"Effective correlator $C_{\mathrm{req}}$")
    ax_bottom.set_title(
        "Required correlator profile for the observed positive excess",
        fontsize=11.5,
    )
    ax_bottom.grid(True, alpha=0.25)
    ax_bottom.legend(loc="best", fontsize=10)
    ax_bottom.set_ylim(0.0, 5.05)

    formula_text = (
        r"$V_{\mathrm{corr,acc}}^2 = V_N^2 + 2C_{\mathrm{req}}(A_gA_d+A_gA_b+A_dA_b)$" "\n"
        r"$C_{\mathrm{req}} = \frac{\max(V_{\mathrm{obs}}^2 - V_N^2, 0)}{2(A_gA_d+A_gA_b+A_dA_b)}$"
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

    fig.suptitle(f"{galaxy.display_name} as baryons plus correlator excess", fontsize=15, color="#1f1f1f", y=0.98)
    fig.text(
        0.5,
        0.955,
        "Observed rotation, Newtonian baryons, and exact correlator accounting of the positive excess",
        ha="center",
        va="top",
        fontsize=10.0,
        color="#3a3a3a",
    )

    fig.tight_layout(rect=[0.03, 0.04, 0.97, 0.90])
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def print_summary(
    galaxy: SparcGalaxy,
    band_image_path: Path,
    band_caption_path: Path,
    accounting_image_path: Path,
    accounting_caption_path: Path,
    csv_path: Path,
) -> None:
    print(galaxy.display_name)
    print(f"  radii: {galaxy.radius_kpc.size}")
    print(f"  observed peak [km/s]: {float(np.max(galaxy.v_obs_kms)):.2f}")
    print(f"  Newtonian peak [km/s]: {float(np.max(galaxy.v_bar_visible)):.2f}")
    print(f"  one-channel upper peak [km/s]: {float(np.max(galaxy.v_energy_flow_one_channel_upper_bound)):.2f}")
    print(f"  conjugate-pair upper peak [km/s]: {float(np.max(galaxy.v_energy_flow_two_channel_upper_bound)):.2f}")
    finite_n = galaxy.n_winding_req[np.isfinite(galaxy.n_winding_req)]
    print(f"  N_req range: {float(np.min(finite_n)):.3f} to {float(np.max(finite_n)):.3f}")
    finite_c = galaxy.c_req[np.isfinite(galaxy.c_req)]
    print(f"  C_req range: {float(np.min(finite_c)):.3f} to {float(np.max(finite_c)):.3f}")
    print(f"  band figure: {band_image_path}")
    print(f"  band caption: {band_caption_path}")
    print(f"  accounting figure: {accounting_image_path}")
    print(f"  accounting caption: {accounting_caption_path}")
    print(f"  extracted data: {csv_path}")


def main() -> int:
    args = parse_args()
    galaxy_ids = args.galaxies or list(DEFAULT_GALAXIES)
    sparc_path = ensure_sparc_table(args.data_dir / Path(SPARC_URL).name, args.refresh_sparc)
    rows = parse_sparc_table(sparc_path)

    for galaxy_id in galaxy_ids:
        galaxy = build_galaxy(rows, galaxy_id)
        csv_path = export_extracted_csv(galaxy, args.data_dir)
        band_image_path = plot_galaxy(galaxy, args.output_dir)
        band_caption_path = write_caption(galaxy, args.output_dir, band_image_path.name)
        accounting_image_path = plot_accounting_galaxy(galaxy, args.output_dir)
        accounting_caption_path = write_accounting_caption(galaxy, args.output_dir, accounting_image_path.name)
        print_summary(
            galaxy,
            band_image_path,
            band_caption_path,
            accounting_image_path,
            accounting_caption_path,
            csv_path,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
