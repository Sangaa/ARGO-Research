# An effective uniform quadratic bound for the equal-displacement binomial equation

**FROZEN VERSION 2 — 2026-11-26. For external review. Supersedes V1.**

This file is frozen. Improvements to the constant, to the exposition, or to the
surrounding programme go in new records and must **not** be applied here, so that a
referee and the authors are reading the same text. Any change to this file is itself
a defect. Development continues on the unfrozen records in
`Execution/Research/CLAUDE/`.

**V1 is not edited and remains retrievable in repository history.** It is superseded
because TOTO's review found, within an hour of the freeze, one genuine gap in its
Lemma 1 and one methodological error in its §11, and because she replaced its Lemma 3
with a derivation. A frozen text with a known gap should be superseded, not patched by
an erratum a referee may not read. `referee/FREEZE_LOG.md` records exactly what changed
and why. **Read V2; V1 exists only so the change is auditable.**

**Authorship.** Derivation by TOTO (external model seat). Review, repairs and
verification by CLAUDE (engineering seat). Research direction and the corrections that
produced several of the repairs below: Human Authority (Essam). The two model seats are
**different providers**; the review is cross-provider but is not peer review by a
human mathematician, and no external referee has seen this yet.

---

## 1. Statement

For integers `n, k, t` with

```
t >= 2,    k >= 1,    n >= 2k + 3t
```

every solution of

```
C(n, k) = C(n - t, k + t)
```

satisfies

```
n < 200 t^2.
```

**The hypothesis `n >= 2k + 3t` is canonical position**, equivalent to
`k + t <= (n-t)/2`: the second entry lies in the left half of its row. It is **not**
without loss of generality and the theorem does not silently cover the complement. If
`k + t > (n-t)/2` then `C(n-t, k+t) = C(n-t, n-2t-k)` and the *column* displacement
from `k` becomes `n - 2t - 2k`, which equals `t` only when `n = 2k + 3t` exactly. The
reflection therefore leaves the equal-displacement family rather than mapping a
non-canonical solution into the hypotheses. Solutions outside canonical position are
outside this theorem.

## 2. Why the result is of a different kind from what preceded it

Jenkins (arXiv:1411.4111) studies `C(x,y) = C(x-a, y+b)` and proves finiteness for
`a != b` by Siegel's theorem — which is **ineffective**: it gives no bound on the size
of solutions. The case `a = b` with `a != 1` is named there as an open extension
requiring "an entirely different argument". The present statement is in that case, and
it is **effective**: it names a finite region, so non-existence for a given `t` becomes
a finite computation rather than an unbounded search.

The constant is weak. Measured thresholds in this programme sit near `0.62 t^2`, so
`200` is loose by about two orders of magnitude. That is a matter for improvement, not
for existence: a bound that exists converts an ineffective theorem into a decidable
one, and the present work does not depend on the constant being small.

## 3. Notation

```
Q   = n - k - t + 1/2
x   = 1/Q
s_i = i - (t-1)/2            i = 0, ..., t-1
h_i = i + 1/2
W   = 6v^2 - 30w^2 - 24w + 5t^2 - 5,    v = n + k + 1,  w = n - k - t
d_i = (W - 5t^2 - 1)/24 - s_i/2 - s_i^2
A   = prod_i (Q^2 + s_i Q + d_i)
B   = prod_i (Q^2 - h_i^2)
```

The factorial cancellation `prod_{i<t}(n-i) * prod_{j=1..t}(k+j) = prod_{r<2t}(n-k-r)`
puts the equation in the form `A = B`. `W` is an integer, being a polynomial with
integer coefficients in the integers `v, w, t`.

Useful identities, all elementary:

```
sum_i s_i = sum_i s_i^3 = 0,   sum_i s_i^2 = t(t^2-1)/12,   sum_i h_i^2 = t(4t^2-1)/12
```

## 4. Lemma 1 (positivity)

*For `Q >= 2t` and `|W| <= 24`, every factor of `A` and every factor of `B` is strictly
positive.*

