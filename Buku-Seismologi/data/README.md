# Data peta Bab 7

Berkas di dalam direktori ini dipakai oleh `build/figs_peta.py` untuk membuat
Gambar 7.1 dan Gambar 7.2. Semuanya adalah **turunan** yang sudah dipotong ke
jendela Indonesia (bujur 91°–143° BT, lintang 14° LS–17° LU) agar ringan
disimpan bersama naskah.

| Berkas | Isi | Sumber |
|:--|:--|:--|
| `pusgen2024-sesar.csv` | 401 jalur sumber sesar aktif beserta jenis, panjang, lebar, kemiringan, laju geser, dan $M_\text{maks}$ | PuSGeN 2024 |
| `bird2003-batas.csv` | 518 ruas batas lempeng: kelas, laju gerak relatif, komponen konvergen dan menganan | Bird (2003), PB2002 |
| `bird2003-lempeng.csv` | poligon lempeng (untuk penamaan) | Bird (2003), PB2002 |
| `relief-indonesia.png` | bayangan relief 1 menit busur, 3120 × 1860 piksel | Natural Earth `GRAY_HR_SR_OB` |
| `relief-indonesia.json` | batas geografis dan ukuran piksel berkas di atas | — |
| `garis-pantai.csv` | 521 bagian garis pantai | Natural Earth `ne_10m_coastline` |
| `sumber-pusgen2024/` | berkas asli PuSGeN 2024 seperti diterima | PuSGeN 2024 |

Data Natural Earth berada pada domain publik. Data PuSGeN dan Bird (2003)
tunduk pada ketentuan sitasi penyedianya masing-masing; keduanya dicantumkan
pada Daftar Pustaka.

## Membangun ulang berkas turunan

`build/siapkan_data.py` dan `build/siapkan_lempeng.py` menghasilkan berkas
turunan di atas. Keduanya memerlukan berkas mentah yang tidak disimpan di
sini karena besarnya:

- `GRAY_HR_SR_OB.tif` dan `ne_10m_coastline.shp` dari Natural Earth
  (`naturalearth.s3.amazonaws.com`);
- `PB2002_steps.json` dan `PB2002_plates.json` (model batas lempeng Bird 2003
  dalam bentuk GeoJSON).

`build/wkb.py` adalah pembaca geometri GeoPackage (header GPKG + WKB) yang
ditulis sendiri, sehingga berkas `.gpkg` PuSGeN dapat dibaca tanpa memerlukan
pustaka GIS.
