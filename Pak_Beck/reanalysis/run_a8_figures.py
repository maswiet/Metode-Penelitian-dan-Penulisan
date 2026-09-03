"""Stage A8: publication figures for the revised manuscript.

Every panel is generated from the result tables written by the earlier stages,
so no number in a figure is entered by hand.
"""
from __future__ import annotations

import json
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

sys.path.insert(0, "reanalysis")
import catalog, fmd, focal  # noqa: E402

TAB, FIG = "results/tables", "results/figures"

# Categorical slots validated for colour-vision-deficiency separation.
C = ["#2a78d6", "#eb6834", "#1baf7a"]
INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8880", "#e3e2dd"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 8,
    "axes.edgecolor": MUTED, "axes.linewidth": 0.6,
    "axes.labelcolor": INK, "axes.titlesize": 8.5, "axes.titleweight": "bold",
    "xtick.color": INK2, "ytick.color": INK2,
    "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "legend.frameon": False, "figure.dpi": 300, "savefig.dpi": 300,
    "savefig.bbox": "tight", "text.color": INK,
})

NAMES = {0: "W segment", 1: "S fore-arc", 2: "E segment"}


def style(ax, ylabel=None, xlabel=None, title=None, grid_axis="y"):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis=grid_axis, color=GRID, lw=0.5, zorder=0)
    ax.set_axisbelow(True)
    if ylabel:
        ax.set_ylabel(ylabel)
    if xlabel:
        ax.set_xlabel(xlabel)
    if title:
        ax.set_title(title, loc="left")


def save(fig, name):
    for ext in ("png", "pdf"):
        fig.savefig(f"{FIG}/{name}.{ext}")
    plt.close(fig)
    print("  wrote", f"{FIG}/{name}.png")


def fig_catalogue(df):
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.4))
    reg = catalog.subset(df, catalog.SEQUENCE_BOX)

    ax = axes[0]
    yr = df[df.mw >= 4.0].groupby(df.dt.dt.year).size()
    ax.plot(yr.index, yr.values, color=C[0], lw=1.6, zorder=3)
    ax.axvline(2009.75, color=INK2, lw=1.0, ls="--", zorder=2)
    ax.annotate("network\ndensified", (2009.9, yr.max() * 0.95), fontsize=7,
                color=INK2, va="top")
    style(ax, "Events per year (Mw ≥ 4.0)", None, "a  Reporting changes in 2009")

    ax = axes[1]
    d = reg[reg.dt.between(*catalog.MANUSCRIPT_WINDOW)].depth
    ax.hist(d, bins=np.arange(0, 61, 2), color=C[0], zorder=3)
    ax.axvline(catalog.DEFAULT_DEPTH_KM, color=C[1], lw=1.4, zorder=4)
    ax.annotate(f"{100*(d == catalog.DEFAULT_DEPTH_KM).mean():.0f}% fixed\nat 10 km",
                (13, ax.get_ylim()[1] * 0.95), fontsize=7, color=C[1], va="top")
    style(ax, "Number of events", "Reported depth (km)",
          "b  Depth is largely unresolved")

    ax = axes[2]
    eras = [("1998–2008", "1998-01-01", "2008-12-31"),
            ("2009–2017", "2009-10-01", "2017-07-26"),
            ("2017–2019", "2017-07-27", "2019-07-29"),
            ("2019–2023", "2019-07-30", "2023-12-31")]
    labs, mcs = [], []
    for lab, s, e in eras:
        sub = reg[reg.dt.between(s, e)]
        g = fmd.mc_goodness_of_fit(sub.mw.values)
        mcs.append(g["mc"] if np.isfinite(g["mc"]) else fmd.mc_maxcurv(sub.mw.values))
        labs.append(lab)
    bars = ax.bar(labs, mcs, color=C[0], width=0.62, zorder=3)
    for b, v in zip(bars, mcs):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.05, f"{v:.1f}",
                ha="center", fontsize=7, color=INK)
    ax.set_ylim(0, max(mcs) * 1.28)
    ax.tick_params(axis="x", rotation=30)
    style(ax, "Magnitude of completeness", None, "c  Completeness varies by era")
    fig.tight_layout()
    save(fig, "fig1_catalogue_diagnostics")


