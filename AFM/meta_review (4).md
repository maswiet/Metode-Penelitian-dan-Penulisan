# Meta-Review and Final Decision

**Paper:** Source-Specific Homogenization of Earthquake Magnitudes in Indonesia: Deming Calibration to MwGCMT and Independent Temporal Validation  
**Authors:** Anas Fauzi Masykuri, Wiwit Suryanto, Theodosius Marwan Irnaka, Bayu Pranata  
**Reviews received:** 3 (Methods & Theory Specialist; Experiments & Practical Impact Specialist; Clarity, Positioning & Broader Impact Specialist)

---

## 1. Overview of Reviewer Assessments

| Criterion | Reviewer 1 (Methods) | Reviewer 2 (Experiments) | Reviewer 3 (Clarity) |
|---|---|---|---|
| Soundness | 3/5 | 3/5 | 3/5 |
| Presentation | 3/5 | 3/5 | 2.5/5 |
| Contribution | 3/5 | 3/5 | 3/5 |
| Overall Rating | 5/10 | 5/10 | 5/10 |
| Recommendation | Major Revision | Major Revision | Major Revision |

All three reviewers independently converged on a **Major Revision** recommendation with scores of 5/10. This is a notable degree of agreement for three reviewers with different areas of emphasis.

---

## 2. Key Agreements Across All Three Reviewers

### 2.1 Methodological Strengths Are Genuine
All three reviewers acknowledge the paper's core methodological contributions:
- The **source-specific (type×agency) framework** is a meaningful advance over pooled approaches.
- The **pre-registration with SHA-256 checksum** before opening the 2025 validation data is an unusually rigorous practice in the magnitude homogenization literature.
- The **forward temporal validation for lambda selection** is a novel procedural contribution.
- The **stratified bootstrap resampling** and **deterministic priority hierarchy** are technically sound.
- The **provenance-preserving event-level product** aligns with FAIR data principles and best practices.

### 2.2 The Manuscript is Submitted in an Incomplete State [CRITICAL — All Reviewers]
All three reviewers independently identified that **core mathematical equations are missing from the manuscript**. Section 2.6 references Equations 1–4 by number but their mathematical content is absent. This is a fatal flaw for a methods paper and must be corrected before any publication decision can be made. Reviewers 2 and 3 also independently identified that:
- **Supplementary Table S2** (details on 4,807 unresolved rows) is referenced but not provided.
- The **data availability statement** is explicitly incomplete ("The public repository DOI and licence remain to be completed before submission").

### 2.3 The Validation Dataset is Critically Small [CRITICAL — All Reviewers]
All three reviewers raised serious concerns about the validation scope:
- Only **108 events** from a single calendar year (2025) constitute the independent validation set.
- Only **4 of 29 relations** (13.8%) have sufficient sample support (≥30 pairs) for full evaluation.
- The **unreviewed status of 2025 ISC data** compromises the quality of the validation dataset.
- The sensitivity analysis (N=76 after excluding duplicate candidates: RMSE 0.1570, R² 0.8051 vs. full-set RMSE 0.1464, R² 0.8684) shows non-trivial performance changes, raising questions about the robustness of the validation metrics.
- **Best practice** in temporal validation (Taroni et al., 2014; Naylor et al., 2022; Iturrieta et al., 2024) recommends multiple non-overlapping years or rolling windows, not a single-year holdout.

### 2.4 No Comparison with Existing Approaches [MAJOR — Reviewers 1 and 2]
Both methodological reviewers independently noted the absence of any comparison between the proposed source-specific Deming relations and:
- Existing global relations (Scordilis, 2006)
- Pooled source-specific relations
- Ordinary least squares on the same data
Without such comparisons, the added value of the source-specific Deming framework cannot be quantified.

### 2.5 Figure 1 Errors [MAJOR — Reviewers 2 and 3]
Both Reviewers 2 and 3 independently identified two errors in Figure 1:
- Caption reads "2010-2014" instead of "2010-2024"
- The figure displays "BMKG?DJA" — a rendering artifact

### 2.6 Lambda Selection Concerns [MAJOR — Reviewers 1 and 2]
Both methodological reviewers raised concerns about the lambda (λ) selection:
- The physical interpretation of λ and its convention (σ²_y/σ²_x or inverse) is not stated.
- 27/29 relations select λ = 0.875 (the upper grid boundary), suggesting the grid may be truncated.
- The exclusion of λ = 1.0 from the selection grid while including λ = 0.875 is not justified.

---

## 3. Reviewer-Specific Concerns Not Shared by Others

### From Reviewer 1 (Methods) Only:
- The pass/fail thresholds for 2025 relation-level validation are not stated in the manuscript body, preventing independent verification of the "pass" claims.
- The forward temporal validation fold construction (active year definition, fold count, blocked RMSE aggregation) is insufficiently described.
- The 4,807 unresolved rows are inadequately characterized.
- No per-event prediction intervals for converted Mw values are provided.

### From Reviewer 2 (Experiments) Only:
- The 70% of development events without Mw (after applying all 29 relations) is not analyzed for representativeness.
- The 2010 demonstration boundary is not statistically validated.
- The Mw ≥ 4.0 threshold comparison may be misleading given GCMT's design completeness threshold (~Mw 5.0).
- The ΔM distribution (Figure 2) is multimodal and the modes are not explained.
- The spatial representativeness of the 108 validation events is not assessed.

