"""Triggering statistics: nearest-neighbour declustering and Omori-Utsu decay.

Provides the objective background/triggered separation that the review
requires before any population may be called postseismic, and the aftershock
decay fit that replaces qualitative statements about redistribution.
"""
from __future__ import annotations

import numpy as np
from scipy import optimize, stats

KM_PER_DEG = 111.19


def _haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dp = p2 - p1
    dl = np.radians(lon2 - lon1)
    a = np.sin(dp / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    return 2 * r * np.arcsin(np.sqrt(a))


def nearest_neighbour_distances(t_days: np.ndarray, lat: np.ndarray, lon: np.ndarray,
                                mag: np.ndarray, b: float = 1.0, d_f: float = 1.6,
                                mc: float = 0.0) -> dict:
    """Zaliapin & Ben-Zion nearest-neighbour distance in time-space-magnitude.

    For each event j the parent is the earlier event i minimising
    eta = t_ij * r_ij**d_f * 10**(-b * (m_i - mc)), with t_ij in years and
    r_ij in km. The distribution of log10(eta) is bimodal: the background mode
    and the clustered (triggered) mode.
    """
    t = np.asarray(t_days, float) / 365.25
    lat, lon, mag = map(lambda a: np.asarray(a, float), (lat, lon, mag))
    n = t.size

    eta = np.full(n, np.inf)
    parent = np.full(n, -1, int)
    T = np.full(n, np.nan)
    R = np.full(n, np.nan)

    for j in range(1, n):
        dt = t[j] - t[:j]
        valid = dt > 0
        if not valid.any():
            continue
        r = _haversine_km(lat[:j], lon[:j], lat[j], lon[j])
        r = np.maximum(r, 0.5)  # below the catalogue resolution floor
        w = 10.0 ** (-b * (mag[:j] - mc))
        e = np.where(valid, dt * r**d_f * w, np.inf)
        i = int(np.argmin(e))
        eta[j] = e[i]
        parent[j] = i
        T[j] = dt[i] * 10.0 ** (-0.5 * b * (mag[i] - mc))
        R[j] = r[i] ** d_f * 10.0 ** (-0.5 * b * (mag[i] - mc))

    return dict(eta=eta, log_eta=np.log10(np.where(np.isfinite(eta) & (eta > 0), eta, np.nan)),
                parent=parent, T=T, R=R)


def decluster_threshold(log_eta: np.ndarray, n_grid: int = 200) -> dict:
    """Split the log-eta distribution into background and clustered modes.

    Fits a two-component Gaussian mixture by grid search over the threshold
    that minimises within-mode variance (Otsu's criterion), which avoids
    imposing a threshold by eye.
    """
    x = log_eta[np.isfinite(log_eta)]
    if x.size < 20:
        return dict(threshold=np.nan, n_background=0, n_clustered=0)

    grid = np.linspace(np.percentile(x, 2), np.percentile(x, 98), n_grid)
    best, best_thr = np.inf, np.nan
    for thr in grid:
        a, b_ = x[x <= thr], x[x > thr]
        if a.size < 5 or b_.size < 5:
            continue
        within = a.size * a.var() + b_.size * b_.var()
        if within < best:
            best, best_thr = within, thr

    return dict(threshold=float(best_thr),
                n_clustered=int((x <= best_thr).sum()),
                n_background=int((x > best_thr).sum()),
                frac_clustered=float((x <= best_thr).mean()))


def omori_utsu_fit(t_days: np.ndarray, t_end: float,
                   t_start: float = 0.0) -> dict:
    """Maximum-likelihood modified Omori law n(t) = K / (t + c)**p.

    Fitted to aftershock times measured from the mainshock, using the
    point-process likelihood so no binning choice enters the estimate.
    """
    t = np.asarray(t_days, float)
    t = t[(t > t_start) & (t <= t_end)]
    n = t.size
    if n < 20:
        return dict(p=np.nan, c=np.nan, K=np.nan, n=n, loglik=np.nan)

    def _integral(p, c):
        """Integral of (t + c)**-p over the observation span."""
        if abs(p - 1.0) < 1e-8:
            return np.log(t_end + c) - np.log(t_start + c)
        return ((t_end + c) ** (1 - p) - (t_start + c) ** (1 - p)) / (1 - p)

    def nll(theta):
        """Negative log-likelihood with the productivity K profiled out.

        For rate K/(t+c)**p the likelihood is
        n*log(K) - p*sum(log(t_i+c)) - K*I, which is maximised at K = n/I.
        """
        p, c = theta
        if not (0 < p <= 3) or not (1e-6 < c <= 30):
            return 1e12
        integral = _integral(p, c)
        if integral <= 0:
            return 1e12
        return -(n * np.log(n / integral) - p * np.sum(np.log(t + c)) - n)

    best = None
    for p0 in (0.8, 1.0, 1.2):
        for c0 in (0.01, 0.1, 1.0):
            r = optimize.minimize(nll, [p0, c0], method="Nelder-Mead",
                                  options=dict(xatol=1e-6, fatol=1e-6, maxiter=4000))
            if best is None or r.fun < best.fun:
                best = r
    p, c = best.x
    integral = _integral(p, c)
    return dict(p=float(p), c=float(c), K=float(n / integral), n=int(n),
                loglik=float(-best.fun))


def rate_comparison(t_days_pre: np.ndarray, span_pre_days: float,
                    t_days_post: np.ndarray, span_post_days: float) -> dict:
    """Poisson test that two observation spans share one background rate.

    Used to ask whether later seismicity is genuinely elevated above the
    pre-sequence background rather than assuming it is postseismic.
    """
    n1, n2 = int(np.size(t_days_pre)), int(np.size(t_days_post))
    r1 = n1 / span_pre_days
    r2 = n2 / span_post_days
    # Binomial test on the split of n1+n2 events between the two exposures.
    expected_p = span_post_days / (span_pre_days + span_post_days)
    res = stats.binomtest(n2, n1 + n2, expected_p, alternative="greater")
    return dict(rate_pre_per_day=float(r1), rate_post_per_day=float(r2),
                ratio=float(r2 / r1) if r1 > 0 else np.inf,
                n_pre=n1, n_post=n2, p_value=float(res.pvalue))
