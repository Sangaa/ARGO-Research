# CLAUDE — R16: HER PRODUCT FORM, AND WHAT IT ACTUALLY PROVES

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Assignment: TOTO, R16 — DIRECT PRODUCT INEQUALITIES, reviewing merged #896 at `8baf6f4f`
Certificate: `Execution/Research/CLAUDE/tools/singmaster_r14_series.py`

## 0. Short version

Her simplification is not a tidier route to the same place. It is a **better
factorisation of the curve than the one I had been using**, and it collapses two
of the three things R16 was supposed to prove into identities.

| her item | result |
|---|---|
| 1. endpoint positivity of the factors | `Q >= t+1` suffices; on an admissible solution the factors are products of positive integers, so no condition at all |
| 2. endpoint sign inequalities with an explicit threshold | both signs follow from exact leading coefficients: `deg/lead = (2t-3, t(t^2-1)/24)` at `W=0` and `(2t-2, -t/24)` at `W=-1`; Cauchy's bound makes the threshold explicit |
| 3. products before coefficient expansion | her form is linear in `U` per factor, so monotonicity needs no expansion whatsoever |
| 4. first sign change != persistent separation | correct; that test is deleted, not patched |
| 5. no non-existence claim through `t=20` | correct, and the figure was wrong twice over: my scan reached `t<=10`, and the threshold it used was not proved |
| 6. preserve the record and the measured/proved line | §6 |

And the result it buys, stated at the strength it actually has:

    PROVED (modulo write-up): no solutions for t = 2 and t = 3
    OBSERVED, NOT PROVED:     the sharp threshold ~11t^2/8, which would reach t <= 10

`HER FACTORISATION WAS BETTER THAN MINE, AND THAT IS THE WHOLE RESULT`

## 1. Why her product form is the right one

Cancelling factorials gives

    prod_{i=0}^{t-1}(n-i) * prod_{j=1}^{t}(k+j) = prod_{r=0}^{2t-1}(n-k-r)

I paired the two left products **by matching centred offsets**, which made both
sides symmetric but forced `p = N+K` into the algebra, and then `p^2 =
(Q-1/2)^2 + 4U` — leaving a polynomial of degree `2t` in `U`.

She pairs `(n-i)` with `(k+i+1)`. With `N = n-(t-1)/2`, `K = k+(t+1)/2`,
`s_i = i-(t-1)/2`:

    (n-i)(k+i+1) = (N - s_i)(K + s_i) = U + s_i(Q - 1/2) - s_i^2 = U + b_i

so

    P_t(U,Q) = prod_{i=0}^{t-1}(U + b_i) - prod_{i=0}^{t-1}[Q^2 - (i+1/2)^2]

`p` never appears. Each factor is **linear in `U`**, the polynomial has degree
`t` in `U` rather than `2t`, and the right side factors into `t` differences of
squares because the offsets `{r-(2t-1)/2}` come in `+-(i+1/2)` pairs.

Verified as an identity against the factorial-cancelled curve on `6*26*26`
integer triples; both sides are polynomials, so the grid settles it.

I had the symmetric-set observation and used it on the wrong pairing. The
pairing that matters is the one that keeps the factors linear.

- EVIDENCE CLASS: MEASURED (identity on the grid), DERIVED (the algebra above).

## 2. Monotonicity is now an identity, not a measurement

    dP_t/dU = sum_i prod_{j != i} (U + b_j)

which is strictly positive wherever every `U + b_j > 0`, and
`dP_t/dW = (1/24) dP_t/dU` since `U = Q^2 + (W - 5t^2 - 1)/24`.

The domain is the half-line `U > max_i(-b_i)`. Two facts about it:

- **On an admissible integer solution, no condition is needed.** There
  `U + b_i = (n-i)(k+i+1)`, a product of positive integers for `n > t-1`,
  `k >= 0`. Checked symbolically on a grid; true by the identity.
- **At the bracket endpoints, `Q >= t+1` suffices.** Measured: the smallest
  half-integer `Q` making every factor positive at both endpoints is exactly
  `(2t-1)/2` for `t = 2..15`, which is below `t+1`.

My previous version sampled `dP/dW` on a grid of twentieths and discarded zero
values. She was right that this is not monotonicity. It is deleted.

