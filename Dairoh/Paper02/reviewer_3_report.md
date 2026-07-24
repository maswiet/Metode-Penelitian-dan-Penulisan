# Reviewer 3 Report — Clarity, Positioning & Broader Impact Specialist

**Paper Title:** Array-Based Dataset Construction for Machine Learning Classification of Long-Distance Volcanic Seismic Signals  
**Authors:** Dairoh, Sudarmaji, Ahmad Ashari, Wiwit Suryanto  
**Reviewer Expertise:** Scientific writing, research communication, literature positioning, broader impact, research ethics, geoscience outreach

---

## Summary

This paper presents a workflow for constructing validated labeled seismic datasets from a remote, low-cost array (Raspberry Shake sensors, ~16 km from Merapi Volcano, Indonesia) and evaluates SVM and XGBoost classifiers on the resulting 275-event dataset. The framework integrates STA/LTA detection, beamforming, FK analysis, and dual-catalogue validation. The paper is motivated by the practical challenge of building reliable training data for ML-based volcanic monitoring from remote stations, where signal quality is lower than at near-field networks. The best classification accuracy achieved is 72.73% (XGBoost, 80:20 split). The paper is a PhD student's manuscript draft and reflects genuine scientific effort, though it requires substantial revision in writing quality, literature positioning, and broader impact framing before it is ready for submission to a top-tier journal.

---

## Soundness: 3.0 / 5

The scientific logic of the paper is generally sound: the motivation is clear, the workflow is reasonable, and the results are honestly reported. The main soundness concern is the inconsistency between "chronological" and "stratified random" splitting, and the modest classification performance that is not fully contextualized against the literature.

---

## Presentation: 2.5 / 5

The manuscript has significant presentation issues that must be addressed: equations are not rendered (Tables 3–6 contain only placeholder numbers), several grammatical and typographical errors are present, some sentences are repetitive, and the related work section does not adequately cover the state of the art.

---

## Contribution: 3.0 / 5

The paper makes a genuine, practically motivated contribution by demonstrating the feasibility of remote array-based dataset construction for ML volcanic monitoring. The contribution is incremental but meaningful for the volcano monitoring community, particularly for resource-limited settings in Indonesia and Southeast Asia.

---

## Strengths

1. **Well-motivated research problem**: The introduction clearly articulates the challenge of near-field station vulnerability during eruptions and the need for remote monitoring alternatives. The motivation for developing a systematic dataset construction framework from remote arrays is convincing and practically relevant.

2. **Transparent and honest reporting**: The authors report all four train–test split scenarios, including the poorly performing 90:10 split, and acknowledge limitations in the conclusion. This transparency is commendable and reflects scientific integrity.

3. **Societal relevance**: Merapi is one of the world's most densely populated volcanic regions. Contributions to its monitoring infrastructure—particularly through low-cost, remotely deployable systems—have direct societal value for disaster risk reduction in Indonesia.

4. **Figures are informative**: The described figures (FK spectra, waveform comparisons, confusion matrices, learning curves, ROC curves, feature distributions) appear to provide a comprehensive visual summary of the results. The figure captions are generally detailed and informative.

5. **Clear workflow description**: The proposed framework is described step-by-step and illustrated in Figure 2, making it accessible to readers unfamiliar with array processing. The separation between dataset construction and classification is clearly explained.

6. **Authorship contributions are declared**: The CRediT authorship statement is included, which is good practice for transparency.

7. **AI use disclosure**: The declaration of generative AI use (Grammarly and Claude for grammar/readability) is appropriately disclosed, reflecting adherence to emerging publication ethics norms.

---

## Weaknesses

### W1: Related Work Section Is Inadequate and Missing Key References
The related work is embedded in the introduction rather than presented as a dedicated section, and it omits several seminal and recent works that are directly relevant:

- **Malfante et al. (2018)** – "Automatic Classification of Volcano Seismic Signatures" (JGR Solid Earth) — the most cited large-scale ML volcanic classification study, directly comparable to this work.
- **Titos et al. (2019)** – "Detection and Classification of Continuous Volcano-Seismic Signals with Recurrent Neural Networks" (IEEE TGRS) — key deep learning benchmark.
- **Espinosa-Curilem et al. (2024)** – Multi-station real-time framework for volcano-seismic event recognition — most recent comparable framework.
- **Smith & Bean (2020)** – RETREAT: A Real-Time Tremor Analysis Tool for Seismic Arrays — directly comparable array processing tool.
- **Ohrnberger (2001)** – "Continuous automatic classification of seismic signals of volcanic origin at Mt. Merapi" — directly relevant Merapi ML baseline.
- **Langer et al. (2009)** – SVM benchmark on Mt. Etna volcanic tremor.
- **Manley et al. (2022)** – "A Deep Active Learning Approach to the Automatic Classification of Volcano-Seismic Events."

