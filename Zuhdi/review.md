# Laporan Review Senior Geophysicist — Gravity dan Magnetik

Naskah yang dinilai adalah **“Centered Horizontal Gradient (CHG): An Improved Operator for Interpreting Circular Gravity Anomalies”** oleh Muhammad Zuhdi, Wiwit Suryanto, dan Sudarmaji. 

## Rekomendasi: **REJECT IN PRESENT FORM — REBUILD THE PAPER FROM ITS MATHEMATICAL FOUNDATION**

Ini bukan kasus *minor revision*. Bahkan istilah *major revision* terlalu ramah. Versi yang dapat dipublikasikan nantinya harus:

* menurunkan ulang makna fisik operator;
* membatasi klaim kebaruan;
* mengaudit satuan dan kode;
* merancang ulang seluruh validasi sintetis;
* mengolah ulang data lapangan;
* dan membuang sebagian besar interpretasi geologis yang saat ini tidak ditopang resolusi data.

Masalah paling mendasarnya sederhana:

> **CHG bukan operator gravitasi baru dalam arti informasi fisik baru. CHG hanyalah vektor gradien horizontal yang ditulis kembali dalam basis radial–tangensial terhadap satu pusat yang dipilih.**

Hal itu dapat berguna sebagai **diagnostik orientasi relatif terhadap pusat**, tetapi tidak otomatis menjadi metode edge detection yang lebih baik. Bahkan tabel hasil penulis sendiri menunjukkan bahwa CHG kalah dari beberapa metode pembanding. Judul mengatakan *improved operator*; angka-angka di dalam naskah mengatakan sebaliknya.

| Aspek                                      |  Penilaian |
| ------------------------------------------ | ---------: |
| Relevansi masalah interpretasi melingkar   |        4/5 |
| Kesederhanaan dan interpretabilitas konsep |        4/5 |
| Kebaruan matematis yang terbukti           |        1/5 |
| Ketepatan interpretasi gradien             |        1/5 |
| Desain model sintetis                      |      1.5/5 |
| Konsistensi satuan                         |      0.5/5 |
| Validasi kuantitatif                       |        1/5 |
| Pengolahan data lapangan                   |      0.5/5 |
| Kekuatan interpretasi geologi              |      0.5/5 |
| Aplikasi magnetik                          |      0.5/5 |
| Kematangan naskah doktoral                 |        1/5 |
| **Putusan**                                | **Reject** |

---

# Hal-hal positif yang layak dipertahankan

Sebelum pisau diasah lebih dalam, beberapa unsur memang bernilai.

Pertama, gagasan memproyeksikan gradien horizontal ke arah radial dan tangensial relatif terhadap suatu pusat bersifat sederhana, intuitif, dan mudah diterapkan. Untuk struktur yang pusatnya telah diketahui secara independen—misalnya kaldera, dome, diapir, pipe, crater, atau intrusive complex—dekomposisi tersebut dapat membantu membedakan pola gradien yang terorganisasi secara radial dari pola azimutal.

Kedua, penulis tidak hanya menampilkan contoh yang disukai. Mereka memasukkan model nonmelingkar dan mengakui bahwa THG lebih baik untuk struktur tersebut.  Ini merupakan naluri ilmiah yang baik, walaupun pengujian negatif tersebut belum cukup.

Ketiga, manuscript mencoba menyediakan:

* optimasi pusat;
* model dengan noise;
* pengujian kedalaman;
* pembandingan dengan beberapa operator lain;
* metrik edge detection;
* data lapangan Samalas dan Tambora;
* serta kode terbuka.

Upaya tersebut luas. Masalahnya bukan kurang bekerja. Masalahnya adalah terlalu banyak analisis dilakukan di atas definisi fisik, satuan, dan desain validasi yang belum dikunci.

Keempat, identitas matematis

[
\mathrm{THG}^2=\mathrm{CHG}*{\mathrm{rad}}^2+\mathrm{CHG}*{\mathrm{tan}}^2
]

dituliskan dengan benar.  Sayangnya, manuscript belum memahami sepenuhnya konsekuensi identitas ini terhadap klaim kebaruan dan “energy response.”

Kelima, kode dan contoh data disebut tersedia secara terbuka. Ini patut diapresiasi, tetapi repository aktif tanpa versi terarsip, commit hash, environment, dan DOI belum merupakan reproduksi ilmiah yang beku. 

---

# A. Kelemahan konseptual yang paling fatal

## 1. CHG adalah rotasi basis, bukan penciptaan operator fisik baru

Untuk pusat ((x_c,y_c)), definisikan

[
r=\sqrt{(x-x_c)^2+(y-y_c)^2},
]

[
\mathbf e_r=
\begin{bmatrix}
\cos\theta\
\sin\theta
\end{bmatrix},
\qquad
\mathbf e_\theta=
\begin{bmatrix}
-\sin\theta\
\cos\theta
\end{bmatrix}.
]

Gradien horizontalnya adalah

[
\nabla_h g=
\begin{bmatrix}
g_x\
g_y
\end{bmatrix}.
]

Maka CHG yang ditawarkan penulis hanyalah

[
\begin{bmatrix}
G_r\
G_\theta
\end{bmatrix}
=============

\begin{bmatrix}
\cos\theta & \sin\theta\
-\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix}
g_x\
g_y
\end{bmatrix}.
]

Matriks tersebut ortogonal. Karena itu,

[
G_r^2+G_\theta^2=g_x^2+g_y^2=\mathrm{THG}^2.
]

Manuskrip justru menyatakan bahwa transformasi ortogonal tersebut “confirms that CHG is a new mathematical formulation, not just a variation of THG.” 

Tidak. Kesimpulan matematisnya justru berkebalikan.

> **Transformasi ortogonal membuktikan bahwa informasi yang sama sedang ditulis dalam basis berbeda. Komputer tidak menemukan medan baru; komputer hanya memutar sumbu koordinat.**

CHG tidak menambah informasi terhadap pasangan ((g_x,g_y)). Ia hanya:

* mempertahankan tanda;
* mengubah basis dari Cartesian menjadi polar;
* menambahkan prior geometris berupa pusat;
* dan membuat orientasi relatif terhadap pusat lebih mudah dibaca.

Itu dapat menjadi kontribusi visualisasi atau parameterisasi. Namun menyebutnya “new operator” atau “significant advancement in gravity-gradient analysis” terlalu berlebihan. Klaim terakhir bahkan muncul kembali di Conclusions. 

### Reposisi yang lebih jujur

Judul yang jauh lebih defensible adalah:

> **Center-Referenced Radial–Tangential Decomposition of the Horizontal Gravity Gradient**

atau:

> **Polar Decomposition of Horizontal Gravity Gradients for Radially Organized Anomalies**

Hapus kata **Improved** sampai ada bukti kuantitatif bahwa hasilnya memang lebih baik.

---

## 2. Bahkan komponen radialnya bukan baru

Pemeriksaan literatur menemukan paper Muhammad Zuhdi tahun 2018 yang telah mendefinisikan *radial derivative* sebagai

[
dT=d_x\cos\theta+d_y\sin\theta,
]

dengan pusat ditentukan dari pusat anomali. Itu secara substansial sama dengan CHGrad saat ini. 

