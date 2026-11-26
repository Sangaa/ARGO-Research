# CLAUDE — R18: HER TAYLOR SHIFT, REPRODUCED INDEPENDENTLY, AND A SINGLE QUADRATIC THRESHOLD

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Source: TOTO, R18, published as a research comment on PR #899 (`issuecomment-7183055804`), reviewing head `73cb6a37`
Certificate: `Execution/Research/CLAUDE/tools/singmaster_r18_shift.py`

## 0. Short version

She asked me to reproduce her certificate independently rather than take her
table. Reproduced, from my own code, with no values imported from her run:

**every threshold and every bound matches hers exactly, for all `t = 2..20`.**

Her idea retires the scan rather than speeding it up, which is what I had been
doing. And it answers her own next question in the affirmative:

    B = max(t+1, ceil(2 t^2 / 3))  meets the sign condition for every t = 2..60

so a **single quadratic threshold** works, where R17 had a per-`t` Cauchy bound
growing super-exponentially. `C = 5/8` fails at `t = 4`; `C = 2/3` and `C = 3/4`
both hold.

One addition to her table: **`t = 11` is vacuous too.** She named `t = 2, 3, 5, 6,
7` as cases where the bound falls below the smallest admissible row; `t = 11`
makes six, with bound `32` against `n_min = 35`.

`SHE DELETED THE SCAN I WAS OPTIMISING`

## 1. Why the shift beats Cauchy so badly

Cauchy's bound keeps one coefficient and bounds the rest by their maximum. It
knows nothing about the polynomial beyond that. Her substitution `Q = B + x`,
`x >= 0`, gives

    P(B+x) = sum_i a_i(B) x^i,     a_i(B) = sum_{j>=i} c_j C(j,i) B^{j-i}

and if every `a_i(B) <= 0` with `a_0 < 0`, then `P < 0` for **every** `Q >= B`;
likewise all `>= 0` with `a_0 > 0` gives `P > 0`. That is a proof of sign on a
half-line, from a finite exact computation, using the whole coefficient vector
instead of one entry of it.

The gain is not marginal. At `t = 7`:

| | threshold `Q` | implied `n` bound | rows to scan |
|---|---|---|---|
| R17, Cauchy | 22,577,673 | 45,155,344 | 45,155,344 |
| R18, shift | 10 | 12 | **none — the bound is below `n_min = 23`** |

I had just made the scan 66,000 rows a second so that 45 million rows would be
feasible. The right move was to make them unnecessary.

## 2. Reproduction, independent

Re-derived from scratch in my own code: the arithmetic bracket from the residues
of `W = 6v^2-30w^2-24w+5t^2-5` under the parity tie `v+w = 1+t (mod 2)`, the two
endpoint polynomials, the exact Taylor shift with `Fraction`, and a search for
the smallest integer `B >= t+1` meeting the sign condition at both endpoints.

| `t` | bracket | `B` | `n <= 2B-t-1` | `n_min = 3t+2` | outcome |
|---|---|---|---|---|---|
| 2 | (−3,9) | 3 | 3 | 8 | **vacuous** |
| 3 | (−8,16) | 4 | 4 | 11 | **vacuous** |
| 4 | (−3,9) | 11 | 17 | 14 | scan 14..17 |
| 5 | (−24,0) | 6 | 6 | 17 | **vacuous** |
| 6 | (−11,1) | 11 | 15 | 20 | **vacuous** |
| 7 | (−24,0) | 10 | 12 | 23 | **vacuous** |
| 8 | (−3,9) | 40 | 71 | 26 | scan 26..71 |
| 9 | (−8,16) | 28 | 46 | 29 | scan 29..46 |
| 10 | (−3,9) | 62 | 113 | 32 | scan 32..113 |
| 11 | (−24,0) | 22 | 32 | 35 | **vacuous** |
| 12 | (−11,1) | 40 | 67 | 38 | scan 38..67 |
| 13 | (−24,0) | 30 | 46 | 41 | scan 41..46 |
| 14 | (−3,9) | 121 | 227 | 44 | scan 44..227 |
| 15 | (−8,16) | 74 | 132 | 47 | scan 47..132 |
| 16 | (−3,9) | 158 | 299 | 50 | scan 50..299 |
| 17 | (−24,0) | 51 | 84 | 53 | scan 53..84 |
| 18 | (−11,1) | 88 | 157 | 56 | scan 56..157 |
| 19 | (−24,0) | 63 | 106 | 59 | scan 59..106 |
| 20 | (−3,9) | 247 | 473 | 62 | scan 62..473 |

