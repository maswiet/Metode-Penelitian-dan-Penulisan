# Meta-Review — RE-REVIEW (Updated, 26 July 2026 Revision)

**Paper Title:** Array-Based Dataset Construction for Machine Learning Classification of Long-Distance Volcanic Seismic Signals  
**Authors:** Dairoh, Sudarmaji, Ahmad Ashari, Wiwit Suryanto  
**Review Round:** 2nd — Re-review of revised manuscript  
**Previous Decision:** Major Revision Required (Overall rating: 4.3/10)

---

## 1. Overview of the Revision

The 26 July 2026 revision adds approximately 750 words over the 23 July version. The substantive additions are:
- A differentiation paragraph in the Introduction explicitly distinguishing this work from prior publication [26]
- Figure 12: representative waveform/spectrum examples of correctly classified and misclassified events
- Table 4 (formerly Table 8): comparison of classification accuracy against Sidik et al. (2023)
- Extended Discussion with near-field performance contextualization and operational implications
- Reference renumbering: [25] now = Chen & Guestrin (XGBoost), [26] = Dairoh prior paper

---

## 2. Summary of Reviewer Assessments

### Areas of Agreement Across All Three Reviewers

**On positive changes:**
- All three reviewers acknowledge the differentiation paragraph as a genuine improvement.
- All three reviewers consider Figure 12 a useful addition that supports the confusion-matrix analysis.
- All three reviewers recognize Table 4 as a step toward better literature positioning, even if its scope is too narrow.
- All three reviewers note that the Discussion is better contextualized in the revision.

**On unresolved critical issues (unanimous):**
1. **Equations still not rendered** (Tables 3–6): All three reviewers flag this as a critical, unresolved formatting failure. The manuscript cannot be submitted to any journal with empty equation tables.
2. **Chronological vs. stratified split inconsistency**: All three reviewers confirm this contradiction persists unchanged across abstract, methods, and conclusion.
3. **Missing key references**: All three reviewers confirm that Titos et al. (2019), Ohrnberger (2001), Smith & Bean (2020), and Espinosa-Curilem (2024) are still absent. Malfante et al. (2018) is cited but not engaged with in the comparison.
4. **AUC values not reported numerically**: All three reviewers note that AUC is discussed qualitatively but no numerical values appear in any table.
5. **No deep learning or Random Forest baselines**: All three reviewers confirm this gap persists.
6. **All typographical errors persist**: All three reviewers confirm that none of the previously identified errors ("Univeritas," "Sciemces," "Leaming," "occorred," "cod.," etc.) have been corrected.

**On new critical issue (introduced in revision):**
- All three reviewers independently identify the same critical new error: the reference numbering swap has caused [25] in the body text (used 8 times to cite UGM array properties, data availability, and STA/LTA detection) to incorrectly point to Chen & Guestrin (XGBoost, 2016) instead of the Dairoh prior paper. This is a pervasive scientific citation error introduced in this revision.

---

### Reviewer-Specific Assessments

**Reviewer 1 (Methods & Theory)** emphasizes:
- FK/beamforming parameters still undisclosed — reproducibility remains impossible
- Multicollinearity (r = 0.98–1.00) still unaddressed in model design
- STA/LTA trigger threshold still not reported
- Bandpass filter still unjustified
- No statistical significance testing added

**Reviewer 2 (Experiments & Practical Impact)** emphasizes:
- Dataset still 275 events, 28 days — no augmentation applied
- No k-fold cross-validation added
- Comparison table (Table 4) too narrow — only one prior study
- Data and code still not deposited in a public repository
- SNR analysis (pre/post-beamforming) still absent

**Reviewer 3 (Clarity & Positioning)** emphasizes:
- Reference [25]/[26] numbering error is pervasive and serious
- Malfante et al. (2018) is already in the reference list but absent from comparison table
- Table 1 feature definitions still empty
- Abstract still too long and repetitive
- Title still does not reflect full scope

---

## 3. Issue-by-Issue Verdict

