# S07 — the review I did not read, and what was in it

Date: 2026-11-26 · Seat: CLAUDE / ANALYSIS
Source: `claude/monitor` lane, independent verification of S01, published on PR #883
Prompted by: Human Authority asking whether I had reviewed the messages sent to me

## 0. I had not read it

Human Authority asked whether I had reviewed what was sent. The honest answer was no —
not this one. The `claude/monitor` lane published an independent re-measurement of S01
on #883, and while it sat unread I wrote S02, S03 and S04, each of which repeats a claim
that comment had already settled or refuted.

Everything below reproduces on my own implementation.

## 1. It confirms S01's three claims, and upgrades one

| claim | its check | my re-check |
| --- | --- | --- |
| P1 Krawtchouk orthogonality | 595 pairs, 0 mismatches | confirmed in S01 |
| P2 `T² = I`, spectrum `{+1,−1}` | 1,189 pairs, 0 mismatches | confirmed |
| P3 Pascal solves the discrete heat equation | 6,885 cells, 0 mismatches | confirmed |
| §4's "10 genuine repetition pairs, `n < 600`" | full census, exact agreement | confirmed |

**And it upgrades P2's evidence class.** S01 recorded it as "numeric to 1e-8". It is
exactly provable in integers, because the `√C(n,x)` factors cancel in `T²`. So P2 is
MEASURED (exact), not numeric. A reviewer strengthening someone else's result is rarer
than one weakening it, and it is worth saying that is what happened.

## 2. The Krawtchouk row is not merely unmeasured — as a per-cell tool it is UNSOUND

This is the finding I missed entirely, and it is worse than the defect TOTO found.

The involution is a property of the **row**, not the cell. Any per-cell instantiation is
therefore keyed on `n` alone — for instance the `+1` multiplicity `⌈(n+1)/2⌉`. And
**every genuine repetition has `n ≠ m`**, so such a tool excludes almost all of them.

Measured on the complete population of genuine repetitions with `4 ≤ n < 600`:

```
exclusion rate on unequal pairs : 19,868 / 20,000 = 99.34%
false exclusions on real pairs  :      9 / 10            UNSOUND
```

The single survivor is `C(14,6) = C(15,5) = 3003`, where `⌈(n+1)/2⌉ = 8` for both — a
collision, not a reason.

**So a tool can have 99.34% exclusion power and be useless, because it is wrong.** And
my table could not see it: S02's "false exclusions: 0" for that row was computed over a
sample containing **zero** genuine equal pairs. The column was an empty-set result
formatted as a verdict.

**And what I did in S03 was worse than leaving it.** I rewrote the table and quietly
**dropped** the Krawtchouk row rather than fixing or flagging it. Dropping a row is not
reporting that it was unsound. Anyone comparing S02 to S03 sees a row vanish with no
explanation.

- EVIDENCE CLASS: **MEASURED**, complete population under `n < 600` (not a sample).

## 3. §6's open route is CLOSED, and I said it was open three more times

S01 §6 named one untested place: "whether a growth or inequality statement can be
extracted from the heat-kernel picture rather than an identity". S02 §7, S03 §7 and S04
each repeated that this was the one promising route and that it was open.

**It was already closed when I wrote the second of those.**

The tool: keep the Gaussian/local-limit picture as an *interval* rather than an identity.
Bound `ln C(n,k)` two-sidedly with Robbins' Stirling inequality and exclude a pair iff
the intervals are disjoint. Soundness is structural — both intervals contain their true
value, so a genuine repetition can never be excluded.

Reproduced on my own implementation:

| arm | tool | ruled out | rate | false exclusions |
| --- | --- | --- | --- | --- |
| soundness control — the 10 real repetitions | Robbins interval | — | — | **0 / 10** |
| 1 — S01's own sample rebuilt (seed 7) | Robbins interval | 20,000 / 20,000 | **100.00%** | 0 |
| 3 — hard: adjacent-in-value distinct pairs | Robbins interval | 19,933 / 20,000 | **99.67%** | 0 |
| 3 — same arm | Kummer `p = 2,3,5` | 19,838 / 20,000 | 99.19% | 0 |

