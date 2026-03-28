# NGC 3198: Observed Rotation, Newtonian Baryons, and the Complete Energy-Flow Curve

This figure is meant to be read in two steps.

The top panel shows three curves for the same galaxy.

- The dark points are the directly observed circular speed `V_obs(R)` from the SPARC mass-model table.
- The orange curve is the Newtonian visible-baryonic prediction `V_N(R)`, built from the SPARC gas, disk, and bulge components using the fiducial stellar mass-to-light choices quoted in the SPARC paper: `Upsilon_disk = 0.5` and `Upsilon_bulge = 0.7` at 3.6 um.
- The blue-green curve is the completed energy-flow calculation `V_EF(R)`, obtained when the same baryonic closures are allowed to contribute their surviving stress-tensor term as well.

The Newtonian visible-baryonic curve is

```text
V_N^2(R) = V_gas(R)|V_gas(R)| + 0.5 V_disk^2(R) + 0.7 V_bulge^2(R).
```

The completed energy-flow curve is then

```text
V_EF^2(R) = V_N^2(R) + V_stress^2(R).
```

The point of the figure is that the completed galactic attraction must coincide with what is observed. In the stress-tensor reading of the Part III note, the task is not to add some second force to the galaxy from outside, but to recover the full observed load from the full stress decomposition of the baryonic-as-energy closures themselves.

The bottom panel isolates the completion term itself. It plots

```text
V_stress(R) = sqrt(max(V_obs^2(R) - V_N^2(R), 0)).
```

so that the full energy-flow reconstruction obeys

```text
V_EF^2(R) = V_N^2(R) + V_stress^2(R).
```

In the language of the book, `V_stress^2(R)` is the local excess `Delta v_phi^2(R)` that must be supplied by organized azimuthal stress if no extra unseen matter is added. By the envelope derivation in the azimuthal-stress note, that same quantity must satisfy

```text
Delta v_phi^2(R) <= k^2(R).
```

So the lower curve is the stress-tensor completion term coming from the same baryonic closures. In this diagnostic figure it is inferred point by point from the observed gap, so the completed energy-flow curve is forced to coincide with the data. That is exactly the structural claim being illustrated: the full observed galactic load is recovered within one stress-tensor account.

Data source:
- SPARC machine-readable mass models: https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt
- SPARC paper: Lelli, McGaugh, and Schombert (2016), https://astroweb.case.edu/ssm/papers/AJv152n157.pdf

Local extracted data file:
- `.scripts/tools/data/sparc/ngc-3198-sparc-visible-baryons.csv`

Figure file: `ngc-3198-observed-newtonian-and-complete-energy-flow.png`
