# 📅 6-Month Learning Plan (PhD Student)

**Topic:** Seismology & Tectonic System in Eastern Indonesia (NTT, PLAI–SOEI–MMRI–KAPI Stations, Lewotobi Volcano)
**Target:** Ready to process waveform data in **Month 7**

---

## 📌 Struktur Mingguan

### **Month 1 — Fundamentals of Geophysics & Seismology**

* **Week 1**:

  * Study: Tectonic framework of Eastern Indonesia (Flores back-arc, Timor subduction).
  * Deliverable: 2–3 page summary on NTT tectonics.
* **Week 2**:

  * Study: Seismic waves (P, S, surface), travel times.
  * Deliverable: Diagram of wave types + notes.
* **Week 3**:

  * Study: Seismic recording systems, channels (EHZ, EHN, EHE), sampling.
  * Deliverable: Summary of PLAI, SOEI, MMRI, KAPI station specs.
* **Week 4**:

  * Study: Waveform formats (miniSEED, SAC). Install **ObsPy**.
  * Deliverable: Script to load waveform using `obspy.read()`.

---

### **Month 2 — Data Handling & Signal Processing**

* **Week 5**: Filtering (bandpass, high/low-pass, Butterworth).

  * Deliverable: Script to filter noise.
* **Week 6**: Instrument response removal (counts → ground motion).

  * Deliverable: Script `remove_response`.
* **Week 7**: Frequency analysis (FFT, STFT).

  * Deliverable: Spectrogram plot of an IRIS earthquake.
* **Week 8**: Event detection basics (STA/LTA).

  * Deliverable: Event detection script.

---

### **Month 3 — Event Processing & Catalog Building**

* **Week 9**: Manual phase picking (P, S).

  * Deliverable: Marked picks on PLAI waveform.
* **Week 10**: Automatic picking (AIC, Baer-Kradolfer).

  * Deliverable: Compare auto vs manual picks.
* **Week 11**: Basic location (3-station travel-time triangulation).

  * Deliverable: Locate 3 events with PLAI–SOEI–MMRI.
* **Week 12**: Add IRIS KAPI station.

  * Deliverable: Event locations with 4 stations.

---

### **Month 4 — Tectonic & Volcanic Analysis**

* **Week 13**: Seismotectonics of NTT.

  * Deliverable: Tectonic map + correlation notes.
* **Week 14**: Volcanic vs tectonic signals.

  * Deliverable: Examples from Lewotobi/IRIS datasets.
* **Week 15**: Local magnitude (ML).

  * Deliverable: Script to compute ML.
* **Week 16**: Event catalog draft.

  * Deliverable: 10-event catalog table.

---

### **Month 5 — Statistics & Visualization**

* **Week 17**: Magnitude–frequency distribution (Gutenberg–Richter law).

  * Deliverable: b-value plot.
* **Week 18**: Visualization (maps, cross-sections with GMT/Matplotlib).

  * Deliverable: Seismicity plot.
* **Week 19**: Correlation with Flores fault system.

  * Deliverable: Short report with map.
* **Week 20**: Discriminating volcanic vs tectonic signals.

  * Deliverable: Comparison table + waveform examples.

---

### **Month 6 — Integration & Mini-Project**

* **Week 21**: Data QC (gaps, overlaps, noise).

  * Deliverable: Cleaning script.
* **Week 22**: Full pipeline (download → preprocess → detect → locate → catalog).

  * Deliverable: First complete pipeline script.
* **Week 23**: Aftershock clustering (ETAS or visual clustering).

  * Deliverable: Aftershock sequence plot.
* **Week 24**: Review & presentation.

  * Deliverable: 20-min seminar + final 6-month progress report.

---

## 📑 Template Laporan Mingguan

```markdown
# Weekly Progress Report
**Name:** [Student Name]  
**Week:** [e.g., Week 5]

## 1. Learning Goals
- [List of study topics]

## 2. Activities Completed
- [Scripts / readings / plots made]

## 3. Results
- [Key findings, outputs, screenshots if needed]

## 4. Challenges
- [Difficulties encountered]

## 5. Plan Next Week
- [Focus for next week]
```

---

## 🎯 Final Outcome (End of Month 6)

1. Mastery of **basic seismology & signal processing**.
2. Working **scripts for detection, filtering, picking, and location**.
3. Small **earthquake catalog** from PLAI, SOEI, MMRI, KAPI.
4. Ready to start **real data research** in Month 7.

