# Response to the reviewer

We thank the reviewer for a report that was accurate on every point of substance. The recommendation — that the manuscript required reconstruction of the methodology from the ground up rather than revision of the narrative — was correct, and we have followed it.

**What we did.** We did not revise the previous text. We replaced the catalogue, discarded the eight-cluster/four-stage framework, rebuilt the analysis from raw data, and rewrote the paper around what survives testing. The new catalogue contains **25,278 events (1998–2023) on a homogenised moment-magnitude scale**, against the 248 mixed-magnitude events analysed previously. All code and data are released; every number and figure regenerates from the raw files with one command.

**What changed in the conclusions.** The eight seismogenic domains, the four evolutionary stages, the progressive vertical localization and the regional postseismic redistribution are withdrawn. What replaces them is smaller and better supported: two back-arc thrust segments activating 13.6 days apart, a distinct southern fore-arc domain, a near-field b-value depression, and an ordinary Omori decay with a measurable triggering radius of about 75 km.

**One correction to the report.** The reviewer predicted that event ordering would prove a dominant instability. We tested it with 200 permutations and it is not: ARI = 0.923 ± 0.018 (minimum 0.842). The dominant instabilities are sample composition (bootstrap ARI = 0.574 at K = 8) and the metric (ARI = 0.466 when the time axis weight is halved). We report this because the reviewer's diagnosis was right about the conclusion and worth correcting on the mechanism.

**One finding neither of us anticipated.** 53.5% of hypocentral depths in the study region are the unresolved 10 km default value, and apparent depth dispersion within clusters is anti-correlated with the default-depth fraction at r = −0.745. The "shallowest, most vertically concentrated domain" was a reporting artefact. This is now Section 4.3.

---

## Part I — the twenty numbered criticisms

### 1. "This is still not a Self-Organizing Map"

**Accepted in full.** The title, abstract and text no longer contain "Self-Organizing Map" as a description of what was run. The procedure is named a **winner-take-all competitive vector quantisation** throughout (Section 3.1), and no topological claim is made for it, because topographic error is undefined without a lattice.

We also did what the reviewer asked as the alternative: we implemented a **genuine Kohonen SOM** with a Gaussian neighbourhood on a 4 × 2 lattice, and report its quantisation error (0.145), topographic error (0.003) and U-matrix. The comparison is instructive — the true SOM has near-perfect topology preservation at higher quantisation error than the WTA procedure, which is the expected trade-off and precisely the property the earlier version claimed without possessing.

### 2. "Eight clusters were ordered in advance, not discovered"

**Accepted, and now tested.** K is estimated, not assumed (Section 4.1, Figure 2a). Silhouette is maximised at K = 4, the gap statistic at K = 2; bootstrap ARI falls monotonically from 0.98 (K = 2) to 0.80 (K = 8) and below 0.65 at K = 9. On the full catalogue clustered in space, K = 3 is selected with bootstrap ARI = 0.980 (5th percentile 0.954), against 0.853 at K = 8.

The reviewer's destroying questions are answered directly. Cluster persistence across K = 6…10 is tabulated in `results/tables/cluster_persistence.csv`. **The eight-cluster conclusion is withdrawn.**

### 3. "Time was an input, then its output was sold as temporal evolution"

**Accepted, and quantified.** We measured the circularity rather than merely conceding it (Table 1, Figure 3a). Clustering on E–N–Z–T gives a spread of cluster mean dates of 159.5 days; on E–N–Z, 80.9 days; random groupings of the same sizes, ~31 days. **Roughly half of the apparent temporal separation was inserted by the input.**

We then adopted the reviewer's recommended design: cluster on space, hold time out, test temporal organisation independently. The result is Section 4.7, and it is the strongest result in the paper — groups built without time differ in occurrence time at H = 104.2, p = 2.4 × 10⁻²³, with eastward migration at ρ = +0.398, p = 1.4 × 10⁻³⁷.

### 4. "The training schedule is a parody of optimisation"

**Accepted, and now demonstrated rather than described.** α(20) = 9.5 × 10⁻⁹ and α(100) = 7.9 × 10⁻³³, below double precision from epoch 52. We verified that **cluster labels are bit-identical after 25 and after 100 epochs**: 75 of the 100 epochs change nothing (Section 4.1, Figure 2b).

On stability, we ran the analyses the reviewer listed: 200 order permutations (ARI = 0.923 ± 0.018), four initialisation schemes, and 100 bootstrap resamples (ARI = 0.574). As noted above, order is not the dominant instability; sample composition is. The reviewer's conclusion stands even though this particular mechanism does not.

### 5. "The radial initialisation is arbitrary and may dominate"

