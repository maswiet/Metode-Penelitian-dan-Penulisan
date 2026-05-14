# Reviewer 2 Report: Experiments and Practical Impact Specialist

## Summary

This manuscript proposes the Centered Horizontal Gravity Gradient (CHG) method for interpreting circular gravity anomalies, with applications to volcanic and caldera structures. The authors test CHG on synthetic models and apply it to gravity data from the Samalas volcanic system in Lombok, Indonesia. While the practical motivation is clear and the application domain is relevant, the manuscript suffers from insufficient experimental validation, inadequate description of datasets and processing methods, lack of quantitative performance metrics, and absence of comparative analysis with existing techniques. The experimental design and validation are insufficient for a methods paper in a journal of Computers and Geosciences' caliber.

---

## Soundness: 2/5

From an experimental and practical validation perspective, the manuscript has significant deficiencies:

**Experimental Design Issues:**

1. **Synthetic Model Testing - Inadequate**:
   - The synthetic models are mentioned but not described in sufficient detail. What are the exact:
     - Density contrasts (Δρ)?
     - Body dimensions (radii, thicknesses)?
     - Burial depths?
     - Background field characteristics?
   - No specification of grid parameters (spacing, extent, resolution).
   - No discussion of forward modeling method used to generate synthetic gravity data.
   - No noise added to synthetic data to test robustness—real gravity data always contains noise.
   - The synthetic tests appear limited to idealized circular models. What about:
     - Elliptical features?
     - Irregular shapes?
     - Multiple overlapping anomalies?
     - Regional trends superimposed on local anomalies?

2. **Real Data Description - Insufficient**:
   - **Data acquisition**: No information about:
     - Survey design (station spacing, coverage area, number of stations)
     - Instrumentation (gravimeter type, precision)
     - Survey date and duration
     - Measurement protocols (repeat stations, drift corrections)
   - **Data quality**: No assessment of:
     - Measurement uncertainties
     - Data completeness (gaps in coverage?)
     - Repeatability or closure errors
   - **Processing steps**: No description of:
     - Terrain corrections (critical in volcanic terrain!)
     - Free-air and Bouguer corrections
     - Regional-residual separation method
     - Filtering or smoothing applied
     - Grid interpolation method and parameters
   - The manuscript states the data is from Samalas but provides no citation to the original data source or acknowledgment of data providers.

3. **Baseline Comparisons - Absent**:
   - The manuscript compares CHG with THG but provides no quantitative metrics for comparison—only visual/qualitative assessment.
   - No comparison with other edge detection methods (analytic signal, tilt angle, theta map, STDR, enhanced THG variants) that are standard in the field.
   - No comparison with directional derivative methods (DTHD), which are conceptually most similar to CHG.
   - Readers cannot assess whether CHG actually outperforms existing methods or simply provides equivalent information in a different format.

4. **Performance Metrics - Nonexistent**:
   - No quantitative measures of edge detection quality (e.g., edge sharpness, localization accuracy).
   - No signal-to-noise ratio calculations.
   - No resolution analysis (smallest detectable feature size).
   - No sensitivity analysis (effect of parameter variations on results).
   - All assessments are subjective ("successfully highlights," "clearly distinguish").

5. **Validation - Missing**:
   - No independent verification of interpretations:
     - Are the CHG-identified "caldera boundaries" confirmed by geological mapping?
     - Are the "pyroclastic flow features" correlated with known deposits?
     - Is there seismic, magnetotelluric, or drilling data to verify subsurface structure?
   - The Samalas volcanic system is well-studied (Lavigne et al., 2013; Malawani et al., 2022; Mutaqin et al., 2019 cited in manuscript), but the authors do not compare their CHG interpretations with published geological/geophysical models.
   - Without ground truth, we cannot assess whether CHG provides correct or improved interpretations.

6. **Reproducibility - Inadequate**:
   - Insufficient information is provided for other researchers to reproduce the results:
     - Center point coordinates not specified for Samalas case.
     - Grid parameters not provided.
     - Processing workflow not detailed.
     - No code or software implementation shared.
   - The subjective center point selection makes reproducibility questionable.

**Statistical Rigor:**

