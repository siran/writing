# NGC 3198: Observed Rotation, Newtonian Baryons, and the Resolved Coherence Band

This figure is meant to be read in two steps.

The top panel shows three curves for the same galaxy.

- The dark points are the directly observed circular speed `V_obs(R)` from the SPARC mass-model table.
- The orange curve is the Newtonian visible-baryonic prediction `V_N(R)`, built from the SPARC gas, disk, and bulge components using the fiducial stellar mass-to-light choices quoted in the SPARC paper: `Upsilon_disk = 0.5` and `Upsilon_bulge = 0.7` at 3.6 um.
- The blue-green curve is the resolved coherence upper bound `V_coh,max(R)`, obtained by letting the resolved gas, disk, and bulge families add with maximal positive coherence.

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
V_EF^2(R) = V_N^2(R) + 2[lambda_gd A_g(R)A_d(R) + lambda_gb A_g(R)A_b(R) + lambda_db A_d(R)A_b(R)],
```

with `0 <= lambda_ij <= 1`.

5. This gives a rigorous lower and upper bound:

```text
V_N^2(R) <= V_EF^2(R) <= (A_g(R) + A_d(R) + A_b(R))^2.
```

So the upper curve in the top panel is

```text
V_coh,max(R) = A_g(R) + A_d(R) + A_b(R),
```

and its excess above Newtonian is

```text
Delta V_coh,max^2(R) = 2[A_g(R)A_d(R) + A_g(R)A_b(R) + A_d(R)A_b(R)].
```

This is shape-independent at the coarse resolved-family level. It does not require picking a microscopic knot. It only uses the positive baryonic amplitudes recovered from the resolved gas, disk, and bulge content.

The bottom panel then asks whether the observed gap fits inside that resolved-family band. Define the required effective resolved coherence

```text
lambda_req(R) = [V_obs^2(R) - V_N^2(R)] / Delta V_coh,max^2(R).
```

If `0 <= lambda_req(R) <= 1`, then the observed excess is recovered inside the resolved gas-disk-bulge coherence band alone. If `lambda_req(R) > 1`, then the resolved SPARC families undercount the full positive cross term and finer baryonic decomposition or additional unresolved baryonic families must still contribute.

In the plot, very large values of `lambda_req` are clipped at `5` only for readability. Those spikes occur where the resolved cross budget in the denominator is very small, so they should be read simply as "well above the resolved-family band."

For NGC 3198, this is exactly what the figure shows. The upper coherence curve already tracks the inner rise shape far better than the Newtonian baryonic curve, which means the omitted positive cross term is pointed in the right direction. But across most of the outer disk the observed rotation still lies above the resolved-family upper curve, and the lower panel correspondingly pushes `lambda_req(R)` above `1`. So the resolved visible families do not close the galaxy by themselves, but they do recover the correct structural mechanism and a nontrivial lower/upper band.

In the language of the book, the required gap still represents the local excess `Delta v_phi^2(R)` that must be supplied by organized azimuthal stress if no extra unseen matter is added. By the envelope derivation in the azimuthal-stress note, that same quantity must satisfy

```text
Delta v_phi^2(R) <= k^2(R).
```

Data source:
- SPARC machine-readable mass models: https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt
- SPARC paper: Lelli, McGaugh, and Schombert (2016), https://astroweb.case.edu/ssm/papers/AJv152n157.pdf

Local extracted data file:
- `.scripts/tools/data/sparc/ngc-3198-sparc-visible-baryons.csv`

Figure file: `ngc-3198-observed-newtonian-and-resolved-coherence-band.png`
