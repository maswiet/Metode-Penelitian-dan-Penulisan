# Reviewer 3 Report — Clarity, Positioning & Broader Impact Specialist

**Paper:** Source-Specific Homogenization of Earthquake Magnitudes in Indonesia: Deming Calibration to MwGCMT and Independent Temporal Validation  
**Reviewer expertise:** Scientific writing, research communication, seismological literature, broader societal impact of earthquake catalogue products, research reproducibility  

---

## Summary

This manuscript presents a source-specific magnitude homogenization method for the Indonesian earthquake catalogue, using Deming regression to convert 29 type×agency magnitude combinations to MwGCMT. The paper emphasizes methodological rigour through pre-registration of model parameters, forward temporal validation, and provenance preservation. Key results include 29 accepted conversion relations, independent 2025 validation metrics (RMSE=0.1464, R²=0.8684 on 108 events), and a demonstration that Mw availability for 2010–2024 increases from 2.437% to 26.876%. The paper is logically structured and generally well-written, but has significant issues with completeness (missing equations, incomplete data availability, missing supplementary materials), several typographic and formatting errors, and limited engagement with the broader implications of the work for seismic hazard, disaster risk reduction, and the Indonesian seismological community.

---

## Soundness: 3/5

The overall scientific approach is sound. The main concerns relate to the incomplete manuscript (missing equations, missing supplementary tables, incomplete data availability statement) and the limited validation scope (108 events, single year).

---

## Presentation: 2.5/5

The manuscript has significant presentation problems that must be corrected. The most critical is the absence of mathematical equations that are cited by number but not displayed. Additional issues include typographic errors in a figure, inconsistent author affiliation formatting, excessively precise numerical reporting in the abstract, and an incomplete data availability statement. These issues collectively suggest the manuscript was submitted in an incomplete draft state.

---

## Contribution: 3/5

The contribution to Indonesian seismology is clear and practically important. The methodological contribution (source-specific framework with pre-registered parameters) is meaningful but would benefit from stronger positioning against the international literature and more explicit discussion of downstream applications.

---

## Strengths

1. **Clear logical structure.** The manuscript is organized into well-defined sections with a logical progression from motivation (Section 1) through methods (Section 2), results (Section 3), discussion (Section 4), and conclusions (Section 5). The analytical sequence is summarized effectively in Figure 1 (notwithstanding the errors identified below).

2. **Honest and detailed limitations section.** Section 4.7 is a model of transparent scientific reporting, listing seven specific limitations including the single-year validation, unreviewed 2025 data, physical duplicate candidates, empirical λ selection, partial audit coverage, limited demonstration window, and map interpretation caveats. This level of transparency is commendable and unusual in a PhD manuscript.

3. **Appropriate figure design.** Figures 2–6 are well-designed, clearly labelled, and include appropriate statistical summaries (medians, percentiles, reference lines). The captions are informative and include important interpretive notes (e.g., "Turnover describes Mw availability, not network-detection completeness" in Figure 5). The spatial maps in Figure 6 are well-formatted and correctly use a 1°×1° grid with minimum cell occupancy threshold.

4. **Correct and careful use of statistical language.** The paper consistently avoids common misinterpretations: R² is explicitly stated not to mean "86.84% accuracy"; the frequency-magnitude turnover is correctly distinguished from magnitude of completeness; percentage-point gains are distinguished from relative percentage increases. These distinctions are important and correctly made.

5. **Practical provenance framework.** The description of the event-level product (Section 2.13) — retaining all original columns, appending Mw_Final with provenance fields, never overwriting original magnitudes — is a practical contribution to data management that aligns with FAIR data principles (Wilkinson et al., 2016).

6. **Reproducibility infrastructure.** The use of versioned Jupyter notebooks, intermediate tables, quality checks, input-output manifests, and checksums is consistent with best practices in reproducible computational research (Sandve et al., 2013; Wilson et al., 2017).

---

## Weaknesses

### W1. Mathematical equations are absent from the manuscript [CRITICAL]
This is the most serious presentation flaw. Section 2.6 (Deming regression) states:
- "For source-specific relation r, source magnitude x was converted directly to y = MwGCMT using a linear model: (1)"
- "The error-variance ratio was defined as: [no equation]"
- "Using centred covariance moments Sxx, Syy, and Sxy, the positive-slope Deming estimator was: [no equation]"
- "Prediction error was summarized using RMSE and bias: [no equation]"

All four equations are referenced by number but their mathematical content is missing. This is unacceptable in a submitted manuscript. A methods paper that does not display its core mathematical formulas cannot be peer-reviewed for correctness. This must be corrected before any further review.

