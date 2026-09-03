"""Global CMT solutions: parsing, faulting style, and Kagan angles.

The review requires that mechanisms be matched to clusters explicitly, with a
stated criterion and a measure of mechanism heterogeneity, rather than being
cited as generic regional context.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

_HEADER = re.compile(
    r"^\s*\S+\s*(\d{4})\s+(\d{1,2})\s+(\d{1,2})\s+(\d{1,2})\s+(\d{1,2})\s+([\d.]+)\s+"
    r"(-?[\d.]+)\s+(-?[\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(.*)$"
)


def parse_cmtsolution(path: str) -> pd.DataFrame:
    """Read a Global CMT CMTSOLUTION export into a table of centroid solutions."""
    rows, cur = [], None
    for line in open(path, encoding="utf-8", errors="replace"):
        m = _HEADER.match(line.rstrip("\n"))
        if m and "event name" not in line:
            if cur:
                rows.append(cur)
            y, mo, d, h, mi, s = m.group(1, 2, 3, 4, 5, 6)
            cur = dict(
                dt=pd.Timestamp(int(y), int(mo), int(d), int(h), int(mi)) +
                   pd.Timedelta(seconds=float(s)),
                region=m.group(12).strip(),
                mb=float(m.group(10)), ms=float(m.group(11)),
            )
            continue
        if cur is None:
            continue
        key, _, val = line.partition(":")
        key = key.strip().lower()
        val = val.strip()
        if key == "event name":
            cur["event_name"] = val
        elif key == "latitude":
            cur["lat"] = float(val)
        elif key == "longitude":
            cur["lon"] = float(val)
        elif key == "depth":
            cur["depth"] = float(val)
        elif key in ("mrr", "mtt", "mpp", "mrt", "mrp", "mtp"):
            cur[key] = float(val)
    if cur:
        rows.append(cur)

    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["m0_dynecm"] = df.apply(lambda r: _scalar_moment(_tensor(r)), axis=1)
    df["mw"] = (2.0 / 3.0) * (np.log10(df["m0_dynecm"]) - 16.1)
    planes = df.apply(lambda r: pd.Series(nodal_planes(_tensor(r))), axis=1)
    df = pd.concat([df, planes], axis=1)
    df["style"] = df.apply(lambda r: faulting_style(r["rake1"], r["dip1"]), axis=1)
    return df.sort_values("dt").reset_index(drop=True)


def _tensor(r) -> np.ndarray:
    """Moment tensor in the (r, theta, phi) = (up, south, east) CMT convention."""
    return np.array([
        [r["mrr"], r["mrt"], r["mrp"]],
        [r["mrt"], r["mtt"], r["mtp"]],
        [r["mrp"], r["mtp"], r["mpp"]],
    ], float)


def _scalar_moment(M: np.ndarray) -> float:
    return float(np.sqrt((M * M).sum() / 2.0))


def _cmt_to_ned(M: np.ndarray) -> np.ndarray:
    """Convert (r,t,p) = (up, south, east) to (north, east, down)."""
    mrr, mtt, mpp = M[0, 0], M[1, 1], M[2, 2]
    mrt, mrp, mtp = M[0, 1], M[0, 2], M[1, 2]
    return np.array([
        [mtt,  -mtp,  mrt],
        [-mtp,  mpp, -mrp],
        [mrt,  -mrp,  mrr],
    ], float)


def nodal_planes(M_cmt: np.ndarray) -> dict:
    """Strike, dip and rake of both nodal planes from the moment tensor."""
    M = _cmt_to_ned(M_cmt)
    vals, vecs = np.linalg.eigh(M)
    order = np.argsort(vals)
    t_axis = vecs[:, order[2]]   # tension
    p_axis = vecs[:, order[0]]   # pressure

    n1 = (t_axis + p_axis) / np.sqrt(2.0)
    n2 = (t_axis - p_axis) / np.sqrt(2.0)

    sdr1 = _plane_from_normal_slip(n1, n2)
    sdr2 = _plane_from_normal_slip(n2, n1)
    return dict(strike1=sdr1[0], dip1=sdr1[1], rake1=sdr1[2],
                strike2=sdr2[0], dip2=sdr2[1], rake2=sdr2[2],
                plunge_t=_plunge(t_axis), plunge_p=_plunge(p_axis))


def _plunge(v: np.ndarray) -> float:
    v = v / np.linalg.norm(v)
    if v[2] < 0:
        v = -v
    return float(np.degrees(np.arcsin(np.clip(v[2], -1, 1))))


def _plane_from_normal_slip(normal: np.ndarray, slip: np.ndarray) -> tuple:
    """Strike/dip/rake for a plane given its normal and slip vectors in NED."""
    n, s = np.array(normal, float), np.array(slip, float)
    if n[2] > 0:          # enforce an upward normal
        n, s = -n, -s
    n /= np.linalg.norm(n)
    s /= np.linalg.norm(s)

    strike = np.degrees(np.arctan2(-n[0], n[1])) % 360.0
    dip = np.degrees(np.arccos(np.clip(-n[2], -1, 1)))

    sv = np.array([np.cos(np.radians(strike)), np.sin(np.radians(strike)), 0.0])
    dv = np.cross(n, sv)
    rake = np.degrees(np.arctan2(float(s @ dv), float(s @ sv)))
    if rake > 180:
        rake -= 360
    if rake < -180:
        rake += 360
    return float(strike), float(dip), float(rake)


def faulting_style(rake: float, dip: float) -> str:
    """Coarse style classification following the common rake bins."""
    r = float(rake)
    if -30 <= r <= 30 or r >= 150 or r <= -150:
        return "strike-slip"
    if 30 < r < 150:
        return "thrust"
    return "normal"


def _sdr_to_matrix(strike: float, dip: float, rake: float) -> np.ndarray:
    """Rotation-equivalent moment tensor basis for a double couple."""
    s, d, r = map(np.radians, (strike, dip, rake))
    n = np.array([-np.sin(d) * np.sin(s), np.sin(d) * np.cos(s), -np.cos(d)])
    u = np.array([
        np.cos(r) * np.cos(s) + np.cos(d) * np.sin(r) * np.sin(s),
        np.cos(r) * np.sin(s) - np.cos(d) * np.sin(r) * np.cos(s),
        -np.sin(r) * np.sin(d),
    ])
    p = (u - n) / np.linalg.norm(u - n)
    t = (u + n) / np.linalg.norm(u + n)
    b = np.cross(t, p)
    return np.column_stack([t, b, p])


def kagan_angle(sdr1: tuple, sdr2: tuple) -> float:
    """Minimum rotation angle between two double-couple mechanisms, in degrees.

    Zero means identical mechanisms; 120 degrees is the maximum for the
    symmetry group of a double couple, and the expected value for random pairs
    is near 70-80 degrees.
    """
    U1, U2 = _sdr_to_matrix(*sdr1), _sdr_to_matrix(*sdr2)
    R = U2 @ U1.T
    # The four rotations equivalent under double-couple symmetry.
    sym = [np.diag([1, 1, 1.0]), np.diag([1, -1, -1.0]),
           np.diag([-1, 1, -1.0]), np.diag([-1, -1, 1.0])]
    best = 180.0
    for S in sym:
        tr = np.trace(R @ S)
        ang = np.degrees(np.arccos(np.clip((tr - 1) / 2.0, -1, 1)))
        best = min(best, ang)
    return float(best)


def match_to_clusters(fm: pd.DataFrame, cat: pd.DataFrame, labels: np.ndarray,
                      max_dt_s: float = 60.0, max_dist_km: float = 60.0) -> pd.DataFrame:
    """Assign each mechanism to a catalogue event, and hence to a cluster.

    The criterion is explicit: the nearest catalogue event within `max_dt_s` of
    the centroid time and `max_dist_km` of the centroid location. Mechanisms
    with no match are reported as unmatched rather than silently dropped.
    """
    out = []
    clat, clon = cat["lat"].to_numpy(), cat["lon"].to_numpy()
    ctime = cat["dt"].to_numpy()
    for _, r in fm.iterrows():
        dt_s = np.abs((ctime - np.datetime64(r["dt"])) / np.timedelta64(1, "s"))
        dist = _haversine(clat, clon, r["lat"], r["lon"])
        ok = (dt_s <= max_dt_s) & (dist <= max_dist_km)
        if ok.any():
            j = int(np.where(ok)[0][np.argmin(dist[ok])])
            out.append(dict(event_name=r.get("event_name"), matched=True,
                            cat_index=j, cluster=int(labels[j]),
                            dt_s=float(dt_s[j]), dist_km=float(dist[j])))
        else:
            out.append(dict(event_name=r.get("event_name"), matched=False,
                            cat_index=-1, cluster=-1,
                            dt_s=float(dt_s.min()), dist_km=float(dist.min())))
    return pd.DataFrame(out)


def _haversine(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dp, dl = p2 - p1, np.radians(lon2 - lon1)
    a = np.sin(dp / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    return 2 * r * np.arcsin(np.sqrt(a))