### From Reviewer 3 (Clarity) Only:
- The abstract reports excessively precise numerical values (e.g., 29.8552%) inappropriate for a scientific abstract.
- Author affiliation formatting is inconsistent (numeric vs. alphabetic superscripts).
- A dedicated Related Work subsection is absent; key comparable papers (Lolli et al., 2023; Tan, 2021; Llenos et al., 2026) are not cited or compared.
- The Discussion section is repetitive, restating Methods and Results content.
- Broader impact (PSHA, tsunami warning, seismotectonic analysis) is underdeveloped.
- The title may overstate the validation claim given its single-year scope.
- The status of the companion paper "Masykuri et al., 2026" is not clarified.

---

## 4. Disagreements Between Reviewers

There are **no substantive disagreements** between the three reviewers. All three converged on the same overall rating (5/10), the same recommendation (Major Revision), and the same primary concerns (missing equations, small validation set, no comparison with existing approaches). The reviewers differ in the specific additional concerns they raise, reflecting their different areas of expertise, but these are complementary rather than contradictory.

The only minor difference in emphasis is that Reviewer 3 is more concerned with the manuscript's incomplete state (missing equations, formatting errors, incomplete data availability) as a presentation issue, while Reviewers 1 and 2 frame the same issues primarily as methodological concerns. This difference in framing does not affect the recommendation.

---

## 5. Assessment of the Paper's Core Contribution

Despite the concerns above, the meta-reviewer notes that the paper's **core scientific contribution is genuine and valuable**:

1. The source-specific framework with pre-registered parameters represents a methodological advance in regional catalogue homogenization that is not documented in equivalent form for Indonesia or most other regional catalogues.
2. The practical impact — increasing Mw availability from ~2.4% to ~26.9% for 2010–2024 — is significant for Indonesian seismology and PSHA.
3. The workflow (source-specific relations + forward-validated λ + stratified bootstrap + deterministic hierarchy + provenance preservation) provides a replicable template for other multi-agency regional catalogues.

The paper has the potential to be a strong contribution to the field. The current issues are primarily about manuscript completeness, validation scope, and positioning — all of which are addressable through revision.

---

## 6. Required Revisions (Mandatory for Acceptance)

The following revisions are **mandatory** and must be completed before the paper can be reconsidered:

**R1. Restore all mathematical equations** (Deming model, λ definition, slope/intercept estimators, RMSE/bias formulas) to Section 2.6. These are essential for a methods paper.

**R2. Complete the data availability statement** with the repository DOI and licence before resubmission. The conversion tables, audit summaries, validation results, and demonstration outputs must be publicly available.

**R3. Add Supplementary Table S2** (details on the 4,807 unresolved rows) to the supplementary material.

**R4. Correct Figure 1**: fix "2010-2014" to "2010-2024" and resolve the "BMKG?DJA" rendering artifact.

**R5. State the pre-specified pass/fail thresholds** for the 2025 relation-level validation in the manuscript body (not only in supplementary material).

**R6. State the λ convention explicitly** (σ²_y/σ²_x or inverse) and provide the physical justification for the λ = 0.875 concentration.

**R7. Standardize author affiliation formatting** (consistent numeric or alphabetic superscripts throughout).

**R8. Add a comparison** of source-specific Deming relations against at least one alternative (global pooled relations or OLS on the same data) on the 2025 validation set.

**R9. Add a dedicated Related Work subsection** citing and comparing Lolli et al. (2023), Weatherill et al. (2016), Holmgren et al. (2023), and at least one regional comparator.

**R10. Revise the abstract** to report numerical values to 2–3 significant figures.

---

## 7. Strongly Recommended Revisions

The following revisions are **strongly recommended** to substantially improve the paper:

**SR1. Extend or strengthen the validation**: Apply the frozen models to at least one additional year (e.g., reviewed 2023 or 2024 ISC data) to provide multi-year validation evidence. Alternatively, perform a retrospective rolling validation holding out 2022, 2023, and 2024 sequentially.

**SR2. Analyze the 70% of events without Mw**: Provide a breakdown by magnitude type, time period, and geographic region to assess whether the 30% with Mw is a representative sample.

**SR3. Add a downstream application**: Include a brief analysis of how the expanded Mw catalogue affects b-value or Mc estimates for at least one Indonesian subregion.

**SR4. Extend the lambda grid** to include λ = 1.0 and values above 1.0, and report whether the concentration at 0.875 persists.

**SR5. Revise the Discussion** to eliminate repetition of Methods/Results content and focus on interpretation, literature comparison, and implications.

**SR6. Clarify the companion paper status** (in press, accepted, published online) in the reference list.

---

## 8. Final Decision

**Decision: MAJOR REVISION**

The paper presents a genuinely novel and practically important contribution to Indonesian seismological catalogue methodology. The pre-registration approach, source-specific framework, and forward-validated lambda selection are meaningful advances that are not documented in equivalent form in the regional catalogue literature. However, the manuscript is currently submitted in an incomplete state (missing equations, incomplete data availability, missing supplementary table, figure errors), the validation dataset is critically small for the claims being made, and the paper lacks comparison with existing approaches. These are not minor editorial issues — they are fundamental to the paper's credibility as a methods paper.

The authors are encouraged to revise the manuscript addressing all mandatory revisions (R1–R10) and as many of the strongly recommended revisions (SR1–SR6) as possible. A revised manuscript that addresses these concerns would be a strong candidate for acceptance in a high-quality seismological journal.

**Estimated revision timeline:** 2–3 months for a thorough revision.

---

*Meta-review prepared based on three independent expert reviews. All three reviewers agreed on Major Revision. No reviewer recommended outright rejection, reflecting the genuine scientific merit of the work despite its current limitations.*
