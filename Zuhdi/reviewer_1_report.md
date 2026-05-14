# Reviewer 1 Report: Methods and Theory Specialist

## Summary

This manuscript introduces the Centered Horizontal Gravity Gradient (CHG) method, a novel gradient operator for interpreting circular or nearly circular gravity anomalies. The method decomposes horizontal gradients into radial (CHGrad) and tangential (CHGtan) components calculated from a specified center point, addressing limitations of the Total Horizontal Gradient (THG) method. The authors apply CHG to synthetic models and field data from the Samalas volcanic system in Lombok, Indonesia. While the conceptual innovation is valuable, the manuscript suffers from significant theoretical gaps, insufficient mathematical rigor, and incomplete methodological development that must be addressed before publication.

---

## Soundness: 2/5

The core concept is sound and represents a genuine contribution, but the mathematical development is incomplete and lacks rigor in several critical areas:

**Strengths in theoretical foundation:**
- The geometric decomposition of horizontal gradients into radial and tangential components is mathematically valid and logically motivated.
- The finite-difference approximations (Equations 3-6) follow standard practice for numerical gradient estimation.
- The transformation from Cartesian to polar-referenced gradients is conceptually correct.

**Critical theoretical deficiencies:**

1. **Mathematical Derivation Gaps:**
   - The transition from Equations 1-2 (defining CHGrad and CHGtan) to Equations 3-6 (finite-difference implementation) is not rigorously derived. The authors state these are "calculated using the finite difference method" but provide no derivation showing how the geometric definitions translate to the specific finite-difference formulas presented.
   - The relationship between the continuous gradient operators (∂g/∂x, ∂g/∂y) and their discrete approximations is not discussed. What is the truncation error? What order of accuracy do these formulas achieve?
   - The manuscript does not define the grid spacing (Δx, Δy) requirements or discuss how grid resolution affects accuracy.

2. **Singularity at the Center Point:**
   - Equations 1-2 contain terms with (x-xc) and (y-yc) in denominators. What happens when evaluating CHG at or near the center point (xc, yc)? The manuscript provides no discussion of this mathematical singularity.
   - Is there a minimum distance from the center point where CHG remains valid? This is critical for practical application but completely unaddressed.

3. **Error Analysis Absent:**
   - No error propagation analysis from observational uncertainties (Δg) to CHG values.
   - No discussion of how errors in center point location (Δxc, Δyc) affect results.
   - No analysis of numerical stability or sensitivity to grid spacing.
   - The statement that CHG "can clearly distinguish between gravity gradients in the radial and tangential directions" is qualitative and unsupported by quantitative error bounds.

4. **Incomplete Theoretical Justification:**
   - Why is the specific finite-difference scheme in Equations 3-6 optimal or appropriate? Have the authors considered higher-order schemes, central differences, or other numerical differentiation methods?
   - The hybrid THG-CHG formulation (Equations 7-9 with α and β parameters) appears ad hoc. What is the theoretical justification for this particular linear combination? How should α and β be chosen for different applications?
   - The manuscript claims CHG "preserves sign information" unlike THG, but does not formally prove or demonstrate the conditions under which radial vs. tangential gradients have positive or negative signs.

5. **Missing Assumptions and Limitations:**
   - What assumptions underlie the method? (e.g., smooth gravity field, isolated circular anomaly, known center location)
   - Under what conditions does the method fail or become unreliable?
   - How does the method perform for elliptical or irregular features that deviate from perfect circularity?

6. **Center Point Determination:**
   - The most critical methodological gap: How is the center point (xc, yc) determined? The manuscript states it is "estimated as the center point of a geological feature" but provides no objective method, algorithm, or criteria.
   - For synthetic data, the center is known a priori, but for real data (Samalas case), how was the center chosen? Visual inspection? Moment analysis? Iterative optimization?
   - How sensitive are the results to misspecification of the center point? This is a fundamental question for method reliability that is completely unaddressed.

7. **Lack of Formal Comparison:**
   - The manuscript does not mathematically compare CHG with existing directional derivative methods (e.g., Directional Total Horizontal Derivative - DTHD). Both methods provide direction-specific gradient information, but the theoretical relationship and relative advantages are not analyzed.
   - No formal comparison with gradient tensor methods (e.g., eigenvector analysis) that also provide directional information.

**Specific Technical Issues:**

- **Equation 1-2**: The notation is ambiguous. Are these definitions or computational formulas? The use of partial derivatives (∂g/∂x, ∂g/∂y) suggests continuous operators, but the subsequent finite-difference formulas suggest discrete approximations. This should be clarified.

