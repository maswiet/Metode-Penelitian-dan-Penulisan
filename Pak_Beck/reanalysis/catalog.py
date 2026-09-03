"""Catalogue ingestion, quality control and coordinate handling.

The source file is a semicolon-delimited export with homogenised moment
magnitudes covering 1998-2023 for the eastern Sunda-Banda arc.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from pyproj import Transformer

# Manuscript study window (Sukrisna et al., 18 Aug 2026 version).
MANUSCRIPT_BOX = dict(lon=(115.2, 118.8), lat=(-11.6, -7.1), depth=(0, 350))
MANUSCRIPT_WINDOW = ("2017-07-27", "2019-07-29")

# Lombok-Sumbawa back-arc region used for the sequence analysis.
SEQUENCE_BOX = dict(lon=(115.75, 117.25), lat=(-8.90, -7.90), depth=(0, 60))

# The network densified in late 2009; earlier years are not comparable.
MODERN_ERA_START = "2009-10-01"

# Reported hypocentres are rounded to 0.01 deg and 1 km.
LATLON_ROUNDING_DEG = 0.01
DEPTH_ROUNDING_KM = 1.0

# BMKG-style default depth assigned when depth is not resolved.
DEFAULT_DEPTH_KM = 10.0

_TO_UTM50S = Transformer.from_crs("EPSG:4326", "EPSG:32750", always_xy=True)


def load_raw(path: str) -> pd.DataFrame:
    """Read the raw CSV and normalise column names and dtypes."""
    df = pd.read_csv(path, sep=";")
    df.columns = ["no", "date", "time", "lat", "lon", "depth", "mw"]
    df["time"] = df["time"].str.strip()
    df["date"] = df["date"].str.strip()
    df["dt"] = pd.to_datetime(df["date"] + " " + df["time"], format="%d-%b-%y %H.%M.%S")
    return df.drop(columns=["date", "time"])


def quality_control(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Drop incomplete and duplicated records, and report what was removed."""
    report = {"input": len(df)}

    df = df.dropna(subset=["dt", "lat", "lon", "depth", "mw"])
    report["after_missing"] = len(df)

    # Same origin time to the second and same rounded hypocentre.
    key = ["dt", "lat", "lon", "depth"]
    df = df.sort_values("dt").drop_duplicates(subset=key, keep="first")
    report["after_duplicates"] = len(df)

    report["removed"] = report["input"] - report["after_duplicates"]
    return df.reset_index(drop=True), report


def add_projection(df: pd.DataFrame) -> pd.DataFrame:
    """Add UTM zone 50S easting/northing in kilometres."""
    east, north = _TO_UTM50S.transform(df["lon"].to_numpy(), df["lat"].to_numpy())
    out = df.copy()
    out["east_km"] = east / 1000.0
    out["north_km"] = north / 1000.0
    return out


def subset(df: pd.DataFrame, box: dict, window: tuple[str, str] | None = None,
           mmin: float | None = None) -> pd.DataFrame:
    """Select events inside a lon/lat/depth box, time window and magnitude cut."""
    m = (
        df["lon"].between(*box["lon"])
        & df["lat"].between(*box["lat"])
        & df["depth"].between(*box["depth"])
    )
    if window is not None:
        m &= df["dt"].between(pd.Timestamp(window[0]), pd.Timestamp(window[1]))
    if mmin is not None:
        m &= df["mw"] >= mmin
    return df.loc[m].sort_values("dt").reset_index(drop=True)


def depth_quality(df: pd.DataFrame) -> dict:
    """Quantify how much of the depth column is actually resolved.

    Events reported at exactly the default depth carry no depth information,
    so any statistic computed on the depth axis is biased towards them.
    """
    n = len(df)
    fixed = int((df["depth"] == DEFAULT_DEPTH_KM).sum())
    return {
        "n": n,
        "n_default_depth": fixed,
        "frac_default_depth": fixed / n if n else np.nan,
        "frac_shallower_15km": float((df["depth"] <= 15).mean()) if n else np.nan,
        "n_unique_depths": int(df["depth"].nunique()),
    }


def elapsed_days(df: pd.DataFrame, t0: pd.Timestamp | None = None) -> np.ndarray:
    """Elapsed time in days relative to the first event (or a given origin)."""
    t0 = df["dt"].min() if t0 is None else t0
    return (df["dt"] - t0).dt.total_seconds().to_numpy() / 86400.0
