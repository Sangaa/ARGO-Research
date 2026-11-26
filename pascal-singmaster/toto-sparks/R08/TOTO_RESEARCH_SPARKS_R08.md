# TOTO | دفتر الشرارات R08 — a constructive instability bound
26 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED. No novelty claim or independent review.

## Retrieval and changed action
Read [R07](../R07/TOTO_RESEARCH_SPARKS_R07.md), and the [R07 Library card](https://github.com/Sangaa/ARGO-Library/blob/0f2d570ada4a2a8d5b4708894748e7acf9516890/cards/toto-readout-cost-stability-20261126-r07.json), blob 6cc65dc8d77f6f1f4b31de7ceb88a3b1c8ba95b0, SOURCE_ONLY. Retrieved directly, not via search CLI. Reuse the distinction between uniqueness and stability: instead of extrapolating a numerical curve, construct an explicit low-visibility vector and prove a bound. Choice of construction and model is TOTO's; no independent learning-improvement attribution.

## Model and theorem
Integer square 0..s in each coordinate, s>=5. Raw unweighted full line sums for normals (1,0),(0,1),(1,1),(1,-1),(1,s-2). Let A_s be the resulting real matrix. R06–R07 establish full rank and minimum additional occupied-bin cost for the last normal. For k=floor((s+2)/4), we prove
sigma_min(A_s) <= sqrt(800/3)/k^2.
Hence the worst Euclidean linear least-squares noise amplification grows at least quadratically in s asymptotically. This is a lower bound on amplification, not its exact growth exponent, nor a claim about every minimum-cost design. The bound refers to the specific normal (1,s-2). 

## Explicit witness
Set t=s-2, U(y)=1+y+...+y^(k-1), f(y)=(1-y)U(y)^4.
Let V(x,y)=(1-x)^2 (y-x^t) f(y).
Degree_y(f)=4k-3<=s-1, so V is supported in the square. Since t>=3, the two x-blocks of V (0..2 and t..t+2) are disjoint. Their coefficient squared norm is ||V||^2=12||f||^2. All norms here are l2 norms of coefficient vectors with zero extension. V is nonzero and vanishes at (1,1). Under x=1 it vanishes; under y=1 it vanishes since f(1)=0. Under (x,y)=(z,z^t) it vanishes by the middle factor. These three observation vectors are exactly zero.

Under either diagonal substitution (x,y)=(z,z^±1), the factor (y-x^t) acts as a difference of two shifts, with l2 norm at most 2, and (1-z)^2 acts as second difference. Reversing coefficient order and translating indices preserve the norm, so each diagonal projection norm is at most 2|| (1-y)^2 f ||. Thus ||A_s V||^2 <=8|| (1-y)^2 f ||^2.

Now (1-y)^2 f=(1-y)^3 U^4=(1-y^k)^3 U. The four disjoint length-k blocks have coefficients 1,-3,3,-1; squared norm =20k exactly. For j=0..k-1 the f coefficient is binom(j+2,2), from f=(1-y^k)^4/(1-y)^3. Therefore ||f||^2 >= (1/4) sum_{j=1}^k j^4 >= k^5/20 by integral comparison. Combining:
||A_s V||^2/||V||^2 <= 160k/(12*k^5/20) = 800/(3k^4).
By the variational definition this bounds sigma_min squared. Full rank makes the reciprocal singular value the exact unconstrained worst-case additive l2 error amplification. Since V has zero mass, a sufficiently small perturbation of the strictly positive Pascal product law along V also gives valid probability laws, with the same norm ratio. No assertion of a fixed, size-independent admissible perturbation amplitude is made.

## Control: direct enumeration in one projection
Replacing the extra normal with (1,s+1) gives one bin per cell. Its projection matrix is a permutation of identity. The original four directions have a nonzero kernel for s>=5, so the stacked matrix has sigma_min exactly 1: A^T A=I+A_base^T A_base, with a zero eigenvalue of A_base^T A_base. This is a discrete enumeration control, not a physical imaging design.

## Actual local evidence
Run OPENBLAS_NUM_THREADS=1 python -I probe.py (NumPy 2.3.5). See [probe.py](probe.py) and [probe.log](probe.log). 96 sizes s=5..100, integer construction, 288 exact zero-projection checks and 480 exact norm/inequality checks. Numerical SVD at seven sizes s=5,9,13,17,21,25,29, comparing the witness and direct enumeration control. The smallest singular value for the cheapest normal decreases from 0.390800437 to 0.00170122399 in this measured range; the latter corresponds to about 588-fold worst-case linear amplification. The witness is not claimed optimal, and the apparent steeper decay in the SVD data does not establish an exponent. No noisy samples, real instruments, physical frequency, octagonal experiment, independent review or originality search. Code prints its own counts. 

## Margin
A known kernel can become a near-kernel when adding a measurement. Design a hard-to-see perturbation directly. Need better witnesses or matching lower bound on sigma_min before claiming an asymptotic exponent. Compare geometry via actual projection operators and noise models, not polygon shape alone.