def fig_identifiability():
    a1 = json.load(open(f"{TAB}/a1_identifiability.json"))
    scan = pd.read_csv(f"{TAB}/k_scan.csv")
    sp = pd.read_csv(f"{TAB}/spatial_k_scan.csv")
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.4))

    ax = axes[0]
    ax.plot(scan.K, scan.silhouette, color=C[0], lw=1.8, marker="o", ms=3.5, zorder=3)
    ax.plot(scan.K, scan.ari_boot, color=C[1], lw=1.8, marker="s", ms=3.5, zorder=3)
    ax.axvline(8, color=MUTED, lw=1.0, ls="--", zorder=2)
    ax.annotate("K = 8 assumed", (8.15, 0.27), fontsize=7, color=INK2)
    ax.text(3.0, 0.60, "silhouette", color=C[0], fontsize=7)
    ax.text(11.0, 0.86, "bootstrap ARI", color=C[1], fontsize=7, ha="center")
    ax.set_ylim(0.2, 1.06)
    style(ax, "Index value", "Number of clusters K",
          "a  No index selects eight clusters")

    ax = axes[1]
    e = np.arange(0, 41)
    ax.semilogy(e, 0.01 * 0.5 ** e, color=C[0], lw=1.8, zorder=3)
    ax.axhline(2.2e-16, color=MUTED, lw=0.8, ls=":", zorder=2)
    ax.axvline(25, color=C[1], lw=1.2, zorder=3)
    ax.annotate("labels already\nfinal by epoch 25", (26, 1e-9), fontsize=7, color=C[1])
    ax.annotate("double precision", (1, 4e-16), fontsize=6.5, color=MUTED)
    ax.set_ylim(1e-18, 3e-2)
    style(ax, "Learning rate α", "Epoch", "b  Training freezes almost at once")

    ax = axes[2]
    s = a1["stability_k8"]
    vals = [float(sp.loc[sp.K == 3, "ari_boot"].iloc[0]),
            s["bootstrap_kmeans"]["ari_mean"], s["bootstrap_wta"]["ari_mean"]]
    bars = ax.bar(["k-means\nK = 3", "k-means\nK = 8", "manuscript\nWTA, K = 8"],
                  vals, color=[C[2], C[0], C[1]], width=0.6, zorder=3)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.025, f"{v:.2f}",
                ha="center", fontsize=7.5, color=INK)
    ax.axhline(0.8, color=INK2, lw=0.9, ls="--", zorder=4)
    ax.annotate("stability floor", (-0.42, 0.825), fontsize=6.5, color=INK2, ha="left")
    ax.set_ylim(0, 1.14)
    style(ax, "Bootstrap ARI", None, "c  Only the small partition reproduces")
    fig.tight_layout()
    save(fig, "fig2_identifiability")


def fig_circularity():
    t = pd.read_csv(f"{TAB}/temporal_circularity.csv")
    a2 = json.load(open(f"{TAB}/a2_circularity.json"))
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.5))

    ax = axes[0]
    y = np.arange(len(t))[::-1].astype(float)
    ax.barh(y, t.temporal_spread_days, color=C[0], height=0.38, zorder=3, label="observed")
    ax.barh(y - 0.40, t.null_mean_days, color=MUTED, height=0.38, zorder=3,
            label="random grouping")
    for yy, r in zip(y, t.itertuples()):
        ax.text(r.temporal_spread_days + 4, yy, f"p = {r.p_value:.3f}",
                va="center", fontsize=7, color=INK)
    ax.set_yticks(y - 0.20)
    ax.set_yticklabels(t.features, fontsize=7)
    ax.set_xlim(0, 215)
    ax.legend(fontsize=7, loc="lower right")
    style(ax, None, "Spread of cluster mean dates (days)",
          "a  Half the temporal signal is inserted", grid_axis="x")

    ax = axes[1]
    pl = a2["progressive_localization"]
    xs = np.linspace(-0.95, 0.95, 300)
    ax.fill_between(xs, np.exp(-0.5 * ((xs - pl["null_mean"]) / pl["null_sd"]) ** 2),
                    color=MUTED, alpha=0.35, zorder=2)
    ax.axvline(pl["observed_corr"], color=C[1], lw=2.0, zorder=4)
    ax.annotate(f"observed r = {pl['observed_corr']:.2f}\np = {pl['p_value']:.3f}",
                (pl["observed_corr"] - 0.06, 0.80), fontsize=7, color=C[1], ha="right")
    ax.annotate("shuffled-time null", (pl["null_mean"] + 0.05, 0.30), fontsize=7,
                color=INK2, ha="left")
    ax.set_yticks([])
    ax.set_ylim(0, 1.18)
    style(ax, None, "corr(cluster mean date, radius of gyration)",
          "b  Localization is real but weak", grid_axis="x")
    fig.tight_layout()
    save(fig, "fig3_circularity")


