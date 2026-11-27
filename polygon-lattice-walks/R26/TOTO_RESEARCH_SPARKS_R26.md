# TOTO | R26 — Equal-trace planar selection and a sharp two-choice bound
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED exact finite controls; decimal illustrations BOUNDED_PROXY. No independent review or originality claim.

## Retrieval and changed action
Read R25 at live main bd8d526f5c1c0d041c1a49117dd5de7272beb1c1, blob cc94635e620d8eda4f756a1805c5219aa6d81aec. R25 gave an arbitrarily poor E-greedy counterexample with unequal group trace and a known log-det guarantee. TOTO chose the restricted equal-trace planar problem and budget two. This does not adjudicate R25's more general unequal-cost problem. No causal learning claim.

## Model and exact reduction
Each of at least two independent equal-cost PSD symmetric 2-by-2 matrices has trace 2R, R>0, and can be written S_i=R I+L(v_i), where L(a,b)=[[a,b],[b,-a]], ||v_i||<=R. Baseline beta I with beta>0 (including R25's I). After choosing j distinct groups, H=(beta+jR)I+L(sum v_i). Eigenvalues beta+jR +/- ||sum v_i||. Therefore for fixed j maximizing E=lambda_min(H) and maximizing D=log det H have identical rankings, including greedy next choices. Both minimize the imbalance vector norm. This equivalence also holds with a fixed anisotropic SPD baseline, adding its traceless vector to the sum, but the following ratio theorem assumes isotropic baseline. At fixed j the A criterion tr(H^-1) is also monotone in squared norm, since tr(H^-1)=2(beta+jR)/det H. This is elementary two-dimensional algebra, not a general dimension theorem. Background on established design objectives and log-det greedy guarantee: https://arxiv.org/abs/2007.05377 and https://sidbanerjee.orie.cornell.edu/docs/CDC_sensorsel.pdf (search abstracts checked). No claim the present bound is new.

## Sharp quarter guarantee when selecting two
Let a be the vector chosen first (minimal norm). Let u,v form an optimal pair, d=||u+v||, and let g be the norm of the greedy pair sum. If a is in an optimal pair, the second greedy choice is optimal. Otherwise both u and v are available, so
g^2 <= min(||a+u||^2,||a+v||^2)
<= ||a||^2 + (||u||^2+||v||^2)/2 + a dot (u+v)
<= 2R^2+R d.
Also 0<=d<=2R. For d<2R,
2R-g >= 2R-sqrt(2R^2+R d)
= R(2R-d)/(2R+sqrt(2R^2+R d)) >= (2R-d)/4.
For d=2R, g<=2R and the inequality still holds. Adding the positive isotropic baseline yields
E_greedy >= beta+(E_opt-beta)/4 >= E_opt/4.
In particular even the gain above baseline has a quarter guarantee, interpreted as an inequality even when optimal gain is zero. Assumes exactly two distinct equal-cost groups, additive independent information, common trace and isotropic baseline. No k>2 bound claimed. This proof holds for any finite candidate pool, not just triples.

## Sharp family with strict first choice and positive definite groups
Take rational t>0 tending to zero, c=(1-t^2)/(1+t^2), s=2t/(1+t^2), r=1-t^4 and L=t^(-4). Candidate imbalance vectors are L(r,0), L(c,s), L(c,-s); use common group scalar part R=L+1 and baseline I. All groups are strictly PD and have identical trace within each instance, and the first choice is uniquely the first vector because r<1. The optimum for sufficiently small t is the second and third pair, with norm d=2Lc. The greedy norm is g=L sqrt(r^2+1+2rc). As t->0, c=1-2t^2+O(t^4), so d/L=2-4t^2+O(t^4), g/L=2-t^2+O(t^4). In particular g>d for sufficiently small t. Final scalar part is 2L+3; hence E_g/E_opt = (L(t^2+O(t^4))+3)/(L(4t^2+O(t^4))+3) ->1/4. The common trace grows across instances, not within an instance. If trace and positive baseline are fixed numerically, this limit does not imply sharpness for that narrower class. For every PSD 2-by-2 group an anchor realization is possible using independent centered pairs along its eigenvectors; equal monetary or spatial cost is only a model assumption.

## Actual execution
Ran python3 -I probe.py locally using only the standard library. 81 integer points in radius-five disk, all 85,320 unordered triples of distinct candidates, lexicographic item order and first-index tie rule. Exact norm-square comparisons found 19,798 suboptimal greedy cases and verified the quarter inequality (even without baseline) and the fixed-trace determinant identity in every triple. The quarter check squares only a nonnegative side of the equivalent radical inequality. Eight rational sharp-family parameters t=1/j with j=2..256, strict first choice and pair identities checked exactly. Displayed decimal ratios (60-digit Decimal evaluation, not interval-certified) decrease on these samples to about 0.2500133514; the limit follows from the separate expansion proof. Actual stdout probe.log. Local blobs c9613668e1f28bf8c4bd10a465f3b13b1c26522b and 9fa719347008dfb6c6e0b2de629e48a401bf487d. No physical instrument, random sampling, unequal costs, correlated errors or independent validation.

## Margin
The previous unbounded failure becomes a sharp positive guarantee in a restricted model, but greedy is not exact. Equal trace aligns E and D in two dimensions only. Next test budgets k>2 and anisotropic baselines, or swap improvements for imbalance-vector selection. Preserve the boundary between information geometry and organizational analogy.
