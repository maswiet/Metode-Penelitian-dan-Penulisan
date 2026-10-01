# Segmented rupture and near-field b-value depression in the 2018 Lombok earthquake sequence: a stability-first reanalysis

Bakti Sukrisna¹, Bagus Endar Bachtiar Nurhandoko²'³*, Wiwit Suryanto¹, Afif Rakhman¹, Yoga Hariman³

¹ Department of Physics, Faculty of Mathematics and Natural Sciences, Universitas Gadjah Mada, Sekip Utara, Bulaksumur, Yogyakarta 55281, Indonesia
² Earth Physics and Complex System Research, Faculty of Mathematics and Natural Sciences, Institut Teknologi Bandung, 10 Ganesha Street, Bandung 40132, Indonesia
³ Rock Fluid Imaging Lab, 5A Sukasenang Raya St., Bandung 40124, Indonesia

\* Corresponding author: bagus@itb.ac.id

---

## Abstract

Unsupervised clustering is increasingly used to reconstruct the spatiotemporal evolution of earthquake sequences, but the reliability of the resulting "domains" is rarely tested. We reanalyse the 2018 Lombok sequence using a homogenised moment-magnitude catalogue of 25,278 events spanning 1998–2023, an order of magnitude larger than catalogues previously applied to this problem, and we make partition stability the primary object of study rather than an afterthought. Three results follow. First, an eight-cluster partition of this catalogue is not identifiable: no internal validity index selects eight groups, the bootstrap adjusted Rand index of a winner-take-all partition at K = 8 is 0.57, and halving the weight given to the time axis changes the partition (ARI = 0.47). Because occurrence time is one of the clustering variables, roughly half of the apparent temporal separation between clusters is inserted by the input rather than discovered; and because 53.5% of hypocentres carry an unresolved default depth of 10 km, apparent depth compactness tracks the fraction of default depths (r = −0.75) rather than any physical thinning of the seismogenic layer. Second, clustering on horizontal position alone yields three groups that reproduce almost perfectly (bootstrap ARI = 0.98) and survive a 0.4° shift of the study boundary: two back-arc thrust groups west and east of 116.5° E with statistically indistinguishable b-values (0.990 ± 0.032 and 1.002 ± 0.031; Utsu q = 0.36), and a southern Lombok fore-arc group with a much higher b-value (1.79 ± 0.10; Utsu q = 1.2 × 10⁻¹³). Because time was withheld from the clustering, it can serve as an independent test variable: the three groups differ strongly in occurrence time (Kruskal–Wallis H = 104.2, p = 2 × 10⁻²³), and activity migrates eastward through the sequence (Spearman ρ = +0.40, p = 1.4 × 10⁻³⁷), with the eastern group activating 13.6 days after the western one. Third, seismicity within 25 km of the mainshock has a significantly lower b-value than the surrounding volume (0.98 versus 1.28; Utsu q = 9 × 10⁻⁶), a contrast that survives removing every event above Mw 5.0 (p = 0.018). Aftershocks decay with an ordinary Omori–Utsu exponent (p = 0.95, c = 0.19 d), and rates remain elevated above the pre-sequence background for years, but only within about 75 km: beyond that distance no rate increase is detectable (p = 0.32), so far-field activity is background seismicity rather than postseismic redistribution. We conclude that the 2018 Lombok sequence is well described as the sequential activation of two adjacent Flores back-arc thrust segments with a distinct fore-arc domain to the south, and that claims of finer domain structure or multi-stage evolution exceed what this class of catalogue can resolve.

**Keywords:** 2018 Lombok earthquake sequence; cluster stability; Gutenberg–Richter b-value; nearest-neighbour declustering; Flores Back-Arc Thrust; catalogue artefacts.

---

## 1. Introduction

The 2018 Lombok earthquake sequence was among Indonesia's most destructive recent seismic episodes. Between 29 July and 19 August 2018 the island was struck by several strong earthquakes, including an Mw 6.9 event on 5 August and Mw 6.3 and Mw 6.9 events on 19 August. The sequence caused 561 fatalities and displaced more than 400,000 people (AHA Centre, 2018). It occurred on the Flores Back-Arc Thrust (FBT), a regional compressional system extending from northern Flores to northern Bali (Hamilton, 1979; McCaffrey, 1988; Bock et al., 2003; Koulali et al., 2016), immediately north of the Rinjani volcanic complex.

Published source studies agree that the sequence involved cascading or partial rupture of multiple thrust segments rather than a single fault plane (Salman et al., 2020; Yang et al., 2020), and relocated seismicity, tomography and shear-wave splitting have characterised the source volume in detail (Supendi et al., 2020; Afif et al., 2021; Lythgoe et al., 2021; Sasmi et al., 2023; Zhao et al., 2024). Against this well-studied background, the question this paper addresses is methodological as much as tectonic: **when unsupervised clustering is applied to a regional earthquake catalogue, how much of the resulting structure is a property of the seismicity, and how much is a property of the algorithm, the metric and the catalogue?**

The question is not rhetorical. Clustering algorithms return a partition for any K the analyst supplies, and internal validity indices, resampling stability and null models are the only instruments that distinguish a discovered domain from an imposed one. Where occurrence time is included among the clustering variables and the resulting clusters are then ordered by time to define evolutionary stages, the inference is circular by construction. Where hypocentral depth is included but a large fraction of depths are unresolved defaults, apparent vertical structure is a reporting artefact. Where cluster-specific b-values are compared across many pairs at different completeness thresholds without correction, nominally striking contrasts need not survive.

We therefore adopt a stability-first design. We begin from a catalogue large enough to support the question (Section 2), quantify what a clustering of it can and cannot identify (Section 4.1–4.2), and then report only those results that survive resampling, null models and multiple-comparison control (Section 4.3–4.6). Some of our results are negative, and we report them as such; the positive results that remain are correspondingly better supported. All data, code and intermediate tables are released (Section 7).

