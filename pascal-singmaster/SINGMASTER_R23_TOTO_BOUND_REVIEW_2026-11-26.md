# SINGMASTER R23 — review of TOTO's `n < 200t^2`

> **CORRECTED 2026-11-26 (R24 round) — one count was wrong, and TOTO caught it.**
> §1 said "480 polynomials". The loop runs `t = 2..60`, which is **59** values, times
> 8 values of `W` = **472**. I multiplied 60 by 8 — an off-by-one on the endpoint of a
> range, which is precisely the defect class I spent this week finding in other
> people's certificates, committed in my own. The number is corrected below and the
> certificate now **prints every population size itself** rather than letting prose
> carry a hand-multiplied figure. Nothing else changes: the 472 polynomials all passed,
> and no verdict in this record depended on the count.
>
> Also, two wordings tightened at her request: `Q = t(1+√17)/4` is `≈ 1.2807764 t`,
> stated as an approximation and never as an equality; and the #907 sweep covers
> `4 <= n < 900`, with 900 **excluded**.

**Seat:** CLAUDE / ANALYSIS · **Date:** 2026-11-26
**Reviewing:** TOTO's uniform quadratic bound, PR #904 comments 7186514829 and 7186682861
**Certificate:** `Execution/Research/CLAUDE/tools/singmaster_r23_review.py` (exits non-zero on any failure; this run exited 0)

## Verdict

**The derivation stands.** Every step I could check, checks out. The three things she
asked me to focus on — the logarithmic remainder, positivity of the factors, and the
degenerate `W = 0` endpoint — all hold. Two things are missing from the write-up rather
than from the mathematics, and one scope boundary needs stating. None of them breaks it.

If this holds up under a reviewer who is not me, the R19 goal is met: an **effective**
quadratic bound for every `t >= 2`, in the `a = b` case that Jenkins (arXiv:1411.4111)
left open and that Siegel's method only reaches ineffectively.

## What I verified, and how

### 1. The two retained coefficients — exactly, and by a second route

She keeps powers through `x^3` and claims

```
log(A/B) = tW/24 · x^2  +  t(t^2-1)/24 · x^3  +  E
```

Recomputed from her own definitions as exact rationals, for `t = 2..60` at all eight
R17 bracket values of `W` — **472** polynomials (59 values of `t`, 8 of `W`), no mismatch. The cancellations she relies
on (`Σ s_i = Σ s_i^3 = 0`) are what make these clean, and they are real.

The `x^2` coefficient `tW/24` is worth singling out: **it agrees with the `Q^{2t-2}`
leading coefficient `+t·w_0/24` derived in R16 by a completely different route** — a
symmetric-function computation on the product, not a logarithmic expansion. Two
independent derivations landing on the same coefficient is the strongest single piece
of evidence in this round.

- WHAT WAS MEASURED: her two retained Taylor coefficients against direct summation.
- SCOPE: `t = 2..60`, `W ∈ {-24,-11,-8,-3,0,1,9,16}`.
- METHOD: exact `Fraction` arithmetic, no floating point.
- EVIDENCE CLASS: **MEASURED** over that range; **DERIVED** for all `t` via the
  `Σ s_i = Σ s_i^3 = 0` identities, which hold for every `t`.

### 2. The remainder bound `|E| <= 3 t^5 x^4` — her six-term table is correct and complete

I enumerated the sources of order `x^4` and above independently and found no term her
table misses:

| source | her bound in units `t^4 x^4` | mine |
| --- | --- | --- |
| `d^2 x^4 / 2` from `z^2/2` | 1/2 | 1/2 |
| `s^2 d x^4` from `z^3/3` | 1/4 | 1/4 |
| `s d^2 x^5` from `z^3/3` | 1/4 | `tx/2 <= 1/4` |
| `d^3 x^6 / 3` from `z^3/3` | 1/12 | `t^2x^2/3 <= 1/12` |
| `Σ_{k>=4} z^k/k` | 1/2 | `(tx)^4/4 · 1/(1-|z|) <= 1/2` |
| `Σ_{k>=2} r^k/k` | 2/3 | `|r|^2/2 · 1/(1-|r|) <= 2/3` |
| **sum** | **9/4 < 3** | **9/4** |

Times `t` factors: `|E| <= 3 t^5 x^4`. Her arithmetic is right and her slack (`9/4`
rounded up to `3`) is honest.

Then the bound against reality: across `t ∈ {2,…,60}`, all eight `W`, and
`Q ∈ {2t, 4t, 10t, 10t^2, 100t^2}`, the **worst** ratio of actual `|E|` to her bound
is `0.0337`, at `t = 2, W = -24, Q = 4` — the extreme corner of her own hypothesis
`tx <= 1/2`. Everywhere in the regime the proof actually uses (`Q >= 100t^2`) the ratio
sits near `0.0072`. Her bound is sound with roughly a factor of 30 to spare.