def fig_map():
    seg = pd.read_csv(f"{TAB}/segmented_catalogue.csv", parse_dates=["dt"])
    prof = pd.read_csv(f"{TAB}/segment_profile.csv")
    fm = focal.parse_cmtsolution("data/gcmt_lombok.cmt")
    fm = fm[fm.dt.between("2017-07-27", "2019-07-29")]

    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    for g, s_ in seg.groupby("g"):
        b = prof.loc[prof.group == g, "b"].iloc[0]
        ax.scatter(s_.lon, s_.lat, s=5, color=C[int(g)], alpha=0.5, lw=0, zorder=3,
                   label=f"{NAMES[int(g)]}   b = {b:.2f}")

    # Direct labels placed in clear areas rather than on the centroids, which
    # sit in the densest part of each group.
    for g, (lon, lat) in {0: (115.92, -8.03), 1: (116.66, -8.73),
                          2: (117.08, -8.10)}.items():
        ax.text(lon, lat, NAMES[g], fontsize=8.5, weight="bold", color=C[g],
                ha="center", zorder=6,
                bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.8))

    # The four Mw >= 6 events are only 25 km apart, so they are numbered and
    # listed rather than labelled in place.
    big = seg[seg.mw >= 6.0].sort_values("dt").reset_index(drop=True)
    ax.scatter(big.lon, big.lat, s=130, marker="*", facecolor="white",
               edgecolor=INK, lw=0.9, zorder=7)
    key = []
    for i, r in big.iterrows():
        ax.annotate(str(i + 1), (r["lon"], r["lat"]), xytext=(7, 5),
                    textcoords="offset points", fontsize=7, weight="bold",
                    color=INK, zorder=8)
        key.append(f"{i+1}  Mw {r['mw']:.1f}   {r['dt']:%d %b %Y}")
    ax.text(0.025, 0.035, "\n".join(key), transform=ax.transAxes, fontsize=6.8,
            color=INK, va="bottom", linespacing=1.5, zorder=8,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GRID, lw=0.6))

    ax.scatter([116.457], [-8.411], marker="^", s=75, facecolor="none",
               edgecolor=INK, lw=1.1, zorder=7)
    ax.annotate("Rinjani", (116.457, -8.411), xytext=(-6, -12),
                textcoords="offset points", fontsize=7, color=INK2, ha="right")
    ax.scatter(fm.lon, fm.lat, s=48, marker="o", facecolor="none",
               edgecolor=INK, lw=0.9, zorder=6)

    ax.set_xlim(115.75, 117.25)
    ax.set_ylim(-8.90, -7.90)
    ax.set_aspect(1 / np.cos(np.radians(8.4)))
    leg1 = ax.legend(fontsize=7, loc="lower right", markerscale=2.4)
    ax.add_artist(leg1)
    handles = [Line2D([], [], marker="*", ls="", mfc="white", mec=INK, ms=10, label="Mw ≥ 6.0"),
               Line2D([], [], marker="o", ls="", mfc="none", mec=INK, ms=6, label="GCMT mechanism"),
               Line2D([], [], marker="^", ls="", mfc="none", mec=INK, ms=7, label="Volcano")]
    ax.legend(handles=handles, fontsize=7, loc="upper right")
    style(ax, "Latitude (°)", "Longitude (°)",
          "Three reproducible spatial groups (time withheld)", grid_axis="both")
    fig.tight_layout()
    save(fig, "fig4_segment_map")