---

Apakah Bapak ingin saya sekalian tambahkan **list textbook + online resources** (gratis) untuk tiap bulan supaya mahasiswa punya referensi bacaan wajib?


# 📚 **Learning Resources per Month**

## **Month 1 — Fundamentals of Geophysics & Seismology**

* **Textbook:**

  * *Introduction to Seismology* — Peter Shearer (2nd ed., Cambridge University Press). → sangat fundamental, mudah diikuti.
  * *An Introduction to Seismology, Earthquakes, and Earth Structure* — Stein & Wysession.

* **Online Resources:**

  * IRIS Seismology Skill-Building Workshop \[Free modules + data examples] → [https://www.iris.edu/hq/inclass/](https://www.iris.edu/hq/inclass/)
  * BMKG tectonic/earthquake maps (Indonesia context) → [https://inatews.bmkg.go.id/](https://inatews.bmkg.go.id/)

---

## **Month 2 — Data Handling & Signal Processing**

* **Textbook:**

  * *Signal Processing for Seismology* — Bormann (ed.) in IASPEI New Manual of Seismological Observatory Practice (NMSOP-2). Free online PDF.
  * *Practical Seismic Data Analysis* — Hua-Wei Zhou (covers filtering, spectra).

* **Online Resources:**

  * ObsPy Tutorials → [https://docs.obspy.org/tutorial/](https://docs.obspy.org/tutorial/)
  * USGS Digital Filtering guide (short intro) → [https://pubs.usgs.gov/of/2002/ofr-02-187/](https://pubs.usgs.gov/of/2002/ofr-02-187/)

---

## **Month 3 — Event Processing & Catalog Building**

* **Textbook:**

  * *Earthquake Location Methods* in *Modern Global Seismology* — Lay & Wallace.
  * *Seismic Data Analysis* — Öz Yilmaz (classic, but focus on exploration; skim relevant sections).

* **Online Resources:**

  * ObsPy phase picking tutorial → [https://docs.obspy.org/tutorial/code\_snippets/picker\_tutorial.html](https://docs.obspy.org/tutorial/code_snippets/picker_tutorial.html)
  * IRIS Earthquake Browser (for cross-checking catalogs) → [https://ds.iris.edu/ieb/](https://ds.iris.edu/ieb/)

---

## **Month 4 — Tectonic & Volcanic Seismology**

* **Textbook:**

  * *Volcano Seismology* — Zobin, 2012.
  * *Monitoring Volcanoes* — McNutt et al. (Cambridge Handbook of Volcano Seismology).

* **Online Resources:**

  * Global Volcanism Program (Smithsonian) → [https://volcano.si.edu/](https://volcano.si.edu/)
  * PVMBG reports (Lewotobi, NTT volcanoes) → [https://magma.esdm.go.id/](https://magma.esdm.go.id/)

---

## **Month 5 — Statistics & Visualization**

* **Textbook:**

  * *Statistical Seismology* — Kagan, Jackson, Mulargia.
  * *Quantitative Seismology* — Aki & Richards (advanced reference, select sections on magnitudes & frequency-magnitude relations).

* **Online Resources:**

  * Gutenberg–Richter law tutorial (IRIS) → [https://www.iris.edu/hq/inclass/lesson/316](https://www.iris.edu/hq/inclass/lesson/316)
  * GMT (Generic Mapping Tools) cookbook → [https://docs.generic-mapping-tools.org/](https://docs.generic-mapping-tools.org/)

---

## **Month 6 — Integration & Mini-Project**

* **Textbook:**

  * *Computational Seismology: A Practical Introduction* — Heiner Igel.
  * *Python in Geophysics* (ObsPy community examples, not formal book but very practical).

* **Online Resources:**

  * SeisBench (deep learning seismic toolbox) → [https://seisbench.readthedocs.io/](https://seisbench.readthedocs.io/)
  * GitHub repos: EQTransformer, PhaseNet (for future deep learning extension).

---

# 📑 **Reading Strategy**

* Minggu awal tiap bulan → baca bab fundamental dari buku utama.
* Minggu 2–3 → coba langsung contoh/script (ObsPy, GMT).
* Minggu terakhir → tulis **summary 1 halaman** apa yang dipelajari (untuk progress report).



