# NGC 3198: Observed Rotation, Newtonian Baryons, and a Trefoil-Based Energy-Flow Curve

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
- `.scripts/tools/data/sparc/ngc-3198-sparc-visible-baryons.csv`

Figure file: `ngc-3198-observed-newtonian-and-trefoil32-energy-flow.png`
