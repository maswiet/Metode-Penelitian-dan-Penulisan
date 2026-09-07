"""Gambar untuk Bab 1-3."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, Wedge, Polygon
from gaya import simpan, kotak, panah, bersih, K, G1, G2, G3, FILL


# ---------------------------------------------------------------- Gambar 1.1
def g11():
    fig, ax = plt.subplots(figsize=(6.3, 4.1))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6.6); bersih(ax)
    ax.set_aspect("auto")

    kotak(ax, 5, 6.15, 2.4, 0.55, "GEOSAINS", fs=9, fc=G3, lw=1.2,
          fontweight="bold")

    l1 = ["GEOLOGI", "GEOGRAFI", "GEODESI", "GEOFISIKA"]
    xs1 = [1.3, 3.4, 5.5, 8.0]
    for x, t in zip(xs1, l1):
        fc = FILL if t == "GEOFISIKA" else "white"
        kotak(ax, x, 5.05, 1.85, 0.5, t, fs=7.5, fc=fc,
              lw=1.2 if t == "GEOFISIKA" else 0.9)
        panah(ax, (5, 5.87), (x, 5.32), lw=0.7, color=G1)

    l2 = ["METEOROLOGI", "OSEANOGRAFI", "HIDROLOGI",
          "GEOKOSMOFISIKA\n(ionosfer)", "GEOFISIKA\nBUMI PADAT"]
    xs2 = [1.15, 3.0, 4.7, 6.5, 8.75]
    for x, t in zip(xs2, l2):
        fc = FILL if "BUMI PADAT" in t else "white"
        kotak(ax, x, 3.85, 1.75, 0.62, t, fs=6.6, fc=fc,
              lw=1.2 if "BUMI PADAT" in t else 0.9)
        panah(ax, (8.0, 4.78), (x, 4.19), lw=0.7, color=G1)

    l3 = ["SEISMOLOGI", "VULKANOLOGI", "GEOMAGNETISME", "GEOELEKTRISITAS",
          "TEKTONOFISIKA", "GRAVITASI", "GEOTERMAL", "GEOKOSMOGONI",
          "GEOKRONOLOGI"]
    for i, t in enumerate(l3):
        col = i % 3
        row = i // 3
        x = 2.1 + col * 2.9
        y = 2.45 - row * 0.75
        fc = G3 if t == "SEISMOLOGI" else "white"
        kotak(ax, x, y, 2.55, 0.5, t, fs=6.8, fc=fc,
              lw=1.3 if t == "SEISMOLOGI" else 0.8,
              fontweight="bold" if t == "SEISMOLOGI" else "normal")
    ax.plot([8.75, 8.75], [3.54, 2.9], lw=0.7, color=G1)
    ax.plot([2.1, 7.9], [2.9, 2.9], lw=0.7, color=G1)
    for col in range(3):
        ax.plot([2.1 + col * 2.9] * 2, [2.9, 2.70], lw=0.7, color=G1)
    simpan(fig, "gbr-1-1-geosains.png")


# ---------------------------------------------------------------- Gambar 1.2
def g12():
    fig, ax = plt.subplots(figsize=(4.2, 3.0))
    x = np.linspace(0, 10, 400)
    y = 9.4 * (1 - np.exp(-0.55 * x))
    ax.plot(x, y, color=K, lw=1.8)
    ax.axvline(2.4, color=G2, ls=":", lw=1.0)
    ax.text(1.1, 8.6, "fase A", fontsize=10, ha="center", fontweight="bold")
    ax.text(6.6, 8.6, "fase B", fontsize=10, ha="center", fontweight="bold")
    ax.annotate("", xy=(2.4, 1.2), xytext=(0.55, 1.2),
                arrowprops=dict(arrowstyle="<->", lw=0.9, color=G1))
    ax.text(1.45, 0.65, "input kecil", fontsize=7, ha="center", color=G1)
    ax.annotate("", xy=(0.35, 6.6), xytext=(0.35, 1.4),
                arrowprops=dict(arrowstyle="<->", lw=0.9, color=G1))
    ax.text(0.75, 4.0, "output\nbesar", fontsize=7, va="center", color=G1)
    ax.annotate("", xy=(9.6, 8.35), xytext=(3.2, 8.35),
                arrowprops=dict(arrowstyle="<->", lw=0.9, color=G1))
    ax.text(6.4, 7.75, "input besar", fontsize=7, ha="center", color=G1)
    ax.annotate("", xy=(9.85, 9.35), xytext=(9.85, 8.5),
                arrowprops=dict(arrowstyle="<->", lw=0.9, color=G1))
    ax.text(9.6, 8.95, "output\nkecil", fontsize=7, ha="right", va="center",
            color=G1)
    ax.set_xlabel("INPUT (usaha, dana, kerumitan)")
    ax.set_ylabel("OUTPUT (ketelitian hasil)")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 10.4); ax.set_ylim(0, 10.2)
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
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.7))
    eps = [0.2, 0.5, 1.0, 2.0]
    wn = 1.0
    w = np.linspace(0.001, 3.0, 800)
    ax = axes[0]
    for e in eps:
        H = 1.0 / np.sqrt((wn**2 - w**2)**2 + 4 * e**2 * wn**2 * w**2)
        ax.plot(w, H, color=K, lw=1.1)
        if e == 0.2:
            ax.text(1.02, 2.62, r"$\varepsilon=0{,}2$", fontsize=7)
        if e == 2.0:
            ax.text(1.55, 0.28, r"$\varepsilon=2$", fontsize=7)
    ax.set_xlabel(r"$\omega/\omega_n$"); ax.set_ylabel(r"$|S_0/I_0|$")
    ax.set_ylim(0, 3.0); ax.set_xlim(0, 3)
    ax.axvline(1, color=G2, ls=":", lw=0.8)
    ax.set_title("(a) skala linear", fontsize=8.5)
    ax = axes[1]
    w = np.logspace(-1.3, 1.3, 800)
    for e in eps:
        H = 1.0 / np.sqrt((wn**2 - w**2)**2 + 4 * e**2 * wn**2 * w**2)
        ax.loglog(w, H, color=K, lw=1.1)
    ax.loglog(w[w > 1.6], 1 / w[w > 1.6]**2, color=G2, ls="--", lw=0.9)
    ax.text(4.5, 0.02, "kemiringan\n$-12$ dB/oktaf", fontsize=6.5, color=G1)
    ax.axvline(1, color=G2, ls=":", lw=0.8)
    ax.set_xlabel(r"$\omega/\omega_n$"); ax.set_ylabel(r"$|S_0/I_0|$")
    ax.set_title("(b) skala logaritmik", fontsize=8.5)
    simpan(fig, "gbr-2-3-orde2.png")


# ---------------------------------------------------------------- Gambar 2.4
def g24():
    fig, ax = plt.subplots(figsize=(3.5, 3.0))
    bersih(ax); ax.set_xlim(0, 6.5); ax.set_ylim(0, 6)
    ax.add_patch(Rectangle((0.8, 1.0), 4.4, 4.2, fc="none", ec=K, lw=1.3))
    ax.text(1.05, 4.9, "kerangka", fontsize=6.5, color=G1)
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
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.7))
    wn = 1.0
    ax = axes[0]
    w = np.linspace(0.001, 4.0, 900)
    for e in [0.2, 0.5, 0.707, 1.0, 2.0]:
        H = w**2 / np.sqrt((wn**2 - w**2)**2 + 4 * e**2 * wn**2 * w**2)
        ax.plot(w, H, color=K, lw=1.1)
    ax.axhline(1, color=G2, ls=":", lw=0.8)
    ax.axvline(1, color=G2, ls=":", lw=0.8)
    ax.text(0.35, 2.35, r"$\varepsilon$ kecil", fontsize=7)
    ax.text(3.0, 1.09, "1", fontsize=7)
    ax.set_xlabel(r"$\omega/\omega_n$"); ax.set_ylabel(r"$|Z_0/X_0|$")
    ax.set_ylim(0, 2.7); ax.set_xlim(0, 4)
    ax.set_title("(a) skala linear", fontsize=8.5)
    ax = axes[1]
    w = np.logspace(-1.5, 1.5, 800)
    H = w**2 / np.sqrt((wn**2 - w**2)**2 + 4 * 0.707**2 * wn**2 * w**2)
    ax.loglog(w, H, color=K, lw=1.4)
    ax.loglog([0.03, 1], [0.03**2, 1], color=G2, ls="--", lw=0.9)
    ax.loglog([1, 32], [1, 1], color=G2, ls="--", lw=0.9)
    ax.text(0.09, 0.02, "+12 dB/oktaf", fontsize=6.8, color=G1, rotation=42)
    ax.text(3.0, 1.25, "0 dB/oktaf", fontsize=6.8, color=G1)
    ax.axvline(1, color=G2, ls=":", lw=0.8)
    ax.text(1.08, 0.003, r"$\omega_n$", fontsize=8)
    ax.set_xlabel(r"$\omega/\omega_n$"); ax.set_ylabel(r"$|Z_0/X_0|$")
    ax.set_title("(b) idealisasi asimtotik", fontsize=8.5)
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
        ax.text(0.055, y[3] * 2.2, f"{s1:+d}", fontsize=6.8, color=G1)
        ax.text(8.0, y[-1] * 1.6, f"{s2:+d}", fontsize=6.8, color=G1)
        ax.set_yticks([])


def g26():
    fig, axes = plt.subplots(1, 3, figsize=(6.5, 2.2))
    _sens(fig, axes, extra=0)
    axes[0].set_ylabel("sensitivitas")
    simpan(fig, "gbr-2-6-sensitivitas.png")


def g27():
    fig, axes = plt.subplots(1, 3, figsize=(6.5, 2.2))
    _sens(fig, axes, extra=1)
    axes[0].set_ylabel("sensitivitas")
    fig.suptitle("seismometer elektromagnetik (keluaran sebanding kecepatan)",
                 fontsize=8, y=1.06)
    simpan(fig, "gbr-2-7-elektromagnetik.png")


# ---------------------------------------------------------------- Gambar 2.8
def g28():
    fig, axes = plt.subplots(1, 3, figsize=(6.4, 2.5))
    for ax in axes:
        bersih(ax); ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax = axes[0]
    ax.plot([0.8, 4.2], [4.5, 4.5], color=K, lw=1.2)
    for xh in np.arange(0.9, 4.3, 0.38):
        ax.plot([xh, xh - 0.2], [4.5, 4.25], color=G2, lw=0.7)
    ys = np.linspace(4.5, 3.0, 180)
    ax.plot(2.5 + 0.16 * np.sin(np.linspace(0, 12 * np.pi, 180)), ys,
            color=K, lw=1.0)
    ax.add_patch(Circle((2.5, 2.6), 0.38, fc=FILL, ec=K, lw=1.2))
    ax.set_title("(a) pendulum vertikal\nsederhana", fontsize=7.5)
    ax = axes[1]
    ax.plot([0.6, 4.4], [4.5, 4.5], color=K, lw=1.2)
    for xh in np.arange(0.7, 4.4, 0.38):
        ax.plot([xh, xh - 0.2], [4.5, 4.25], color=G2, lw=0.7)
    ax.plot([1.0, 4.0], [2.2, 2.2], color=K, lw=1.6)
    ax.add_patch(Circle((4.0, 2.2), 0.32, fc=FILL, ec=K, lw=1.2))
    ax.add_patch(Circle((1.0, 2.2), 0.09, fc=K, ec=K))
    xs = np.linspace(1.05, 3.1, 160)
    ax.plot(xs, np.linspace(4.5, 2.35, 160) +
            0.13 * np.sin(np.linspace(0, 13 * np.pi, 160)), color=K, lw=1.0)
    ax.text(1.9, 3.1, "pegas\npanjang-nol", fontsize=6.2, color=G1)
    ax.set_title("(b) suspensi LaCoste", fontsize=7.5)
    ax = axes[2]
    ax.plot([2.4, 2.4], [0.8, 4.5], color=K, lw=1.4)
    ax.plot([2.4, 4.1], [3.9, 3.35], color=K, lw=1.4)
    ax.add_patch(Circle((4.1, 3.35), 0.3, fc=FILL, ec=K, lw=1.2))
    ax.plot([2.4, 4.1], [1.3, 3.2], color=G1, lw=0.9, ls="--")
    a = Arc((2.4, 4.5), 1.4, 1.4, theta1=250, theta2=285, color=G1, lw=0.8)
    ax.add_patch(a)
    ax.text(2.62, 4.05, r"$\theta$ kecil", fontsize=6.2, color=G1)
    ax.set_title("(c) pendulum\n$garden$-$gate$ (horizontal)", fontsize=7.5)
    simpan(fig, "gbr-2-8-konfigurasi.png")


# ---------------------------------------------------------------- Gambar 2.9
def g29():
    fig, ax = plt.subplots(figsize=(6.4, 2.5))
    ax.set_xlim(0, 15.6); ax.set_ylim(0, 4.2); bersih(ax); ax.set_aspect("auto")
    lab = ["Gerakan\ntanah", "Sensor\n(pita lebar /\nakselerometer)",
           "Digitizer\n24 bit\n+ GNSS", "Telemetri\n(VSAT, seluler,\nserat)",
           "Pusat data\nminiSEED +\nStationXML", "Pengolahan\notomatis\n(SeisComP)",
           "Katalog,\nShakeMap,\nperingatan"]
    xs = np.linspace(1.1, 14.5, 7)
    for x, t in zip(xs, lab):
        kotak(ax, x, 2.6, 2.05, 1.25, t, fs=6.3,
              fc=FILL if "Sensor" in t or "Digitizer" in t else "white")
    for i in range(6):
        panah(ax, (xs[i] + 1.05, 2.6), (xs[i + 1] - 1.05, 2.6), lw=0.9)
    ket = ["besaran\nfisis", "tegangan\nanalog", "cacahan\n(counts)",
           "paket\ndata", "berkas\nterarsip", "parameter\ngempa"]
    for i, t in enumerate(ket):
        ax.text((xs[i] + xs[i + 1]) / 2, 1.45, t, fontsize=5.6, ha="center",
                va="top", color=G1, style="italic")
    ax.text(7.8, 0.32, "Kualitas rekaman ditentukan oleh mata rantai terlemah",
            fontsize=6.8, ha="center", color=G1)
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
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    bersih(ax); ax.set_xlim(0, 10); ax.set_ylim(0, 7)
    ax.axhline(3.5, color=K, lw=1.3)
    ax.fill_between([0, 10], 0, 3.5, color=FILL)
    ax.text(0.3, 3.75, "medium 1: $v_{p1}, v_{s1}$", fontsize=7)
    ax.text(0.3, 3.0, "medium 2: $v_{p2}, v_{s2}\\ (>v_1)$", fontsize=7)
    O = (5.0, 3.5)
    panah(ax, (1.6, 6.6), O, lw=1.4)
    ax.text(2.4, 6.2, "P datang", fontsize=7)
    panah(ax, O, (8.4, 6.6), lw=1.2)
    ax.text(7.6, 6.3, "P pantul", fontsize=6.8)
    panah(ax, O, (7.3, 6.85), lw=1.0, ls="--")
    ax.text(6.15, 6.75, "SV pantul", fontsize=6.8)
    panah(ax, O, (7.9, 0.8), lw=1.2)
    ax.text(8.0, 1.35, "P bias", fontsize=6.8)
    panah(ax, O, (6.6, 0.6), lw=1.0, ls="--")
    ax.text(5.6, 0.75, "SV bias", fontsize=6.8)
    ax.plot([5, 5], [0.3, 6.9], color=G2, ls=":", lw=0.9)
    ax.text(5.06, 6.75, "normal", fontsize=6.2, color=G1)
    ax.add_patch(Arc(O, 2.0, 2.0, theta1=112, theta2=90, color=G1, lw=0.8))
    ax.text(4.45, 4.62, "$i_1$", fontsize=8)
    ax.add_patch(Arc(O, 2.0, 2.0, theta1=90, theta2=112 + 45, color="none"))
    ax.add_patch(Arc(O, 2.4, 2.4, theta1=68, theta2=90, color=G1, lw=0.8))
    ax.text(5.5, 4.72, "$r_1$", fontsize=8)
    ax.add_patch(Arc(O, 2.4, 2.4, theta1=270, theta2=292, color=G1, lw=0.8))
    ax.text(5.5, 2.25, "$i_1'$", fontsize=8)
    simpan(fig, "gbr-3-2-snell.png")


# ---------------------------------------------------------------- Gambar 3.3
def g33():
    fig, ax = plt.subplots(figsize=(4.8, 3.0))
    bersih(ax); ax.set_xlim(0, 11); ax.set_ylim(0, 6.4); ax.set_aspect("auto")
    for y, lab in [(5.0, "$v_1$"), (3.4, "$v_2 > v_1$"), (1.6, "$v_3 > v_2$")]:
        ax.axhline(y, color=K, lw=1.0)
        ax.text(0.15, y - 0.55, lab, fontsize=7.5)
    ax.axhline(6.2, color=K, lw=1.3)
    src = (1.2, 6.2)
    for p, sty, nm in [(0.10, "-", "berkas I ($p_1$)"),
                       (0.16, "--", "berkas II ($p_2>p_1$)")]:
        x = src[0]; y = src[1]
        pts = [(x, y)]
        for v, ytop, ybot in [(1.0, 6.2, 5.0), (1.5, 5.0, 3.4),
                              (2.2, 3.4, 1.6), (3.0, 1.6, 0.3)]:
            s = np.clip(p * v, 0, 0.999)
            th = np.arcsin(s)
            dy = ytop - ybot
            x = x + dy * np.tan(th)
            y = ybot
            pts.append((x, y))
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], color=K, lw=1.2, ls=sty)
        ax.text(pts[-1, 0] + 0.15, 0.45, nm, fontsize=6.5)
    ax.add_patch(Circle(src, 0.14, fc=K))
    ax.text(0.75, 5.85, "sumber", fontsize=6.5)
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
    fig, ax = plt.subplots(figsize=(5.2, 2.9))
    bersih(ax); ax.set_xlim(0, 12); ax.set_ylim(0, 5.6); ax.set_aspect("auto")
    ax.axhline(4.8, color=K, lw=1.2)
    ax.axhline(2.0, color=K, lw=1.4)
    ax.fill_between([0, 12], 0, 2.0, color=FILL)
    ax.text(0.2, 2.2, "$v_1$", fontsize=8)
    ax.text(0.2, 1.4, "$v_2 > v_1$", fontsize=8)
    S = (1.4, 4.8)
    ax.add_patch(Circle(S, 0.13, fc=K))
    ax.text(1.4, 5.1, "sumber", fontsize=6.5, ha="center")
    ic = 3.6
    ax.plot([S[0], ic], [4.8, 2.0], color=K, lw=1.3)
    ax.plot([ic, 9.6], [2.0, 2.0], color=K, lw=1.6)
    for xx in np.linspace(4.2, 9.4, 6):
        ax.plot([xx, xx + 2.2], [2.0, 4.8], color=K, lw=0.8)
        th = np.linspace(0, np.pi, 60)
    ax.plot([9.6, 11.4], [2.0, 4.8], color=K, lw=1.3)
    ax.plot([S[0], 11.0], [4.8, 4.8], color=G2, lw=0.9, ls="--")
    ax.text(6.4, 4.95, "gelombang langsung", fontsize=6.3, color=G1)
    ax.text(6.0, 1.65, "menjalar dengan $v_2$", fontsize=6.3, color=G1)
    ax.text(9.0, 3.2, "muka gelombang\nkepala", fontsize=6.3, color=G1)
    ax.text(2.05, 3.3, "$i_c$", fontsize=8)
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
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.6))
    for ax, judul, lapisan in [
            (axes[0], "(a) kerak benua",
             [(0, 18, "granit", "#ffffff"), (18, 35, "basalt", FILL),
              (35, 45, "mantel", G3)]),
            (axes[1], "(b) kerak samudra",
             [(0, 5, "air laut", "#eef2f5"), (5, 11, "basalt", FILL),
              (11, 22, "mantel", G3)])]:
        bersih(ax); ax.set_aspect("auto")
        ax.set_xlim(0, 100); ax.set_ylim(45 if "benua" in judul else 22, -6)
        for y0, y1, nm, c in lapisan:
            ax.add_patch(Rectangle((0, y0), 100, y1 - y0, fc=c, ec=K, lw=0.9))
            ax.text(2, (y0 + y1) / 2, nm, fontsize=6.5, va="center")
        top = lapisan[0][0]
        src = (12, lapisan[0][1] * 0.55 if "benua" in judul else 7.5)
        ax.plot(*src, "*", color=K, ms=9)
        ax.plot([src[0], 82], [src[1], top], color=K, lw=1.0)
        ax.text(46, (src[1] + top) / 2 - 1.2, "Pg / Sg", fontsize=6.3)
        mid = lapisan[1][0]
        ax.plot([src[0], 30, 72, 88], [src[1], mid, mid, top], color=K,
                lw=1.0, ls="--")
        ax.text(50, mid - 1.2, "P* / S*", fontsize=6.3)
        moh = lapisan[2][0]
        ax.plot([src[0], 34, 78, 92], [src[1], moh, moh, top], color=K,
                lw=1.0, ls=":")
        ax.text(55, moh - 1.3, "Pn / Sn", fontsize=6.3)
        ax.text(96, top - 1.5, "O", fontsize=7, ha="right")
        if "benua" in judul:
            ax.text(96, mid - 1.5, "C", fontsize=7, ha="right")
        ax.text(96, moh - 1.5, "M", fontsize=7, ha="right")
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
    fig, axes = plt.subplots(3, 1, figsize=(5.2, 3.2), sharex=True)
    x = np.linspace(0, 60, 2500)
    y1 = np.sin(2 * np.pi * x / 6.0)
    y2 = np.sin(2 * np.pi * x / 6.7)
    for ax, y, lab in [(axes[0], y1, "(a) satu frekuensi"),
                       (axes[1], y2, "(b) frekuensi sedikit berbeda"),
                       (axes[2], y1 + y2, "(c) hasil interferensi")]:
        ax.plot(x, y, color=K, lw=0.9)
        ax.set_yticks([]); ax.set_title(lab, fontsize=7.6, loc="left")
        for s in ["top", "right", "left"]:
            ax.spines[s].set_visible(False)
    env = 2 * np.abs(np.cos(np.pi * x * (1 / 6.0 - 1 / 6.7)))
    axes[2].plot(x, env, color=G1, lw=0.9, ls="--")
    axes[2].plot(x, -env, color=G1, lw=0.9, ls="--")
    axes[2].annotate("amplop menjalar\ndengan kecepatan grup $U$",
                     xy=(21, 1.9), xytext=(30, 2.6), fontsize=6.4, color=G1,
                     arrowprops=dict(arrowstyle="->", lw=0.7, color=G1))
    axes[2].set_xlabel("Jarak")
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
