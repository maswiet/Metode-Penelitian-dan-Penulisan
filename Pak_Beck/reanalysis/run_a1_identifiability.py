"""Stage A1: is the eight-cluster partition identifiable at all?

Reproduces the manuscript's winner-take-all procedure and subjects it to the
order, initialisation and resampling tests the review requires, then scans the
cluster number against internal validity indices and bootstrap stability.
"""
from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import adjusted_rand_score

sys.path.insert(0, "reanalysis")
import catalog, clustering as cl, features as ft  # noqa: E402

OUT = "results/tables"
RNG = 20260903


def manuscript_scale_sample(df: pd.DataFrame, mmin: float = 4.4) -> pd.DataFrame:
    """A subset of comparable size to the 248 events the manuscript analysed."""
    s = catalog.subset(df, catalog.MANUSCRIPT_BOX, catalog.MANUSCRIPT_WINDOW, mmin=mmin)
    return s.assign(t_days=catalog.elapsed_days(s))


def main() -> None:
    df, qc = catalog.quality_control(catalog.load_raw("data/lombok2018new.csv"))
    df = catalog.add_projection(df)
    sample = manuscript_scale_sample(df)
    X_raw, cols = ft.build_features(sample)
    X = ft.scale(X_raw, "minmax")
    print(f"replication sample: n={len(sample)}  features={cols}")

    results = {"qc": qc, "n_events": len(sample), "features": cols}

    # ---- the learning-rate schedule actually anneals to nothing ------------
    alphas = {e: 0.01 * 0.5**e for e in (0, 5, 10, 20, 50, 100)}
    short = cl.wta_competitive(X, k=8, epochs=25, rng=np.random.default_rng(RNG))
    full = cl.wta_competitive(X, k=8, epochs=100, rng=np.random.default_rng(RNG))
    results["learning_rate"] = {
        "alpha_by_epoch": {str(k): v for k, v in alphas.items()},
        "labels_identical_25_vs_100_epochs": bool((short["labels"] == full["labels"]).all()),
        "max_prototype_shift_after_epoch25": float(np.abs(full["W"] - short["W"]).max()),
    }
    print("  alpha(20) = %.3e, alpha(100) = %.3e" % (alphas[20], alphas[100]))
    print("  labels identical at 25 vs 100 epochs:",
          results["learning_rate"]["labels_identical_25_vs_100_epochs"])

    # ---- order, initialisation and bootstrap stability at K = 8 -----------
    print("  order sensitivity (200 shuffles)...")
    order = cl.order_sensitivity(X, k=8, n_perm=200, seed=RNG, epochs=25)
    print("  init sensitivity...")
    init = cl.init_sensitivity(X, k=8, seed=RNG, epochs=25)
    print("  bootstrap stability...")
    boot_wta = cl.bootstrap_stability(X, 8, "wta", n_boot=100, seed=RNG)
    boot_km = cl.bootstrap_stability(X, 8, "kmeans", n_boot=100, seed=RNG)

    results["stability_k8"] = {
        "order_shuffle": {k: v for k, v in order.items() if k != "scores"},
        "initialisation": init,
        "bootstrap_wta": {k: v for k, v in boot_wta.items() if k != "scores"},
        "bootstrap_kmeans": {k: v for k, v in boot_km.items() if k != "scores"},
    }
    print("  ARI vs shuffled order: %.3f +- %.3f (min %.3f)"
          % (order["ari_mean"], order["ari_std"], order["ari_min"]))
    print("  ARI bootstrap WTA    : %.3f    kmeans: %.3f"
          % (boot_wta["ari_mean"], boot_km["ari_mean"]))

    # ---- is the WTA partition even different from plain k-means? ----------
    ref = cl.wta_competitive(X, k=8, epochs=25, rng=np.random.default_rng(RNG))["labels"]
    km = cl.baseline_labels(X, 8, "kmeans", seed=RNG)
    results["wta_vs_kmeans_ari"] = float(adjusted_rand_score(ref, km))
    print("  ARI(WTA, k-means) at K=8: %.3f" % results["wta_vs_kmeans_ari"])

    # ---- cluster-number scan ---------------------------------------------
    print("  scanning K = 2..15 ...")
    rows = []
    for k in range(2, 16):
        lab = cl.baseline_labels(X, k, "kmeans", seed=RNG)
        vi = cl.validity_indices(X, lab)
        gap = cl.gap_statistic(X, k, n_ref=30, seed=RNG)
        bs = cl.bootstrap_stability(X, k, "kmeans", n_boot=50, seed=RNG)
        rows.append(dict(K=k, **vi, gap=gap["gap"], gap_sk=gap["sk"],
                         ari_boot=bs["ari_mean"], ari_boot_sd=bs["ari_std"]))
        print(f"    K={k:2d} sil={vi['silhouette']:.3f} DB={vi['davies_bouldin']:.3f} "
              f"CH={vi['calinski_harabasz']:7.1f} gap={gap['gap']:.3f} ARI={bs['ari_mean']:.3f}")
    scan = pd.DataFrame(rows)
    scan.to_csv(f"{OUT}/k_scan.csv", index=False)

    # ---- does C3/C4 persist across K? ------------------------------------
    print("  cluster persistence across K ...")
    base = cl.baseline_labels(X, 8, "kmeans", seed=RNG)
    pers = []
    for k in range(6, 11):
        lab = cl.baseline_labels(X, k, "kmeans", seed=RNG)
        for c in np.unique(base):
            members = base == c
            # Best Jaccard overlap with any cluster at this K.
            j = max(((members & (lab == o)).sum() /
                     max((members | (lab == o)).sum(), 1)) for o in np.unique(lab))
            pers.append(dict(K=k, cluster=int(c), n=int(members.sum()),
                             best_jaccard=float(j)))
    pd.DataFrame(pers).to_csv(f"{OUT}/cluster_persistence.csv", index=False)

    # ---- the metric's implicit exchange rate ------------------------------
    results["metric"] = ft.metric_exchange_rate(sample, cols)
    print("  metric: %.1f days per km of depth; %.1f days per km horizontal"
          % (results["metric"]["days_per_km_depth"],
             results["metric"]["days_per_km_horizontal"]))

    with open(f"{OUT}/a1_identifiability.json", "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print("wrote", f"{OUT}/a1_identifiability.json")


if __name__ == "__main__":
    main()
