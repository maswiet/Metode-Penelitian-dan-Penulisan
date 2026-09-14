"""Menyiapkan dua berkas data untuk peta tektonik:
  data/pusgen2024-sesar.csv   401 jalur sesar PuSGeN 2024 (dari GeoPackage)
  data/relief-indonesia.png   bayangan relief Natural Earth (potongan)
  data/garis-pantai.csv       garis pantai Natural Earth 1:10 juta (potongan)
"""
import csv
import json
import os
import sqlite3

import numpy as np
import shapefile
from PIL import Image

import wkb

Image.MAX_IMAGE_PIXELS = None

SUMBER = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "data", "sumber-pusgen2024")
GPKG = os.path.join(SUMBER, "01_PUSGEN2024_401_Trace_and_Polygon_Primary.gpkg")
DATA = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "data")
BATAS = (91.0, 143.0, -14.0, 17.0)      # lon0, lon1, lat0, lat1


def sesar():
    c = sqlite3.connect(GPKG)
    kolom = ("Source_ID", "Region", "Main", "Segment", "Type", "Dip_raw",
             "Length_km", "Width_km", "Mmax", "Sliprate", "Status")
    baris = []
    q = "select %s, geom from trace_frozen_401 order by Source_ID" % \
        ", ".join('"%s"' % k for k in kolom)
    for r in c.execute(q):
        t, pts = wkb.gpkg_geom(r[-1])
        assert t == "LineString"
        koor = " ".join("%.5f,%.5f" % (x, y) for x, y in pts)
        baris.append(list(r[:-1]) + [len(pts), koor])
    with open(os.path.join(DATA, "pusgen2024-sesar.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(list(kolom) + ["N_vertex", "Coords_lonlat"])
        w.writerows(baris)
    print("sesar:", len(baris))


def relief():
    tif = "ne/GRAY_HR_SR_OB.tif"
    im = Image.open(tif)
    # tfw: piksel 1/60 derajat, titik tengah piksel pertama di (-179.99167, 89.99167)
    dp = 1.0 / 60.0
    x0, y0 = -179.99166666666667, 89.99166666666667
    lon0, lon1, lat0, lat1 = BATAS
    i0 = int(round((lon0 - x0) / dp))
    i1 = int(round((lon1 - x0) / dp))
    j0 = int(round((y0 - lat1) / dp))
    j1 = int(round((y0 - lat0) / dp))
    pot = im.crop((i0, j0, i1, j1))
    print("relief:", pot.size)
    pot.save(os.path.join(DATA, "relief-indonesia.png"), optimize=True)
    with open(os.path.join(DATA, "relief-indonesia.json"), "w") as f:
        json.dump({"sumber": "Natural Earth GRAY_HR_SR_OB (1:10 juta, 1 menit busur)",
                   "extent_lon_lat": list(BATAS),
                   "ukuran_piksel_derajat": dp,
                   "lisensi": "domain publik"}, f, indent=1)


def pantai():
    sf = shapefile.Reader("ne/ne_10m_coastline")
    lon0, lon1, lat0, lat1 = BATAS
    n = 0
    with open(os.path.join(DATA, "garis-pantai.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Coords_lonlat"])
        for sh in sf.shapes():
            pts = np.asarray(sh.points, float)
            if pts.size == 0:
                continue
            if (pts[:, 0].max() < lon0 or pts[:, 0].min() > lon1
                    or pts[:, 1].max() < lat0 or pts[:, 1].min() > lat1):
                continue
            for a, b in zip(sh.parts, list(sh.parts[1:]) + [len(pts)]):
                p = pts[a:b]
                if len(p) < 2:
                    continue
                w.writerow([" ".join("%.4f,%.4f" % (x, y) for x, y in p)])
                n += 1
    print("bagian garis pantai:", n)


if __name__ == "__main__":
    sesar()
    relief()
    pantai()
