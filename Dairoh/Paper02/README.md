# Meta-Review and Final Decision

**Paper Title:** Array-Based Dataset Construction for Machine Learning Classification of Long-Distance Volcanic Seismic Signals  
**Authors:** Dairoh, Sudarmaji, Ahmad Ashari, Wiwit Suryanto  
**Manuscript Status:** PhD Student Draft (Dairoh, first/doctoral author)

---

## Summary of Reviewer Reports

### Areas of Agreement Across All Three Reviewers

All three reviewers identify the following shared strengths and concerns:

**Shared Strengths:**
- The research problem is genuinely motivated and practically relevant: constructing reliable labeled datasets from remote, low-cost seismic arrays addresses a real gap in volcanic monitoring infrastructure.
- The dual-catalogue validation (BMKG + BPPTKG) is a methodologically sound approach to label verification.
- The paper is transparent and honest in reporting results, including less favorable outcomes (e.g., the poor 90:10 split performance).
- The broader societal context (Merapi Volcano, Indonesia, hazard mitigation) is important and well-motivated.

**Shared Concerns:**
1. **Unrendered equations (Tables 3–6)**: All three reviewers note that mathematical formulas appear as empty placeholder numbers, which is a critical formatting failure.
2. **Chronological vs. stratified split inconsistency**: All reviewers flag the contradiction between the "chronological train–test strategy" claimed in the abstract/conclusion and the "stratified random sampling" described in the Methods section.
3. **Missing key literature references**: All reviewers independently identify that the paper fails to cite and discuss seminal works including Malfante et al. (2018), Titos et al. (2019), Ohrnberger (2001), Smith & Bean (2020), and Espinosa-Curilem et al. (2024).
4. **Overlap with prior publication [26]**: All reviewers note that the boundary between the current paper and Dairoh et al. (2026) [26] is insufficiently delineated, raising concerns about redundant publication.
5. **Small dataset (275 events, 28 days)**: All reviewers consider the dataset too small for robust ML evaluation and generalization.
6. **Absence of deep learning baselines**: All reviewers agree that the omission of CNN, LSTM, or Random Forest comparisons makes the experimental evaluation incomplete.

---

### Reviewer-Specific Concerns (Not Shared by All)

**Reviewer 1 (Methods & Theory)** raises additional technical concerns (lebih detail [disini](./reviewer_1_report.md)):
- FK analysis parameters (slowness grid, coherence threshold, back-azimuth tolerance) are not disclosed, preventing reproducibility.
- The beamforming algorithm is not specified (delay-and-sum, Capon, MUSIC?).
- STA/LTA trigger threshold and other parameters are not reported.
- Severe multicollinearity among amplitude features (r = 0.98–1.00) is not addressed before model training.
- No statistical significance testing is applied to performance comparisons.
- The 0.8–1.8 Hz bandpass filter is very narrow and may suppress discriminative information for some event classes.

**Reviewer 2 (Experiments & Practical Impact)** raises additional experimental concerns (lebih detail [disini](./reviewer_2_report.md)):
- No data augmentation is attempted despite the small, imbalanced dataset.
- AUC values are listed as evaluation metrics but never reported quantitatively.
- No comparison with near-field BPPTKG station performance is provided.
- No feature importance analysis (SHAP, permutation importance) is conducted.
- The 90:10 split performance degradation is not adequately explained or investigated.
- The labeled dataset and code are not deposited in a public repository.

**Reviewer 3 (Clarity & Positioning)** raises additional presentation concerns (lebih detail [disini](./reviewer_3_report.md)):
- Multiple typographical errors (e.g., "Univeritas," "Sciemces," "Leaming," "occorred," "Skweness," truncated "cod").
- The abstract is too long and repetitive.
- The title does not fully reflect the paper's scope.
- Broader impact (scalability, operational deployment, misclassification consequences) is not discussed.
- Table 1 has empty definition cells and an unclear feature name ("i from the energy center").
- Reference list has quality issues (typos, inconsistent agency abbreviations, incomplete entries).

---

## Conflicting Opinions and Resolution

**On overall rating:**
- Reviewer 1 rates the paper 4/10 (Reject, major revision required), emphasizing methodological incompleteness.
- Reviewer 2 rates the paper 4/10 (Reject, major revision required), emphasizing experimental inadequacy.
- Reviewer 3 rates the paper 5/10 (Borderline Reject/Major Revision), acknowledging the genuine practical contribution while flagging presentation and positioning issues.

**Resolution:** The slight divergence between Reviewers 1–2 and Reviewer 3 reflects the difference between technical rigor (which is clearly insufficient) and practical contribution (which is real but modest). The meta-reviewer agrees with Reviewers 1 and 2 that the technical and experimental deficiencies are too significant for borderline acceptance. The paper requires major revision before it can be considered further.

**On novelty:** 
- All three reviewers agree the paper makes an incremental but useful contribution. No reviewer considers the work transformative or highly novel. The primary novelty is the end-to-end integration of array processing with ML dataset construction for a remote low-cost array—a combination that is underrepresented in the literature but not unprecedented. Lebih lengkap untuk kebaruan [disini](./novelty_report.md)

