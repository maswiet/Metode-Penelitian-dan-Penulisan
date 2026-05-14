# Novelty and Impact Assessment Report

## Executive Summary

The manuscript introduces the **Centered Horizontal Gravity Gradient (CHG)** method, a novel gradient operator designed to improve interpretation of circular or nearly circular gravity anomalies. The method decomposes horizontal gradients into radial (CHGrad) and tangential (CHGtan) components calculated from a user-specified center point. Based on comprehensive literature review across 188 unique papers (2000-2025), this approach represents a genuinely novel contribution that addresses documented limitations in existing methods, particularly for circular geological features.

---

## 1. State-of-the-Art in Edge Detection Methods

### 1.1 Existing Methods and Their Characteristics

The literature reveals a well-established toolkit for potential field edge detection:

**Amplitude-based methods:**
- **Total Horizontal Gradient (THG)**: The most popular method, combining horizontal derivatives; computationally simple but depth-biased toward shallow sources [Blakely & Simpson, 1986; Pham et al., 2021].
- **Analytic Signal**: Provides amplitude-based, phase-stable edge detection; widely used for boundary location [Pham et al., 2021].

**Phase-based methods:**
- **Tilt angle and theta maps**: Help flatten depth effects and show zero-crossings tied to edges [Chen et al., 2017; Pham et al., 2019].
- **Local phase filters**: Reduce amplitude dominance effects [Ma, 2013].

**Enhanced and normalized variants:**
- **Logistic THG, Enhanced THG, Normalized Analytic Signal**: Developed to suppress shallow anomaly dominance and display features at multiple depths simultaneously [Pham et al., 2019; Nguyen et al., 2024].
- **STDR (Second-order vertical to horizontal derivative ratio)**: Normalizes depth/amplitude contrasts [Nasuti et al., 2019].

**Directional and tensor-based methods:**
- **Directional Total Horizontal Derivatives (DTHD)**: Compute gradients along chosen azimuths to enhance edges with orientation sensitivity [Yuan & Geng, 2014; Yuan et al., 2015].
- **Full tensor gradient methods**: Exploit multiple gradient-tensor components for higher resolution [Yuan et al., 2015].

### 1.2 Documented Limitations of THG and Horizontal Gradient Methods

The literature identifies several critical weaknesses:

1. **Depth-amplitude bias**: THG struggles to outline deeper sources when large shallow anomalies dominate [Nasuti et al., 2019; Pham et al., 2019].

2. **Source superposition and ambiguity**: Overlapping sources reduce THG's ability to separate boundaries [Nasuti et al., 2019; Nguyen et al., 2024].

3. **Noise amplification**: Derivative operations increase high-frequency noise sensitivity [Li, 2013; Ma, 2013].

4. **Variable performance**: No single filter performs best across all geological scenarios [Pham et al., 2021].

**Critical finding**: While the literature documents extensive work on circular geological structures (calderas, volcanic systems), **no study explicitly documents or addresses THG's specific failure mode for circular anomalies**. The manuscript's claim that "THG cannot distinguish between radial and tangential gravity gradients" appears to be an **original observation** not previously documented in the peer-reviewed literature.

---

## 2. Methods for Circular Geological Structures

### 2.1 Interpretation Approaches for Calderas and Volcanic Systems

The literature shows consistent workflows for circular structures:

**Primary methods:**
- Gravity and magnetic surveys combined with derivative operators (THD, horizontal gradient, tilt angle) [Caratori Tontini et al., 2016; Nigussie et al., 2023].
- Forward and inverse 2D-3D modeling with regularization [Setyawan et al., 2009; Paulatto et al., 2019].
- Joint inversions with seismic, MT, bathymetry, and InSAR data [Park et al., 2011; Paulatto et al., 2019].

**Case studies relevant to this work:**
- **Monowai volcanic centre**: Ring dykes and buried plutons identified using gravity/magnetic inversion and bathymetry [Paulatto et al., 2014].
- **Phlegraean Fields, Italy**: Circular rim anomalies tied to caldera structure using multiscale boundary analysis [Florio et al., 2024; De Ritis et al., 2022].
- **Tulu Moye, Ethiopia**: Nested caldera with shallow intrusions mapped using derivatives and MT integration [Nigussie et al., 2023].
- **Hwasan Caldera, Korea**: Pyroclastic fill and ring-fault intrusives resolved via gravity-MT integration [Park et al., 2011].

