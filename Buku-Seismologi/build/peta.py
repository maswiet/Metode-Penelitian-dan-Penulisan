"""Perkakas peta: pemuat data dan latar bayangan relief.

Data yang dipakai (semuanya tersimpan di dalam ../data):
  relief-indonesia.png   bayangan relief Natural Earth GRAY_HR_SR_OB,
                         1 menit busur, domain publik
  garis-pantai.csv       garis pantai Natural Earth 1:10 juta
  pusgen2024-sesar.csv   401 jalur sesar aktif PuSGeN 2024
  bird2003-batas.csv     ruas batas lempeng Bird (2003) beserta kelas,
                         laju, dan azimut gerak relatif
  bird2003-lempeng.csv   poligon lempeng Bird (2003)
"""
import csv
import json
import os

import numpy as np
from matplotlib.path import Path

import gaya

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

# Lempeng atas pada setiap zona subduksi. Tata nama Bird (2003) memakai
# "/" dan "\" yang menggambarkan arah tunjaman: pada "A/B" bidang menurun
# dari sisi B ke sisi A, sehingga B adalah lempeng bawah dan A lempeng atas;
# pada "A\B" berlaku sebaliknya.
KELAS = {"SUB": "subduksi", "OSR": "pematang", "OTF": "transform samudra",
         "CTF": "transform benua", "OCB": "konvergen samudra",
         "CCB": "konvergen benua", "CRB": "regangan benua"}

NAMA_LEMPENG = {
    "SU": "LEMPENG SUNDA", "AU": "LEMPENG AUSTRALIA", "PS": "LEMPENG\nLAUT FILIPINA",
    "PA": "LEMPENG PASIFIK", "EU": "LEMPENG EURASIA", "IN": "LEMPENG INDIA",
    "BU": "Burma", "MS": "Laut\nMaluku", "BH": "Kepala\nBurung", "BS": "Laut Banda",
    "TI": "Timor", "MO": "Maoke", "WL": "Weber", "CL": "Caroline",
    "NB": "Bismarck\nUtara", "SB": "Bismarck\nSelatan",
}


def _koor(s):
    return np.array([[float(v) for v in p.split(",")]
                     for p in s.split()], float)


def relief():
    """Mengembalikan (citra, extent) bayangan relief."""
    import matplotlib.image as mpimg
    meta = json.load(open(os.path.join(DATA, "relief-indonesia.json")))
    im = mpimg.imread(os.path.join(DATA, "relief-indonesia.png"))
    if im.ndim == 3:
        im = im[..., 0]
    if im.dtype != np.float32 and im.max() > 1.5:
        im = im / 255.0
    return im, meta["extent_lon_lat"]


def pantai():
    with open(os.path.join(DATA, "garis-pantai.csv")) as f:
        return [_koor(r["Coords_lonlat"]) for r in csv.DictReader(f)]


def sesar():
    with open(os.path.join(DATA, "pusgen2024-sesar.csv")) as f:
        out = []
        for r in csv.DictReader(f):
            r["xy"] = _koor(r["Coords_lonlat"])
            r["Mmax"] = float(r["Mmax"])
            r["Length_km"] = float(r["Length_km"])
            out.append(r)
        return out


def batas():
    with open(os.path.join(DATA, "bird2003-batas.csv")) as f:
        out = []
        for r in csv.DictReader(f):
            out.append(dict(nama=r["Platebound"], kelas=r["Stepclass"],
                            p1=(float(r["Lon1"]), float(r["Lat1"])),
                            p2=(float(r["Lon2"]), float(r["Lat2"])),
                            v=float(r["Vel_mm_per_yr"]),
                            az=float(r["Vel_azimuth_deg"]),
                            vdiv=float(r["Vel_divergent_mm_per_yr"]),
                            vrl=float(r["Vel_rightlateral_mm_per_yr"]),
                            azstep=float(r["Step_azimuth_deg"])))
        return out


def lempeng():
    with open(os.path.join(DATA, "bird2003-lempeng.csv")) as f:
        out = {}
        for r in csv.DictReader(f):
            out.setdefault(r["Code"], []).append(_koor(r["Coords_lonlat"]))
        return {k: [Path(v) for v in vs] for k, vs in out.items()}


def upper_lower(nama):
    """Kode lempeng (atas, bawah) dari nama batas subduksi Bird (2003)."""
    if "/" in nama:
        a, b = nama.split("/")
        return a, b
    if "\\" in nama:
        a, b = nama.split("\\")
        return b, a
    return None, None


def _di_dalam(poly, x, y):
    return any(p.contains_point((x, y)) for p in poly)


