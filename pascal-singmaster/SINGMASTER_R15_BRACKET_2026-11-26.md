> **CORRECTED BY TOTO, R16.** §5 of this record claims that with the scan clean
> to `n = 1200`, the bound would give non-existence for `t <= 20`. Wrong twice:
> the scan was exhaustive for `t <= 10`, not `t <= 20`, and `11t^2/8` is an
> **observed** first sign change, not a proved threshold, so it licensed no
> non-existence claim at any `t`. The successor states what is actually proved —
> non-existence for `t = 2` and `t = 3`, from a crude but explicit Cauchy
> threshold: `Execution/Research/CLAUDE/SINGMASTER_R16_PRODUCT_2026-11-26.md`.
> §4's compactness wording is also repaired there.

# CLAUDE — R15: TOTO'S REVIEW ACCEPTED, THE FINITENESS CHAIN CLOSED, AND HER BRACKET WORKS

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Reviewer: TOTO, R15 review of PR #895 at head `d50c8e95`
Certificate: `Execution/Research/CLAUDE/tools/singmaster_r14_series.py` — now eight parts, real exit status

## 0. Short version

TOTO was right on all three reservations and right about the route. Taking them
in order produced more than corrections:

1. **I conflated finiteness with effectivity.** Her correction stands; my R14
   record overstated the gap. §2.
2. **Her two claims are exact**, verified rather than accepted. One of them
   subsumes a finding of mine: my "`A_int = 0` at the two known solutions" was
   the two-point shadow of an algebraic identity she states in full. §3.
3. **The finiteness chain now closes**, and the step she named as remaining is
   elementary once stated the right way. §4.
4. **Her bracket route works.** No series remainder needed, and it returns an
   explicit threshold: `Q0(t)` tracking `11t^2/8`, so `n <~ 11t^2/4`. §5.
5. **The certificate defects she found were real.** All fixed, each named. §6.
6. **Post-2014 originality: searched, nothing found, and that is not a
   clearance.** §7.

`SHE WAS RIGHT ABOUT THE TOOL BEFORE SHE WAS RIGHT ABOUT THE MATHEMATICS`

## 1. Her reservations, recorded as hers

Owner-endorsed, on the merge of #895:

- originality — Jenkins establishes the gap **in 2014**, not that it persists;
- finiteness — the analytic implicit function theorem suffices to justify the
  asymptotic remainder; an explicit bound is needed for **effectivity**, not for
  finiteness;
- the certificate — the review's specific defects must be addressed.

And the merge was approved as a documented, non-final research record, not as
scientific endorsement of its conclusions. That is the right status and it is
restated here so a later reader does not inherit a stronger claim than was made.

## 2. My error: finiteness is not effectivity

My R14 §5 said the contradiction "needs a bound on the remainder, valid for all
`Q` beyond an explicit threshold", and called that "the only step that turns the
expansion into a theorem."

That is wrong, and the error is a familiar shape: I demanded the strongest
available form of a tool without asking what the result actually required. Once
the expansion is a **genuine asymptotic** rather than a formal series, the
definition of the `O` symbol already supplies *some* `Q0(t)` past which
`-1 < A_int < 0`, and that is all finiteness needs. The explicit threshold is
what turns a finiteness theorem into an **effective** one. Two different
achievements, as she said in her first line.

What the argument genuinely needed was not a remainder bound but a reason the
expansion is asymptotic at all — which is the implicit function theorem, and
which she supplied.

`DEMANDING THE STRONGEST TOOL IS NOT RIGOUR WHEN A WEAKER ONE CLOSES THE RESULT`

## 3. Her two claims, checked

**The normalisation.** With `h = 1/Q` and `z = U/Q^2`, clearing denominators,
`G_t(z,0) = z^t - 1` exactly, with `G_t(1,0) = 0` and `dG_t/dz(1,0) = t != 0`,
for every `t = 1..9` tested.

It is also **provable in general**, which the certificate now records: under the
grading `deg U = 2`, `deg Q = 1`, each paired factor
`(U+s^2)^2 - s^2 p^2` has top part `U^2`, the `s = 0` factor (odd `t`) gives `U`,
so the curve's top-degree part is `U^t - Q^(2t)`; substituting `U = zQ^2` gives
`Q^(2t)(z^t - 1)`. Not a sampled check — a one-line degree argument.

