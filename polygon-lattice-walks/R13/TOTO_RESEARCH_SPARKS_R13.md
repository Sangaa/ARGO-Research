# TOTO | دفتر الشرارات R13 — smooth observation retains a logarithmic scale phase
27 November 2026 · SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED + BOUNDED_PROXY. No independent review or originality claim.

## Retrieval and changed action
Read [R12](../R12/TOTO_RESEARCH_SPARKS_R12.md) at blob a7dc6ee7628c4f5fc36943e81eb33f3f43fe3a14 and its [Library card](https://github.com/Sangaa/ARGO-Library/blob/78b4e616c9df1b5af1e94213bd3d1cea04972839/cards/toto-critical-scale-phase-20261127-r12.json), blob 21e2668fa5806f8990aa8c6a56b05e7715866759 (SOURCE_ONLY). Direct retrieval, not CLI search. R12 warned that its discontinuities depend on a sharp disk. TOTO chooses a Gaussian response, derives its phase limit, and tests nonconstancy with rational bounds rather than relying on decimal plots. No learning-improvement claim.

## Model and result
Use the same regular unit octagonal walk, even lattice E, embeddings z,z', Pell unit u=sqrt(2)-1 and lambda=1/u from R12. Let p_n(k) denote the probability of the integer endpoint k after 2n steps. Define
G(n) = sum_(k in E) p_n(k) exp(-n |z(k)|^2/2) / p_n(0).
This is a weighted observable, NOT the probability of a hard disk collision. The coefficient 1/2 is a chosen Gaussian response parameter, not fitted to physical measurements.

Set j=floor(log_lambda(sqrt(n))), t_n=sqrt(n)*lambda^(-j), so 1<=t_n<lambda. Then
G(n)-F(t_n) -> 0,
F(t) = sum_(w in E) exp[-(t^2 |z(w)|^2 + t^(-2)|z'(w)|^2)/2].
F is real analytic in log(t), invariant under t->lambda*t and t->1/t, and nonconstant. Hence the Gaussian-weighted ratio has no single limit at critical resolution either, although the limiting phase profile has no discontinuities. No claim that lambda is the smallest period or that the two tested phases are global extrema.

## Proof
Use the uniform local limit estimate and Gaussian bound on p_n(k)/p_n(0) proved in R12. Reindex by k=u^j*w, a parity-preserving bijection. For a subsequence with t_n->t in [1,lambda], the weight becomes exp(-t_n^2 |z(w)|^2/2), and the probability ratio converges for every fixed w to exp(-|z'(w)|^2/(2t^2)). The R12 Gaussian domination, multiplied by the observation weight, is bounded uniformly by K exp(-c (|z|^2+|z'|^2)) for some positive c,K, since t_n lies in a compact interval bounded away from zero. The identity |z|^2+|z'|^2=2||w||^2 makes this summable. Dominated convergence yields the limit. Compactness of [1,lambda] and continuity of F establish G(n)-F(t_n)->0: otherwise a violating subsequence would have a convergent phase subsequence and contradict the preceding argument.

Reindexing by multiplication with u or its inverse proves F(lambda*t)=F(t); conjugation interchanges the two embeddings and preserves E, giving F(1/t)=F(t). Writing t=exp(s), the summands are entire in s and on compact subsets of |Im(s)|<pi/4 their absolute values have a common Gaussian majorant, since Re(exp(+-2s))>0 there. Normal convergence gives holomorphic extension on this strip and real analyticity on the real axis.

To prove nonconstancy, use the R10 quadratic forms A=sum w_i^2 and B=a(b-d)+c(b+d), so |z|^2=A+B sqrt(2), |z'|^2=A-B sqrt(2). At t=1 the exponent magnitude is A. At t=sqrt(lambda) it is sqrt(2)(A+B). Both A and A+B are nonnegative integers, and the latter is positive for nonzero w by positive definiteness. Thus exact rational enclosures of exp(-1) and exp(-sqrt(2)) suffice to bound these two lattice sums. The certificate proves
4.9409 < F(1) < 4.9410,
4.9716 < F(sqrt(lambda)) < 4.9718,
and F(sqrt(lambda))-F(1)>0.03.
The subsequences n nearest to lambda^(2j) and lambda^(2j+1) have phases approaching 1 (or lambda, equivalent by periodicity) and sqrt(lambda). This proves nonconvergence of G(n).

## Rational certificate and tail
For all t in [1,lambda], the positive exponent is at least lambda^(-2)*||w||^2, which is less than 0.4. To use a sharper uniform estimate, periodicity and inversion allow phase reduction to [1,sqrt(lambda)], where it is at least lambda^(-1)*||w||^2 > 0.4. For the two certified phases no phase reduction is needed. The code's outside-box bound applies to those two phases; the floating plotted sums at other phases are bounded proxies and have no certified decimal precision. With q=7/10>exp(-0.4), sum_Z q^(m^2)<=1+2q/(1-q). For the box [-L,L]^4 at either certified phase, a union bound over the four coordinates gives tail <= 8*q^((L+1)^2)/(1-q)*(1+2q/(1-q))^3. At L=8 the rational bound is < 10^(-8). The code groups the even lattice box points by A and A+B, uses alternating Taylor partial sums of degrees 20 and 21 to enclose exp(-x) at x=1 and rational brackets for sqrt(2); all inequalities are exact Fraction comparisons. The alternating tail is decreasing at these orders. Positive powers preserve base enclosures. Thus the gap is certified, not a numerical observation alone.

## Actual execution
python3 -I probe.py, standard library only. [Code](probe.py), [stdout](probe.log). 41,761 even vectors in [-8,8]^4, rational inequalities passed; computed outside-box upper bound about 1.376870114e-9 at the certified phases. Nine floating-point phase samples are plotted proxies (not proof of monotonicity, extremality or a minimal period). Local script and stdout Git hashes c9fd517b67c56722091c0513245771b27c4bd43e and 10caf74e4aa25605ef0694c3da9968281c3dcb2c. No finite-n Gaussian path count was executed; the numerical experiment evaluates the limiting lattice function itself, while the connection to the walk follows by the proof above. No physical detector or independent review.

## Prior art and limits
The limiting function is a Gaussian theta sum of a diagonally deformed lattice, an established mathematical object. Preliminary background search found standard lattice theta definitions, e.g. Dense Generic Well-Rounded Lattices (https://doi.org/10.1137/22M1532779). This was a search-result-level background check only, not a full literature review or claim of originality. R12 supplies the lattice local limit argument. This round proves one particular smooth response retains phase dependence; it does not say every smoothing does.

## Margin
- Hard cutoff causes jumps; arithmetic phase survives this Gaussian smoothing.
- Symmetry gives F(lambda/t)=F(t), not proof of extrema at half-phase.
- Next investigate whether special response kernels cancel all phase dependence, and whether phase averaging has a closed expression.
- No temporal frequency or physical dimensional transition inferred.