- **Equations 3-6**: These appear to be forward-difference approximations, which are first-order accurate and introduce directional bias. Why not use central differences, which are second-order accurate and unbiased? This choice is not justified.

- **Equations 7-9**: The normalization factors in the hybrid formulation are not explained. Why are CHGrad and CHGtan normalized by their respective maxima before combining with THG? What effect does this have on the physical interpretation?

- **Section 2 (Method)**: The description jumps directly to formulas without establishing the theoretical framework. A proper derivation would start with the definition of horizontal gradient in polar coordinates, then show how to transform Cartesian derivatives, and finally derive the discrete approximations with error analysis.

**Recommendation for Theoretical Development:**

To achieve publication quality for *Computers and Geosciences*, the authors must:

1. Provide rigorous mathematical derivation from first principles to finite-difference implementation.
2. Include formal error analysis (truncation error, error propagation, sensitivity analysis).
3. Discuss singularity behavior near the center point and define valid application domain.
4. Develop objective method(s) for center point determination with validation.
5. Compare mathematically with directional derivative and tensor methods.
6. Clearly state all assumptions, approximations, and limitations.
7. Provide convergence analysis showing how CHG accuracy improves with grid refinement.

---

## Presentation: 3/5

**Positive aspects:**
- The manuscript is generally well-organized with clear section structure.
- The writing is mostly clear, though some grammatical errors exist (e.g., "Centered Horizontal Gravity Gradient" should perhaps be "Center-Referenced" for clarity).
- Figures appear to illustrate the concepts, though I cannot view them in the parsed text.

**Presentation deficiencies:**

1. **Mathematical Notation:**
   - Inconsistent notation between continuous (∂/∂x) and discrete (Δx) representations.
   - The subscript notation in Equations 3-6 (e.g., g(x+Δx, y)) should be clarified—is this g evaluated at position (x+Δx, y) or is it a grid point index?
   - The relationship between (x, y) coordinates and grid indices (i, j) is not established.

2. **Method Description:**
   - Section 2 is too brief and jumps to equations without adequate conceptual explanation.
   - The geometric intuition behind radial vs. tangential gradients could be explained more clearly before presenting formulas.
   - A schematic diagram showing the coordinate transformation from Cartesian (x, y) to center-referenced (r, θ) would significantly aid understanding.

3. **Results Presentation:**
   - The synthetic model description (Section 3) lacks sufficient detail. What are the exact density contrasts, dimensions, and depths of the modeled bodies?
   - The real data description (Section 4) provides geological context but insufficient information about data acquisition, processing, and quality.
   - Quantitative results are absent—all assessments are qualitative ("successfully highlights," "clearly distinguish").

4. **Figure Quality (from description in text):**
   - The manuscript mentions multiple figures but provides insufficient caption detail in the parsed text.
   - Figures should include quantitative information (color scales, contour values, coordinate systems).
   - Comparison figures should use identical color scales and ranges for fair comparison.

5. **Missing Technical Details:**
   - Grid spacing and resolution not specified for any examples.
   - Computational implementation details absent (programming language, software used, processing time).
   - Data preprocessing steps not described (filtering, continuation, reduction).

---

## Contribution: 3/5

**Originality:**

The CHG concept is genuinely novel. Based on extensive literature review (see novelty report), no existing published method explicitly decomposes horizontal gradients into radial and tangential components about a user-specified center point. This represents an original contribution to potential field interpretation methodology.

**Significance:**

The contribution is **moderately significant** with potential for higher impact if properly developed:

- **Positive aspects:**
  - Addresses a real limitation of THG for circular anomalies (though this limitation was not previously documented in literature).
  - Provides clearer geological interpretation for volcanic and caldera structures where radial and tangential features have distinct meanings.
  - Computationally simple and easy to implement.
  - Potentially useful for geothermal exploration, mineral exploration, and volcanic hazard assessment.

- **Limitations to significance:**
  - Narrow applicability: only useful for circular or nearly circular features.
  - Incremental rather than transformative: adds directional information to existing gradient analysis rather than fundamentally changing interpretation paradigms.
  - Unclear advantages over existing directional derivative methods (not compared).
  - Single case study limits demonstration of generalizability.

**Advancement of the field:**

The work makes a **modest advancement** in potential field interpretation techniques:

- It does not introduce new geophysical theory or physical principles.
- It does not develop new computational methods (finite differences are standard).
- It does provide a new geometric perspective that may prove useful for specific applications.
- It could become a standard tool for circular anomaly interpretation if properly validated.

