# Pascal's triangle: repeated values, spectra, and an effective bound

A working research record. Not a finished paper — a lane-by-lane log of what was
derived, what was measured, what was wrong, and who corrected it.

The subject is the **Singmaster conjecture**: that the number of times a value `> 1`
can appear in Pascal's triangle is bounded by an absolute constant. `3003` appears
eight times and nobody knows whether anything appears nine.

---

## ما هو ده (بالعربي)

ده سجل بحث شغّال على **حدسية سينجماستر**: هل عدد المرات اللي رقم أكبر من 1 يقدر يتكرر
فيها في مثلث باسكال محدود بثابت؟ أكبر تكرار معروف هو 8 مرات، للرقم 3003، ومحدش يعرف
لو فيه رقم بيتكرر 9.

**المستودع ده مش ورقة علمية مكتملة.** ده دفتر معمل: كل مسار بحثي بسجله زي ما جرى —
اللي اشتقناه، واللي قِسناه، واللي كان غلط، ومين صلّحه. الأغلاط مكتوبة جوه السجلات
بنفس تفاصيل النتايج، لأن ده شرط إن الشغل يبقى قابل للمراجعة.

**ليه كل سكريبت موجود:** كل رقم في السجلات ده ليه سكريبت في `tools/` بيطلّعه. مافيش
رقم مكتوب بالإيد. السبب إن ده حصل فعلًا — رقم اتكتب بالإيد (480 بدل 472) وصفر اتكتب
بالإيد جوه جدول قياس، والاتنين اتمسكوا من مراجعين. فالقاعدة بقت: الشهادة بتطبع
أعدادها بنفسها.

**مين عمل إيه:** التوجيه البحثي والتصحيحات الموضوعية من Human Authority (عصام).
الاشتقاق الأساسي للحد في `referee/` من TOTO (مقعد نموذج خارجي). المراجعة والإصلاحات
والتحقق من CLAUDE. المقعدين من مزوّدَين مختلفين، فالمراجعة عبر-مزوّد — **لكنها مش
مراجعة أقران بشرية، ومحدش من بره شاف ده لحد الآن.**

---

## The routes

Six lanes. They are not stages of one pipeline; three of them were opened because
another one closed.

### 1. `referee/` — the one result offered for external review

An **effective** uniform quadratic bound for the equal-displacement equation:

> for `t >= 2`, `k >= 1`, `n >= 2k + 3t`, every solution of `C(n,k) = C(n-t, k+t)`
> satisfies `n < 200 t²`.

Read **`SINGMASTER_UNIFORM_QUADRATIC_BOUND_FROZEN_V3_2026-11-26.md`**.

Why it is of a different kind from what preceded it: Jenkins (arXiv:1411.4111) proves
*finiteness* for `t_1 != t_2` by Siegel's theorem, which is **ineffective** — it gives
no searchable range. This bound is explicit, so for each `t` the solution set is
decidable by a finite search. Jenkins' §3 already sketches finiteness at `t = 2` via
genus 3 + Siegel, so the honest statement of the contribution is two rows:
**effectivity is uniformly new; finiteness is new only for `t >= 3`.**

The freeze rule: a frozen version never moves. Improvements become a new version with
an entry in `FREEZE_LOG.md`; the superseded file is never edited, so a referee holding
an old copy can see exactly what differs. V1 was frozen and was holed **within the
hour** by a reviewer — which is the argument for freezing, not against it.

*Known defect, deliberately unfixed:* V3's own header still carries V2's line
`Read V2; V1 exists only so the change is auditable.` It is a leftover. Editing a
frozen file in place is a worse defect than a stale pointer, so it stays, recorded
here and in `FREEZE_LOG.md`.

### 2. `SINGMASTER_R09`–`R23` — the main derivation lane

Round by round, in date order. The useful ones to start from:

| record | what is in it |
| --- | --- |
| `R09_R11` | the `1:2:3` ratio at row 14 is **forced, not lucky** — the only place in the triangle where three consecutive entries stand in ratio `1:2:3`; so `3003` is two *readings* of one ratio vector, not two independent mechanisms meeting. This killed a proposed route to **disproving** the conjecture. |
| `R12` | first literature review |
| `R13` | genus transfer; the Siegel correction |
| `R14`–`R19` | the series expansion, the bracket, the product form, the arithmetic scan, the shift, the exact root bound, Fujiwara |
| `R20`–`R22` | the margin, and the `J1`/`J2` layers |
| `R23` | review of the `n < 200t²` derivation — the verdict that produced `referee/V1` |

### 3. `spectral/S01`–`S08` — does Pascal's regularity reach the laws of nature?

Opened by a direction from Human Authority: Pascal's row is the binomial
distribution, which is the discrete heat kernel and tends to the Gaussian — so does
that regularity connect to the equations that describe physical systems, waves and
frequencies in particular?

What actually came out of it:

- **Pascal *is* the discrete heat kernel**, exactly: `u_{n+1}(x) = (u_n(x-1) + u_n(x+1))/2`.
- **Krawtchouk polynomials are the Fourier transform of `(Z/2Z)^n`** on radial
  functions. As a *per-cell exclusion tool* they are **UNSOUND** — measured: they
  falsely exclude 9 of 10 genuine repetitions. See the correction notice at the top
  of `S01`.
- **The generative condition.** The `n`-step kernel is proportional to a Pascal row for
  every `n` **iff** `f(z) = c·z^m·(1+z^L)^s`. Nothing else generates the triangle.
- **`2cos(π/m)` is the growth rate** of residue spread mod `m`. Bounded iff
  `2cos(π/m) <= 1` iff `m <= 3`. At `m = 5` the rate is `φ`, and Fibonacci structure
  enters — which is also where the `(1,1)` displacement class lands (see lane 4).
- **`D = a² + b² + c² - ab - bc - ca = |a + bω + cω²|²`** — the Eisenstein norm. This
  merged the mod-3/6/9 thread and the hexagonal-lattice thread into one object, `Z[ω]`.
- **The exclusion taxonomy**, which is the lane's most portable result:
  identity **0%** → congruence (Kummer) **86.6% at `p = 2`, rising to 100% at 12
  primes** → inequality (Robbins/Stirling) **99.67–100%**. An identity is true at every
  cell, so it cannot exclude anything — that is why the 0% row is structural and not a
  small sample. Scope: 20,000-cell samples; the 99.67% figure is the *hard* arm
  (adjacent-in-value distinct pairs), and every rate here was checked for soundness
  against all 10 genuine repetition pairs in range (**0 false exclusions**), which is
  the check the Krawtchouk row failed.

`S04` and `S01` carry correction notices at the top. `S07` is the record of a review
published by a parallel lane that **I did not read** before writing three records that
repeat claims it had already refuted.

### 4. `hex_lattice_R10/` — the geometric lane, and why it closed

A hexagonal embedding `x = k - n/2`, `y = √3·n/2`, in which the distance between cells
displaced by `(d,e)` is `√(d² + de + e²)`.

- The six neighbour ratios and the closed-ring product are **exact** — and the ring
  product is **empty**: it telescopes by construction, so no window could have refuted
  it. Measured exclusionary power of the hexagonal relations: **zero**, on 154
  candidate cells. Both relations are identities. That is the identity row of the
  taxonomy above, measured.
- The one non-telescoping relation the hexagon carries is the **Star of David theorem**
  (Gould 1972 for the gcd form; Butterworth 2002 for the equal-product form) — already
  known.
- **What survived, and it is the best thing in this lane:** the minimum hex distance
  between two distinct interior cells of equal value `> 1`, modulo the row mirror, is
  exactly `√3`, attained at `(15,5) ↔ (14,6)`. The `√3` class is `(d,e) = (1,1)`, whose
  equality condition is the Pell equation `X² - 5m² = -4` — and in Jenkins' terms
  `(1,1)` is `a = b`, **the case his method does not settle**, and the case with
  infinitely many solutions. So the shortest step in this geometry is precisely the
  open one. That is a connection between two known facts, labelled as such.
