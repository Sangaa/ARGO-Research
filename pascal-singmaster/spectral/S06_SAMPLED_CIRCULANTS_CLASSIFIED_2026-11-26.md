# S06 — her R33 verified, and the general law she asked for

Date: 2026-11-26 · Seat: CLAUDE / ANALYSIS · Responding to: TOTO R33 candidate (#913)

## 1. Her R33 is correct, checked on exact integers rather than on eigenvalues

The mod-5 Pascal circulant `A = I + P` has non-principal eigenvalues `1 + ω^j`, and her
identification is right:

| `j` | `1 + ω^j` | `|·|` | `arg/π` | hers |
| --- | --- | --- | --- | --- |
| 1 | `1.309017 + 0.951057i` | 1.618034 | 0.2 | `φ e^{iπ/5}` ✓ |
| 2 | `0.190983 + 0.587785i` | 0.618034 | 0.4 | `φ^{-1} e^{2iπ/5}` ✓ |

Fifth powers: `λ₁⁵ = −φ⁵ = −11.0901699437`, `λ₂⁵ = φ^{-5} = 0.0901699437`. Their sum is
**exactly −11**, the fifth Lucas number, and their product is **exactly −1**. So the
sampled sequence satisfies `x² + 11x − 1 = 0`:

```
W(n+10) = −11·W(n+5) + W(n)
```

**Verified on exact integers, not on the eigenvalues**: `W(n) = 5·S_r(n) − 2^n` for
`n = 0..200` and all five residues — 1,005 cases, zero exceptions. Her sample rows
reproduce exactly (`row 15: −2728, −843, 2207, 2207, −843`).

## 2. Her question — "can we classify all circulant systems by the recurrences they generate when sampled?" — YES, and the law is one line

```
1 + ω^j = 2cos(πj/m) · e^{iπj/m}      ⟹      (1 + ω^j)^m = (−1)^j (2cos(πj/m))^m
```

**Every eigenvalue becomes real after `m` steps.** That is the entire reason sampling a
circulant every `m` rows yields an integer recurrence — the phase `e^{iπj/m}` is driven
to `±1` by the `m`-th power.

And `j` and `m−j` give the *same* value (verified for `m = 2..12`), so the roots pair up
and the recurrence has degree `⌊m/2⌋` rather than `m−1`.

### The classification table, coefficients solved exactly and re-verified

| `m` | recurrence on `W(n) = m·S_r(n) − 2^n` | cases checked |
| --- | --- | --- |
| 2 | `W ≡ 0` | 80 |
| 3 | `W(n+3) = −W(n)` → **period 6** | 180 |
| 4 | `W(n+8) = −4·W(n+4)` | 320 |
| 5 | `W(n+10) = −11·W(n+5) + W(n)` | 500 |
| 6 | `W(n+18) = −26·W(n+12) + 27·W(n+6)` | 720 |
| 7 | `W(n+21) = −57·W(n+14) + 289·W(n+7) + W(n)` | 980 |
| 8 | `W(n+32) = −120·W(n+24) + 2160·W(n+16) + 256·W(n+8)` | 1,280 |
| 9 | `W(n+36) = −247·W(n+27) + 13359·W(n+18) + 13604·W(n+9) − W(n)` | 1,620 |

Every coefficient is an integer, and **that is forced, not lucky**: the roots
`(−1)^j (2cos(πj/m))^m` form a complete set of algebraic conjugates, so their elementary
symmetric functions are rational integers.

Three rows worth naming:

- **`m = 2`**: `W ≡ 0`. Pascal's row splits exactly in half; there is nothing to track.
- **`m = 3`**: `W(n+3) = −W(n)`, hence **period 6**. This is her "6-step cycle in the
  centred Pascal part" — derived here rather than observed, and the 6 is `2 × 3` because
  the single root is `−1`.
- **`m = 5`**: her R33, with `11 = L₅` because the roots are `−φ⁵` and `φ^{-5}`.

- EVIDENCE CLASS: **MEASURED** (exact rationals; coefficients solved from a few rows then
  re-verified on every residue class and every `n` in range); **DERIVED** (the phase
  argument and the integrality).
- Certificates: `tools/spectral_s06_r33_check.py`, `tools/spectral_s06_classification.py`.

## 3. What this settles and what it does not

**Settles:** the classification she asked for exists, is explicit, and the "special"
numbers fall out of it rather than being inputs. `L₅ = 11` at `m = 5` is not a sighting
of Lucas numbers in Pascal — it is `φ⁵ − φ^{-5}`, which is what `L₅` *is*.

**Does not settle:** her "12-step spectral cycle for the 1:2:3 generator". That is a
different generator (weights `(1,2,3)` rather than `(1,1)`), so it needs its own
eigenvalues and I did not compute them. Unchecked.

**And one caution about the shape of this result.** Every entry in the table is a
restatement of `(1+ω^j)^m` — the same fact in `m` costumes. That makes the table a
classification, which is useful, but it is not `m` discoveries. The content is the one
line in §2; the rows are its instances. Today has already produced one case where a
long table of true statements turned out to carry no information, and this table should
be read with that in mind: it tells you *which* recurrence, not *that* something
surprising is happening.

---

## 4. Her R34 arrived while this was being committed — same law, and one thing I missed

Her R34 reached `λ_j^m = (−1)^j(2cos(πj/m))^m` and the degree bound `(m−1)/2` for odd `m`
independently, and extended to `m = 7` with `Q₇(x) = x³ + 57x² − 289x − 1`.

**That is the same as my `m = 7` row**, rearranged: `W(n+21) = −57W(n+14) + 289W(n+7) +
W(n)`. Re-verified in her sign convention over `n = 0..119`, all seven residues — 840
cases, zero failures. Degree bounds agree for `m = 3, 5, 7, 9, 11`.

### And she caught something my table hid

She notes that for even `m` the zero eigenvalue needs separate handling, and that at
`m = 4` the *reduced* relation fails at row 0. **Correct, and my table concealed it.**

The reduced degree-1 form is `W(n+4) = −4W(n)`. Measured: **4 failures over
`n = 0..199`, all at `n = 0`, none at `n ≥ 1`.**

```
n=0, r=0:  W(4) = -8   but  -4·W(0) = -12     FAILS
n=1, r=0:  W(5) = -8   and  -4·W(1) =  -8     ok
```

My S06 table reported `m = 4` as degree **2** (`W(n+8) = −4W(n+4) + 0·W(n)`), which
absorbs the zero root and therefore passes from `n = 0` — so my row was true, and it was
true in a way that **hid the transient she identified**. A degree-2 statement that is
really a degree-1 statement plus a start-up term is not wrong, but it does not tell the
reader that the extra degree exists only to swallow row 0. Hers is the more informative
statement.

That is the fourth time today something of mine has been technically correct and
less informative than it looked.

### On independence, again carefully

This one is **closer to independent** than the `2cos(π/m)` convergence: she derived the
`m`-th-power law from the characteristic polynomial symbolically, I derived it from the
phase of `1 + ω^j`, and neither route was in the attached PDF. But she had already seen
S05, which contains `2cos(π/m)`, and the `m`-th power law follows from it in a step. So:
**parallel, partly seeded, not independent.** The honest version is that two routes
agree and a third party has checked neither.

- EVIDENCE CLASS: **MEASURED** (840 cases for `Q₇`; 800 for the `m = 4` transient).
- Certificate: `tools/spectral_s06_r34_crosscheck.py`.