Paper tersebut tidak muncul dalam daftar pustaka naskah ini.

Ini masalah serius bagi klaim novelty. Bukan karena penulis dilarang mengembangkan karyanya sendiri, tetapi karena manuscript wajib menjelaskan dengan terang:

* apa yang telah dipublikasikan sebelumnya;
* bagian apa yang identik;
* bagian apa yang benar-benar baru;
* apakah novelty sekarang hanya CHGtan;
* apakah novelty-nya center optimization;
* atau apakah novelty-nya hybrid visualization.

> **Menyebut CHGrad sebagai metode baru sambil tidak menyitir paper sendiri yang telah menuliskan formula yang sama akan membuat reviewer bertanya apakah penulis lupa terhadap karyanya sendiri atau berharap reviewer juga lupa.**

Saya tidak menyimpulkan adanya duplikasi teks tanpa pemeriksaan terpisah. Namun sebagai masalah *prior art* dan integritas klaim novelty, ini harus diperbaiki sebelum submission.

---

## 3. Manuskrip mencampuradukkan orientasi fitur dengan arah normal gradien

Dalam koordinat polar,

[
\nabla g=
\mathbf e_r\frac{\partial g}{\partial r}
+
\mathbf e_\theta\frac{1}{r}\frac{\partial g}{\partial\theta}.
]

Jadi:

[
\mathrm{CHG}_{\mathrm{rad}}
===========================

\frac{\partial g}{\partial r},
]

[
\mathrm{CHG}_{\mathrm{tan}}
===========================

\frac{1}{r}\frac{\partial g}{\partial\theta}.
]

Untuk anomali yang benar-benar radial-simetris,

[
g=g(r),
]

sehingga

[
\frac{\partial g}{\partial\theta}=0
]

dan dengan demikian

[
\mathrm{CHG}_{\mathrm{tan}}=0.
]

Ini mempunyai konsekuensi geometris yang tidak boleh salah pada level doktoral:

* batas kaldera yang melingkar mempunyai arah **tangen** sepanjang kelilingnya;
* tetapi arah normal batas tersebut adalah **radial**;
* gradien selalu menunjuk terutama ke arah normal;
* maka batas lingkaran ideal diperkuat oleh **CHGrad**, bukan CHGtan.

Sebaliknya:

* sebuah lineament yang memancar radial dari pusat mempunyai arah radial;
* normal terhadap lineament itu lebih tangensial;
* maka lineament radial dapat muncul kuat pada CHGtan.

Abstract menyatakan bahwa CHGtan menekankan “tangential features such as caldera boundaries.”  Pernyataan ini tidak presisi dan secara geometris menyesatkan.

Figure 2 sebenarnya sudah memperlihatkan kenyataan yang benar:

* struktur melingkar lebih jelas pada komponen radial;
* struktur berbentuk spokes atau garis radial lebih menonjol pada komponen tangensial.

Namun prosa manuscript belum membedakan:

1. arah memanjang fitur;
2. arah normal batas;
3. arah komponen gradien.

> **Bila mahasiswa doktoral belum membedakan orientasi sebuah garis dari orientasi normalnya, interpretasi peta gradien apa pun menjadi rapuh sejak kalimat pertama.**

Gunakan terminologi berikut:

* **CHGrad enhances boundaries whose normal is radial**, termasuk batas sirkular atau tangensial;
* **CHGtan enhances boundaries whose normal is tangential**, termasuk lineament radial atau spoke-like features.

---

## 4. Kritik terhadap THG dibangun sebagai straw man

Manuskrip mengatakan THG kurang efektif untuk circular anomalies karena memakai “non-centered finite-difference operator.” 

Ini salah secara konseptual.

THG adalah

[
\mathrm{THG}
============

\sqrt{g_x^2+g_y^2}.
]

Ia:

* rotationally invariant;
* tidak bergantung pada arah sumbu;
* tidak membutuhkan pusat;
* dan mendeteksi gradien kuat pada batas dalam orientasi apa pun.

THG memang kehilangan:

* tanda;
* arah gradien;
* informasi apakah gradien sejajar radial atau tangensial terhadap suatu pusat tertentu.

Tetapi THG tidak kehilangan kemampuan mendeteksi batas melingkar. Bahkan untuk anomali radial sempurna:

[
\mathrm{THG}=|\mathrm{CHGrad}|.
]

Jadi CHG bukan memperbaiki ketidakmampuan THG mendeteksi circular edge. CHG hanya memberi **orientational attribution relative to a prescribed center**.

Itu perbedaan yang sangat penting:

> **THG adalah edge detector. CHG adalah dekomposisi orientasi dengan prior pusat.**

Manuskrip sekarang menjual yang kedua sebagai versi yang lebih baik dari yang pertama. Itu kategori yang salah.

---

## 5. “Energy response” hanyalah identitas Pythagoras yang dibuat terdengar geofisika

Penulis menghitung

[
P_r
===

\frac{\sum G_r^2}
{\sum \mathrm{THG}^2}\times100%,
]

dan

[
P_\theta
========

\frac{\sum G_\theta^2}
{\sum \mathrm{THG}^2}\times100%.
]

Karena

[
G_r^2+G_\theta^2=\mathrm{THG}^2
]

pada setiap titik, maka secara otomatis

[
P_r+P_\theta=100%.
]

Itulah sebabnya hasilnya selalu seperti:

* 55.3% + 44.7%;
* 42.1% + 57.9%;
* 51.2% + 48.8%.



Ini bukan validasi metode. Ini konsekuensi aljabar yang harus terjadi.

> **Komputer di sini belum menemukan dominasi energi geologi; komputer baru saja membuktikan teorema Pythagoras berkali-kali.**

Selain itu, istilah **energy** terlalu fisikal. Ini bukan gravitational energy. Istilah yang lebih aman adalah:

> normalized squared-gradient partition.

Bahkan fraksi tersebut belum tentu menunjukkan geometri sumber karena dipengaruhi oleh:

* lokasi pusat;
* regional trend;
* noise;
* edge effects;
* area domain;
* dan distribusi amplitudo.

Model 3 memperoleh pembagian 51.2%–48.8%. Itu bukan bukti Model 3 “dominated by radial component.” Nilai dekat 50–50 justru menunjukkan tidak ada organisasi orientasi yang kuat relatif terhadap pusat tersebut.

---

## 6. CHG linear hanya jika pusatnya telah ditetapkan

Manuskrip menyatakan CHGrad dan CHGtan merupakan linear operators dan memenuhi superposition. 

Itu hanya benar untuk pusat ((x_c,y_c)) yang tetap.

Untuk pusat tetap:

[
\mathcal L_{c}(g_1+g_2)
=======================

\mathcal L_{c}(g_1)+\mathcal L_{c}(g_2).
]

Namun pipeline manuscript menentukan pusat dari data:

[
c^*(g)
======

\arg\min_c J(c;g),
]

lalu menghitung

[
\mathrm{CHG}(g)
===============

\mathcal L_{c^*(g)}g.
]

Secara umum,

[
c^*(g_1+g_2)
\neq
c^*(g_1)
\neq
c^*(g_2).
]

Jadi keseluruhan pipeline **center optimization + CHG** bukan operator linear.

Hybrid normalization dengan membagi terhadap nilai maksimum juga nonlinear.

