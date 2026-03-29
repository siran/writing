# NGC 3198: Observed Rotation, Newtonian Baryons, and the Winding-Channel Band

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
- `.scripts/tools/data/sparc/ngc-3198-sparc-visible-baryons.csv`

Figure file: `ngc-3198-observed-newtonian-and-winding-channel-band.png`
