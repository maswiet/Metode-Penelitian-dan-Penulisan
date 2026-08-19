# Laporan Reviewer Brutal

Naskah yang dinilai adalah **“Array-Based Dataset Construction for Machine Learning Classification of Long-Distance Volcanic Seismic Signals”**, manuscript **AIIG-D-26-00215**, dengan Dairoh sebagai penulis pertama. 

## Rekomendasi: **REJECT AND REBUILD**

Bukan *minor revision*. Bahkan bukan *major revision* biasa. Naskah ini memerlukan:

* audit ulang label;
* evaluasi ulang kemampuan deteksi;
* pembuktian resolusi array;
* desain ulang validasi machine learning;
* eksperimen ablation;
* pelepasan data dan kode;
* serta penulisan ulang hampir seluruh Results dan Discussion.

Versi sekarang tidak membuktikan bahwa framework menghasilkan dataset yang “reliable”. Ia hanya menunjukkan bahwa **XGBoost dapat menebak 40 dari 55 event pada satu random split dari 275 event yang sebelumnya telah disaring keras, dicocokkan dengan katalog, dan diperiksa oleh penulis pertama sendiri**.

> **Ini belum merupakan sistem klasifikasi seismik jarak jauh. Ini adalah eksperimen klasifikasi pada subset kecil dari event-event paling mudah yang sudah diketahui jawabannya.**

| Aspek                      |      Nilai |
| -------------------------- | ---------: |
| Relevansi persoalan        |        4/5 |
| Potensi array UGM          |        4/5 |
| Validitas label            |        1/5 |
| Validitas array processing |      1.5/5 |
| Desain machine learning    |        1/5 |
| Evaluasi statistik         |        1/5 |
| Generalisasi               |      0.5/5 |
| Reproducibility            |      0.5/5 |
| Kebaruan AI                |        1/5 |
| Kualitas editorial         |      0.5/5 |
| **Putusan**                | **Reject** |

---

# Hal-hal positif yang memang ada

Saya mulai dengan beberapa bagian yang layak dipertahankan.

Pertama, gagasan menggunakan array yang terletak sekitar 16 km dari Merapi sebagai pelengkap jaringan dekat puncak memang relevan. Array terdiri atas lima stasiun dengan konfigurasi pentagonal dan jarak antarelemen sekitar 250 m. 

Kedua, penggunaan kombinasi deteksi STA/LTA, beamforming, analisis frekuensi–bilangan gelombang, serta katalog BMKG dan BPPTKG adalah alur kerja yang secara konseptual masuk akal untuk menyaring event-event yang terekam secara koheren. 

Ketiga, distribusi kelas cukup seimbang: 71 Multiphase, 49 gempa regional, 84 Rockfall, dan 71 Volcano-Tectonic B. Ini lebih baik daripada dataset yang satu kelasnya mendominasi 95%. 

Keempat, StandardScaler dan SMOTE disebut ditempatkan di dalam pipeline dan SMOTE hanya diterapkan pada training folds, bukan pada validation atau test data. Secara prinsip, ini adalah prosedur yang benar. 

Kelima, penulis pada akhirnya mengakui dua keterbatasan penting: dataset hanya berasal dari satu bulan dan fitur amplitudo dapat merepresentasikan jarak, atenuasi, dan site response alih-alih jenis sumber. 

Namun, kesadaran bahwa kapal berlubang bukan pengganti tindakan menutup lubangnya.

---

# Kelemahan fatal

## 1. “Independent catalogue validation” adalah istilah yang salah

BPPTKG dan BMKG bukan dataset independen untuk memvalidasi label. Mereka adalah **sumber label**.

Workflow-nya adalah:

1. event dideteksi;
2. event diperiksa dengan beamforming dan FK;
3. event dicocokkan dengan katalog BPPTKG atau BMKG;
4. kelas dari katalog itu kemudian menjadi label target machine learning.

Dengan demikian, yang dilakukan adalah:

> **catalogue-based label transfer**, bukan independent validation.

Lebih buruk lagi, quality control manual dilakukan oleh **penulis pertama seorang diri**, berdasarkan “waveform consistency and agreement with array-processing results.” Tidak ada second reviewer, blind review, inter-annotator agreement, Cohen’s kappa, maupun aturan adjudication. 

Jadi kata “validated” dalam naskah berarti:

> Penulis pertama melihat waveform, memeriksa apakah sesuai dengan hasil algoritmanya sendiri, kemudian menyatakan labelnya benar.

Itu bukan validasi independen. Itu **self-confirmation with extra steps**.

### Yang harus dilakukan

Ambil subset sekurang-kurangnya 300–500 event dan minta minimal dua ahli seismologi gunung api memberi label secara buta, tanpa mengetahui:

* label BPPTKG;
* hasil FK;
* hasil classifier;
* identitas event.

Kemudian laporkan:

* confusion matrix antar-annotator;
* Cohen/Fleiss kappa;
* agreement katalog versus ahli;
* ambiguous-label fraction;
* final consensus label.

Tanpa ini, “reliable labelled dataset” hanya merupakan slogan.

---

## 2. Toleransi waktu pencocokan terlalu lebar dan berisiko menghasilkan label kebetulan

Table 1 menetapkan:

* pencocokan BPPTKG dengan toleransi **5–50 s**;
* pencocokan BMKG dengan rentang **15–60 s**;
* back-azimuth ke Merapi dalam ±15°. 

Selama 28 hari, katalog BPPTKG berisi **9.924 event**, atau rata-rata sekitar:

[
\frac{9{,}924}{28}\approx354\ \text{event/hari},
]

yakni satu event setiap sekitar 244 s. 

Dengan pendekatan Poisson sederhana:

* peluang setidaknya satu event katalog jatuh dalam satu window 50 s adalah sekitar 18,5%;
* bila yang dimaksud ±50 s, peluangnya sekitar 33,6%.

Itu belum memperhitungkan hari-hari dengan lebih dari 500 event, ketika accidental matching akan lebih besar.

