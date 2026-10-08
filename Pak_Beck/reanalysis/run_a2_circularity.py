"""Stage A2: is the temporal story discovered, or inserted through the input?

Time is one of the four clustering variables in the manuscript and is then
reused to order the clusters and define evolutionary stages. These experiments
separate the two roles: cluster without time, then test temporal organisation
independently; and re-run the whole procedure on catalogues whose event times
have been shuffled, which destroys any real temporal structure while leaving
the spatial pattern intact.
"""
from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "reanalysis")
import catalog, clustering as cl, features as ft, geometry as gm  # noqa: E402

OUT = "results/tables"
RNG = 20260903
K = 8


def temporal_spread(labels: np.ndarray, t_days: np.ndarray) -> float:
    """Between-cluster spread of mean occurrence date, in days.

    This is the statistic the manuscript's chronological ordering rests on:
    if clusters carry real temporal information, their mean dates should be
    more widely separated than random groupings of the same sizes.
    """
    means = [t_days[labels == u].mean() for u in np.unique(labels) if (labels == u).sum() > 0]
    return float(np.std(means, ddof=1)) if len(means) > 1 else np.nan


def localization_trend(labels: np.ndarray, df: pd.DataFrame) -> float:
    """Correlation between a cluster's mean date and its radius of gyration.

    Negative values mean later clusters are more compact, which is what the
    manuscript reports as progressive localization.
    """
    rows = []
    for u in np.unique(labels):
        m = labels == u
        if m.sum() < 5:
            continue
        g = gm.covariance_descriptors(df.loc[m, "east_km"], df.loc[m, "north_km"])
        rows.append((df.loc[m, "t_days"].mean(), g["R_g"]))
    if len(rows) < 4:
        return np.nan
    a = np.array(rows)
    return float(np.corrcoef(a[:, 0], a[:, 1])[0, 1])