- Attribution correction found here: the family is **Lind 1968 / Singmaster 1975**, not
  Singmaster alone.

### 5. `literature/` and `reviews/`

`LIT_01` is the primary-source read of Jenkins. `REV_01` reviews a 78-page living
reference and a parallel lane's octagon programme, and contains the one corollary this
lane contributed to it: from their own `M(t) = m·P(t) + I(t)` with `I >= 0` it follows
that `M >= P`, so **`M` bounded ⟹ Singmaster, for every polygon in the family** — no
polygon gives a weaker statement, so the geometric generalisation cannot be a route
*to* Singmaster. All its content lives in `I(t)`, and whether `I` is bounded in terms
of `P` decides equivalent vs strictly stronger. Open.

### 6. `tools/` — the certificates

One script per claim, `python3 -I`, no network, no external data. Each exits non-zero
on failure and prints its own population sizes.

```sh
python3 -I tools/singmaster_r23_review.py      # the 12 checks behind the R23 verdict
python3 -I tools/spectral_s02_generative_corrected.py
cd hex_lattice_R10 && python3 -I census.py     # reproduces out_census.json byte-for-byte
```

Note `tools/spectral_s02_generative_first_attempt.py` is kept **beside** its corrected
version on purpose. The first attempt is wrong and the diff is the lesson.

**Run status, measured before publication:** all 43 scripts were executed
(`python3 -I`, no network). **42 exit 0.** One exits non-zero **by design**:

`singmaster_curve_genus.py` computes the genus of the equal-displacement curve for
`t = 1..5` over large primes — obtaining `0, 3, 10, 21, 36`, where **the genus 3 at
`t = 2` reproduces Jenkins' own §3 computation** — and then, on reaching `p = 101`,
its guard refuses:

> `prime 101 is too small: interpolating a degree-114 resultant needs 115 distinct
> nonzero points, so p must exceed 115.`

That is the script detecting that its own method is invalid at that prime and
declining to print a number, which is the behaviour wanted from a certificate. The
`p = 101` sweep runs last, so no earlier result is lost. The exit code is **not**
patched to hide it: a certificate that returns 0 while skipping a case it could not
compute is the defect this whole programme exists to catch.

Reproduction of the stored outputs was also checked rather than assumed:
`hex_lattice_R10`'s four scripts regenerate `out_*.json` **byte-for-byte**.

---

## What is open

1. Whether `I(t)` can be bounded in terms of `P(t)` — decides whether the octagon
   programme is equivalent to Singmaster or strictly stronger.
2. A citation sweep of work citing Jenkins. **The highest-value unfinished task**: the
   originality of everything in `referee/` rests on it and it has not been done.
3. Identifiability for `s >= 3`, and for `s = 2` against half-integer-mean rivals.
4. The regular-octagon tail bound. The attackable step is the claim that for `h > 0`
   one can *always* choose an opposing pair on an axis other than the largest residual
   coordinate.
5. The `p`-adic / valuation reading of the de Moivre leg — named as not run.

## What is not in this repository

The research lanes above are the mathematics. The house that produced them also runs
engineering, review and governance lanes which are **not published**: those records
carry third-party and operational material that does not belong in a public repo, and
removing the sensitive parts would leave records that no longer support their own
claims. Cross-references in these files to `Sangaa/ARGO-KOP` pull requests point at a
**private** repository and will not resolve for an outside reader; they are kept
because deleting a record's provenance to make it look self-contained is worse than a
dead link.

Two further research lanes exist in the house and are not here: a vision-science /
perception lane, and a method retrospective on how earlier answers were justified.
Both are entangled with personal material.

## Status of every claim

Each record binds its claims with
`WHAT WAS MEASURED → SCOPE → METHOD → EVIDENCE → LIMITATION → EVIDENCE CLASS`,
and the class is one of `MEASURED / DERIVED / BOUNDED_PROXY / UNAVAILABLE`.
Read the class before the claim. A number with class `BOUNDED_PROXY` was measured in
one window with one parameter range and is not a theorem.

Nothing here has been peer-reviewed by a human mathematician.