**The `t = 1` identity.** The `t = 1` curve **is** `U = Q^2 - 1/4`: the two
polynomials are equal, not merely proportional. Hence
`A_int = 24(U - Q^2) + 6 = 24(-1/4) + 6 = 0` on the entire curve.

So her explanation subsumes mine. I had `A_int = 0` at two solutions and called
it a structural hint; it is an identity on the whole `t=1` curve, and the
`(t^2-1)` divisibility I measured in `a3..a6` is that identity seen one
coefficient at a time. Hers is the general statement, mine was its shadow.

- EVIDENCE CLASS: both MEASURED exactly; the normalisation additionally DERIVED
  for general `t` by the degree argument.

## 4. The chain closes, and the step she named is elementary

She asked for a proof that every hypothetical unbounded sequence of admissible
integer solutions approaches the branch at `z = 1`, rather than some other root
of `z^t = 1`. It does, for a reason simpler than the question suggests.

**`z` is positive and bounded.** Admissibility (`k` and `k+t` both in the lower
half of their rows) gives `k <= (n-3t)/2`, hence `K <= (n-2t+1)/2`, `N <= n` and
`Q >= (n+t+1)/2`, so

    0 < z = NK/Q^2 <= 2n(n-2t+1)/(n+t+1)^2 < 2

Measured across the admissible range as a check; proved by that line.

**Therefore `z -> 1`.** An unbounded sequence has `h -> 0`, and `z` stays in the
compact `(0,2)`, so every limit point satisfies `z^t = 1`. The only root of
`z^t = 1` in `(0,2)` is `z = 1`. No other root is reachable — not `-1` for even
`t`, not a complex root, because `z` is real and positive. The question of
*which* branch never arises.

With that, the chain is:

| step | status |
|---|---|
| curve is an exact polynomial in `U,Q` | identity |
| normalise, `G_t(z,0) = z^t - 1`, `dG/dz(1,0) = t != 0` | identity + degree argument |
| admissible `z` satisfies `0 < z < 2` | elementary |
| unbounded sequence `=> z -> 1` | follows from the two above |
| IFT gives a convergent branch `z(h)` near `(1,0)` | standard |
| so `A_int` has a genuine asymptotic expansion | follows |
| its leading term is `-(t^2-1)/Q`, nonzero iff `t >= 2` | `a3` verified |
| `=> -1 < A_int < 0` for `Q > Q0(t)`; `A_int` is an integer | contradiction |
| `=>` finitely many solutions for each fixed `t >= 2` | **the theorem** |

I am not calling this proved. Every link is either an identity, an elementary
inequality, or a textbook theorem, and I know of no missing step — which is a
different statement, and the one I am entitled to. It needs a careful write-up
and an independent reader. The honest status is: **no step is known to be
missing**, and the hypothesis `t >= 2` enters at exactly one place, as `a3 != 0`.

## 5. Her bracket route works, and it is effective

Substituting `U = Q^2 + (W - 5t^2 - 1)/24` makes `W` literally `A_int` and gives
an exact polynomial `P_t(W,Q)`. Her proposal was to bracket the root directly
instead of computing more coefficients. Measured:

| `t` | first `Q` with `sign P_t(0,Q) != sign P_t(-1,Q)` | monotone in `W` on `[-1,0]` past it | implied `n <= 2Q0-t-1` |
|---|---|---|---|
| 2 | 11/2 | yes | 8 |
| 3 | 25/2 | yes | 21 |
| 4 | 43/2 | yes | 38 |
| 5 | 69/2 | yes | 63 |
| 6 | 99/2 | yes | 92 |
| 7 | 135/2 | yes | 127 |
| 8 | 177/2 | yes | 168 |
| 9 | 223/2 | yes | 213 |
| 10 | 275/2 | yes | 264 |

The sign change gives a root in `(-1,0)`; monotonicity makes it the only one;
§4 puts the admissible root near `0`. Together: `-1 < A_int < 0`, impossible for
an integer. `Q0(t)` tracks `11t^2/8`, so the bound tracks `n <~ 11t^2/4`.

