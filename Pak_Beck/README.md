# Laporan Reviewer Paper SOM Pak Beck

Naskah yang dinilai adalah **“Spatiotemporal Analysis of the 2018 Lombok Earthquake Sequence Using a Simplified Manual Self-Organizing Map”** oleh Bakti Sukrisna dan rekan-rekan. 

## Rekomendasi: **REJECT — tidak layak diperbaiki hanya melalui revisi narasi**

Versi 18 Agustus ini memang lebih jujur daripada versi sebelumnya. Penulis sekarang terang-terangan mengakui bahwa:

* jumlah neuron delapan ditentukan sejak awal;
* algoritmanya bukan Self-Organizing Map konvensional;
* urutan event tidak diacak;
* learning rate meluruh sangat agresif;
* magnitude tidak homogen;
* (M_c) C1 dipilih ulang secara manual;
* tahap-tahap temporal saling tumpang tindih;
* focal mechanism tidak dipasangkan ke masing-masing cluster.

Masalahnya, setelah menuliskan daftar pengakuan dosa tersebut, naskah tetap melanjutkan kesimpulan yang sama: delapan *seismogenic domains*, empat tahap evolusi, progressive localization, postseismic redistribution, serta implikasi bahaya gempa. 

> **Naskah ini telah belajar mengakui kelemahannya, tetapi belum belajar memperbaikinya.**

*Limitation section* bukan surat pengampunan metodologis. Bila keterbatasan tersebut menghancurkan identifiability hasil, menuliskannya secara jujur tidak membuat hasil tiba-tiba valid.

| Aspek                             |      Nilai |
| --------------------------------- | ---------: |
| Pentingnya kasus Lombok 2018      |        4/5 |
| Kualitas katalog untuk tujuan ini |        1/5 |
| Ketepatan nama algoritma          |      0.5/5 |
| Pemilihan jumlah cluster          |        0/5 |
| Analisis stabilitas               |        0/5 |
| Validitas inferensi temporal      |      0.5/5 |
| Analisis Gutenberg–Richter        |        1/5 |
| Validasi fisik                    |        1/5 |
| Kebaruan ilmiah                   |        1/5 |
| Kematangan level doktoral         |        1/5 |
| **Putusan**                       | **Reject** |

---

# Diagnosis utama

Naskah ini melakukan hal berikut:

1. memasukkan **easting, northing, depth, dan time** ke algoritma;
2. memerintahkan algoritma membentuk **tepat delapan prototype**;
3. menggunakan prosedur training yang hampir membeku setelah beberapa epoch;
4. menyusun cluster kembali berdasarkan time yang sudah menjadi input;
5. menggunakan kembali space, time, dan depth untuk menyatakan bahwa cluster berbeda;
6. mengelompokkan delapan cluster secara manual menjadi empat tahap;
7. menempelkan b-value, focal mechanism, Flores Thrust, dan Rinjani sebagai penjelasan;
8. lalu menyebut konstruksi tersebut sebagai *data-driven seismotectonic reconstruction*.

> **Ini bukan penemuan empat tahap evolusi seismotektonik. Ini sebuah taksonomi yang dirakit oleh penulis, lalu diberi legitimasi retroaktif oleh statistik deskriptif.**

---

# 1. Ini tetap bukan Self-Organizing Map

Penulis mengakui bahwa algoritma:

* hanya memperbarui Best Matching Unit;
* tidak menggunakan fungsi neighbourhood;
* tidak memiliki neighbourhood radius;
* tidak memperbarui adjacent neurons;
* tidak mempertahankan topologi pada lattice.

Namun judul dan hampir seluruh naskah tetap mempertahankan merek **Self-Organizing Map**. 

Tanpa neighbourhood learning, unsur yang menjadikan SOM sebagai **map** dan **self-organizing topology-preserving representation** sudah dicabut. Yang tersisa adalah *winner-take-all competitive vector quantization*, sangat dekat secara konseptual dengan *online k-means*.

Menyebutnya “simplified manual SOM” tidak menyelesaikan masalah. Itu seperti melepas mesin, transmisi, dan setir sebuah mobil, lalu menyebut sisanya “simplified manual automobile.”

Lebih buruk lagi, kata **manual** juga tidak jelas. Algoritma dijalankan secara deterministik pada komputer. Apa yang manual?

* pemilihan delapan neuron?
* pemilihan learning rate?
* pengelompokan empat tahap?
* pemilihan (M_c) untuk C1?

Bila jawabannya semua, justru itulah masalahnya.

### Konsekuensi

Penulis tidak boleh mengklaim:

* topology preservation;
* nonlinear mapping dari SOM;
* neuron-lattice organisation;
* SOM-derived evolutionary topology;
* novelty berbasis SOM.

Judul yang jujur seharusnya berbunyi seperti:

> **A Deterministic Winner-Take-All Vector Quantization of the 2018 Lombok Earthquake Catalogue**

Masalahnya, setelah nama metode dibuat jujur, kebaruannya langsung tampak jauh lebih tipis. Itu bukan kesalahan judul; itu diagnosis kontribusi.

---

# 2. Delapan cluster tidak ditemukan—delapan cluster dipesan sebelumnya

Arsitektur (K=8) ditentukan *a priori*. Penulis mengakui tidak ada optimasi terhadap jumlah cluster dan tidak mengklaim bahwa delapan merupakan solusi unik atau optimal. 