- No statistical analysis of results (confidence intervals, significance tests, uncertainty quantification).
- No discussion of how data uncertainties propagate to CHG values.
- No assessment of whether observed differences between CHGrad and CHGtan are statistically significant or could arise from noise.

**Practical Considerations:**

- **Computational efficiency**: Not discussed. How long does CHG calculation take? Is it practical for large datasets?
- **User expertise required**: What level of expertise is needed to apply CHG effectively? The subjective center point selection suggests significant user judgment is required.
- **Software availability**: No mention of implementation platform or plans to release software, limiting practical adoption.
- **Workflow integration**: How does CHG fit into typical gravity interpretation workflows? Should it replace THG or complement it?

---

## Presentation: 3/5

**Positive Aspects:**

- The manuscript is generally well-organized with logical section progression.
- The motivation and geological context are clearly presented.
- The writing is mostly clear, though some sections lack necessary detail.

**Presentation Deficiencies:**

1. **Methods Section - Too Brief**:
   - Section 2 is extremely short and lacks critical methodological details.
   - No description of how to implement the method in practice.
   - No discussion of data requirements, preprocessing steps, or quality control.
   - No workflow diagram showing steps from raw data to final interpretation.

2. **Results Section - Insufficient Detail**:
   - **Section 3 (Synthetic Model)**: Lacks quantitative description of model parameters. Figure references suggest results are shown, but without viewing figures, I cannot assess whether they adequately demonstrate the method's capabilities.
   - **Section 4 (Field Data)**: Provides geological background but insufficient information about the gravity data itself, processing applied, or quantitative results obtained.

3. **Figure Quality (based on text descriptions)**:
   - The manuscript mentions figures but I cannot assess their quality directly.
   - From the text, it appears figures show qualitative comparisons but may lack:
     - Quantitative annotations (contour values, color bar scales)
     - Statistical information (uncertainties, significance)
     - Direct comparison panels (side-by-side with same scales)
     - Difference maps showing CHG advantages over THG

4. **Data Tables - Absent**:
   - No tables summarizing:
     - Model parameters for synthetic tests
     - Data acquisition parameters for field surveys
     - Quantitative comparison of methods
     - Performance metrics

5. **Supplementary Materials - Not Mentioned**:
   - Modern methods papers typically include:
     - Detailed model specifications
     - Additional test cases
     - Code implementation
     - Sample datasets
   - No mention of supplementary materials that could address detail limitations in main text.

6. **Discussion Section - Weak**:
   - Section 7 (Discussion) is brief and mostly qualitative.
   - Does not critically evaluate method limitations.
   - Does not compare with existing methods in detail.
   - Does not discuss practical considerations for adoption.
   - Does not address potential failure modes or when CHG is inappropriate.

---

## Contribution: 3/5

**Practical Relevance:**

The application domain (volcanic and caldera structures) is highly relevant:
- **Geothermal exploration**: Identifying ring fractures and hydrothermal circulation pathways.
- **Volcanic hazard assessment**: Mapping caldera boundaries and collapse structures.
- **Mineral exploration**: Delineating ring complexes associated with mineralization.
- **Geological mapping**: Improving understanding of volcanic evolution and structure.

These are important practical problems where improved interpretation tools could have real impact.

**Demonstrated Impact:**

However, the **demonstrated practical value is limited**:

1. **Single Case Study**: Only the Samalas volcanic system is presented. This is insufficient to demonstrate:
   - Generalizability across different geological settings
   - Robustness across different data qualities
   - Applicability to different types of circular features (impact craters, igneous intrusions, salt domes, etc.)

2. **No Validation**: Without independent verification (geological mapping, seismic data, drilling), we cannot confirm that CHG interpretations are correct or superior to existing methods.

3. **No Comparative Performance**: Without quantitative comparison showing CHG outperforms or complements existing methods, the practical advantage remains undemonstrated.

4. **Limited Scope**: The method appears applicable only to circular or nearly circular features, limiting its utility compared to general-purpose edge detection methods.

**Innovation vs. Incremental Improvement:**

From a practical perspective, the contribution appears **incremental rather than transformative**:

- It provides additional directional information (radial vs. tangential) but does not fundamentally change interpretation capabilities.
- Existing methods (directional derivatives, gradient tensor analysis) may provide similar information through different approaches.
- The need to specify a center point adds subjectivity and limits automation potential.
- The practical advantages over simpler approaches (e.g., applying THG along radial and tangential profiles) are not clearly demonstrated.