## 2. Data

### 2.1 Earthquake catalogue

We use a regional catalogue of 25,280 events for the eastern Sunda–Banda arc spanning 2 January 1998 to 31 December 2023, covering 113.5°–122.5° E and 13.94°–7.00° S with depths from 2 to 750 km. Magnitudes are reported on a single homogenised moment-magnitude scale (Mw 2.46–7.27); the non-integer magnitude values throughout the file indicate that the conversion from the original reporting scales was applied at catalogue level rather than by us. Homogeneity of the magnitude scale is a prerequisite for the frequency–magnitude comparisons in Section 4.5 and is the principal advantage of this catalogue over the compilation used previously for this problem.

Quality control removed records with missing origin time, hypocentre or magnitude, and records duplicated in origin time and rounded hypocentre. Two records were removed, leaving **25,278 events**. Hypocentres were projected to UTM zone 50S (EPSG:32750).

### 2.2 Three catalogue properties that constrain the analysis

Three features of this catalogue, quantified in Figure 1, limit what any method applied to it can resolve. They are stated here because they determine the design of everything that follows.

**Reporting completeness changes in 2009.** Annual counts of Mw ≥ 4.0 events rise from roughly 40 per year (1998–2008) to more than 240 per year from late 2009 (Figure 1a), a network densification rather than a tectonic change. Estimated completeness magnitudes in the Lombok region are Mc = 4.4 (1998–2008), 3.7 (2009 to mid-2017), 3.6 (2017–2019) and 3.3 (2019–2023) (Figure 1c). Any comparison of rates across this boundary is meaningless, so all rate and b-value analyses are restricted to **1 October 2009 onward** and use a **common Mc = 3.7**, the most conservative value applicable to every sub-period compared.

**Half of all depths are unresolved.** Within the 2017–2019 window and the Lombok region, **53.5% of events carry a depth of exactly 10 km** (Figure 1b), the default assigned when depth is not constrained, and 78% are reported shallower than 15 km. Depth is therefore not a usable clustering feature for this catalogue, and any statistic computed on the depth axis is dominated by the default value. We show in Section 4.3 that this alone accounts for apparent depth compactness.

**Hypocentres are rounded.** Coordinates are given to 0.01° and depths to 1 km. Rounding alone imposes a horizontal resolution floor of 0.45 km (standard deviation of a uniform quantisation error over a 1.1 km cell), before any true location uncertainty is considered. Differences in cluster size of order 1 km are therefore not interpretable.

### 2.3 Focal mechanisms

We use Global CMT centroid-moment-tensor solutions (Dziewonski et al., 1981; Ekström et al., 2012) for 115°–117.5° E, 9.5°–7.5° S, Mw ≥ 5.5, 1976–2025: **25 solutions in total, of which 8 fall inside the 2017–2019 study window.** Nodal planes, scalar moments and faulting styles were computed from the moment tensors. We note explicitly that eight is the entire mechanism resource for this sequence above Mw 5.5; per-group mechanism statistics are limited by the data, not by the matching procedure.

### 2.4 Study region

The sequence analyses use a Lombok–Sumbawa back-arc region of 115.75°–117.25° E, 8.90°–7.90° S and 0–60 km depth. Section 4.7 shows that the results do not depend on this choice.

## 3. Methods

### 3.1 What the algorithms are, and what they are called

We evaluate three families of partitioning method and are explicit about their names.

A **winner-take-all (WTA) competitive vector quantisation** updates only the best-matching prototype for each observation:

  W_c(q+1) = W_c(q) + α_e [x_i − W_c(q)],  c = arg min_j ‖x_i − W_j‖²,

with all other prototypes unchanged. This is the procedure used in the earlier version of this study. It has no neighbourhood function, no neighbourhood radius and no lattice. Because topology preservation in a Self-Organizing Map arises specifically from neighbourhood updating on a lattice (Kohonen, 1982, 1995), a procedure without those elements is not a Self-Organizing Map and cannot be described as topology-preserving. We therefore call it a winner-take-all competitive vector quantisation throughout, and we report no topological quantity for it because none is defined.

A **Kohonen Self-Organizing Map** proper is implemented separately for comparison, on a 4 × 2 lattice with a Gaussian neighbourhood whose radius and learning rate both decay exponentially. For this map, quantisation error and topographic error are defined and reported.

**Baselines** are k-means, a full-covariance Gaussian mixture, Ward agglomerative clustering and HDBSCAN. A custom method that does not outperform these on the same data provides no methodological contribution, and we test this directly.

### 3.2 Cluster number, stability and the null models

The number of clusters is treated as a quantity to be estimated, not assumed. For K = 2…15 we compute the silhouette coefficient, Davies–Bouldin and Calinski–Harabasz indices, and the gap statistic against uniform references.

Stability is measured by the **adjusted Rand index (ARI)** between the full-data partition and partitions refitted on 50–100 bootstrap resamples, scored on the events the two partitions share. We take ARI ≥ 0.8 as the conventional threshold for a reproducible partition. We additionally measure sensitivity to **event order** (200 random permutations of the presentation order for the online WTA procedure), to **initialisation** (the radial-shell scheme of the earlier version, random, k-means++ and principal-component starts), and to **feature scaling** (min–max, z-score, robust and Mahalanobis, plus explicit re-weighting of the time and horizontal axes).

Two null models test the temporal claims. To ask whether clusters carry more temporal information than their sizes alone imply, we compare the observed spread of cluster mean dates against 2,000 random groupings of identical sizes. To ask whether progressive spatial localization is a real trend, we recompute the correlation between cluster mean date and cluster radius of gyration on 500 catalogues in which **event times have been shuffled**, which destroys temporal structure while leaving the spatial pattern intact.

### 3.3 Spatial descriptors

