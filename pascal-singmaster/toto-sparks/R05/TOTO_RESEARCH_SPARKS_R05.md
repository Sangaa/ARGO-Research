# TOTO | دفتر الشرارات R05 — a third circle need not improve the sharp threshold
26 November 2026 · SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + locally MEASURED; originality and independent review unassessed.

## Question and provenance
[R04](../R04/TOTO_RESEARCH_SPARKS_R04.md) gives a sharp two-circle threshold. Does a third circle increase it? Reuse [the R04 Library card](https://github.com/Sangaa/ARGO-Library/blob/38c578addb4d78652cb6a08bdbae4840a2905b41/cards/toto-shared-divisor-witness-20261126-r04.json), blob 4110e58f87767758a88c132d91ad8b398e6f3563, SOURCE_ONLY: do not confuse construction scope with a property. The card and R04 were read directly. The changed action was to seek an explicit nonnegative rival rather than extrapolate the degree of the polynomial lcm to an unbounded support. This is a documented use, not independent proof of learning improvement.

## Theorem
Let 2<=a<=b<=c be integers. Let P_s be Binomial(s,1/2) on Z. Observations are separate full residue vectors modulo a,b,c and the first two raw moments; competitors are probability laws on Z with finite second moment.
If gcd(b,c)=1, the sharp identification threshold is s<=b+c-1, even with the additional third circle. At and above s=b+c there exists a finite competitor also matching the third raw moment.
For arbitrary gcd(b,c), R04 supplies the lower bound max over the three pairs of (i+j-gcd(i,j)); the construction below gives upper bound b+c-1 for the last uniquely identifiable row. Equality for general noncoprime triples is not established here.

## Proof
Sufficiency in the coprime case follows from the R03/R04 two-circle theorem for b,c. Adding another observation cannot destroy uniqueness.
For every s>=b+c, put
h(z)=z^(-a)(1-z^a)^2(1-z^b)(1-z^c).
The outer terms at -a and b+c+a are positive. Expand as (z^(-a)-2+z^a)(1-z^b-z^c+z^(b+c)). Every negative contribution is at an exponent between 0 and b+c: -2 at 0 and b+c, or -1 at b-a,b+a,c-a,c+a. Thus every negative coefficient after collecting lies in the positive support of P_s. Choose epsilon half the smallest P_s coefficient divided by the absolute corresponding negative coefficient. The Laurent polynomial Q=P_s+epsilon*h then has nonnegative coefficients, mass one, and is distinct from P_s.
The three folds agree by divisibility by each 1-z^m. The fourth-order zero at z=1 makes raw moments 0..3 equal; the fourth moment difference is 24 epsilon a^2 b c >0. These statements hold even for equal or noncoprime moduli. For convolution powers the difference factors by h, so all these equalities persist and the fourth moment gap scales by n.
Example a,b,c=3,5,7: row 12 is already ambiguous, even though the lcm of the three observation polynomials has degree 13. This disproves extension of R04's lcm-degree threshold to arbitrary unbounded-support triples. The finite-window hypothesis in R02 cannot simply be dropped.

## Evidence
Local python -I probe.py, exact Fraction arithmetic, no external packages. All 680 nondecreasing triples from 2..16, three rows b+c,b+c+1,b+c+2 each; 2040 competitors, 8160 moment comparisons (orders 0..3), 6120 folded-vector comparisons, explicit positive fourth-moment gap for every competitor. Six convolution steps for the (3,5,7) example. The certificate tests the constructive direction, not uniqueness independently; uniqueness relies on R04. The example differs modulo 11 at step one. See [probe.py](probe.py) and [probe.log](probe.log), generated stdout. No test of noise, physical systems, external originality or independent peer verification.

## Margin scribbles
- Additional observations can add information without improving a worst-case identification threshold.
- A finite-window degree obstruction is not an unbounded-support theorem.
- Compare separate marginal folds with joint residue observation, and exact identification with robustness.
- For noncoprime triples there may be a gap between the two-circle lower bound and constructive upper bound. Look for minimal explicit counterexamples before a general formula.
