# EHZ UGM 2023: potongan event dan IAS-Capon

Analisis ulang **EHZ saja**, 26 Oktober 2026. Hasil ini terpisah dari eksperimen beamforming dan XGBoost lama di folder induk.

**40 kandidat dipotong dan diplot; 17 masuk daftar utama (9 VTB dan 8 TECT).** Daftar utama adalah hasil seleksi operasional waveform/beam, bukan jumlah sumber gempa yang sudah terkonfirmasi. Seluruh 40 hasil tetap disimpan agar keputusan seleksinya dapat diaudit.

## Mulai memeriksa gambar

- **[Galeri 17 kandidat utama](selected-gallery.md)** — time series lima EHZ, beam MVDR, spectrogram beam, dan peta slowness.
- [Galeri 23 kandidat yang perlu review](review-gallery.md).
- Galeri per label katalog: [VTB](gallery-VTB.md), [TECT](gallery-TECT.md), [MP](gallery-MP.md), [ROCKFALL](gallery-ROCKFALL.md).
- [Tabel kandidat utama](selected-events.csv), [tabel seluruh hasil dan alasan seleksi](event-summary.csv).

Contoh VTB yang jelas pada kelima stasiun dan mengarah ke utara:

![Contoh VTB](figures/20230824T130113_VTB_row49485.png)

## Hasil seleksi

| Kelas katalog | Dipotong dan diplot | Kandidat utama | Perlu review |
|---|---:|---:|---:|
| MP | 4 | 0 | 4 |
| ROCKFALL | 11 | 0 | 11 |
| TECT | 8 | 8 | 0 |
| VTB | 17 | 9 | 8 |
| **Total** | **40** | **17** | **23** |

Semua 40 potongan yang diperluas lolos pemeriksaan kesinambungan sampel dan kesehatan teknis dasar. Kegagalan seleksi beam **tidak otomatis berarti noise**: arah di luar sektor utara, SNR beam rendah, atau sensitivitas diagonal loading perlu ditinjau. Label MP/ROCKFALL dalam galeri tetap label katalog, bukan konfirmasi bahwa transien yang terlihat berasal dari event tersebut.

Satu TECT mempunyai flag arah kurang teresolusi dekat slowness nol; waveform-nya tetap masuk daftar utama karena TECT tidak diberi batas arah. Estimasi BAZ pada small-aperture array ini tidak boleh dianggap presisi lokasi sumber.

## Data dan pemilihan kandidat

- Array: RE5DE, R6940, R265F, R7D17, R0279; channel AM.*.00.EHZ, 100 Hz.
- Cakupan induk mengikuti tanggal arsip UTC: 16 Agustus–12 September, 27 Oktober, 30 Oktober 2023. File harian pada tanggal tersebut tidak selalu kontinu.
- Penyaringan sebelumnya memeriksa 9.423 kandidat katalog. Dari 42 yang menunjukkan transien EHZ pada kelima stasiun, dua mempunyai asosiasi waktu ambigu; 40 sisanya menjadi input tahap ini. Ini **bukan pencarian detektor baru pada seluruh tahun 2023**.
- [Kandidat input dan pemeriksaan visual sebelumnya](data/candidates.csv), [metrik QC EHZ kandidat](data/candidate-qc.jsonl), [hasil screen EHZ populasi induk](data/initial-EHZ-screen.csv), [baris katalog terpilih](data/catalog-selected.csv).
- Waktu katalog dibaca sebagai WIB, lalu dikonversi ke UTC. Asumsi ini konsisten dengan README induk dan dua gempa regional dengan waktu resmi. Kolom `eventdate_microsecond` diasumsikan perseratus detik (0–99), bukan metadata zona waktu/subdetik yang terverifikasi.
- Identitas `rowNNNNN` adalah nomor baris CSV asli, termasuk header; SHA-256 katalog sumber ada di [provenance](metadata/provenance.json).

## Pemotongan waveform

Setiap potongan mulai 60 detik sebelum waktu katalog. Akhirnya paling sedikit 180 detik setelah waktu katalog, atau `duration+120 s`, atau puncak EHZ+120 s, mana yang lebih panjang. Dua TECT dengan coda panjang diperluas hingga +600 s; nilai ini tercatat pada CSV input. Potongan menyertakan baseline dan coda, dan **bisa memuat event katalog lain**; daftar tetangga waktunya ada pada masing-masing JSON metadata.

Data dibaca ulang dari MiniSEED asli. Gap atau overlap dengan nilai sampel bertentangan menyebabkan penolakan; tidak ada zero fill atau interpolasi melintasi gap. Pemeriksaan tambahan menolak plateau nilai mentah ≥0,2 s dan nilai dekat rail ADC 24-bit yang diasumsikan. Pemeriksaan ini bukan sertifikasi menyeluruh kondisi perangkat.

File `*_EHZ_RAW.mseed` mempertahankan 100 Hz dan waktu sampel asli masing-masing stasiun. Produk 25 Hz adalah hasil demean, zero-phase Butterworth orde 4 pada 0,5–10 Hz, anti-alias polyphase resampling, lalu interpolasi dalam trace kontinu ke grid bersama. Filtering memakai konteks asli di luar tepi potongan. Respons instrumen tidak dihilangkan; unit mentah adalah counts.

## Implementasi algoritma Gal