The standard deviation of radial distance from a centroid, SD_R, used in the earlier version as a compactness measure, is not one: a ring of events of radius 100 km has SD_R = 0 while spanning 200 km. We instead use the **radius of gyration** R_g = √⟨|x − x̄|²⟩, the eigenvalues of the spatial covariance (major and minor axes, elongation and azimuth) and the convex-hull area. Uncertainty on R_g is obtained by bootstrap with added Gaussian jitter equal to the catalogue's rounding-induced resolution floor, so that differences can be compared against what the data can resolve. For comparison with published tables, R_g can be recovered from a reported mean radius and SD_R as R_g = √(R̄² + [(N−1)/N] SD_R²).

### 3.4 Frequency–magnitude analysis

Completeness is estimated both by maximum curvature and by the goodness-of-fit criterion of Wiemer and Wyss (2000) at the 90% level. b-values use the Aki (1965) maximum-likelihood estimator with the Bender (1983) bin correction and the Shi and Bolt (1982) standard error. Two features distinguish the present treatment:

1. **A common completeness threshold** is used for all groups compared. Comparing slopes estimated above different thresholds does not test the same quantity. We report the sensitivity of the regional b-value to this choice explicitly.
2. **Uncertainty includes the completeness decision.** A bootstrap re-estimates Mc inside every resample, so the reported interval propagates the choice of threshold rather than conditioning on it.

Differences between b-values are tested with the **Utsu (1992) likelihood ratio** and corrected for multiple comparisons by the Benjamini–Hochberg procedure. A **permutation test** holds group memberships fixed and shuffles magnitudes between events, giving the distribution of the most extreme group b-value under the null of no magnitude–group association.

We note an identity that governs the interpretation: for a fixed Mc the Aki estimator is b = log₁₀e / (M̄ − (Mc − ΔM/2)), an exact reciprocal function of the mean magnitude. A low b-value and a high mean magnitude in the same group are therefore one measurement reported twice, not two independent lines of evidence.

### 3.5 Triggering and background

Background and triggered events are separated using **nearest-neighbour distances in the space–time–magnitude metric** of Zaliapin and Ben-Zion (2013): for each event j, η = min_i [ t_ij · r_ij^d_f · 10^(−b(m_i − Mc)) ] over earlier events i, with t in years, r in kilometres, d_f = 1.6 and b from the regional fit. The threshold separating the background and clustered modes is placed by minimising within-mode variance rather than by eye.

Aftershock decay is fitted by maximum likelihood to the modified Omori law n(t) = K/(t + c)^p as a non-stationary Poisson process, with K profiled out analytically, so no binning choice enters the estimate. Whether later seismicity is elevated above background is tested by a binomial comparison of counts against exposure between the pre-sequence period and each later period, at the common Mc.

### 3.6 Focal-mechanism matching

Mechanisms are matched to catalogue events by an explicit criterion — within 120 s of the centroid time and 60 km of the centroid location — and unmatched mechanisms are reported rather than dropped. Mechanism heterogeneity within a group is measured by the **Kagan angle**, the minimum rotation between two double couples, referenced against the ≈ 73° mean expected for randomly oriented pairs.

### 3.7 Verification

Each estimator was checked against a control before use: the b-value routine recovers b = 0.99 from a synthetic catalogue drawn with b = 1.00; the Omori–Utsu fit recovers (p, c) from three synthetic sequences with known parameters; the Kagan angle returns 0° for identical mechanisms and 90° for a thrust against a normal mechanism; and the radial statistic returns SD_R = 0 for the 100 km ring described in Section 3.3.

## 4. Results

### 4.1 An eight-cluster partition of this catalogue is not identifiable

We first ask whether an eight-cluster partition in the four-dimensional easting–northing–depth–time space is supported. To make the comparison with the earlier version like-for-like, we use a subset of comparable size: the manuscript study box and window at Mw ≥ 4.4, giving n = 277 events.

**No index selects eight clusters** (Figure 2a). The silhouette coefficient is maximised at K = 4 (0.557) and falls to 0.485 at K = 8; the gap statistic is maximised at K = 2; bootstrap stability declines monotonically from ARI = 0.98 at K = 2 to 0.80 at K = 8 and below 0.65 at K = 9 and K = 11.

**The training schedule is decorative** (Figure 2b). With α₀ = 0.01 halved each epoch, α = 9.5 × 10⁻⁹ by epoch 20 and 7.9 × 10⁻³³ by epoch 100 — below double precision from epoch 52. We verified that cluster labels are **identical after 25 and after 100 epochs**: 75 of the 100 epochs perform no computation that changes the result.

**The partition does not reproduce** (Figure 2c). At K = 8 the WTA partition has a bootstrap ARI of **0.574**, well below the 0.8 reproducibility threshold, and below plain k-means on the same data (0.829). Sensitivity to event order is moderate rather than severe (ARI = 0.923 ± 0.018 over 200 shuffles, minimum 0.842), so processing order is not the dominant instability; sample composition is. The WTA and k-means partitions at K = 8 agree only weakly (ARI = 0.336), so the custom procedure is not recovering the same structure as the baseline — it is recovering a less stable one.

**The metric embeds an undeclared exchange rate.** Under min–max scaling each axis spans one unit, so the metric equates the full time range with the full depth range. For this dataset that means **2.4 days per kilometre of depth and 1.7 days per kilometre of horizontal distance**: 10 km of depth is treated as equivalent to 24 days. Horizontal position moreover occupies two of the four axes and therefore carries twice the weight of depth or time in the squared Euclidean distance. These are modelling choices, not consequences of normalisation. Changing them changes the answer: halving the weight of the time axis yields a partition sharing only ARI = 0.466 with the min–max result, and robust scaling gives 0.715.

### 4.2 Half of the apparent temporal separation is inserted by the input

Because occurrence time is one of the clustering variables, clusters can be ordered by time whether or not the seismicity carries temporal structure. Table 1 and Figure 3a separate the two contributions.

