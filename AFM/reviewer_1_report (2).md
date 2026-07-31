# Reviewer 1 Report — Methods & Theory Specialist

**Paper:** Source-Specific Homogenization of Earthquake Magnitudes in Indonesia: Deming Calibration to MwGCMT and Independent Temporal Validation  
**Reviewer expertise:** Statistical seismology, errors-in-variables regression, magnitude scaling, earthquake catalogue methodology  

---

## Summary

This paper presents a source-specific earthquake magnitude homogenization framework for the Indonesian earthquake catalogue, converting 29 type×agency magnitude combinations directly to MwGCMT using Deming regression. The methodology includes a seven-value lambda (error-variance ratio) grid evaluated by expanding-window forward temporal validation, paired bootstrap resampling stratified by year, and a deterministic priority hierarchy for selecting one final Mw per event. All model parameters were finalized and checksummed before opening an independent 2025 validation dataset. The paper reports RMSE=0.1464, bias=+0.0258, and R²=0.8684 on 108 independent 2025 events, with 4 of 29 relations having sufficient sample support for full evaluation. The methodology is applied to demonstrate a Mw availability increase from 2.437% to 26.876% for the 2010–2024 window.

---

## Soundness: 3/5

The theoretical foundations are generally correct, but several critical methodological details are either missing, incompletely reported, or insufficiently justified, undermining the reproducibility and theoretical soundness of the work.

---

## Presentation: 3/5

The paper is clearly structured and logically organized. However, the mathematical exposition is critically incomplete: equations are referenced by number but their content is not rendered in the manuscript (e.g., Equations 1, 2, 3, 4 are cited but the actual mathematical expressions are absent or appear as placeholders). This is a fatal flaw for a methods paper. Writing quality is generally good, though some sections are excessively verbose and repeat the same caveats multiple times.

---

## Contribution: 3/5

The systematic workflow (source-specific relations + forward-validated λ selection + pre-registration + stratified bootstrap + deterministic hierarchy) is a meaningful contribution to regional catalogue methodology. The individual mathematical components (Deming regression, bootstrap, forward validation) are not new. The combination and its application to Indonesia fill a documented gap.

---

## Strengths

1. **Methodologically rigorous workflow design.** The decision to treat each type×agency combination as a separate relation, prohibit chained conversion and cross-agency pooling, and finalize all parameters before validation is principled and well-motivated. This addresses documented weaknesses in the catalogue homogenization literature (Lolli & Gasperini, 2012; Weatherill et al., 2016).

2. **Forward temporal validation for lambda selection.** Using expanding-window forward cross-validation to select the error-variance ratio λ — rather than fixing it a priori or selecting post hoc — is a methodological contribution not documented in equivalent regional catalogue work. The expanding-window design correctly prevents information leakage from later years into model fitting.

3. **Stratified bootstrap resampling.** Stratifying bootstrap replicates within year preserves the temporal structure of the data and avoids the well-known problem of random resampling breaking temporal autocorrelation. This is a technically sound choice.

4. **Pre-registration with SHA-256 checksum.** Archiving the finalized model set with a cryptographic hash before opening the 2025 data is a strong reproducibility measure that effectively prevents post hoc model adjustment. This practice is rare in the magnitude homogenization literature and represents a genuine methodological advance.

5. **Numerical verification.** Independent verification of Deming coefficients to machine precision (max absolute differences of ~4.8×10⁻¹⁰) demonstrates implementation correctness. The distinction between numerical verification (implementation correctness) and temporal validation (generalizability) is clearly and correctly drawn.

6. **Deterministic selection hierarchy.** The fixed priority rule for selecting one final Mw per event (observed GCMT > preferred relation > conditional relation > missing) prevents event-by-event manual selection after predictions are known, which is a meaningful protection against data dredging.

---

## Weaknesses

### W1. Equations are missing from the manuscript [CRITICAL]
Equations 1–4 (the Deming model, the lambda definition, the slope/intercept estimators, the RMSE/bias formulas) are referenced in the text but their mathematical content is not present in the submitted document. This is a critical flaw: a methods paper that does not display its core equations cannot be evaluated for theoretical correctness. The manuscript states "Using centred covariance moments Sxx, Syy, and Sxy, the positive-slope Deming estimator was:" followed by nothing. This must be corrected before any serious review can be completed.