Namun Abstract tetap mengatakan bahwa konfigurasi tersebut “partitioned the catalogue into eight statistical clusters,” lalu memperlakukannya sebagai delapan domain fisik dan membangun empat tahap seismotektonik di atasnya. 

Tentu algoritma menghasilkan delapan cluster. Penulis memberinya delapan prototype.

> **Sebuah mesin yang diperintah menghasilkan delapan kotak lalu menghasilkan delapan kotak tidak sedang menemukan delapan domain geologi. Ia hanya sedang patuh.**

Tidak tersedia:

* silhouette score;
* gap statistic;
* Davies–Bouldin index;
* Calinski–Harabasz index;
* likelihood;
* stability under bootstrap;
* adjusted Rand index;
* variation of information;
* persistence across (K);
* physical validation untuk menentukan (K).

Pernyataan bahwa ukuran akhirnya berbeda-beda—18 event pada C1 dan 66 pada C4—juga bukan validasi. Itu hanya menunjukkan bahwa prototype akhir memiliki Voronoi cells dengan populasi berbeda. 

### Pertanyaan yang menghancurkan keseluruhan paper

* Apakah C3 dan C4 masih muncul bila (K=7)?
* Apakah “C3–C4 transition” tetap ada bila (K=9)?
* Apakah empat tahap tetap muncul bila (K=6)?
* Berapa banyak event yang mempertahankan labelnya setelah bootstrap?
* Apakah hasil tersebut lebih stabil daripada k-means biasa?

Naskah tidak mengetahui jawabannya.

Maka seluruh cerita C1–C8 berdiri di atas angka delapan yang dipilih penulis sendiri. Ini bukan *data-driven*. Ini **author-driven partitioning**.

---

# 3. Waktu dimasukkan ke algoritma, lalu output-nya dijual sebagai evolusi temporal

Input model adalah:

[
\mathbf{x}_i=(E_i,N_i,Z_i,t_i).
]

Waktu kemudian dipakai lagi untuk:

* menghitung mean date;
* menghitung median date;
* mengurutkan cluster;
* menyusun “evolution”;
* membentuk empat tahap;
* menafsirkan pre-, co-, dan postseismic behaviour. 

Ini merupakan sirkularitas metodologis.

> **Penulis memasukkan kalender ke dalam algoritma, kemudian terkesima ketika output-nya dapat diurutkan menurut kalender.**

Penambahan minimum, median, mean, dan maximum date memang perbaikan. Tetapi justru tabel baru tersebut memperlihatkan bahwa cerita empat tahap sangat rapuh.

Contohnya:

* C8, yang disebut domain paling awal, berlangsung sampai **14 April 2019**;
* C1 berlangsung dari **25 September 2017 sampai 9 Juni 2019**;
* C4, yang diklaim sebagai main-sequence/early-aftershock domain, berlangsung sampai **3 Mei 2019**;
* C6 sudah mulai **19 Agustus 2018**, ketika C4 masih sangat aktif;
* C1 dan C5 memiliki mean date sama, tetapi median-nya **10 Juni** versus **19 Agustus 2018**. 

Dua distribusi yang median-nya berbeda sekitar 70 hari bukan “coeval” hanya karena rata-ratanya kebetulan sama. Mean C5 jelas ditarik ke belakang oleh sejumlah kejadian awal.

Penulis sekarang mengatakan tahap-tahap tersebut tidak strictly non-overlapping. Itu jujur, tetapi menimbulkan pertanyaan:

> Bila tidak memiliki batas temporal, tidak berurutan secara eksklusif, dan anggotanya tumpang tindih berbulan-bulan, dalam arti apa mereka merupakan “stages”?

Jawabannya: dalam arti ilustrasi konseptual yang dibuat penulis setelah melihat hasil.

### Desain yang lebih sah

Bila tujuan utamanya menemukan evolusi temporal:

1. cluster berdasarkan **space and depth only**;
2. pertahankan time sebagai variabel independen;
3. kemudian uji apakah cluster tersebut memiliki temporal organisation yang signifikan.

Alternatifnya, gunakan metode yang memang dirancang untuk perubahan temporal:

* change-point analysis;
* hidden Markov model;
* space–time DBSCAN;
* ETAS-based classification;
* moving-window mixture model.

Saat ini, kesimpulan temporal sudah ditanam di input.

---

# 4. Training schedule-nya nyaris sebuah parodi optimasi

Learning rate awal adalah 0.01 dan dibagi dua setiap epoch. Data diproses dalam urutan tetap, tanpa random shuffling, selama 100 epoch. 

Dengan aturan penulis:

[
\alpha_e=0.01(0.5)^e.
]

Maka:

[
\alpha_{10}\approx9.8\times10^{-6},
]

[
\alpha_{20}\approx9.5\times10^{-9},
]

dan

[
\alpha_{100}\approx7.9\times10^{-33}.
]

Pada epoch ke-20, algoritma praktis sudah membatu. Epoch ke-100 tidak sedang belajar; ia hanya menghadiri upacara pemakaman learning rate.

> **Seratus epoch di sini adalah angka dekoratif. Hampir semua pembelajaran selesai pada beberapa epoch pertama, tepat ketika pengaruh inisialisasi dan urutan event paling kuat.**

Karena metode bersifat online dan event diproses dalam fixed order, hasil dapat sangat sensitif terhadap:

* urutan katalog;
* event yang muncul awal;
* event yang muncul akhir dalam tiap epoch;
* prototype initialization.