### 2.2 Treatment of Radial vs. Tangential Features

The literature addresses radial and tangential features through:

1. **Edge detection operators**: Horizontal gradients and THD delineate ring faults and rim boundaries [Perrini et al., 2025; Setyawan et al., 2009].

2. **Directional diagnostics**: Gravity gradient tensor analyses and eigenvector directions infer wall dips and preferred orientations [Kusumoto, 2016].

3. **Scale separation**: Spectral analysis isolates short-wavelength (shallow radial features) from long-wavelength (deep bodies) components [Caratori Tontini et al., 2009; Florio et al., 2024].

4. **Geomorphology integration**: DEM/bathymetry reveals radial fissures and rim-hosted features [Paulatto et al., 2014; Caratori Tontini et al., 2016].

**Critical gap**: While directional derivatives provide azimuthal specificity, **no published method explicitly decomposes gradients into radial and tangential components about a user-specified center point**. Existing directional methods (DTHD) compute gradients along fixed azimuths, not in a center-referenced radial/tangential coordinate system.

### 2.3 Numerical Methods for Gradient Calculation

The literature documents several computational approaches:

- **Fourier-domain convolution**: FFT-based fast forward modeling [Caratori Tontini et al., 2009].
- **Finite-element methods**: FEM-based Green's functions for linear inverse modeling [Ronchin et al., 2017].
- **Mesh-based methods**: Octree/quadtree meshing with numerical forward modeling (SimPEG-style) [Ardestani et al., 2021].
- **Iterative solvers**: Conjugate-gradient optimization for 3D inversion [Nakatsuka & Okuma, 2014].

**Critical finding**: The literature emphasizes Fourier, FEM, and mesh-based methods rather than explicit finite-difference schemes for gradient calculation. The manuscript's use of **finite-difference formulation for CHG calculation** is standard practice but not prominently discussed in recent literature, which has moved toward spectral and FEM approaches.

---

## 3. Novelty Assessment of the CHG Method

### 3.1 Conceptual Novelty

The CHG method introduces **three novel elements**:

1. **Center-point reference frame**: Gradients calculated from a specific center point rather than in a fixed geographic coordinate system.

2. **Explicit radial/tangential decomposition**: Separates horizontal gradients into components parallel (radial) and perpendicular (tangential) to the direction from the center point.

3. **Geometric interpretation**: Provides physical meaning to gradient components in the context of circular anomaly geometry.

**Literature comparison**: 
- **Directional THD** [Yuan & Geng, 2014; Yuan et al., 2015] computes gradients along selected azimuths but does not reference a center point or separate radial from tangential components.
- **Gravity gradient tensor analysis** [Kusumoto, 2016] uses eigenvector directions but does not explicitly decompose into radial/tangential components.
- **No existing method** in the reviewed literature (188 papers, 2000-2025) explicitly implements a center-referenced radial/tangential gradient decomposition.

**Novelty verdict**: The CHG concept is **genuinely novel** and represents an original contribution to potential field interpretation methodology.

### 3.2 Methodological Novelty

The manuscript develops:

1. **Mathematical formulation**: Explicit finite-difference equations for CHGrad and CHGtan based on geometric projections.

2. **Hybrid visualization**: Combination parameter allowing flexible mixing of CHG and THG (equations for α and β weighting).

3. **Implementation approach**: Computationally simple method requiring only horizontal derivatives and center-point coordinates.

**Strengths**:
- The mathematical development appears sound and follows logically from geometric principles.
- The method is computationally efficient, requiring no iterative optimization or complex numerical schemes.
- The approach is generalizable to any potential field data (gravity or magnetic).

**Concerns**:
- The finite-difference formulation is standard; the novelty lies in the geometric framework, not the numerical method.
- The manuscript does not appear to provide error analysis or discuss numerical accuracy/stability.
- No comparison with directional derivative methods (DTHD) is provided, despite conceptual similarities.

