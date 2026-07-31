# Reviewer 2 Report — Experiments & Practical Impact Specialist

**Paper:** Source-Specific Homogenization of Earthquake Magnitudes in Indonesia: Deming Calibration to MwGCMT and Independent Temporal Validation  
**Reviewer expertise:** Seismic catalogue construction, experimental design, statistical validation, seismic hazard analysis, earthquake data processing  

---

## Summary

This paper develops a source-specific magnitude homogenization method for the Indonesian earthquake catalogue, converting 29 type×agency magnitude combinations to MwGCMT via Deming regression. The experimental design separates data into development (1905–2024) and independent validation (2025) datasets, with all model parameters frozen before the validation data are opened. The study applies the resulting relations to 193,464 events and demonstrates a Mw availability increase from 2.437% to 26.876% for 2010–2024. The independent 2025 validation on 108 events yields RMSE=0.1464, MAE=0.0986, bias=+0.0258, and R²=0.8684. Four relations achieve full evaluation (N≥30 pairs), all passing pre-specified criteria. The paper presents six figures and eight tables describing the data composition, results, and spatial distribution of Mw availability.

---

## Soundness: 3/5

The experimental design is conceptually sound and the data separation is principled. However, the validation dataset is critically small (108 events, only 4 relations fully evaluated), the unreviewed status of 2025 ISC data is a material concern, and the absence of any comparison against existing global or pooled relations means the practical benefit of the approach cannot be quantified.

---

## Presentation: 3/5

Figures are generally informative and appropriately labelled. However, Figure 1 contains two errors (discussed below), Table 8 (Supplementary Table S1) is not adequately described in the main text, and several tables referenced in the text appear to be missing from the submitted document. The abstract reports excessively precise decimal values (e.g., 29.8552%, 24.439 pp) that are inappropriate for a scientific abstract and suggest the text was auto-generated from code output without editorial review.

---

## Contribution: 3/5

The practical contribution — increasing Mw availability for Indonesia from ~2.4% to ~26.9% — is significant for Indonesian seismology and downstream PSHA applications. The methodological contribution (source-specific relations with pre-registered parameters) is meaningful. However, the contribution is weakened by the limited validation scope and the absence of downstream application or comparison with existing approaches.

---

## Strengths

1. **Principled data separation.** The strict separation of development data (1905–2024) and validation data (2025), with SHA-256 checksumming of the frozen model archive, is a strong experimental design that effectively prevents data leakage. This is rare in the catalogue homogenization literature and substantially increases the credibility of the validation claim.

2. **Large development dataset.** The use of 193,464 events with 887,472 magnitude reports from 106 agency codes and 45 magnitude types provides a comprehensive basis for deriving 29 relations. The dataset scale is appropriate for the Indonesian catalogue context.

3. **Transparent reporting of limitations.** The paper is commendably honest about its limitations: the single-year validation, the unreviewed 2025 data, the insufficient sample support for 25 of 29 relations, and the non-statistical nature of the 2010 boundary. This transparency is a strength.

4. **Spatial analysis.** Figure 6 and the spatial Mw availability analysis (368 eligible 1° cells, median gain 29.134 pp) provide a useful geographic perspective on the practical impact of the homogenization. The map correctly identifies that gains are spatially uneven, which is important for regional hazard applications.

5. **Correct interpretation of frequency-magnitude distribution.** The paper explicitly and correctly states that the shift in availability turnover from Mw 5.0 to 4.1 describes Mw availability, not network detection completeness. This distinction is important and is often incorrectly made in catalogue papers.

6. **Provenance preservation.** The event-level product retains all original catalogue columns and appends Mw_Final with full provenance fields (relation, source value, model identifier, domain status, selection reason). This is a best practice that enables downstream auditing and reanalysis.

7. **Supplementary Table S1.** Providing all 29 frozen equations, lambda values, domains, and metrics in a supplementary table supports reproducibility and enables direct application by other researchers.

---

## Weaknesses

### W1. Validation dataset is critically small [CRITICAL]
The independent 2025 validation is based on only 108 events with observed MwGCMT, of which only 4 relations have ≥30 pairs. The remaining 25 relations have either 10–29 pairs (4 relations) or fewer than 10 pairs (21 relations). This means:
- 86.2% of accepted relations (25/29) cannot be fully evaluated.
- The system-level RMSE of 0.1464 is based on 108 events drawn predominantly from 4 relations, so it does not represent the full system.
- A sample of 108 events in one calendar year is insufficient to distinguish genuine temporal generalizability from stochastic variation. The literature on temporal validation in seismology recommends multiple non-overlapping years or rolling windows (Taroni et al., 2014; Naylor et al., 2022) to characterize performance variability.