| Clustering features | Spread of cluster mean dates | Random-grouping null | p | Bootstrap ARI |
|---|---:|---:|---:|---:|
| Easting, northing, depth, time | 159.5 d | 30.9 d | 0.0005 | 0.798 |
| Easting, northing, depth | 80.9 d | 32.5 d | 0.0010 | 0.594 |
| Easting, northing | 34.9 d | 32.0 d | 0.370 | 0.837 |

*Table 1. Temporal separation of clusters as a function of which variables enter the clustering.*

Including time inflates the apparent temporal separation from 80.9 to 159.5 days — **roughly half of the reported temporal structure is a restatement of the input.** The remaining half is real: clusters formed without time still separate in time significantly (p = 0.0010). Space alone, at this sample size, does not (p = 0.370); Section 4.4 shows that with the full catalogue it does.

Progressive spatial localization is likewise real but weak (Figure 3b). The correlation between cluster mean date and radius of gyration is r = −0.402, against a shuffled-time null of +0.011 ± 0.208 (p = 0.020, single test). This is a genuine effect at the margin of significance, not the strong organising principle it has been presented as.

### 4.3 Apparent depth localization is a reporting artefact

Across the eight-cluster partition of the replication sample (in which 54.5% of events carry the default depth), the standard deviation of depth within a cluster is strongly **anti-correlated with the fraction of that cluster's events carrying the 10 km default depth (r = −0.745)**. Clusters that appear vertically compact are those made mostly of events whose depths were never determined. In the crustal sequence region over the 2017–2019 window (n = 2,117, of which 53.5% carry the default depth), the depth standard deviation is 5.8 km using all events but rises to 6.7 km using only the 985 events with resolved depths: removing the unresolved events makes the population *less* vertically concentrated, not more.

A cluster reported as "the shallowest, most vertically concentrated domain" with a depth dispersion of about 5 km is therefore not evidence of a thinning seismogenic layer. We conclude that **no vertical-structure inference can be supported by this catalogue**, and we exclude depth from all subsequent clustering.

### 4.4 Three spatial groups are reproducible

Clustering the completeness-limited modern catalogue (n = 1,582 events at Mw ≥ 3.7, 2009–2023) on **horizontal position alone** — withholding time so that it remains available as an independent test variable — gives a different picture. The silhouette coefficient is maximised at K = 3 (0.454) with a bootstrap ARI of **0.980** (5th percentile 0.954). K = 8 on the same data reaches silhouette 0.395 and ARI 0.853.

| Group | n | Centroid | R_g (km) | Elongation | Azimuth | b (Mc = 3.7) | Median date |
|---|---:|---|---:|---:|---:|---|---|
| Western thrust | 625 | 8.24° S, 116.24° E | 22.5 [21.7, 23.3] | 1.94 | 070° | 0.99 ± 0.03 | 11 Aug 2018 |
| Southern fore-arc | 259 | 8.67° S, 116.27° E | 29.4 [27.4, 31.7] | 2.04 | 104° | 1.79 ± 0.10 | 07 Aug 2018 |
| Eastern thrust | 698 | 8.34° S, 116.81° E | 23.9 [22.8, 24.8] | 1.53 | 097° | 1.00 ± 0.03 | 25 Aug 2018 |

*Table 2. The three reproducible spatial groups (Figure 4). R_g intervals are 95% bootstrap with location jitter at the catalogue resolution floor. Azimuth is of the major axis, clockwise from north.*

The two thrust groups lie along the back-arc system north of Lombok, west and east of about 116.5° E, and are elongated approximately east–west (070° and 097°), parallel to the mapped thrust front. Both are cut by the mainshock area. The third group lies south of the island in the fore-arc, is separated from the thrust groups by about 40 km, and has a markedly different magnitude distribution.

**The method used does not matter at this K.** k-means, the WTA procedure and a Gaussian mixture all recover essentially the same three groups (WTA versus k-means, ARI = 0.993). This answers the methodological question directly: at the cluster number the data actually support, the custom procedure and plain k-means are interchangeable, so the choice of algorithm contributes nothing to the result. A genuine Kohonen SOM on a 4 × 2 lattice achieves a topographic error of 0.003, confirming near-perfect topology preservation, at a higher quantisation error (0.145) than the WTA procedure (0.095) — the expected trade-off, and the reason a topology-preserving map cannot be claimed for a procedure that has no lattice. HDBSCAN finds only two clusters and labels 18.6% of events as noise.

### 4.5 b-values: what survives proper testing

The regional b-value at the common Mc = 3.7 is **1.19 ± 0.03** (Shi–Bolt); the bootstrap that also re-estimates Mc gives 1.13 ± 0.04 with Mc = 3.59 ± 0.03. The estimate is sensitive to the completeness choice — b ranges from 0.95 at Mc = 3.4 to 1.39 at Mc = 4.3 — which is why a common, justified threshold is essential.

**By tectonic zone** (Figure 5a), seismicity within 25 km of the mainshock has b = 0.975 ± 0.049 (n = 404), against 1.277 ± 0.032 (n = 1,293) at 25–75 km and 1.190 ± 0.134 (n = 62) beyond 75 km. The near-field/intermediate contrast is significant after FDR correction (Δb = 0.301, Utsu q = 9.4 × 10⁻⁶); the far-field group is distinguishable from neither, its 62 events being too few (q = 0.20 and 0.32).

The near-field zone is defined around the largest event, so the contrast must be shown not to be an artefact of the mainshock itself (Figure 5c). It is not:

| Events excluded | b (near field) | b (25–75 km) | Δb | p |
|---|---:|---:|---:|---:|
| none | 0.975 | 1.277 | 0.301 | 3.1 × 10⁻⁶ |
| Mw ≥ 6.0 | 1.033 | 1.277 | 0.243 | 3.1 × 10⁻⁴ |
| Mw ≥ 5.5 | 1.052 | 1.291 | 0.239 | 5.0 × 10⁻⁴ |
| Mw ≥ 5.0 | 1.146 | 1.319 | 0.173 | 1.8 × 10⁻² |

