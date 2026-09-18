# Laporan Review Disertasi — Dairoh (23/526467/SPA/00970)

**Naskah:** *Klasifikasi Gempa Vulkanik Gunung Merapi Menggunakan Machine Learning Berdasarkan Rekaman Sinyal Seismik Stasiun Antena UGM Jarak Jauh* (Versi 3A + 3B1 + 3B2, 2026)

**Peran reviewer:** seismolog + praktisi machine learning sinyal vulkanik. Saya keras terhadap naskah, bukan terhadap penulisnya. Semua angka di laporan ini saya hitung ulang sendiri dari naskah dan dari berkas hasil milik penulis; tidak ada yang saya kutip begitu saja.

---

## Putusan

> ### BELUM LAYAK MAJU UJIAN TERTUTUP.
> Bukan karena tulisannya berantakan — itu bisa dirapikan dalam seminggu. Melainkan karena **kontribusi utama yang diklaim (fitur spasial array) diukur pada pita frekuensi di mana array ini secara fisika tidak bisa mengukurnya**, dan karena **label kelas — target seluruh supervised learning — tidak pernah divalidasi jenisnya**, padahal penulis sendiri sudah punya bukti bahwa label itu 45% tidak cocok dengan BPPTKG.

| Aspek | Nilai |
| --- | ---: |
| Relevansi masalah & niat ilmiah | 4/5 |
| Kelayakan instrumen untuk pita yang dipilih | 0.5/5 |
| Kelayakan array untuk mengukur BAZ/slowness | 0/5 |
| Validitas label (ground truth) | 0.5/5 |
| Ketepatan statistik & pengujian hipotesis | 0.5/5 |
| Konsistensi angka antar bab | 1/5 |
| Ketepatan konsep seismologi | 1.5/5 |
| Kerapian & integritas dokumen | 0.5/5 |
| Kebaruan yang benar-benar terbukti | 1/5 |
| **Kesimpulan** | **Major revision berat — perlu analisis ulang, bukan perbaikan kalimat** |

---

# BAGIAN I — TIGA CACAT FATAL

## 1. Pita 0.8–1.8 Hz: menyaring data ke rentang di mana sensornya tuli

Naskah (4.3.3.1) menerapkan **Butterworth bandpass 0.8–1.8 Hz orde 4** pada semua sinyal. Sensornya (4.1) adalah geophone **Racotech RGI-20DX dengan frekuensi natural 4.5 Hz**.

Respons geophone terhadap kecepatan tanah turun sebagai *f²* di bawah frekuensi sudutnya. Dengan redaman standar *h* = 0.7:

| Frekuensi | Sensitivitas relatif | Relatif terhadap pita datar |
| ---: | ---: | ---: |
| 0.8 Hz | 0.032 | **−30.0 dB** |
| 1.3 Hz | 0.083 | **−21.6 dB** |
| 1.8 Hz | 0.158 | **−16.0 dB** |
| 4.5 Hz | 0.714 | −2.9 dB |
| 10 Hz | 0.984 | −0.1 dB |

**Seluruh passband yang dipilih berada di bawah frekuensi sudut sensornya sendiri.** Naskah membuang pita 4.5–20 Hz — satu-satunya pita di mana instrumen ini bekerja normal — dan mempertahankan pita di mana sensitivitasnya 16–30 dB lebih rendah.

Lebih buruk lagi, kalimat pembenarannya tidak nyambung secara logika. Halaman 44:

> "…geophone yang digunakan … dengan natural frekuensi atau batas frekuensi sebesar 4.5Hz. **sehingga** filter Butterworth dipilih, karena memiliki respon frekuensi yang relatif halus pada passband…"

Frekuensi natural 4.5 Hz adalah argumen **melawan** bekerja di 0.8–1.8 Hz, bukan argumen untuk memilih Butterworth. Dan kalimat "Butterworth dipilih karena respons halus" muncul **dua kali**, di halaman 43 dan 44, copy-paste, dipakai untuk membenarkan dua hal berbeda. Alasan pemilihan cut-off tidak pernah benar-benar diberikan.

### Konsekuensi yang menghancurkan seluruh tujuan klasifikasi

Pembeda utama antar kelas gempa vulkanik Merapi **adalah kandungan frekuensinya**:

* VTB: dominan 5–15 Hz
* MP (multiphase): campuran, 1–5 Hz
* LF: 0.5–2 Hz
* Rockfall: broadband 1–10+ Hz, durasi panjang, onset emergent
* Tektonik: broadband, ada fase P & S tegas

Menyaring **semua** kelas ke jendela selebar 1 Hz berarti **menghapus justru informasi yang membedakan kelas-kelas itu**. Setelah difilter 0.8–1.8 Hz, "dominant frequency", "spectral centroid" dan "spectral entropy" tidak lagi mengukur sumber — mereka mengukur bentuk filter dan noise. Ini penjelasan paling sederhana dan paling mungkin mengapa akurasi mentok di 63–73%, bukan 90%+ seperti literatur klasifikasi vulkano-seismik pada umumnya.

