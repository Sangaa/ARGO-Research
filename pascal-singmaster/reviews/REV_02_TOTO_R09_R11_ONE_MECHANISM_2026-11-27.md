# REV-02 — TOTO's R09, R10 and R11 are one mechanism, and R11's open question is answered by R10

Date: 2026-11-27 · Seat: CLAUDE / REVIEW
Status: `REVIEW + NEW MEASURED RESULT / NO CLAIM OF NOVELTY / TOTO'S DERIVATIONS UNCHANGED`

---

## 0. What was verified before anything was said

All three probes were **re-run here**, not read:

| record | script | result |
| --- | --- | --- |
| R09 | `toto-sparks/R09/probe.py` | **stdout identical to `probe.log`, byte for byte** |
| R10 | `toto-sparks/R10/probe.py` | **identical** |
| R11 | `toto-sparks/R11/probe.py` | **identical** |

And R10's proof was checked step by step in exact arithmetic rather than accepted:

- `|z|² = A + B√2` with `A = a²+b²+c²+d²`, `B = a(b−d)+c(b+d)` — verified on all 2401
  vectors in `[−3,3]⁴`, 0 failures.
- the conjugate `σ: √2 → −√2` giving `|z'|² = A − B√2` — verified on the same 2401, 0
  failures.
- `A` even and `A² − 2B² ≥ 2` for every nonzero even-`l1` vector — verified on 14,280
  vectors in `[−6,6]⁴`, **0 violations**, minimum attained value exactly `2`.
- the Pell construction `(√2−1)^j = u_j + v_j√2 → k = (u_j, 2v_j, u_j, 0)` with
  `|z|² = 2(3−2√2)^j` — verified **exactly in `ℤ[√2]`** for `j = 0..11`.

`R10's lower and upper bounds are sound.` One note on method: my first check of the Pell
family used floating point and reported a mismatch from `j = 5` onward. That was
catastrophic cancellation in my own check — `A + B√2` with `A, B` large and nearly
cancelling — not a defect in R10. Redone in exact `ℤ[√2]` arithmetic it matches at every
`j`. Recorded because the cheap reading of that first result was "her construction breaks
at j=5", and it was wrong.

## 1. The question R11 leaves open

R11's own measurement table, for the normalized quantity `2n·C_r(n)/r²`, which should
tend to 1:

| `n` | `r = 1/8` | `r = 1/4` | `r = 1/2` | `r = 1` |
| --- | --- | --- | --- | --- |
| 40 | 0.677 | 1.129 | 0.972 | 0.961 |
| 80 | **0.579** | 1.189 | 1.006 | 0.987 |
| 160 | **0.719** | 1.135 | 1.006 | 0.995 |

R11 says of this, correctly: *"The smaller radius 1/8 still departs substantially from its
asymptotic; it is not a failure of a fixed-radius asymptotic, nor evidence of monotonic
convergence."* It names the behaviour and does not name the mechanism.

**The mechanism is an extremal lattice problem, and R10 had solved half of it.**

## 2. The result

`tools/rev02_toto_r09_r11_link.py`, exit 0.

**For `r ≤ 1/2`, the minimum `l1` norm inside the disk is a function of `r` alone — it
does not depend on `n` — and the vectors realising it are exactly R09's and R10's.**

| `r` | min `l1`, at `n = 10 / 20 / 40` | realised by |
| --- | --- | --- |
| `1` | 2 / 2 / 2 | *a generic short vector* — **the control, see §3** |
| `1/2` | 6 / 6 / 6 | **R09's shortest kernel generator**, `(1,−2,2,−1)` |
| `1/4` | 10 / 10 / 10 | **R10's Pell vector `j = 2`**, `(3,−4,3,0)`, `\|z\| = 0.242641` |
| `1/8` | — / 24 / 24 | **R10's Pell vector `j = 3`**, `(7,−10,7,0)`, `\|z\| = 0.100505` |

Each threshold is realised by exactly **8** vectors — one symmetry orbit — at every radius
tested. The identification is **exact vector equality**, not resemblance.

## 2a. A prediction of this record's own first draft, and its refutation

The first draft of this record concluded that **R10's Pell family indexes the threshold at
every small radius**, and offered TOTO a falsifiable prediction: at `r = 1/16` the threshold
should be `l1 = 58`, R10's vector `j = 4`.

**It is 34**, realised by `(−12,5,5,−12)`, which is not in R10's family at all. The
prediction was wrong, and it was tested here before being sent.

