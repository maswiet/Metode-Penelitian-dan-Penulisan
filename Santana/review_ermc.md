# Review sangat seksama

Naskah yang dinilai adalah **“Efficient Monte Carlo Simulation of Continuous-Variable Hamiltonians within the Phase-Space Formulation”** oleh Santana Y. Pradata dan rekan-rekan. Naskah memperkenalkan *epistemically restricted Monte Carlo* atau ERMC, yaitu estimasi energi variational berbasis *epistemically restricted phase space*, dengan satu ensemble posisi–momentum yang digunakan kembali selama optimasi. 

Saya akan keras terhadap naskahnya, bukan terhadap martabat Santana. Untuk ukuran mahasiswa S1, keberanian memasuki wilayah variational Monte Carlo, continuous-variable circuits, Hamilton–Jacobi theory, dan epistemically restricted phase space patut dipuji. Namun, begitu karya ini mengenakan template **Quantum Science and Technology** dan memakai kata **efficient**, ia harus dinilai sebagai artikel jurnal internasional—bukan diberi kelonggaran karena penulis pertamanya masih sarjana.

# Putusan

## **REJECT IN PRESENT FORM — REBUILD THE NUMERICAL STUDY**

Bukan *minor revision*. Bukan sekadar memperbaiki bahasa Inggris, menambah error bar, atau mengganti beberapa caption.

Masalah utamanya adalah:

1. klaim efisiensi dibangun dari perbandingan VMC yang tidak adil dan sebagian waktunya hanya diekstrapolasi;
2. parameter dioptimalkan dan dievaluasi pada ensemble Monte Carlo yang sama, sehingga terjadi *optimizer’s curse* atau bias seleksi;
3. Markov chain tidak pernah dibuktikan telah konvergen atau menghasilkan sampel efektif yang independen;
4. random variable (\xi) disampling meskipun untuk observable kuadratik ekspektasinya sebenarnya dapat diintegrasikan secara analitik;
5. gate set yang dipakai sangat terbatas dan secara aljabar membuat transformasi posisi tetap affine, sehingga penambahan layer sebagian besar hanya menambah parameter redundan;
6. pseudocode utama mengandung kesalahan indeks, input, output, dan kondisi penghentian yang membuatnya tidak dapat dijalankan sebagaimana tertulis;
7. benchmark terlalu sederhana dan belum menunjukkan keunggulan terhadap VMC modern, correlated sampling, reweighting, atau normalizing-flow-based variational methods;
8. klaim “Hamiltonian simulation” terlalu luas untuk pekerjaan yang sebenarnya hanya menghitung energi keadaan dasar secara variational.

Diagnosis paling ringkas:

> **Naskah ini memiliki benih teori yang menarik, tetapi bukti numeriknya saat ini lebih menyerupai demonstrasi bahwa squeezing dapat mengubah lebar Gaussian daripada demonstrasi sebuah metode Monte Carlo baru yang efisien dan umum.**

| Aspek                                  |      Nilai |
| -------------------------------------- | ---------: |
| Ambisi intelektual untuk level S1      |        5/5 |
| Kejelasan ide dasar                    |      3.5/5 |
| Kebaruan yang telah dibuktikan         |        2/5 |
| Kebenaran matematis implementasi       |      1.5/5 |
| Validitas sampling dan statistik       |        1/5 |
| Keadilan benchmark                     |      0.5/5 |
| Analisis efisiensi                     |        1/5 |
| Generalisasi ke sistem banyak partikel |        1/5 |
| Reproducibility dari manuskrip         |      1.5/5 |
| Kesiapan untuk QST                     |        1/5 |
| **Rekomendasi**                        | **Reject** |

---

# Hal yang memang layak diapresiasi

## 1. Ide utamanya menarik

Gagasan menggunakan satu ensemble phase-space, kemudian mentransformasikannya berulang kali selama optimasi, berpotensi mengamortisasi biaya sampling. Naskah juga cukup jelas membedakan ERMC dari implementasi VMC sederhana yang mengganti distribusi sampling saat parameter trial wave function berubah. 

## 2. Penulis tidak sepenuhnya menyembunyikan batas teorinya

Naskah menyatakan bahwa ekuivalensi ERPS hanya berlaku ketika observable setelah transformasi tetap paling tinggi orde dua terhadap momentum. Penulis juga mengakui bahwa gate set yang digunakan belum universal. Kejujuran ini penting.  

## 3. Ada upaya membandingkan akurasi, waktu, ukuran sampel, jenis distribusi, dan kedalaman circuit

Sebagai eksplorasi awal mahasiswa S1, cakupannya cukup luas:

* pengaruh (N_s);
* distribusi (\xi);
* perbandingan ERMC–VMC;
* jumlah layer;
* tiga Hamiltonian;
* tiga trial ansatz.

Ini menunjukkan Santana tidak berhenti setelah memperoleh satu plot yang terlihat bagus.

## 4. Penulis mengakui ERMC mempunyai varians lebih besar

Naskah tidak menyembunyikan bahwa ERMC memberikan standard error lebih besar daripada VMC pada ukuran sampel sama. Penulis juga mengakui bahwa layer lebih dalam tidak otomatis memperbaiki energi dan dapat memperbesar biaya optimasi.  

## 5. Kode dinyatakan terbuka

Q-McSpare tersedia melalui repositori publik. Itu modal yang baik, walaupun repositori aktif tanpa commit terarsip, environment terkunci, dan seed yang didokumentasikan belum cukup untuk memenuhi reproducibility artikel. 

Apresiasi selesai. Sekarang bagian yang membuat naskah ini belum layak terbit.

---

# A. Kelemahan konseptual dan matematis yang fatal

## 1. Ini bukan “Hamiltonian simulation” dalam makna yang lazim

Judul mengatakan:

> **Efficient Monte Carlo simulation of continuous-variable Hamiltonians**

Tetapi naskah tidak mensimulasikan dinamika:

[
e^{-i\hat H t},
]

tidak menghitung propagasi waktu, tidak melakukan real-time atau imaginary-time evolution, dan tidak menunjukkan simulasi circuit dynamics.

Yang dilakukan adalah:

[
\min_{\boldsymbol{\theta}}
\langle\psi|
\hat U^\dagger(\boldsymbol{\theta})
\hat H
\hat U(\boldsymbol{\theta})
|\psi\rangle,
]

yakni **variational ground-state energy estimation**.

Dalam komunitas quantum algorithms, “Hamiltonian simulation” mempunyai arti jauh lebih spesifik daripada “menghitung nilai harapan Hamiltonian.” Menggunakan istilah besar untuk tugas yang lebih sempit akan membuat reviewer curiga sejak judul.

