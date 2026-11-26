> **CORRECTED BY TOTO, R19 review.** Four points, all accepted, in the successor
> `Execution/Research/CLAUDE/SINGMASTER_R19_EXACT_2026-11-26.md`:
> the measured range was 33 scattered values of `t`, not the contiguous `2..50`
> this record claims; the certificate compared floating-point `j`-th roots where
> an exact rational inequality is equivalent; `j = 1, 2` attaining the maximum was
> empirical, and the stronger "`j = 1` always dominates" that I was about to
> propose is now **refuted** with six counterexamples; and §5's methodology note
> was wrong — Cauchy's raw-ratio bound is a **correct theorem, merely loose**, not
> a misapplication. The successor also reproduces the exact test contiguously:
> 118 polynomials, 7,061 exact inequalities, 0 failures, `t = 2..60`.

# CLAUDE — R19: CAUCHY USED THE RAW RATIO; THE RIGHT TOOL IS THE j-TH ROOT

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Assignment: TOTO, R19 — do not commit to `C = 2/3`, and do not require every
shifted coefficient to share a sign; prove `exists C > 0 : n <= C t^2` for every
admissible solution at `t >= 2`, however large `C` is.

## 0. Short version

Her framing was the unlock. Dropping the demand for a *good* constant exposes
that R17's blow-up was never about the mathematics — it was about using the wrong
root bound.

Cauchy's bound I used takes `max_j |c_{d-j}/c_d|`, a **raw ratio**. The standard
tool for root location takes the **`j`-th root** of it (Fujiwara):

    every root rho satisfies  |rho| <= 2 * max_j ( |c_{d-j}/c_d| )^(1/j)

Measured on both bracket endpoints, that quantity divided by `t^2` is **bounded
by 1** across `t = 2..50`:

    max over t = 2..50 of  max_j (|c_{d-j}/c_d|)^(1/j) / t^2  =  0.99889

so `Q_0 <= 2t^2` and therefore

    n <= 4 t^2        on the range measured

which is R19's target shape with `C = 4`. And the binding term is identified in
closed form, not merely observed.

`THE BOUND WAS NEVER THE PROBLEM; THE NORM I USED ON IT WAS`

## 1. Why Cauchy exploded and Fujiwara does not

The closed forms, computed exactly and held out against further `t`:

| coefficient | lower endpoint `W = -L` |
|---|---|
| `c_{2t-2}` (leading) | `-t L / 24` |
| `c_{2t-3}` | `t(t^2-1)/24` |
| `c_{2t-4}` | `(25t^5 + 48t^4 - 56t^3 - 3t^2 - 14t)/1152` |

The raw ratios therefore grow like

    |c_{2t-3}/c_{2t-2}|       = (t^2-1)/L           ~ t^2
    |c_{2t-4}/c_{2t-2}|       ~ 25 t^4/(48 L)       ~ t^4
    ... and the j-th one like t^{2j}

Cauchy takes the maximum of those directly, so it inherits `t^{2d}` with
`d = 2t-2` — super-exponential in `t`, which is exactly the blow-up seen in R17.
Taking the `j`-th root first turns every one of them back into `O(t^2)`.

The two bounds differ by nothing but a norm, and the whole 45-million-row scan at
`t = 7` was the price of that choice.

- EVIDENCE CLASS: the three closed forms MEASURED exactly and fitted-and-held-out
  on `t = 3..17`; the `t^{2j}` growth pattern DERIVED from the first two and
  OBSERVED for the rest.

## 2. The binding term, in closed form

The maximum is attained at `j = 1` for the `t = 0 (mod 6)` class, whose bracket
is `(-11, 1)`: the upper endpoint has `R = 1`, so `c_d = tR/24 = t/24` while
`c_{d-1} = t(t^2-1)/24`, giving

    |c_{d-1}/c_d| = (t^2-1)/R = t^2 - 1