Penulis mengakui bahwa reproducibility tidak sama dengan stability. Bagus. Namun setelah mengakuinya, tidak ada stability test yang dilakukan.

Repeated execution menghasilkan hasil sama karena tidak ada randomness. Itu bukan robustness.

> **Jam mati juga sangat reproducible: ia salah dengan cara yang persis sama setiap hari.**

Analisis yang wajib:

* 100–500 random permutations event order;
* random initialization;
* k-means++ initialization;
* principal-component initialization;
* alternative decay schedules;
* batch centroid recomputation;
* convergence curve;
* assignment probability setiap event;
* adjusted Rand index antar-run.

Tanpa itu, label C1–C8 mungkin hanya sidik jari urutan file CSV.

---

# 5. Inisialisasi radial empat dimensi arbitrer dan kemungkinan mendominasi hasil

Penulis menghitung norma Euclidean setiap vector yang sudah dinormalisasi, mengurutkannya, lalu membagi hasil tersebut menjadi delapan radial partitions sebagai prototype awal. 

Ini bukan inisialisasi netral.

Setelah min–max scaling, norma

[
R_i=\sqrt{E_i'^2+N_i'^2+Z_i'^2+t_i'^2}
]

mengukur jarak dari sudut ((0,0,0,0)), yaitu kombinasi:

* easting minimum;
* northing minimum;
* depth minimum;
* waktu paling awal.

Mengapa sudut itu mempunyai makna seismotektonik?

Tidak ada.

Radial partition tersebut secara implisit menyusun event sepanjang diagonal buatan dalam ruang E–N–Z–T. Karena learning rate membeku sangat cepat, prototype awal ini sangat mungkin meninggalkan jejak kuat pada hasil akhir.

Dengan kata lain, delapan domain mungkin bukan organisasi alami katalog, melainkan delapan kulit bawang di sekitar origin buatan hasil min–max scaling.

Inisialisasi ini harus dibandingkan dengan:

* random initialization;
* k-means++;
* farthest-point initialization;
* principal components;
* hierarchical centroids.

Bila hasil berubah, interpretasi tektoniknya runtuh.

---

# 6. Min–max normalization bukan pembenaran fisik bagi metric

Penulis mengatakan min–max normalization memungkinkan empat dimensi berkontribusi sebanding. 

Tidak.

Min–max hanya menyamakan rentang numerik. Ia tidak menjawab pertanyaan fisik:

> Berapa hari setara dengan berapa kilometer?

Dalam model ini:

* keseluruhan rentang easting bernilai satu;
* keseluruhan rentang northing bernilai satu;
* rentang depth 3.8–303.5 km bernilai satu;
* rentang waktu hampir dua tahun bernilai satu.

Tidak ada teori seismologi yang menyatakan bahwa:

* 300 km kedalaman;
* ratusan kilometer horizontal;
* hampir 700 hari;

harus mempunyai bobot yang sama.

Selain itu, horizontal location memiliki **dua dimensi**, E dan N. Maka dalam squared Euclidean distance, lokasi horizontal secara potensial menyumbang dua unit, sedangkan time dan depth masing-masing hanya satu. Ini adalah prior tersembunyi bahwa horizontal position dua kali lebih penting daripada time atau depth.

Deep events hingga 303.5 km juga mengompresi variasi depth kerak. Perbedaan depth 10 dan 20 km hanya sekitar:

[
\frac{10}{303.5-3.8}\approx0.033
]

dalam normalized space.

Artinya, perbedaan geologis besar antara gempa 10 dan 20 km dapat berkontribusi lebih kecil daripada beberapa minggu perbedaan waktu.

Tidak ada sensitivity test terhadap:

* z-score scaling;
* robust scaling;
* Mahalanobis distance;
* feature weighting;
* pengeluaran deep events;
* perubahan observation window.

Maka geometry clustering adalah keputusan penulis yang disamarkan sebagai normalisasi objektif.

---

# 7. “Independent post-hoc characterization” adalah penyalahgunaan kata *independent*

Cluster dibentuk menggunakan E, N, Z, dan time. Setelah itu penulis “memvalidasi” cluster menggunakan:

* spatial centroid;
* radial dispersion;
* mean depth;
* depth dispersion;
* mean date;
* temporal range.

Itu adalah variabel yang sama yang digunakan untuk membuat cluster. 

Tidak mengherankan bila cluster berbasis depth mempunyai mean depth berbeda.

Tidak mengherankan bila cluster berbasis space mempunyai centroid berbeda.

Tidak mengherankan bila cluster berbasis time mempunyai mean date berbeda.

> **Penulis membuat kelompok menggunakan soal E–N–Z–T, lalu memeriksa jawabannya menggunakan E–N–Z–T dan memberi nilai lulus kepada dirinya sendiri.**

Magnitude memang tidak dimasukkan secara eksplisit. Tetapi magnitude tidak otomatis menjadi statistically independent karena:

* gempa besar terjadi pada waktu tertentu;
* berada pada lokasi tertentu;
* mempunyai depth tertentu;

dan ketiganya sudah digunakan dalam clustering.

Istilah yang benar adalah:

> **post-hoc variables not directly included in training**

bukan:

> **independent evidence**.

Independensi bukan sifat yang muncul hanya karena sebuah kolom tidak dimasukkan ke matrix input.

---

# 8. Katalog 248 event terlalu miskin untuk ambisi interpretasi sebesar ini

Katalog hanya terdiri atas 248 event, magnitude 3.7–6.9, depth 3.8–303.5 km, dengan magnitude type yang tidak homogen. 