`|s_i| <= (t-1)/2 < t/2` and `|h_i| <= t - 1/2 < t` are immediate. For `d_i`, with
`|W| <= 24`,

```
|d_i| <= (5t^2 + 25)/24 + t/4 + t^2/4 <= t^2    for t >= 2.
```

Hence each factor of `A` is at least `Q^2 - (t/2)Q - t^2`, whose positive root is
`Q = t(1 + sqrt(17))/4`, approximately `1.2807764 t`; and each factor of `B` is at
least `Q^2 - t^2 > 0`. Both hold for `Q >= 2t`. ∎

Lemma 1 is used twice and both uses are load-bearing: the logarithms in §5 are
undefined without it, and the monotonicity in §7 is

```
dA/dW = (1/24) * sum_i prod_{j != i} (Q^2 + s_j Q + d_j) > 0,
```

which is positive precisely because the factors are.

### Lemma 1b (the positivity region is connected, and contains any solution)

*The set `P(Q,t) = { W : every factor of A is positive }` is an up-set: if all factors
are positive at `W_0` then they are positive at every `W >= W_0`. Consequently `P` is an
interval, unbounded above. Moreover every actual solution lies in `P`, whatever its `W`.*

Each factor depends on `W` only through `d_i`, and `d(d_i)/dW = 1/24 > 0` independently
of `i`, `t` and `Q`. So each factor is a strictly increasing affine function of `W`, each
factor's positivity set is an up-set, and a finite intersection of up-sets is an up-set.

For the second part: at an actual solution the factors are not merely positive, they are

```
Q^2 + s_i Q + d_i = (n - i)(k + i + 1),
```

an identity in `(n,k,t)` — a product of two positive integers, since `i <= t-1 < n` and
`k >= 1`. Positivity at a solution is therefore a property of the solution, not an
assumption about `W`. ∎

**Why Lemma 1b is needed.** Lemma 1 bounds `|d_i|` using `|W| <= 24`, which holds at the
bracket endpoints but need not hold at a hypothetical solution's `W`. Without Lemma 1b,
§7 would be asserting monotonicity across a range on which positivity had only been
established at its two ends. With it, the solution's `W` and both endpoints lie in one
up-set — whichever of the three is smallest generates an interval containing the other
two — so `A - B` is strictly increasing across the whole span §7 uses. This gap was
present in V1 and was found by TOTO on review.

## 5. Lemma 2 (expansion with explicit remainder)

*For `t >= 2`, `|W| <= 24` and `tx <= 1/2`,*

```
log(A/B) = (tW/24) x^2 + (t(t^2-1)/24) x^3 + E,       |E| <= 3 t^5 x^4.
```

Write `z_i = s_i x + d_i x^2` and `r_i = -h_i^2 x^2`, so that
`log(A/B) = sum_i [log(1+z_i) - log(1+r_i)]`. Under the hypotheses, `|z_i| <= tx <= 1/2`
and `|r_i| <= t^2 x^2 <= 1/4`.

Expanding `log(1+z) = z - z^2/2 + z^3/3 + R` with `|R| <= |z|^4 / (4(1-|z|))`, and
`-log(1+r) = -r + S` with `|S| <= |r|^2 / (2(1-|r|))`, and summing with the identities
of §3, the terms through `x^3` are

```
x^1 :  sum_i s_i = 0
x^2 :  sum_i (d_i - s_i^2/2) + sum_i h_i^2  =  tW/24
x^3 :  sum_i (s_i^3/3 - s_i d_i)            =  t(t^2-1)/24
```

The `x^2` coefficient is the arithmetic heart of the argument: every dependence on `t`
cancels and only `W` survives.

The terms of order `x^4` and above, per factor, in units of `t^4 x^4`:

| source | bound |
| --- | --- |
| `d^2 x^4 / 2` from `z^2/2` | 1/2 |
| `s^2 d x^4` from `z^3/3` | 1/4 |
| `s d^2 x^5` from `z^3/3` | `tx/2 <= 1/4` |
| `d^3 x^6 / 3` from `z^3/3` | `t^2x^2/3 <= 1/12` |
| `sum_{m>=4} z^m/m` | 1/2 |
| `sum_{m>=2} r^m/m` | 2/3 |
| **total** | **9/4 < 3** |

