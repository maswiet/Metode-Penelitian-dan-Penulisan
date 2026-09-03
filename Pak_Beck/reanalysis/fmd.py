"""Frequency-magnitude distribution: completeness, b-value and formal tests.

Implements the estimators the review requires: goodness-of-fit completeness
(Wiemer & Wyss, 2000), maximum curvature, bootstrap uncertainties on both Mc
and b, the Utsu likelihood-ratio test for b-value differences, and a
permutation test for magnitude-cluster association.
"""
from __future__ import annotations

import numpy as np
from scipy import stats

LOG10E = np.log10(np.e)


def _binned(mags: np.ndarray, dm: float) -> np.ndarray:
    return np.round(np.asarray(mags, float) / dm) * dm


def b_value_aki(mags: np.ndarray, mc: float, dm: float = 0.1) -> dict:
    """Aki (1965) maximum-likelihood b with the Bender (1983) bin correction.

    Returns b, the Shi & Bolt (1982) standard error, the a-value and n.
    """
    m = np.asarray(mags, float)
    m = m[m >= mc - dm / 2 + 1e-9]
    n = m.size
    if n < 2:
        return dict(b=np.nan, sigma_b=np.nan, a=np.nan, n=n, mean_mag=np.nan)

    mbar = m.mean()
    m_min = mc - dm / 2.0
    denom = mbar - m_min
    if denom <= 0:
        return dict(b=np.nan, sigma_b=np.nan, a=np.nan, n=n, mean_mag=mbar)

    b = LOG10E / denom
    # Shi & Bolt (1982)
    sigma_b = 2.303 * b**2 * np.sqrt(np.sum((m - mbar) ** 2) / (n * (n - 1)))
    a = np.log10(n) + b * mc
    return dict(b=b, sigma_b=sigma_b, a=a, n=n, mean_mag=mbar)


def mc_maxcurv(mags: np.ndarray, dm: float = 0.1, correction: float = 0.2) -> float:
    """Maximum-curvature completeness: modal bin of the non-cumulative FMD."""
    m = _binned(mags, dm)
    vals, counts = np.unique(m, return_counts=True)
    if vals.size == 0:
        return np.nan
    return float(vals[np.argmax(counts)] + correction)


def mc_goodness_of_fit(mags: np.ndarray, dm: float = 0.1,
                       target: float = 90.0, mc_grid: np.ndarray | None = None) -> dict:
    """Wiemer & Wyss (2000) goodness-of-fit completeness.

    Scans candidate Mc and returns the lowest one whose synthetic
    Gutenberg-Richter model reproduces at least `target` percent of the
    observed cumulative distribution. Falls back to the best available fit
    when the target is never reached.
    """
    m = _binned(mags, dm)
    if mc_grid is None:
        mc_grid = np.arange(np.nanmin(m), np.nanmax(m) - 0.3 + 1e-9, dm)

    rows = []
    for mc in mc_grid:
        sub = m[m >= mc - 1e-9]
        if sub.size < 20:
            continue
        est = b_value_aki(sub, mc, dm)
        b, a = est["b"], est["a"]
        if not np.isfinite(b):
            continue
        bins = np.arange(mc, sub.max() + dm, dm)
        obs = np.array([(sub >= x - 1e-9).sum() for x in bins], float)
        syn = 10 ** (a - b * bins)
        r = 100.0 * (1.0 - np.sum(np.abs(obs - syn)) / np.sum(obs))
        rows.append((float(mc), float(r), float(b), int(sub.size)))

    if not rows:
        return dict(mc=np.nan, R=np.nan, b=np.nan, n=0, reached_target=False)

    arr = np.array(rows)
    ok = arr[arr[:, 1] >= target]
    if ok.size:
        best = ok[0]
        return dict(mc=best[0], R=best[1], b=best[2], n=int(best[3]), reached_target=True)
    best = arr[np.argmax(arr[:, 1])]
    return dict(mc=best[0], R=best[1], b=best[2], n=int(best[3]), reached_target=False)