def latar(ax, wilayah, *, terang=0.60, pantai_lw=0.3, pantai_warna="#6f6f6f"):
    """Menggambar latar bayangan relief dan garis pantai pada satu sumbu."""
    lo0, lo1, la0, la1 = wilayah
    im, ext = relief()
    dp = (ext[1] - ext[0]) / im.shape[1]
    j0 = int(round((ext[3] - la1) / dp)); j1 = int(round((ext[3] - la0) / dp))
    i0 = int(round((lo0 - ext[0]) / dp)); i1 = int(round((lo1 - ext[0]) / dp))
    pot = im[max(j0, 0):j1, max(i0, 0):i1]
    # direntang lalu dicerahkan: julat penuh dipakai agar tekstur lantai
    # samudra dan palung tetap terlihat, tetapi seluruh nada digeser ke
    # arah terang supaya lapisan di atasnya tetap terbaca
    v0, v1 = float(np.percentile(pot, 1)), float(np.percentile(pot, 99.5))
    pot = np.clip((pot - v0) / max(v1 - v0, 1e-6), 0.0, 1.0) ** 0.88
    pot = terang + (1.0 - terang) * pot
    ax.imshow(pot, cmap="gray", vmin=0.0, vmax=1.0, origin="upper",
              extent=(lo0, lo1, la0, la1), interpolation="bilinear",
              zorder=0, rasterized=True)
    for g in pantai():
        if (g[:, 0].max() < lo0 or g[:, 0].min() > lo1
                or g[:, 1].max() < la0 or g[:, 1].min() > la1):
            continue
        ax.plot(g[:, 0], g[:, 1], lw=pantai_lw, color=pantai_warna, zorder=1.2,
                solid_capstyle="round")
    ax.set_xlim(lo0, lo1); ax.set_ylim(la0, la1)
    ax.set_aspect(1.0)


def gerigi(ax, p1, p2, sisi, panjang=0.38, lw=0.0, warna=None, zorder=3.5):
    """Satu gerigi (segitiga) pada ruas p1-p2, menghadap `sisi` (+1/-1)."""
    warna = warna or gaya.K
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = x2 - x1, y2 - y1
    n = np.hypot(dx, dy)
    if n == 0:
        return
    ux, uy = dx / n, dy / n
    nx, ny = -uy * sisi, ux * sisi
    xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
    b = panjang * 0.62
    tri = np.array([[xm - ux * b, ym - uy * b],
                    [xm + ux * b, ym + uy * b],
                    [xm + nx * panjang, ym + ny * panjang]])
    ax.fill(tri[:, 0], tri[:, 1], color=warna, lw=lw, zorder=zorder,
            clip_on=True)


_RELIEF = None


def _cerah(x, y):
    """Kecerahan bayangan relief pada (bujur, lintang); daratan dan busur
    pulau jauh lebih cerah daripada lantai samudra dan palung."""
    global _RELIEF
    if _RELIEF is None:
        im, ext = relief()
        _RELIEF = (im, ext, (ext[1] - ext[0]) / im.shape[1])
    im, ext, dp = _RELIEF
    j = int(round((ext[3] - y) / dp)); i = int(round((x - ext[0]) / dp))
    if not (0 <= j < im.shape[0] and 0 <= i < im.shape[1]):
        return np.nan
    return float(im[j, i])


def normal(p1, p2, sisi=1):
    """Vektor satuan normal ruas p1-p2, diputar `sisi` kali +90 derajat."""
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = x2 - x1, y2 - y1
    n = np.hypot(dx, dy)
    if n == 0:
        return None
    return np.array([-dy / n, dx / n]) * sisi


def sisi_atas(p1, p2, jarak=(1.2, 2.0, 2.8)):
    """+1 atau -1: sisi ruas tempat lempeng atas (busur) berada.

    Ditentukan dari data, bukan dari tata nama: lempeng atas selalu
    membawa busur pulau atau tepi benua, sehingga sisinya jauh lebih
    cerah pada bayangan relief daripada sisi palung dan lantai samudra.
    """
    nv = normal(p1, p2)
    if nv is None:
        return None
    xm, ym = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    skor = []
    for s in (+1, -1):
        v = [_cerah(xm + nv[0] * s * d, ym + nv[1] * s * d) for d in jarak]
        v = [z for z in v if not np.isnan(z)]
        skor.append(np.mean(v) if v else np.nan)
    if np.isnan(skor[0]) or np.isnan(skor[1]):
        return None
    return +1 if skor[0] > skor[1] else -1


def v_relatif(b, sisi):
    """Vektor gerak lempeng bawah relatif terhadap lempeng atas (mm/tahun).

    Komponen konvergen (|Vel_divergent|) tegak lurus batas menuju lempeng
    atas, dan komponen menganan (Vel_rightlateral) sejajar batas. Keduanya
    tidak bergantung pada kerangka acuan, sehingga arah yang dihasilkan
    tidak bergantung pada tata nama batas.
    """
    nv = normal(b["p1"], b["p2"], sisi)
    if nv is None:
        return None
    d_rl = np.array([-nv[1], nv[0]])
    return -b["vdiv"] * nv + b["vrl"] * d_rl