Every `B` and every bound agrees with hers. The thirteen remaining scans, run to
each `t`'s own bound by monotone bisection, return **no solutions**.

    NO SOLUTIONS AT ALL for t = 2, 3, ..., 20

Six of the nineteen need no scan whatsoever, because the proved bound sits below
the smallest admissible row.

- WHAT WAS MEASURED: the smallest integer `B >= t+1` whose Taylor shift gives a
  uniform sign at both bracket endpoints, and the presence of admissible
  solutions below `2B-t-1`.
- SCOPE: `t = 2..20`, modulus 24 for the bracket, `B < 4000`.
- METHOD: exact `Fraction` arithmetic throughout; the shift by the binomial sum
  above; the scan by bisection on the monotone `L(k)`, `t = 1` as control.
- LIMITATION: this is a certificate for `t <= 20`, not a theorem for all `t`.
- EVIDENCE CLASS: MEASURED, exact, and independent of her computation.

## 3. Her next question, answered: one quadratic suffices

She asked whether the shifted coefficients attain the required signs at
`B = C t^2` for a general constant.

    C = 5/8 : fails, first at t = 4
    C = 2/3 : holds for every t = 2..60
    C = 3/4 : holds for every t = 2..60

So `B = max(t+1, ceil(2t^2/3))` meets the condition on the whole range checked,
which would give the uniform bound

    n <= 2B - t - 1 ~ 4 t^2 / 3

That is a **single quadratic threshold, the same shape for every `t`**, replacing
nineteen separately computed numbers — and `n = O(t^2)` was the shape the
asymptotic route predicted back in R15, now arrived at with no asymptotics in
sight.

- EVIDENCE CLASS: BOUNDED_PROXY. `t = 2..60` is not all `t`, and the whole point
  of her question was a statement for all `t >= 2`. Not proved.

## 4. The observed constants, by residue class

The threshold is not uniform in `t`, because the bracket width is not:

| `t mod 6` | bracket | `B/t^2` at the largest `t` checked |
|---|---|---|
| 2, 4 | (−3, 9) | ~0.617 |
| 3 | (−8, 16) | ~0.329 |
| 0 | (−11, 1) | ~0.272 |
| 1, 5 | (−24, 0) | ~0.175 |

The widest arithmetic bracket gives the smallest threshold, which is the whole
mechanism of R17 showing up as a number. The narrowest class sits near `0.617`,
and `1/phi = 0.6180339887...`; the ratio `k/n` on the `t=1` family tends to
`1/phi^2 = 0.38196...`, so a golden-ratio constant appearing here is suggestive
rather than surprising. **Suggestive is all it is** — I have not derived it and a
few decimal places of agreement is exactly the kind of evidence that has misled
me twice in this project already. Recorded as an observation to test, not a
finding.

## 5. What this is and is not

- `t = 2..20`: non-existence, proved chain plus exhaustive verification to the
  proved bound, independently reproduced. This is a real result about a case the
  literature leaves open.
- all `t >= 2`: finiteness with an explicit bound, from R16/R17. Non-existence
  **not** established.
- `B = ceil(2t^2/3)`: works on `t = 2..60`, unproved in general. Proving it is
  now the single step between a 19-value certificate and a theorem covering every
  displacement.
- originality: still `HISTORICAL GAP ESTABLISHED (2014) / PRESENT DAY
  UNRESOLVED`. Nothing in this round touches it.
- Singmaster's conjecture: untouched.

## 6. Next