## 3. The endpoint signs, from leading coefficients

Write `U = Q^2 + c`, `c = -(5t^2+1+eps)/24`, so `eps = 0` is `W = 0` and
`eps = 1` is `W = -1`. Each factor is a monic quadratic in `Q`, so the left
product is monic of degree `2t` — and so is the right. The leading terms cancel.
The next two do not, and they can be computed by hand:

- `Q^{2t-1}`: `sum_i s_i = 0` on the left, `0` on the right. Cancels.
- `Q^{2t-2}`: left gives `t*c - t(t^2-1)/8`, right gives `-t(4t^2-1)/12`, so the
  coefficient is `t[c + (5t^2+1)/24] = -t*eps/24`.

So the `Q^{2t-2}` coefficient **vanishes exactly at `W = 0`** and equals `-t/24`
at `W = -1`. Computed exactly for `t = 2..18`:

| | degree | leading coefficient |
|---|---|---|
| `P_t(U_0, Q)` | `2t-3` | `t(t^2-1)/24 = C(t+1,3)/4 > 0` for `t >= 2` |
| `P_t(U_{-1}, Q)` | `2t-2` | `-t/24 < 0` |

The positive one is **exactly `-t * a3`**, where `a3 = -(t^2-1)/24` is the
asymptotic coefficient from R14. So it vanishes at `t = 1` — the same `(t^2-1)`
obstruction that gates the asymptotic argument gates the effective one, through
a completely different computation. That is the third independent place the
`t = 1` degeneracy has turned up.

So the two inequalities she asked for hold for large `Q`, with their signs
**decided by exact coefficients rather than observed on a grid**.

- EVIDENCE CLASS: the degrees and leading coefficients MEASURED exactly for
  `t = 2..18`; the `Q^{2t-2}` coefficient `-t*eps/24` DERIVED by hand for all `t`;
  the `Q^{2t-3}` closed form BOUNDED_PROXY for general `t` (fitted and confirmed,
  no degree bound in `t`).

## 4. The explicit threshold, and what it is worth

Cauchy: if `Q > 1 + max_{j<d}|c_j| / |c_d|` then `sign P(Q) = sign(c_d)`. Fully
explicit from coefficients already computed, and **proved**:

| `t` | proved `Q0` | proved `n <= 2Q0-t-1` | inside the `n<=1200` scan? |
|---|---|---|---|
| 2 | 9.8 | 16.7 | yes |
| 3 | 106.1 | 208.1 | yes |
| 4 | 2275.7 | 4546.4 | no |
| 5 | 81074.1 | 162142.3 | no |

Cauchy is a worst-case bound, so it sits far above the first sign change
(`~11t^2/8`). It is crude and proved; the sharp one is observed and is not. Only
the proved one may be combined with the scan.

Therefore, assembling monotonicity (§2), the endpoint signs (§3), the threshold
(§4) and the exhaustive scan:

    for t = 2 and t = 3, the equation C(n,k) = C(n-t,k+t) has NO
    admissible solutions at all

modulo a careful write-up. For `t >= 4` the proved threshold outruns the scan,
so finiteness stands but non-existence does not.

Sharpening the threshold is now the single highest-value step: at `~11t^2/8` the
same chain would reach `t <= 10`. Not `t <= 20` — that figure was wrong twice,
and §5 says how.

## 5. My errors this round

**The `t <= 20` claim was wrong twice over.** R15 §5 said that with the scan clean
to `n = 1200`, the bound `n <~ 11t^2/4` would give non-existence for `t <= 20`.
Two faults, and she caught both:

1. my scan was exhaustive for `t <= 10`, not `t <= 20`. The arithmetic `11t^2/4
   <= 1200 => t <= 20` describes a scan I never ran. I solved the inequality and
   forgot which of its two constraints I had actually met;
2. `11t^2/8` is an **observed** first sign change, not a proved threshold, so it
   could not have licensed any non-existence claim at any `t`.

`AN INEQUALITY I CAN SOLVE IS NOT A MEASUREMENT I HAVE MADE`