### W2. Figure 1 caption error: "2010-2014" should be "2010-2024" [MAJOR]
The caption for Figure 1 reads: "Data through 2024 were used to build and finalize the models; the 2025 data were used only for independent temporal validation; 2010-2014 was used to demonstrate catalogue consequences." The correct period is 2010–2024, as stated consistently throughout the manuscript. This error in the figure caption of the paper's only workflow diagram is a significant oversight.

### W3. Figure 1 contains "BMKG?DJA" rendering artifact [MAJOR]
The cross-source archival audit box in Figure 1 displays "BMKG?DJA" with a question mark. This is almost certainly a character encoding or font rendering error (the intended text is likely "BMKG/DJA" or "BMKG–DJA"). This error appears in the submitted figure and must be corrected.

### W4. Author affiliation formatting is inconsistent [MAJOR]
The title page lists authors as "Anas Fauzi Masykuri¹·²·³, Wiwit Suryanto¹·²·*, Theodosius Marwan Irnakaa, Bayu Pranatac" — the first two authors use numeric superscripts (1, 2, 3) while the last two use alphabetic superscripts (a, c). Affiliation footnote b appears to be missing. This is a formatting error that must be corrected.

### W5. Abstract reports excessively precise numerical values [MAJOR]
The abstract contains values such as "29.8552%", "24.439 percentage points", and "29.134 percentage points." These levels of precision (4–5 significant figures) are inappropriate for an abstract and suggest the text was pasted directly from code output without editorial review. Abstracts should report values to 2–3 significant figures (e.g., "~30%", "~24 percentage points"). The excessive precision also creates a false impression of measurement accuracy that is inconsistent with the acknowledged limitations (unreviewed data, single-year validation).

### W6. Data availability statement is incomplete [MAJOR]
The data availability section states: "The public repository DOI and licence remain to be completed before submission." This is an explicit acknowledgment that the manuscript is being submitted in an incomplete state. A manuscript cannot be properly reviewed if the data and code repository is not available. The authors must deposit the conversion tables, audit summaries, validation results, and demonstration outputs in a public repository (e.g., Zenodo, Mendeley Data, GitHub with DOI) and provide the complete DOI and licence before submission.

### W7. Supplementary Table S2 is referenced but not provided [MAJOR]
Section 2.2 references "Supplementary Table S2" for details on the 4,807 unresolved rows. The "Referenced supplementary material" section lists only Table S1. This supplementary table is missing from the submitted document. The companion paper dataset (Mendeley Data, DOI 10.17632/26zjrr4sgp.1) is referenced but the current paper's own supplementary data are incomplete.

### W8. Related work section is absent [MAJOR]
The introduction contains relevant background citations but there is no dedicated "Related Work" or "Previous Studies" subsection that systematically positions this paper against comparable regional and global magnitude homogenization studies. The following important works are not cited or compared:
- **Lolli et al. (2023)** — ISC Bulletin magnitude homogenization (Geophysical Journal International) — the most directly comparable global-scale work using a similar EIV approach
- **Weatherill et al. (2016)** — cited but not compared in terms of methodology
- **Holmgren et al. (2023)** — cited but no explicit comparison of the GOR approach vs. this paper's Deming framework
- **Tan (2021)** — homogeneous catalogue for Turkey — a regional comparator
- **Llenos et al. (2026)** — magnitude conversion relations create substantial differences in seismic hazard models — directly relevant to the impact discussion

The absence of systematic comparison with these works leaves the reader unable to assess where this paper fits in the international landscape of catalogue homogenization.

### W9. The paper's title may overstate the validation claim [MODERATE]
The title includes "Independent Temporal Validation" as a co-equal contribution alongside the Deming calibration. Given that the validation covers only 108 events in a single year, with only 4 of 29 relations fully evaluated and the data being unreviewed, the title may set expectations that the results cannot fully meet. A more qualified subtitle (e.g., "...and Preliminary Independent Temporal Validation" or "...with Single-Year Independent Temporal Validation") would better reflect the actual validation scope.

### W10. Discussion section is repetitive [MODERATE]
Several points in the Discussion (Section 4) repeat content from the Methods and Results sections without adding new insight. For example:
- Section 4.2 restates the validation metrics already reported in Section 3.5.
- Section 4.3 restates the design constraints already described in Section 2.4.
- Section 4.5 restates the lambda concentration result already reported in Section 3.2.

The Discussion should focus on interpreting results in the context of the broader literature, not on restating what was already reported. This repetitiveness inflates the manuscript length without adding scientific content.

### W11. Broader impact and downstream applications are underdeveloped [MODERATE]
The paper demonstrates a Mw availability increase from ~2.4% to ~26.9% for 2010–2024 but does not discuss the specific downstream applications that this enables. For example:
- **b-value and Mc estimation:** How does the increased Mw availability affect estimates of the Gutenberg-Richter b-value and magnitude of completeness for Indonesian subregions?
- **PSHA:** What is the expected impact on probabilistic seismic hazard curves for major Indonesian cities (Jakarta, Banda Aceh, Padang)?
- **Tsunami warning:** BMKG operates the InaTEWS tsunami warning system. Does the homogenized Mw catalogue improve rapid magnitude estimation for tsunami triggering?
- **Seismotectonic analysis:** How does the expanded Mw catalogue affect understanding of seismicity patterns along the Sunda Megathrust and other major fault systems?