*Table 3. The near-field b-value depression survives removal of the large events that define the zone.*

The depression is attenuated but not removed by excluding every event above Mw 5.0, so it is a property of the near-rupture volume's magnitude distribution rather than of a few large events. A permutation test on zone labels gives p = 0.039 for the minimum b-value, so the effect is modest in the multiple-comparison sense and we present it accordingly.

**By spatial group** (Figure 5b), the two thrust groups have statistically indistinguishable b-values (0.990 versus 1.002; Utsu q = 0.36) while the southern fore-arc group differs sharply from both (1.795; q = 1.2 × 10⁻¹³). This is the clearest magnitude–distribution result in the dataset: the back-arc thrust system behaves as one population in magnitude terms, and the fore-arc is a different one.

**By sequence phase**, b rises from 1.110 ± 0.036 during the main sequence to 1.407 ± 0.068 after mid-2019 (q = 0.0027), consistent with a return to a more heterogeneous, lower-stress regime after the sequence.

### 4.6 Triggering: elevated for years, but only within 75 km

Nearest-neighbour declustering of the modern catalogue at Mw ≥ 4.0 separates the population at log₁₀η = −2.29, classifying 60.9% of events as triggered (Figure 6a). We note that the distribution is only weakly bimodal at this magnitude threshold, so the split should be read as a reasonable operating point rather than a sharp natural boundary.

Aftershocks of the 5 August mainshock decay with an **ordinary Omori–Utsu law: p = 0.946, c = 0.19 d** (n = 449 over one year; Figure 6b). Nothing about the temporal decay of this sequence is anomalous.

Rates remain elevated above the pre-sequence background for years:

| Period | n | Rate (yr⁻¹) | × pre-sequence | p |
|---|---:|---:|---:|---:|
| Sep–Dec 2018 | 87 | 262.6 | 46.8 | 8 × 10⁻⁸⁹ |
| Jan–Jul 2019 | 47 | 81.4 | 14.5 | 7 × 10⁻³¹ |
| Aug 2019–Jul 2020 | 40 | 40.0 | 7.1 | 6 × 10⁻¹⁷ |
| Aug 2020–Jul 2021 | 13 | 13.0 | 2.3 | 9 × 10⁻³ |
| Aug 2021–Dec 2023 | 41 | 17.0 | 3.0 | 4 × 10⁻⁷ |

*Table 4. Seismicity rate at Mw ≥ 4.0 relative to the 2010–2018 pre-sequence background.*

The spatial reach of this elevation is the decisive result (Figure 6c). Relative to the pre-sequence background, the rate increase is a factor of 338 within 25 km of the mainshock, 42 at 25–50 km, 6.3 at 50–75 km, and **1.9 at 75–100 km, which is not statistically significant (p = 0.32)**. Beyond about 75 km there is no detectable response to the sequence at all.

This bears directly on the interpretation of dispersed later seismicity. A group of events whose centroid lies more than 75 km from the rupture and whose rate does not exceed the pre-sequence background is **background regional seismicity that happens to postdate the mainshock**, not postseismic redistribution. The distinction matters because "postseismic" asserts a causal relationship that the rate data do not support at those distances.

### 4.7 Temporal organisation and eastward migration, with time held out

Because the three groups of Section 4.4 were built from horizontal position alone, occurrence time is an independent test variable. It carries a strong signal: the three groups differ in occurrence time with **Kruskal–Wallis H = 104.2, p = 2.4 × 10⁻²³**.

The structure is a west-to-east activation (Figure 7). The eastern thrust group's events during the sequence are displaced **13.6 days later** than the western group's (Mann–Whitney q = 1.1 × 10⁻²⁵, FDR corrected), matching the 5 August (western) and 19 August (eastern) mainshocks. Across all 956 sequence events, occurrence time correlates with longitude at **Spearman ρ = +0.398, p = 1.4 × 10⁻³⁷**. The path is not monotonic — activity concentrates near 116.44° E in the first three days, moves west to 116.22° E after the 5 August event, then east to 116.76° E after 19 August — but the net migration is eastward, along a major-axis azimuth of 087°.

This is a genuine spatiotemporal result: it is not built into the clustering, it is significant by a wide margin, and it reproduces the segmented cascading rupture inferred independently from source modelling (Salman et al., 2020; Yang et al., 2020).

### 4.8 Focal mechanisms

Of the eight GCMT solutions in the study window, seven are thrust and one (17 March 2019) is normal. Matching to catalogue events by the stated criterion succeeded for all eight.

Mechanism coherence is quantifiable. Within the 25–75 km zone the six mechanisms have a **mean pairwise Kagan angle of 39.6°** (median 41.3°), well below the 73.4° expected for randomly oriented double couples — genuinely coherent thrust faulting on a common structural system. The two near-field mechanisms differ by 84.9°, but with n = 2 this is not interpretable.

Eight mechanisms cannot validate a partition into three groups, let alone eight. What they establish is that the principal events are thrust-dominated on structures compatible with the Flores Back-Arc Thrust, which is consistent with, but not independent of, published source models.

### 4.9 Sensitivity to the study boundary

Moving the southern boundary of the study region from 8.90° S to 9.10° S and 9.30° S leaves the three-group structure intact: bootstrap ARI remains 0.975–0.986, the two thrust groups keep b = 0.99–1.04, and the southern group keeps b = 1.71–1.88. The southern group's mean depth increases from 15.5 km to 18.1 km as the boundary moves south, consistent with progressive inclusion of deeper fore-arc and upper-slab seismicity. The structure is a property of the seismicity, not of the window.

## 5. Discussion

### 5.1 What the sequence was

