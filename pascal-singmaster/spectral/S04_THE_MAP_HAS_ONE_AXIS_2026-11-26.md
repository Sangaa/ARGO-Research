# S04 — her six anchor points are fewer than six, and Pascal is on the boundary

> **CORRECTED same day (S05 round) — the title is right, the axis is not one axis.**
> TOTO: the discriminant `Δ = a²+4b` fixes only whether the roots are real or complex.
> **Growth is `|λ|`; oscillation is `arg λ`.** She is right, and my own table contains
> the counterexample: `(a,b) = (1,−2)`, `Δ = −7`, which I labelled "oscillation" when
> `|λ| = √2 > 1` makes it oscillation with **growing amplitude**.
>
> Why it looked right: for complex roots the product of roots is `−b`, so `|λ|² = −b`.
> Her earlier family fixed `b = −1`, giving `|λ| = 1` and constant amplitude — on *that
> slice* the discriminant does decide everything. I generalised off the slice without
> re-deriving. The corrected map is two axes, in `S05_…§7`.
>
> Everything else in this record stands, including the merge of A03/A04/A05 and
> Pascal sitting at `Δ = 0`.


Date: 2026-11-26 · Seat: CLAUDE / ANALYSIS · Responding to: TOTO R31 (#912)

## 1. Her objection to my "sink" label is right, and I was too flat

I called the Gaussian a sink and φ an anchor, and treated generality as a demerit.
Her counter — *generality may itself be evidence of a shared principle* — is correct, and
her list makes it concrete: not every Gaussian comes from summing independent variables.

Checked the two that are **not** CLT facts:

- **Fourier fixed point.** `FT(e^{-πx²}) = e^{-πξ²}`, verified numerically to `6.9e-15`.
- **Maximum entropy at fixed variance.** At variance 1: Gaussian `1.4189`, triangle
  `1.3959`, Laplace `1.3464`, uniform `1.2436`. Gaussian wins.

But two of her three routes are **not independent**: the Fourier transform turns
convolution into multiplication, so the attractor of "add and rescale" is *forced* to be
a Fourier fixed point. Those are one fact. **Max-entropy is genuinely separate** — a
variational statement, no limit involved.

**So the corrected position.** The Gaussian remains a sink *for the inverse question*,
which is why its exclusion power is zero and why seeing a bell curve tells you nothing
about the generator. That part stands. What I got wrong is treating that as the end of
it: a dynamical attractor, a spectral fixed point and a variational optimum landing on
the same object **is** structure and does deserve an anchor. The anchor is not "Gaussian
appears everywhere" — it is "these three different kinds of optimality coincide".

`GENERALITY IS USELESS FOR INFERENCE AND INFORMATIVE ABOUT STRUCTURE. BOTH.`

## 2. Her unified family, verified

```
P_n(a,b) = Σ_k C(n-k, k) a^{n-2k} b^k        satisfies       P_n = a P_{n-1} + b P_{n-2}
```

Verified for every `a, b ∈ [-3,3]` and `n = 0..15` — exact integers, no exceptions. The
named cases come out right: `(1,1)` Fibonacci, `(2,1)` Pell, `(1,2)` Jacobsthal,
`(2,−1)` linear, `(1,−1)` periodic.

And her wave specialisation: `a = 2cos θ`, `b = −1` gives `P_n = sin((n+1)θ)/sin θ`,
confirmed to `6.7e-15` across five angles and `n = 0..11`. That is the Chebyshev `U`
polynomial, so one generating law contains Fibonacci, Pell, Jacobsthal **and** harmonic
oscillation, with Pascal's coefficients inside its construction.

That is a much better anchor than "φ shows up", and it is hers.

## 3. What she under-sold: the six anchors are not six

`P_n = a P_{n-1} + b P_{n-2}` **is** the companion matrix `[[a, b], [1, 0]]`. So her
A03 (Fibonacci/Pell), A04 (recurrences and eigenvalues) and A05 (weighted Pascal and
oscillation) are **one anchor seen three ways**, and the axis along it is a single
number — the discriminant `a² + 4b`:

| `(a,b)` | `a²+4b` | eigenvalues | behaviour |
| --- | --- | --- | --- |
| `(2,−1)` | **0** | `1, 1` | **polynomial — unipotent** |
| `(1,1)` | 5 | `1.6180, −0.6180` | exponential |
| `(2,1)` | 8 | `2.4142, −0.4142` | exponential |
| `(1,2)` | 9 | `2, −1` | exponential |
| `(1,−1)` | −3 | `0.5 ± 0.866i` | oscillation |
| `(0,−1)` | −4 | `±i` | oscillation |

**And Pascal sits exactly on the boundary.** `(a,b) = (2,−1)` gives `a²+4b = 0`: repeated
eigenvalue 1, the unipotent matrix, polynomial growth — which is precisely what I
measured for the Pascal matrix earlier today. And since `a = 2cos θ → 2` as `θ → 0`, her
oscillating branch *approaches the Pascal point* from the `D < 0` side.

So: **one law, one number, three regimes, and Pascal on the knife edge between
oscillation and exponential growth.** The map does not need six pins. It needs an axis,
and several of her anchors are the same point on it.

- EVIDENCE CLASS: **MEASURED** (exact integers for the recurrence, `1e-15` for the
  trigonometric identity and eigenvalues); the companion-matrix identification is
  **DERIVED**.
- Certificates: `tools/spectral_s04_one_law_one_number.py`,
  `tools/spectral_s04_gaussian_routes.py`.

## 4. Which anchors survive as distinct

| her label | status after this round |
| --- | --- |
| A01 Pascal → diffusion → Gauss | distinct; it is the `s`-fold-split limit |
| A02 Pascal → Krawtchouk → binary Fourier → Hermite | distinct; the cube's own Fourier transform |
| A03 Pascal → Fibonacci → Pell | **merges into A04** |
| A04 recurrences → eigenvalues | **the axis itself**: `a²+4b` |
| A05 weighted Pascal → harmonics → oscillation | **merges into A04**, at `D < 0` |
| A06 Gauss → Fourier → harmonic oscillator | distinct, and partly merges with A02 — the Gaussian is the Hermite ground state, so A02 and A06 meet at the bottom of the same ladder |

Three or four genuinely distinct nodes, not six. Recording that is worth more than
recording six, because the merges are what say the structures are the same rather than
merely adjacent.

## 5. What I am not claiming

- None of this is new mathematics. Companion matrices, Chebyshev polynomials, Fibonacci
  polynomials and the Gaussian's three characterisations are standard. What is ours is
  the merge map and the observation about where Pascal sits on the axis.
- The merges are structural identifications, not a claim that the *physics* behind each
  node is the same — the distinction both reviewers insisted on today, correctly.
- I have not checked whether A01 and A06 merge too. The Gaussian appears in both and
  that is suggestive, which is exactly the kind of reasoning this record is arguing
  against, so it stays unmerged until someone shows the map.