Jangan mengklaim superposition untuk keseluruhan metode. Batasi:

> For a fixed, externally specified center, the radial and tangential projections are linear functions of the input gravity field.

---

## 7. Operator tidak terdefinisi tepat di pusat

Pada

[
r=0,
]

nilai

[
\cos\theta=\frac{x-x_c}{r},
\qquad
\sin\theta=\frac{y-y_c}{r}
]

tidak terdefinisi.

Naskah tidak menjelaskan:

* apakah center pixel diberi NaN;
* diinterpolasi;
* diset nol;
* dipindahkan setengah grid;
* atau dikeluarkan dari analisis.

Peta Samalas dan Tambora memperlihatkan pusat yang sangat kuat atau berlubang. Tanpa aturan eksplisit, pembaca tidak tahu apakah itu:

* respons geologi;
* nilai anomali asli;
* singularity handling;
* clipping;
* atau artefak plotting.

Hal seperti ini tidak boleh diserahkan kepada tebakan pembaca.

---

# B. Center optimization belum layak disebut geophysical center estimation

## 8. Weighted centroid dengan nilai gravitasi bertanda dapat gagal secara elementer

Estimasi awal menggunakan gravity amplitude sebagai bobot. 

Bila formulanya menggunakan (g_i), maka untuk data yang mempunyai anomali positif dan negatif:

[
x_{c0}
======

\frac{\sum_i x_i g_i}{\sum_i g_i}
]

dapat menjadi:

* tidak stabil ketika (\sum g_i\approx0);
* terletak di luar area data;
* bergeser drastis akibat regional trend;
* bergantung pada datum atau constant offset;
* berlawanan arah untuk density contrast negatif.

Gravity anomaly bukan probability density. Ia tidak berhak diperlakukan sebagai positive mass weight tanpa penjelasan.

Alternatif seperti (|g|), (g^2), atau gradient energy juga mempunyai bias tersendiri. Karena itu, penulis harus:

* mendefinisikan tepat bobot;
* menunjukkan invariance terhadap constant offset dan sign reversal;
* menguji positive dan negative density contrast;
* serta melakukan sensitivity analysis.

---

## 9. Radial-variance minimum bukan otomatis pusat geologi

Objective center dibuat dengan mengelompokkan nilai gravitasi ke dalam radial bins dan meminimalkan variance di dalam setiap ring. 

Secara konseptual, ini dapat menemukan pusat radial symmetry. Namun banyak pertanyaan penting tidak dijawab:

* Bagaimana (dr) dipilih?
* Apakah ring dengan lima titik diberi bobot sama dengan ring berisi ribuan titik?
* Apa yang dilakukan terhadap empty bins?
* Bagaimana partial rings di tepi domain ditangani?
* Apakah variance dinormalisasi terhadap radial signal amplitude?
* Bagaimana regional trend dihilangkan?
* Apakah objective memiliki banyak local minima?
* Bagaimana confidence region pusat dihitung?
* Bagaimana nilai objective dibandingkan dengan null model noncircular?
* Kapan algoritma menyatakan “tidak ada pusat bermakna”?

Tanpa *null test*, algoritma akan selalu mengembalikan suatu pusat.

Model 3 yang tidak melingkar pun menghasilkan “optimized center” yang disebut cukup stabil. 

Itu bukan kekuatan metode. Itu peringatan.

> **Algoritma yang selalu menemukan pusat, bahkan ketika objeknya tidak mempunyai pusat, bukan detektor pusat. Ia hanya mesin penghasil koordinat.**

Diperlukan **circularity significance score**. Bila symmetry score tidak berbeda dari phase-randomized, translated, atau noncircular null models, pusat harus ditolak sebagai tidak bermakna.

---

## 10. Pengujian pusat sintetis terlalu mudah

Model 1 dan Model 2:

* dibangun simetris;
* ditempatkan dekat pusat grid;
* pusat sebenarnya sudah diketahui;
* local search mencakup pusat sebenarnya;
* dan weighted centroid awal sudah sangat dekat.

Lalu optimizer mencapai error 0%.

Itu hampir tidak memberi informasi.

> **Menyembunyikan koin di tengah meja, mencari di sekitar tengah meja, lalu menemukan koin bukan demonstrasi algoritma pencarian yang mengesankan.**

Pengujian yang benar harus mencakup:

* true center acak;
* true center di antara grid nodes;
* pusat dekat boundary;
* multiple circular bodies;
* ellipse;
* partial ring;
* azimuthally variable density;
* overlapping linear regional anomaly;
* noise levels berbeda;
* missing data;
* irregular survey boundaries.

Laporkan distribusi center error dari ratusan realization, bukan satu angka yang kebetulan nol.

---

## 11. Center optimization field data tidak konsisten dengan klaim paper

Abstract menjual automatic center optimization sebagai kontribusi utama. 

Namun pada aplikasi:

* pusat Samalas dipilih di pusat Lake Segara Anak;
* pusat Tambora dipilih di tengah crater.

 

Itu merupakan **geologically prescribed center**, bukan blind optimized center.

Discussion mengatakan optimization field data dibatasi pada wilayah sekitar Samalas, tetapi tabel pusat yang diberikan hanya memuat Models 1–3 dan tidak menunjukkan:

* pusat awal Samalas;
* pusat optimum Samalas;
* objective score;
* confidence interval;
* perbedaan terhadap crater center;
* hasil Tambora.



Jadi center optimization belum benar-benar divalidasi pada data lapangan.

Penulis harus memilih salah satu positioning:

1. **center known independently**, lalu CHG hanya melakukan decomposition; atau
2. **center inferred from gravity**, lalu hasil pusat, uncertainty, dan external validation harus ditampilkan.

Saat ini manuscript ingin menikmati keduanya sekaligus.

---

## 12. Komputasinya tidak layak disebut efisien

Untuk satu juta grid points, center optimization membutuhkan 5.767 s, sekitar 96 menit. 

Tidak dijelaskan:

* hardware;
* jumlah candidate centers;
* ukuran search region;
* jumlah radial bins;
* implementasi loop;
* vectorization;
* parallelization;
* kompleksitas algoritma.

Kalimat “regrid to decrease matrix size” bukan solusi ilmiah bila regridding mengubah objective dan menghapus informasi.

Gunakan:

* coarse-to-fine search;
* image pyramid;
* vectorized polar binning;
* precomputed radial-index matrices;
* FFT or correlation methods;
* GPU;
* local optimizer setelah coarse scan.

Namun efisiensi komputasi adalah masalah sekunder. Yang lebih penting: objective-nya harus benar terlebih dahulu. Mempercepat objective yang bias hanya menghasilkan jawaban salah dengan lebih cepat.

---

# C. Model sintetis dan validasi kuantitatif gagal meyakinkan

## 13. Model sintetis dirancang agar operator berhasil

Model 1 dan Model 2 memuat pola:

* lingkaran;
* ellipse;
* radial spokes;
* pola yang berpusat hampir sempurna pada pusat CHG.



Ini merupakan *demonstration model*, bukan stress test.

Tidak ada:

* circular body sederhana dengan analytical response;
* partial caldera;
* eccentric ring;
* dipping contact;
* azimuthally heterogeneous density;
* multiple overlapping sources;
* regional gradient;
* topographic residual;
* irregular sampling;
* missing data;
* correlated noise;
* center uncertainty.