**Comparison with state-of-the-art:**

The manuscript inadequately positions the work relative to recent developments:

- **Missing comparisons** with directional derivative methods (Yuan & Geng, 2014; Yuan et al., 2015; Ekinci et al., 2013; Mazzoldi et al., 2020).
- **No discussion** of gradient tensor methods (Kusumoto, 2016) that also provide directional/structural information.
- **Limited engagement** with enhanced/normalized THG variants (Pham et al., 2019; Nasuti et al., 2019) that address THG limitations through different approaches.

The contribution would be strengthened by:
1. Explicit comparison showing CHG outperforms or complements existing methods.
2. Multiple case studies demonstrating applicability across different geological settings.
3. Validation against independent data (seismic, drilling, geological mapping).
4. Open-source software implementation to facilitate adoption.

---

## Strengths

1. **Genuine Novelty**: The center-referenced radial/tangential decomposition is an original concept not found in existing literature. This represents a true methodological innovation.

2. **Clear Geometric Intuition**: The idea of separating gradients into components parallel and perpendicular to the direction from a center point is geometrically intuitive and physically meaningful for circular structures.

3. **Computational Simplicity**: The method requires only horizontal derivatives and a center point, making it easy to implement with standard geophysical software. No iterative optimization or complex numerical schemes are needed.

4. **Preservation of Sign Information**: Unlike THG (always positive), CHG preserves directional information through signed values, potentially enabling more nuanced interpretation.

5. **Relevant Application Domain**: The focus on volcanic and caldera structures addresses a geophysically important problem with practical implications for geothermal exploration and volcanic hazard assessment.

6. **Flexibility**: The hybrid formulation (Equations 7-9) allows users to blend CHG and THG, potentially offering interpretative flexibility.

7. **Appropriate Case Study**: The Samalas volcanic system is a well-studied, geologically relevant example with documented circular structures.

---

## Weaknesses

### Critical Weaknesses (Must be addressed):

1. **Incomplete Mathematical Derivation**: The transition from geometric definitions to finite-difference formulas lacks rigorous derivation. The manuscript presents formulas without showing how they are obtained or why they are appropriate.

2. **No Error Analysis**: Absence of truncation error estimates, error propagation analysis, or sensitivity studies. The reliability and accuracy of the method cannot be assessed without this.

3. **Undefined Center Point Determination**: The most critical methodological gap. No objective method is provided for determining the center point from data. This makes the method subjective and potentially unreproducible.

4. **Singularity Issues Unaddressed**: The mathematical behavior at or near the center point is not discussed. Equations 1-2 contain potential singularities that could cause numerical instability.

5. **No Comparison with Existing Methods**: Despite conceptual similarities with directional derivative methods, no comparison is provided. Readers cannot assess relative advantages or appropriate use cases.

6. **Single Case Study**: Only one real-world example is presented, limiting demonstration of generalizability and robustness across different geological settings.

7. **Lack of Validation**: No comparison with independent geophysical data (seismic, MT) or ground truth (drilling, geological mapping) to verify that CHG interpretations are correct.

8. **Missing Key Literature**: Directional derivative methods (Yuan & Geng, 2014; Yuan et al., 2015; Ekinci et al., 2013) and gradient tensor approaches (Kusumoto, 2016) are not cited or discussed, despite being highly relevant.

### Significant Weaknesses (Should be addressed):

9. **Insufficient Synthetic Testing**: The synthetic models are not described in sufficient detail. More comprehensive synthetic tests with known solutions would strengthen validation.

10. **No Quantitative Metrics**: All performance assessments are qualitative ("successfully highlights," "clearly distinguish"). Objective metrics (e.g., edge sharpness, signal-to-noise ratio, resolution) should be defined and calculated.

11. **Grid Spacing Not Specified**: The required grid resolution and its effect on accuracy are not discussed. This is critical practical information for users.

12. **Hybrid Formulation Unjustified**: The mixing of CHG and THG (Equations 7-9) appears ad hoc. The theoretical basis and optimal choice of α and β parameters are not established.

13. **Limited Scope Discussion**: The manuscript does not clearly delineate when CHG is appropriate vs. when other methods should be preferred. Guidance on applicability is needed.

14. **Numerical Implementation Details Missing**: Programming language, software, computational cost, and implementation challenges are not discussed.

### Minor Weaknesses:

15. **Grammatical Errors**: Some awkward phrasing and grammatical issues (e.g., "Centered Horizontal Gravity" vs. "Centered Horizontal Gravity Gradient" inconsistency in title vs. text).