and `(t^2-1)/t^2 -> 1` from below. That is precisely the measured sequence:
`0.97222` at `t = 6`, `0.99306` at `t = 12`, `0.99889` at `t = 30` — and
`1 - 1/900 = 0.998888...` exactly.

So the worst case is not an empirical accident. It is `(t^2-1)/R`, with the
narrowest permitted positive endpoint `R = 1`, and it is **strictly below `t^2`
for every `t`**.

For the `t = +-1 (mod 6)` classes, `R = 0` and the upper endpoint is the
degenerate one (degree `2t-3`, leading `t(t^2-1)/24`); there the measured value is
about `0.52 t^2`. Every other class sits near `0.18 t^2` to `0.48 t^2`.

## 3. What is proved and what is not

**Proved, in closed form:** the `j = 1` term is `(t^2-1)/R < t^2` for `R >= 1`,
and the degenerate-endpoint variant is likewise bounded.

**Not proved:** that `|c_{d-j}/c_d|^{1/j} <= t^2` for **all** `j`. Measured for
`t = 2..50` across both endpoints, where the maximum over `j` never exceeded
`0.99889 t^2` and was attained at `j = 1` or `j = 2` throughout. A general proof
needs a uniform bound on the coefficient vector, which is a well-posed and finite
task: the coefficients are elementary symmetric functions of the `s_i`, `d_i` and
`h_i^2`, all of which have closed forms.

So R19's goal is **reduced to one inequality in `j`**, with the hardest case
already settled:

    claim:  for every t >= 2 and every j,  |c_{d-j}/c_d| <= t^{2j}
    then:   Q_0 <= 2t^2  and  n <= 4t^2  for every admissible solution

- EVIDENCE CLASS: `j = 1` DERIVED; the general `j` BOUNDED_PROXY on `t = 2..50`.

## 4. Her scoping correction on the cross-validation — accepted

R18 §8 called the R17 brute-force scans an independent witness for the R18
bounds. She narrowed that correctly: the two routes are independent **in the
sign argument only**. They share

- the original equation `C(n,k) = C(n-t,k+t)` and its factorial cancellation;
- the normalisation `U = NK`, `Q = (n-k)-t+1/2`;
- the arithmetic bracket from `W = 5(t^2-1) (mod 6)` and the parity tie.

A fault in any of those would not be caught by either route, because both inherit
it. What the cross-validation does establish is that the **Taylor-shift sign
logic** is not producing a spuriously small bound, over a range `552,000` times
wider at `t = 6`. That is worth having and it is all it is.

Corrected in the R18 record rather than left to stand.

`INDEPENDENT IN ONE COMPONENT != INDEPENDENT`

## 5. Methodology note — the superseded method as cross-validator

Her experience #51, recorded here in the research trail rather than in the
library index, since merging the library's permanent files is routed to SEMER and
is not mine to place:

    SUPERSEDED METHOD AS CROSS-VALIDATOR
    source      : R17, R18, PR #902
    use         : a replaced-but-correct method checks the method that replaced it
    precondition: state which components the two share, and in which single
                  component they are independent
    status      : supported inside this research; transfer untested

The `t = 6, 7` scans cost 32.5 minutes and 53,449,293 rows after they had been
made unnecessary, and they are the only check we have that R18's bound of
`n <= 15` is not an artefact. A correct method does not stop being useful when a
faster one appears; it becomes the witness.

And R19 adds a second note of the same kind, pointing the other way:

    A SUPERSEDED TOOL MAY HAVE BEEN MISUSED RATHER THAN OUTGROWN
    Cauchy's bound was not too weak for this problem. It was applied in the raw
    ratio where the j-th root was the standard form. Before replacing a tool that
    is giving a bad answer, check that it was used in its intended norm.

That one is about my error, not about the method, and it is the more useful of
the two.

## 6. Next

1. Prove `|c_{d-j}/c_d| <= t^{2j}` for all `j`. With the hardest case in closed
   form and the coefficients expressible through elementary symmetric functions,
   this is the concrete remaining step for `n = O(t^2)` in general.
