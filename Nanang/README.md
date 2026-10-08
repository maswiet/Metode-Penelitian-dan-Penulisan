# Putusan Meta Review

Naskah yang saya telaah adalah **“Dynamic Strain Across Central Sumatra: Magnitude Scaling, Station-Fixed Amplification, and Artifacts That Can Be Mistaken for Crustal Structure”** oleh Nanang Sugianto dan rekan-rekan. Main_Text-English_corr_MN

## **Jangan submit ke *Tectonophysics* dalam bentuk sekarang**

Simulasi rekomendasi saya sebagai reviewer:

> **Reject in present form — the central tectonic interpretation is not supported by the physical validity of the strain estimators. Fundamental reanalysis is required.**

Secara topik, naskah masih berada dalam koridor *Tectonophysics*, yang menekankan penelitian mengenai kinematika, struktur, komposisi, dan dinamika Bumi padat serta integrasi berbagai pendekatan geofisika dan geologi. [SciJournal](https://scijournal.org/tectonophysics) Namun, jurnal itu bukan tempat memajang peta berwarna yang sebagian besar kemudian diakui sebagai artefak. Ia membutuhkan inferensi struktur tektonik yang benar-benar bertahan terhadap kontrol fisik dan statistik.

Masalah naskah ini dapat diringkas dalam satu kalimat:

> **Penulis memakai medan regangan sesaat dari gelombang seismik yang lewat untuk menguji geometri deformasi tektonik jangka panjang, menggunakan wave gradiometry pada array yang secara terang-terangan melanggar sampling requirement, lalu tetap mempertahankan interpretasi segmen sesudah menunjukkan bahwa arah regangannya sebagian dikunci oleh bentuk segitiga stasiun.**

Itu bukan kelemahan kecil. Itu menyentuh ontologi observasi: **apa sebenarnya yang sedang diukur?**

| Komponen | Nilai |
|---|---:|
| Nilai dataset tiga jaringan | 4.5/5 |
| Relevansi masalah dynamic strain | 4/5 |
| Kejujuran terhadap hasil negatif | 4.5/5 |
| Validitas fisik plane-wave estimate | 2/5 |
| Model phase velocity | 1.5/5 |
| Validitas spatial-gradient method | **0.5/5** |
| Statistik amplitude scaling | 1.5/5 |
| Identifikasi station effect | 2/5 |
| Validitas interpretasi tektonik | **0.5/5** |
| Reproducibility | 1.5/5 |
| Kualitas dokumen submission | 1.5/5 |
| Kesiapan untuk *Tectonophysics* | **1/5** |

---

# Bagian yang memang bagus

## 1. Dataset-nya bernilai

Penggunaan 29 gempa dan hingga 119 stasiun dari jaringan ZB, 7A, dan GE memberikan kesempatan langka untuk melihat stabilitas pola amplitude pada banyak sumber dan azimut. Pemisahan sumber lokal SFS, forearc, dan teleseismik juga secara konseptual berguna. Main_Text-English_corr_MN

## 2. Penulis berani membunuh sebagian ceritanya sendiri

Naskah secara eksplisit menunjukkan bahwa:

- pola pembalikan utara–selatan pada forearc sebagian besar merupakan residual jarak;
- kontras orientasi island–basin tidak dapat dipisahkan dari geometri triplet;
- SGM menghasilkan amplitude hanya sekitar 0.1–0.2 kali PWM;
- station-fixed amplification tidak dapat dipisahkan dari instrumen;
- dan beberapa inferensi awal tentang struktur harus ditarik kembali.

Main_Text-English_corr_MN

Ini kualitas ilmiah yang baik. Banyak naskah akan menyembunyikan hasil tersebut.

## 3. Temuan terkuat sebenarnya bersifat metodologis

Naskah menunjukkan bahwa peta dynamic strain dari regional sparse network dapat menghasilkan pola yang tampak geologis akibat:

- distance trend;
- heterogeneous station geometry;
- spatial aliasing;
- network/instrument differences;
- dan source-dependent wavefield.

Ini potensial menjadi paper yang kuat.

Masalahnya: manuscript masih berusaha mempertahankan sedikit interpretasi Sumpur–Sumani–Suliti dari metode yang fondasi fisiknya belum sah.

> **Setelah kapal tenggelam, penulis masih mencoba menjual tiga kursi yang terapung sebagai peta dasar laut.**

---

# Komentar fatal 1 — Dynamic wave strain bukan tectonic strain field

Naskah menguji apakah orientasi principal strain \(\varepsilon_1\) berada sekitar \(45^\circ\) terhadap strike SFS, sesuai ekspektasi simple shear, dan kemudian menafsirkan deviasi sebagai kemungkinan pengaruh bend atau step-over. Main_Text-English_corr_MN

Ini merupakan **category error**.

Untuk gelombang bidang,

\[
\mathbf{u}(\mathbf{x},t)
=
\mathbf{p}\,f(t-\mathbf{s}\cdot\mathbf{x}),
\]

dengan \(\mathbf{p}\) sebagai polarisasi dan \(\mathbf{s}\) sebagai slowness vector. Gradien displacement-nya adalah

\[
\frac{\partial u_i}{\partial x_j}
=
-v_i s_j,
\]

sehingga strain tensor sesaat adalah

\[
\varepsilon_{ij}
=
-\frac{1}{2}
\left(v_i s_j+v_j s_i\right).
\]

Artinya, orientasi principal dynamic strain dikontrol oleh:

- arah rambat gelombang;
- polarisasi;
- jenis fase;
- incidence angle;
- source mechanism;
- interferensi antarwave packet;
- dan struktur sepanjang lintasan.

Ia **tidak** secara umum harus mengikuti orientasi strain tektonik regional.

Untuk P wave, principal strain terutama mengikuti ray direction. Untuk S wave, principal axes dapat berorientasi sekitar \(\pm45^\circ\) terhadap kombinasi arah rambat dan polarisasinya. Untuk Rayleigh dan Love waves, tensor strain berubah sepanjang siklus dan bergantung pada ellipticity serta mode.

Jadi baseline:

\[
\delta\theta=45^\circ
\]

terhadap strike sesar bukan null hypothesis universal untuk sebuah **passing seismic wavefield**.

Andersonian simple shear menjelaskan state of deformation atau stress akibat fault kinematics. Ia bukan prediksi orientasi instantaneous strain dari gempa lain yang gelombangnya kebetulan lewat di atas segmen tersebut.

> **Anda sedang membandingkan arah getaran karpet ketika diinjak seseorang dengan arah deformasi permanen lantai di bawahnya. Keduanya sama-sama “deformation”, tetapi bukan observasi yang sama.**

### Konsekuensi

Seluruh interpretasi berikut belum mempunyai fondasi:

- Sumpur fault-perpendicular response;
- Sumani–Suliti releasing step-over response;
- deviation from simple shear;
- hubungan dengan pull-apart basin;
- pembandingan dengan anisotropy Tarutung.

Naskah sendiri menemukan bahwa orientasi berkorelasi dengan longest side triplet dan cenderung terkunci tegak lurus terhadapnya. Main_Text-English_corr_MN

Sebelum faktor tersebut dimodelkan secara sintetis, tidak ada alasan memilih interpretasi tektonik dibanding wavefield geometry.

### Perbaikan wajib

Bangun baseline sintetis untuk setiap kombinasi:

\[
(\text{event},\text{triplet},f,\text{back azimuth},\text{wave type}),
\]

menggunakan plane P, SV, SH, Rayleigh, dan Love waves dengan geometri stasiun sebenarnya.

Baru kemudian hitung:

\[
\Delta\theta_{\rm residual}
=
\theta_{\rm observed}
-
\theta_{\rm synthetic\,geometry}.
\]

Hanya residual yang melampaui uncertainty sintetis yang boleh dibandingkan dengan struktur geologi.

---

# Komentar fatal 2 — Spatial Gradient Method secara fisik tidak valid pada array ini

Naskah melaporkan:

- median dominant wavelength local sekitar 4 km;
- regional sekitar 28 km;
- teleseismic sekitar 57 km;
- median longest side triplet sekitar 50–61 km;
- hanya **0.1%** triplet memenuhi quarter-wavelength condition.

Main_Text-English_corr_MN

Itu bukan sekadar “keterbatasan”.

Itu berarti sampling theorem dilanggar oleh hampir seluruh observasi.

Untuk gelombang bidang satu dimensi,

\[
u(x)=A e^{ikx},
\]

centered finite difference pada baseline \(L\) menghasilkan respons terhadap true derivative sebesar

\[
\frac{D_Lu}{du/dx}
=
\frac{\sin(kL/2)}{kL/2}.
\]

Faktor ini adalah fungsi sinc.

Jika:

\[
L=\lambda/4,
\]

responsnya masih sekitar 0.90. Tetapi bila \(L\sim\lambda\), respons dapat mendekati nol. Bila \(L>\lambda\), respons dapat:

- teredam berat;
- berubah tanda;
- mengalami spatial aliasing;
- dan mengubah arah inferred gradient.

Untuk local events:

\[
\frac{L}{\lambda}
\sim
\frac{50}{4}
=
12.5.
\]

Ini bukan “sedikit melewati syarat”. Ini penghancuran total terhadap asumsi linear-gradient.

Naskah memang mendapatkan rasio SGM/PWM hanya 0.1–0.2. Main_Text-English_corr_MN Itu bukan kejutan ilmiah dan bukan hanya akibat noise. Itu tepat perilaku low-pass spatial differencing ketika baseline jauh lebih besar daripada wavelength.

> **Condition number tidak dapat membatalkan sampling theorem. Menamai segitiga sebagai “good” tidak membuat gelombangnya menjadi lebih panjang.**

## Klasifikasi “good”–“moderate” menyesatkan

Triplet disebut “good” hingga:

\[
\kappa\le9000,\qquad L_{\max}\le150\ {\rm km}.
\]

Moderate bahkan diizinkan sampai 180 km. Main_Text-English_corr_MN

Untuk wavelength local 4 km, batas “good” 150 km adalah sekitar:

\[
37.5\lambda.
\]

Itu bukan good. Itu **catastrophically undersampled**.

Condition number hanya mengukur stabilitas aljabar inversi geometri. Ia tidak mengukur kemampuan array merekonstruksi wavefield yang sudah teralias.

Yang lebih memalukan, tier “moderate” pada event pengecekan mempunyai korelasi PWM–SGM 0.83, lebih tinggi daripada “good” 0.70. Main_Text-English_corr_MN Itu menunjukkan label tier belum tervalidasi sebagai ordered quality scale.

## Bootstrap tidak menyelamatkannya

Time-block bootstrap mengukur repeatability terhadap perubahan sample waktu. Ia tidak mengukur:

- spatial aliasing;
- finite-baseline bias;
- wavefront curvature;
- multimode interference;
- atau orientation locking akibat geometry.

> **Bootstrapping an aliased estimate only produces a precise estimate of the wrong answer.**

### Putusan atas SGM

Dalam bentuk sekarang:

- absolute amplitude SGM harus dibuang;
- orientation analysis SGM belum layak untuk interpretasi tektonik;
- deformation-type classification belum mempunyai arti struktural;
- forearc island–basin analysis lebih baik dipindahkan menjadi demonstrasi artefak.

SGM baru dapat dipertahankan setelah dilakukan full synthetic transfer-function analysis pada setiap triplet.

---

# Komentar fatal 3 — Plane-Wave Method belum didefinisikan sebagai tensor strain yang dapat diaudit

Metode utama dijelaskan hanya sebagai ground velocity yang dibagi phase velocity. Penghitungan dilakukan pada Z, N, E, R, dan T; selanjutnya \(\varepsilon_H\) dibentuk dari kombinasi envelope N dan E. Main_Text-English_corr_MN

Namun core equations tidak disajikan di main text.

Tidak jelas:

- apakah \(\varepsilon_Z\) adalah vertical normal strain, vertical shear strain, atau sekadar \(v_Z/c\);
- bagaimana N dan E digabung;
- apakah tensor rotation dilakukan;
- apakah factor \(1/2\) pada shear strain diperhitungkan;
- bagaimana slowness vector ditentukan;
- bagaimana incidence angle ditangani;
- mengapa R/T serta N/E sama-sama dianalisis;
- dan apa tepatnya yang dimaksud “maximum seismic strain”.

Membagi particle velocity dengan phase velocity memang dapat menghasilkan satu spatial derivative untuk satu plane wave dengan slowness diketahui. Tetapi itu belum otomatis menghasilkan maximum principal strain.

Lebih serius lagi, phase-velocity model yang dipakai terutama merupakan Rayleigh-wave model. Namun metode diterapkan pada:

- vertical component;
- radial component;
- transverse component;
- N/E mixtures;
- local Lg;
- regional wavefields;
- dan teleseismic signals.

T component lebih dekat dengan Love/SH motion, bukan Rayleigh dispersion. Lg adalah superposisi guided crustal S waves, bukan satu fundamental Rayleigh mode. P dan S body waves membutuhkan body-wave slowness, bukan surface-wave phase velocity.

> **Satu lookup table tidak boleh dipaksa menjadi paspor diplomatik bagi semua fase gelombang.**

### Yang wajib dilakukan

Pisahkan analisis menurut wave type:

1. P-wave strain;
2. S-wave strain;
3. Rayleigh-wave strain;
4. Love-wave strain;
5. Lg wavefield.

Gunakan slowness dan polarization yang sesuai bagi masing-masing. Bila fase tidak dapat dipisahkan, sebut output sebagai:

> **velocity-to-apparent-strain proxy**

bukan maximum seismic strain tensor.

---

# Komentar fatal 4 — Phase-velocity model merupakan campuran observasi, group velocity, dan model substitute

Pipeline yang digunakan terdiri atas:

- two-station FTAN pada 5–50 s;
- apparent velocity dari Lg arrival di bawah 5 s;
- PREM untuk teleseismic long periods;
- CRUST1.0 forward modelling untuk coverage gaps;
- dan penggantian period 12 dan 15 s dengan nilai CRUST1.0.

Main_Text-English_corr_MN

Ini bukan satu empirical phase-velocity model. Ini adalah **patchwork velocity table**.

## Masalah spesifik

### 1. Lg arrival velocity bukan Rayleigh phase velocity

Nilai:

\[
c_{Lg}=2.978\pm0.148\ {\rm km\,s^{-1}}
\]

diturunkan dari Lg arrival times. Main_Text-English_corr_MN

Itu lebih dekat kepada apparent group/travel velocity suatu wave packet multipath. Menggunakannya sebagai phase velocity dalam hubungan strain \(v/c\) memerlukan justifikasi yang jauh lebih kuat.

### 2. Two-station geometry belum cukup dijamin oleh beda back azimuth ≤12°

Metode two-station phase velocity membutuhkan kedua stasiun berada dekat satu great-circle source–receiver path. Beda back azimuth 12° pada separation ratusan kilometer dapat menghasilkan substantial off-path propagation, terutama di margin heterogen Sumatra.

### 3. Anomali 12 dan 15 s diganti model karena hasil datanya tidak nyaman

Naskah menemukan bimodality pada 12 dan 15 s, kemudian mengganti nilai tersebut dengan CRUST1.0. Main_Text-English_corr_MN

Itu bukan “handling uncertainty”. Itu membuang hasil observasi yang tidak cocok dengan satu-curve assumption lalu mengisinya dengan model.

Pilihan yang ilmiah adalah:

- mempertahankan dua branches;
- membuat source-depth-dependent curves;
- mengeluarkan period itu dari strain estimation;
- atau memodelkan mode conversion.

Bukan mengganti data dengan angka yang kemudian dipakai untuk menyatakan kurva empirical dekat dengan CRUST1.0.

### 4. CRUST1.0 pada Tarutung bukan model seluruh Sumatra

Path data melintasi forearc, arc, Toba, SFS, offshore islands, dan regional sources. Satu profile CRUST1.0 pada koordinat Tarutung tidak mewakili seluruh raypath.

### 5. “Lebih dekat ke CRUST1.0 daripada PREM” bukan validasi besar

Pada periode yang sensitif terhadap kerak, kurva regional lebih dekat ke crustal compilation dibanding whole-Earth average bukanlah penemuan struktural yang mengejutkan.

### Perbaikan

Pisahkan velocity curves berdasarkan:

- source depth;
- source region;
- path azimuth;
- wave type;
- dan network subarray.

Propagasi seluruh velocity uncertainty ke strain uncertainty. Jangan hanya memberi 8% pada dua period yang diganti model.

---

# Komentar fatal 5 — Magnitude scaling 1.11 belum dapat dipercaya

Hasil headline adalah:

\[
\log_{10}\varepsilon
=
-13.41+1.11M,
\qquad
R^2=0.84.
\]

Naskah memperoleh nilai itu dari 21 events setelah setiap event dinormalisasi ke 300 km menggunakan decay slope event tersebut. Main_Text-English_corr_MN

Masalahnya bertumpuk.

## 1. Magnitude scale dicampur

Table 1 mencampurkan:

- \(M_w\);
- \(m_b\);
- \(M_{Lv}\).

Main_Text-English_corr_MN

Ketiga skala itu tidak interchangeable, terutama pada rentang 4–6 dan pada source classes berbeda. \(m_b\) dapat saturate dan \(M_L\) mempunyai calibration regional tersendiri.

Naskah mengakui masalah ini, tetapi tetap menjadikan slope 1.11 sebagai headline. Main_Text-English_corr_MN

## 2. Event-specific decay line digunakan untuk membuat dependent variable baru

Setiap event memiliki:

\[
\log\varepsilon=a_e+b_e\log R.
\]

Nilai di 300 km kemudian dipakai sebagai observasi pada regression magnitude. Tetapi uncertainty \(a_e\) dan \(b_e\), serta covariance keduanya, tidak dipropagasikan.

Dengan kata lain, regression kedua memperlakukan fitted values dari regression pertama sebagai data tanpa error.

Ini dapat menggelembungkan \(R^2\).

## 3. Bandpass berbeda untuk setiap event

Optimal band events berkisar dari sekitar 0.02 Hz sampai hampir 10 Hz. Main_Text-English_corr_MN

Strain proxy kira-kira bergantung pada particle velocity dan wave slowness, sedangkan particle velocity spectrum sangat frequency-dependent. Membandingkan peak strain dari band berbeda berarti membandingkan target fisik berbeda.

Larger events juga cenderung mempunyai duration lebih panjang, dan kriteria overlap N/E disebut lebih ketat bagi event besar. Main_Text-English_corr_MN Ini menghasilkan magnitude-dependent missingness.

## 4. Magnitude, distance coverage, source class, dan frequency band saling confounded

Local events:

- magnitudenya lebih kecil;
- frekuensinya lebih tinggi;
- jaraknya lebih dekat;
- magnitude type-nya sering \(m_b/M_L\).

Regional events:

- umumnya \(M_w\);
- jaraknya lebih jauh;
- frekuensinya lebih rendah.

Jadi slope magnitude dapat menyerap source class dan band effect.

## 5. Decay slope bukan bukti langsung anelastic attenuation

Slope event berada pada \(-4.6\) sampai \(-1.0\), dengan median \(-1.7\), kemudian dikatakan lebih curam daripada geometric spreading dan mengimplikasikan anelastic attenuation. Main_Text-English_corr_MN

Attenuation fisik biasanya mempunyai bentuk frequency-dependent:

\[
A(R,f)
\propto
R^{-\gamma}
\exp\left(-\frac{\pi fR}{Qc}\right).
\]

Satu power-law slope pada mixed phase, mixed frequency, dan mixed path tidak dapat secara unik dipisahkan menjadi geometric spreading dan \(Q\).

### Model statistik yang diperlukan

Gunakan hierarchical model seperti:

\[
\log \varepsilon_{es}
=
\alpha
+\beta M_e
+g(\log R_{es})
+\eta\log f_e
+\zeta_{\rm magtype}
+\xi_{\rm sourceclass}
+b_s
+u_e
+\epsilon_{es},
\]

dengan:

- \(b_s\): station random intercept;
- \(u_e\): event/source effect;
- network/instrument fixed effects;
- event-specific distance slope bila didukung;
- uncertainty phase velocity;
- standardized magnitude scale atau separate magnitude-type slopes.

Tanpa model itu, slope 1.11 adalah exploratory number, bukan tectonophysical scaling law.

---

# Komentar fatal 6 — “Station-fixed amplification” belum diidentifikasi

Naskah menemukan correlation pola residual:

- \(+0.78\) antara northern dan southern regional sources;
- \(+0.33\) sampai \(+0.68\) antar-source classes.

Main_Text-English_corr_MN

Ini menarik. Tetapi penyebabnya tidak diketahui karena jaringan mencampurkan:

- ZB;
- 7A short-period sensors;
- GE broadband stations;
- installation berbeda;
- soil coupling berbeda;
- sensor response berbeda;
- station vault berbeda;
- dan frequency bands berbeda.

Instrument-response removal tidak otomatis menghapus:

- metadata gain error;
- orientation error;
- clipping;
- poor coupling;
- installation resonance;
- malfunctioning component;
- atau calibration inconsistency.

Site amplification sendiri juga frequency-dependent. Bila setiap event memakai band berbeda, “station-fixed” tidak otomatis berarti site term.

> **Sesuatu yang menetap pada sebuah kode stasiun belum tentu merupakan kerak. Bisa saja itu hanya sekrup, kabel, metadata gain, atau lubang instalasi yang sama.**

### Yang diperlukan

1. Fit crossed mixed-effects model dengan station dan event.
2. Masukkan network/sensor type sebagai fixed effect.
3. Ulangi pada common frequency bands.
4. Gunakan hanya stations yang merekam semua source classes.
5. Lakukan leave-one-event-out station-effect validation.
6. Bandingkan dengan:
   - HVSR;
   - geology;
   - Vs30;
   - topography;
   - station installation;
   - instrument model.
7. Kalibrasikan network offsets menggunakan common teleseismic events.

Sampai itu dilakukan, title boleh menggunakan:

> **station-associated residual amplification**

bukan:

> station/site amplification.

---

# Komentar fatal 7 — Peta utama dibuat menggunakan koreksi yang sudah diketahui salah

Manuscript memakai class-level distance trend untuk membuat `Amplif_H_distcorr`. Namun hasil menunjukkan bahwa individual regional-event slopes sangat bervariasi, dan sesudah event-specific trends dikeluarkan, pembalikan north–south hilang. Main_Text-English_corr_MN

Jadi penulis telah membuktikan bahwa koreksi yang dipakai untuk menghasilkan salah satu peta utama meninggalkan artefak.

Tidak cukup menampilkan peta yang keliru, lalu menulis beberapa halaman kemudian bahwa polanya bukan struktur.

Semua maps harus dibuat ulang menggunakan:

- event-specific distance residuals;
- uncertainty;
- source-radiation correction bila mungkin;
- common station set;
- dan common frequency band.

Natural-neighbour interpolation juga memberikan permukaan halus dari titik tidak merata tanpa menunjukkan uncertainty. Metode memang tidak extrapolate melewati convex hull, tetapi tetap menghasilkan kesan resolusi kontinu yang tidak dimiliki jaringan. Main_Text-English_corr_MN

Tampilkan:

- station points;
- sampling density;
- convex hull;
- interpolation uncertainty;
- leave-one-station-out residual;
- atau lebih aman, Voronoi cells.

> **Peta tidak menjadi struktur hanya karena warnanya halus.**

---

# Komentar fatal 8 — Statistiknya penuh pseudoreplikasi

Analisis segmen menggunakan:

- 1,715 triplet-event pairs;
- tetapi hanya 455 unique triplets;
- dan hanya delapan source areas.

Main_Text-English_corr_MN

Triplet juga saling overlap dan berbagi stasiun. Maka mereka bukan independent samples.

Mengambil median per unique triplet mengurangi pengulangan event, tetapi tidak menghilangkan:

- spatial autocorrelation;
- shared-station dependence;
- shared source;
- shared network geometry.

Forearc Rayleigh tests memakai 628 triplet-event pairs dari 151 unique triplets dan memperoleh p-values sangat kecil. Main_Text-English_corr_MN Dengan pseudoreplikasi sebanyak itu, p-value kecil hampir tidak informatif.

Gunakan:

- event-block bootstrap;
- station-block or spatial-block bootstrap;
- circular mixed-effects model;
- permutation by event/source area;
- leave-one-station-out;
- leave-one-event-out.

Unit inferensi utama seharusnya event atau independent subarray, bukan ribuan kombinasi triplet yang berbagi node.

---

# Komentar mayor 9 — Quality score adalah konstruksi arbitrary yang diberi seragam ilmiah

Composite score menggabungkan:

- energy capture;
- integrated SNR;
- bandwidth efficiency;
- spectral coverage.

Kemudian diberi label:

- Exceptional;
- Excellent;
- Very Good;
- Good;
- Fair.

Main_Text-English_corr_MN

Tidak ada bukti bahwa threshold 2, 3, 4, dan 5 berkorespondensi dengan tingkat strain accuracy tertentu.

Sitasi McNamara & Buland tentang ambient seismic noise tidak memvalidasi scoring formula buatan ini.

Table 1 bahkan melaporkan “integrated SNR” seperti:

- 13,955,197:1;
- 8,850,563:1;
- 1,138,552:1.

Main_Text-English_corr_MN

Angka seperti ini hampir pasti bukan SNR dalam penggunaan seismologi biasa. Ia mungkin ratio integrated spectral energy dengan denominator sangat kecil. Jangan menamainya SNR tanpa definisi dan calibration.

### Perbaikan

- Tampilkan formula score di main text.
- Laporkan setiap component sebelum weighting.
- Uji sensitivity terhadap weights.
- Gunakan conventional pre-event/post-event RMS or spectral SNR dalam dB.
- Validasi score terhadap known strain uncertainty atau manual QC.
- Hapus label “Exceptional”; gunakan nilai numerik atau pass/fail dengan alasan fisik.

---

# Komentar mayor 10 — “Independent methods” tidak benar

Abstract menyebut PWM dan SGM sebagai dua independent methods. Main_Text-English_corr_MN

Namun:

- memakai waveform yang sama;
- filter yang sama;
- window yang sama;
- phase timing yang sama;
- dan SGM quality thresholds justru dikalibrasikan menggunakan kesesuaiannya terhadap PWM.

Naskah sendiri mengakui agreement tersebut bukan independent validation. Main_Text-English_corr_MN

Gunakan:

> **two distinct estimators**

bukan:

> **two independent methods**.

---

# Komentar mayor 11 — Naskah terlalu penuh dan kehilangan satu kontribusi pusat

Di dalam satu paper terdapat:

1. event-quality scoring baru;
2. empirical phase-velocity model;
3. Lg analysis;
4. PWM strain maps;
5. SGM wave gradiometry;
6. magnitude scaling;
7. attenuation;
8. station effects;
9. forearc structure;
10. SFS segment orientation;
11. deformation-type classification;
12. comparison with anisotropy and geology.

Hasilnya: setiap komponen memperoleh analisis cukup panjang, tetapi tidak ada yang benar-benar selesai.

Paper terbaik yang dapat lahir dari dataset ini bukan “kami memetakan struktur Sumatra melalui dynamic strain”.

Paper terbaiknya adalah:

> **Sparse regional networks can generate compelling but false dynamic-strain structure through distance residuals, spatial aliasing, and array geometry.**

Itu fokus yang tajam, baru, dan jujur.

---

# Review per bagian

## Judul

Judul saat ini cukup jujur karena menyebut artifacts. Namun “Across Central Sumatra” tidak konsisten dengan cakupan data yang mencapai North Sumatra, Pagai, Sunda Strait, dan sumber teleseismik. Conclusion sendiri menyebut North-Central Sumatra. Main_Text-English_corr_MN

Judul yang lebih tepat:

> **Limits of Dynamic-Strain Mapping with Sparse Regional Networks: Distance, Aperture, and Geometry Artifacts in Sumatra**

atau:

> **Dynamic Strain from a Sparse Sumatran Network: What Plane-Wave and Wave-Gradiometry Estimates Can—and Cannot—Resolve**

## Abstract

Abstract sudah lebih baik daripada kebanyakan draft karena menyampaikan hasil negatif. Namun harus:

- menghapus “independent methods”;
- tidak mempromosikan segment-scale orientation;
- menjelaskan bahwa the 45° tectonic test itself is not physically justified;
- mengganti “station-fixed amplification” dengan station-associated residual;
- menonjolkan aperture failure sebagai hasil utama.

## Introduction

Kalimat bahwa combined network mempunyai density “sufficient to resolve spatial gradients” bertentangan langsung dengan hasil bahwa 99.9% triplet melanggar quarter-wavelength criterion. Main_Text-English_corr_MN

Kalimat itu harus dihapus.

Hipotesis \(45^\circ\) terhadap fault strike juga harus dihapus atau dirumuskan sebagai hypothesis yang diuji melalui full wavefield simulation, bukan static Andersonian assumption.

## Methods

Section numbering melompat dari **3.1** langsung ke **3.4**, kemudian 3.4.1 dan 3.4.2. Main_Text-English_corr_MN

Entah dua section hilang atau numbering belum diperbaiki. Untuk draft target jurnal, ini memalukan.

Core equations untuk PWM dan SGM juga harus berada dalam main manuscript, bukan diserahkan kepada supplement atau code.

## Results

Naskah tidak menonjolkan rentang absolute strain amplitude aktual. Paper bernama “Dynamic Strain”, tetapi reader lebih banyak melihat normalized amplification, ratios, dan orientation daripada angka strain fisis.

Laporkan:

- median;
- range;
- percentile;
- uncertainty;

dalam strain dimensionless untuk tiap source class dan wave type.

Teleseismic groups masing-masing hanya memiliki tiga events. Hentikan bahasa population-level; perlakukan sebagai case studies.

## Conclusions

Kesimpulan Sumpur, Sumani, dan Suliti harus diturunkan drastis. Bahkan manuscript mengakui:

- Sumpur tidak memiliki documented step-over;
- Sumani dan Suliti hanya marginal;
- geometry accounts for sebagian besar raw deviation;
- stricter restriction menyisakan Sumpur saja.

Main_Text-English_corr_MN

Kesimpulan yang aman:

> No segment-scale tectonic orientation can presently be isolated from source-wave and triplet-geometry effects.

Itu memang lebih negatif, tetapi benar.

---

# Masalah submission dan editorial

## 1. Beberapa figure tidak aman secara teknis

Saat saya render DOCX menjadi PDF pada lingkungan non-Microsoft, Figures 1–6 tidak tampil; halaman hanya menyisakan caption dan ruang kosong. File DOCX menyimpan banyak gambar sebagai EMF.

Elsevier akan membangun submission PDF secara otomatis. Jangan berasumsi bahwa file yang terlihat di satu komputer akan aman di server jurnal.

Konversikan semua figure menjadi:

- PDF/EPS vector untuk line art;
- TIFF/PNG resolusi tinggi untuk raster;
- embed permanen, bukan linked object.

## 2. Caption Figure 1 menyebut SF-1–12

Caption menyebut forearc SuF-1–12 dan SFS SF-1–12, tetapi Table 1 hanya mempunyai SF-1–11. Main_Text-English_corr_MN Main_Text-English_corr_MN

Audit seluruh IDs.

## 3. Table 1 tidak memuat tanggal/origin time

Untuk event catalogue yang menjadi fondasi paper, latitude–longitude–depth–magnitude saja tidak cukup. Reader tidak dapat mereproduksi event selection tanpa:

- origin time;
- catalogue event ID;
- magnitude type/source;
- focal mechanism source;
- station count.

## 4. Terminologi tidak konsisten

Contoh:

- SFS versus SFZ;
- `Metode Spatial Gradient`;
- `caƒnnot`;
- `sits is located`;
- Geophysics “Studi” Program;
- Central versus North-Central Sumatra.

Ini belum siap upload.

## 5. References belum diaudit

Terdapat, misalnya:

- dua versi referensi DeMets et al. 2010;
- format DOI yang tidak konsisten;
- volume JVGR Ryberg et al. tampak salah;
- campuran gaya bibliografi.

## 6. Data availability kontradiktif

Waveforms dikatakan tersedia dari public archives, tetapi bagian berikutnya menyatakan earthquake data tersedia from authors upon request. Main_Text-English_corr_MN

Yang harus dirilis:

- exact event catalogue;
- station list;
- waveform query manifest;
- processing code;
- phase-velocity table;
- all triplet definitions;
- strain estimates;
- quality flags;
- all regression inputs;
- map grids;
- random seeds;
- supplement;
- DOI repository.

---

# Analisis yang wajib sebelum submission

## 1. Synthetic transfer-function audit untuk SGM

Untuk setiap event–triplet:

1. gunakan exact station coordinates;
2. gunakan dominant frequency;
3. simulasikan plane P, SV, SH, Rayleigh, dan Love waves;
4. gunakan actual back azimuth;
5. hitung recovered amplitude dan orientation;
6. bandingkan dengan true tensor;
7. buat quality score berdasarkan actual error.

Quality criterion harus berupa misalnya:

\[
\left|
\frac{\varepsilon_{\rm recovered}}
{\varepsilon_{\rm true}}
-1
\right|<0.25
\]

dan

\[
|\Delta\theta|<10^\circ,
\]

bukan \(\kappa<9000\).

Kemungkinan hasilnya kejam: sebagian besar local-event triplets harus dibuang. Terima hasil itu.

## 2. Bangun ulang plane-wave estimator

- Sajikan tensor equation.
- Pisahkan fase.
- Gunakan wave-type-specific slowness.
- Jangan campur Rayleigh phase velocity dengan Love/Lg/body-wave measurements.
- Propagasikan uncertainty \(c\) ke \(\varepsilon\).
- Gunakan common passbands untuk perbandingan.

## 3. Hapus static 45° null model

Ganti dengan source-wave kinematic null derived from synthetics.

## 4. Gunakan hierarchical amplitude model

Fit seluruh station-event observations sekaligus, bukan two-stage regression.

Model harus mengandung:

- standardized magnitude;
- distance;
- frequency;
- source depth/class;
- station;
- network/instrument;
- event;
- phase velocity uncertainty.

## 5. Homogenisasi magnitude

Pilih salah satu:

- konversi seluruh magnitude menjadi \(M_w\) dengan documented relationships;
- gunakan seismic moment;
- atau fit magnitude-type-specific effects.

Jangan masukkan \(M_w\), \(m_b\), dan \(M_L\) ke satu garis lalu memperlakukan coefficient-nya sebagai hukum universal.

## 6. Estimasi station effect dengan benar

- common station subset;
- common frequency;
- mixed-effects model;
- network offsets;
- leave-one-event-out;
- external site proxies.

## 7. Buat ulang seluruh amplification map

Gunakan event-specific residuals. Jangan tampilkan class-level-corrected map yang diketahui menyimpan distance artifact.

## 8. Lakukan inference dengan unit independen

Bootstrap/permutation harus memblokir:

- events;
- stations;
- source areas;
- dan spatial triplet clusters.

## 9. Publikasikan reproducibility package

Tanpa code dan processed data, banyak threshold operasional tidak dapat diaudit.

---

# Storyline baru yang dapat menyelamatkan manuscript

Saya akan membuang sebagian besar klaim struktur dan membangun paper dengan alur berikut:

### Pertanyaan utama

> Under what conditions can dynamic strain be recovered from a sparse regional network, and which apparent tectonic patterns are generated by distance and geometry artifacts?

### Hasil utama

1. PWM amplitude requires wave-type-specific velocity and event-specific distance correction.
2. Class-level normalization creates false north–south structure.
3. Station-associated residuals repeat, but site and instrument effects remain inseparable.
4. SGM fails quantitatively where aperture exceeds wavelength.
5. Triplet geometry can impose apparent strain orientation.
6. Structural interpretation requires synthetic array-response correction.

### Nilai novelty

Bukan “first dynamic strain map of Sumatra”.

Melainkan:

> **A controlled demonstration of why sparse regional arrays can mimic crustal structure in dynamic-strain maps.**

Itu jauh lebih kuat.

---

# Pertanyaan yang harus dapat dijawab mahasiswa

1. Apa persamaan lengkap strain tensor pada PWM?

2. Apakah \(\varepsilon_Z\) merupakan \(\varepsilon_{zz}\), \(\varepsilon_{rz}\), atau hanya \(v_Z/c\)?

3. Mengapa Rayleigh phase velocity dipakai pada transverse motion?

4. Bagaimana Love, Rayleigh, Lg, P, dan S dipisahkan?

5. Apakah Lg arrival velocity merupakan phase velocity atau group velocity?

6. Mengapa hasil 12 dan 15 s diganti CRUST1.0 daripada dimodelkan sebagai dua populations?

7. Bagaimana satu CRUST1.0 profile di Tarutung mewakili seluruh paths?

8. Mengapa magnitudes \(M_w\), \(m_b\), dan \(M_{Lv}\) dimasukkan dalam satu regression?

9. Berapa slope magnitude jika hanya \(M_w\) digunakan?

10. Berapa slope jika analysis memakai common frequency band?

11. Berapa uncertainty normalized strain pada 300 km setelah decay-slope uncertainty dipropagasikan?

12. Mengapa power-law distance slope dianggap anelastic attenuation?

13. Berapa network/instrument contribution pada station-fixed term?

14. Apakah station effect bertahan setelah hanya satu instrument family digunakan?

15. Bagaimana triplet dengan side 150 km dapat disebut good untuk wavelength 4 km?

16. Apa spatial-transfer function triplet tersebut?

17. Mengapa condition number dapat memperbaiki aliasing?

18. Mengapa bootstrap waktu dapat mendeteksi bias spasial?

19. Apa prediksi orientation strain dari plane S wave yang datang dari source azimuth tertentu?

20. Mengapa instantaneous wave strain harus berada 45° terhadap fault strike?

21. Apa hasil orientation setelah source polarization dan propagation direction dikurangi?

22. Mengapa Sumpur signifikan bila tidak ada step-over terdokumentasi?

23. Apakah Sumpur merupakan discovery, atau hanya residual artifact yang belum dijelaskan?

24. Mengapa forearc Rayleigh tests menggunakan triplet-event pairs seolah-olah independen?

25. Apa independent unit of replication dalam penelitian ini?

26. Mengapa map menggunakan class-level correction setelah diketahui correction tersebut menyisakan near-source trend?

27. Berapa actual absolute strain ranges per source class?

28. Apa satu kesimpulan tektonik yang tetap berdiri apabila seluruh SGM result dihapus?

Pertanyaan nomor 28 adalah penentu.

Jawaban saat ini tampaknya:

> **Hampir tidak ada kesimpulan tektonik yang tersisa.**

Itu berarti SGM belum menjadi evidence; ia masih menjadi liability.

---

# Contoh komentar kepada editor

> **Recommendation: Reject in present form, with encouragement to resubmit after fundamental methodological reanalysis.** The manuscript uses a valuable multi-network data set and addresses an important question: whether dynamic strain and its orientation can be interpreted from a sparse regional seismic network. The authors commendably identify several apparent structural patterns as artifacts of distance correction and array geometry. However, the remaining tectonic interpretations are not supported by the physical validity of the estimators. Nearly all station triplets violate the quarter-wavelength small-aperture condition, with median triplet dimensions comparable to or much larger than the dominant wavelengths and only 0.1% of triplets satisfying the stated criterion. The observed SGM/PWM amplitude ratio of 0.1–0.2 is therefore consistent with severe finite-baseline attenuation and spatial aliasing. Condition-number thresholds and temporal bootstrap intervals do not correct this bias. In addition, the principal dynamic-strain orientation of a passing seismic wave is governed by propagation direction, polarization, phase type and source radiation; it is not generally expected to lie 45° from the local fault strike as in a static simple-shear model. The plane-wave estimator also combines Rayleigh-derived phase velocities, Lg arrival velocities and global-model substitutes across mixed body- and surface-wave components without presenting a complete tensor formulation. The magnitude-scaling result mixes \(M_w\), \(m_b\) and local magnitudes and compares event-dependent passbands through a two-stage regression without propagating distance-decay uncertainty. Finally, the station-fixed residual cannot be separated from network, instrument and installation effects. The manuscript could become a strong methodological paper on distance, aperture and geometry artifacts in sparse-network dynamic-strain mapping, but its current segment-scale tectonic interpretations should be removed or tested against full synthetic array-response calculations.

---

# Putusan akhir

## **Naskah mempunyai potensi kuat, tetapi bukan dalam bentuk sekarang**

Hal terbaik dari paper ini adalah bahwa penulis sudah menemukan bagaimana analisisnya sendiri dapat berbohong:

- distance correction dapat membuat batas kerak palsu;
- triangle geometry dapat membuat orientasi palsu;
- station identity dapat menyerupai site amplification;
- smoothing map dapat menyerupai struktur.

Itu sangat bernilai.

Namun manuscript masih melakukan kesalahan terakhir:

> **setelah membuktikan bahwa metodenya mudah menghasilkan artefak, ia tetap memilih beberapa residual dan menafsirkannya sebagai tektonik.**

## Rekomendasi saya

### **Reject and rebuild before submission.**

Bukan *English correction*. Bukan menambah dua paragraf limitations. Bukan mengganti color scale.

Yang dibutuhkan adalah:

1. mendefinisikan ulang observable secara fisik;
2. menghapus baseline 45° yang salah kategori;
3. melakukan synthetic wavefield recovery pada semua triplet;
4. mengganti regression magnitude dengan hierarchical model;
5. memisahkan station, network, frequency, dan source effects;
6. serta membangun paper sebagai audit keterbatasan sparse-network dynamic strain.

Kalimat paling keras tetapi paling jujur:

> **A condition number cannot repeal the sampling theorem. A p-value cannot turn transient wave polarization into tectonic strain. And a smooth colour map cannot convert an aliased spatial derivative into crustal structure.**
