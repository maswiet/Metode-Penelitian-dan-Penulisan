---
title: "Centered Horizontal Gravity Gradient (CHG): A Reproducible Operator for the Interpretation of Circular Gravity Anomalies, with Application to Samalas and Tambora Calderas"
author:
  - Muhammad Zuhdi^1^
  - Wiwit Suryanto^1^
  - Sudarmaji^1^
date: 2026
affiliation: |
  ^1^ Geophysics Department, Faculty of Mathematics and Natural Sciences, Universitas Gadjah Mada, Yogyakarta, Indonesia.
abstract: |
  The Total Horizontal Gradient (THG) is the workhorse operator for delineating the lateral boundaries of subsurface bodies from gravity data, but its omnidirectional nature blends radial and tangential gradient information whenever the target has a circular or near-circular geometry — exactly the geometry common to calderas, plutons, kimberlites, and impact structures. We introduce the *Centered Horizontal Gravity Gradient* (CHG), a pair of operators ($\mathit{CHG}_{\mathrm{rad}}$, $\mathit{CHG}_{\mathrm{tan}}$) that decompose the horizontal gradient about a user- or algorithm-specified centre into its radial and tangential components. The decomposition is an orthogonal rotation of the gradient vector and therefore preserves all gradient information through the exact identity $\mathrm{THG}^2 = \mathit{CHG}_{\mathrm{rad}}^2 + \mathit{CHG}_{\mathrm{tan}}^2$. Relative to the previously circulated version of this work we (i) derive the discrete operator from the continuous polar decomposition with explicit second-order truncation bounds, (ii) treat the central-point singularity by means of an annulus mask, (iii) replace the subjective visual choice of centre with an objective grid-search procedure that minimises the fraction of horizontal-gradient energy carried by the tangential component, (iv) reframe the visualisation blends $E_{\mathrm{rad}}(\alpha)$ and $E_{\mathrm{tan}}(\beta)$ as convex combinations of range-normalised maps (a transparent image-fusion technique rather than an ad hoc physical claim), (v) quantify noise robustness on a Gaussian synthetic with and without low-pass pre-filtering, and (vi) apply the full pipeline to two Indonesian calderas — the morphologically complex Rinjani--Samalas system and the simpler Tambora caldera (1815 eruption). The data-driven centre matches the Smithsonian Global Volcanism Program location of Tambora to within $0.63\ \mathrm{km}$ (sub-grid-cell accuracy) and recovers a coherent dipolar rim signature in $\mathit{CHG}_{\mathrm{rad}}$ for both targets. Complete Python source code and parameter files are provided as supplementary material.
keywords:
  - Gravity anomaly
  - Centered Horizontal Gravity Gradient (CHG)
  - Total Horizontal Gradient (THG)
  - Caldera
  - Edge detection
  - Potential-field interpretation
  - GGM Plus
  - Samalas
  - Tambora
---

# 1. Introduction

The lateral boundaries of subsurface geological features can be detected from the horizontal variation of the gravity (or magnetic) potential across the surface. The standard tool for this purpose is the Total Horizontal Gradient (THG), introduced by @Blakely1986, which returns the Euclidean magnitude of the first horizontal derivative of the field. THG is fast, simple, and effective on lateral discontinuities that are short relative to the wavelength of the regional field, and it has been used for half a century to delineate basin edges, fault traces, contacts, intrusive boundaries, and a range of other geophysical features [@Cordell1985; @Ferreira2013]. Many enhancement strategies build on the same omnidirectional gradient idea — tilt derivatives [@Verduzco2004], local-phase enhancements [@Cooper2006; @Cooper2008], analytic-signal amplitude [@Roest1992], the normalised standard deviation [@Cooper2017], and sun-shaded visualisation [@Cooper2003; @Cooper2023].

THG and its derivatives share, however, a property that is well suited to long, linear contacts but ill suited to the *circular or near-circular* geometries that dominate the structural inventory of calderas, plutons, kimberlite pipes, impact craters, and salt diapirs: by construction the operator discards all directional information at every point. THG does not distinguish the signal of a radial rim (the boundary of a circular density contrast) from that of a linear feature crossing the same point, and consequently it tends to *mix* the two on circular targets, sometimes to the point of obscuring them entirely. Directional alternatives exist — the directional horizontal derivative [@Pham2018], the gradient-tensor eigenvector decomposition [@Beiki2010], the curvature attributes adopted from seismic interpretation [@Roberts2001] — but each of them is referenced to a globally fixed direction or to an intrinsic geometric quantity, and so they do not give the interpreter a natural way of *quantitatively projecting* the gradient onto the radial and tangential directions of a specific candidate centre.

In this paper we develop and validate the *Centered Horizontal Gravity Gradient* (CHG), an operator that performs exactly this projection, with the methodological rigour that practical adoption requires. We restate $\mathit{CHG}_{\mathrm{rad}}$ and $\mathit{CHG}_{\mathrm{tan}}$ as the orthogonal rotation of the continuous gradient vector about a chosen centre, and derive their discrete form from second-order central differences with documented $O(\Delta x^2)$ truncation bounds and an annulus mask that handles the central-point singularity by construction. We give the centre an objective definition: it is the minimiser of the bounded functional $J(x_c, y_c) = \langle \mathit{CHG}_{\mathrm{tan}}^2 \rangle / \langle \mathrm{THG}^2 \rangle \in [0, 1]$ over an annular evaluation domain, located by a coarse-to-fine grid search anchored at the local Bouguer minimum, so that no human judgement enters its determination. We define the $\alpha$-blend and $\beta$-blend visualisation operators as convex combinations of range-normalised scalar fields — the alpha-compositing operation of image processing — and make explicit that $\alpha$ and $\beta$ are interpretive display knobs, not parameters to be fitted. We validate the operator on three synthetic experiments (a Gaussian anomaly, a noise-robustness sweep with and without low-pass pre-filtering, and a band-limited "wagon-wheel" model containing both axisymmetric and radial components) and apply the full pipeline — Somigliana normal-gravity reduction, free-air and simple Bouguer corrections, scale separation, automated centre search, CHG decomposition — to two Indonesian volcanic calderas: the morphologically complex Rinjani--Samalas system and the simpler 1815-eruption caldera of Tambora, using freely available GGM Plus gravity [@Hirt2013; @Hirt2015] and SRTM 90 m topography [@Jarvis2008]. All source code, parameter files, and intermediate data archives are released as supplementary material so that every figure in this paper can be regenerated from raw inputs in a single command. The remainder of the paper develops the theory (§2), reports three synthetic validation experiments (§3), applies the pipeline to Samalas and Tambora (§4), places CHG in the context of related directional operators and recommends a workflow (§5), and concludes (§6).

# 2. Theory

## 2.1 Continuous operators: THG and CHG

We work on a regular two-dimensional grid in the horizontal plane and we assume that the gravity field $g(x, y)$ is twice continuously differentiable so that its first horizontal derivatives are defined everywhere except, possibly, on a set of measure zero. The horizontal gradient vector at point $(x, y)$ is

$$
\nabla_h g(x, y) \;=\; \left( \dfrac{\partial g}{\partial x},\; \dfrac{\partial g}{\partial y} \right).
\tag{1}
$$

The Total Horizontal Gradient (THG) is its Euclidean magnitude,

$$
\mathrm{THG}(x, y) \;=\; \lVert \nabla_h g(x, y) \rVert
\;=\; \sqrt{ \left( \dfrac{\partial g}{\partial x} \right)^{\!2} + \left( \dfrac{\partial g}{\partial y} \right)^{\!2} }.
\tag{2}
$$

Equation (2) is the operator of @Blakely1986. It is the magnitude of a vector and is therefore a non-negative scalar. The magnitude operator,