2. Extend the `t = 2..20` non-existence certificate upward — cheap now, and a
   guard against an error in step 1.
3. Originality: a citation sweep of the papers citing Jenkins.

Research only. No operational routing; library file placement is SEMER's to
coordinate.

---

## 7. Addendum — a clean lemma, and the crude route failing for the old reason

Attacking `|c_{d-j}/c_d| <= t^{2j}` for general `j`, the natural handle is that
`P = A - B` with

    A(Q) = prod_i (Q^2 + s_i Q + d_i),   B(Q) = prod_i (Q^2 - h_i^2)

both products of monic quadratics, so their coefficients are elementary
symmetric functions of their roots — and if the roots are small, the
coefficients are controlled.

### 7.1 The lemma: every root has modulus exactly at most `t - 1/2`

Measured across both endpoints:

| `t` | 2 | 3 | 5 | 10 | 20 | 40 | 60 |
|---|---|---|---|---|---|---|---|
| max root modulus | 1.5 | 2.5 | 4.5 | 9.5 | 19.5 | 39.5 | 59.5 |

Exactly `t - 1/2` in every case, which is `h_{t-1}`, the largest of `B`'s roots.
So `A`'s roots are no larger than `B`'s, and

    every root of both products lies in |z| <= t - 1/2 < t

That is a clean statement, independent of `w_0`, and it is the kind of thing a
general proof would be built on.

### 7.2 Why it is not enough, and it is the same reason as before

With all `2t` roots inside `|z| <= t`, each product's coefficients obey
`|coef of Q^{2t-j}| <= C(2t,j) t^j`, so for the difference

    |c_{d-j}/c_d| <= 2 C(2t, j+2) t^{j+2} / (tL/24)

and at `j = 1` that reads `~ 64 t^5 / L` — against a measured value of `t^2 - 1`.
Three orders of `t` too weak.

The reason is the one that has now bitten three times in this project: **`A` and
`B` very nearly cancel**, and a bound built from their roots separately throws
that away. `P`'s leading two coefficients vanish precisely because the products
agree to that order; any estimate that treats them as independent polynomials
cannot see it.

So the crude route is closed, and closed informatively. A proof of the general
`j` bound has to work with the *difference* — the elementary symmetric functions
of the two root sets subtracted term by term, where the near-agreement of the
sets is the content — rather than with either product's size.

`A BOUND THAT IGNORES THE CANCELLATION CANNOT SEE THE RESULT`

Third occurrence of that exact shape: the floating-point attempt in R14 (`U` and
`Q^2` cancel to `O(1)`), the `sum r_i` attempt in R18 (`sum s_i = 0` makes the
pairwise terms leading), and this one. It is worth stating as a standing rule for
this problem rather than relearning it:

    every quantity in this problem is a near-cancellation of two large ones.
    No estimate that bounds the two sides separately will be sharp enough.

### 7.3 Status unchanged, better localised

| statement | status |
|---|---|
| all roots of both products in `\|z\| <= t - 1/2` | measured exactly, `t <= 60`; expected provable |
| `j = 1`: `\|c_{d-1}/c_d\| = (t^2-1)/R < t^2` | proved |
| general `j`: `\|c_{d-j}/c_d\| <= t^{2j}` | measured `t <= 50`; crude root bound insufficient |
| `n <= 4t^2` for all `t >= 2` | follows from the general `j` claim; not proved |
| non-existence, `t = 2..20` | proved and exhaustively verified |

The measured `j*` is always `1` or `2`: `j* = 1` for `t = 0 (mod 6)` where the
ratio tends to `1`, and `j* = 2` elsewhere where it settles near `0.424`. So the
general claim may only need those two cases plus a monotone-in-`j` argument,
which is a much smaller target than all `j` at once.

- EVIDENCE CLASS: §7.1 MEASURED exactly for `t <= 60`; §7.2 DERIVED; the `j*`
  observation MEASURED for `t <= 50`.