16. **Notation Inconsistencies**: Mixing of continuous and discrete notation without clear distinction.

17. **Figure Captions**: Based on the text, figure captions may lack sufficient detail for standalone understanding.

18. **Data Availability**: No mention of whether data or code will be made available for reproducibility.

---

## Suggestions

### Essential for Acceptance:

1. **Provide Rigorous Mathematical Derivation**:
   - Start from first principles (gradient in polar coordinates).
   - Show step-by-step derivation of Equations 1-2 from geometric considerations.
   - Derive finite-difference formulas (Equations 3-6) with truncation error analysis.
   - Discuss why this particular discretization is chosen over alternatives.

2. **Develop Center Point Determination Method**:
   - Propose objective algorithm(s) for determining center point from gravity data.
   - Options could include: moment analysis, symmetry detection, iterative optimization to maximize CHG interpretability.
   - Test and validate the method on synthetic data with known centers.
   - Apply consistently to real data and document the procedure.

3. **Conduct Comprehensive Error Analysis**:
   - Derive truncation error for finite-difference approximations.
   - Perform error propagation from data uncertainties to CHG values.
   - Conduct sensitivity analysis: how do errors in center point location affect results?
   - Test numerical stability and convergence with grid refinement.

4. **Address Singularity Behavior**:
   - Analyze mathematical behavior of Equations 1-2 as (x,y) → (xc, yc).
   - Define minimum distance from center point where CHG is valid.
   - Propose regularization or alternative formulation if needed near the center.

5. **Compare with Directional Derivative Methods**:
   - Implement directional THD (Yuan & Geng, 2014) on the same datasets.
   - Provide side-by-side comparison showing relative advantages.
   - Discuss when CHG is preferable vs. when DTHD is preferable.
   - Mathematically relate the two approaches.

6. **Add Multiple Case Studies**:
   - Include at least 1-2 additional real-world examples from different geological settings.
   - Demonstrate that the method works for various circular structures (calderas, intrusions, impact craters).
   - Show examples of method limitations or failure cases.

7. **Validate with Independent Data**:
   - For at least one case study, compare CHG interpretation with independent constraints (seismic, MT, drilling, geological mapping).
   - Show that CHG-identified features correspond to known geological structures.

### Highly Recommended:

8. **Expand Synthetic Testing**:
   - Create comprehensive suite of synthetic models with varying:
     - Degrees of circularity (perfect circles to ellipses to irregular shapes)
     - Radial vs. tangential density variations
     - Depth ranges
     - Multiple overlapping anomalies
   - Document model parameters completely.
   - Use synthetic tests to establish method capabilities and limitations.

9. **Define Quantitative Metrics**:
   - Develop objective measures of CHG performance (e.g., edge sharpness index, feature separation metric).
   - Apply consistently across all examples.
   - Use metrics to objectively compare with other methods.

10. **Provide Implementation Guidance**:
    - Specify grid spacing requirements (e.g., at least X points per anomaly wavelength).
    - Discuss data quality and preprocessing requirements.
    - Provide workflow diagram showing steps from raw data to CHG interpretation.
    - Include discussion of computational cost and efficiency.

11. **Justify Hybrid Formulation**:
    - Provide theoretical basis for combining CHG and THG (Equations 7-9).
    - Develop guidelines for choosing α and β parameters.
    - Show examples demonstrating the utility of the hybrid approach.

12. **Expand Literature Review**:
    - Cite and discuss directional derivative methods comprehensively.
    - Include gradient tensor methods in the discussion.
    - Position CHG clearly relative to these existing approaches.
    - Create comparison table summarizing methods, advantages, and use cases.

### Recommended Enhancements:

13. **Extend Theoretical Discussion**:
    - Discuss relationship to polar coordinate systems and vector calculus.
    - Consider extension to 3D gradient tensors or gradiometry data.
    - Explore potential application to magnetic data.

14. **Add Schematic Diagrams**:
    - Create conceptual diagram showing radial vs. tangential gradient components.
    - Illustrate coordinate transformation from Cartesian to center-referenced system.
    - Show finite-difference stencil used for gradient calculation.

15. **Improve Figure Presentation**:
    - Ensure all figures have detailed, self-contained captions.
    - Use consistent color scales and ranges for comparisons.
    - Add quantitative annotations (contour values, scale bars, coordinates).
    - Include difference maps showing CHG advantages over THG.

