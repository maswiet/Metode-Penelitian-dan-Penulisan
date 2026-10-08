"""Stage A6: what spatial structure is actually supported, and by which method?

Clusters the completeness-limited catalogue on space alone, so that occurrence
time stays available as an independent test variable, scans the cluster number
against validity and stability, benchmarks the manuscript's procedure against a
genuine SOM and standard algorithms, and characterises only the partition that
survives.
"""
from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import adjusted_rand_score

sys.path.insert(0, "reanalysis")
import catalog, clustering as cl, features as ft, fmd, geometry as gm, seismicity as sz  # noqa: E402

OUT = "results/tables"
RNG = 20260903


def main() -> None:
    df, _ = catalog.quality_control(catalog.load_raw("data/lombok2018new.csv"))
    df = catalog.add_projection(df)
    region = catalog.subset(df, catalog.SEQUENCE_BOX)
    modern = region[region.dt >= catalog.MODERN_ERA_START]
    mc = float(np.ceil(fmd.mc_goodness_of_fit(modern.mw.values)["mc"] * 10) / 10)
    cat = modern[modern.mw >= mc].reset_index(drop=True)
    cat = cat.assign(t_days=catalog.elapsed_days(cat))
    print(f"structure set: n={len(cat)} events at Mw >= {mc:.1f}")
    out = {"n": len(cat), "mc": mc}

    # Space only: time is deliberately withheld so it can serve as an
    # independent test of whatever partition emerges.
    X = ft.scale(cat[["east_km", "north_km"]].to_numpy(float), "minmax")

    # ---- how many spatial groups does the catalogue support? -------------
    rows = []
    for k in range(2, 13):
        lab = cl.baseline_labels(X, k, "kmeans", seed=RNG)
        vi = cl.validity_indices(X, lab)
        bs = cl.bootstrap_stability(X, k, "kmeans", n_boot=60, seed=RNG)
        gap = cl.gap_statistic(X, k, n_ref=30, seed=RNG)
        rows.append(dict(K=k, **vi, gap=gap["gap"], ari_boot=bs["ari_mean"],
                         ari_boot_p05=bs["ari_p05"]))
        print(f"  K={k:2d} sil={vi['silhouette']:.3f} DB={vi['davies_bouldin']:.3f} "
              f"gap={gap['gap']:.3f} ARI={bs['ari_mean']:.3f} (5th pct {bs['ari_p05']:.3f})")
    scan = pd.DataFrame(rows)
    scan.to_csv(f"{OUT}/spatial_k_scan.csv", index=False)

    # Prefer the largest K that is both well separated and reproducible.
    ok = scan[(scan.ari_boot >= 0.80)]
    k_best = int(ok.loc[ok.silhouette.idxmax(), "K"]) if len(ok) else int(scan.loc[scan.silhouette.idxmax(), "K"])
    out["k_selected"] = k_best
    out["k_scan"] = scan.to_dict("records")
    print(f"  selected K = {k_best} (highest silhouette among partitions with bootstrap ARI >= 0.80)")

    # ---- method benchmark at the selected K ------------------------------
    ref = cl.baseline_labels(X, k_best, "kmeans", seed=RNG)
    bench = []
    for meth in ("kmeans", "gmm", "ward", "wta", "som"):
        kw = {"grid": (k_best, 1)} if meth == "som" else {}
        lab = cl.baseline_labels(X, k_best, meth, seed=RNG, **kw)
        bs = cl.bootstrap_stability(X, k_best, meth, n_boot=50, seed=RNG, **kw)
        vi = cl.validity_indices(X, lab)
        bench.append(dict(method=meth, silhouette=vi["silhouette"],
                          ari_vs_kmeans=float(adjusted_rand_score(ref, lab)),
                          ari_bootstrap=bs["ari_mean"]))
        print(f"  {meth:8s} sil={vi['silhouette']:.3f}  ARI vs kmeans={bench[-1]['ari_vs_kmeans']:.3f}  "
              f"bootstrap ARI={bs['ari_mean']:.3f}")
    hdb = cl.baseline_labels(X, k_best, "hdbscan", seed=RNG, min_cluster_size=30)
    bench.append(dict(method="hdbscan", silhouette=cl.validity_indices(X, hdb)["silhouette"],
                      ari_vs_kmeans=float(adjusted_rand_score(ref, hdb)),
                      ari_bootstrap=np.nan))
    print(f"  hdbscan  found {len(set(hdb[hdb>=0]))} clusters, "
          f"{100*(hdb<0).mean():.1f}% classed as noise")
    pd.DataFrame(bench).to_csv(f"{OUT}/method_benchmark.csv", index=False)
    out["benchmark"] = bench
    out["hdbscan"] = dict(n_clusters=int(len(set(hdb[hdb >= 0]))),
                          noise_fraction=float((hdb < 0).mean()))

    # ---- a genuine SOM: quantisation and topographic error ---------------
    som = cl.kohonen_som(X, grid=(4, 2), epochs=150, rng=np.random.default_rng(RNG))
    wta = cl.wta_competitive(X, k=8, epochs=25, rng=np.random.default_rng(RNG))
    out["som_vs_wta"] = dict(
        som_qe=som["qe"], som_te=som["te"], wta_qe=wta["qe"],
        note=("Topographic error is defined only where a lattice exists. The "
              "winner-take-all procedure has no lattice, so it has no "
              "topographic error and cannot be said to preserve topology."),
        u_matrix=som["umatrix"].tolist())
    print(f"  true SOM (4x2): QE={som['qe']:.4f}, TE={som['te']:.4f}; "
          f"WTA K=8: QE={wta['qe']:.4f}, TE undefined (no lattice)")

    # ---- characterise the surviving partition ----------------------------
    lab = ref
    ms = cat.loc[cat.mw.idxmax()]
    floor = gm.location_error_floor()
    recs = []
    for u in np.unique(lab):
        m = lab == u
        sub = cat[m]
        g = gm.covariance_descriptors(sub.east_km, sub.north_km)
        rg = gm.bootstrap_descriptor(sub.east_km.values, sub.north_km.values,
                                     "R_g", n_boot=300,
                                     jitter_km=floor["sd_horizontal_km"], seed=RNG)
        est = fmd.b_value_aki(sub.mw.values, mc)
        recs.append(dict(
            group=int(u), n=int(m.sum()),
            lat=float(sub.lat.mean()), lon=float(sub.lon.mean()),
            dist_mainshock_km=float(sz._haversine_km(sub.lat.mean(), sub.lon.mean(), ms.lat, ms.lon)),
            R_g_km=g["R_g"], R_g_ci_lo=rg["ci"][0], R_g_ci_hi=rg["ci"][1],
            major_km=g["major_km"], minor_km=g["minor_km"],
            elongation=g["elongation"], azimuth_deg=g["azimuth_deg"],
            hull_area_km2=g["hull_area_km2"],
            SD_R_km=gm.radial_stats(sub.east_km, sub.north_km)["SD_R"],
            median_date=str(sub.dt.median().date()),
            frac_default_depth=float((sub.depth == catalog.DEFAULT_DEPTH_KM).mean()),
            b=est["b"], sigma_b=est["sigma_b"], n_above_mc=est["n"]))
    prof = pd.DataFrame(recs)
    prof.to_csv(f"{OUT}/robust_groups.csv", index=False)
    out["groups"] = recs
    out["location_error_floor"] = floor
    print("\n  surviving spatial groups:")
    for r in recs:
        print(f"    G{r['group']}: n={r['n']:4d}  R_g={r['R_g_km']:5.1f} km "
              f"[{r['R_g_ci_lo']:.1f}, {r['R_g_ci_hi']:.1f}]  SD_R={r['SD_R_km']:5.1f}  "
              f"elong={r['elongation']:.2f} az={r['azimuth_deg']:5.1f} deg  "
              f"b={r['b']:.2f}+-{r['sigma_b']:.2f}")

    with open(f"{OUT}/a6_structure.json", "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print("wrote", f"{OUT}/a6_structure.json")


if __name__ == "__main__":
    main()