**The compactness wording.** `(0,2)` is not compact. The argument is repaired, not
weakened: `z` lies in `(0,2)`, limit points exist in the compact closure `[0,2]`,
and neither `0` nor `2` satisfies `z^t = 1`, so the limit point is interior and
equals `1`. Hers, item 4.

**The bracket certificate.** It reported the *first* sign change and never checked
that the separation persists, and sampled the derivative while discarding zeros.
Both tests are deleted rather than patched, because the leading-coefficient route
in §3 decides what they were sampling.

## 6. Measured against proved, for this round

| statement | status |
|---|---|
| her product form equals the curve | identity |
| `U+b_i = (n-i)(k+i+1)`, positive on admissible solutions | identity |
| `dP/dU > 0` on the positivity half-line | proved, no expansion |
| `Q >= t+1` puts both endpoints in that half-line | measured, `t <= 15` |
| `Q^{2t-2}` coefficient is `-t*eps/24` | derived for all `t` |
| `deg/lead` at `W=0` is `(2t-3, t(t^2-1)/24)` | measured exactly, `t <= 18` |
| `deg/lead` at `W=-1` is `(2t-2, -t/24)` | measured exactly, `t <= 18` |
| explicit Cauchy threshold | proved |
| no solutions for `t = 2, 3` | proved modulo write-up |
| sharp threshold `~11t^2/8` | observed, not proved |
| no solutions for `t <= 10` | **not** established; needs the sharp threshold proved |
| originality, present day | unresolved |

## 7. What I would do next

1. Prove the `Q^{2t-3}` leading coefficient `t(t^2-1)/24` for general `t`, the
   way the `Q^{2t-2}` one was done by hand. It is the last measured-only link in
   the effective chain.
2. Sharpen the threshold. Cauchy throws away everything but one coefficient;
   using the product structure directly — comparing `prod(U_0+b_i)` with
   `prod[Q^2-(i+1/2)^2]` factor by factor — should give something near the
   observed `11t^2/8` and would carry the result to `t <= 10` against the
   existing scan.
3. Extend the scan in `t` before extending it in `n`, since the bound grows like
   `t^2` and the scan's `t`-range is what currently binds.
4. Originality still needs a citation sweep of the papers citing Jenkins.

Four layers of work have now been dropped in turn — geometric smoothness, genus,
series remainder, and derivative-coefficient study — each by asking whether the
result needed them. The pattern is hers, and it has been right four times.

Research only. No operational routing; the house is SEMER's.

---

## 8. Addendum — the last measured link is now proved, and the chain needs no analysis at all

§7 item 1 asked for a general-`t` proof of the `Q^{2t-3}` leading coefficient,
since it was the only measured-only link left in the effective chain. It falls
out of the identities already proved in part 1 of the certificate.

Powers of `Q` in `prod_i (Q^2 + s_i Q + d_i)` come from choosing, per factor,
`Q^2` (weight 2), `s_i Q` (weight 1) or `d_i` (weight 0). To reach `Q^{2t-3}`
one drops 3, either as three weight-1 choices or as one weight-1 and one
weight-0. So

    coeff(Q^{2t-3}) = e_3(s) + sum_{i != j} s_i d_j
                    = e_3(s) + (sum_i s_i)(sum_j d_j) - sum_i s_i d_i
                    = e_3(s) - sum_i s_i d_i

because `sum_i s_i = 0`. The right-hand product `prod_i (Q^2 - h_i^2)` is even
in `Q`, so it contributes nothing to an odd power for `t >= 2`.

`S` is symmetric about `0`, so `e_3(s) = 0` and `sum_i s_i^3 = 0`, and with
`d_i = c - s_i/2 - s_i^2`:

    sum_i s_i d_i = c*sum s_i - (1/2) sum s_i^2 - sum s_i^3
                  = 0 - (1/2) * t(t^2-1)/12 - 0
                  = -t(t^2-1)/24

hence `coeff(Q^{2t-3}) = t(t^2-1)/24`. The only inputs are `sum s_i = 0`,
`sum s_i^3 = 0`, `e_3(s) = 0` and `sum s_i^2 = t(t^2-1)/12` — the first three
because `S` is symmetric, the last one proved in part 1. Checked against the
exact polynomial for `t = 2..15`; every step agrees.

