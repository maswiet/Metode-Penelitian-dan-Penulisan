"""Stage A3: background, triggered, and whether later activity is postseismic.

Applies nearest-neighbour declustering to separate background from triggered
events objectively, fits the Omori-Utsu decay of the 2018 sequence, and tests
whether the later seismicity the manuscript calls postseismic redistribution is
actually elevated above the pre-sequence background rate.
"""
from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "reanalysis")
import catalog, fmd, seismicity as sz  # noqa: E402

OUT = "results/tables"
MAINSHOCK = pd.Timestamp("2018-08-05 11:46:38")
FIRST_EVENT = pd.Timestamp("2018-07-28 22:47:38")


def main() -> None:
    df, _ = catalog.quality_control(catalog.load_raw("data/lombok2018new.csv"))
    df = catalog.add_projection(df)
    out = {}

    # A common completeness threshold is required before any rate comparison,
    # because the network densified during the catalogue period.
    region = catalog.subset(df, catalog.SEQUENCE_BOX)
    modern = region[region.dt >= catalog.MODERN_ERA_START].reset_index(drop=True)
    mc_modern = fmd.mc_goodness_of_fit(modern.mw.values)
    mc_pre = fmd.mc_goodness_of_fit(
        modern[modern.dt < FIRST_EVENT].mw.values)
    mc_common = float(max(mc_modern["mc"], mc_pre["mc"], 4.0))
    out["completeness"] = dict(mc_modern=mc_modern, mc_pre_sequence=mc_pre,
                               mc_common_adopted=mc_common)
    print(f"Mc modern era {mc_modern['mc']:.2f}, pre-sequence {mc_pre['mc']:.2f}, "
          f"common adopted {mc_common:.2f}")

    cat = modern[modern.mw >= mc_common].reset_index(drop=True)
    print(f"declustering set: n={len(cat)} events, {cat.dt.min().date()} to {cat.dt.max().date()}")

    # ---- nearest-neighbour declustering ----------------------------------
    b_reg = fmd.b_value_aki(cat.mw.values, mc_common)["b"]
    nnd = sz.nearest_neighbour_distances(
        catalog.elapsed_days(cat), cat.lat.values, cat.lon.values,
        cat.mw.values, b=b_reg, d_f=1.6, mc=mc_common)
    split = sz.decluster_threshold(nnd["log_eta"])
    out["declustering"] = dict(b_used=float(b_reg), **split)
    print(f"  b used {b_reg:.3f}; log10(eta) threshold {split['threshold']:.2f}; "
          f"{100*split['frac_clustered']:.1f}% triggered")

    cat = cat.assign(log_eta=nnd["log_eta"],
                     triggered=nnd["log_eta"] <= split["threshold"])
    cat.loc[0, "triggered"] = False  # first event has no possible parent
    cat.to_csv(f"{OUT}/declustered_catalogue.csv", index=False)

    # ---- Omori-Utsu decay of the 2018 sequence ---------------------------
    aft = cat[(cat.dt > MAINSHOCK) & (cat.dt <= MAINSHOCK + pd.Timedelta(days=365))]
    t_af = (aft.dt - MAINSHOCK).dt.total_seconds().to_numpy() / 86400.0
    om = sz.omori_utsu_fit(t_af, t_end=365.0)
    out["omori"] = om
    print(f"  Omori-Utsu: p={om['p']:.3f}, c={om['c']:.4f} d, K={om['K']:.1f}, n={om['n']}")

    # ---- is later activity above background, and for how long? -----------
    pre = cat[cat.dt < FIRST_EVENT]
    span_pre = (FIRST_EVENT - cat.dt.min()).total_seconds() / 86400.0
    rows = []
    for label, start, end in [
        ("Sep-Dec 2018", "2018-09-01", "2018-12-31"),
        ("Jan-Jul 2019", "2019-01-01", "2019-07-31"),
        ("Aug 2019-Jul 2020", "2019-08-01", "2020-07-31"),
        ("Aug 2020-Jul 2021", "2020-08-01", "2021-07-31"),
        ("Aug 2021-Dec 2023", "2021-08-01", "2023-12-31"),
    ]:
        sub = cat[cat.dt.between(start, end)]
        span = (pd.Timestamp(end) - pd.Timestamp(start)).total_seconds() / 86400.0
        r = sz.rate_comparison(pre.dt.values, span_pre, sub.dt.values, span)
        bg = sub[~sub.triggered]
        rows.append(dict(period=label, n=len(sub), n_background=int((~sub.triggered).sum()),
                         rate_per_year=r["rate_post_per_day"] * 365.25,
                         background_rate_per_year=float(len(bg) / span * 365.25),
                         ratio_to_pre=r["ratio"], p_value=r["p_value"]))
        print(f"  {label:20s} n={len(sub):4d}  rate {r['rate_post_per_day']*365.25:6.1f}/yr  "
              f"x{r['ratio']:5.2f} pre-sequence  p={r['p_value']:.2e}")
    pd.DataFrame(rows).to_csv(f"{OUT}/rate_comparison.csv", index=False)
    out["rate_comparison"] = rows
    out["pre_sequence_rate_per_year"] = float(len(pre) / span_pre * 365.25)

    # ---- how far from the rupture does triggering extend? ----------------
    ms = cat.loc[(cat.mw.idxmax())]
    d_km = sz._haversine_km(cat.lat.values, cat.lon.values, ms.lat, ms.lon)
    cat2 = cat.assign(dist_ms_km=d_km)
    dist_rows = []
    for lo, hi in [(0, 25), (25, 50), (50, 75), (75, 100), (100, 150)]:
        sub = cat2[(cat2.dist_ms_km >= lo) & (cat2.dist_ms_km < hi)]
        post = sub[sub.dt.between("2018-09-01", "2019-07-31")]
        pre_s = sub[sub.dt < FIRST_EVENT]
        span_post = (pd.Timestamp("2019-07-31") - pd.Timestamp("2018-09-01")).days
        if len(pre_s) + len(post) < 5:
            continue
        r = sz.rate_comparison(pre_s.dt.values, span_pre, post.dt.values, span_post)
        dist_rows.append(dict(band_km=f"{lo}-{hi}", n_pre=len(pre_s), n_post=len(post),
                              ratio=r["ratio"], p_value=r["p_value"],
                              frac_triggered=float(post.triggered.mean()) if len(post) else np.nan))
        print(f"  {lo:3d}-{hi:3d} km from mainshock: x{r['ratio']:6.2f} pre-rate  "
              f"p={r['p_value']:.3f}  triggered fraction {100*post.triggered.mean() if len(post) else float('nan'):.0f}%")
    pd.DataFrame(dist_rows).to_csv(f"{OUT}/triggering_distance.csv", index=False)
    out["triggering_distance"] = dist_rows

    with open(f"{OUT}/a3_triggering.json", "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print("wrote", f"{OUT}/a3_triggering.json")


if __name__ == "__main__":
    main()
