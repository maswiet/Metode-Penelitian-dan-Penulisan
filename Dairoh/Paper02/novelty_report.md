# Novelty and Impact Report

**Paper:** Array-Based Dataset Construction for Machine Learning Classification of Long-Distance Volcanic Seismic Signals  
**Authors:** Dairoh, Sudarmaji, Ahmad Ashari, Wiwit Suryanto  
**Affiliation:** Universitas Gadjah Mada, Indonesia

---

## 1. Overview of the Claimed Contributions

The paper proposes three main contributions:
1. A reproducible array-based pipeline (STA/LTA → beamforming → FK analysis → catalogue validation) for constructing validated labeled datasets from continuous remote-array recordings.
2. A validated labeled dataset of 275 seismic events in four classes (VTB, Rockfall, Multiphase, Non Event) at ~16 km from Merapi Volcano.
3. An experimental evaluation of SVM and XGBoost classifiers using temporal and spectral features with a chronological train–test strategy.

---

## 2. Novelty Assessment

### 2.1 Array-Based Dataset Construction Framework

**Degree of novelty: Moderate–Low**

The individual components of the proposed framework—STA/LTA detection, beamforming, and FK analysis—are well-established tools in seismological array processing (Capon, 1969; Rost & Thomas, 2002). Their application to volcanic seismic monitoring has been documented extensively (e.g., Saccorotti & Del Pezzo, 2000; Leva et al., 2021). Real-time array processing tools such as RETREAT (Smith & Bean, 2020) already integrate FK analysis and beamforming for continuous volcanic tremor monitoring.

What is relatively novel is the **systematic integration of these array-processing outputs as a preprocessing and labeling filter** specifically designed to construct validated ML-ready datasets from remote low-cost arrays. Most existing ML studies (e.g., Malfante et al., 2018; Titos et al., 2019; Espinosa-Curilem et al., 2024) assume pre-labeled datasets are available and do not explicitly describe how array-derived parameters (backazimuth, slowness) were used during the labeling process. The UGM antenna station's previous publication (Dairoh et al., 2026, [26]) describes the same array and detection methodology, which reduces the novelty of the dataset construction component in the current manuscript.

**Key concern:** The manuscript's own prior work [26] already applied STA/LTA + beamforming + FK analysis to the same dataset and array. The current paper extends this by adding catalogue validation and ML classification, but the differentiation from [26] should be more clearly articulated.

### 2.2 Remote Low-Cost Array Deployment

**Degree of novelty: Moderate**

The use of Raspberry Shake sensors in a pentagonal array configuration at ~16 km from Merapi is a relatively distinctive setting. Most published ML studies for Merapi use BPPTKG near-field stations (~3 km from the summit), as noted by Ohrnberger (2001) and more recent Merapi-specific ML studies cited in [19–21]. The demonstration that reliable labeled datasets can be constructed from a remote, low-cost array is a meaningful practical contribution, though it is incremental rather than transformative. Similar low-cost or remote deployments exist in the literature but are rarely coupled with systematic ML dataset construction pipelines.

### 2.3 Machine Learning Classification (SVM and XGBoost)

**Degree of novelty: Low**

SVM and XGBoost are well-established algorithms with extensive application in volcanic seismic classification. Malfante et al. (2018) demonstrated SVM achieving ~93.5% accuracy on 109,609 events at Ubinas; Langer et al. (2009) reported SVM at 94.8% on Mt. Etna tremor data; Lara-Cueva et al. (2016) demonstrated SVM at ~97% for LP/VT discrimination at Cotopaxi. XGBoost has also been applied to volcanic earthquake pattern classification (Achmad et al., 2023). The choice of only SVM and XGBoost, without comparison to CNN, LSTM, or Random Forest, represents a significant gap in methodological coverage relative to state-of-the-art approaches (Titos et al., 2019; Espinosa-Curilem et al., 2024; Tan et al., 2024).

The use of 11 temporal and spectral features is conventional and does not introduce new feature engineering. The feature set (mean, std, skewness, kurtosis, RMS, dominant frequency, spectral centroid, spectral entropy, etc.) has been widely used in prior work (e.g., Curilem et al., 2014; Wang et al., 2022 [33]).

### 2.4 Chronological Train–Test Strategy

**Degree of novelty: Low–Moderate**

The use of a chronological (temporal) train–test split to reduce data leakage is a methodologically sound choice that is underused in the volcanic seismic ML literature. Most studies use random stratified splits, which can overestimate performance due to temporal autocorrelation. The paper's acknowledgment of this issue is commendable, though a more rigorous treatment (e.g., time-series cross-validation) would strengthen the contribution.

---

## 3. Comparison with Existing State-of-the-Art

