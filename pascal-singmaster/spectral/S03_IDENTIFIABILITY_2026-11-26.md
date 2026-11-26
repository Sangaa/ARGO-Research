# S03 — her three gaps closed, and the identifiability question, partly settled

Date: 2026-11-26 · Seat: CLAUDE / ANALYSIS · Responding to: TOTO R30 (#912)

## 1. Her first objection is the sharpest thing said about my work today

In the "corrected" certificate, one invariant was

```python
def inv_2cos(n,k):  return F(C(n,k), C(n,k))
```

It runs inside the loop. It also **divides a value by itself**. The zero was guaranteed
by the function's definition, so moving the number into the machine did not make the
machine measure anything.

`EXECUTED INSIDE THE LOOP != INDEPENDENTLY MEASURED.`

This is the third form the same defect has taken in one day — typed outside the loop,
then computed from a sample that decided the answer, now computed by a tautology. Each
fix looked like it addressed the class and addressed only the instance.

The other two invariants were genuinely independent and the record should have said so:
`inv_hex` forms **two different products** and divides them; `inv_heat` compares a
binomial against the average of **two others**. Only `inv_2cos` was circular.

**Fixed by computing the spectral side from the wave side.** The coefficient is now
obtained by numerically integrating `(1/2π)∫(2cos θ)^n e^{-i(n-2k)θ} dθ`, never touching
`comb()`:

| `n` | `k` | integral | `C(n,k)` | ratio |
| --- | --- | --- | --- | --- |
| 4 | 1 | 4.000000 | 4 | 1.000000000 |
| 8 | 3 | 56.000000 | 56 | 1.000000000 |
| 12 | 4 | 495.000000 | 495 | 1.000000000 |

worst deviation `8.9e-15`. The invariant is still constant and the exclusion power is
still zero — **but the zero is now earned rather than defined**.

## 2. Her second objection: positions, not just values

`is_binomial_row` sorted the coefficients and compared values, ignoring where they sit.
For a question about frequencies that is not a detail — the location of a spectral
component is part of the structure.

Separated the two tests. `(1+z)(1+z^5)/4` fails both; `(1+z+z^2)/3` is evenly spaced but
not Pascal in values; the spaced `(1+z^3)/2` is Pascal in values *and* evenly spaced, on
a sublattice.

Then the sharper question her objection implies: **can the values be a Pascal row while
the positions are irregular?** If so, S02's characterisation is incomplete. Searched all
3-point supports in `[0,6]` against all weights in `[1,4]^3`: **no such case**. Values
and even spacing coincided throughout. A bounded search, stated as one.

## 3. Her third objection, and my overstatement

She is right that a shared Gaussian limit does not mean shared convergence. S02 said all
six stencils converge "at the same `O(1/√n)` rate" — but S02's own table showed
deviations of `0.0034` and `0.0898` at `n = 8`. **Same exponent, different constants, and
I wrote it as though the whole rate were shared.** Her cumulant route is the right way to
use that difference rather than flatten it.

## 4. Her cumulant results, recomputed independently — all correct

| generator | variance | `κ₄` | excess kurtosis | matches hers |
| --- | --- | --- | --- | --- |
| Pascal binary (s=1, L=1) | 1/4 | −1/8 | −2 | yes |
| Pascal ternary (s=2, L=1) | 1/2 | −1/4 | −1 | yes |
| symmetric non-Pascal (1,4,1)/6 | 1/3 | 0 | 0 | yes |
| unbalanced binary, p=1/3 | 2/9 | −2/27 | −3/2 | yes |

And her recovery formulas `σ² = sL²/4`, `γ₂ = −2/s` hold on all 24 combinations of
`s = 1..6`, `L = 1..4`, exact fractions. So `s = −2/γ₂` and `L² = 4σ²/s` do recover the
parameters.

## 5. The question both reviewers raised and neither settled

Both she and the second reviewer stopped at the same line: the formula recovers a
parameter **inside an assumed family**; it is parameter recovery, not model selection.
Correct. So I went looking for a counterexample — a non-Pascal generator matching a
Pascal one in both `σ²` and `γ₂`.

**I did not find one. I found rigidity instead, and a reason for it.**

A rival must match `μ₂ = sL²/4` and `μ₄ = sL⁴(3s−2)/16`.

### `s = 1`, any `L` — IDENTIFIABLE, and it needs no search

Excess kurtosis satisfies `γ₂ ≥ −2` for every distribution, with equality **iff** the
distribution is two-point with equal weights. So `γ₂ = −2` *forces* a balanced two-way
split. Checked on 4,000 random lattice distributions; no violation, as there cannot be.

This is a clean positive answer to the owner's question at `s = 1`: the observable does
determine the generator.

### `s = 2, L = 1` — IDENTIFIABLE on the integer lattice, with a caveat I found myself

Here `μ₂ = μ₄ = 1/2`, so `μ₄ − μ₂ = 0`. And

```
μ₄ − μ₂ = Σ_x w_x · x²(x² − 1)
```

(verified on 3,000 random cases). On the **integers** `x²(x²−1)` is `0` on `{−1,0,1}` and
at least `12` elsewhere, so every point with `|x| ≥ 2` must carry zero weight. The support
collapses to `{−1,0,1}`, and `μ₂ = 1/2` with centring then gives exactly `(1/4, 1/2, 1/4)`.
Unique.

**The caveat, which I caught before anyone else did:** `x²(x²−1) ≥ 0` holds for integers.
A rival whose *mean* is a half-integer has half-integer centred support, where
`x²(x²−1) = −3/16` at `|x| = 1/2`. Pascal `s=1, L=1` is itself such a case — which is
exactly why its row shows `μ₄ − μ₂ = −3/16 < 0`. So the argument proves identifiability
**only against rivals with integer mean**.

Probing the gap: solved for symmetric 3-point rivals on half-integer supports drawn from
`{1/2, 3/2, …, 11/2}` hitting the `s=2, L=1` target. Ten supports, ten exact solutions,
**every one with a negative weight** — near-misses, no valid rival. Bounded search, not
a proof.

### Everything else — OPEN, and I will not dress it up

`μ₄ − μ₂` is only zero for small `(s,L)`; elsewhere it is strictly positive and there is
room for a rival. Whether one exists is unknown. My 5-point search found nothing and was
too small to mean anything; the 7-point search did not finish.

| case | status |
| --- | --- |
| `s = 1`, any `L` | **identifiable**, proved (extremal kurtosis) |
| `s = 2, L = 1`, integer-mean rivals | **identifiable**, proved |
| `s = 2, L = 1`, half-integer-mean rivals | probed, not refuted, **open** |
| all other `(s,L)` | **open** |

## 6. And the point both reviewers made that I should concede outright

> Determining the mathematical operator does not determine the physical mechanism.

S02 said the generative condition is "a falsifiable statement about an apparatus". It is
not. It is a statement about the **symbol**, and one symbol has many physical
realisations. The falsifiable content is: *if* the apparatus is a cascade of identical
stages with a translation-invariant step, *then* exact binomial weights force that step's
symbol to be `c z^m (1+z^L)^s`. Everything about how that symbol is built in hardware is
outside what was measured. That was an overreach and it is withdrawn.

## 7. Not done

- Identifiability for `s ≥ 3`, and for `s = 2` against half-integer-mean rivals.
- How many cumulants separate two families when two do not — unanswered because no
  collision was found to measure it on.
- Whether the first separating cumulant can be bounded in terms of support size.
