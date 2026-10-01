"""Menyaring model batas lempeng Bird (2003) ke jendela Indonesia.

Keluaran (di dalam data/):
  bird2003-batas.csv    ruas batas lempeng: koordinat, kelas, laju, azimut
  bird2003-lempeng.csv  poligon lempeng (untuk penamaan dan uji sisi)
"""
import csv
import json
import os

DATA = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "data")
BATAS = (91.0, 143.0, -14.0, 17.0)
lon0, lon1, lat0, lat1 = BATAS
M = 3.0        # jendela diperlebar agar ruas di tepi tetap utuh


def ruas():
    d = json.load(open("PB2002_steps.json"))
    out = []
    for f in d["features"]:
        p = f["properties"]
        la = (p["STARTLAT"] + p["FINALLAT"]) / 2
        lo = (p["STARTLONG"] + p["FINALLONG"]) / 2
        if not (lon0 - M < lo < lon1 + M and lat0 - M < la < lat1 + M):
            continue
        out.append([p["PLATEBOUND"], p["STEPCLASS"],
                    round(p["STARTLONG"], 4), round(p["STARTLAT"], 4),
                    round(p["FINALLONG"], 4), round(p["FINALLAT"], 4),
                    round(p["VELOCITYLE"], 1), round(p["VELOCITYAZ"], 1),
                    round(p["VELOCITYDI"], 1), round(p["VELOCITYRI"], 1),
                    round(p["AZIMUTHCEN"], 1), round(p["STEPLENGTH"], 1)])
    with open(os.path.join(DATA, "bird2003-batas.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Platebound", "Stepclass", "Lon1", "Lat1", "Lon2", "Lat2",
                    "Vel_mm_per_yr", "Vel_azimuth_deg", "Vel_divergent_mm_per_yr",
                    "Vel_rightlateral_mm_per_yr", "Step_azimuth_deg",
                    "Steplength_km"])
        w.writerows(out)
    print("ruas batas:", len(out))


def lempeng():
    d = json.load(open("PB2002_plates.json"))
    n = 0
    with open(os.path.join(DATA, "bird2003-lempeng.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Code", "Name", "Coords_lonlat"])
        for ft in d["features"]:
            p = ft["properties"]
            g = ft["geometry"]
            cin = g["coordinates"] if g["type"] == "Polygon" else \
                [r for poly in g["coordinates"] for r in poly]
            for ring in cin:
                xs = [c[0] for c in ring]; ys = [c[1] for c in ring]
                if (max(xs) < lon0 - M or min(xs) > lon1 + M
                        or max(ys) < lat0 - M or min(ys) > lat1 + M):
                    continue
                w.writerow([p.get("Code", ""), p.get("PlateName", ""),
                            " ".join("%.4f,%.4f" % (x, y) for x, y in
                                     zip(xs, ys))])
                n += 1
    print("cincin lempeng:", n)


if __name__ == "__main__":
    ruas()
    lempeng()
