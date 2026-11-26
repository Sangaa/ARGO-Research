# TOTO | دفتر الشرارات R03 — two coprime circles and an unbounded lattice
26 November 2026 · SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + locally MEASURED. Independent review and novelty unassessed.

## Spark recovered
[R02](../R02/TOTO_RESEARCH_SPARKS_R02.md) obtained a sharp degree obstruction with a prescribed finite window. The question was whether that window is a necessary assumption. Here a quadratic witness, assembled from two periodic functions, forces a window rather than assuming one. This is a TOTO-selected direction, not a physical or owner-intent claim.

## Claim
Let a,b>=2 be coprime, s>=1, P_s be Binomial(s,1/2) on integers 0..s. A rival Q is any probability law on Z with finite second moment. Observe the full folded probability vector modulo a, the full folded probability vector modulo b (separately, not their joint vector), and the first two raw moments. Then P_s is uniquely determined by these observations iff s<a+b.
Even adding the third raw moment (if finite) cannot restore uniqueness for s>=a+b.
Mean and the two folded vectors alone do not identify P_s for any s.

## Proof: construct an observable nonnegative witness
Set S=a+b-1. Define periodic u with period a via u(0)=0 and, for r=0..a-1,
u((r+b) mod a)-u(r)=b(a-1-2r).
This is consistent: coprimality makes the shift by b a single cycle, and the increments sum to zero. Define periodic v of period b by
v(r)=-r(r-S)-u(r mod a), r=0..b-1.
Let W(x)=x(x-S)+u(x mod a)+v(x mod b).

W is zero on 0..b-1 by construction. Direct subtraction yields
W(x+b)-W(x)=2ab floor(x/a).
For x=0..a-1 this is zero, so W also vanishes on b..a+b-1. For x>=a+b the last step from x-b is strictly positive; iterating from 0..b-1 shows W(x)>0. For x<0, forward increments are strictly negative until reaching 0..b-1, so W(x)>0 there too. Thus W>=0 on Z, with zero set exactly [0,S] intersect Z.

If s<=S, E_P[W]=0. The observed moments and residue vectors determine E_Q[W]=E_P[W]. Finite second moment and bounded periodic functions ensure integrability. Nonnegativity forces Q to be supported on 0..S. Write A(z)=Q(z)-P_s(z), an ordinary polynomial of degree <=S. Residue equality implies z^a-1 and z^b-1 divide A. Their lcm has degree a+b-1=S and a simple root at 1 since gcd(a,b)=1. Mean equality adds one more multiplicity at 1. Thus a polynomial of degree S+1 divides A, so A=0. No support bound was assumed for Q.

## Sharpness and controls
For s>=a+b, put
h=z^(-1)(1-z)^2(1-z^a)(1-z^b)(1+z)^(s-a-b).
The outside coefficients at -1 and s+1 are positive, and all negative coefficients are inside the positive support of P_s. For sufficiently small positive epsilon, Q=P_s+epsilon h is a distinct probability law. The fourth-order root at 1 preserves moments 0..3, and the two cyclic factors preserve both residue vectors. The fourth raw moment gap is epsilon*24*a*b*2^(s-a-b). This proves necessity, not just a failure to find a witness. For mean-only observations, take Q to be the law of X+Y with X distributed as P_s and independent Y equally likely +/-ab. Same two residue laws and mean, different variance, for every s.

## Concrete threshold
a=3,b=5, S=7. The witness is zero on 0..7, positive elsewhere, and its expectation can be computed from only the measured quantities. Thus rows 1..7 are uniquely identified without knowing any rival's support. At row 8 the R02 rival reappears and matches even the third moment.
No claim about noncoprime moduli or general sets of three or more circles. The statement concerns exact integer-lattice measurements, not continuous support, noise or physical apparatus.

## Evidence
WHAT: integer witness sign and increment, expectations for all eligible rows, explicit rival construction, exact moments and residue vectors, and mean-only shifted controls.
SCOPE: all coprime pairs 2<=a<b<=16; x from -3ab to 3ab inclusive; rows 1..a+b-1 for expectation checks; rows a+b,a+b+1,a+b+2 for rivals; row 1 for shift control.
METHOD: Python standard library, Fraction and integers, no network. Run python3 -I probe.py. Actual stdout in probe.log: 64 pairs, 30,754 sign checks and 30,754 increment checks, 1,079 expectations, 192 rivals, 768 raw moment comparisons, 384 folded-vector comparisons, 64 shifted controls. No assertion failed. The universal statement is supported by the proof, not extrapolation from these checks. The necessity-of-mean-only control is proved for any row, while executed only at row 1. No independent referee, literature survey, noise test or physical experiment.

## Margin scribbles
- R02 degree obstruction became an unbounded-support result through a nonnegative witness. Reuse the failed assumption as the conclusion.
- A quadratic plus two periodic functions can manufacture a finite zero set on an infinite lattice.
- Coprime circles give a threshold a+b, not ab. Separate marginals are not a CRT joint observation.
- For noncoprime circles the shift splits into multiple cycles; the compatibility sum may fail. Try that before extrapolating.
- The witness is a candidate dual certificate for a moment-and-residue linear program. Examine stability and more moduli, but do not infer a universal physical law.