**Yang harus dilakukan:** ulangi seluruh ekstraksi fitur pada pita lebar (mis. 1–20 Hz), dan bandingkan head-to-head dengan 0.8–1.8 Hz. Bila akurasi naik tajam — dan saya menduga demikian — maka hasil di naskah sekarang adalah artefak keputusan filter.

---

## 2. Array 359 m tidak bisa mengukur back azimuth maupun slowness di 0.8–1.8 Hz

Ini cacat paling serius, karena menyerang tepat pada **kebaruan yang diklaim** (Bab 1.6 poin 2: integrasi parameter spasial array).

Dari koordinat Tabel 4.1, saya hitung geometri array yang sebenarnya:

* **Apertur maksimum: 359 m** (UGM01–UGM04)
* Jarak antar-stasiun minimum 157 m, rata-rata 271 m
* Jarak ke puncak Merapi: **16.9 km**, azimut **2.1°**

Resolusi sudut sebuah array dibatasi rasio panjang gelombang terhadap apertur (λ/D). Bila λ/D > 1, array **lebih kecil dari satu panjang gelombang** dan main lobe-nya melebar ke seluruh langit — tidak ada resolusi arah sama sekali.

| f (Hz) | c = 1000 m/s | c = 1500 m/s | c = 2500 m/s |
| ---: | ---: | ---: | ---: |
| 0.8 | λ/D = 3.48 | 5.22 | 8.70 |
| 1.3 | 2.14 | 3.21 | 5.35 |
| 1.8 | 1.55 | 2.32 | 3.87 |

**Tidak satu pun kombinasi menghasilkan λ/D < 1.** Pada pita yang dipakai naskah, array ini buta arah, untuk semua kecepatan yang masuk akal.

Untuk slowness lebih telak lagi. Resolusi slowness ≈ 1/(f·D):

* f = 0.8 Hz → Δu ≈ **3.48 s/km**
* f = 1.3 Hz → Δu ≈ **2.14 s/km**
* f = 1.8 Hz → Δu ≈ **1.55 s/km**

Sementara **rentang fisis yang ingin diukur** hanya 0.2–0.3 s/km (gelombang badan) sampai 0.5–1.0 s/km (gelombang permukaan). Artinya **ketidakpastian pengukuran 2–7 kali lebih besar daripada seluruh rentang besaran yang diukur.** Angka slowness yang keluar dari grid search itu bukan pengukuran; itu lokasi puncak noise di peta FK.

Tambahan: moveout maksimum melintasi array hanya 144–239 ms, yaitu **0.19–0.31 periode** pada 1.3 Hz. Pada pita selebar 1 Hz sinyalnya nyaris monokromatik, sehingga estimasi delay sub-periode bersifat ambigu (rawan cycle-skipping).

### Dan justru fitur itulah yang jadi juara

Naskah (5.2.2) melaporkan feature importance:

* **slowness — peringkat 1, 0.129**
* back azimuth — peringkat 6, 0.081
* beam power — peringkat 8, 0.067

Dengan 14 fitur, importance yang diharapkan dari fitur **tanpa informasi apa pun** adalah 1/14 = **0.071**. Jadi back azimuth (0.081) dan beam power (0.067) duduk **persis di level kebetulan**. Slowness 0.129 hanya 1.8× level itu — dan model pohon memang terkenal royal memberi importance pada fitur noise.

Naskah juga menafsirkan korelasi rendah BAZ/slowness terhadap fitur lain sebagai bukti "informasi komplementer" (hal. 136). Ini kekeliruan logika: **fitur acak juga punya korelasi mendekati nol terhadap segalanya.** Hipotesis nol "slowness adalah noise" memprediksi persis semua yang diamati: korelasi ~0 dengan semuanya, importance sedikit di atas 1/14, dan kenaikan akurasi yang tidak signifikan.

**Yang harus dilakukan:** (a) hitung ulang BAZ/slowness pada pita 4–15 Hz di mana λ/D < 1; (b) laporkan array response function / beam pattern array ini — wajib untuk paper array mana pun; (c) uji permutasi: acak nilai slowness antar event, latih ulang, lihat apakah akurasi turun. Kalau tidak turun, fitur itu memang kosong.

---

## 3. Label kelas tidak pernah divalidasi jenisnya — hanya waktunya

Naskah menyatakan dataset "telah divalidasi menggunakan katalog BPPTKG dan BMKG" (Batasan Masalah b; 4.3.7; 5.1). Tetapi prosedurnya, sesuai kalimatnya sendiri, adalah pencocokan **"kesesuaian atau kemiripan waktu kejadian (original time)"**.

Artinya: katalog dipakai untuk memastikan *event itu ada*, lalu **jenis kelasnya diambil dari label folder buatan penulis sendiri**. Jenis event tidak pernah diadu dengan `eventtype` BPPTKG.

Ini bukan kecurigaan saya. **Penulis sudah punya buktinya sendiri.** Pada berkas hasil di `Dairoh/accepted_beam_vs_bpptkg_all.csv` (128 event, eksperimen paralel pada periode yang beririsan), saya hitung ulang:

| Label folder | n | Paling sering di bulletin | Sesuai yang dimaksud |
| --- | ---: | --- | ---: |
| Gempa_Bumi | 29 | TECT 23/29 (79%) | 79% |
| **Multiphase** | 36 | **VTB 33/36 (92%)** | **MP 2/36 — 6%** |
| Rockfall | 16 | VTB 7/16 (44%) | ROCKFALL 6/16 — 38% |
| VTB | 47 | VTB 39/47 (83%) | 83% |

* **Kesesuaian keseluruhan: 70/128 = 54.7%**
* **Cohen's κ = 0.347** — hanya "fair" pada skala Landis–Koch

Dan kesesuaian itu **tidak** dijelaskan oleh kelonggaran pencocokan waktu: 121 dari 128 event cocok lewat `inside_window_buffer`, median offset hanya 14 detik, dan justru pencocokan paling ketat (0–10 s) punya kesesuaian **paling rendah** (47%). Ketidaksesuaiannya nyata, bukan artefak matching.

### Mengapa ini mematikan

92% event yang penulis beri label "Multiphase" dikatalogkan BPPTKG sebagai **VTB**. Artinya model diminta memisahkan dua kelas yang menurut ground truth **adalah kelas yang sama**. Dan benar saja — pada eksperimen 128-event itu, kebingungan terbesar model persis MP↔VTB.

Jadi sebagian dari 27% error yang tersisa di disertasi bukan kegagalan model. Itu model yang **berhasil** mempelajari label yang salah.

**Peringatan metodologis:** dataset disertasi (275 event) **berbeda** dari dataset 128-event itu. Angka 54.7% tidak boleh langsung dikutip untuk dataset 275. Yang wajib dilakukan adalah **mengulang audit yang sama pada 275 event**, dan melaporkan tabel silang label-folder × eventtype-BPPTKG beserta κ-nya di Bab V. Kalau hasilnya serupa, seluruh Bab V harus dijalankan ulang memakai label BPPTKG sebagai target.

---

# BAGIAN II — STATISTIK: KLAIM UTAMA TIDAK TERUJI

## 4. Kenaikan akurasi karena fitur array: tidak signifikan, bahkan dalam skenario terbaik yang mungkin

Ini menguji langsung **H2**, hipotesis kebaruan naskah. Dari Tabel 5.7, dengan ukuran data uji dari Tabel 5.4 (110, 83, 55, 28):

| Split | Model | Tanpa array | Dengan array | Selisih | McNemar kasus terbaik |
| --- | --- | ---: | ---: | ---: | ---: |
| 60:40 | SVM | 64/110 | 66/110 | **+2 event** | p = 0.500 |
| 60:40 | XGB | 68/110 | 70/110 | **+2 event** | p = 0.500 |
| 70:30 | SVM | 48/83 | 50/83 | **+2 event** | p = 0.500 |
| 70:30 | XGB | 52/83 | 56/83 | **+4 event** | p = 0.125 |
| 80:20 | SVM | 34/55 | 35/55 | **+1 event** | p = 1.000 |
| 80:20 | XGB | 36/55 | 40/55 | **+4 event** | p = 0.125 |
| 90:10 | SVM | 15/28 | 16/28 | **+1 event** | p = 1.000 |
| 90:10 | XGB | 17/28 | 18/28 | **+1 event** | p = 1.000 |

Karena data uji berpasangan, uji yang benar adalah **McNemar**. Naskah tidak melaporkan jumlah discordant, jadi saya hitung **batas paling menguntungkan bagi klaim** — seolah setiap ketidaksepakatan berpihak pada model+array.

> **Bahkan dengan asumsi paling murah hati yang secara matematis mungkin, tidak satu pun dari delapan perbandingan bisa mencapai p < 0.05.**

Seluruh "kebaruan" naskah bersandar pada perpindahan **1 sampai 4 event**.

Naskah menyebutnya "kenaikan yang cukup signifikan" (hal. 119). Kata *signifikan* tidak boleh dipakai tanpa uji. Di sini ujinya tidak bisa lulus, bahkan secara prinsip.

Perbandingan XGBoost vs SVM di 80:20 (35/55 → 40/55, +5 event) pun hanya mencapai **p = 0.062** dalam kasus terbaik — masih gagal.

## 5. Selang kepercayaan lebih lebar daripada seluruh efek yang diklaim

| Split | Model + array | Akurasi | 95% CI (Wilson) | Lebar |
| --- | --- | ---: | --- | ---: |
| 60:40 | XGB | 0.6364 | [0.543, 0.720] | 0.177 |
| 70:30 | XGB | 0.6764 | [0.568, 0.766] | 0.198 |
| **80:20** | **XGB** | **0.7273** | **[0.598, 0.827]** | **0.230** |
| 90:10 | XGB | 0.6429 | [0.458, 0.793] | 0.335 |
| 80:20 | SVM | 0.6364 | [0.504, 0.751] | 0.246 |

Selang untuk angka unggulan (72.73%) selebar **23 poin persentase**, sementara efek yang diklaim hanya **7 poin**. Naskah memilih 80:20 sebagai "terbaik", padahal CI-nya tumpang tindih sempurna dengan semua skenario lain.

