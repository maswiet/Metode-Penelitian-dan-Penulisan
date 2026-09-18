# Lombok 2018 — reanalysis after the reviewer report

The reviewer recommended **Reject**, on the grounds that the weaknesses were
structural and could not be fixed by revising the text. This directory is the
response: the catalogue was replaced, the analysis rebuilt from raw data, and
the paper rewritten around what survives testing.

`README.md` in this directory is the original reviewer report and is unchanged.

## What is here

| Path | Contents |
|---|---|
| `manuscript/Lombok_revised_manuscript.docx` | the revised paper, figures embedded |
| `manuscript/revised_manuscript.md` | same paper in Markdown (the editable source) |
| `manuscript/Response_to_reviewer.docx` | point-by-point response |
| `manuscript/response_to_reviewer.md` | same, in Markdown |
| `data/` | both raw input files, unmodified |
| `reanalysis/` | the analysis code, with its own README |
| `results/tables/` | every table and statistical test output |
| `results/figures/` | the seven figures, PNG and PDF |

Reproduce everything with `python3 reanalysis/run_all.py` (about six minutes).

## What changed

The previous version analysed **248 events with non-homogeneous magnitude
types**. This one analyses **25,278 events on a homogenised moment-magnitude
scale** (1998–2023) — the catalogue supplied for this revision.

**Withdrawn:** eight seismogenic domains; four evolutionary stages; progressive
vertical localization; regional postseismic redistribution; the description of
the algorithm as a Self-Organizing Map.

**Retained and strengthened:** the sequence as segmented, sequential thrust
rupture, now established from catalogue statistics with occurrence time held
out of the clustering.

## The main results

| Result | Value |
|---|---|
| Eight-cluster partition, bootstrap ARI | 0.574 — below the 0.8 reproducibility threshold |
| Cluster number actually supported | K = 3 in space (ARI = 0.980) |
| Training epochs that change the result | 25 of 100; α(100) = 7.9 × 10⁻³³ |
| Temporal separation inserted by using time as an input | about half (159.5 d with time vs 80.9 d without) |
| Hypocentral depths at the unresolved 10 km default | 53.5%; corr(default fraction, SD_Z) = −0.745 |
| Western vs eastern thrust segment b-value | 0.990 ± 0.032 vs 1.002 ± 0.031 — indistinguishable (q = 0.36) |
| Southern fore-arc b-value | 1.795 ± 0.099 (q = 1.2 × 10⁻¹³) |
| Inter-segment activation delay | 13.6 days (q = 1.1 × 10⁻²⁵) |
| Eastward migration | Spearman ρ = +0.398, p = 1.4 × 10⁻³⁷ |
| Near-field b-value depression | 0.975 vs 1.277 (q = 9.4 × 10⁻⁶); survives excluding all Mw ≥ 5.0 (p = 0.018) |
| Aftershock decay | Omori–Utsu p = 0.946, c = 0.19 d |
| Triggering radius | ~75 km; beyond it the rate increase is ×1.9, p = 0.32 (not significant) |

## Audit of the previously published tables

Recomputed from Table 1 and Table 2 of the 18 August version, without needing
the original event list (`results/tables/published_*_audit.csv`):

- **"C4 is the most compact domain"** — by radius of gyration C4 = 19.97 km and
  C3 = 20.96 km, a difference of 0.99 km against a 0.45 km resolution floor
  from coordinate rounding alone.
- **The b-value contrasts** — all 28 pairwise Utsu tests fail after
  Benjamini–Hochberg correction; the strongest is p = 0.037, q = 0.368.
- **"C3 has both the lowest b and the highest mean magnitude"** — b = 0.58 at
  Mc = 4.1 implies a mean magnitude of 4.80, which is the value reported
  separately as corroboration. One statistic, counted twice.
