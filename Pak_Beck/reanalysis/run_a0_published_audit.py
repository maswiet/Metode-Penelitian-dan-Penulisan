"""Stage A0: audit of the numbers in the submitted manuscript's own tables.

Every quantity here is recomputed from Table 1 and Table 2 of the 18 August
version, so the arithmetic can be checked without the original event list.
"""
from __future__ import annotations

import itertools
import json
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "reanalysis")
import fmd, geometry as gm  # noqa: E402

OUT = "results/tables"

# Table 1 of the submitted manuscript.
TABLE1 = pd.DataFrame([
    # cluster, N, R_mean, SD_R, Z_mean, SD_Z, M_mean
    (8, 27, 75.2, 55.3, 119.2, 77.1, 4.5),
    (1, 18, 114.6, 59.4, 24.1, 18.4, 4.5),
    (5, 24, 33.7, 27.1, 17.4, 19.9, 4.4),
    (2, 46, 23.9, 24.8, 34.8, 46.4, 4.6),
    (3, 25, 16.5, 13.2, 30.7, 22.5, 4.8),
    (4, 66, 17.1, 10.4, 11.3, 4.9, 4.6),
    (6, 21, 22.2, 25.8, 21.7, 18.1, 4.7),
    (7, 21, 121.6, 55.4, 38.3, 35.2, 4.6),
], columns=["cluster", "N", "R_mean", "SD_R", "Z_mean", "SD_Z", "M_mean"])

# Table 2 of the submitted manuscript.
TABLE2 = pd.DataFrame([
    (8, 4.2, 1.01, 0.14, 24), (1, 4.2, 1.05, 0.18, 16),
    (5, 4.1, 1.00, 0.18, 22), (2, 4.2, 0.92, 0.12, 41),
    (3, 4.1, 0.58, 0.13, 25), (4, 4.4, 0.97, 0.13, 49),
    (6, 4.4, 0.85, 0.15, 15), (7, 4.2, 0.94, 0.15, 19),
], columns=["cluster", "Mc", "b", "sigma_b", "n_above_mc"])


def main() -> None:
    out = {}

    # ---- 1. SD_R is not a size measure ----------------------------------
    t = TABLE1.copy()
    t["R_g"] = [gm.rg_from_radial(r.R_mean, r.SD_R, int(r.N)) for r in t.itertuples()]
    t = t.sort_values("R_g")
    print("Radius of gyration recovered from the published mean radius and SD_R:")
    for r in t.itertuples():
        print(f"  C{int(r.cluster)}: R̄={r.R_mean:6.1f}  SD_R={r.SD_R:5.1f}  →  R_g={r.R_g:6.2f} km")
    c3 = float(t.loc[t.cluster == 3, "R_g"].iloc[0])
    c4 = float(t.loc[t.cluster == 4, "R_g"].iloc[0])
    floor = gm.location_error_floor()
    out["compactness"] = dict(
        R_g=t.set_index("cluster")["R_g"].to_dict(),
        C3_minus_C4_km=c3 - c4,
        smallest_by_R_g=int(t.iloc[0]["cluster"]),
        horizontal_resolution_floor_km=floor["sd_horizontal_km"],
        note=("The manuscript calls C4 the most compact domain. By radius of "
              "gyration C4 and C3 differ by about one kilometre, which is "
              "within the catalogue's own hypocentral resolution."))
    print(f"\n  C3 − C4 = {c3 - c4:+.2f} km; catalogue horizontal resolution floor "
          f"≈ {floor['sd_horizontal_km']:.2f} km (0.01° rounding alone)")
    t.to_csv(f"{OUT}/published_compactness_audit.csv", index=False)

    # ---- 2. Are the published b-value contrasts significant? -------------
    rows = []
    for a, b_ in itertools.combinations(TABLE2.itertuples(), 2):
        u = fmd.utsu_test(a.b, int(a.n_above_mc), b_.b, int(b_.n_above_mc))
        se = np.hypot(a.sigma_b, b_.sigma_b)
        rows.append(dict(pair=f"C{int(a.cluster)}-C{int(b_.cluster)}",
                         b_a=a.b, b_b=b_.b, delta_b=a.b - b_.b,
                         combined_se=se, n_sigma=abs(a.b - b_.b) / se,
                         utsu_p=u["p"]))
    pw = pd.DataFrame(rows)
    bh = fmd.benjamini_hochberg(pw.utsu_p.values)
    pw["q_value"], pw["significant_fdr05"] = bh["q"], bh["rejected"]
    pw = pw.sort_values("utsu_p")
    pw.to_csv(f"{OUT}/published_bvalue_audit.csv", index=False)
    n_sig = int(pw.significant_fdr05.sum())
    print(f"\n  {len(pw)} pairwise b-value comparisons among the eight published clusters;")
    print(f"  {n_sig} remain significant after Benjamini-Hochberg correction at q < 0.05.")
    print("  strongest contrasts:")
    for r in pw.head(5).itertuples():
        mark = "significant" if r.significant_fdr05 else "not significant"
        print(f"    {r.pair:8s} Δb={r.delta_b:+.2f}  {r.n_sigma:.1f}σ  "
              f"p={r.utsu_p:.4f}  q={r.q_value:.4f}  {mark}")
    out["bvalue_pairs"] = dict(n_pairs=len(pw), n_significant_fdr=n_sig,
                               table=pw.to_dict("records"))

    # ---- 3. b and mean magnitude are one statistic ----------------------
    # Recover mean magnitude implied by each published b and Mc, and compare
    # with the mean magnitude the manuscript reports separately.
    chk = []
    for r2 in TABLE2.itertuples():
        implied = (r2.Mc - 0.05) + fmd.LOG10E / r2.b
        chk.append(dict(cluster=int(r2.cluster), b=r2.b, mc=r2.Mc,
                        implied_mean_mag_above_mc=implied))
    out["b_implies_mean_magnitude"] = chk
    print("\n  b and mean magnitude are the same statistic; C3's b = 0.58 implies")
    print(f"  a mean magnitude above Mc of {chk[4]['implied_mean_mag_above_mc']:.2f}, "
          "which is what Table 1 reports as an independent result.")

    # ---- 4. The learning-rate schedule ----------------------------------
    out["learning_rate"] = {str(e): 0.01 * 0.5**e for e in (10, 20, 50, 100)}
    print(f"\n  learning rate: α(20) = {0.01*0.5**20:.2e}, α(100) = {0.01*0.5**100:.2e}")

    with open(f"{OUT}/a0_published_audit.json", "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print("\nwrote", f"{OUT}/a0_published_audit.json")


if __name__ == "__main__":
    main()
