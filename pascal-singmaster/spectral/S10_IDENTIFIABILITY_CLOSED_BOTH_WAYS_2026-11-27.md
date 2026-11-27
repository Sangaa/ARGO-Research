# S10 — S03's open identifiability cases, closed; one positively, one negatively

Date: 2026-11-27 · Seat: CLAUDE / ANALYSIS · Closing: `S03 §5` and `S03 §7`
Status: `TWO OPEN CASES SETTLED / ONE S03 CLAIM NARROWED / NO LEMMA OF THE REFEREE BOUND TOUCHED`

`S03` recovered `(s, L)` from `(σ², γ₂)` **inside** the Pascal family, and both reviewers
made the same objection: that is parameter recovery, not model selection. `S03` accepted it,
proved identifiability for `s = 1` and for `s = 2, L = 1` against integer-mean rivals, and
left two cases open:

| `S03`'s table | |
| --- | --- |
| `s = 2, L = 1`, half-integer-mean rivals | probed, not refuted, **open** |
| all other `(s, L)` | **open** |

Both are now settled, **in opposite directions**. The whole result is reproducible from
`tools/s10_identifiability.py`, which exits 0 and prints every figure below.

---

## 1. The answer in one table

| case | verdict | basis |
| --- | --- | --- |
| `s = 1`, any `L` | identifiable | proof — `S03`, unchanged |
| `s = 2, L = 1`, integer-mean rival | identifiable | proof — `S03`, unchanged |
| **`s = 2, L = 1`, half-integer rival** | **identifiable** | **proof, here** (was open) |
| `s = 2, L = 1`, any unit lattice, offset `β` | no rival | **LP-measured**, here |
| `s = 2, L = 1`, off every lattice | **not** identifiable | explicit witness, here |
| **`s ≥ 3`, `L = 1`** | **not identifiable** | **explicit witnesses**, here (was open) |

The direction is the point. `S03` wrote of `s ≥ 3` that *"`μ₄ − μ₂` is strictly positive and
there is room for a rival. Whether one exists is unknown."* **The room is real, and the
rival is explicit.** So `σ² = sL²/4` and `γ₂ = −2/s` are parameter recovery and **not** a
model-selection test for `s ≥ 3`. The reviewers were right, for a sharper reason than
either of them gave.

---

## 2. The open case, closed by a relaxation rather than a search

`μ₂` and `μ₄` depend only on `m = x²`. So **drop the mean-zero constraint** — that enlarges
the feasible set, so any lower bound it gives holds a fortiori. What is left is a linear
objective under two equality constraints, whose optimum sits at a vertex with at most two
support points, and for a two-point mix bracketing the mean,

```
V(m₁, m₂) = (m₁ + m₂)/2 − m₁·m₂ ,   m₁ ≤ 1/2 ≤ m₂ .
```

`∂V/∂m₂ = 1/2 − m₁ ≥ 0` and `∂V/∂m₁ = 1/2 − m₂ ≤ 0`, so `V` is minimised by the pair that
brackets `1/2` **most tightly**. That pair is computable from the lattice. **No search.**

On `ℤ + 1/2` the squared values are `{1/4, 9/4, 25/4, …}`, so `m₁ = 1/4`, `m₂ = 9/4` — the
lattice holds nothing between them — and

```
V = 5/4 − 9/16 = 11/16 > 1/2 .
```

Symmetry makes the dropped constraint free there, so this is a proof: **no law on `ℤ + 1/2`
with `μ₂ = 1/2` can have `μ₄ = 1/2`.** The gap is exactly `3/16`.

**`3/16` is the same number `S03` found as the caveat** — the value of `x²(x² − 1)` at
`|x| = 1/2`, the reason its integer argument did not extend. The obstruction and its
resolution are one quantity seen from two sides.

### How far the proof reaches, exactly

For `β ∈ [1 − 1/√2, 1/2]` the bracketing pair is `(1−β)²` and `(1+β)²`, so with `u = β²`,
`V = 3u − u²`, and `V > 1/2` iff `u > (3 − √7)/2`. The relaxation therefore **proves**
exclusion for every offset above

```
β* = √((3 − √7)/2) = 0.4208614314… ,
```

which is 15.8 % of the offset range `(0, 1/2]` — and it contains the case `S03` left open.

### Below `β*`, it is measurement and is labelled as such

`EVIDENCE CLASS: MEASURED.` 200 offsets in `(0, 1/2]`, step `1/400`, LP on the window
`|x| ≤ 40` with the mean-zero constraint in place: `min μ₄ > 1/2` at every one. The
minimiser is, every time, the **three lattice points nearest the origin**, and the attained
value is

```
min μ₄(β) = 1/2 + 3β⁴ ,
```

exact on that support (checked in fractions at `β = 0, 1/4, 1/3, 2/5, 1/2`; worst LP
deviation `2.5e-16`). **The optimality of that support is LP evidence, not a theorem**, and
so the closed form is a measured regularity rather than a proved formula. It is not promoted.

### The limit of the whole result: the lattice is load-bearing

Off a lattice a rival exists, and it is small enough to write down. A symmetric four-point
law with mass `P/2` at each of `±1/2` and `Q/2` at each of `±u` forces
`8u⁴ − 14u² + 3 = 0`, hence `u² = 3/2`:

```
mass 2/5 at each of ±1/2 ,   mass 1/10 at each of ±√(3/2) ,
μ₂ = 1/2 ,  μ₄ = 1/2  — both on target ;  μ₆ = 11/16 against Pascal's 1/2 .
```

All four weights are strictly positive and `√(3/2) − 1/2` is irrational, so this law lies on
no unit lattice. **The identifiability claim is conditional on the lattice**, and `S03`'s
word *"lattice distributions"* is doing work that `S03` did not flag.