| # | Issue (from previous review) | Previous Status | Current Status | Change |
|---|-------------------------------|-----------------|----------------|--------|
| 1 | Equation rendering (Tables 3–6) | Critical | ❌ UNRESOLVED | No change |
| 2 | Chronological/stratified split inconsistency | Critical | ❌ UNRESOLVED | No change |
| 3 | FK/beamforming parameter disclosure | Critical | ❌ UNRESOLVED | No change |
| 4 | Deep learning/Random Forest baselines | Critical | ❌ UNRESOLVED | No change |
| 5 | Differentiation from [26] | Critical | ✅ PARTIALLY RESOLVED | Improved |
| 6 | Missing key references | Critical | ❌ UNRESOLVED | No change |
| 7 | AUC reporting (numerical values) | Critical | ❌ UNRESOLVED | No change |
| 8 | Typographical errors | Important | ❌ UNRESOLVED | No change |
| 9 | Multicollinearity/feature selection | Important | ❌ UNRESOLVED | No change |
| 10 | Data augmentation | Important | ❌ UNRESOLVED | No change |
| 11 | Statistical significance testing | Important | ❌ UNRESOLVED | No change |
| 12 | Table 1 definitions missing | Important | ❌ UNRESOLVED | No change |
| 13 | Abstract length/repetition | Important | ❌ UNRESOLVED | No change |
| 14 | Broader impact discussion | Moderate | ⚠️ PARTIALLY ADDRESSED | Slight improvement |
| 15 | Comparison with near-field performance | Moderate | ✅ PARTIALLY RESOLVED | Table 4 added |
| — | Reference [25]/[26] numbering error | NEW ISSUE | ❌ NEW PROBLEM | Introduced in revision |

**Score: 2 issues partially/fully resolved out of 15; 1 new critical issue introduced.**

---

## 4. Conflicting Opinions and Resolution

**On overall rating:**
- Reviewer 1: 4/10 (Reject, major revision) — emphasis on methodological incompleteness
- Reviewer 2: 5/10 (Reject, major revision) — acknowledges new additions but flags critical gaps
- Reviewer 3: 5/10 (Reject, major revision) — acknowledges positive effort but notes persistent failures

**Resolution:** The three reviewers are in close agreement. The slight upward movement from Reviewer 2 and 3 (4→5) reflects the genuine positive additions (differentiation paragraph, Figure 12, Table 4). However, all three agree the manuscript is still not publishable. The meta-reviewer concurs: the revision is insufficient.

**On the reference numbering error:**
All three reviewers independently identified this as a serious new problem. The meta-reviewer agrees that this error alone — incorrectly attributing 8 body-text citations about the UGM array to an XGBoost paper — would be grounds for immediate rejection at most journals and must be corrected before resubmission.

---

## 5. Final Decision: **REJECT — MAJOR REVISION STILL REQUIRED**

### Verdict: The manuscript is NOT ready for publication.

The revision demonstrates that the authors have made some effort to respond to reviewer feedback (differentiation paragraph, new figure, new table). However, the revision is inadequate in scope and depth. Of the 15 issues raised in the previous review, only 2 have been partially resolved, and 1 significant new error has been introduced. The manuscript cannot be published in its current state.

### Minimum Requirements for Next Revision

The following issues are **non-negotiable** and must be fully resolved before the manuscript can be re-reviewed:

#### 🔴 CRITICAL (Must Fix — Manuscript Unpublishable Without These)

**C1. Render all equations in Tables 3–6.**  
Every formula — SVM decision function, XGBoost objective, precision, recall, F1, TPR, FPR — must be properly typeset with mathematical notation. This is the most basic requirement for any scientific publication.

**C2. Fix the reference numbering error.**  
All [25] citations in the body text that refer to UGM array properties, data availability, and STA/LTA detection must be corrected to [26] (Dairoh prior paper). Verify every single citation in the manuscript against the reference list. Also fix the out-of-order reference list ([26] appears before [25]).

**C3. Resolve the chronological vs. stratified split inconsistency.**  
Choose one approach, implement it correctly, and describe it consistently in the abstract, methods, results, and conclusion. If stratified random sampling was used (as stated in Methods), remove all references to "chronological strategy." If chronological splitting was used, correct the Methods section and verify the implementation.