The absence of these references means the paper does not adequately position itself within the existing literature and may mislead readers about the novelty of the work.

### W2: Inconsistency Between "Chronological" and "Stratified Random" Splitting
The abstract states "chronological train–test strategy," the conclusion states "chronological train–test strategy," but the Methods section describes "stratified random sampling." These are fundamentally different approaches. This inconsistency is not merely a writing issue—it reflects ambiguity about the actual experimental design. The authors must clarify and correct this throughout the manuscript.

### W3: Equations Are Not Rendered (Tables 3–6)
Tables 3–6 contain only equation numbers "(1)", "(2)", "(3)–(6)", "(7)–(8)" without any mathematical content. This is a critical formatting failure that makes the mathematical foundations of the paper inaccessible to reviewers and readers. All equations must be properly typeset and rendered.

### W4: Writing Quality Requires Improvement
Several writing issues are present throughout the manuscript:

- **Repetitive phrasing**: Key sentences describing the framework components are repeated almost verbatim in the abstract, introduction, methods, results, and conclusion. For example, the sentence "integrates STA/LTA event detection, beamforming, Frequency–Wavenumber (FK) analysis, and independent catalogue validation" appears in nearly identical form at least six times.
- **Typographical errors**: "Univeritas" (should be "Universitas") in affiliation 2; "Sciemces" (should be "Sciences") in reference [26]; "Leaming" (should be "Learning") in reference [47]; "occorred" (should be "occurred") in the XGBoost description.
- **Spelling error**: "Skweness" (should be "Skewness") in Table 1.
- **Inconsistent abbreviation**: "BPPTKG" and "PVMBG" are used interchangeably for the same agency; this should be standardized.
- **Incomplete sentence**: "Multiphase events are composed of emergent waveforms with gradually increasing amplitudes and long-lasting oscillatory cod." — "cod" appears to be a truncated word (likely "coda").
- **Redundant phrase in Figure 7(b) description**: The sentence "variations are observed in the dominant-frequency peaks, spectral-energy distribution, and spectral amplitudes" is repeated twice in the same paragraph.

### W5: The Title Does Not Fully Reflect the Paper's Content
The title "Array-Based Dataset Construction for Machine Learning Classification of Long-Distance Volcanic Seismic Signals" emphasizes dataset construction but the paper also presents classification results. A more accurate title might be: "Array-Based Framework for Validated Dataset Construction and Machine Learning Classification of Long-Distance Volcanic Seismic Signals at Merapi Volcano."

### W6: Abstract Overloads Technical Details
The abstract is 250+ words and contains excessive technical detail (e.g., specific sensor names, exact observation dates, exact event counts per class). For most journals, a 150–200 word abstract that highlights the key novelty, approach, and main finding is preferred. The abstract should be condensed and sharpened.

### W7: Broader Impact Is Not Discussed
The paper does not include a section or substantive discussion on:
- **Scalability**: Can the framework be applied to other volcanoes in Indonesia (Sinabung, Kelud, Anak Krakatau) or globally?
- **Operational deployment**: What would be needed to transition from this research prototype to an operational monitoring system?
- **Limitations for hazard assessment**: The 72.73% accuracy implies ~27% misclassification rate. What are the consequences of misclassifying VTB events as Non Event in a real monitoring context?
- **Ethical/societal considerations**: How would false alarms or missed detections affect evacuation decisions and public trust?

### W8: Overlap with Prior Publication [26] Is Not Adequately Addressed
Reference [26] (Dairoh et al., 2026, "Discrimination of Seismic Signals in UGM Antenna Station Recordings at Merapi Volcano Using a Remote Seismic Array: Beamforming and FK Analysis") uses the same array, the same 28-day dataset, and the same STA/LTA + beamforming + FK analysis pipeline to detect 442 candidate events. The current manuscript builds upon this but does not clearly delineate what is new. This creates a risk of self-plagiarism or redundant publication. The authors must explicitly state in the introduction what [26] did and what the current paper adds beyond it.