### 3.3 Practical Novelty and Impact

**Application to synthetic data**: The manuscript tests CHG on synthetic circular anomalies with radial and tangential density variations, demonstrating successful separation of these components.

**Application to real data**: The Samalas volcanic system (Lombok, Indonesia) serves as a case study, with CHGrad highlighting caldera boundaries and CHGtan revealing pyroclastic flow features.

**Documented advantages**:
- Clear visual separation of radial vs. tangential features
- Preservation of sign information (unlike THG, which is always positive)
- Flexibility in interpretation through α-β mixing parameters

**Potential impact**:
- **High relevance** for volcanic and caldera studies, where radial (collapse, intrusion) and tangential (ring faults, flow deposits) features have distinct geological meanings.
- **Practical value** for geothermal exploration, mineral exploration around ring structures, and volcanic hazard assessment.
- **Complementary** to existing methods rather than replacing them; CHG adds information not available from THG alone.

---

## 4. Positioning Relative to Existing Literature

### 4.1 Advances Over THG

The manuscript correctly identifies that:
- THG combines all horizontal gradient components into a single positive value, losing directional information.
- For circular anomalies, this conflates radial changes (toward/away from center) with tangential changes (around the perimeter).

**Novel contribution**: CHG preserves directional information and explicitly separates these components, providing clearer geological interpretation.

**Literature support**: While THG's limitations are well-documented for depth bias and source superposition [Nasuti et al., 2019; Pham et al., 2019], its specific limitation for circular anomalies is **not explicitly discussed** in the reviewed literature. This represents an **original insight** by the authors.

### 4.2 Relationship to Directional Derivative Methods

**Similarities**:
- Both CHG and directional derivatives (DTHD) provide orientation-specific gradient information.
- Both can enhance features aligned with specific directions.

**Key differences**:
- **DTHD** computes gradients along fixed geographic azimuths (e.g., N-S, E-W, NE-SW).
- **CHG** computes gradients in a center-referenced polar coordinate system (radial and tangential).
- **DTHD** requires multiple azimuth calculations to cover all directions.
- **CHG** provides complete radial/tangential decomposition from a single center point.

**Advantage of CHG**: For circular or nearly circular features, CHG's center-referenced approach is more geometrically intuitive and directly interpretable than DTHD's azimuth-based approach.

**Missing discussion**: The manuscript does not cite or compare with directional derivative methods [Yuan & Geng, 2014; Yuan et al., 2015; Ekinci et al., 2013], which represent the closest conceptual relatives in the literature. **This is a significant gap** that should be addressed.

### 4.3 Relationship to Gradient Tensor Methods

**Gradient tensor approaches** [Kusumoto, 2016] use eigenvector analysis to identify structural orientations and can distinguish different structural trends.

**Comparison**:
- Tensor methods provide orientation information but require full gradient tensor data (including vertical derivatives).
- CHG requires only horizontal derivatives and a center point estimate.
- Tensor methods are more data-intensive but provide richer structural information.
- CHG is simpler, more intuitive, and specifically designed for circular features.

**Positioning**: CHG occupies a middle ground between simple THG and complex tensor methods, offering enhanced interpretability for circular features without requiring full tensor data.

---

## 5. Gaps and Limitations in the Manuscript

### 5.1 Missing Literature Comparisons

**Critical omissions**:
1. **Directional derivative methods**: No citation of Yuan & Geng (2014), Yuan et al. (2015), Ekinci et al. (2013), or Mazzoldi et al. (2020) on directional THD and its applications.
2. **Gradient tensor methods**: No discussion of Kusumoto (2016) on structural analysis of calderas using gravity gradient tensors.
3. **Enhanced THG variants**: Limited discussion of normalized/enhanced THG methods that also address THG limitations.

**Impact**: Without explicit comparison to these methods, readers cannot fully assess CHG's advantages and appropriate use cases.

### 5.2 Theoretical Gaps