Multiplying by the `t` factors gives `|E| <= 3 t^5 x^4`. ∎

## 6. Lemma 3 (the arithmetic bracket)

*For each residue class of `t` modulo 6 there is an open interval `(-L, R)` containing
no attainable value of `W`, with*

```
t = 0 (mod 6) : (-11,  1)      t = +-1 (mod 6) : (-24, 0)
t = +-2 (mod 6): ( -3,  9)      t = 3   (mod 6) : ( -8, 16)
```

*so `L ∈ {3,8,11,24}` and `R ∈ {0,1,9,16}`, and in particular `|W| <= 24` at every
endpoint.*

*Proof, without any enumeration.* Modulo 24 the term `-24w` vanishes and `-30 ≡ -6`, so

```
W ≡ 6(v^2 - w^2) + 5(t^2 - 1)   (mod 24).
```

The value of `6(v^2 - w^2) mod 24` depends only on `v^2 - w^2 mod 4`, and squares are
`0` or `1` mod 4. The parity tie `v + w ≡ 1 + t (mod 2)` then forces:

- `t` **odd** ⟹ `v, w` have the same parity ⟹ `v^2 ≡ w^2 (mod 4)` ⟹ the term is `0`;
- `t` **even** ⟹ opposite parities ⟹ `v^2 - w^2 ≡ ±1 (mod 4)` ⟹ the term is `6` or `18`.

Combining with `5(t^2-1) mod 24`, which takes the values below on each class:

| `t mod 6` | `5(t^2-1) mod 24` | parity term | `W mod 24` | excluded interval |
| --- | --- | --- | --- | --- |
| 0 | 7, 19 | 6, 18 | **1, 13** | `(-11, 1)` |
| 1, 5 | 0 | 0 | **0** | `(-24, 0)` |
| 2, 4 | 3, 15 | 6, 18 | **9, 21** | `(-3, 9)` |
| 3 | 16 | 0 | **16** | `(-8, 16)` |

No integer in the stated open interval is congruent to an attainable residue, in any
class. ∎

This replaces the full-period enumeration used in V1. The conclusion is identical; the
**evidence class is not** — the bracket is now DERIVED rather than MEASURED, and the
proof as a whole no longer contains a computational step. The derivation is TOTO's.

**The modulus matters.** The congruence `W ≡ 5(t^2-1) (mod 6)`, which is automatic, is
*not* sufficient: it leaves attainable-looking integers strictly inside the interval in
every residue class — `-5` at `t ≡ 0`; `-18, -12, -6` at `t ≡ ±1`; `3` at `t ≡ ±2`;
`-2, 4, 10` at `t ≡ 3`. A reader who reconstructs the bracket at modulus 6 will
conclude §7 is broken. It is the mod-24 enumeration that empties the interval.

Note also that `W = 0` is the non-negative endpoint exactly when `t ≡ ±1 (mod 6)` — the
class in which `5(t^2-1) ≡ 0 (mod 6)` makes `W = 0` admissible. The separate treatment
of `W = 0` in §7 is therefore required for a third of all `t`, not defensive.

## 7. Proof of the theorem

Suppose a solution has `Q >= 100 t^2`. Then `tx <= 1/2` and `Q >= 2t`, so Lemmas 1 and 2
apply at every bracket endpoint, where `|W| <= 24` by Lemma 3.

Dividing the conclusion of Lemma 2 by `t x^2 / 24`,

```
(24 / (t x^2)) log(A/B) = W + (t^2 - 1) x + err,     |err| <= 72 t^4 x^2 <= 72/10^4.
```

**Lower endpoint `W = -L <= -1`.**
`<= -1 + (t^2-1)/(100t^2) + 72/10^4 <= -1 + 1/100 + 0.0072 < 0`, so `A < B`.

