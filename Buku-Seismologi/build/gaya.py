"""Gaya bersama untuk semua gambar buku Pengantar Seismologi."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
os.makedirs(FIGDIR, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9.5,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.3,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.03,
    "mathtext.fontset": "dejavuserif",
})

# Palet abu-abu ramah cetak hitam-putih
K = "#111111"     # garis utama
G1 = "#4a4a4a"    # garis sekunder
G2 = "#8a8a8a"    # garis bantu
G3 = "#c9c9c9"    # arsir muda
FILL = "#e6e6e6"  # isian


def simpan(fig, nama):
    path = os.path.join(FIGDIR, nama)
    fig.savefig(path)
    plt.close(fig)
    print("  ->", os.path.basename(path))


def kotak(ax, x, y, w, h, teks, fs=7.5, fc="white", ec=K, lw=0.9, **kw):
    """Kotak berlabel, koordinat pusat."""
    from matplotlib.patches import FancyBboxPatch
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                       boxstyle="round,pad=0.012,rounding_size=0.02",
                       fc=fc, ec=ec, lw=lw, zorder=3)
    ax.add_patch(p)
    ax.text(x, y, teks, ha="center", va="center", fontsize=fs, zorder=4, **kw)
    return p


def panah(ax, xy_from, xy_to, lw=0.9, ls="-", color=K, **kw):
    ax.annotate("", xy=xy_to, xytext=xy_from,
                arrowprops=dict(arrowstyle="-|>", lw=lw, ls=ls,
                                color=color, shrinkA=1, shrinkB=1,
                                mutation_scale=9), zorder=2, **kw)


def bersih(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_aspect("equal")