**Adoption Potential:**

Several factors may limit practical adoption:

1. **Subjectivity**: Requiring user-specified center points makes the method less objective and potentially less reproducible than automatic edge detection methods.

2. **Limited applicability**: Only useful for circular features, whereas most gravity interpretation involves complex, irregular structures.

3. **No software**: Without readily available implementation, practitioners are unlikely to adopt the method.

4. **Insufficient validation**: Geophysicists will be hesitant to adopt a new method without clear demonstration that it provides superior or complementary information to existing techniques.

5. **Learning curve**: Users must understand when and how to apply CHG, but the manuscript provides insufficient guidance.

**Potential for Impact:**

Despite current limitations, the method **could have moderate impact if properly developed**:

- If validated on multiple case studies with ground truth, it could become a standard tool for circular anomaly interpretation.
- If implemented in popular software packages (Oasis montaj, Geosoft, Python libraries), adoption would increase.
- If shown to provide unique information not available from other methods, it would fill a methodological gap.
- If extended to magnetic data and 3D gradient tensors, applicability would broaden.

---

## Strengths

1. **Clear Practical Motivation**: The focus on circular geological features (calderas, volcanic systems) addresses a real interpretation challenge with practical importance.

2. **Relevant Application Domain**: Volcanic and geothermal systems are active research areas with societal relevance (hazard assessment, renewable energy).

3. **Appropriate Case Study Selection**: The Samalas volcanic system is a well-studied, geologically significant example with documented circular structures.

4. **Computational Simplicity**: The method appears straightforward to implement, requiring only standard horizontal derivatives and basic calculations.

5. **Intuitive Concept**: The separation of radial and tangential gradients is conceptually clear and aligns with geological thinking about circular structures (radial collapse/intrusion vs. tangential ring faults/flows).

6. **Preservation of Directional Information**: Unlike THG (always positive), CHG preserves sign information, potentially enabling more nuanced interpretation of gradient directions.

7. **Flexibility**: The hybrid CHG-THG formulation (Equations 7-9) offers interpretative flexibility, allowing users to emphasize different aspects.

---

## Weaknesses

### Critical Experimental Weaknesses:

1. **Insufficient Synthetic Testing**:
   - Models not described in quantitative detail (density contrasts, dimensions, depths).
   - No noise added to test robustness.
   - Limited range of test scenarios (only idealized circular models).
   - No tests of method limitations (elliptical features, overlapping anomalies, regional trends).
   - Grid parameters not specified.

2. **Inadequate Real Data Description**:
   - No information on data acquisition (survey design, instrumentation, precision).
   - No description of data processing (corrections, filtering, gridding).
   - No assessment of data quality (uncertainties, completeness).
   - No citation of data source or acknowledgment of providers.
   - Critical information missing for reproducibility.

3. **No Baseline Comparisons**:
   - CHG compared only with THG, not with other edge detection methods.
   - No comparison with directional derivative methods (most conceptually similar).
   - No comparison with enhanced THG variants, analytic signal, tilt angle, or other standard techniques.
   - Impossible to assess relative performance without comparisons.

4. **Absence of Quantitative Metrics**:
   - All performance assessments are qualitative and subjective.
   - No edge sharpness, localization accuracy, or signal-to-noise metrics.
   - No resolution analysis or sensitivity testing.
   - No statistical significance testing.
   - Impossible to objectively evaluate method performance.

5. **No Independent Validation**:
   - CHG interpretations not verified against geological mapping, seismic data, or drilling results.
   - No comparison with published geophysical models of Samalas system.
   - Cannot confirm that CHG provides correct or improved interpretations.
   - No ground truth to assess accuracy.

6. **Single Case Study**:
   - Only one real-world example (Samalas).
   - Insufficient to demonstrate generalizability across:
     - Different geological settings (intrusions, impact craters, salt domes)
     - Different data qualities and resolutions
     - Different scales (small intrusions to large calderas)
   - Limits confidence in method robustness.

7. **Subjective Center Point Selection**:
   - No objective method for determining center point.
   - Samalas case: center point selection process not described.
   - Makes method subjective and potentially unreproducible.
   - Sensitivity to center point location not tested.