## 6. Satu seed, tanpa pengulangan — padahal penulis tahu variansinya ±0.07

Naskah memakai `random_state = 42` tunggal untuk setiap skenario (4.3.8), dan menarik kesimpulan dari perbandingan antar-skenario.

Ini tidak bisa dipertahankan, dan penulis **sudah tahu** tidak bisa: pada `Dairoh/repeated_split_summary.csv`, penulis menjalankan 50 pengulangan split dan memperoleh **std akurasi = 0.070**, rentang 0.385–0.692. Artinya dua skenario yang berbeda 0.02–0.07 tidak terbedakan dari derau split.

Jadi penulis memiliki bukti bahwa angka single-split tidak stabil, lalu membangun Bab V di atas angka single-split. Ini harus diperbaiki: ulangi 50–100 kali, laporkan mean ± std, dan bandingkan dengan uji berpasangan.

## 7. Overfitting yang dilaporkan tetapi tidak ditindaklanjuti

Selisih Tabel 5.5 (training) vs Tabel 5.7 (uji), keduanya dengan fitur array:

| Split | SVM train → uji | Gap | XGB train → uji | Gap |
| --- | --- | ---: | --- | ---: |
| 60:40 | 0.7636 → 0.6000 | +0.164 | 0.7697 → 0.6364 | +0.133 |
| 70:30 | 0.7656 → 0.6024 | +0.163 | 0.8438 → 0.6764 | +0.167 |
| 80:20 | 0.7409 → 0.6364 | +0.105 | 0.8500 → 0.7273 | +0.123 |
| 90:10 | 0.7530 → 0.5714 | +0.182 | **0.8745 → 0.6429** | **+0.232** |

Gap 10–23 poin. Naskah menyebut learning curve dan gap (hal. 111) lalu melanjutkan seolah tidak terjadi apa-apa. Pada 90:10, model menghafal 87% data latih dan hanya membawa 64% ke data uji.

## 8. Baseline tidak pernah dilaporkan

Distribusi kelas: RF 84, MP 71, VTB 71, NEV 49 (total 275). **Baseline kelas mayoritas = 30.55%.**

Angka ini tidak ada di naskah. Tanpa baseline, pembaca tidak bisa menilai apakah 72.73% itu bagus. (Untuk adilnya: 72.73% memang jauh di atas 30.55% — model **memang** belajar sesuatu. Yang tidak terbukti adalah bahwa *fitur array* yang membuatnya begitu.)

---

# BAGIAN III — KESALAHAN KONSEP

## 9. VTB didefinisikan salah, dan didefinisikan berbeda-beda di tiga tempat

| Lokasi | Definisi yang ditulis |
| --- | --- |
| Bab IV, hal. 60 | "**Vulkanik Tipe-B** (VTB)" — **benar** |
| Tabel 5.2, hal. 91 | "Gempa **vulkanik** dangkal (VTB)" — benar |
| Hal. 107 (teks) | "gempa bumi dangkal (VTB)" — kabur |
| **Tabel 5.4, hal. 108** | "**Gempa tektonik dangkal** (VTB)" — **SALAH** |

VTB (Volcano-Tectonic type B, klasifikasi Minakami) adalah **gempa vulkanik dangkal** di bawah kawah, biasanya < 1–2 km. Menyebutnya "gempa tektonik dangkal" bukan sekadar salah ketik — itu memindahkan kelas tersebut ke kategori yang salah secara fisis, dan membuatnya tumpang tindih dengan kelas NEV (Gempa Bumi / tektonik) yang justru seharusnya menjadi lawannya. Pada disertasi yang seluruh isinya adalah klasifikasi empat kelas, kelas terpenting tidak boleh punya tiga nama berbeda.

## 10. Tabel 4.2 — definisi confusion matrix tertukar

Naskah menulis (hal. 60):

| | Prediksi Negatif | Prediksi Positif |
| --- | --- | --- |
| Aktual Negatif | TN | **FN** |
| Aktual Positif | **FP** | TP |

Yang benar: Aktual Negatif × Prediksi Positif = **FP**; Aktual Positif × Prediksi Negatif = **FN**. **FP dan FN tertukar.** Ini tabel yang mendefinisikan seluruh metrik evaluasi di Persamaan 4.2–4.7. Untungnya hasil numeriknya dihitung oleh scikit-learn, jadi angkanya kemungkinan benar — tetapi definisi yang tertulis salah, dan penguji akan menanyakannya.

## 11. Persamaan 4.5: rumus F1 diberi nama "precision"

```
(4.4)  recision = TP/(TP+FP)
(4.5)  recision = 2 × (Recall × Precision)/(Recall + Precision)
```

Dua besaran berbeda diberi nama sama, dan keduanya salah eja ("recision"). Persamaan 4.5 adalah **F1-score**, bukan precision.

## 12. "NEV" tidak pernah didefinisikan