**Mathematical derivation concerns**:
1. The manuscript presents finite-difference formulas but does not discuss:
   - Truncation error and numerical accuracy
   - Grid spacing requirements for reliable gradient estimation
   - Sensitivity to center point misspecification
   - Behavior near the center point (singularity issues?)

2. No error propagation analysis from data uncertainties to CHG values.

3. No discussion of how to objectively determine the center point for real data (appears to be manual/subjective).

**Methodological concerns**:
1. The hybrid THG-CHG mixing (α and β parameters) is introduced but not rigorously justified or tested.
2. No quantitative metrics for evaluating CHG performance (only visual assessment).
3. No comparison of CHG with other methods on the same synthetic or real datasets.

### 5.3 Practical Application Gaps

**Real data limitations**:
1. Only one case study (Samalas) is presented; additional examples would strengthen the validation.
2. No comparison with independent geological/geophysical data (seismic, MT, drilling) to verify interpretations.
3. No discussion of when CHG is appropriate vs. when other methods should be preferred.
4. No guidance on grid resolution, data quality requirements, or preprocessing steps.

**Generalization questions**:
1. How does CHG perform for elliptical or irregular features?
2. How sensitive is the method to the accuracy of center point determination?
3. Can CHG be extended to 3D gradient tensor data or only 2D horizontal gradients?

---

## 6. Significance and Impact Assessment

### 6.1 Scientific Significance

**Theoretical contribution**: **Moderate to High**
- Introduces a genuinely novel geometric framework for gradient analysis.
- Provides new insight into THG's limitations for circular anomalies (not previously documented).
- Offers a simple, intuitive method that is easy to implement and interpret.

**Methodological contribution**: **Moderate**
- The mathematical development is straightforward (geometric projection + finite differences).
- No new numerical techniques or computational innovations.
- The novelty is primarily conceptual rather than mathematical.

### 6.2 Practical Impact

**Application domains**:
1. **Volcanic and caldera studies**: High impact for distinguishing collapse structures (radial) from ring faults and flow deposits (tangential).
2. **Geothermal exploration**: Useful for mapping circular hydrothermal systems and ring fracture zones.
3. **Mineral exploration**: Relevant for ring complexes, kimberlite pipes, and circular intrusions.
4. **Impact crater studies**: Applicable to central uplifts and ring structures.

**Adoption potential**: **Moderate to High**
- Simple to implement (can be added to existing software).
- Computationally efficient (no iterative algorithms).
- Provides clear, interpretable results.
- Requires only standard gravity data and a center point estimate.

**Limitations to impact**:
- Applicability limited to circular or nearly circular features.
- Requires a priori knowledge or estimation of center point.
- May be less useful for complex, irregular, or multiple overlapping anomalies.

### 6.3 Comparison with Recent Developments

**Recent trends in potential field edge detection** (2020-2025):
- Emphasis on normalized/balanced filters to handle multi-scale features [Nguyen et al., 2024].
- Integration with machine learning for automated feature detection.
- Joint inversion with multiple geophysical datasets [Paulatto et al., 2019; Nigussie et al., 2023].
- Full tensor gradient exploitation for higher resolution [Yuan et al., 2015].

**CHG's position**: The method aligns with the trend toward **application-specific, interpretable filters** rather than universal edge detectors. It does not leverage recent advances in machine learning or joint inversion but offers a targeted solution for a specific geometric class of anomalies.

---

## 7. Recommendations for Strengthening the Manuscript

### 7.1 Essential Additions

1. **Comparative analysis**: Include quantitative comparison with directional THD [Yuan & Geng, 2014; Ekinci et al., 2013] on the same synthetic and real datasets.

2. **Error analysis**: Discuss numerical accuracy, truncation error, sensitivity to center point location, and error propagation.

3. **Center point determination**: Provide objective methods or guidelines for determining the center point from data (e.g., using symmetry analysis, moment calculations, or iterative optimization).

4. **Additional case studies**: Include 1-2 more real-world examples from different geological settings to demonstrate generalizability.

5. **Validation**: Compare CHG interpretations with independent data (seismic, drilling, geological mapping) to verify accuracy.

### 7.2 Important Enhancements