The picture that survives testing is simple and consistent with independent source studies. The 2018 Lombok sequence activated **two adjacent segments of the Flores back-arc thrust system**, west and east of approximately 116.5° E, in that order, separated by about 14 days. The two segments are statistically indistinguishable in their magnitude distributions (q = 0.36), which is what one expects of two portions of a single structural system rather than of mechanically distinct domains. To the south, a fore-arc population with a much higher b-value (1.79 versus 1.00) forms a genuinely separate domain, and its distinctness is the most robust magnitude-distribution result in the dataset.

Within the sequence, the near-rupture volume has a depressed b-value relative to its surroundings that survives the removal of all events above Mw 5.0. This is the classical signature associated with locally elevated differential stress or asperity-dominated failure (Mogi, 1962; Scholz, 1968; Wyss, 1973), and we note the association without treating b as a calibrated stressmeter: the relationship is not unique and not transferable between settings.

Aftershock decay is unremarkable (p = 0.95). Rates stay above background for years but only within about 75 km of the rupture. Beyond that, seismicity is background.

### 5.2 What the sequence was not, on this evidence

Three claims that have been made for this sequence are not supported by a catalogue of this class, and we state that plainly.

**Eight seismogenic domains.** No validity index selects eight groups, and an eight-group partition of a few hundred events does not reproduce under resampling (ARI = 0.57). Eight groups can always be produced; they cannot be shown to exist.

**Four evolutionary stages.** Stages defined by grouping clusters whose mean dates were computed from a variable used to build them are not a finding. Roughly half of the apparent temporal separation is circular, and the remaining half supports a two-segment, one-transition structure, not four stages with overlapping membership.

**Progressive vertical localization.** With 53.5% of hypocentral depths set to a 10 km default and apparent depth dispersion anti-correlated with the default-depth fraction at r = −0.75, statements about the seismogenic layer thinning through the sequence describe the reporting practice, not the crust.

**Postseismic redistribution at regional distance.** Beyond 75 km the rate is indistinguishable from the pre-sequence background. Later seismicity there is not shown to be causally related to the mainshock.

### 5.3 Implications for clustering studies of earthquake catalogues

Three general points follow, and they are the methodological contribution of this paper.

First, **including occurrence time among the clustering variables and then interpreting the temporal ordering of the result is circular**, and the magnitude of the circularity is measurable: here it accounts for about half of the apparent temporal separation. The remedy is inexpensive — cluster on space, then test temporal organisation independently — and it converts an assumption into a result (Section 4.7, p = 2 × 10⁻²³).

Second, **catalogue artefacts propagate into "physical" conclusions in ways that resemble physics**. A default depth assigned to unconstrained events produces exactly the signature of a thin, well-defined seismogenic layer. This is not detectable from the clustering output; it is detectable only by inspecting the catalogue. We recommend that any study using hypocentral depth as a feature report the fraction of events at the default depth.

Third, **a custom algorithm must be benchmarked against a standard one on the same data.** Here, at the cluster number the data support, the winner-take-all procedure and k-means agree at ARI = 0.993, and at K = 8 the custom procedure is the *less* stable of the two. Neither outcome supports a methodological claim.

### 5.4 The Rinjani volcanic complex

The two thrust groups lie 30–39 km from the Rinjani summit, and the mainshock area lies within the region where crustal heterogeneity associated with the volcanic complex has been imaged (Lythgoe et al., 2021; Afif et al., 2021). Our analysis contains no variable measuring temperature, attenuation, velocity structure, fluid content or fracture density, so it cannot test whether that heterogeneity controls the seismicity distribution. The defensible statement is that the seismicity distribution is spatially compatible with previously reported crustal heterogeneity near Rinjani. We make no claim of magmatic triggering or thermal control.

### 5.5 Limitations

The catalogue has no relocation and no reported location uncertainties; our resolution floor is derived from coordinate rounding alone and is therefore a lower bound on the true uncertainty. Depth is unusable, so this study is two-dimensional in space and cannot address the down-dip geometry of the thrust segments. The declustering split is only weakly bimodal at Mw ≥ 4.0 and should be regarded as an operating point. Eight focal mechanisms cannot constrain per-group faulting statistics. Finally, the near-field b-value depression, while surviving every sensitivity test we applied, has a permutation p-value of 0.039, and we do not present it as strongly established.

## 6. Conclusions

1. An eight-cluster partition of the 2018 Lombok catalogue in easting–northing–depth–time space **is not identifiable**. No internal validity index selects eight groups; the bootstrap ARI at K = 8 is 0.57; 75 of the 100 training epochs change nothing; and the partition depends on undeclared metric choices (halving the time weight gives ARI = 0.47).

2. Roughly **half of the apparent temporal separation between clusters is inserted** by including time among the clustering variables. Apparent vertical localization is a **reporting artefact**: 53.5% of depths are the 10 km default, and depth dispersion is anti-correlated with the default fraction at r = −0.75.

3. Clustering on horizontal position alone yields **three reproducible groups** (bootstrap ARI = 0.98, stable under a 0.4° boundary shift): western and eastern back-arc thrust groups with indistinguishable b-values (0.990 ± 0.032 and 1.002 ± 0.031, Utsu q = 0.36), and a southern fore-arc group with b = 1.79 ± 0.10 (q = 1.2 × 10⁻¹³).

4. With time withheld from the clustering, the groups nonetheless separate strongly in time (H = 104.2, p = 2 × 10⁻²³) and activity migrates **eastward** through the sequence (Spearman ρ = +0.40, p = 1.4 × 10⁻³⁷), the eastern segment activating 13.6 days after the western. This reproduces the segmented cascading rupture inferred from source modelling, from catalogue statistics alone.

5. The near-rupture volume has a **depressed b-value** (0.975 versus 1.277 at 25–75 km, Utsu q = 9.4 × 10⁻⁶) that survives excluding all events above Mw 5.0 (p = 0.018).

