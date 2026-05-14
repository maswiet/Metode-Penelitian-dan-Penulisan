# Reviewer 3 Report: Clarity, Positioning, and Broader Impact Specialist

## Summary

This manuscript introduces the Centered Horizontal Gravity Gradient (CHG) method for interpreting circular gravity anomalies, with application to the Samalas volcanic system in Indonesia. The core idea—decomposing horizontal gradients into radial and tangential components relative to a center point—is conceptually appealing and addresses a relevant problem in volcanic and geothermal geophysics. However, the manuscript suffers from significant weaknesses in writing quality, structural organization, literature positioning, and contextual framing that prevent it from meeting publication standards for *Computers and Geosciences*. The work needs substantial revision to improve clarity, properly position the contribution within existing literature, provide adequate context for readers, and address ethical and practical considerations.

---

## Soundness: 3/5

From a clarity and positioning perspective, the manuscript has moderate soundness with several concerns:

**Conceptual Clarity:**
- The basic concept of center-referenced radial/tangential gradient decomposition is clearly motivated and conceptually sound.
- The geometric intuition is easy to grasp and aligns well with how geologists think about circular structures.
- However, the presentation lacks precision in key areas (see Presentation section).

**Logical Structure:**
- The overall flow (Introduction → Method → Synthetic Test → Field Application → Discussion → Conclusion) is reasonable.
- However, transitions between sections are abrupt, and the narrative lacks cohesion.
- The argumentation for why CHG is needed and how it advances the field is incomplete.

**Positioning Issues:**
- The manuscript inadequately positions the work relative to existing literature, particularly directional derivative methods and gradient tensor approaches.
- The claimed limitations of THG for circular anomalies are not supported by citations—this appears to be an original observation by the authors, but it's presented as if it's established knowledge.
- The novelty and significance are not clearly articulated relative to the state-of-the-art.

---

## Presentation: 2/5

The manuscript has significant presentation issues that impede understanding and diminish impact:

### Writing Quality Issues:

1. **Title Inconsistency**:
   - Title: "Centered Horizontal Gravity Gradient (CHG)"
   - Abstract: "Centered Horizontal Gravity (CHG)"
   - The abbreviation CHG is inconsistent between title and abstract. Which is correct?

2. **Abstract Problems**:
   - First sentence is awkward: "Gravity gradient is one of the best methods for determining the lateral boundaries of geological features gravity anomaly." (Missing punctuation or word?)
   - "The weakness of the THG method is that its value is always positive, making it sometimes impractical for understanding subsurface structures" – This is imprecise. The positive-only nature of THG is not necessarily "impractical"; the issue is loss of directional information.
   - "The THG method is also unable to provide a good interpretation of geological features with circular Or nearly circular shapes" – "Or" should be lowercase; also, this claim needs more precise explanation.
   - The abstract introduces "CHGrad" and "CHGtan" without first explaining what "radial" and "tangential" mean in this context.
   - The abstract is too long and includes unnecessary detail (e.g., "synthetic gravity anomaly model has been created").

3. **Grammatical and Language Issues Throughout**:
   - "Gravity gradient is one of the best methods" – awkward phrasing; should be "Gravity gradient analysis is among the most effective methods"
   - "gravity anomaly" (missing punctuation in abstract)
   - "Circular Or nearly circular" (capitalization error)
   - "A synthetic gravity anomaly model has been created to test" – passive voice overuse
   - "CHG was also tested" – passive voice
   - "The results of trials" – awkward; "Tests on synthetic and field data"
   - Many sentences are overly long and complex, reducing clarity.

4. **Terminology Issues**:
   - The title says "Centered Horizontal Gravity Gradient" but the abstract says "Centered Horizontal Gravity" – which term is correct?
   - The term "Centered" is potentially confusing. Does it mean "center-referenced" or "centered around a point"? Consider "Center-Referenced Horizontal Gravity Gradient" for clarity.
   - "Concentrated Horizontal Gradient (CHG)" appears in the Keywords but "Centered" is used everywhere else – is this a typo?
   - Inconsistent terminology for the method throughout.