Kelas keempat ditulis "Gempa Bumi (NEV)" / "(Non Event Vulkanik/NEV)". Singkatan NEV tidak ada di daftar singkatan dan tidak dijelaskan saat pertama muncul. Juga secara konseptual janggal: menyebut gempa tektonik sebagai "non-event" adalah penamaan yang menyesatkan — event-nya jelas ada, hanya bukan vulkanik.

## 13. Parameter STA/LTA berpotensi membuang justru kelas yang paling sulit

Naskah memakai STA = 10 s, LTA = 120 s, on = 3.0, off = 0.5, lalu memotong jendela event **120 detik**.

LTA (120 s) **sama panjang** dengan jendela event. Untuk event berdurasi panjang dan ber-onset landai — rockfall dan tremor — energi event akan ikut masuk ke jendela LTA, menaikkan LTA, menekan rasio STA/LTA, dan menggagalkan trigger. Detektor ini secara sistematis bias terhadap event impulsif (VT, tektonik) dan merugikan rockfall/LF. Perlu justifikasi, atau uji sensitivitas terhadap panjang LTA.

## 14. Corong seleksi 9.589 → 446 → 275 tidak pernah diperiksa biasnya

Naskah melaporkan (hal. 129–130): 9.589 kandidat STA/LTA → **446** event lolos kriteria ≥3 stasiun → **275** event tervalidasi katalog.

Dua hal serius:

**(a) Kriteria 3 stasiun membuang 95.3% kandidat.** Untuk array berapertur 359 m, kelima sensor melihat praktis sinyal yang sama. Kalau 95% deteksi gagal koinsidensi 3-stasiun, kemungkinan besar detektornya memicu pada noise lokal tiap sensor (stasiun berada di permukiman — naskah sendiri menyebut noise antropogenik). Yang lolos adalah event terbesar saja. Distribusi amplitudo event yang lolos vs yang dibuang tidak pernah ditampilkan.

**(b) Langkah 446 → 275 membuang 171 event yang tidak ada di katalog.** Ini bertentangan langsung dengan tujuan penelitian. Naskah ingin membuktikan stasiun UGM bisa **melengkapi** pemantauan. Tetapi dengan membuang setiap event yang belum ada di katalog resmi, desainnya **secara konstruksi tidak mungkin** menunjukkan nilai tambah deteksi. 171 event itu justru bukti paling menarik yang dimiliki penulis — dan dibuang tanpa diperiksa.

---

# BAGIAN IV — ANGKA YANG TIDAK KONSISTEN

## 15. Abstrak dan Kesimpulan menyebut angka dari kolom yang salah

**Abstrak** (hal. xv & xvii) dan **Kesimpulan 6.1 poin 3** menyatakan:

> "akurasi tertinggi pada skenario 80:20 dengan **65.45% di SVM** dan 72.73% pada XGBoost"

Tabel 5.7, skenario 80:20:

| | Tanpa array | Dengan array |
| --- | ---: | ---: |
| SVM | 0.6182 (61.82%) | **0.6364 (63.64%)** |
| XGBoost | **0.6545 (65.45%)** | 0.7273 (72.73%) |

**65.45% adalah akurasi XGBoost TANPA fitur array.** Angka itu dilaporkan di abstrak dan di kesimpulan sebagai capaian SVM. Nilai SVM yang benar adalah **63.64%**.

Ini bukan salah ketik kecil: kesalahan yang sama muncul di **tiga tempat** (intisari, abstract, simpulan), yaitu tepat bagian yang paling banyak dibaca penguji dan yang akan dikutip orang.

## 16. Satu angka di Tabel 5.7 mustahil secara aritmetika

Data uji skenario 70:30 berisi **83 event** (Tabel 5.4). Maka akurasi hanya bisa bernilai k/83:

* 55/83 = 0.6627
* 56/83 = **0.6747**
* 57/83 = 0.6867

Tabel 5.7 mencantumkan **0.6764** untuk XGBoost + array. Angka itu **tidak dapat dihasilkan** oleh 83 sampel (0.6764 × 83 = 56.14). Kemungkinan besar 0.6747 tertukar digitnya. Semua nilai lain di Tabel 5.7 saya cek dan menghasilkan bilangan bulat — hanya yang satu ini yang cacat.

## 17. Teks Bab V bertentangan dengan tabelnya sendiri

| Besaran | Teks hal. 119 | Tabel 5.7 |
| --- | ---: | ---: |
| Kenaikan XGBoost 60:40 | 0.0098 | **0.0182** |
| F1-macro SVM 90:10 | 0.5702 | **0.5798** |
| F1-macro XGBoost 90:10 | 0.6434 | **0.6058** |

Tiga kontradiksi di halaman yang sama dengan tabelnya. Selain itu ada deret rusak di hal. 118: *"0.6182; 0.6265, 0, 0.6545 dan 0.6071"* — lima nilai untuk empat skenario, dengan "0," nyasar di tengah.

## 18. Periode data disebut tiga kali dengan tiga jawaban berbeda

| Lokasi | Periode |
| --- | --- |
| Batasan Masalah (b) | 16 Agustus – 12 September 2023 (**28 hari**) |
| 4.1 Data | Agustus – Desember 2023 |
| 4.3.2 Akuisisi | Juli – Desember 2023 |

