"""Stage A5: focal mechanisms matched to groups, with an explicit criterion.

The review requires mechanism counts per group, a stated matching rule, Kagan
angles and a measure of mechanism heterogeneity, instead of citing a regional
mechanism set as validation of a partition.
"""
from __future__ import annotations

import itertools
import json
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "reanalysis")
import catalog, focal, seismicity as sz  # noqa: E402

OUT = "results/tables"
FIRST_EVENT = pd.Timestamp("2018-07-28 22:47:38")


def main() -> None:
    fm = focal.parse_cmtsolution("data/gcmt_lombok.cmt")
    fm.to_csv(f"{OUT}/gcmt_solutions.csv", index=False)
    out = {"n_solutions_file": len(fm),
           "search": "Mw >= 5.5, 1976-2025, 115-117.5E, 9.5-7.5S"}
    print(f"GCMT solutions in file: {len(fm)} (Mw>=5.5, 1976-2025)")

    win = fm[fm.dt.between("2017-07-27", "2019-07-29")].reset_index(drop=True)
    out["n_in_study_window"] = len(win)
    print(f"  inside the 2017-2019 study window: {len(win)}")
    print("  This is the entire mechanism resource for the sequence; per-group")
    print("  mechanism statistics are therefore limited by it, not by the method.")

    df, _ = catalog.quality_control(catalog.load_raw("data/lombok2018new.csv"))
    df = catalog.add_projection(df)
    region = catalog.subset(df, catalog.SEQUENCE_BOX)
    modern = region[region.dt >= catalog.MODERN_ERA_START].reset_index(drop=True)
    ms = modern.loc[modern.mw.idxmax()]

    d = sz._haversine_km(win.lat.values, win.lon.values, ms.lat, ms.lon)
    win = win.assign(dist_ms_km=d,
                     zone=np.where(d <= 25, "near field (<=25 km)",
                           np.where(d <= 75, "intermediate (25-75 km)",
                                    "far field (>75 km)")),
                     phase=np.where(win.dt < FIRST_EVENT, "pre-sequence",
                             np.where(win.dt <= pd.Timestamp("2018-08-31"), "main sequence",
                                      "post-sequence")))
    win.to_csv(f"{OUT}/gcmt_in_window.csv", index=False)

    print("\n  mechanisms by zone and style:")
    tab = win.groupby(["zone", "style"]).size().unstack(fill_value=0)
    print(tab.to_string())
    out["by_zone_style"] = tab.to_dict()

    # ---- Kagan angles: how uniform is the faulting within a group? -------
    rows = []
    for zone, sub in win.groupby("zone"):
        sdrs = list(zip(sub.strike1, sub.dip1, sub.rake1))
        if len(sdrs) < 2:
            rows.append(dict(zone=zone, n=len(sdrs), mean_kagan=np.nan,
                             median_kagan=np.nan, max_kagan=np.nan))
            continue
        ang = [focal.kagan_angle(a, b) for a, b in itertools.combinations(sdrs, 2)]
        rows.append(dict(zone=zone, n=len(sdrs), mean_kagan=float(np.mean(ang)),
                         median_kagan=float(np.median(ang)), max_kagan=float(np.max(ang))))
        print(f"    {zone:24s} n={len(sdrs)}  mean Kagan {np.mean(ang):5.1f} deg, "
              f"median {np.median(ang):5.1f}, max {np.max(ang):5.1f}")
    kag = pd.DataFrame(rows)
    kag.to_csv(f"{OUT}/kagan_by_zone.csv", index=False)
    out["kagan_by_zone"] = rows

    # A random pair of double couples averages near 70-80 degrees; values well
    # below that indicate a genuinely coherent faulting style.
    rng = np.random.default_rng(0)
    rand = [focal.kagan_angle(
        (rng.uniform(0, 360), rng.uniform(0, 90), rng.uniform(-180, 180)),
        (rng.uniform(0, 360), rng.uniform(0, 90), rng.uniform(-180, 180)))
        for _ in range(4000)]
    out["kagan_random_reference"] = dict(mean=float(np.mean(rand)),
                                         median=float(np.median(rand)))
    print(f"    random-mechanism reference: mean {np.mean(rand):.1f} deg, "
          f"median {np.median(rand):.1f} deg")

    # ---- match mechanisms to catalogue events ----------------------------
    labels = np.zeros(len(modern), int)
    match = focal.match_to_clusters(win, modern, labels, max_dt_s=120.0, max_dist_km=60.0)
    out["matching"] = dict(n=len(match), n_matched=int(match.matched.sum()),
                           criterion="within 120 s and 60 km of the CMT centroid")
    print(f"\n  catalogue matching: {int(match.matched.sum())}/{len(match)} mechanisms "
          f"matched within 120 s and 60 km")
    match.to_csv(f"{OUT}/focal_catalogue_match.csv", index=False)

    with open(f"{OUT}/a5_focal.json", "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print("wrote", f"{OUT}/a5_focal.json")


if __name__ == "__main__":
    main()