6. Aftershocks decay with **p = 0.95, c = 0.19 d**. Rates remain above background for years, but only within about 75 km; beyond that the rate increase is not significant (p = 0.32), so far-field later seismicity is **background, not postseismic redistribution**.

For hazard assessment, the operationally useful statements are that the back-arc thrust system north of Lombok behaves as a segmented structure capable of sequential multi-segment failure over weeks, that the near-rupture volume is characterised by a relatively larger proportion of large events, and that the region of measurable interaction extends to about 75 km. Finer domain structure, staged evolution and depth-resolved inferences require a relocated catalogue with reported uncertainties, which this class of catalogue is not.

## 7. Data and code availability

The two source data files (the 25,280-event regional catalogue and the Global CMT solution file) are released in `Pak_Beck/data/`. The complete analysis code is in `Pak_Beck/reanalysis/`, and every table and figure in this paper is regenerated from the raw data by a single command (`python3 reanalysis/run_all.py`). All intermediate result tables are released in `Pak_Beck/results/tables/`, including per-event cluster labels, declustering assignments and all statistical test outputs. Every stage is seeded, so results are reproducible bit-for-bit.

## Acknowledgments

We thank the Geological Agency of Indonesia for regional fault and tectonic data, the Global CMT Project for moment-tensor solutions, and the Smithsonian Institution Global Volcanism Program for volcano information. We thank the Dean of FMIPA, Universitas Gadjah Mada, and the Geophysics Laboratory, FMIPA UGM, for support. Bakti Sukrisna acknowledges support from the Rock Fluid Imaging Laboratory. Bagus Endar Bachtiar Nurhandoko acknowledges funding from the FMIPA PPMI programme at Institut Teknologi Bandung. We are grateful to the reviewer whose detailed criticism of the earlier version motivated this reanalysis.

## References

Afif, H., Nugraha, A.D., Muzli, M., et al. (2021). Local earthquake tomography of the source region of the 2018 Lombok earthquake sequence, Indonesia. *Geophysical Journal International*, 226(3), 1814–1823. https://doi.org/10.1093/gji/ggab189

AHA Centre (2018). *Situation Update No. 8: The 2018 Lombok Earthquake, Indonesia*, 1–17.

Aki, K. (1965). Maximum likelihood estimate of b in the formula log N = a − bM and its confidence limits. *Bulletin of the Earthquake Research Institute, University of Tokyo*, 43, 237–239.

Bender, B. (1983). Maximum likelihood estimation of b values for magnitude grouped data. *Bulletin of the Seismological Society of America*, 73(3), 831–851. https://doi.org/10.1785/BSSA0730030831

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate. *Journal of the Royal Statistical Society B*, 57(1), 289–300.

Bock, Y., Prawirodirdjo, L., Genrich, J.F., et al. (2003). Crustal motion in Indonesia from Global Positioning System measurements. *Journal of Geophysical Research: Solid Earth*, 108(B8). https://doi.org/10.1029/2001JB000324

Campello, R.J.G.B., Moulavi, D., & Sander, J. (2013). Density-based clustering based on hierarchical density estimates. In *Advances in Knowledge Discovery and Data Mining* (pp. 160–172). https://doi.org/10.1007/978-3-642-37456-2_14

Dziewonski, A.M., Chou, T.-A., & Woodhouse, J.H. (1981). Determination of earthquake source parameters from waveform data for studies of global and regional seismicity. *Journal of Geophysical Research*, 86(B4), 2825–2852. https://doi.org/10.1029/JB086iB04p02825

Ekström, G., Nettles, M., & Dziewonski, A.M. (2012). The Global CMT Project 2004–2010. *Physics of the Earth and Planetary Interiors*, 200–201, 1–9. https://doi.org/10.1016/j.pepi.2012.04.002

Gutenberg, B., & Richter, C.F. (1944). Frequency of earthquakes in California. *Bulletin of the Seismological Society of America*, 34(4), 185–188. https://doi.org/10.1785/BSSA0340040185

Hamilton, W.B. (1979). *Tectonics of the Indonesian Region*. U.S. Geological Survey Professional Paper 1078. https://doi.org/10.3133/pp1078

Hubert, L., & Arabie, P. (1985). Comparing partitions. *Journal of Classification*, 2(1), 193–218. https://doi.org/10.1007/BF01908075

Kagan, Y.Y. (1991). 3-D rotation of double-couple earthquake sources. *Geophysical Journal International*, 106(3), 709–716. https://doi.org/10.1111/j.1365-246X.1991.tb06343.x

Kohonen, T. (1982). Self-organized formation of topologically correct feature maps. *Biological Cybernetics*, 43(1), 59–69. https://doi.org/10.1007/BF00337288

Kohonen, T. (1995). *Self-Organizing Maps*. Springer. https://doi.org/10.1007/978-3-642-97610-0

Koulali, A., Susilo, S., McClusky, S., et al. (2016). Crustal strain partitioning and the associated earthquake hazard in the eastern Sunda-Banda Arc. *Geophysical Research Letters*, 43(5), 1943–1949. https://doi.org/10.1002/2016GL067941

Lavigne, F., Degeai, J.P., Komorowski, J.C., et al. (2013). Source of the great A.D. 1257 mystery eruption unveiled, Samalas volcano, Rinjani Volcanic Complex, Indonesia. *PNAS*, 110(42), 16742–16747. https://doi.org/10.1073/pnas.1307520110

Lythgoe, K., Muzli, M., Bradley, K., et al. (2021). Thermal squeezing of the seismogenic zone controlled rupture of the volcano-rooted Flores Thrust. *Science Advances*, 7(5). https://doi.org/10.1126/sciadv.abe2348

McCaffrey, R. (1988). Active tectonics of the Eastern Sunda and Banda Arcs. *Journal of Geophysical Research: Solid Earth*, 93(B12), 15163–15182. https://doi.org/10.1029/JB093iB12p15163