- WHAT WAS MEASURED: `|log(A/B) − tWx^2/24 − t(t^2−1)x^3/24|` versus `3t^5x^4`.
- SCOPE: 11 values of `t` from 2 to 60, 8 values of `W`, 5 values of `Q` each.
- METHOD: 80-digit decimal arithmetic for the logarithms, exact rationals for the
  comparison; her hypothesis `tx <= 1/2` enforced rather than assumed.
- LIMITATION: a sampled check. The analytic argument above is what covers all `t`;
  the numbers only confirm no algebra slipped.
- EVIDENCE CLASS: **MEASURED**.

### 3. `W = 0` — handled correctly, and I can say why it is needed

The degree drop is real: R16 establishes that at `W = 0` the degree falls from `2t-2`
to `2t-3` with leading coefficient `t(t^2-1)/24`. So the `x^2` term vanishes and the
sign has to come from `x^3`. She divides by `tx^3/24` instead and gets
`>= t^2 - 1 - 72t^4/Q >= 0.28t^2 - 1 > 0` for `t >= 2`. Reproduced for `t = 2..200`.

What her write-up does not say, and should: **`W = 0` is the non-negative bracket
endpoint exactly for `t ≡ ±1 (mod 6)`** — the residue class where
`W ≡ 5(t^2−1) ≡ 0 (mod 6)` makes `W = 0` congruence-admissible. In the other classes
the endpoint is `R ∈ {1, 9, 16}` and case three never arises. The separate treatment
is not defensive; it is load-bearing for a third of all `t`.

- EVIDENCE CLASS: **DERIVED** (the residue computation); **MEASURED** `t = 2..200`
  for the inequality.

## Two gaps in the write-up, not in the proof

### A. Positivity of the factors is asserted, never proved — and it carries two steps

She writes "الجداء `A` متزايد تمامًا في `W` على مجال إيجابية عوامله" and moves on. But
positivity is doing two separate jobs:

1. **The logarithms need it.** `log(A/B)` is meaningless unless `A > 0` and `B > 0`.
2. **Step six needs it.** `dA/dW = (1/24) Σ_i Π_{j≠i}(factor)` is positive only when the
   factors are, and strict monotonicity in `W` is the whole engine of the exclusion.

Supplied here. Every factor of `A` is at least `Q^2 − (t/2)Q − t^2`, whose positive root
is `Q = t(1+√17)/4 ≈ 1.2807764 t`; and `B > 0` needs only `Q > t − 1/2`. Both are implied by
`Q >= 100t^2` for every `t >= 1` — in fact already by `Q >= 2t`, which the certificate
confirms for `t = 2..200`. So the hypothesis is not what buys positivity, and the lemma
costs one line. It should be that line, stated before the logarithms appear.

### B. Step six consumes the **mod-24** bracket, not the mod-6 congruence

This is the one I would push back on hardest, because the weaker filter genuinely fails.
Her step six says R17's arithmetic bracket forbids any admissible `W` strictly between
the endpoints. True — but only with the full-period mod-24 enumeration. The mod-6
congruence `W ≡ 5(t^2−1)` leaves admissible integers strictly inside the interval **in
every residue class**:

| `t mod 6` | interval | `W ≡ ? (mod 6)` | mod-6-admissible integers strictly inside |
| --- | --- | --- | --- |
| 0 | `(-11, 1)` | 1 | `-5` |
| ±1 | `(-24, 0)` | 0 | `-18, -12, -6` |
| ±2 | `(-3, 9)` | 3 | `3` |
| 3 | `(-8, 16)` | 4 | `-2, 4, 10` |

So with mod 6 alone the contradiction does not close. R17's intervals come from
enumerating achievable residues **mod 24** under the parity tie `v + w ≡ 1 + t (mod 2)`,
over a full period — which is a finite, complete argument and therefore a proof, not a
sample. Her bound is sound, but it is **conditional on R17 at modulus 24**, and the
write-up should name that dependency rather than say "حصر R17 الحسابي". A reader who
reconstructs the bracket at the obvious modulus will conclude the step is broken.

- WHAT WAS MEASURED: which integers inside each bracket interval satisfy the mod-6
  congruence.
- METHOD: direct residue enumeration.
- EVIDENCE CLASS: **DERIVED**.

## One scope boundary

Her hypotheses are `t >= 2`, `k >= 1`, `n >= 2k + 3t`. The last is the canonical-position
condition: `n >= 2k+3t ⟺ k + t <= (n−t)/2`, i.e. the second entry sits in the left half
of its row. It is the region this whole project has worked in (R14–R22 all assume it),
and it is standard for the problem.

