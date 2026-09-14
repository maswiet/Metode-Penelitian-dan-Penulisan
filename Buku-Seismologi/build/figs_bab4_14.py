"""Gambar untuk Bab 4-14."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, Wedge, Polygon, Ellipse
from gaya import simpan, kotak, panah, bersih, K, G1, G2, G3, FILL


# ---------------------------------------------------------------- Gambar 4.1
def g41():
    fig, ax = plt.subplots(figsize=(4.2, 3.4))
    bersih(ax); ax.set_xlim(-6, 6); ax.set_ylim(-4.5, 4.5)
    S = {"S1": (-4.0, 2.6), "S2": (4.2, 1.9), "S3": (-0.6, -3.6)}
    E = np.array([0.9, 0.9])
    for nm, p in S.items():
        ax.plot(*p, "^", color=K, ms=8)
        ax.text(p[0], p[1] + 0.38, nm, fontsize=7.5, ha="center")
    pairs = [("S1", "S2"), ("S2", "S3"), ("S1", "S3")]
    xs, ys = np.meshgrid(np.linspace(-6, 6, 500), np.linspace(-4.5, 4.5, 400))
    for a, b in pairs:
        A = np.array(S[a]); B = np.array(S[b])
        d = (np.hypot(xs - A[0], ys - A[1]) - np.hypot(xs - B[0], ys - B[1]))
        d0 = np.hypot(*(E - A)) - np.hypot(*(E - B))
        ax.contour(xs, ys, d, levels=[d0], colors=[K], linewidths=1.1)
    ax.plot(*E, "*", color=K, ms=13)
    ax.text(E[0] + 0.35, E[1] + 0.2, "episenter", fontsize=7.5)
    simpan(fig, "gbr-4-1-hiperbola.png")


# ---------------------------------------------------------------- Gambar 4.2
def g42():
    fig, ax = plt.subplots(figsize=(4.2, 3.4))
    bersih(ax); ax.set_xlim(-6, 6); ax.set_ylim(-4.5, 4.5)
    S = [(-3.6, 2.4), (3.8, 1.6), (-0.4, -3.2)]
    E = np.array([0.6, 0.6])
    for i, p in enumerate(S):
        ax.plot(*p, "^", color=K, ms=8)
        ax.text(p[0], p[1] + 0.35, f"S{i+1}", fontsize=7.5, ha="center")
        r = np.hypot(E[0] - p[0], E[1] - p[1]) * 1.13
        ax.add_patch(Circle(p, r, fc="none", ec=K, lw=1.0))
    ax.plot(*E, "*", color=K, ms=11)
    ax.add_patch(Circle(E, 0.75, fc=G3, ec=G1, lw=0.8, alpha=0.8, zorder=0))
    ax.annotate("daerah tumpang tindih\n(waktu kejadian terlalu dini)",
                xy=(E[0] + 0.6, E[1] - 0.5), xytext=(1.9, -3.4), fontsize=6.8,
                arrowprops=dict(arrowstyle="->", lw=0.7, color=G1))
    simpan(fig, "gbr-4-2-lingkaran.png")


# ---------------------------------------------------------------- Gambar 4.3
def g43():
    fig, axes = plt.subplots(1, 2, figsize=(6.2, 2.9))
    ax = axes[0]
    t = np.linspace(0, 6, 900)
    for i, (nm, amp) in enumerate([("Z", 0.7), ("N", -0.55), ("E", 0.85)]):
        sig = np.zeros_like(t)
        m = t > 1.2
        sig[m] = amp * np.exp(-1.1 * (t[m] - 1.2)) * np.sin(
            2 * np.pi * 1.6 * (t[m] - 1.2))
        ax.plot(t, sig - i * 2.0, color=K, lw=0.9)
        ax.text(-0.15, -i * 2.0, nm, fontsize=8, ha="right", va="center")
    ax.axvline(1.2, color=G2, ls=":", lw=0.9)
    ax.text(1.3, 1.35, "gerakan pertama P", fontsize=6.8)
    ax.set_yticks([]); ax.set_xlabel("Waktu (s)")
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.set_title("(a) rekaman tiga komponen", fontsize=8.2)
    ax = axes[1]
    bersih(ax); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    ax.axhline(0, color=G2, lw=0.7); ax.axvline(0, color=G2, lw=0.7)
    ax.text(0, 1.35, "U", fontsize=8, ha="center")
    ax.text(1.35, 0, "T", fontsize=8, va="center")
    ax.text(0, -1.42, "S", fontsize=8, ha="center")
    ax.text(-1.4, 0, "B", fontsize=8, va="center")
    panah(ax, (0, 0), (0.85, 0), lw=1.0, color=G1)
    panah(ax, (0, 0), (0, -0.55), lw=1.0, color=G1)
    panah(ax, (0, 0), (0.85, -0.55), lw=1.6)
    ax.text(0.55, -0.85, "resultan", fontsize=7)
    ax.plot([-1.05, 1.05], [0.68, -0.68], color=K, ls="--", lw=0.9)
    ax.text(-1.35, 0.78, "arah episenter\n(dua kemungkinan)", fontsize=6.3)
    ax.set_title("(b) resultan horizontal", fontsize=8.2)
    simpan(fig, "gbr-4-3-galitzin.png")


# ---------------------------------------------------------------- Gambar 4.4
def g44():
    fig, ax = plt.subplots(figsize=(4.8, 2.7))
    a = np.linspace(0, 360, 500)
    y = 0.55 + 1.2 * np.sin(np.radians(a - 20))
    ax.plot(a, y, color=K, lw=1.4)
    ax.axhline(0, color=G2, lw=0.8)
    ax.axhline(0.55, color=G1, ls="--", lw=0.9)
    rng = np.random.default_rng(3)
    aa = np.sort(rng.uniform(0, 360, 16))
    ax.plot(aa, 0.55 + 1.2 * np.sin(np.radians(aa - 20)) +
            rng.normal(0, 0.12, aa.size), "o", ms=3.4, color=K)
    ax.annotate("", xy=(345, 0.55), xytext=(345, 0.0),
                arrowprops=dict(arrowstyle="<->", lw=0.8, color=G1))
    ax.text(338, 0.28, r"$\Delta O$", fontsize=8, ha="right", color=G1)
    ax.annotate("", xy=(110, 1.75), xytext=(110, 0.55),
                arrowprops=dict(arrowstyle="<->", lw=0.8, color=G1))
    ax.text(115, 1.15, r"$\Delta E$", fontsize=8, color=G1)
    ax.set_xlabel("Azimut $A_{ES}$ (derajat)")
    ax.set_ylabel("$E - E_0$")
    ax.set_xlim(0, 360); ax.set_xticks([0, 90, 180, 270, 360])
    simpan(fig, "gbr-4-4-richter.png")


# ---------------------------------------------------------------- Gambar 4.5
def g45():
    fig, ax = plt.subplots(figsize=(4.4, 3.4))
    mw = np.linspace(2, 9.6, 400)
    ml = np.where(mw < 6.0, mw, 6.0 + 0.6 * (1 - np.exp(-(mw - 6.0))))
    mb = np.where(mw < 5.2, mw, 5.2 + 1.15 * (1 - np.exp(-0.75 * (mw - 5.2))))
    ms = np.where(mw < 7.0, mw + 0.05 * (mw - 5),
                  7.1 + 1.35 * (1 - np.exp(-0.55 * (mw - 7.0))))
    ax.plot(mw, mw, color=K, lw=1.6, label="$M_w$ (momen)")
    ax.plot(mw, ms, color=G1, lw=1.3, ls="--", label="$M_s$")
    ax.plot(mw, mb, color=K, lw=1.1, ls="-.", label="$m_b$")
    ax.plot(mw, ml, color=G1, lw=1.1, ls=":", label="$M_L$")
    ax.set_xlabel("Magnitudo momen $M_w$")
    ax.set_ylabel("Magnitudo terukur")
    ax.set_xlim(2, 9.6); ax.set_ylim(2, 9.6)
    ax.legend(loc="upper left", frameon=False)
    ax.grid(True, lw=0.3, color=G3)
    ax.annotate("penjenuhan", xy=(9.15, 6.28), xytext=(8.45, 4.75),
                fontsize=7.5, color=G1, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.8, color=G1))
    ax.plot(9.1, 9.1, "*", color=K, ms=10)
    ax.text(8.85, 9.05, "Aceh 2004", fontsize=6.4, ha="right", va="top")
    ax.plot(6.3, 6.3, "o", color=K, ms=4.5)
    ax.text(6.05, 6.55, "Yogyakarta 2006", fontsize=6.4, ha="right",
            va="bottom")
    simpan(fig, "gbr-4-5-magnitudo.png")


# ================================================================ Bab 5
def g51():
    fig, axes = plt.subplots(1, 3, figsize=(6.4, 2.4))
    for i, (ax, lab) in enumerate(zip(axes, ["(a)", "(b)", "(c)"])):
        bersih(ax); ax.set_xlim(0, 6); ax.set_ylim(0, 5)
        ax.add_patch(Rectangle((0.4, 0.6), 5.2, 3.8, fc=FILL, ec=K, lw=1.0))
        for y in np.linspace(1.1, 3.9, 6):
            if i == 0:
                ax.plot([0.4, 5.6], [y, y], color=K, lw=0.9)
            elif i == 1:
                xx = np.linspace(0.4, 5.6, 200)
                ax.plot(xx, y + 0.42 * np.tanh((xx - 3.0) * 1.4) *
                        (1 if True else 1) * 0.0 +
                        0.38 * np.tanh((xx - 3.0) * 1.2), color=K, lw=0.9)
            else:
                xx1 = np.linspace(0.4, 3.0, 100)
                xx2 = np.linspace(3.0, 5.6, 100)
                ax.plot(xx1, y - 0.42 + 0.0 * xx1, color=K, lw=0.9)
                ax.plot(xx2, y + 0.42 + 0.0 * xx2, color=K, lw=0.9)
        if i == 2:
            ax.plot([3.0, 3.0], [0.6, 4.4], color=K, lw=1.6)
            ax.text(3.12, 4.55, "sesar", fontsize=6.5)
        panah(ax, (0.15, 4.75), (1.6, 4.75), lw=1.0)
        panah(ax, (5.85, 0.25), (4.4, 0.25), lw=1.0)
        ax.set_title(lab, fontsize=8.5)
    axes[0].text(3.0, 0.15, "keadaan awal", fontsize=6.5, ha="center")
    axes[1].text(3.0, 0.15, "regangan terakumulasi", fontsize=6.5, ha="center")
    axes[2].text(3.0, 0.15, "pelepasan mendadak", fontsize=6.5, ha="center")
    simpan(fig, "gbr-5-1-bingkas.png")


def g52():
    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    bersih(ax); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    for a0 in [0, 180]:
        ax.add_patch(Wedge((0, 0), 1.0, a0 - 45, a0 + 45, fc=G3, ec="none"))
    ax.add_patch(Circle((0, 0), 1.0, fc="none", ec=K, lw=1.4))
    for a in [45, 135]:
        r = np.radians(a)
        ax.plot([-1.02 * np.cos(r), 1.02 * np.cos(r)],
                [-1.02 * np.sin(r), 1.02 * np.sin(r)], color=K, lw=1.2)
    ax.text(0.62, 0.0, "kompresi", fontsize=7, ha="center", va="center")
    ax.text(-0.62, 0.0, "kompresi", fontsize=7, ha="center", va="center")
    ax.text(0.0, 0.62, "dilatasi", fontsize=7, ha="center", va="center")
    ax.text(0.0, -0.62, "dilatasi", fontsize=7, ha="center", va="center")
    ax.text(0.80, 0.86, "bidang\nnodal", fontsize=6.3, ha="center")
    ax.plot(0, 0, "+", color=K, ms=8)
    for a, lab in [(0, "T"), (90, "P")]:
        r = np.radians(a)
        ax.plot(0.42 * np.cos(r), 0.42 * np.sin(r), "o", ms=0)
    simpan(fig, "gbr-5-2-kuadran.png")


def g53():
    fig, ax = plt.subplots(figsize=(4.0, 3.4))
    bersih(ax); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.15, 1.25)
    ax.add_patch(Wedge((0, -0.15), 1.15, 0, 180, fc="white", ec=K, lw=1.3))
    ax.plot([-1.2, 1.2], [-0.15, -0.15], color=K, lw=1.3)
    ax.text(-1.15, 0.95, "permukaan bumi", fontsize=6.8)
    F = (0.0, -0.62)
    ax.add_patch(Circle(F, 0.22, fc="none", ec=K, lw=1.0, ls="--"))
    ax.plot(*F, "*", color=K, ms=9)
    ax.text(0.0, -0.95, "bola fokus", fontsize=6.5, ha="center")
    for ang, pol in [(115, "C"), (75, "D"), (40, "C"), (145, "D")]:
        r = np.radians(ang)
        st = (1.15 * np.cos(r), -0.15 + 1.15 * np.sin(r))
        t = np.linspace(0, 1, 60)
        px = F[0] + (st[0] - F[0]) * t
        py = F[1] + (st[1] - F[1]) * t - 0.16 * np.sin(np.pi * t)
        ax.plot(px, py, color=K, lw=0.8)
        ax.plot(*st, "^", color=K, ms=6)
        u = np.array([st[0] - F[0], st[1] - F[1]])
        u = u / np.linalg.norm(u)
        p0 = (F[0] + 0.22 * u[0], F[1] + 0.22 * u[1])
        ax.plot(*p0, "o" if pol == "C" else "o", ms=3.6,
                mfc=K if pol == "C" else "white", mec=K)
    ax.text(-1.28, -0.62, "polaritas kekal\nsepanjang lintasan", fontsize=6.3,
            va="center")
    ax.plot([], [], "o", mfc=K, mec=K, ms=4, label="kompresi")
    ax.plot([], [], "o", mfc="white", mec=K, ms=4, label="dilatasi")
    ax.legend(loc="upper right", frameon=False, fontsize=6.5)
    simpan(fig, "gbr-5-3-polaritas.png")


def g54():
    fig, axes = plt.subplots(1, 2, figsize=(5.2, 2.5))
    for ax, lab in zip(axes, ["(a) kopel tunggal", "(b) kopel ganda"]):
        bersih(ax); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
        ax.plot([-1.2, 1.2], [0, 0], color=G2, lw=0.6, ls=":")
        ax.plot([0, 0], [-1.2, 1.2], color=G2, lw=0.6, ls=":")
        panah(ax, (-0.85, 0.28), (0.55, 0.28), lw=1.5)
        panah(ax, (0.85, -0.28), (-0.55, -0.28), lw=1.5)
        if "ganda" in lab:
            panah(ax, (0.28, -0.85), (0.28, 0.55), lw=1.5)
            panah(ax, (-0.28, 0.85), (-0.28, -0.55), lw=1.5)
        ax.set_title(lab, fontsize=8.2)
    simpan(fig, "gbr-5-4-kopel.png")


def g55():
    fig, axes = plt.subplots(2, 2, figsize=(5.0, 5.0))
    th = np.linspace(0, 2 * np.pi, 500)
    setting = [(0, 0, "P, kopel tunggal", np.abs(np.sin(th) * np.cos(th))),
               (0, 1, "P, kopel ganda", np.abs(np.sin(2 * th))),
               (1, 0, "S, kopel tunggal", np.abs(np.cos(2 * th))),
               (1, 1, "S, kopel ganda", np.abs(np.cos(2 * th)))]
    for i, j, lab, r in setting:
        ax = axes[i][j]
        bersih(ax); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3)
        ax.plot(r * np.cos(th), r * np.sin(th), color=K, lw=1.2)
        ax.add_patch(Circle((0, 0), 1.05, fc="none", ec=G2, lw=0.6, ls=":"))
        ax.plot(0, 0, "+", color=K, ms=7)
        ax.set_title(lab, fontsize=7.8)
    fig.text(0.5, 0.965, "(a) kopel tunggal                (b) kopel ganda",
             ha="center", fontsize=8)
    simpan(fig, "gbr-5-5-radiasi.png")


def _lingkaran_kecil(sumbu, alfa, n=400):
    """Titik-titik yang membentuk sudut alfa terhadap sumbu (derajat)."""
    a = np.array(sumbu, float); a = a / np.linalg.norm(a)
    tmp = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(tmp, a)) > 0.9:
        tmp = np.array([1.0, 0.0, 0.0])
    u = np.cross(a, tmp); u /= np.linalg.norm(u)
    w = np.cross(a, u)
    al = np.radians(alfa)
    th = np.linspace(0, 2 * np.pi, n)
    return (np.cos(al) * a[None, :]
            + np.sin(al) * (np.cos(th)[:, None] * u[None, :]
                            + np.sin(th)[:, None] * w[None, :]))


def _gambar_kurva(ax, vecs, equal_area, **kw):
    """Gambar kurva pada proyeksi, memutus lompatan antarbelahan."""
    pts = np.array([_proj(v, equal_area) for v in vecs])
    bawah = vecs[:, 2] <= 0
    seg, cur = [], []
    for i in range(len(pts)):
        if bawah[i]:
            cur.append(pts[i])
        else:
            if len(cur) > 1:
                seg.append(np.array(cur))
            cur = []
    if len(cur) > 1:
        seg.append(np.array(cur))
    for sgm in seg:
        ax.plot(sgm[:, 0], sgm[:, 1], **kw)


def _stereonet(ax, equal_area=True, n=9):
    """Jaring stereo setengah bola bawah (meridian + lingkaran kecil)."""
    ax.add_patch(Circle((0, 0), 1.0, fc="white", ec=K, lw=1.3, zorder=0))
    # meridian: bidang berjurus utara-selatan dengan berbagai dip
    for dip in range(10, 180, 10):
        if dip == 90:
            ax.plot([0, 0], [-1, 1], color=G2, lw=0.45)
            continue
        stk, dd = (0, dip) if dip < 90 else (180, 180 - dip)
        p = _bidang(stk, dd, equal_area, npts=300)
        ax.plot(p[:, 0], p[:, 1], color=G2, lw=0.45)
    # lingkaran kecil: kerucut terhadap sumbu horizontal utara-selatan
    for alfa in range(10, 180, 10):
        v = _lingkaran_kecil([0.0, 1.0, 0.0], alfa)
        _gambar_kurva(ax, v, equal_area, color=G2, lw=0.45)
    ax.plot([-1, 1], [0, 0], color=G1, lw=0.6)
    ax.plot([0, 0], [-1, 1], color=G1, lw=0.6)


def _proj(v, equal_area=True):
    """Proyeksi setengah bola bawah; v = (E, N, Up)."""
    e, n, u = v
    if u > 0:
        e, n, u = -e, -n, -u
    pl = np.arcsin(-u)                      # plunge dari horizontal
    r = (np.sqrt(2) * np.sin((np.pi / 2 - pl) / 2) if equal_area
         else np.tan((np.pi / 2 - pl) / 2))
    r = r / 1.0
    az = np.arctan2(e, n)
    return np.array([r * np.sin(az), r * np.cos(az)])


def g56():
    fig, axes = plt.subplots(1, 2, figsize=(5.4, 2.9))
    for ax, ea, lab in [(axes[0], False, "(a) sama sudut (Wulff)"),
                        (axes[1], True, "(b) sama luas (Schmidt)")]:
        bersih(ax); ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.2, 1.2)
        _stereonet(ax, equal_area=ea)
        ax.text(0, 1.06, "N", fontsize=7.5, ha="center")
        ax.set_title(lab, fontsize=8)
    simpan(fig, "gbr-5-6-stereonet.png")


def _vec(trend, plunge):
    t = np.radians(trend); p = np.radians(plunge)
    return np.array([np.cos(p) * np.sin(t), np.cos(p) * np.cos(t), -np.sin(p)])


def g57():
    fig, axes = plt.subplots(1, 2, figsize=(5.6, 2.9))
    ax = axes[0]
    bersih(ax); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.4, 1.4)
    ax.add_patch(Ellipse((0, 0), 2.0, 0.7, fc="none", ec=K, lw=1.1))
    ax.add_patch(Wedge((0, 0), 1.0, 180, 360, fc="#f7f7f7", ec=K, lw=1.1))
    ax.plot(0, 0, "o", color=K, ms=3)
    v = _vec(150, 30)
    ax.plot([0, v[0]], [0, v[1] * 0.35 + v[2] * 0.75], color=K, lw=1.6)
    ax.text(0.32, -0.62, "OP", fontsize=8)
    ax.text(-1.35, 0.9, "setengah bola bawah", fontsize=6.4)
    ax.set_title("kiri: orientasi garis dalam ruang", fontsize=7.6)
    ax = axes[1]
    bersih(ax); ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.25, 1.25)
    _stereonet(ax, equal_area=True)
    p = _proj(_vec(150, 30))
    ax.plot(*p, "o", color=K, ms=5)
    ax.plot([0, p[0]], [0, p[1]], color=K, lw=0.9, ls="--")
    ax.text(p[0] + 0.06, p[1] - 0.02, "P", fontsize=8)
    ax.text(0, 1.06, "N", fontsize=7.5, ha="center")
    ax.text(-1.15, -1.12, "trend $=150°$\nplunge $=30°$", fontsize=6.8)
    ax.set_title("kanan: titik pada proyeksi", fontsize=7.6)
    simpan(fig, "gbr-5-7-garis.png")


def _bidang(strike, dip, equal_area=True, npts=200):
    pts = []
    for rake in np.linspace(0, np.pi, npts):
        s = np.radians(strike); d = np.radians(dip)
        # vektor pada bidang
        u = np.array([np.sin(s), np.cos(s), 0.0])
        w = np.array([np.cos(s) * np.cos(d), -np.sin(s) * np.cos(d),
                      -np.sin(d)])
        v = np.cos(rake) * u + np.sin(rake) * w
        pts.append(_proj(v, equal_area))
    return np.array(pts)


def g58():
    fig, axes = plt.subplots(1, 2, figsize=(5.6, 2.9))
    ax = axes[0]
    bersih(ax); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.4, 1.4)
    ax.add_patch(Ellipse((0, 0), 2.0, 0.7, fc="none", ec=K, lw=1.1))
    ax.add_patch(Wedge((0, 0), 1.0, 180, 360, fc="#f7f7f7", ec=K, lw=1.1))
    ax.add_patch(Polygon([[-0.85, 0.18], [0.75, -0.15], [0.45, -0.85],
                          [-1.0, -0.4]], fc=G3, ec=K, lw=1.0, alpha=0.85))
    ax.text(-0.5, -0.35, "bidang OAB", fontsize=7)
    ax.set_title("kiri: orientasi bidang dalam ruang", fontsize=7.6)
    ax = axes[1]
    bersih(ax); ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.25, 1.25)
    _stereonet(ax, equal_area=True)
    p = _bidang(30, 40)
    ax.plot(p[:, 0], p[:, 1], color=K, lw=1.6)
    ax.text(0, 1.06, "N", fontsize=7.5, ha="center")
    ax.text(-1.15, -1.12, "strike $=30°$\ndip $=40°$", fontsize=6.8)
    ax.set_title("kanan: garis meridian pada proyeksi", fontsize=7.6)
    simpan(fig, "gbr-5-8-bidang.png")


def g59():
    fig, ax = plt.subplots(figsize=(4.2, 3.6))
    bersih(ax); ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.25, 1.3)
    ax.add_patch(Circle((0, 0), 1.15, fc="white", ec=K, lw=1.4))
    ax.plot(0, 0, "+", color=K, ms=6)
    F = (0.0, 0.72)
    ax.add_patch(Circle(F, 0.30, fc="none", ec=K, lw=1.0, ls="--"))
    ax.plot(*F, "*", color=K, ms=9)
    ax.text(0.05, 1.0, "hiposenter", fontsize=6.5)
    ax.text(-0.42, 0.55, "bola fokus", fontsize=6.2)
    for ang in [30, 55, 100]:
        r = np.radians(ang)
        st = (1.15 * np.sin(r), 1.15 * np.cos(r))
        t = np.linspace(0, 1, 80)
        px = F[0] + (st[0] - F[0]) * t
        py = F[1] + (st[1] - F[1]) * t - 0.14 * np.sin(np.pi * t)
        ax.plot(px, py, color=K, lw=0.9)
        ax.plot(*st, "^", color=K, ms=6)
    ax.plot([F[0], F[0]], [F[1], F[1] - 0.55], color=G2, lw=0.8, ls=":")
    ax.add_patch(Arc(F, 0.5, 0.5, theta1=250, theta2=305, color=G1, lw=0.8))
    ax.text(0.13, 0.44, "$i_h$", fontsize=8)
    ang = np.radians(55)
    st = np.array([1.15 * np.sin(ang), 1.15 * np.cos(ang)])
    nrm = st / np.linalg.norm(st)
    ax.plot([st[0], st[0] + 0.28 * nrm[0]], [st[1], st[1] + 0.28 * nrm[1]],
            color=G2, lw=0.8, ls=":")
    ax.text(st[0] + 0.12, st[1] + 0.22, "$i_0$", fontsize=8)
    ax.text(0, -0.55, "bumi", fontsize=7, ha="center", color=G1)
    simpan(fig, "gbr-5-9-bolafokus.png")


# ------------------------------------------- Gambar 5.10: FPS dari Tabel 5.1
TAB51 = [
    ("DAV", 350, "D", 71.36), ("CGP", 345, "D", 71.06), ("BKB", 252, "C", 70.05),
    ("JAY", 107, "C", 65.43), ("KHKI", 227, "C", 65.24), ("BAG", 338, "D", 63.61),
    ("TZZ", 116, "C", 61.84), ("SZP", 339, "D", 60.53), ("TRT", 236, "C", 60.34),
    ("MYK", 357, "D", 43.27), ("WB3", 161, "C", 43.13), ("QIZ", 317, "D", 41.86),
    ("MBL", 196, "C", 41.69), ("NAH", 3, "D", 40.91), ("MVI", 10, "C", 40.89),
    ("KMI", 1, "D", 40.76), ("NGO", 3, "D", 40.51), ("ISO", 151, "D", 39.28),
    ("SNG", 282, "D", 38.85), ("LOE", 304, "D", 38.12), ("CTAO", 139, "C", 38.11),
    ("NST", 299, "D", 38.06), ("NOB", 8, "D", 37.71), ("BDT", 301, "D", 37.70),
    ("CHTO", 304, "D", 34.49), ("SHK", 9, "D", 37.21), ("BAL", 195, "C", 37.06),
    ("OSK", 14, "D", 37.02), ("KLB", 193, "C", 36.87), ("MUN", 195, "C", 36.68),
    ("RMQ", 144, "C", 36.56), ("CD2", 326, "D", 36.31), ("MAJO", 16, "D", 36.27),
    ("STK", 158, "C", 36.20), ("AIK", 15, "C", 35.81), ("ADE", 164, "C", 35.57),
    ("YAM", 18, "D", 35.54), ("BRS", 141, "C", 35.52), ("KHM", 310, "C", 35.29),
    ("SNY", 357, "D", 35.03), ("COO", 145, "D", 34.93), ("VLA", 6, "D", 34.55),
    ("CNB", 152, "C", 34.14), ("TOO", 158, "C", 34.06), ("KKN", 307, "D", 32.58),
    ("KUR", 21, "D", 32.58), ("YSS", 15, "D", 32.57), ("TAU", 160, "D", 32.18),
    ("KOD", 282, "D", 31.79),
]


def _radiasi_p(strike, dip, rake, az, ih):
    """Amplitudo radiasi P kopel ganda (Aki & Richards)."""
    s, d, l = map(np.radians, (strike, dip, rake))
    f = np.radians(az) - s
    i = np.radians(ih)
    return (np.cos(l) * np.sin(d) * np.sin(i)**2 * np.sin(2 * f)
            - np.cos(l) * np.cos(d) * np.sin(2 * i) * np.cos(f)
            + np.sin(l) * np.sin(2 * d) * (np.cos(i)**2
                                           - np.sin(i)**2 * np.sin(f)**2)
            + np.sin(l) * np.cos(2 * d) * np.sin(2 * i) * np.sin(f))


def g510():
    az = np.array([r[1] for r in TAB51], float)
    ih = np.array([r[3] for r in TAB51], float)
    pol = np.array([1 if r[2] == "C" else -1 for r in TAB51])
    best, bestn = None, -1
    for st in range(0, 360, 3):
        for dp in range(10, 91, 4):
            for rk in range(-180, 180, 6):
                a = _radiasi_p(st, dp, rk, az, ih)
                n = np.sum(np.sign(a) == pol)
                if n > bestn:
                    bestn, best = n, (st, dp, rk)
    st, dp, rk = best
    print(f"     FPS terbaik: strike={st} dip={dp} rake={rk} "
          f"cocok {bestn}/{len(pol)}")
    fig, ax = plt.subplots(figsize=(3.9, 4.0))
    bersih(ax); ax.set_xlim(-1.28, 1.28); ax.set_ylim(-1.3, 1.35)
    # kuadran kompresi
    ng = 400
    gx, gy = np.meshgrid(np.linspace(-1, 1, ng), np.linspace(-1, 1, ng))
    rr = np.hypot(gx, gy)
    azg = np.degrees(np.arctan2(gx, gy)) % 360
    ihg = 2 * np.degrees(np.arcsin(np.clip(rr / np.sqrt(2), 0, 1)))
    amp = _radiasi_p(st, dp, rk, azg, ihg)
    amp = np.where(rr <= 1, amp, np.nan)
    ax.contourf(gx, gy, amp, levels=[0, 1e9], colors=[G3])
    ax.contour(gx, gy, amp, levels=[0], colors=[K], linewidths=1.3)
    ax.add_patch(Circle((0, 0), 1.0, fc="none", ec=K, lw=1.5))
    for (nm, a, p, i) in TAB51:
        v = _vec(a, 90 - i)
        q = _proj(v, True)
        ax.plot(q[0], q[1], "o", ms=4.2, mfc=K if p == "C" else "white",
                mec=K, mew=0.8)
    ax.text(0, 1.08, "N", fontsize=8, ha="center")
    ax.plot([], [], "o", mfc=K, mec=K, ms=4.5, label="kompresi")
    ax.plot([], [], "o", mfc="white", mec=K, ms=4.5, label="dilatasi")
    ax.legend(loc="lower left", frameon=False, fontsize=6.5,
              bbox_to_anchor=(-0.14, 0.01))
    ax.text(0.10, -1.28,
            f"bidang nodal terbaik: strike ${st}°$, dip ${dp}°$, rake ${rk}°$",
            fontsize=6.4, ha="center")
    simpan(fig, "gbr-5-10-fps.png")


def g511():
    from obspy.imaging.beachball import beach
    fig, axes = plt.subplots(1, 3, figsize=(6.0, 2.5))
    dat = [((0, 90, 0), "sesar geser murni\n(mengiri)"),
           ((0, 45, 90), "sesar naik murni"),
           ((0, 45, -90), "sesar turun murni")]
    for ax, (mt, lab) in zip(axes, dat):
        bersih(ax); ax.set_xlim(-130, 130); ax.set_ylim(-140, 150)
        b = beach(mt, width=200, facecolor=G1, edgecolor=K, linewidth=1.0,
                  xy=(0, 0))
        ax.add_collection(b)
        ax.text(0, 120, "N", fontsize=7.5, ha="center")
        ax.set_title(lab, fontsize=7.6)
    simpan(fig, "gbr-5-11-jenis-sesar.png")


def _uw(strike, dip):
    s_ = np.radians(strike); d_ = np.radians(dip)
    u = np.array([np.sin(s_), np.cos(s_), 0.0])
    w = np.array([np.cos(s_) * np.cos(d_), -np.sin(s_) * np.cos(d_),
                  -np.sin(d_)])
    return u, w


def _pole(strike, dip):
    u, w = _uw(strike, dip)
    n = np.cross(u, w)
    return n / np.linalg.norm(n)


def _cari_sd(target):
    """Cari (strike, dip) yang polenya searah dengan vektor target."""
    t = target / np.linalg.norm(target)
    terbaik, skor = None, -2
    for st in np.arange(0, 360, 0.5):
        for dp in np.arange(1, 90.1, 0.5):
            c = abs(float(np.dot(_pole(st, dp), t)))
            if c > skor:
                skor, terbaik = c, (st, dp)
    return terbaik


def g512():
    """Bidang nodal, sumbu P dan T, semuanya dihitung secara numerik."""
    st1, dp1 = 30.0, 70.0
    u1, w1 = _uw(st1, dp1)
    n1 = _pole(st1, dp1)
    # arah slip pada bidang 1 (rake diukur dari arah strike)
    rake = -160.0
    d1 = np.cos(np.radians(rake)) * u1 - np.sin(np.radians(rake)) * w1
    d1 = d1 / np.linalg.norm(d1)
    st2, dp2 = _cari_sd(d1)
    P = (n1 - d1); P /= np.linalg.norm(P)
    T = (n1 + d1); T /= np.linalg.norm(T)

    def tp(v):
        v = np.array(v, float)
        if v[2] > 0:
            v = -v
        pl = np.degrees(np.arcsin(-v[2]))
        tr = np.degrees(np.arctan2(v[0], v[1])) % 360
        return tr, pl

    fig, ax = plt.subplots(figsize=(3.9, 4.0))
    bersih(ax); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.32, 1.38)
    _stereonet(ax, equal_area=True)
    for stx, dpx in [(st1, dp1), (st2, dp2)]:
        pcur = _bidang(stx, dpx)
        ax.plot(pcur[:, 0], pcur[:, 1], color=K, lw=1.7)
    for v, lab in [(P, "P"), (T, "T")]:
        tr, pl = tp(v)
        q = _proj(_vec(tr, pl), True)
        ax.plot(*q, "o", ms=7, mfc="white", mec=K, mew=1.3, zorder=5)
        ax.text(q[0] + 0.07, q[1] + 0.05, lab, fontsize=9,
                fontweight="bold", zorder=5)
    ax.text(0, 1.09, "N", fontsize=8, ha="center")
    ax.text(0.02, -1.30,
            f"bidang nodal 1: strike ${st1:.0f}°$, dip ${dp1:.0f}°$, "
            f"rake ${rake:.0f}°$\nbidang nodal 2: strike ${st2:.0f}°$, "
            f"dip ${dp2:.0f}°$", fontsize=6.4, ha="center", va="top")
    q = _proj(_vec(st1, 0), True)
    ax.annotate("strike bidang 1", xy=q, xytext=(0.36, 1.22), fontsize=6.4,
                arrowprops=dict(arrowstyle="->", lw=0.7, color=G1))
    simpan(fig, "gbr-5-12-parameter.png")


def g513():
    fig, axes = plt.subplots(1, 2, figsize=(5.4, 2.9))
    for ax, tipe, lab in [(axes[0], "single", "(a) kopel tunggal"),
                          (axes[1], "double", "(b) kopel ganda")]:
        bersih(ax); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3)
        ax.add_patch(Circle((0, 0), 1.0, fc="none", ec=K, lw=1.3))
        for a in [45, 135]:
            r = np.radians(a)
            ax.plot([-np.cos(r), np.cos(r)], [-np.sin(r), np.sin(r)],
                    color=K, lw=1.0, ls="--")
        for rr in [0.35, 0.65, 0.9]:
            for a in np.arange(0, 360, 30):
                r = np.radians(a)
                x, y = rr * np.cos(r), rr * np.sin(r)
                if tipe == "single":
                    dx, dy = -np.sin(r), np.cos(r)
                else:
                    dx, dy = np.cos(2 * r), -np.sin(2 * r)
                    n = np.hypot(dx, dy)
                    dx, dy = dx / n, dy / n
                ax.plot([x - 0.07 * dx, x + 0.07 * dx],
                        [y - 0.07 * dy, y + 0.07 * dy], color=K, lw=0.9)
        ax.set_title(lab, fontsize=8.2)
    simpan(fig, "gbr-5-13-polarisasi-s.png")


def g514():
    from obspy.imaging.beachball import beach
    fig, ax = plt.subplots(figsize=(6.2, 2.7))
    bersih(ax); ax.set_aspect("auto")
    ax.set_xlim(0, 6); ax.set_ylim(-0.5, 1.5)
    dat = [((329, 8, 110), "Aceh 2004\n$M_w$ 9,1\nnaik"),
           ((48, 89, -178), "Yogyakarta 2006\n$M_w$ 6,3\ngeser"),
           ((290, 12, 96), "Pangandaran 2006\n$M_w$ 7,7\nnaik lambat"),
           ((104, 65, 74), "Lombok 5 Ags 2018\n$M_w$ 6,9\nnaik"),
           ((350, 67, -172), "Palu 2018\n$M_w$ 7,5\ngeser mengiri")]
    for i, (mt, lab) in enumerate(dat):
        x = 0.6 + i * 1.2
        b = beach(mt, width=0.72, facecolor=G1, edgecolor=K, linewidth=0.9,
                  xy=(x, 0.75), axes=ax)
        ax.add_collection(b)
        ax.text(x, -0.02, lab, fontsize=6.2, ha="center", va="top")
    ax.text(3.0, 1.42,
            "Parameter mekanisme bersifat indikatif; gunakan katalog "
            "GCMT/USGS/BMKG untuk kerja kuantitatif.",
            fontsize=5.8, ha="center", color=G1, style="italic")
    simpan(fig, "gbr-5-14-beachball-indonesia.png")


# ================================================================ Bab 6-14
def g61():
    """Sketsa penampang tektonik Jawa Tengah dari palung sampai busur."""
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    bersih(ax); ax.set_aspect("auto")
    ax.set_xlim(0, 640); ax.set_ylim(225, -52)
    putih = dict(fc="white", ec="none", pad=1.0, alpha=0.9)

    # permukaan, laut, dan daratan
    ax.plot([0, 640], [0, 0], color=K, lw=1.2)
    ax.fill_between([0, 250], -12, 0, color="#eef2f5")
    ax.text(110, -20, "Samudra Hindia", fontsize=6.6, ha="center")
    ax.text(570, -20, "Pulau Jawa", fontsize=6.6, ha="center")

    # lempeng menunjam
    sx = np.array([215, 260, 320, 390, 460, 530, 600])
    sy = np.array([6, 25, 60, 105, 150, 190, 218])
    ax.plot(sx, sy, color=K, lw=1.6)
    ax.plot(sx, sy - 28, color=K, lw=1.0)
    ax.fill_between(sx, sy - 28, sy, color=G3, alpha=0.6)
    ax.annotate("lempeng menunjam\n(Indo-Australia)", xy=(345, 92),
                xytext=(120, 118), fontsize=6.6, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.7, color=G1))

    # kegempaan zona Wadati-Benioff
    rng = np.random.default_rng(7)
    for _ in range(85):
        t = rng.uniform(0, 1)
        x = np.interp(t, np.linspace(0, 1, 7), sx)
        y = np.interp(t, np.linspace(0, 1, 7), sy) - rng.uniform(0, 26)
        ax.plot(x + rng.normal(0, 6), y + rng.normal(0, 5), "o", ms=1.6,
                color=G1, alpha=0.75)

    # Moho
    ax.plot([250, 636], [30, 30], color=K, lw=1.0, ls=(0, (4, 2.5)))
    ax.text(632, 24, "Moho $\\approx$ 30 km", fontsize=6.2, ha="right",
            va="bottom", bbox=putih)

    # gunung api dan jalur fluida
    ax.add_patch(Polygon([[452, 0], [470, -28], [488, 0]], fc=G3, ec=K,
                         lw=1.0))
    ax.text(470, -34, "Merapi", fontsize=6.8, ha="center", va="bottom")
    ax.annotate("", xy=(468, -6), xytext=(408, 104),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color=G1,
                                connectionstyle="arc3,rad=0.28",
                                mutation_scale=9))
    ax.text(398, 72, "fluida naik", fontsize=6.4, color=G1, rotation=-62,
            ha="center", va="center", bbox=putih)

    # zona sumber gempa Yogyakarta 2006
    ax.plot(398, 12, "x", color=K, ms=6, mew=1.6)
    ax.annotate("zona sumber\ngempa 2006", xy=(398, 12), xytext=(300, -32),
                fontsize=6.4, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.7, color=G1))

    ax.annotate("palung", xy=(216, 4), xytext=(168, -34), fontsize=6.6,
                ha="center", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.7, color=G1))

    ax.set_ylabel("Kedalaman (km)")
    ax.set_xlabel("Jarak dari palung (km)")
    ax.set_yticks([0, 50, 100, 150, 200])
    ax.set_xticks([0, 200, 400, 600])
    for sp in ("left", "bottom"):
        ax.spines[sp].set_visible(True)
    simpan(fig, "gbr-6-1-meramex.png")



def g73():
    fig, ax = plt.subplots(figsize=(6.2, 2.9))
    bersih(ax); ax.set_aspect("auto")
    ax.set_xlim(0, 700); ax.set_ylim(300, -60)
    ax.plot([0, 700], [0, 0], color=K, lw=1.2)
    ax.fill_between([0, 230], -16, 0, color="#eef2f5")
    sx = np.array([225, 280, 350, 430, 510, 590, 670])
    sy = np.array([5, 30, 75, 130, 190, 250, 298])
    ax.plot(sx, sy, color=K, lw=1.5)
    ax.plot(sx, sy - 30, color=K, lw=1.0)
    ax.fill_between(sx, sy - 30, sy, color=G3, alpha=0.5)
    rng = np.random.default_rng(11)
    for i in range(140):
        t = rng.uniform(0, 1)
        x = np.interp(t, np.linspace(0, 1, 7), sx) + rng.normal(0, 8)
        y = np.interp(t, np.linspace(0, 1, 7), sy) - rng.uniform(0, 28)
        ax.plot(x, y, "o", ms=1.7, color=G1, alpha=0.8)
    ax.add_patch(Ellipse((262, 16), 90, 26, angle=22, fc="none", ec=K,
                         lw=1.2))
    ax.text(258, -22, "1. megathrust", fontsize=6.8, ha="center")
    ax.add_patch(Ellipse((470, 152), 130, 60, angle=36, fc="none", ec=K,
                         lw=1.2, ls="--"))
    ax.text(556, 128, "2. dalam lempeng\nmenunjam", fontsize=6.8)
    ax.add_patch(Ellipse((420, 10), 120, 26, fc="none", ec=K, lw=1.2, ls=":"))
    ax.text(420, -22, "3. sesar dangkal di kerak", fontsize=6.8, ha="center")
    ax.plot([230, 700], [30, 30], color=G2, lw=0.8, ls="--")
    ax.text(690, 24, "Moho", fontsize=6.2, ha="right")
    ax.axhline(300, color=G2, lw=0.5)
    ax.set_ylabel("Kedalaman (km)")
    ax.set_yticks([0, 100, 200, 300])
    ax.set_xticks([])
    for s in ["left"]:
        ax.spines[s].set_visible(True)
    ax.text(660, 292, "berlanjut sampai\n$\\approx$ 660 km", fontsize=6.0,
            ha="right", va="bottom")
    simpan(fig, "gbr-7-3-benioff.png")


def g81():
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    M = np.arange(0.5, 7.6, 0.1)
    a, b = 5.0, 1.0
    N = 10**(a - b * M)
    Mc = 2.5
    det = 1 / (1 + np.exp(-(M - Mc) * 3.2))
    ax.semilogy(M, N, color=G2, lw=1.0, ls="--",
                label="kegempaan sebenarnya")
    ax.semilogy(M, N * det, color=K, lw=1.6, label="katalog teramati")
    ax.axvline(Mc, color=G1, ls=":", lw=1.0)
    ax.text(Mc + 0.1, 2e4, "$M_c$", fontsize=9)
    ax.annotate("kemiringan $= -b$", xy=(4.6, 10**(a - 4.6)),
                xytext=(5.2, 2500), fontsize=7,
                arrowprops=dict(arrowstyle="->", lw=0.7, color=G1))
    ax.set_xlabel("Magnitudo $M$")
    ax.set_ylabel("$N(\\geq M)$ kumulatif")
    ax.legend(frameon=False, loc="upper right", fontsize=7)
    ax.grid(True, lw=0.3, color=G3, which="both")
    simpan(fig, "gbr-8-1-gutenberg-richter.png")


def g82():
    fig, ax = plt.subplots(figsize=(4.4, 3.0))
    t = np.logspace(-2, 2.3, 300)
    for p, ls in [(0.9, ":"), (1.1, "-"), (1.4, "--")]:
        n = 500 / (t + 0.05)**p
        ax.loglog(t, n, color=K, ls=ls, lw=1.3, label=f"$p={p}$")
    ax.set_xlabel("Waktu sejak gempa utama (hari)")
    ax.set_ylabel("Laju gempa susulan (per hari)")
    ax.legend(frameon=False, fontsize=7.5)
    ax.grid(True, lw=0.3, color=G3, which="both")
    simpan(fig, "gbr-8-2-omori.png")


def g91():
    fig, ax = plt.subplots(figsize=(4.6, 3.1))
    T = np.logspace(-2, 0.8, 400)
    keras = 0.35 * np.exp(-((np.log10(T) + 0.85) / 0.45)**2) + 0.05
    lunak = 0.85 * np.exp(-((np.log10(T) + 0.05) / 0.35)**2) + 0.07
    ax.semilogx(T, keras, color=K, lw=1.5, label="situs batuan keras")
    ax.semilogx(T, lunak, color=G1, lw=1.5, ls="--",
                label="situs endapan lunak")
    ax.set_xlabel("Perioda $T$ (s)")
    ax.set_ylabel("$S_a$ (g), redaman 5%")
    ax.legend(frameon=False, fontsize=7.5)
    ax.grid(True, lw=0.3, color=G3, which="both")
    for T0, n in [(0.3, "3 lantai"), (1.0, "10 lantai")]:
        ax.axvline(T0, color=G2, ls=":", lw=0.8)
        ax.text(T0 * 1.06, 0.92, n, fontsize=6.4, rotation=90, va="top")
    simpan(fig, "gbr-9-1-hvsr-tmp.png") if False else simpan(
        fig, "gbr-9-1-spektrum-tanggapan.png")


def g92():
    fig = plt.figure(figsize=(6.4, 2.5))
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)
    f = np.logspace(-1, 1.4, 400)
    ax1.semilogx(f, 1.0 + 0.15 * np.sin(6 * np.log10(f)), color=K, lw=1.3)
    ax1.set_ylim(0, 7); ax1.set_title("(a) batuan keras", fontsize=7.8)
    hv = 1.0 + 5.0 * np.exp(-((np.log10(f) - np.log10(1.4)) / 0.16)**2)
    ax2.semilogx(f, hv, color=K, lw=1.3)
    ax2.axvline(1.4, color=G1, ls=":", lw=0.9)
    ax2.text(1.55, 5.4, "$f_0$", fontsize=9)
    ax2.set_ylim(0, 7); ax2.set_title("(b) endapan lunak", fontsize=7.8)
    for ax in (ax1, ax2):
        ax.set_xlabel("Frekuensi (Hz)"); ax.set_ylabel("H/V")
        ax.grid(True, lw=0.3, color=G3, which="both")
    bersih(ax3); ax3.set_xlim(0, 6); ax3.set_ylim(0, 6)
    ax3.add_patch(Rectangle((0.6, 3.2), 4.8, 1.5, fc=FILL, ec=K, lw=1.0))
    ax3.add_patch(Rectangle((0.6, 0.8), 4.8, 2.4, fc=G3, ec=K, lw=1.0))
    ax3.text(3.0, 3.95, "endapan lunak, $v_s$ kecil", fontsize=6.2,
             ha="center")
    ax3.text(3.0, 2.0, "batuan dasar, $v_s$ besar", fontsize=6.2, ha="center")
    ax3.annotate("", xy=(3.0, 4.7), xytext=(3.0, 3.2),
                 arrowprops=dict(arrowstyle="-|>", lw=1.4, color=K,
                                 mutation_scale=10))
    xx = np.linspace(0.8, 5.2, 200)
    ax3.plot(xx, 5.4 + 0.5 * np.sin(4 * xx), color=K, lw=1.0)
    ax3.plot(xx, 1.0 + 0.16 * np.sin(4 * xx), color=K, lw=1.0)
    ax3.text(3.0, 0.35, "$f_0 = v_s/4H$", fontsize=7.5, ha="center")
    ax3.set_title("(c) penguatan", fontsize=7.8)
    fig.tight_layout()
    simpan(fig, "gbr-9-2-hvsr.png")


def g101():
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.8))
    ax = axes[0]
    bersih(ax); ax.set_xlim(0, 10); ax.set_ylim(0, 6.5); ax.set_aspect("auto")
    kotak(ax, 1.5, 5.2, 2.4, 1.0, "Model sumber\n(sesar, megathrust,\nlatar)",
          fs=6.2)
    kotak(ax, 1.5, 2.6, 2.4, 1.0, "Distribusi $M$\n(Gutenberg–Richter)",
          fs=6.2)
    kotak(ax, 5.0, 3.9, 2.2, 1.0, "GMPE\n$+$ sebaran", fs=6.4, fc=FILL)
    kotak(ax, 8.4, 3.9, 2.4, 1.0, "Kurva bahaya\n$\\lambda(Y>y)$", fs=6.4)
    panah(ax, (2.75, 5.0), (3.9, 4.2), lw=0.8)
    panah(ax, (2.75, 2.8), (3.9, 3.6), lw=0.8)
    panah(ax, (6.15, 3.9), (7.2, 3.9), lw=0.8)
    ax.text(5.0, 0.9, "integrasi atas semua $m$, $r$, dan sumber",
            fontsize=6.4, ha="center", color=G1, style="italic")
    ax.set_title("(a) alur PSHA", fontsize=8.2)
    ax = axes[1]
    y = np.logspace(-2, 0.35, 300)
    lam = 0.06 * y**(-2.4) * np.exp(-y * 1.1)
    ax.loglog(y, lam, color=K, lw=1.5)
    for lv, lab in [(1 / 475, "475 tahun\n(10% / 50 th)"),
                    (1 / 2475, "2.475 tahun\n(2% / 50 th)")]:
        ax.axhline(lv, color=G1, ls=":", lw=0.9)
        yy = np.interp(lv, lam[::-1], y[::-1])
        ax.plot(yy, lv, "o", color=K, ms=4)
        ax.text(0.012, lv * 1.25, lab, fontsize=6.2)
    ax.set_xlabel("PGA (g)")
    ax.set_ylabel("Laju tahunan terlampaui")
    ax.grid(True, lw=0.3, color=G3, which="both")
    ax.set_title("(b) kurva bahaya", fontsize=8.2)
    simpan(fig, "gbr-10-1-psha.png")


def g111():
    fig, ax = plt.subplots(figsize=(6.2, 2.8))
    bersih(ax); ax.set_aspect("auto")
    ax.set_xlim(0, 100); ax.set_ylim(-6, 3.6)
    x = np.linspace(0, 100, 800)
    depth = np.where(x < 70, -5.0, -5.0 + 4.9 * ((x - 70) / 30)**2)
    ax.fill_between(x, depth, 0, color="#eef2f5")
    ax.plot(x, depth, color=K, lw=1.2)
    ax.fill_between(x, -6, depth, color=G3)
    amp = 0.28 * (np.clip(-depth, 0.15, 5) / 5.0)**(-0.25)
    lam = np.clip(-depth, 0.15, 5)**0.5
    y = amp * np.sin(2 * np.pi * np.cumsum(1 / (lam * 9)) * (x[1] - x[0]))
    ax.plot(x, y * 1.0, color=K, lw=1.1)
    ax.axhline(0, color=G2, lw=0.6, ls=":")
    ax.annotate("sumber:\npergeseran dasar laut", xy=(6, -4.6),
                xytext=(4, 2.4), fontsize=6.4,
                arrowprops=dict(arrowstyle="->", lw=0.7))
    ax.text(35, 1.6, "laut dalam: cepat ($\\approx$ 700 km/jam),\n"
                     "panjang gelombang besar, tinggi kecil", fontsize=6.4)
    ax.text(84, 1.9, "pantai:\nlambat, tinggi", fontsize=6.4, ha="center")
    ax.text(50, -5.5, "$c=\\sqrt{gh}$", fontsize=8, ha="center")
    ax.set_ylabel("Tinggi / kedalaman (tidak berskala)")
    simpan(fig, "gbr-11-1-tsunami.png")


def g112():
    fig, ax = plt.subplots(figsize=(6.4, 2.7))
    bersih(ax); ax.set_aspect("auto")
    ax.set_xlim(0, 40); ax.set_ylim(0, 5.4)

    def waktu_x(t):
        return 1.0 + t * 1.06

    ax.plot([0.5, 39.2], [1.0, 1.0], color=K, lw=1.2)
    for t, lab in [(0, "0"), (2, "2 mnt"), (5, "5 mnt"), (20, "20 mnt"),
                   (35, "35 mnt")]:
        x = waktu_x(t)
        ax.plot([x, x], [0.82, 1.18], color=K, lw=1.0)
        ax.text(x, 0.62, lab, fontsize=6.2, ha="center", va="top")
    ax.text(20, 0.12, "waktu sejak gempa", fontsize=6.6, ha="center",
            va="bottom", color=G1)

    tahap = [(0.0, "Gempa\nterjadi"), (2.0, "Deteksi &\nparameter otomatis"),
             (5.0, "Keputusan &\nperingatan"),
             (16.0, "Penyebaran,\nsirene, media"),
             (26.5, "EVAKUASI\nMANDIRI"), (35.0, "Tsunami\ntiba")]
    # kotak disusun merata agar tidak bertumpuk, lalu ditarik ke titik waktunya
    w = 5.9
    pusat = [3.3 + i * 6.6 for i in range(len(tahap))]
    for (t, lab), cx in zip(tahap, pusat):
        penting = "EVAKUASI" in lab
        kotak(ax, cx, 3.55, w, 1.45, lab, fs=6.2,
              fc=G3 if penting else "white", lw=1.4 if penting else 0.9)
        tx = waktu_x(t)
        ax.plot([cx, cx, tx, tx], [2.83, 2.15, 2.15, 1.24],
                color=G1, lw=0.7, solid_joinstyle="miter")
        ax.plot(tx, 1.24, "v", color=G1, ms=3)
    ax.text(20, 5.05, "Mata rantai terlemah bukan teknologi, "
                      "melainkan tanggapan masyarakat",
            fontsize=6.6, ha="center", va="center", style="italic", color=G1)
    simpan(fig, "gbr-11-2-inatews.png")


def g121():
    fig, axes = plt.subplots(3, 2, figsize=(6.2, 3.9),
                             gridspec_kw={"width_ratios": [2.2, 1]},
                             constrained_layout=True)
    t = np.linspace(0, 20, 4000)
    rng = np.random.default_rng(5)
    sinyal = {}
    e = np.zeros_like(t); m = t > 3
    e[m] = np.exp(-1.3 * (t[m] - 3))
    sinyal["VT"] = e * np.sin(2 * np.pi * 8 * t) * (1 + 0.3 * rng.normal(
        0, 1, t.size) * 0.1)
    e2 = np.zeros_like(t)
    e2[m] = (1 - np.exp(-2.5 * (t[m] - 3))) * np.exp(-0.55 * (t[m] - 3))
    sinyal["LP"] = e2 * np.sin(2 * np.pi * 1.4 * t)
    env = np.clip(np.minimum((t - 2) / 3, (18 - t) / 4), 0, 1)
    sinyal["Tremor"] = env * (np.sin(2 * np.pi * 2.4 * t)
                              + 0.4 * np.sin(2 * np.pi * 4.9 * t))
    for i, (nm, s) in enumerate(sinyal.items()):
        ax = axes[i][0]
        ax.plot(t, s + 0.03 * rng.normal(0, 1, t.size), color=K, lw=0.6)
        ax.set_yticks([]); ax.set_ylabel(nm, fontsize=8)
        ax.set_xlim(0, 20); ax.set_xticks([0, 5, 10, 15, 20])
        for sp in ["top", "right", "left"]:
            ax.spines[sp].set_visible(False)
        if i < 2:
            ax.set_xticks([])
        ax = axes[i][1]
        F = np.fft.rfftfreq(t.size, t[1] - t[0])
        A = np.abs(np.fft.rfft(s))
        ax.semilogy(F, A + 1e-3, color=K, lw=0.8)
        ax.set_xlim(0, 15); ax.set_yticks([])
        ax.set_xticks([0, 5, 10, 15])
        for sp in ["top", "right", "left"]:
            ax.spines[sp].set_visible(False)
        if i < 2:
            ax.set_xticks([])
    axes[2][0].set_xlabel("Waktu (s)")
    axes[2][1].set_xlabel("Frekuensi (Hz)")
    axes[0][0].set_title("seismogram", fontsize=8)
    axes[0][1].set_title("spektrum", fontsize=8)
    simpan(fig, "gbr-12-1-gempa-vulkanik.png")


def g141():
    """Sketsa daerah sumber gempa Yogyakarta 2006."""
    fig, ax = plt.subplots(figsize=(5.0, 3.8))
    ax.set_xlim(110.20, 110.68); ax.set_ylim(-8.10, -7.76)
    ax.set_aspect(1.0)

    putih = dict(fc="white", ec="none", pad=1.2, alpha=0.9)

    # daerah kerusakan terberat
    ax.add_patch(Ellipse((110.40, -7.95), 0.20, 0.30, angle=-42, fc=G3,
                         ec=G2, lw=0.9, alpha=0.5, zorder=0))
    ax.annotate("kerusakan\nterberat", xy=(110.305, -7.895),
                xytext=(110.212, -7.845), fontsize=6.4, ha="left",
                va="center", arrowprops=dict(arrowstyle="->", lw=0.7,
                                             color=G1))

    # jalur Sesar Opak
    ox = np.array([110.30, 110.36, 110.42, 110.47])
    oy = np.array([-8.05, -7.96, -7.87, -7.80])
    ax.plot(ox, oy, color=K, lw=2.2, solid_capstyle="round", zorder=3)
    ax.text(110.318, -7.988, "jalur Sesar Opak", fontsize=6.4, rotation=56,
            ha="center", va="center", bbox=putih, zorder=4)

    # sebaran gempa susulan, bergeser ke timur
    sx = ox + 0.10
    sy = oy - 0.01
    rng = np.random.default_rng(21)
    for _ in range(200):
        t = rng.uniform(0, 1)
        x = np.interp(t, np.linspace(0, 1, 4), sx) + rng.normal(0, 0.016)
        y = np.interp(t, np.linspace(0, 1, 4), sy) + rng.normal(0, 0.016)
        ax.plot(x, y, "o", ms=1.9, color=G1, alpha=0.55, zorder=1)
    ax.plot(sx, sy, color=K, lw=1.2, ls=(0, (4, 2.4)), zorder=3)
    ax.annotate("pusat sebaran\ngempa susulan", xy=(110.535, -7.945),
                xytext=(110.60, -8.035), fontsize=6.4, ha="center",
                va="center", zorder=4,
                arrowprops=dict(arrowstyle="->", lw=0.7, color=G1))

    # jarak antara jalur Opak dan pusat gempa susulan
    yd = -7.905
    x1 = np.interp(yd, oy, ox)
    x2 = np.interp(yd, sy, sx)
    ax.annotate("", xy=(x2, yd), xytext=(x1, yd),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.9, color=K,
                                mutation_scale=7), zorder=4)
    ax.text((x1 + x2) / 2, yd + 0.006, "$\\approx$ 10–20 km", fontsize=6.5,
            ha="center", va="bottom", bbox=putih, zorder=5)

    # episenter instrumental
    ax.plot(110.458, -7.962, "*", color=K, ms=13, mfc="white", mew=1.2,
            zorder=5)
    ax.text(110.470, -7.974, "episenter USGS", fontsize=6.4, ha="left",
            va="top", bbox=putih, zorder=5)

    # kota
    for x, y, nm, ms in [(110.37, -7.80, "Kota Yogyakarta", 5.0),
                         (110.33, -7.89, "Bantul", 3.6)]:
        ax.plot(x, y, "s", color=K, ms=ms, zorder=4)
        ax.text(x - 0.010, y, nm, fontsize=6.5, ha="right", va="center",
                bbox=putih, zorder=5)

    ax.set_xlabel("Bujur (°BT)"); ax.set_ylabel("Lintang (°)")
    ax.set_xticks([110.2, 110.3, 110.4, 110.5, 110.6])
    ax.set_yticks([-8.10, -8.00, -7.90, -7.80])
    ax.grid(True, lw=0.3, color=G3)
    ax.set_title("Sketsa daerah sumber gempa Yogyakarta 2006\n"
                 "(skematis, tidak untuk kerja kuantitatif)", fontsize=8)
    simpan(fig, "gbr-14-1-peta-yogya.png")


if __name__ == "__main__":
    print("Bab 4-14:")
    for f in [g41, g42, g43, g44, g45, g51, g52, g53, g54, g55, g56, g57,
              g58, g59, g510, g511, g512, g513, g514, g61, g71, g72, g81,
              g82, g91, g92, g101, g111, g112, g121, g141]:
        f()
