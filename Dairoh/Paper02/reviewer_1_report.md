# Reviewer 1 Report — Methods & Theory Specialist

**Paper Title:** Array-Based Dataset Construction for Machine Learning Classification of Long-Distance Volcanic Seismic Signals  
**Authors:** Dairoh, Sudarmaji, Ahmad Ashari, Wiwit Suryanto  
**Reviewer Expertise:** Seismic array processing, signal processing, machine learning theory, geophysical data analysis

---

## Summary

This manuscript proposes an array-based framework for constructing validated labeled datasets from continuous seismic recordings of the UGM remote array (~16 km from Merapi Volcano, Indonesia). The framework integrates STA/LTA event detection, beamforming, Frequency–Wavenumber (FK) analysis, and independent catalogue validation (BMKG + BPPTKG) to produce a 275-event labeled dataset across four classes (VTB, Rockfall, Multiphase, Non Event). Temporal and spectral features (11 total) are extracted and used to train SVM and XGBoost classifiers under four train–test split scenarios (60:40 to 90:10). The best result—72.73% accuracy—is achieved by XGBoost at the 80:20 split. The paper positions itself as addressing the gap in constructing reliable labeled datasets from remote low-cost arrays, as opposed to near-field summit stations.

---

## Soundness: 2.5 / 5

The individual methods are technically sound but several critical methodological details are missing or inadequately described, and the theoretical underpinning of the classification framework is insufficiently rigorous for a top-tier journal.

---

## Presentation: 3.0 / 5

The paper is generally readable and well-structured. However, mathematical formulations are incomplete, key parameters are insufficiently justified, and several equations appear as placeholder boxes (Tables 3–6) without proper rendering, suggesting unresolved typesetting issues.

---

## Contribution: 2.5 / 5

The integration of array-based preprocessing with ML dataset construction for remote volcanic monitoring is a useful contribution. However, the classification component is methodologically weak (only SVM and XGBoost, no deep learning), the dataset is small, and the novelty relative to the authors' own prior publication [26] is insufficiently differentiated.

---

## Strengths

1. **Clear pipeline design**: The proposed workflow (STA/LTA → beamforming → FK → catalogue validation → feature extraction → ML) is logically structured and reproducible. The separation of event identification from classification is a sound methodological choice.

2. **Dual catalogue validation**: Cross-referencing with both the BMKG earthquake catalogue and BPPTKG volcanic-event catalogue for event label verification is a rigorous approach that enhances label reliability and reduces the risk of mislabeling.

3. **Chronological train–test split**: The use of a chronological (temporal) train–test partitioning strategy to reduce temporal data leakage is methodologically sound and underused in the volcanic seismic ML literature. This is a commendable methodological choice.

4. **Array geometry justification**: The pentagonal array geometry is appropriately motivated by its FK analysis performance, and the ~250 m inter-station spacing is relevant to the target frequency band (0.8–1.8 Hz).

5. **Multiple split scenarios**: Evaluating four train–test split ratios (60:40, 70:30, 80:20, 90:10) provides useful insight into the sensitivity of model performance to training data volume.

6. **Hyperparameter optimization**: The use of GridSearchCV with stratified 5-fold cross-validation for hyperparameter tuning is appropriate.

---

## Weaknesses

### W1: Mathematical Formulations Are Incomplete and Improperly Rendered
Tables 3–6 appear to contain equation placeholders (e.g., "(1)", "(2)", "(3)–(6)", "(7)–(8)") without the actual mathematical content being visible in the manuscript. The SVM decision function (Equation 1) and XGBoost objective function (Equation 2) are referenced in text but their mathematical content cannot be verified. The performance metrics (precision, recall, F1, ROC, AUC) are referenced but their formulas appear in placeholder tables. This is a critical formatting/completeness issue that must be resolved.

### W2: FK Analysis Parameters Are Undisclosed
The FK analysis is a central component of the framework, yet critical parameters are not reported:
- Frequency band used for FK analysis (different from the 0.8–1.8 Hz bandpass filter?)
- Slowness grid resolution and search range
- Time window length for FK analysis
- Coherence threshold for accepting a dominant beam direction
- Specific back-azimuth tolerance used to distinguish Merapi-direction signals from non-volcanic events

Without these parameters, the framework cannot be reproduced by other researchers.

### W3: Beamforming Algorithm Not Specified
The manuscript states beamforming was applied but does not specify the beamforming method used (e.g., conventional delay-and-sum, Capon/minimum variance, MUSIC). This is a fundamental methodological omission.

### W4: STA/LTA Parameters Partially Disclosed
Only the STA (10 s) and LTA (120 s) window lengths are given. The trigger threshold (on/off ratio), minimum event duration, and minimum inter-event interval are not reported. These parameters critically affect the 442 candidate events detected and must be disclosed.

### W5: Bandpass Filter Choice Lacks Justification
The 0.8–1.8 Hz bandpass filter is stated to "preserve the dominant frequency content of volcanic seismic signals" but:
- No spectral analysis of the raw data is shown to justify this range
- The dominant frequency of Rockfall events is typically 1–10 Hz; VTB events are typically 1–5 Hz; Multiphase events span 1–10 Hz. A 0.8–1.8 Hz passband is very narrow and may suppress important discriminative information for these classes.
- No sensitivity analysis of the filter choice is provided.