Rujukan: [mgalcode/IAS-Capon](https://github.com/mgalcode/IAS-Capon), fungsi [IAS_Capon pada commit f929041](https://github.com/mgalcode/IAS-Capon/blob/f9290415279a6cc372d4fc0d9eafa2d9bf4c0352/subroutines.py), serta Gal et al. (2014), [doi:10.1093/gji/ggu183](https://doi.org/10.1093/gji/ggu183).

Kode asli membutuhkan Python 2 dan `scipy.weave`. Analisis ini memakai **padanan NumPy dari prosedur numeriknya**, bukan menjalankan kode asli tanpa perubahan. Tidak ada kode IAS-Capon upstream yang disalin utuh ke repo ini.

1. Geometri WGS84 diubah menjadi east/north dalam km, direferensikan ke pusat array. Upstream memakai derajat; slowness di sini s/km.
2. Spektrum silang dibentuk per bin frekuensi dari subwindow Hann 4 s, overlap 50%, demean per subwindow. Window fit 32 s berada di sekitar puncak transien EHZ hasil QC, dengan 14–15 snapshot (>5 sensor).
3. CSD di-whiten per stasiun/per frekuensi, lalu diberi diagonal loading `dl * trace(C) / nsamp`, sesuai urutan IAS-Capon asli.
4. Grid east/north masing-masing −3 hingga +3 s/km, langkah 0,05 s/km. Peta adalah **penjumlahan tak koheren** spektrum Capon per frekuensi 1–8 Hz, masing-masing memakai steering vector pada frekuensinya sendiri.
5. `dl=1` adalah hasil utama; `dl=10` dan `100` diperiksa sebagai sensitivitas. Pergeseran slowness >0,25 s/km diberi flag.
6. Output asli IAS-Capon adalah **spektrum arah/slowness**, bukan waveform. Karena itu trace yang ditampilkan merupakan **ekstensi MVDR berarah tetap yang ditentukan oleh puncak IAS-Capon**. Kovarians counts tanpa whitening frekuensi digunakan untuk bobot rekonstruksi; gain steering diuji sama dengan satu. Bobot tetap diterapkan lewat STFT/ISTFT 4 s, overlap 50%. Beam delay-sum pada arah yang sama disediakan sebagai pembanding.

MVDR tidak selalu meningkatkan SNR dibanding delay-sum, khususnya jika model gelombang bidang atau respons antarstasiun tidak sesuai. Kedua SNR disimpan; hasil yang menurun tidak disembunyikan.

## Aturan daftar utama

- SNR RMS beam MVDR ≥3, dihitung pada jendela `[0, max(duration, peak+15 s)]` relatif terhadap RMS noise `[−50,−10 s]`. Ini berbeda dari SNR puncak 3 s pada penyaringan awal.
- Tidak ada flag tepi grid, sensitivitas loading, atau aktivitas kuat tersisa pada akhir potongan. Diagnostik akhir potongan memakai median envelope RMS 1 s antarstasiun / RMS noise; median 20 s terakhir harus ≤2. Ini tidak membuktikan semua coda fisik telah selesai.
- Untuk VTB/MP/ROCKFALL, BAZ berada di 350°–10° mengikuti aturan seleksi utara pada README induk. Ini adalah prior arah, bukan bukti tunggal sumber Merapi. TECT tidak dibatasi arah.
- Flag BAZ dekat slowness nol tetap ditampilkan untuk TECT, tetapi tidak dipakai menolak waveform TECT yang jelas.

Pita yang dipakai dan ambang QC membatasi hasil: sinyal lemah atau di luar pita dapat terlewat. LF tidak ditambahkan ke tahap ini karena 39 kandidat LF tidak lolos screening sebelumnya, termasuk pemeriksaan tambahan 0,1–2 Hz. Tidak ada analisis HDF dalam produk ini. Keputusan di sini tidak boleh dipakai sebagai ground truth otomatis untuk training tanpa review sumber dan event yang bertumpang tindih.

## Cara membaca gambar

Panel pertama memperlihatkan lima EHZ pada grid waktu bersama; amplitudo tiap stasiun diskalakan untuk perbandingan bentuk. Panel kedua membandingkan MVDR dan delay-sum, masing-masing dibagi RMS noise beam-nya. Panel ketiga adalah spectrogram **trace MVDR**, bukan spectrogram satu stasiun; PSD ditampilkan relatif terhadap maksimum pada potongan yang sama (−60 hingga 0 dB), sehingga warna antar-event tidak membandingkan energi absolut. Panel terakhir berisi peta IAS-Capon dan parameter fit. Garis merah menandai waktu katalog dan arsiran menandai durasi katalog.

## File dan reproduksi

- `waveforms/`: 40 potongan lima-stasiun 100 Hz asli dan 40 produk proses 25 Hz.
- `beam_products/`: 40 MiniSEED berisi trace `MVDR` dan `DAS`, serta 40 peta scan `.npz`.
- `figures/`: 40 PNG time series, spectrogram, dan peta IAS-Capon.
- `metadata/`: parameter per event, sensitivitas loading, flag, tetangga katalog, dan provenance.
- [Hasil pengujian numerik](validation.json), [hasil pemeriksaan produk](artifact-validation.json), [checksum produk](SHA256SUMS.txt).
- [Kode pemrosesan](scripts/analyze_events.py), [implementasi IAS-Capon NumPy](scripts/ias_capon_numpy.py), [pengujian](scripts/test_ias_capon.py).

Dari folder ini, setelah dependensi NumPy, SciPy, ObsPy dan Matplotlib tersedia:

```bash
python scripts/test_ias_capon.py
python scripts/analyze_events.py --archive /path/to/AM --candidates data/candidates.csv --qc-metrics data/candidate-qc.jsonl
python scripts/build_report.py
```

Reproduksi memerlukan arsip harian asli; repo ini menyertakan potongan event, bukan seluruh rekaman harian. Versi lingkungan ada di `metadata/environment.json`. Peta sensitivitas dan waveform adalah hasil analisis kandidat, bukan sertifikat lokasi/jenis sumber.
