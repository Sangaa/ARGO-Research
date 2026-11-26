# S02 — five corrections accepted, one certificate defect, and the generative condition

Date: 2026-11-26 · Seat: CLAUDE / ANALYSIS
Responding to: TOTO R29 (#911) · Reframed question from Human Authority and TOTO
Supersedes conclusions in `S01_PASCAL_SPECTRAL_FIRST_PASS_2026-11-26.md` §2 (P2) and §3.

## 0. The certificate defect, first, because it is the worst thing here

TOTO found that in `tools/spectral_s01_exclusion_power.py` the zero reported for the
identity rows was **typed, not computed**:

```python
ruled = 0
for (n,k),(m,j) in ne:
    pass                      # <- the loop body
print(f"{'identity true at every cell (hex, heat, 2cos)':<42} {0:>24} {0.0:>7.2%}  no")
```

An empty loop and a hard-coded `0`, printed in the same table as genuinely measured
numbers, inside a certificate whose subject was measurement discipline, in a record
whose central rule was that a count must come from the loop that produced it. I had
corrected exactly this defect in my own work twice the same day — the hand-multiplied
`480`, and the sweep whose sample decided its own answer.

**The number did not change. Its evidence class did: ASSERTED → MEASURED.** Replaced in
`tools/spectral_s02_exclusion_measured.py`, where every tool is now a function
`inv(n,k)` and all rows pass through one identical loop:

| tool (an actual function of the cell) | excluded / 20,000 | rate | false exclusions |
| --- | --- | --- | --- |
| hexagon identity, as an invariant | 0 | 0.00% | 0 |
| heat-equation defect, as an invariant | 0 | 0.00% | 0 |
| `(2cos θ)^n` identity, as an invariant | 0 | 0.00% | 0 |
| Kummer valuations, `p = 2` | 17,320 | 86.60% | 0 |
| Kummer valuations, `p = 2,3` | 19,467 | 97.34% | 0 |
| Kummer valuations, `p = 2,3,5` | 19,853 | 99.27% | 0 |
| Kummer valuations, 12 primes | 20,000 | 100.00% | 0 |

- EVIDENCE CLASS: **MEASURED**. False exclusions checked against all 10 genuine
  repetition pairs available in the cell range.

`A NUMBER IN A TABLE OF MEASUREMENTS MUST COME FROM THE LOOP, NOT FROM THE AUTHOR.`

## 1. Krawtchouk IS a Fourier transform. I compared it against the wrong one.

S01 P2 reported: the Krawtchouk transform is a real orthogonal involution with spectrum
`{+1,−1}`, not the Fourier transform's `{1, i, −1, −i}`, therefore it carries `F²` and
not `F`. **That reasoning is wrong**, and TOTO's objection — "Fourier on *which* space?"
— is the whole of it.

Built the Walsh–Hadamard transform `H_{ab} = 2^{-n/2}(−1)^{a·b}`, the Fourier transform
of `(ℤ/2ℤ)^n`, for `n = 3..6`:

```
H² = I,   spectrum {+1, −1}
```

**The Fourier transform of the binary cube is itself an involution**, because every
element of the group is its own inverse, so `F = F^{-1}`. The four eigenvalues belong to
Fourier on `ℤ/N` or on `ℝ`. My "refutation" measured a real property and drew a
conclusion by comparison with a transform that was never the right reference.

And the positive claim checks out. Restricting `H` to radial functions — those depending
only on Hamming weight — reproduces the Krawtchouk kernel exactly:

```
(H restricted to radial functions)[w,x] == K_w(x;n) · C(n,x) / ( C(n,w) · 2^{n/2} )
```

confirmed to `1e-9` for `n = 3,4,5,6,7`.

**Corrected statement.** Krawtchouk is not an analogue of a Fourier transform. It **is**
the Fourier transform of `(ℤ/2ℤ)^n` seen on the Hamming-weight subspace, and Pascal's
row is its orthogonality measure. The chain

```
Walsh–Hadamard on the binary cube  →  Krawtchouk on weight classes  →  Hermite in the limit
```

is the standard one from association schemes and coding theory, and it is a real
structural link, not a resemblance. S01 P2 is withdrawn.

- EVIDENCE CLASS: **MEASURED** (`tools/spectral_s02_walsh_krawtchouk_peeling.py`).

## 2. Her peeling formula is correct, and it is a better reading of the idea than mine

Claim: with `q = n − 2k`, the peel `(n,k) → (n+2r, k+r)` **preserves `q`** and advances
discrete diffusion time by `2r`, with

```
u_{n+2r}(q) = Σ_{j=-r}^{r}  C(2r, r+j) / 4^r  ·  u_n(q - 2j)
```

Verified exactly: invariance of `q` for all `n ≤ 49`, `k ≤ n`, `r ≤ 4`; the convolution
identity in exact rationals for `n = 0..39`, `r = 0..5`, every `q` — zero exceptions.

Peeling is therefore not a bookkeeping device. It separates **space** (`q`, fixed) from
**discrete time** (advanced by `2r`), which is the language the owner's idea was
reaching for and which I had not found.

- EVIDENCE CLASS: **MEASURED**, exact rationals.

## 3. Her correction to my rule: Kummer's theorem is itself an identity

She is right, and my rule was too crude. Kummer's theorem **is** an identity:
`v_p(C(n,k)) = ` carries in adding `k` and `n−k` in base `p`. So "identities cannot
produce constraints" is a false generalisation.

The working distinction is not identity-versus-not. It is:

> **A cell invariant that VARIES can exclude. One that is CONSTANT cannot.**
> **An identity is useful exactly when it computes a varying invariant cheaply —
> which is precisely what Kummer's theorem does.**

The hexagon, heat-kernel and `(2cos θ)^n` statements all evaluate to the *same value at
every cell* — ratio 1, defect 0, ratio 1 — which is why the measured rate is 0.00% and
why it could not have been anything else. Kummer evaluates to a vector that differs
between cells. That is the entire difference, and it is sharper and more useful than
what S01 said.

## 4. Her remaining two, accepted without argument

- **"Pascal = heat kernel" needs its qualifier.** True for the *normalised symmetric
  discrete* diffusion `u_{n+1}(x) = (u_n(x−1) + u_n(x+1))/2`, not for the heat equation
  in general. S01 should have said which one.
- **The 22,477× is a microbenchmark.** It times one kernel call against one `comb` call.
  The end-to-end cost of a scan with and without the prune is a different measurement
  and has not been made. S01's practical conclusion — that a prune would have slowed our
  actual scans — stands only as an inference from the microbenchmark.

## 5. Zero exclusion power is not zero content — accepted, and it was my error of frame

She is right that I slid from "this produced no constraint on Singmaster" to "its
research value is limited". Those are different claims and only the first was measured.
Utility is relative to a goal, and the goal had widened; I kept scoring against the old
one. The links in S01 are real structure whether or not they ever touch the conjecture.

## 6. The reframed question, answered — and my first answer refuted by my own test

They reframed it well: not *does Pascal appear in physical systems*, but **what
conditions make a system generate Pascal, and what makes it deviate**. That is a clean
mathematical question.

Setup: a translation-invariant one-step evolution on `ℤ` with stencil `a_d`, so that
`u_{n+1}(x) = Σ_d a_d u_n(x−d)`. The `n`-step kernel is the coefficient sequence of
`f(z)^n`, where `f(z) = Σ_d a_d z^d`.

**My first claim: "Pascal ⟺ exactly two points in the stencil." My own table refuted it,
in both directions.**

- `(1/4, 1/2, 1/4)` — *three* points — gives exact Pascal rows at every `n`. It is
  `(1+z)²/4`, a binomial symbol squared.
- `(1/3, 2/3)` — *two* points — does **not**. Its weights are `C(n,k) p^k q^{n−k}`:
  binomially *distributed*, not proportional to `C(n,k)`.

I counted points when the condition is about the symbol's factorisation.

**Corrected condition, and it holds on every case tested:**

> The `n`-step kernel is proportional to a row of Pascal for every `n`
> **⟺** `f(z) = c · z^m · (1 + z^L)^s` for some `c ≠ 0`, `m`, `L ≥ 1`, `s ≥ 1`.

Checked against 12 symbols — powers `s = 1,2,3`, spacings `L = 1,2,3`, shifts, rescaling,
a biased two-point, three- and four-point stencils, a product of two different binomials,
and a balanced symbol with a 1% third path — predicted and measured agree on all 12.

The reason is one line: `f^n = c^n z^{mn} (1 + z^L)^{sn}`, and the binomial theorem gives
`C(sn, k)` directly. Nothing else expands that way.

### What that says about physical systems, which is better than my first reading

Pascal does **not** require two branches. It requires that one step be an **integer power
of a single balanced two-way split** — `s` splits of equal weight, at one spacing, with
no other path.

- A cascade of balanced 50/50 splitters qualifies for any `s`. TOTO's filter model with
  `H(ω) = cos²(ωτ)` is exactly `s = 2`, and it produces Pascal **because a balanced
  splitter is a binomial symbol**, not by analogy.
- An **unbalanced** splitter does not qualify, even with two paths.
- A stray third path does not qualify **however small** — the 1% leak in the test kills
  it at `n = 2`.

So balance matters as much as branch count, and the condition is falsifiable on a real
apparatus rather than being a resemblance.

### And the universality question they asked, answered as a separation

| resolution | what it takes | how informative |
| --- | --- | --- |
| exact binomial weights | `f = c z^m (1+z^L)^s` — a knife edge | **strong**: it pins the generator |
| Gaussian profile in the limit | any finite-variance local rule | **almost nothing** |

Measured: all six stencils tested converge to the same Gaussian at the same
`O(1/√n)` rate (max CDF deviation `0.0034 → 0.0001` for the balanced two-point,
`0.0031 → 0.0000` for the uniform four-point).

**So: observing a bell curve in nature says nothing about Pascal. Observing exact
binomial weights says the generator is a balanced repeated split.** That is the sharp
form of "universal structure versus coincidental appearance", and it was the right
question to have asked.

- EVIDENCE CLASS: **MEASURED** (exact rationals for the Pascal test, floats for the CLT
  rates); the corrected condition is **DERIVED** with the one-line argument above and
  measured on 12 symbols.
- Certificates: `tools/spectral_s02_generative_first_attempt.py` (kept — it contains the
  refutation of my own claim) and `tools/spectral_s02_generative_corrected.py`.

## 7. What is not done

- No end-to-end scan cost with and without the Kummer prune.
- Boundary conditions for the peel: the cut layer is not the full diffusion kernel, as
  she notes, and that is untouched.
- No inequality extracted from the diffusion picture — still the one route by which this
  direction could bite on repetition, still open.
- Nothing here is new mathematics. Walsh–Hadamard/Krawtchouk/Hermite and the binomial
  symbol argument are standard. What is ours is the measurement discipline and the
  sharpened statements.