5. **Section-Specific Issues**:

   **Introduction (Section 1):**
   - Too brief and lacks depth. For a methods paper, the introduction should more thoroughly review existing methods and their limitations.
   - The transition from discussing THG limitations to proposing CHG is abrupt; needs better logical development.
   - The statement "THG cannot distinguish between radial and tangential gravity gradients" is presented without citation or justification. Is this documented in literature or an original observation?
   - The introduction does not clearly state the research objectives or contribution.
   - Missing discussion of why radial vs. tangential distinction is geologically important.

   **Method (Section 2):**
   - Extremely brief (appears to be only a few paragraphs based on parsed text).
   - Jumps directly to equations without adequate conceptual explanation.
   - No figure illustrating the geometric concept (radial vs. tangential directions).
   - No discussion of assumptions, limitations, or applicability conditions.
   - The finite-difference formulas are presented without derivation or justification.
   - No discussion of implementation considerations (grid resolution, center point determination, etc.).

   **Synthetic Model (Section 3):**
   - Lacks sufficient detail about model parameters.
   - No clear explanation of what the synthetic test is designed to demonstrate.
   - Results description is too brief and qualitative.

   **Field Data (Section 4-6):**
   - Section 4 provides geological background but insufficient information about the gravity data itself.
   - Sections 5-6 (Results and Interpretation) are not clearly distinguished; the structure is confusing.
   - Results are described qualitatively without quantitative support.
   - The interpretation relies heavily on visual assessment of figures.

   **Discussion (Section 7):**
   - Too brief for a methods paper.
   - Does not critically evaluate limitations.
   - Does not compare with existing methods in depth.
   - Does not discuss practical implications or guide users on when to apply CHG.
   - Does not address potential failure modes or inappropriate use cases.

   **Conclusion (Section 8 appears to be "Contribution"):**
   - The section titled "Contribution" (Section 8 in parsed text) appears to be author contributions, not scientific conclusions.
   - No proper conclusions section summarizing key findings, implications, and future directions.

### Structural Issues:

6. **Section Organization**:
   - The manuscript structure is somewhat unconventional:
     - Section 8 is "Contribution" (author contributions) rather than "Conclusions"
     - No dedicated "Conclusions" section
     - "Discussion" is very brief
   - The flow from sections 4→5→6→7 is unclear without viewing the full document.

7. **Missing Elements**:
   - No schematic diagrams explaining the concept (radial vs. tangential gradients, coordinate transformation).
   - No workflow diagram showing implementation steps.
   - No tables summarizing model parameters, data characteristics, or method comparisons.
   - No supplementary materials mentioned.

8. **Figure Integration (based on text)**:
   - Figures are mentioned but not adequately integrated into the narrative.
   - Figure captions (from parsed text) may lack sufficient detail for standalone understanding.
   - No clear connection between figures and key points in the text.

### Accessibility Issues:

9. **Readability**:
   - The manuscript uses technical jargon without always defining terms.
   - Equations are presented without sufficient explanation for readers unfamiliar with finite-difference methods.
   - The geological context (Samalas volcanic system) is described but not connected clearly to the methodological demonstration.

10. **Reproducibility**:
    - Insufficient detail for readers to implement the method.
    - Key parameters not specified (center point coordinates, grid resolution, processing steps).
    - No code or software availability mentioned.

---

## Contribution: 3/5

### Positioning in Literature:

**Major Gap: Inadequate Literature Review**

The manuscript has a **critical weakness** in how it positions the work relative to existing literature:

1. **Missing Key References**:
   - **Directional derivative methods**: The manuscript does not cite or discuss:
     - Yuan & Geng (2014): "Directional Total Horizontal Derivatives of Gravity Gradient Tensor"
     - Yuan et al. (2015): "Using enhanced directional total horizontal derivatives"
     - Ekinci et al. (2013): "On the effectiveness of directional derivative based filters"
     - Mazzoldi et al. (2020): "Directional-derivatives-based computational filters"
   - These are highly relevant as they also provide direction-specific gradient information, making them the closest conceptual relatives to CHG.

   - **Gradient tensor methods**: No mention of:
     - Kusumoto (2016): "Structural Analysis of Calderas by Semiautomatic Interpretation of the Gravity Gradient Tensor"
     - This work specifically addresses caldera interpretation using gradient tensor analysis, directly relevant to the Samalas case study.

   - **Enhanced THG variants**: Limited discussion of:
     - Pham et al. (2019): Logistic THG
     - Nasuti et al. (2019): STDR method
     - Nguyen et al. (2024): Recent THG enhancements
   - These methods also address THG limitations, providing alternative approaches to the same problem.

2. **Insufficient Comparison**:
   - The manuscript compares CHG only with basic THG, not with the broader family of edge detection methods.
   - No discussion of how CHG relates to or differs from directional derivatives, which seem conceptually similar.
   - No acknowledgment that gradient tensor methods also provide directional/structural information for calderas.

3. **Unsupported Claims**:
   - The claim that "THG cannot distinguish between radial and tangential gravity gradients and even tends to confuse both of them" is not supported by citations.
   - If this is an original observation (which it appears to be, based on literature review), it should be clearly stated as such and demonstrated more rigorously.
   - The manuscript presents this as if it's established knowledge, which is misleading.

4. **Novelty Not Clearly Articulated**:
   - The manuscript does not explicitly state what is novel about CHG compared to existing methods.
   - Readers are left to infer the contribution rather than having it clearly explained.
   - The relationship between CHG and directional derivatives needs clarification—are they fundamentally different or variations on a theme?

### Significance Assessment:

**Potential Significance: Moderate**

The contribution has moderate potential significance, but it's not clearly demonstrated:

**Positive aspects:**
- Addresses interpretation of circular anomalies, relevant for volcanic/geothermal applications.
- Provides intuitive geometric framework (radial vs. tangential).
- Computationally simple and potentially easy to adopt.

**Limitations to significance:**
- **Narrow scope**: Only applicable to circular or nearly circular features.
- **Incremental nature**: Adds directional information but doesn't fundamentally change interpretation capabilities.
- **Unclear advantages**: Without comparative analysis, the practical benefits over existing methods are unclear.
- **Limited validation**: Single case study without independent verification limits demonstrated impact.

**For higher significance, the manuscript needs:**
- Clear demonstration that CHG provides information not available from existing methods.
- Multiple case studies showing generalizability.
- Quantitative evidence of improved interpretation accuracy or reliability.
- Validation against ground truth (geological mapping, seismic data, drilling).

### Broader Impact Considerations:

**Positive Impacts:**
- Could improve interpretation of volcanic and caldera structures, relevant for:
  - Geothermal resource assessment (renewable energy)
  - Volcanic hazard assessment (public safety)
  - Understanding volcanic evolution (scientific knowledge)
  - Mineral exploration (economic value)

**Practical Adoption Considerations:**
- **Ease of implementation**: Appears straightforward, which favors adoption.
- **Software availability**: Not mentioned; without readily available tools, adoption will be limited.
- **User expertise required**: The subjective center point selection may require significant expertise and geological knowledge.
- **Applicability scope**: Limited to circular features may restrict utility compared to general-purpose methods.

**Ethical and Societal Considerations:**

The manuscript does not discuss:
- **Data availability and sharing**: Will the Samalas data be made available? Are there any restrictions?
- **Open science**: Will code be released as open source?
- **Reproducibility**: Are sufficient details provided for others to reproduce and verify the results?
- **Potential misuse**: Could incorrect application of CHG lead to misinterpretation with negative consequences (e.g., mislocating geothermal resources, underestimating volcanic hazards)?
- **Accessibility**: Is the method accessible to researchers in developing countries where volcanic hazards are often highest?

These considerations are increasingly important for modern scientific publishing and should be addressed.

---

## Strengths

1. **Clear Conceptual Motivation**: The geometric intuition behind separating radial and tangential gradients is clear and aligns well with geological thinking about circular structures.

