# TOTO | دفتر الشرارات R02 — إخفاء مركب: العزوم والدوائر
26 November 2026 · SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
Derived and locally executed; originality unassessed; no independent review.

## Spark
Revisit two ideas that previously did not identify the generator: moment measurements and cyclic projections. Instead of asking whether a naturally occurring rival exists, design a rival in the joint kernel. The owner requested reconsideration of old unsuccessful ideas; the choice of this construction is TOTO's.

Source anchors: [R01](../R01/TOTO_RESEARCH_SPARKS_R01.md), [S03](../../spectral/S03_IDENTIFIABILITY_2026-11-26.md), cyclic Pascal/roots-of-unity filter from R34–R39 in the earlier research. No inference about the owner's undisclosed goal.

## Derived theorem: sharp finite-window criterion
Let P_s(z)=2^(-s)(1+z)^s, s>=1; rivals Q have nonnegative weights, mass one, supported on integer positions -1,...,s+1. Let d>=2 be even. Choose a finite nonempty set M of integer moduli >=2. Require raw moments 0,...,d-1 and all residue-class masses for each m in M to agree with P_s.

Define T={k>=2: k divides at least one m in M}, and
H(z)=(1-z)^d product_{k in T} Phi_k(z),
D=d+sum_{k in T} phi(k).
Phi_k is the kth cyclotomic polynomial.

Claim: a distinct rival exists in this window iff D<=s+2.

Necessity: A(z)=z(Q(z)-P_s(z)) is an ordinary polynomial of degree at most s+2. Matching raw moments gives a root of multiplicity at least d at z=1 (Euler derivatives and ordinary derivatives are triangularly related). Matching residue masses is equivalent to divisibility by z^m-1, since the remainder folds coefficients by residue. Multiplication by z merely shifts residues. Over R the required factors are coprime after excluding repeated factors, hence H divides A. If D>s+2 then A=0.

Sufficiency: set h=z^(-1)H(z)(1+z)^(s+2-D). Its outer coefficients are both +1 (d even, Phi_k monic with constant one for k>1), so all negative coefficients are interior, where P_s is strictly positive. h(1)=0 and h is nonzero, hence there are negative coefficients. Choose epsilon>0 strictly below min P_s(x)/(-h_x) over negative coefficients. Q=P_s+epsilon h is strictly positive on the window, normalized, distinct and symmetric about s/2 because the even difference power and cyclotomic factors are reciprocal. Both sets of observations match exactly. This proves existence and the degree obstruction without a numerical search.

The first differing raw moment is d: its difference equals epsilon*d!*product_{k in T}Phi_k(1)*2^(s+2-D)>0. All claims concern this specified finite window and even d, not arbitrary unbounded support, odd d, or unknown coordinates.

## Persistent hiding under evolution
For every n>=1, Q^n-P_s^n is divisible by Q-P_s in the Laurent polynomial ring. Therefore both observations remain identical after every number of iid convolution steps. The first differing raw moment grows by a factor n because the other factor in the power difference evaluates to n at z=1. This is an exact algebraic statement, not a physical experiment.

## Worked example
d=4, M={3,5}, D=10, s=8.
H=(1-z)^4 Phi_3 Phi_5=(1-z)^2(1-z^3)(1-z^5).
epsilon=1/1024.
Q weights on -1,...,9 are (1,2,33,111,226,278,226,111,33,2,1)/1024.
P and Q agree in raw moments 0..3 and all residue masses modulo 3 and 5. Fourth moment difference is 45/128; mod 7 distinguishes the one-step distributions. No claim that mod 7 distinguishes them at every n.
Moduli overlap in their factors: observing mod 2 and mod 4 costs no more degree than mod 4 alone. For distinct prime moduli the extra degree is the sum of p-1. Observation redundancy, not merely number of sensors, determines this algebraic threshold.

## Executed certificate
WHAT: construct rivals, verify positivity, mass, distinctness, exact moments, folds, first different moment sign, and selected convolution powers.
SCOPE: every 1-, 2-, or 3-element subset of moduli 2..8; d in {2,4,6}; s in {D-2,D-1,D}. Example convolution powers n=1..6.
METHOD: Python 3 isolated mode, Fraction, exact polynomial arithmetic, no external dependencies. Command: python3 -I probe.py.
EVIDENCE: [probe.py](probe.py), [probe.log](probe.log), actual stdout: 567 rivals, 2268 moment comparisons, 1386 residue-vector comparisons, 6 convolution steps. All assertions passed. Degree impossibility is algebraic; no separate exhaustive search for rivals below threshold was run. 
LIMITATION: author-run bounded checks, not blind or independent; no noise, no physical measurements, no external literature comparison. EVIDENCE CLASS: DERIVED + MEASURED.

## Margin scribbles
- A sensor is a quotient; a family of sensors is an intersection of kernels.
- Can the least common multiple of observation polynomials guide sensor selection?
- Finite support is a hypothesis, not a measurement. Remove it and seek a new obstruction.
- Degree cost versus noise stability: exact identification is not stable identification.
- Old failures are reusable tools. Do not force an interpretation in physics.
- Next possible play: multivariate lattice projections or an unbounded-support counterexample. Not a commitment.
