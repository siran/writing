# NGC 3198: Observed Rotation, Visible Baryons, and the Required Azimuthal-Stress Term

This figure is meant to be read in two steps.

The top panel shows the directly observed circular speed `V_obs(R)` from the SPARC mass-model table against the visible baryonic curve `V_bar(R)`. The visible baryonic curve is built from the SPARC gas, disk, and bulge components using the fiducial stellar mass-to-light choices quoted in the SPARC paper: `Upsilon_disk = 0.5` and `Upsilon_bulge = 0.7` at 3.6 um. Concretely,

```text
V_bar^2(R) = V_gas(R)|V_gas(R)| + 0.5 V_disk^2(R) + 0.7 V_bulge^2(R).
```

So the orange curve is the speed expected from the visible baryons alone under the standard SPARC fiducial normalization.

The bottom panel rewrites the same discrepancy as the azimuthal-stress term required by the Part III derivation. It plots

```text
V_stress(R) = sqrt(max(V_obs^2(R) - V_bar^2(R), 0)).
```

so that

```text
V_obs^2(R) = V_bar^2(R) + V_stress^2(R).
```

In the language of the book, `V_stress^2(R)` is the local excess `Delta v_phi^2(R)` that must be supplied by organized azimuthal stress if no extra unseen matter is added. By the envelope derivation in the azimuthal-stress note, that same quantity must satisfy

```text
Delta v_phi^2(R) <= k^2(R).
```

So the blue curve is also the minimum local transport-speed scale that any admissible `k(R)` profile would have to exceed if this channel accounts for the full galactic excess.

Data source:
- SPARC machine-readable mass models: https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt
- SPARC paper: Lelli, McGaugh, and Schombert (2016), https://astroweb.case.edu/ssm/papers/AJv152n157.pdf

Local extracted data file:
- `.scripts/tools/data/sparc/ngc-3198-sparc-visible-baryons.csv`

Figure file: `ngc-3198-visible-baryons-and-required-azimuthal-stress.png`
