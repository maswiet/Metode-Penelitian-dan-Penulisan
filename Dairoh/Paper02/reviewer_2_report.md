# Reviewer 2 Report — Experiments & Practical Impact Specialist

**Paper Title:** Array-Based Dataset Construction for Machine Learning Classification of Long-Distance Volcanic Seismic Signals  
**Authors:** Dairoh, Sudarmaji, Ahmad Ashari, Wiwit Suryanto  
**Reviewer Expertise:** Experimental design, seismic monitoring systems, ML benchmarking, geophysical data analysis, volcanic hazard applications

---

## Summary

This paper introduces an array-based dataset construction workflow for volcanic seismic classification at Merapi Volcano, using a remote five-element array (Raspberry Shake sensors) located ~16 km from the summit. The workflow chains STA/LTA event detection, beamforming, FK analysis, and dual-catalogue validation (BMKG + BPPTKG) to produce a 275-event labeled dataset. Eleven temporal and spectral features are extracted and used to train SVM and XGBoost classifiers. The best performance—72.73% accuracy with XGBoost—is achieved at the 80:20 train–test split. The paper claims to demonstrate that reliable labeled datasets can be constructed from remote low-cost arrays, extending ML-based volcanic monitoring beyond near-field networks.

---

## Soundness: 2.5 / 5

The experimental setup has notable weaknesses: the dataset is very small (275 events over 28 days), only two classifiers are evaluated, no data augmentation is attempted, and the performance metrics are reported without statistical uncertainty quantification. Several experimental claims are not fully supported by the evidence presented.

---

## Presentation: 3.0 / 5

The paper is generally well-organized with a clear workflow. However, the equations in Tables 3–6 appear as empty placeholders, several figures are referenced but their content is described only in captions (figures are not reproduced in the text review), and some inconsistencies in terminology (e.g., "stratified" vs. "chronological" splitting) reduce clarity.

---

## Contribution: 2.5 / 5

The proof-of-concept demonstration of remote array-based dataset construction is practically relevant. However, the experimental scope is too narrow—only two classifiers, 28 days of data, and a single volcano—to support the broad claims made in the conclusions about "extending machine-learning-based volcanic seismic monitoring beyond conventional near-field monitoring networks."

---

## Strengths

1. **Practically motivated research question**: Constructing reliable labeled datasets from remote, low-cost arrays addresses a genuine operational challenge in volcanic monitoring, particularly for resource-limited agencies in developing countries. The Merapi context is highly relevant given its status as one of Indonesia's most hazardous volcanoes.

2. **Dual-catalogue cross-validation**: The use of both BMKG (regional earthquakes) and BPPTKG (volcanic events) catalogues as independent reference datasets for label verification is methodologically robust and adds credibility to the labeled dataset.

3. **Multiple train–test split scenarios**: Evaluating four split ratios (60:40, 70:30, 80:20, 90:10) provides insight into the sensitivity of both classifiers to training data volume and is more informative than a single fixed split.

4. **Comprehensive evaluation metrics**: The use of confusion matrices, precision, recall, F1-score, ROC curves, AUC, and learning curves provides a multi-faceted view of model performance beyond simple accuracy.

5. **Learning curve analysis**: Including learning curves to assess overfitting/underfitting tendencies is a valuable addition that strengthens the experimental evaluation.

6. **Low-cost hardware documentation**: The explicit documentation of the Raspberry Shake and Boom sensor array provides useful practical information for other research groups seeking to deploy similar systems.

7. **Transparency about dataset limitations**: The authors acknowledge that 167 of 442 candidate events were discarded and provide a breakdown of the final dataset by class, which is commendable.

---

## Weaknesses

### W1: Dataset Is Too Small for Robust ML Evaluation
The final dataset of 275 events (71 Multiphase, 84 Rockfall, 71 VTB, 49 Non Event) is very small relative to comparable studies in the literature. Malfante et al. (2018) used 109,609 events; Titos et al. (2019) used thousands of events; even modest studies use 1,000–5,000 events. With 275 events and four classes, the average of ~69 events per class is insufficient to train robust classifiers or draw statistically meaningful conclusions about class-level performance. The 90:10 split yields only 31 test samples, making per-class metrics highly unstable.

### W2: No Data Augmentation or Resampling Strategy
Given the small dataset, no data augmentation (e.g., time-shifting, amplitude scaling, noise injection, SMOTE) or class-resampling strategy is applied. Class imbalance (Non Event: 49 vs. Rockfall: 84) is acknowledged but not addressed beyond stratified splitting. The literature demonstrates that augmentation can substantially improve performance on small imbalanced volcanic seismic datasets (Manley et al., 2022; Espinosa-Curilem et al., 2024).

### W3: Only Two Classifiers Evaluated — No Deep Learning Baseline
The experimental comparison is limited to SVM and XGBoost. The absence of Random Forest, CNN, LSTM, or any deep learning baseline is a major gap. State-of-the-art results for volcanic seismic classification report 90–97% accuracy with CNN and LSTM on comparable or smaller datasets (Titos et al., 2019; Tan et al., 2024). Without these baselines, it is impossible to assess whether the 72.73% XGBoost result is competitive or whether the proposed dataset and features support better performance with more powerful models. This omission significantly limits the practical impact of the experimental section.

### W4: No Cross-Validation on Full Dataset
Model performance is assessed using a single train–test split (no repeated cross-validation on the full dataset). Given the small sample size, k-fold cross-validation (e.g., 5- or 10-fold stratified) on the full 275-event dataset would provide more stable and reliable performance estimates. The current approach produces highly variable results (e.g., SVM accuracy drops from 63.64% at 80:20 to 46.43% at 90:10), suggesting high variance due to small test set sizes rather than genuine model degradation.