Artinya, dengan toleransi selebar itu, pencocokan waktu saja dapat menghasilkan banyak “pasangan” yang kebetulan. Beamforming mungkin mengurangi peluang tersebut, tetapi naskah tidak melaporkan:

* berapa kandidat memiliki lebih dari satu kemungkinan pasangan katalog;
* bagaimana konflik diselesaikan;
* apakah matching bersifat one-to-one;
* apakah toleransi adalah satu sisi atau dua sisi;
* distribusi residual waktu;
* probabilitas accidental match;
* apakah onset BPPTKG merupakan origin time atau waktu tiba pada stasiun referensi;
* bagaimana travel time dihitung.

Pada level doktoral, “5–50 seconds” bukan metode. Itu rentang yang cukup lebar untuk memasukkan ketidakpastian, event lain, dan mungkin makan siang operator.

---

## 3. Dataset akhir hanya sekitar 2,6% dari populasi katalog referensi

Naskah memakai:

* 9.924 event vulkanik BPPTKG;
* 724 gempa regional BMKG;
* total 10.648 event referensi.

Dari jumlah tersebut:

* hanya 442 kandidat ditemukan oleh STA/LTA;
* hanya 275 dipertahankan;
* event vulkanik yang bertahan hanya (71+84+71=226);
* gempa regional yang bertahan hanya 49. 

Jadi secara kasar:

[
\frac{226}{9{,}924}=2.28%
]

untuk event vulkanik,

[
\frac{49}{724}=6.77%
]

untuk gempa regional, dan

[
\frac{275}{10{,}648}=2.58%
]

untuk keseluruhan katalog.

Penulis akhirnya mengakui bahwa accuracy hanya berlaku bagi **detectable, catalogue-matched remote-array events**, bukan populasi event Merapi secara keseluruhan. 

Pengakuan itu benar, tetapi menghancurkan positioning Abstract dan Conclusions.

> **Framework ini tidak membangun representasi event Merapi. Ia membangun museum berisi 2–3% specimen yang paling bersih dan paling mudah dikenali.**

Ini boleh menjadi dataset eksperimen. Tetapi jangan disebut “reliable dataset for long-distance volcanic seismic classification” tanpa kata-kata:

* high-SNR;
* catalogue-matched;
* quality-selected;
* detectable subset.

---

## 4. Acceptance rate bukan detection performance

Penulis menghitung:

[
\frac{275}{442}=62.2%
]

dan menampilkannya sebagai daily acceptance rate.

Namun angka itu bukan:

* precision;
* recall;
* sensitivity;
* specificity;
* false-positive rate;
* false-negative rate.

Ia hanya mengatakan bahwa 62,2% hasil STA/LTA lolos filter berikutnya.

Naskah tidak menjawab:

* berapa dari 9.924 event BPPTKG yang seharusnya dapat terdeteksi;
* berapa event besar yang gagal ditemukan;
* berapa kandidat yang sebenarnya event tetapi dibuang;
* berapa kandidat yang benar-benar noise;
* berapa false negative per kelas;
* bagaimana recall berubah terhadap amplitudo, magnitude, jarak, waktu, dan jumlah stasiun aktif.

Penulis mengatakan detektor dipilih untuk “maximize event sensitivity,” tetapi tidak pernah mengukur sensitivity. 

> **Menyebut algoritma sensitif tanpa menghitung sensitivitas adalah seperti menyebut termometer akurat karena jarumnya bergerak.**

Lakukan evaluasi detection-level terlebih dahulu sebelum membahas classifier.

---

## 5. Framework “cadangan ketika jaringan puncak gagal” masih bergantung pada jaringan puncak

Discussion menjual remote array sebagai pelengkap ketika stasiun puncak:

* tidak tersedia;
* sulit dirawat;
* atau terganggu saat aktivitas meningkat. 

Namun label training dibuat menggunakan katalog BPPTKG, yang berasal dari sistem pemantauan konvensional tersebut.

Jadi framework cadangan ini masih membutuhkan jawaban dari sistem yang hendak dicadangkannya.

> **Sekoci penyelamatnya masih terikat dengan tali pusar pada kapal yang diklaim hendak diselamatkan.**

Model terlatih memang secara teoritis dapat dijalankan tanpa katalog BPPTKG, tetapi naskah tidak pernah mengujinya pada periode ketika:

* katalog BPPTKG disembunyikan;
* stasiun dekat puncak tidak aktif;
* sebagian elemen array hilang;
* kualitas data memburuk saat krisis.

Bahkan penulis memilih periode dengan **99% data availability**, yaitu keadaan nyaris ideal—bukan kondisi kegagalan yang dipakai sebagai motivasi. 

Klaim resilience harus diuji melalui:

* station-dropout experiments;
* temporal hold-out;
* blind classification tanpa bantuan katalog;
* deployment pada periode aktivitas berbeda.

---

## 6. Resolusi array tidak pernah dibuktikan

Array memiliki:

* lima stasiun;
* spacing rata-rata sekitar 250 m;
* hanya komponen vertikal;
* bandpass 0,8–1,8 Hz.  

Pada apparent velocity 2,2–6,7 km/s, panjang gelombang di band tersebut berada pada orde sekitar 1–8 km. Aperture array hanya sebagian kecil dari panjang gelombang itu.

Namun penulis menggunakan batas keras:

[
|\Delta\mathrm{BAZ}|\le15^\circ
]

seolah kemampuan menentukan back-azimuth ±15° sudah terbukti. 

Tidak ada:

* array response function;
* beam pattern;
* side-lobe analysis;
* point-spread function;
* synthetic recovery;
* back-azimuth uncertainty;
* slowness uncertainty;
* sensitivity terhadap timing error;
* sensitivity terhadap coordinate error;
* station-dropout test;
* per-event uncertainty.

Dengan aperture seperti ini, batas ±15° tidak boleh diterima hanya karena terlihat rapi dalam tabel.

### Pembuktian minimum

Untuk berbagai frekuensi dan SNR:

1. injeksikan plane wave dengan back-azimuth diketahui;
2. tambahkan realistic noise;
3. recover back-azimuth dan slowness;
4. laporkan bias dan interval 95%;
5. ulangi untuk empat dan tiga stasiun;
6. tampilkan array transfer function.

Bila uncertainty back-azimuth ternyata ±25° atau ±40°, seluruh decision rule ±15° kehilangan fondasinya.

---

## 7. Urutan beamforming dan FK dijelaskan secara fisik membingungkan

Naskah menyatakan bahwa penulis:

1. mengoreksi propagation delays;
2. menggabungkan sinyal dengan beamforming;
3. menggunakan “enhanced wavefield” tersebut untuk mengestimasi back-azimuth dan slowness dengan FK. 

Masalahnya, setelah lima trace digabung menjadi satu beamformed trace, informasi spasial untuk FK telah hilang. FK membutuhkan multichannel array data.

Jadi ada dua kemungkinan:

* FK sebenarnya dihitung dari lima trace asli, tetapi penulisan metode salah; atau
* FK dihitung dari single beam, dan analisisnya tidak sah.

Lebih sirkular lagi, untuk “correct propagation delays” biasanya arah dan slowness harus diketahui atau dipindai terlebih dahulu. Jadi mana yang dilakukan lebih dulu?

* FK menentukan delay lalu beamforming?
* beamforming scan menentukan BAZ/slowness?
* beamforming dan FK adalah nama berbeda untuk operasi yang sama?
* conventional delay-and-sum atau Capon?

Saat ini, metode array-nya terdengar seperti:

> penulis membutuhkan arah untuk membentuk beam, lalu membutuhkan beam untuk menemukan arah.

Untuk naskah yang mengklaim array processing sebagai kontribusi utama, kekaburan ini tidak dapat ditoleransi.

---

## 8. Tidak ada bukti bahwa array processing benar-benar meningkatkan classification

Penulis secara eksplisit menyatakan bahwa input classifier hanyalah 11 fitur dari **satu beamformed waveform**, sedangkan beam power, back-azimuth, dan slowness tidak digunakan sebagai fitur machine learning. 

Tidak ada pembanding terhadap:

* satu stasiun terbaik;
* rata-rata sederhana lima stasiun;
* median stack;
* beamforming tanpa FK screening;
* catalogue matching tanpa array screening;
* classifier dengan array features;
* classifier tanpa beamforming.

Dengan demikian, naskah tidak membuktikan bahwa kata **array-based** di judul memberikan keuntungan apa pun.

Mungkin classifier yang sama pada satu stasiun memperoleh 73%. Mungkin simple stack memperoleh 75%. Mungkin FK tidak menambah satu event benar pun. Naskah tidak tahu.

> **Array adalah tokoh utama di judul, tetapi tidak pernah diminta menunjukkan kontribusinya dalam eksperimen.**

Wajib ada ablation:

| Konfigurasi           | Evaluasi            |
| --------------------- | ------------------- |
| Single station        | baseline            |
| Simple average stack  | baseline            |
| Delay-and-sum beam    | efek beamforming    |
| Beam + FK QC          | efek FK             |
| Beam + array features | manfaat penuh array |
| Catalogue labels only | efek screening      |

Tanpa tabel tersebut, “array-based framework” adalah branding, bukan hasil.

---

## 9. Filter 0,8–1,8 Hz hampir mensterilkan fitur spektral

Semua waveform difilter pada 0,8–1,8 Hz. Setelah itu penulis menghitung:

* dominant frequency;
* spectral centroid;
* energy centre;
* RMS bandwidth;
* spectral entropy.  

Artinya, penulis terlebih dahulu memaksa seluruh sinyal masuk ke lorong selebar 1 Hz, kemudian dengan serius mengukur di mana posisi energinya di dalam lorong tersebut.

> **Spektrum sudah dicekik oleh filter, lalu classifier diminta mendiagnosis bentuk lehernya.**

Figure 19 dan Figure 24 bahkan memperlihatkan spektrum hingga 10 Hz, padahal hampir seluruh energi secara desain harus berada di bawah 2 Hz. Plot kosong di atas 2 Hz bukan informasi geofisika; itu dokumentasi bahwa filter bekerja.

Band sempit mungkin masuk akal untuk stabilitas beamforming. Namun tidak ada alasan fitur klasifikasi harus diekstrak dari band yang sama.

Lakukan pemisahan:

* band array processing: 0,8–1,8 Hz;
* band feature classification: misalnya beberapa band lebih lebar;
* multiband features;
* wavelet or spectrogram features;
* sensitivity terhadap filter.

Saat ini, beberapa spectral features hampir pasti sangat berkorelasi karena semuanya merupakan transformasi dari spektrum yang sudah dibatasi secara agresif.

---

## 10. Zero filling dapat menciptakan fitur palsu

Data yang terputus digabung menggunakan:

```text
method=1, fill_value=0
```

sebelum taper dan filtering. 

Mengisi gap dengan nol dapat menciptakan:

* discontinuity;
* spectral leakage;
* perubahan zero-crossing;
* kurtosis palsu;
* perubahan standard deviation;
* energi frekuensi rendah/tinggi buatan;
* onset palsu setelah filtering.

Padahal enam dari sebelas fitur yang digunakan sangat sensitif terhadap hal-hal tersebut.

Window yang memotong gap harus:

* ditolak;
* atau diberi mask;
* atau hanya gap sangat pendek yang diinterpolasi secara terkontrol.

Naskah tidak melaporkan:

* jumlah gap;
* durasi gap;
* berapa event window mengandung gap;
* berapa fitur terpengaruh.

Menciptakan nol buatan lalu menghitung zero-crossing adalah lelucon yang terlalu mudah ditulis oleh reviewer.

---

## 11. Classifier kemungkinan besar belajar amplitudo, bukan jenis event

Fitur meliputi:

* maximum amplitude;
* standard deviation;
* mean;
* beberapa ukuran energi.

Penulis sendiri mengakui bahwa amplitude dipengaruhi oleh:

* source size;
* propagation;
* source distance;
* attenuation;
* site response,