Dengan delapan cluster, rata-rata hanya sekitar 31 event per cluster. Setelah completeness threshold, jumlahnya menjadi 15–49 event.

Namun dari katalog sekecil dan seheterogen itu, penulis ingin memperoleh:

* delapan seismogenic domains;
* empat evolutionary stages;
* progressive localization;
* vertical concentration;
* postseismic redistribution;
* fault segmentation;
* stress-related b-value variation;
* volcanic heterogeneity;
* hazard implications.

Ini adalah rasio klaim terhadap informasi yang tidak sehat.

Lebih buruk lagi:

* tidak ada relocation;
* tidak ada hypocentral uncertainty;
* tidak ada propagation of location error;
* tidak ada katalog magnitude homogen;
* tidak ada detection-completeness history;
* event deep slab dicampur dengan crustal sequence;
* background regional seismicity sengaja tidak dipisahkan.

C8 dengan mean depth 119.2 km mungkin bukan “Stage 1 of an evolving seismogenic system.” Ia mungkin hanya menjadi **deep-earthquake cluster** karena depth memang dimasukkan sebagai fitur.

Algoritma tidak menciptakan resolusi yang tidak ada di katalog. Ia hanya membagi ketidakpastian menjadi beberapa warna.

> **Neural-network terminology tidak dapat menyulap katalog tipis menjadi katalog presisi.**

Untuk studi doktoral, menggunakan katalog kompilasi 248-event yang kasar ketika relocated Lombok catalogs sudah tersedia dan bahkan dikutip merupakan pilihan metodologis yang sulit dibela.

---

# 9. Ukuran compactness-nya secara geometris salah

Penulis menggunakan standard deviation dari radial distance, (SD_R), sebagai descriptor compactness. 

Ini bukan ukuran compactness yang sah secara umum.

Bayangkan seluruh event terletak pada lingkaran sempurna berjari-jari 100 km. Semua event mempunyai radius yang sama, sehingga:

[
SD_R=0.
]

Menurut metric penulis, cluster itu akan disebut “sangat compact,” padahal diameternya 200 km.

Jadi (SD_R) mengukur **keragaman radius**, bukan ukuran spatial footprint.

Masalah ini langsung memukul klaim utama bahwa C4 adalah cluster “most compact.”

Dari Table 1:

* C3: (\bar R=16.5) km, (SD_R=13.2) km, (N=25);
* C4: (\bar R=17.1) km, (SD_R=10.4) km, (N=66). 

Berdasarkan mean radius, C3 justru sedikit lebih kecil.

Bila dihitung radius of gyration sederhana,

[
R_g=\sqrt{\bar R^2+\frac{N-1}{N}SD_R^2},
]

diperoleh kira-kira:

[
R_{g,\mathrm{C3}}\approx21.0\ {\rm km},
]

[
R_{g,\mathrm{C4}}\approx20.0\ {\rm km}.
]

Selisihnya sekitar **1 km**.

Tanpa hypocentral-location uncertainty, selisih satu kilometer tersebut tidak layak menjadi fondasi kalimat “the most compact domain.”

Untuk struktur sesar yang anisotropik, radial metric juga membuang informasi paling penting:

* arah elongation;
* major axis;
* minor axis;
* orientation;
* planarity.

Gunakan:

* covariance ellipse;
* determinant atau eigenvalues spatial covariance;
* radius of gyration;
* convex-hull area;
* kernel-density footprint;
* fault-normal dan fault-parallel spread.

Saat ini, “compactness” lebih merupakan pilihan kata daripada hasil geometris.

---

# 10. Empat tahap merupakan karya editorial, bukan hasil algoritma

Penulis mengelompokkan:

* Stage 1: C8;
* Stage 2: C1 dan C5;
* Stage 3: C2, C3, C4;
* Stage 4: C6 dan C7.

Penulis juga mengakui tahap-tahap tersebut bukan output langsung algoritma dan bukan interval waktu yang tidak tumpang tindih. 

Tidak ada:

* second-level clustering;
* temporal change-point;
* likelihood comparison;
* transition probability;
* state-space model;
* objective grouping rule;
* resampling stability.

Jadi empat stages dibuat oleh author setelah membaca delapan cluster.

> **Ini bukan four-stage reconstruction. Ini PowerPoint taxonomy.**

Label “Stage” juga menimbulkan ilusi urutan proses fisik. Namun C1, C8, dan C4 masing-masing memanjang jauh melampaui tanggal rata-ratanya. Satu event population dapat hadir sebelum, selama, dan sesudah “stages” lain.

Bila stages saling overlap secara masif, lebih jujur menyebutnya:

* descriptive populations;
* statistical components;
* broad event groups.

Bukan stages.

Figures yang memplot (SD_R) dan (SD_Z) terhadap mean cluster date, lalu menghubungkan titik dengan garis, juga menciptakan pseudo-trajectory. 

Cluster means bukan observasi time series. Menghubungkannya dengan garis tidak membuktikan evolusi kontinu. Garis tersebut hanya memandu mata menuju cerita yang sudah dipilih penulis.

---

# 11. “Progressive localization” belum dibedakan dari artefak algoritma

Naskah menyatakan penurunan dispersion C2 → C3 → C4 sebagai progressive localization.

Tetapi:

* space merupakan input;
* time merupakan input;
* depth merupakan input;
* cluster count ditentukan;
* urutan training tetap;
* mean dates digunakan untuk menyusun output;
* metric compactness bermasalah;
* tidak ada null model.