Model seperti roda sepeda memang akan terlihat seperti roda sepeda ketika dianalisis dengan koordinat polar yang pusatnya ditempatkan pada hub roda. Itu belum membuktikan operator berguna pada geologi nyata.

---

## 14. Hanya satu realisasi noise

Noise ditambahkan sebesar 5% standard deviation. 

Tidak ada:

* jumlah realization;
* random seed;
* variasi level noise;
* coloured noise;
* survey-line artefacts;
* regional trend;
* grid interpolation noise;
* uncertainty interval.

Satu realisasi noise hanya menghasilkan satu gambar. Ia tidak menghasilkan robustness.

Lakukan minimal 100–500 realizations untuk noise:

[
0,\ 1,\ 2,\ 5,\ 10,\ 20%.
]

Laporkan:

* center error;
* F1;
* precision–recall;
* orientation recovery;
* component-energy fraction;
* confidence intervals.

---

## 15. Metrik edge detection justru membantah judul

Table edge detection melaporkan kira-kira:

* EHD: (F1=0.252), (IoU=0.201);
* CHGrad: (F1=0.046), (IoU=0.024);
* CHGtan: (F1=0.062), (IoU=0.035).



Penulis sendiri menyimpulkan EHD memberi kompromi terbaik, sedangkan CHGrad termasuk metode dengan positional error terbesar. 

Dengan kata lain:

> **Metode yang disebut “Improved Operator” memperoleh F1 sekitar 0.05 dan dikalahkan oleh metode pembanding menurut tabelnya sendiri. Judulnya tidak sekadar optimistis; judulnya dibantah oleh hasil penelitian.**

Ada dua kemungkinan:

1. CHG memang buruk sebagai edge detector; atau
2. pipeline evaluasi edge detection salah.

Keduanya mengharuskan perombakan.

---

## 16. Semua F1 dan IoU terlalu rendah untuk mendukung klaim keberhasilan

Bahkan EHD, metode terbaik, hanya mempunyai F1 sekitar 0.25. THG hanya sekitar 0.018.

Ini menunjukkan salah satu atau beberapa masalah:

* threshold edge tidak tepat;
* ground truth terlalu tipis;
* matching hanya exact-pixel;
* tolerance tidak diberikan;
* morphology/dilation tidak distandarkan;
* operator berbeda dinilai dengan threshold yang tidak fair;
* units/resolution keliru;
* edge mask salah.

Naskah tidak menjelaskan bagaimana continuous response map diubah menjadi detected-edge pixels:

* threshold absolut atau persentil?
* threshold sama untuk semua metode?
* nonmaximum suppression?
* hysteresis?
* connected-component filtering?
* edge tolerance?
* sign handling?
* positive and negative lobes digabung atau dipisah?

Tanpa prosedur itu, Precision, Recall, F1, dan IoU tidak dapat direproduksi.

Gunakan:

* precision–recall curves;
* optimal threshold dari validation subset;
* Pratt’s figure of merit;
* symmetric Chamfer distance;
* Hausdorff distance;
* tolerance dalam satuan grid resolution;
* topology-aware edge metrics.

---

## 17. THG dan “Direct Derivative” menghasilkan angka identik

Dalam tabel:

* jumlah detected edge sama;
* MAEE sama;
* RMSE sama;
* Precision sama;
* Recall sama;
* F1 sama;
* IoU sama.



Ini sangat mencurigakan.

Bila “Directional Derivative” menggunakan fixed direction, hasilnya tidak seharusnya identik dengan THG.

Bila direction-nya selalu dipilih sejajar gradient maksimum, maka hasilnya memang THG—tetapi metode pembandingnya menjadi redundan.

Audit kode wajib dilakukan. Jangan sampai satu array hasil THG tanpa sengaja dipakai dua kali dan diberi dua label berbeda.

---

## 18. Perbandingan metode mencampur operator yang berbeda satuan dan fungsi

Figure 3 membandingkan:

* gravity anomaly;
* THG;
* EHD;
* MDA;
* directional derivative;
* DTHD;
* CHGrad;
* CHGtan.



Tetapi operator tersebut tidak semuanya mempunyai:

* orde turunan sama;
* satuan sama;
* rentang nilai sama;
* output signed versus unsigned yang sama;
* fungsi yang sama.

Pada gambar halaman 12, colorbar bahkan memakai eksponen berbeda untuk masing-masing panel, sementara teks mengatakan seluruh peta berada pada rentang (-0.4) sampai (0.4\ \mathrm{mGal/m}).

Ini tidak benar secara visual maupun dimensional.

Selain itu, Fedi (2002) di daftar pustaka adalah **Multiscale Derivative Analysis**, tetapi manuscript menyebutnya “Multi-Directional Analysis.”  

Itu bukan perbedaan ejaan. Itu metode yang berbeda.

Literature review dan implementasi baseline harus diaudit dari paper asli, bukan dari ringkasan sekunder atau dugaan berdasarkan singkatan.

---

## 19. Satuan gradien tampak salah beberapa orde besaran

Manuskrip mengatakan maximum synthetic gravity anomaly sekitar 12 µGal dengan grid spacing 100 m. 

Konversinya:

[
12\ \mu\mathrm{Gal}=0.012\ \mathrm{mGal}.
]

Bahkan bila seluruh perubahan 0.012 mGal terjadi hanya dalam satu sel 100 m, orde gradiennya sekitar

[
\frac{0.012\ \mathrm{mGal}}{100\ \mathrm{m}}
============================================

1.2\times10^{-4}\ \mathrm{mGal/m}.
]

Namun teks Figure 3 menyebut rentang sampai sekitar

[
0.4\ \mathrm{mGal/m}.
]



Itu ribuan kali lebih besar daripada skala yang masuk akal dari angka anomali dan grid yang dinyatakan.

Pada aplikasi Samalas, manuscript menyebut CHGtan sekitar (\pm2.4\ \mathrm{mGal/m}). 

Dalam satuan Eötvös:

[
1\ \mathrm{mGal/m}=10{,}000\ \mathrm{E},
]

sehingga:

[
2.4\ \mathrm{mGal/m}=24{,}000\ \mathrm{E}.
]

Itu angka yang luar biasa besar untuk interpretasi kerak dangkal biasa dan hampir pasti menunjukkan salah satu dari berikut:

* derivative dihitung per degree;
* derivative dihitung per grid index;
* jarak dipakai dalam kilometre tetapi diberi label metre;
* scale factor hilang;
* colorbar label salah;
* data sebenarnya dalam mGal/km.

> **Sampai satuan ini diaudit dari input hingga output, seluruh interpretasi kuantitatif harus dianggap tidak sah.**

Tidak boleh ada satu pun klaim deposit, ketebalan, atau perbandingan operator sebelum unit test sederhana berhasil:

[
g(x)=ax+by
]

harus menghasilkan tepat:

[
g_x=a,\qquad g_y=b
]

dalam satuan fisik yang benar.

---

## 20. Klaim akurasi beberapa meter pada grid 100 m tidak dapat diterima tanpa penjelasan

