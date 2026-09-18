"""Spatial descriptors that survive anisotropy, plus location-error propagation.

The review shows that the standard deviation of radial distance is not a
compactness measure: a ring of events has SD_R = 0 at any radius. These
descriptors are based on the spatial covariance instead.
"""
from __future__ import annotations

import numpy as np
from scipy.spatial import ConvexHull


def radial_stats(east_km: np.ndarray, north_km: np.ndarray) -> dict:
    """The manuscript's descriptors, retained so the bias can be shown."""
    e, n = np.asarray(east_km, float), np.asarray(north_km, float)
    ce, cn = e.mean(), n.mean()
    r = np.hypot(e - ce, n - cn)
    return dict(centroid_e=float(ce), centroid_n=float(cn),
                R_mean=float(r.mean()),
                SD_R=float(r.std(ddof=1)) if r.size > 1 else np.nan)


def covariance_descriptors(east_km: np.ndarray, north_km: np.ndarray) -> dict:
    """Radius of gyration, principal axes, elongation and hull area.

    R_g is the root-mean-square distance to the centroid and is the honest
    scalar size measure; the eigenvalues of the covariance give the major and
    minor axes and hence the orientation and elongation that a radial statistic
    discards.
    """
    e, n = np.asarray(east_km, float), np.asarray(north_km, float)
    pts = np.column_stack([e, n])
    m = pts.shape[0]
    out = dict(n=m)
    if m < 3:
        return {**out, "R_g": np.nan, "major_km": np.nan, "minor_km": np.nan,
                "elongation": np.nan, "azimuth_deg": np.nan, "hull_area_km2": np.nan}

    c = pts.mean(axis=0)
    d = pts - c
    out["R_g"] = float(np.sqrt((d**2).sum(axis=1).mean()))

    cov = np.cov(d, rowvar=False)
    vals, vecs = np.linalg.eigh(cov)
    order = np.argsort(vals)[::-1]
    vals, vecs = vals[order], vecs[:, order]
    major, minor = np.sqrt(np.maximum(vals, 0))
    out["major_km"] = float(major)
    out["minor_km"] = float(minor)
    out["elongation"] = float(major / minor) if minor > 0 else np.inf
    # Azimuth of the major axis, degrees clockwise from north.
    out["azimuth_deg"] = float(np.degrees(np.arctan2(vecs[0, 0], vecs[1, 0])) % 180.0)

    try:
        out["hull_area_km2"] = float(ConvexHull(pts).volume)
    except Exception:
        out["hull_area_km2"] = np.nan
    return out


def rg_from_radial(R_mean: float, SD_R: float, n: int) -> float:
    """Radius of gyration recovered from published mean radius and SD_R.

    Lets the original Table 1 be re-expressed in a valid size measure without
    access to the individual events.
    """
    if n is None or n < 2:
        return np.nan
    return float(np.sqrt(R_mean**2 + (n - 1) / n * SD_R**2))


def location_error_floor(lat_rounding_deg: float = 0.01,
                         depth_rounding_km: float = 1.0,
                         lat_deg: float = -8.4) -> dict:
    """Resolution floor implied by catalogue rounding alone.

    Quantisation to 0.01 deg contributes a uniform error of width w with
    standard deviation w/sqrt(12) on each horizontal axis; the reported
    hypocentre cannot resolve differences below this, before any true
    location uncertainty is considered.
    """
    km_per_deg_lat = 110.574
    km_per_deg_lon = 111.320 * np.cos(np.radians(lat_deg))
    w_ns = lat_rounding_deg * km_per_deg_lat
    w_ew = lat_rounding_deg * km_per_deg_lon
    sd_ns, sd_ew = w_ns / np.sqrt(12), w_ew / np.sqrt(12)
    return dict(
        cell_ns_km=float(w_ns), cell_ew_km=float(w_ew),
        sd_ns_km=float(sd_ns), sd_ew_km=float(sd_ew),
        sd_horizontal_km=float(np.hypot(sd_ns, sd_ew)),
        sd_depth_km=float(depth_rounding_km / np.sqrt(12)),
    )


def bootstrap_descriptor(east_km: np.ndarray, north_km: np.ndarray,
                         key: str = "R_g", n_boot: int = 1000,
                         jitter_km: float = 0.0,
                         seed: int = 0) -> dict:
    """Bootstrap a spatial descriptor, optionally adding location jitter.

    The jitter propagates the hypocentral resolution floor so that differences
    between clusters can be compared against what the catalogue can resolve.
    """
    rng = np.random.default_rng(seed)
    e, n = np.asarray(east_km, float), np.asarray(north_km, float)
    m = e.size
    vals = []
    for _ in range(n_boot):
        idx = rng.integers(0, m, m)
        ee, nn = e[idx], n[idx]
        if jitter_km > 0:
            ee = ee + rng.normal(0, jitter_km, m)
            nn = nn + rng.normal(0, jitter_km, m)
        vals.append(covariance_descriptors(ee, nn)[key])
    v = np.array(vals, float)
    return dict(mean=float(np.nanmean(v)), std=float(np.nanstd(v, ddof=1)),
                ci=(float(np.nanpercentile(v, 2.5)), float(np.nanpercentile(v, 97.5))))