**Tested.** Initialisation sensitivity is reported in `results/tables/a1_identifiability.json` for radial, random, k-means++ and principal-component starts. More decisively, the question is now moot: at the cluster number the data support, the WTA partition and k-means agree at ARI = 0.993 (Section 4.4), so no initialisation-specific structure survives.

### 6. "Min–max normalisation is not a physical justification"

**Accepted, and the exchange rate is now stated.** The reviewer asked how many days are equivalent to how many kilometres. For this dataset the metric implies **2.4 days per kilometre of depth and 1.7 days per kilometre of horizontal distance** — 10 km of depth is treated as 24 days. We also state that horizontal position occupies two of four axes and therefore carries twice the weight of depth or time.

We tested the alternatives requested: z-score (ARI = 0.888 against min–max), robust (0.715), Mahalanobis (0.877), and explicit re-weighting — halving the time weight gives **ARI = 0.466**. The partition is a function of the metric, and we say so.

### 7. "'Independent post-hoc characterization' misuses the word independent"

**Accepted.** The word is removed. Post-hoc descriptors computed from clustering variables are now called what they are. The genuinely independent test in the new paper is occurrence time evaluated on a partition built from horizontal position alone (Section 4.7), which is independent in the operative sense: withheld from training.

On magnitude, the reviewer was right that exclusion from the input does not confer statistical independence. We therefore added the permutation test proposed in point 14: memberships fixed, magnitudes shuffled. Result: p = 0.039 for the minimum group b-value. We report the effect as modest and describe it accordingly.

### 8. "248 events is too poor a catalogue for this ambition"

**Accepted, and remedied.** The catalogue is replaced. The new one has **25,278 events on a homogenised Mw scale**; within the previous study box and window it contains 3,781 events against the previous 248. Completeness falls to Mc = 3.6–3.7 in the modern era, against the 4.1–4.4 thresholds previously used.

We also now report what the reviewer correctly said was missing: the 2009 completeness change (Figure 1a, 1c), the fixed-depth artefact (Figure 1b), and the resolution floor implied by coordinate rounding (0.45 km). Deep slab events are excluded by restricting the sequence analysis to 0–60 km, so no cluster is a deep-earthquake artefact.

### 9. "The compactness measure is geometrically wrong"

**Accepted; the reviewer's counterexample is exact.** Our implementation returns SD_R = 0.0 for a 400-point ring of radius 100 km, confirming the point, and this test is retained as a unit check in `geometry.py`.

SD_R is replaced by the radius of gyration, the eigenvalues of the spatial covariance (major/minor axes, elongation, azimuth) and convex-hull area, with bootstrap intervals that include location jitter at the catalogue resolution floor.

We also audited the published table (`results/tables/published_compactness_audit.csv`). Recovering R_g from the reported R̄ and SD_R gives **C4 = 19.97 km and C3 = 20.96 km — a difference of 0.99 km**, against a rounding-induced resolution floor of 0.45 km. The reviewer's ~1 km estimate was right, and the claim that C4 was "the most compact domain" is withdrawn.

### 10. "The four stages are editorial work, not an algorithmic result"

**Accepted. The four-stage model is withdrawn entirely.** It is not restated in weakened form.

What replaces it is a two-segment structure with one transition, established without using time to build the groups: western segment median 11 August, eastern segment median 25 August, a 13.6-day shift significant at q = 1.1 × 10⁻²⁵. We no longer connect cluster means with lines; Figure 7 plots individual events, not cluster centroids.

### 11. "Progressive localization has not been separated from algorithmic artefact"

**Tested with the null model the reviewer specified.** Shuffling event times and re-clustering 500 times gives a null distribution for the correlation between cluster mean date and radius of gyration of +0.011 ± 0.208. The observed value is −0.402, **p = 0.020** (Figure 3b).

So the effect is real but weak — a single test at the 2% level with a wide null. We report it as "real but weak" rather than as an organising principle, and the paper's conclusions do not rest on it.

### 12. "C6–C7 are not shown to be postseismic redistribution"

**Accepted, and now settled empirically.** We applied nearest-neighbour declustering (Zaliapin & Ben-Zion, 2013) and Poisson rate comparison against the 2010–2018 pre-sequence background at a common Mc.

The result is decisive (Figure 6c): the rate increase is ×338 within 25 km, ×42 at 25–50 km, ×6.3 at 50–75 km, and **×1.9 at 75–100 km, which is not significant (p = 0.32)**. Beyond about 75 km there is no detectable response to the sequence.

