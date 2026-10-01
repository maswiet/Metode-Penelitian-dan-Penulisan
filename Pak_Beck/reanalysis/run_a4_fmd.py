"""Stage A4: Gutenberg-Richter analysis done to the standard the review demands.

Every b-value is estimated at a common completeness threshold with bootstrap
uncertainty that includes the choice of Mc, differences are tested with the
Utsu likelihood ratio and corrected for multiple comparisons, and the headline
association between grouping and magnitude is checked against a permutation
null.
"""
from __future__ import annotations

import itertools
import json
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "reanalysis")
import catalog, fmd, seismicity as sz  # noqa: E402

OUT = "results/tables"
MAINSHOCK = pd.Timestamp("2018-08-05 11:46:38")
FIRST_EVENT = pd.Timestamp("2018-07-28 22:47:38")
RNG = 20260903


def assign_groups(cat: pd.DataFrame) -> pd.DataFrame:
    """Seismologically defined groups, fixed before any magnitude is inspected.

    Unlike the manuscript's eight clusters these are defined by the rupture
    geometry and the sequence chronology, not by an algorithm that already saw
    the data, so comparing their magnitude distributions is not circular.
    """
    ms = cat.loc[cat.mw.idxmax()]
    d = sz._haversine_km(cat.lat.values, cat.lon.values, ms.lat, ms.lon)
    cat = cat.assign(dist_ms_km=d)

    phase = np.where(cat.dt < FIRST_EVENT, "pre-sequence",
             np.where(cat.dt <= pd.Timestamp("2018-08-31"), "main sequence",
              np.where(cat.dt <= pd.Timestamp("2019-07-31"), "first-year post",
                       "later")))
    zone = np.where(d <= 25, "near field (<=25 km)",
            np.where(d <= 75, "intermediate (25-75 km)", "far field (>75 km)"))
    return cat.assign(phase=phase, zone=zone)


def group_table(cat: pd.DataFrame, key: str, mc: float, dm: float = 0.1,
                n_boot: int = 500) -> pd.DataFrame:
    """b-value per group at a common Mc, with bootstrapped uncertainty."""
    rows = []
    for g, sub in cat.groupby(key):
        m = sub.mw.values
        est = fmd.b_value_aki(m, mc, dm)
        if est["n"] < 20:
            rows.append(dict(group=g, n_total=len(sub), n_above_mc=est["n"],
                             b=np.nan, sigma_b=np.nan, b_boot=np.nan,
                             b_boot_sd=np.nan, ci_lo=np.nan, ci_hi=np.nan,
                             mean_mag=est["mean_mag"], estimable=False))
            continue
        bs = fmd.bootstrap_mc_b(m[m >= mc - dm / 2], dm=dm, n_boot=n_boot,
                                method="maxcurv",
                                rng=np.random.default_rng(RNG))
        rows.append(dict(group=g, n_total=len(sub), n_above_mc=est["n"],
                         b=est["b"], sigma_b=est["sigma_b"],
                         b_boot=bs["b_mean"], b_boot_sd=bs["b_std"],
                         ci_lo=bs["b_ci"][0], ci_hi=bs["b_ci"][1],
                         mean_mag=est["mean_mag"], estimable=True))
    return pd.DataFrame(rows)


def pairwise_utsu(tab: pd.DataFrame) -> pd.DataFrame:
    """All pairwise Utsu tests with Benjamini-Hochberg FDR control."""
    ok = tab[tab.estimable].reset_index(drop=True)
    rows = []
    for i, j in itertools.combinations(range(len(ok)), 2):
        a, b_ = ok.loc[i], ok.loc[j]
        t = fmd.utsu_test(a.b, int(a.n_above_mc), b_.b, int(b_.n_above_mc))
        rows.append(dict(group_a=a.group, group_b=b_.group,
                         b_a=a.b, b_b=b_.b, delta_b=a.b - b_.b,
                         dAIC=t["dAIC"], p=t["p"]))
    out = pd.DataFrame(rows)
    if len(out):
        bh = fmd.benjamini_hochberg(out.p.values)
        out["q_value"] = bh["q"]
        out["significant_fdr05"] = bh["rejected"]
    return out


