"""Clustering algorithms and the stability diagnostics the review demands.

Contains a faithful replication of the manuscript's winner-take-all procedure,
a genuine topology-preserving Kohonen SOM for comparison, standard baselines,
internal validity indices and resampling-based stability measures.
"""
from __future__ import annotations

import numpy as np
from sklearn.cluster import AgglomerativeClustering, DBSCAN, HDBSCAN, KMeans
from sklearn.metrics import (adjusted_rand_score, calinski_harabasz_score,
                             davies_bouldin_score, silhouette_score)
from sklearn.mixture import GaussianMixture


# --------------------------------------------------------------------------
# The manuscript's algorithm, reproduced exactly as described in its Section 2.3
# --------------------------------------------------------------------------
def radial_init(X: np.ndarray, k: int) -> np.ndarray:
    """Prototypes from k equal-count partitions of the Euclidean norm.

    This is the manuscript's initialisation: it orders events by distance from
    the origin of the normalised space and averages each radial shell.
    """
    r = np.linalg.norm(X, axis=1)
    order = np.argsort(r)
    return np.array([X[part].mean(axis=0) for part in np.array_split(order, k)])


def wta_competitive(X: np.ndarray, k: int = 8, epochs: int = 100,
                    alpha0: float = 0.01, decay: float = 0.5,
                    init: np.ndarray | str = "radial",
                    shuffle: bool = False,
                    rng: np.random.Generator | None = None) -> dict:
    """Online winner-take-all vector quantisation (BMU-only updates).

    No neighbourhood function is applied, so this is not a topology-preserving
    SOM; it is the procedure the manuscript actually ran.
    """
    rng = np.random.default_rng(0) if rng is None else rng
    n = X.shape[0]

    if isinstance(init, str):
        if init == "radial":
            W = radial_init(X, k)
        elif init == "random":
            W = X[rng.choice(n, k, replace=False)].copy()
        elif init == "kmeans++":
            W = KMeans(n_clusters=k, init="k-means++", n_init=1,
                       max_iter=1, random_state=int(rng.integers(1e6))).fit(X).cluster_centers_
        elif init == "pca":
            Xc = X - X.mean(0)
            _, _, Vt = np.linalg.svd(Xc, full_matrices=False)
            t = np.linspace(-1, 1, k)[:, None]
            W = X.mean(0) + t * (Xc @ Vt[0])[:, None].std() * Vt[0]
        else:
            raise ValueError(f"unknown init {init!r}")
    else:
        W = np.array(init, float).copy()

    W = W.copy()
    alpha = alpha0
    order = np.arange(n)
    history = []
    for _ in range(epochs):
        if shuffle:
            order = rng.permutation(n)
        for i in order:
            d = ((X[i] - W) ** 2).sum(axis=1)
            c = int(np.argmin(d))
            W[c] += alpha * (X[i] - W[c])
        history.append(_quantisation_error(X, W))
        alpha *= decay

    labels = assign(X, W)
    return dict(W=W, labels=labels, history=np.array(history),
                alpha_final=alpha, qe=history[-1])


def assign(X: np.ndarray, W: np.ndarray) -> np.ndarray:
    """Nearest-prototype assignment."""
    d = ((X[:, None, :] - W[None, :, :]) ** 2).sum(axis=2)
    return np.argmin(d, axis=1)


def _quantisation_error(X: np.ndarray, W: np.ndarray) -> float:
    d = ((X[:, None, :] - W[None, :, :]) ** 2).sum(axis=2)
    return float(np.sqrt(d.min(axis=1)).mean())