The paper acknowledges this limitation but does not adequately discuss its implications for the strength of the validation claim. The phrase "The remaining relations were not classified as failures" is logically correct but does not resolve the practical problem: 25 relations are deployed in the catalogue without independent validation.

### W2. 2025 data quality is compromised [CRITICAL]
Section 2.3 states: "ISC metadata indicated that records from 2024 onward were unreviewed at the time of extraction." Unreviewed ISC data may contain duplicate events, incorrect magnitude assignments, or missing reports that would inflate or deflate the apparent error. The sensitivity analysis (excluding physical duplicate candidates: N=76, RMSE=0.1570, R²=0.8051) shows non-trivial changes in performance metrics when potential duplicates are removed. The paper treats this as a "sensitivity analysis" but does not resolve whether the unreviewed data are suitable for a definitive independent validation. The authors should either (a) use reviewed data only, (b) demonstrate that the unreviewed records do not systematically bias the results, or (c) downgrade the validation claim accordingly.

### W3. No comparison with existing approaches [MAJOR]
The paper does not compare its source-specific Deming relations against:
- Global relations (Scordilis, 2006) applied to Indonesian events
- Pooled relations (e.g., combining mbNEIC + mbGFZ + mbISC into one relation)
- The relations used in the companion catalogue (Masykuri et al., 2026)
- Ordinary least squares applied to the same data

Without such comparisons, the claim that source-specific Deming regression is superior to existing approaches is not supported by evidence. The opposite-direction ΔM plot (Figure 3) demonstrates that pooled corrections would be misleading, but it does not demonstrate that the source-specific Deming relations are more accurate than, for example, source-specific OLS relations.

### W4. Figure 1 contains two errors [MAJOR]
- The caption states "2010-2014" but the text consistently and correctly states "2010-2024." This is a clear typographic error that should have been caught in proofreading.
- The figure shows "BMKG?DJA" in the cross-source archival audit box. The question mark is presumably a rendering artifact (likely a non-standard character or encoding issue), but it appears in the submitted figure and is unprofessional.

### W5. Mw availability is only ~30% of the development catalogue [MAJOR]
After applying all 29 relations to 193,464 development events, only 57,759 events (29.86%) receive a final Mw. This means ~70% of the catalogue remains without Mw. The paper does not:
- Analyze why 70% of events cannot be converted (are they missing the required magnitude type? Outside the domain? Pre-1905?)
- Discuss the implications for analyses that require a complete Mw catalogue (e.g., b-value estimation, Mc assessment)
- Provide guidance on whether the 30% with Mw is representative of the full catalogue in terms of magnitude, depth, and geographic distribution

For the 2010–2024 window, Mw availability is 26.876% — still leaving 73% of events without Mw. The practical utility of the catalogue for PSHA depends critically on whether this 27% is a representative sample.

### W6. The 2010 boundary is not statistically validated [MODERATE]
Section 2.11 states: "The year 2010 was chosen as the start of a contemporary window because it aligned with a post-2009 shift in catalogue-source composition toward BMKG reporting. This restriction reduced confounding... The 2010 boundary was not estimated as a statistical change point." The choice of 2010 as the demonstration window start is therefore subjective. The paper should either (a) provide a statistical change-point analysis to support the 2010 boundary, (b) test sensitivity of the results to alternative boundaries (e.g., 2008, 2012), or (c) more clearly label the 2010–2024 results as a descriptive demonstration rather than a validated finding.

### W7. Threshold analysis in Table 7 is potentially misleading [MODERATE]
Table 7 shows that at Mw ≥ 4.0, the homogenized catalogue contains 27,752 events vs. 2,937 observed MwGCMT. However, GCMT does not report events below Mw ~5.0 systematically. The comparison at Mw ≥ 4.0 is therefore between a homogenized catalogue (which includes converted mb, ML, and Ms values) and a GCMT catalogue that is by design incomplete below Mw 5.0. This comparison is potentially misleading about the "gain" at low magnitudes. The paper should clarify that the comparison at Mw ≥ 4.0 reflects the lower GCMT completeness threshold, not a failure of the homogenization.

### W8. No assessment of spatial representativeness of the validation set [MODERATE]
The 108 validation events are drawn from a single ISC search rectangle (latitude -15° to 5°, longitude 90° to 142°). No analysis is provided of whether these 108 events are spatially representative of the full Indonesian catalogue or whether they are concentrated in specific subregions (e.g., Sumatra, Java, Sulawesi). Given that the conversion relations are derived from the full catalogue, spatial clustering in the validation set could bias the system-level metrics.