def main() -> None:
    df, _ = catalog.quality_control(catalog.load_raw("data/lombok2018new.csv"))
    df = catalog.add_projection(df)
    region = catalog.subset(df, catalog.SEQUENCE_BOX)
    modern = region[region.dt >= catalog.MODERN_ERA_START].reset_index(drop=True)

    gft = fmd.mc_goodness_of_fit(modern.mw.values)
    mc = float(np.ceil(gft["mc"] * 10) / 10)
    print(f"common Mc adopted: {mc:.2f} (GFT {gft['mc']:.2f}, R={gft['R']:.1f}%)")
    out = {"mc_common": mc, "gft": gft}

    cat = assign_groups(modern)
    cat.to_csv(f"{OUT}/grouped_catalogue.csv", index=False)

    # ---- regional b-value with full uncertainty --------------------------
    reg = fmd.b_value_aki(modern.mw.values, mc)
    reg_boot = fmd.bootstrap_mc_b(modern.mw.values, n_boot=500,
                                  rng=np.random.default_rng(RNG))
    out["regional"] = dict(**{k: float(v) for k, v in reg.items()},
                           boot=reg_boot)
    print(f"regional b = {reg['b']:.3f} +- {reg['sigma_b']:.3f} (Shi-Bolt); "
          f"bootstrap {reg_boot['b_mean']:.3f} +- {reg_boot['b_std']:.3f}, "
          f"Mc bootstrap {reg_boot['mc_mean']:.2f} +- {reg_boot['mc_std']:.2f}")

    # ---- b-value by phase and by zone ------------------------------------
    for key, fname in [("phase", "b_by_phase"), ("zone", "b_by_zone")]:
        tab = group_table(cat, key, mc)
        tab.to_csv(f"{OUT}/{fname}.csv", index=False)
        print(f"\n  b-value by {key} (common Mc={mc}):")
        for _, r in tab.iterrows():
            if r.estimable:
                print(f"    {r.group:24s} n={int(r.n_above_mc):4d}  b={r.b:.3f}+-{r.sigma_b:.3f}"
                      f"  boot 95% CI [{r.ci_lo:.2f}, {r.ci_hi:.2f}]  M̄={r.mean_mag:.2f}")
            else:
                print(f"    {r.group:24s} n={int(r.n_above_mc):4d}  not estimable")
        pw = pairwise_utsu(tab)
        pw.to_csv(f"{OUT}/{fname}_utsu.csv", index=False)
        if len(pw):
            print(f"  pairwise Utsu tests ({key}):")
            for _, r in pw.iterrows():
                mark = "SIGNIFICANT" if r.significant_fdr05 else "not significant"
                print(f"    {r.group_a:22s} vs {r.group_b:22s} "
                      f"db={r.delta_b:+.3f}  p={r.p:.4f}  q={r.q_value:.4f}  {mark}")
        out[fname] = tab.to_dict("records")
        out[f"{fname}_utsu"] = pw.to_dict("records") if len(pw) else []

    # ---- b-value and mean magnitude are the same statistic ---------------
    # For a fixed Mc the Aki estimator is a deterministic function of mean
    # magnitude, so reporting both as separate evidence double counts.
    from scipy.stats import spearmanr
    mm = np.linspace(mc + 0.05, mc + 1.2, 50)
    bb = fmd.LOG10E / (mm - (mc - 0.05))
    out["b_meanmag_identity"] = dict(
        spearman=float(spearmanr(mm, bb).statistic),
        pearson=float(np.corrcoef(mm, bb)[0, 1]),
        note=("b = log10(e) / (mean_mag - (Mc - dM/2)). At fixed Mc this is an "
              "exact reciprocal identity, not an empirical correlation, so a "
              "low b and a high mean magnitude are one result reported twice."),
    )
    print(f"\n  b vs mean magnitude at fixed Mc: exact identity "
          f"(Spearman {out['b_meanmag_identity']['spearman']:+.3f}, "
          f"Pearson {out['b_meanmag_identity']['pearson']:+.3f} because the relation is reciprocal)")

    # ---- does the zone contrast survive removing the largest events? -----
    # The near-field zone is centred on the mainshock, so the largest events
    # sit inside it by construction. The contrast must be re-tested without
    # them before it can be called a property of the volume.
    sens_rows = []
    for cut in (None, 6.0, 5.5, 5.0):
        sub = cat if cut is None else cat[cat.mw < cut]
        tab_c = group_table(sub, "zone", mc, n_boot=200)
        near = tab_c[tab_c.group.str.startswith("near")]
        inter = tab_c[tab_c.group.str.startswith("intermediate")]
        if near.empty or inter.empty or not (near.estimable.iloc[0] and inter.estimable.iloc[0]):
            continue
        t = fmd.utsu_test(float(near.b.iloc[0]), int(near.n_above_mc.iloc[0]),
                          float(inter.b.iloc[0]), int(inter.n_above_mc.iloc[0]))
        sens_rows.append(dict(max_mw_excluded=("none" if cut is None else f">= {cut}"),
                              n_near=int(near.n_above_mc.iloc[0]),
                              b_near=float(near.b.iloc[0]),
                              n_inter=int(inter.n_above_mc.iloc[0]),
                              b_inter=float(inter.b.iloc[0]),
                              delta_b=float(near.b.iloc[0] - inter.b.iloc[0]),
                              p=t["p"]))
        r = sens_rows[-1]
        print(f"    excluding Mw {r['max_mw_excluded']:>6s}: b_near={r['b_near']:.3f} "
              f"b_inter={r['b_inter']:.3f}  db={r['delta_b']:+.3f}  p={r['p']:.4f}")
    pd.DataFrame(sens_rows).to_csv(f"{OUT}/b_zone_mainshock_sensitivity.csv", index=False)
    out["zone_mainshock_sensitivity"] = sens_rows

    # ---- permutation test on the strongest grouping ----------------------
    codes, uniq = pd.factorize(cat["zone"])
    perm = fmd.permutation_extreme_b(cat.mw.values, codes, mc, n_perm=5000,
                                     rng=np.random.default_rng(RNG))
    perm["labels"] = list(uniq)
    out["permutation_zone"] = perm
    print(f"  permutation test (zone): min b = {perm['b_min_obs']:.3f}, "
          f"p = {perm['p_min']:.4f}; b range = {perm['b_range_obs']:.3f}, p = {perm['p_range']:.4f}")

    # ---- sensitivity of b to the completeness choice ---------------------
    sens = [dict(mc=float(m), **{k: float(v) for k, v in
                                 fmd.b_value_aki(modern.mw.values, m).items()})
            for m in np.arange(3.4, 4.7, 0.1)]
    pd.DataFrame(sens).to_csv(f"{OUT}/b_vs_mc_sensitivity.csv", index=False)
    out["b_vs_mc"] = sens
    print("  b vs Mc: " + ", ".join(f"Mc={s['mc']:.1f}:b={s['b']:.2f}" for s in sens[::3]))

    with open(f"{OUT}/a4_fmd.json", "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print("\nwrote", f"{OUT}/a4_fmd.json")


if __name__ == "__main__":
    main()