Table edge detection melaporkan MAEE sekitar 6–17 m, sementara model dibangun pada grid 100 m.  

Subgrid error secara matematis mungkin dihitung terhadap analytical boundary. Namun itu tidak berarti spatial resolution-nya 6 m.

Naskah harus menjelaskan:

* apakah edge coordinates diinterpolasi subpixel;
* apakah jarak dihitung dari pixel center ke analytical curve;
* apakah units sebenarnya grid index;
* apakah coordinates telah dikonversi dari metre;
* bagaimana uncertainty akibat 100 m sampling dimasukkan.

Jangan melaporkan MAEE 6.0083 m dengan empat angka desimal seolah model 100 m mempunyai kemampuan survei total station.

---

## 21. Uji kedalaman memiliki kontradiksi fatal

Caption Figure 4 mengatakan depth 20 m dan 30 m.

Table 2 dan teks membahas depth:

* 1.000 m;
* 2.000 m;
* 3.000 m.



Ini bukan typo kecil. Depth adalah variabel utama eksperimen.

Pembaca tidak tahu apakah model diuji pada:

* 20–30 m;
* 1–3 km;
* atau angka lain dalam kode.

Selain itu, precision, recall, F1, dan IoU justru meningkat ketika sumber makin dalam, sementara positional errors memburuk. Ini mungkin terjadi karena smoothing menghasilkan lebih sedikit false edges, tetapi harus dijelaskan dengan precision–recall trade-off, bukan dirayakan sebagai sebagian peningkatan performa.

---

# D. Pengolahan data lapangan adalah bagian terlemah naskah

## 22. GGMplus bukan ground gravity survey beresolusi 22 m

Naskah menggunakan GGMplus yang awalnya sekitar 220 m, kemudian melakukan regridding menjadi:

* 111 m untuk Samalas;
* 22.2 m untuk Tambora.

Penulis bahkan mengakui regridding hanya meningkatkan graphical resolution, bukan information content. 

Benar. Lalu mengapa derivative dihitung dan ditafsirkan pada grid palsu tersebut?

> **Regridding bukan mesin fotokopi informasi. Memecah satu pixel menjadi seratus pixel tidak membuat Bumi mengungkap sembilan puluh sembilan fakta baru.**

GGMplus merupakan model komposit sekitar 200 m yang menggabungkan:

* GOCE/GRACE;
* EGM2008;
* dan short-wavelength topographic gravity dari high-pass terrain model.

Dengan kata lain, detail paling pendek pada GGMplus terutama dimodelkan dari topografi, bukan berasal dari pengukuran gravimeter lokal independen. ([Curtin University][1])

Ini sangat penting di Samalas dan Tambora, yang mempunyai relief vulkanik ekstrem.

Sebelum menafsirkan gradient sebagai density structure, penulis harus menjawab:

* berapa bagian signal yang berasal dari topographic gravity model;
* berapa yang berasal dari measured gravity;
* apakah Bouguer correction menggunakan DEM yang sama;
* apakah terjadi double counting;
* apakah derivative hanya memetakan relief residual;
* bagaimana hasil dibandingkan dengan ground gravity.

---

## 23. “Local Bouguer anomaly” tidak dijelaskan secara geodetik

Naskah menyatakan gravity disturbance dari GGMplus dikonversi menjadi Simple Bouguer Anomaly menggunakan DEM dan density 2.67 g/cm³. 

Namun tidak ada formula lengkap untuk:

* normal gravity;
* free-air correction;
* Bouguer slab correction;
* atmospheric correction;
* terrain correction;
* observation height;
* geoid/ellipsoid treatment;
* sign convention;
* unit conversion.

Istilah yang digunakan bergeser antara:

* gravity acceleration;
* gravity disturbance;
* gravity anomaly disturbance;
* Local Bouguer anomaly;
* Simple Bouguer anomaly.

Ini bukan sinonim.

Untuk volcano dengan topografi curam, **Simple Bouguer anomaly** tidak cukup. Terrain correction harus dilakukan secara lengkap. Kesalahan terrain correction akan diperkuat oleh horizontal derivative.

Lebih jauh, density 2.67 g/cm³ sebagai satu angka global mungkin cocok untuk batuan kerak umum, tetapi tidak untuk seluruh kombinasi:

* lava;
* welded tuff;
* unconsolidated pyroclastics;
* caldera fill;
* marine sediment;
* volcanic edifice.

Lakukan sensitivity test terhadap Bouguer density, misalnya 2.0–2.8 g/cm³, dan bandingkan CHG terhadap gradient DEM.

---

## 24. Detail field map berpotensi merupakan topographic imprint

Karena short-wavelength GGMplus sangat dipengaruhi modeled topographic gravity, pola konsentris di sekitar volcanic edifice dapat muncul karena:

* bentuk gunung;
* caldera depression;
* steep flank;
* coastal escarpment;
* DEM-derived component.

Maka penulis harus membandingkan:

[
\mathrm{CHG}(g)
]

dengan:

[
\mathrm{CHG}(h),
]

di mana (h) adalah topografi atau modeled topographic gravity.

Hitung:

* pixelwise correlation;
* spectral coherence;
* azimuthal profile;
* partial correlation setelah topographic component dikeluarkan;
* hasil setelah upward continuation.

Tanpa itu, manuscript mungkin sedang menafsirkan topografi yang telah dimasukkan ke dalam GGMplus sebagai density structure independen.

---

## 25. Klaim deposit setebal 15 m tidak mungkin ditopang oleh data ini

Pada Point D, manuscript menghubungkan CHGtan dengan body:

* tebal 15 m;
* lebar 2.000 m;
* density 2.1 g/cm³.



Tetapi:

* input GGMplus nominalnya sekitar 200–220 m;
* data diregrid secara artifisial;
* tidak ada ground gravity;
* tidak ada inversion;
* tidak ada uncertainty;
* tidak ada model residual;
* tidak ada parameter trade-off;
* dan unit gradient sendiri meragukan.

Gravity potential field bersifat nonunik. Satu nilai atau pola gradient tidak dapat menentukan secara unik:

* ketebalan;
* lebar;
* density;
* kedalaman;
* maupun jenis deposit.

> **Peta berwarna bukan borehole. CHGtan tidak dapat mengukur lapisan 15 m hanya karena warna merah bertemu warna biru.**

Bila penulis ingin mempertahankan model 15 m × 2 km:

1. tampilkan geometry;
2. forward response;
3. filter dengan bandwidth GGMplus;
4. sample pada original 220 m grid;
5. beri noise;
6. bandingkan amplitude dan wavelength;
7. lakukan parameter sensitivity;
8. tunjukkan nonuniqueness.

Saat ini model 2D itu muncul sebagai angka pembenaran setelah pola visual ditemukan.

---

## 26. Interpretasi geologi berubah menjadi pareidolia

Manuskrip menghubungkan pola dengan:

* Sembalun Caldera;
* pyroclastic-flow deposits;
* Tebing Beach;
* buried Pamatan Kingdom;
* Pekat Kingdom;
* radial faults;
* earthquake damage.



Namun tidak ada:

* mapped contact overlay;
* geological polygons;
* cross-section;
* field control points;
* gravity transect;
* uncertainty;
* statistical correspondence;
* blind validation;
* forward model untuk masing-masing target.

