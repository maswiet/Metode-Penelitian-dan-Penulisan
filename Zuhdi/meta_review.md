# Meta-Review and Editorial Decision

## Paper: Centered Horizontal Gravity Gradient (CHG): An Improved Operator for Interpreting Circular Gravity Anomalies

**Authors:** Muhammad Zuhdi, Wiwit Suryanto, Sudarmaji  
**Affiliation:** Gadjah Mada University, Indonesia  
**Submitted to:** Journal of Geophysical Research: Solid Earth (JGR)

**Associate Editor Assessment**  
**Date:** 2024

---

## Executive Summary

This manuscript introduces the Centered Horizontal Gravity Gradient (CHG) method, which decomposes horizontal gravity gradients into radial and tangential components relative to a selected center point for improved interpretation of circular anomalies. The paper includes synthetic model testing and application to gravity data from Samalas volcano caldera (Lombok, Indonesia). Three expert reviewers have evaluated the manuscript from complementary perspectives: theoretical/methodological (Reviewer 1), experimental/practical (Reviewer 2), and presentation/broader impact (Reviewer 3).

**Consensus Assessment:** All three reviewers agree that:
1. The core concept is genuinely novel and addresses a real interpretational challenge
2. The paper has significant potential but requires major revisions before acceptance
3. Comparison with advanced methods (not just standard THG) is essential
4. Validation is insufficient (single field case, no independent verification)
5. Presentation quality needs substantial improvement

**Editorial Decision:** **MAJOR REVISIONS REQUIRED**

---

## Reviewer Summary

### Reviewer 1: Methods & Theory Specialist
- **Rating:** 6/10 (Weak Accept / Major Revisions Required)
- **Soundness:** 3/5 | **Presentation:** 3/5 | **Contribution:** 6/10
- **Confidence:** 5/5 (Very Confident)

**Key Points:**
- Confirms genuine novelty of radial/tangential decomposition
- Mathematical framework is sound but theoretical development incomplete
- Critical issue: No comparison with state-of-the-art methods (EHD, MDA, GGT)
- Concerning SNR degradation in complex models inadequately addressed
- Center-point sensitivity not quantified
- Depth resolution not analyzed

### Reviewer 2: Experiments & Practical Impact Specialist
- **Rating:** 5/10 (Weak Reject / Major Revisions Required)
- **Soundness:** 3/5 | **Presentation:** 4/5 | **Contribution:** 5/10
- **Confidence:** 5/5 (Very Confident)

**Key Points:**
- Synthetic experiments well-designed but limited in scope
- Field validation insufficient (single case, no independent verification)
- Noise amplification in Model 3 is serious concern
- Data quality documentation inadequate
- No quantitative accuracy metrics provided
- Practical utility unclear without comparison to advanced methods

### Reviewer 3: Clarity, Positioning & Broader Impact Specialist
- **Rating:** 5/10 (Weak Reject / Major Revisions Required)
- **Soundness:** 3/5 | **Presentation:** 3/5 | **Contribution:** 5/10
- **Confidence:** 4/5 (Confident)

**Key Points:**
- Literature positioning inadequate (ignores advanced methods)
- Broader impacts underdeveloped (hazards, geothermal, societal relevance)
- Presentation quality poor (abstract errors, grammar, figure quality)
- Geological interpretation lacks validation and depth
- Practical guidance missing (when to use CHG vs. alternatives)

### Consensus Scores
- **Average Rating:** 5.3/10 (Major Revisions Required)
- **Average Soundness:** 3/5
- **Average Presentation:** 3.3/5
- **Average Contribution:** 5.3/10

---

## Areas of Agreement Among Reviewers

### Strengths (All Reviewers Agree)

1. **Genuine Novelty** ✅
   - All three reviewers confirm that the center-referenced radial/tangential decomposition is new
   - Literature review (227 papers, 1980-2025) found no prior work on this specific approach
   - Fills a conceptual gap in circular anomaly interpretation

2. **Sound Mathematical Framework** ✅
   - Coordinate transformation correctly implemented
   - Equations 3-4 properly project gradients onto radial/tangential directions
   - Core methodology is mathematically valid