**C4. Disclose all FK analysis and beamforming parameters.**  
Add a comprehensive parameter table covering: beamforming algorithm, slowness search range and grid resolution, FK time-window length, coherence/beam-power threshold, back-azimuth tolerance for Merapi-direction discrimination, STA/LTA trigger on/off threshold.

**C5. Report AUC values numerically.**  
Add per-class AUC values for both classifiers under all four split scenarios to Table 3 or a dedicated table.

**C6. Fix all typographical errors.**  
Correct every error identified in previous reviews: "Univeritas," "Sciemces," "Leaming," "occorred," "eismology," "cod.," "wth Machine." These are trivially correctable.

#### 🟡 IMPORTANT (Strongly Recommended — Required for Top-Tier Journal)

**I1. Add at least one additional classifier baseline.**  
Random Forest is the minimum; CNN or LSTM would be preferred. This is essential for contextualizing the SVM/XGBoost results.

**I2. Add missing key references and engage with them.**  
At minimum: Titos et al. (2019), Ohrnberger (2001), Smith & Bean (2020). Malfante et al. (2018) is already cited — add it to Table 4.

**I3. Address multicollinearity.**  
Apply PCA, recursive feature elimination, or feature selection to address r = 0.98–1.00 correlations among amplitude features.

**I4. Complete Table 1.**  
Add mathematical definitions for all 11 features; clarify "i from the energy center."

**I5. Deposit dataset and code.**  
Make the 275-event labeled dataset and processing scripts publicly available.

---

## 6. Guidance for the PhD Student (Dairoh) — Second Round

The authors have made a genuine effort in this revision, and the positive additions (differentiation paragraph, Figure 12, Table 4) show that the authors understand the direction of improvement needed. However, the revision is incomplete. Here is specific guidance for the next round:

**What was done well:**
- The differentiation paragraph is clear and well-written — keep it.
- Figure 12 is a valuable addition — keep it.
- Table 4 is useful — expand it to include Malfante et al. (2018) and Ohrnberger (2001).
- The Discussion is better framed — maintain this improvement.

**What must be done immediately (before anything else):**
1. Fix the reference numbers — this is a one-hour task that will prevent immediate rejection.
2. Render the equations — this requires formatting work in Word/LaTeX but is essential.
3. Fix all typos — run Grammarly again and check every word.

**What requires more work:**
4. The split inconsistency needs a definitive decision: what did you actually do? Check your Python code and report what was implemented.
5. The FK parameter table needs to be compiled from your processing logs.
6. Adding Random Forest takes one afternoon in Python using scikit-learn.
7. AUC values can be extracted from your existing ROC curve data.

**Realistic assessment for publication:**
This paper has genuine merit as a proof-of-concept study demonstrating remote array-based dataset construction for volcanic monitoring. With the critical fixes above, it could be suitable for journals such as:
- *Seismological Research Letters* (SRL) — appropriate scope and level
- *Journal of Volcanology and Geothermal Research* (JVGR) — good fit for volcanic monitoring focus
- *Frontiers in Earth Science* — open-access, appropriate for proof-of-concept studies

For *Geophysical Journal International* (GJI), the dataset size (275 events), observation period (28 days), and absence of deep learning comparison would likely remain barriers even after the critical fixes.

---

## 7. Updated Summary Scorecard

| Criterion | Rev. 1 | Rev. 2 | Rev. 3 | Consensus |
|-----------|--------|--------|--------|-----------|
| Soundness | 2.5/5 | 2.5/5 | 3.0/5 | **2.7/5** |
| Presentation | 2.5/5 | 3.0/5 | 2.5/5 | **2.7/5** |
| Contribution | 2.5/5 | 3.0/5 | 3.0/5 | **2.8/5** |
| Overall Rating | 4/10 | 5/10 | 5/10 | **4.7/10** |
| Decision | Major Revision | Major Revision | Major Revision | **Major Revision** |

*Note: Slight improvement in Reviewer 2 and 3 scores (4→5) reflects the genuine positive additions in the revision. Reviewer 1 maintains 4/10 due to persistent methodological deficiencies. Overall consensus remains Major Revision.*
