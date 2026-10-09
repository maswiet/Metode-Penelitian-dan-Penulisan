# Pengantar Seismologi — Waluyo, Ade Anggraini, Wiwit Suryanto

Buku ajar *Pengantar Seismologi: Teori, Instrumentasi, dan Penerapannya di
Indonesia*, disusun dari naskah kuliah almarhum **Waluyo** (Laboratorium
Geofisika, Departemen Fisika FMIPA UGM) yang disunting, dilengkapi, dan
dimutakhirkan.

**Keluaran:** [`Pengantar-Seismologi.docx`](Pengantar-Seismologi.docx) —
satu berkas Word siap cetak, ukuran B5 (176 × 250 mm), ± 212 halaman,
14 bab + 4 lampiran, 56 gambar, 22 tabel, dan daftar pustaka.

## Isi

| Bagian | Bab |
|:--|:--|
| I — Dasar seismologi | 1 Sejarah dan wawasan · 2 Instrumentasi dan jaringan · 3 Gelombang seismik · 4 Parameter sumber · 5 Mekanisme sumber |
| II — Bumi dan Indonesia | 6 Struktur bumi dari data seismik · 7 Seismotektonik Indonesia · 8 Statistik kegempaan |
| III — Seismologi terapan | 9 Gerakan tanah kuat dan efek situs · 10 Bahaya dan risiko gempa · 11 Tsunami dan peringatan dini · 12 Seismologi gunung api · 13 Pengolahan data modern |
| IV — Studi kasus | 14 Gempa Yogyakarta 27 Mei 2006 · Lampiran A–D · Daftar pustaka |

Bab 1–5 adalah naskah asli Waluyo yang dipertahankan struktur dan gaya
penuturannya; Bab 6–14 dan lampiran adalah tambahan penyunting. Seluruh
koreksi substantif terhadap naskah asli dicatat pada **Lampiran D** dan
ditandai di dalam teks sebagai kotak *Catatan Pemutakhiran*.

## Susunan berkas

```
arsip/           naskah asli Waluyo (.doc, Word 97) — jangan diubah
src/*.md         naskah buku (Markdown; satu berkas per bab)
figs/*.png       56 gambar, 300 dpi, dihasilkan skrip
data/            data peta Bab 7 (lihat data/README.md)
build/
  gaya.py            gaya bersama untuk semua gambar
  figs_bab1_3.py     pembangkit gambar Bab 1–3
  figs_bab4_14.py    pembangkit gambar Bab 4–14
  figs_peta.py       pembangkit peta Bab 7 (Gambar 7.1 dan 7.2)
  peta.py            pemuat data peta dan latar bayangan relief
  wkb.py             pembaca geometri GeoPackage (tanpa pustaka GIS)
  siapkan_data.py    penyiap data sesar, relief, dan garis pantai
  siapkan_lempeng.py penyiap data batas lempeng Bird (2003)
  periksa_gambar.py  pemeriksa tata letak teks pada seluruh gambar
  buat_reference.py  pembuat templat Word (B5, gaya, header, footer)
  build.py           perakit: Markdown -> .docx
  pasca.py           penyuntingan akhir .docx
Pengantar-Seismologi.docx   hasil akhir
```

## Membangun ulang

Prasyarat: `pandoc`, Python 3 dengan `matplotlib`, `numpy`, `obspy`,
`python-docx`, dan `pillow`.

```bash
cd build
python3 figs_bab1_3.py        # gambar Bab 1-3
python3 figs_bab4_14.py       # gambar Bab 4-14
python3 figs_peta.py          # peta Bab 7
python3 periksa_gambar.py     # (opsional) periksa tata letak teks
python3 buat_reference.py     # templat Word
python3 build.py              # rakit .docx
python3 pasca.py              # penyuntingan akhir
```

Untuk pratayang PDF (opsional):

```bash
soffice --headless --convert-to pdf --outdir build ../Pengantar-Seismologi.docx
```

## Catatan bagi penyunting akhir

1. **Daftar isi.** Berkas memuat *field* daftar isi Word. Buka di Microsoft
   Word, tekan `Ctrl+A` lalu `F9`, pilih "perbarui seluruh daftar", agar judul
   bab dan nomor halamannya muncul. Daftar Gambar dan Daftar Tabel sudah
   terisi (tanpa nomor halaman).
2. **Isian yang perlu dilengkapi.** Halaman katalog memuat penanda
   *(diisi penerbit)*, *(diisi bulan dan tahun)*, dan *(diisi nomor ISBN)*;
   halaman In Memoriam dan Prakata memuat *(bulan tahun)*.
3. **Persamaan.** Semua persamaan berupa objek persamaan Word (OMML) yang
   dapat disunting langsung. Nomor persamaan diletakkan di ujung kanan
   persamaan dengan spasi tetap.
4. **Gambar.** Semua gambar dibuat ulang dari nol karena gambar pada naskah
   asli berupa objek gambar Word yang tidak dapat diekstrak. Gambar berlabel
   "sketsa skematis" sengaja tidak berskala peta dan tidak boleh dipakai untuk
   kerja kuantitatif.
5. **Peta Bab 7.** Gambar 7.1 dan 7.2 dibuat dari data, bukan sketsa:
   basis data 401 sumber sesar aktif PuSGeN 2024, model batas lempeng
   Bird (2003), dan bayangan relief Natural Earth. Arah gerigi subduksi
   ditentukan dari data (sisi yang lebih cerah pada bayangan relief, yaitu
   sisi busur), dan anak panah konvergensi dihitung dari komponen konvergen
   serta komponen menganan model Bird sehingga tidak bergantung pada kerangka
   acuan. Satu nilai pada basis data PuSGeN dibetulkan: $M_\text{maks}$
   segmen Salak (JAV18) tercantum 65,0 dan dibaca 6,5 — lihat Catatan
   Pemutakhiran 7.1.
6. **Izin yang perlu dipastikan sebelum cetak.** Gambar 6.1 **digambar
   ulang** (bukan disalin) dan disederhanakan menjadi hitam-putih dari
   Gambar 5.10 Lühr, Koulakov & Suryanto (2023), bab dalam buku *Merapi
   Volcano* terbitan Springer. Salah seorang penulis bab itu adalah penulis
   buku ini, tetapi hak cipta bab ada pada penerbit. Walaupun gambar ini
   karya turunan yang digambar dari nol dan bukan reproduksi, sebaiknya
   status izinnya dipastikan kepada Springer dan kepada kedua penulis lain
   sebelum naskah dikunci. Jika reproduksi gambar aslinya yang berwarna
   lebih disukai, izin formal Springer wajib diperoleh terlebih dahulu.
7. **Data yang perlu diperiksa sebelum cetak.** Angka kelembagaan yang
   berubah dari waktu ke waktu — jumlah sensor BMKG, versi SNI 1726 yang
   berlaku, dan rincian skala SIG-BMKG — sebaiknya dipastikan kembali ke
   sumber resmi terbaru pada saat naskah dikunci.
8. **Gambar 5.10** dihitung langsung dari himpunan data Tabel 5.1 (bahan ajar
   asli Waluyo) melalui pencarian sistematis atas strike, dip, dan rake;
   penyelesaian terbaik mencocokkan 45 dari 49 polaritas.