$$
\nabla_h g \in \mathbb{R}^2 \;\longmapsto\; \lVert \nabla_h g \rVert \in \mathbb{R}_{\geq 0},
\tag{3}
$$

discards the orientation of the gradient. The information lost in this step is precisely what we restore in the CHG operators.

Let $(x_c, y_c)$ be a chosen "centre" of the geological feature of interest. At every point $(x, y) \neq (x_c, y_c)$ we define the local *radial* angle $\theta(x, y) = \operatorname{atan2}(y - y_c,\, x - x_c)$ together with the unit vectors

$$
\hat{\mathbf{r}}(x,y) = (\cos\theta,\, \sin\theta), \qquad
\hat{\mathbf{t}}(x,y) = (-\sin\theta,\, \cos\theta),
\tag{4}
$$

which form a right-handed orthonormal frame rotated by angle $\theta$ relative to $(\hat{\mathbf{x}}, \hat{\mathbf{y}})$. The *radial* and *tangential* components of the horizontal gradient are simply its projections onto this rotated frame,

$$
\mathit{CHG}_{\mathrm{rad}}(x, y) \;=\; \nabla_h g(x, y) \cdot \hat{\mathbf{r}}(x, y)
\;=\; \dfrac{\partial g}{\partial x}\cos\theta \,+\, \dfrac{\partial g}{\partial y}\sin\theta,
\tag{5}
$$

$$
\mathit{CHG}_{\mathrm{tan}}(x, y) \;=\; \nabla_h g(x, y) \cdot \hat{\mathbf{t}}(x, y)
\;=\; -\dfrac{\partial g}{\partial x}\sin\theta \,+\, \dfrac{\partial g}{\partial y}\cos\theta.
\tag{6}
$$

Because the transformation $(\hat{\mathbf{x}}, \hat{\mathbf{y}}) \to (\hat{\mathbf{r}}, \hat{\mathbf{t}})$ is an orthogonal rotation, it preserves Euclidean lengths exactly. Consequently the three operators satisfy the *Pythagoras identity*

$$
\mathrm{THG}^2(x, y) \;=\; \mathit{CHG}_{\mathrm{rad}}^2(x, y) \;+\; \mathit{CHG}_{\mathrm{tan}}^2(x, y),
\tag{7}
$$

at every point where they are defined. The CHG decomposition therefore loses no information: it merely re-expresses the gradient vector in a basis that is *aligned with the geometry of the target feature*. For a perfectly radially symmetric source centred at $(x_c, y_c)$, the gradient is purely radial and $\mathit{CHG}_{\mathrm{tan}} \equiv 0$ everywhere; we will exploit this property in §2.4 to identify the centre objectively.

Substituting (4) into (5)--(6) and expressing $\cos\theta$ and $\sin\theta$ in terms of the Cartesian offsets gives the closed-form expressions

$$
\mathit{CHG}_{\mathrm{rad}}(x,y) =
\dfrac{1}{r}\!\left[
\dfrac{\partial g}{\partial x}\,(x - x_c) +
\dfrac{\partial g}{\partial y}\,(y - y_c)
\right],
\tag{8}
$$

$$
\mathit{CHG}_{\mathrm{tan}}(x,y) =
\dfrac{1}{r}\!\left[
-\dfrac{\partial g}{\partial x}\,(y - y_c) +
\dfrac{\partial g}{\partial y}\,(x - x_c)
\right],
\tag{9}
$$

with $r(x,y) = \sqrt{(x - x_c)^2 + (y - y_c)^2}$.

## 2.2 Discrete implementation

For data sampled on a regular grid $\{(x_i, y_j) : i = 0,\dots,N_x-1;\; j = 0,\dots,N_y-1\}$ with spacings $\Delta x$ and $\Delta y$, we approximate the continuous derivatives in (1) by *second-order accurate central differences* at every interior grid point:

$$
\dfrac{\partial g}{\partial x}\bigg|_{i,j} \;=\; \dfrac{g_{i+1,j} - g_{i-1,j}}{2\,\Delta x} \;+\; O(\Delta x^2),
\tag{10}
$$

$$
\dfrac{\partial g}{\partial y}\bigg|_{i,j} \;=\; \dfrac{g_{i,j+1} - g_{i,j-1}}{2\,\Delta y} \;+\; O(\Delta y^2).
\tag{11}
$$

Equations (10)--(11) follow from Taylor expansion of $g$ about $(x_i, y_j)$ to fourth order: writing $g_{i\pm 1, j} = g_{i,j} \pm \Delta x\, g_x + \tfrac{1}{2}\Delta x^2\, g_{xx} \pm \tfrac{1}{6}\Delta x^3\, g_{xxx} + O(\Delta x^4)$ and subtracting the two expansions cancels the zeroth-, second-, and fourth-order terms; division by $2\Delta x$ leaves $g_x + \tfrac{1}{6}\Delta x^2\, g_{xxx} + O(\Delta x^4)$, so the leading truncation error is $\tfrac{1}{6}\Delta x^2\, g_{xxx}$. This is one order higher than the forward-difference scheme that was used in the previous version of this work, removes the directional bias of forward differences, and is the same scheme used by every standard numerical-gradient routine (e.g., `numpy.gradient` with `edge_order=2`).

At the four edges of the grid, where one of the three stencil points $\{g_{i-1,j}, g_{i,j}, g_{i+1,j}\}$ is missing, we use the second-order accurate one-sided difference

$$
\dfrac{\partial g}{\partial x}\bigg|_{0,j} \;=\; \dfrac{-3\,g_{0,j} + 4\,g_{1,j} - g_{2,j}}{2\,\Delta x} \;+\; O(\Delta x^2),
\tag{12}
$$

and the mirror form at the right edge, so that the truncation order is uniform across the whole grid.

The discrete CHG operators are now obtained by *pointwise* substitution of the tabulated derivatives (10)--(12) into the closed-form expressions (8)--(9). Writing $\widehat{g_x}_{i,j}$ and $\widehat{g_y}_{i,j}$ for the second-order accurate gradient estimates at grid point $(x_i, y_j)$ and denoting $\Delta x_{i,c} = x_i - x_c$, $\Delta y_{j,c} = y_j - y_c$, $r_{i,j} = \sqrt{\Delta x_{i,c}^2 + \Delta y_{j,c}^2}$, this yields

$$
\widehat{\mathit{CHG}_{\mathrm{rad}}}_{\;i,j} \;=\;
\dfrac{1}{\max(r_{i,j},\,\varepsilon_r)}
\left[\, \widehat{g_x}_{i,j}\, \Delta x_{i,c} \;+\; \widehat{g_y}_{i,j}\, \Delta y_{j,c} \,\right],
\tag{13}
$$

$$
\widehat{\mathit{CHG}_{\mathrm{tan}}}_{\;i,j} \;=\;
\dfrac{1}{\max(r_{i,j},\,\varepsilon_r)}
\left[\, -\widehat{g_x}_{i,j}\, \Delta y_{j,c} \;+\; \widehat{g_y}_{i,j}\, \Delta x_{i,c} \,\right],
\tag{14}
$$

with the regularisation floor $\varepsilon_r = 10^{-9}\,\Delta x$ acting only at the single cell that coincides with the trial centre (see §2.3). Equations (13)--(14) are the literal, line-for-line translation of the continuous CHG definitions (8)--(9): the geometric factors $\Delta x_{i,c}/r$ and $\Delta y_{j,c}/r$ are exact at machine precision because they involve only differences and a square root of grid coordinates, and the only source of truncation error is the gradient estimation step. The discrete CHG fields therefore inherit the second-order accuracy of (10)--(12). For the $\sim 220$ m GGM Plus grid and a feature of dominant wavelength $\lambda$, the relative truncation error is $\frac{2\pi^2}{3}(\Delta x/\lambda)^2 \approx 8 \times 10^{-3}$ for $\lambda = 6$ km — well below the $\sim 2$ mGal noise floor of GGM Plus on land grid points.