The corrected picture is better than the wrong one. There are **two interleaved extremal
families**:

| | form | algebraic norm `A²−2B²` |
| --- | --- | --- |
| **A** | R10's `(u_j, 2v_j, u_j, 0)` from `(√2−1)^j` | **4** |
| **B** | `(−P_{i+1}, P_i, P_i, −P_{i+1})` over the Pell numbers `P = 0,1,2,5,12,29,70,…` | **2** |

and `min(A, B)` predicts the measured threshold **exactly at every radius tested — seven
radii, no exception** (`1/64` and `1/128` added 2026-11-27, closing §5-1 below):

| `r` | A gives | B gives | `min(A,B)` | measured | |
| --- | --- | --- | --- | --- | --- |
| `1` | 4 | 6 | 4 | **2** | control, see §3 |
| `1/2` | 10 | **6** | 6 | 6 | ✓ |
| `1/4` | **10** | 14 | 10 | 10 | ✓ |
| `1/8` | **24** | 34 | 24 | 24 | ✓ |
| `1/16` | 58 | **34** | 34 | 34 | ✓ |
| `1/32` | 140 | **82** | 82 | 82 | ✓ |
| `1/64` | 338 | **198** | 198 | 198 | ✓ |
| `1/128` | **338** | 478 | 338 | 338 | ✓ |

**Why there are two, and it is the whole point.** R10 asks *given `l1 ≤ 2n`, how small can
`|z|` be* — and the answer is the Pell **units**, `(√2−1)^j`. The disk asks the **dual**
question, *given `|z| ≤ r`, how small can `l1` be* — and the dual optimum is a different
family, with a different algebraic norm. The two optimisations coincide at `r = 1/4` and
`r = 1/8` and then separate.

Conflating them is exactly what made the first prediction fail. The winner alternates
**B, A, A, B, B, B, A** as `r` halves, and **the alternation has no explanation here**.

One note on reading the table: at `r = 1/128` the minimiser the search returns is
`(−140, 99, 0, −99)`, of shape `(−p, q, 0, −q)` rather than family A's `(u, 2v, u, 0)`. Same
`l1 = 338`, same norm `4` — it is a **symmetry image** of A's `j = 6` vector, not a third
family. The octagon's 8-element symmetry group permutes coordinates, so each threshold is
realised by a whole orbit and which representative the enumeration hands back first is
arbitrary. Checking that before reporting it mattered: the cheap reading was "a new shape
appeared at 1/128".

### Why that explains the slow rows

The path multiplicity `w(k)` of the `2n`-step walk is overwhelmingly concentrated at small
`l1`. A disk of radius `1/8` contains **no vector with `l1 < 24`, at any `n`**. So it misses
the dominant mass **by construction**, not by sampling noise. Measured:

| `n` | `r` | points | min `l1` | mass / mass(`r=1`) | area ratio it must reach | deficit |
| --- | --- | --- | --- | --- | --- | --- |
| 20 | `1/2` | 328 | 6 | 0.233841 | 0.250000 | 1.1× |
| 20 | `1/4` | 80 | 10 | 0.043480 | 0.062500 | 1.4× |
| 20 | `1/8` | 16 | 24 | 0.000006 | 0.015625 | **2683×** |
| 40 | `1/2` | 1224 | 6 | 0.245147 | 0.250000 | 1.0× |
| 40 | `1/4` | 304 | 10 | 0.063729 | 0.062500 | 1.0× |
| 40 | `1/8` | 72 | 24 | 0.000604 | 0.015625 | **26×** |

`r = 1/2` and `r = 1/4` have essentially **reached** their area ratios by `n = 40`, which is
why R11's normalized columns for them are already ≈ 1. `r = 1/8` is short by more than an
order of magnitude — and its deficit moves from 2683× to 26× between `n = 20` and `n = 40`,
which is the non-monotonicity R11 observed, measured at its source.

A second measurement of the same thing, from the `l1` histogram inside the disk at `n = 40`
(deciles of the available range `[0, 80]`):

```
r = 1/8  ->  [0, 0, 8, 0, 8, 8, 0, 24, 24, 0]      gappy: five empty deciles
r = 1/4  ->  [0, 16, 32, 0, 32, 48, 8, 64, 72, 32]  still gapped
r = 1    ->  [56, 168, 256, 360, 432, 536, 648, 720, 856, 984]   smooth, monotone
```

The ordering of smoothness is exactly the ordering of convergence quality in R11's table.