### W9: Table 1 Has Missing Content
Table 1 (features list) has empty "Definition" cells for all 11 features. The feature definitions are described in the text but should also be provided in the table for reader convenience. The "i from the energy center" feature name is unclear and likely refers to "temporal centroid" or "energy centroid"—this should be clarified.

### W10: Figure Captions Are Embedded in Text
Figure captions appear as regular text paragraphs in the body of the manuscript rather than as properly formatted captions below their respective figures. This is a formatting issue that must be corrected for journal submission.

### W11: References Have Quality Issues
Several references have formatting or content problems:
- Reference [1] (McNutt, 2005): The DOI points to a 2005 paper but the year in the DOI link says 2004 — verify.
- Reference [26]: Journal name "Trend In Sciemces" contains a typo ("Sciemces" → "Sciences").
- Reference [42]: The paper title contains a typo ("wth" → "with") and the page range "1–54" for a Scientific Reports article is unusual.
- Reference [47]: "Machine Leaming" should be "Machine Learning."
- Reference [29]: Listed as PVMBG but cited in the text as BPPTKG — these are different agencies and the citation should be consistent.
- Several references lack complete information (e.g., missing volume/page numbers for some journal articles).

---

## Suggestions

1. **Add a dedicated Related Work section**: Restructure the introduction to include a concise but comprehensive review of ML-based volcanic seismic classification, array processing for volcanic monitoring, and remote/low-cost monitoring systems. Cite the missing key references identified above.
2. **Resolve the chronological vs. stratified split inconsistency**: Clarify the actual approach used and correct all instances throughout the manuscript.
3. **Fix all typographical and grammatical errors**: Conduct a thorough proofreading pass, paying particular attention to the errors identified in W4 and W11.
4. **Condense and sharpen the abstract**: Reduce to 150–200 words focusing on novelty, approach, and key finding.
5. **Add a broader impact/limitations discussion**: Discuss scalability, operational deployment requirements, and the implications of misclassification for volcanic hazard assessment.
6. **Clearly differentiate from [26]**: Add a dedicated paragraph in the introduction explicitly stating what [26] accomplished and what the current paper adds.
7. **Complete Table 1**: Add feature definitions to all rows and clarify the "i from the energy center" feature name.
8. **Revise the title**: Make it more precise and reflective of the paper's full scope.
9. **Clean up references**: Fix all typographical errors, standardize agency abbreviations (BPPTKG vs. PVMBG), and ensure all references are complete.
10. **Render all equations**: Ensure Tables 3–6 contain properly typeset mathematical expressions.

---

## Questions

1. The paper acknowledges using Claude (AI) for grammar and readability improvement. Can the authors confirm that the scientific content, interpretations, and conclusions are entirely the authors' own work and that AI was used only for language editing?
2. Is reference [26] (Dairoh et al., 2026) already published, under review, or in preparation? The 2026 date suggests it may be a concurrent or future submission. How does this relate to the journal submission timeline for the current manuscript?
3. The paper mentions "Antenna Gadjah Mada University (UGM)" — is this the officially recognized name of the array, or is it "UGM remote seismic array"? Consistent naming throughout the manuscript would improve clarity.
4. Are there plans to expand the dataset beyond 28 days and 275 events? If so, what is the expected timeline, and could this be incorporated into the current paper?
5. Has the proposed framework been tested or validated on any other volcano or array configuration, even informally? This would significantly strengthen the generalizability claims.

---

## Rating: 5 / 10 — Borderline Reject / Major Revision

**Key reasons:** The paper addresses a genuinely important practical problem and presents honest, transparent results. However, it requires major revision in: (1) writing quality (repetition, typos, incomplete sentences), (2) literature positioning (missing key references), (3) presentation (unrendered equations, formatting issues), and (4) broader impact discussion. The scientific contribution is real but modest, and the manuscript is not yet ready for submission to a top-tier journal. With substantial revision addressing the issues above, this paper could make a meaningful contribution to the volcanic monitoring literature.

---

## Confidence: High

I am highly confident in this assessment. The writing and presentation issues are clearly identifiable from the manuscript text, and the literature positioning gaps are verifiable against the published literature in volcanic seismic monitoring and machine learning.