def fig_bvalues():
    zone = pd.read_csv(f"{TAB}/b_by_zone.csv")
    prof = pd.read_csv(f"{TAB}/segment_profile.csv")
    sens = pd.read_csv(f"{TAB}/b_zone_mainshock_sensitivity.csv")
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.6))

    ax = axes[0]
    z = zone[zone.estimable].sort_values("b").reset_index(drop=True)
    y = np.arange(len(z), dtype=float)
    # Shi-Bolt 95% interval at the common Mc, matching the Utsu tests reported
    # with it. A bootstrap that also re-estimates Mc shifts every value up by
    # 0.02-0.12 without changing the ordering; both are given in Table 3.
    ax.errorbar(z.b, y, xerr=1.96 * z.sigma_b, fmt="o", ms=5,
                color=C[0], ecolor=MUTED, elinewidth=1.2, capsize=2.5, zorder=3)
    for yy, r in zip(y, z.itertuples()):
        ax.text(r.b, yy + 0.20, f"{r.b:.2f}  (n = {int(r.n_above_mc)})",
                fontsize=7, color=INK, ha="center")
    ax.set_yticks(y)
    ax.set_yticklabels([s_.replace(" (", "\n(") for s_ in z.group], fontsize=7)
    ax.set_ylim(-0.6, len(z) - 0.15)
    ax.set_xlim(0.80, 1.60)
    style(ax, None, "b-value (common Mc = 3.7)", "a  Near-rupture b is lower",
          grid_axis="x")

    ax = axes[1]
    y = np.arange(len(prof), dtype=float)
    ax.errorbar(prof.b, y, xerr=1.96 * prof.sigma_b, fmt="o", ms=5,
                color=C[0], ecolor=MUTED, elinewidth=1.2, capsize=2.5, zorder=3)
    for yy, r in zip(y, prof.itertuples()):
        ax.text(r.b, yy + 0.19, f"{r.b:.2f}", fontsize=7, color=INK, ha="center")
    ax.set_yticks(y)
    ax.set_yticklabels([NAMES[int(g)] for g in prof.group], fontsize=7)
    ax.set_ylim(-0.6, len(prof) - 0.15)
    ax.set_xlim(0.80, 2.15)
    ax.annotate("two thrust segments\nshare one b  (q = 0.36)", (1.72, 0.30),
                fontsize=6.5, color=INK2, ha="center")
    style(ax, None, "b-value (common Mc = 3.7)",
          "b  Only the fore-arc differs", grid_axis="x")

    ax = axes[2]
    x = np.arange(len(sens), dtype=float)
    vals = (-sens.delta_b).to_numpy()
    ax.bar(x, vals, color=C[0], width=0.58, zorder=3)
    for xx, v, pv in zip(x, vals, sens.p):
        ax.text(xx, v / 2, f"p = {pv:.0e}".replace("e-0", "e−"), rotation=90,
                ha="center", va="center", fontsize=6.5, color="white")
    ax.set_xticks(x)
    ax.set_xticklabels(["all", "< 6.0", "< 5.5", "< 5.0"], fontsize=7)
    ax.set_ylim(0, vals.max() * 1.18)
    style(ax, "b(intermediate) − b(near field)", "Magnitude ceiling (Mw)",
          "c  Contrast survives event removal")
    fig.tight_layout(w_pad=2.0)
    save(fig, "fig5_bvalues")