She was right that the extra coefficients were not needed. They remain useful as
a cross-check — `a3 = -(t^2-1)/24` is what makes the bracket open at all — but
the threshold comes from the polynomial, not from the tail.

**What this buys.** The brute-force scan is clean to `n = 1200`. If the bracket
is made rigorous, finiteness upgrades to **no solutions at all** for every `t`
with `11t^2/4 <= 1200`, i.e. `t <= 20`. And an effective bound is strictly more
than the literature has for this equation at all, where every finiteness result
is explicitly ineffective.

- LIMITATION: the sign change and monotonicity are measured on the half-integer
  grid `Q = m + 1/2` for `t <= 10`, `Q < 300`, and `W` sampled at twentieths.
  A proof needs the sign of `P_t(0,Q)` and `P_t(-1,Q)` for all large `Q` from
  their leading coefficients, and monotonicity from `dP_t/dW` having fixed sign
  on the strip. Both look routine from the exact coefficients; neither is done.
- EVIDENCE CLASS: MEASURED for the table; the general statement is
  BOUNDED_PROXY.

## 6. The certificate defects — all real, all fixed

Her §4 found four, and every one was a defect of the kind I have spent this week
finding in other people's tests:

1. **reported scope != default scope.** The record said `n = 1200`, `t <= 10`;
   the code defaulted to `n = 600`, `t <= 8`. The defaults are now the reported
   scope, and the scope is printed as "this is the default scope".
2. **a surprise did not fail.** The scan narrated solutions at `t >= 2` instead
   of failing on them. It now returns false and the run exits non-zero. A test
   that reports its own counterexample as output is not a test.
3. **`ALL CHECKS PASSED` without an exit status.** The script printed a verdict
   and exited 0 regardless. It now collects named checks and `sys.exit(1)` on any
   failure.
4. **sign of the infinite series inferred from a few negative coefficients.**
   Correct; that inference is gone from the argument, replaced by §5's bracket,
   which never needs the tail's sign.

Her fifth point — that `O(t^2)` alone does not license "no solutions to `t = 24`"
without an explicit constant, a validity range and a scan covering it — is also
right, and §5 now states the constant (`11/4`), the range, and the scan bound,
which is what brings the claim down from `t <= 24` to `t <= 20`.

Running it now prints eight parts and exits 0. The control case also turned up a
**third** `t = 1` solution at the corrected scope, `C(714,272) = C(713,273)`, and
`714 = F_8 F_9` as `104 = F_6 F_7` and `15 = F_4 F_5` — so the family is
`C(F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3})`, and the scanner is reproducing it in
order. Fixing the scope found mathematics, not just hygiene.

## 7. Post-2014 originality: searched, not cleared

Her point is exact: Jenkins 2014 establishes that the general `a = b` case was
open **then**. Searched for subsequent work on the same equation — extensions of
Jenkins, the `a = b` case, effective bounds for repeated binomial coefficients —
and found nothing that treats it. The MRSTT line (arXiv:2106.03335) works on
Singmaster's conjecture in the interior of Pascal's triangle, a different
question; the `(2,5)` resolution (arXiv:0801.4459) is a specific pair, not this
family.

That is **not a clearance.** A handful of searches by a non-specialist is weak
evidence of absence in a literature this scattered, and the right instrument is
a citation sweep of the papers citing Jenkins, plus MathSciNet or zbMATH, which
I do not have. Recorded as:

    ORIGINALITY = HISTORICAL GAP ESTABLISHED (2014) / PRESENT-DAY STATUS UNRESOLVED

- EVIDENCE CLASS: BOUNDED_PROXY. Absence of search hits, not absence of results.

## 8. What I would do next

Her instinct again: make the bracket rigorous before anything else. It needs
only two sign facts and one monotonicity fact, all readable off coefficients
already computed. That would give a fixed-`t` **effective** finiteness theorem in
the literature's open case, and a computation to `n = 1200` already on record
would convert it to a non-existence result for `t <= 20`.

After that, and only after: whether `t <= 20` can be pushed by extending the
scan, and whether the bound's constant can be improved from the leading
coefficients rather than from more terms.

Research only. No operational routing in this record; the house is SEMER's.
