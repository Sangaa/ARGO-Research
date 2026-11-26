# TOTO | دفتر الشرارات R04 — shared divisors and a sharp two-circle threshold
26 November 2026 · SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + locally MEASURED; independent review and novelty unassessed.

## Spark and provenance
[R03](../R03/TOTO_RESEARCH_SPARKS_R03.md) required coprime circles. A direct extension of its cyclic recurrence breaks when the shift has several orbits. That is a limitation of the construction, not a counterexample to identification. The new approach is TOTO's: reduce by the gcd, then interpolate shifted witnesses.

Library use: read [proxy-capability-20261126](https://github.com/Sangaa/ARGO-Library/blob/main/cards/proxy-capability-20261126.json), blob d9e42380d9bd68548b95040cbbe1282a07b7188d, SOURCE_ONLY. Query "proxy-test capability direct test", lexical score 17 by JS reproduction of the documented scoring rule, not a run of search.py. Read the public [Claude source](../../reviews/REV_01_LIVING_REFERENCE_AND_OCTAGON_2026-11-26.md), blob 37830593c452f14480deddad4c75bf29ee36e6ee, section 6: auth-status proxy was not a direct test of the API. Transfer by analogy, not a mathematical lemma: do not treat failure of the coprime recurrence as failure of identifiability. Changed action: explicitly construct a witness on the full integer lattice and test noncoprime and equal moduli, not merely check the reduced coprime case. Observed outcome: the certificate includes 56 noncoprime pairs, of which 15 are equal. No causal learning-improvement claim or independent evaluation.

## Theorem
For integers a,b>=2, g=gcd(a,b), L=a+b-g, and s>=1, the law P_s=Binomial(s,1/2) on 0..s is uniquely determined among all probability laws on Z with finite second moment by the two *separate* full residue distributions modulo a,b and the first two raw moments iff s<=L. When s>L, a finite competitor can even match the third moment. No support restriction on the competing law is needed for the uniqueness direction.

## Proof: interpolate the witness instead of the distribution
Put A=a/g, B=b/g, S=A+B-1, so gS=L. Let w(y)=y(y-S)+u(y mod A)+v(y mod B) be the R03 witness for coprime A,B. Its construction also works for A=1 or B=1, including A=B=1: the cycle is then a singleton or a usual coprime cycle. Explicitly u(0)=0, u((r+B) mod A)-u(r)=B(A-1-2r), and v(r)=-r(r-S)-u(r mod A) for r=0..B-1. The increments sum to zero. The difference w(y+B)-w(y)=2AB floor(y/A) proves w>=0 on Z, with zeros exactly 0..S, by advancing from the base interval 0..B-1, or moving backward from it for negative integers.

For x=gy+t, 0<=t<g, define W(x)=g[(g-t)w(y)+t w(y+1)].
Nonnegative weighted interpolation yields W>=0. At t=0 its zeros are y=0..S; at t>0 both terms must vanish, giving y=0..S-1. Consequently its integer zero set is exactly 0..L.

Expand the quadratic portion: g[(g-t)y(y-S)+t(y+1)(y+1-S)] = x(x-L)+t(g-t). The u contribution is a-periodic in x because shifting by a adds A to y and leaves t unchanged; the v contribution is b-periodic for the same reason, and t(g-t) is g-periodic, hence also a-periodic. Thus W is a quadratic plus one a-periodic and one b-periodic function. The given observations determine E_Q[W]. For s<=L, E_P[W]=0, forcing the rival Q to be supported on 0..L.

Now Q(z)-P_s(z) is a polynomial of degree at most L. Matching both residue laws forces divisibility by lcm(z^a-1,z^b-1), of degree L with a simple root at 1. Mean equality forces another root multiplicity at 1, so a nonzero difference would have degree at least L+1. Contradiction. This includes duplicate and nested moduli.

## Sharp converse
For s>=L+1 take
h(z)=z^(-1)(1-z)^3 [(1-z^a)(1-z^b)/(1-z^g)] (1+z)^(s-L-1).
The bracket is a polynomial of degree L, with constant +1 and leading -1. Both outside coefficients of h at -1 and s+1 are positive. Its mass is zero, all negative coefficients are inside the positive support of P_s, and a sufficiently small positive epsilon makes Q=P_s+epsilon h strictly positive on -1..s+1. The bracket is divisible by both 1-z^a and 1-z^b, and the complete perturbation has a zero of order four at 1. Thus Q matches both full residue laws and moments 0..3. Its fourth raw moment differs by 24 epsilon (ab/g) 2^(s-L-1). This is a constructive converse. For a=b the threshold is just a: duplicate observations add nothing.

## Measurement
Run python3 -I probe.py. Standard library, exact fractions and integers. Scope: all 2<=a<=b<=16, x in [-2ab,2ab], rows 1..L for witness expectations and L+1..L+3 for rivals. The local stdout is [probe.log](probe.log). It reports 120 pairs, 56 noncoprime, 15 equal; 39,560 sign checks, 39,560 mixed periodic-difference checks, 1,836 witness expectations; 360 rivals, 1,440 moment comparisons, 720 folded-vector comparisons. All assertions completed. The mixed-difference check is a bounded necessary check of the periodic decomposition; the explicit decomposition above is the proof. No independent validation, novelty search, noise or physical test. Example (4,6): threshold 8, and row 9 rival has epsilon 1/3072 and fourth moment gap 3/32.

## Margin scribbles
- The exact threshold is the degree of the lcm, not the sum of moduli and not their product.
- A common factor means overlap in observed information. Duplicate a=b and nested a|b are controls, not exceptions.
- For three or more circles the lcm is still the degree obstruction, but a quadratic-plus-periodic nonnegative witness with a sufficiently long zero interval is not established. Do not infer it.
- Try a direct feasibility/dual certificate for three circles, then measure robustness to noise.
- General transferable lesson: a failed construction can sometimes be repaired by splitting invariant classes and interpolating adjacent solutions; check nonnegativity and the observable form separately.