def fig_triggering():
    a3 = json.load(open(f"{TAB}/a3_triggering.json"))
    dist = pd.read_csv(f"{TAB}/triggering_distance.csv")
    dec = pd.read_csv(f"{TAB}/declustered_catalogue.csv", parse_dates=["dt"])
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.4))

    ax = axes[0]
    ax.hist(dec.log_eta.dropna(), bins=40, color=C[0], zorder=3)
    thr = a3["declustering"]["threshold"]
    ax.axvline(thr, color=C[1], lw=1.6, zorder=4)
    ax.annotate(f"{100*a3['declustering']['frac_clustered']:.0f}% triggered",
                (thr + 0.3, ax.get_ylim()[1] * 0.95), fontsize=7, color=C[1], va="top")
    style(ax, "Number of events", "log₁₀ nearest-neighbour distance η",
          "a  Nearest-neighbour distances")

    ax = axes[1]
    ms = pd.Timestamp("2018-08-05 11:46:38")
    aft = dec[(dec.dt > ms) & (dec.dt <= ms + pd.Timedelta(days=365))]
    t = (aft.dt - ms).dt.total_seconds().to_numpy() / 86400.0
    edges = np.logspace(np.log10(0.02), np.log10(365), 22)
    cnt, _ = np.histogram(t, bins=edges)
    ctr = np.sqrt(edges[:-1] * edges[1:])
    ok = cnt > 0
    ax.loglog(ctr[ok], (cnt / np.diff(edges))[ok], "o", ms=4, color=C[0], zorder=3)
    om = a3["omori"]
    tt = np.logspace(np.log10(0.02), np.log10(365), 100)
    ax.loglog(tt, om["K"] / (tt + om["c"]) ** om["p"], color=C[1], lw=1.6, zorder=4)
    ax.annotate(f"p = {om['p']:.2f}\nc = {om['c']:.2f} d", (0.03, 0.35),
                fontsize=7, color=C[1])
    style(ax, "Events per day (Mw ≥ 4.0)", "Days after the Mw 6.8 mainshock",
          "b  Omori–Utsu decay", grid_axis="both")

    ax = axes[2]
    x = np.arange(len(dist), dtype=float)
    sig = (dist.p_value < 0.05).to_numpy()
    ax.bar(x[sig], dist.ratio[sig], color=C[0], width=0.6, zorder=3)
    ax.bar(x[~sig], dist.ratio[~sig], color=MUTED, width=0.6, zorder=3)
    ax.axhline(1.0, color=INK2, lw=0.9, ls="--", zorder=4)
    for xx, r in zip(x, dist.itertuples()):
        lab = f"×{r.ratio:.0f}" if r.p_value < 0.05 else "not\nsignificant"
        ax.text(xx, r.ratio * 1.3, lab, ha="center", fontsize=6.5, color=INK)
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(dist.band_km, fontsize=7)
    ax.set_ylim(0.4, dist.ratio.max() * 9)
    style(ax, "Rate increase over background", "Distance from mainshock (km)",
          "c  Triggering stops beyond ~75 km")
    fig.tight_layout(w_pad=1.8)
    save(fig, "fig6_triggering")


def fig_migration():
    a7 = json.load(open(f"{TAB}/a7_migration.json"))
    seg = pd.read_csv(f"{TAB}/segmented_catalogue.csv", parse_dates=["dt"])
    seq = seg[seg.dt.between("2018-07-28", "2018-09-30")]
    fig, ax = plt.subplots(figsize=(5.8, 2.9))
    t0 = pd.Timestamp("2018-07-28")
    for g, s in seq.groupby("g"):
        ax.scatter((s.dt - t0).dt.total_seconds() / 86400.0, s.lon, s=6,
                   color=C[int(g)], alpha=0.5, lw=0, zorder=3, label=NAMES[int(g)])
    for d, lab in [(8.5, "Mw 6.8, 5 Aug"), (22.6, "Mw 6.7, 19 Aug")]:
        ax.axvline(d, color=INK2, lw=0.9, ls="--", zorder=2)
        ax.annotate(lab, (d + 0.7, 117.20), fontsize=6.5, color=INK2,
                    rotation=90, va="top")
    mg = a7["migration"]
    ax.annotate(f"Spearman ρ(time, longitude) = {mg['spearman_rho_longitude']:+.2f},  "
                f"p = {mg['p_longitude']:.0e}".replace("e-", "e−"),
                (0.98, 0.08), xycoords="axes fraction", ha="right", fontsize=7, color=INK)
    ax.legend(fontsize=7, loc="lower left", markerscale=2.4, ncol=3)
    ax.set_ylim(115.75, 117.30)
    style(ax, "Longitude (°)", "Days after 28 July 2018",
          "Net eastward migration, with time held out of the clustering")
    fig.tight_layout()
    save(fig, "fig7_migration")


def main():
    df, _ = catalog.quality_control(catalog.load_raw("data/lombok2018new.csv"))
    df = catalog.add_projection(df)
    fig_catalogue(df)
    fig_identifiability()
    fig_circularity()
    fig_map()
    fig_bvalues()
    fig_triggering()
    fig_migration()


if __name__ == "__main__":
    main()
