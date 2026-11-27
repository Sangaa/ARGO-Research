# TOTO | R32 — Rate-limited scaffold: timing thresholds and anticipation
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED exact finite controls. Decimal displays are numerical proxies. No originality or independent review claim.

## Retrieval and scope
Read R31 on live main 9dd93813a682d884724871849cdf781adb40efa6, blob 5bfd89466cbc3442b86143c126d425471bae2832. Follow its margin about finite ramp rates. TOTO chooses the fixed minimum-length, one-swap-per-unit-time path with zero auxiliary support at both endpoints. No operational system or instantaneous transition is authorized. Classical prior art: the McShane–Whitney Lipschitz envelope (search extracts, not full literature survey), e.g. https://www.academia.edu/66894320/Learning_over_compact_metric_spaces ; https://homepages.uc.edu/~shanmun/book.pdf . The envelope formula itself is standard; no novelty claim.

## General finite-horizon schedule
Let z_i>=0 be known deterministic required support at unit-spaced states i=0..k, z_0=z_k=0. Choose w_i>=z_i, w_0=w_k=0 and |w_(i+1)-w_i|<=rho. Fixed direction, no delay besides ramp, no switching penalty, no intra-step physics. Pointwise least possible ramp-limited majorant is
w_i*=max_(0<=j<=k)(z_j-rho*|i-j|).
Any feasible w dominates this by chaining the ramp inequality. The max of rho-Lipschitz functions is rho-Lipschitz, and the j=i term implies w*>=z. Consequently feasibility with zero endpoints holds iff w*_0=w*_k=0, equivalently rho>=rho0=max_(1<=i<k) z_i/min(i,k-i). Tracking without extra support holds iff rho>=rho1=max_i |z_(i+1)-z_i|. When feasible, w* minimizes cumulative sum and every nonnegative weighted sum of per-state support, with max w*=max z. The latter follows since each envelope term <=max z and the peak's own term attains it. Two forward/backward max passes compute this envelope in O(k) arithmetic operations; no bit-complexity claim. Unlike arbitrary fixed paths, the R31 minimum-length path attains each layer minimum, and any other k-step path visits layers 0..k in order. Thus it also attains the best envelope among all k-step paths in that family. Longer paths, preparation before the start, waits and arbitrary deadlines not optimized.

## R31 family and asymptotics
Use q=k-1, e=1/(8*k*q^3). The R31 layer minima are
z_n=max(0,[min(n,k-n)^2/(4q^2)-kne+n^2e^2]/[k-ne]).
The minimum-length path attaining them is the one proved in R31. For t=n/k write k*z_n as the sample of
max(0,[(k/q)^2*min(t,1-t)^2/4-k^2*t*e+k^2*t^2*e^2]/[1-t*e]).
This converges uniformly to phi(t)=min(t,1-t)^2/4. The piecewise smooth unclipped expression has derivatives converging uniformly to those of phi on each half-interval; clipping at zero is nonexpansive, and away from endpoints does not affect the derivative for sufficiently large k. Hence k^2*rho1->1/4 by an upper derivative bound and a lower difference adjacent to the midpoint on one side. For rho0, use z_n<=min(n,k-n)^2/[4q^2*(k-ke)] and the midpoint for matching lower bound, giving k^2*rho0->1/8. Thus the minimum rate for on-time completion is asymptotically half the tracking rate.

For feasible sequences rho with k^2*rho->c>=1/8, the scaled envelope converges uniformly on the sampled grid to psi_c(t)=sup_(s in [0,1])(phi(s)-c*|t-s|). This follows by uniform convergence of k*z, convergence of c and dense-grid approximation of a uniformly Lipschitz continuous function. On either half interval phi is convex, so each segment split at t and 1/2 has its maximum at an endpoint. Therefore psi_c=max(phi(t),1/16-c*|t-1/2|,0). For c>=1/4, psi=phi. For 1/8<=c<=1/4 the middle cone dominates on [4c-1/2,3/2-4c]; integrate the difference over both halves to get
lim sum_i w_i*=1/48 + (1-4c)^3/12.
For c>=1/4 the limit is 1/48. At c=1/8 (e.g. rho=rho0 for each finite k), the limit is 1/32, 1.5 times the unconstrained 1/48. Peak remains unchanged. These are normalized asymptotic rate limits, not physical time estimates. In particular setting exactly c=1/8 at finite k need not be feasible; use the exact rho0 formula.

## Actual execution
Local python3 -I /mnt/data/toto-r32/probe.py executed with captured stdout. Standard library only. 128 family sizes k=2..129; six rational rates each, 768 exact checks comparing linear-time envelope with direct maximum, ramp constraints, peak, endpoint feasibility and tracking. Independent bounded brute-force integer schedules for 625 instances (three interior requirements 0..4, five rates, all 125 integer schedules each); verifies feasibility and min sum. All assertions passed. Printed scaled thresholds and sums use ordinary float conversion from exact rationals. No independent human review. Local Git blobs script 1463a477d35f2fe493bc4f35bc6e390d5bf9202a, stdout 33ea5c2a6ece34772e46681a992ba78fad949aa1. Unused external physical data: none. No noisy demand prediction, real actuator, cost, energy, or organizational experiment.

## Margin
Available peak and delivery rate differ. The slowest feasible ramp requires anticipatory support and extra cumulative use, even without increasing the peak. Anticipation here relies on a known deterministic future demand; it does not prove prediction accuracy. Next investigate uncertain demand, asymmetric ramp rates, or how much lead time compensates for a slower rate. Research only.