Beberapa titik A–E bahkan tidak tampak pada Figure 6 yang diberikan. Figure tersebut hanya memperlihatkan empat peta tanpa annotation yang diperlukan untuk memeriksa klaim.

Interpretasi seperti “fitur ini adalah kerajaan yang terkubur” tidak boleh muncul dari gradient map tanpa independent archaeological/geophysical constraints pada lokasi yang sama.

> **Bila setiap bercak warna diberi nama formasi, deposit, fault, atau kerajaan, itu bukan interpretasi geofisika. Itu kegiatan memberi nama pada awan.**

Gunakan bahasa:

* “spatially coincides with”;
* “is compatible with”;
* “may warrant field verification.”

Jangan gunakan “shows,” “confirms,” atau “corresponds to thickness” sebelum ada validasi.

---

## 27. Peta CHGtan menunjukkan pola starburst yang dapat dipaksakan oleh koordinat

Pada Figure 6 dan Figure 8, CHGtan memperlihatkan garis-garis yang memancar dari pusat.

Pola tersebut dapat muncul karena basis tangensial sendiri berubah arah terhadap azimuth. Bahkan gradient background yang tidak mempunyai sumber radial dapat menghasilkan sectoral or spoke-like patterns setelah diproyeksikan ke basis yang berotasi.

Karena itu, setiap pola radial pada output harus diuji terhadap:

* center shift;
* random center;
* phase-randomized field;
* linear regional gradient;
* rotated field;
* synthetic noise dengan covariance yang sama.

Eksperimen paling sederhana:

1. pindahkan pusat 1, 2, 5, dan 10 km;
2. ulangi CHG;
3. lihat apakah “radial faults” dan “pyroclastic fans” ikut bergerak atau berputar.

Bila pola berubah mengikuti pusat, itu artefak operator, bukan geologi.

---

## 28. Field center dipilih berdasarkan crater, sehingga interpretasinya berisiko sirkular

Penulis memilih pusat di crater, kemudian menggunakan basis radial terhadap crater, lalu menemukan pola radial dan circular di sekitar crater.

Tentu saja.

> **Bila seluruh koordinat didefinisikan agar menghadap crater, hasil akhirnya hampir pasti terlihat crater-centric. Itu bukan validasi; itu konsekuensi konstruksi.**

Diperlukan pembanding:

* center optimized blind;
* crater center;
* shifted center;
* center of Bouguer anomaly;
* center of topography;
* center of mapped caldera.

Kemudian nilai objective dan geological correspondence harus dibandingkan.

---

# E. Hybrid CHG–THG tidak mempunyai makna fisik yang jelas

Hybrid didefinisikan sebagai campuran normalized CHG dengan normalized THG menggunakan (\alpha) atau (\beta). 

Masalahnya:

1. THG nonnegative, CHGrad dan CHGtan signed.
2. Normalisasi memakai `max`, bukan maximum absolute value.
3. Negative extrema dapat lebih besar secara absolut daripada positive extrema.
4. Signed component dapat membatalkan THG.
5. (\alpha) dan (\beta) dipilih subjektif.
6. Tidak ada objective function untuk memilih bobot.
7. Tidak ada bukti hybrid memperbaiki edge metrics.
8. Perubahan warna dapat hanya berasal dari rescaling.

Ini adalah **visualization slider**, bukan operator geofisika baru.

Lebih informatif bila penulis mendefinisikan:

[
C_r=
\frac{|G_r|}
{\mathrm{THG}+\epsilon},
]

[
C_\theta=
\frac{|G_\theta|}
{\mathrm{THG}+\epsilon},
]

atau orientation angle:

[
\phi=
\operatorname{atan2}(G_\theta,G_r).
]

Dengan demikian:

* (C_r\approx1) berarti gradient normal dominan radial;
* (C_\theta\approx1) berarti gradient normal dominan tangensial;
* amplitude dan orientation dapat ditampilkan terpisah.

Saat ini hybrid mencampur amplitude dan orientation menjadi satu warna tanpa makna yang dapat diuji.

---

# F. Klaim aplikasi magnetik terlalu sembrono

Naskah mengatakan CHG juga sesuai untuk magnetic anomalies setelah reduction to the pole. 

Kalimat ini terlalu sederhana, khususnya untuk Indonesia yang berada pada lintang magnetik rendah.

Standard RTP dikenal menjadi tidak stabil pada low magnetic latitude dan tidak terdefinisi secara klasik di magnetic equator. ([SEG Library][2])

Aplikasi magnetik juga dipengaruhi:

* inducing-field inclination;
* declination;
* remanent magnetization;
* anisotropy;
* unknown total magnetization direction;
* overlapping dipolar anomalies.

Jadi sebelum mengklaim aplikasi magnetik, lakukan synthetic tests untuk:

* inclination (0^\circ, 10^\circ, 30^\circ, 60^\circ, 90^\circ);
* remanence berbeda;
* RTP standard dan stabilized RTP;
* reduction to equator;
* analytic signal;
* noise dan overlapping sources.

Satu kalimat “after RTP” bukan validasi magnetik.

---

# G. Masalah visual, editorial, dan quality control

## 29. Figure 2 tidak mempunyai satuan dan koordinat fisik yang jelas

Axes hanya menunjukkan angka 200, 400, 600, 800, tampaknya grid indices. Colorbar menggunakan faktor (10^{-8}), (10^{-6}), dan sebagainya tanpa unit yang konsisten.

Naskah lalu memberi satuan µGal dan mGal/m dalam teks.

Pembaca tidak dapat melacak:

[
\text{model density}
\rightarrow
g
\rightarrow
g_x,g_y
\rightarrow
\mathrm{CHG}
]

dengan satuan yang konsisten.

Setiap panel harus memiliki:

* x dan y dalam km;
* gravity dalam mGal atau µGal;
* gradient dalam mGal/km atau E;
* common color scales bila dibandingkan;
* explicit noise level.

---

## 30. Figure 3 membandingkan color scales yang berbeda

Visual halaman 12 menunjukkan setiap operator memakai exponent dan color range sendiri. Namun teks menyatakan semua berada pada rentang yang sama.

Dengan autoscaling terpisah, metode yang sangat lemah dapat tampak sama tajamnya dengan metode kuat.

Gunakan dua versi:

1. common physical color scale;
2. normalized scale untuk membandingkan morphology.

Jangan mencampurkan keduanya.

---

## 31. Figure 4 salah menyebut kedalaman

Caption mengatakan 20 m dan 30 m, sedangkan tabel mengatakan 1.000–3.000 m. Ini harus diperbaiki setelah mengecek source code, bukan hanya mengganti caption berdasarkan dugaan.

---

## 32. Figure 6 kehilangan seluruh titik interpretasi utama

Teks membahas Points A, B, C, D, dan E, tetapi figure tidak menampilkan label tersebut dengan jelas. Pembaca tidak dapat memeriksa interpretasi.

Selain itu:

* colorbar tidak memiliki unit;
* coastline/geology tidak ada;
* crater outline tidak ada;
* scale bar tidak ada;
* north arrow tidak ada;
* data-resolution footprint tidak ada;
* point locations tidak ada.

Figure tersebut belum dapat berfungsi sebagai scientific evidence.

---