Maka pola tersebut dapat muncul hanya karena algoritma harus membagi:

* regional background;
* mainshock concentration;
* later regional seismicity.

Untuk membuktikan progressive localization, penulis harus menunjukkan bahwa pola tersebut tidak diperoleh dengan:

* simple monthly bins;
* equal-event temporal windows;
* moving-window centroid;
* k-means;
* shuffled event times;
* stationary simulated catalogue;
* ETAS synthetic catalogue.

Tanpa null model, “progressive localization” hanyalah deskripsi bahwa mainshocks dan aftershocks utama lebih berkelompok daripada background seismicity. Itu sudah dapat diketahui dari scatter plot.

Tidak diperlukan neural network untuk menemukan bahwa aftershocks berkumpul di sekitar rupture zone.

---

# 12. C6–C7 belum terbukti sebagai postseismic redistribution

C6 dan C7 disebut mewakili postseismic redistribution dan regional structural readjustment. Namun naskah sendiri mengakui clustering tidak dapat menentukan apakah broadening disebabkan afterslip, viscoelastic relaxation, Coulomb transfer, atau proses lain. 

Lebih mendasar lagi, belum dibuktikan bahwa event-event C6 dan C7 merupakan bagian dari sequence Lombok.

Mereka bisa saja merupakan:

* background regional seismicity;
* independent Sumbawa events;
* slab events;
* event families yang tidak dipicu mainshock;
* artefak panjang observation window.

Tidak ada:

* ETAS triggering probability;
* rate-change test;
* comparison terhadap pre-event background;
* Coulomb modelling;
* decay analysis;
* spatial triggering kernel;
* nearest-neighbour declustering;
* migration speed.

“Terjadi kemudian” bukan sinonim “postseismically redistributed.”

> **Gempa yang datang setelah mainshock tidak otomatis menjadi anak kandung mainshock.**

Istilah yang masih sah adalah:

> later regional seismicity.

---

# 13. Analisis b-value tetap tidak layak menopang interpretasi mekanik

## 13.1 Magnitude scale campuran

Naskah mengakui magnitude type tidak homogen. Namun b-values tetap dibandingkan antarcluster yang secara kuat berkorelasi dengan time dan region. 

Bila magnitude type atau reporting practices berubah menurut waktu atau sumber katalog, apparent b-value variation dapat sepenuhnya nonfisik.

Mengatakan bahwa b-values hanya “comparative and exploratory” tidak menyelesaikan masalah karena relative comparison juga dapat bias.

## 13.2 (M_c) berbeda antarcluster

(M_c) berkisar 4.1–4.4. Cluster kemudian dibandingkan seolah slope-nya berada pada basis observasi yang sama. 

Analisis minimum harus mencakup:

* common (M_c=4.4);
* bootstrap (M_c);
* goodness-of-fit completeness;
* multiple completeness methods;
* sensitivity terhadap magnitude bin;
* homogeneous magnitude subset.

## 13.3 C1 adalah pemindahan gawang yang ditulis transparan

Automatic maximum curvature untuk C1 tidak digunakan karena menyisakan terlalu sedikit event. Penulis kemudian memeriksa ulang FMD secara manual, memilih (M_c=4.2), mempertahankan 16 dari 18 event, dan akhirnya memperoleh b-value yang dapat dimasukkan ke tabel. 

Ini adalah classic researcher degrees of freedom.

> **Metode otomatis memberi hasil yang tidak nyaman, lalu threshold dipindahkan sampai statistik dapat dihitung. Menuliskan bahwa perpindahan itu dilakukan secara manual tidak membuatnya objektif.**

Pilihan yang benar:

* laporkan C1 sebagai **not estimable**;
* atau gunakan formal goodness-of-fit method yang sama untuk semua cluster;
* atau gunakan Bayesian estimation dengan uncertainty penuh.

Tidak boleh memilih threshold karena hasil awal “tidak useful.”

## 13.4 C3 low b dan high mean magnitude bukan dua temuan independen

Estimator yang digunakan adalah:

[
b=\frac{\log_{10}e}
{\bar M-(M_c-\Delta M/2)}.
]

Untuk (M_c) tertentu, b-value secara langsung merupakan fungsi mean magnitude.

Jadi pernyataan:

* C3 mempunyai mean magnitude tertinggi;
* C3 mempunyai b-value terendah;

bukan dua bukti yang saling menguatkan. Keduanya hampir merupakan dua cara mengucapkan statistik yang sama.

> **Naskah menghitung satu fakta dua kali, memberinya dua nama, lalu menggunakannya sebagai dua saksi independen.**

## 13.5 Signifikansi perbedaan tidak meyakinkan

C3 versus C2:

[
\Delta b=0.92-0.58=0.34,
]

dengan combined standard error kira-kira:

[
\sqrt{0.13^2+0.12^2}\approx0.177,
]

atau sekitar 1.9 standard errors.

C3 versus C4:

[
\Delta b=0.39,
]

combined error:

[
\sqrt{0.13^2+0.13^2}\approx0.184,
]

atau sekitar 2.1 standard errors.

Itu belum “pronounced” setelah mempertimbangkan:

* delapan cluster;
* multiple comparisons;
* uncertainty (M_c);
* mixed magnitude scales;
* cluster assignment uncertainty;
* small samples.

Diperlukan Utsu likelihood-ratio tests, bootstrap, permutation tests, dan correction for multiple testing.