Bab V memastikan yang benar: *"deteksi … selama periode **28 hari**"*. Jadi dua pernyataan lain keliru. Bagi penguji, ini langsung memunculkan pertanyaan: kalau datanya Juli–Desember, mengapa hanya 28 hari yang dipakai, dan atas dasar apa 28 hari itu dipilih?

## 19. Jumlah fitur tidak konsisten lintas dokumen

* Disertasi: **14 fitur** (4.3.6)
* `Dairoh/README.md`: "Total fitur yang dipakai: **102 fitur**"
* `Dairoh/xgb_feature_importance.csv`: **105 fitur**

Ketiganya milik penulis. Minimal satu salah. (README dan CSV berasal dari eksperimen 128-event yang berbeda, tetapi selisih 102 vs 105 di dalam satu eksperimen yang sama tetap kesalahan.)

---

# BAGIAN V — INTEGRITAS DOKUMEN

Bagian ini paling mudah diperbaiki, tetapi paling cepat merusak kredibilitas di ruang ujian.

## 20. Dokumen punya tiga penomoran halaman yang saling bertabrakan

| Bagian | Halaman tercetak |
| --- | --- |
| Bab I | 1–13 |
| Bab II | 14–41 |
| Tabel 2.2 (landscape) | **1, 2, 3** ← restart |
| Halaman transisi | **1** ← restart lagi |
| Bab III | **2**–38 ← lanjut dari restart |
| Bab IV | 39–88 |
| Bab V | 89–~148 |

Halaman bernomor 14–38 **muncul dua kali** di dokumen yang sama. Akibatnya **Daftar Isi salah total**: DAFTAR ISI menyebut Bab III di hal. 41, Bab IV di hal. 78, Bab V di hal. 103, Bab VI di hal. 180 — tidak satu pun cocok dengan halaman sebenarnya (2, 39, 89, ~147). Ini tanda jelas naskah disusun dengan menempelkan beberapa berkas Word tanpa menyatukan section break.

Terkait: naskah dikirim sebagai **tiga PDF terpisah** (3A, 3B1, 3B2), dan 3A terpotong **di tengah persamaan** (Pers. 3.49/3.50) di halaman 38.

## 21. Penomoran subbab Bab IV kacau, dan satu bagian diduplikasi utuh

Urutan di batang tubuh:

```
4.3.3.1  Pra-pemrosesan
4.3.3.2  Deteksi Event
4.3.3.3  Picking dan Event windowing
4.3.4    Analisis FK dan Beamforming      ← melompat
4.3.3.4  Korelasi silang                  ← mundur lagi
4.3.3.5  Spektral
4.3.5    Beamforming pada Data Array      ← duplikat dari 4.3.4
```

**Subbab 4.3.4 dan 4.3.5 hampir identik kata per kata**, termasuk kalimat yang sama persis: *"Implementasi kode merealisasikan proses penggabungan tersebut melalui operasi `np.mean(aligned, axis=0)`"*. Beamforming dijelaskan dua kali penuh dengan isi yang sama.

Penomoran di Daftar Isi berbeda lagi dari batang tubuh (4.3.4 Ekstraksi Fitur, 4.3.5 Pembagian Dataset, …) dan **melompati 4.3.9**.

## 22. Salah rujuk silang dan penomoran gambar rusak

* Hal. 53 (Bab IV) merujuk **"tabel 3.1"** untuk daftar fitur — seharusnya tabel di Bab IV.
* Hal. 62 (Bab II): *"seperti pada **Tabel 2.3**: Berdasarkan **Tabel 2.1** dapat dike…"* — dua rujukan berbeda untuk objek yang sama dalam satu kalimat, dan Tabel 2.1 sebenarnya adalah klasifikasi Shimozuru.
* Nomor gambar rusak di banyak tempat: "Gambar 5.1 2", "Gambar 5.1 7", "Gambar 5.2 0", "Gambar 5.2 1", "Gambar 5.2 4", "Gambar 5.2 7" — spasi menyisip di tengah nomor (artefak field Word).

## 23. Tabel 4.1: koordinat tidak bisa dibaca sebagai koordinat

```
Nama stasiun  Kode    Longtitude    Latitude (BT)
UGM 1         RE5DE   -7.692.254    110.438.530
```

* Nilainya memakai pemisah ribuan Indonesia pada bilangan desimal: **−7.692.254** seharusnya **−7.692254**.
* Judul kolom tertukar: nilai pertama adalah **lintang**, bukan bujur.
* "(BT)" = Bujur Timur dilekatkan pada kolom **Latitude**.
* "Longtitude" salah eja.

Empat kesalahan dalam satu baris judul tabel, pada tabel yang mendefinisikan geometri array — fondasi seluruh analisis spasial.

## 24. Rujukan bermasalah