16. **Discuss Limitations and Future Work**:
    - Clearly state when CHG is appropriate vs. inappropriate.
    - Acknowledge limitations (circular features only, center point required, etc.).
    - Suggest future research directions (extension to 3D, automation, machine learning integration).

17. **Provide Software and Data**:
    - Make code implementation available (e.g., GitHub repository).
    - Provide sample datasets for testing.
    - Include documentation and usage examples.

---

## Questions for Authors

1. **Mathematical Derivation**: Can you provide a rigorous step-by-step derivation showing how Equations 3-6 are obtained from Equations 1-2? What is the truncation error of your finite-difference scheme?

2. **Center Point Determination**: What specific procedure did you use to determine the center point for the Samalas case study? Can you propose an objective, reproducible method that could be applied by other researchers?

3. **Singularity Behavior**: How do Equations 1-2 behave at the center point (xc, yc) where the denominators become zero? Is there a minimum distance from the center where CHG should not be evaluated?

4. **Comparison with DTHD**: How does CHG differ mathematically from Directional Total Horizontal Derivative (DTHD) methods? What are the relative advantages of each approach?

5. **Error Sensitivity**: How sensitive are CHG results to errors in center point location? If the center is misspecified by 1 km, how does this affect the radial and tangential gradient patterns?

6. **Grid Resolution**: What grid spacing is required for accurate CHG calculation? How does CHG accuracy depend on the ratio of grid spacing to anomaly wavelength?

7. **Validation**: For the Samalas case study, are there independent geophysical or geological data that confirm the CHG-identified features (caldera boundaries, pyroclastic flows)?

8. **Finite-Difference Choice**: Why did you choose forward differences (Equations 3-6) rather than central differences, which are more accurate and unbiased? Have you tested alternative discretization schemes?

9. **Hybrid Parameters**: How should users choose the α and β parameters in Equations 7-9? Is there an optimal strategy or does it depend on the application?

10. **Applicability Limits**: How circular must an anomaly be for CHG to be useful? Have you tested CHG on elliptical or irregular features?

11. **Computational Cost**: What is the computational cost of CHG compared to THG? Are there any efficiency considerations for large datasets?

12. **Extension to 3D**: Could CHG be extended to work with full gradient tensor data or 3D gravity gradiometry? What modifications would be needed?

---

## Rating: 4/10 (Reject, but encourage major revision and resubmission)

**Justification:**

The manuscript presents a genuinely novel and potentially valuable methodological contribution (center-referenced radial/tangential gradient decomposition for circular anomalies). However, it suffers from critical deficiencies in mathematical rigor, theoretical development, and validation that prevent recommendation for publication in its current form.

**Key reasons for rejection:**

1. **Incomplete mathematical foundation**: Lack of rigorous derivation, error analysis, and treatment of singularities makes the method's reliability and accuracy unclear.

2. **Undefined methodology**: The absence of an objective center point determination method is a fundamental gap that makes the approach subjective and potentially unreproducible.

3. **Insufficient validation**: A single case study without independent verification and no comparison with existing methods provides inadequate evidence of the method's utility and advantages.

4. **Missing literature engagement**: Failure to cite and compare with highly relevant directional derivative and gradient tensor methods leaves the work poorly positioned within the field.

**Recommendation:**

I recommend **rejection with encouragement to revise and resubmit** after addressing the critical issues outlined above. With substantial additional work—particularly rigorous mathematical development, objective center point determination, comprehensive error analysis, comparison with existing methods, and additional case studies—this could become a strong contribution worthy of publication in *Computers and Geosciences*.

The core idea is sound and original, but the execution needs significant strengthening to meet the standards of a leading geophysics methods journal.

---

## Confidence: 4/5 (High Confidence)

I am confident in this assessment based on:

1. **Expertise in potential field methods**: I have thorough knowledge of gravity and magnetic gradient techniques, including THG, analytic signal, and directional derivatives.

2. **Mathematical background**: I can assess the rigor and completeness of the mathematical development, and I have identified specific gaps and deficiencies.

3. **Literature knowledge**: I have reviewed 188 relevant papers (2000-2025) and can confidently state that the CHG concept is novel but that important related work is not cited.

4. **Practical experience**: I understand the practical requirements for implementing and validating geophysical methods.

**Slight uncertainty (4/5 rather than 5/5) stems from:**
- I cannot view the figures directly, so my assessment of visual results is based on textual descriptions.
- Detailed numerical testing would be needed to fully verify the mathematical concerns I've raised.
- The authors may have additional information or justifications not included in the manuscript that could address some concerns.

Nevertheless, I am highly confident that the identified weaknesses are real and must be addressed for publication.
