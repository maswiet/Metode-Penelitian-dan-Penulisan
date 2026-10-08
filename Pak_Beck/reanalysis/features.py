"""Feature construction and the scaling choices that define the metric.

The manuscript's min-max scaling equates the full depth range with the full
time range and gives horizontal position two axes against one each for depth
and time. These helpers make that implicit weighting explicit and testable.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def build_features(df: pd.DataFrame, use_time: bool = True,
                   use_depth: bool = True) -> tuple[np.ndarray, list[str]]:
    """Physical-unit feature matrix in the manuscript's variable order."""
    cols = ["east_km", "north_km"]
    if use_depth:
        cols.append("depth")
    if use_time:
        cols.append("t_days")
    return df[cols].to_numpy(float), cols


def scale(X: np.ndarray, method: str = "minmax",
          weights: np.ndarray | None = None) -> np.ndarray:
    """Rescale features; `weights` multiplies the scaled axes afterwards."""
    X = np.asarray(X, float)
    if method == "minmax":
        lo, hi = X.min(0), X.max(0)
        rng = np.where(hi > lo, hi - lo, 1.0)
        Z = (X - lo) / rng
    elif method == "zscore":
        sd = np.where(X.std(0) > 0, X.std(0), 1.0)
        Z = (X - X.mean(0)) / sd
    elif method == "robust":
        med = np.median(X, axis=0)
        iqr = np.percentile(X, 75, axis=0) - np.percentile(X, 25, axis=0)
        iqr = np.where(iqr > 0, iqr, 1.0)
        Z = (X - med) / iqr
    elif method == "mahalanobis":
        Xc = X - X.mean(0)
        cov = np.cov(Xc, rowvar=False)
        L = np.linalg.cholesky(np.linalg.inv(cov + 1e-12 * np.eye(X.shape[1])))
        Z = Xc @ L
    else:
        raise ValueError(f"unknown scaling {method!r}")
    return Z if weights is None else Z * np.asarray(weights, float)


def metric_exchange_rate(df: pd.DataFrame, cols: list[str]) -> dict:
    """How many days the metric treats as equivalent to one kilometre.

    Under min-max scaling each axis spans one unit, so the implied exchange
    rate is the ratio of the physical ranges. This is the number the review
    asks for and the manuscript never states.
    """
    rng = {c: float(df[c].max() - df[c].min()) for c in cols}
    out = {"ranges": rng}
    if "t_days" in rng and "depth" in rng and rng["depth"] > 0:
        out["days_per_km_depth"] = rng["t_days"] / rng["depth"]
    if "t_days" in rng:
        horiz = max(rng.get("east_km", 0.0), rng.get("north_km", 0.0))
        if horiz > 0:
            out["days_per_km_horizontal"] = rng["t_days"] / horiz
    if "depth" in rng and rng["depth"] > 0:
        out["depth_km_per_10km_horizontal"] = 10.0 * rng["depth"] / max(
            rng.get("east_km", 1.0), rng.get("north_km", 1.0))
    # Horizontal position occupies two of the axes, so in squared Euclidean
    # distance it carries twice the weight of depth or time.
    n_horiz = sum(c in rng for c in ("east_km", "north_km"))
    out["horizontal_axis_count"] = n_horiz
    out["implied_horizontal_weight"] = n_horiz / 1.0
    return out