2. **Relevant Application Domain**: Volcanic and caldera structures are important targets for geothermal exploration and hazard assessment, giving the work practical relevance.

3. **Appropriate Case Study**: The Samalas volcanic system is well-studied and provides a good test case with documented circular features.

4. **Computational Simplicity**: The method appears straightforward to implement, which could facilitate adoption.

5. **Preservation of Directional Information**: Unlike THG, CHG preserves sign information, potentially enabling more nuanced interpretation.

6. **Interdisciplinary Relevance**: The work bridges geophysics, volcanology, and geothermal exploration, potentially appealing to multiple communities.

7. **Timely Topic**: With increasing interest in geothermal energy and volcanic hazard assessment, improved interpretation tools are valuable.

---

## Weaknesses

### Critical Weaknesses:

1. **Poor Literature Positioning**:
   - Missing citations to highly relevant directional derivative methods (Yuan & Geng, 2014; Yuan et al., 2015; Ekinci et al., 2013).
   - No discussion of gradient tensor methods for calderas (Kusumoto, 2016).
   - Inadequate engagement with enhanced THG literature.
   - Failure to clearly distinguish CHG from existing approaches.
   - Novelty not explicitly stated or justified relative to prior work.

2. **Inadequate Introduction**:
   - Too brief for a methods paper.
   - Does not thoroughly review existing methods and their limitations.
   - Does not clearly state research objectives or contribution.
   - Lacks logical development of argumentation.
   - Does not explain why radial-tangential distinction is geologically important.

3. **Insufficient Method Description**:
   - Section 2 is extremely brief and lacks detail.
   - No conceptual diagram illustrating radial vs. tangential gradients.
   - No discussion of assumptions, limitations, or applicability.
   - No guidance on implementation (center point determination, grid resolution, etc.).
   - Equations presented without adequate explanation.

4. **Weak Discussion Section**:
   - Too brief and superficial.
   - Does not critically evaluate limitations.
   - Does not compare with existing methods in depth.
   - Does not provide practical guidance for users.
   - Does not discuss failure modes or inappropriate use cases.

5. **Writing Quality Issues**:
   - Numerous grammatical errors and awkward phrasing.
   - Inconsistent terminology (Centered vs. Concentrated; CHG definition varies).
   - Overuse of passive voice.
   - Overly long, complex sentences that reduce clarity.
   - Abstract is too long and poorly structured.

6. **Structural Problems**:
   - No proper Conclusions section (Section 8 is author contributions).
   - Section organization is unconventional and potentially confusing.
   - Abrupt transitions between sections.
   - Poor narrative flow and cohesion.

7. **Missing Visual Aids**:
   - No schematic diagram explaining the concept.
   - No workflow diagram showing implementation steps.
   - No tables summarizing parameters or comparisons.
   - Figure integration appears weak based on text.

8. **Reproducibility Concerns**:
   - Insufficient detail for others to implement the method.
   - Key parameters not specified.
   - No code or data availability statements.
   - Subjective center point selection reduces reproducibility.

### Significant Weaknesses:

9. **Unsupported Claims**:
   - THG's limitation for circular anomalies presented without citation or rigorous demonstration.
   - Claims about CHG's advantages not quantitatively supported.
   - Interpretation statements not validated against independent data.

10. **Single Case Study**:
    - Only Samalas example provided.
    - Limits demonstration of generalizability.
    - Insufficient to establish method robustness.

11. **No Comparative Analysis**:
    - CHG compared only with basic THG.
    - Other edge detection methods not applied to same data.
    - Relative advantages unclear.

12. **Qualitative Assessment Only**:
    - All performance evaluations are subjective.
    - No quantitative metrics defined or calculated.
    - No statistical analysis.

13. **Limited Scope Discussion**:
    - Applicability to non-circular features not explored.
    - Conditions for method success/failure not discussed.
    - Practical guidance for users missing.

