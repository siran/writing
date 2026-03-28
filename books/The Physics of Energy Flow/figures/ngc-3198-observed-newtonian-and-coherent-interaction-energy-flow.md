# NGC 3198: Observed Rotation, Newtonian Baryons, and a Coherent-Interaction Energy-Flow Curve

This figure is meant to be read in two steps.

The top panel shows three curves for the same galaxy.

- The dark points are the directly observed circular speed `V_obs(R)` from the SPARC mass-model table.
- The orange curve is the Newtonian visible-baryonic prediction `V_N(R)`, built from the SPARC gas, disk, and bulge components using the fiducial stellar mass-to-light choices quoted in the SPARC paper: `Upsilon_disk = 0.5` and `Upsilon_bulge = 0.7` at 3.6 um.
- The blue-green curve is the coherent-interaction energy-flow curve `V_EF,x(R)`, obtained from the visible baryons alone by keeping the positive cross term of the coherent azimuthal second moment.

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

3. In the aligned azimuthal regime, coherent loading means the local azimuthal stress is the square of the amplitude sum, not just the sum of diagonal pieces:

```text
Sigma_phiphi,coh ~ (sum_a a_a)^2 = sum_a a_a^2 + 2 sum_{a<b} a_a a_b.
```

So the missing galactic interaction term is the positive cross part.

4. Assume each baryonic closure is a `(3,2)` trefoil with coherent `4u` strengthening in the toroidal sector. The corresponding toroidal fraction is

```text
chi_32 = (4 m^2) / (4 m^2 + n^2) = 36 / 40 = 0.9.
```

5. Truncate the coherent interaction to the resolved SPARC families gas, disk, and bulge. This gives the resolved lower-bound interaction term

```text
Delta V_x^2(R) = 2 chi_32 [A_g(R) A_d(R) + A_g(R) A_b(R) + A_d(R) A_b(R)].
```

and the corresponding coherent-interaction energy-flow curve

```text
V_EF,x^2(R) = V_N^2(R) + Delta V_x^2(R).
```

This is not the observed gap inserted back into the curve. It is a baryonic-only interaction expression built from the visible baryons together with the coherent cross-term rule.

The bottom panel compares two different completion terms:

```text
V_x(R) = sqrt(Delta V_x^2(R))
```

from the resolved coherent-interaction lower bound, and

```text
V_stress,req(R) = sqrt(max(V_obs^2(R) - V_N^2(R), 0))
```

required by the observed gap.

So the lower panel is the actual test. If the resolved coherent interaction is sufficient, the blue curve should track the gray required-completion curve. If it stays below it, the resolved SPARC truncation undercounts the full coherent interaction.

For NGC 3198, that is exactly what this first test shows: the coherent-interaction lower bound improves on the Newtonian baryonic curve and tracks the inner rise in the right direction, but it still stays below the observed outer rotation and below the required completion through most of the disk. So the construction is now honest and baryonic-only, and the remaining gap has a clean interpretation: the resolved gas-disk-bulge split is only a lower bound on the full positive cross term of all finer baryonic closures.

In the language of the book, the required gap still represents the local excess `Delta v_phi^2(R)` that must be supplied by organized azimuthal stress if no extra unseen matter is added. By the envelope derivation in the azimuthal-stress note, that same quantity must satisfy

```text
Delta v_phi^2(R) <= k^2(R).
```

Data source:
- SPARC machine-readable mass models: https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt
- SPARC paper: Lelli, McGaugh, and Schombert (2016), https://astroweb.case.edu/ssm/papers/AJv152n157.pdf

Local extracted data file:
- `.scripts/tools/data/sparc/ngc-3198-sparc-visible-baryons.csv`

Figure file: `ngc-3198-observed-newtonian-and-coherent-interaction-energy-flow.png`