def main() -> None:
    df, _ = catalog.quality_control(catalog.load_raw("data/lombok2018new.csv"))
    df = catalog.add_projection(df)
    s = catalog.subset(df, catalog.MANUSCRIPT_BOX, catalog.MANUSCRIPT_WINDOW, mmin=4.4)
    s = s.assign(t_days=catalog.elapsed_days(s)).reset_index(drop=True)
    rng = np.random.default_rng(RNG)
    out = {"n_events": len(s)}

    # ---- 1. Temporal separation is manufactured by including time ---------
    variants = {
        "ENZT (manuscript)": dict(use_time=True, use_depth=True),
        "ENZ (no time)": dict(use_time=False, use_depth=True),
        "EN (space only)": dict(use_time=False, use_depth=False),
    }
    rows = []
    for name, kw in variants.items():
        Xr, cols = ft.build_features(s, **kw)
        X = ft.scale(Xr, "minmax")
        lab = cl.baseline_labels(X, K, "kmeans", seed=RNG)
        obs = temporal_spread(lab, s["t_days"].to_numpy())

        # Null: random groupings of the same sizes.
        sizes = np.bincount(lab, minlength=K)
        null = []
        for _ in range(2000):
            perm = rng.permutation(len(s))
            fake = np.concatenate([np.full(n, i) for i, n in enumerate(sizes)])
            null.append(temporal_spread(fake[np.argsort(perm)], s["t_days"].to_numpy()))
        null = np.array(null)
        p = (np.sum(null >= obs) + 1) / (len(null) + 1)
        boot = cl.bootstrap_stability(X, K, "kmeans", n_boot=50, seed=RNG)
        rows.append(dict(features=name, temporal_spread_days=obs,
                         null_mean_days=float(null.mean()),
                         p_value=float(p), ari_bootstrap=boot["ari_mean"]))
        print(f"  {name:20s} temporal spread {obs:6.1f} d "
              f"(null {null.mean():5.1f} d, p={p:.4f})  ARI={boot['ari_mean']:.3f}")
    out["temporal_separation"] = rows
    pd.DataFrame(rows).to_csv(f"{OUT}/temporal_circularity.csv", index=False)

    # ---- 2. Progressive localization under a shuffled-time null -----------
    Xr, cols = ft.build_features(s, use_time=True, use_depth=True)
    X = ft.scale(Xr, "minmax")
    lab = cl.baseline_labels(X, K, "kmeans", seed=RNG)
    obs_trend = localization_trend(lab, s)

    null_trend = []
    for _ in range(500):
        sh = s.copy()
        sh["t_days"] = rng.permutation(s["t_days"].to_numpy())
        Xs = ft.scale(ft.build_features(sh, use_time=True, use_depth=True)[0], "minmax")
        lab_s = cl.baseline_labels(Xs, K, "kmeans", seed=int(rng.integers(1e6)))
        null_trend.append(localization_trend(lab_s, sh))
    null_trend = np.array([v for v in null_trend if np.isfinite(v)])
    p_trend = (np.sum(null_trend <= obs_trend) + 1) / (len(null_trend) + 1)
    out["progressive_localization"] = dict(
        observed_corr=obs_trend, null_mean=float(null_trend.mean()),
        null_sd=float(null_trend.std(ddof=1)), p_value=float(p_trend),
        n_null=int(null_trend.size))
    print(f"  localization corr(mean date, R_g) = {obs_trend:+.3f}  "
          f"shuffled-time null {null_trend.mean():+.3f} +- {null_trend.std(ddof=1):.3f}  p={p_trend:.3f}")

    # ---- 3. Depth structure versus the fixed-depth default ----------------
    dq_all = catalog.depth_quality(s)
    resolved = s[s["depth"] != catalog.DEFAULT_DEPTH_KM].reset_index(drop=True)

    # The replication sample is small and spans the full 0-350 km query depth,
    # so depth statistics are also reported for the crustal sequence region,
    # which is the population any seismogenic-layer claim would refer to.
    seq_reg = catalog.subset(df, catalog.SEQUENCE_BOX, catalog.MANUSCRIPT_WINDOW)
    seq_res = seq_reg[seq_reg["depth"] != catalog.DEFAULT_DEPTH_KM]
    out["depth_sequence_region"] = dict(
        **catalog.depth_quality(seq_reg),
        n_resolved=int(len(seq_res)),
        sd_depth_all=float(seq_reg["depth"].std(ddof=1)),
        sd_depth_resolved=float(seq_res["depth"].std(ddof=1)),
        median_depth=float(seq_reg["depth"].median()))
    d = out["depth_sequence_region"]
    print(f"  sequence region 2017-2019: n={d['n']}, {100*d['frac_default_depth']:.1f}% at the "
          f"{catalog.DEFAULT_DEPTH_KM:.0f} km default, {d['n_resolved']} resolved; "
          f"SD_Z {d['sd_depth_all']:.1f} km all vs {d['sd_depth_resolved']:.1f} km resolved")
    lab_all = lab
    depth_rows = []
    for name, sub, lb in [("all events", s, lab_all)]:
        for u in np.unique(lb):
            m = lb == u
            if m.sum() < 5:
                continue
            d = sub.loc[m, "depth"]
            depth_rows.append(dict(subset=name, cluster=int(u), n=int(m.sum()),
                                   mean_depth=float(d.mean()),
                                   sd_depth=float(d.std(ddof=1)),
                                   frac_default=float((d == catalog.DEFAULT_DEPTH_KM).mean())))
    dr = pd.DataFrame(depth_rows)
    dr.to_csv(f"{OUT}/depth_artefact.csv", index=False)
    # Does apparent depth compactness simply track the default-depth fraction?
    if len(dr) > 3:
        c = float(np.corrcoef(dr["frac_default"], dr["sd_depth"])[0, 1])
        out["depth_artefact"] = dict(
            sample="manuscript box, Mw >= 4.4, query depth 0-350 km",
            catalogue=dq_all, n_resolved=int(len(resolved)),
            corr_frac_default_vs_sd_depth=c,
            sd_depth_all=float(s["depth"].std(ddof=1)),
            sd_depth_resolved=float(resolved["depth"].std(ddof=1)))
        print(f"  depth: {100*dq_all['frac_default_depth']:.1f}% of events at the {catalog.DEFAULT_DEPTH_KM:.0f} km default; "
              f"corr(default fraction, SD_Z) = {c:+.3f}")

    # ---- 4. Scaling and feature-weighting sensitivity ---------------------
    scal_rows = []
    ref = cl.baseline_labels(ft.scale(Xr, "minmax"), K, "kmeans", seed=RNG)
    from sklearn.metrics import adjusted_rand_score
    for meth in ("minmax", "zscore", "robust", "mahalanobis"):
        lb = cl.baseline_labels(ft.scale(Xr, meth), K, "kmeans", seed=RNG)
        scal_rows.append(dict(scaling=meth, weights="equal",
                              ari_vs_minmax=float(adjusted_rand_score(ref, lb))))
    for w, tag in [((1, 1, 1, 0.5), "time x0.5"), ((1, 1, 1, 2.0), "time x2"),
                   ((0.5, 0.5, 1, 1), "horizontal x0.5")]:
        lb = cl.baseline_labels(ft.scale(Xr, "minmax", np.array(w)), K, "kmeans", seed=RNG)
        scal_rows.append(dict(scaling="minmax", weights=tag,
                              ari_vs_minmax=float(adjusted_rand_score(ref, lb))))
    pd.DataFrame(scal_rows).to_csv(f"{OUT}/scaling_sensitivity.csv", index=False)
    out["scaling_sensitivity"] = scal_rows
    for r in scal_rows:
        print(f"  scaling {r['scaling']:12s} {r['weights']:16s} ARI vs min-max = {r['ari_vs_minmax']:.3f}")

    with open(f"{OUT}/a2_circularity.json", "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print("wrote", f"{OUT}/a2_circularity.json")


if __name__ == "__main__":
    main()
