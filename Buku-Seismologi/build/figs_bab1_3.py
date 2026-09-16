"""Gambar untuk Bab 1-3."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, Wedge, Polygon
from gaya import simpan, kotak, panah, bersih, K, G1, G2, G3, FILL


# ---------------------------------------------------------------- Gambar 1.1
def g11():
    """Bagan pohon geosains: penyiku ortogonal, jalur seismologi ditonjolkan."""
    from matplotlib.patches import FancyBboxPatch

    fig, ax = plt.subplots(figsize=(6.3, 4.6))
    ax.set_xlim(0, 136); ax.set_ylim(98.5, -2)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)

    TEBAL, TIPIS = 1.5, 0.85          # lebar garis jalur utama dan cabang
    SOROT, BIASA = "#d9d9d9", "white"

    def kotak(cx, cy, w, h, teks, fs=7.0, fc=BIASA, lw=0.9, bold=False):
        ax.add_patch(FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0,rounding_size=1.4",
            fc=fc, ec=K, lw=lw, zorder=3))
        ax.text(cx, cy, teks, ha="center", va="center", fontsize=fs,
                zorder=4, linespacing=1.15,
                fontweight="bold" if bold else "normal")

    def garis(pts, lw=TIPIS):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=K, lw=lw, solid_capstyle="round",
                solid_joinstyle="miter", zorder=2)

    # ---------------------------------------------------------- aras 0 dan 1
    y0, h0 = 6.0, 9.0
    kotak(68, y0, 38, h0, "GEOSAINS", fs=10, fc=SOROT, lw=1.4, bold=True)

    y1, h1, w1 = 24.0, 9.0, 29.0
    x1 = [18.5, 51.0, 83.5, 116.0]
    nama1 = ["GEOLOGI", "GEOGRAFI", "GEODESI", "GEOFISIKA"]
    bus1 = 16.5
    garis([(68, y0 + h0 / 2), (68, bus1)], TEBAL)
    garis([(x1[0], bus1), (68, bus1)])
    garis([(68, bus1), (x1[3], bus1)], TEBAL)
    for x, nm in zip(x1, nama1):
        utama = nm == "GEOFISIKA"
        garis([(x, bus1), (x, y1 - h1 / 2)], TEBAL if utama else TIPIS)
        kotak(x, y1, w1, h1, nm, fs=8,
              fc=SOROT if utama else BIASA, lw=1.3 if utama else 0.9,
              bold=utama)

    # ----------------------------------------------------------------- aras 2
    y2, h2, w2 = 45.5, 14.0, 24.0
    x2 = [14.0, 41.0, 68.0, 95.0, 122.0]
    nama2 = ["METEOROLOGI", "OSEANOGRAFI", "HIDROLOGI",
             "GEOKOSMO-\nFISIKA\n(ionosfer)", "GEOFISIKA\nBUMI\nPADAT"]
    bus2 = 36.0
    garis([(x1[3], y1 + h1 / 2), (x1[3], bus2)], TEBAL)
    garis([(x2[0], bus2), (x1[3], bus2)])
    garis([(x1[3], bus2), (x2[4], bus2)], TEBAL)
    for x, nm in zip(x2, nama2):
        utama = nm.startswith("GEOFISIKA")
        garis([(x, bus2), (x, y2 - h2 / 2)], TEBAL if utama else TIPIS)
        fs2 = 6.3
        kotak(x, y2, w2, h2, nm, fs=fs2,
              fc=SOROT if utama else BIASA, lw=1.3 if utama else 0.9,
              bold=utama)

    # ----------------------------------------------- aras 3: cabang bumi padat
    nama3 = ["SEISMOLOGI", "VULKANOLOGI", "GEOMAGNETISME",
             "GEOELEKTRISITAS", "TEKTONOFISIKA", "GRAVITASI",
             "GEOTERMAL", "GEOKOSMOGONI", "GEOKRONOLOGI"]
    w3, h3 = 38.0, 9.0
    kolom = [26.0, 68.0, 110.0]           # titik pusat tiap kolom
    baris = [67.0, 79.5, 92.0]            # titik pusat tiap baris
    tulang = [c - w3 / 2 - 4.0 for c in kolom]
    bus3 = 58.0
    garis([(x2[4], y2 + h2 / 2), (x2[4], bus3)], TEBAL)
    garis([(tulang[1], bus3), (x2[4], bus3)])
    garis([(tulang[0], bus3), (tulang[1], bus3)], TEBAL)
    garis([(tulang[2], bus3), (x2[4], bus3)])
    for k, (cx, tl) in enumerate(zip(kolom, tulang)):
        utama = k == 0
        garis([(tl, bus3), (tl, baris[-1])], TEBAL if utama else TIPIS)
        for b, y in enumerate(baris):
            nm = nama3[b * 3 + k]
            sorot = nm == "SEISMOLOGI"
            garis([(tl, y), (cx - w3 / 2, y)],
                  TEBAL if sorot else TIPIS)
            kotak(cx, y, w3, h3, nm, fs=7.0,
                  fc=SOROT if sorot else BIASA,
                  lw=1.4 if sorot else 0.9, bold=sorot)

    simpan(fig, "gbr-1-1-geosains.png")


# ---------------------------------------------------------------- Gambar 1.2
def g12():
    """Kurva output-input fase A dan fase B dengan garis ukur yang rapi."""
    fig, ax = plt.subplots(figsize=(5.2, 3.5))
    ax.set_xlim(0, 11.7); ax.set_ylim(0, 10.7)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_linewidth(1.0)
        ax.spines[sp].set_color(K)
    # ujung sumbu diberi mata panah
    ax.plot(1, 0, ">", color=K, ms=5, transform=ax.get_yaxis_transform(),
            clip_on=False)
    ax.plot(0, 1, "^", color=K, ms=5, transform=ax.get_xaxis_transform(),
            clip_on=False)

    def f(x):
        return 9.4 * (1 - np.exp(-0.55 * x))

    xd = 2.4                                   # batas fase A dan fase B
    ax.axvspan(0, xd, color=G3, alpha=0.32, lw=0)
    ax.plot([xd, xd], [0, 10.25], color=G2, lw=0.9, ls=(0, (2, 2.6)))

    x = np.linspace(0, 10.2, 500)
    ax.plot(x, f(x), color=K, lw=2.2, solid_capstyle="round")

    def ukur(p1, p2, arah, label, geser, fs=7.2, label_x=None):
        """Garis ukur berpanah dua arah beserta labelnya."""
        ax.annotate("", xy=p2, xytext=p1,
                    arrowprops=dict(arrowstyle="<|-|>", lw=0.85, color=G1,
                                    mutation_scale=7, shrinkA=0, shrinkB=0))
        if arah == "h":
            for px in (p1[0], p2[0]):
                ax.plot([px, px], [p1[1] - 0.22, p1[1] + 0.22], color=G1,
                        lw=0.7)
            ax.text((p1[0] + p2[0]) / 2, p1[1] + geser, label, fontsize=fs,
                    ha="center", va="top", color=G1)
        else:
            for py in (p1[1], p2[1]):
                ax.plot([p1[0] - 0.16, p1[0] + 0.16], [py, py], color=G1,
                        lw=0.7)
            lx = label_x if label_x is not None else p1[0] + geser
            ax.text(lx, (p1[1] + p2[1]) / 2, label, fontsize=fs,
                    ha="center", va="center", color=G1, rotation=90)

    def bantu(pts):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=G2, lw=0.6, ls=(0, (1.6, 2.0)), zorder=1)

    # ------------------------------------------------------------ fase A
    xa1, xa2 = 0.55, xd
    ya1, ya2 = f(xa1), f(xa2)
    bantu([(xa1, 1.05), (xa1, ya1)]); bantu([(xa2, 1.05), (xa2, ya2)])
    bantu([(0.33, ya1), (xa1, ya1)]); bantu([(0.33, ya2), (xa2, ya2)])
    ukur((xa1, 1.05), (xa2, 1.05), "h", "input kecil", -0.28)
    ukur((0.33, ya1), (0.33, ya2), "v", "", 0.0)
    # label diletakkan mendatar di atas garis ukur, di daerah yang kosong
    ax.text(0.20, ya2 + 0.34, "output besar", fontsize=7.2, color=G1,
            ha="left", va="bottom")

    # ------------------------------------------------------------ fase B
    xb1, xb2 = 3.2, 9.7
    yb1, yb2 = f(xb1), f(xb2)
    bantu([(xb1, 6.0), (xb1, yb1)]); bantu([(xb2, 6.0), (xb2, yb2)])
    bantu([(xb1, yb1), (10.45, yb1)]); bantu([(xb2, yb2), (10.45, yb2)])
    ukur((xb1, 6.0), (xb2, 6.0), "h", "input besar", -0.28)
    ukur((10.45, yb1), (10.45, yb2), "v", "output kecil", 0.55)

    ax.text(1.18, 8.85, "FASE A", fontsize=10, fontweight="bold", ha="center")
    ax.text(1.18, 8.15, "tahap awal", fontsize=6.8, color=G1, ha="center",
            style="italic")
    ax.text(6.30, 3.35, "FASE B", fontsize=10, fontweight="bold", ha="center")
    ax.text(6.30, 2.65, "tahap lanjut", fontsize=6.8, color=G1, ha="center",
            style="italic")

    ax.set_xlabel("INPUT (usaha, dana, kerumitan)", labelpad=6)
    ax.set_ylabel("OUTPUT (ketelitian hasil)", labelpad=6)
    simpan(fig, "gbr-1-2-fase.png")


# ---------------------------------------------------------------- Gambar 2.1
def g21():
    fig, axes = plt.subplots(1, 2, figsize=(6.0, 2.9))
    # (a) horizontal
    ax = axes[0]; bersih(ax); ax.set_xlim(0, 6); ax.set_ylim(0, 6)
    ax.add_patch(Rectangle((0.4, 4.9), 5.0, 0.35, fc=G3, ec=K, lw=1.0))
    ax.plot([0.6, 5.2], [4.9, 4.9], color=K, lw=1.0)
    for xh in np.arange(0.7, 5.3, 0.45):
        ax.plot([xh, xh - 0.22], [4.9, 4.62], color=G2, lw=0.7)
    ax.plot([2.9, 2.9], [4.9, 2.5], color=K, lw=1.0)
    ax.add_patch(Circle((2.9, 2.25), 0.33, fc=FILL, ec=K, lw=1.2, zorder=3))
    ax.text(2.9, 2.25, "m", ha="center", va="center", fontsize=8, zorder=4)
    ax.plot([2.9, 2.9], [1.92, 1.55], color=K, lw=1.0)
    ax.add_patch(Rectangle((0.55, 0.75), 4.9, 0.75, fc="white", ec=K, lw=1.0))
    xx = np.linspace(0.6, 5.4, 300)
    ax.plot(xx, 1.12 + 0.16 * np.sin(9 * xx), color=G1, lw=0.9)
    ax.text(3.0, 0.42, "kertas bergerak", fontsize=6.5, ha="center", color=G1)
    panah(ax, (1.0, 5.75), (2.3, 5.75), lw=1.0)
    ax.text(1.65, 5.95, "getaran tanah", fontsize=7, ha="center")
    ax.text(3.15, 3.6, "penggantung", fontsize=6.5, color=G1)
    ax.set_title("(a) komponen horizontal", fontsize=8.5)
    # (b) vertikal
    ax = axes[1]; bersih(ax); ax.set_xlim(0, 6); ax.set_ylim(0, 6)
    ax.add_patch(Rectangle((0.4, 4.9), 5.0, 0.35, fc=G3, ec=K, lw=1.0))
    for xh in np.arange(0.7, 5.3, 0.45):
        ax.plot([xh, xh - 0.22], [4.9, 4.62], color=G2, lw=0.7)
    ys = np.linspace(4.9, 3.15, 240)
    ax.plot(2.0 + 0.22 * np.sin(np.linspace(0, 16 * np.pi, 240)), ys,
            color=K, lw=1.0)
    ax.add_patch(Rectangle((1.45, 2.45), 1.1, 0.62, fc=FILL, ec=K, lw=1.2,
                           zorder=3))
    ax.text(2.0, 2.76, "m", ha="center", va="center", fontsize=8, zorder=4)
    ax.plot([2.55, 4.5], [2.76, 2.76], color=K, lw=1.0)
    ax.add_patch(Rectangle((4.3, 0.9), 1.15, 3.9, fc="white", ec=K, lw=1.0))
    yy = np.linspace(1.0, 4.7, 300)
    ax.plot(4.87 + 0.2 * np.sin(7 * yy), yy, color=G1, lw=0.9)
    panah(ax, (0.9, 4.2), (0.9, 3.1), lw=1.0)
    ax.text(0.72, 3.65, "getaran\ntanah", fontsize=7, ha="right", va="center")
    ax.text(2.55, 3.9, "pegas $k$", fontsize=6.5, color=G1)
    ax.set_title("(b) komponen vertikal", fontsize=8.5)
    simpan(fig, "gbr-2-1-pendulum.png")


# ---------------------------------------------------------------- Gambar 2.2
def g22():
    fig, ax = plt.subplots(figsize=(3.3, 3.0))
    bersih(ax); ax.set_xlim(0, 6); ax.set_ylim(0, 6)
    ax.plot([0.7, 5.3], [5.4, 5.4], color=K, lw=1.3)
    for xh in np.arange(0.8, 5.4, 0.42):
        ax.plot([xh, xh - 0.22], [5.4, 5.12], color=G2, lw=0.7)
    ys = np.linspace(5.4, 3.5, 220)
    ax.plot(1.9 + 0.2 * np.sin(np.linspace(0, 14 * np.pi, 220)), ys,
            color=K, lw=1.0)
    ax.text(1.35, 4.45, "$k$", fontsize=9)
    ax.plot([4.0, 4.0], [5.4, 4.65], color=K, lw=1.0)
    ax.add_patch(Rectangle((3.7, 4.0), 0.6, 0.65, fc="white", ec=K, lw=1.0))
    ax.plot([4.0, 4.0], [4.32, 3.5], color=K, lw=1.0)
    ax.plot([3.78, 4.22], [4.32, 4.32], color=K, lw=1.4)
    ax.text(4.45, 4.3, "$c$", fontsize=9)
    ax.add_patch(Rectangle((1.3, 2.6), 3.4, 0.9, fc=FILL, ec=K, lw=1.3))
    ax.text(3.0, 3.05, "$m$", ha="center", va="center", fontsize=10)
    panah(ax, (3.0, 1.35), (3.0, 2.5), lw=1.3)
    ax.text(3.2, 1.6, "$i(t)$", fontsize=9)
    ax.plot([0.55, 0.55], [2.2, 3.9], color=G2, lw=0.8, ls=":")
    ax.text(0.42, 3.05, "$y$", fontsize=9, ha="right", va="center")
    ax.annotate("", xy=(0.55, 3.9), xytext=(0.55, 3.05),
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=G2,
                                mutation_scale=8))
    simpan(fig, "gbr-2-2-mpk.png")


# ---------------------------------------------------------------- Gambar 2.3
def g23():
    """Tanggapan amplitudo sistem orde dua, skala linear dan logaritmik."""
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.95),
                             constrained_layout=True)
    wn = 1.0
    kasus = [(0.2, "-", 1.5), (0.5, "--", 1.2), (1.0, "-.", 1.2),
             (2.0, (0, (1.4, 1.6)), 1.2)]

    def H(w, e):
        return 1.0 / np.sqrt((wn**2 - w**2)**2 + 4 * e**2 * wn**2 * w**2)

    def nama(e):
        teks = f"{e:.1f}".replace(".", "{,}")
        return (rf"$\varepsilon = {teks}$"
                + ("  (kritis)" if e == 1.0 else ""))

    # --------------------------------------------------- (a) skala linear
    ax = axes[0]
    w = np.linspace(0.001, 3.0, 900)
    for e, ls, lw in kasus:
        ax.plot(w, H(w, e), color=K, ls=ls, lw=lw, label=nama(e))
    ax.axvline(1, color=G2, ls=":", lw=0.8, zorder=0)
    ax.text(1.04, 0.06, r"$\omega_n$", fontsize=7.5, color=G1)
    ax.set_xlim(0, 3); ax.set_ylim(0, 2.9)
    ax.set_xlabel(r"$\omega/\omega_n$")
    ax.set_ylabel(r"$|S_0/I_0|$")
    ax.set_title("(a) skala linear", fontsize=8.5)
    ax.grid(True, lw=0.3, color=G3)
    ax.legend(loc="upper right", frameon=True, framealpha=0.92,
              edgecolor=G2, fontsize=6.6, borderpad=0.45,
              handlelength=2.3, labelspacing=0.35)

    # ---------------------------------------------- (b) skala logaritmik
    ax = axes[1]
    w = np.logspace(-1.3, 1.3, 700)
    for e, ls, lw in kasus:
        ax.loglog(w, H(w, e), color=K, ls=ls, lw=lw)
    ax.axvline(1, color=G2, ls=":", lw=0.8, zorder=0)
    # segitiga acuan kemiringan, diletakkan di daerah yang kosong
    xa, xb, ya = 4.4, 9.2, 1.30
    yb = ya * (xa / xb) ** 2
    ax.loglog([xa, xb], [ya, yb], color=K, lw=1.3)
    ax.loglog([xa, xb], [ya, ya], color=G1, lw=0.8)
    ax.loglog([xb, xb], [ya, yb], color=G1, lw=0.8)
    ax.text(np.sqrt(xa * xb), ya * 1.20, "1", fontsize=6.6, color=G1,
            ha="center", va="bottom")
    ax.text(xb * 1.12, np.sqrt(ya * yb), "2", fontsize=6.6, color=G1,
            ha="left", va="center")
    ax.text(np.sqrt(xa * xb), yb * 0.60, "$-12$ dB/oktaf",
            fontsize=6.5, color=G1, ha="center", va="top")
    ax.set_xlim(0.05, 20); ax.set_ylim(3e-3, 4)
    ax.set_xlabel(r"$\omega/\omega_n$")
    ax.set_ylabel(r"$|S_0/I_0|$")
    ax.set_title("(b) skala logaritmik", fontsize=8.5)
    ax.grid(True, lw=0.3, color=G3, which="both")
    ax.text(1.18, 4.6e-3, r"$\omega_n$", fontsize=7.5, color=G1)
    simpan(fig, "gbr-2-3-orde2.png")


# ---------------------------------------------------------------- Gambar 2.4
def g24():
    fig, ax = plt.subplots(figsize=(3.5, 3.0))
    bersih(ax); ax.set_xlim(0, 6.5); ax.set_ylim(0, 6)
    ax.add_patch(Rectangle((0.8, 1.0), 4.4, 4.2, fc="none", ec=K, lw=1.3))
    ax.text(5.05, 1.25, "kerangka", fontsize=6.5, color=G1, ha="right",
            va="bottom")
    ys = np.linspace(5.2, 3.6, 200)
    ax.plot(2.1 + 0.18 * np.sin(np.linspace(0, 12 * np.pi, 200)), ys,
            color=K, lw=1.0)
    ax.text(1.6, 4.4, "$k$", fontsize=9)
    ax.plot([3.9, 3.9], [5.2, 4.5], color=K, lw=1.0)
    ax.add_patch(Rectangle((3.62, 3.9), 0.56, 0.6, fc="white", ec=K, lw=1.0))
    ax.plot([3.9, 3.9], [4.2, 3.6], color=K, lw=1.0)
    ax.text(4.3, 4.2, "$c$", fontsize=9)
    ax.add_patch(Rectangle((1.4, 2.9), 3.2, 0.75, fc=FILL, ec=K, lw=1.3))
    ax.text(3.0, 3.27, "$m$", ha="center", va="center", fontsize=10)
    for xh in np.arange(0.9, 5.3, 0.4):
        ax.plot([xh, xh - 0.2], [1.0, 0.75], color=G2, lw=0.7)
    panah(ax, (0.6, 0.45), (2.2, 0.45), lw=1.2)
    ax.text(1.4, 0.12, "$x$ (gerakan tanah)", fontsize=7, ha="center")
    ax.plot([5.65, 5.65], [2.8, 3.9], color=G1, lw=0.9, ls=":")
    ax.annotate("", xy=(5.65, 3.9), xytext=(5.65, 3.27),
                arrowprops=dict(arrowstyle="-|>", lw=0.9, color=G1,
                                mutation_scale=8))
    ax.text(5.85, 3.5, "$z=y-x$", fontsize=8, va="center")
    simpan(fig, "gbr-2-4-seismometer.png")


# ---------------------------------------------------------------- Gambar 2.5
def g25():
    """Tanggapan amplitudo seismometer: skala linear dan idealisasi asimtotik."""
    fig, axes = plt.subplots(1, 2, figsize=(5.28, 2.5),
                             constrained_layout=True)
    wn = 1.0
    kasus = [(0.2, "-", 1.25), (0.5, (0, (4.2, 1.5)), 1.0),
             (0.707, (0, (2.2, 1.1)), 1.35),
             (1.0, (0, (3.2, 1.1, 0.6, 1.1)), 1.0),
             (2.0, (0, (0.7, 1.5)), 1.0)]

    ax = axes[0]
    w = np.linspace(0.001, 4.0, 900)
    for e, ls, lw in kasus:
        H = w**2 / np.sqrt((wn**2 - w**2)**2 + 4 * e**2 * wn**2 * w**2)
        nm = r"$\varepsilon = 0{,}707$ (kritis)" if abs(e - 0.707) < 1e-6 \
            else r"$\varepsilon = %s$" % ("%g" % e).replace(".", "{,}")
        ax.plot(w, H, color=K, lw=lw, ls=ls, label=nm)
    ax.axhline(1, color=G2, ls=":", lw=0.8)
    ax.axvline(1, color=G2, ls=":", lw=0.8)
    ax.annotate("resonansi pada\nredaman kecil", xy=(1.02, 2.56),
                xytext=(0.06, 2.93), fontsize=5.8, ha="left", va="top",
                color=G1,
                arrowprops=dict(arrowstyle="->", lw=0.6, color=G1,
                                shrinkA=1, shrinkB=2))
    ax.set_xlabel(r"$\omega/\omega_n$"); ax.set_ylabel(r"$|Z_0/X_0|$")
    ax.set_ylim(0, 2.95); ax.set_xlim(0, 4)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_title("(a) skala linear", fontsize=8.0)
    ax.legend(loc="upper right", fontsize=5.4, frameon=False,
              handlelength=2.6, labelspacing=0.22, borderaxespad=0.25)

    ax = axes[1]
    w = np.logspace(-1.65, 1.65, 800)
    H = w**2 / np.sqrt((wn**2 - w**2)**2 + 4 * 0.707**2 * wn**2 * w**2)
    ax.loglog([0.02, 1], [0.02**2, 1], color=G2, ls="--", lw=0.9)
    ax.loglog([1, 50], [1, 1], color=G2, ls="--", lw=0.9)
    ax.loglog(w, H, color=K, lw=1.4)
    ax.axvline(1, color=G2, ls=":", lw=0.8)
    ax.annotate(r"$+12$ dB/oktaf  ($\propto \omega^{2}$)",
                xy=(0.13, 0.0169), xytext=(0.031, 0.62), fontsize=5.6,
                color=G1, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.6, color=G1,
                                shrinkA=1, shrinkB=2))
    ax.annotate("0 dB/oktaf (datar)", xy=(9.0, 1.0), xytext=(2.2, 0.10),
                fontsize=5.6, color=G1, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.6, color=G1,
                                shrinkA=1, shrinkB=2))
    ax.text(1.18, 8.0e-4, r"$\omega_n$", fontsize=7.5, ha="left", va="bottom")
    ax.set_xlim(0.022, 45); ax.set_ylim(5.5e-4, 2.4)
    ax.set_xlabel(r"$\omega/\omega_n$"); ax.set_ylabel(r"$|Z_0/X_0|$")
    ax.set_title(r"(b) idealisasi asimtotik ($\varepsilon = 0{,}707$)",
                 fontsize=8.0)
    simpan(fig, "gbr-2-5-tanggapan-seismometer.png")


# ------------------------------------------------------------ Gambar 2.6/2.7
def _sens(fig, axes, extra=0):
    wn = 1.0; e = 0.707
    w = np.logspace(-1.5, 1.5, 700)
    D = np.sqrt((wn**2 - w**2)**2 + 4 * e**2 * wn**2 * w**2)
    V = w**(2 + extra) / D
    S = w**(1 + extra) / D
    E = w**(0 + extra) / D
    for ax, y, lab, s1, s2 in zip(
            axes, [V, S, E], ["$V$ (pergeseran)", "$S$ (kecepatan)",
                              "$E$ (percepatan)"],
            [12 + 6 * extra, 6 + 6 * extra, 0 + 6 * extra],
            [0 + 6 * extra, -6 + 6 * extra, -12 + 6 * extra]):
        ax.loglog(w, y, color=K, lw=1.4)
        ax.axvline(1, color=G2, ls=":", lw=0.8)
        ax.set_title(lab, fontsize=8)
        ax.set_xlabel(r"$\omega/\omega_n$")
        ax.text(0.05, 0.05, f"{s1:+d}", fontsize=6.8, color=G1,
                transform=ax.transAxes, ha="left", va="bottom")
        ax.text(0.95, 0.05, f"{s2:+d}", fontsize=6.8, color=G1,
                transform=ax.transAxes, ha="right", va="bottom")
        ax.set_yticks([])
        ax.set_xlim(0.03, 32)
        ax.set_xticks([0.1, 1, 10])
        ax.tick_params(axis="x", which="minor", length=1.6)


def g26():
    fig, axes = plt.subplots(1, 3, figsize=(6.5, 2.25),
                             constrained_layout=True)
    _sens(fig, axes, extra=0)
    axes[0].set_ylabel("sensitivitas")
    simpan(fig, "gbr-2-6-sensitivitas.png")


def g27():
    fig, axes = plt.subplots(1, 3, figsize=(6.5, 2.25),
                             constrained_layout=True)
    _sens(fig, axes, extra=1)
    axes[0].set_ylabel("sensitivitas")
    fig.suptitle("seismometer elektromagnetik (keluaran sebanding kecepatan)",
                 fontsize=8, y=1.06)
    simpan(fig, "gbr-2-7-elektromagnetik.png")


# ---------------------------------------------------------------- Gambar 2.8
def g28():
    """Tiga cara menggantung massa dan akibatnya pada perioda bebas."""
    fig, axes = plt.subplots(1, 3, figsize=(5.28, 2.78))
    fig.subplots_adjust(left=0.008, right=0.992, top=0.855, bottom=0.005,
                        wspace=0.04)
    for ax in axes:
        bersih(ax); ax.set_xlim(0, 5); ax.set_ylim(0, 5)

    def langit(ax, x0, x1, y=4.55):
        ax.plot([x0, x1], [y, y], color=K, lw=1.2)
        for xh in np.arange(x0 + 0.1, x1, 0.32):
            ax.plot([xh, xh - 0.18], [y, y - 0.22], color=G2, lw=0.7)

    def pegas(ax, p0, p1, n=11, amp=0.14, lw=1.0):
        p0 = np.asarray(p0, float); p1 = np.asarray(p1, float)
        t = np.linspace(0, 1, 240)
        d = p1 - p0; L = np.hypot(*d)
        u = d / L; v = np.array([-u[1], u[0]])
        pts = p0 + np.outer(t, d) + np.outer(
            amp * np.sin(2 * np.pi * n * t) * np.sin(np.pi * t), v)
        ax.plot(pts[:, 0], pts[:, 1], color=K, lw=lw)

    def massa(ax, c, r, fs=6.8):
        ax.add_patch(Circle(c, r, fc=FILL, ec=K, lw=1.2, zorder=3))
        ax.text(c[0], c[1], "$m$", fontsize=fs, ha="center", va="center",
                zorder=4)

    def rumus(ax, teks, catatan, fs=6.6):
        ax.text(2.5, 1.06, teks, fontsize=fs, ha="center", va="center")
        ax.text(2.5, 0.38, catatan, fontsize=5.4, ha="center", va="center",
                color=G1, linespacing=1.3)

    def arah(ax, x, y, tegak, teks, pj=0.44):
        dx, dy = (0.0, pj) if tegak else (pj, 0.0)
        ax.annotate("", xy=(x + dx, y + dy), xytext=(x - dx, y - dy),
                    arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=G1,
                                    mutation_scale=6))
        ax.text(x, y - (pj + 0.14), teks, fontsize=5.3, color=G1,
                ha="center", va="top", linespacing=1.2)

    # ---- (a) pendulum vertikal sederhana
    ax = axes[0]
    langit(ax, 1.05, 3.95)
    pegas(ax, (2.5, 4.55), (2.5, 3.05), n=9)
    massa(ax, (2.5, 2.66), 0.39)
    ax.text(2.80, 3.85, "$k$", fontsize=7, ha="left", va="center")
    arah(ax, 1.00, 2.96, True, "gerakan\ntanah")
    ax.set_title("(a) pendulum vertikal\nsederhana", fontsize=7.2)
    rumus(ax, r"$T_0 = 2\pi\sqrt{\delta/g}$",
          "perioda panjang menuntut regangan\n"
          r"statis besar: $T_0 = 10$ s $\Rightarrow \delta \approx 25$ m")

    # ---- (b) suspensi LaCoste
    ax = axes[1]
    langit(ax, 0.75, 4.25)
    ax.plot([1.05, 3.60], [2.45, 2.45], color=K, lw=1.7)
    massa(ax, (3.98, 2.45), 0.36, fs=6.4)
    ax.add_patch(Circle((1.05, 2.45), 0.10, fc=K, ec=K, zorder=4))
    ax.text(1.05, 2.16, "sumbu putar", fontsize=5.3, color=G1, ha="center",
            va="top")
    pegas(ax, (1.62, 4.55), (3.05, 2.45), n=10, amp=0.11)
    ax.add_patch(Circle((3.05, 2.45), 0.07, fc=K, ec=K, zorder=4))
    ax.annotate("pegas\npanjang-nol", xy=(2.45, 3.45), xytext=(3.62, 3.80),
                fontsize=5.3, color=G1, ha="center", va="center",
                linespacing=1.2,
                arrowprops=dict(arrowstyle="->", lw=0.6, color=G1,
                                shrinkA=1, shrinkB=2))
    arah(ax, 0.55, 3.62, True, "gerakan\ntanah")
    ax.set_title("(b) suspensi LaCoste\n(astatik)", fontsize=7.2)
    rumus(ax, r"$T_0$ panjang tanpa" "\n" r"pegas panjang",
          "gaya pemulih hampir dihapus oleh\n"
          "bobot, sehingga perioda dapat disetel")

    # ---- (c) pendulum garden-gate
    ax = axes[2]
    A = np.array([3.05, 4.55]); B = np.array([2.29, 1.50])
    ax.plot([A[0], B[0]], [A[1], B[1]], color=K, lw=1.6)
    ax.plot([A[0], A[0]], [A[1], 1.50], color=G2, lw=0.7, ls=":")
    ax.add_patch(Arc(A, 1.5, 1.5, theta1=256, theta2=270, color=G1, lw=0.9))
    ax.text(A[0] - 0.36, A[1] - 0.74, r"$\theta$", fontsize=7.5, color=G1,
            ha="right", va="center")
    C = A + 0.40 * (B - A)
    Mx, My = 4.22, C[1]
    massa(ax, (Mx, My), 0.34, fs=6.4)
    ax.plot([C[0], Mx - 0.34], [C[1], My], color=K, lw=1.6)
    ax.add_patch(Circle(C, 0.07, fc=K, ec=K, zorder=4))
    ax.add_patch(Arc((C[0], My), 2.0 * (Mx - C[0]), 0.62, theta1=-40,
                     theta2=40, color=G1, lw=0.8, ls="--"))
    arah(ax, Mx, 2.42, False, "gerakan tanah", pj=0.50)
    ax.set_title("(c) pendulum $garden$-$gate$\n(horizontal)", fontsize=7.2)
    rumus(ax, r"$T_0 = 2\pi\sqrt{l/(g\sin\theta)}$",
          r"sumbu dimiringkan sedikit dari tegak;" "\n"
          r"$\theta$ kecil memberi perioda panjang", fs=6.2)
    simpan(fig, "gbr-2-8-konfigurasi.png")


# ---------------------------------------------------------------- Gambar 2.9
def g29():
    """Rantai perekaman: tujuh mata rantai dengan anak panah yang terlihat."""
    fig, ax = plt.subplots(figsize=(5.28, 2.05))
    fig.subplots_adjust(left=0.004, right=0.996, top=0.996, bottom=0.004)
    ax.set_xlim(0, 100); ax.set_ylim(9, 100)
    bersih(ax); ax.set_aspect("auto")

    lab = ["Gerakan\ntanah", "Sensor\npita lebar /\nakselerometer",
           "Digitizer\n24 bit\n+ GNSS", "Telemetri\nVSAT, seluler,\nserat",
           "Pusat data\nminiSEED +\nStationXML",
           "Pengolahan\notomatis\n(SeisComP)",
           "Katalog,\nShakeMap,\nperingatan"]
    ket = ["besaran\nfisis", "tegangan\nanalog", "cacahan\n(counts)",
           "paket\ndata", "berkas\nterarsip", "parameter\ngempa"]

    y0, y1 = 42.0, 78.0
    w, sela = 11.95, 2.60
    x = 0.3
    tengah = []
    for i, t in enumerate(lab):
        fc = FILL if i in (1, 2) else "white"
        ax.add_patch(Rectangle((x, y0), w, y1 - y0, fc=fc, ec=K, lw=0.9,
                               zorder=2))
        ax.text(x + w / 2, (y0 + y1) / 2, t, fontsize=5.4, ha="center",
                va="center", zorder=3, linespacing=1.24)
        if i < 6:
            tengah.append(x + w + sela / 2)
            panah(ax, (x + w + 0.25, (y0 + y1) / 2),
                  (x + w + sela - 0.25, (y0 + y1) / 2), lw=1.0)
        x += w + sela

    # besaran yang mengalir pada setiap sambungan
    for xb, t in zip(tengah, ket):
        ax.plot([xb, xb], [y0 - 1.5, 30.0], color=G2, lw=0.55, zorder=1)
        ax.text(xb, 27.5, t, fontsize=5.0, ha="center", va="top", color=G1,
                style="italic", linespacing=1.22)

    def kurung(x0, x1, y, teks):
        ax.plot([x0, x0, x1, x1], [y - 2.8, y, y, y - 2.8], color=G1, lw=0.6)
        ax.text((x0 + x1) / 2, y + 1.8, teks, fontsize=5.2, ha="center",
                va="bottom", color=G1, style="italic")
    kurung(0.3 + (w + sela), 0.3 + 3 * (w + sela) + w, 86.0,
           "perangkat di lapangan")
    kurung(0.3 + 4 * (w + sela), 0.3 + 6 * (w + sela) + w, 86.0,
           "di pusat data")
    simpan(fig, "gbr-2-9-rantai.png")


# --------------------------------------------------------------- Gambar 2.10
def g210():
    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    T = np.logspace(-2, 3, 500)
    # kurva skematis mirip NLNM/NHNM (nilai indikatif, bukan tabel resmi)
    nlnm = (-168 + 16 * np.log10(T) - 6 * np.exp(-((np.log10(T) - 0.75) / 0.35)**2)
            + 22 * np.exp(-((np.log10(T) - 2.4) / 0.6)**2))
    nhnm = nlnm + 45 + 8 * np.exp(-((np.log10(T) - 0.8) / 0.4)**2)
    ax.semilogx(T, nlnm, color=K, lw=1.5, label="NLNM")
    ax.semilogx(T, nhnm, color=K, lw=1.5, ls="--", label="NHNM")
    ax.fill_between(T, nlnm, nhnm, color=G3, alpha=0.45)
    ax.axvspan(4, 8, color=G2, alpha=0.18)
    ax.axvspan(12, 20, color=G2, alpha=0.12)
    ax.text(5.6, -95, "mikroseism\nsekunder", fontsize=6.5, ha="center")
    ax.text(15.5, -172, "mikroseism\nprimer", fontsize=6.5, ha="center")
    ax.text(0.05, -100, "derau budaya\n(mesin, lalu lintas)", fontsize=6.5)
    ax.text(200, -170, "derau atmosfer,\npasang surut", fontsize=6.5,
            ha="center")
    ax.set_xlabel("Perioda (s)")
    ax.set_ylabel("PSD percepatan (dB relatif $1\\ (\\mathrm{m/s^2})^2/$Hz)")
    ax.set_ylim(-200, -70)
    ax.legend(loc="upper right", frameon=False)
    ax.set_title("Model derau baku (skematis, mengikuti Peterson 1993)",
                 fontsize=8)
    simpan(fig, "gbr-2-10-derau.png")


# ---------------------------------------------------------------- Gambar 3.1
def g31():
    fig, axes = plt.subplots(2, 1, figsize=(5.6, 4.0))
    for ax, judul, pasangan in [
            (axes[0], "(a) dilihat dari samping",
             [("P", "longitudinal"), ("SV", "transversal vertikal"),
              ("R", "eliptik retrograd")]),
            (axes[1], "(b) dilihat dari atas",
             [("P", "longitudinal"), ("SH", "transversal horizontal"),
              ("L", "horizontal, tegak lurus")])]:
        bersih(ax); ax.set_xlim(0, 12); ax.set_ylim(0, 3.4)
        ax.set_aspect("auto")
        ax.add_patch(Circle((0.75, 1.7), 0.3, fc=K, ec=K))
        ax.text(0.75, 2.35, "sumber", fontsize=6.5, ha="center")
        panah(ax, (1.15, 1.7), (11.4, 1.7), lw=0.8, color=G2)
        pos = [3.0, 6.2, 9.4]
        for x, (nm, ket) in zip(pos, pasangan):
            for i in range(9):
                xx = x - 1.1 + i * 0.26
                if nm == "P":
                    d = 0.09 * np.sin(i * 1.1)
                    ax.plot([xx + d, xx + d], [1.35, 2.05], color=K, lw=1.6)
                elif nm in ("SV",):
                    ax.plot([xx, xx], [1.7 - 0.32 * np.sin(i * 0.9),
                                       1.7 + 0.32 * np.sin(i * 0.9)],
                            color=K, lw=0.9)
                    ax.plot(xx, 1.7 + 0.32 * np.sin(i * 0.9), "o", ms=1.8,
                            color=K)
                elif nm in ("SH", "L"):
                    ax.plot([xx, xx], [1.7, 1.7 + 0.30 * np.sin(i * 0.9)],
                            color=K, lw=0.9)
                    ax.plot(xx, 1.7 + 0.30 * np.sin(i * 0.9), "o", ms=2.0,
                            color=K)
                else:
                    th = np.linspace(0, 2 * np.pi, 40)
                    ax.plot(xx + 0.08 * np.cos(th), 1.7 + 0.22 * np.sin(th),
                            color=K, lw=0.7)
            ax.text(x, 0.55, f"{nm}\n{ket}", fontsize=6.5, ha="center")
        ax.set_title(judul, fontsize=8, loc="left")
    simpan(fig, "gbr-3-1-gerakan-partikel.png")


# ---------------------------------------------------------------- Gambar 3.2
def g32():
    """Pantulan dan pembiasan pada bidang batas beserta konversi mode."""
    fig, ax = plt.subplots(figsize=(5.34, 3.99))
    fig.subplots_adjust(left=0.004, right=0.996, top=0.996, bottom=0.004)
    bersih(ax); ax.set_xlim(0, 10); ax.set_ylim(0, 7.4)
    ax.axhline(3.5, color=K, lw=1.3, zorder=2)
    ax.fill_between([0, 10], 0, 3.5, color=FILL, zorder=0)
    O = np.array([5.0, 3.5])
    putih = dict(fc="white", ec="none", pad=1.0, alpha=0.9)

    # kecepatan yang dipakai (km/s) dan sudut menurut hukum Snell
    vp1, vs1, vp2, vs2 = 6.0, 3.46, 8.0, 4.60
    i1 = np.radians(40.0)
    p = np.sin(i1) / vp1                        # parameter gelombang
    sudut = {}
    for nama, v, atas in [("P pantul", vp1, True), ("SV pantul", vs1, True),
                          ("P bias", vp2, False), ("SV bias", vs2, False)]:
        sudut[nama] = (np.arcsin(np.clip(p * v, -1, 1)), atas)

    def sinar(a, atas, R=3.3):
        """Titik ujung sinar yang membentuk sudut a dengan normal."""
        dy = R * np.cos(a) * (1 if atas else -1)
        return O + np.array([R * np.sin(a), dy])

    # sinar datang
    P_in = O + np.array([-3.3 * np.sin(i1), 3.3 * np.cos(i1)])
    panah(ax, P_in, O, lw=1.4)
    ax.text(P_in[0] - 0.1, P_in[1] + 0.12, "P datang", fontsize=7,
            ha="left", va="bottom")

    for nama, lw, ls, dx, dy, ha in [
            ("P pantul", 1.2, "-", 0.14, 0.14, "left"),
            ("SV pantul", 1.0, "--", -0.05, 0.22, "center"),
            ("P bias", 1.2, "-", 0.16, -0.10, "left"),
            ("SV bias", 1.0, "--", -0.02, -0.26, "center")]:
        a, atas = sudut[nama]
        Q = sinar(a, atas)
        panah(ax, O, Q, lw=lw, ls=ls)
        ax.text(Q[0] + dx, Q[1] + dy, nama, fontsize=6.6, ha=ha,
                va="bottom" if atas else "top", bbox=putih, zorder=4)

    # normal
    ax.plot([5, 5], [0.35, 7.05], color=G2, ls=":", lw=0.9)
    ax.text(5.10, 0.40, "normal", fontsize=6.2, color=G1, va="bottom",
            bbox=putih, zorder=4)

    # busur sudut: digambar dari arah normal ke arah sinar
    def busur(a, atas, R, teks, geser=1.0, bagi=0.5):
        t0 = 90.0 if atas else 270.0
        t1 = t0 - np.degrees(a) if atas else t0 + np.degrees(a)
        ax.add_patch(Arc(O, 2 * R, 2 * R, theta1=min(t0, t1),
                         theta2=max(t0, t1), color=G1, lw=0.8))
        am = a * bagi
        q = O + geser * R * np.array([np.sin(am),
                                      np.cos(am) * (1 if atas else -1)])
        ax.text(q[0], q[1], teks, fontsize=8, ha="center", va="center",
                bbox=putih, zorder=4)

    # sudut datang di sisi kiri normal
    ax.add_patch(Arc(O, 2.8, 2.8, theta1=90, theta2=90 + np.degrees(i1),
                     color=G1, lw=0.8))
    am = i1 / 2
    ax.text(O[0] - 1.4 * np.sin(am), O[1] + 1.4 * np.cos(am), "$i_1$",
            fontsize=8, ha="center", va="center", bbox=putih, zorder=4)
    busur(sudut["P pantul"][0], True, 1.75, "$i_1$", 1.18, bagi=0.80)
    busur(sudut["P bias"][0], False, 1.5, "$i_2$", 1.18)

    ax.text(0.25, 4.55, "medium 1: $v_{p1}$, $v_{s1}$", fontsize=7,
            bbox=putih, zorder=4)
    ax.text(0.25, 2.52, "medium 2: $v_{p2} > v_{p1}$", fontsize=7,
            bbox=putih, zorder=4)
    ax.text(9.75, 3.62, r"$\dfrac{\sin i_1}{v_{p1}} = \dfrac{\sin i_2}{v_{p2}}$",
            fontsize=7, ha="right", va="bottom", bbox=putih, zorder=4)
    simpan(fig, "gbr-3-2-snell.png")


# ---------------------------------------------------------------- Gambar 3.3
def g33():
    fig, ax = plt.subplots(figsize=(4.8, 3.0))
    bersih(ax); ax.set_xlim(0, 9.6); ax.set_ylim(0, 6.4)
    ax.set_aspect("auto")
    for y, lab in [(5.0, "$v_1$"), (3.4, "$v_2 > v_1$"), (1.6, "$v_3 > v_2$")]:
        ax.axhline(y, color=K, lw=1.0)
        ax.text(0.15, y - 0.55, lab, fontsize=7.5)
    ax.axhline(6.2, color=K, lw=1.3)
    src = (1.2, 6.2)
    for p, sty, nm, lx, ly, lha in [
            (0.40, "-", "berkas I ($p_1$)", 4.8, 0.85, "right"),
            (0.50, "--", "berkas II ($p_2>p_1$)", 7.6, 2.45, "left")]:
        x = src[0]; y = src[1]
        pts = [(x, y)]
        for v, ytop, ybot in [(1.0, 6.2, 5.0), (1.25, 5.0, 3.4),
                              (1.5, 3.4, 1.6), (1.8, 1.6, 0.3)]:
            s = np.clip(p * v, 0, 0.999)
            th = np.arcsin(s)
            dy = ytop - ybot
            x = x + dy * np.tan(th)
            y = ybot
            pts.append((x, y))
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], color=K, lw=1.2, ls=sty)
        ax.text(lx, ly, nm, fontsize=6.5, va="center", ha=lha,
                bbox=dict(fc="white", ec="none", pad=0.8, alpha=0.9))
    ax.add_patch(Circle(src, 0.14, fc=K))
    ax.text(1.9, 5.98, "sumber", fontsize=6.5, ha="left", va="top")
    simpan(fig, "gbr-3-3-berkas.png")


# ---------------------------------------------------------------- Gambar 3.4
def g34():
    fig, ax = plt.subplots(figsize=(3.6, 3.6))
    bersih(ax); ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
    ax.add_patch(Circle((0, 0), 1.0, fc="white", ec=K, lw=1.5))
    for r, ls in [(0.75, ":"), (0.5, ":")]:
        ax.add_patch(Circle((0, 0), r, fc="none", ec=G2, lw=0.7, ls=ls))
    ax.add_patch(Circle((0, 0), 0.03, fc=K))
    th0 = np.pi / 2
    src = (np.cos(th0), np.sin(th0))
    for depth, label in [(0.62, None), (0.75, None), (0.86, None)]:
        t = np.linspace(0, 1, 200)
        ang = th0 - t * (0.9 * (1 - depth) * 8)
        r = 1 - (1 - depth) * np.sin(np.pi * t)
        ax.plot(r * np.cos(ang), r * np.sin(ang), color=K, lw=1.1)
    ax.plot([src[0]], [src[1]], "o", color=K, ms=4)
    ax.text(0.02, 1.06, "sumber", fontsize=6.5, ha="center")
    ax.plot([0, 1.05 * np.cos(th0 - 1.9)], [0, 1.05 * np.sin(th0 - 1.9)],
            color=G2, lw=0.7, ls="--")
    ax.text(0.62, 0.28, "$R_i$", fontsize=7.5, color=G1)
    ax.text(-0.1, 0.4, "$v$ bertambah\nterhadap kedalaman", fontsize=6.3,
            color=G1, ha="center")
    simpan(fig, "gbr-3-4-mantel.png")


# ---------------------------------------------------------------- Gambar 3.5
def g35():
    """Gelombang kepala: sinar kritis, muka gelombangnya, dan perbandingannya
    dengan muka gelombang langsung pada saat yang sama."""
    v1, v2 = 2.0, 4.0
    ic = np.arcsin(v1 / v2)                    # 30 derajat
    ys, yi = 4.8, 2.0                          # permukaan dan bidang batas
    h = ys - yi
    S = np.array([1.4, ys])
    xk = S[0] + h * np.tan(ic)                 # titik kritis di bidang batas
    xf = 9.6                                   # muka gelombang kepala
    fig, ax = plt.subplots(figsize=(5.34, 2.46))
    fig.subplots_adjust(left=0.004, right=0.996, top=0.996, bottom=0.004)
    bersih(ax); ax.set_xlim(0, 12.4); ax.set_ylim(0.6, 5.9)
    putih = dict(fc="white", ec="none", pad=1.0, alpha=0.9)

    ax.plot([0, 12.4], [ys, ys], color=K, lw=1.1)
    ax.plot([0, 12.4], [yi, yi], color=K, lw=1.4)
    ax.fill_between([0, 12.4], 0.6, yi, color=FILL)
    ax.text(0.20, yi + 0.28, "$v_1$", fontsize=8, bbox=putih)
    ax.text(0.20, yi - 0.66, "$v_2 > v_1$", fontsize=8, bbox=putih)
    ax.text(0.20, ys - 0.18, "permukaan", fontsize=6.0, color=G1,
            ha="left", va="top")

    ax.add_patch(Circle(S, 0.12, fc=K, zorder=5))
    ax.text(S[0] - 0.12, ys + 0.16, "sumber", fontsize=6.4, ha="left",
            va="bottom")

    # sinar kritis turun, lalu gelombang kepala menjalar di bidang batas
    ax.plot([S[0], xk], [ys, yi], color=K, lw=1.0)
    ax.plot([xk, xf], [yi, yi], color=K, lw=2.1)
    ax.add_patch(Arc((S[0], ys), 1.9, 1.9, theta1=270,
                     theta2=270 + np.degrees(ic), color=G1, lw=0.8))
    ax.text(S[0] + 0.52, ys - 1.02, "$i_c$", fontsize=8, bbox=putih)

    # sinar gelombang kepala, semuanya keluar pada sudut kritis
    u = np.array([np.sin(ic), np.cos(ic)])
    for xi in np.arange(xk + 0.55, xf - 0.05, 0.85):
        srt = (xf - xi) / 2.0
        Q = np.array([xi, yi]) + srt * u
        ax.plot([xi, Q[0]], [yi, Q[1]], color=K, lw=0.7)

    # muka gelombang kepala: tegak lurus sinar-sinar itu
    x_atas = xf - h / np.tan(ic)
    ax.plot([xf, x_atas], [yi, ys], color=K, lw=2.1)
    ax.annotate("muka gelombang kepala", xy=(5.85, 4.20), xytext=(3.35, 5.45),
                fontsize=6.2, color=G1, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.6, color=G1,
                                shrinkA=1, shrinkB=2))

    # muka gelombang langsung pada saat yang sama: busur berpusat di sumber
    t = (h / np.cos(ic)) / v1 + (xf - xk) / v2
    R = v1 * t
    th = np.linspace(-np.arcsin(h / R), 0.0, 240)
    ax.plot(S[0] + R * np.cos(th), ys + R * np.sin(th), color=K, lw=2.1,
            ls=(0, (3.2, 1.6)))
    ax.annotate("muka gelombang langsung\n(kecepatan $v_1$)",
                xy=(7.75, 4.35), xytext=(10.2, 5.25), fontsize=6.2, color=G1,
                ha="center", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.6, color=G1,
                                shrinkA=1, shrinkB=2))
    ax.text(6.55, yi - 0.66, "menjalar dengan $v_2$", fontsize=6.2, color=G1,
            bbox=putih)
    simpan(fig, "gbr-3-5-headwave.png")


# ---------------------------------------------------------------- Gambar 3.6
def g36():
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    bersih(ax); ax.set_xlim(-1.32, 1.32); ax.set_ylim(-1.32, 1.32)
    R = 1.0
    rc = 1 - 2891 / 6371.0
    ri = 1 - 5150 / 6371.0
    ax.add_patch(Circle((0, 0), R, fc="white", ec=K, lw=1.6, zorder=1))
    ax.add_patch(Circle((0, 0), rc, fc="#f4f4f4", ec=K, lw=1.2, zorder=1))
    ax.add_patch(Circle((0, 0), ri, fc=G3, ec=K, lw=1.0, zorder=1))
    ax.text(0, -0.02, "inti\ndalam", fontsize=5.6, ha="center", va="center",
            zorder=5)
    ax.text(0, -0.44, "inti luar", fontsize=6.2, ha="center", zorder=5)
    ax.text(-0.62, 0.55, "mantel", fontsize=6.6, ha="center", zorder=5)
    a0 = np.pi / 2                       # posisi sumber di puncak

    def titik(delta, r=R):
        a = a0 - np.radians(delta)
        return np.array([r * np.cos(a), r * np.sin(a)])

    def busur(d1, d2, rmin, **kw):
        t = np.linspace(0, 1, 240)
        a = a0 - np.radians(d1 + (d2 - d1) * t)
        r = R - (R - rmin) * np.sin(np.pi * t)
        ax.plot(r * np.cos(a), r * np.sin(a), zorder=4, **kw)

    ax.plot(*titik(0), "*", color=K, ms=11, zorder=6)
    ax.text(0.0, 1.08, "sumber", fontsize=6.8, ha="center")
    # P langsung
    busur(0, 80, 0.62, color=K, lw=1.2)
    ax.text(*(titik(66, 0.70)), "P", fontsize=8, ha="center")
    # PP
    busur(0, 55, 0.74, color=K, lw=1.0)
    busur(55, 110, 0.74, color=K, lw=1.0)
    ax.text(*(titik(55, 1.06)), "PP", fontsize=7.5, ha="center")
    # PcP
    pc = titik(14, rc)
    ax.plot([titik(0)[0], pc[0]], [titik(0)[1], pc[1]], color=K, lw=1.0,
            ls="-", zorder=4)
    ax.plot([pc[0], titik(28)[0]], [pc[1], titik(28)[1]], color=K, lw=1.0,
            zorder=4)
    ax.text(*(titik(9, 0.62)), "PcP", fontsize=7.5, ha="center")
    # PKP: mantel -> inti luar -> mantel
    p1 = titik(52, rc)
    p2 = titik(128, rc)
    ax.plot([titik(0)[0], p1[0]], [titik(0)[1], p1[1]], color=K, lw=1.0,
            ls="--", zorder=4)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=K, lw=1.0, ls="--",
            zorder=4)
    ax.plot([p2[0], titik(168)[0]], [p2[1], titik(168)[1]], color=K, lw=1.0,
            ls="--", zorder=4)
    ax.text(*(titik(92, 0.30)), "PKP", fontsize=7.5, ha="center")
    # daerah bayangan
    th1 = np.degrees(a0 - np.radians(143))
    th2 = np.degrees(a0 - np.radians(103))
    ax.add_patch(Wedge((0, 0), 1.155, th1, th2, width=0.14, fc=G3,
                       ec="none", zorder=2))
    for d in (103, 143):
        q = titik(d, 1.02)
        ax.plot([0, q[0] * 1.14], [0, q[1] * 1.14], color=G2, lw=0.6, ls=":",
                zorder=1)
    qm = titik(123, 1.30)
    ax.text(qm[0], qm[1], "daerah bayangan P\n$103°-143°$", fontsize=6.2,
            ha="center", va="center")
    for d in (0, 45, 90, 135, 180):
        q = titik(d, 1.0)
        ax.plot([q[0], q[0] * 1.035], [q[1], q[1] * 1.035], color=K, lw=0.7,
                zorder=5)
    simpan(fig, "gbr-3-6-fase.png")


# ---------------------------------------------------------- Gambar 3.7 & 3.8
def g37_g38():
    from obspy.taup import TauPyModel
    model = TauPyModel(model="ak135")
    fig, ax = plt.subplots(figsize=(5.4, 4.0))
    fases = {"P": "-", "PP": "--", "S": "-", "SS": "--",
             "PKIKP": ":", "ScS": "-."}
    warna = {"P": K, "PP": G1, "S": K, "SS": G1, "PKIKP": K, "ScS": G1}
    for ph, ls in fases.items():
        d, t = [], []
        for dist in np.arange(1, 180, 1.0):
            try:
                arr = model.get_travel_times(source_depth_in_km=0.0,
                                             distance_in_degree=dist,
                                             phase_list=[ph])
            except Exception:
                continue
            if arr:
                d.append(dist); t.append(arr[0].time / 60.0)
        if d:
            ax.plot(d, t, ls, color=warna[ph], lw=1.2)
            ax.text(d[len(d) // 2], t[len(t) // 2] + 0.6, ph, fontsize=7,
                    color=warna[ph],
                    bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.85))
    ax.axvspan(103, 143, color=G3, alpha=0.55)
    ax.text(123, 2.0, "daerah\nbayangan P", fontsize=6.4, ha="center")
    ax.set_xlabel("Jarak episenter $\\Delta$ (derajat)")
    ax.set_ylabel("Waktu tempuh (menit)")
    ax.set_xlim(0, 180); ax.set_ylim(0, 45)
    ax.grid(True, lw=0.3, color=G3)
    ax.set_title("Kurva waktu tempuh, model ak135, sumber di permukaan",
                 fontsize=8.5)
    simpan(fig, "gbr-3-7-waktu-tempuh.png")

    # Gambar 3.8 - model kecepatan
    m = model.model.s_mod.v_mod
    z = np.linspace(0, 6370.5, 3000)
    vp = np.array([float(np.atleast_1d(m.evaluate_below(zz, "p"))[0])
                   for zz in z])
    vs = np.array([float(np.atleast_1d(m.evaluate_below(zz, "s"))[0])
                   for zz in z])
    fig, ax = plt.subplots(figsize=(3.6, 4.4))
    ax.plot(vp, z, color=K, lw=1.4, label="$v_p$")
    ax.plot(vs, z, color=G1, lw=1.4, ls="--", label="$v_s$")
    for zz, lab in [(410, "410"), (660, "660"), (2891, "CMB 2891"),
                    (5150, "ICB 5150")]:
        ax.axhline(zz, color=G2, lw=0.6, ls=":")
        ax.text(13.6, zz - 60, lab, fontsize=6.0, ha="right", color=G1)
    ax.set_ylim(6371, 0)
    ax.set_xlim(0, 14.5)
    ax.set_xlabel("Kecepatan (km/s)")
    ax.set_ylabel("Kedalaman (km)")
    ax.legend(loc="lower left", frameon=False)
    ax.set_title("Model ak135", fontsize=8.5)
    ax.grid(True, lw=0.3, color=G3)
    simpan(fig, "gbr-3-8-model-ak135.png")


# ---------------------------------------------------------------- Gambar 3.9
def g39():
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.7),
                             constrained_layout=True)
    putih = dict(fc="white", ec="none", pad=0.8, alpha=0.9)
    for ax, judul, lapisan, sx in [
            (axes[0], "(a) kerak benua",
             [(0, 18, "granit", "#ffffff"), (18, 35, "basalt", FILL),
              (35, 45, "mantel", G3)], 14),
            (axes[1], "(b) kerak samudra",
             [(0, 5, "air laut", "#eef2f5"), (5, 11, "basalt", FILL),
              (11, 22, "mantel", G3)], 14)]:
        bersih(ax); ax.set_aspect("auto")
        atas = lapisan[0][0]
        bawah = lapisan[-1][1]
        ax.set_xlim(0, 100); ax.set_ylim(bawah, -0.09 * bawah)
        for y0, y1, nm, c in lapisan:
            ax.add_patch(Rectangle((0, y0), 100, y1 - y0, fc=c, ec=K, lw=0.9))
        # nama lapisan di tepi kiri, di bawah garis batasnya
        for y0, y1, nm, c in lapisan:
            ax.text(2.5, y0 + 0.26 * (y1 - y0), nm, fontsize=6.3,
                    va="center", ha="left", bbox=putih)
        # sumber gempa
        ysrc = lapisan[0][1] * 0.55 if "benua" in judul else 7.6
        ax.plot(sx, ysrc, "*", color=K, ms=9, zorder=4)
        mid = lapisan[1][0]
        moh = lapisan[2][0]
        # fase langsung, fase Conrad, dan fase Moho
        if "benua" in judul:
            jalur = [((sx, ysrc), (86, atas), "-", "Pg / Sg", 0.62),
                     ((sx, ysrc), (30, mid), (78, mid), (92, atas), "--",
                      "P* / S*", 0.50),
                     ((sx, ysrc), (34, moh), (80, moh), (95, atas), ":",
                      "Pn / Sn", 0.72)]
        else:
            jalur = [((sx, ysrc), (88, atas), "-", "P* / S*", 0.60),
                     ((sx, ysrc), (32, moh), (80, moh), (95, atas), ":",
                      "Pn / Sn", 0.72)]
        for item in jalur:
            *titik, sty, nm, fr = item
            xs = [t[0] for t in titik]; ys = [t[1] for t in titik]
            ax.plot(xs, ys, color=K, lw=1.0, ls=sty)
            # label di tengah penggal mendatar atau di tengah lintasan
            if len(titik) == 2:
                lx = xs[0] + fr * (xs[1] - xs[0])
                ly = ys[0] + fr * (ys[1] - ys[0])
            else:
                lx = (xs[1] + xs[2]) / 2
                ly = ys[1] - 0.045 * bawah      # sedikit di atas bidang batas
            ax.text(lx, ly, nm, fontsize=6.3, ha="center", va="center",
                    bbox=putih, zorder=5)
        # penanda bidang batas di luar kerangka gambar
        tanda = [(atas, "O"), (moh, "M")]
        if "benua" in judul:
            tanda.insert(1, (mid, "C"))
        for y, nm in tanda:
            ax.text(101.5, y, nm, fontsize=7, ha="left", va="center",
                    clip_on=False)
        ax.set_title(judul, fontsize=8.2)
    simpan(fig, "gbr-3-9-kerak.png")


# --------------------------------------------------------------- Gambar 3.10
def g310():
    fig, axes = plt.subplots(2, 1, figsize=(5.2, 2.7), sharex=True)
    t = np.linspace(0, 60, 2000)
    for ax, gr, lab in [(axes[0], 0.045, "(a) gradien kecepatan kecil"),
                        (axes[1], 0.11, "(b) gradien kecepatan lebih besar")]:
        f = 0.30 - gr * 0.012 * t
        y = np.sin(2 * np.pi * np.cumsum(f) * (t[1] - t[0]))
        env = np.exp(-((t - 30) / (9 + gr * 130))**2)
        ax.plot(t, y * env, color=K, lw=0.9)
        ax.set_yticks([]); ax.set_title(lab, fontsize=7.8, loc="left")
        for s in ["top", "right", "left"]:
            ax.spines[s].set_visible(False)
    axes[1].set_xlabel("Waktu (s)")
    simpan(fig, "gbr-3-10-dispersi.png")


# --------------------------------------------------------------- Gambar 3.11
def g311():
    """Kecepatan fase dan kecepatan grup dari interferensi dua frekuensi."""
    fig, axes = plt.subplots(3, 1, figsize=(5.28, 3.3), sharex=True)
    fig.subplots_adjust(left=0.035, right=0.985, top=0.965, bottom=0.115,
                        hspace=0.42)
    x = np.linspace(0, 60, 2500)
    y1 = np.sin(2 * np.pi * x / 6.0)
    y2 = np.sin(2 * np.pi * x / 6.7)
    for ax, y, lab, ylim in [
            (axes[0], y1, "(a) satu frekuensi", 1.75),
            (axes[1], y2, "(b) frekuensi sedikit berbeda", 1.75),
            (axes[2], y1 + y2, "(c) hasil interferensi", 3.6)]:
        ax.plot(x, y, color=K, lw=0.9)
        ax.set_yticks([]); ax.set_ylim(-ylim, ylim)
        ax.text(0.0, ylim * 0.97, lab, fontsize=7.0, ha="left", va="top")
        for sp in ("top", "right", "left"):
            ax.spines[sp].set_visible(False)
        ax.spines["bottom"].set_linewidth(0.7)
        if ax is not axes[2]:
            ax.tick_params(bottom=False, labelbottom=False)
    env = 2 * np.abs(np.cos(np.pi * x * (1 / 6.0 - 1 / 6.7)))
    axes[2].plot(x, env, color=G1, lw=0.9, ls="--")
    axes[2].plot(x, -env, color=G1, lw=0.9, ls="--")
    axes[2].annotate("amplop menjalar dengan kecepatan grup $U$",
                     xy=(20.9, 2.02), xytext=(30.5, 3.15), fontsize=6.2,
                     color=G1, ha="center", va="center",
                     arrowprops=dict(arrowstyle="->", lw=0.7, color=G1,
                                     shrinkA=1, shrinkB=2))
    axes[2].annotate("puncak menjalar dengan kecepatan fase $c$",
                     xy=(9.0, -1.55), xytext=(30.0, -2.80), fontsize=6.2,
                     color=G1, ha="center", va="center",
                     bbox=dict(fc="white", ec="none", pad=1.0, alpha=0.9),
                     arrowprops=dict(arrowstyle="->", lw=0.7, color=G1,
                                     shrinkA=1, shrinkB=2))
    axes[2].set_xlabel("Jarak", fontsize=7.5)
    axes[2].tick_params(labelsize=6.6)
    simpan(fig, "gbr-3-11-grup-fase.png")


# --------------------------------------------------------------- Gambar 3.12
def g312():
    fig, axes = plt.subplots(1, 4, figsize=(6.4, 1.95))
    modes = [("$_0S_0$", "radial"), ("$_0S_2$", "sferoidal $l=2$"),
             ("$_0T_2$", "torsional $l=2$"), ("$_0S_3$", "sferoidal $l=3$")]
    for ax, (nm, ket) in zip(axes, modes):
        bersih(ax); ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.35, 1.35)
        ax.add_patch(Circle((0, 0), 1.0, fc="white", ec=K, lw=1.3))
        if nm == "$_0S_0$":
            ax.add_patch(Circle((0, 0), 1.13, fc="none", ec=G2, lw=0.8,
                                ls="--"))
            for a in np.linspace(0, 2 * np.pi, 12, endpoint=False):
                panah(ax, (0.95 * np.cos(a), 0.95 * np.sin(a)),
                      (1.22 * np.cos(a), 1.22 * np.sin(a)), lw=0.6, color=G1)
            ax.text(0, 0, "U", fontsize=7, ha="center", va="center")
        elif "S_2" in nm:
            for y in [0.5, -0.5]:
                ax.plot([-0.87, 0.87], [y, y], color=G1, lw=0.8, ls="--")
            for yy, s in [(0.78, "U"), (0.0, "D"), (-0.78, "U")]:
                ax.text(0, yy, s, fontsize=7, ha="center", va="center")
        elif "T_2" in nm:
            for y in [0.5, -0.5]:
                ax.plot([-0.87, 0.87], [y, y], color=G1, lw=0.8, ls="--")
            for yy, d in [(0.75, 1), (0.0, -1), (-0.75, 1)]:
                panah(ax, (-0.3 * d, yy), (0.3 * d, yy), lw=0.8, color=K)
        else:
            for y in [0.7, 0.0, -0.7]:
                r = np.sqrt(max(1 - y**2, 0.02))
                ax.plot([-r, r], [y, y], color=G1, lw=0.8, ls="--")
            for yy, s in [(0.87, "U"), (0.35, "D"), (-0.35, "U"),
                          (-0.87, "D")]:
                ax.text(0, yy, s, fontsize=6.4, ha="center", va="center")
        ax.set_title(f"{nm}\n{ket}", fontsize=7.2)
    simpan(fig, "gbr-3-12-mode.png")


if __name__ == "__main__":
    print("Bab 1-3:")
    for f in [g11, g12, g21, g22, g23, g24, g25, g26, g27, g28, g29, g210,
              g31, g32, g33, g34, g35, g36, g37_g38, g39, g310, g311, g312]:
        f()