### W2. Lambda selection rationale is insufficiently justified [MAJOR]
The paper selects λ from the grid {0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875} using forward temporal validation. However:
- The physical interpretation of each λ value is not discussed. λ = error variance of y / error variance of x (or its inverse, depending on convention). The paper does not state which convention is used, nor does it provide any empirical estimate of measurement uncertainties for any magnitude type or agency.
- The fact that 27 of 29 relations select λ = 0.875 raises a critical question: does this reflect a genuine signal in the data, or is it an artifact of the grid being truncated below the optimal value? The paper acknowledges this and suggests extending the grid above 1.0 for future work, but does not test it within the current study. This is a significant omission.
- Symmetric Deming (λ = 1) and OLS are described as "benchmarks" but are excluded from the principal selection grid. There is no justification for excluding λ = 1 from the selection grid while including λ = 0.875 — the difference is small and the exclusion is arbitrary.
- The selection criterion (lowest blocked RMSE, then lowest absolute bias, then lowest absolute temporal residual trend, then higher λ as tie-breaker) mixes prediction error with a regularization preference for higher λ. The use of higher λ as a tie-breaker introduces a systematic bias toward the upper grid boundary that is not physically motivated.

### W3. Screening criteria are not fully reported [MAJOR]
Table 3 is referenced as containing "eligibility and classification criteria" but its full content is not visible in the manuscript. The text mentions "at least 30 direct pairs with GCMT, at least three active overlap years, and source and target magnitude ranges of at least 0.8" as basic eligibility criteria, and references "additional criteria" for preferred classification, but these are not listed explicitly. Without the complete criteria table, the classification of 19 preferred vs. 10 conditional relations cannot be independently evaluated.

### W4. The pass/fail thresholds for 2025 validation are not stated [MAJOR]
Section 2.10 states that "a pass required:" followed by criteria described as "relation-specific because they incorporated forward-validation performance during development." However, the actual numerical thresholds are not stated in the manuscript body. The reader cannot verify whether the four relations that "passed" actually met pre-specified criteria or whether the thresholds were set to ensure passage. This is a critical transparency issue for a study that emphasizes pre-registration.

### W5. Lambda convention and physical interpretation are absent [MAJOR]
The paper defines λ as "the relative uncertainty of the GCMT target and the source magnitude" but does not provide a mathematical definition. In the Deming/GOR literature, λ = σ²_y / σ²_x (or its inverse) and its value determines the regression direction between OLS(x on y) and OLS(y on x). The paper does not state which convention is used, does not provide any empirical estimates of σ_x or σ_y for any magnitude type, and does not discuss how the GCMT measurement uncertainty (which is known to vary with event size and mechanism) is handled. This is a significant theoretical gap.

### W6. The 4,807 unresolved rows are inadequately addressed [MODERATE]
Section 2.2 states that "a tail of 4,807 unresolved rows was reported separately and excluded from the pre-validation completeness claim." This represents ~5.4% of the 89,278-event matrix. The nature of these unresolved rows (duplicates? conflicting reports? missing agency codes?) is not described, and their exclusion is not justified. This affects the completeness of the cross-source audit claim (99.992237% exact numeric-cell reconstruction).

### W7. Forward temporal validation fold details are insufficient [MODERATE]
Section 2.7 describes "expanding-window forward active-year blocks" but does not specify:
- How "active years" are defined (years with ≥N pairs? years with any pairs?)
- How many folds were generated for each relation
- Whether the blocked RMSE is averaged across folds or computed on the concatenated test set
- How the temporal residual trend is quantified (slope of residuals vs. time? Mann-Kendall test?)

### W8. No comparison with existing global or pooled relations [MODERATE]
The paper does not compare its source-specific Deming relations against: (a) existing global relations (Scordilis, 2006; ISC-GEM relations), (b) simpler pooled relations (pooling mbNEIC + mbGFZ + mbISC), or (c) ordinary least squares. Without such comparisons, the added value of the source-specific framework and the Deming estimator cannot be quantified. The claim that source-specific relations are necessary is supported by the opposite-direction ΔM plot but not by a formal comparison.

