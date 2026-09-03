# Reanalysis pipeline

Reproduces every number and figure in the revised manuscript from the two raw
data files in `../data/`.

## Requirements

```
python >= 3.11
numpy scipy pandas matplotlib scikit-learn pyproj
```

## Running

```
cd Pak_Beck
python3 reanalysis/run_all.py
```

Roughly six minutes; the cluster-number scans dominate. Outputs land in
`../results/tables/` (CSV and JSON) and `../results/figures/` (PNG and PDF).
Every stage is seeded (`RNG = 20260903`), so results are bit-reproducible.

## Modules

| File | Contents |
|---|---|
| `catalog.py` | ingestion, quality control, UTM projection, depth-quality diagnostics |
| `features.py` | feature construction, four scalings, the metric's implied exchange rate |
| `fmd.py` | Mc by maximum curvature and goodness-of-fit, Aki-Utsu b, Shi-Bolt error, bootstrap over Mc and b, Utsu test, Benjamini-Hochberg, permutation test |
| `geometry.py` | radius of gyration, principal axes, hull area, location-error floor, descriptor bootstrap |
| `seismicity.py` | Zaliapin-Ben-Zion nearest-neighbour distances, declustering threshold, Omori-Utsu maximum likelihood, Poisson rate comparison |
| `focal.py` | CMTSOLUTION parsing, nodal planes from the moment tensor, faulting style, Kagan angle, catalogue matching |
| `clustering.py` | winner-take-all replication, true Kohonen SOM with U-matrix and topographic error, baselines, validity indices, gap statistic, bootstrap/order/initialisation stability |

## Stages

| Stage | Question |
|---|---|
| A0 | Do the submitted manuscript's own tables support its claims? |
| A1 | Is an eight-cluster partition identifiable at all? |
| A2 | Is the temporal story discovered, or inserted through the input? |
| A3 | Is later seismicity above background, and how far does triggering reach? |
| A4 | What b-value differences survive a common Mc, bootstrap, Utsu and FDR? |
| A5 | What do the focal mechanisms actually constrain? |
| A6 | What spatial structure is supported, and by which method? |
| A7 | Does a partition that never saw time still carry temporal information? |
| A9 | Is the structure an artefact of the study boundary? |
| A8 | Figures |

## Verification built into the modules

The estimators were checked against controls before use: the b-value routine
recovers b = 0.99 from a synthetic catalogue drawn with b = 1.00; the
Omori-Utsu fit recovers (p, c) from three synthetic sequences; the Kagan angle
returns 0 for identical mechanisms and 90 degrees for a thrust against a normal
mechanism; the radial statistic returns SD_R = 0 for a ring of radius 100 km,
which is the counterexample that motivated replacing it.