# --------------------------------------------------------------------------
# A genuine Kohonen SOM, for the comparison the review asks for
# --------------------------------------------------------------------------
def kohonen_som(X: np.ndarray, grid: tuple[int, int] = (4, 2), epochs: int = 200,
                alpha0: float = 0.5, sigma0: float | None = None,
                rng: np.random.Generator | None = None) -> dict:
    """Batch-free Kohonen SOM with a Gaussian neighbourhood on a 2-D lattice.

    Both the learning rate and the neighbourhood radius decay exponentially,
    which is what makes the map topology-preserving and lets quantisation and
    topographic error be defined.
    """
    rng = np.random.default_rng(0) if rng is None else rng
    rows, cols = grid
    k = rows * cols
    coords = np.array([(i, j) for i in range(rows) for j in range(cols)], float)
    n, dim = X.shape

    W = X[rng.choice(n, k, replace=False)].copy()
    sigma0 = max(rows, cols) / 2.0 if sigma0 is None else sigma0
    lam = epochs / np.log(max(sigma0, 1.0 + 1e-9)) if sigma0 > 1 else epochs

    history = []
    for e in range(epochs):
        alpha = alpha0 * np.exp(-e / epochs)
        sigma = max(sigma0 * np.exp(-e / lam), 0.5)
        for i in rng.permutation(n):
            d = ((X[i] - W) ** 2).sum(axis=1)
            c = int(np.argmin(d))
            lat = ((coords - coords[c]) ** 2).sum(axis=1)
            h = np.exp(-lat / (2 * sigma**2))
            W += alpha * h[:, None] * (X[i] - W)
        history.append(_quantisation_error(X, W))

    labels = assign(X, W)
    return dict(W=W, labels=labels, coords=coords, grid=grid,
                history=np.array(history),
                qe=_quantisation_error(X, W),
                te=topographic_error(X, W, coords),
                umatrix=u_matrix(W, coords, grid))


def topographic_error(X: np.ndarray, W: np.ndarray, coords: np.ndarray) -> float:
    """Fraction of events whose two best-matching units are not lattice neighbours."""
    d = ((X[:, None, :] - W[None, :, :]) ** 2).sum(axis=2)
    two = np.argsort(d, axis=1)[:, :2]
    sep = np.linalg.norm(coords[two[:, 0]] - coords[two[:, 1]], axis=1)
    return float((sep > 1.5).mean())


def u_matrix(W: np.ndarray, coords: np.ndarray, grid: tuple[int, int]) -> np.ndarray:
    """Mean distance from each unit to its immediate lattice neighbours."""
    rows, cols = grid
    u = np.zeros(len(W))
    for i, c in enumerate(coords):
        nb = np.where((np.abs(coords - c).sum(axis=1) == 1))[0]
        u[i] = np.linalg.norm(W[nb] - W[i], axis=1).mean() if nb.size else np.nan
    return u.reshape(rows, cols)


# --------------------------------------------------------------------------
# Baselines
# --------------------------------------------------------------------------
def baseline_labels(X: np.ndarray, k: int, method: str, seed: int = 0,
                    **kw) -> np.ndarray:
    """Cluster labels from a standard algorithm, for benchmarking."""
    if method == "kmeans":
        return KMeans(n_clusters=k, n_init=10, random_state=seed).fit_predict(X)
    if method == "gmm":
        return GaussianMixture(n_components=k, covariance_type="full",
                               n_init=5, random_state=seed).fit_predict(X)
    if method == "ward":
        return AgglomerativeClustering(n_clusters=k, linkage="ward").fit_predict(X)
    if method == "hdbscan":
        return HDBSCAN(min_cluster_size=kw.get("min_cluster_size", 25), copy=True).fit_predict(X)
    if method == "dbscan":
        return DBSCAN(eps=kw.get("eps", 0.05),
                      min_samples=kw.get("min_samples", 10)).fit_predict(X)
    if method == "wta":
        return wta_competitive(X, k=k, rng=np.random.default_rng(seed))["labels"]
    if method == "som":
        return kohonen_som(X, grid=kw.get("grid", (4, 2)),
                           rng=np.random.default_rng(seed))["labels"]
    raise ValueError(f"unknown method {method!r}")


# --------------------------------------------------------------------------
# Internal validity and stability
# --------------------------------------------------------------------------
def validity_indices(X: np.ndarray, labels: np.ndarray) -> dict:
    """Silhouette, Davies-Bouldin and Calinski-Harabasz for one partition."""
    mask = labels >= 0
    lab, Xs = labels[mask], X[mask]
    if np.unique(lab).size < 2:
        return dict(silhouette=np.nan, davies_bouldin=np.nan, calinski_harabasz=np.nan)
    return dict(
        silhouette=float(silhouette_score(Xs, lab)),
        davies_bouldin=float(davies_bouldin_score(Xs, lab)),
        calinski_harabasz=float(calinski_harabasz_score(Xs, lab)),
    )


