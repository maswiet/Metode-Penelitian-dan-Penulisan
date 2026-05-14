# Meta-Review and Editorial Decision

## Manuscript Information

**Title**: Centered Horizontal Gravity Gradient (CHG): An Improved Operator for Interpreting Circular Gravity Anomalies

**Authors**: Muhammad Zuhdi, Wiwit Suryanto, Sudarmadji

**Affiliation**: Geophysics Department, Faculty of Mathematics and Natural Sciences, Gadjah Mada University, Indonesia

**Target Journal**: Computers and Geosciences

**Manuscript Type**: PhD student manuscript (Methods paper)

---

## Summary of Reviewer Assessments

Three independent reviewers with complementary expertise have evaluated this manuscript:

- **Reviewer 1 (Methods & Theory Specialist)**: Rating 4/10, Confidence 4/5
- **Reviewer 2 (Experiments & Practical Impact Specialist)**: Rating 4/10, Confidence 4/5
- **Reviewer 3 (Clarity, Positioning & Broader Impact Specialist)**: Rating 4/10, Confidence 4/5

All three reviewers reached the same conclusion: **Reject, but encourage major revision and resubmission**.

### Reviewer Scores Summary

| Aspect | Reviewer 1 | Reviewer 2 | Reviewer 3 | Average |
|--------|------------|------------|------------|---------|
| Soundness | 2/5 | 2/5 | 3/5 | 2.3/5 |
| Presentation | 3/5 | 3/5 | 2/5 | 2.7/5 |
| Contribution | 3/5 | 3/5 | 3/5 | 3.0/5 |
| Overall Rating | 4/10 | 4/10 | 4/10 | 4/10 |

---

## Consensus Strengths

All three reviewers acknowledged the following strengths:

### 1. Genuine Conceptual Novelty
The center-referenced radial/tangential gradient decomposition is an **original contribution** not found in existing literature. Based on comprehensive literature review (188 papers, 2000-2025), no published method explicitly decomposes horizontal gradients into radial and tangential components about a user-specified center point. This represents a true methodological innovation.

### 2. Clear Geometric Intuition
The idea of separating gradients into components parallel (radial) and perpendicular (tangential) to the direction from a center point is geometrically intuitive and physically meaningful for circular structures. This aligns well with how geologists think about volcanic calderas, ring complexes, and other circular features.

### 3. Relevant Application Domain
The focus on volcanic and caldera structures addresses important practical problems:
- Geothermal resource assessment (renewable energy)
- Volcanic hazard assessment (public safety)
- Understanding volcanic evolution (scientific knowledge)
- Mineral exploration around ring complexes (economic value)

### 4. Computational Simplicity
The method requires only horizontal derivatives and a center point, making it easy to implement with standard geophysical software. No iterative optimization or complex numerical schemes are needed, which could facilitate practical adoption.

### 5. Preservation of Directional Information
Unlike THG (which is always positive), CHG preserves sign information through signed values, potentially enabling more nuanced interpretation of gradient directions and magnitude changes.

### 6. Appropriate Case Study
The Samalas volcanic system (Lombok, Indonesia) is a well-studied, geologically significant example with documented circular structures, making it a suitable test case.

---

## Critical Weaknesses: Areas of Complete Agreement

All three reviewers identified the following **critical deficiencies** that must be addressed:

### 1. Inadequate Literature Positioning (All Reviewers - Critical)

**The Problem:**
The manuscript fails to cite and discuss highly relevant existing methods, particularly:

- **Directional derivative methods** (Yuan & Geng, 2014; Yuan et al., 2015; Ekinci et al., 2013; Mazzoldi et al., 2020): These methods also provide direction-specific gradient information and are conceptually most similar to CHG.
- **Gradient tensor methods** (Kusumoto, 2016): Specifically addresses caldera interpretation using gravity gradient tensors, directly relevant to the Samalas case.
- **Enhanced THG variants** (Pham et al., 2019; Nasuti et al., 2019; Nguyen et al., 2024): Address THG limitations through different approaches.

**Impact:**
Without comparison to these methods, readers cannot assess:
- Whether CHG is fundamentally different or a variation on existing approaches
- What unique advantages CHG offers over directional derivatives
- When CHG is preferable to other methods
- How CHG fits within the broader landscape of edge detection techniques