* **"(Raschka & Mirjalili, 2006)"** — buku *Python Machine Learning* terbit 2015/2017/2019. Tidak ada edisi 2006. Di tempat lain naskah mengutip "2019" dengan benar.
* **"(Wegler and Birger, 2001)"** — hampir pasti maksudnya **Wegler & Lühr (2001)** tentang scattering di Merapi. Nama penulis kedua keliru.
* **"(Aki & Richards, 1980)"** vs "(Aki & Richards, 2002)" — dua edisi dikutip untuk hal serupa tanpa penjelasan.
* **"Anonim. 2021"** — dokumentasi XGBoost dikutip sebagai anonim. Seharusnya Chen & Guestrin (2016) atau dokumentasi resmi dengan penulis korporat.
* **"(Scikit-learn, 2026)"** — rujukan bertahun **masa depan**.
* **"(Shake, n.d)"** — tanpa tahun, tanpa penulis jelas.
* **"Allen Rex, V (1978)"** — nama kacau; seharusnya Allen, R. V.
* **"Anantrasirichai, P."** — inisial keliru; seharusnya Anantrasirichai, N.

## 25. Salah eja pada bagian formal

"**ABTSRACT**" (judul halaman abstrak Inggris), "**HIPOTESISI**" (Daftar Isi), "**Rcokfall**" dan "**RFF**" (hal. 107), "**Longtitude**", "**Postif**", "**Actual1**", "**recision**", "**XGBoosr**", "Extrem Gradient Boosting", "**mterdapat**", "**dna**", "**sebnayak**", "**Selanjunta**", "**berjarka**", "**memnunjukkan**", "**diidapatkan**".

Kalimat berulang juga banyak, mis. hal. 5: *"XGBoost(Chen & Guestrin, 2016; Hibert et al., 2017), XGBoost(Chen & Guestrin, 2016; Hibert et al., 2017)"* dan *"(Perol et al., 2018; Titos et al., 2019; Sudarmaji et al., 2025) (Perol et al., 2018; Titos et al., 2019; Sudarmaji et al., 2025)"* — sitasi ditempel dua kali berturut-turut.

Pada halaman Prakata tertulis "Bapak Rektor **Sudriman Said** Universitas **Harkat Negeri**" — mohon dicek, nama institusi dan pejabat harus benar.

---

# BAGIAN VI — PERTANYAAN UJIAN

Siapkan jawaban berangka, bukan jawaban naratif.

1. Berapa apertur array Anda, dan berapa λ/D pada 1.3 Hz? Tunjukkan bahwa array ini bisa menyelesaikan back azimuth di pita 0.8–1.8 Hz.
2. Berapa resolusi slowness 1/(f·D) array Anda? Bandingkan dengan rentang slowness fisis yang Anda ukur.
3. Mengapa memfilter 0.8–1.8 Hz ketika geophone Anda bersudut 4.5 Hz dan responsnya −22 dB di tengah pita itu?
4. Setelah difilter ke lebar pita 1 Hz, informasi apa yang tersisa untuk membedakan VTB (5–15 Hz) dari MP (1–5 Hz)?
5. Slowness menempati peringkat 1 feature importance (0.129). Dengan 14 fitur, importance kebetulan adalah 0.071. Apa bukti bahwa 0.129 bukan noise?
6. Jalankan uji permutasi: acak slowness antar event, latih ulang. Berapa akurasinya?
7. Kenaikan akurasi karena fitur array adalah +1 sampai +4 event. Berapa p-value McNemar-nya?
8. Berapa baseline kelas mayoritas dataset Anda?
9. Berapa 95% CI dari 72.73%? Apakah tumpang tindih dengan 65.45%?
10. Mengapa Tabel 5.7 memuat 0.6764 padahal data uji 70:30 hanya 83 event?
11. Abstrak dan Simpulan menulis SVM 65.45%. Tabel 5.7 menulis 63.64%. Mana yang benar, dan mengapa angka XGBoost-tanpa-array muncul sebagai capaian SVM?
12. Dari 36 event berlabel "Multiphase" pada analisis Anda sendiri, hanya 2 yang dikatalogkan MP oleh BPPTKG dan 33 sebagai VTB. Apa dasar mempertahankan label folder sebagai target pelatihan?
13. Berapa Cohen's κ antara label Anda dan `eventtype` BPPTKG untuk 275 event?
14. Anda menjalankan 50 repeated split dan memperoleh std 0.070. Mengapa Bab V memakai satu seed?
15. Gap train–test XGBoost 90:10 adalah 0.232. Apa langkah mitigasi overfitting-nya?
16. Kriteria 3-stasiun membuang 95.3% kandidat pada array berapertur 359 m. Mengapa kelima sensor tidak melihat event yang sama?
17. 171 event lolos kriteria 3-stasiun tetapi tidak ada di katalog, lalu dibuang. Bukankah justru itu bukti nilai tambah stasiun UGM?
18. VTB: "Vulkanik Tipe-B" (hal. 60), "gempa vulkanik dangkal" (Tabel 5.2), atau "gempa tektonik dangkal" (Tabel 5.4)? Mana yang benar dan apa konsekuensinya bagi kelas NEV?
19. Pada Tabel 4.2, FP dan FN berada di posisi yang tertukar. Mana yang benar?
20. LTA Anda 120 detik dan jendela event Anda juga 120 detik. Bagaimana detektor ini bisa memicu pada rockfall berdurasi panjang?