| Aspect | This Study | State of the Art |
|--------|-----------|-----------------|
| Dataset size | 275 events | 425–109,609 events in comparable studies |
| Number of classes | 4 | 4–6 in comparable studies |
| Best accuracy | 72.73% (XGBoost, 80:20) | 90–97% (CNN, LSTM, SVM on larger datasets) |
| Classifiers | SVM, XGBoost | SVM, RF, CNN, LSTM, GRU, UNet, transfer learning |
| Feature type | 11 temporal/spectral | Similar + waveform images, spectrograms, multi-station tensors |
| Array processing role | Preprocessing/labeling | Rarely integrated; mostly post-hoc |
| Dataset source | Remote array, 16 km | Mostly near-field (~1–5 km) |
| Observation period | 28 days | Months to years in larger studies |

The 72.73% XGBoost accuracy is modest compared to the literature. However, this is partially attributable to the small dataset size (275 events), the challenging long-distance recording conditions, and the absence of data augmentation. An HMM-based system applied to a short Merapi campaign (Ohrnberger, 2001) achieved ~67% overall accuracy, suggesting that the 72.73% result is reasonable for a small, challenging dataset but remains far below what is achievable with larger, better-balanced datasets and more powerful classifiers.

---

## 4. Impact and Significance

### Positive Contributions
- **Practical significance**: The framework addresses a real operational challenge—constructing reliable labeled datasets from remote, low-cost seismic arrays—which is relevant for volcano monitoring in resource-limited settings.
- **Reproducibility**: The step-by-step integration of STA/LTA, beamforming, FK analysis, and catalogue validation provides a transparent, reproducible pipeline that could be adapted by other monitoring agencies.
- **Safety relevance**: Demonstrating that ML classification is feasible from 16 km (vs. 3 km) has direct implications for station safety during eruptions.
- **Regional significance**: Merapi is one of the most active and dangerous volcanoes in Indonesia; contributions to its monitoring infrastructure are of high societal relevance.

### Limitations on Impact
- **Modest classification performance**: The 72.73% accuracy is unlikely to be sufficient for operational deployment in a real monitoring system.
- **Short observation window**: 28 days is insufficient to capture seasonal variability, different volcanic activity phases, or rare event types.
- **No deep learning comparison**: The absence of CNN/LSTM baselines makes it impossible to assess whether the framework is competitive with modern approaches.
- **Small dataset**: 275 events limits generalizability and statistical robustness of conclusions.
- **Overlap with prior publication [26]**: The novelty boundary between this manuscript and [26] is not sufficiently delineated.

---

## 5. Missing Related Work

The manuscript is missing several important references that should be cited and discussed:

1. **Malfante et al. (2018)** – "Automatic Classification of Volcano Seismic Signatures," JGR Solid Earth – the most directly comparable large-scale SVM/ML volcanic classification study.
2. **Titos et al. (2019)** – "Detection and Classification of Continuous Volcano-Seismic Signals with Recurrent Neural Networks," IEEE TGRS – key deep learning baseline.
3. **Espinosa-Curilem et al. (2024)** – "A Framework for Real-Time Volcano-Seismic Event Recognition Based on Multi-Station Seismograms and Semantic Segmentation Models" – most recent multi-station framework.
4. **Smith & Bean (2020)** – "RETREAT: A REal-Time TREmor Analysis Tool for Seismic Arrays" – directly comparable array processing tool.
5. **Langer et al. (2009)** – "Synopsis of supervised and unsupervised pattern classification techniques applied to volcanic tremor data at Mt Etna" – classic SVM benchmark.
6. **Ohrnberger (2001)** – "Continuous automatic classification of seismic signals of volcanic origin at Mt. Merapi" – directly relevant Merapi baseline.
7. **Lara-Cueva et al. (2016)** – "Automatic Recognition of Long Period Events from Volcano Tectonic Earthquakes at Cotopaxi Volcano" – SVM LP/VT discrimination benchmark.
8. **Saccorotti & Del Pezzo (2000)** – "A probabilistic approach to the inversion of data from a seismic array" – foundational FK analysis reference.

---

## 6. Overall Novelty and Significance Rating

| Dimension | Score (1–5) | Justification |
|-----------|-------------|---------------|
| Methodological novelty | 2.5/5 | Integration of known methods; novel in combination for remote array labeling |
| Empirical contribution | 2.5/5 | Small dataset, modest accuracy; valuable proof-of-concept |
| Practical significance | 3.5/5 | Addresses real operational need; safety-relevant |
| Literature positioning | 2.0/5 | Missing key references; insufficient comparison with DL methods |
| Overall novelty | 2.5/5 | Incremental advance; requires strengthening before publication |

**Summary:** The paper makes a useful, incremental contribution to the field of volcanic seismic monitoring by demonstrating that array-based dataset construction from a remote low-cost array is feasible. However, the novelty of individual components is limited, the classification performance is modest, the dataset is small, and the comparison with state-of-the-art methods is incomplete. The manuscript requires substantial revision—particularly in expanding the ML comparison, increasing dataset size or observation period, and more clearly differentiating from the authors' own prior work [26].