### W9. The ΔM distribution (Figure 2) is multimodal and unexplained [MODERATE]
Figure 2 shows a clearly multimodal distribution of ΔM values, with clusters at approximately ΔM ≈ -0.5, -0.2, 0.0, +0.1, and +1.0. The paper notes that "a small aggregate correction can conceal source-specific corrections in opposite directions" but does not explain the specific modes. The multimodality likely reflects the different relations (e.g., mB_DJA with large positive ΔM, mb with moderate negative ΔM), but this is not explicitly demonstrated. Figure 3 (route-specific median ΔM) partially addresses this but the connection between the two figures is not made explicit.

### W10. Data availability statement is incomplete [MODERATE]
The data availability section states: "The public repository DOI and licence remain to be completed before submission." This is unacceptable for a manuscript submitted for peer review. The conversion tables, audit summaries, and validation results should be deposited in a public repository before submission, with a complete DOI provided. Without this, the reproducibility claim cannot be verified.

### W11. Supplementary Table S2 is referenced but not provided [MINOR]
Section 2.2 references "Supplementary Table S2" for details on the 4,807 unresolved rows, but only Table S1 is listed in the "Referenced supplementary material" section. This supplementary table is missing from the submitted document.

---

## Suggestions

1. **Extend the validation period** by applying the frozen models to 2026 data (when available) or by performing a retrospective multi-year rolling validation (e.g., holding out 2022, 2023, 2024 sequentially) to provide more robust performance estimates across multiple years.
2. **Add a comparison table** showing performance of source-specific Deming relations vs. global relations (Scordilis, 2006) and vs. pooled source relations on the 2025 validation set.
3. **Correct Figure 1** errors: change "2010-2014" to "2010-2024" and fix the "BMKG?DJA" rendering artifact.
4. **Complete the data availability statement** before submission, including the repository DOI, licence, and a clear description of what is and is not publicly available.
5. **Add Supplementary Table S2** (the 4,807 unresolved rows) to the supplementary material.
6. **Analyze the 70% of events without Mw**: provide a breakdown by magnitude type, time period, and geographic region to assess representativeness.
7. **Clarify the Mw ≥ 4.0 comparison** in Table 7 by noting that GCMT is systematically incomplete below Mw ~5.0, so the "gain" at low magnitudes partly reflects GCMT's design threshold rather than a homogenization benefit.
8. **Provide spatial analysis of the 108 validation events** to assess geographic representativeness.
9. **Perform a sensitivity analysis** for the 2010 boundary using alternative start years (2008, 2012) to assess robustness.
10. **Explicitly connect Figure 2 and Figure 3**: identify which modes in the ΔM distribution correspond to which source-specific relations.

---

## Questions

1. Of the 193,464 development events, approximately how many lack any magnitude report that falls within the domain of any accepted relation? Is the 70% without Mw primarily due to domain exclusions, missing magnitude types, or pre-1960 historical events?

2. For the 2025 validation, how many of the 108 events are from each of the four fully-evaluated relations (MwwNEIC, MGFZ, mbNEIC, mbGFZ)? Is the system-level RMSE dominated by one or two relations?

3. What is the geographic distribution of the 108 validation events? Are they concentrated in specific tectonic subregions of Indonesia?

4. The sensitivity analysis after excluding physical duplicate candidates (N=76, RMSE=0.1570, R²=0.8051) shows a meaningful drop in R² (from 0.8684 to 0.8051). How were "physical duplicate candidates" identified? Is this identification itself based on the 2025 data, and if so, does it constitute post-validation data inspection?

5. For the 2010–2024 demonstration, the paper reports that 29,450 events obtained Mw through conversion. What is the magnitude distribution of these converted events? Are they predominantly in the Mw 4.0–5.0 range (where GCMT is incomplete) or are there also conversions at higher magnitudes where GCMT should already provide coverage?

6. The data availability section states that the public repository DOI is "to be completed before submission." Has the data been deposited? If not, when will it be available?

---

## Rating: 5/10

**Recommendation: Major Revision**

The paper presents a practically important and methodologically principled contribution to Indonesian seismology. The data separation design and provenance-preserving framework are genuine strengths. However, the validation dataset is critically small (108 events, 4 relations fully evaluated), the 2025 data quality is compromised by the unreviewed status, no comparison with existing approaches is provided, Figure 1 contains two errors, and the data availability statement is incomplete. These are not minor editorial issues — they are fundamental to the paper's central claim of "independent temporal validation." The paper should be substantially revised to address these concerns before it can be considered for acceptance.

---

## Confidence: High

I am highly confident in this assessment based on extensive experience with seismic catalogue construction, experimental design for validation studies, and the specific challenges of multi-agency magnitude homogenization.