## 33. Figure 8 caption salah jumlah panel

Figure 8 secara visual mempunyai:

* gravity;
* THG;
* CHGrad;
* CHGtan.

Namun caption hanya menyebut tiga panel dan urutannya tidak tepat. Teks selanjutnya menyebut Figure 8(a)–8(d), menunjukkan caption dan figure berasal dari versi berbeda. 

---

## 34. Tabel dan nomor bagian tidak terkendali

Naskah menggunakan “Table 1” untuk beberapa tabel berbeda:

* perbandingan metode;
* edge detection;
* elapsed time.

Nomor section meloncat dari 4.2 ke 6. Tidak ada Section 5.

Ini merupakan tanda bahwa manuscript belum melalui satu kali pun pemeriksaan editorial menyeluruh.

---

## 35. Daftar pustaka memuat jejak output chatbot

Naskah menyatakan ChatGPT digunakan untuk perbaikan bahasa, dan itu sendiri tidak bermasalah bila disunting serta diverifikasi. 

Namun salah satu entri referensi berakhir dengan tautan yang memuat:

```text
utm_source=chatgpt.com
```

serta fragmen “Bottom of Form.” 

Itu tidak dapat dibiarkan.

> **Deklarasi penggunaan AI adalah transparansi. Membiarkan sampah antarmuka chatbot masuk daftar pustaka adalah kegagalan quality control.**

Semua referensi harus diperiksa satu per satu terhadap sumber primer:

* judul;
* penulis;
* tahun;
* jurnal;
* volume;
* halaman;
* DOI;
* relevansi;
* apakah benar disitasi;
* apakah mendukung pernyataan yang ditempelinya.

---

## 36. Klaim melebar tanpa bukti

Discussion mengatakan CHG dapat diaplikasikan untuk:

* planetary gravity;
* magnetic data;
* geothermal;
* disaster mitigation.



Tidak ada satu pun pengujian untuk tiga kategori pertama selain gravity terrestrial, dan sama sekali tidak ada hubungan kuantitatif dengan disaster mitigation.

Hapus.

Klaim yang terlalu luas tidak membuat paper terlihat visioner. Ia membuat paper terlihat tidak mampu membedakan hasil dari harapan.

---

# H. Analisis minimum sebelum naskah boleh dikirim kembali

## 1. Ubah positioning ilmiahnya

Jangan jual CHG sebagai improved edge detector.

Posisikan sebagai:

> **center-referenced orientation decomposition of the horizontal gradient.**

Nyatakan dengan jujur bahwa tidak ada informasi baru relatif terhadap (g_x,g_y); nilai tambahnya adalah interpretabilitas relatif terhadap pusat.

---

## 2. Audit novelty dan sitasi karya terdahulu

Masukkan paper radial derivative sebelumnya dan buat tabel:

| Unsur                 | Radial derivative terdahulu | Naskah CHG  |
| --------------------- | --------------------------- | ----------- |
| Radial projection     | Ada                         | Ada         |
| Tangential projection | Tidak/Ada?                  | Ada         |
| Automatic center      | Tidak                       | Diklaim ada |
| Norm relation         | Tidak                       | Ada         |
| Edge metrics          | Terbatas                    | Ada         |
| Field caldera test    | Tidak                       | Ada         |

Kebaruan harus berada pada sel yang benar-benar berbeda.

---

## 3. Benahi interpretasi geometri

Gunakan terminologi:

* radial-normal response;
* tangential-normal response;
* circumferential boundary;
* radial lineament;
* azimuthal asymmetry.

Turunkan secara eksplisit:

[
G_r=\partial g/\partial r,
]

[
G_\theta=(1/r)\partial g/\partial\theta.
]

Tunjukkan bahwa untuk (g(r)):

[
G_\theta=0.
]

---

## 4. Bangun synthetic benchmark yang benar

Gunakan sedikitnya:

* circle;
* ring;
* ellipse;
* partial ring;
* eccentric double circles;
* radial dykes;
* tangential arcs;
* dipping faults;
* multiple overlapping bodies;
* variable density;
* regional trend;
* realistic terrain residual;
* irregular mask.

Untuk setiap model, variasikan:

* noise;
* depth;
* center offset;
* grid spacing;
* smoothing;
* survey extent.

Gunakan ratusan realizations dan confidence intervals.

---

## 5. Audit satuan dari kode paling dasar

Buat unit tests:

### Linear field

[
g(x,y)=2x+3y.
]

Harus diperoleh:

[
g_x=2,\qquad g_y=3.
]

### Radial field

[
g(x,y)=x^2+y^2.
]

Harus diperoleh:

[
G_r=2r,\qquad G_\theta=0.
]

### Azimuthal field

Gunakan fungsi dengan variasi sudut terkontrol dan verifikasi (G_\theta).

Semua test harus menghasilkan satuan benar untuk:

* metre;
* kilometre;
* degree;
* grid index.

---

## 6. Redesign center optimization

Diperlukan:

* normalized circularity objective;
* minimum sample per ring;
* weighting berdasarkan occupancy;
* treatment of incomplete rings;
* objective landscape;
* center uncertainty;
* null-model rejection;
* blind random-center tests;
* multiple-center extension;
* sensitivity terhadap regional trend.

Pusat harus dapat dinyatakan **not identifiable**. Jangan memaksa setiap peta mempunyai pusat.

---

## 7. Gunakan data lapangan pada bandwidth asli

Untuk GGMplus:

* gunakan original grid;
* jangan menafsirkan interpolated 22.2 m pixels sebagai observasi;
* dokumentasikan produk GGMplus;
* pisahkan topographic component;
* lakukan terrain correction lengkap;
* uji Bouguer density;
* lakukan upward-continuation sensitivity;
* bandingkan dengan ground gravity bila tersedia.

---

## 8. Hilangkan klaim ketebalan tanpa inversion

Jangan menyatakan deposit 15 m atau geometry tertentu dari CHG map.

Gunakan forward modelling/inversion dengan:

* density bounds;
* depth bounds;
* uncertainty;
* resolution;
* alternative models.

---

## 9. Validasi field secara kuantitatif

Overlay:

* mapped caldera rim;
* faults;
* pyroclastic boundaries;
* archaeological sites;
* independent electrical/seismic profiles.

Hitung:

* edge-distance error;
* precision–recall dengan spatial tolerance;
* profile correlation;
* azimuthal coherence;
* bootstrap uncertainty.

---

## 10. Pisahkan amplitude dan orientation

Alih-alih hybrid (\alpha/\beta) subjektif, tampilkan:

* THG amplitude;
* orientation angle;
* radial alignment ratio;
* tangential alignment ratio;
* confidence mask untuk THG rendah.

---

## 11. Hapus aplikasi magnetik sampai diuji

Atau tambahkan synthetic magnetic section lengkap, khususnya pada low latitude dan remanent magnetization.

---

# Kesimpulan ilmiah yang masih dapat dipertahankan

Versi defensible dari kontribusi ini adalah:

> Untuk pusat yang telah ditentukan, horizontal gravity-gradient vector dapat ditransformasikan secara ortogonal dari basis Cartesian ke basis radial–tangensial. Komponen radial dan tangensial tersebut mempertahankan tanda serta memungkinkan orientasi gradien dianalisis relatif terhadap pusat. Dekomposisi ini tidak menambahkan informasi terhadap horizontal gradient vector dan tidak secara inheren meningkatkan edge localization, tetapi dapat membantu visualisasi struktur yang terorganisasi secara radial ketika pusat mempunyai dasar geologis yang independen.