---

# 14. Magnitude tidak dimasukkan ke input bukan berarti hasil magnitude “independent”

Penulis berulang kali membanggakan bahwa C3 low b dan high mean magnitude muncul “independently” karena magnitude tidak dipakai untuk clustering. 

Ini terlalu naif.

Gempa besar sequence 2018 terjadi:

* pada tanggal tertentu;
* di area tertentu;
* pada depth tertentu.

Semua variabel tersebut menjadi input.

Maka clustering dapat mengisolasi mainshock population tanpa melihat kolom magnitude secara langsung. Magnitude tetap berkorelasi dengan feature input.

Analisis yang benar adalah permutation test:

1. pertahankan cluster assignment;
2. acak magnitude antarevent;
3. hitung distribusi minimum b dan maximum mean magnitude;
4. evaluasi seberapa ekstrem C3 di bawah null.

Tanpa itu, kata “independently” adalah dekorasi retoris.

---

# 15. Raw event count bukan seismic productivity

C4 disebut “most productive” karena memiliki:

* 66 total events;
* 49 event di atas (M_c).

Tetapi cluster memiliki:

* temporal duration berbeda;
* spatial footprint berbeda;
* (M_c) berbeda;
* detection conditions berbeda;
* regional exposure berbeda.

Jumlah mentah bukan productivity.

Productivity minimal memerlukan:

[
\lambda=
\frac{N(M\ge M_c)}
{\Delta t},
]

dengan common (M_c), dan idealnya dinormalisasi terhadap spatial domain atau triggering model.

Membandingkan 49 event di atas (M_c=4.4) pada C4 dengan 41 event di atas (M_c=4.2) pada C2 juga tidak fair. Threshold C4 lebih tinggi.

Sampai rate dan common completeness dihitung, gunakan:

> largest cluster population,

bukan:

> highest seismic productivity.

Satu adalah fakta algoritmik. Yang lain adalah klaim proses fisik.

---

# 16. Focal mechanism tidak memvalidasi delapan cluster

Dataset focal mechanism terdiri atas 22 event dan merepresentasikan broader sequence, bukan subset formal dari cluster tertentu. Penulis bahkan menyatakan tidak ada formal event-to-cluster matching. 

Maka focal mechanism hanya dapat mendukung kesimpulan umum bahwa:

> gempa-gempa utama Lombok didominasi reverse-to-thrust faulting dalam sistem Flores Back-Arc Thrust.

Hal tersebut sudah diketahui dari literatur yang dikutip.

Focal mechanisms tidak membuktikan bahwa:

* C3 adalah asperity regime;
* C4 adalah distinct shallow domain;
* C2–C4 merupakan sequential activation;
* C6–C7 adalah postseismic adjustment;
* delapan cluster merepresentasikan delapan seismogenic domains.

Tidak tersedia:

* mechanism count per cluster;
* Kagan angle within cluster;
* stress tensor inversion;
* nodal-plane consistency;
* uncertainty;
* event matching.

Menyebut 22 mekanisme tersebut “independent mechanical constraints” terhadap four-stage model terlalu murah hati. Mereka adalah **regional tectonic context**, bukan validation.

---

# 17. Rinjani masih menjadi ornamen interpretatif

Penulis menyebut lithology, rigidity, thermal structure, fractures, dan fluids di sekitar Rinjani sebagai faktor yang mungkin memodulasi seismogenic volume, sambil mengakui bahwa hasil tidak membuktikan magmatic triggering. 

Pengakuan terakhir tepat. Namun tidak ada variabel dalam analisis yang mengukur:

* temperature;
* attenuation;
* velocity anomaly;
* fluids;
* deformation volcano;
* magma;
* fracture density;
* distance to volcanic edifice;
* volcanic versus tectonic event type.

Dengan demikian, Rinjani bukan hasil penelitian ini. Ia merupakan plausible explanation yang diambil dari literatur.

Kalimat yang masih sah:

> The cluster distribution is spatially compatible with previously reported crustal heterogeneity near Rinjani.

Kalimat yang tidak sah:

> Rinjani heterogeneity explains or controls C3–C4 localisation.

Naskah belum melakukan pengujian yang dapat membedakan penjelasan Rinjani dari fault segmentation biasa.

---

# 18. Kebaruannya terlalu tipis untuk paper doktoral

Apa temuan baru yang tidak sudah diketahui?

* sequence terkait Flores Back-Arc Thrust;
* main events dominan thrust;
* rupture segmented;
* mainshock/aftershock activity spatially concentrated;
* deep regional events berbeda dari shallow sequence;
* later regional activity lebih menyebar;
* Rinjani mungkin memengaruhi crustal heterogeneity.

Sebagian besar sudah terdapat dalam studi Salman, Supendi, Lythgoe, Afif, Sasmi, dan Zhao yang dikutip penulis sendiri.

Apa kontribusi algoritmiknya?

* bukan conventional SOM;
* tidak ada topology preservation;
* (K) arbitrer;
* tidak ada stability test;
* tidak ada comparison dengan baseline;
* tidak ada independent application.

Maka novelty saat ini dapat diringkas menjadi:

> sebuah algoritma nearest-prototype yang disetel untuk menghasilkan delapan kelompok diterapkan pada katalog kasar Lombok dan diberi interpretasi tektonik yang sudah dikenal.

Itu tidak cukup.

---

# 19. Introduction membuang ruang pada kerusakan yang tidak pernah dianalisis