### W5: Observation Period Is Too Short (28 Days)
The 28-day observation window (16 August – 12 September 2023) is insufficient to:
- Capture seasonal variability in background noise
- Represent different phases of volcanic activity (quiescent, unrest, eruption)
- Include rare event types (e.g., Volcano-Tectonic A, long-period, tremor)
- Assess model generalizability across time

The paper acknowledges this limitation in the conclusion but does not discuss its implications for the reliability of the trained models.

### W6: Performance Degradation at 90:10 Split Is Not Adequately Explained
SVM accuracy drops sharply from 63.64% (80:20) to 46.43% (90:10), while XGBoost drops from 72.73% to 67.86%. The paper attributes this to small test set size but does not investigate whether this reflects genuine overfitting (which would be visible in the learning curves) or statistical instability due to the small test set. A more rigorous analysis is needed.

### W7: No Ablation Study on Feature Importance
The paper extracts 11 features but does not perform a systematic feature importance analysis (e.g., SHAP values, permutation importance) to identify which features are most discriminative for each class. Given the high multicollinearity among amplitude features (r = 0.98–1.00 per Figure 9a), understanding which features drive classification is important for both interpretability and model improvement.

### W8: No Comparison with Near-Field Station Performance
The paper's central claim is that remote array recordings can support ML classification. However, no comparison is made with classification performance on near-field BPPTKG station recordings for the same events. Without this baseline, it is impossible to quantify the performance degradation attributable to the longer propagation distance and lower SNR of the remote array.

### W9: Confusion Matrix Interpretation Is Incomplete
The paper notes that Multiphase and Non Event are most frequently confused but does not analyze why. Given that the FK analysis already discriminates Merapi-direction events from regional earthquakes, the confusion between Non Event (regional tectonic) and Multiphase (volcanic) at the classification stage suggests that the temporal/spectral features alone are insufficient. The authors should discuss whether incorporating array-derived features (back-azimuth, slowness, beam power) as additional ML inputs would resolve this confusion.

### W10: ROC/AUC Results Are Not Discussed Quantitatively
The paper mentions ROC curves and AUC as evaluation metrics but the actual AUC values are not reported in the text or tables. Only accuracy, precision, recall, and F1-score are tabulated. AUC values should be reported for each class and each split scenario to provide a complete picture of classifier performance.

### W11: Dataset Availability Is Unclear
The data availability statement mentions that seismic waveform data are from the UGM antenna station but does not indicate whether the labeled dataset (275 events, features, labels) is publicly available. For reproducibility, the dataset and code should be deposited in a public repository (e.g., Zenodo, GitHub).

### W12: No Discussion of Real-Time Applicability
The paper claims the framework extends ML-based monitoring "beyond conventional near-field monitoring networks," implying operational applicability. However, the processing pipeline (manual FK analysis, catalogue cross-checking) is not automated end-to-end and cannot be deployed in real time as described. The gap between the research prototype and an operational system is not discussed.

---

## Suggestions

1. **Expand the dataset**: Extend the observation period to at least 6 months or 1 year to increase the number of events per class and capture different activity phases.
2. **Add deep learning baselines**: Include at least 1D CNN and LSTM classifiers for comparison. Even a simple CNN trained on raw waveform segments would provide a meaningful benchmark.
3. **Apply data augmentation**: Test SMOTE, time-shifting, or noise injection to address class imbalance and increase effective training set size.
4. **Perform feature importance analysis**: Use SHAP values or permutation importance to identify the most discriminative features and guide feature selection.
5. **Report AUC values explicitly**: Add a table of per-class AUC values for both classifiers under all split scenarios.
6. **Provide a near-field comparison**: If possible, apply the same feature extraction and classification pipeline to BPPTKG near-field recordings for the same events to quantify the performance cost of remote monitoring.
7. **Deposit dataset and code**: Make the labeled dataset and processing code publicly available (e.g., Zenodo, GitHub) to support reproducibility and community use.
8. **Discuss real-time deployment pathway**: Add a section discussing what would be needed to automate the pipeline for real-time operational use.
9. **Investigate incorporating FK features as ML inputs**: Test whether adding back-azimuth, slowness, and beam power as additional ML features improves classification of ambiguous events (particularly Multiphase vs. Non Event).

---

## Questions

1. What were the AUC values for each class under the 80:20 split (the best-performing scenario)? Are these reported in the learning curve figures?
2. Were the 275 validated events distributed uniformly across the 28-day observation period, or were they concentrated in specific days? If concentrated, does this affect the chronological train–test split?
3. What is the SNR distribution of the validated events? Are there systematic differences in SNR between correctly and incorrectly classified events?
4. Were any events present in both the BMKG and BPPTKG catalogues (i.e., events that could be either tectonic or volcanic)? How were these handled?
5. Is the labeled dataset (275 events with extracted features) available for download? If not, are there plans to make it available?
6. How does the XGBoost model perform on the individual classes at the 80:20 split? The overall accuracy is 72.73%, but what are the per-class recall values for VTB and Multiphase specifically?

---

## Rating: 4 / 10 — Reject (Major Revision Required)

**Key reasons:** (1) The dataset is too small (275 events, 28 days) to support robust ML evaluation and the broad conclusions drawn. (2) The absence of deep learning baselines (CNN, LSTM) and Random Forest makes the experimental comparison incomplete. (3) No data augmentation is applied despite severe small-sample limitations. (4) AUC values are not reported despite being listed as an evaluation metric. These issues collectively undermine the experimental validity of the paper's claims.

---

## Confidence: High

I am highly confident in this assessment based on my expertise in experimental design for seismic monitoring systems and ML benchmarking. The weaknesses identified are clearly verifiable from the manuscript content and directly impact the validity of the experimental conclusions.