### W6: Stratified vs. Chronological Split Inconsistency
The manuscript states in the abstract and conclusion that a "chronological train–test strategy" was used, but Section "Train/Test Split" describes "stratified random sampling." These are contradictory. Stratified random sampling does not preserve temporal order; a truly chronological split would assign the first N% of events (by timestamp) to training and the remaining to testing. The authors must clarify which approach was actually used and correct the inconsistency throughout.

### W7: Feature Correlation and Redundancy Not Addressed in Model Design
The Pearson correlation matrix (Figure 9a) reveals extremely high correlations (r = 0.98–1.00) among amplitude-based features (peak amplitude, mean amplitude, std, RMS, signal energy). Despite this, all 11 features are used directly as inputs without dimensionality reduction or feature selection. This introduces severe multicollinearity that can destabilize SVM's hyperplane estimation. The scree plot (Figure 9b) shows ~90% variance explained by 5 PCs, suggesting PCA-based dimensionality reduction would be appropriate but is not applied.

### W8: No Statistical Significance Testing
All performance comparisons (SVM vs. XGBoost, different split ratios) are based on single train–test splits without confidence intervals, bootstrap estimates, or statistical significance tests (e.g., McNemar's test). With 31–110 test samples, individual accuracy estimates have wide confidence intervals. For example, at the 90:10 split (31 test samples), a 1-event misclassification changes accuracy by ~3.2%.

### W9: Catalogue Validation Criteria Are Opaque
The paper states that 167 of 442 candidate events were discarded as "false or ambiguous," but the specific criteria for rejection are not quantified:
- What back-azimuth tolerance was used to accept/reject a Merapi-direction event?
- What time window was used to match STA/LTA detections to catalogue entries?
- How were "ambiguous" events defined and handled?
- What fraction of discarded events were false detections vs. real events not in the catalogue?

### W10: No Comparison with Deep Learning Methods
The manuscript does not compare SVM and XGBoost with CNN, LSTM, or Random Forest classifiers. Given the current state of the art—where LSTM achieves ~94% (Titos et al., 2019), CNN achieves 81–90% (Tan et al., 2024), and SVM achieves ~93.5% on larger datasets (Malfante et al., 2018)—the absence of deep learning baselines makes it impossible to assess whether the proposed dataset and features are competitive.

### W11: Overlap with Prior Publication [26] Not Adequately Addressed
Reference [26] (Dairoh et al., 2026) describes the same UGM antenna array, the same STA/LTA detection of 442 candidate events, and the same beamforming/FK analysis on the same data. The current manuscript must clearly articulate what is new beyond [26] and ensure the two papers do not constitute redundant publication.

---

## Suggestions

1. **Resolve all mathematical equations**: Ensure all formulas (SVM, XGBoost, evaluation metrics) are properly typeset and visible in the manuscript.
2. **Report all FK/beamforming parameters**: Provide a comprehensive parameter table for reproducibility.
3. **Clarify the train–test split strategy**: Resolve the inconsistency between "chronological" and "stratified random" splits throughout the manuscript.
4. **Apply feature selection or PCA**: Given the high multicollinearity among amplitude features, apply PCA or recursive feature elimination before model training.
5. **Add statistical significance testing**: Report confidence intervals on accuracy estimates and use McNemar's test for pairwise comparisons.
6. **Add deep learning baselines**: Include at least a 1D CNN and/or LSTM baseline trained on the same feature set or raw waveforms to contextualize the SVM/XGBoost results.
7. **Clarify the novelty boundary with [26]**: Add a dedicated paragraph explicitly distinguishing the current work from the prior publication.
8. **Justify the bandpass filter**: Provide spectral analysis of raw data to justify the 0.8–1.8 Hz passband choice.
9. **Quantify catalogue validation criteria**: Provide explicit thresholds for back-azimuth tolerance, time-matching windows, and rejection criteria.

---

## Questions

1. In the STA/LTA detection, what trigger threshold (on/off ratio) was used, and how was it selected? Was it optimized against the catalogue, or set empirically?
2. What specific back-azimuth tolerance was applied to distinguish Merapi-direction events from non-volcanic signals in the FK analysis stage?
3. Were the 167 discarded candidate events predominantly false detections (noise triggers), events with ambiguous back-azimuth, or real events absent from both catalogues? Can the authors provide a breakdown?
4. How was the STA/LTA window of 10 s (STA) and 120 s (LTA) selected? These are unusual values—most volcanic STA/LTA implementations use 0.5–5 s STA and 10–60 s LTA. Were alternative window lengths tested?
5. Was the same 0.8–1.8 Hz bandpass applied during FK analysis, or was a different frequency band used? If the same, how does this narrow band affect the FK resolution for the target events?
6. The paper states that Multiphase and Non Event are most frequently confused. Were the FK analysis results (back-azimuth, slowness) examined to understand whether these two classes have overlapping propagation characteristics?

---

## Rating: 4 / 10 — Reject (Major Revision Required)

**Key reasons:** (1) Critical methodological parameters (FK analysis settings, beamforming algorithm, catalogue validation criteria) are undisclosed, preventing reproducibility. (2) A fundamental inconsistency between "chronological" and "stratified random" train–test splitting undermines the methodological claims. (3) The absence of deep learning baselines and statistical significance testing makes the experimental evaluation incomplete. (4) Severe multicollinearity in the feature set is not addressed. These issues require substantial revision before the paper can be considered for publication.

---

## Confidence: High

I am highly confident in this assessment given my expertise in seismic array processing and machine learning methodology. The technical concerns identified are unambiguous and verifiable from the manuscript text.