Yang belum dapat dipertahankan:

> CHG merupakan operator baru yang lebih baik daripada THG, secara otomatis menentukan pusat geologi, mengidentifikasi deposit pyroclastic 15 m, menemukan kerajaan terkubur, dan siap digunakan untuk gravity, magnetic, planetary, geothermal, serta disaster mitigation.

---

# Pertanyaan untuk menguji Muhammad Zuhdi

1. **Tuliskan gradien scalar field dalam koordinat polar. Apa makna fisik (G_r) dan (G_\theta)?**

2. **Untuk anomali sempurna (g=g(r)), berapa nilai CHGtan?**

3. **Mengapa circular boundary yang arah garisnya tangensial justru memiliki gradient normal radial?**

4. **Apa yang benar-benar baru dibanding paper radial derivative Anda tahun 2018 yang memakai formula (d_x\cos\theta+d_y\sin\theta)?**

5. **Bila (\mathrm{THG}^2=G_r^2+G_\theta^2), informasi baru apa yang diciptakan CHG?**

6. **Mengapa persentase radial dan tangensial selalu berjumlah 100%? Apakah itu performa atau identitas?**

7. **Apa makna fisik kata “energy” dalam energy response Anda?**

8. **Bagaimana CHG didefinisikan tepat pada (r=0)?**

9. **Mengapa THG dikatakan tidak cocok untuk circular feature, padahal THG rotationally invariant?**

10. **Mengapa judul memakai kata “Improved” ketika EHD mempunyai F1 dan IoU jauh lebih tinggi?**

11. **Bagaimana threshold detected edges dipilih untuk setiap metode?**

12. **Mengapa THG dan Direct Derivative memiliki seluruh metrik yang identik?**

13. **Bagaimana MAEE 6 m diperoleh dari grid 100 m?**

14. **Apakah derivative dihitung per metre, kilometre, degree, atau grid index?**

15. **Bagaimana 12 µGal pada grid 100 m dapat menghasilkan gradient hingga 0.4 mGal/m?**

16. **Berapa Eötvös nilai 2.4 mGal/m, dan apakah angka itu masuk akal?**

17. **Mengapa Figure 4 mengatakan depth 20–30 m sedangkan Table 2 mengatakan 1–3 km?**

18. **Apa yang terjadi pada center estimate bila anomaly sign dibalik?**

19. **Apa yang terjadi bila (\sum g_i) pada weighted centroid mendekati nol?**

20. **Bagaimana algoritma menyatakan bahwa suatu dataset tidak mempunyai circular center?**

21. **Mengapa Model 3 yang noncircular tetap menghasilkan optimized center?**

22. **Berapa uncertainty pusat Samalas dan Tambora?**

23. **Apakah pusat field data benar-benar dioptimalkan atau dipilih dari crater center?**

24. **Apa yang terjadi pada peta CHGtan bila center dipindahkan 5 km?**

25. **Bagaimana Anda membuktikan pola starburst bukan artefak basis yang berotasi?**

26. **Bagaimana GGMplus membangun wavelength di bawah sekitar 10 km?**

27. **Berapa korelasi CHG map dengan DEM dan modeled topographic gravity?**

28. **Mengapa regridding 220 m menjadi 22.2 m dilakukan sebelum differentiation?**

29. **Apa perbedaan Simple Bouguer dan Complete Bouguer anomaly pada topografi vulkanik curam?**

30. **Bagaimana CHGtan dapat menentukan deposit setebal 15 m tanpa inversion dan uncertainty?**

31. **Mengapa standard RTP aman digunakan di Indonesia yang berada pada magnetic latitude rendah?**

32. **Temuan geologi mana yang tetap berdiri bila seluruh label A–G dan sejarah erupsi disembunyikan dari interpreter?**

Bila mahasiswa tidak dapat menjawab pertanyaan-pertanyaan tersebut dengan derivasi, unit tests, dan eksperimen—bukan dengan menunjuk warna pada peta—maka ia belum menguasai metode yang diajukan.

---

# Contoh komentar ringkas kepada editor

> **Recommendation: Reject.** The manuscript presents the radial and tangential projections of the horizontal gravity-gradient vector relative to a chosen center. This decomposition may provide a useful orientation diagnostic, but it is an orthogonal coordinate transformation and does not create information beyond the Cartesian gradient components. The novelty is further unclear because a prior publication by the first author already defines the same radial derivative. The manuscript also appears to confuse feature orientation with gradient-normal orientation: a circular boundary should produce a radial-gradient response, while the tangential component measures azimuthal variation. The quantitative tests do not support the title’s claim of an improved operator; the reported CHG F1 and IoU scores are substantially lower than those of EHD, and the edge-thresholding procedure is insufficiently documented. Serious unit inconsistencies occur between the stated synthetic anomaly amplitudes, grid spacing, and reported gradient values. The field application uses GGMplus data regridded far below its original sampling, applies incompletely documented Bouguer corrections in steep volcanic terrain, and makes highly specific interpretations of thin pyroclastic deposits and archaeological sites without inversion, uncertainty analysis, or independent ground-gravity validation. The center-optimization procedure is not demonstrated blindly on the field examples and lacks uncertainty and a no-center rejection criterion. A complete conceptual and numerical redesign is required.

# Putusan akhir

## **Sebagai ide awal disertasi: ada inti yang dapat diselamatkan.**

Inti yang berguna adalah:

* dekomposisi orientasi;
* relative-to-center analysis;
* pemisahan circumferential versus radial structural organization;
* visualisasi signed gradient components.

## **Sebagai manuscript metode potensial internasional: reject.**

Naskah saat ini:

* menyebut rotasi basis sebagai operator baru;
* tidak menyitir metode radial terdahulu milik penulis sendiri;
* salah atau kabur membedakan arah fitur dan arah gradien;
* dikalahkan oleh baseline menurut metriknya sendiri;
* mempunyai satuan yang tidak dapat dipertanggungjawabkan;
* menguji pusat dengan kasus yang terlalu mudah;
* memperlakukan regridding sebagai resolusi;
* menafsirkan GGMplus seolah ground survey;
* dan melompat dari pola warna ke deposit, fault, kerajaan terkubur, hingga disaster mitigation.

> **Masalahnya bukan bahasa Inggris. Masalahnya bukan kurang banyak gambar. Masalahnya adalah manuscript belum memisahkan mana identitas matematis, mana informasi data, mana prior geometris, mana artefak koordinat, dan mana geologi yang benar-benar dibuktikan.**

Untuk level doktoral, pemisahan itu bukan kemewahan. Itulah inti kompetensi ilmiahnya.

[1]: https://ddfe.curtin.edu.au/gravitymodels/GGMPlus/hirt2013_ultrahighres_gravity.pdf "GGMplus - a 200m-resolution picture of Earth’s gravity field"
[2]: https://library.seg.org/doi/abs/10.1190/1.1444948?utm_source=chatgpt.com "Stable reduction to the pole at the magnetic equator"

