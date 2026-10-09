"""Gambar peta Bab 7: tatanan tektonik dan peta sumber sesar PuSGeN 2024.

Sumber data (lihat ../data):
  bayangan relief   Natural Earth GRAY_HR_SR_OB, 1 menit busur
  garis pantai      Natural Earth 1:10 juta
  batas lempeng     Bird (2003), PB2002
  sesar aktif       PuSGeN 2024, 401 sumber sesar
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon as MplPolygon

import peta
from gaya import simpan, K, G1, G2

LEBAR = 5.28                     # lebar kolom teks B5, inci
PUTIH = dict(fc="white", ec="none", pad=0.9, alpha=0.80)
ABU = "#3d3d3d"


def _bingkai(ax, wil, dx=10, dy=5, fs=5.4):
    lo0, lo1, la0, la1 = wil
    xt = np.arange(np.ceil(lo0 / dx) * dx, lo1 + 0.1, dx)
    yt = np.arange(np.ceil(la0 / dy) * dy, la1 + 0.1, dy)
    ax.set_xticks(xt); ax.set_yticks(yt)
    ax.set_xticklabels(["%d°E" % v for v in xt], fontsize=fs)
    ax.set_yticklabels(["%d°%s" % (abs(v), "S" if v < 0 else
                                   ("N" if v > 0 else "")) for v in yt],
                       fontsize=fs)
    ax.tick_params(length=2, width=0.5, pad=1.4, color=G1)
    for s in ax.spines.values():
        s.set_linewidth(0.6); s.set_color(G1)


def _batas_lempeng(ax, wil, lw_sub=1.45, lw_lain=0.6, gerigi_tiap=2,
                   panjang=0.42):
    """Batas lempeng: zona subduksi bergerigi, batas lain garis tipis."""
    lo0, lo1, la0, la1 = wil
    bs = peta.batas()
    for b in bs:
        (x1, y1), (x2, y2) = b["p1"], b["p2"]
        if max(x1, x2) < lo0 - 1 or min(x1, x2) > lo1 + 1 \
                or max(y1, y2) < la0 - 1 or min(y1, y2) > la1 + 1:
            continue
        sub = b["kelas"] == "SUB"
        ax.plot([x1, x2], [y1, y2], lw=lw_sub if sub else lw_lain,
                color=K if sub else "#5a5a5a", zorder=3.1 if sub else 2.9,
                solid_capstyle="round")
    n = 0
    for b in bs:
        if b["kelas"] != "SUB":
            continue
        n += 1
        if n % gerigi_tiap:
            continue
        s = peta.sisi_atas(b["p1"], b["p2"])
        if s:
            peta.gerigi(ax, b["p1"], b["p2"], s, panjang=panjang)


def _sesar(ax, wil, lw=0.42, warna="#151515"):
    lo0, lo1, la0, la1 = wil
    for s in peta.sesar():
        xy = s["xy"]
        if (xy[:, 0].max() < lo0 or xy[:, 0].min() > lo1
                or xy[:, 1].max() < la0 or xy[:, 1].min() > la1):
            continue
        ax.plot(xy[:, 0], xy[:, 1], lw=lw, color=warna, zorder=2.6,
                solid_capstyle="round")


def _anak_panah_konvergensi(ax, titik, *, panjang=2.6, fs=5.2, geser=(0, 0)):
    """Anak panah gerak lempeng bawah relatif terhadap lempeng atas.

    Arah dan laju dihitung dari komponen konvergen dan komponen menganan
    model Bird (2003) -- keduanya tidak bergantung kerangka acuan.
    """
    bs = [b for b in peta.batas() if b["kelas"] == "SUB"]
    x, y = titik
    b = min(bs, key=lambda b: np.hypot(b["p1"][0] - x, b["p1"][1] - y))
    s = peta.sisi_atas(b["p1"], b["p2"])
    if s is None:
        return
    v = peta.v_relatif(b, s)
    u = v / np.hypot(*v)
    x0, y0 = x - u[0] * panjang, y - u[1] * panjang
    ax.annotate("", xy=(x, y), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color=K,
                                mutation_scale=6.5, shrinkA=0, shrinkB=0),
                zorder=4.2)
    ax.text(x0 + geser[0], y0 + geser[1], "%.0f mm/th" % np.hypot(*v),
            fontsize=fs, ha="center", va="center", color=K, zorder=4.3,
            bbox=PUTIH)


def _skala(ax, x0, y, km=500, fs=5.0):
    d = km / 111.19
    ax.plot([x0, x0 + d], [y, y], lw=1.5, color=K, zorder=4.4,
            solid_capstyle="butt")
    for xx in (x0, x0 + d):
        ax.plot([xx, xx], [y - 0.28, y + 0.28], lw=0.9, color=K, zorder=4.4)
    ax.text(x0 + d / 2, y + 0.55, "%d km" % km, fontsize=fs, ha="center",
            va="bottom", color=K, zorder=4.4, bbox=PUTIH)


# ------------------------------------------------ Gambar 7.1: tatanan tektonik
WIL71 = (93.0, 142.0, -12.6, 9.6)


def g71():
    lo0, lo1, la0, la1 = WIL71
    tinggi = LEBAR * (la1 - la0) / (lo1 - lo0)
    H = tinggi + 0.50
    fig = plt.figure(figsize=(LEBAR, H))
    ax = fig.add_axes([0.055, 0.40 / H, 0.938, tinggi / H * 0.975])
    peta.latar(ax, WIL71, terang=0.56, pantai_lw=0.28)
    _sesar(ax, WIL71)
    _batas_lempeng(ax, WIL71)

    # anak panah konvergensi: arah dan laju dari data
    for t, geser, pj in [((99.6, -4.4), (-2.2, -0.2), 2.4),
                         ((112.5, -10.5), (2.9, 0.25), 2.0),
                         ((122.4, -10.4), (2.8, 0.1), 1.7),
                         ((127.3, 7.2), (1.3, 1.7), 2.4),
                         ((137.4, -1.4), (-2.7, 0.5), 2.4)]:
        _anak_panah_konvergensi(ax, t, geser=geser, panjang=pj)

    # nama lempeng dan blok mikro
    besar = dict(fontsize=6.2, color=ABU, ha="center", va="center",
                 fontweight="bold", zorder=4.5, bbox=PUTIH)
    kecil = dict(fontsize=5.2, color=ABU, ha="center", va="center",
                 style="italic", zorder=4.5, bbox=PUTIH)
    ax.text(112.6, 4.2, "LEMPENG SUNDA", **besar)
    ax.text(97.6, -10.4, "LEMPENG\nINDO-AUSTRALIA", **besar)
    ax.text(134.9, 6.5, "LEMPENG\nLAUT FILIPINA", **besar)
    ax.text(95.7, 8.6, "EURASIA", **besar)
    ax.text(124.8, 2.3, "Laut\nMaluku", **kecil)
    ax.text(133.5, -2.3, "Kepala\nBurung", **kecil)
    ax.text(127.7, -5.7, "Laut\nBanda", **kecil)
    ax.text(125.3, -9.9, "Timor", **kecil)

    # nama palung
    pal = dict(fontsize=5.4, color=K, ha="center", va="center", zorder=4.5,
               bbox=PUTIH)
    ax.text(95.3, -1.1, "PALUNG SUNDA", rotation=-58, **pal)
    ax.text(107.6, -11.8, "PALUNG JAWA", rotation=-10, **pal)
    ax.text(130.7, 3.0, "PALUNG FILIPINA", rotation=-80, **pal)
    ax.text(130.8, -7.9, "busur Banda", rotation=0, **pal)
    ax.text(138.9, -3.5, "Palung Nugini", rotation=0, **pal)

    _skala(ax, 132.6, -11.6, 500)
    _bingkai(ax, WIL71)

    # keterangan di bawah peta
    kunci = [Line2D([], [], color=K, lw=1.45,
                    label="zona subduksi (gerigi ke arah lempeng atas)"),
             Line2D([], [], color="#5a5a5a", lw=0.7,
                    label="batas lempeng lain"),
             Line2D([], [], color="#151515", lw=0.6,
                    label="sesar aktif PuSGeN 2024 (401 sumber)")]
    fig.legend(handles=kunci, loc="lower center", ncol=3, frameon=False,
               fontsize=5.1, handlelength=1.9, columnspacing=1.0,
               handletextpad=0.5, borderaxespad=0.0,
               bbox_to_anchor=(0.52, 0.004))
    simpan(fig, "gbr-7-1-tektonik-indonesia.png")




# --------------------------------------- Gambar 7.2: peta sumber sesar PuSGeN
WIL72A = (95.0, 122.0, -11.0, 5.2)
WIL72B = (118.0, 142.0, -10.2, 3.9)

# Mmax tertinggi yang masuk akal pada basis data; nilai 65,0 pada satu
# segmen (Salak, JAV18) jelas salah ketik untuk 6,5 dan dibetulkan di sini.
MMAKS = 8.7


def _jenis(t):
    t = (t or "").strip().upper()
    if t.startswith("R"):
        return "naik"
    if t.startswith("N"):
        return "normal"
    return "geser"


GAYA_SESAR = {
    "naik": dict(color="#0f0f0f", ls="-"),
    "geser": dict(color="#0f0f0f", ls=(0, (2.6, 1.1))),
    "normal": dict(color="#565656", ls=(0, (0.7, 1.0))),
}


def _mmax(s):
    m = s["Mmax"]
    return m / 10.0 if m > 9.5 else m


def _lw(m):
    return 0.38 + 0.80 * (min(m, MMAKS) - 5.5) / (MMAKS - 5.5)


def _sesar_rinci(ax, wil):
    lo0, lo1, la0, la1 = wil
    for s in peta.sesar():
        xy = s["xy"]
        if (xy[:, 0].max() < lo0 or xy[:, 0].min() > lo1
                or xy[:, 1].max() < la0 or xy[:, 1].min() > la1):
            continue
        g = GAYA_SESAR[_jenis(s["Type"])]
        ax.plot(xy[:, 0], xy[:, 1], lw=_lw(_mmax(s)), zorder=2.7,
                solid_capstyle="round", dash_capstyle="round", **g)


def _pusat(nama, wilayah=None):
    pts = [s["xy"] for s in peta.sesar() if s["Main"] == nama
           and (wilayah is None or s["Region"] == wilayah)]
    if not pts:
        raise KeyError(nama)
    P = np.vstack(pts)
    return P[:, 0].mean(), P[:, 1].mean()


def _label_sesar(ax, daftar, fs=5.1):
    """Setiap butir: (nama_data, teks, x, y[, wilayah][, rotasi]).

    Bila rotasi diberikan, label ditaruh langsung tanpa garis penunjuk.
    """
    for butir in daftar:
        nama, teks, lx, ly = butir[:4]
        wil = butir[4] if len(butir) > 4 else None
        rot = butir[5] if len(butir) > 5 else None
        if rot is not None:
            ax.text(lx, ly, teks, fontsize=fs, ha="center", va="center",
                    rotation=rot, color=K, zorder=4.6, bbox=PUTIH,
                    linespacing=1.15)
            continue
        cx, cy = _pusat(nama, wil)
        ax.annotate(teks, xy=(cx, cy), xytext=(lx, ly), fontsize=fs,
                    ha="center", va="center", color=K, zorder=4.6,
                    bbox=PUTIH, linespacing=1.15,
                    arrowprops=dict(arrowstyle="-", lw=0.45, color="#2b2b2b",
                                    shrinkA=1.0, shrinkB=0.5))


def g72():
    wa, wb = WIL72A, WIL72B
    ha = LEBAR * (wa[3] - wa[2]) / (wa[1] - wa[0])
    hb = LEBAR * (wb[3] - wb[2]) / (wb[1] - wb[0])
    sela, bawah = 0.13, 0.31
    H = ha + hb + sela + bawah
    fig = plt.figure(figsize=(LEBAR, H))
    ax_a = fig.add_axes([0.052, (hb + sela + bawah) / H, 0.942, ha / H])
    ax_b = fig.add_axes([0.052, bawah / H, 0.942, hb / H])

    for ax, wil, hur in ((ax_a, wa, "a"), (ax_b, wb, "b")):
        peta.latar(ax, wil, terang=0.66, pantai_lw=0.26,
                   pantai_warna="#7b7b7b")
        _batas_lempeng(ax, wil, lw_sub=0.95, lw_lain=0.45, gerigi_tiap=3,
                       panjang=0.28)
        _sesar_rinci(ax, wil)
        _bingkai(ax, wil, dx=5, dy=5, fs=5.0)
        ax.text(0.008, 0.985, "(%s)" % hur, transform=ax.transAxes,
                fontsize=6.4, fontweight="bold", ha="left", va="top",
                color=K, zorder=5, bbox=PUTIH)

    _label_sesar(ax_a, [
        ("Sumatran Fault", "SESAR SUMATRA", 100.9, 1.3, None, -47),
        ("Mentawai Fault", "Sesar Mentawai", 99.9, -6.2),
        ("Java Back-arc Thrust", "Sesar naik belakang\nbusur Jawa", 108.4, -3.6),
        ("RMKS", "Zona RMKS", 115.4, -5.0),
        ("Opak Fault", "Sesar Opak", 112.3, -9.5),
        ("Lembang Fault", "Sesar Lembang\ndan Cimandiri", 102.9, -9.6),
        ("Makassar Strait Thrust", "Sesar naik\nSelat Makassar", 119.4, -5.0),
    ])
    _label_sesar(ax_b, [
        ("Palukoro", "Sesar Palu–Koro", 121.5, 2.4),
        ("Matano", "Sesar Matano", 124.4, -4.7),
        ("Sangihe Thrust", "Sesar naik Sangihe", 124.3, 3.3),
        ("Halmahera Thrust", "Sesar naik Halmahera", 130.7, 2.9),
        ("Sorong Fault", "Sesar Sorong", 133.2, 2.1, "Papua"),
        ("Yapen Fault", "Sesar Yapen", 138.2, 0.4),
        ("Tarera-Aiduna", "Sesar Tarera–Aiduna", 131.2, -6.5),
        ("Papua Fold Thrust Belt", "Sabuk lipat–sesar\nnaik Papua", 138.2, -7.8),
        ("Flores Back-arc Thrust", "Sesar naik\nbelakang\nbusur Flores", 120.7, -9.2),
        ("Timor FTB", "Sabuk lipat–sesar\nnaik Timor", 125.2, -9.5),
    ])

    kunci = [Line2D([], [], lw=0.9, label="sesar naik", **GAYA_SESAR["naik"]),
             Line2D([], [], lw=0.9, label="sesar geser", **GAYA_SESAR["geser"]),
             Line2D([], [], lw=0.9, label="sesar normal", **GAYA_SESAR["normal"]),
             Line2D([], [], color="#0f0f0f", lw=_lw(6.0), label="$M_{maks}$ 6,0"),
             Line2D([], [], color="#0f0f0f", lw=_lw(8.5), label="$M_{maks}$ 8,5")]
    fig.legend(handles=kunci, loc="lower center", ncol=5, frameon=False,
               fontsize=5.1, handlelength=2.0, columnspacing=1.0,
               handletextpad=0.5, borderaxespad=0.0,
               bbox_to_anchor=(0.52, 0.004))
    simpan(fig, "gbr-7-2-sesar-pusgen.png")


if __name__ == "__main__":
    g71()
    g72()