Mogi, K. (1962). Magnitude-frequency relation for elastic shocks accompanying fractures of various materials. *Bulletin of the Earthquake Research Institute, Tokyo University*, 40, 831–853.

Ogata, Y. (1988). Statistical models for earthquake occurrences and residual analysis for point processes. *Journal of the American Statistical Association*, 83(401), 9–27. https://doi.org/10.1080/01621459.1988.10478560

Rousseeuw, P.J. (1987). Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics*, 20, 53–65. https://doi.org/10.1016/0377-0427(87)90125-7

Salman, R., Lindsey, E.O., Lythgoe, K.H., et al. (2020). Cascading partial rupture of the Flores Thrust during the 2018 Lombok earthquake sequence, Indonesia. *Seismological Research Letters*, 91(4), 2141–2151. https://doi.org/10.1785/0220190378

Sasmi, A.T., Nugraha, A.D., Muzli, M., et al. (2023). Shear wave splitting of the 2018 Lombok earthquake aftershock area, Indonesia. *Geoscience Letters*, 10(1), 7. https://doi.org/10.1186/s40562-022-00258-3

Scholz, C.H. (1968). The frequency-magnitude relation of microfracturing in rock and its relation to earthquakes. *Bulletin of the Seismological Society of America*, 58(1), 399–415. https://doi.org/10.1785/BSSA0580010399

Shi, Y., & Bolt, B.A. (1982). The standard error of the magnitude-frequency b value. *Bulletin of the Seismological Society of America*, 72(5), 1677–1687. https://doi.org/10.1785/BSSA0720051677

Supendi, P., Nugraha, A.D., Widiyantoro, S., et al. (2020). Relocated aftershocks and background seismicity in eastern Indonesia shed light on the 2018 Lombok and Palu earthquake sequences. *Geophysical Journal International*, 221(3), 1845–1855. https://doi.org/10.1093/gji/ggaa118

Tibshirani, R., Walther, G., & Hastie, T. (2001). Estimating the number of clusters in a data set via the gap statistic. *Journal of the Royal Statistical Society B*, 63(2), 411–423. https://doi.org/10.1111/1467-9868.00293

Utsu, T. (1961). A statistical study on the occurrence of aftershocks. *Geophysical Magazine*, 30, 521–605.

Utsu, T. (1992). Introduction to seismicity. In *Report of the Coordinating Committee for Earthquake Prediction*, 34, 139–157.

Wiemer, S., & Wyss, M. (2000). Minimum magnitude of completeness in earthquake catalogs: examples from Alaska, the western United States, and Japan. *Bulletin of the Seismological Society of America*, 90(4), 859–869. https://doi.org/10.1785/0119990114

Wyss, M. (1973). Towards a physical understanding of the earthquake frequency distribution. *Geophysical Journal International*, 31(4), 341–359. https://doi.org/10.1111/j.1365-246X.1973.tb06506.x

Yang, X., Singh, S.C., & Tripathi, A. (2020). Did the Flores backarc thrust rupture offshore during the 2018 Lombok earthquake sequence in Indonesia? *Geophysical Journal International*, 221(2), 758–768. https://doi.org/10.1093/gji/ggaa018

Zaliapin, I., & Ben-Zion, Y. (2013). Earthquake clusters in southern California I: identification and stability. *Journal of Geophysical Research: Solid Earth*, 118(6), 2847–2864. https://doi.org/10.1002/jgrb.50179

Zhao, S., McClusky, S., Miller, M., & Cummins, P. (2024). Time-dependent seismic and volcanic source models of the 2018 Lombok earthquake sequence and the Rinjani-Samalas volcanic complex. *Geophysical Journal International*.

---

## Figure captions

**Figure 1.** Catalogue properties that constrain the analysis. (a) Annual counts of Mw ≥ 4.0 events across the whole catalogue; reporting rate rises sharply from late 2009 with network densification. (b) Reported depths in the Lombok region for the 2017–2019 window; 53% of events carry the 10 km default depth. (c) Goodness-of-fit completeness magnitude by era.

**Figure 2.** The eight-cluster partition is not identifiable. (a) Silhouette coefficient and bootstrap adjusted Rand index against cluster number for the manuscript-scale sample; neither selects K = 8. (b) The learning-rate schedule α = 0.01 × 0.5^e; cluster labels are identical after 25 and 100 epochs. (c) Bootstrap ARI at the assumed and supported cluster numbers, against the conventional 0.8 reproducibility threshold.

**Figure 3.** Temporal claims against null models. (a) Spread of cluster mean dates for three choices of clustering variables, each against the spread of random groupings of identical sizes; including time roughly doubles the apparent separation. (b) Correlation between cluster mean date and radius of gyration, against the distribution obtained from 500 catalogues with shuffled event times.

**Figure 4.** The three reproducible spatial groups, obtained by clustering on horizontal position alone with occurrence time withheld. Group b-values at the common Mc = 3.7 are shown in the legend. Open circles are the eight GCMT solutions in the study window; stars are the four Mw ≥ 6.0 events, numbered by date.

**Figure 5.** Frequency–magnitude results. (a) b-value by distance from the mainshock at a common Mc = 3.7, with Shi–Bolt 95% intervals. (b) b-value by spatial group; the two thrust groups are statistically indistinguishable while the fore-arc group differs. (c) The near-field/intermediate contrast under progressive removal of the largest events.

**Figure 6.** Triggering. (a) Distribution of nearest-neighbour distances with the variance-minimising background/triggered threshold. (b) Aftershock rate after the 5 August mainshock with the maximum-likelihood Omori–Utsu fit. (c) Rate increase over the pre-sequence background by distance band; the 75–100 km band is not significant.

**Figure 7.** Longitude of sequence events against time, coloured by the spatial group each event belongs to. Because groups were defined without using time, the temporal separation is an independent result.