Introduction membahas casualty, damaged houses, displacement, volcaniclastic deposits, site response, dan memasukkan foto kerusakan. 

Namun tidak ada analisis terhadap:

* intensity;
* ground motion;
* site amplification;
* vulnerability;
* damage distribution;
* pumice deposits.

Foto kerusakan pada Figure 1 hanyalah dekorasi emosional.

Paper ini tentang clustering katalog gempa. Entah:

* lakukan analisis hubungan cluster–shaking–damage;
* atau hapus pembahasan dan panel kerusakan.

Saat ini, pendahuluan menggunakan tragedi manusia sebagai panggung visual bagi metode yang sama sekali tidak menjawab persoalan kerusakan.

---

# 20. Reproducibility-nya tidak memenuhi standar paper “data-driven”

Processed dataset hanya tersedia “upon reasonable request.” 

Untuk metode custom dan sangat sensitif terhadap:

* urutan event;
* scaling;
* initialization;
* learning rate;
* exact catalogue;
* manual (M_c);
* grouping empat tahap;

ini tidak dapat diterima.

Wajib dilepas terbuka:

* exact source catalogue;
* query parameters;
* event ordering;
* normalized input table;
* initial prototypes;
* final prototypes;
* event-to-cluster labels;
* MATLAB code;
* all parameters;
* FMD scripts;
* focal-mechanism matching table;
* figures;
* environment/version;
* persistent DOI.

“Available upon reasonable request” dalam paper reproducibility berarti:

> tersedia sampai mahasiswa lulus, laptop rusak, dan email tidak lagi dijawab.

---

# Bagian yang layak diapresiasi

Ada beberapa perbaikan nyata.

Pertama, manuscript sekarang secara eksplisit mengakui bahwa metode bukan SOM konvensional. Itu lebih baik daripada mempertahankan klaim topological SOM yang tidak benar. 

Kedua, penambahan minimum, median, mean, dan maximum dates merupakan langkah baik. Ini memungkinkan pembaca melihat temporal overlap yang sebelumnya disembunyikan oleh mean date tunggal. 

Ketiga, penulis tidak lagi menyebut b-value sebagai direct stress measurement atau deterministic precursor.

Keempat, penulis tidak memaksakan klaim magmatic triggering.

Kelima, limitation section cukup jujur mengenai fixed (K), event order, magnitude heterogeneity, manual (M_c), temporal overlap, dan keterbatasan focal mechanisms. 

Namun ini perlu dipahami:

> **Kejujuran mengenai cacat desain patut diapresiasi. Cacat desainnya sendiri tetap fatal.**

Kesadaran metodologis bukan pengganti eksperimen metodologis.

---

# Analisis yang wajib dilakukan sebelum resubmission

## 1. Ganti atau perbaiki algoritma

Pilih salah satu:

* implementasikan true SOM dengan neighbourhood function, lattice, radius decay, U-matrix, quantization error, dan topographic error; atau
* jujur menyebut metode competitive vector quantization dan berhenti menjual topology-preserving SOM.

## 2. Uji jumlah cluster

Uji setidaknya:

[
K=2,\ldots,15.
]

Laporkan:

* silhouette;
* Davies–Bouldin;
* Calinski–Harabasz;
* gap statistic;
* bootstrap stability;
* adjusted Rand index;
* persistence C3–C4.

## 3. Putuskan hubungan time dengan tujuan penelitian

Bila temporal evolution adalah hasil utama, keluarkan time dari input.

Cluster space–depth terlebih dahulu, kemudian uji temporal organisation secara independen.

## 4. Uji sensitivitas training

* 100–500 shuffled event orders;
* multiple initialisations;
* several learning-rate schedules;
* batch versus online update;
* assignment confidence;
* convergence history.

## 5. Uji metric

Bandingkan:

* min–max;
* z-score;
* robust scaler;
* Mahalanobis distance;
* alternative feature weights;
* no-deep-event catalogue;
* crustal-only catalogue.

## 6. Gunakan katalog lebih baik

Gunakan:

* relocated local catalogue;
* homogeneous magnitude;
* location uncertainties;
* documented completeness;
* substantially more events.

## 7. Gunakan baseline methods

Minimal:

* k-means;
* Gaussian mixture;
* hierarchical clustering;
* HDBSCAN;
* ST-DBSCAN;
* simple temporal bins.

Bila simple time bins menghasilkan cerita yang sama, SOM branding tidak memberi nilai tambah.

## 8. Perbaiki compactness

Gunakan:

* covariance ellipses;
* radius of gyration;
* major/minor axes;
* spatial area;
* fault-normal and fault-parallel spread;
* uncertainty propagation.

## 9. Ulangi Gutenberg–Richter

* homogenize magnitude;
* common-(M_c) test;
* goodness-of-fit (M_c);
* bootstrap (M_c) dan (b);
* Utsu test;
* permutation test;
* multiple-comparison correction;
* remove-mainshock sensitivity.

C1 sebaiknya dilaporkan **not estimable** sampai formal completeness criterion menyatakan sebaliknya.

## 10. Uji postseismic triggering

Gunakan:

* ETAS;
* nearest-neighbour triggering;
* rate-change analysis;
* Coulomb stress;
* background comparison.

Tanpa itu, C6–C7 jangan disebut postseismic redistribution.

## 11. Match focal mechanisms ke cluster

Laporkan:

* jumlah mechanism per cluster;
* matching criterion;
* Kagan angles;
* mechanism heterogeneity;
* stress inversion bila memungkinkan.

## 12. Buka data dan kode

Tanpa open catalogue dan code release, jangan gunakan frasa *reproducible data-driven framework*.

---

# Pertanyaan ujian untuk mahasiswa S3

1. **Secara matematis, unsur apa yang membuat algoritma Anda masih layak disebut Self-Organizing Map setelah neighbourhood update dihapus?**

2. **Mengapa jumlah neuron delapan? Tunjukkan bahwa C3–C4 tetap ada pada (K=6,7,9,) dan 10.**

3. **Berapa adjusted Rand index setelah event order diacak 100 kali?**

4. **Mengapa menggunakan 100 epoch ketika learning rate setelah 20 epoch sekitar (10^{-8})?**

5. **Apa makna fisik menyetarakan seluruh rentang waktu katalog dengan seluruh rentang kedalaman?**

6. **Berapa hari yang setara dengan 10 km dalam metric Anda?**

7. **Mengapa horizontal position memperoleh dua dimensi sedangkan time hanya satu?**

8. **Mengapa output yang dibentuk menggunakan time dapat dianggap independent evidence untuk temporal evolution?**

9. **Apa nilai (SD_R) bagi sekumpulan event pada lingkaran berjari-jari 100 km? Apakah cluster tersebut compact?**

10. **Mengapa C4 disebut paling compact ketika mean radius C3 lebih kecil?**

11. **Apa bukti C6–C7 dipicu sequence Lombok dan bukan background regional events?**

12. **Mengapa C1 (M_c) diubah ketika hasil otomatis tidak menyisakan cukup event?**

13. **Apakah perbedaan b-value C3–C2 dan C3–C4 signifikan menurut Utsu test?**

14. **Mengapa high mean magnitude dan low b-value dianggap dua bukti, padahal estimator b merupakan fungsi langsung mean magnitude?**

15. **Berapa b-value seluruh cluster bila common (M_c=4.4) digunakan?**

16. **Berapa focal mechanisms yang benar-benar masuk C3 dan C4?**

17. **Apa temuan baru paper ini yang tidak sudah diketahui dari relocated seismicity dan source models Lombok terdahulu?**

18. **Bila k-means biasa menghasilkan cluster yang sama, apa kontribusi SOM Anda?**

19. **Bila simple monthly bins menghasilkan progressive localization yang sama, apa kontribusi machine learning?**

20. **Mengapa data dan kode belum terbuka bila reproducibility disebut sebagai kekuatan?**

Bila jawaban mahasiswa terus berputar pada kata:

* *framework*;
* *data-driven*;
* *consistent with*;
* *exploratory*;
* *future studies*;

tanpa angka dan eksperimen baru, maka ia belum menguasai metodologinya.

---

# Komentar singkat kepada editor

> **Recommendation: Reject.** The manuscript applies a deterministic winner-take-all vector-quantization procedure but continues to present it as a simplified Self-Organizing Map, despite omitting the neighbourhood learning that defines topology-preserving SOMs. The number of clusters is fixed a priori at eight, event order is not shuffled, the learning rate effectively vanishes after only a few epochs, and no cluster-number, order, initialization, scaling, or bootstrap stability analysis is performed. Time is used as a clustering input and then reused to infer temporal evolution, while space and depth are similarly reused as purported post-hoc validation. The four-stage model is an author-defined interpretive grouping rather than an algorithmic or statistically identified result. The catalogue contains only 248 events with non-homogeneous magnitude types and no propagated location uncertainty. Cluster-specific b-values rely on small samples, variable completeness thresholds, and a manually reassessed threshold for C1. Focal mechanisms are not formally matched to clusters and therefore cannot validate the proposed domains. These are structural methodological failures requiring a complete reanalysis rather than textual revision.

# Putusan akhir

## **REJECT**

Versi baru ini lebih hati-hati dalam bahasa, tetapi belum lebih kuat dalam sains. Bahkan, dengan mengakui seluruh keputusan arbitrer secara terbuka, naskah kini semakin jelas menunjukkan bahwa kesimpulan utamanya tidak teridentifikasi oleh data.

Penulis belum menemukan:

* delapan domain yang stabil;
* empat tahap yang objektif;
* migrasi atau localization yang bebas dari circularity;
* b-value contrast yang signifikan;
* postseismic redistribution;
* hubungan mekanik cluster–fault;
* pengaruh Rinjani.

Yang telah dilakukan adalah:

> **membagi katalog 248-event menjadi delapan kelompok menggunakan delapan prototype yang dipilih sebelumnya, kemudian menulis cerita tektonik yang masuk akal di sekitar hasil pembagian tersebut.**

Cerita yang masuk akal bukan otomatis bukti ilmiah.

Pada level doktoral, naskah ini belum menunjukkan bahwa mahasiswa memahami perbedaan antara:

* clustering dan classification by imposed prototypes;
* reproducibility dan stability;
* post-hoc description dan independent validation;
* temporal input dan temporal discovery;
* statistical association dan physical mechanism;
* caveat dan correction.

Manuskrip ini masih dapat diselamatkan, tetapi hanya melalui **rekonstruksi metodologi dari dasar**. Memperhalus kalimat, menambah disclaimer, atau mengganti “demonstrates” menjadi “suggests” tidak akan menolong. Saat ini, kelemahannya bukan pada nada klaim. Kelemahannya berada pada mesin yang menghasilkan klaim tersebut.