dan classifier dapat mengeksploitasi faktor-faktor tersebut. 

Itu bukan limitation kecil untuk “future work.” Itu ancaman langsung terhadap interpretasi utama.

Regional earthquakes memiliki:

* distribusi jarak berbeda;
* magnitude berbeda;
* path berbeda;
* kemungkinan duration berbeda.

Maka classifier dapat saja belajar:

> besar amplitudo + bentuk envelope tertentu = regional earthquake,

bukan memahami event physics.

Figure 20 juga menunjukkan maximum amplitude dan standard deviation memiliki rentang sangat berbeda antarkelas. Figure 21 menunjukkan korelasi kuat antarfitur amplitude. Penulis sudah melihat confound-nya, lalu memilih memublikasikan hasil dan meminta generasi berikutnya memperbaikinya.

Tidak. Lakukan sekarang:

1. waveform peak normalization;
2. RMS normalization;
3. amplitude-feature removal;
4. distance-corrected amplitude;
5. model dengan morphology-only;
6. model dengan spectral-only;
7. model dengan amplitude-only;
8. SHAP/permutation importance;
9. performance comparison.

Bila accuracy jatuh dari 73% menjadi 45% setelah amplitude normalization, maka paper ini bukan classifier event type. Ia adalah **amplitude-and-distance detector**.

---

## 12. Mean waveform sebagai fitur hampir tidak berguna setelah detrending

Waveforms di-detrend dan mean offset dihilangkan. Setelah itu, “mean” tetap dimasukkan sebagai fitur.

Tidak mengherankan Figure 20 menunjukkan mean dekat nol untuk hampir seluruh kelas.

Ini memberi kesan feature set dipilih karena mudah dihitung, bukan karena mempunyai dasar fisik atau diskriminatif.

Pada level doktoral, daftar fitur bukan daftar belanja. Setiap fitur harus mempunyai:

* definisi;
* satuan;
* physical interpretation;
* stability;
* discriminative evidence;
* sensitivity to preprocessing.

---

## 13. Random split menciptakan leakage antar-event family

Dataset berasal dari satu array, satu lokasi, dan hanya 28 hari. Event vulkanik sering muncul dalam keluarga waveform yang sangat mirip.

Namun penulis menggunakan stratified random split 60:40, 70:30, 80:20, dan 90:10. 

Akibatnya, waveform dari event family yang sama dapat muncul:

* sebagian di training;
* sebagian di testing.

Model tidak diuji terhadap event baru. Model diuji terhadap saudara dekat event training.

Random split juga dapat membagi event dari hari yang sama ke train dan test, sehingga:

* noise background;
* instrument condition;
* weather;
* station response;
* event family;
* activity phase,

semuanya bocor melintasi split.

Validasi yang layak adalah:

* leave-one-day-out;
* leave-one-week-out;
* chronological hold-out;
* grouped split berdasarkan waveform family;
* event-cluster-disjoint split;
* independent month;
* independent eruptive episode.

Saya juga tidak menemukan random seed yang dilaporkan. Jadi “reproducible framework” bahkan belum menjamin bahwa seorang pengguna memperoleh pembagian event yang sama.

---

## 14. Penulis memilih hasil terbaik dari empat test set

Naskah mencoba empat proporsi train:test dan menonjolkan hasil terbaik, yaitu 80:20.

Pada split itu:

* test set hanya 55 event;
* XGBoost benar pada 40 event;
* SVM benar pada 35 event;
* perbedaannya hanya **lima event**.  

Confidence intervals:

* SVM: 0,4909–0,7455;
* XGBoost: 0,6000–0,8364.

Mereka tumpang tindih sangat luas.

Namun Abstract mengatakan XGBoost “outperforming” SVM, dan Discussion berbicara tentang “superior discriminative capability.”

> **Lima event dengan confidence interval bertumpuk bukan kemenangan algoritmik. Itu fluktuasi sampel yang mengenakan tiga angka desimal.**

Lebih buruk lagi, setelah melihat empat test sets, penulis memilih yang menghasilkan angka tertinggi sebagai headline. Test set tersebut tidak lagi benar-benar untouched; ia telah menjadi bagian dari model-selection narrative.

Satu event pada split 80:20 mengubah accuracy sebesar:

[
\frac{1}{55}=1.82%.
]

Pada split 90:10, satu event mengubah accuracy sebesar:

[
\frac{1}{28}=3.57%.
]

Menulis accuracy 72,73% memberikan kesan presisi yang tidak dimiliki eksperimen.

### Yang dibutuhkan

* repeated stratified nested cross-validation;
* group/temporal CV;
* sekurang-kurangnya 50–100 outer repetitions;
* paired comparison;
* McNemar test;
* paired bootstrap;
* distribution of performance, bukan satu angka;
* one final untouched test period.

---

## 15. “Increasing training proportion improves generalization” adalah inferensi yang salah

Penulis mengatakan peningkatan training proportion dari 60% ke 80% mengurangi misclassification dan menunjukkan generalization yang lebih baik. 

Tidak dapat disimpulkan demikian karena test sets-nya berbeda.

Perubahan accuracy dapat terjadi karena:

* training set lebih besar;
* test set lebih kecil;
* komposisi event test berubah;
* random sampling kebetulan lebih mudah.

Untuk membuat learning curve, test set harus tetap atau evaluasi dilakukan melalui repeated cross-validation dengan error bars.

Membandingkan empat test set berbeda seolah mereka empat tahap eksperimen terkontrol adalah statistik tingkat tutorial, bukan paper doktoral.

---

## 16. Hyperparameter search terlalu besar untuk dataset sekecil ini

Search space XGBoost memuat:

[
3\times2\times2\times2\times2\times3\times3\times3\times3
=========================================================

3{,}888
]

kombinasi.

Dengan five-fold CV, itu berarti sampai sekitar:

[
19{,}440
]

fits untuk mencari parameter terbaik pada training set yang hanya berisi 165–247 event. 

Hampir seluruh optimum berada di batas search grid:

* `n_estimators=150`: batas atas;
* `max_depth=2`: batas bawah;
* `learning_rate=0.05`: batas atas;
* `subsample=0.6`: batas bawah;
* `colsample_bytree=0.6`: batas bawah;
* `min_child_weight=3`: batas bawah;
* `gamma=0.5`: batas bawah;
* `reg_alpha=0`: batas bawah;
* `reg_lambda=2`: batas bawah.

Ini berarti grid tidak benar-benar membatasi optimum. Ia berhenti karena daftar kandidat habis.

Naskah juga memberikan **satu** set “optimal hyperparameters” dan mengatakan nilai itu dipakai untuk seluruh eksperimen. Tidak jelas:

* apakah tuning dilakukan pada split 60:40;
* pada split 80:20;
* pada seluruh dataset;
* atau diulang pada setiap split dan kebetulan identik.

Bila tuning memakai seluruh dataset, terjadi leakage. Bila tuning hanya memakai satu split, tiga eksperimen lainnya tidak dituning secara independen. Bila diulang, tampilkan hasil tiap split.

Selain itu, methods menyebut `class_weight` sebagai hyperparameter SVM, tetapi Table 2 tidak menyediakan search space-nya. Ini menunjukkan workflow dan manuscript tidak berasal dari satu versi analisis yang terkunci.

---

## 17. Persamaan SVM-RBF yang diberikan adalah persamaan SVM linear

Naskah menyebut model **SVM-RBF**, tetapi menulis:

[
f(x)=w\cdot x+b.
]



Itu adalah bentuk linear di input space. Untuk kernel RBF, bentuk keputusan yang relevan adalah:

[
f(x)=
\sum_{i\in SV}
\alpha_i y_i
\exp\left(-\gamma|x-x_i|^2\right)+b.
]

Ini bukan typo editorial yang remeh. Ini adalah persamaan model utama.

> **Penulis mengklaim menggunakan kernel nonlinear tetapi menjelaskan classifier linear. Pada level S3, tidak memahami persamaan algoritma utama adalah lampu merah, bukan noda tinta.**

Bagian textbook tentang SVM dan XGBoost sebaiknya dipangkas. Gunakan ruangnya untuk menjelaskan hal-hal yang justru hilang:

* matching algorithm;
* event-window placement;
* random seed;
* code version;
* uncertainty;
* label ambiguity;
* array resolution.

---

## 18. PCA diinterpretasikan secara keliru

Penulis mengatakan dua principal components menjelaskan 63,6% variance dan menyimpulkan bahwa “most of the information” dapat direpresentasikan dalam ruang berdimensi rendah. 

PCA mempertahankan **variance**, bukan class-discriminative information.

Fitur dengan variance kecil dapat sangat penting bagi klasifikasi. Sebaliknya, amplitude dengan variance besar dapat mendominasi PCA tetapi hanya merepresentasikan magnitude atau jarak.

Figure 21 juga menunjukkan empat kelas bertumpuk kuat pada PC1–PC2. Jadi visual tersebut lebih dekat kepada bukti bahwa separasi kelas lemah daripada bukti keberhasilan feature engineering.

PCA di sini hanya boleh digunakan untuk:

* mendeskripsikan covariance;
* mengidentifikasi redundancy;
* membantu visualisasi.

Ia tidak boleh dipakai untuk menyatakan feature set “preserves information required for classification” tanpa supervised test.

---

## 19. Nilai 72,73% tidak layak disebut “reliable classification”

Pada test set terbaik:

[
55-40=15
]

event salah diklasifikasikan.

Jadi sekitar 27% event salah bahkan setelah:

* event noise dibuang;
* ambiguous events dibuang;
* hanya event koheren dipilih;
* event harus cocok dengan katalog;
* event diperiksa secara manual;
* kelas dibatasi hanya empat.

Dalam kondisi semudah itu, satu dari empat masih salah.

Lebih mengkhawatirkan, naskah mengatakan kesalahan penting terjadi antara Multiphase dan regional earthquakes. 

Dalam monitoring operasional, membingungkan event vulkanik dengan gempa regional bukan kekeliruan kosmetik.

Figure 24 kemudian justru memilih contoh Multiphase yang salah diklasifikasikan sebagai Rockfall, bukan regional earthquake, sehingga narasi error analysis-nya sendiri tidak konsisten. 

Gunakan istilah:

> moderate classification skill on a selected four-class subset.

Bukan:

> reliable classification.

---

## 20. Tidak ada kelas noise, unknown, atau event lain

Framework hanya mengklasifikasikan event yang:

* berhasil dideteksi;
* lolos coherence;
* lolos FK;
* cocok katalog;
* dan lolos manual inspection.

Seluruh noise, event ambigu, local anthropogenic signals, tremor, event lain, dan kemungkinan event tak berkatalog dibuang sebelum classifier melihatnya.

Maka model ini tidak dapat menjawab pertanyaan operasional:

> Apakah window ini VTB, Rockfall, Multiphase, regional earthquake, noise, atau sesuatu yang belum pernah dilihat?

Ini adalah **closed-set classification on prevalidated windows**, bukan continuous volcanic monitoring.

Untuk klaim operasional, perlu:

* noise class;
* unknown/open-set class;
* rejected-event evaluation;
* end-to-end detection + classification;
* false-alarm rate per hari;
* event-rate-normalized performance;
* confidence/rejection threshold.

Tanpa itu, classifier hanya bekerja setelah manusia dan katalog menyelesaikan bagian tersulit.

---

## 21. SMOTE belum tentu diperlukan dan dapat menghasilkan “gempa sintetis” yang tidak fisik

Class counts adalah 49–84. Imbalance ratio hanya sekitar 1,7:1.

Pada dataset sekecil ini, SMOTE menginterpolasi feature vectors dan dapat menghasilkan kombinasi seperti:

* amplitude tinggi;
* kurtosis rendah;
* entropy tertentu;
* bandwidth tertentu,

yang belum tentu dimiliki waveform nyata.

Bandingkan minimal:

* tanpa balancing;
* `class_weight`;
* random oversampling;
* SMOTE;
* Borderline-SMOTE.

Lebih penting lagi, laporkan apakah XGBoost tetap unggul tanpa synthetic samples. Saat ini, kita tidak tahu apakah model belajar struktur data atau geometri buatan SMOTE.

---

## 22. Tidak ada evaluasi manfaat beamforming terhadap SNR

Naskah berkali-kali mengatakan beamforming meningkatkan SNR. Namun tidak ada tabel yang menunjukkan:

[
\Delta \mathrm{SNR}
===================

## \mathrm{SNR}_{beam}

\mathrm{SNR}_{single}.
]

Tidak ada:

* median gain;
* distribution;
* per-class gain;
* station-to-beam comparison;
* effect on detection recall;
* effect on classification score.

Figure satu atau dua event yang dipilih penulis bukan bukti populasi.

Kalau beamforming adalah salah satu kontribusi utama, tampilkan statistik seluruh 275 event. Bila median SNR gain hanya 0,5 dB, narasi perlu diubah.

---

## 23. “Source location” dari satu array kecil adalah overclaim

Naskah menyatakan konfigurasi pentagonal digunakan untuk memperkirakan propagation direction dan source location. 

Satu array pada dasarnya memberikan:

* back-azimuth;
* apparent slowness;
* mungkin wavefront curvature bila aperture dan SNR memadai.

Ia tidak memberikan unique source location tanpa:

* range information;
* velocity model;
* second array;
* curvature constraint yang kuat;
* atau katalog eksternal.

Gunakan istilah:

> source-direction estimation atau directional discrimination.

Bukan source localization, kecuali range benar-benar diinversi dan divalidasi.

---

## 24. Klaim generalisasi melampaui data

Dataset berasal dari:

* satu volcano;
* satu array;
* satu lokasi;
* satu konfigurasi;
* satu periode 28 hari;
* satu bandpass;
* satu musim;
* satu kondisi operasional;
* empat kelas.

Penulis sendiri mengaku bahwa robustness terhadap periode lebih panjang dan volcano lain belum diuji. 

Namun Conclusion tetap menyatakan bahwa framework memperluas machine learning “beyond conventional near-field monitoring networks” dan menyediakan fondasi monitoring jarak jauh. 

Tidak.

Yang telah dibuktikan hanyalah:

> Pada satu bulan tertentu, sejumlah event Merapi yang bersih dan cocok katalog dapat diklasifikasikan secara moderat menggunakan dua algoritma standar.

Generalisasi membutuhkan:

* bulan independen;
* musim independen;
* episode erupsi lain;
* volcano lain;
* array lain;
* sensor lain;
* leave-one-station-out;
* domain adaptation.

---

## 25. “Long-distance” adalah adjective pemasaran

Array berada sekitar 16 km dari summit. 

Itu memang lebih jauh daripada stasiun 3 km, tetapi dalam terminologi seismologi umum tetap merupakan observasi lokal/distal, bukan “long-distance” dalam arti regional atau teleseismik.

Istilah yang lebih presisi:

* distal volcanic array;
* off-edifice array;
* remote local array;
* 16-km-offset array.

Judul saat ini membuat 16 km terdengar seperti sinyal telah melintasi benua.

---

## 26. Kontribusi AI sangat tipis

Isi AI-nya adalah:

* 11 handcrafted features;
* SVM-RBF;
* XGBoost;
* GridSearchCV;
* SMOTE.

Tidak ada:

* metode AI baru;
* representation learning;
* domain adaptation;
* uncertainty-aware classification;
* open-set recognition;
* explainability yang bermakna;
* benchmark dataset terbuka;
* external validation;
* baseline lengkap;
* operational deployment.

Penulis sendiri mengatakan kontribusi utama bukan classifier baru, melainkan dataset construction. 

Masalahnya, dataset-nya tidak dibuka.

Naskah ini saat ini terjebak di tempat yang tidak nyaman:

> terlalu sedikit novelty untuk paper AI, terlalu tertutup untuk data paper, dan terlalu sedikit temuan gunung api untuk paper geosains.

---

## 27. Reproducibility runtuh karena data tidak tersedia

Data Availability menyatakan waveform tidak tersedia untuk publik dan hanya mungkin diberikan dengan izin UGM. 

Tidak ada persistent repository untuk:

* 275 event labels;
* feature matrix;
* timestamps;
* catalogue matches;
* rejection reasons;
* beamforming parameters;
* FK outputs;
* exact train/test indices;
* random seed;
* preprocessing scripts;
* trained models;
* environment;
* code commit.

Untuk naskah yang mengulang kata **reproducible**, kondisi ini tidak dapat diterima.

Bila raw waveform memang dibatasi, setidaknya buka:

1. feature table;
2. event metadata;
3. labels;
4. match residuals;
5. BAZ/slowness/semblance;
6. decision flags;
7. fixed split indices;
8. scripts;
9. synthetic or anonymized waveform subset;
10. trained model.

> **Reproducibility yang bergantung pada izin personal bukan reproducibility. Itu hospitality.**

---

# Masalah editorial dan penulisan

## 1. Figure dan table numbering sudah kehilangan kontak dengan realitas

Contohnya:

* Figure 2 disebut “Fig 14” dalam Methods; 
* class distribution dirujuk sebagai `Error! Reference source not found`; 
* Figure 6 disebut Fig 18;
* Figure 7 disebut Fig 19;
* Figure 8 disebut Fig 20;
* Figure 9 disebut Fig 21;
* Figure 10 disebut Fig 22;
* Figure 11 disebut Fig 23;
* Figure 12 disebut Fig 24;
* ROC bahkan dirujuk sebagai Fig 1 di Discussion.

Ini bukan satu typo. Ini tanda bahwa manuscript dirakit dari beberapa versi tanpa quality control.

Table numbering juga kacau: setelah Table 2, muncul kembali “Table 1” untuk class distribution.

Reviewer tidak seharusnya diminta melakukan arkeologi versi dokumen.

---