---

## 3. The other open case, closed the other way

A symmetric law on `{0, ±1, ±2}` with `w(±1) = a`, `w(±2) = b` has `μ₂ = 2a + 8b` and
`μ₄ = 2a + 32b`. Matching Pascal's `s/4` and `s(3s−2)/16` gives, in closed form,

```
b = s(s−2)/128 ,   a = s(6−s)/32 ,   w(0) = (3s² − 22s + 64)/64
```

and `3s² − 22s + 64` has negative discriminant, so `w(0) > 0` for every `s`. Valid for
`2 ≤ s ≤ 6`; at `s = 2` and `s = 4` it lands **on** Pascal (for even `s` Pascal already
lives on the integer lattice), and at `s = 3, 5, 6` it lands beside it.

### The witness at `s = 3`, written out

| | support | weights | `μ₂` | `μ₄` | `μ₆` |
| --- | --- | --- | --- | --- | --- |
| Pascal `(1,3,3,1)/8` | `±1/2, ±3/2` | `3/8, 1/8` | `3/4` | `21/16` | `183/64` |
| **rival** | `0, ±1, ±2` | `25/64, 9/32, 3/128` | `3/4` | `21/16` | **`57/16`** |

Same variance, same excess kurtosis `−2/3`, different law, different lattice. Two cumulants
do not tell them apart.

### And for every `s` up to 20

LP over symmetric integer-lattice laws, `|x| ≤ K`:

- `s = 1` — **infeasible**: no symmetric integer-lattice law has `μ₂ = 1/4, μ₄ = 1/16` at
  all, consistent with `S03`'s extremal-kurtosis proof.
- `s = 2` — feasible, and the only vertex found is Pascal, consistent with `S03`'s proof.
  (One vertex is not a uniqueness proof; `S03`'s argument is what carries that row.)
- **`s = 3 … 20` — a non-Pascal rival every time**, `K = 3` up to `s = 12` and `K = 4`
  beyond. Each witness's moments were re-measured against the target to `< 1e-9`.

At `s = 4` the two constraints leave a one-parameter family and the closed form merely
happened to pick the Pascal point in it; the LP picks another. So `s = 4` is **not**
identifiable either — the closed form's coincidence there was not evidence of rigidity.

---

## 4. The question `S03` could not measure, now measurable

`S03 §7` asked: *"How many cumulants separate two families when two do not — unanswered
because no collision was found to measure it on."* The `s = 3` collision above is one.

**On this collision: two even moments do not separate, three do.** `μ₆` differs by a factor
of `1.245902…` (`57/16` against `183/64`). One collision is not a theorem about the family,
and nothing is claimed beyond it — but the question is no longer unanswerable for want of
an instance.

---

## 5. What this does and does not touch

**It does not touch the referee bound.** Nothing here is a lemma, a constant or a step of
`referee/`. This is the spectral side-lane that `S01`–`S09` live in.

**It narrows one `S03` claim.** `S03 §5` presented the rigidity it found as evidence that
the observable may determine the generator. For `s ≥ 3` it does not, and the sentence
*"I found rigidity instead, and a reason for it"* should be read as scoped to `s ≤ 2`.
`S03`'s own table already said `s ≥ 3` was open; what changes is that the open case has
resolved **against** the hopeful reading.

**One thing I should state plainly about my own method.** Every negative result here was
easy — a 5-point symmetric support and two linear equations. `S03` searched 5-point and
7-point supports, found nothing, and reported the 7-point search as unfinished. So the
honest first question is not *"why is this new?"* but *"why did the earlier search miss
something this cheap?"*

I can offer a hypothesis and I am labelling it as one, because `S03` did not record the
support its searches ranged over: the `s = 3` rival sits on the **integers** while Pascal
`s = 3` sits on the **half-integers**, so a search that enumerated supports on Pascal's own
lattice could not have contained it. That would explain the miss exactly. `UNVERIFIED` —
`S03` states the support sizes (5-point, 7-point) and not the lattice, and the search code
was not preserved, so this cannot be checked from the record and I am not asserting it.

What is not a hypothesis is the lesson: a finished search over the wrong index set reports
the same "nothing found" as a finished search over the right one. **Absence of a witness is
evidence only about the window searched**, and `S03` did say its searches were "too small to
mean anything" — that caution was correct and this is what it was protecting against.

---

## Evidence

- `tools/s10_identifiability.py` — one file, exits 0, prints every number above. Exact
  fractions wherever the claim is exact; `scipy.optimize.linprog` with its window and grid
  stated wherever it is not.
- `EVIDENCE CLASS: MEASURED` — the Pascal closed forms on 32 `(s,L)` pairs; the exact
  attained `μ₄` on the three-point support; the `s = 3 … 20` LP witnesses and their moment
  residuals; the 200-offset scan.
- `EVIDENCE CLASS: DERIVED` — the vertex argument behind `V(m₁, m₂)`, the `β*` threshold,
  the closed forms for `a`, `b`, `w(0)`, and the `u² = 3/2` off-lattice witness. Each is a
  short derivation a second reader can redo from the text; each is also re-measured
  numerically by the script.
- `EVIDENCE CLASS: BOUNDED_PROXY` — the claim that `min μ₄(β) = 1/2 + 3β⁴` for **all**
  `β`, and the claim that no rival exists for `0 < β < β*`. Both rest on the LP's choice of
  minimiser over a finite window and a finite grid.
- Sources read: `spectral/S03_IDENTIFIABILITY_2026-11-26.md` §5 and §7 (the open items and
  the `3/16` caveat), `spectral/S02_HER_FIVE_CORRECTIONS_AND_THE_GENERATIVE_CONDITION_2026-11-26.md`
  (the recovery formulas).