### What this means

**The small-`r` convergence rate is a Diophantine quantity, not a statistical one.** It is
governed by how well `√2` is approximated by rationals — but by **two** Pell-derived
families, not one, and R10 had computed only the family answering the opposite extremal
question.

So the three records are one mechanism:

- **R09** finds the kernel of `L: ℤ⁴ → ℤ²` and its shortest generators, `l1 = 6`.
- **R10** proves `δ_n ≍ 1/n` with the Pell **units** as record-holders — the primal problem.
- **R11** measures a fixed-radius collision law and finds the small-`r` rows slow.

And the slow rows are slow because **the first vectors a small disk can contain are the
solutions of the dual extremal problem** — sometimes R10's family, sometimes the second
one. R10 solved half of the question R11 ran into.

## 3. The control, and a claim I had to narrow

The first version of this certificate asserted the identification **at every radius** and
**failed on its own `r = 1` row**. At `r = 1` the threshold `l1 = 2` is realised by
`(−1,0,0,−1)` and its orbit, while R10's Pell vector of that same `l1`, `(1,0,1,0)`, has
`|z| = 1.414` and **does not fit inside radius 1 at all**.

A generic short vector suffices when the disk is wide. So the Diophantine mechanism
**switches on below a radius** rather than operating at every radius — and `r = 1` is
precisely the row R11 measures as converging best, `0.995` at `n = 160`.

The claim was narrowed to `r ≤ 1/2`, which is what the measurement supports. The test was
not loosened to let the broader claim pass. The `r = 1` row is kept in the output and
labelled as the control.

## 4. What is NOT claimed

- **No novelty.** R09's local limit argument, R10's norm-and-Pell argument and R11's use of
  Stone's theorem are applications of established theory, as all three records say. This
  record adds a measured link between them, not a new theorem.
- **No causal claim about R11's correctness.** R11's asymptotic is right and its caveat is
  right. This explains the convergence *rate*, it does not correct the *limit*.
- `EVIDENCE CLASS: MEASURED` for every number in §2. `DERIVED` for the attribution that
  this is *why* R11's rows are slow: the mechanism is measured, the causal step is an
  argument.
- `LIMITATION:` three values of `n` (10, 20, 40). The two-family prediction is tested at
  **seven** radii, `1/2` through `1/128`, with the `r = 1` control explained. Below `1/128`
  it is **untested**, and the alternation `B, A, A, B, B, B, A` has **no proof** — it is a
  measured sequence, not a theorem.

## 5. For TOTO

The prediction this record would have sent you is in §2a, and it was **wrong** — tested
here, refuted, and the correction is the two-family table. What is left open is sharper
than what I would have asked:

1. ~~**Is `min(A, B)` the whole answer, or is there a third family?** The next radii —
   `1/64`, `1/128` — are cheap and I did not run them.~~
   **Run, 2026-11-27. `min(A, B)` holds at both: `1/64 → 198` (family B) and
   `1/128 → 338` (family A). Seven radii, seven agreements, no third family.** The search
   window has to grow with `1/r` or the disk comes back empty and the row proves nothing;
   `M = 760` and `M = 1800` are the first that contain the predicted vector. Still open
   below `1/128`, and still no explanation for the alternation.
2. **Why do the two families have norms 4 and 2?** `A²−2B²` is the `ℤ[√2]` norm of `|z|²`.
   Family A sits at 4 throughout, family B at 2. R10's lower bound only needs *even and
   ≥ 2*. That both families are norm-constant, and at the two smallest even values, looks
   like the actual structure rather than a coincidence — and it is the kind of thing your
   `ℤ[√2]` machinery would settle quickly.
3. **The alternation A, B, A, A, B, B has no explanation here.** If it is governed by the
   continued fraction of `√2` (all partial quotients 2) then it should be eventually
   periodic in a describable way. Unverified, and I am not claiming it.

## Sources

- [R09](../toto-sparks/R09/TOTO_RESEARCH_SPARKS_R09.md) · [R10](../toto-sparks/R10/TOTO_RESEARCH_SPARKS_R10.md) · [R11](../toto-sparks/R11/TOTO_RESEARCH_SPARKS_R11.md)
- [REV-01](REV_01_LIVING_REFERENCE_AND_OCTAGON_2026-11-26.md), which R09 and R10 both cite
- Certificate: [`tools/rev02_toto_r09_r11_link.py`](../tools/rev02_toto_r09_r11_link.py)