def gap_statistic(X: np.ndarray, k: int, n_ref: int = 50, seed: int = 0) -> dict:
    """Tibshirani gap statistic against uniform references in the data hull."""
    rng = np.random.default_rng(seed)

    def wk(data, labels):
        tot = 0.0
        for u in np.unique(labels):
            pts = data[labels == u]
            if len(pts) > 1:
                tot += ((pts - pts.mean(0)) ** 2).sum() / (2 * len(pts))
        return tot

    obs = np.log(wk(X, KMeans(n_clusters=k, n_init=10, random_state=seed).fit_predict(X)) + 1e-12)
    lo, hi = X.min(0), X.max(0)
    refs = []
    for _ in range(n_ref):
        Z = rng.uniform(lo, hi, size=X.shape)
        refs.append(np.log(wk(Z, KMeans(n_clusters=k, n_init=5,
                                        random_state=int(rng.integers(1e6))).fit_predict(Z)) + 1e-12))
    refs = np.array(refs)
    return dict(gap=float(refs.mean() - obs),
                sk=float(refs.std(ddof=1) * np.sqrt(1 + 1 / n_ref)))


def bootstrap_stability(X: np.ndarray, k: int, method: str = "kmeans",
                        n_boot: int = 100, seed: int = 0, **kw) -> dict:
    """Adjusted Rand index between the full-data partition and bootstrap refits.

    Each resample is clustered independently and scored on the events the two
    partitions share, which measures whether the partition is a property of the
    data or of the particular sample.
    """
    rng = np.random.default_rng(seed)
    n = X.shape[0]
    ref = baseline_labels(X, k, method, seed=seed, **kw)
    scores = []
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        uniq = np.unique(idx)
        lab = baseline_labels(X[idx], k, method, seed=int(rng.integers(1e6)), **kw)
        # Map each retained event to the label of its first bootstrap copy.
        first = {}
        for pos, e in enumerate(idx):
            first.setdefault(e, lab[pos])
        boot_lab = np.array([first[e] for e in uniq])
        scores.append(adjusted_rand_score(ref[uniq], boot_lab))
    s = np.array(scores)
    return dict(ari_mean=float(s.mean()), ari_std=float(s.std(ddof=1)),
                ari_min=float(s.min()), ari_max=float(s.max()),
                ari_p05=float(np.percentile(s, 5)), n_boot=n_boot, scores=s)


def order_sensitivity(X: np.ndarray, k: int = 8, n_perm: int = 200,
                      seed: int = 0, **kw) -> dict:
    """ARI between the fixed-order WTA partition and shuffled-order refits.

    The manuscript processes events in catalogue order every epoch; this
    measures how much of the resulting partition is an artefact of that order.
    """
    rng = np.random.default_rng(seed)
    ref = wta_competitive(X, k=k, rng=np.random.default_rng(seed), **kw)["labels"]
    scores = []
    for _ in range(n_perm):
        r = np.random.default_rng(int(rng.integers(1e9)))
        lab = wta_competitive(X, k=k, shuffle=True, rng=r, **kw)["labels"]
        scores.append(adjusted_rand_score(ref, lab))
    s = np.array(scores)
    return dict(ari_mean=float(s.mean()), ari_std=float(s.std(ddof=1)),
                ari_min=float(s.min()), ari_max=float(s.max()), scores=s)


def init_sensitivity(X: np.ndarray, k: int = 8, seed: int = 0,
                     inits=("radial", "random", "kmeans++", "pca"),
                     n_rep: int = 20, **kw) -> dict:
    """ARI of the manuscript's radial-init partition against other initialisations."""
    rng = np.random.default_rng(seed)
    ref = wta_competitive(X, k=k, init="radial",
                          rng=np.random.default_rng(seed), **kw)["labels"]
    out = {}
    for name in inits:
        reps = 1 if name in ("radial", "pca") else n_rep
        sc = []
        for _ in range(reps):
            lab = wta_competitive(X, k=k, init=name,
                                  rng=np.random.default_rng(int(rng.integers(1e9))),
                                  **kw)["labels"]
            sc.append(adjusted_rand_score(ref, lab))
        out[name] = dict(ari_mean=float(np.mean(sc)),
                         ari_std=float(np.std(sc, ddof=1)) if len(sc) > 1 else 0.0,
                         n=len(sc))
    return out