**Required Action:**
- Add comprehensive literature review covering directional derivatives and gradient tensor methods
- Explicitly compare CHG with directional THD mathematically and experimentally
- Clearly articulate what is novel about CHG relative to these existing approaches
- Position CHG within the full spectrum of potential field interpretation methods

### 2. Undefined Center Point Determination (All Reviewers - Critical)

**The Problem:**
The manuscript provides **no objective method** for determining the center point (xc, yc), which is fundamental to the CHG calculation. The text states it is "estimated as the center point of a geological feature" but provides no algorithm, criteria, or procedure.

**Impact:**
- The method becomes **subjective** and dependent on user judgment
- Results are potentially **unreproducible** by other researchers
- Reliability and accuracy cannot be assessed without knowing center point sensitivity
- Practical application is hindered by lack of guidance

**Required Action:**
- Develop objective algorithm(s) for center point determination (e.g., moment analysis, symmetry detection, iterative optimization)
- Document exactly how the center point was determined for the Samalas case study
- Test sensitivity to center point location (how do results change if center is mislocated by 1 km, 2 km, 5 km?)
- Provide clear guidelines for users on center point selection

### 3. Incomplete Mathematical Development (Reviewer 1 - Critical; Reviewers 2 & 3 - Significant)

**The Problem:**
The mathematical presentation lacks rigor in several areas:

- **No derivation**: The transition from geometric definitions (Equations 1-2) to finite-difference formulas (Equations 3-6) is not rigorously derived
- **No error analysis**: Truncation error, error propagation, and numerical accuracy are not discussed
- **Singularity unaddressed**: Behavior at or near the center point (where denominators → 0) is not analyzed
- **Assumptions unstated**: What conditions must hold for CHG to be valid?
- **Grid spacing not specified**: Required resolution for accurate results not discussed

**Impact:**
- The method's reliability and accuracy are unclear
- Users don't know how fine a grid is needed
- Potential numerical instabilities near the center are not addressed
- The theoretical foundation appears incomplete

**Required Action:**
- Provide rigorous step-by-step derivation from geometric principles to discrete formulas
- Include truncation error analysis and convergence testing
- Discuss singularity behavior and define valid application domain (minimum distance from center)
- State all assumptions explicitly
- Specify grid spacing requirements

### 4. Insufficient Experimental Validation (Reviewer 2 - Critical; Reviewers 1 & 3 - Significant)

**The Problem:**
The experimental validation is inadequate for a methods paper:

- **Synthetic tests lack detail**: Model parameters not quantitatively specified; no noise added; limited range of scenarios
- **Real data poorly described**: No information on data acquisition, processing, or quality
- **Single case study**: Only Samalas example; insufficient to demonstrate generalizability
- **No baseline comparisons**: CHG compared only with basic THG, not with other edge detection methods
- **No validation**: CHG interpretations not verified against independent data (geological maps, seismic, drilling)
- **Only qualitative assessment**: No quantitative performance metrics defined or calculated

**Impact:**
- Cannot assess whether CHG actually outperforms or complements existing methods
- Cannot verify that CHG interpretations are correct
- Cannot determine method robustness across different scenarios
- Cannot objectively evaluate method performance

**Required Action:**
- Expand synthetic testing with complete model specifications, noise analysis, and diverse scenarios
- Provide full description of real data (acquisition, processing, quality)
- Add at least 1-2 additional case studies from different geological settings
- Compare quantitatively with multiple edge detection methods (especially directional THD)
- Validate interpretations against independent geological/geophysical data
- Define and calculate objective performance metrics

### 5. Poor Presentation Quality (Reviewer 3 - Critical; Reviewers 1 & 2 - Significant)

**The Problem:**
The manuscript has significant presentation issues:

- **Writing quality**: Numerous grammatical errors, inconsistent terminology, awkward phrasing
- **Structural problems**: No proper Conclusions section; brief Method and Discussion sections; abrupt transitions
- **Missing elements**: No schematic diagrams, no workflow guidance, no comparison tables
- **Inadequate Introduction**: Too brief; doesn't thoroughly review existing methods; doesn't clearly state objectives
- **Weak Discussion**: Too brief; doesn't critically evaluate limitations; doesn't provide practical guidance