## 2. Kalimat berulang dan bertabrakan

Contoh yang sangat terang:

> “variations are observed in the dominant-frequency peaks, spectral-energy distribution, and spectral amplitudes”

ditulis dua kali dalam satu kalimat. 

Contoh lain:

> “enabling discrimination between distinguishing the four seismic-event classes”

dan kalimat berakhir dengan dua titik.

Naskah mendeklarasikan penggunaan Grammarly, tetapi masih memuat:

* “for for”;
* “Harardz”;
* “commercial of financial relationship”;
* “conflict oof interest”;
* “This study propose”;
* “array-bassed”;
* `Error! Reference source not found`. 

> **Tampaknya Grammarly juga tidak mau bertanggung jawab atas naskah ini.**

---

## 3. Prosa mencoba membuat novelty melalui repetisi

Dari penghitungan teks seluruh PDF, termasuk cover letter dan appendix:

* `framework`: sekitar 42 kali;
* `proposed`: sekitar 36 kali;
* `dataset`: sekitar 77 kali;
* `classification`: sekitar 90 kali;
* frasa `proposed framework`: 17 kali;
* `temporal and spectral features`: 19 kali;
* `catalogue-matched`: 14 kali;
* `remote seismic array`: 20 kali.

Naskah berkali-kali mengulang:

> “catalogue-matched, array-quality-controlled labelled dataset”

seolah semakin banyak hyphen akan semakin kuat validasinya.

> **Novelty tidak dapat diproduksi dengan mengulang nama workflow sampai pembaca menyerah.**

Potong naskah sedikitnya 25–30%. Satu penjelasan tajam lebih ilmiah daripada enam parafrasa yang semuanya mengatakan hal sama.

---

## 4. Referensi tampak ditumpuk tanpa pemeriksaan relevansi

Bagian ROC mengutip referensi [41–43]. Namun [41] adalah paper tentang evaluasi kesalahan produk curah hujan GPM IMERG dan TRMM.  

Mengutip paper koreksi error curah hujan sebagai landasan ROC untuk klasifikasi gempa menunjukkan citation assembly, bukan literature synthesis.

Kesalahan lain:

* Cortes dan Vapnik ditulis “Cortez”;
* “Machine Leaming”;
* DOI berulang `https://doi.org/https://doi.org`;
* judul dan nama jurnal tidak konsisten;
* beberapa referensi hampir tidak relevan terhadap volcano-seismic classification;
* SVM-RBF dibandingkan dengan “linear SVM-RBF,” istilah yang kontradiktif.

Daftar pustaka membutuhkan audit manual satu per satu.

---

# Sisi visual

## Figure 17: dua contoh bukan validasi array

Hanya satu regional earthquake dan satu VTB ditampilkan. Keduanya tampak dipilih karena menghasilkan gambar yang bagus.

Yang dibutuhkan:

* seluruh distribusi BAZ residual;
* slowness residual;
* beam power;
* semblance;
* uncertainty;
* accepted versus rejected events;
* class-wise summary.

## Figure 18: justru memperlihatkan kelemahan representativeness

Panel atas menunjukkan ratusan event katalog per hari. Panel tengah hanya menunjukkan belasan kandidat dan event tervalidasi.

Secara visual, gambar itu mengatakan:

> framework hanya melihat sebagian amat kecil dari aktivitas yang tercatat BPPTKG.

Namun Discussion membacanya sebagai bukti reliability.

## Figure 20: overlap fitur besar

Violin plots memperlihatkan overlap yang luas. Maximum amplitude dan standard deviation juga memiliki tails ekstrem, terutama regional earthquake. Ini menguatkan dugaan amplitude confounding.

## Figure 21: PCA tidak menunjukkan empat cluster yang jelas

PCA score plot memperlihatkan empat kelas bercampur. Jadi figure ini tidak mendukung kalimat bahwa feature space mempunyai separability yang kuat.

## Figure 22: confusion matrices terlalu kecil

Delapan confusion matrices dijejalkan dalam satu figure. Angkanya sulit dibaca dan tidak ada normalization percentage. Gunakan:

* satu repeated-CV aggregate confusion matrix;
* confidence intervals per cell;
* class recall/precision.

## Figure 23: AUC dari lima event tidak bermakna

Pada split 90:10, test set regional earthquake hanya memiliki lima contoh dan kelas lain tujuh sampai sembilan. 

ROC curve dari lima positives adalah staircase dekoratif. Tanpa confidence band, AUC dua desimal hanya menipu mata.

## Figure 24: contoh terpilih bukan error analysis

Memilih beberapa event benar dan dua event salah tidak membuktikan alasan kegagalan. Lakukan:

* systematic error stratification;
* SHAP distribution;
* error versus SNR;
* error versus amplitude;
* error versus date;
* error versus BAZ residual;
* error versus catalogue-match residual.

---

# Analisis wajib sebelum resubmission

## 1. Bangun gold-standard labels

* minimal dua ahli independen;
* blind annotation;
* consensus adjudication;
* inter-rater agreement;
* uncertainty/ambiguous class;
* label provenance.

## 2. Audit catalogue matching

* one-to-one matching;
* residual-time distribution;
* predicted arrival calculation;
* conflict resolution;
* accidental-match simulation;
* sensitivity terhadap tolerance;
* per-event match confidence.

## 3. Evaluasi detection end-to-end

* precision;
* recall;
* F1;
* false alarms/day;
* class-wise recovery;
* magnitude/amplitude-dependent recovery;
* manual audit automatic-only and rejected events.

## 4. Buktikan kemampuan array

* array response;
* synthetic back-azimuth recovery;
* slowness uncertainty;
* beam power/semblance distributions;
* timing-error sensitivity;
* station dropout;
* predicted versus observed BAZ.

## 5. Lakukan array ablation

Bandingkan single station, simple stack, beamforming, beamforming + FK, dan array features.

## 6. Desain ulang validation

* nested repeated group CV;
* group by day/week/event family;
* chronological test period;
* fixed external test set;
* paired significance;
* report mean, median, SD, and intervals.