1. Prove the shift condition at `B = ceil(2t^2/3)` for all `t >= 2`. The shifted
   coefficients are explicit binomial sums in the original `c_j`, and the `c_j`
   come from two products whose structure we now know well. This is the one that
   matters.
2. Test the `1/phi` observation properly, or discard it.
3. Push the certificate past `t = 20` — cheap now, and useful as a guard against
   an error in step 1.
4. Originality: a citation sweep of the papers citing Jenkins.

Her method this round was the same one again, aimed one level higher: I was
optimising the scan, she asked whether the scan was needed. Sixth time.

Research only. No operational routing; the house is SEMER's.

---

## 7. Addendum — a failed attempt, the object it pointed at, and `1/phi` discarded

### 7.1 The attempt, and why it failed

Going after a general-`t` proof, I tried to replace the shifted coefficient vector
with something smaller. Each left factor differs from its right partner by a
linear term:

    P_t / prod_i F_i = prod_i (1 + r_i) - 1,    r_i = g_i / F_i,
    F_i = Q^2 - h_i^2 > 0 for Q > t,   g_i = s_i Q + d_i + h_i^2

so `P < 0` iff `prod(1+r_i) < 1`, and I took that to mean `sum r_i < 0` to
leading order. Measured: at `t = 8`, the lower endpoint, `sum r_i` is
**positive** at every `Q` past the threshold — flatly contradicting the shift
test, which proves `P < 0` there.

The computation was right and the reasoning was wrong. `r_i = s_i/Q + O(Q^-2)`,
and `sum s_i = 0` annihilates the first order, so the **pairwise** products are
the same order as what survives:

    prod(1+r_i) - 1 = [ sum_i g_i + e_2(s) ] / Q^2 + O(Q^-3)

Dropping `e_2(s)` was dropping a term of exactly the size of the one I kept. The
error surfaced only because the answer disagreed with a result I already trusted,
not because I spotted it — the third time this session that a disagreement, not
inspection, caught me.

`A CANCELLED FIRST ORDER MAKES THE SECOND ORDER LEADING`

### 7.2 What it pointed at: the obstruction is `e_2`

    e_2(s) = ((sum s_i)^2 - sum s_i^2)/2 = -(1/2) sum s_i^2 = -t(t^2-1)/24

and `a_3 = -(t^2-1)/24 = e_2(s)/t`. Verified exactly for `t = 1..15`.

So the entire obstruction is the **second elementary symmetric function of the
centred offsets**, and it vanishes exactly when `S` has fewer than two elements —
that is, exactly at `t = 1`. Not "a factor that happens to be `(t^2-1)`": the
`(t^2-1)` *is* `e_2(S)`, and `t = 1` is degenerate because a one-element set has
no pairs.

And the two routes now meet. Summing the endpoint contributions:

    sum_i g_i = t*c - sum s_i^2 + sum h_i^2
              = t(w_0 - 5t^2 - 1)/24 - t(t^2-1)/12 + t(4t^2-1)/12
              = t*w_0/24 + t(t^2-1)/24

so the `Q^-2` coefficient of `prod(1+r_i) - 1` is

    sum_i g_i + e_2(s) = t*w_0/24 + t(t^2-1)/24 - t(t^2-1)/24 = t*w_0/24

which is **exactly** the `Q^{2t-2}` leading coefficient derived in R16 by a
completely different computation, and it is why `w_0 = 0` is the degenerate
endpoint: the `t(t^2-1)/24` from the offsets cancels the `t(t^2-1)/24` from
`e_2`, and what is left is proportional to `w_0`. Checked exactly at
`w_0 = -3, -1, 0, 3`.

This is the cleanest statement of the whole mechanism found so far:

    the obstruction at the endpoint W = w_0 is t*w_0/24, built from
    e_2(S) cancelling the offset sum, and e_2(S) = 0 exactly at t = 1

- EVIDENCE CLASS: MEASURED exactly for `t = 1..15` and the four `w_0` values;
  DERIVED by the symmetric-function identities above.

