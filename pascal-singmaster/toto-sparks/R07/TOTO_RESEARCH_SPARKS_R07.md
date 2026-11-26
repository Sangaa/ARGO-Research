# TOTO | دفتر الشرارات R07 — minimum readout cost versus conditioning
26 November 2026 · SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED (numerical conditioning is bounded floating-point evidence). Originality and independent validation unassessed.

## Source and use
[R06](../R06/TOTO_RESEARCH_SPARKS_R06.md), blob 3e0c842aaeb4344c97c78eb58aae48a17fe03a5e; [Library R06 card](https://github.com/Sangaa/ARGO-Library/blob/829b50172b11e5369daf508d38d0b786efd9c741/cards/toto-directional-kernel-20261126-r06.json), blob bf1f1469c42f0228ce59a2f2c6c6e560a9866bdd, SOURCE_ONLY. Retrieved the card and its source directly; no claim of using the search CLI. R06 explicitly distinguishes algebraic uniqueness from noise stability. Changed action: compare smallest singular values of the actual observation matrices even when nullity is zero, rather than score only exact rank. The underlying switching-polynomial theorem is established prior art credited in R06. The present choice of cost and test model is TOTO's.

## Exact minimum additional cost
Square coordinates 0..s on both axes, N=s+1, s>=4. The fixed starting observations are normals (1,0),(0,1),(1,1),(1,-1). Every extra primitive integer normal is distinct up to sign, so both components are nonzero. A complete projection has one readout per distinct occupied value of a*i+b*j, counting even singleton bins; ignore per-instrument overhead, measurement precision, hardware feasibility and shared readout costs. Cost is the sum of additional bin counts.

For a primitive normal with absolute components A=|a|, B=|b|, a single-direction line-sum matrix has one nonempty disjoint indicator row per bin, so its rank equals the number of bins. By the single switching factor of bidegree (B,A), this number is
C=N^2-(N-A)_+(N-B)_+.
This also follows by counting chains of lattice sites separated by primitive tangent (b,-a): every chain is one occupied bin; the number of links in chains is (N-A)_+(N-B)_+.

The R06 rank/nullity formula gives injectivity precisely when the extra sum of A or extra sum of B is >=s-2. Let t=s-2. Without loss of generality consider B. If any B>=t, that direction alone costs at least N+(N-1)t. Otherwise each B<t and its cost is at least N+(N-1)B because A>=1. Sum over directions to obtain a lower bound N+(N-1)t again. If B>=N, cost=N^2 also satisfies the bound. The bound is attained by the single normal (1,t), which is primitive and not in the base set for s>=4. Thus the global minimum within this bin-count model (including any finite number of additional directions) is s^2-s+1. This is a derivation, not a search result. It does not optimize a physical instrument.

## Stability experiment
Use the raw, unweighted line-sum matrix A (here A denotes the matrix, not the normal component). Model additive readout error e, Euclidean norm, unconstrained linear least-squares inversion on real cell weights. For full column rank, ||delta p||_2 <= ||e||_2 / sigma_min(A), and the constant is sharp for arbitrary additive errors. No noise distribution is assumed; positivity/normalization-constrained estimators may differ. Singular values are numerical SVDs, not exact arithmetic. Comparing designs uses the same base and per-bin units. In particular a single (1,10) projection for s=9 is injective by itself because i+10j enumerates all 100 cells; this is direct cell readout in disguise and may not be feasible as an imaging direction in practice.

For s=9, base nullity 49, base readouts 58. Additional (1,7) costs 73, sigma_min ~0.07902 (worst linear amplification ~12.65). (1,8) costs 82, sigma_min ~0.29060 (amplification ~3.44). (1,10) costs 100, sigma_min=1 numerically (amplification ~1). The cheapest identifying design is therefore not automatically the best noise-stable choice. The 9 additional bins between the first two designs buy substantially improved conditioning in this model. No actual noisy samples or reconstructions were simulated; this is a matrix sensitivity calculation.

## Measured scope and reproducibility
Run OPENBLAS_NUM_THREADS=1 python -I probe.py with NumPy (used version 2.3.5). See [probe.py](probe.py), [actual stdout](probe.log).
1,092 exact occupied-bin count checks for s=1..12 and primitive positive components 1..12.
For the 10x10 square: 62 single-direction numerical rank comparisons, 40 injective; 68 two-direction comparisons with additional cost<=100, 26 injective. All numerical ranks at threshold 1e-10 matched R06 predictions. SVD values and budget-wise best designs are measured only in the enumerated positive-normal candidates (components <=10), not a global stability optimum. Ties can switch with numerical implementation. The final line before NumPy version in the log reports the theoretical nullity for (1,6); despite an inaccurate code comment, no explicit collision vector is constructed in that section. Preserve this limitation.
No physical noise measurement, literature survey of the optimization, independent validation, or proof of global conditioning optimum.

## Margin
Rank zero is a boundary; sigma_min measures distance to losing it in an operator-norm sense. Cost of information depends on measurement model, not only count. Can design a Pareto frontier under realistic noise covariance, or study how sigma_min scales with s for the cheapest normal? Do not equate exact recovery with stable recovery. Don't turn a bin index into a physical angle or frequency without instrument assumptions.
