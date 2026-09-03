"""Stage A7: temporal organisation of a partition that never saw time.

The spatial groups are built from horizontal position alone. Occurrence time is
therefore free to act as an independent test variable, which is what makes any
temporal result here a discovery rather than a restatement of the input.
"""
from __future__ import annotations

import itertools
import json
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "reanalysis")
import catalog, clustering as cl, features as ft, fmd, seismicity as sz  # noqa: E402

OUT = "results/tables"
RNG = 20260903
MC = 3.7
K = 3


def main() -> None:
    df, _ = catalog.quality_control(catalog.load_raw("data/lombok2018new.csv"))
    df = catalog.add_projection(df)
    region = catalog.subset(df, catalog.SEQUENCE_BOX)
    modern = region[region.dt >= catalog.MODERN_ERA_START]
    cat = modern[modern.mw >= MC].reset_index(drop=True)
    cat = cat.assign(t_days=catalog.elapsed_days(cat))

    X = ft.scale(cat[["east_km", "north_km"]].to_numpy(float), "minmax")
    cat = cat.assign(g=cl.baseline_labels(X, K, "kmeans", seed=RNG))
    ms = cat.loc[cat.mw.idxmax()]
    out = {"n": len(cat), "mc": MC, "K": K,
           "mainshock": dict(dt=str(ms["dt"]), lat=float(ms["lat"]),
                             lon=float(ms["lon"]), mw=float(ms["mw"]))}

    # ---- do space-only groups carry real temporal information? -----------
    kw = stats.kruskal(*[s.t_days.values for _, s in cat.groupby("g")])
    out["kruskal_time"] = dict(H=float(kw.statistic), p=float(kw.pvalue))
    print(f"Kruskal-Wallis on occurrence time across space-only groups: "
          f"H={kw.statistic:.1f}, p={kw.pvalue:.2e}")

    # ---- segment activation during the 2018 sequence ---------------------
    seq = cat[cat.dt.between("2018-07-28", "2018-09-30")]
    rows = []
    for g, s in cat.groupby("g"):
        ss = seq[seq.g == g]
        rows.append(dict(
            group=int(g), n=len(s), n_sequence=len(ss),
            lat=float(s.lat.mean()), lon=float(s.lon.mean()),
            dist_mainshock_km=float(sz._haversine_km(s.lat.mean(), s.lon.mean(),
                                                     ms["lat"], ms["lon"])),
            median_date=str(s.dt.median().date()),
            median_date_sequence=str(ss.dt.median().date()) if len(ss) else None,
            mw_max=float(s.mw.max()),
            frac_default_depth=float((s.depth == catalog.DEFAULT_DEPTH_KM).mean()),
            b=float(fmd.b_value_aki(s.mw.values, MC)["b"]),
            sigma_b=float(fmd.b_value_aki(s.mw.values, MC)["sigma_b"]),
            n_above_mc=int(fmd.b_value_aki(s.mw.values, MC)["n"])))
        print(f"  G{g}: n={len(s):4d}  centroid ({rows[-1]['lat']:.3f},{rows[-1]['lon']:.3f})  "
              f"median {rows[-1]['median_date']}  Mw_max {rows[-1]['mw_max']:.2f}  "
              f"b={rows[-1]['b']:.3f}+-{rows[-1]['sigma_b']:.3f}")
    prof = pd.DataFrame(rows)
    prof.to_csv(f"{OUT}/segment_profile.csv", index=False)
    out["segments"] = rows

    # ---- pairwise tests: are the timings and the b-values different? -----
    pair = []
    for a, b_ in itertools.combinations(sorted(cat.g.unique()), 2):
        ta = seq[seq.g == a].t_days.values
        tb = seq[seq.g == b_].t_days.values
        u = stats.mannwhitneyu(ta, tb, alternative="two-sided") if len(ta) and len(tb) else None
        ea = fmd.b_value_aki(cat[cat.g == a].mw.values, MC)
        eb = fmd.b_value_aki(cat[cat.g == b_].mw.values, MC)
        ut = fmd.utsu_test(ea["b"], ea["n"], eb["b"], eb["n"])
        pair.append(dict(group_a=int(a), group_b=int(b_),
                         median_shift_days=float(np.median(tb) - np.median(ta)) if len(ta) and len(tb) else np.nan,
                         mannwhitney_p=float(u.pvalue) if u else np.nan,
                         delta_b=float(ea["b"] - eb["b"]), utsu_p=float(ut["p"])))
    pdf = pd.DataFrame(pair)
    bh_t = fmd.benjamini_hochberg(pdf.mannwhitney_p.values)
    bh_b = fmd.benjamini_hochberg(pdf.utsu_p.values)
    pdf["q_time"], pdf["q_b"] = bh_t["q"], bh_b["q"]
    pdf.to_csv(f"{OUT}/segment_pairwise.csv", index=False)
    out["pairwise"] = pdf.to_dict("records")
    print("\n  pairwise segment tests (FDR corrected):")
    for _, r in pdf.iterrows():
        print(f"    G{int(r.group_a)} vs G{int(r.group_b)}: timing shift "
              f"{r.median_shift_days:+6.1f} d (q={r.q_time:.2e})   "
              f"db={r.delta_b:+.3f} (q={r.q_b:.2e})")

    # ---- along-strike migration of the 2018 activity ---------------------
    # Project epicentres onto the mean strike of the thrust system and track
    # the running median position, which tests migration without any clustering.
    xy = seq[["east_km", "north_km"]].to_numpy(float)
    xy = xy - xy.mean(0)
    _, _, Vt = np.linalg.svd(xy, full_matrices=False)
    along = xy @ Vt[0]
    strike_az = float(np.degrees(np.arctan2(Vt[0][0], Vt[0][1])) % 180.0)
    t = seq.t_days.to_numpy()
    rho = stats.spearmanr(t, along)
    # Report the correlation against longitude as well: the sign of a principal
    # axis is arbitrary, so the longitude version is the one a reader can check
    # against the figure.
    rho_lon = stats.spearmanr(t, seq.lon.to_numpy())
    out["migration"] = dict(strike_azimuth_deg=strike_az,
                            spearman_rho_alongstrike=float(rho.statistic),
                            p_alongstrike=float(rho.pvalue),
                            spearman_rho_longitude=float(rho_lon.statistic),
                            p_longitude=float(rho_lon.pvalue),
                            direction=("eastward" if rho_lon.statistic > 0 else "westward"),
                            n=int(len(seq)))
    print(f"\n  migration (strike azimuth {strike_az:.0f} deg): along-strike "
          f"rho={rho.statistic:+.3f} (p={rho.pvalue:.2e}); "
          f"longitude rho={rho_lon.statistic:+.3f} (p={rho_lon.pvalue:.2e}), n={len(seq)}")

    win = []
    for lo, hi in [(0, 3), (3, 7), (7, 14), (14, 21), (21, 35), (35, 64)]:
        d0 = pd.Timestamp("2018-07-28")
        sub = seq[(seq.dt >= d0 + pd.Timedelta(days=lo)) & (seq.dt < d0 + pd.Timedelta(days=hi))]
        if len(sub) < 10:
            continue
        a = (sub[["east_km", "north_km"]].to_numpy(float) - seq[["east_km", "north_km"]].to_numpy(float).mean(0)) @ Vt[0]
        win.append(dict(days=f"{lo}-{hi}", n=len(sub), median_along_km=float(np.median(a)),
                        median_lon=float(sub.lon.median()), median_lat=float(sub.lat.median())))
        print(f"    days {lo:2d}-{hi:2d}: n={len(sub):4d}  along-strike median "
              f"{np.median(a):+7.1f} km  (lon {sub.lon.median():.3f})")
    pd.DataFrame(win).to_csv(f"{OUT}/migration_windows.csv", index=False)
    out["migration_windows"] = win

    cat.to_csv(f"{OUT}/segmented_catalogue.csv", index=False)
    with open(f"{OUT}/a7_migration.json", "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print("wrote", f"{OUT}/a7_migration.json")


if __name__ == "__main__":
    main()
