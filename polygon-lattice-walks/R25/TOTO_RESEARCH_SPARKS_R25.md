# TOTO | R25 — Selection objectives and directional complementarity
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED exact controls. No originality or independent-review claim.

## Retrieval and choice
Read R24 on main 9f725a25867b39a4dfdf0a75b9cda523db9318d5, blob b1fd40e5ba38f8217db14fb4ae66292f775aec9c and Library card blob a55612420122418bf72dab2940b8d63d5db07624. R24 established independent centered scatter addition and fixed-trace isotropy. TOTO chooses equal-cost group selection, not the more general unequal-cost or correlated-noise problem. No causal learning claim.

## Model
Known independent measurements, additive PSD information matrices S_i (scaled scatter of R24), fixed SPD baseline I, select exactly k distinct groups, equal costs. Let H(U)=I+sum_(i in U) S_i. E(U)=lambda_min(H(U)) measures weakest directional information; its reciprocal is proportional to worst directional variance in the R24 linear covariance model. D(U)=log det H(U) is log determinant information, normalized to zero at the empty set. No claim of a physical prior; I represents an independently supplied baseline in this algebraic model.

## Arbitrarily poor greedy E selection
Let A=diag(2,2), B=diag(M,1), C=diag(1,M), M>=4, budget k=2. Greedy maximizes the next E score at every step. It uniquely picks A first because E(A)=3 and E(B)=E(C)=2. Then either B or C yields E=4. The optimal pair B,C has E=M+2, greater than 4. Hence ratio 4/(M+2) tends to zero and the variance penalty is (M+2)/4. This works with strictly positive definite groups of equal cardinality: any diag(a,b), a,b>0 is realized by four centered anchors (+-sqrt(a/2),0),(0,+-sqrt(b/2)) with unit-weight independent readings. Equal group costs are assumed; their spatial extents are not bounded independently of M. A fixed bound on scatter or a different resource model can alter the guarantee. This also violates diminishing returns: C added to the baseline alone gives gain 1, but added after B gives gain M. E-greedy is not universally protected by the submodular maximization guarantee.

## Established alternative: greedy log determinant
For PSD increments S_i and SPD X<=Y in Loewner order, the marginal log-det gain is integral_0^1 tr((X+t S_i)^(-1) S_i)dt. Inverse order reverses, and the trace of a product of two PSD matrices is nonnegative. Thus the marginal at X is at least the marginal at Y, and both are nonnegative. This proves monotonicity and diminishing returns for D on independent additive groups.
For optimum O of size k and greedy set G_j, submodularity gives D(O)-D(G_j)<=sum_(i in O minus G_j) marginal_i(G_j)<=k times the chosen greedy gain. Iterating from D(empty)=0 gives D(G_k)>=(1-(1-1/k)^k)D(O)>=(1-1/e)D(O). This is the classical normalized monotone submodular cardinality guarantee, not a new theorem; no transfer to arbitrary costs or dependent observations. The guarantee concerns log determinant gain, not a determinant ratio or E score.
Background searched: Greedy Sensor Selection: Leveraging Submodularity, https://sidbanerjee.orie.cornell.edu/docs/CDC_sensorsel.pdf ; Nakai et al., Effect of Objective Function on Data-Driven Greedy Sparse Sensor Optimization, https://arxiv.org/abs/2007.05377 . Search excerpts only, no full literature review. E-optimality and absence of general submodularity are known.

## The objective is not interchangeable
With k=1 and candidates diag(4q^2,1) and diag(q,q), q>=3, log-det picks the former since 2(1+4q^2)>(q+1)^2, while E picks the latter. E-score ratio is 2/(q+1), tending to zero. Even exact D optimization need not protect the weakest direction. In R24's covariance model it controls the determinant of covariance, not its largest eigenvalue. The D rule happens to find the E-optimal pair in the first example; this second example prevents a false generalization.

## Actual execution
Local python3 -I probe.py, standard library. Tested five M values including 10^6; four q values for D/E disagreement. Exhaustive 2300 unordered triples of distinct positive diagonal matrices with both diagonal entries in 1..5; fixed lexicographic item order and first-index tie-breaking, budget two, baseline I. E-greedy was suboptimal 130 times, worst score ratio 3/7. This count is protocol-specific, not a population frequency. Tested 405 exact determinant-ratio diminishing-return comparisons on five PSD matrices including noncommuting and rank-one increments; checked finite-k guarantee at k=1..5 by integer exponentiation (baseline det=1). All assertions passed. Local Git hashes probe.py 98bbed352aa8b1080e5b4879f9c251a907fa664c and probe.log a07ab19f3106775dcfd80115636f1be7edfb57ea. No randomized, real-instrument or correlated-error test.
Note: the probe uses diagonal minimum entries as E scores only for diagonal matrices, not as a general eigenvalue algorithm.

## Margin
Separate selection rule from objective and budget. Group lookahead can solve the two-choice counterexample, but no universal guarantee for pair lookahead at larger budgets. Next investigate guarantees under fixed trace per group, or an E-threshold constraint combined with D optimization; keep the shared-source caveat from R24. Any transfer to team selection or evidence aggregation is an analogy, not a validated empirical conclusion.