These applications are mentioned obliquely (Section 4.8) but not developed. A brief quantitative demonstration for one downstream application would substantially strengthen the paper's impact case.

### W12. The reference to a 2026 paper is unusual and unexplained [MINOR]
The companion paper "Masykuri et al., 2026" is cited throughout with a full DOI and journal reference (Frontiers in Earth Science, 14, 1779764). If this paper is accepted and in press, this should be stated explicitly (e.g., "Masykuri et al., in press, 2026"). If it has already been published online ahead of print, the access date should be provided. The citation as "2026" without explanation is confusing to readers in the current year.

### W13. Conclusions section could be more concise [MINOR]
The Conclusions section (Section 5) largely repeats the abstract. It could be condensed to 3–4 sentences stating the main findings and their implications, with the quantitative details already provided in the abstract.

---

## Suggestions

1. **Restore all four equations** (Deming model, λ definition, slope/intercept estimators, RMSE/bias) to Section 2.6. These are essential for the manuscript.
2. **Correct Figure 1**: change "2010-2014" to "2010-2024" and fix the "BMKG?DJA" rendering artifact.
3. **Standardize author affiliation superscripts** to a single system (all numeric or all alphabetic) and ensure all affiliations (1, 2, 3, a, b, c) are consistently defined.
4. **Revise the abstract** to report numerical values to 2–3 significant figures (e.g., "~30%" instead of "29.8552%").
5. **Complete the data availability statement** with the repository DOI and licence before submission.
6. **Add Supplementary Table S2** (details on the 4,807 unresolved rows).
7. **Add a dedicated Related Work subsection** in the Introduction, explicitly comparing this paper's approach to Lolli et al. (2023), Weatherill et al. (2016), Holmgren et al. (2023), and at least one other regional catalogue paper.
8. **Revise the Discussion** to eliminate repetition of Methods and Results content and focus on interpretation, comparison with the literature, and implications.
9. **Add a downstream application section** — even a brief analysis of b-value or Mc changes for one Indonesian subregion would substantially strengthen the impact case.
10. **Clarify the status of the companion paper** (in press, accepted, published online) in the reference list.
11. **Consider qualifying the title** to accurately reflect the single-year, limited-coverage nature of the validation.
12. **Condense the Conclusions** to avoid repeating the abstract.

---

## Questions

1. The companion paper (Masykuri et al., 2026) is cited as published in Frontiers in Earth Science with a DOI. Is this paper currently accessible online? If so, please provide an access date. If not, how can reviewers of the current paper verify the event framework on which this study depends?

2. The paper emphasizes that the 2025 data cannot be used to modify the model and then described as independent validation. Has any model adjustment been made after the 2025 results were known? The SHA-256 checksum provides a strong safeguard, but the paper should explicitly confirm that no model changes were made after the validation data were opened.

3. The paper mentions that "operational deployment would require continuous data integration, an interface, maintenance, and institutional governance." Is there a plan for operational deployment within BMKG? If so, what is the timeline and what institutional arrangements are being made?

4. The abstract states that "chained conversion, untested cross-agency pooling, segmented final models, averaging of multiple predictions, and extrapolation beyond empirical domains were not used." Are there any circumstances where these approaches might be appropriate? The paper's prohibition of these practices is presented as absolute, but some contexts (e.g., historical events before 1960 with limited magnitude coverage) might justify different approaches.

5. Figure 2 shows a clearly multimodal ΔM distribution. What are the approximate magnitudes corresponding to each mode? Is the mode at ΔM ≈ +1.0 associated with a specific relation (e.g., MS_ISC, which has the largest positive median ΔM in Figure 3)?

---

## Rating: 5/10

**Recommendation: Major Revision**

The paper addresses an important problem for Indonesian seismology with a principled and transparent methodology. The provenance-preserving framework, pre-registration approach, and honest limitations discussion are genuine strengths. However, the manuscript is submitted in an incomplete state: core equations are missing, a figure contains two errors, author affiliations are inconsistently formatted, the data availability statement is incomplete, and a supplementary table is missing. The related work positioning is insufficient, the discussion is repetitive, and the broader impact is underdeveloped. These are not minor editorial issues — several are fundamental to the paper's scientific content. The manuscript requires substantial revision before it can be considered for publication.

---

## Confidence: High

I am highly confident in this assessment based on extensive experience evaluating scientific manuscripts in seismology and related geosciences, with particular attention to research communication, reproducibility standards, and the positioning of regional catalogue studies within the international literature.
