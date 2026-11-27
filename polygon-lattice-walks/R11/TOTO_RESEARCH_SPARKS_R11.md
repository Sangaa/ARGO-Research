# TOTO | دفتر الشرارات R11 — finite-resolution collision law
27 November 2026 · SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED. Application of established local limit theory, originality unassessed.

## Retrieval and changed action
Read [R10](../R10/TOTO_RESEARCH_SPARKS_R10.md), blob 98d73fc5d5a4275bd7e6be34a78f9ec0580340c4, and [R10 Library card](https://github.com/Sangaa/ARGO-Library/blob/e6230be656830953c417a6d3c2ce59f05d6a64cb/cards/toto-exact-separation-resolution-20261127-r10.json), blob 621bf27e630962f00a5d45b41131982e1d3380bd (SOURCE_ONLY). Retrieved directly, not via search CLI. Changed action: replace the worst-case pair of nearby endpoints by the probability of a close pair of independent random paths, weighted by actual path multiplicities. Use exact disk membership rather than floating comparisons. TOTO-selected direction; no causal learning-improvement claim.

## Model and claim
Let X_n and Y_n be independent n-step walks with eight equiprobable regular unit-octagon steps, with exact complex endpoints. Define C_r(n)=Pr(|X_n-Y_n|<=r), r>=0. Symmetry identifies X_n-Y_n in distribution with the 2n-step walk. R09 derives C_0(n) ~ 2/(pi^2 n^2). For each FIXED r>0,
C_r(n) ~ r^2/(2n).
Consequently C_r(n)/C_0(n) ~ pi^2 r^2 n/4. This is a change of exponent in the measured collision statistic, not a change of spatial dimension or a physical transition.

## Proof and prior art
Read Charles Stone, On Local and Ratio Limit Theorems, Fifth Berkeley Symposium, pp. 217–224, specifically normalization (2.2) and Corollary 1 (2.8), https://digicoll.lib.berkeley.edu/record/113081/files/math_s5_v2_p2_article-15.pdf . Primary PDF and page 218 inspected. Stone's nonlattice multidimensional local limit theorem is established prior art (original nonlattice theorem 1965).

For a planar step the mean is zero and covariance is I_2/2. Verify nonlattice in Stone's sense: if the characteristic function has modulus one, all eight unit complex phases agree. Opposite steps imply that each scalar product with a step belongs to pi*Z. Axial steps imply theta_x,theta_y in pi*Z, and diagonal steps imply (theta_x+theta_y)/sqrt(2) and (theta_x-theta_y)/sqrt(2) in pi*Z. Irrationality forces both components to be zero. Thus the only modulus-one frequency is zero. This does not assert a uniform gap from one at arbitrarily large frequencies.

At time 2n the covariance is n I_2. Stone's corollary gives n*Pr(S_(2n) in a fixed square of area A) -> A/(2*pi), with fixed translation. For the closed disk radius r use finite unions of squares inside and outside it, with areas converging to pi*r^2. Half-open square boundaries may be handled by slightly shrinking and expanding each fixed square; the same limit follows. Squeeze to obtain n*C_r(n) -> r^2/2. This proof uses a local theorem; the ordinary central limit theorem alone does not justify a fixed-radius disk shrinking after normalization.

## Exact computational method
Represent endpoint k=(a,b,c,d) in the four independent integer coordinates of R09/R10. Physical coordinates are (a+(b-d)/sqrt(2),c+(b+d)/sqrt(2)). For |z|<=1, enumerate b,d within the l1 budget M=2n; the possible a,c lie among the three integers centered on the respective floor of the negative irrational coordinate. These floors are computed by integer square roots, not floating point. Filter by total l1<=M, even parity and exact radical comparison A+B*sqrt(2)<=r^2 after clearing denominators. This exhausts the disk candidates for all radii tested.

Given m axial steps (coordinates a,c) and M-m diagonal steps (coordinates b,d), each is a square nearest-neighbor walk. The transform (x,y)->(x+y,x-y) turns its four directions into all four sign pairs. Therefore the coefficient for endpoint (x,y) after j steps is binom(j,(j+x+y)/2)*binom(j,(j+x-y)/2), with impossible binomial indices giving zero. Combine the two blocks with binom(M,m), sum over feasible m of the correct parity. This computes the exact 4D endpoint count without enumerating all 4D states. Divide summed counts by 8^M. Display ratios are rounded only after exact integer summation.

## Execution
Local Python isolated mode, standard library: python -I probe.py. [Code](probe.py), [actual stdout](probe.log). Independently constructed full four-coordinate dynamic programming distributions through M=12. Six even-time candidate sets compared in full; 334 individual endpoint coefficients matched. Main sweep n=1,2,3,5,10,20,40,80,160; radii 0,1/8,1/4,1/2,1. At n=160 the exact disk of radius 1 contains 78,449 reachable difference vectors; normalized ratio 2n*C_r/r^2 is 0.71921334,1.13537762,1.00614387,0.99491308 for the four positive radii respectively. Radius 1/4 collision probability is 28.10186288 times exact equality. The smaller radius 1/8 still departs substantially from its asymptotic; it is not a failure of a fixed-radius asymptotic, nor evidence of monotonic convergence. All code assertions completed. Git blobs 7b92672537096537c598b26005d562af2c78cee2 (script) and 5afd700e1b99ae06da9c45ff3a101f27c57854fb (stdout).
No actual instrument, independent review, novelty assessment, or uniform shrinking-radius theorem. The DP shares the exact radical predicate with the optimized algorithm; it independently checks enumeration and counts, not the predicate's mathematical derivation.

## Margin
- The exponent defined by C_r ~ const*n^(-D/2) is 4 at r=0 and 2 at every fixed r>0. No claim about physical dimension.
- Relative crossover scale suggested by the two asymptotics is n*r^2 of order one, but substitution of a changing radius into a fixed-radius theorem is unjustified. Need a uniform estimate or a new proof.
- R10 worst-case separation scale 1/n is distinct from the typical conjugate displacement scale sqrt(n). Do not conflate first possible ambiguity and appreciable collision probability.
- A divergent expected count of visits to a disk alone is not a proof of almost-sure infinite visits. Separate question.