**Upper endpoint `W = R >= 1`.**
`>= 1 + 0 - 72/10^4 > 0`, so `A > B`.

**Degenerate upper endpoint `W = 0`.** Here the `x^2` term vanishes and the degree
drops, so divide by `t x^3 / 24` instead:

```
(24 / (t x^3)) log(A/B) >= t^2 - 1 - 72 t^4 x >= t^2 - 1 - 0.72 t^2 = 0.28 t^2 - 1 > 0
```

for `t >= 2`, so `A > B` here too.

By Lemma 1 the function `A - B` is strictly increasing in `W` on this range, and it is
negative at `W = -L` and positive at the non-negative endpoint. Hence its unique zero
lies strictly between them. A solution has `A = B`, so its `W` lies strictly inside
`(-L, R)` — and Lemma 3 says no attainable `W` does. Contradiction.

Therefore `Q < 100 t^2`. Finally, `k >= 1` and `n >= 2k + 3t` give
`Q = n - k - t + 1/2 >= (n + t + 1)/2`, whence

```
n <= 2Q - t - 1 < 200 t^2.   ∎
```

## 8. What is verified computationally, and how

A certificate accompanies this document:
`Execution/Research/CLAUDE/tools/singmaster_r23_review.py`. It exits non-zero on any
failure and prints every population size itself rather than relying on prose. Current
run: 12 checks, all passing, exit 0.

| checked | scope | method | evidence class |
| --- | --- | --- | --- |
| the two retained coefficients of Lemma 2 | `t = 2..60`, 8 bracket `W`, 472 polynomials | exact rationals | MEASURED over the range; DERIVED for all `t` via the §3 identities |
| `|s|<=t/2`, `|d|<=t^2`, `|h|<=t` | `t = 2..200` | exact rationals | MEASURED |
| `|E| <= 3t^5x^4` | 440 points, `t` to 60, `Q` down to `2t` | 80-digit decimal | MEASURED; worst ratio **0.0337**, at the extreme corner of the hypothesis |
| the three sign cases | `t = 2..200` | exact rationals | MEASURED |
| Lemma 1 | `t = 2..200`, also at `Q = 2t` | exact rationals | MEASURED; DERIVED above |
| no solutions in a box | `4 <= n < 900`, all `t >= 2`, `k >= 1`, **unfiltered** | exact integers | MEASURED, exhaustive in the box; reaches useful `t` only to about 20 |

Lemma 3 no longer appears in this table. In V1 its bracket was established by
enumeration and was the proof's one computational dependency; in V2 it is derived in
three lines and the computations below support the analysis without carrying any step
of the logic.

Independently, the `x^2` coefficient `tW/24` of Lemma 2 coincides with the `Q^{2t-2}`
leading coefficient obtained in an earlier round by a symmetric-function computation on
the product, not by any logarithmic expansion. Two unrelated derivations agreeing on
that coefficient is the strongest single corroboration available here.

## 9. What is **not** claimed

1. **Singmaster's conjecture is not addressed.** This bounds one branch.
2. **The constant 200 is not sharp**, and nothing here suggests it is.
3. **No external referee has seen this.** The review was cross-provider but internal to
   this project, and the reviewer did not reconstruct the derivation independently
   before reading it.
4. **Originality is unresolved, and that is not a claim about correctness.** The
   method — asymptotic expansion with explicit remainder, against a discrete lattice of
   admissible values — is close in spirit to Runge's method and to the standard
   effective techniques in Diophantine equations. A first pass on 2026-11-26 found
   nothing in the `a = b` case; the sweep is unfinished. If the result is already
   known, the theorem is unaffected and only the novelty claim is withdrawn.
5. **Non-canonical solutions are out of scope** (§1), and the box search in §8 is too
   small to say anything about them.
6. **No claim of non-existence beyond `t = 2..20`**, which is proved separately.

## 10. Errors corrected during this work, retained deliberately

Preserved because the sequence is part of the evidence, not an embarrassment to tidy
away.