14. **No Broader Impact Discussion**:
    - Ethical considerations not addressed.
    - Data and code sharing not discussed.
    - Accessibility and reproducibility not considered.
    - Potential for misuse or misinterpretation not acknowledged.

### Minor Weaknesses:

15. **Abstract Issues**:
    - Too long and detailed.
    - Poor structure (not following standard IMRaD format).
    - Includes unnecessary implementation details.

16. **Keyword Problems**:
    - "Concentrated Horizontal Gradient (CHG)" in keywords but "Centered" everywhere else—typo?
    - Keywords could be more specific and comprehensive.

17. **References**:
    - Reference list appears short (only 8 references in parsed text).
    - Missing many relevant recent papers (2020-2025).
    - Limited engagement with recent methodological developments.

18. **Author Contributions Section**:
    - Placed where Conclusions should be.
    - Could be moved to end or acknowledgments.

---

## Suggestions

### Essential for Acceptance:

1. **Expand and Improve Literature Review**:
   - Add comprehensive review of edge detection methods in Introduction:
     - THG and its variants (enhanced, normalized, logistic)
     - Analytic signal and enhanced versions
     - Tilt angle and theta maps
     - **Directional derivative methods** (Yuan & Geng, 2014; Yuan et al., 2015; Ekinci et al., 2013; Mazzoldi et al., 2020) – Critical addition
     - **Gradient tensor methods** (Kusumoto, 2016) – Important for caldera applications
   - Clearly identify gaps in existing methods that CHG addresses.
   - Explicitly state what is novel about CHG compared to directional derivatives.
   - Position CHG within the broader landscape of potential field interpretation methods.

2. **Rewrite Introduction**:
   - Expand to provide thorough background and motivation.
   - Structure logically:
     - Importance of gravity interpretation for circular structures
     - Review of existing edge detection methods
     - Limitations of existing methods (with citations or demonstrations)
     - Specific gap that CHG addresses
     - Clear statement of research objectives and contributions
   - Explain why radial-tangential distinction is geologically important.
   - Provide clear argumentation for why CHG is needed.

3. **Expand Method Section**:
   - Add conceptual explanation before equations:
     - Describe coordinate transformation from Cartesian to center-referenced
     - Explain geometric meaning of radial and tangential gradients
     - Discuss intuition behind the approach
   - Include schematic diagram showing:
     - Radial and tangential directions relative to center point
     - How horizontal gradients are decomposed
     - Coordinate system and notation
   - Provide step-by-step implementation procedure:
     - How to determine center point
     - How to calculate horizontal derivatives
     - How to compute CHGrad and CHGtan
     - How to interpret results
   - Discuss assumptions and limitations clearly.
   - Explain applicability conditions.

4. **Strengthen Discussion Section**:
   - Expand significantly to include:
     - Critical evaluation of method strengths and limitations
     - Detailed comparison with existing methods (especially directional derivatives)
     - Practical considerations for adoption
     - Guidelines for when CHG is appropriate vs. inappropriate
     - Potential failure modes and how to recognize them
     - Future research directions
   - Connect results back to broader context of potential field interpretation.
   - Discuss implications for volcanic and geothermal exploration.

5. **Add Proper Conclusions Section**:
   - Replace or supplement Section 8 (currently author contributions) with scientific conclusions.
   - Summarize key findings:
     - What does CHG enable that wasn't possible before?
     - What are the main results from synthetic and field tests?
     - What are the key limitations?
   - State implications for practice and future research.
   - Provide clear take-home messages.

6. **Improve Writing Quality Throughout**:
   - Fix grammatical errors and awkward phrasing.
   - Ensure consistent terminology (decide on "Centered Horizontal Gravity Gradient" and use consistently).
   - Fix capitalization errors ("Or" → "or").
   - Reduce passive voice; use active voice where appropriate.
   - Break up overly long, complex sentences.
   - Improve clarity and readability.
   - Have manuscript professionally edited if English is not authors' first language.