### Judul yang lebih jujur

> **Epistemically Restricted Phase-Space Monte Carlo for Variational Energy Estimation**

atau:

> **Reusable Phase-Space Ensembles for Variational Energy Estimation under Restricted Continuous-Variable Transformations**

Kata **efficient** juga harus dikeluarkan sampai efisiensi dibuktikan dengan benchmark yang fair.

---

## 2. Kebaruan algoritmiknya belum dibedakan dari *common random numbers* dan *correlated sampling*

Core contribution yang ditawarkan adalah:

> sample sekali, gunakan ensemble yang sama untuk banyak nilai parameter.

Masalahnya, penggunaan sampel bersama untuk membandingkan beberapa parameter bukan gagasan asing dalam komputasi stokastik. Dalam VMC dikenal:

* correlated sampling;
* reweighting;
* persistent Markov chains;
* stochastic reconfiguration;
* sample reuse;
* transport-map atau normalizing-flow sampling;
* reparameterization-based optimization.

Naskah memang menyebut bahwa VMC dapat memerlukan re-equilibration atau “appropriate reweighting procedure,” tetapi tidak membandingkan ERMC dengan prosedur tersebut. 

Sebaliknya, baseline yang dipilih adalah VMC yang melakukan sampling terpisah untuk setiap titik parameter.

> **Penulis mengikat kaki lawan, mengajaknya lomba lari, kemudian menggunakan kemenangan itu sebagai bukti efisiensi.**

Untuk membuktikan novelty, penulis harus menjawab:

* Apa perbedaan matematis ERMC dari correlated-sampling VMC?
* Apa keuntungan ERPS momentum dibanding reparameterized sampling biasa?
* Mengapa transformasi sampel bukan sekadar normalizing flow dengan base distribution tetap?
* Apa theorem, estimator, atau scaling baru yang tidak sudah terdapat pada metode transport/correlated sampling?

Tanpa kajian dan benchmark tersebut, ERMC masih dapat terlihat sebagai nama baru bagi kombinasi teknik yang sudah dikenal.

---

## 3. Optimasi dan evaluasi menggunakan ensemble yang sama menghasilkan bias seleksi

Ini mungkin masalah statistik paling serius.

Untuk parameter tetap (\theta), estimator

[
\widehat E_S(\theta)
====================

\frac{1}{N_s}
\sum_{i=1}^{N_s}
H\bigl(\Gamma(q_i,p_i\mid\theta)\bigr)
]

dapat menjadi estimator tak bias—dengan asumsi sampelnya benar.

Tetapi naskah memilih:

[
\widehat\theta
==============

\arg\min_\theta \widehat E_S(\theta)
]

menggunakan ensemble (S) yang sama, lalu melaporkan

[
\widehat E_S(\widehat\theta)
]

sebagai hasil akhir.

Optimizer dapat mengeksploitasi fluktuasi kebetulan dalam sampel tetap tersebut. Ini dikenal sebagai:

* *optimizer’s curse*;
* adaptive overfitting to Monte Carlo noise;
* selection bias;
* winner’s bias.

Dengan kata lain:

> **Sampel yang sama menjadi data latihan, data validasi, dan data ujian. Tentu optimizer akan tampak pintar—ia sudah menghafal kebisingannya.**

Naskah sendiri menunjukkan bahwa pada sampel kecil ERMC dapat jatuh di bawah exact ground-state energy dan standard error-nya dapat terestimasi terlalu kecil. 

Lebih nyata lagi, Table 2 melaporkan untuk harmonic oscillator dengan (E_0=3):

[
E_{\rm ER}^{\rm Slater}=2.9981\pm0.0017,
]

yakni central estimate di bawah variational bound. 

Secara statistik, selisih tersebut belum signifikan. Tetapi secara metodologis, ia menunjukkan bahwa nilai minimum Monte Carlo tidak dapat langsung diperlakukan sebagai variational upper bound.

### Perbaikan wajib

Gunakan tiga ensemble independen:

1. **training ensemble** untuk optimasi;
2. **validation ensemble** untuk early stopping dan pemilihan hyperparameter;
3. **fresh test ensemble** untuk melaporkan energi final.

Ulangi seluruh prosedur sedikitnya 20–50 kali menggunakan seed independen. Laporkan:

* distribusi (\widehat\theta);
* training energy;
* independent test energy;
* optimizer generalization gap;
* frekuensi estimasi jatuh di bawah (E_0).

Tanpa ini, angka energi hasil optimasi belum dapat dipercaya.

---

## 4. Variabel acak (\xi) sebenarnya tidak perlu disampling untuk mean energy

Momentum ERPS ditulis sebagai:

[
p=a(q)+\xi b(q).
]

Naskah membatasi observable hasil transformasi agar paling tinggi kuadratik terhadap momentum. Karena itu, untuk (q) dan (\theta) tetap,

[
O(q,p)
======

A(q,\theta)
+
B(q,\theta)\xi
+
C(q,\theta)\xi^2.
]

Ekspektasinya terhadap (\xi) adalah:

[
\mathbb E_\xi[O]
================

A
+
B\mathbb E[\xi]
+
C\mathbb E[\xi^2].
]

Karena manuskrip menetapkan:

[
\mathbb E[\xi]=0,\qquad
\mathbb E[\xi^2]=\hbar^2,
]

maka:

[
\mathbb E_\xi[O]
================

A+C\hbar^2.
]

Artinya, **bentuk distribusi penuh (\chi(\xi)) memang tidak dapat memengaruhi mean energy** selama observable paling tinggi kuadratik dalam (p). Hal ini sudah mengikuti secara analitik dari asumsi metode. Kondisi mean dan varians tersebut dinyatakan eksplisit dalam naskah. 

Maka Figure 1(a), yang “menemukan” hanya ada pengaruh lemah dari bentuk distribusi, bukanlah penemuan numerik. Itu seharusnya identitas matematis dalam limit sampling tak hingga.

Yang dapat dipengaruhi higher moments distribusi adalah **variance estimator**, karena (O^2) dapat mengandung hingga (\xi^4).

### Masalah yang lebih memalukan

Karena dua momen yang diperlukan sudah diketahui tepat, penulis dapat melakukan *conditional analytical averaging* terhadap (\xi) atau menggunakan pasangan antithetic (\xi=\pm\hbar).

Dengan demikian, stochastic noise tambahan dari (\xi) dapat dihilangkan atau dikurangi drastis.