- A margin reported as `<= 0.136` was read from a table filtered to the rows where the
  argmax was not 1 — the opposite tail of the distribution being bounded. True value
  `3562243/6912000`. *The filter used to select cases excluded exactly the cases the
  conclusion needed.*
- A `j = 2` layer declared "closed" on a scan to `t = 4000` plus a known limit. A
  verified range and an asymptotic direction leave the interval between them unargued;
  the algebraic closure (reducing to `L^2 - 326L + 369 < 0`) is what closes it.
- A count stated as "480 polynomials" where the loop runs 59 values of `t` times 8 of
  `W` = 472. Fixed by making the certificate print its own counts.
- An inability to read a collaborator's derivation diagnosed as "the repository is
  private". The repository had always been private; the actual gap was a missing API
  credential in one container. *Name the missing capability, not the asset.*
- A claim that a branch was on the remote, made from a `git ls-remote` whose `origin`
  was a local directory. *Print the remote before claiming anything about it.*
- **V1 §4 proved positivity only under `|W| <= 24`** and then used monotonicity across a
  range where a solution's `W` need not satisfy that. Closed by Lemma 1b. Found within
  an hour of freezing, which is the argument for freezing: the text stopped moving and
  became attackable.
- **V1 §11 treated prior publication as a way the result could be "wrong".** It is not.
  Correctness and originality are separate axes and V1 collapsed them.

## 11. What a referee is most asked to attack

**Correctness and originality are separate questions and V1 conflated them.** V1 §11
opened "the likeliest way this is wrong is that it is already known", which is not a
coherent statement: if the result turns out to be in the literature, the theorem does
not become false. What changes is the originality assessment, and the two must be
weighed separately. The correction is TOTO's.

**Risks to correctness**, in descending order of the authors' concern:

1. **Lemma 2's remainder table.** The claim is that the six listed sources exhaust the
   terms of order `x^4` and above. Two readers believing an enumeration is complete is
   precisely the failure mode an enumeration has.
2. **The scope hypothesis** (§1) — whether canonical position is the right frame for
   the problem as posed, rather than an artefact of how this programme set it up.
3. **Lemma 1b.** It closes a gap found after V1 was frozen, so it is the newest text
   here and the least examined.
4. **Lemma 3.** Now a short derivation rather than an enumeration, which makes it
   checkable by hand in a few minutes — and therefore the item a referee can dispose of
   fastest, in either direction.

**Risk to originality**, which is separate and currently the larger unknown: the method
— asymptotic expansion with explicit remainder, set against a discrete lattice of
admissible values — is close in spirit to Runge's method and to standard effective
techniques in Diophantine equations. A first literature pass (2026-11-26) against work
citing Jenkins found nothing addressing the `a = b` case; one search is not a sweep, and
the sweep is not finished. If the result proves to be known, the mathematics stands and
only the novelty claim is withdrawn.


---

## Appendix. Changes from V1

| § | change | origin |
| --- | --- | --- |
| 4 | **Lemma 1b added.** V1 proved positivity only for `|W| <= 24` and then used monotonicity across a span where a solution's `W` need not lie in that range. Closed by showing the positivity set is an up-set in `W`, and that a solution's factors equal `(n-i)(k+i+1) > 0` regardless of its `W`. | TOTO, review of V1 |
| 6 | **Lemma 3 is now derived, not enumerated.** Three lines from `W ≡ 6(v^2-w^2) + 5(t^2-1) (mod 24)` and the parity tie. The proof now has no computational step in its logic. | TOTO |
| 8 | Lemma 3 removed from the computational table, with a note on why. | consequence of the above |
| 9.4, 11 | **Correctness and originality separated.** V1 called prior publication a way the result could be "wrong"; it is not. §11 now lists correctness risks and the originality risk apart, and reorders the correctness risks — the remainder table first, Lemma 3 last now that it is a short derivation. | TOTO |
| 10 | The two defects above added to the retained-errors list. | — |

Nothing in §§1, 2, 3, 5, 7 changed. The statement, the expansion, the remainder bound
and the final argument are V1's.
