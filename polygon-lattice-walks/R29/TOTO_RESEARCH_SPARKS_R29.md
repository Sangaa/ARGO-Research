# TOTO | R29 — Batch-radius dependence of the R28 transition barrier
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED exact integer controls; displayed decimal ratios are BOUNDED_PROXY. No originality or independent-review claim.

## Retrieval and choice
Read R28 on live main 6bfee0e0a80fdc2609b7bb3b016f1802d060239f, blob 31758c916e4c3bc4678c77286a652e013cc43fa1. TOTO extends only its mathematical exchange graph from single replacements to bounded batches. The owner jokingly warned against instantaneous transition systems; no operational transition system is designed or authorized. Only this research lane is changed. Prior art on bottleneck paths: https://link.springer.com/article/10.1007/s10994-022-06270-0 (search excerpt inspected). No causal learning claim or comprehensive originality survey.

## Model
q>=1, k=q+1, e=1/(8*k*q^3), j in {0,1}, 0<=l<=q. As R28, f(j,l)=(k/2-(j+l)e)^2+(jq-l)^2/(4q^2); start (0,0), optimum (1,q), E=beta+k-sqrt(f). Final gain G=ke. Allow at most p distinct identity replacements in a step, 1<=p<=k. Observe only discrete states before/after each batch, not intermediate physical execution. The minimum exchange distance between count states is (|dj|+|dl|+|dj+dl|)/2, by balancing counts of the a,b,c types. Every edge is realizable from any selection with those starting counts. Define F_p as minimum over all allowed paths of maximum f, including endpoints. B_p=sqrt(F_p)-k/2.

## Closed form and proof
Put n=k-p, m=floor(n/2). Then
F_p=f(0,m) when n is even; F_p=f(1,m+p-1) when n is odd.
For p=k this is f(0,0), directly attained. For p<k, f(0,l) increases and f(1,l) decreases in l, as proved in R28. Every path must cross from j=0 to j=1. For departure (0,l), the largest attainable arrival index is L=min(q,l+p-1), so its minimum possible crossing peak is max(f(0,l),f(1,L)). Every such crossing can be reached and exited by single swaps staying below this peak, using row monotonicity. Therefore minimize that maximum over integer l=0..q; no monotone-path assumption needed for the lower bound.
If n=2m>0, l=m gives vertical magnitudes equal to m/(2q) on both sides; the arrival has smaller horizontal component, so peak=f(0,m). For l>=m the departure is at least this value. For l<m the arrival is at least f(1,m+p-2), whose vertical square exceeds the candidate by (2m+1)/(4q^2); its horizontal square can be smaller by at most k(p-1)e <=1/(8q^2). Hence the candidate is optimal.
If n=2m+1, l=m has arrival vertical magnitude (m+1)/(2q) versus m/(2q) at departure. The difference of vertical squares n/(4q^2) exceeds the possible horizontal decrease kp e <=1/(8q^2); peak=f(1,m+p-1). For l<=m the arrival is no smaller. For l>=m+1 departure >=f(0,m+1), with same vertical square as the candidate and horizontal component no smaller (p>=1). Thus this peak is optimal. R28 is recovered at p=1 (odd case equal to f(0,m+1)). This proof uses actual batch distance and includes paths that backtrack.

## Threshold for loss no greater than gain
For p<k, the strict trap of R27 implies B_p>0. For p=k, B_p=0. For q>=3, B_p<=G iff p>=q=k-1. Proof: at p=q, n=1, F_p-k^2/4=1/(8q^2)+q^2 e^2 <= k^2 e+k^2 e^2, the squared increment corresponding to B=G. At p=q-1, n=2, F_p-k^2/4=(2q-1)/(8q^3)+e^2. Subtract k^2 e+k^2 e^2 to obtain (q-2)/(8q^3)-(k^2-1)e^2>0 for q>=3. The barrier is nonincreasing in p by edge inclusion, proving the threshold. The two smaller q are not included in this threshold theorem.

## Scaling
For p/k tending to alpha with 0<=alpha<1 as q grows, F_p-k^2/4 tends to (1-alpha)^2/16, and B_p/G is asymptotic to (1-alpha)^2 q^2/2. If instead the deficit n=k-p is a fixed positive integer, the ratio tends to 2 ceil(n/2)^2 - (1 if n odd else 0). Derive by expanding F_p-k^2/4=ceil(n/2)^2/(4q^2)-k a e+a^2 e^2 with a=m for even n, a=m+p for odd n, and rationalizing the radical. The limit is parity-dependent because of discrete crossing positions. These results are properties of the R27 family and endpoint-only batch model, not general optimal batch sizes, monetary costs or safety thresholds.

## Actual execution
Local python3 -I /mnt/data/toto-r29/probe.py with stdout captured by tee. Standard library only. Scale f by D^2 where D=8*k*q^3, so scores are exact integers. For q=1..64 and every p=1..k, check connectivity at predicted threshold and disconnection one integer unit below, monotone barrier in p, zero barrier only at p=k, and B<=G threshold for q>=3. 2144 cases, 4288 connectivity checks. Additional 14 uncompressed identity graph cases for q=1..4, all p, 28 connectivity checks with exact identity difference metric. All assertions passed. Displayed ratios are ordinary float evaluations of exact barriers with rationalized radical difference, not certified decimal intervals. Actual blobs probe.py 2d0e0618398f9434d550c193c1e1b6fb9428d5f1 and probe.log 3318257fc1aab7491cfcdca1ede15ad60e58dc81. No physical, economic, organizational or independent validation.

## Margin
A large allowed batch radius may still leave a large barrier relative to a tiny endpoint gain. Parity effects are a reminder that continuous approximations can miss small discrete thresholds. Next explore whether an alternative intermediate state outside the fixed-cardinality model (e.g. a temporary reference) changes the conclusion, or whether the objective gap can be certified cheaply before seeking an escape. This is a research question only; no operational recommendation.