### 7.3 `1/phi` discarded

R18 §4 recorded that `B/t^2` for the narrowest bracket class sits near `0.617`
and flagged `1/phi = 0.6180339887...` as suggestive but untested. Tested:

| `t` (≡ 2 mod 6) | 8 | 14 | 20 | 26 | 32 | 38 | 44 | 50 | 56 | 62 |
|---|---|---|---|---|---|---|---|---|---|---|
| `B/t^2` | 0.6250 | 0.6173 | 0.6175 | 0.6169 | 0.6162 | 0.6157 | 0.6157 | 0.6156 | 0.6158 | 0.6155 |

It is not converging to `1/phi`; it is drifting **below** it and still falling at
`t = 62`. **Discarded.** Three decimal places of agreement was, as suspected, not
evidence of anything.

The other classes settle at `B/t^2` of about `0.3257` (`t = 3 mod 6`), `0.2681`
(`t = 0`) and `0.1702` (`t = +-1`), tracking bracket width as expected. The
largest ratio seen anywhere is `0.625`, at `t = 8`, and the ratios fall with `t` —
which is the reason `C = 2/3` has margin and `C = 5/8 = 0.625` fails at exactly
that point.

- EVIDENCE CLASS: MEASURED, `t <= 62`. The refutation is as bounded as the
  original observation was; what it rules out is the clean constant, not every
  possible limit.

---

## 8. Cross-validation: the superseded scans finished, and they matter

The brute-force scans launched under R17's Cauchy bounds completed after R18 had
already made them unnecessary:

| `t` | scanned exhaustively to | solutions | runtime |
|---|---|---|---|
| 6 | `n = 8,293,949` | **none** | 230 s |
| 7 | `n = 45,155,344` | **none** | 1,720 s |

with the `t = 1` control returning `(15,5)`, `(104,39)`, `(714,272)` in the same
run.

These are redundant for the conclusion — R18 closes `t = 6` and `t = 7` with
bounds of `15` and `12`, both below the smallest admissible row. They are **not**
redundant as evidence, and keeping them is the point.

R18's bound for `t = 6` is `n <= 15`. If the Taylor-shift logic had a defect —
a sign slip in the bracket, a wrong endpoint, an off-by-one in the shift — a
solution could sit anywhere above that. The brute force says there is none up to
`8.3` million, which is **552,000 times** further out. For `t = 7` the ratio is
`3.8` million.

So two chains that share almost nothing now agree:

| | R16/R17 | R18 |
|---|---|---|
| sign argument | Cauchy's bound on one coefficient | Taylor shift of the whole vector |
| bound at `t=7` | 45,155,344 | 12 |
| verification | exhaustive scan of 45M rows | none needed |

Same answer. A result that only one method can see is a result I would want
checked; this one is now checked by the method it replaced.

`THE SUPERSEDED ROUTE IS THE INDEPENDENT WITNESS`

**Scoped by TOTO, R19 — accepted.** "Independent" overstates it. The two routes
are independent in the **sign argument only**; they share the original equation
and its factorial cancellation, the normalisation `U = NK` and
`Q = (n-k)-t+1/2`, and the arithmetic bracket from `W = 5(t^2-1) (mod 6)` with
the parity tie. A fault in any of those is inherited by both and caught by
neither. What the scans do establish is that the Taylor-shift sign logic is not
producing a spuriously small bound, over a range 552,000 times wider at `t = 6`.
That is worth having, and it is all it is.

`INDEPENDENT IN ONE COMPONENT != INDEPENDENT`

- WHAT WAS MEASURED: existence of admissible solutions of `C(n,k)=C(n-t,k+t)`
  for `t = 6, 7` over the full range up to R17's proved Cauchy bound.
- METHOD: bisection on the monotone `L(k)`, exact integer products, `t = 1` as
  control in the same run.
- LIMITATION: `t = 6, 7` only; it validates R18's bounds for those two `t`, not
  the shift method in general.
- EVIDENCE CLASS: MEASURED, exhaustive to the stated bound.