**Impact:**
- Clarity and understanding are significantly impeded
- The contribution is not compellingly presented
- Readers lack guidance on when and how to apply the method
- The manuscript doesn't meet presentation standards for a leading journal

**Required Action:**
- Thoroughly edit for grammar, consistency, and clarity
- Expand Introduction with comprehensive literature review and clear statement of objectives
- Expand Method section with conceptual explanation, schematic diagrams, and implementation guidance
- Expand Discussion with critical evaluation, comparison with existing methods, and practical considerations
- Add proper Conclusions section summarizing findings and implications
- Add visual aids (schematic diagrams, workflow charts, comparison tables)

---

## Significant Weaknesses: Areas of Strong Agreement

### 6. No Quantitative Performance Metrics (All Reviewers - Significant)

All assessments are qualitative ("successfully highlights," "clearly distinguish"). No objective metrics are defined or calculated (e.g., edge sharpness, localization accuracy, signal-to-noise ratio, feature separation index). This makes objective evaluation impossible.

**Required:** Define quantitative metrics and apply them to all test cases and comparison methods.

### 7. No Comparison with Directional Derivative Methods (All Reviewers - Significant)

Despite conceptual similarities, CHG is not compared with directional total horizontal derivative (DTHD) methods. This is the most important missing comparison.

**Required:** Implement directional THD on the same datasets and provide detailed quantitative and qualitative comparison.

### 8. Insufficient Synthetic Testing (All Reviewers - Significant)

Synthetic models lack detail and realism. No noise added. Limited range of scenarios (only idealized circular models; no elliptical, irregular, or overlapping features tested).

**Required:** Comprehensive synthetic test suite with full specifications, noise analysis, and diverse scenarios including non-ideal cases.

### 9. Missing Validation with Ground Truth (All Reviewers - Significant)

CHG interpretations are not verified against independent data. For Samalas, no comparison with published geological maps or geophysical models despite extensive prior work (Lavigne et al., 2013; Mutaqin et al., 2019; Malawani et al., 2022).

**Required:** Compare CHG interpretations with known geological features and published models for at least one case study.

### 10. No Sensitivity Analysis (Reviewers 1 & 2 - Significant)

Sensitivity to center point location, grid spacing, and noise level is not tested. Method robustness is unknown.

**Required:** Systematic sensitivity testing for key parameters.

---

## Areas of Partial Agreement or Differing Emphasis

### Hybrid THG-CHG Formulation (Equations 7-9)

- **Reviewer 1**: Questions theoretical justification; considers it ad hoc
- **Reviewer 2**: Notes it's introduced but not tested or validated
- **Reviewer 3**: Mentions it as offering flexibility but lacking guidance

**Consensus**: The hybrid formulation needs better justification and guidelines for choosing α and β parameters, or should be de-emphasized if not essential.

### Scope and Applicability

- **Reviewer 1**: Emphasizes narrow scope (circular features only) as limiting significance
- **Reviewer 2**: Notes limited applicability but sees potential if properly validated
- **Reviewer 3**: Questions whether elliptical/irregular features have been tested

**Consensus**: The method's scope limitations should be clearly stated, and behavior on non-circular features should be tested and documented.

### Software and Reproducibility

- **Reviewer 1**: Notes missing code/software availability
- **Reviewer 2**: Emphasizes this as critical for adoption
- **Reviewer 3**: Frames it as an ethical/open science consideration

**Consensus**: Code should be made available, and full reproducibility information should be provided.

---

## Novelty and Impact Assessment

### Novelty: Confirmed Original Contribution

Based on comprehensive literature review (188 papers, 2000-2025) and all three reviewers' assessments:

**The CHG concept is genuinely novel.** No existing published method explicitly decomposes horizontal gradients into radial and tangential components about a user-specified center point.

**However:**
- The relationship to directional derivative methods needs clarification
- The novelty must be more clearly articulated in the manuscript
- The mathematical development (finite-difference implementation) is standard; novelty is conceptual

### Significance: Moderate Potential, Insufficiently Demonstrated

**Potential significance**: Moderate to High
- Relevant for important applications (geothermal, volcanic hazards, mineral exploration)
- Could become a standard tool for circular anomaly interpretation
- Computationally simple and potentially easy to adopt