8. **Reproducibility Issues**:
   - Insufficient detail for others to reproduce results.
   - No code or software provided.
   - Key parameters not specified (center point coordinates, grid parameters).
   - Processing workflow not detailed.

### Significant Weaknesses:

9. **No Error Analysis**:
   - Data uncertainties not quantified or propagated to CHG values.
   - No discussion of how noise affects CHG interpretation.
   - No confidence intervals or uncertainty estimates.

10. **Limited Scope Demonstration**:
    - Method tested only on circular features.
    - Behavior on elliptical or irregular features not explored.
    - Limits practical applicability.

11. **No Failure Cases Shown**:
    - When does CHG fail or produce misleading results?
    - What are the method's limitations?
    - No discussion of inappropriate use cases.

12. **Workflow Integration Not Addressed**:
    - How does CHG fit into typical gravity interpretation workflows?
    - Should it replace THG or complement it?
    - What preprocessing is required?
    - What post-processing or interpretation steps follow?

13. **Computational Aspects Not Discussed**:
    - Processing time not reported.
    - Computational efficiency not assessed.
    - Scalability to large datasets not discussed.

14. **No Practical Guidelines**:
    - When should practitioners use CHG vs. other methods?
    - How to choose grid resolution?
    - How to determine center point?
    - How to interpret CHG values quantitatively?

### Minor Weaknesses:

15. **Limited Discussion Section**:
    - Brief and mostly qualitative.
    - Does not critically evaluate limitations.
    - Does not provide practical guidance for users.

16. **No Software Availability Statement**:
    - No mention of code release plans.
    - Limits practical adoption and reproducibility.

17. **Figures May Lack Quantitative Information**:
    - Cannot assess directly, but text suggests qualitative visual comparisons.
    - Should include contour values, statistical annotations, difference maps.

18. **No Supplementary Materials**:
    - Additional details, test cases, and code could be provided as supplements.

---

## Suggestions

### Essential for Acceptance:

1. **Expand Synthetic Testing**:
   - Provide complete quantitative description of all synthetic models:
     - Density contrasts (Δρ in kg/m³)
     - Body dimensions (radius, thickness in km)
     - Burial depth (km)
     - Grid parameters (spacing, extent, resolution)
     - Forward modeling method used
   - Add noise to synthetic data at realistic levels (e.g., ±0.1 mGal) and test robustness.
   - Create comprehensive test suite including:
     - Perfect circles at various depths
     - Elliptical features (varying eccentricity)
     - Irregular shapes
     - Multiple overlapping anomalies
     - Regional trends + local anomalies
     - Varying signal-to-noise ratios
   - Document all model parameters in tables.

2. **Provide Complete Real Data Description**:
   - **Acquisition**: Survey date, instrumentation, station spacing, coverage area, number of stations.
   - **Processing**: Terrain corrections, free-air/Bouguer corrections, regional-residual separation method, filtering, gridding method and parameters.
   - **Quality**: Measurement precision, repeatability, closure errors, data completeness, uncertainty estimates.
   - **Source**: Cite original data source, acknowledge data providers, state data availability.
   - **Center point**: Document how center point was determined for Samalas case (coordinates, method, justification).

3. **Implement Comparative Analysis**:
   - Apply multiple edge detection methods to the same datasets:
     - THG (already included)
     - Analytic signal
     - Tilt angle / theta map
     - Directional THD (most important comparison)
     - Enhanced THG or normalized variants
   - Present side-by-side comparisons with identical display parameters.
   - Discuss relative advantages and disadvantages of each method.
   - Show when CHG provides unique or superior information.

4. **Define and Calculate Quantitative Metrics**:
   - Develop objective performance measures, such as:
     - Edge sharpness index
     - Localization accuracy (for synthetic data with known edges)
     - Signal-to-noise ratio
     - Feature separation metric (radial vs. tangential)
   - Apply metrics consistently to all methods and datasets.
   - Use metrics to objectively compare CHG with baseline methods.
   - Present results in tables and/or bar charts.

5. **Validate with Independent Data**:
   - For Samalas case study:
     - Compare CHG-identified caldera boundaries with published geological maps (Lavigne et al., 2013; Mutaqin et al., 2019).
     - Correlate CHG features with known pyroclastic flow deposits.
     - If available, compare with seismic, MT, or other geophysical data.
   - Quantify agreement (e.g., distance between CHG edges and mapped boundaries).
   - Discuss any discrepancies and their possible causes.