## 7. Hentikan test-set shopping

Pilih satu evaluation protocol sebelum melihat hasil. Jangan menjadikan split dengan accuracy tertinggi sebagai headline.

## 8. Audit feature physics

* broad-band versus narrow-band;
* amplitude normalization;
* feature ablation;
* distance correction;
* morphology-only;
* spectral-only;
* amplitude-only;
* SHAP/permutation importance.

## 9. Tambahkan open-set evaluation

Masukkan noise, ambiguous events, unclassified volcanic events, dan unknown signals.

## 10. Buka hasil penelitian

Release minimal:

* event list;
* labels;
* feature matrix;
* matching table;
* array metrics;
* train/test groups;
* code;
* environment;
* seeds;
* trained models.

## 11. Ulangi pada data independen

Minimal satu periode berbeda. Lebih baik satu volcano atau satu array berbeda.

---

# Pertanyaan untuk menguji Dairoh

1. **Apa definisi ground truth dalam penelitian ini? Mengapa katalog yang menyediakan label disebut independent validation?**

2. **Dengan rata-rata 354 event BPPTKG per hari, berapa probabilitas accidental match dalam window 50 s?**

3. **Berapa recall array terhadap setiap kelas BPPTKG? Bukan acceptance rate—recall.**

4. **Mengapa hanya 226 dari 9.924 event vulkanik yang masuk dataset? Apa karakteristik 97,7% yang hilang?**

5. **Berapa resolusi back-azimuth array lima stasiun pada 0,8, 1,3, dan 1,8 Hz?**

6. **Bagaimana FK dihitung setelah sinyal sudah digabung menjadi satu beamformed trace?**

7. **Bagaimana propagation delay ditentukan sebelum arah dan slowness diketahui?**

8. **Apakah classifier single-station lebih buruk daripada classifier beamformed? Tunjukkan angkanya.**

9. **Mengapa spectral centroid dan RMS bandwidth dihitung setelah data dibatasi 0,8–1,8 Hz?**

10. **Apa pengaruh `fill_value=0` terhadap zero-crossing, kurtosis, dan spectral entropy?**

11. **Apakah XGBoost masih memperoleh 72% setelah maximum amplitude dan standard deviation dihapus?**

12. **Mengapa random event split dianggap independent ketika event dari family dan hari yang sama dapat berada di train dan test?**

13. **Mengapa hasil 40/55 dianggap superior terhadap 35/55 ketika confidence intervals bertumpuk?**

14. **Mengapa empat test splits dicoba lalu yang tertinggi dijadikan hasil utama?**

15. **Grid XGBoost menguji 3.888 kombinasi. Bagaimana Anda mengendalikan winner’s curse pada training set 220 event?**

16. **Mengapa persamaan yang ditulis untuk SVM-RBF adalah persamaan linear SVM?**

17. **Mengapa 63,6% explained variance PCA dianggap sebagai 63,6% informasi untuk klasifikasi?**

18. **Bagaimana model akan beroperasi ketika BPPTKG tidak tersedia, padahal label training bergantung pada BPPTKG?**

19. **Mengapa dataset yang menjadi kontribusi utama tidak dibuka?**

20. **Apa kontribusi ilmiah yang tetap tersisa bila satu stasiun dan logistic regression menghasilkan performa yang sama?**

Bila mahasiswa menjawab pertanyaan-pertanyaan ini dengan “future work,” maka masalahnya bukan kekurangan ruang dalam manuscript. Masalahnya adalah eksperimen inti belum dilakukan.

---

# Contoh komentar kepada editor

> **Recommendation: Reject.** The manuscript addresses a relevant monitoring problem, but it does not yet demonstrate the validity or generalizability of the proposed dataset-construction framework. The reported labels are transferred from the BMKG and BPPTKG catalogues rather than independently validated; matching tolerances are broad, and the only manual quality control was performed by the first author without inter-annotator assessment. From more than 10,000 reference-catalogue events, only 442 candidates and 275 selected events enter the analysis, yet detection recall and false-negative rates are not reported. The five-station, approximately 250-m-aperture array is used with a hard ±15° back-azimuth criterion without array-response or recovery tests. No ablation demonstrates that beamforming or FK analysis improves dataset quality or classification relative to a single station or simple stack. The machine-learning evaluation uses random splits from a single 28-day period, allowing likely leakage between temporally adjacent waveform families. The headline 72.73% accuracy represents 40 correct classifications among only 55 test events and is selected from four alternative train–test splits; confidence intervals overlap substantially with SVM. The RBF-SVM formulation is also incorrectly presented as a linear decision function. Finally, the waveform data and processing code are not publicly available, which is incompatible with the manuscript’s repeated claims of reproducibility. A complete redesign of the label audit, array validation, machine-learning evaluation, and data release is required.

# Putusan akhir

## **REJECT**

Data dan array-nya berpotensi. Pertanyaan ilmiahnya relevan. Tetapi naskah saat ini belum menunjukkan bahwa:

* labelnya benar;
* matching-nya unik;
* detector-nya sensitif;
* array-nya memiliki resolusi ±15°;
* beamforming memberi manfaat;
* spectral features merepresentasikan sumber;
* amplitude tidak menjadi shortcut;
* random split bebas leakage;
* XGBoost sungguh lebih baik;
* model dapat menangani noise dan unknown events;
* framework dapat digeneralisasi;
* atau analisisnya dapat direproduksi.

Yang dibuktikan baru:

> **Dari 275 event bersih yang telah dipilih dengan bantuan katalog dan inspeksi manual, XGBoost mengklasifikasikan 40 dari 55 event pada satu random split.**

Itu hasil pilot study. Bukan full-length demonstration dari framework machine learning yang reliable.

Pada level mahasiswa S3, manuscript ini terlalu banyak menguasai kosakata—*framework, validated, reliable, systematic, independent, generalizable*—dan terlalu sedikit memberikan eksperimen yang membuat kosakata tersebut benar.

**Jangan poles kalimatnya dahulu. Bongkar eksperimennya.**
