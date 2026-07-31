# Novelty and Impact Report

**Paper:** Source-Specific Homogenization of Earthquake Magnitudes in Indonesia: Deming Calibration to MwGCMT and Independent Temporal Validation  
**Author(s):** Anas Fauzi Masykuri, Wiwit Suryanto, Theodosius Marwan Irnaka, Bayu Pranata  
**Affiliation:** Universitas Gadjah Mada / BMKG, Indonesia  

---

## 1. Summary of Core Claims

The paper claims the following contributions:
1. A source-specific (type × agency) magnitude homogenization framework for Indonesia, using direct Deming regression to MwGCMT.
2. A systematic lambda (error-variance ratio) selection procedure using forward temporal validation across a grid of seven λ values.
3. Pre-registration of all model parameters before opening independent 2025 validation data.
4. 29 accepted conversion relations (19 preferred, 10 conditional) applied to 193,464 events (1905–2024).
5. Independent temporal validation on 108 events from 2025 (RMSE=0.1464, R²=0.8684).
6. A demonstration of Mw availability gain from 2.437% to 26.876% for 2010–2024.

---

## 2. Novelty Assessment

### 2.1 Deming Regression and Errors-in-Variables Methods

**State of the art:** Errors-in-variables (EIV) regression methods — including general orthogonal regression (GOR), York/Williamson bivariate fits, and Deming/total least squares — are well-established in the seismological literature for magnitude conversion (Lolli & Gasperini, 2012; Castellaro et al., 2006; Wason et al., 2012). Bootstrap confidence intervals (typically 1,000 resamples) and sensitivity testing of the error-variance ratio are also documented practices. The ISC Bulletin homogenization (Lolli et al., 2023) uses chi-square regression with explicit uncertainties. Robust maximum-likelihood estimators have also been proposed (Akkaya & Yucemen, 2014).

**Novelty of this paper's approach:**
- The specific use of **Deming regression with a 7-value λ grid selected by forward temporal validation** is not documented in the seismological literature reviewed. Prior studies either use a fixed ratio, test sensitivity post hoc, or use iterative York fits with empirically estimated uncertainties. The forward-validation-driven lambda selection is a genuinely novel procedural contribution.
- The **stratified-by-year bootstrap** (preserving temporal structure during resampling) is a methodological refinement not widely described in regional catalogue papers.
- However, the regression estimator itself (Deming/GOR) is not new. The novelty lies in the **systematic workflow** rather than the mathematical method.

**Assessment:** *Moderate novelty* in regression methodology; *higher novelty* in the systematic lambda-selection and bootstrap stratification procedure.

### 2.2 Source-Specific (Type × Agency) Framework

**State of the art:** Most regional homogenization studies pool magnitude types across agencies (e.g., all mb reports regardless of origin), or derive global/regional relations without preserving agency identity (Scordilis, 2006; Das et al., 2011; Tan, 2021). A few studies note agency-specific biases (Kumar et al., 2020; Wason et al., 2012), and the ISC Bulletin homogenization (Lolli et al., 2023) uses agency-tagged data. For Indonesia specifically, existing work (Yanto & Yee, 2022; Anggraini & Heryandoko, 2018) uses pooled or global relations without explicit type×agency separation. The East African Rift catalogue (Holmgren et al., 2023, cited in the paper) uses GOR with agency-specific tracking but does not implement the full source-specific priority framework described here.

**Novelty of this paper's approach:**
- Treating each **magnitude-type × reporting-agency combination** as a separate calibration unit (e.g., mbNEIC ≠ mbGFZ ≠ mbISC) is a meaningful methodological distinction that is underrepresented in the regional catalogue literature.
- The **hierarchical priority system** (preferred vs. conditional, with a deterministic selection rule finalized before validation) is a structured provenance-preserving framework not documented in equivalent form for any Indonesian or Southeast Asian catalogue.
- The explicit prohibition of chained conversion, cross-agency pooling, and averaging of multiple predictions represents a set of principled design constraints that go beyond most published approaches.

**Assessment:** *High novelty* for Indonesia and Southeast Asia; *moderate novelty* globally, as the ISC Bulletin and some global catalogues implicitly handle agency identity but do not formalize the full decision framework described here.

### 2.3 Pre-Registration and Independent Temporal Validation

**State of the art:** In earthquake forecasting and seismological model evaluation, the distinction between retrospective and prospective (out-of-sample) testing is well-established (Tashman, 2000; Roberts et al., 2017; Iturrieta et al., 2024; CSEP framework). Forward temporal cross-validation (rolling-origin) is increasingly used in seismic model evaluation (Nandan et al., 2019; Mizrahi et al., 2024). However, in the **magnitude homogenization literature**, formal pre-registration of model parameters before a validation dataset is opened is essentially absent — most studies report in-sample or cross-validated performance without a strict data-separation protocol.

**Novelty of this paper's approach:**
- Applying **prospective-style pre-registration** (SHA-256 checksum of the frozen model archive before opening 2025 data) to a magnitude-conversion calibration problem is genuinely novel in this literature domain. It directly addresses the critique that cross-validation in temporally structured seismological data can overstate performance (Roberts et al., 2017).
- The **expanding-window forward temporal validation** used for lambda selection (not just for final reporting) is a methodological contribution that goes beyond most published homogenization workflows.

**Assessment:** *High novelty* in the context of magnitude homogenization; the approach imports rigorous validation practices from forecasting science into catalogue construction.

### 2.4 Application to Indonesia