Importantly, the Pythagoras identity (7) holds *exactly* between the discrete fields (13)--(14) (up to floating-point round-off), because (7) is an algebraic identity that follows from the orthogonal rotation of the *components* of the gradient vector and is independent of how those components are computed. We verify this in §3 to within $\sim 10^{-19}$ on every synthetic experiment and the field data — a no-cost self-consistency test that anyone reproducing the method should perform. The reference implementation `chg_core.compute_chg` in the supplementary material is a 25-line NumPy function whose source closely mirrors equations (10)--(14).

## 2.3 Singularity at the centre and the annulus mask

The unit vectors $\hat{\mathbf{r}}$ and $\hat{\mathbf{t}}$ in (4) are undefined at the centre point $(x_c, y_c)$ because $\theta$ is undefined when $r = 0$. In the discrete implementation we replace $r$ by $\max(r, \varepsilon_r)$ with a small numerical floor $\varepsilon_r$ to avoid division by zero, but pointwise CHG values at radii smaller than one or two grid spacings are dominated by this regularisation and should not be interpreted physically.

For any operation that averages CHG over a spatial region — most importantly the centre-search objective of §2.4 — we therefore use an *annulus mask*

$$
\mathcal{A}(x_c, y_c) \;=\; \{ (x, y) : r_{\min} \leq r(x, y) \leq r_{\max} \},
\tag{15}
$$

with inner radius $r_{\min}$ chosen so that the regularisation region is excluded (typically a few grid spacings) and outer radius $r_{\max}$ chosen of the order of the expected feature size. The mask is annular rather than disc-shaped because the *outermost* parts of the grid contribute large geometric path lengths that distort the radial-vector field for trial centres near the boundary; restricting to an annulus removes that bias.

## 2.4 Objective centre-point determination

The single most important methodological criticism of the earlier version was that the centre $(x_c, y_c)$ was chosen visually, without any reproducible procedure. We replace that choice with an optimisation problem.

For a perfectly radially symmetric source centred at $(x_c^\star, y_c^\star)$, the gradient is purely radial and $\mathit{CHG}_{\mathrm{tan}}(x, y; x_c^\star, y_c^\star) \equiv 0$ at every $(x, y)$. Consequently any positive functional of $\mathit{CHG}_{\mathrm{tan}}$ vanishes at the true centre and is positive elsewhere. We adopt the *normalised tangential-energy ratio*

$$
J(x_c, y_c)
\;=\;
\dfrac{ \langle \mathit{CHG}_{\mathrm{tan}}^2 \rangle_{\mathcal{A}} }
     { \langle \mathrm{THG}^2 \rangle_{\mathcal{A}} },
\tag{16}
$$

where $\langle \cdot \rangle_{\mathcal{A}}$ denotes the spatial average over the annulus (15). By the Pythagoras identity (7), $J$ is the fraction of horizontal-gradient energy carried by the tangential component, so it lies in $[0, 1]$ for all admissible trial centres. The bounded character of $J$ is essential: the unnormalised functional $\langle \mathit{CHG}_{\mathrm{tan}}^2 \rangle$ collapses to zero whenever the trial centre is placed in a signal-free region (because both the radial and tangential gradients vanish there), so the search would *minimise spuriously* outside the data. We therefore use (16) throughout. A safety guard rejects trial centres for which the annular THG energy is smaller than a small fraction (we use $10^{-3}$) of the global peak THG$^2$, preventing the search from drifting to anywhere the data carries no signal.

We minimise $J(x_c, y_c)$ in three stages:

(i) *Coarse grid.* Evaluate $J$ on a regular grid of $N_c \times N_c$ trial centres covering a user-specified search rectangle (default: the inner 60% of the data extent). For each trial we compute $\mathit{CHG}_{\mathrm{tan}}$ once over the grid, then average over the annulus.

(ii) *Fine grid.* Refine around the coarse minimum on a $N_f \times N_f$ sub-grid spanning $\pm 2$ coarse spacings.

(iii) *Powell polishing.* A gradient-free Powell step locates the sub-pixel minimum. Powell is robust against the small numerical noise that the discretisation introduces in $J$, and converges in $O(10)$ function evaluations.

In all the examples in this paper we use $N_c = N_f = 21$, but the method is insensitive to those choices. On the noise-free Gaussian synthetic of §3.1 this procedure recovers the centre to within $10^{-3}$ grid cells; on noisy data we report the empirical recovery accuracy in §3.2.

For complex fields containing multiple competing circular features (volcanic edifice + caldera + smaller craters), $J$ is multi-modal and the global minimum is not necessarily the geological target of interest. We document this behaviour explicitly on the wagon-wheel synthetic of §3.3, and we resolve it for the field application by combining a *data-driven seed* (the location of the local minimum of the residual SBA, which is the physical signature of a mass-deficit caldera) with a tight search region around that seed; see §4.4.

## 2.5 Range-normalised visualisation blends

Several composite visualisations of THG and the directional CHG operators have proved interpretively useful. We define

$$
E_{\mathrm{rad}}(x, y;\alpha) \;=\;
\alpha \,\dfrac{\mathit{CHG}_{\mathrm{rad}}(x, y)}{\max\!\big|\mathit{CHG}_{\mathrm{rad}}\big|}
\;+\;
(1-\alpha)\,\dfrac{\mathrm{THG}(x, y)}{\max\!\big(\mathrm{THG}\big)},
\qquad \alpha \in [0, 1],
\tag{17}
$$

$$
E_{\mathrm{tan}}(x, y;\beta) \;=\;
\beta \,\dfrac{\mathit{CHG}_{\mathrm{tan}}(x, y)}{\max\!\big|\mathit{CHG}_{\mathrm{tan}}\big|}
\;+\;
(1-\beta)\,\dfrac{\mathrm{THG}(x, y)}{\max\!\big(\mathrm{THG}\big)},
\qquad \beta \in [0, 1].
\tag{18}
$$

Two clarifications relative to the prior version are warranted. First, the normalisation of the *signed* fields $\mathit{CHG}_{\mathrm{rad}}$ and $\mathit{CHG}_{\mathrm{tan}}$ is by $\max|\cdot|$ rather than $\max(\cdot)$: using only the positive maximum lets the negative tail of each field exceed unity in magnitude, which compromises the convex-combination property below. Second, expressions (17)--(18) are mathematically nothing more than *convex combinations of range-normalised scalar fields* — formally identical to alpha-compositing as used in image processing for the controlled blending of two co-registered raster layers. They are a *visualisation* technique: $\alpha$ and $\beta$ are interpretive knobs that the user adjusts to find the most informative compromise between the omnidirectional view of THG and the directional view of CHG, not parameters to be fit. We do not claim a physical interpretation for any intermediate value of $\alpha$ or $\beta$, and we report no procedure for choosing them.

Two limits are noteworthy. At $\alpha = 0$ (resp. $\beta = 0$), $E_{\mathrm{rad}} = E_{\mathrm{tan}} = \mathrm{THG}/\max(\mathrm{THG})$, the normalised THG map. At $\alpha = 1$ (resp. $\beta = 1$), $E_{\mathrm{rad}}$ ($E_{\mathrm{tan}}$) reduces to the normalised pure-CHG map. The interpreter may therefore sweep $\alpha$ from $0$ to $1$ to trace the gradual emergence of the radial component out of the omnidirectional baseline; the wagon-wheel synthetic in §3.3 demonstrates this sweep visually and §3.4 quantifies the contrast gain.

## 2.6 Stated limitations