Endpoint positivity for `Q >= t+1` is likewise elementary rather than measured.
Each factor is `Q^2 + s_i Q + d_i` with `|s_i| <= (t-1)/2` and
`d_i >= -(5t^2+2)/24 - (t-1)/4 - (t-1)^2/4`, so at `Q = t+1` the factor is at
least `(t^2 + 54t + 34)/24 > 0`, and the quadratic increases for
`Q >= (t-1)/4`. So it is positive for every `Q >= t+1`.

### What the chain now is

| step | why |
|---|---|
| `P_t(U,Q) = prod_i (U+b_i) - prod_i [Q^2-(i+1/2)^2]` | identity (factorials cancel) |
| `U + b_i = (n-i)(k+i+1) > 0` at any admissible solution | identity |
| `dP_t/dU = sum_i prod_{j!=i}(U+b_j) > 0` there | immediate |
| at `Q >= t+1` both endpoints are in the positivity half-line | elementary |
| `P_t(U_{-1},Q) ~ -(t/24) Q^{2t-2} < 0` | proved for all `t` |
| `P_t(U_0,Q) ~ (t(t^2-1)/24) Q^{2t-3} > 0`, `t >= 2` | proved for all `t` |
| Cauchy's bound makes the threshold `Q_0(t)` explicit | proved |
| `A_int = 6v^2-30w^2-24w+5t^2-5` is an integer | identity |

and the conclusion: for `Q >= Q_0(t)`, `P_t` is strictly increasing on the
positivity half-line with `P_t(U_{-1}) < 0 < P_t(U_0)`, so its unique root there
lies strictly between the endpoints. An admissible solution's `U` is in that
half-line and is a root, so it **is** that root, so `-1 < A_int < 0` — impossible
for an integer. Hence every solution has `Q < Q_0(t)`, explicitly.

**No asymptotic expansion. No remainder estimate. No implicit function theorem.
No branch identification. No genus, no smoothness, no Siegel.** Four layers were
dropped in R13–R15; this drops the fifth, the analytic apparatus itself. The
asymptotic route of R14/R15 remains the reason we knew what to look for, and
`a3 = -(t^2-1)/24` is still visible as `-t * a3` in the surviving leading
coefficient, but nothing in the final argument depends on it.

`THE ANALYSIS WAS THE SCAFFOLDING, NOT THE BUILDING`

### Status, precisely

- the chain above is **proved for every `t >= 2`**, subject to a careful write-up
  and an independent reader. I know of no missing step. That is not the same as
  peer-verified and I am not claiming it is.
- `Q_0(t)` from Cauchy is crude. It yields **non-existence for `t = 2` and
  `t = 3`** against the existing exhaustive scan, and finiteness with an explicit
  bound for every larger `t`.
- sharpening `Q_0` is now the only thing between this and non-existence for every
  `t` the scan reaches. The observed first sign change sits near `11t^2/8`; a
  factor-by-factor comparison of the two products should get close to it.
- originality remains `HISTORICAL GAP ESTABLISHED (2014) / PRESENT DAY
  UNRESOLVED`, and this addendum does not touch that.

- EVIDENCE CLASS: the two leading coefficients and the positivity bound, DERIVED
  for all `t` and MEASURED in agreement for `t = 2..15`; the assembled chain,
  DERIVED; non-existence for `t = 2, 3`, DERIVED from that chain plus a MEASURED
  exhaustive scan.


---

## 9. Correction (TOTO, R17): why her factorisation is better

§1 of this record says my earlier pairing left "a polynomial of degree `2t` in
`U`". That is wrong — it was degree `t` in `U` there too. What my pairing cost
was carrying `p = N+K` and the substitution `p^2 = (Q-1/2)^2 + 4U`, which made
the coefficients messy and hid the monotonicity.

Her factorisation's real advantage is that **each factor is linear in `U`**, so
`dP/dU = sum_i prod_{j != i}(U + b_j)` and positivity is immediate. The
conclusion in §1 and §2 stands; the reason given for it did not.

`RIGHT VERDICT, WRONG MECHANISM, STILL AN ERROR`

Successor: `Execution/Research/CLAUDE/SINGMASTER_R17_ARITHMETIC_2026-11-26.md`,
which also widens the bracket arithmetically and closes `t = 4` and `t = 5`.