Dispersed later seismicity at regional distance is therefore **background seismicity that postdates the mainshock**, exactly as the reviewer suspected. We adopted the suggested wording ("later regional seismicity") and go further by giving the distance at which triggering becomes undetectable. Aftershock decay within the triggered volume is ordinary: p = 0.946, c = 0.19 d.

### 13. "The b-value analysis cannot support a mechanical interpretation"

**Accepted on all four sub-points.**

**13.1 Mixed magnitude scales.** Resolved by the new catalogue, which is homogenised Mw.

**13.2 Different Mc between clusters.** All comparisons now use a **common Mc = 3.7**, justified as the most conservative value applicable to every period compared. We report the sensitivity explicitly: b ranges from 0.95 (Mc = 3.4) to 1.39 (Mc = 4.3). Uncertainty is bootstrapped with **Mc re-estimated inside every resample**, so the interval propagates the completeness decision instead of conditioning on it. We also state where this matters: the bootstrap mean sits 0.02–0.12 above the fixed-Mc estimate, without changing any ordering.

**13.3 The C1 threshold was moved because the result was inconvenient.** Accepted without qualification. No threshold in the new analysis is selected by hand, and no group-specific threshold is used at all. Where a group has too few events above the common threshold, it is reported as not estimable — as the reviewer instructed.

**13.4 Low b and high mean magnitude are one statistic.** Confirmed exactly. For fixed Mc, b = log₁₀e/(M̄ − (Mc − ΔM/2)) is an exact reciprocal identity (Spearman −1.000). We verified the double-counting arithmetically: the published b = 0.58 at Mc = 4.1 implies a mean magnitude above Mc of **4.80**, which is precisely the "M̄ = 4.8" the previous Table 1 reported as independent corroboration. The new paper never cites both as separate evidence.

**13.5 The differences were not significant.** Confirmed, and worse than the reviewer estimated. We ran all 28 pairwise Utsu tests on the previously published b-values with Benjamini–Hochberg correction: **zero survive at q < 0.05.** The strongest (C3–C4) has p = 0.037, q = 0.368. The entire published b-value narrative was unsupported.

In the new analysis, two contrasts do survive: near-field versus intermediate (Δb = 0.301, q = 9.4 × 10⁻⁶), and the southern fore-arc versus both thrust groups (q = 1.2 × 10⁻¹³). Notably, the two thrust groups are **not** distinguishable (q = 0.36), and we report that as a result.

### 14. "Excluding magnitude from the input does not make magnitude results independent"

**Accepted; the permutation test the reviewer specified is implemented.** Memberships fixed, magnitudes shuffled, 5,000 permutations: p = 0.039 for the minimum group b-value and p = 0.065 for the b-value range. The word "independently" is removed.

We added a further test the reviewer did not request but which the same logic demands. The near-field zone is defined around the largest event, so the largest events are inside it by construction. Excluding progressively more of them (Table 3): Δb falls from 0.301 to 0.173 but remains significant with every event above **Mw 5.0** removed (p = 0.018). The contrast is a property of the volume, not of a few large events.

### 15. "Raw event count is not seismic productivity"

**Accepted.** The word "productive" is removed. Rates are now reported as events per year above a common Mc with explicit exposure (Table 4), and the productivity parameter K of the Omori–Utsu fit is estimated by maximum likelihood rather than inferred from a count.

### 16. "Focal mechanisms cannot validate eight clusters"

**Accepted, and the data are thinner than previously stated.** The Global CMT search returns 25 solutions for the region over 1976–2025, of which **only 8 fall inside the study window** — not the 22 previously claimed for the sequence. We state this plainly.

Everything the reviewer asked for is now provided: an explicit matching criterion (within 120 s and 60 km of the centroid), the match outcome for every mechanism (8 of 8 matched), per-zone counts, and Kagan angles. Mechanism coherence in the 25–75 km zone is genuine and quantified: **mean pairwise Kagan angle 39.6°** against 73.4° for random double couples. The near-field pair differs by 84.9°, but with n = 2 we state it is not interpretable.

We agree that eight mechanisms cannot validate a partition, and we make no such claim. Stress-tensor inversion is not attempted; the data do not support it.

### 17. "Rinjani is interpretive ornament"

**Accepted.** We adopted the reviewer's own formulation almost verbatim. Section 5.4 states that the seismicity distribution is spatially compatible with previously reported crustal heterogeneity near Rinjani, notes that our analysis contains no variable measuring temperature, attenuation, velocity, fluids or fracture density, and therefore cannot test the hypothesis. No claim of magmatic triggering or thermal control is made.

### 18. "The novelty is too thin for doctoral work"

**Accepted as a criticism of the previous version.** We agree that re-deriving known tectonics with a mislabelled algorithm is not a contribution.