---

# BAGIAN VII — YANG HARUS DIKERJAKAN

## Wajib sebelum ujian (mengubah hasil)

1. **Ulangi seluruh pipeline pada pita lebar** (mis. 1–20 Hz). Bandingkan langsung dengan 0.8–1.8 Hz dalam satu tabel. Ini kemungkinan besar menaikkan akurasi secara substansial dan mengubah kesimpulan.
2. **Hitung ulang BAZ/slowness/beam power pada pita di mana λ/D < 1** (≥ 4 Hz). Lampirkan array response function. Bila fitur spasial tetap tidak menolong, laporkan itu sebagai temuan — hasil negatif yang jujur jauh lebih kuat daripada klaim yang tidak teruji.
3. **Audit label terhadap `eventtype` BPPTKG untuk seluruh 275 event.** Laporkan tabel silang dan κ. Bila κ rendah seperti pada eksperimen 128-event, latih ulang memakai label BPPTKG sebagai target.
4. **Ganti single split dengan repeated stratified split (≥50×)**, laporkan mean ± std, dan uji perbandingan dengan McNemar berpasangan. Laporkan baseline kelas mayoritas dan CI di setiap tabel.
5. **Uji permutasi fitur spasial** untuk membuktikan ia membawa informasi.

## Wajib sebelum ujian (tidak mengubah hasil)

6. Perbaiki **65.45% → 63.64%** di intisari, abstract, dan Simpulan.
7. Perbaiki **0.6764 → 0.6747** dan tiga kontradiksi teks-vs-tabel di hal. 118–119.
8. Samakan **periode data** menjadi 16 Agustus – 12 September 2023 di seluruh naskah, dan jelaskan alasan pemilihannya.
9. Samakan definisi **VTB = gempa vulkanik dangkal (Volcano-Tectonic tipe B)** di semua tabel dan teks. Definisikan NEV saat pertama muncul.
10. Perbaiki **Tabel 4.2** (posisi FP/FN) dan **Pers. 4.5** (beri nama F1-score).
11. Perbaiki **Tabel 4.1**: desimal, judul kolom, satuan.
12. **Hapus duplikasi subbab 4.3.4/4.3.5**, rapikan penomoran 4.3.x, sinkronkan dengan Daftar Isi.
13. **Satukan dokumen menjadi satu PDF**, satu urutan halaman, regenerasi Daftar Isi.
14. Bersihkan rujukan: Raschka & Mirjalili 2019, Wegler & Lühr 2001, hapus "Scikit-learn 2026" dan "Anonim 2021", perbaiki nama penulis.
15. Baca ulang untuk salah eja pada bagian formal (ABTSRACT, HIPOTESISI, Rcokfall, nama pejabat di Prakata).

## Untuk menyelamatkan kebaruan

Kebaruan sekarang diklaim sebagai "integrasi fitur spasial array". Dengan bukti yang ada, klaim itu tidak bertahan. Ada dua jalan jujur:

**Jalan A — perbaiki fisikanya.** Pindah ke pita ≥4 Hz, buktikan array bisa mengukur BAZ/slowness di sana, lalu tunjukkan peningkatan yang signifikan secara statistik. Kalau berhasil, kebaruannya nyata dan kuat.

**Jalan B — ubah pertanyaan penelitiannya.** Jadikan disertasi ini tentang **batas kemampuan** array berbiaya rendah berapertur kecil pada jarak 16 km: sampai frekuensi berapa array 359 m masih informatif, seberapa besar degradasi akibat label noise, dan berapa akurasi yang realistis. Itu pertanyaan yang sah, penting bagi komunitas low-cost seismology Indonesia, dan **datanya sudah ada di tangan**. Hasil negatif yang dikuantifikasi dengan benar adalah disertasi doktor yang sah.

Yang tidak bisa dipertahankan adalah posisi sekarang: mengklaim fitur spasial meningkatkan kinerja, ketika array-nya tidak bisa mengukur fitur itu dan kenaikannya sebesar satu sampai empat event.

---

## Catatan penutup

Ada pekerjaan nyata di balik naskah ini: 9.589 deteksi diproses, pipeline beamforming dibangun, dua algoritma dibandingkan lintas empat skenario, dan — ini yang paling saya hargai — penulis **sudah menjalankan sendiri** repeated split 50× dan audit label terhadap BPPTKG. Dua analisis itu adalah instrumen yang tepat. Masalahnya, keduanya dikerjakan **di luar** disertasi dan hasilnya tidak dibawa masuk, padahal keduanya mengubah kesimpulan.

Jadi ini bukan kasus mahasiswa yang tidak tahu cara menguji. Ini kasus mahasiswa yang sudah menguji, menemukan jawaban yang tidak nyaman, lalu menulis disertasi seolah pengujian itu tidak pernah terjadi. Itu yang harus diperbaiki lebih dulu — sebelum satu kalimat pun dirapikan.
