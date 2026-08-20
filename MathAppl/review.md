Berikut adalah daftar periksa (*checklist*) yang terstruktur berdasarkan komentar para *reviewer*. Format ini dirancang agar siap digunakan untuk melacak progres revisi naskah secara sistematis.

### 1. Justifikasi Pemodelan & Arsitektur

* [ ] **MMPP vs. ETAS Non-stasioner:** Tuliskan argumen eksplisit mengapa MMPP lebih dipilih dibandingkan model ETAS non-stasioner (mis. Kumazawa & Ogata, 2004).
* [ ] **Ablation Analysis:** Lakukan analisis untuk memisahkan dan mengukur kontribusi spesifik dari *probabilistic declustering* vs. penggunaan MMPP terhadap peningkatan performa model.
* [ ] **Perbandingan Model (Opsional tapi disarankan):** Bandingkan performa model yang diusulkan secara langsung dengan setidaknya satu model ETAS non-stasioner.
* [ ] **Risiko Double Counting:** Analisis dan bahas potensi *double counting* antara kejadian gempa pada *state* MMPP berfrekuensi tinggi (yang mungkin berupa sisa klaster/swarm) dengan komponen pemicuan ETAS pada Persamaan 12.

### 2. Machine Learning & Declustering Probabilistik

* [ ] **Domain Shift & Bias:** Tambahkan diskusi eksplisit mengenai keterbatasan pengklasifikasi ML yang dilatih pada data sintetik ETAS, termasuk risiko model mewarisi bias asumsi ETAS tersebut.
* [ ] **Uji Kekokohan (Robustness):** Evaluasi performa pengklasifikasi terhadap parameter simulasi ETAS atau bandingkan hasilnya dengan metode *stochastic declustering* (mis. Zhuang et al., 2002).
* [ ] **Kalibrasi ML:** Jelaskan secara persis bagaimana probabilitas pengklasifikasi dikalibrasi dan tunjukkan hasil kalibrasinya pada data validasi sintetik.
* [ ] **Propagasi Ketidakpastian:** Perjelas alur propagasi ketidakpastian dari ML ke LGCP/MMPP. Jika menggunakan metode *thinning* untuk propagasi, pertimbangkan untuk menggunakan lebih dari 12 realisasi agar representatif.

### 3. Formulasi Statistik & Likelihood

* [ ] **Justifikasi Poisson Likelihood:** Berikan turunan atau justifikasi matematis terkait penggunaan nilai fraksional ($\omega_k$) ke dalam *Poisson likelihood* pada model spasial LGCP.
* [ ] **Weighted MMPP Likelihood:** Tuliskan bentuk matematis secara eksplisit dari *weighted MMPP likelihood* yang digunakan, atau pertimbangkan untuk mengadopsi formulasi *latent-variable* (variabel Bernoulli).
* [ ] **Ambang Batas Kelengkapan (Mc):** Koreksi dan jelaskan inkonsistensi perhitungan matematis (pernyataan bahwa 3.3 + 0.2 menghasilkan *working threshold* 4.5).
* [ ] **Inkonsistensi Magnitudo:** Lakukan homogenisasi skala magnitudo pada katalog sebelum analisis dilakukan.

### 4. Resolusi Spasial (SPDE) & Interpretasi Temporal (MMPP)

* [ ] **Resolusi Mesh SPDE:** Berikan justifikasi (melalui analisis sensitivitas) mengapa *mesh* dengan 60 sel integrasi dianggap memadai untuk area seluas 1,93 juta km².
* [ ] **Pelabelan State MMPP:** Hapus istilah fisis seperti "post-megathrust" atau "quiescent tectonic" pada pendefinisian model awal. Gunakan deskripsi statistik seperti "low-rate state" dan "high-rate state".
* [ ] **Instabilitas Parameter:** Bahas perbedaan signifikan antara estimasi *maximum-likelihood* parameter $\lambda_2$ dengan nilai rata-rata dari *thinned realizations*.

### 5. Validasi, Pengujian, & Reproduksibilitas

* [ ] **Validasi Full Model:** Lakukan pengujian OEF (*N-Test*) menggunakan keseluruhan katalog gempa asli (*background* + *triggered*), bukan sekadar pada katalog hasil *declustering*.
* [ ] **Horizon Operasional:** Tampilkan performa prakiraan sebagai fungsi horizon waktu jangka pendek (mis. 1 hari, 7 hari, 30 hari, 90 hari) alih-alih hanya berfokus pada *N-Test* berdurasi 9 tahun.
* [ ] **Validasi Spasial:** Hitung ulang dan laporkan hasil *L-Test* dan *R-Test* spesifik untuk model spasial pada naskah ini, jangan hanya mengutip hasil dari *companion paper*.
* [ ] **Signifikansi Statistik:** Uji signifikansi perbaikan skor *prospective* (mis. *Information gain* 0.103 dan perubahan *Brier-score*).
* [ ] **Kemandirian Naskah:** Laporkan secara lengkap: parameter arsitektur ML (jumlah katalog, parameter ETAS penuh, *train/val/test splits*), parameter ETAS untuk Persamaan 12 (produktivitas, *spatial-triggering*), dan *hyperparameters* LGCP/SPDE.

### 6. Tinjauan Pustaka & Sitasi Baru

* [ ] **SPDE-ETAS:** Tambahkan diskusi mengenai metode *joint Bayesian inference* (Rahmani et al., 2026).
* [ ] **MMPP & Multistage ETAS:** Diskusikan penelitian Benali et al. (2020) dan Benali et al. (2022) terkait variasi *background rate*.
* [ ] **Diskritisasi SPDE & INLA:** Sitasi dan diskusikan referensi terkait dekomposisi data seismik menggunakan INLA (DOI: 10.1029/2024GL109418).
* [ ] **Model Prakiraan Operasional:** Bahas model peramalan lain seperti ORION di bagian Diskusi.

### 7. Teks, Notasi, & Perbaikan Minor

* [ ] Ubah istilah "*prospective*" menjadi "*pseudo-prospective*" atau "*retrospective out-of-sample*".
* [ ] Definisikan singkatan saat pertama kali muncul: LGCP, INLA, SPDE, AUC, TV, SML, GK.
* [ ] Definisikan variabel matematis secara lengkap: parameter pada Persamaan 3, $\gamma$, $\Delta LL$, $d_f$, $q$, dan $\delta^2$.
* [ ] Periksa dan konsistenkan notasi probabilitas: $p_j$, $p_k$, *background probabilities*, dan indeks *event* MMPP.
* [ ] Pecah kalimat yang terlalu panjang dan kompleks (terutama di Abstrak, baris 39-43).
* [ ] Perbaiki persentase di halaman 6 baris 234: $703/693 \approx 101.4\%$ (bukan 1.4%).
* [ ] Haluskan klaim-klaim mutlak seperti "*tectonically physical rate everywhere*" atau "*inherits declustering uncertainty*" jika belum dibuktikan secara langsung dalam analisis.

Apakah Anda ingin saya menjabarkan salah satu poin di atas ke dalam format paragraf revisi langsung?