7. **Rewrite Abstract**:
   - Shorten to ~200-250 words.
   - Follow standard structure:
     - Background/motivation (1-2 sentences)
     - Objective (1 sentence)
     - Method (2-3 sentences)
     - Key results (2-3 sentences)
     - Conclusions/implications (1-2 sentences)
   - Remove unnecessary details (e.g., "synthetic model has been created").
   - Ensure terminology is consistent with title and body.
   - Make it self-contained and compelling.

8. **Fix Structural Issues**:
   - Add proper Conclusions section.
   - Move author contributions to end or acknowledgments.
   - Ensure section numbering and organization are logical.
   - Improve transitions between sections for better narrative flow.
   - Consider restructuring Results/Interpretation sections if they're confusing.

### Highly Recommended:

9. **Add Visual Aids**:
   - **Schematic diagram** explaining radial vs. tangential gradients (essential).
   - **Workflow diagram** showing implementation steps.
   - **Comparison table** summarizing CHG vs. other methods (advantages, disadvantages, use cases).
   - **Model parameter table** for synthetic tests.
   - **Data characteristics table** for field surveys.

10. **Expand Synthetic Testing Description**:
    - Provide complete quantitative description of models.
    - Explain what each test is designed to demonstrate.
    - Present results more systematically.
    - Include quantitative metrics where possible.

11. **Improve Field Data Description**:
    - Provide more information about gravity survey (acquisition, processing).
    - Explain how center point was determined for Samalas case.
    - Connect CHG results to known geological features more explicitly.
    - Consider adding comparison with published geological/geophysical models.

12. **Add Comparative Analysis**:
    - Apply at least one other method (directional THD or analytic signal) to same data.
    - Present side-by-side comparison.
    - Discuss relative advantages clearly.

13. **Include Reproducibility Information**:
    - Specify all parameters needed to reproduce results.
    - State whether code will be made available (ideally yes).
    - State whether data can be shared (or provide citation to data source).
    - Include detailed workflow description.

14. **Address Broader Impact**:
    - Add brief discussion of ethical considerations (data sharing, reproducibility).
    - Mention plans for code/data release to support open science.
    - Discuss accessibility of method to broader community.
    - Acknowledge potential for misinterpretation and how to avoid it.

### Recommended Enhancements:

15. **Improve Figure Quality and Integration**:
    - Ensure all figures have detailed, self-contained captions.
    - Reference figures explicitly in text at appropriate points.
    - Add quantitative annotations to figures.
    - Consider adding profile plots or difference maps.

16. **Expand Reference List**:
    - Include more recent papers (2020-2025).
    - Add missing key references on directional derivatives and gradient tensors.
    - Ensure comprehensive coverage of edge detection literature.

17. **Add Supplementary Materials**:
    - Detailed model specifications
    - Extended methodology
    - Additional test cases
    - Code implementation
    - Sample datasets

18. **Consider Adding**:
    - Limitations subsection in Discussion
    - Future Work subsection in Discussion or Conclusions
    - Practical Guidelines box or appendix
    - Glossary of terms for interdisciplinary readers

