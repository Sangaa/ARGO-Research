# SINGMASTER R24 — tightening the effective bound to `n < (225/2) t^2`

**Date:** 2026-11-27  
**Status:** SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION  
**Evidence class:** DERIVED, conditional on the lemmas in frozen V3  
**Novelty:** UNASSESSED. No external literature search for this smaller constant was performed.

## Research question

Can the scoped effective bound in
[`referee/SINGMASTER_UNIFORM_QUADRATIC_BOUND_FROZEN_V3_2026-11-26.md`](referee/SINGMASTER_UNIFORM_QUADRATIC_BOUND_FROZEN_V3_2026-11-26.md)
be tightened without changing its argument?

The previous proof used `|E| <= 3 t^5 x^4` in its logarithmic expansion. Its own six-term remainder table sums to `9/4`, so the same proof supports the sharper bound `|E| <= (9/4)t^5 x^4`. This changes the normalized error constant from `72` to `54`.

## Theorem

For integers `t >= 2`, `k >= 1`, and `n >= 2k + 3t`, if

```text
binom(n,k) = binom(n-t,k+t),
```

then

```text
n < (225/2) t^2.
```

This retains V3's canonical-position hypothesis. It does not cover non-canonical triples and does not settle the Singmaster conjecture.

## Derivation

Keep V3's variables `Q = n-k-t+1/2`, `x=1/Q`, and bracket endpoints `W=-L` or `W=R`, with `L in {3,8,11,24}` and `R in {0,1,9,16}`. The factorwise Taylor remainder bounds in V3's Lemma 2 sum to

```text
1/2 + 1/4 + 1/4 + 1/12 + 1/2 + 2/3 = 9/4.
```

The sum is **strictly** less than `9/4`: in particular, the `s_i^2 d_i x^4` source is strictly below its listed `1/4` bound because `|s_i| <= (t-1)/2 < t/2`, while the other source bounds are no larger than their listed entries. Thus `|E| < (9/4)t^5x^4`. After dividing the logarithmic identity by `t x^2/24`, the error is strictly less than `54t^4x^2`:

```text
(24/(t x^2)) log(A/B) = W + (t^2-1)x + err,
|err| < 54t^4x^2.
```

Assume for contradiction that `Q >= (225/4)t^2`. Then `x <= 4/(225t^2)`. At a lower bracket endpoint, `W=-L<=-1`, so

```text
(24/(t x^2)) log(A/B)
  < -1 + 4/225 + 864/50625 < 0.
```

At an upper endpoint with `R>=1`,

```text
(24/(t x^2)) log(A/B) > 1 - 864/50625 > 0.
```

The remaining case is `R=0`. By the mod-24 bracket, this occurs only when `t == +/-1 (mod 6)`; since `t>=2`, then `t>=5`. Dividing by `t x^3/24` instead gives

```text
(24/(t x^3)) log(A/B)
  > t^2 - 1 - 54t^4x
  >= t^2/25 - 1
  >= 0.
```

At `t=5` the last coarse lower bound is zero, but the first inequality is strict because the Taylor remainder is strict; for larger admissible `t`, the final bound is positive. The endpoint signs and V3's monotonicity lemma place the unique zero strictly inside the excluded arithmetic bracket, a contradiction. Thus `Q < (225/4)t^2`.

Canonical position gives `n <= 2Q-t-1`, hence `n < (225/2)t^2-t-1 < (225/2)t^2`.

## Independent review and evidence limits

HORUS independently reconstructed the factorial reduction, mod-24 bracket, remainder estimate, positivity/monotonicity step, and canonical-position scope in V3/R23 and found no gap in those steps. HORUS also identified the direct constant tightening. This is a model-side review within this session, not human peer review or external validation.

[`singmaster_r24_bound.py`](tools/singmaster_r24_bound.py) checks the displayed margins using exact rational arithmetic. The strict remainder step is explicit in this record; the certificate does not re-prove V3's analytic remainder expansion or its binomial-factorization identities, which remain inherited proof obligations. No scan, numerical approximation, or empirical data supports the all-`t` conclusion.

## Next

1. Have a human number theorist review the inherited V3 lemmas and this constant improvement.
2. Search the literature for sharper effective bounds in this exact equal-displacement form.
3. If those checks hold, optimize the constant using the actual residue-class endpoints and the strict remainder margin. Do not edit any frozen V1–V3 file.
