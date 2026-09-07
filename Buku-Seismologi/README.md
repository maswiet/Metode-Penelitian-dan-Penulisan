# Pengantar Seismologi — Waluyo, Ade Anggraini, Wiwit Suryanto

Buku ajar *Pengantar Seismologi: Teori, Instrumentasi, dan Penerapannya di
Indonesia*, disusun dari naskah kuliah almarhum **Waluyo** (Laboratorium
Geofisika, Departemen Fisika FMIPA UGM) yang disunting, dilengkapi, dan
dimutakhirkan.

**Keluaran:** [`Pengantar-Seismologi.docx`](Pengantar-Seismologi.docx) —
satu berkas Word siap cetak, ukuran B5 (176 × 250 mm), ± 200 halaman,
14 bab + 4 lampiran, 55 gambar, 22 tabel, dan daftar pustaka.

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
figs/*.png       55 gambar, 300 dpi, dihasilkan skrip
build/
  gaya.py            gaya bersama untuk semua gambar
  figs_bab1_3.py     pembangkit gambar Bab 1–3
  figs_bab4_14.py    pembangkit gambar Bab 4–14
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
5. **Data yang perlu diperiksa sebelum cetak.** Angka kelembagaan yang
   berubah dari waktu ke waktu — jumlah sensor BMKG, versi SNI 1726 yang
   berlaku, dan rincian skala SIG-BMKG — sebaiknya dipastikan kembali ke
   sumber resmi terbaru pada saat naskah dikunci.
6. **Gambar 5.10** dihitung langsung dari himpunan data Tabel 5.1 (bahan ajar
   asli Waluyo) melalui pencarian sistematis atas strike, dip, dan rake;
   penyelesaian terbaik mencocokkan 45 dari 49 polaritas.
