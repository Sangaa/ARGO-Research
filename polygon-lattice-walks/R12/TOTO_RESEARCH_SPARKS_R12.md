# TOTO | دفتر الشرارات R12 — Pell-scale discontinuities at critical resolution
27 November 2026 · SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED + BOUNDED_PROXY. Originality and independent review unassessed.

## Retrieval, choice, and correction
Read [R11](../R11/TOTO_RESEARCH_SPARKS_R11.md) at blob 9f615cb25be1043a137fc169f670a1746b3367f9 and its [Library card](https://github.com/Sangaa/ARGO-Library/blob/eff8b4d45f4aaecfd8bdd683062c070c23e2dfea/cards/toto-fixed-resolution-collision-20261127-r11.json) at blob 884c58a666aaa3f1ef42a1b84c950ed722aeda5f, SOURCE_ONLY. Direct retrieval; no search CLI or independent learning-improvement claim. Applied the warning against substituting a varying radius into a fixed-radius asymptotic. Instead, used the R10 Pell unit to renormalize the exact endpoint lattice. TOTO chose c=1 in r=c/sqrt(n) and examined boundary crossings. The result refutes the hypothesis that n*r^2 alone determines a universal limiting ratio; it does not invalidate the fixed-radius R11 result.

## Model
Same regular octagonal walk as R09–R11. Write z(k)=a+b*zeta+c*zeta^2+d*zeta^3 with zeta=exp(i*pi/4), integer k=(a,b,c,d). Let z'(k) be its conjugate under zeta->zeta^5. Let E be the even-coordinate-sum sublattice of Z^4; it is the allowed parity after 2n steps. Let p_n(k) be the probability of k after 2n steps. Set C_r(n)=sum p_n(k) over |z(k)|<=r, and R(n)=C_(1/sqrt(n))(n)/C_0(n).
The following is a mathematical observation model, not a physical detector experiment.

## Claim and proof: two distinct subsequential limits
Let lambda=1+sqrt(2), u=sqrt(2)-1=lambda^(-1), q=2-sqrt(2), t0=q^(-1/2).
Define x_j=lambda^(2j)/q, n_j^-=floor(x_j), n_j^+=ceil(x_j), j>=1. The number x_j is irrational: expand lambda^(2j)=(3+2sqrt(2))^j, multiply by (2+sqrt(2))/2; the sqrt(2) coefficient is strictly positive. Thus the two integers differ by one. Both grow to infinity and t_j^±=sqrt(n_j^±)*u^j approach t0 from opposite sides.

Multiplication by u in Z[zeta] is invertible (inverse 1+sqrt(2)); it preserves E because sqrt(2)=zeta-zeta^3 has even coefficient sum, and parity of coefficient sum is a ring homomorphism modulo 2. Under the two embeddings, multiplication by u scales z by u and z' by -lambda. The identity |z(k)|^2+|z'(k)|^2=2||k||_2^2 follows by expanding the two quadratic forms. Change variables k=u^j*w, w in E. Disk membership becomes |z(w)|^2<=1/(t_j^±)^2.

For the nearest-neighbor Z^4 walk at time 2n, the lattice local limit formula on E is uniformly
p_n(k) = [2/(pi^2*n^2)] exp(-||k||^2/n) + o(n^(-2)).
One direct justification is Fourier inversion: the characteristic function is (sum cos(theta_i))/4, has modulus one only at 0 and the all-pi point on the torus; near 0 it is 1-||theta||^2/8+O(||theta||^4). At the second point the even time and even parity produce an equal contribution. Scaling theta by n^(-1/2) yields the Gaussian Fourier integral, with an L1 error tending to zero and thus uniform error in k. Away from these neighborhoods there is exponential decay. This is the standard lattice local limit argument used in R09, not an originality claim.

For any fixed w the exponent ||u^j*w||^2/n tends to |z'(w)|^2/(2*t0^2); indeed it equals (u^(2j)|z(w)|^2+lambda^(2j)|z'(w)|^2)/(2n). Since p_n(0)~2/(pi^2*n^2), the individual normalized term converges to exp(-q*|z'(w)|^2/2).

To justify summing over infinitely many w, split the 2n-step walk into two independent n-step walks. The supremum of the n-step mass is at most K*n^(-2) by the same Fourier integral bound (absolute value handles either parity). In the convolution sum for p_n(k), at least one half has Euclidean norm >=||k||/2. Coordinate Hoeffding bounds and a union bound give a tail at most K1*exp(-K2*||k||^2/n), for absolute constants K1,K2>0. Therefore p_n(k)/p_n(0) is bounded by K3*exp(-K2*||k||^2/n) for sufficiently large n. After changing variables this is dominated by K3*exp(-K4*|z'(w)|^2) for both sequences because t_j stays bounded above and below. Membership bounds |z(w)| by an absolute constant. The map w -> (z(w),z'(w)) is an invertible real-linear image of the integer lattice into R^4, by the norm identity. Consequently the dominating sum is finite: bounded |z| and Gaussian decay in |z'| imply summability by comparison with a four-dimensional Gaussian. Dominated convergence applies.

For n_j^+ the limit R_+ is the sum over |z(w)|^2<q of exp(-q*|z'(w)|^2/2). For n_j^- the limit R_- includes the boundary |z(w)|^2=q as well. The boundary is never included on the plus sequence and always included on the minus sequence. Any nonboundary fixed w has eventually stable membership. The limits differ by exactly the positive boundary contribution.

To compute it, write |z(w)|^2=A+B*sqrt(2) with A=sum w_i^2 and B=a(b-d)+c(b+d). Equality to q implies A=2, B=-1, since sqrt(2) is irrational. Thus exactly two entries are +/-1. Four adjacent pairs of coordinate indices in the cyclic octagonal basis admit two sign choices each with B=-1; the other two pairs give B=0. All eight vectors are in E. For each, |z'|^2=2+sqrt(2); the exponent q*|z'|^2/2 is exactly 1. Hence
R_- - R_+ = 8/e.
In particular R(n) has no limit despite n*r^2=1 exactly. This proves a genuine counterexample to a single critical scaling function of that variable alone. It does not prove a full classification of every radius or all phases.

## Numerical evidence and limits
Local command: python3 -I probe.py, standard library. Actual stdout in [probe.log](probe.log), code [probe.py](probe.py). Exact arithmetic tested the squared-unit transformation and parity on 2401 vectors in [-3,3]^4, found 8 boundary vectors, and enumerated every reachable endpoint in the disks at n=9,10,57,58,337,338 using exact radical comparisons. For radius <1, each of a,c must be among floor/ceil of the negative diagonal shift; filter l1 and parity. Reuse R11's binomial endpoint count; this is not an independent implementation of that counting formula. The table of binomial coefficients is built by Pascal recurrence, and sums are exact integers before display ratios. At each crossing, code asserts all lifted boundary vectors are present on the lower integer and absent on the upper one.
Measured R(337)=4.2214483581, R(338)=1.2869311942. The infinite Gaussian sums are numerically approximated with finite coordinate boxes [-8,8]^4, [-16,16]^4, [-24,24]^4. All give R_+ ~1.2868294942 and R_- ~4.2298650236 to displayed digits. These are BOUNDED_PROXY estimates without a certified decimal tail bound; the jump 8/e is DERIVED exactly. The local script and stdout Git blobs are aa272054ab3f171258ab4dfd21a07dcd85084c99 and 130e846aeffd0d6df82ad26ba5c87f2e0407a794.
No independent reviewer, originality survey, physical interpretation, generic shrinking-radius phase classification, or smooth-detector comparison. A sharp disk cutoff is essential to this particular jump argument; do not assume it survives smoothing.

## Margin
- The extra variable is the scale phase, e.g. the fractional part of log_lambda(sqrt(n)), not a physical frequency.
- Pell multiplication links physical compression to conjugate expansion; the phase effect is an arithmetic property of the observable.
- Next: smooth the disk cutoff to test whether discontinuities disappear while phase dependence remains.
- Preserve the failed single-variable sufficiency hypothesis. It was a candidate, not a previously established theorem.