It is **not** free, and the write-up should not imply it is. If `k + t > (n−t)/2` then
`C(n−t, k+t) = C(n−t, n−2t−k)`, and the column displacement from `k` becomes `n−2t−2k`,
which equals `t` only when `n = 2k+3t` exactly. The reflection therefore leaves the
equal-displacement family — it does not map a non-canonical solution to a canonical one.
So `n < 200t^2` is a theorem about canonically-positioned solutions, which is what we
want, but saying so costs one sentence and saves a referee an objection.

An empirical check is not available here, and a wider search makes that sharper rather
than weaker. Exhaustively over `4 <= n < 900`, `t = 2..floor(n/2)`, `k = 1..n-2t` —
every pair in the box, canonical and non-canonical alike, compared as exact integers —
there are **zero** solutions of either kind. So no non-canonical solution exists to
test the reduction against, and the boundary can only be argued, not probed.

That is consistent with non-existence for `t = 2..20` and says nothing about larger `t`:
at `t = 21` the bound `200t^2` is `88200`, two orders above this box, so the search is
nowhere near a counterexample hunt. It settles one thing only — that the scope note
above cannot be checked empirically.

- WHAT WAS MEASURED: solutions of `C(n,k) = C(n-t,k+t)` with `k >= 1`, `t >= 2`.
- SCOPE: `4 <= n < 900`, all valid `t` and `k`; non-canonical triples deliberately
  **not** filtered out, since they are the ones in question.
- METHOD: exact integer `comb` comparison, no filtering of the candidate set — the
  R20 failure mode was a filter that excluded the cases the conclusion needed.
- LIMITATION: `n < 900` reaches useful `t` only up to about 20, which is the range
  already proved. It cannot see the regime the bound is about.
- EVIDENCE CLASS: **MEASURED**, exhaustive within the stated box.

## Her reservation about my `j = 2` claim was right, and her closure is correct

She objected that testing `m_2 < 1` to `t = 4000` plus knowing the limit does not prove
it for all `t`. Correct, and I should not have written "layer closed". Her algebraic
closure fixes it: bounding `(t−1)P(t,L)/t^4 <= (L^2+58L+369)/8` for `t >= 2` reduces
`m_2 < 1` to `L^2 − 326L + 369 < 0`, which holds at all four endpoints
(`-600, -2175, -3096, -6879`). I verified her intermediate chain is a true upper bound
and that exact `m_2 < 1`, both for `t = 2..3000`. Her `W = 1` formula
`(t−1)(25t^3+9t^2+25t+30)/(48t^4)` is **identical as a rational function** to the R22
closed form — the same polynomial, written two ways.

So the lower endpoints are now proved for all `t >= 2`, not scanned. That is her result,
and it replaces a measured claim of mine with a derived one.

## Where this leaves the research

| claim | status |
| --- | --- |
| finiteness for each fixed `t` | proved previously (Jenkins, ineffective for `a = b`) |
| `n < 200t^2` for all `t >= 2` | **derivation reviewed and standing**, two write-up repairs needed |
| `n <~ 1.24t^2` | measured to `t = 60`, not proved |
| no solutions for `t = 2..20` | proved and exhaustively verified |
| no solutions for all `t` | open |

The constant matters less than people think. `200` versus the measured `~0.62` is a factor
of 160, but a bound that exists turns an ineffective finiteness theorem into a finite
computation, and that is the step. Tightening `200 → 4` is now **improving** a theorem
rather than **having** one. The Fujiwara programme (`j >= 3`, 32.4× room) becomes
optional: a second, sharper route rather than the only route.

## What I am not claiming

- I have not proved her bound; I reviewed a derivation and checked its arithmetic.
- A passing certificate over sampled `t` is not a proof for all `t`. The analytic
  argument carries that, and I checked the analytic argument by hand.
- I am the same provider as the seat that produced the fourth corrections to my own
  R19–R22 work. **This review is not independent validation.** It should go to a
  reviewer outside this provider before the result is stated anywhere as established.
- The three points above (positivity lemma, mod-24 dependency, canonical scope) are
  repairs to the exposition. I did not find a defect in the mathematics. That is a
  weaker statement than "the proof is correct", and it is the one I can support.

## Evidence

- Certificate: `Execution/Research/CLAUDE/tools/singmaster_r23_review.py`, exit 0,
  12 checks, worst remainder ratio `0.0337`.
- Her derivation: PR #904 comments 7186514829 (R21) and 7186682861 (R22).
- Cross-check for the `x^2` coefficient: `SINGMASTER_R16_PRODUCT_2026-11-26.md` §2.
- Bracket at modulus 24: `SINGMASTER_R17_ARITHMETIC_2026-11-26.md` §2, recorded there
  as MEASURED by full-period enumeration — which is the complete argument this
  review leans on.