> **Penulis memperkenalkan random variable, mengetahui tepat mean dan variansnya, lalu tetap melakukan Monte Carlo terhadapnya dan mengeluhkan bahwa standard error menjadi lebih besar. Itu bukan efisiensi; itu membayar noise untuk informasi yang sudah dimiliki gratis.**

Ini dapat menjadi perbaikan metodologis paling bernilai:

* Rao–Blackwellize estimator terhadap (\xi);
* bandingkan raw ERMC versus analytically averaged ERMC;
* ukur variance reduction;
* revisi klaim efisiensi berdasarkan estimator yang lebih optimal.

---

## 5. Bentuk distribusi (\xi) tidak dijelaskan secara reproducible

Figure 1 menampilkan:

* Binomial;
* Gaussian;
* Exponential;
* Lognormal;
* Gamma;
* Uniform.

Tetapi naskah tidak memberi tabel parameter distribusi.

Untuk exponential, lognormal, dan gamma—yang pada bentuk standar hanya memiliki dukungan positif—bagaimana distribusi tersebut diubah agar memiliki mean nol?

* Apakah dikurangi mean?
* Apakah diskalakan?
* Apakah kemudian varians tepat (\hbar^2)?
* Apakah satu (\xi) digunakan per konfigurasi atau per komponen?
* Apakah seed sama untuk seluruh distribusi?

Tanpa definisi lengkap, Figure 1 tidak dapat direproduksi.

Bila “binomial” sebenarnya adalah distribusi dua titik (\xi=\pm\hbar), istilah yang lebih tepat mungkin Rademacher-scaled distribution, bukan sekadar “binomial.”

---

## 6. Gate set membuat transformasi posisi tetap affine

Gate yang digunakan adalah:

* squeezing;
* displacement;
* beam splitter;
* cubic phase. 

Perhatikan transformasi posisi:

* squeezing: (q\mapsto A q);
* displacement: (q\mapsto q+d);
* beam splitter: (q\mapsto Bq);
* cubic phase: (q\mapsto q).

Jadi setelah satu layer ataupun seratus layer:

[
q' = A_{\rm total}q+d_{\rm total}.
]

Transformasi posisi tetap **affine**.

Akibatnya, probability density hasil transformasi hanyalah affine pushforward dari base density:

[
\rho'(q')
=========