3. **Interesting Field Application** ✅
   - Samalas caldera is significant (VEI 7, 1257 CE eruption, global climate impact)
   - First gravity-based structural interpretation of this important caldera
   - Timely given hazard implications for densely populated Lombok

4. **Systematic Synthetic Testing** ✅
   - Progression from simple to complex models is pedagogically sound
   - SNR analysis provides quantitative assessment (though results are concerning)
   - Forward modeling approach is appropriate

5. **Practical Utility Potential** ✅
   - Method addresses real interpretational need for circular features
   - Computationally efficient (uses only first derivatives)
   - Applicable to volcanic, geothermal, impact crater studies

### Critical Weaknesses (All Reviewers Agree)

1. **Inadequate Comparison with Advanced Methods** ❌
   - **Unanimous concern:** Comparison limited to standard THG (1986 baseline)
   - Missing comparisons with:
     * Enhanced Horizontal Derivative (EHD) - Fedi & Florio, 2001
     * Multiscale Derivative Analysis (MDA) - Fedi, 2002
     * Directional Total Horizontal Derivatives (DTHD) - Yuan & Geng, 2014
     * Gravity Gradient Tensor (GGT) methods - Kusumoto, 2016
     * Enhanced THG variants - Pham et al., 2024
   - **Impact:** Cannot assess whether CHG improves on current best practices
   - **All three reviewers identify this as the most critical deficiency**

2. **Insufficient Field Validation** ❌
   - **Unanimous concern:** Only one field case (Samalas) tested
   - No independent verification:
     * No comparison with published geological maps
     * No integration with seismic data (Sarjan et al., 2021; Priyono et al., 2021)
     * No validation with resistivity results (Hiden et al., 2017)
     * No testing on other well-studied calderas
   - No quantitative accuracy metrics (all interpretation qualitative)
   - **Impact:** Cannot verify accuracy or assess generalizability

3. **Concerning Noise Behavior** ⚠️
   - **All reviewers note:** Model 3 shows CHG SNR (7.0) worse than THG (10.1)
   - CHG SNR degrades dramatically: 35.5 (Model 1) → 7.0 (Model 3)
   - Authors acknowledge but don't adequately address
   - No mitigation strategies provided
   - **Impact:** Method may be unreliable in realistic complex geological settings

4. **Center-Point Sensitivity Not Quantified** ❌
   - Optimization proposed (Eq. 11) but not validated
   - No systematic testing of sensitivity to center-point errors
   - Convergence properties not analyzed
   - **Impact:** Unknown how critical accurate centering is

5. **Presentation Quality Issues** ❌
   - Grammar and language errors throughout
   - **Abstract contains formatting error (line 7) and typo (line 20)**
   - Figures lack geological context (no caldera rim, faults overlaid)
   - Missing tables (survey specs, model parameters, method comparison)
   - Insufficient methodological detail for reproduction

---

## Divergent Opinions and Resolution

### Minor Disagreement: Severity of Issues

**Reviewer 1** (Methods specialist) is slightly more positive (6/10 - Weak Accept) because:
- Mathematical framework is sound
- Core concept has theoretical merit
- Sees potential with revisions

**Reviewers 2 & 3** (Practical/Impact specialists) are more critical (5/10 - Weak Reject) because:
- Experimental validation insufficient
- Practical utility undemonstrated
- Broader impacts underdeveloped

**Editorial Resolution:**
Both perspectives are valid. The paper has theoretical merit but lacks practical validation. The consensus rating (5.3/10) reflects this: the work is not ready for acceptance but has potential with substantial revisions. The decision is **MAJOR REVISIONS** rather than outright rejection because:
- Core novelty is confirmed
- Methodological framework is sound
- Issues are addressable with additional work

### Presentation Quality Assessment

**Reviewer 2** rates presentation slightly higher (4/5) than Reviewers 1 & 3 (both 3/5).

**Reason:** Reviewer 2 focused more on figure design and data presentation, finding them generally clear despite missing details. Reviewers 1 & 3 weighted grammar errors and missing contextual information more heavily.