def bootstrap_mc_b(mags: np.ndarray, dm: float = 0.1, n_boot: int = 1000,
                   method: str = "gft", target: float = 90.0,
                   rng: np.random.Generator | None = None) -> dict:
    """Bootstrap Mc and b jointly, re-estimating Mc inside every resample.

    Propagating the completeness choice is what makes the b-value uncertainty
    honest; holding Mc fixed understates it.
    """
    rng = np.random.default_rng(0) if rng is None else rng
    m = np.asarray(mags, float)
    n = m.size
    mcs, bs = [], []
    for _ in range(n_boot):
        s = rng.choice(m, size=n, replace=True)
        mc = (mc_goodness_of_fit(s, dm, target)["mc"] if method == "gft"
              else mc_maxcurv(s, dm))
        if not np.isfinite(mc):
            continue
        est = b_value_aki(s, mc, dm)
        if np.isfinite(est["b"]):
            mcs.append(mc)
            bs.append(est["b"])
    if not bs:
        return dict(mc_mean=np.nan, mc_std=np.nan, b_mean=np.nan, b_std=np.nan,
                    b_ci=(np.nan, np.nan), n_ok=0)
    bs = np.array(bs)
    mcs = np.array(mcs)
    return dict(
        mc_mean=float(mcs.mean()), mc_std=float(mcs.std(ddof=1)),
        b_mean=float(bs.mean()), b_std=float(bs.std(ddof=1)),
        b_ci=(float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))),
        n_ok=int(bs.size),
    )


def utsu_test(b1: float, n1: int, b2: float, n2: int) -> dict:
    """Utsu (1992) likelihood-ratio test that two b-values differ.

    Returns the probability that the difference arises by chance; small p
    means the two samples are unlikely to share a b-value.
    """
    if not all(np.isfinite([b1, b2])) or n1 < 2 or n2 < 2:
        return dict(dAIC=np.nan, p=np.nan)
    N = n1 + n2
    # Utsu's dAIC formulation for two magnitude samples.
    dAIC = (-2 * N * np.log(N)
            + 2 * n1 * np.log(n1 + n2 * b1 / b2)
            + 2 * n2 * np.log(n1 * b2 / b1 + n2)
            - 2)
    p = float(np.exp(-dAIC / 2 - 2))
    return dict(dAIC=float(dAIC), p=min(p, 1.0))


def benjamini_hochberg(pvals: np.ndarray, alpha: float = 0.05) -> dict:
    """Benjamini-Hochberg FDR control for the many pairwise b-value tests."""
    p = np.asarray(pvals, float)
    ok = np.isfinite(p)
    order = np.argsort(np.where(ok, p, np.inf))
    m = int(ok.sum())
    q = np.full(p.shape, np.nan)
    if m == 0:
        return dict(q=q, rejected=np.zeros_like(p, bool), threshold=np.nan)
    ranked = p[order][:m]
    qv = ranked * m / np.arange(1, m + 1)
    qv = np.minimum.accumulate(qv[::-1])[::-1]
    q[order[:m]] = np.minimum(qv, 1.0)
    below = np.where(ranked <= alpha * np.arange(1, m + 1) / m)[0]
    thr = ranked[below[-1]] if below.size else np.nan
    return dict(q=q, rejected=(q <= alpha) & ok, threshold=float(thr) if np.isfinite(thr) else np.nan)


def permutation_extreme_b(mags: np.ndarray, labels: np.ndarray, mc: float,
                          dm: float = 0.1, n_perm: int = 5000,
                          min_n: int = 20,
                          rng: np.random.Generator | None = None) -> dict:
    """Is the most extreme cluster b-value surprising under label exchange?

    Cluster memberships are held fixed and magnitudes are shuffled between
    events, which is the null the review asks for: it removes any real
    magnitude-cluster association while preserving both the magnitude
    distribution and the cluster sizes.
    """
    rng = np.random.default_rng(0) if rng is None else rng
    m = np.asarray(mags, float)
    lab = np.asarray(labels)
    keep = m >= mc - dm / 2 + 1e-9
    m, lab = m[keep], lab[keep]

    uniq = [u for u in np.unique(lab) if (lab == u).sum() >= min_n]
    if len(uniq) < 2:
        return dict(b_min_obs=np.nan, p_min=np.nan, b_range_obs=np.nan,
                    p_range=np.nan, n_perm=0, clusters=uniq)

    def stats_for(labels_):
        bs = [b_value_aki(m[labels_ == u], mc, dm)["b"] for u in uniq]
        bs = np.array(bs, float)
        return np.nanmin(bs), np.nanmax(bs) - np.nanmin(bs)

    b_min_obs, b_rng_obs = stats_for(lab)
    cnt_min = cnt_rng = 0
    for _ in range(n_perm):
        bmin, brng = stats_for(rng.permutation(lab))
        cnt_min += bmin <= b_min_obs
        cnt_rng += brng >= b_rng_obs
    return dict(
        b_min_obs=float(b_min_obs), p_min=(cnt_min + 1) / (n_perm + 1),
        b_range_obs=float(b_rng_obs), p_range=(cnt_rng + 1) / (n_perm + 1),
        n_perm=n_perm, clusters=[int(u) for u in uniq],
    )
