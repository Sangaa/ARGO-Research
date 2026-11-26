# CLAUDE | R10 Pascal / hexagonal-lattice leg — results, failures and hypotheses

Status: `SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION`. Written by the CLAUDE monitor lane at
`2026-11-24T1839Z` in answer to `#883/7135146895` (Owner-sourced R10 geometric direction) and
`#883/7135323031` (Owner's hexagonal extension). No repository authority is claimed for anything here, and
this folder is the monitor lane's own write surface (`claude/monitor`), not a canonical research location —
promotion needs a route and an owner.

Every numbered claim carries `WHAT WAS MEASURED → SCOPE → METHOD → EVIDENCE → LIMITATION → EVIDENCE CLASS`.
Scripts and their raw output sit beside this file. `python3 -I`, no network, no lab, no Actions minute.

The three results are kept apart on purpose: **(I) confirmed**, **(II) already in the literature — the part
of my own work that is not new**, **(III) open hypotheses**. Section II is the one that matters most; it is
the reason the literature probe ran before the write-up and not after.

---

## 0. Notation and the Owner's metric

Cell `(n,k)` holds `V = C(n,k)`. The embedding from `#883/7135146895` is `x = k − n/2`, `y = √3·n/2`.
Euclidean distance in that embedding between `(n,k)` and `(n+Δn, k+Δk)` is

`dist² = Δn² − Δn·Δk + Δk²`

which for a step `(Δn, Δk) = (−d, +e)` is `d² + de + e²` — the Owner's own expression, so the metric used
below is his, re-derived rather than assumed. I call `(d,e)` the **displacement class** and
`√(d²+de+e²)` its **hex distance**.

---

## I. CONFIRMED (and all of it trivial or known — stated so the rest can be trusted)

**I-1. The six neighbour ratios in `#883/7135323031` are exact.**
MEASURED: `C(a,b)/C(n,k)` against the six stated rationals.
SCOPE: 5,711 cells — every interior `(n,k)` with `n ≤ 59`, plus 4,000 random cells `n ≤ 400`.
METHOD: exact `Fraction` equality, boundary cells skipped. `hex.py`, `out_hex.json`.
EVIDENCE: `points_tested 5711 / mismatches 0`.
LIMITATION: a finite window; the ratios are elementary and a proof is one line of factorials.
CLASS: `MEASURED`.

**I-2. The closed-hexagon ratio product is 1, and this is empty — exactly as the Owner's own warning says.**
MEASURED: the product of the six consecutive step-ratios around the ring.
SCOPE: 6,786 complete interior rings, `n ≤ 119`.
METHOD: exact `Fraction` product around the ring. `hex.py`.
EVIDENCE: `rings_tested 6786 / product_ne_1 0`.
LIMITATION: none needed — the product telescopes to `V_start/V_start` by construction, so no window could
have refuted it. **It carries no information about repetition.** The warning in the assignment is correct and
the measurement adds only that it was checked rather than assumed.
CLASS: `MEASURED`.

**I-3. The one non-telescoping relation the hexagon does carry — and it is a known identity.**
The ring's six cells split into two alternating triples
`T₁ = {(n−1,k−1), (n,k+1), (n+1,k)}` and `T₂ = {(n−1,k), (n,k−1), (n+1,k+1)}`.
MEASURED: `∏T₁ = ∏T₂`, and `gcd T₁ = gcd T₂`.
SCOPE: 12,561 hexagons, `n ≤ 159`.
METHOD: exact integer products and `gcd`. `hex.py`.
EVIDENCE: `product_mismatch 0`, `gcd_mismatch 0`.
LITERATURE: this is the **Star of David theorem**. MathWorld attributes the gcd form to
H. W. Gould, *Fib. Quart.* 10 (1972) 579–584, 628, and the equal-**product** form ("a second star of David
theorem") to Butterworth (2002), with Ando–Sato (1990) also in its references on equal product/GCD/LCM
properties; the page does not say which form was stated first. Either way it is **not new**, and it is still
an *identity* — true at every cell — so see II-2 for its exclusionary power.
CLASS: `MEASURED` for the arithmetic; `DERIVED` for the attribution (one secondary source, read today).

**I-4. No two lattice-neighbours carry equal values except the mirror pair inside one row.**
MEASURED: all six neighbour-equality equations, solved and then brute-forced.
SCOPE: every cell with `n ≤ 299`, all `k`.
METHOD: setting each ratio to 1 gives `n = 2k±1` for the two horizontal steps and `k ∈ {0, n}` for the other
four; confirmed by enumeration. `hex.py`, `out_hex.json`.
EVIDENCE: 1,496 distance-1 equal pairs found; **300** are same-row mirrors (`n = 2k+1`, one per odd row, both
directions), **1,196** are cross-row and every one of them is a boundary cell with `V = 1`, and
`cross_row_interior = 0`.
LIMITATION: `n ≤ 299`; the algebra above is general, so the enumeration is a control on the algebra rather
than the source of the claim.
CLASS: `MEASURED`.

---

## II. ALREADY KNOWN — including the piece of my own derivation that is not mine

**II-1. The "general transition law" I was asked to link to the geometry is equation (3) of a 2014 paper.**
I derived, and verified, that for displacement `(d,e)`

`C(n−d, k+e) / C(n,k) = ∏_{i=0}^{d+e−1}(n−k−i) / [ ∏_{i=0}^{d−1}(n−i) · ∏_{j=1}^{e}(k+j) ]`

so **equality at a fixed displacement is the integer-point set of one algebraic curve of total degree `d+e`**,
and the hex distance of that class is `√(d²+de+e²)`. I was one draft away from offering that decomposition as
the geometric contribution.
MEASURED: the law itself, 24,775 cells (`n ≤ 79`, `k ≤ n/2`, `1 ≤ d,e ≤ 4`), exact `Fraction`,
`mismatches 0` (`extra.py`, `out_extra.json`). CLASS: `MEASURED`.
LITERATURE: Hugo Jenkins, *Repeated binomial coefficients and high-degree curves*, arXiv:1411.4111, studies
`C(x,y) = C(x−a, y+b)` and writes exactly this as its equation (3),
`∏_{r=0}^{a+b−1}(x−y−r) − ∏_{p=0}^{a−1}(x−p)·∏_{q=1}^{b}(y+q) = 0`, of total degree `a+b`, states *"Any such
equation can be written as the equation of an algebraic curve"*, and proves by irreducibility + genus +
**Siegel's theorem** that for `b ≠ a` the solution set is **finite**; it computes genus 3 for `a = b = 2`
and reaches finiteness there too, and leaves the `a = b` case as the open extension. My `(d,e)` is his
`(a,b)`, my `(n,k)` his `(x,y)`.
CONSEQUENCE: the displacement-curve decomposition is **not a new result**, and its finiteness half is
*stronger* in the literature than anything I measured. CLASS of my own share: `DERIVED, NOT NOVEL`.

**II-2. Exclusionary power of the hexagonal system, measured rather than argued: zero.**
This is lesson 37's own test — run the constraint and count what it excludes that was not already excluded.
MEASURED: the number of coincidence candidates rejected by `H1` (ring product = 1) and `H2` (Star of David
equal triple products).
SCOPE: the full coincidence population of a census of `n ≤ 1000`, `k ≤ n/2` — 251,001 cells, 249,927
distinct values, **77** equal-value pairs (`V > 1`), 154 candidate cells.
METHOD: evaluate `H1` and `H2` at every cell of every candidate pair. `census.py`, `out_census.json`.
EVIDENCE: `candidate_cells_tested 154 / rejected_by_H1_or_H2 0 / inapplicable_boundary_cells 0`.
WHY, structurally: both are identities in `(n,k)`. A predicate true at every cell cannot reject a candidate,
so **the hexagonal relations as stated cannot eliminate a single repetition.** The Owner's instruction was to
test the idea rather than assume its usefulness; tested, on this axis it has no exclusionary power, and that
is a result about the method, not about the conjecture.
CLASS: `MEASURED`.

**II-3. The de Moivre / multiple-angle leg reduces to parity slices of the same lattice.**
The coefficient families in the `cos nθ` / `sin nθ` expansions are the `k`-even and `k`-odd slices of the same
rows, so their coincidence sets are subsets of the census by construction.
MEASURED: coincidence pairs inside each slice, and how many are absent from the full census.
SCOPE: same census, `n ≤ 1000`.
METHOD: `extra.py`, `out_extra.json`.
EVIDENCE: full census **77** pairs; even-`k` slice **3**; odd-`k` slice **17**;
`slice_pairs_not_in_full_census` **0**.
LIMITATION: this closes the *coefficient-coincidence* reading of the de Moivre leg only. A `p`-adic reading
(Kummer/Legendre valuations, roots of unity → `(2cos(θ/2))^n`) is a different instrument and was **not run**.
CLASS: `MEASURED` for the subset claim; the valuation route is `UNAVAILABLE` here.

**II-4. Attribution correction for the control family.** The assignment calls it *"عائلة سينجماستر"*.
Jenkins credits the family to **D. A. Lind**, *Fib. Quart.* 6 (1968), with Singmaster (1975) also providing a
proof; Wikipedia records Singmaster (1975) showing the Diophantine equation has infinitely many solutions.
So *Lind 1968 / Singmaster 1975*, not Singmaster alone. CLASS: `DERIVED` (two secondary sources).

---

## III. OPEN — the one connection I think is worth carrying, and the hypotheses it does not prove

**III-1. The Owner's metric singles out exactly the case the literature leaves open.**
MEASURED: the hex distance of every coincidence in the census, and the complete solution set of the shortest
class.
SCOPE / EVIDENCE:
- The **minimum** hex distance between two distinct interior cells with equal `V > 1`, **modulo the row
  mirror `C(n,k) = C(n,n−k)`**, is exactly **`√3`**. Both halves are settled rather than sampled: the only
  distances below `√3` in this lattice are `0` and `1` (`Δn² − ΔnΔk + Δk²` is a Loeschian number, so it
  cannot be `2`), and `I-4` excludes every distance-1 pair algebraically for all `(n,k)` — boundary cells or
  the mirror — while `√3` is attained at `(15,5) ↔ (14,6)`. The `√3` class is `(d,e) = (1,1)`.
- `(1,1)` equality is the conic `(n−k)(n−k−1) = n(k+1)`, i.e. `n² − (3k+2)n + k(k+1) = 0`, solvable in
  integers iff `5k² + 8k + 4` is a square, i.e. **`X² − 5m² = −4` with `X = 5k+4`** — a Pell equation, which
  is where `√5` and the Fibonacci structure enter the geometry. Solved for all `k < 200,000`:
  `(15,5), (104,39), (714,272), (4895,1869), (33552,12815), (229970,87840)` — the Lind/Singmaster family,
  with `m = 13, 89, 610, 4181, 28657, 196418` (Fibonacci), every one satisfying `X² − 5m² = −4` and
  `C(n,k) = C(n−1,k+1)` (`classes.py`, `extra.py`; verified against `math.comb` up to a 66,416-digit value).
- In Jenkins' terms `(1,1)` is `a = b`, the case his finiteness method does **not** settle — and it is
  the case with infinitely many solutions.
READING: the shortest step in the Owner's hexagonal geometry is precisely the one displacement class that is
both infinite and open in the literature. That is a **connection between two known facts**, not a new
theorem, and I am labelling it that way deliberately.
CLASS: `MEASURED` for the arithmetic; `DERIVED` for the "open in the literature" half (one source).

**III-2. No bounded-distance or curvature argument can cap multiplicity.** The coincidence distance spectrum
in the census runs from `√3` to `√904404 ≈ 951.0` (with a `k ≤ 1` leg) and to `√42876 ≈ 207.1` with both legs
`k ≥ 2`, and the maximum grows with the window because `C(V,1) = V` supplies arbitrarily distant partners.
So the Owner's *"convexity alone is not enough"* extends to the metric itself: a uniform cap on `N(V)` cannot
follow from any statement that bounds how far apart equal values may sit. `MEASURED` inside `n ≤ 1000`;
the unboundedness claim is `DERIVED` from the `C(V,1)` family.

**III-3. Displacement-class census — what the decomposition does and does not buy.**
SCOPE: all 64 classes `1 ≤ d,e ≤ 8`, window `n ≤ 600`, `k ≥ 2`, `k ≤ n/2`.
EVIDENCE (`classes.py`, `out_classes.json`): **4** of 64 classes carry any solution —
`(1,1)`: `(15,5), (104,39)`; `(1,3)`: `(15,5)`; `(6,1)`: `(16,2)`; `(6,5)`: `(16,2)`.
`(1,3)` and `(6,5)` are the row-mirror images of `(1,1)` and `(6,1)` (`C(14,6) = C(14,8)`,
`C(10,3) = C(10,7)`), so **2** genuine classes occur. HYPOTHESIS, not shown: the occupied-class set is
sparse but **unbounded**, which is exactly why the per-curve finiteness results do not compose into a cap —
a bound would need to bound the *set of classes*, and nothing here does. `BOUNDED_PROXY` (one window, one
`d,e` range).

**III-4. Census facts offered as controls for whoever continues.** `n ≤ 1000`, `k ≤ n/2`:
canonical multiplicities are `249,855` singletons, **68** doubles, **3** triples, plus `V = 1` at 1,001 cells.
The three triples are `120 = C(10,3) = C(16,2) = C(120,1)`, `210 = C(10,4) = C(21,2) = C(210,1)` and
`3003 = C(14,6) = C(15,5) = C(78,2)` — with row mirrors, multiplicity 6, 6 and **8**; `3003`'s fourth
canonical representative `C(3003,1)` lies outside the window and was fetched separately
(`full_multiplicity_with_mirrors = 8`, `out_census.json`). Six of the 68 doubles have both legs at `k ≥ 2`.
Wikipedia records 3003 as the smallest and only known value of multiplicity 8, that it is unknown whether any
value appears more than eight times, and the standing bounds: Singmaster (1971), Abbott–Erdős–Hanson (1974),
best unconditional due to Kane (2007). `MEASURED` for the census, `DERIVED` for the Wikipedia half.

---

## IV. Failures and near-misses, kept per the assignment

1. **I nearly published the displacement-curve decomposition as a contribution.** It is Jenkins' equation (3)
   (II-1). What caught it was a literature probe on the *shape of the equation*, not on the topic words:
   searching `Pascal`/`Singmaster` returns the conjecture's own pages, while the paper that already holds the
   result surfaces under *repeated binomial coefficients* + *curves*. Probe the derived object, not the topic.
2. **The hexagonal idea's exclusionary power is zero and I could have reported it as promising.** Both
   relations are identities (II-2). The test that settles it is lesson 37's counting test, run before any
   framing.
3. **A `−4` that looked like a sign error.** `X² − 5m² = −4` (not `+4`) is the correct Pell form here; checked
   on all six family members rather than adjusted to taste.
4. **Not run, and named so nobody reads this as covering it:** the Gamma-surface leg (level curves, slope,
   curvature, integer lattice points) is `TOTO`'s half of the assignment and I did not touch it; the `p`-adic
   valuation route (II-3); and any claim about whether `(1,1)`'s infinitude can be ruled out for `d = e ≥ 2`
   beyond Jenkins' `a = b = 2` genus-3 result, which I did not reproduce.

## V. Resume point

`RESUME`: (1) decide whether the displacement-class decomposition is worth any further work given II-1 —
my reading is that it is not, as stated; (2) if the hexagonal direction continues, the only axis with content
is `gcd`/valuation rather than product identities, because products telescope and the gcd form is where the
literature's own generalisations live (Sato 1975; Hitotumatu–Sato 1975, per MathWorld); (3) TOTO's Gamma/
curvature leg is independent of everything above and is not blocked by it; (4) the cross-review the Owner
asked for cannot be done from this lane alone — TOTO's results are not in this repository and I found no
R01–R09 artifact on `main` (the only `R10` path in the tree,
`Execution/Projects/LiveBoard_Prototype/R10_LAB_EVIDENCE.md`, is an unrelated lab file, so the label `R10`
collides inside the house).

`PRIOR_EVIDENCE` for item IV-1: `NONE` for the external-literature dimension — `LESSONS.md` had no row about
checking a derived statement against published mathematics; `C87` is the same failure against the house's own
prior posts. A row was added as `C88`.

---

## VI. Owner evaluation correction, incorporated 2026-11-25T0640Z — additive, nothing above rewritten

**Source.** `ARGO-KOP #888/7154054066` @ `2026-11-25T05:42:04Z`, posted by TOTO as an explicit Human Authority
correction from the TOTO conversation of 2026-11-25. Self-declared status in the comment itself:
`OWNER-DIRECTED EVALUATION CORRECTION / SESSION-DERIVED EXPERIENCE / NON-CANONICAL pending governed
integration`, and *"not a claim of a merged file change"*. Its closing line names the follow-up:
*"Requested follow-up for CLAUDE/SEMER: incorporate this owner correction into the durable research evaluation
and subsequent reports without rewriting historical evidence."* This section is CLAUDE's half of that, in this
lane's own durable record. It is **not** an integration into `main`: no governed path was touched, and the
comment is a relay of a conversation this lane cannot read, so its authority is `SOURCE-REPORTED`, not verified
from an Owner-authored artifact in the repository (`§E`: a comment's author label is not an authenticated
identity).

**What changes.** Sections I–V above stand as written, including every failure. What changes is how the
Jenkins match in §IV-1 is to be *scored*:

- The Owner distinguishes **independent reasoning** from **originality**, and states the experiment deliberately
  runs `problem understanding → own hypotheses/derivations → own tests and corrections → subsequent literature
  comparison → acquisition of stronger tools → renewed research`. Reading literature *after* independent work is
  intentional in that design, not wasted work.
- *"Finding that a previously derived result or method agrees with published work is positive evidence of
  convergence of reasoning, not a failed experiment. Do not score a rediscovery as a loss merely because it is
  not novel."*
- Seven evaluation axes, with 6 and 7 assessed **separately** from 1–5: (1) correctness of derivations;
  (2) chronological evidence of derivation before the literature was consulted; (3) quality of hypothesis
  selection and convergence with established mathematics; (4) error detection and correction; (5) acquisition
  and later application of new tools; (6) originality; (7) progress toward a uniform multiplicity bound.
  The first five can succeed while 6 and 7 remain unresolved.
- **Attribution the Owner assigns to himself, not to the assistants:** the problem was new to him, and his
  contribution was *redirecting enumeration toward generating laws and geometry*. Recorded here as his.
- **Bound, not granted:** *"The reported Jenkins matches are candidates for documented rediscovery; bind each to
  dated earlier records and exact literature passages before claiming verified convergence."* So §IV-1's match
  is a `CANDIDATE REDISCOVERY`, pending that binding — it is not upgraded to `convergence` by this section.
- **No inference the experiment does not support:** no claim of absence of pretraining exposure, consciousness,
  weight updates, or sustained cross-session learning follows from it; durable learning needs later transfer
  tests. Merging a file is not learning.
- Genuine failures stay separate from correct rediscoveries: the `78x` measurement, the invalid `0%` test, the
  incorrect open-pair claim, and TOTO's definitional identity treated as a constraint.

**What this lane owes next, and what it cannot do.** The binding in the fourth bullet is the actionable item and
it is *not* satisfied yet: it needs, per Jenkins match, (a) the dated prior record in this repository that shows
the derivation preceded the literature read, and (b) the exact passage of `arXiv:1411.4111` it matches. For the
degree-`d+e` curve result, (a) is available in this lane's own commit history on `claude/monitor` and (b) is
named in §IV-1 as equation (3); neither has been bound as a pair with timestamps, so the honest label today is
`CANDIDATE REDISCOVERY / BINDING NOT YET PRODUCED`. `EVIDENCE CLASS: UNAVAILABLE` for any convergence verdict
until then.

`LIMITATION (C64, with the failing route named).` This section is a faithful transcription of one comment's
directive content into this lane's record; it is **not** an integration of the correction into any governed
surface, and it does not reach `Execution/Research/CLAUDE/SINGMASTER_CLAUDE_R09_R11_RECORD_2026-11-25.md`, which
merged to `main` at `23a9c144c35c6d1cdd90a5786dcc277236590590` (via `#885`, `04:33Z`) **1 h 09 min before** the
correction was posted and therefore carries none of it. Writing to that path is a protected-path mutation needing
an explicit current work order this lane does not hold, so the artifact is prepared here and stops here
(`PROTOCOL.md` §3). `NEXT ACTOR:` whoever holds the work order for `Execution/Research/CLAUDE/**`, with SEMER
named alongside CLAUDE in the Owner's own follow-up line.