6. **Add Multiple Case Studies**:
   - Include at least 2-3 additional real-world examples:
     - Different geological settings (e.g., igneous intrusion, impact crater)
     - Different scales (small intrusion to large caldera)
     - Different data qualities
   - Demonstrate method generalizability and robustness.
   - Show successful applications and any limitations encountered.

7. **Test Center Point Sensitivity**:
   - For at least one dataset (synthetic and real):
     - Systematically vary center point location
     - Calculate CHG for each center point
     - Quantify how results change with center point displacement
   - Define acceptable center point accuracy for reliable interpretation.
   - Propose method for objectively determining center point or assessing sensitivity.

8. **Provide Reproducibility Information**:
   - Specify all parameters needed to reproduce results:
     - Center point coordinates
     - Grid parameters (spacing, extent, resolution)
     - Processing steps and parameters
   - Provide code implementation (e.g., Python script, MATLAB function).
   - Make sample dataset available (if permitted by data provider).
   - Include detailed workflow description or flowchart.

### Highly Recommended:

9. **Conduct Error Analysis**:
   - Quantify data uncertainties for real datasets.
   - Propagate uncertainties through CHG calculation.
   - Provide uncertainty estimates for CHG values.
   - Discuss how noise affects interpretation reliability.

10. **Test Method Limitations**:
    - Apply CHG to challenging scenarios:
      - Highly elliptical or irregular features
      - Very small or very large anomalies
      - Low signal-to-noise data
      - Complex overlapping sources
    - Document failure modes and limitations.
    - Provide guidance on when CHG is inappropriate.

11. **Develop Practical Guidelines**:
    - Create step-by-step workflow for applying CHG.
    - Provide recommendations for:
      - Grid resolution (e.g., X points per anomaly wavelength)
      - Data quality requirements
      - Center point determination
      - Interpretation of CHG values
    - Include decision tree: when to use CHG vs. other methods?

12. **Assess Computational Performance**:
    - Report processing time for test cases.
    - Discuss computational efficiency.
    - Compare with computational cost of other methods.
    - Address scalability to large datasets.

13. **Expand Discussion Section**:
    - Critical evaluation of method strengths and limitations.
    - Comparison with existing methods (advantages/disadvantages).
    - Practical considerations for adoption.
    - Appropriate use cases and inappropriate use cases.
    - Future research directions.

14. **Improve Figure Presentation**:
    - Ensure all figures have detailed, self-contained captions.
    - Include quantitative annotations (contour values, color scales, coordinates).
    - Use consistent scales for fair comparisons.
    - Add difference maps highlighting CHG advantages.
    - Consider adding profile plots showing quantitative comparisons.

15. **Add Data Tables**:
    - Table 1: Synthetic model parameters
    - Table 2: Real data acquisition and processing parameters
    - Table 3: Quantitative comparison of methods (metrics)
    - Table 4: Comparison of CHG with existing methods (qualitative)

### Recommended Enhancements:

16. **Provide Software Implementation**:
    - Release open-source code (GitHub repository).
    - Include documentation and usage examples.
    - Consider implementing as plugin for popular software (Oasis montaj, Python libraries).

17. **Add Supplementary Materials**:
    - Detailed model specifications
    - Additional test cases
    - Extended methodology description
    - Full-resolution figures
    - Sample datasets and code

18. **Consider Statistical Analysis**:
    - Significance testing (are radial-tangential differences statistically significant?).
    - Confidence intervals for edge locations.
    - Uncertainty quantification using Monte Carlo or bootstrap methods.

19. **Explore Extensions**:
    - Application to magnetic data.
    - Extension to 3D gradient tensor data.
    - Automated center point detection using optimization or pattern recognition.
    - Machine learning integration for feature classification.

---

## Questions for Authors

1. **Synthetic Models**: Can you provide complete quantitative specifications for all synthetic models (density contrasts, dimensions, depths, grid parameters)? Why were these particular model parameters chosen?

2. **Data Acquisition**: What are the acquisition parameters for the Samalas gravity survey (survey date, instrumentation, station spacing, coverage, precision)? Can you provide a station location map?

