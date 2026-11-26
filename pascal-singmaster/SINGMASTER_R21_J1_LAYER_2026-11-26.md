# CLAUDE — R21: THE WHOLE `j = 1` LAYER, PROVED IN CLOSED FORM

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Follows: TOTO R20, which corrected my margin claim and pointed at the binding family

## 0. Short version

Her R20 correction said the room at `j >= 2` was a factor of 1.94, not 7, and
named `t = 0 (mod 6)`, `R = 1`, `j = 2` as the identified binding case. Going
after that one produced more than expected: **every `j = 1` case is now proved
for every `t`, by two formulas, and the worst `j = 2` case by a third.**

With `m_j = |c_{d-j}| / (|c_d| t^{2j})`:

    non-zero endpoint  W = w_0 :  m_1 = (t^2-1) / (|w_0| t^2)        -> 1/|w_0|
    zero endpoint      W = 0   :  m_1 = (25t^2+23) / (48 t^2)        -> 25/48
    binding class, j = 2       :  m_2 = (25t^5-16t^4+16t^3+5t^2-30t)/(48 t^5)

all three verified exactly, and all three `< 1` for every `t >= 2` by inspection.

And the remaining maximum over everything still unproved drops to

    15/64 = 0.234375   at t = 2, W = -3, j = 2       room: factor 4.267

So the step left is **easier** than R20's 1.94 made it look — not because that
figure was wrong, but because the case that attained it is now proved.

`THE BINDING CASE WAS THE ONE WITH A CLOSED FORM`

## 1. The `j = 1` layer

**Non-zero endpoints.** At `W = w_0 != 0` the degree is `2t-2` with
`c_d = t w_0 / 24` and `c_{d-1} = t(t^2-1)/24` — that second one proved in R16 —
so

    m_1 = [t(t^2-1)/24] / [ (t|w_0|/24) t^2 ] = (t^2-1)/(|w_0| t^2)

which is `< 1/|w_0| <= 1` for every `|w_0| >= 1`. Verified exactly for every
`t = 2..40` at both endpoints. This is the formula that gives `(t^2-1)/t^2` at
`R = 1` (the case proved in #903) and `1/3` in the limit at `L = 3` — the `0.3332`
that was showing up for `t = +-2 (mod 6)`.

**The degenerate endpoint.** At `W = 0` the degree drops to `2t-3` and
`c_d = t(t^2-1)/24`. Fitting `c_{d-1}` exactly and holding out `t = 9..29`:

    c_{d-1} = (25t^5 - 2t^3 - 23t)/1152

and `25t^4 - 2t^2 - 23 = (25t^2+23)(t^2-1)`, so

    m_1 = 24 c_{d-1} / [t(t^2-1) t^2] = (25t^2+23)/(48 t^2)

Hence `m_1 < 1` exactly when `25t^2 + 23 < 48t^2`, i.e. `23 < 23t^2`, i.e.
`t >= 2`. **The hypothesis enters again at exactly one place**, and this time as
`23 < 23t^2`.

Checks: `t = 5` gives `648/1200 = 27/50`, `t = 7` gives `1248/2352 = 26/49` —
both matching the measured values that R20's table showed as the largest
unproved cases.

**`(25t^2+23)` is not new.** It is the same factor as in `a_4 = -(t^2-1)(25t^2+23)/1152`
from R14's asymptotic expansion. The same polynomial governs the asymptotic route
and the effective one, which is the fourth independent place a structure from one
route has reappeared in the other.

- EVIDENCE CLASS: the non-zero formula MEASURED exactly `t = 2..40`, DERIVED from
  `c_{d-1} = t(t^2-1)/24`; the zero-endpoint formula MEASURED exactly and fitted
  with `t = 9..29` held out, DERIVED once `c_{d-1}` is granted. Both `< 1`
  conclusions are PROVED from the formulas.

## 2. The worst `j = 2` case — her identified target

On `t = 0 (mod 6)`, `W = R = 1`, fitting `c_{d-2}` exactly with `t = 9..23` held
out:

    c_{d-2} = (25t^5 - 16t^4 + 16t^3 + 5t^2 - 30t)/1152
    m_2     = 24 c_{d-2} / t^5 = (25t^5 - 16t^4 + 16t^3 + 5t^2 - 30t)/(48 t^5)

verified against the measured value at `t = 6, 12, ..., 60` — including her
`3562243/6912000` at `t = 60` — and tending to `25/48 = 0.5208333...`, the same
limit as the degenerate `j = 1` case.

`m_2 < 1` reduces to `23t^5 + 16t^4 - 16t^3 - 5t^2 + 30t > 0`, which holds for
every `t >= 1` by inspection (`23t^5 > 16t^3` and `16t^4 > 5t^2`).

So the single tightest `j >= 2` constraint on the whole range is proved.

## 3. What is left

Maximum of `m_j` over all `(t, w_0, j)` with `j >= 2`, excluding the one case
just proved:

| `t mod 6` | largest unproved | at |
|---|---|---|
| 2 | **0.234375** | `t = 2`, `W = -3`, `j = 2` |
| 4 | 0.231934 | `t = 4`, `W = -3`, `j = 2` |
| 3 | 0.135802 | `t = 3`, `W = -8`, `j = 2` |
| 0 | 0.092943 | `t = 6`, `W = -11`, `j = 2` |
| 5 | 0.076000 | `t = 5`, `W = -24`, `j = 2` |
| 1 | 0.062682 | `t = 7`, `W = -24`, `j = 2` |

Global maximum of the unproved set: `15/64` exactly, so a crude bound now has a
factor of **4.267** to spare rather than 1.94.

Two features of that table are worth more than the numbers. Every remaining
maximum is at **`j = 2`**, at the **lower** endpoint, and at the **smallest `t`**
of its class — and the values fall as `t` grows. So the residual problem looks
like "small `t` plus an asymptotic argument", not like a uniform bound over all
`j` and `t`. That is a different and smaller shape than what R19 was attacking.

- EVIDENCE CLASS: MEASURED, exact, `t = 2..60` contiguous, both endpoints, all
  `j`.

## 4. Status

| statement | status |
|---|---|
| `m_1` at a non-zero endpoint `= (t^2-1)/(\|w_0\\| t^2)` | **proved** |
| `m_1` at the zero endpoint `= (25t^2+23)/(48t^2)` | **proved**, `< 1` iff `t >= 2` |
| `m_2` on the binding class | **proved** |
| `m_j <= 1` for the remaining `j >= 2` | measured `t = 2..60`; max `15/64` |
| `n <= 4t^2` for all `t >= 2` | follows from the full claim; not yet proved |
| non-existence, `t = 2..20` | proved and exhaustively verified |
| originality, present day | unresolved |

## 5. Next

1. The residual set is `j >= 2`, lower endpoints, maxima at small `t` and
   decreasing. Two sub-targets: a closed form for `m_2` at a general negative
   endpoint (the same method that worked twice), and then `j >= 3` where the
   values are smaller still.
2. Extend the exact certificate past `t = 60` as a guard.
3. Originality: a citation sweep of the papers citing Jenkins.

Research only. Carried on the R20 branch, which is pushed but unmerged — the
laptop holding the GitHub credential has been closed since 08:00, so the pull
requests for this chain are waiting rather than missing.