**Current demonstrated significance**: Low to Moderate
- Single case study limits demonstration of generalizability
- No validation against ground truth
- No comparison showing advantages over existing methods
- Unclear when CHG is preferable to other approaches

**To achieve high significance:**
- Multiple validated case studies needed
- Quantitative demonstration of advantages over existing methods required
- Practical guidelines for application must be provided
- Software implementation should be released

### Advancement of the Field: Incremental but Valuable

The work represents an **incremental but potentially valuable advancement**:

- **Not transformative**: Doesn't fundamentally change interpretation paradigms or introduce new physical principles
- **Not computationally innovative**: Uses standard finite-difference methods
- **But fills a gap**: Provides a geometrically intuitive, application-specific tool for circular anomalies
- **Complements existing methods**: Adds information rather than replacing other techniques

With proper development, validation, and positioning, CHG could become a useful addition to the geophysicist's toolkit for volcanic and geothermal applications.

---

## Detailed Recommendations for Revision

### Priority 1: Critical Issues (Must be fully addressed)

1. **Comprehensive Literature Review and Positioning**
   - Add thorough review of directional derivative methods with citations
   - Add discussion of gradient tensor methods
   - Clearly articulate what is novel about CHG compared to these approaches
   - Explain when CHG is preferable vs. when other methods should be used

2. **Objective Center Point Determination Method**
   - Develop and present algorithm for center point determination
   - Document procedure used for Samalas case
   - Test sensitivity to center point location systematically
   - Provide guidelines for users

3. **Rigorous Mathematical Development**
   - Provide complete derivation from geometric principles to discrete formulas
   - Include error analysis (truncation error, error propagation)
   - Discuss singularity behavior near center point
   - State all assumptions explicitly
   - Specify grid spacing requirements

4. **Comprehensive Experimental Validation**
   - Expand synthetic testing (full specifications, noise, diverse scenarios)
   - Provide complete real data description (acquisition, processing, quality)
   - Add 1-2 additional case studies
   - Validate against independent data for at least one case
   - Define and calculate quantitative performance metrics

5. **Quantitative Comparison with Existing Methods**
   - Implement directional THD on same datasets (essential comparison)
   - Apply other edge detection methods (analytic signal, tilt angle)
   - Present side-by-side quantitative comparisons
   - Discuss relative advantages and appropriate use cases

6. **Major Presentation Improvements**
   - Expand Introduction with thorough background and clear objectives
   - Expand Method section with conceptual explanation and implementation guidance
   - Add schematic diagrams illustrating the concept
   - Expand Discussion with critical evaluation and practical guidance
   - Add proper Conclusions section
   - Thoroughly edit for grammar, consistency, and clarity

### Priority 2: Important Enhancements (Should be addressed)

7. **Sensitivity and Robustness Testing**
   - Systematic sensitivity analysis (center point, grid spacing, noise)
   - Test on elliptical and irregular features
   - Document failure modes and limitations

8. **Practical Guidelines**
   - Step-by-step workflow for applying CHG
   - Guidelines for grid resolution, data quality, center point determination
   - Decision criteria for when to use CHG vs. other methods

9. **Additional Visual Aids**
   - Workflow diagram
   - Comparison tables (CHG vs. other methods)
   - Model parameter tables
   - Enhanced figures with quantitative annotations

10. **Reproducibility Package**
    - Specify all parameters for reproducing results
    - Provide code implementation (ideally open source)
    - State data availability or provide sample datasets
    - Include detailed workflow description

### Priority 3: Recommended Additions (Would strengthen manuscript)

11. **Extended Discussion**
    - Broader context within potential field interpretation
    - Implications for volcanic and geothermal exploration
    - Future research directions
    - Potential extensions (magnetic data, 3D tensors)

12. **Supplementary Materials**
    - Detailed model specifications
    - Additional test cases
    - Extended methodology
    - Code and documentation

13. **Broader Impact Considerations**
    - Data and code sharing plans
    - Accessibility considerations
    - Potential for misuse and how to avoid it

---

## Editorial Decision

### **REJECT with strong encouragement for major revision and resubmission**

### Justification