### W9. Uncertainty in converted Mw values is not propagated [MODERATE]
The paper reports RMSE and bias for the validation set but does not provide per-event uncertainty estimates for the converted Mw values. For downstream PSHA and b-value analyses, uncertainty propagation is essential. The bootstrap procedure generates coefficient uncertainty, but this is not translated into prediction intervals for individual events.

### W10. The reference "Masykuri et al., 2026" is problematic [MINOR]
The companion paper is cited as "Masykuri et al., 2026" with a full DOI and journal reference. This implies the paper is either accepted/in press or has been assigned a future publication date. If the companion paper is not yet published and peer-reviewed, the current manuscript's reliance on it (for the event framework, data provenance, and catalogue structure) is a concern. The current paper cannot be fully evaluated without access to the companion paper.

---

## Suggestions

1. **Restore all equations** (Deming model, λ definition, slope/intercept estimators, RMSE/bias formulas) to the manuscript. These are essential for a methods paper.
2. **State the λ convention explicitly** (σ²_y/σ²_x or σ²_x/σ²_y) and provide at least order-of-magnitude empirical estimates of measurement uncertainty for the major magnitude types.
3. **Extend the lambda grid** to include λ = 1.0 and values above 1.0 (e.g., {0.875, 1.0, 1.5, 2.0}) and report whether the concentration at 0.875 persists. If it does, the current grid is adequate; if not, the current results may be suboptimal.
4. **Report the pre-specified pass/fail thresholds** for the 2025 validation in the manuscript body (not only in supplementary material), so readers can verify the pass claims independently.
5. **Add a comparison table** showing performance of source-specific Deming relations vs. pooled relations and vs. OLS for at least the four highest-N relations.
6. **Describe the 4,807 unresolved rows** and assess whether their exclusion affects any of the main results.
7. **Provide per-event prediction intervals** for converted Mw values, derived from the bootstrap coefficient distributions.
8. **Clarify fold construction** for the forward temporal validation: number of folds per relation, minimum training/test sizes, and how blocked RMSE is aggregated.
9. **Add a section or appendix** comparing the source-specific approach against pooled alternatives to quantify the benefit of agency separation.

---

## Questions

1. What is the exact mathematical definition of λ in your Deming implementation? Is it σ²_y/σ²_x (GCMT variance / source variance) or the inverse? This affects whether λ = 0.875 implies the source magnitude is more uncertain than GCMT or vice versa.

2. Why was λ = 1.0 (symmetric Deming) excluded from the principal selection grid? Given that 27 of 29 relations select λ = 0.875, which is the closest value to 1.0 in your grid, this exclusion seems arbitrary.

3. For the 21 candidate model records excluded during initial screening (from 322 candidates to 301), what were the specific reasons for exclusion? Were any of these exclusions made after inspecting the forward-validation results?

4. What are the exact numerical pass/fail thresholds for the 2025 relation-level evaluation? The manuscript states they are "relation-specific" and "incorporated forward-validation performance" but does not provide the actual values.

5. How is "blocked RMSE" defined and computed? Is it the RMSE on the concatenated test-period observations across all folds, or is it the average of fold-level RMSEs?

6. The 4,807 unresolved rows: what is their nature? Are they events with conflicting reports from different agencies? Duplicate entries? Missing agency codes? Do they disproportionately affect any particular relation?

---

## Rating: 5/10

**Recommendation: Major Revision**

The paper addresses a genuine and important problem with a principled methodological workflow. The pre-registration approach and forward-validated lambda selection are meaningful contributions. However, the absence of the core mathematical equations from the manuscript is a fatal flaw for a methods paper. Several critical methodological details (pass/fail thresholds, lambda convention, fold construction, screening criteria) are either missing or incompletely reported. The lack of comparison with existing global or pooled relations prevents quantification of the added value of the source-specific approach. These issues must be resolved before the paper can be accepted.

---

## Confidence: High

I am highly confident in this assessment based on deep familiarity with the errors-in-variables regression literature in seismology and the specific methodological choices described (and not described) in this manuscript.