19. **Improve Keywords**:
    - Fix "Concentrated" → "Centered" (if that's correct).
    - Add more specific keywords (e.g., "volcanic calderas," "geothermal exploration," "potential field interpretation").
    - Ensure keywords match terms readers would search for.

20. **Strengthen Geological Context**:
    - Explain why Samalas is an ideal test case more clearly.
    - Connect CHG results to volcanic processes and evolution.
    - Discuss implications for understanding Samalas eruption and structure.
    - Relate findings to broader volcanic/geothermal exploration context.

---

## Questions for Authors

1. **Terminology**: Is the correct term "Centered Horizontal Gravity Gradient" (title) or "Centered Horizontal Gravity" (abstract)? Why does "Concentrated" appear in keywords? Please clarify and use consistently.

2. **Literature Positioning**: Are you aware of directional derivative methods (Yuan & Geng, 2014; Yuan et al., 2015; Ekinci et al., 2013)? How does CHG differ from or relate to these approaches? Why were these not cited or compared?

3. **Novelty**: Is the claim that "THG cannot distinguish between radial and tangential gradients" your original observation, or is it documented in prior literature? If original, can you demonstrate this more rigorously?

4. **Center Point**: How exactly did you determine the center point for the Samalas case study? Can you provide an objective, reproducible method?

5. **Comparison**: Have you applied other edge detection methods (analytic signal, tilt angle, directional THD) to the Samalas data? If so, why aren't comparisons shown? If not, why not?

6. **Validation**: Can you compare your CHG interpretation with published geological maps or geophysical models of Samalas (Lavigne et al., 2013; Mutaqin et al., 2019)? Do CHG features correspond to known structures?

7. **Scope**: Have you tested CHG on elliptical or irregular features? What are the limits of applicability?

8. **Reproducibility**: Will you make code and/or data available? What information is needed for others to reproduce your results?

9. **Practical Guidance**: Can you provide guidelines for when practitioners should use CHG vs. other methods? What are the key considerations?

10. **Future Work**: Do you plan to extend CHG to magnetic data or 3D gradient tensors? What are the next steps for this research?

11. **Broader Impact**: Have you considered ethical aspects such as data sharing, open source code release, and potential for misuse? How will you ensure the method is accessible and used appropriately?

12. **Writing**: Would you consider having the manuscript professionally edited for English language and clarity? This would significantly improve readability and impact.

---

## Rating: 4/10 (Reject, but encourage major revision and resubmission)

**Justification:**

The manuscript presents a conceptually interesting and potentially valuable methodological contribution (center-referenced radial/tangential gradient decomposition). However, it suffers from critical weaknesses in presentation, literature positioning, and contextual framing that prevent recommendation for publication in its current form.

**Key reasons for rejection:**

1. **Inadequate literature positioning**: Missing critical citations to directional derivative and gradient tensor methods; novelty not clearly articulated; relationship to existing approaches unclear.

2. **Poor writing quality**: Numerous grammatical errors, inconsistent terminology, awkward phrasing, and structural problems significantly impede clarity and understanding.

3. **Insufficient context and explanation**: Introduction too brief; method section lacks detail; discussion weak; no proper conclusions; limited guidance for readers.

4. **Weak argumentation**: Claims about THG limitations not rigorously supported; advantages of CHG not clearly demonstrated; contribution not compellingly presented.

5. **Missing elements**: No schematic diagrams, no workflow guidance, no comparative analysis, no broader impact discussion, no reproducibility information.

**Path forward:**

The manuscript requires **major revision** focusing on:
- Comprehensive literature review and clear positioning relative to directional derivatives and gradient tensors
- Complete rewriting of Introduction, Method, and Discussion sections with much more detail
- Addition of proper Conclusions section
- Thorough editing for writing quality, consistency, and clarity
- Addition of schematic diagrams and other visual aids
- Comparative analysis with existing methods
- Reproducibility and broader impact considerations

**Potential after revision:**

With substantial revision addressing these issues, the manuscript could become a solid methodological contribution. The core concept has merit, but the presentation and positioning need to be brought up to the standards of *Computers and Geosciences*.

---

## Confidence: 4/5 (High Confidence)

I am confident in this assessment based on:

1. **Expertise in scientific communication**: I can assess writing quality, structural organization, and clarity effectively.

2. **Knowledge of literature**: Through comprehensive review of 188 papers (2000-2025), I can identify gaps in literature coverage and positioning issues.

3. **Understanding of publication standards**: I know what is expected for methods papers in high-quality geophysics journals.

4. **Experience with interdisciplinary work**: I understand the challenges of communicating across geophysics, geology, and applied domains.

**Slight uncertainty (4/5 rather than 5/5) because:**
- I cannot directly view the figures, so my assessment of visual presentation is based on textual descriptions.
- Some presentation issues might be artifacts of PDF parsing rather than actual manuscript problems.
- The authors may have additional context or justifications not fully captured in the manuscript text.

Nevertheless, I am highly confident that the presentation, positioning, and contextual weaknesses identified are substantial and must be addressed for publication.