The contribution now claimed is different and, we hope, defensible on its own terms:

1. A **quantified identifiability analysis** of a class of study that is common and rarely tested — including a measurement of how much temporal structure is manufactured by including time as a clustering variable (a factor of two here).
2. A **catalogue artefact with general consequences**: unresolved default depths reproduce the exact signature of a thin, well-defined seismogenic layer. Any study using depth as a clustering feature should report the default-depth fraction; we could not find one that does.
3. A **positive seismological result reproduced from catalogue statistics alone** — segmented, sequential, eastward activation of the back-arc thrust with a 13.6-day inter-segment delay — matching what source inversion found independently, with time held out of the clustering.
4. A **quantified triggering radius** of about 75 km for this sequence, and a near-field b-value depression that survives removal of every event above Mw 5.0.
5. A **negative methodological result stated plainly**: at the supported cluster number the custom algorithm and k-means are interchangeable (ARI = 0.993), and at K = 8 the custom algorithm is the less stable of the two.

If the reviewer judges that this is a methodological paper rather than a discovery paper, we would not dispute the characterisation.

### 19. "The Introduction spends space on damage that is never analysed"

**Accepted.** The casualty and damage discussion is reduced to two sentences establishing why the sequence matters, and the damage photograph is removed. We did not attempt a shaking or vulnerability analysis, so we no longer illustrate one.

### 20. "'Available upon reasonable request' is not acceptable"

**Accepted without reservation.** Everything is released: both raw data files, the complete analysis code, all intermediate tables including per-event cluster labels and declustering assignments, and every figure. `python3 reanalysis/run_all.py` regenerates the entire paper from the raw files in about six minutes. All stages are seeded, so results are bit-reproducible.

---

## Part II — the twenty examination questions

| # | Question | Answer |
|---|---|---|
| 1 | What makes it a SOM after neighbourhood update is removed? | Nothing. It is a winner-take-all competitive vector quantisation, and is now named that. |
| 2 | Why eight neurons? Show C3–C4 persist at K = 6, 7, 9, 10. | There is no justification for eight; K is now estimated. Silhouette peaks at K = 4, gap at K = 2, and on the full catalogue in space K = 3 (ARI = 0.980). Persistence across K = 6–10 is tabulated in `cluster_persistence.csv`. The C3–C4 claim is withdrawn. |
| 3 | Adjusted Rand index after 100 order shuffles? | 0.923 ± 0.018 over 200 shuffles (minimum 0.842). Order is not the dominant instability; bootstrap ARI at K = 8 is 0.574. |
| 4 | Why 100 epochs when α ≈ 10⁻⁸ after 20? | There is no reason. Labels are identical at 25 and 100 epochs; 75 epochs are no-ops. α(100) = 7.9 × 10⁻³³. |
| 5 | Physical meaning of equating the time and depth ranges? | None. It is an undeclared modelling choice, now stated as such. |
| 6 | How many days equal 10 km in your metric? | 24 days for 10 km of depth; 17 days for 10 km horizontally. |
| 7 | Why does horizontal position get two dimensions and time one? | No justification. It gives horizontal position twice the weight in squared Euclidean distance; now stated, and tested by re-weighting. |
| 8 | How can output built using time be independent evidence for temporal evolution? | It cannot. The circularity is measured (159.5 vs 80.9 days) and the design is changed: cluster on space, test time independently (H = 104.2, p = 2.4 × 10⁻²³). |
| 9 | SD_R for events on a 100 km ring — is that cluster compact? | SD_R = 0 exactly; R_g = 100 km. Not compact. This is now a unit test in the code. |
| 10 | Why was C4 called most compact when C3's mean radius is smaller? | It should not have been. R_g gives C4 = 19.97 km and C3 = 20.96 km, a 0.99 km difference against a 0.45 km resolution floor. Claim withdrawn. |
| 11 | What evidence that C6–C7 were triggered rather than background? | None, and we now show the opposite: beyond 75 km the rate increase is ×1.9, p = 0.32. Far-field later seismicity is background. |
| 12 | Why was C1's Mc changed when the automatic result was inconvenient? | It should not have been. No threshold is chosen by hand in the new analysis; a common Mc = 3.7 is used throughout. |
| 13 | Are the C3–C2 and C3–C4 b-differences significant by Utsu? | No. All 28 published pairwise tests fail after FDR correction; the strongest is p = 0.037, q = 0.368. |
| 14 | Why treat high mean magnitude and low b as two pieces of evidence? | They are one. b = log₁₀e/(M̄ − (Mc − ΔM/2)) exactly. The published b = 0.58 implies M̄ = 4.80 above Mc — the figure reported as corroboration. |
| 15 | What are all cluster b-values at a common Mc = 4.4? | The new analysis uses a common Mc = 3.7 on a homogenised catalogue: near-field 0.975 ± 0.049, intermediate 1.277 ± 0.032, far-field 1.190 ± 0.134; by group, 0.990, 1.002 and 1.795. Full sensitivity from Mc = 3.4 to 4.6 in `b_vs_mc_sensitivity.csv`. |
| 16 | How many focal mechanisms actually fall in C3 and C4? | The question no longer applies, but the matching is now explicit: 8 mechanisms exist in the window, all 8 matched to catalogue events; 6 lie at 25–75 km (mean Kagan 39.6°) and 2 within 25 km. |
| 17 | What is new that is not already known from relocated seismicity? | The identifiability analysis, the fixed-depth artefact, the ~75 km triggering radius, the near-field b-depression surviving Mw ≥ 5.0 removal, and the demonstration that segmented sequential rupture is recoverable from catalogue statistics with time withheld. |
| 18 | If plain k-means gives the same clusters, what does your SOM contribute? | Nothing, and we now state it: at K = 3, ARI(WTA, k-means) = 0.993. At K = 8 the custom method is *less* stable (0.574 vs 0.829). |
| 19 | If simple time bins give the same localization, what does the ML contribute? | Very little. The localization trend is p = 0.020 against a shuffled-time null, and the migration result (ρ = +0.398) is obtained by projecting epicentres on the strike axis without any clustering at all. We say so in Section 5.3. |
| 20 | Why are data and code not open if reproducibility is claimed? | They are now — all data, all code, all intermediate tables, one command, seeded. |