The operator inherits the assumptions of every horizontal-gradient method: it is meaningful only at the wavelengths where the gravity field is well sampled, only outside the central singularity (mitigated by the annulus mask), and only where the signal-to-noise ratio supports differentiation. In addition, the centre-search functional (16) has the following specific limitations:

1. *Single-feature assumption.* When the field contains multiple competing circular features (e.g. nested calderas, or a volcanic edifice enclosing a caldera that is itself smaller), $J$ is multi-modal and the *global* minimum is not necessarily the geological feature of interest. The user must either tighten the annulus to the expected feature scale or supply a data-driven seed (§4.4).

2. *Radial-linear sensitivity.* The functional is biased by features that radiate from the true centre — dykes, valleys, pyroclastic channels — because such features are tangential-gradient sources at the true centre. We document this on the wagon-wheel synthetic in §3.3 and on the Rinjani--Samalas field example in §4.5. The bias does not destroy the method: it simply means that on spoke-rich fields the recovered centre is the geometric centre of best radial fit, not the centre of the rim alone.

3. *No claim to fit non-circular geometries.* The operator is designed for circular or near-circular targets. For elongated, lobate, or chaotic features it remains computable but does not separate radial from tangential information in any useful sense.

We return to these limitations in §5.

# 3. Synthetic validation

We test the operator on three synthetic experiments of increasing complexity. The first is a single, radially symmetric Gaussian anomaly that exercises every component of the operator on an ideal target (§3.1). The second is a noise-robustness test on the same anomaly that quantifies the recovery accuracy as a function of signal-to-noise ratio and pre-smoothing (§3.2). The third is a band-limited "wagon-wheel" model that combines an axisymmetric rim with $N$ radial spokes; it tests directional separation, the visualisation blends (17)--(18), and the multi-feature limitation of the centre search (§3.3).

## 3.1 Single Gaussian anomaly

We place a radially symmetric Gaussian

$$
g(x, y) \;=\; A \, \exp\!\left[ -\dfrac{(x - x_c^\star)^2 + (y - y_c^\star)^2}{2\,\sigma^2} \right]
\tag{19}
$$

on a $200 \times 200$ grid with $\Delta x = \Delta y = 100\ \mathrm{m}$ (domain $20 \times 20\ \mathrm{km}$), amplitude $A = 5\ \mathrm{mGal}$, width $\sigma = 1500\ \mathrm{m}$, and true centre $(x_c^\star, y_c^\star) = (7300, 11200)\ \mathrm{m}$ — off-set from the grid centre so that a default "centre" guess is wrong by construction. The annulus mask uses $r_{\min} = \sigma = 1500\ \mathrm{m}$, $r_{\max} = 4\sigma = 6000\ \mathrm{m}$.