6. **Quantitative metrics**: Define objective measures of CHG performance (e.g., edge sharpness, signal-to-noise ratio, feature separation index).

7. **Parameter sensitivity**: Systematically test sensitivity to grid spacing, center point location, and α-β mixing parameters.

8. **Limitation discussion**: Clearly state when CHG is appropriate vs. when other methods should be used.

9. **Extended literature review**: Include comprehensive discussion of directional derivative and gradient tensor methods.

10. **Mathematical rigor**: Provide formal derivations with assumptions, approximations, and accuracy estimates.

### 7.3 Desirable Improvements

11. **Software availability**: Provide open-source code implementation to facilitate adoption.

12. **Workflow guidance**: Develop step-by-step methodology for applying CHG to new datasets.

13. **Extension discussion**: Explore potential extensions to 3D gradient tensors, magnetic data, and non-circular features.

14. **Comparison tables**: Summarize advantages/disadvantages of CHG vs. THG, DTHD, and tensor methods in tabular form.

---

## 8. Conclusion

The **Centered Horizontal Gravity Gradient (CHG) method represents a genuinely novel and valuable contribution** to potential field interpretation, particularly for circular and nearly circular geological features. The method addresses a previously undocumented limitation of THG and provides clear, interpretable separation of radial and tangential gradient components.

**Key strengths**:
- **Original concept**: No existing method provides center-referenced radial/tangential gradient decomposition.
- **Practical value**: High relevance for volcanic, geothermal, and mineral exploration applications.
- **Simplicity**: Easy to implement and computationally efficient.
- **Interpretability**: Provides clear geological meaning for circular anomalies.

**Key weaknesses**:
- **Limited validation**: Only one real-world case study; needs more examples.
- **Missing comparisons**: No comparison with directional derivative or tensor methods.
- **Theoretical gaps**: Insufficient discussion of numerical accuracy, error analysis, and center point determination.
- **Narrow scope**: Applicability limited to circular or nearly circular features.

**Overall assessment**: The manuscript is **suitable for publication in Computers and Geosciences** after **major revisions** to address the identified gaps, particularly:
1. Comparative analysis with directional derivative methods
2. Error analysis and sensitivity testing
3. Additional case studies
4. Expanded literature review and positioning

**Impact potential**: If properly validated and compared with existing methods, CHG could become a **standard tool** for interpreting circular gravity anomalies in volcanic and geothermal systems, with moderate to high citation impact expected within the geophysical community.

---

## References Cited in This Report

[Full reference list from both search insights, formatted consistently]

**Edge Detection Methods:**
- Blakely, R.J., & Simpson, R.W. (1986). Approximating edges of source bodies from magnetic gravity anomalies. Geophysics, 51(7), 1494-1498.
- Chen, A.G., Zhou, T.F., Liu, D.J., et al. (2017). Application of an enhanced theta-based filter for potential field edge detection: A case study of the Luzong ore district. Chinese Journal of Geophysics.
- Ekinci, Y.L., Ertekin, C., & Yiğitbaş, E. (2013). On the effectiveness of directional derivative based filters on gravity anomalies for source edge approximation. Journal of Geophysics and Engineering, 10(3).
- Li, L.L. (2013). New edge detection method of potential field data-enhanced horizontal derivative method.
- Ma, G. (2013). Edge detection of potential field data using improved local phase filter. Exploration Geophysics.
- Nasuti, Y., Nasuti, A., & Moghadas, D. (2019). STDR: A novel approach for enhancing and edge detection of potential field data. Pure and Applied Geophysics.
- Nguyen, D.V., Kieu, T.D., Nguyen, L.N., et al. (2024). Studying the theoretical basis and advantages and disadvantages of Logistic methods of the total horizontal gradient. Journal of Mining and Earth Sciences, 65(1).
- Pham, L.T., Vu, M.D., & Le, S.T. (2021). Performance evaluation of amplitude- and phase-based methods for estimating edges of potential field sources. Iranian Journal of Science and Technology Transaction A-Science.
- Pham, L.T., Oksum, E., & Do, T.D. (2019). Edge enhancement of potential field data using the logistic function and the total horizontal gradient. Acta Geodaetica et Geophysica Hungarica.
- Yuan, Y., & Geng, M. (2014). Directional total horizontal derivatives of gravity gradient tensor and their application to delineate the edges. EAGE Conference Proceedings.
- Yuan, Y., Huang, D.N., & Yu, Q.L. (2015). Using enhanced directional total horizontal derivatives to detect the edges of potential-field full tensor data. Chinese Journal of Geophysics.

