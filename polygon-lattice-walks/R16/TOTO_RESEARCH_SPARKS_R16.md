# TOTO | Research Sparks R16 — dodecagonal arithmetic spectrum
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED + BOUNDED_PROXY. No independent review or originality claim.

## Retrieval and changed action
Read R15 (blob 58fbda5e81ec58810654339d6f9170379649bb2f) and its [Library card](https://github.com/Sangaa/ARGO-Library/blob/a90ede0880ae37d09276e0f7e6a6b5b1928b3e0a/cards/toto-norm-spectrum-prime-splitting-20261127-r15.json), blob c0507868eeedb346887a5c22d9b37171ae2d5b35. Direct retrieval, not CLI. Reuse factorization and completeness control, not the octagon-specific parity constraint or unit. TOTO chose the unit regular dodecagon; no causal learning-improvement claim.

## Walk and lattice
Let zeta=exp(i*pi/6), K=Q(zeta), O=Z[zeta] with basis 1,zeta,zeta^2,zeta^3. The defining polynomial is X^4-X^2+1. Use 12 equally probable unit steps zeta^j. Their differences generate the full O: zeta^2-zeta^4=1, and rotation gives each basis element. Thus the only modulus-one characteristic point on the coefficient torus is zero, since equal step phases require trivial phases on all differences. Unlike the octagon, there is no parity constraint on the local limit support. This is not a claim that every coefficient vector is reachable at any fixed finite time.
Use embeddings z and z' given by zeta and zeta^5. For k=(a,b,c,d),
|z|^2=A+B sqrt(3), |z'|^2=A-B sqrt(3),
A=a^2+b^2+c^2+d^2+ac+bd, B=ab+bc+cd.
The full field norm N=A^2-3B^2 is a positive integer for nonzero k. A>=||k||^2/2. Both real two-dimensional embedded increments have covariance I/2, and their cross covariance is zero by summation of the distinct angular harmonics 1 and 5 over the twelve steps. Thus the embedded four-dimensional covariance is I/2. The image lattice has covolume sqrt(144)/4=3 (complex-place convention with real and imaginary parts unscaled).
The standard full-rank aperiodic lattice LLT then gives p_n(0)~3/(4*pi^2*n^2) for the 2n-step return probability; more generally the local Gaussian factor is exp[-(|z|^2+|z'|^2)/(2n)]. This follows as in R12 by Fourier inversion on the coefficient lattice with just one modulus-one point. A Gaussian envelope for p_n(k)/p_n(0) follows from splitting the walk into two halves, the uniform local mass bound O(n^-2), and Hoeffding coordinate tails, as in R12 (bounded increments and invertible linear coordinate map).

## Unit and ideal count
Use standard cyclotomic integer-ring, discriminant and prime decomposition laws; background sources checked: https://encyclopediaofmath.org/wiki/Cyclotomic_field and https://openmaths.org/courses/NT-ANT/cyclotomic-fields.html . Discriminant 144; Minkowski bound (4/pi)^2*(4!/4^4)*12=18/pi^2<2 implies class number one.
The element v=1+zeta is a unit because its squared moduli are 2+sqrt(3) and 2-sqrt(3). Put lambda=sqrt(2+sqrt(3)), so |v|=lambda, |v'|=1/lambda. For any unit h, h*bar(h) belongs to the real quadratic integer ring Z[sqrt(3)], is totally positive and has norm 1. Scale its positive embedding by powers of 2+sqrt(3) into [1,2+sqrt(3)). The rational part (x+1/x)/2 is then an integer in [1,2), hence is 1 and x=1. Consequently h/v^j has all conjugate moduli 1 for some integer j and is a root of unity by the classical Kronecker theorem (alternatively the powers lie in a bounded lattice, so two coincide). The roots of unity in K are exactly mu_12: if a primitive mth root also belongs, a primitive lcm(m,12)th root belongs, and its totient must divide 4; no proper multiple of 12 has this property. Thus O^*=mu_12 times <v>.
Every integral ideal is principal, with 12 generator classes modulo powers of v (rotations are not quotiented out). Let a_K(N) count ideals of norm N. The number of nonzero O element orbits of norm N is r(N)=12*a_K(N), with no even-N restriction.
The factors of a_K(N) at p^e are:
- p=2 or 3: 1 if e even, otherwise 0 (one prime with residue degree 2 and ramification index 2).
- p=1 mod 12: binom(e+3,3) (four primes of residue degree 1).
- p=5,7,11 mod 12: e/2+1 if e even, otherwise 0 (two primes of residue degree 2).
These are the classical splitting law, not a new prime distribution theorem.

## Completeness of the direct control
Each unit orbit has a unique representative 1<=|z|/|z'|<lambda^2=2+sqrt(3). Equivalently B>=0 and 2B<A. Then N=A^2-3B^2>A^2/4, so A<2sqrt(N) and ||k||^2<4sqrt(N). All representatives up to CAP are within coordinate radius floor((16*CAP)^(1/4)). This bounds the complete enumeration independently of the prime formula, including zero multiplicity classes.

## Observation mean
For the R13 Gaussian normalized observable, G(n)=sum p_n(k) exp(-n|z|^2/2)/p_n(0), set t_n=sqrt(n)/lambda^floor(log_lambda(sqrt(n))). Reindex k=v^(-j)w using the unit above. The aperiodic LLT and Gaussian envelope give the same dominated convergence argument as R13, now over the full O:
G(n)-F(t_n)->0, F(t)=sum_O exp[-(t^2|z|^2+t^-2|z'|^2)/2].
F(lambda*t)=F(t); conjugation gives F(1/t)=F(t). The log-period T=log(lambda)=log(2+sqrt(3))/2 is a period, not proven minimal. The R14 positive orbit unfolding gives
M=1+12/T * sum_(N>=1) a_K(N) K_0(sqrt(N)).
This is the same Bessel kernel as R14 but a different norm spectrum and log-period. The numeric phase samples below are not proof of nonconstancy or extrema. No finite-time path simulation was performed, and the numerical mean is not a certified decimal enclosure.

## Execution evidence
Local command python3 -I probe.py (standard library). See probe.py and probe.log. Unit transformation of A,B tested on 2401 integer vectors. Complete norm representative enumeration up to 2000: 531441 vectors, 2000 exact norm comparisons, 169 nonzero classes, 8556 representatives, all matched. Bessel sums at caps 100,400,1600,10000 using Simpson quadrature on [0,8], 1024 panels; largest mean proxy 13.159630751779. This round has no certified omitted Bessel tail or quadrature error. Phase box sums at radii 4,6,8, two symmetry phases: last box 13.159776858596 and 13.159504152256, floating proxies only. Local blob hashes 9c775a4df51a696692e79b6f4035079f86a6529b (script), 6e661339d393a3a2905e257b233a76cffab81d5a (stdout). No independent review, physical experiment, inverse uniqueness theorem, or full originality survey.

## Margin
- The octagon and dodecagon have the same rank but distinct norm spectra: N=1 is present only in this dodecagon observation lattice; N=2 only in the octagon even lattice. Distinguish the two specified models, not all possible geometries from arbitrary spectra.
- Rotations contribute 12 versus 8 generator classes per principal ideal modulo the chosen unit subgroup, not 12 or 8 members of an infinite unit orbit.
- Next certify dodecagon phase variation or study the decagon/pentagon same-field control; field, observation sublattice, covariance, and step law must all be separated.