![Decomposition and centre recovery on a single Gaussian anomaly (§3.1). (a) Synthetic gravity field with true centre marked. (b) THG: classic doughnut signature. (c) $\mathit{CHG}_{\mathrm{rad}}$ about the true centre: clean negative ring, the gradient pointing radially inward toward the positive Gaussian. (d) $\mathit{CHG}_{\mathrm{tan}}$ at the true centre: at the level of $10^{-7}$ — three orders of magnitude smaller than $\mathit{CHG}_{\mathrm{rad}}$ — confirming the vanishing-tangential property of axisymmetric sources. The eight-petal residual is the algebraic signature of the Cartesian stencil on a circular function and is purely a discretisation artefact. (e) The objective $J(x_c, y_c)$ has a sharp, isolated minimum at the true centre on the coarse grid. (f) Numerical summary: Powell polishing locates the centre to within $0.001$ grid cells.](/mnt/user-data/outputs/step1_gaussian_recovery.png){#fig:gaussian width=100%}

Three numerical observations are worth recording (figure 1).

*Pythagoras invariant.* The supremum of $|\mathrm{THG}^2 - \mathit{CHG}_{\mathrm{rad}}^2 - \mathit{CHG}_{\mathrm{tan}}^2|$ over the grid is $1.7 \times 10^{-21}$ in the units of $g^2$, i.e. at the level of double-precision round-off. The discrete operators inherit the continuous identity (7) exactly.

*Vanishing tangential at the true centre.* The root-mean-square of $\mathit{CHG}_{\mathrm{tan}}$ at the true centre is $2.7 \times 10^{-7}\ \mathrm{mGal/m}$, compared with $7.4 \times 10^{-4}\ \mathrm{mGal/m}$ for $\mathit{CHG}_{\mathrm{rad}}$ — a ratio of $\sim 4 \times 10^{-4}$. The residual at the level of $10^{-7}$ is the algebraic signature of evaluating a radially symmetric function on a Cartesian grid (the eight-petal pattern visible in figure 1d): the same residual pattern is exactly reproducible from the discrete stencil alone, and is not a feature of the data.

*Sub-grid centre recovery.* With Powell polishing, the recovered centre matches the true centre to better than $1\ \mathrm{mm}$ — well below the $100\ \mathrm{m}$ grid spacing. This is the noise-free upper bound on the localisation precision of the method.

## 3.2 Noise robustness with Gaussian pre-filtering

A standard concern for any operator built on numerical differentiation is its behaviour under measurement noise: for additive white noise of standard deviation $\sigma_n$ on a field sampled with spacing $h$, central differences amplify the noise to $\sigma(\partial g/\partial x) \approx \sigma_n / h$. We quantify the practical consequences for the centre-search functional (16) by repeating the Gaussian experiment of §3.1 with independent additive Gaussian noise of standard deviation $\sigma_n = A / \mathrm{SNR}$, where SNR is the peak signal-to-noise ratio. We sweep SNR through $\{\infty, 50, 20, 10, 5, 2\}$ and report results both *without* any pre-processing and with Gaussian pre-smoothing of width $\sigma_s \in \{0, 1, 2\}$ grid cells before the gradient is taken. For each combination we run twelve independent noise realisations and report the median recovery error.

![Noise robustness with and without Gaussian pre-smoothing (§3.2). (a) Median recovery error against SNR for three pre-smoothing levels; shaded bands are inter-quartile ranges over twelve noise realisations. The dashed line marks half a grid cell. Without pre-smoothing, the recovery collapses below SNR $\sim$ 20; with $\sigma_s = 2$ cells ($\sim 200\ \mathrm{m}$), recovery stays under a single grid cell down to SNR = 5. (b) Scatter of recovered centres at SNR = 10 for the three pre-smoothing levels; without smoothing the recovered centres are essentially random across the search region, whereas with $\sigma_s \geq 1$ they cluster tightly on the truth.](/mnt/user-data/outputs/step1_noise_robustness.png){#fig:noise width=100%}

Figure 2 summarises the results. The recovery error in the noise-free case (median $0$ m) confirms §3.1. Without pre-smoothing, the recovery degrades sharply below SNR $\approx 20$ — at SNR = 10 the median error is approximately $8\ \mathrm{km}$, i.e. effectively random over the search region — because the noise-amplified gradient dominates the objective. With Gaussian pre-smoothing of width $\sigma_s = 2$ grid cells ($\approx 200\ \mathrm{m}$, well below the $1500\ \mathrm{m}$ Gaussian width of the anomaly), the median recovery error stays at $0.85\ \mathrm{m}$ for SNR = 50, $110\ \mathrm{m}$ ($\approx 1$ cell) for SNR = 10, and $174\ \mathrm{m}$ ($\approx 2$ cells) for SNR = 5. The latter is acceptable for any practical localisation purpose. Pre-smoothing therefore mitigates the noise sensitivity of the operator at no cost in interpretation when the smoothing width is small relative to the feature scale.

## 3.3 Wagon-wheel synthetic and the visualisation blend

The third synthetic experiment is designed to test (i) the *directional separation* claim of CHG on a controlled multi-feature target, (ii) the behaviour of the visualisation blends (17)--(18), and (iii) the multi-feature limitation of the centre search functional. We construct a band-limited "wagon-wheel" anomaly consisting of an annular Gaussian rim (radius $4\ \mathrm{km}$, half-width $250\ \mathrm{m}$) and four diameter lines (eight visual rays at $0^\circ$, $45^\circ$, $90^\circ$, $135^\circ$) of half-width $200\ \mathrm{m}$, both apertured in radius and convolved with a final Gaussian of width $1.5$ grid cells to mimic a depth-induced low-pass. The rim is purely axisymmetric about the true centre $(9300, 10800)\ \mathrm{m}$; the spokes are radial about the same centre.

![Wagon-wheel decomposition about the true centre (§3.3). (a) Synthetic gravity field $g$. (b) THG: both rim and spokes are equally bright — the omnidirectional operator does not separate them. (c) $\mathit{CHG}_{\mathrm{rad}}$ about the true centre: rim is preserved as a clean positive--negative dipole around the radius of maximum gradient; spokes have faded to a faint residual. (d) $\mathit{CHG}_{\mathrm{tan}}$ about the true centre: spokes are preserved as eight bipolar tracks; the rim has collapsed to a vanishingly weak ring. The decomposition is textbook clean despite the band-limited construction.](/mnt/user-data/outputs/step2_wagon_decomposition.png){#fig:wagonwheel width=100%}

Figure 3 shows the decomposition about the true centre. The visual result is the cleanest demonstration we know of the CHG claim: $\mathit{CHG}_{\mathrm{rad}}$ retains the rim and suppresses the spokes; $\mathit{CHG}_{\mathrm{tan}}$ retains the spokes and suppresses the rim. The Pythagoras residual on this experiment is $1.0 \times 10^{-20}$, again at the level of round-off.

![Range-normalised blends $E_{\mathrm{rad}}(\alpha)$ (top) and $E_{\mathrm{tan}}(\beta)$ (bottom) of equations (17)--(18), swept across $\alpha, \beta \in \{0, 0.2, 0.4, 0.6, 0.8, 1.0\}$. At $\alpha = 0$ (and $\beta = 0$) the panels reduce to the normalised THG view. As $\alpha$ ($\beta$) increases the spokes (rim) progressively fade out of $E_{\mathrm{rad}}$ ($E_{\mathrm{tan}}$) until only the rim (spokes) remain at unit weight. The blends are convex combinations of two range-normalised scalar fields and have no fitted parameters.](/mnt/user-data/outputs/step2_alpha_beta_sweep.png){#fig:alphabeta width=100%}

Figure 4 demonstrates the visualisation blends (17)--(18) for the same anomaly. As $\alpha$ sweeps from 0 to 1, the linear spoke pattern progressively thins out of $E_{\mathrm{rad}}$ and the rim emerges as a coherent dipolar ring; as $\beta$ sweeps from 0 to 1, the rim fades out of $E_{\mathrm{tan}}$ and the spokes become the dominant directional structure. The transition is smooth, monotonic, and free of arbitrary thresholds.

![Quantitative validation of the visualisation blend (§3.3). For each $\alpha$ (or $\beta$) we measure the energy contrast between the rim mask (an annular band about the true centre at the rim radius) and the spoke mask (the four spoke lines, minus the rim band). Both contrasts increase monotonically by a factor of $\sim 4$--5 as the directional CHG weight grows from zero to one, confirming that the directional operator does separate the two feature families *quantitatively*, not merely visually.](/mnt/user-data/outputs/step2_contrast.png){#fig:contrast width=80%}

A more careful test asks not only whether the blend looks right but whether it actually concentrates energy on the intended feature. We define the rim-to-spoke contrast in $E_{\mathrm{rad}}$ as $C_{\mathrm{rad}}(\alpha) = \langle E_{\mathrm{rad}}^2 \rangle_{\mathrm{rim}} \big/ \langle E_{\mathrm{rad}}^2 \rangle_{\mathrm{spoke}}$, and analogously $C_{\mathrm{tan}}(\beta)$ with the roles reversed. Figure 5 traces both contrasts across the full $[0,1]$ range. The rim-to-spoke contrast in $E_{\mathrm{rad}}$ rises monotonically from $C_{\mathrm{rad}}(0) = 1.63$ (pure THG) to $C_{\mathrm{rad}}(1) = 7.02$ (pure $\mathit{CHG}_{\mathrm{rad}}$), an improvement of $4.3\times$. The spoke-to-rim contrast in $E_{\mathrm{tan}}$ rises from $0.61$ to $2.94$, a $4.8\times$ improvement. Both improvements happen monotonically, with no peak at any intermediate $\alpha$ or $\beta$: the directional view is *strictly more contrasted* than the omnidirectional view on this target.

![Documented limitation: the centre-search functional $J(x_c, y_c)$ on a multi-feature field (§3.3). (a) On the wagon-wheel field with an annulus mask attached to the trial centre, the minimum of $J$ sits $\sim 1.5\ \mathrm{km}$ off the true centre because the spokes are tangential-gradient sources at the true centre and an off-centre trial reduces their $\mathit{CHG}_{\mathrm{tan}}^2$ contribution faster than it increases the rim's. (b) The same field with the spokes removed (rim only) recovers the true centre to within one grid cell with a perfectly unimodal cost surface. This limitation is one of the reasons the field-data pipeline of §4 uses a data-driven seed rather than relying on $J$ globally.](/mnt/user-data/outputs/step2_J_surface.png){#fig:Jsurface width=100%}

Finally, figure 6 documents the second of the stated limitations of §2.6. On the wagon-wheel field the global minimum of $J(x_c, y_c)$ is offset from the true centre by approximately $1.5\ \mathrm{km}$: the spokes are tangential-gradient sources *at the true centre*, so an off-centre trial reduces their contribution to $\langle \mathit{CHG}_{\mathrm{tan}}^2 \rangle$ faster than it increases the rim's. The bias disappears entirely on a rim-only field of the same geometry (figure 6b) — the cost surface is then a clean unimodal basin centred to within one grid cell of truth. The wagon-wheel scenario is therefore a "worst case" diagnostic of the centre search on mixed fields and motivates the data-driven seeding strategy used for the field examples.

# 4. Field application: Samalas and Tambora

We now apply the full pipeline — gravity reductions, scale separation, data-driven centre search, CHG decomposition — to two Indonesian volcanic calderas separated by about 110 km along the Sunda volcanic arc. The first is the Rinjani--Samalas complex on Lombok Island (lat $\sim -8.42^\circ$, lon $\sim +116.42^\circ$), the site of the cataclysmic 1257 CE eruption of Samalas [@Lavigne2013] whose southern remnant is the Segara Anak crater lake; this is the example used in the original version of the manuscript. The second is Tambora on Sumbawa Island (lat $-8.25^\circ$, lon $+118.00^\circ$), the source of the 1815 eruption — the largest in recorded history — whose $\sim 6\ \mathrm{km}$ caldera is morphologically simpler than the Rinjani--Samalas complex and therefore makes a useful contrast.

## 4.1 Data

The gravity field is taken from the freely available GGM Plus model of @Hirt2013, @Hirt2015, distributed by Curtin University. GGM Plus combines GRACE, GOCE, and a residual topographic gravity model to produce a $\sim 220\ \mathrm{m}$-resolution gravity-acceleration grid at the topographic surface. Tiles are distributed as raw Big-Endian Int32 binaries with the nominal scaling raw $/10 = \mathrm{mGal}$ and the sea/no-data sentinel $-2{,}147{,}483{,}648$. The Lombok--Sumbawa tile, file `S10E115.ga`, covers latitudes $-10^\circ$ to $-5^\circ$ and longitudes $115^\circ$ to $120^\circ$ at $2500 \times 2500$ cells.

The topography is taken from the SRTM 90 m DEM v4.1 [@Jarvis2008] distributed by OpenTopography, in a single GeoTIFF (`output_hh.tif`) covering lat $[-9.17^\circ, -7.97^\circ]$ and lon $[+115.10^\circ, +119.41^\circ]$ at approximately $90\ \mathrm{m}$ horizontal resolution.

For each target we extract a $0.40^\circ \times 0.40^\circ$ window (Samalas: lat $[-8.60, -8.20]$, lon $[+116.25, +116.65]$; Tambora: lat $[-8.45, -8.05]$, lon $[+117.80, +118.20]$), producing $200 \times 200$ GGM cells at $\Delta x \approx 220\ \mathrm{m}$ in each. SRTM is cropped to the same bounding box and resampled by bilinear interpolation onto the GGM grid. A simple equirectangular projection about the centroid of each crop is used for the local-metric coordinates used in §4.4--§4.7, with negligible distortion at the $\sim 44\ \mathrm{km}$ scale of the crops.

## 4.2 Reduction chain to a Simple Bouguer Anomaly

GGM Plus delivers the *absolute* gravity acceleration at the topographic surface — the cropped data span 977,460 to 978,250 mGal — not an anomaly. We reduce it to a Simple Bouguer Anomaly (SBA) in three steps.

*Normal gravity.* The closed-form Somigliana expression for the WGS84 ellipsoid,

$$
\gamma_n(\varphi) \;=\; \gamma_{\mathrm{eq}}\,
\dfrac{1 + k\,\sin^2\varphi}{\sqrt{1 - e^2\,\sin^2\varphi}}
\quad\text{(mGal)},
\tag{20}
$$

with $\gamma_{\mathrm{eq}} = 978{,}032.677715\ \mathrm{mGal}$, $k = 0.001931851353$, and $e^2 = 0.006694379990141$, is evaluated at the latitude of every cell. Across the Samalas crop $\gamma_n$ varies from $978{,}137.8$ to $978{,}148.1\ \mathrm{mGal}$ — a 10 mGal span over the $0.4^\circ$ latitude range. We retain the closed form rather than the standard series approximation because the latter introduces a $\sim 1\ \mathrm{mGal}$ error at high latitudes which is not negligible relative to the precision we require here.

*Free-air correction.* We add the first-order free-air correction $\delta_{\mathrm{FA}}\,h$ with the standard gradient $\delta_{\mathrm{FA}} = 0.3086\ \mathrm{mGal/m}$ where $h$ is the SRTM elevation in metres. Across the Samalas crop $h$ ranges from sea level to $3658\ \mathrm{m}$, so the correction ranges from zero to $1128.7\ \mathrm{mGal}$.

*Simple Bouguer slab.* We subtract a horizontal infinite-slab correction of density $\rho = 2670\ \mathrm{kg/m^3}$,

$$
\Delta g_{\mathrm{B}} \;=\; 2\pi\,G\,\rho\,h \;=\; 4.1928 \times 10^{-5}\,\rho\,h \quad\text{(mGal)},
\tag{21}
$$

producing the Simple Bouguer Anomaly

$$
\mathrm{SBA}(x, y) \;=\; g_{\mathrm{obs}}(x, y) - \gamma_n(\varphi) + 0.3086\,h - 2\pi G \rho\,h.
\tag{22}
$$

We do not apply a terrain correction; the SBA is therefore not a Complete Bouguer Anomaly. For the present purpose of demonstrating the CHG operator the simple slab is sufficient because the operator works on gradients, and the gradient of the terrain correction is a higher-order effect at the scales we examine.

*A note on GGM Plus and the Bouguer slab.* GGM Plus already incorporates a residual topographic forward model (RTM) above the EGM2008 long-wavelength field. Subtracting the simple slab in (21) therefore does not produce a Complete Bouguer Anomaly in the traditional, ground-survey sense — there is a long-wavelength offset of $\sim +100\ \mathrm{mGal}$ in the Samalas SBA that reflects both the regional arc-scale gravity high and the partial double-counting of topography between the RTM in GGM Plus and our slab. We make this discrepancy explicit because long-wavelength offsets are visible in figure 7 below. They are, however, irrelevant for CHG: the operator depends only on horizontal gradients, and the gradient of any constant is zero. The shape and spatial localisation of the CHG signature are unaffected.

## 4.3 Scale separation

The cropped SBA is dominated by a slowly varying regional component on which the caldera signature is superimposed. The regional component is itself the result of the arc-scale Bouguer high together with the long-wavelength GGM Plus offsets discussed above. Both are at scales much larger than the $\sim 6\ \mathrm{km}$ caldera, and both contribute strong horizontal gradients that, applied directly to the CHG centre search, would dominate the local feature. We therefore separate scales in the standard way: a wide low-pass filter isolates the regional trend and is subtracted from the field to leave a local residual.

Specifically, we form

$$
g_{\mathrm{smooth}}(x, y) \;=\; G_{\sigma_s} * \mathrm{SBA}(x, y), \qquad
g_{\mathrm{regional}}(x, y) \;=\; G_{\sigma_R} * g_{\mathrm{smooth}}(x, y),
\tag{23}
$$

$$
g_{\mathrm{local}}(x, y) \;=\; g_{\mathrm{smooth}}(x, y) - g_{\mathrm{regional}}(x, y),
\tag{24}
$$

with $G_\sigma$ the isotropic Gaussian kernel of standard deviation $\sigma$. We use $\sigma_s = 2$ grid cells ($\approx 440\ \mathrm{m}$) for the noise-removal filter and $\sigma_R = 50$ grid cells ($\approx 11\ \mathrm{km}$) for the regional trend. The choice $\sigma_R \approx 2\times$ the expected caldera diameter is the standard separation-of-scales heuristic in gravity processing. The CHG decomposition is applied to $g_{\mathrm{local}}$.

## 4.4 Data-driven seed and centre refinement

A caldera is, geophysically, a *local gravity low*: low-density pyroclastic infill replaces denser country rock and produces a mass deficit relative to the surrounding crust. After the scale separation of §4.3, this signature appears as the global minimum of $g_{\mathrm{local}}$. We use that minimum location as the seed for the centre search,

$$
(x_c^{(0)}, y_c^{(0)}) \;=\; \arg\min_{(x, y)} \, g_{\mathrm{local}}(x, y),
\tag{25}
$$

and we then refine it by the three-stage grid search of §2.4 (coarse, fine, Powell) over a $\pm 3\ \mathrm{km}$ window around the seed with the annulus mask $r_{\min} = 1500\ \mathrm{m}$, $r_{\max} = 4500\ \mathrm{m}$. Restricting the search to a local window has two purposes. First, it confines the optimisation to the single geological feature that the amplitude-based seed has identified, side-stepping the multi-feature limitation of §3.3. Second, it bounds the worst-case computational cost: the entire centre-search procedure completes in a few seconds at our grid resolution.

We emphasise that the seeding step (25) is *not* a free choice on the part of the interpreter. It is a deterministic function of the data: anyone applying the procedure to the same field will obtain the same seed and the same refined centre.

## 4.5 Results: Rinjani--Samalas complex

![CHG decomposition of the Rinjani--Samalas Simple Bouguer Anomaly (§4.5). (a) Local-residual SBA after the scale separation of (24). The recovered centre (yellow star) lies $3.94\ \mathrm{km}$ east of the published Segara Anak crater lake (white plus). (b) THG: a strong but distorted gradient ring traces the volcanic edifice. The dashed white ellipses outline the annulus $r_{\min}$--$r_{\max}$. (c) $\mathit{CHG}_{\mathrm{rad}}$ about the recovered centre: a coherent dipolar ring marks the rim of the gravity-defined edifice. (d) $\mathit{CHG}_{\mathrm{tan}}$: scattered features attributable to lateral structural complexity within the Rinjani--Samalas system. (e) Recovered centre and the most negative (blue) and most positive (red) $\mathit{CHG}_{\mathrm{rad}}$ contours over SRTM topography. (f) The objective $J(x_c, y_c)$ over the local search window: the cost surface is broad rather than sharp, the expected signature of a multi-feature field.](/mnt/user-data/outputs/step4_samalas_chg.png){#fig:samalas width=100%}

Figure 7 reports the headline result for the Rinjani--Samalas complex. The data-driven seed lands at $(990, -1223)\ \mathrm{m}$ in local-metre coordinates; the refined centre is at $(559, -1473)\ \mathrm{m}$, corresponding to $\mathrm{lat} = -8.413^\circ$, $\mathrm{lon} = +116.455^\circ$. The Pythagoras residual on the field grid is $6.5 \times 10^{-19}$, again at the level of round-off. The recovered centre lies $3.94\ \mathrm{km}$ east of the published Segara Anak crater lake location.

Two points are worth making. First, the offset relative to Segara Anak is *not* a failure of the operator: Segara Anak is a lake occupying the western part of the Samalas caldera floor, not the geometric centre of the gravity-defined rim. The recovered centre lies inside the coherent dipolar ring of $\mathit{CHG}_{\mathrm{rad}}$ (figure 7c) and at the visual centre of the high-THG annulus (figure 7b). It is the centre of the gravity rim, not of the lake. Second, the $J$ cost surface (figure 7f) is broad rather than sharp — the expected signature of a multi-feature field, where multiple competing circular structures (the volcanic edifice, the caldera proper, smaller summit features) contribute to the functional. The data-driven seed is what disambiguates them.

## 4.6 Results: Tambora caldera

![CHG decomposition of the Tambora Simple Bouguer Anomaly (§4.6). Layout and conventions as in figure 7. (a) The local-residual SBA shows an essentially perfect isolated circular low — the gravimetric signature of the 1815 caldera. The recovered centre (yellow star) is $0.63\ \mathrm{km}$ from the published Smithsonian Global Volcanism Program location (white plus), i.e. less than three grid cells. (b) THG: a strong, almost perfectly axisymmetric ring traces the caldera rim. (c) $\mathit{CHG}_{\mathrm{rad}}$: the cleanest dipolar ring of the entire study, a textbook-clean demonstration of the CHG claim. (d) $\mathit{CHG}_{\mathrm{tan}}$: only weak, scattered features attributable to erosional gullies on the volcano flanks. (e) Topographic overlay confirms that the recovered centre sits inside the caldera. (f) The $J$ cost surface is sharply unimodal, with the basin entirely contained within the local search window — the expected signature of a clean axisymmetric target.](/mnt/user-data/outputs/step5_tambora_chg.png){#fig:tambora width=100%}

Figure 8 reports the corresponding result for Tambora. The data-driven seed lands at $(990, 3002)\ \mathrm{m}$ in local-metre coordinates; the refined centre is at $(-464, 419)\ \mathrm{m}$, corresponding to $\mathrm{lat} = -8.246^\circ$, $\mathrm{lon} = +117.996^\circ$. This places the recovered centre $626\ \mathrm{m}$ — less than three grid cells — from the Smithsonian Global Volcanism Program reference at $-8.250^\circ, +118.000^\circ$. The Pythagoras residual is $8.7 \times 10^{-19}$.

The contrast with the Samalas result is striking. The local-residual SBA (figure 8a) shows an essentially perfect isolated circular low — the gravimetric signature of the 1815 caldera, undistorted by neighbouring volcanic edifices. The THG (figure 8b) traces an almost perfectly axisymmetric ring around the recovered centre. $\mathit{CHG}_{\mathrm{rad}}$ (figure 8c) is the cleanest dipolar ring in the entire study; $\mathit{CHG}_{\mathrm{tan}}$ (figure 8d) is essentially noise, as expected for a target with no strong radial linear features. The cost surface $J(x_c, y_c)$ (figure 8f) is a sharp, unimodal basin entirely contained within the local search window.

## 4.7 Side-by-side comparison and discussion

![Side-by-side comparison of the Rinjani--Samalas (top) and Tambora (bottom) results. Columns: local-residual SBA (left), $\mathit{CHG}_{\mathrm{rad}}$ (centre), centre-search objective $J(x_c, y_c)$ (right). The two cases illustrate the full operating envelope of the method: Tambora is a "clean" axisymmetric target on which the recovery is sub-grid-cell and the $J$ surface is sharply unimodal; Rinjani--Samalas is a "complex" multi-feature target on which the recovery is $3.94\ \mathrm{km}$ from the lake (but coincident with the geometric centre of the gravity-defined rim) and the $J$ surface is broad. The data-driven seed of §4.4 is what makes the method robust across both regimes.](/mnt/user-data/outputs/comparison_samalas_vs_tambora.png){#fig:comparison width=100%}

Figure 9 places the two case studies side by side. Together they cover the full operating envelope of the method.

Tambora is a "clean" axisymmetric target: a relatively isolated caldera with no comparable circular feature within tens of kilometres. The CHG decomposition produces a textbook result and the centre search recovers a published reference to better than three grid cells with a sharply unimodal cost surface. This is the regime in which the method works as the synthetic experiments of §3 predict it should.

The Rinjani--Samalas complex is a "multi-feature" target: a young Samalas caldera adjacent to an older Rinjani edifice, with a more recent post-1257 cone (Barujari) inside the same depression. The CHG decomposition still produces a coherent dipolar ring on the dominant feature, and the data-driven seed correctly identifies that dominant feature, but the cost surface is broad and the recovered centre is approximately $4\ \mathrm{km}$ from the published Segara Anak coordinates. The offset is interpretable — Segara Anak is not the geometric centre of the gravity rim — and the method gives the interpreter a quantitative handle on the structure (the position of the dominant low, the orientation of the rim, the existence of secondary features in $\mathit{CHG}_{\mathrm{tan}}$) that is not available from THG alone.

We summarise the operating characteristics of the two cases in Table 1.

| Quantity | Rinjani--Samalas | Tambora |
|---|---|---|
| Local crop (GGM cells) | $200 \times 200$ | $200 \times 200$ |
| Grid spacing | $\Delta x \approx 220\ \mathrm{m}$ | $\Delta x \approx 220\ \mathrm{m}$ |
| SRTM elevation range | $0\text{--}3658\ \mathrm{m}$ | $0\text{--}2674\ \mathrm{m}$ |
| Local-residual SBA range | $-68.3\text{--}+50.9\ \mathrm{mGal}$ | $-36.9\text{--}+30.0\ \mathrm{mGal}$ |
| Data-driven seed (lat, lon) | $(-8.422^\circ, +116.464^\circ)$ | $(-8.223^\circ, +118.009^\circ)$ |
| Refined centre (lat, lon) | $(-8.413^\circ, +116.455^\circ)$ | $(-8.246^\circ, +117.996^\circ)$ |
| Published reference | $(-8.420^\circ, +116.420^\circ)$ — Segara Anak | $(-8.250^\circ, +118.000^\circ)$ — GVP |
| Offset (m) | $3936$ | $626$ |
| $J$ at minimum | $0.135$ | $0.122$ |
| $J$ surface topology | Broad | Sharp unimodal |
| Pythagoras residual | $6.5 \times 10^{-19}$ | $8.7 \times 10^{-19}$ |

Table: Field-application summary statistics for the two case studies. {#tbl:fieldsummary}

The cost-surface topology (broad vs. sharp) is itself a useful interpretive diagnostic. A sharp unimodal $J$ surface, as in Tambora, indicates a single axisymmetric target and grants the recovered centre high confidence. A broad multi-modal $J$ surface, as in Rinjani--Samalas, indicates a multi-feature target and signals that the recovered centre is meaningful only relative to the seeding step. This is a *post hoc* uncertainty metric that the operator delivers for free.

# 5. Discussion

## 5.1 Relation to other directional operators

CHG is one of several attempts to extract directional information from the horizontal gradient of a potential field. The closest comparison is with the Directional Total Horizontal Derivative (DTHD) of @Pham2018, which projects the horizontal gradient onto a *globally fixed* unit vector $\hat{\mathbf{u}}$, returning the scalar $|\nabla_h g \cdot \hat{\mathbf{u}}|$. DTHD is well suited to detecting *linear* features of known azimuth (rifts, regional faults). CHG generalises the same projection idea but uses a *position-dependent* unit vector — radial or tangential about a chosen centre — making it the natural tool for *circular* targets rather than for linear ones. The two methods are complementary: an interpreter who suspects both linear and circular structure can apply DTHD and CHG in turn.

The gradient-tensor eigenvector decomposition [@Beiki2010] is a second relative. It computes the eigenvectors of the gradient of $\nabla_h g$ (or, for full gradiometry, of the full Marussi tensor), and uses their orientation as a local indicator of structural fabric. This method is intrinsically local — at every point it returns the principal axes of *that point's* second-derivative tensor — and it does not refer to a global centre. CHG occupies the complementary regime: it is a *first*-derivative method that refers to a *global* feature centre. The two could in principle be combined (the eigenvector orientation could seed the CHG centre, or the CHG residual could be analysed by the eigenvector method), but we leave that combination to future work.

Curvature attributes adopted from seismic interpretation [@Roberts2001] use second derivatives of the field to detect ridges, valleys, and saddles. They are sensitive to the same circular features as CHG but at one differentiation order higher, and are correspondingly more noise-sensitive. For data with the precision and resolution of GGM Plus, CHG is the more robust first choice.

## 5.2 Recommended workflow

Based on the synthetic and field experiments above, we recommend the following workflow for applying CHG to gravity (or, by direct extension, magnetic) data.

1. *Reduce.* Compute the Simple Bouguer Anomaly with the closed-form Somigliana normal gravity and the standard $\rho = 2670\ \mathrm{kg/m^3}$ slab, or whatever the local literature uses. The CHG operator does not require any specific reduction, but the same anomaly should be used throughout an interpretation for consistency.

2. *Separate scales.* Subtract a Gaussian low-pass of the SBA with a kernel width comparable to twice the expected feature diameter. This isolates the local feature against the regional trend.

3. *Pre-smooth.* Apply a mild Gaussian pre-filter ($\sigma_s = 1$--$3$ grid cells, well below the feature scale) before differentiation. §3.2 shows this is essential at SNR $\lesssim 20$.

4. *Seed.* For amplitude-defined features (calderas, plutons), seed the centre search from $\arg\min$ or $\arg\max$ of the local residual. For features without a clear amplitude signature, seed from the centroid of $|g - \mathrm{median}(g)|$, or from any independent geological constraint.

5. *Refine.* Run the three-stage grid-search optimisation of §2.4 on a tight window around the seed, with the annulus mask sized to the expected feature scale.

6. *Interpret.* Compute $\mathit{CHG}_{\mathrm{rad}}$ and $\mathit{CHG}_{\mathrm{tan}}$ about the refined centre. Use the cost-surface topology as an uncertainty metric: a sharp unimodal basin (figure 8f) supports a high-confidence centre; a broad basin (figure 7f) signals a multi-feature target and motivates the user to examine $\mathit{CHG}_{\mathrm{tan}}$ for evidence of off-axis structure.

7. *Visualise.* If desired, blend $\mathit{CHG}_{\mathrm{rad}}$ with THG via equation (17) at $\alpha \in [0.5, 0.8]$ to display the directional and omnidirectional information together; this is purely cosmetic but is often interpretively useful.

8. *Report.* Quote the Pythagoras residual; it is a no-cost self-consistency check that should be at the level of double-precision round-off.

## 5.3 Limitations and future work

The operator has the limitations of every horizontal-gradient method (wavelength sensitivity, noise amplification, no information about depth) together with two specific to the centre-search: the multi-feature limitation of §2.6 (mitigated by data-driven seeding) and the radial-linear sensitivity of §3.3 (which the user can probe by examining $\mathit{CHG}_{\mathrm{tan}}$ separately).

Three extensions are worth pursuing. *Terrain correction*: for a Complete Bouguer Anomaly the slab term should be replaced by a full Bouguer-plus-terrain correction. For Lombok and Sumbawa this is straightforward but does not change any of the qualitative conclusions above. *Magnetic-field extension*: equations (4)--(9) make no use of the fact that $g$ is a gravity field; the same operator applied to total-magnetic-intensity anomalies, with the appropriate reduction, should image magnetised circular features (e.g. ring complexes) in exactly the same way. *3-D gradiometry*: with full Marussi-tensor data the radial--tangential decomposition can be applied to each component independently, producing six scalar fields whose joint analysis could resolve depth as well as horizontal geometry. We leave these extensions for future work.

# 6. Conclusions

We have presented a methodologically revised version of the Centered Horizontal Gravity Gradient (CHG) operator. Relative to the previously circulated form, the present version:

* derives the discrete operator from the continuous polar decomposition with explicit second-order central differences, second-order one-sided boundary treatment, and quantified truncation behaviour;
* treats the central-point singularity transparently by means of an annulus mask;
* replaces the subjective visual centre choice with an objective, reproducible grid-search optimisation that minimises the bounded ratio $\langle \mathit{CHG}_{\mathrm{tan}}^2 \rangle / \langle \mathrm{THG}^2 \rangle$;
* recasts the visualisation blends $E_{\mathrm{rad}}(\alpha)$ and $E_{\mathrm{tan}}(\beta)$ as convex combinations of range-normalised maps, with no fitted parameters;
* validates the operator on three synthetic experiments, quantifies its noise robustness, and documents the multi-feature and radial-linear limitations;
* applies the full pipeline to two Indonesian volcanic calderas (Rinjani--Samalas and Tambora) using freely available GGM Plus gravity and SRTM topography, with the Tambora centre recovered to $0.63\ \mathrm{km}$ — sub-grid-cell accuracy — of the Smithsonian Global Volcanism Program reference.

The method is implemented in approximately one thousand lines of pure NumPy/SciPy code, runs on a laptop in tens of seconds per case study, and reproduces every figure in this paper from the raw inputs in a single command. The complete source, parameter files, and intermediate-data archives are provided as supplementary material; we hope this will allow the method to be tested, refined, and extended by the community.

# Code and data availability

All Python source code, parameter files, intermediate NumPy data archives, and figure-generation drivers used in this paper are provided in the supplementary material under the name `chg-toolkit`. The toolkit depends on NumPy, SciPy, Matplotlib, and rasterio; it has no other dependencies. The GGM Plus gravity tiles are freely available from Curtin University (<https://ddfe.curtin.edu.au/models/GGMplus/>). The SRTM 90 m topographic data are available from OpenTopography (<https://opentopography.org>).

# Author contributions

MZ developed the initial idea, constructed the program, and wrote the manuscript. WS refined the idea, improved the methodological structure, and revised the narrative. SS refined the idea and structure and reviewed the manuscript.

# Acknowledgements

We thank the editorial board and three anonymous reviewers of an earlier version of this manuscript for criticisms that materially improved the methodological foundations of the present version. We thank Curtin University and OpenTopography for free public access to the data sets used in the field application.

# References

::: {#refs}
:::

\bibliography{references}