\rho!\left(A^{-1}(q'-d)\right)
\left|\det A^{-1}\right|.
]

Penambahan cubic phase mengubah momentum atau phase, tetapi tidak mengubah modulus wave function pada representasi posisi.

Ini memiliki konsekuensi besar:

1. base Gaussian tetap berada dalam keluarga correlated Gaussian;
2. penambahan layer tidak menciptakan deformasi nonlinear baru pada amplitude;
3. trial density tidak dapat secara umum membentuk ground state anharmonik yang strongly non-Gaussian;
4. layer-layer tambahan dapat hanya mereparameterisasi transformasi efektif yang sama.

Naskah menemukan bahwa penambahan layer tidak memperbaiki energi secara sistematis dan menduga optimization landscape atau partial redundancy. 

Tetapi ini bukan sekadar dugaan numerik. Ada alasan aljabar langsung:

> **Mengulang transformasi affine tidak membuatnya menjadi nonlinear. Ia hanya membuat formula affine itu lebih panjang dan komputasinya lebih mahal.**

Alih-alih buru-buru memanggil literatur *barren plateau*, penulis harus:

* menurunkan bentuk tertutup komposisi layer;
* menghitung jumlah parameter independen;
* mengidentifikasi parameter redundan;
* menunjukkan apakah (L) layer dapat direduksi menjadi satu effective layer;
* menjelaskan expressive family yang sebenarnya.

Figure 4 saat ini lebih mirip bukti bahwa arsitektur tidak bertambah ekspresif daripada bukti adanya circuit-depth phenomenon.

---

## 7. Harmonic oscillator adalah pertandingan kandang yang sudah diatur agar ERMC menang

Benchmark utama change-of-variables menggunakan:

* Gaussian trial state;
* harmonic oscillator;
* squeezing transformation.

Squeezing memang secara analitik mengubah lebar Gaussian. Jadi kesesuaian kurva ERMC dan VMC pada Figure 2 pada dasarnya adalah pemeriksaan change-of-variables yang seharusnya berhasil bila kode tidak salah. 

Ini berguna sebagai **unit test**.

Tetapi ia bukan benchmark kuat bagi metode baru.

> **Menunjukkan bahwa squeezing dapat mengubah lebar Gaussian pada harmonic oscillator sama dengan menunjukkan bahwa penggaris dapat mengukur garis lurus. Perlu dilakukan, tetapi jangan dipasarkan sebagai kemenangan komputasi.**

Benchmark yang benar-benar discriminating harus memerlukan:

* nonlinear amplitude deformation;
* correlation yang tidak dapat direduksi ke Gaussian covariance;
* nodal structure;
* fermionic antisymmetry;
* multimodality;
* dimensional scaling.

---

## 8. Klaim bahwa hasil anharmonik “worked well” tidak didukung angka

Table 2 memberi exact or reference energy:

[
E_0^{\rm anharmonic}=1.09.
]

Hasil ERMC:

* Gaussian: (1.1765\pm0.0015);
* Slater-type: (1.1763\pm0.0015);
* Jastrow: (1.1986\pm0.0014). 

Relative errors-nya kira-kira:

* Gaussian: **7.94%**;
* Slater-type: **7.92%**;
* Jastrow: **9.96%**.

Ini bukan error statistik. Selisih Gaussian terhadap reference energy adalah sekitar:

[
\frac{1.1765-1.09}{0.0015}\approx58
]

standard errors.

Jadi kalimat bahwa Gaussian dan Slater-type “worked well” tidak dapat dipertahankan tanpa mendefinisikan terlebih dahulu arti *worked well*.

> **Empat digit desimal tidak dapat menyembunyikan error sistematis delapan persen.**

Gunakan tabel yang memuat:

* exact/reference energy;
* ERMC energy;
* VMC energy;
* absolute error;
* relative error;
* Monte Carlo SE;
* optimizer-run SD;
* runtime;
* time to achieve a prescribed error.

---

## 9. Benchmark Gezerlis juga belum cukup

Untuk Gezerlis-type Hamiltonian, manuscript menyatakan (E_0=16), tetapi tidak menunjukkan:

* bagaimana nilai tersebut diperoleh;
* apakah exact diagonalization, DMC, atau angka dari proyek buku;
* numerical uncertainty;
* parameter dan boundary conditions reference calculation.

Hasil terbaik adalah:

[
16.2554\pm0.0048,
]

sekitar 1.60% di atas 16. 

Ini mungkin cukup baik sebagai proof of concept. Namun tidak cukup untuk membuktikan ERMC kompetitif sebelum dibandingkan dengan:

* VMC memakai ansatz sama;
* VMC dengan ansatz yang lebih natural;
* exact diagonalization;
* diffusion Monte Carlo;
* correlated-sampling VMC.

Bagian Gezerlis bahkan mengatakan bahwa keberhasilannya disebabkan “ground-state distribution of the anharmonic Hamiltonian,” padahal subbagian itu sedang membahas Gezerlis Hamiltonian. 

Itu bukan sekadar typo kecil. Itu menunjukkan interpretasi hasil disalin tanpa pemeriksaan konseptual.

---

## 10. “Slater-type” bukan Slater determinant dan “Jastrow-type” bukan Jastrow factor yang lazim

Trial functions yang ditulis adalah bentuk radial dari norma total konfigurasi. 

Masalahnya:

### Slater-type

Slater-type orbital adalah exponential radial profile. Tetapi untuk many-fermion state, istilah “Slater” biasanya mengacu pada Slater determinant yang menjamin antisymmetry.

Fungsi yang dipakai naskah tidak tampak sebagai determinant dan tidak memiliki exchange antisymmetry.

### Jastrow-type

Jastrow factor many-body yang lazim berbentuk fungsi korelasi pasangan:

[
\exp\left[\sum_{i<j}u(r_{ij})\right].
]

Formula manuscript tampaknya hanya bergantung pada global norm (|q|), bukan pair distances (r_{ij}).

Maka penyebutannya sebagai “Jastrow” dapat menyesatkan pembaca.

### Konsekuensi

* statistik boson/fermion tidak dibahas;
* nodal structure tidak ada;
* sign problem tidak disentuh;
* correlation structure sangat terbatas.

Untuk paper yang dimotivasi oleh exponential many-body Hilbert space, ini kelemahan mendasar.

---

## 11. Klaim many-body tidak diuji secara sungguh-sungguh

Sistem terbesar memakai:

[
N_p=4,\qquad N_d=3,
]

atau hanya 12 coordinate dimensions. 

Tidak ada scaling experiment terhadap:

* jumlah partikel;
* jumlah dimensi;
* jumlah mode;
* parameter circuit;
* memory;
* acceptance rate;
* autocorrelation time;
* optimizer iterations.

Pendahuluan berbicara tentang ledakan dimensi Hilbert space, tetapi Results berhenti pada empat partikel.

> **Naskah memotivasi masalah many-body, lalu menguji sebuah keluarga kecil yang bahkan laptop mahasiswa tidak akan anggap many-body.**

Untuk mengklaim scalability, tampilkan minimal:

[
N_p=1,2,4,8,16,\ldots
]

dengan:

* runtime;
* memory;
* acceptance rate;
* effective sample size;
* energy error;
* number of optimizer parameters.

---

# B. Kelemahan sampling Monte Carlo

## 12. Markov chain tidak mempunyai burn-in

Algorithm 1 menginisialisasi:

[
q_{\rm old}\sim U(-1,1),
]

kemudian langsung menjalankan random-walk proposal. Sampel disimpan setiap (n_m=10) langkah.  

Tidak ada tahap:

* burn-in;
* warm-up;
* equilibration;
* convergence checking.

Lebih buruk lagi, bila loop dimulai dari (i=0), kondisi

```text
if i mod nm == 0
```

dapat menyimpan state setelah proposal pertama—bukan setelah sepuluh langkah penuh.

Kalimat bahwa initial position “is not crucial” karena disusul randomization berikutnya adalah salah.

> **Satu langkah Metropolis tidak membaptis sebuah titik acak menjadi sampel equilibrium.**

Untuk target distribution yang sempit, multimodal, atau high-dimensional, initialization bias dapat bertahan lama.

---

## 13. (n_m=10) tidak otomatis menghilangkan korelasi

Naskah mengatakan interlude sepuluh langkah digunakan “to prevent correlations between two consecutive samples.” 

Tidak ada nilai universal bahwa sepuluh langkah cukup.

Yang harus dihitung:

* autocorrelation function;
* integrated autocorrelation time (\tau_{\rm int});
* effective sample size;

[
N_{\rm eff}\approx
\frac{N_s}{2\tau_{\rm int}};
]

* acceptance rate;
* trace plot;
* Gelman–Rubin diagnostics untuk multiple chains.

Satu juta stored samples tidak berarti satu juta independent samples.

> **Satu juta salinan dari sampel yang saling berkorelasi tetap bukan satu juta informasi independen.**

---

## 14. Standard error yang dilaporkan mengasumsikan sampel independen

Equation 20 menggunakan standard error biasa dari sample variance. Untuk sampel IID, bentuk itu masuk akal. Namun q berasal dari Markov chain.

Naskah sendiri mengakui bahwa bila sampel berkorelasi, effective number of independent samples lebih kecil daripada (N_s). Tetapi setelah mengakui itu, seluruh error bar tetap dihitung menggunakan (N_s) mentah. 

Ini adalah pola yang berulang:

> Manuskrip mengenali lubang di kapal, menuliskan bahwa lubang itu ada, lalu tetap berlayar tanpa menutupnya.

Untuk MCMC, asymptotic variance melibatkan autocovariance sum:

[
\operatorname{Var}(\overline O)
\approx
\frac{\sigma_O^2}{N_s}
\left[
1+2\sum_{k=1}^{\infty}\rho_O(k)
\right].
]

Error bars Figure 1–4 harus dihitung menggunakan (N_{\rm eff}), bukan (N_s).

---

## 15. Tidak ada acceptance-rate tuning

Proposal ditetapkan:

[
q_{\rm new}
===========

q_{\rm old}+0.8,U(-1,1)
]

untuk seluruh sistem. 

Tidak ada laporan:

* acceptance fraction;
* tuning step size;
* dimension-dependent proposal;
* block updates;
* adaptive warm-up;
* multiple walkers.

Dalam random-walk Metropolis, proposal yang mengubah seluruh coordinate vector sekaligus dapat mengalami acceptance collapse ketika dimensi meningkat.

Manuskrip mengatakan MH dipilih karena cocok bagi distribusi kompleks berdimensi tinggi, tetapi tidak pernah membuktikannya. Benchmark terbesar hanya 12 dimensi.

---

## 16. Singularitas pada log-derivative tidak dibahas

Momentum memerlukan:

[
\frac{\nabla\psi}{\psi},
\qquad
\frac{\nabla|\psi|^2}{|\psi|^2}.
]



Di dekat node atau daerah dengan (|\psi|) sangat kecil, kuantitas ini dapat:

* divergen;
* menghasilkan overflow;
* menimbulkan heavy-tailed kinetic-energy estimator;
* memberikan varians tak stabil.

Tidak ada penjelasan tentang:

* log-domain evaluation;
* clipping;
* node handling;
* automatic differentiation precision;
* float32 versus float64;
* outlier rejection;
* finite-variance conditions.

Ini menjadi sangat penting bila metode kelak digunakan untuk fermionic wave functions yang memiliki nodal surfaces.

---

# C. Pseudocode dan reproducibility

## 17. Algorithm 1 mengembalikan variabel yang salah

Algorithm 1 mendeklarasikan output (q_E), tetapi baris terakhir mengembalikan (q), bukan (q_E). 

Mungkin hanya typo. Tetapi ada terlalu banyak “mungkin hanya typo” dalam algoritma inti.

---

## 18. Algorithm 2 tidak konsisten pada input dan output

Header menyebut input (\psi,q), fungsi memakai (\psi,q_E), output ditulis (p), tetapi yang dibangun adalah (p_E). 

Lagi-lagi, pembaca dipaksa menebak niat penulis.

---

## 19. Algorithm 3 secara literal tidak dapat bekerja

Algorithm 3 pada halaman 8 mempunyai beberapa kegagalan sekaligus. 

### Salah signature

Ditulis:

```text
qE ← MH(χ, ψ, N, nm)
```

padahal Algorithm 1 tidak menerima (\chi).

### Salah indeks dalam summation

Penjumlahan menggunakan indeks (j), tetapi observable dievaluasi pada elemen (i):

```text
Σj O(q'Ek,i, p'Ek,i)
```

### Kondisi early stopping tautologis

Ditulis kira-kira:

[
E_{{\rm ER},k}\geq E_{{\rm ER},k}.
]

Setiap bilangan tentu lebih besar atau sama dengan dirinya sendiri. Bila dijalankan literal, kondisi ini selalu benar.

### Indeks yang tidak terdefinisi

Saat mencari minimum dalam window, pseudocode memakai interval:

[
[i-\zeta,i]
]

padahal indeks iterasi optimasi adalah (k), sedangkan (i) merupakan indeks sample loop.

### Salah variabel minimum

Tidak jelas apakah early stopping membandingkan:

* current energy dengan semua energy sebelumnya;
* current energy dengan minimum window;
* moving average;
* validation energy;
* atau patience counter.

> **Algorithm 3 bukan sekadar kurang rapi. Ia saat ini merupakan tempat indeks (i), (j), dan (k) datang untuk kehilangan identitas.**

Untuk sebuah paper metode komputasi, pseudocode yang salah dapat menjadi alasan penolakan langsung.

---

## 20. Optimizer sebenarnya tidak pernah dijelaskan

Table 1 hanya mendefinisikan (\upsilon) sebagai generic optimizer. Sebuah footnote mengatakan update dapat berupa SGD atau Adam. Namun manuscript tidak menyatakan dengan jelas:

* optimizer yang benar-benar digunakan;
* learning rate;
* (\beta_1,\beta_2,\epsilon) bila Adam;
* gradient computation;
* finite difference atau automatic differentiation;
* parameter initialization;
* parameter bounds;
* early-stopping patience (\zeta);
* maximum epoch;
* gradient clipping;
* scheduler;
* random seed.

Figure 3 bahkan menyatakan convergence sensitif terhadap random parameter initialization. 

Namun hanya satu trajectory per (N_s) tampaknya ditampilkan.

> **Sebuah metode optimasi yang tidak menyebut optimizer-nya belum menjadi metode; ia baru menjadi niat baik.**

---

## 21. GitHub aktif belum sama dengan artefak reproducible

Data availability hanya menunjuk repositori GitHub. 

Diperlukan:

* commit hash;
* release tag;
* DOI Zenodo;
* `environment.yml` atau `requirements.lock`;
* Python version;
* CPU/GPU specifications;
* random seeds;
* raw output tables;
* scripts yang membangun seluruh figures;
* unit tests untuk Algorithms 1–3;
* continuous integration.

Kode yang berubah setelah review dapat membuat angka manuscript tidak lagi identik dengan repository.

---

# D. Klaim efisiensi tidak dibuktikan secara adil

## 22. Figure 2 mempunyai accounting waktu yang diakui salah oleh caption-nya sendiri

Caption Figure 2 mengatakan:

* ERMC melakukan sampling sekali dan memakai ulang sampel;
* VMC melakukan sampling terpisah untuk setiap titik;
* runtime ERMC yang diplot **overestimated** karena sampling time dihitung berulang. 

Mengapa hasil yang diketahui salah accounting-nya tetap dijadikan figure utama?

Yang perlu dibandingkan adalah:

### Tugas yang sama

Misalnya scan 51 nilai (\alpha):

[
T_{\rm VMC,total}
=================

\sum_{\alpha}T_{\rm VMC}(\alpha),
]

dan:

[
T_{\rm ERMC,total}
==================

T_{\rm sample}
+
\sum_{\alpha}T_{\rm transform}(\alpha).
]

Bukan meletakkan one-time ERMC sampling cost pada setiap titik lalu menjelaskan kesalahannya dalam caption.

---

## 23. “Speedup” Figure 3 sebagian besar berasal dari runtime VMC yang diekstrapolasi

Caption dan teks mengakui bahwa VMC timing tidak benar-benar dijalankan penuh pada seluruh ukuran sampel. Ia diperkirakan dengan mengalikan average time per iteration dengan jumlah iteration dari nonstochastic optimization. 

Maka Figure 3 bukan measured speedup. Itu **estimated speedup under a chosen extrapolation model**.

Lebih buruk lagi:

* optimizer ERMC stochastic;
* epoch count sangat nonmonotonic;
* random initialization memengaruhi convergence;
* VMC dan ERMC tidak menggunakan prosedur optimasi identik;
* error akhir tidak disamakan.

> **Kata efficient saat ini berdiri di atas stopwatch untuk ERMC dan kalkulator untuk VMC.**

Untuk klaim efisiensi, lakukan benchmark end-to-end:

* hardware sama;
* precision sama;
* initial ansatz sama;
* target energy error sama;
* target confidence sama;
* optimizer effort comparable;
* actual wall-clock;
* repeated seeds;
* median dan quantiles;
* memory peak;
* energy-error-versus-time curve.

---

## 24. Runtime harus dibandingkan pada akurasi yang sama

ERMC memiliki standard error lebih besar pada (N_s) sama. Maka membandingkan runtime pada ukuran sampel sama tidak cukup.

Metrik yang relevan adalah:

[
T(\epsilon)
===========

\text{waktu untuk mencapai RMSE atau confidence interval } \epsilon.
]

Atau efficiency:

[
\mathcal E
==========

\frac{1}
{\operatorname{Var}(\widehat E),T}.
]

Bila ERMC 10 kali lebih cepat tetapi membutuhkan 100 kali lebih banyak sampel untuk varians sama, ERMC sebenarnya lebih buruk.

Manuskrip mengakui trade-off ini secara verbal, tetapi tidak menghitungnya. 

---

## 25. Perbandingan VMC-nya merupakan *straw-man baseline*

VMC baseline selalu melakukan sampling baru per nilai parameter. Padahal baseline terdekat seharusnya mencakup:

1. VMC dengan persistent chains;
2. VMC dengan correlated sampling;
3. VMC dengan reweighting;
4. reparameterized VMC;
5. normalizing-flow VMC;
6. deterministic quadrature untuk benchmark satu dimensi.

Bila ERMC hanya unggul terhadap versi VMC yang sengaja diimplementasikan secara paling naif, kontribusinya tidak cukup kuat untuk jurnal.

---

# E. Kelemahan statistik hasil

## 26. Standard error Monte Carlo bukan uncertainty total

Error bars pada Figures dan Table 2 hanya merepresentasikan sampling standard error.

Mereka tidak mencakup:

* random initialization;
* optimizer convergence;
* local minima;
* hyperparameter sensitivity;
* Markov-chain correlation;
* sample-selection bias;
* model/ansatz error;
* exact-reference uncertainty.

Figure 3 mengakui optimizer trajectory bergantung pada initialization, tetapi tidak ada run-to-run error bars. 

Table 2 melaporkan empat digit desimal seolah nilai-nilai itu terukur dengan luar biasa presisi, sementara systematic errors mencapai 2–10%.

Komputer memang dapat mencetak empat angka di belakang koma. Alam tidak ikut menjadi empat digit lebih pasti karena itu.

---

## 27. Figure 2 memperbesar error bar 100 kali

Caption mengakui error bars ERMC diperbesar faktor 100 untuk visualisasi. 

Ini boleh dilakukan, tetapi figure harus menampilkan:

* actual numerical SE;
* label jelas pada panel;
* inset atau table;
* ratio (\sigma_{\rm ERMC}/\sigma_{\rm VMC}).

Pembaca seharusnya tidak perlu membaca caption panjang untuk mengetahui bahwa skala error bar telah dimanipulasi.

---

## 28. Chebyshev bound tidak sesuai langsung dengan output Markov chain

Equation 25–26 menggunakan variance of IID sample mean. Penulis kemudian mengakui bahwa sampel berkorelasi dapat mempunyai effective number lebih kecil. 

Maka sample-size guarantee seharusnya menggunakan asymptotic MCMC variance atau (N_{\rm eff}), bukan (N_s).

Saat ini bagian “Achieving a Desired Level of Statistical Accuracy” memberi kesan ada jaminan formal, padahal prosedur aktual tidak menghitung besaran yang dibutuhkan jaminan itu.

---

# F. Validitas transformasi quantum dan operator ordering

## 29. “Promise” bukan pengganti pembuktian

Algorithm 3 hanya menyatakan sebagai promise:

> (O(\Gamma(q,p))) at most second order in (p).

Untuk paper metode, penulis harus membuktikan untuk setiap Hamiltonian dan circuit:

[
\hat U^\dagger \hat H\hat U
]

memang direpresentasikan tepat oleh substitusi phase-space yang digunakan.

Ini sangat penting untuk cubic phase gate. Bila:

[
\hat p\mapsto \hat p+\lambda\hat q^2,
]

maka kinetic term menjadi:

[
(\hat p+\lambda\hat q^2)^2
==========================

\hat p^2
+\lambda(\hat p\hat q^2+\hat q^2\hat p)
+\lambda^2\hat q^4.
]

Classical substitution memberi (2\lambda pq^2). Penulis harus menjelaskan operator ordering atau Weyl/symmetric correspondence yang membuat kedua ekspresi ekuivalen di ERPS.

Sekadar menunjuk referensi [27] tidak cukup untuk sebuah implementasi baru.

---

## 30. Kondisi transformasi yang ditulis tidak mencakup beam splitter secara tepat

Naskah menyatakan bentuk yang diperbolehkan:

[
q\mapsto f(q),
\qquad
p\mapsto g(q)+c_0p,
]

dengan (c_0) konstanta. 

Namun beam splitter mencampur beberapa momentum melalui matrix rotation:

[
\mathbf p'!=B\mathbf p.
]

Jadi (c_0) bukan scalar umum, tetapi paling tidak constant matrix.

Ini mungkin mudah diperbaiki menjadi:

[
\mathbf p'
==========

A\mathbf p+\mathbf g(\mathbf q).
]

Namun dalam manuscript teori, pernyataan kondisi yang salah tidak boleh dibiarkan karena kondisi itu merupakan batas validitas keseluruhan metode.

---

## 31. Simbol cubic gate tidak konsisten

Naskah mendefinisikan cubic phase gate sebagai (\hat V), tetapi layer kemudian memakai (\hat\Phi). 

Apakah (\Phi=V), satu produk cubic gates, atau sesuatu berbeda?

Definisikan sekali dan konsisten.

---

# G. Interpretasi hasil dan ansatz

## 32. Penjelasan “mirip Gaussian” terlalu dangkal

Bagian hasil mengatakan Slater-type bekerja baik karena bentuknya “somewhat similar” dengan Gaussian. 

Itu bukan analisis.

Gunakan:

* density overlap;
* fidelity;
* KL divergence;
* covariance;
* radial moment;
* node structure;
* pair-correlation function.

Kalimat visual semacam “somewhat similar” terlalu rendah untuk menjelaskan hasil quantum variational calculation.

---

## 33. Parameter ansatz tidak dilaporkan secara lengkap

Manuskrip mendefinisikan:

* (\alpha);
* (A);
* (n);
* (\zeta);
* (F).

Namun nilai yang digunakan untuk setiap Hamiltonian tidak jelas dalam naskah utama. Tidak jelas pula apakah parameter-parameter base ansatz:

* dioptimalkan;
* ditetapkan;
* dipilih dari literatur;
* atau diambil dari kode.

Karena base density menentukan seluruh sample ensemble, parameter ini bukan detail kecil.

---

## 34. Wave-function reconstruction hanya memperoleh modulus

Bagian rekonstruksi mengatakan (\rho'=|\psi'|^2) hanya menentukan modulus dan wave function diketahui hingga phase. 

Tetapi cubic phase gate justru terutama mengubah phase.

Jadi rekonstruksi tersebut tidak cukup untuk:

* full-state verification;
* phase-sensitive observables;
* interference;
* circuit output validation.

Bagian ini sebaiknya dipersempit menjadi **density reconstruction**, bukan wave-function reconstruction, kecuali phase juga benar-benar direkonstruksi.

---

# H. Masalah Figure dan Table

## Figure 1, halaman 9

Masalah:

* hanya tampak satu realization atau sangat sedikit realization;
* parameter distribusi tidak diberikan;
* error bars tidak membedakan MCMC uncertainty dan optimizer uncertainty;
* mean energy seharusnya analitik-independen dari bentuk (\chi);
* sample-size curve tidak menampilkan bias atau coverage dari repeated trials.

Ganti dengan:

* 50–100 independent runs per (N_s);
* bias;
* RMSE;
* empirical confidence-interval coverage;
* effective sample size;
* variance versus fourth moment distribusi (\xi).

## Figure 2, halaman 12

Panel energi berguna sebagai unit test. Panel waktu tidak layak karena accounting-nya sendiri diakui overestimated.

Tampilkan:

* total runtime seluruh parameter scan;
* one-time sampling cost;
* per-parameter transform cost;
* actual VMC total;
* error-matched comparison.

## Figure 3, halaman 13

Ini figure paling bermasalah.

* speedup merupakan estimasi;
* VMC tidak benar-benar dijalankan end-to-end;
* epoch counts sangat nonmonotonic;
* tidak ada uncertainty dari random initialization;
* tidak ada energy accuracy pada panel yang sama.

Buat plot:

[
\text{absolute energy error versus wall time}
]

untuk setiap metode.

## Figure 4, halaman 14

Semua energy error bars banyak bertumpuk dan penambahan layer tidak memberikan penurunan yang berarti, sementara training time melonjak. 

Ini seharusnya menjadi analisis aljabar redundansi, bukan sekadar observation bahwa “more layers may not help.”

Untuk Gezerlis, waktu pada layer tinggi tampak meningkat sampai puluhan ribu detik tanpa perbaikan energi yang jelas. Ini bukan tanda circuit sedang menjadi canggih. Ini tanda optimizer sedang menghabiskan listrik.

## Table 2, halaman 15

Tambahkan kolom:

| Hamiltonian | Ansatz | Exact | ERMC train | ERMC fresh-test | VMC | Absolute error | Relative error | (N_{\rm eff}) | Time |
| ----------- | ------ | ----: | ---------: | --------------: | --: | -------------: | -------------: | ------------: | ---: |

Saat ini Table 2 mencampur Monte Carlo precision dengan variational accuracy.

---

# I. Masalah editorial dan tipografi

Beberapa masalah yang harus diperbaiki:

1. `ans¨atze`, `Schr¨odinger`, dan berbagai glyph terlihat rusak.
2. Placeholder template `vv (yyyy) aaaaaa` dan `dd Month yyyy` masih ada.
3. Algorithm 1, 2, dan 3 mempunyai input/output yang tidak konsisten.
4. `Table. 1` dan `Table. 2` memakai titik yang tidak perlu.
5. `SlaterType`, `Slater-type`, dan “SlaterType wavefunction” tidak konsisten.
6. “ground state energy of the this Hamiltonian” salah grammar.
7. Bagian Gezerlis menyebut ground-state distribution “of the anharmonic Hamiltonian.”
8. (E_{\rm ER}) dipakai sekaligus sebagai mean estimate, energy dengan error bar, dan objective optimasi.
9. (\delta) pada Table 1 didefinisikan secara membingungkan, padahal dalam Eq. 26 ia adalah failure probability.
10. Figure axes untuk (\hbar\omega_0) tampak kurang terbaca atau mengalami masalah glyph.
11. Binomial/Gaussian/Exponential dan singkatan lain pada Figure 1 tidak dijelaskan lengkap.
12. Formula dan pseudocode perlu diperiksa langsung terhadap source code, baris demi baris.

Naskah ini terlihat rapi dari jarak dua meter. Pada jarak membaca persamaan, baut-bautnya mulai jatuh.

---

# Analisis minimum sebelum resubmission

## 1. Perbaiki fondasi matematis

* Turunkan estimator ERMC secara bersih.
* Jelaskan operator ordering.
* Buktikan admissibility untuk setiap gate dan Hamiltonian.
* Generalisasi (c_0) menjadi matrix bila diperlukan.
* Pisahkan (\widehat E) dari standard error.
* Perbaiki seluruh pseudocode dan unit-test terhadap implementasi.

## 2. Integrasikan (\xi) secara analitik

Bandingkan:

1. stochastic-(\xi) ERMC;
2. antithetic-(\xi) ERMC;
3. Rao–Blackwellized ERMC.

Ini berpotensi menjadi kontribusi metode yang benar-benar baru dan berguna.

## 3. Gunakan prosedur train–validation–test

* Optimize pada ensemble A.
* Early stop pada ensemble B.
* Laporkan final energy pada ensemble C.
* Ulangi pada minimal 20–50 seeds.

## 4. Validasi MCMC

Untuk setiap ansatz dan sistem:

* burn-in;
* acceptance rate;
* trace plots;
* autocorrelation;
* integrated autocorrelation time;
* (N_{\rm eff});
* multiple chains;
* convergence diagnostics.

## 5. Lakukan benchmark yang fair

Bandingkan ERMC dengan:

* naive VMC;
* persistent-chain VMC;
* correlated-sampling VMC;
* reweighted VMC;
* flow/reparameterized VMC;
* exact calculation bila tersedia.

Gunakan target accuracy sama.

## 6. Uji scaling

Variasikan:

* (N_p);
* (N_d);
* (N_s);
* layer count;
* number of parameters.

Laporkan:

* runtime;
* memory;
* ESS;
* error;
* convergence probability.

## 7. Uji expressivity

* Buktikan bentuk tertutup (q'=Aq+d).
* Tentukan apakah multi-layer circuit dapat dikompresi.
* Tambahkan nonlinear (q)-transformation yang masih admissible, bila mungkin.
* Bandingkan density dan wave-function overlap terhadap exact ground state.

## 8. Perbaiki ansatz

* Gunakan actual Slater determinant untuk fermion;
* actual pairwise Jastrow;
* correlated Gaussian;
* neural or normalizing-flow ansatz sebagai pembanding;
* laporkan semua parameter.

## 9. Bekukan reproduksi

* Zenodo DOI;
* exact commit;
* environment lock;
* seeds;
* raw result tables;
* automated test;
* one-command reproduction.

---

# Kesimpulan yang masih dapat dipertahankan

Dengan data saat ini, klaim yang defensible adalah:

> ERPS sampling combined with restricted parameterized phase-space transformations can reproduce a simple Gaussian squeezing change-of-variables test and yield approximate variational energies for several low-dimensional benchmark Hamiltonians. Reusing a common phase-space ensemble may amortize sampling costs over parameter scans, although the present implementation has larger sampling variance, limited transformation expressivity, and has not yet been benchmarked fairly against modern sample-reuse VMC methods.

Yang belum dapat dipertahankan:

> ERMC adalah metode Monte Carlo yang efisien untuk simulasi Hamiltonian continuous-variable secara umum, memberikan speedup besar terhadap VMC, dan menyediakan framework yang telah tervalidasi untuk broader CV quantum-circuit simulation.

---

# Pertanyaan ujian untuk Santana

1. **Apa perbedaan antara Hamiltonian simulation dan variational ground-state energy estimation?**

2. **Mengapa energi hasil optimasi pada ensemble yang sama dapat bias ke bawah meskipun estimator untuk parameter tetap tidak bias?**

3. **Mengapa variational energy pada Table 2 dapat berada di bawah exact ground-state energy?**

4. **Turunkan bahwa untuk (p=a+\xi b) dan observable kuadratik dalam (p), mean energy hanya bergantung pada (\mathbb E[\xi]) dan (\mathbb E[\xi^2]).**

5. **Bila dua momen (\xi) sudah diketahui, mengapa (\xi) masih perlu disampling?**

6. **Apa keuntungan Rao–Blackwellization dalam kasus ini?**

7. **Buktikan bahwa dengan gate yang digunakan, transformasi posisi setelah sembarang jumlah layer tetap berbentuk (q'=Aq+d).**

8. **Bila demikian, apa expressivity tambahan dari layer kedua sampai kesepuluh?**

9. **Mengapa thinning setiap sepuluh langkah tidak menjamin sampel independen?**

10. **Bagaimana menghitung integrated autocorrelation time dan effective sample size?**

11. **Apa acceptance rate Markov chain Anda untuk masing-masing Hamiltonian dan ukuran sistem?**

12. **Mengapa tidak ada burn-in pada Algorithm 1?**

13. **Apa kesalahan pada kondisi early stopping Algorithm 3?**

14. **Mengapa summation menggunakan (j), tetapi observable memakai indeks (i)?**

15. **Optimizer apa yang sebenarnya digunakan dan bagaimana gradient dihitung?**

16. **Apa perbedaan ERMC dengan correlated-sampling VMC?**

17. **Mengapa Figure 3 memakai VMC runtime hasil extrapolation, bukan actual wall-clock?**

18. **Bagaimana Anda membandingkan dua metode yang mempunyai variance estimator berbeda?**

19. **Mengapa fungsi yang disebut Slater-type bukan Slater determinant?**

20. **Di mana pairwise correlation pada fungsi yang disebut Jastrow-type?**

21. **Bagaimana operator ordering ditangani setelah cubic phase transformation?**

22. **Dari mana exact energy (E_0=16) untuk Gezerlis Hamiltonian diperoleh dan berapa ketidakpastiannya?**

23. **Mengapa error 7.9% pada anharmonic oscillator disebut “worked well”?**

24. **Apa hasil ERMC bila final energy dievaluasi pada fresh independent ensemble?**

25. **Apa kontribusi ilmiah yang tetap tersisa bila correlated-sampling VMC menghasilkan akurasi dan waktu yang sama?**

Bila mahasiswa dapat menjawab pertanyaan-pertanyaan ini dengan derivasi dan eksperimen, bukan sekadar menunjuk kode Python, berarti ia benar-benar menguasai pekerjaannya.

---

# Contoh komentar ringkas kepada editor

> **Recommendation: Reject in present form.** The manuscript presents an intellectually interesting application of the epistemically restricted phase-space representation to variational energy estimation, but its central claims of efficiency and generality are not yet demonstrated. The optimization and final energy evaluation appear to use the same fixed Monte Carlo ensemble, introducing adaptive selection bias and undermining the variational interpretation. The Metropolis–Hastings procedure has no documented burn-in, acceptance-rate analysis, autocorrelation correction, or effective-sample-size estimate, while the reported standard errors assume independent samples. The auxiliary random variable is sampled even though, for observables at most quadratic in momentum, its contribution to the mean can be integrated analytically from its known first two moments. The restricted gate set leaves the position transformation affine under arbitrary layer composition, substantially limiting expressivity and likely explaining why deeper circuits do not improve the energy. The VMC speedup is based on an unfair baseline and partly extrapolated rather than measured timing. Several benchmark and pseudocode inconsistencies—including a tautological early-stopping condition and incorrect indices—also prevent reproduction from the manuscript. A new numerical and statistical study is required.

# Putusan akhir

## **Untuk karya S1: sangat ambisius dan berpotensi kuat.**

Santana telah berani memasuki persoalan yang jauh di atas rata-rata skripsi sarjana. Ada pemahaman awal yang baik tentang:

* Monte Carlo;
* phase-space representation;
* variational principles;
* continuous-variable gates;
* computational implementation.

Itu patut diapresiasi.

## **Untuk artikel Quantum Science and Technology: belum layak submit.**

Manuskrip saat ini belum membuktikan bahwa ERMC:

* lebih efisien pada akurasi sama;
* bebas bias akibat reuse ensemble;
* mempunyai uncertainty yang benar;
* scalable;
* lebih baik daripada correlated-sampling VMC;
* cukup ekspresif untuk nontrivial ground states;
* atau dapat direproduksi dari algoritma yang dicetak.

Jangan dahulu memoles Abstract atau menambah adjective seperti *efficient*, *broader*, dan *reproducible*.

> **Perbaiki estimatornya. Validasi Markov chain-nya. Gunakan independent test ensemble. Hadapkan ERMC kepada lawan VMC yang tidak sengaja dibuat bodoh.**

Setelah itu, baru naskah ini berhak membicarakan efisiensi.