**Circular Structures and Calderas:**
- Ardestani, V.E., Fournier, D., et al. (2021). Gravity and magnetic processing and inversion over the Mahallat geothermal system using open source resources in Python. Pure and Applied Geophysics.
- Caratori Tontini, F., Cocchi, L., & Carmisciano, C. (2009). Rapid 3-D forward model of potential fields with application to the Palinuro Seamount magnetic anomaly. Journal of Geophysical Research.
- Caratori Tontini, F., de Ronde, C.E.J., Scott, B.J., et al. (2016). Interpretation of gravity and magnetic anomalies at Lake Rotomahana: Geological and hydrothermal implications. Journal of Volcanology and Geothermal Research.
- De Ritis, R., Cocchi, L., Passaro, S., et al. (2022). Bouguer anomaly re-reduction and interpretative remarks of the Phlegraean Fields caldera structures. Remote Sensing, 15(1).
- Florio, G., Fedi, M., Di Vito, M.A., et al. (2024). Structural elements from gravity and magnetic data in the Phlegraean Fields. EGU General Assembly.
- Handyarso, A. (2023). Caldera-like delineation and geological resources identification of Majenang area, Indonesia by gravity and magnetic data inversions. IOP Conference Series: Earth and Environmental Science.
- Kusumoto, S. (2016). Structural analysis of calderas by semiautomatic interpretation of the gravity gradient tensor: A case study in Central Kyushu, Japan. InTech.
- Mazzoldi, A., Garduño-Monroy, V.H., Gómez Cortes, J.J., et al. (2020). Geophysics for geothermal exploration: Directional-derivatives-based computational filters applied to geomagnetic data at Lake Cuitzeo, Mexico. Geofísica Internacional, 59(2).
- Nakatsuka, T., & Okuma, S. (2014). Aeromagnetic 3D subsurface imaging with effective source volume minimisation and its application to data from the Otoge cauldron. Exploration Geophysics.
- Nigussie, W., Alemu, A., Mickus, K.L., et al. (2023). Subsurface structural control of geothermal resources in a magmatic rift: Gravity and magnetic study of the Tulu Moye geothermal prospect, Main Ethiopian Rift. Frontiers in Earth Science.
- Park, G., Lee, C.K., Yang, J.M., et al. (2011). 3-D geological structure interpretation by the integrated analysis of magnetotelluric and gravity model at Hwasan Caldera. Journal of The Korean Earth Science Society, 32(6).
- Paulatto, M., de Ronde, C.E.J., Peirce, C., et al. (2014). Potential field and bathymetric investigation of the Monowai volcanic centre, Kermadec Arc: Implications for caldera formation and volcanic evolution. Geophysical Journal International.
- Paulatto, M., Moorkamp, M., Hautmann, S., et al. (2019). Vertically extensive magma reservoir revealed from joint inversion and quantitative interpretation of seismic and gravity data. Journal of Geophysical Research.
- Perrini, M., Barone, A., Tizzani, P., et al. (2025). Advanced boundary analysis techniques as a tool to decipher volcano-tectonic setting of the Campi Flegrei caldera. EGU General Assembly.
- Ronchin, E., Masterlark, T., et al. (2017). Imaging the complex geometry of a magma reservoir using FEM-based linear inverse modeling of InSAR data: Application to Rabaul Caldera, Papua New Guinea. Geophysical Journal International.
- Saltus, R.W., & Blakely, R.J. (2011). Unique geologic insights from "non-unique" gravity and magnetic interpretation. GSA Today.
- Setyawan, A., Ehara, S., et al. (2009). The gravity anomaly of Ungaran volcano, Indonesia: Analysis and interpretation. Journal of the Geothermal Research Society of Japan, 31(3).