This manuscript presents a **genuinely novel and potentially valuable methodological contribution** to potential field interpretation. The concept of center-referenced radial/tangential gradient decomposition is original, geometrically intuitive, and addresses a real need in volcanic and geothermal geophysics.

**However, the manuscript in its current form has critical deficiencies that prevent acceptance:**

1. **Inadequate positioning** relative to existing literature, particularly directional derivative methods
2. **Undefined methodology** for the critical step of center point determination
3. **Incomplete mathematical development** lacking rigor, error analysis, and treatment of singularities
4. **Insufficient experimental validation** with only one case study, no independent verification, and no quantitative comparisons
5. **Poor presentation quality** with significant writing, structural, and organizational issues

**These are not minor issues that can be addressed through revision of the current manuscript.** The manuscript requires substantial additional work:

- Extensive literature review and comparative analysis
- Development of objective center point determination method
- Rigorous mathematical derivation and error analysis
- Comprehensive synthetic testing and multiple real-world case studies
- Quantitative comparison with existing methods, especially directional derivatives
- Validation against independent data
- Major rewriting of all sections for clarity and completeness

**The amount of work required constitutes a major revision that goes well beyond what can be accomplished in a typical revision cycle.**

### Recommendation

**Reject the current submission** but **strongly encourage the authors to undertake the major revisions outlined above and resubmit as a new manuscript.**

**Reasons for encouragement:**

1. **The core concept is novel and valuable** – no existing method provides this specific capability
2. **The application domain is important** – volcanic and geothermal systems have high practical and societal relevance
3. **The approach is computationally simple** – potential for wide adoption if properly validated
4. **The authors have made a good start** – the Samalas case study provides a foundation to build upon

**What success would look like:**

A revised manuscript that:
- Clearly positions CHG within the landscape of edge detection methods, especially relative to directional derivatives
- Provides objective, reproducible center point determination
- Includes rigorous mathematical development with error analysis
- Presents comprehensive validation with 3+ case studies verified against ground truth
- Demonstrates quantitatively that CHG provides unique or superior information compared to existing methods
- Offers clear practical guidance for when and how to apply CHG
- Is clearly written with high-quality figures and comprehensive documentation
- Includes open-source code implementation

**Such a manuscript would be a strong contribution worthy of publication in *Computers and Geosciences* and would likely have significant impact in the volcanic and geothermal geophysics community.**

---

## Timeline and Process Recommendations

### For the Authors

**Estimated time for major revision: 6-12 months**

This timeline assumes:
- 2-3 months: Literature review, comparative analysis, mathematical development
- 2-3 months: Additional synthetic testing and case studies
- 2-3 months: Data analysis, validation, quantitative comparisons
- 1-2 months: Writing, figure preparation, code documentation
- 1 month: Internal review and editing

**Recommended steps:**

1. **Months 1-2**: Comprehensive literature review; mathematical derivation and error analysis; center point determination method development

2. **Months 3-4**: Extensive synthetic testing; implementation of comparison methods (directional THD, analytic signal, etc.)

3. **Months 5-6**: Additional case studies (2-3 more examples); validation against independent data

4. **Months 7-8**: Quantitative analysis and comparison; sensitivity testing; robustness analysis

5. **Months 9-10**: Complete rewriting of manuscript with expanded sections; figure preparation; code documentation

6. **Months 11-12**: Internal review; editing; preparation of supplementary materials; submission

**Consider:**
- Collaborating with researchers who have expertise in directional derivative or gradient tensor methods
- Seeking additional case study data from colleagues working in other volcanic/geothermal systems
- Having the manuscript professionally edited before resubmission
- Preparing code for open-source release (e.g., GitHub repository)

### For the Editorial Process

**Recommendation for resubmission:**
- Treat as a **new submission** rather than a revision
- Fresh peer review process (though previous reviews should be considered)
- Authors should include a cover letter explaining how they addressed the major issues raised

**Potential for acceptance:**
If the authors successfully address the critical issues outlined above, the revised manuscript would have **strong potential for acceptance**. The core contribution is solid; it needs proper development, validation, and presentation.

---

## Specific Guidance for PhD Student and Advisors

This manuscript represents a PhD student's work, which provides context for both its strengths (novel thinking, fresh perspective) and weaknesses (incomplete development, limited experience with methods papers).

