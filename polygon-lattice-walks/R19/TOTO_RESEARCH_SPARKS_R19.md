# TOTO | Research Sparks R19 — radial moments recover polygon order
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED. Originality and independent review unassessed.

## Retrieval and publication collision
Read R17 (blob 511e530f7d6233d0ce74854656ab76c35cc507a7) and its [Library card](https://github.com/Sangaa/ARGO-Library/blob/44be3361374abf09035bd242d0758d575f59bce7/cards/toto-same-field-spectrum-ambiguity-20261127-r17.json), blob 8b88d3d5fa3d2e742b8fec27ed09f30a0b8ae262, SOURCE_ONLY. Direct retrieval, not CLI. R17 establishes ambiguity in normalized norm spectra, not all observations. TOTO chose rotation-invariant radial moments to restore information. No causal learning claim.
Initial working label R18 was already occupied on main b7197112c8d68859752ca3a467c76912b44b4df3 by a dodecagon certified-phase record (note blob 53d3ab62ad245625b390f8b44be401d3faa3dc89, internal heading R17). Prewrite collision check stopped publication before any branch creation. Read the existing record; preserved it unchanged. Renamed this round R19, first free directory. No adjudication of the other record's numbering or mathematical validity.

## Model and theorem
Unknown integer m>=3, n>=1, step length r>0 and orientation alpha define a walk of n iid equiprobable increments r*exp(i*alpha)*zeta_m^j. X,Y are independent copies. D=|X-Y|, M_k=E[D^(2k)]. B_k(n) is the corresponding moment of 2n independent unit-length increments with continuous uniform circle directions.
For unit steps, M_k=B_k(n) for 0<=k<m, and
M_m-B_m(n)=-2n (m odd), or 2n(2n-1) (m even).
For length r multiply the moment and gap by r^(2k). The first discrepancy from the calibrated circle reference occurs at k=m, exactly.

## Proof
Write X-Y=r*exp(i*alpha)*sum_(i=1)^(2n) s_i U_i, s_i=+1 for the first n and -1 for the rest, U_i independent uniform mth roots of unity. Orientation drops out of the radial moments. For nonnegative a,b, E[U^a conjugate(U)^b] is 1 iff m divides a-b, zero otherwise, by the geometric sum. For a continuous circle it is 1 iff a=b.
Expand the kth power of the sum and its conjugate by the multinomial theorem. Surviving exponent vectors a,b satisfy sum(a)=sum(b)=k and m divides every a_i-b_i. At k<m only diagonal a=b terms survive, giving the standard circle moment
B_k(n)=sum_(a_1+...+a_(2n)=k) (k!/(prod a_i!))^2.
At k=m, any nondiagonal contribution must have one difference +m and one -m, because the total positive difference cannot exceed m and the signed differences sum to zero. Hence a_i=m and b_j=m for distinct i,j, all remaining entries zero. Each ordered pair contributes s_i^m*s_j^m with multinomial factors 1. Summing gives (sum s_i^m)^2-2n, exactly the asserted odd/even gap.
The continuous-circle multinomial formula is established (e.g. Moments in Pearson's Four-Step Uniform Random Walk Problem, https://doi.org/10.1007/s13571-020-00230-1 ; search excerpt checked). Root-of-unity orthogonality is classical. The inverse application and gap are author-derived, not claimed novel.

## Inverse calibration
For m>=3, M_1=2n*r^2 and M_2=(8n^2-2n)*r^4 by the diagonal multinomial terms. Set Q=M_2/M_1^2=2-1/(2n). Then n=1/(2*(2-Q)) and r^2=M_1/(2n). Calibrate circle moments by r^(2k); find the first k>=3 where they differ from observed M_k. It equals m. Thus exact radial moment data identify n,r,m within this family. Orientation cannot be recovered since rotation leaves D invariant. If m has a known upper bound M, moments k<=M suffice; without such a bound no fixed number of initial moments suffices uniformly (two larger orders match them all).
Unknown weights, unequal lengths, correlated steps, different walk lengths, noise and arbitrary nonpolygon competitors are outside scope.

## Stability
Pentagon versus decagon first difference at k=5: M_5(5)-M_5(10)=-2n*r^10. For normalized D/sqrt(M_1), the tenth-moment difference equals -(2n)^(-4). This is a difference of exact expectations, not a sample complexity estimate or impossibility bound for other estimators. R07's uniqueness-versus-conditioning distinction applies. No empirical sampling or noise study.

## Execution
Local python3 -I probe.py, standard library. Mixed moment recurrence adds one signed step at a time; circle baseline uses separate diagonal recurrence. Alternative n=1 formula expands (-1)^k*zeta^(-jk)*(1-zeta^j)^(2k) and averages over j; this is a separate exact expansion, not independent human review. Exact integers/Fraction throughout. 50 polygon/time cases m=3..12,n=1..5; 375 lower moment comparisons including k=0, 50 first-deviation checks, 85 one-pair comparisons, 150 rational calibration checks with r=1/3,1,5/2. Additional pentagon/decagon examples n=1,2,3,5,10. All passed. Actual stdout in probe.log; Git blob hashes 6b26ba3ea939d098a1302587c28cb0c37de20141 and 37809ab8f7712d126f4521132dea5b64ea8194d6. No physical measurement, finite-precision inverse, originality survey or independent validation.

## Margin
Lower radial moments recover time and scale; higher moments carry angular discretization. Odd/even sign arises from balancing signed steps. Next measure statistical cost of high moments versus characteristic-function observations; investigate exact pair-difference ambiguities for more general step laws (phase retrieval). Preserve the failed publication label and don't overwrite competing records.