3. **Data Processing**: What specific processing steps were applied to the Samalas data (terrain corrections, regional-residual separation, filtering, gridding)? What parameters were used for each step?

4. **Data Quality**: What are the estimated uncertainties in the Samalas gravity data? Are there gaps in coverage or areas of poor data quality? How do these affect CHG interpretation?

5. **Center Point Selection**: Exactly how was the center point determined for the Samalas case study? What are its coordinates? Could you provide an objective, reproducible method for center point determination?

6. **Sensitivity Analysis**: How sensitive are the CHG results to the center point location? If the center is mislocated by 1 km, 2 km, 5 km, how do the results change?

7. **Validation**: Can you compare your CHG interpretation with published geological maps or geophysical models of Samalas? Do the CHG-identified features correspond to known structures?

8. **Comparative Performance**: Have you applied other edge detection methods (analytic signal, tilt angle, directional THD) to the same data? How does CHG performance compare quantitatively?

9. **Quantitative Metrics**: Can you define and calculate objective performance metrics (edge sharpness, signal-to-noise, localization accuracy) for CHG and comparison methods?

10. **Noise Robustness**: How does CHG perform on noisy data? Have you tested with realistic noise levels added to synthetic data?

11. **Non-Circular Features**: How does CHG behave for elliptical or irregular features? Have you tested this?

12. **Computational Cost**: What is the computational time required for CHG calculation? How does this compare with other methods?

13. **Grid Resolution**: What grid spacing is required for accurate CHG calculation? How does accuracy depend on the ratio of grid spacing to anomaly wavelength?

14. **Failure Modes**: Under what conditions does CHG fail or produce misleading results? Can you provide examples?

15. **Practical Adoption**: Do you plan to release software implementation? What steps are needed for practitioners to adopt CHG in their workflows?

---

## Rating: 4/10 (Reject, but encourage major revision and resubmission)

**Justification:**

The manuscript presents a conceptually interesting method with potential practical value for volcanic and geothermal applications. However, from an experimental and validation perspective, it falls significantly short of publication standards for *Computers and Geosciences*.

**Key reasons for rejection:**

1. **Inadequate experimental validation**: Synthetic tests lack detail and realism; single real-world case study is insufficient; no independent verification of interpretations.

2. **Missing baseline comparisons**: No quantitative comparison with existing edge detection methods; impossible to assess relative performance or advantages.

3. **Absence of quantitative metrics**: All assessments are qualitative and subjective; no objective performance measures defined or calculated.

4. **Insufficient methodological detail**: Data acquisition, processing, and quality not described; reproducibility severely compromised.

5. **No robustness testing**: Sensitivity to noise, center point location, and parameter variations not assessed.

**Path forward:**

The manuscript requires **major revision** addressing:
- Comprehensive synthetic testing with full model specifications and noise analysis
- Complete real data description (acquisition, processing, quality)
- Quantitative comparison with multiple existing methods using objective metrics
- Independent validation of interpretations against geological/geophysical ground truth
- Additional case studies demonstrating generalizability
- Sensitivity analysis and robustness testing
- Reproducibility information (parameters, code, data availability)

With these substantial additions, the manuscript could become a solid methodological contribution. The core concept has merit, but the experimental work needs to be brought up to journal standards.

---

## Confidence: 4/5 (High Confidence)

I am confident in this assessment based on:

1. **Expertise in geophysical data analysis**: I have extensive experience with gravity data acquisition, processing, and interpretation, including edge detection methods.

2. **Knowledge of validation standards**: I understand the experimental rigor required for methods papers in geophysics journals.

3. **Familiarity with the application domain**: I have knowledge of volcanic and caldera studies and the practical requirements for geothermal exploration.

4. **Assessment of experimental design**: I can identify gaps in testing, validation, and comparison that compromise the manuscript's soundness.

**Slight uncertainty (4/5 rather than 5/5) because:**
- I cannot directly view the figures, so my assessment of visual results is based on textual descriptions.
- The authors may have additional data or results not included in the manuscript that could partially address some concerns.
- Detailed hands-on testing of the method would provide fuller assessment of practical performance.

Nevertheless, I am highly confident that the experimental and validation deficiencies identified are substantial and must be addressed for publication.
