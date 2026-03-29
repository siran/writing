# NGC 3198: Observed Rotation, Newtonian Baryons, and Correlator Accounting of the Excess

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
- `.scripts/tools/data/sparc/ngc-3198-sparc-visible-baryons.csv`

Figure file: `ngc-3198-observed-newtonian-and-correlator-accounting.png`