---

## Part III — the reviewer's required analyses

| Required | Where |
|---|---|
| 1. Fix or rename the algorithm | Section 3.1; true Kohonen SOM implemented with QE 0.145 and TE 0.003 |
| 2. Test cluster number (K = 2…15) with silhouette, DB, CH, gap, bootstrap, ARI | Section 4.1, 4.4; Figure 2a; `k_scan.csv`, `spatial_k_scan.csv` |
| 3. Break the link between time and the research aim | Section 4.4, 4.7 — clustering on space, time withheld as test variable |
| 4. Training sensitivity: order, initialisation, schedules, convergence | Section 4.1; `a1_identifiability.json` |
| 5. Metric tests: min–max, z-score, robust, Mahalanobis, weights, no deep events | Section 4.1; `scaling_sensitivity.csv` |
| 6. A better catalogue | Section 2 — 25,278 homogenised-Mw events versus 248 |
| 7. Baselines: k-means, GMM, hierarchical, HDBSCAN, time bins | Section 4.4; `method_benchmark.csv` |
| 8. Proper compactness: covariance ellipses, R_g, axes, area, uncertainty | Section 3.3, Table 2; `geometry.py` |
| 9. Redo Gutenberg–Richter: homogeneous M, common Mc, GFT, bootstrap, Utsu, permutation, multiple comparisons, mainshock sensitivity | Section 3.4, 4.5; Tables 3; Figure 5 |
| 10. Test postseismic triggering: declustering, rate change, background comparison | Section 3.5, 4.6; Figure 6 |
| 11. Match focal mechanisms to groups with counts, criterion, Kagan angles | Section 3.6, 4.8; `focal_catalogue_match.csv`, `kagan_by_zone.csv` |
| 12. Open data and code | Section 7 |

Not done, and why: **ETAS fitting** and **Coulomb stress modelling** (point 10) were not attempted. With Mc = 3.7 and a two-decade record, an ETAS fit would be poorly constrained relative to what the nearest-neighbour method and the direct rate comparison already establish, and Coulomb modelling requires slip distributions we do not derive. **Stress-tensor inversion** (point 11) is not attempted with eight mechanisms. **Relocation** is not attempted, so the study remains two-dimensional in space; we state this as the principal limitation and the reason no depth-resolved inference is offered.

---

## What we ask of the reviewer

We do not ask that the previous conclusions be reconsidered; we have withdrawn them. We ask instead whether the reduced set of claims — two thrust segments with indistinguishable b-values activating 13.6 days apart, a distinct fore-arc domain, a near-field b-value depression surviving Mw ≥ 5.0 removal, an ordinary Omori decay, and a ~75 km triggering radius — is proportionate to the evidence now presented, and whether the identifiability analysis and the fixed-depth artefact constitute a contribution in their own right.

If the judgement is that this is a methodological paper about the limits of catalogue clustering rather than a discovery paper about Lombok, we accept that framing and would retitle accordingly.
