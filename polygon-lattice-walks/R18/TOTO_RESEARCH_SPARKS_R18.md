# TOTO | Research Sparks R18 — certified phase variation in the dodecagonal walk

**Date:** 2026-11-27  
**Status:** SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION  
**Evidence:** DERIVED + MEASURED EXACTLY WITH RATIONAL INTERVALS  
**Originality:** UNASSESSED; no external literature search is claimed.

## Research question

R16 derived a log-periodic limiting lattice function for the regular dodecagonal walk, but its phase values were only numerical proxies. Is that function actually nonconstant?

This round answers that specific open question with a certified strict inequality. It does not infer a physical frequency or establish that the model describes a physical detector.

## Model and result

Let `zeta = exp(i*pi/6)`, `O = Z[zeta]`, and write `w=a+b*zeta+c*zeta^2+d*zeta^3`. Use the two embeddings `z` and `z'` from R16. Their squared moduli are

```text
|z(w)|^2  = A + B sqrt(3)
|z'(w)|^2 = A - B sqrt(3)
A = a^2+b^2+c^2+d^2+ac+bd
B = ab+bc+cd.
```

For `lambda=sqrt(2+sqrt(3))`, R16's limiting function is

```text
F(t) = sum_(w in Z^4) exp(-[t^2 |z(w)|^2 + t^(-2)|z'(w)|^2]/2).
```

At `t=1` the exponent is `A`. At `t=sqrt(lambda)`, it is
`(sqrt(6)/2)(A+B)`, since `lambda+lambda^(-1)=sqrt(6)` and
`sqrt(3)(lambda-lambda^(-1))=sqrt(6)`. The exact certificate proves

```text
F(1) - F(sqrt(lambda)) > 1/10000.
```

Therefore this limiting phase function is nonconstant. Combining this with R16's local-limit result shows that the normalized dodecagonal walk observable retains a genuine scale phase in the limit. This resolves the specific open item recorded at the end of R16.

## Proof of a summable common envelope

For `A`, the inequalities `2|ac| <= a^2+c^2` and `2|bd| <= b^2+d^2` give `A >= ||w||_2^2/2`.

The quadratic form `U=A+B` has eigenvalues
`1/2`, `1`, `(5-sqrt(17))/4`, and `(5+sqrt(17))/4`. Thus

```text
(sqrt(6)/2) U >= (sqrt(6)(5-sqrt(17))/8) ||w||_2^2 > ||w||_2^2/4,
```

where the last inequality is equivalent, after squaring positive quantities, to `62^2 > 15^2*17`. Hence both phase summands are bounded above by `(4/5)^(||w||_2^2)`: use `exp(1/4)>5/4`, which follows from the first three positive terms of its series.

Outside the box `[-12,12]^4`, a four-coordinate union bound gives the common tail

```text
8 (4/5)^169 / (1-4/5) * (1 + 2(4/5)/(1-4/5))^3 < 1/10^10.
```

The certificate checks this rational inequality exactly.

## Exact finite comparison

The box contains `25^4 = 390625` integer vectors. The certificate groups them by the integer exponents `A` and `U=A+B`.

- For `A >= 50`, or for `U >= 42`, the corresponding exponent is at least 50 because `sqrt(6)/2 > 6/5`. The omitted in-box terms are bounded above by `(2/5)^50` each, using `e > 5/2`.
- The constant `sqrt(6)/2` is enclosed by rational endpoints obtained from an integer square root at denominator `10^18`.
- For each remaining exponential, divide its argument by a power of two until it is at most `1/4`. The alternating Taylor sums of degrees 15 and 14 give lower and upper rational bounds; raising the positive bounds back to the original power preserves the enclosure.
- Each term is rounded outward to a grid of size `10^-30`. The finite sums, omitted-term bounds, and outside-box tails are combined using exact fractions.

`probe.py` prints the population counts and exits nonzero if any exact inequality fails. `probe.log` is its actual stdout. The final lower bound on the difference is checked directly against `1/10000`; no floating-point comparison is used in the proof.

## Review and provenance

The question came from R16's open-work note. TOTO derived the two evaluation points, envelope, and rational certificate in this session. HORUS was asked to review the derivation and certificate independently; this is a model-side review, not human peer review. The result is session-derived and non-canonical until separately validated.

The proof depends on R16's derivation that `F` is the limiting phase function for the stated walk. This round certifies only that `F` is nonconstant. It does not certify the numerical mean in R16, prove minimality of the period, identify extrema, analyze other kernels, or provide experimental evidence about nature.

## Next

1. Ask a human specialist to review the cyclotomic embeddings, local-limit transfer from R16, and this rational certificate.
2. Search the theta-function literature before making any novelty claim about this model-specific phase inequality.
3. Keep phase variation, period minimality, extrema, and physical interpretation as separate questions.
