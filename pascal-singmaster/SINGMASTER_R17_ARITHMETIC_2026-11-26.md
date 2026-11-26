# CLAUDE — R17: THE LATTICE IS COARSER THAN WE WERE ASKING FOR

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Assignment: TOTO, R17 — IMPROVE THE ARITHMETIC OBSTRUCTION BEFORE IMPROVING THE BOUND

## 0. Short version

Her question was whether `(-1, 0)` is necessary. It is not, and the gain is
larger than the mod-6 argument shows, because `v` and `w` are not independent.

- her residue classes are **correct**, verified independently;
- the parity tie `v + w = 1 + t (mod 2)` plus modulus 24 widens the free interval
  at **both** ends, not just the lower one;
- the leading-coefficient formula already in hand gives the upper end for free:
  at `W = w_0` the `Q^{2t-2}` coefficient is `+t*w_0/24`, so a permitted positive
  endpoint is non-degenerate, unlike `W = 0`;
- thresholds drop by **2.6x to 17.6x**;
- and with a scan made `O(log n)` per row instead of `O(n)`, non-existence is now
  established for **`t = 2, 3, 4, 5`**, where R16 reached only `t = 2, 3`.

Also: **her correction to my R16 explanation is right.** My earlier pairing also
gave degree `t` in `U`, not `2t`. The real advantage of her factorisation is the
linearity of the factors and the monotonicity that falls straight out of it.
Corrected in the R16 record.

`WE WERE PROVING A SHARPER CONFINEMENT THAN THE RESULT NEEDED`

## 1. Her residue classes, verified

`W = 6v^2 - 30w^2 - 24w + 5t^2 - 5` with `v = n+k+1`, `w = n-k-t`, so every term
but the last two is divisible by 6 and

    W = 5(t^2 - 1)  (mod 6)

Enumerating achievable residues over a full period confirms her table exactly:

| `t mod 6` | `W mod 6` | nearest permitted negative `m(t)` |
|---|---|---|
| 0 | 1 | −5 |
| 1, 5 | 0 | −6 |
| 2, 4 | 3 | −3 |
| 3 | 4 | −2 |

- EVIDENCE CLASS: MEASURED (full-period enumeration) and DERIVED (the divisibility).

## 2. The tie she did not use: `v` and `w` are not independent

    v + w = (n+k+1) + (n-k-t) = 2n + 1 - t   =>   v + w = 1 + t  (mod 2)

So the parities of `v` and `w` are **locked to each other** by `t`: opposite for
even `t`, equal for odd `t`. That is one extra bit of information per solution,
and it survives to a larger modulus. Enumerating achievable residues mod 24 under
that constraint:

| `t mod 6` | mod-6 free interval | mod-12 | **mod-24** |
|---|---|---|---|
| 0 | (−5, 1) | (−11, 1) | (−11, 1) |
| 1, 5 | (−6, 0) | (−12, 0) | **(−24, 0)** |
| 2, 4 | (−3, 3) | (−3, 9) | (−3, 9) |
| 3 | (−2, 4) | (−8, 4) | **(−8, 16)** |

The `t = +-1 (mod 6)` case gains a factor of four on the lower end, and `t = 3
(mod 6)` gains at both ends. Where `0` is itself permitted — exactly the
`t = +-1 (mod 6)` classes — the upper endpoint must stay at `W = 0` and the
argument still needs `W < 0` strictly; elsewhere both ends move.

- EVIDENCE CLASS: MEASURED, full-period enumeration under the parity constraint.

## 3. Both ends widen, and the upper one is better behaved

At `U = Q^2 + c` with `W = 24(U-Q^2) + 5t^2 + 1 = w_0`, the R16 formula for the
`Q^{2t-2}` coefficient reads `-t*eps/24` with `eps = -w_0`, hence `+t*w_0/24`.

- `w_0 < 0`: coefficient `t*w_0/24 < 0`, degree `2t-2`. Her `-t*m(t)/24`.
- `w_0 = 0`: coefficient vanishes, degree drops to `2t-3`, leading
  `t(t^2-1)/24 > 0` — the degenerate case.
- `w_0 > 0`: coefficient `t*w_0/24 > 0`, degree `2t-2` — **non-degenerate**, so a
  permitted positive endpoint is strictly better conditioned than `W = 0`.

So where arithmetic permits a positive endpoint, the bracket is
`(W = -L, W = +R)` with both ends of full degree `2t-2` and leading coefficients
`-tL/24` and `+tR/24`.

Endpoint positivity of the factors: `Q >= t+1` still suffices. Each factor is
`Q^2 + s_i Q + d_i` with `|s_i| <= (t-1)/2` and
`d_i >= -(5t^2+1+L)/24 - (t-1)/4 - (t-1)^2/4`; with `L <= 24` the same
computation as R16 gives a positive value at `Q = t+1` and the quadratic
increases from there. Measured for `t <= 15` at both endpoints.

## 4. What it buys, measured

Cauchy's bound on each endpoint polynomial, R16's bracket against R17's:

| `t` | bracket | R16 `n` bound | R17 `n` bound | gain |
|---|---|---|---|---|
| 2 | (−3, 9) | 16.7 | **6.5** | 2.6x |
| 3 | (−8, 16) | 208.1 | **37.4** | 5.6x |
| 4 | (−3, 9) | 4546.4 | **1644.7** | 2.8x |
| 5 | (−24, 0) | 162142.3 | **13256.6** | 12.2x |
| 6 | (−11, 1) | 8736441.3 | 8293948.1 | 1.1x |
| 7 | (−24, 0) | 667557690.8 | **45155344.0** | 14.8x |
| 11 | (−24, 0) | 3.3e17 | **1.9e16** | 17.6x |

Her caution was the right one: she declined to predict a ratio, and the ratio is
not uniform. The `t = +-1 (mod 6)` classes gain an order of magnitude; `t = 0
(mod 6)` barely moves, because its interval was already `(-5,1)` and mod 24 adds
little there.

**Cauchy's growth still dominates.** The bracket is a constant-factor win against
a super-exponentially growing bound, so widening it alone does not extend the
range of `t` very far. That is the honest limit of this round's gain, and it says
where the remaining work is: the threshold, not the obstruction.

## 5. The scan was the other bottleneck, and it was removable

The scan had been `O(n)` per row, comparing full binomials. It need not be.
After factorials cancel,

    L(k) = prod_{i<t}(n-i) * prod_{j=1..t}(k+j) - prod_{r<2t}(n-k-r)

is **strictly increasing in `k`** on the admissible range: the first product
grows with `k`, the second shrinks. So each row has at most one root and
bisection finds it in `O(log n)` with small-integer products and no binomials.
Monotonicity verified on a grid; the `t = 1` control still returns
`(15,5)`, `(104,39)`, `(714,272)`.

That turns ~66,000 rows per second, which changes which `t` are reachable.

Scanning each `t` exhaustively up to its own proved R17 bound:

| `t` | proved bound | scanned | solutions | verdict |
|---|---|---|---|---|
| 2 | 7 | 7 | none | **closed** |
| 3 | 38 | 38 | none | **closed** |
| 4 | 1645 | 1645 | none | **closed** |
| 5 | 13257 | 13257 | none | **closed** |

    NO SOLUTIONS AT ALL for t = 2, 3, 4, 5

against R16's `t = 2, 3`. `t = 6` and `t = 7` have bounds of 8.3M and 45.2M rows,
which the bisection scan can reach; those runs are reported separately when they
finish rather than claimed here.

- EVIDENCE CLASS: the bounds DERIVED (R16 chain plus §2–§3); the scans MEASURED
  and exhaustive **to the stated bound**, which is the whole point — an
  exhaustive scan to an arbitrary limit proves nothing, a scan to the proved
  bound proves non-existence.

## 6. Her correction to my R16 explanation

I wrote that my earlier pairing left "a polynomial of degree `2t` in `U`". Wrong:
it was degree `t` in `U` there too. What my pairing actually cost was carrying
`p = N+K` and the substitution `p^2 = (Q-1/2)^2 + 4U`, which made the
coefficients messy and hid the monotonicity. Her factorisation's real advantage
is that **each factor is linear in `U`**, so `dP/dU` is a sum of products of the
others and positivity is immediate.

A correction note is appended to the R16 record. I had the right conclusion about
her form being better and the wrong reason for it, which is its own lesson: a
claim can be directionally right and still be evidence of nothing.

`RIGHT VERDICT, WRONG MECHANISM, STILL AN ERROR`

## 7. Status

| statement | status |
|---|---|
| `W = 5(t^2-1) (mod 6)`; her `m(t)` table | proved + verified |
| `v + w = 1 + t (mod 2)` | proved |
| mod-24 free intervals under that tie | measured, full period |
| `Q^{2t-2}` coefficient `= +t*w_0/24` at `W = w_0` | derived, all `t` |
| endpoint positivity at `Q >= t+1` for the wider bracket | measured, `t <= 15` |
| threshold gains 2.6x–17.6x | measured |
| **no solutions for `t = 2, 3, 4, 5`** | **proved + exhaustively verified** |
| no solutions for `t >= 6` | open; `t = 6, 7` scans running |
| sharper threshold than Cauchy | not attempted this round |
| originality, present day | unresolved |

## 8. Next

1. Finish the `t = 6, 7` scans and report them.
2. The threshold is now the only bottleneck. Cauchy discards every coefficient
   but one; comparing the two products factor by factor should give something far
   smaller. That is the single highest-value step and it is the one I have not
   started.
3. Stronger congruences beyond mod 24 — her item 4 — gave nothing further here
   under the parity tie alone. A constraint that uses the curve itself, rather
   than treating `v, w` as free integers subject to parity, might.
4. Originality still needs a citation sweep of the papers citing Jenkins.

Her question this round was not "is this tool necessary" but "is the condition I
am trying to meet stronger than the result requires". It was, by a factor of up
to 24 on the lattice and up to 17.6x on the bound. Fifth time the pattern has
paid.

Research only. No operational routing; the house is SEMER's.
