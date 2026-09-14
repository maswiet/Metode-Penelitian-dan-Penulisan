"""Pemeriksa tata letak gambar: mencari teks yang bertumpuk, teks yang
tertindih garis/kurva, dan teks yang keluar dari bidang gambar.

Cara kerja: setiap fungsi gambar dijalankan, lalu sebelum berkas disimpan
figure-nya dicegat. Kotak batas seluruh objek teks dihitung dalam satuan
piksel, kemudian
  (1) dibandingkan satu sama lain untuk mencari pertampalan;
  (2) gambar dirender ulang tanpa teks, dan kerapatan tinta di dalam setiap
      kotak teks dihitung -- kerapatan tinggi berarti teks menumpang di atas
      garis, kurva, atau arsiran;
  (3) kotak teks dibandingkan dengan batas bidang gambar.
"""
import io
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import gaya

AMBANG_TINTA = 0.055        # fraksi piksel bertinta yang dianggap tertindih
AMBANG_TUMPANG = 0.14       # fraksi luas kotak teks yang bertampalan
tertangkap = []


def _kumpulkan_teks(fig):
    out = []
    for ax in fig.get_axes():
        for t in ax.texts:
            out.append((t, ax))
        for lab in (ax.title, ax.xaxis.label, ax.yaxis.label):
            out.append((lab, ax))
        leg = ax.get_legend()
        if leg is not None:
            for t in leg.get_texts():
                out.append((t, ax))
        for t in ax.get_xticklabels() + ax.get_yticklabels():
            out.append((t, ax))
    for t in fig.texts:
        out.append((t, None))
    return [(t, ax) for t, ax in out if t.get_text().strip()
            and t.get_visible()]


def _raster(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100)
    buf.seek(0)
    import matplotlib.image as mpimg
    return mpimg.imread(buf)


def _luas(b):
    return max(b[2] - b[0], 0) * max(b[3] - b[1], 0)


def _potong(b1, b2):
    x0 = max(b1[0], b2[0]); x1 = min(b1[2], b2[2])
    y0 = max(b1[1], b2[1]); y1 = min(b1[3], b2[3])
    return _luas((x0, y0, x1, y1))


def periksa(fig, nama):
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    daftar = _kumpulkan_teks(fig)
    kotak = []
    for t, ax in daftar:
        try:
            bb = t.get_window_extent(renderer=rend)
        except Exception:
            continue
        if bb.width <= 0 or bb.height <= 0:
            continue
        kotak.append(((bb.x0, bb.y0, bb.x1, bb.y1), t, ax))

    masalah = []

    # (1) teks bertumpuk dengan teks lain
    for i in range(len(kotak)):
        for j in range(i + 1, len(kotak)):
            b1, t1, _ = kotak[i]
            b2, t2, _ = kotak[j]
            p = _potong(b1, b2)
            if p <= 0:
                continue
            frac = p / min(_luas(b1), _luas(b2))
            if frac > AMBANG_TUMPANG:
                masalah.append(
                    f"teks bertumpuk {frac:5.0%}: "
                    f"{t1.get_text()[:34]!r} x {t2.get_text()[:34]!r}")

    # (2) teks menumpang di atas garis atau arsiran
    tersembunyi = []
    for _, t, _ in kotak:
        if t.get_visible():
            tersembunyi.append(t)
            t.set_visible(False)
    arr = _raster(fig)
    for t in tersembunyi:
        t.set_visible(True)
    tinggi_px = arr.shape[0]
    skala = arr.shape[1] / (fig.get_size_inches()[0] * fig.dpi)
    abu = arr[..., :3].mean(axis=2)
    for b, t, ax in kotak:
        if ax is None or t in (ax.title, ax.xaxis.label, ax.yaxis.label):
            continue
        if t in ax.get_xticklabels() + ax.get_yticklabels():
            continue
        x0, y0, x1, y1 = [v * skala for v in b]
        # koordinat piksel gambar: y dari atas
        px0, px1 = int(max(x0, 0)), int(min(x1, arr.shape[1]))
        py0, py1 = int(max(tinggi_px - y1, 0)), int(min(tinggi_px - y0,
                                                       tinggi_px))
        if px1 - px0 < 3 or py1 - py0 < 3:
            continue
        petak = abu[py0:py1, px0:px1]
        tinta = float((petak < 0.55).mean())
        if tinta > AMBANG_TINTA:
            masalah.append(f"teks tertindih grafik {tinta:5.1%}: "
                           f"{t.get_text()[:40]!r}")

    # (3) teks keluar dari bidang gambar
    lebar_px = fig.get_size_inches()[0] * fig.dpi
    tinggi_fig = fig.get_size_inches()[1] * fig.dpi
    for b, t, _ in kotak:
        if b[0] < -2 or b[1] < -2 or b[2] > lebar_px + 2 \
                or b[3] > tinggi_fig + 2:
            masalah.append(f"teks keluar bidang: {t.get_text()[:40]!r}")

    if masalah:
        tertangkap.append((nama, masalah))


def main():
    asli = gaya.simpan

    def cegat(fig, nama):
        try:
            periksa(fig, nama)
        except Exception as e:                       # pemeriksaan gagal
            tertangkap.append((nama, [f"pemeriksaan gagal: {e}"]))
        asli(fig, nama)

    gaya.simpan = cegat
    import figs_bab1_3 as A
    import figs_bab4_14 as B
    import figs_peta as C
    for mod in (A, B, C):
        mod.simpan = cegat

    fungsi = []
    for mod in (A, B, C):
        for nm in dir(mod):
            if nm.startswith("g") and nm[1:2].isdigit():
                fungsi.append((nm, getattr(mod, nm)))
    print(f"memeriksa {len(fungsi)} gambar ...\n")
    for nm, f in fungsi:
        try:
            f()
        except Exception as e:
            print(f"  !! {nm} gagal dijalankan: {e}")
        plt.close("all")

    print("\n================ HASIL PEMERIKSAAN ================")
    if not tertangkap:
        print("tidak ada masalah tata letak yang terdeteksi")
    for nama, ms in sorted(tertangkap):
        print(f"\n{nama}")
        for m in ms:
            print(f"   - {m}")
    print(f"\ngambar bermasalah: {len(tertangkap)} dari {len(fungsi)}")


if __name__ == "__main__":
    main()