**State of the art:** Indonesia is among the most seismically active regions globally, yet its earthquake catalogues have historically relied on pooled or global magnitude conversion relations (Scordilis, 2006 applied globally; regional BMKG conversions are limited). The companion paper (Masykuri et al., 2026) establishes the integrated event framework. The present study fills a documented gap in source-specific, provenance-preserving Mw homogenization for Indonesia.

**Novelty:** *High practical novelty* — no equivalent source-specific, multi-agency, forward-validated homogenization framework exists for the Indonesian catalogue in the published literature.

---

## 3. Impact Assessment

### 3.1 Significance for the Field

- **Seismic hazard analysis:** The increase in Mw availability from ~2.4% to ~26.9% (2010–2024) has direct implications for probabilistic seismic hazard analysis (PSHA), b-value estimation, and magnitude-of-completeness studies in Indonesia. The demonstration that pooled corrections can cancel (opposite-direction shifts across agencies) is practically important for hazard modellers.
- **Reproducibility and data provenance:** The emphasis on provenance fields (relation identifier, source value, domain status, selection reason) addresses a gap in catalogue transparency that has been noted in the literature (Sandve et al., 2013; Wilkinson et al., 2016).
- **Methodological template:** The workflow — source-specific relations, pre-registered parameters, forward-validated lambda selection, stratified bootstrap, deterministic hierarchy — could serve as a template for other multi-agency regional catalogues (Southeast Asia, East Africa, Himalayan belt).

### 3.2 Limitations Affecting Impact

- **Single validation year (2025):** The independent validation covers only 108 events in one calendar year, with only 4 of 29 relations having ≥30 validation pairs. This substantially limits the strength of the generalization claim. Best practices recommend multiple non-overlapping years or rolling windows (Taroni et al., 2014; Naylor et al., 2022; Iturrieta et al., 2024).
- **Unreviewed 2025 data:** ISC records from 2024 onward were unreviewed at extraction, introducing potential data quality issues in the validation set.
- **Lambda concentration at 0.875:** 27 of 29 relations select λ = 0.875, suggesting the grid may not be optimally placed. The physical interpretation of this concentration is not fully explored.
- **No uncertainty propagation downstream:** The paper does not propagate conversion uncertainty into downstream seismological products (b-value, Mc, hazard curves), limiting its direct applicability to PSHA.
- **Historical catalogue coverage:** Only 29.86% of 193,464 development events receive a final Mw, leaving ~70% without Mw. The implications for historical (pre-2010) seismicity analyses are not fully addressed.
- **Missing comparison with global/existing relations:** The paper does not directly compare its source-specific relations against existing global relations (Scordilis, 2006; ISC-GEM) or against simpler pooled relations, making it difficult to quantify the added value of the source-specific approach.

---

## 4. Positioning with Respect to Key Prior Work

| Prior Work | Relationship to This Paper |
|---|---|
| Lolli & Gasperini (2012) — GOR comparison | Uses similar EIV framework; this paper extends with forward-validated λ selection |
| Scordilis (2006) — global Ms/mb → Mw | Global pooled relations; this paper provides Indonesia-specific source-specific alternatives |
| Weatherill et al. (2016) — OpenQuake homogenization | Closest methodological comparator; this paper adds agency identity and pre-registration |
| ISC Bulletin homogenization (Lolli et al., 2023) | Global scale, chi-square regression; this paper is regional with forward-validated λ |
| Holmgren et al. (2023) — East African Rift | GOR with agency tracking; this paper adds priority hierarchy and pre-registration |
| Yanto & Yee (2022) — Expanding Mw pools for Indonesia | Pooled approach; this paper provides source-specific alternative |
| Roberts et al. (2017) — temporal CV strategies | Provides theoretical basis for this paper's forward validation approach |
| Tashman (2000) — out-of-sample testing | Foundational reference for the pre-registration claim |

---

## 5. Overall Novelty and Impact Verdict

**Novelty score: Moderate-to-High**  
The paper's novelty lies primarily in the *systematic workflow* (source-specific relations + forward-validated λ selection + pre-registration + stratified bootstrap + deterministic hierarchy), rather than in any single new mathematical method. The combination of these elements in a regional catalogue context for Indonesia is genuinely novel.

**Impact score: Moderate**  
The practical impact on Indonesian seismology is significant. The methodological template has broader applicability. However, the single-year validation limitation, the absence of uncertainty propagation downstream, the lack of direct comparison with existing global/pooled relations, and the incomplete data availability statement reduce the immediate scientific impact. Strengthening the validation strategy and adding comparative benchmarks would substantially increase the paper's contribution.

---

## 6. Missing Citations and Literature Gaps

The following relevant works are not cited in the manuscript and should be considered:
1. **Lolli et al. (2023)** — ISC Bulletin magnitude homogenization (Geophysical Journal International) — directly comparable global-scale work
2. **Holmgren et al. (2023)** — East African Rift relocated catalogue with GOR — cited in paper but comparison not made explicit
3. **Wason et al. (2012)** — Magnitude conversion problem using GOR — foundational for EIV discussion
4. **Akkaya & Yucemen (2014)** — Robust estimation of magnitude conversion equations
5. **Gasperini et al. (2013)** — Empirical calibration of local magnitude vs Mw in Italy — relevant for ML conversion methodology
6. **Llenos et al. (2026)** — Magnitude conversion relations create substantial differences in seismic hazard models — directly relevant to impact discussion
7. **Iturrieta et al. (2024)** — Decade-long prospective earthquake forecasting experiment — relevant for validation framework discussion
8. **Tan (2021)** — Homogeneous earthquake catalogue for Turkey — regional comparator
