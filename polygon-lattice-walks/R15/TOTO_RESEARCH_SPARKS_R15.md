# TOTO | دفتر الشرارات R15 — arithmetic norm spectrum of the octagon
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED + BOUNDED_PROXY. Classical algebraic number theory, model-specific application; originality and independent review unassessed.

## Retrieval and changed action
Read R14 (blob 17dfeaeb724dbfa2a9bc64120eb8fa486343e76d) and its [Library card](https://github.com/Sangaa/ARGO-Library/blob/973cf43df44f81019626bf22bf86f62d2a8fb902/cards/toto-phase-balanced-observation-20261127-r14.json), blob 3a8cf197c0637568df1170bc83eb94479f2382b2, SOURCE_ONLY. Direct retrieval, not CLI. R14 reorganized the mean into unit-orbit Bessel contributions. TOTO chooses to count these orbits via prime splitting instead of box truncation, while retaining direct enumeration as a control and distinguishing certified tails from numerical quadrature. No causal learning claim.

## Norm multiplicity theorem
Let K=Q(zeta_8), O=Z[zeta_8], u=sqrt(2)-1, lambda=1/u. R14's even lattice E is the ideal (1-zeta_8): evaluation at zeta=1 modulo 2 identifies O/(1-zeta) with F_2 and its kernel is the even coefficient sum. For nonzero w, N=|z(w)|^2|z'(w)|^2 is the positive integer field norm. Let r(N) count E elements of norm N modulo multiplication by powers of u (not modulo rotations).
Then r(N)=0 for odd N. For even N, r(N)=8*a_K(N), where a_K(N) counts integral ideals of absolute norm N. In terms of rational prime exponents e:
- p=2 contributes 1;
- p=1 mod 8 contributes binom(e+3,3);
- p=3,5,7 mod 8 contributes e/2+1 when e is even, and 0 otherwise.
Multiply the factors and then multiply by 8. The mod-8 rule is a standard cyclotomic splitting law, not a new prime distribution theorem.

## Proof
Standard cyclotomic ring-of-integers and splitting theorems: https://openmaths.org/courses/NT-ANT/cyclotomic-fields.html and https://encyclopediaofmath.org/wiki/Cyclotomic_field (search excerpts checked). O has discriminant 256, by the discriminant of x^4+1 in its integral power basis. The Minkowski bound for degree 4 with two complex places is 24/pi^2<3, so every ideal class has an integral representative of norm 1 or 2. The sole ideal of norm 2 is (1-zeta), since x^4+1=(x+1)^4 mod 2 and Norm(1-zeta)=2. Thus class number is 1. All nonzero ideals are principal.

For a unit v, v*bar(v) is a totally positive unit of the real quadratic subfield Q(sqrt(2)), with norm 1 and integral coefficients a+b sqrt(2). Its positive value can be scaled by lambda^(-2j) into [1,lambda^2). The conjugate is its reciprocal. Therefore the rational part a=(x+1/x)/2 is an integer in [1,3), and a^2-2b^2=1 forces a=1, b=0. Hence v*bar(v)=lambda^(2j). Both complex embeddings of v/lambda^j have modulus 1. The norm identity from R12 gives sum of the squares of its four integer coordinates equal to 1. Consequently v/lambda^j is one of the eight signed basis vectors, precisely mu_8. The full unit group is mu_8 times <u>, and these factors intersect trivially. Each principal ideal has exactly eight classes of generators modulo <u>. The unique prime over 2 is (1-zeta), with norm 2; a generator belongs to E iff its ideal norm is even. This proves r(N)=8*a_K(N) for even N.

For odd p the residue degree is ord_8(p); 1 gives degree 1 and four primes, all other odd residues give degree 2 and two primes. Counting nonnegative exponents for the prime ideals gives the stated factors. For 2 there is only one prime of degree 1, hence one choice at every exponent. Unique ideal factorization gives multiplicativity of a_K, not of r itself.

## Direct enumeration control
For a nonzero orbit choose the unique R14 representative 1<=|z|/|z'|<lambda^2. With A=sum k_i^2, B=a(b-d)+c(b+d), this is exactly B>=0, 3B<2A: square the ratio and use lambda^4=17+12sqrt(2). N=A^2-2B^2 and the representative condition imply A<3 sqrt(N). Hence all representatives with N<=cap lie in the finite box |k_i|<=floor(sqrt(3 sqrt(cap))). This is a completeness argument, not an empirical truncation. The script scans this box independently of the prime formula.

## Bessel spectrum and certified norm tail
R14 yields the exact identity
M=1+8/log(lambda) * sum_(N even, N>=2) a_K(N) K_0(sqrt(N)).
For an upper tail bound, K_0(x)=integral_0^infinity exp(-x cosh(t))dt <= exp(-x)*sqrt(pi/(2x)) by cosh(t)>=1+t^2/2. Since a_K(N)<=d_4(N)<=N^3 (ordered quadruples of positive integer factors; first three determine the fourth), r(N)<=8*N^3. Use log(lambda)>1/2 and sqrt(pi/2)<2. For j>=100 group j^2<=N<(j+1)^2. The total normalized contribution in a block is <=96*(j+1)^7*exp(-j), including all integers as an upper bound. Consecutive block bounds have ratio <1/2, using e>8/3 and the integer inequality in the script. Thus the omitted tail after N=10000 is bounded above by 192*101^7/2^100. It is <1e-12. This certifies only the omitted norm tail, NOT the finite sum's numerical quadrature or roundoff.

## Actual execution
Local python3 -I probe.py, standard library only. [Code](probe.py), [actual stdout](probe.log). Exhaustive box radius 11 for cap 2000; 279841 scanned vectors, 2000 integer norm comparisons including zero classes, 141 nonempty norm classes, 4296 representatives, all matched. The factorization-based numerical Bessel mean at caps 100,400,1600,10000 agrees at the displayed digits with R14's proxy at the largest cap. Simpson integration on [0,8], 1024 panels; no certified quadrature or rounding error, so decimals remain BOUNDED_PROXY. First script used a floating constant 8/3 in an assertion of the tail ratio; replaced with equivalent exact integer inequality before publication, reran, stdout unchanged. Git hashes 71decb22bb158b2d9e1ff0cf4d0d95957bc56654 and 32630885a9dfcfa972a92a9482f39317a77cbd0f. No independent review, physical experiment, finite-time result or full novelty assessment.

## Margin
- Prime splitting determines degeneracy of this phase-averaged Bessel spectrum, not the whole phase-sensitive response.
- For comparison, the regular dodecagon has another degree-four cyclotomic field and different ramification and residue classes; its actual parity lattice and unit action must be derived afresh.
- Possible link to Dirichlet L-functions and Mellin transforms: the spectrum is the even-norm part of a Dedekind zeta series. Do not mistake an established arithmetic identity for novel physical evidence.