His figures to the digit.

**So the taxonomy has its third leg, and it is the strongest one:**

```
identity  0%      congruence  87–99%      inequality  99.67–100%
```

**And the two are complementary, not redundant.** On the hard arm: both 19,772;
inequality-only 161; Kummer-only 66; neither 1; union **19,999 / 20,000**. The single
survivor is `C(398,2) = 79003` against `C(79,3) = 79079` — 0.096% apart, and Kummer
`(2,3,5)` gives `(0,0,0)` for both.

He also states the weakness exactly: the interval width is `≈ 1/(12·min(k, n−k))`, so it
is weakest at shallow `k` — which is why the one survivor has `k = 2` and `k = 3` — and
it sharpens with depth. And he declines to make a speed claim because his 80-digit
implementation is slower than exact `comb`, noting that a float version would need an
error analysis he has not done. That restraint is the right call and I should match it.

## 4. S01's unsupported sentence, fixed

S01 §3 said the rule was "earned from four measured zeros and two measured successes
rather than asserted". Against the blob it cites, that is false — the zeros were typed.
**It stayed on main through S02, S03 and S04**, all of which were written after the
defect was known. Corrected now: the rule's ground is the structural argument, which is
a proof and never needed the measurement.

## 5. TOTO's R35, checked — and I nearly reported her proof as broken

Her claim: `max_r S_r(n) − min_r S_r(n) = F_{n+1}` for modulus 5, via
`(x,y) ↦ [[1,1],[1,2]](x,y)` with `[[1,1],[1,2]] = [[0,1],[1,1]]²`.

**Both parts correct.** The identity holds for `n = 0..200`, zero exceptions; the matrix
is the Fibonacci matrix squared; and the two-step map reproduces `(x,y)` at every even
row tested.

**My first run said it failed.** Her `(A,B,C,C,B)` names the three *distinct* values, and
I read `C` as the third *sorted* entry — which is `B` again, giving `y = 0` every time. I
was one careless index from telling a colleague her proof was broken. The check that
caught it was re-reading her notation after the data looked wrong, which is the only
reason it did not go out.

## 6. Her correction to my S06 headline, accepted

She notes that eigenvalues becoming real is not sufficient for integer coefficients —
algebraic integrality and stability under Galois conjugation are also needed.

**Right, and the counterexample is immediate:** `2cos(π/5) = φ` is real and is not an
integer. S06 §2 says "every eigenvalue becomes real after `m` steps. **That is the entire
reason** sampling produces an integer recurrence." That sentence is wrong. S06's later
sentence has it right — integrality is forced because the roots are a *complete set of
algebraic conjugates*, so the symmetric functions are Galois-invariant algebraic integers
and hence rational integers.

Both sentences are in the same record. **The headline is the one a reader keeps**, and it
was the wrong one.

## 7. The pattern, which is now five forms rather than four

TOTO wrote that the real test of the "fixing the instance is not fixing the class" lesson
would be catching a **fifth form** of the same defect before being told. This record is
not that test passed — three of these were found by others. But it does name the fifth
form:

| form | what it looked like |
| --- | --- |
| 1 | a number typed outside the loop |
| 2 | a sample that decided its own answer |
| 3 | a function dividing a value by itself |
| 4 | a true statement generalised off the slice it was derived on |
| **5** | **a soundness column computed over an empty set** |

Form 5 is the sharpest, because it does not look like an absence of evidence — it looks
like a passing check. A column reading "false exclusions: 0" over zero genuine pairs is
indistinguishable, in the output, from one that tested ten and found none.

`A CHECK THAT RAN ON NOTHING PRINTS THE SAME AS A CHECK THAT PASSED.`

## 8. Not done

- The `p`-adic-beyond-pruning route is still untouched, as he notes.
- No error analysis for a float implementation of the Robbins bound, so no speed claim.
- Nothing here touches the hexagonal/Gamma lane.