### For Muhammad Zuhdi (PhD Student)

**Congratulations on developing a genuinely novel concept!** This is a real achievement and the foundation for a strong methods paper. The work needed now is to:

1. **Develop the method more completely** – move from initial concept to fully validated technique
2. **Position it properly** – show how it relates to and improves upon existing methods
3. **Validate rigorously** – demonstrate that it works across multiple cases and provides advantages over alternatives
4. **Present clearly** – communicate the work effectively to the geophysics community

**This is normal for PhD research.** Initial ideas need substantial development before publication. Use the detailed reviewer feedback as a roadmap for strengthening your work.

**Consider this an opportunity:**
- To deepen your understanding of edge detection methods
- To develop skills in rigorous validation and comparison
- To improve your scientific writing
- To create a stronger publication that will have more impact

### For Wiwit Suryanto and Sudarmadji (Advisors)

**Recommendations:**

1. **Literature Review**: Help Muhammad conduct a comprehensive review of directional derivative methods and gradient tensor approaches. Consider reaching out to authors of key papers (Yuan, Ekinci, Kusumoto) for insights.

2. **Collaborative Comparison**: Consider collaborating with researchers experienced in directional derivatives to ensure fair and accurate comparison.

3. **Additional Case Studies**: Leverage your network to obtain gravity data from other volcanic/geothermal systems (Merapi, Krakatau, Toba, other Indonesian examples) for validation.

4. **Mathematical Development**: Work with Muhammad to develop the rigorous mathematical derivation and error analysis. Consider consulting with a numerical methods specialist if needed.

5. **Writing Support**: Consider engaging a professional scientific editor to help with English language and presentation quality.

6. **Publication Strategy**: Consider whether to:
   - Submit to *Computers and Geosciences* after major revision (high-impact but high standards)
   - Submit to a more specialized journal first (e.g., *Geophysical Prospecting*, *Journal of Applied Geophysics*) to build publication record
   - Split into two papers: (1) method development and synthetic testing; (2) applications to Indonesian volcanic systems

7. **Open Science**: Encourage Muhammad to develop open-source code and share data where possible. This will increase impact and citations.

### Positive Aspects to Build On

Despite the critical feedback, there are strong positives:

- **Novel concept** – this is the hardest part and Muhammad has achieved it
- **Clear application domain** – volcanic and geothermal systems are important and well-defined
- **Good initial case study** – Samalas is appropriate and well-studied
- **Computational simplicity** – the method is implementable and practical
- **Enthusiasm and motivation** – evident in the work

**With dedicated effort over the next 6-12 months, this can become a strong publication that makes a real contribution to the field.**

---

## Final Summary

**Decision**: **REJECT with strong encouragement for major revision and resubmission**

**Core Message**: The CHG method is a genuinely novel and potentially valuable contribution, but the manuscript requires substantial additional work in mathematical development, experimental validation, comparative analysis, and presentation before it meets publication standards for *Computers and Geosciences*.

**Key Actions Required**:
1. Position relative to directional derivative methods with quantitative comparison
2. Develop objective center point determination method
3. Provide rigorous mathematical derivation with error analysis
4. Expand validation with multiple case studies and ground truth verification
5. Define and calculate quantitative performance metrics
6. Substantially improve presentation quality throughout

**Potential After Revision**: **High** – With proper development, this could become a strong methodological contribution with significant impact in volcanic and geothermal geophysics.

**Timeline**: 6-12 months for major revision

**Recommendation**: The authors should view this as an opportunity to strengthen their work substantially and create a publication that will have lasting impact in the field.

---

## Meta-Review Prepared By

**Date**: [Current Date]

**Process**: Three independent expert reviewers with complementary expertise (methods/theory, experiments/practice, clarity/positioning) conducted thorough evaluations. This meta-review synthesizes their assessments, identifies areas of consensus and disagreement, and provides a unified editorial decision with detailed guidance for revision.

**Comprehensive Literature Review**: 188 papers (2000-2025) across edge detection methods, circular structure interpretation, and volcanic/caldera geophysics were reviewed to assess novelty and positioning.

**Confidence in Decision**: **High** – All three reviewers reached the same conclusion independently, with strong agreement on critical issues and consistent ratings across all evaluation criteria.