**Editorial Resolution:**
Average of 3.3/5 is appropriate. While figures are reasonably designed, the combination of:
- Grammar/language errors
- Abstract formatting error and typo
- Missing geological overlays
- Insufficient methodological detail
- No tables provided

...justifies a below-average presentation score. The abstract errors are particularly problematic and must be fixed.

---

## Detailed Assessment by Category

### 1. Novelty and Originality (STRONG)

**Reviewer consensus:** ✅ **Confirmed genuine novelty**

- Literature search (227 papers, 1980-2025) found no prior work on center-referenced radial/tangential decomposition
- Method addresses a documented gap: THG provides only scalar magnitude, cannot distinguish radial from tangential components
- Related approaches exist (directional derivatives, GGT) but are fundamentally different

**Novelty score: 8/10** (Reviewer 1's assessment, supported by literature analysis)

**However:** Novelty alone is insufficient. The paper must demonstrate that this novel approach provides practical advantages over existing methods.

### 2. Theoretical Foundation (MODERATE - NEEDS IMPROVEMENT)

**Reviewer 1 concerns (shared by others):**
- Incomplete theoretical analysis of when/why CHG outperforms alternatives
- Relationship to GGT not explored (could CHG be derived from tensor components?)
- Radial variance optimization (Eq. 11) lacks theoretical justification
- No error propagation analysis
- Depth resolution not analyzed

**Required improvements:**
- Derive conditions under which CHGrad maxima coincide with anomaly boundaries
- Explain relationship to GGT and directional derivatives theoretically
- Provide rigorous justification for radial variance metric
- Analyze depth resolution capabilities and limitations

### 3. Experimental Validation (WEAK - MAJOR IMPROVEMENTS NEEDED)

**All reviewers agree:** This is the paper's weakest aspect.

**Synthetic testing:**
- ✅ Well-designed progression (simple → complex)
- ✅ SNR analysis included
- ❌ Limited scenarios (only 3 models, all simple geometry)
- ❌ No depth variation testing
- ❌ No elliptical/irregular anomaly testing
- ❌ No comparison with advanced methods

**Field validation:**
- ✅ Significant application (Samalas caldera)
- ❌ Only one field case
- ❌ No independent verification (seismic, geological maps)
- ❌ No quantitative accuracy metrics
- ❌ Results entirely qualitative

**Critical requirement:** Add 2-3 well-studied calderas with independent structural control and quantitative validation.

### 4. Method Comparison (CRITICAL DEFICIENCY)

**Unanimous reviewer concern:** This is the most serious flaw.

**Current state:** Comparison only with standard THG (Blakely & Simpson, 1986)

**Required comparisons:**
1. **Enhanced Horizontal Derivative (EHD)** - Fedi & Florio, 2001
2. **Multiscale Derivative Analysis (MDA)** - Fedi, 2002
3. **Directional Total Horizontal Derivatives (DTHD)** - Yuan & Geng, 2014
4. **Gravity Gradient Tensor (GGT) methods** - Kusumoto, 2016
5. **Enhanced THG variants** - logistic, balanced, power-law (Pham et al., 2024)

**Why this is critical:**
- Cannot assess whether CHG provides practical improvement over current best practices
- Reviewers cannot recommend adoption without knowing performance relative to established methods
- This is standard expectation for methods papers

**Editorial requirement:** At minimum, compare with EHD, MDA, and one GGT method on all synthetic and field datasets.

### 5. Noise Sensitivity (SERIOUS CONCERN)

**All reviewers flag:** Model 3 SNR results are concerning.

**Observations:**
- CHG SNR: 35.5 (Model 1) → 16.8 (Model 2) → **7.0 (Model 3)**
- THG SNR: 30.7 (Model 1) → 15.6 (Model 2) → **10.1 (Model 3)**
- CHG shows worse noise performance in complex model

**Authors' response:** Acknowledge issue (line 285) but provide no:
- Explanation of mechanism
- Mitigation strategies
- Guidance on when CHG is appropriate

**Required improvements:**
- Explain why noise amplification occurs in complex models
- Test filtering/regularization strategies
- Define criteria for when CHG is suitable
- Provide quality control guidelines

**Reviewer 2 assessment:** "This suggests CHG may fail in realistic complex settings" - serious concern for practical adoption.

### 6. Data Quality and Documentation (INADEQUATE)

**Reviewer 2 emphasis (supported by others):**

**Missing information:**
- Gravity survey specifications (station spacing, coverage, accuracy)
- Processing parameters (gridding, filtering, derivative calculation)
- Data quality assessment (uncertainty, spatial error distribution)
- Regional/residual separation methodology
- Bouguer reduction density

**Impact:**
- Cannot assess data quality or suitability
- Cannot reproduce processing workflow
- Cannot evaluate reliability of results

**Required:** Comprehensive data documentation including survey specifications table and processing workflow description.

### 7. Presentation Quality (BELOW AVERAGE)

**Consensus issues:**

**Critical (must fix):**
- Abstract line 7: "gravity-= ~gradient" (formatting error)
- Abstract line 20: "CHGan" → "CHGtan" (typo)
- Grammar and language errors throughout

**Major (should fix):**
- Figures 8-10 lack geological overlays (caldera rim, faults, volcanic centers)
- No tables provided (survey specs, model parameters, method comparison)
- Captions too brief and uninformative
- Insufficient methodological detail

**Moderate:**
- Inconsistent notation (gx vs. ∂g/∂x)
- Low-resolution text in some figures
- Discussion section weak

**Reviewer 3:** "Abstract errors are particularly problematic" - first impression matters.

### 8. Broader Impacts (UNDERDEVELOPED)

**Reviewer 3 emphasis (supported by others):**

**Missing discussions:**
- Volcanic hazard assessment implications (despite Lombok application!)
- Geothermal exploration applications (mentioned once in passing)
- Planetary geophysics applications (not mentioned)
- Economic benefits for resource exploration
- Societal relevance (Lombok population, hazard mitigation)

**Context:** Samalas 1257 eruption had global climate impacts; Lombok is densely populated; method has clear hazard/resource implications.

**Required:** Substantially expand broader impacts discussion, emphasizing practical applications and societal relevance.

### 9. Practical Utility (UNCLEAR)

**All reviewers note:** Unclear when practitioners should use CHG vs. alternatives.

**Missing guidance:**
- When is CHG appropriate vs. EHD, MDA, GGT?
- What data quality is required?
- How critical is accurate center-point selection?
- What are the failure modes?
- Cost-benefit trade-offs?

**Required:** Provide practical decision framework for method selection and application guidelines.

---

## Required Revisions for Acceptance

### Essential (Must be completed for acceptance)

#### 1. Comprehensive Method Comparison ⭐⭐⭐
**Priority: CRITICAL**

- Implement EHD, MDA, DTHD, and at least one GGT method
- Apply all methods to:
  * All three synthetic models
  * Samalas field data
  * At least one additional field case
- Create side-by-side comparison figures
- Provide quantitative comparison table:
  * SNR for all models
  * Edge detection accuracy
  * Computational cost
  * Depth resolution
- Discuss when CHG outperforms alternatives and when it doesn't

**Reviewer consensus:** "This is the most critical deficiency" - all three reviewers

#### 2. Expand Field Validation ⭐⭐⭐
**Priority: CRITICAL**

- Apply CHG to 2-3 additional well-studied calderas:
  * Suggested: Campi Flegrei, Tambora, Yellowstone, or Kutcharo
  * Require independent structural control (seismic, drilling, detailed mapping)
- For Samalas case:
  * Overlay published caldera rim on CHG results
  * Integrate with seismic tomography (Sarjan et al., 2021)
  * Compare with attenuation results (Priyono et al., 2021)
  * Validate with resistivity data (Hiden et al., 2017)
- Provide quantitative accuracy metrics:
  * Distance between CHG-detected and mapped rim
  * ROC curves for edge detection
  * Misfit analysis for forward models

**Reviewer consensus:** "Single field case insufficient" - all three reviewers

#### 3. Address Noise Amplification ⭐⭐⭐
**Priority: CRITICAL**

- Explain why Model 3 shows SNR degradation
- Test mitigation strategies:
  * Upward continuation
  * Wavelength filtering
  * Regularization approaches
- Define criteria for when CHG is appropriate vs. when THG/alternatives are better
- Provide quality control guidelines
- Test with realistic (correlated) noise, not just white noise

**Reviewer 2:** "Method may be unreliable in realistic complex settings" - serious concern

#### 4. Validate Center-Point Optimization ⭐⭐
**Priority: HIGH**

- Test Eq. 11 on synthetic models with known centers
- Systematic sensitivity analysis (±0.5, 1, 2, 5 km offsets)
- Show convergence plots
- Demonstrate robustness to initial guess
- Specify search parameters (step size, convergence criteria)
- Test on multiple overlapping circles

**Reviewer 1:** "Performance sensitive to center-point accuracy; optimization not tested"

#### 5. Fix Presentation Issues ⭐⭐
**Priority: HIGH**

**Critical fixes:**
- Fix abstract formatting error (line 7)
- Fix abstract typo (line 20: CHGan → CHGtan)
- Careful proofreading to eliminate grammar errors
- Standardize notation throughout

**Major improvements:**
- Add geological overlays to Figures 8-10 (caldera rim, faults, volcanic centers)
- Create essential tables:
  * Survey specifications
  * Synthetic model parameters
  * Quantitative method comparison
  * SNR summary
- Improve figure captions (complete information, explain what to observe)
- Add methodological detail for reproducibility

**Reviewer 3:** "Abstract errors particularly problematic" - affects first impression

### Highly Desirable (Strongly recommended)

#### 6. Expand Synthetic Testing ⭐
**Priority: MODERATE-HIGH**

- Test varying source depths (1, 3, 5, 10 km)
- Test elliptical anomalies (eccentricity 0.2, 0.5, 0.8)
- Test tilted/dipping circular structures
- Test regional gradient superposition
- Test realistic density contrasts (±0.1-0.2 g/cm³, not just ±0.4)

#### 7. Strengthen Theoretical Foundation ⭐
**Priority: MODERATE-HIGH**

- Derive conditions for optimal CHG performance
- Explain relationship to GGT (can CHG be derived from tensor?)
- Provide theoretical justification for radial variance metric
- Include error propagation analysis
- Analyze depth resolution capabilities

#### 8. Expand Broader Impacts Discussion ⭐
**Priority: MODERATE-HIGH**

- Volcanic hazard assessment implications
- Geothermal exploration applications (with examples)
- Planetary geophysics potential
- Economic benefits for resource exploration
- Societal relevance (Lombok population, hazard mitigation)
- Add dedicated "Broader Impacts and Applications" section

#### 9. Provide Practical Guidance ⭐
**Priority: MODERATE**

- Decision framework: when to use CHG vs. EHD, MDA, GGT
- Data quality requirements (station spacing, accuracy)
- How to recognize failure modes
- Quality control procedures
- Cost-benefit trade-offs

#### 10. Release Software/Code ⭐
**Priority: MODERATE**

- Provide Python/MATLAB implementation
- Include tutorial with examples
- Share synthetic model scripts
- Consider open-source software package
- Greatly enhances reproducibility and adoption

### Additional Improvements (Desirable)

#### 11. Improve Data Documentation
- Complete survey specifications
- Detailed processing workflow
- Data quality/uncertainty maps
- Regional/residual separation methodology

#### 12. Enhance Geological Interpretation
- Expected gravity signatures for interpreted features
- Forward modeling validation
- Alternative interpretations considered
- Interpretation confidence/uncertainty

#### 13. Strengthen Discussion Section
- Compare with other caldera gravity studies
- Discuss volcanic process implications
- Address limitations thoroughly
- Outline future research directions

#### 14. Improve Accessibility
- Plain-language summary for non-specialists
- Conceptual diagrams for key concepts
- Define technical terms when first used
- Flowchart showing CHG workflow

---

## Editorial Assessment and Recommendations

### Suitability for Journal of Geophysical Research: Solid Earth

**Current status:** **Not suitable in present form**

JGR: Solid Earth is a top-tier journal with high standards for:
- Methodological rigor
- Comprehensive validation
- Comparison with state-of-the-art
- Broader scientific impact

**Current manuscript gaps:**
- ❌ No comparison with advanced methods
- ❌ Insufficient validation (single field case)
- ❌ Limited broader impact discussion
- ❌ Presentation quality below journal standards

**Path to JGR acceptance:**
- Complete all "Essential" revisions (items 1-5)
- Complete most "Highly Desirable" revisions (items 6-10)
- Demonstrate clear advantages over existing methods
- Validate on multiple well-studied cases
- Expand broader impacts significantly

**Estimated additional work:** 6-12 months

### Alternative Venue Recommendations

If authors prefer faster publication with less extensive revisions, consider:

**Tier 1 (Moderate revisions):**
- **Geophysical Prospecting** - methodological focus, good fit
- **Journal of Applied Geophysics** - applied methods, practical emphasis
- Still require comparison with advanced methods and additional validation

**Tier 2 (Minor-moderate revisions):**
- **Journal of Volcanology and Geothermal Research** - application focus
- **Geophysical Journal International** - broad scope
- Emphasis on application rather than methodology

**Tier 3 (Minor revisions):**
- **Bulletin of Volcanology** - volcanic application emphasis
- **Geosciences** - open access, broad scope
- Focus on Samalas case study rather than method development

### Decision Rationale

**Why MAJOR REVISIONS rather than REJECT:**

✅ **Core novelty confirmed** - Genuine methodological innovation  
✅ **Sound mathematical framework** - No fundamental flaws  
✅ **Significant application** - Important caldera system  
✅ **Issues are addressable** - Additional work can resolve concerns  
✅ **Potential for impact** - Method could be useful if properly validated  

**Why not MINOR REVISIONS or ACCEPT:**

❌ **Critical comparison missing** - Cannot assess value without comparing to advanced methods  
❌ **Validation insufficient** - Single case inadequate for methods paper  
❌ **Noise concerns unresolved** - SNR degradation needs explanation/mitigation  
❌ **Presentation issues** - Abstract errors, missing tables, inadequate figures  
❌ **Broader impacts weak** - Doesn't demonstrate practical significance  

### Conditions for Acceptance

The revised manuscript must:

1. **Demonstrate clear advantages** over EHD, MDA, and GGT through quantitative comparison
2. **Validate on 3+ field cases** with independent structural control
3. **Resolve noise amplification** concerns with mitigation strategies
4. **Fix all presentation issues** (abstract errors, grammar, figures, tables)
5. **Expand broader impacts** to demonstrate practical significance

**If these conditions are met,** the paper could be a solid contribution to *Geophysical Prospecting* or *Journal of Applied Geophysics*, and potentially suitable for *JGR: Solid Earth* with exceptional execution.

**If authors cannot commit to this level of revision,** consider alternative venues (Tier 2-3 above) with more modest scope.

---

## Reviewer Recommendations Summary

| Aspect | Rev 1 | Rev 2 | Rev 3 | Consensus |
|--------|-------|-------|-------|-----------|
| **Overall Rating** | 6/10 | 5/10 | 5/10 | **5.3/10** |
| **Recommendation** | Major Rev | Major Rev | Major Rev | **MAJOR REVISIONS** |
| **Soundness** | 3/5 | 3/5 | 3/5 | **3/5** |
| **Presentation** | 3/5 | 4/5 | 3/5 | **3.3/5** |
| **Contribution** | 6/10 | 5/10 | 5/10 | **5.3/10** |
| **Confidence** | 5/5 | 5/5 | 4/5 | **4.7/5** |

**Unanimous positions:**
- ✅ Core concept is novel and interesting
- ✅ Mathematical framework is sound
- ❌ Comparison with advanced methods essential
- ❌ Field validation insufficient
- ❌ Presentation needs improvement
- ⚠️ Noise amplification is concerning

**Strong consensus:** All reviewers recommend **MAJOR REVISIONS** with similar required improvements.

---

## Timeline and Next Steps

### For Authors

**Recommended revision timeline:** 4-6 months minimum

**Priority order:**
1. **Months 1-2:** Implement comparison methods (EHD, MDA, GGT) and apply to all datasets
2. **Months 2-3:** Acquire/process 2-3 additional field cases; validate Samalas interpretation
3. **Months 3-4:** Address noise amplification; validate optimization; expand synthetic tests
4. **Months 4-5:** Improve presentation (fix errors, enhance figures, create tables, expand discussion)
5. **Month 6:** Final polishing, broader impacts expansion, software preparation

**Critical path:** Method comparison and field validation (items 1-2) are most time-consuming.

### Resubmission Requirements

**Cover letter must address:**
- How each reviewer concern was addressed
- Point-by-point response to all reviewer comments
- Justification for any recommendations not followed
- Summary of major changes and additions

**Revised manuscript must include:**
- Comprehensive method comparison (figures, tables, quantitative metrics)
- 2-3 additional validated field cases
- Resolution of noise amplification concerns
- All presentation issues fixed
- Expanded broader impacts discussion

**Supplementary materials should include:**
- Software/code for CHG implementation
- Synthetic model parameters and scripts
- Additional figures (sensitivity analysis, method comparison)
- Detailed processing workflows

### Editorial Decision

**DECISION: MAJOR REVISIONS REQUIRED**

This manuscript presents an interesting and potentially valuable methodological contribution, but substantial additional work is required before it can be accepted for publication. The core concept - center-referenced radial/tangential decomposition of horizontal gravity gradients - is genuinely novel and addresses a real interpretational challenge for circular anomalies. However, the paper currently lacks:

1. Comparison with state-of-the-art methods (most critical deficiency)
2. Sufficient field validation (single case inadequate)
3. Resolution of noise amplification concerns
4. Adequate presentation quality
5. Developed broader impacts discussion

All three expert reviewers agree that major revisions are required, with strong consensus on the specific improvements needed. The authors should carefully consider whether they can commit to the substantial additional work required (estimated 4-6 months minimum). If so, the revised manuscript could potentially be suitable for *JGR: Solid Earth* or, more likely, a specialized journal such as *Geophysical Prospecting* or *Journal of Applied Geophysics*.

**The manuscript will be reconsidered after major revisions addressing the reviewers' concerns.**

---

**Associate Editor**  
*Journal of Geophysical Research: Solid Earth*  
Date: 2024

---

## Appendix: Key References for Authors

### Methods for Comparison

1. **Fedi, M., & Florio, G. (2001).** Detection of potential fields source boundaries by enhanced horizontal derivative method. *Geophysical Prospecting*, 49(1), 40-58.

2. **Fedi, M. (2002).** Multiscale derivative analysis: A new tool to enhance detection of gravity source boundaries at various scales. *Geophysical Research Letters*, 29(2), 1-4.

3. **Yuan, Y., & Geng, M. (2014).** Directional total horizontal derivatives of gravity gradient tensor and their application to delineate the edges. *76th EAGE Conference & Exhibition*.

4. **Kusumoto, S. (2016).** Structural Analysis of Calderas by Semiautomatic Interpretation of the Gravity Gradient Tensor: A Case Study in Central Kyushu, Japan. *InTech Open*.

5. **Pham, L.T., et al. (2024).** Enhancement of the balanced total horizontal derivative of gravity data using the power law approach. *Geocarto International*.

### Samalas/Lombok Studies for Integration

6. **Lavigne, F., et al. (2013).** Source of the great A.D. 1257 mystery eruption unveiled, Samalas volcano, Rinjani Volcanic Complex, Indonesia. *PNAS*, 110(42), 16742-16747.

7. **Vidal, C.M., et al. (2015).** Dynamics of the major plinian eruption of Samalas in 1257 A.D. (Lombok, Indonesia). *Bulletin of Volcanology*, 77, 73.

8. **Sarjan, A.F.N., et al. (2021).** Delineation of Upper Crustal Structure Beneath the Island of Lombok, Indonesia, Using Ambient Seismic Noise Tomography. *Frontiers in Earth Science*, 9, 560428.

9. **Priyono, A., et al. (2021).** Seismic Attenuation Tomography From 2018 Lombok Earthquakes, Indonesia. *Frontiers in Earth Science*, 9, 639692.

10. **Hiden, et al. (2017).** The Isopach Mapping of Volcanic Deposits of Mount Samalas 1257 AD Based on the Values of Resistivity and Physical Properties. *Geosciences*, 7(3), 67.