---

## Final Decision: **Major Revision Required (Reject for Resubmission)**

The paper presents a practically motivated and honest scientific contribution, but it is **not ready for publication** in its current form. The following issues are critical and must be addressed in a major revision:

### Critical Issues (Must Be Resolved)

1. **Render all equations properly**: Tables 3–6 must contain properly typeset mathematical formulas. The SVM, XGBoost, and evaluation metric equations must be visible and verifiable.

2. **Resolve the train–test split inconsistency**: Clarify whether chronological or stratified random splitting was used, correct all instances throughout the manuscript, and justify the choice.

3. **Disclose all FK analysis and beamforming parameters**: Provide a comprehensive parameter table (slowness range, grid resolution, coherence threshold, back-azimuth tolerance, beamforming algorithm) to enable reproducibility.

4. **Add deep learning and Random Forest baselines**: Include at least CNN and/or LSTM classifiers for comparison. This is essential for contextualizing the SVM/XGBoost results.

5. **Clearly differentiate from prior publication [26]**: Add a dedicated paragraph in the introduction explicitly stating what [26] accomplished and what the current paper adds beyond it. Ensure there is no redundant publication.

6. **Add missing key references**: Cite and discuss Malfante et al. (2018), Titos et al. (2019), Ohrnberger (2001), Smith & Bean (2020), Espinosa-Curilem et al. (2024), and Langer et al. (2009).

7. **Report AUC values explicitly**: Add a table of per-class AUC values for all split scenarios.

8. **Fix all typographical errors**: Conduct a comprehensive proofreading pass addressing all errors identified by Reviewer 3.

### Important Issues (Strongly Recommended)

9. **Apply feature selection or address multicollinearity**: Given r = 0.98–1.00 among amplitude features, apply PCA, recursive feature elimination, or feature selection before model training.

10. **Add data augmentation**: Apply SMOTE, time-shifting, or noise injection to address the small dataset size and class imbalance.

11. **Add statistical significance testing**: Report confidence intervals on accuracy estimates and use McNemar's test for pairwise model comparisons.

12. **Add feature importance analysis**: Use SHAP values or permutation importance to identify the most discriminative features.

13. **Deposit dataset and code**: Make the labeled dataset and processing scripts publicly available (e.g., Zenodo, GitHub) to support reproducibility.

14. **Add a broader impact discussion**: Discuss scalability, operational deployment requirements, and the consequences of misclassification for volcanic hazard assessment.

15. **Justify the bandpass filter**: Provide spectral analysis of raw data to support the 0.8–1.8 Hz passband choice.

---

## Guidance for the PhD Student (Dairoh)

This manuscript reflects genuine scientific effort and addresses a meaningful research problem. The core idea—using array processing to systematically construct validated ML datasets from remote low-cost arrays—is a valuable contribution to the volcanic monitoring community. The following guidance is offered for the revision:

1. **The most urgent fix is the equation rendering**: The manuscript cannot be reviewed or published with empty equation tables. This must be resolved immediately.

2. **The split inconsistency is a fundamental issue**: If stratified random sampling was used (as stated in Methods), then the claims about "chronological strategy" in the abstract and conclusion must be corrected. If chronological splitting was used, the Methods section must be corrected. This is not a minor writing issue—it affects the validity of the experimental design.

3. **Adding deep learning baselines is essential for publication in a top-tier journal**: Even a simple 1D CNN trained on raw waveform windows would significantly strengthen the paper. The 72.73% XGBoost accuracy needs context.

4. **The dataset is the paper's most important contribution**: Focus the narrative on the dataset construction framework and its validation. The classification results are secondary and should be presented as a proof-of-concept evaluation rather than a definitive performance benchmark.

5. **Extend the observation period if possible**: Even adding 2–3 more months of data would substantially increase the dataset size and strengthen the paper's conclusions.

6. **The paper has a strong practical story**: The remote low-cost array, the dual-catalogue validation, and the systematic pipeline are all compelling. Make sure these strengths are highlighted clearly in the abstract and introduction.

With thorough revision addressing the critical issues above, this paper has the potential to make a meaningful contribution to the volcanic seismic monitoring literature and would be appropriate for journals such as *Seismological Research Letters*, *Journal of Volcanology and Geothermal Research*, *Frontiers in Earth Science*, or *IEEE Transactions on Geoscience and Remote Sensing*.

---

## Summary Scorecard

| Criterion | Reviewer 1 | Reviewer 2 | Reviewer 3 | Consensus |
|-----------|-----------|-----------|-----------|-----------|
| Soundness | 2.5/5 | 2.5/5 | 3.0/5 | 2.7/5 |
| Presentation | 3.0/5 | 3.0/5 | 2.5/5 | 2.8/5 |
| Contribution | 2.5/5 | 2.5/5 | 3.0/5 | 2.7/5 |
| Overall Rating | 4/10 | 4/10 | 5/10 | 4.3/10 |
| Decision | Major Revision | Major Revision | Major Revision | **Major Revision** |
