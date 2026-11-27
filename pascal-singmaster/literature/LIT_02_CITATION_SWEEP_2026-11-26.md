# LIT_02 — the citation sweep the originality claim was resting on, and what it found

Date: 2026-11-26 · Seat: CLAUDE / ANALYSIS
Status: `LITERATURE FINDING / NO PROOF CHANGED / ONE CORRECTION TO THE RECORD, ONE NEW PRECEDENT`

Every record in this lane since R12 has carried the same open item: the originality of the
bound in `referee/` had never been checked against work that cites Jenkins. `LIT_01` read
Jenkins himself; nobody read outward from him. This is that sweep.

**Nothing below changes a lemma, a constant or a step of the proof.** Two things change:
the record's citation of Jenkins is wrong in a way that matters, and there is a precedent
`referee/V3 §2` does not name.

`EVIDENCE CLASS for every literature claim here: DERIVED.` Each is a reading of a primary
or secondary source named with its exact locator. None is `MEASURED` — a reading is not a
measurement, and a second reader can disagree with any of them from the same locators.

---

## 1. The citation in every one of our records is to the wrong version

We cite `arXiv:1411.4111`. The field cites:

> H. Jenkins, *Repeated binomial coefficients and high-degree curves*,
> **Integers 16 (2016), Paper No. A69, 14 pp.**

That is how Matomäki–Radziwiłł–Shao–Tao–Teräväinen list it (their reference [13]). The
published paper's own front matter gives: received 12/20/14, **revised 2/2/16**, accepted
9/30/16, published 10/5/16. So `arXiv:1411.4111` is the *submitted* version, and it was
revised over fourteen months before publication.

**This is not pedantry, because the versions differ in a way that touches our precedent
analysis.** Read both:

| | preprint (`arXiv:1411.4111`) | published (`Integers 16 #A69`) |
| --- | --- | --- |
| cites Beukers–Shorey–Tijdeman | **no — absent from text and references** | **yes, as reference [4]** |
| reference count | — | 25 |
| §3 `a = b = 2` genus-3 computation | present | present |
| §4 names `a = b, a ≠ 1` as the extension | present | present |
| Theorem 1 requires `b ≠ a` | yes | yes |

The `a = b` precedent question that forced `referee/V2 → V3` was settled from the preprint.
It happens to come out the same way in both versions, so V3's correction stands. But the
*reference list* does not, and that is where a precedent for our own theorem would live.

`SCOPE / METHOD:` both versions read directly; the published one's reference list and front
matter read in full, the preprint's text searched for "Beukers", "Shorey", "Tijdeman" and
for every numeric bound. `LIMITATION:` I did not diff the two versions line by line, so I
can state the reference-list difference and the survival of §§3–4, not that nothing else
moved.

## 2. The precedent `referee/V3 §2` does not name: Beukers–Shorey–Tijdeman 1999

> F. Beukers, T. N. Shorey, R. Tijdeman, *Irreducibility of polynomials and arithmetic
> progressions with equal products of terms*, in **Number theory in progress, Vol. 1**,
> de Gruyter, Berlin, 1999, 11–26.

What it gives, as MRSTT describe it in their Remark 1.5: for **fixed `m < m'`**, the number
of solutions of `C(n,m) = C(n₀,m₀)` is **finite**, by Siegel's theorem on integral points.
And MRSTT state plainly that the resulting function is **"completely ineffective"** because
it rests on Siegel.

Jenkins cites it too — in the published version, for the finiteness of `x^a = y^b` for all
`(a,b)`, and he also calls it ineffective.

`referee/V3 §2` discusses only Jenkins. It should discuss this as well: it is the earlier
Siegel-based finiteness result in this exact area, it is what the current literature points
at for the fixed-column case, and it is ineffective — which is the axis our claim lives on.
V3 §2 is therefore **incomplete rather than wrong**: no sentence in it becomes false, but a
referee reading §2 would not learn that the ineffective-finiteness precedent goes back to
1999 and not to 2014.

## 3. A distinction I was about to draw, and it is false

Before checking, I had reasoned that our statement differs from Jenkins' by being *uniform
in `k`* — that he fixes the columns while we fix the displacement and quantify over all `k`.

**That is wrong.** Jenkins' Theorem 1 fixes `a` and `b` and ranges over all natural `x, y`.
It is already uniform in `y`, which is our `k`. The quantifier structure is the same as ours.

Checked at source: Theorem 1 is stated for each fixed pair `(a,b)` with `b ≠ a`, concluding
finitely many solutions in natural numbers `x, y`, with no lower bound on `y` and no
canonical-position hypothesis. (Proposition 1 carries an `a < y` condition because its proof
divides by the leftmost term; Theorem 1 does not repeat it.)

So the contribution is **not** uniformity. It is exactly the two rows V3 already states:
effectivity, and `a = b` for `t >= 3`. Had I written the uniformity claim down it would have
been a false distinction flattering our own result, built on not having read the theorem
statement.

## 4. What the sweep did NOT find, which is the point of running it

Read outward from Jenkins, through the papers that cite him and the papers he cites:

| source | what it bounds | effective? | our form? |
| --- | --- | --- | --- |
| Beukers–Shorey–Tijdeman 1999 | finiteness for fixed `m < m'` | **no** (Siegel) | no bound on `n` |
| Jenkins, Integers 16 (2016) #A69 | finiteness for `b ≠ a`; `a=b=2` by illustration | **no** (Siegel) | no bound on `n` |
| Matomäki–Radziwiłł–Shao–Tao–Teräväinen, *Singmaster's conjecture in the interior of Pascal's triangle*, Q. J. Math. 73 (2022) 1137–…, `arXiv:2106.03335` | the **number** of solutions of `C(n,m)=t` in the interior region `exp(log^{2/3+ε} n) <= m <= n/2` — at most two, sharp | thresholds effective but "unoptimized and likely too large for numerical verification" (their Rem. 1.7) | **no** — bounds a count, not `n` in terms of a displacement |
| de Weger, *Equal binomial coefficients: some elementary considerations*, J. Number Theory 63 (1997) | specific equations `C(x,2)=C(y,4)`, `C(x,3)=C(y,4)` solved completely | yes, for those cases | no, and no displacement family |
| *Binomial collisions and near collisions*, `arXiv:1707.06893` | computational: no unknown collisions for `n <= 10^6`, `C(n,k) <= 10^60`; seven infinite near-collision families; de Weger's Conjecture 2.1 = "no other collisions than those given" | computational cutoffs only | no |
| Kane 2004/2007, Abbott–Erdős–Hanson 1974, Singmaster 1971 | `N(t)`, the multiplicity of a value | yes | no — the dual problem |

**No source found gives an effective bound on `n` in terms of the displacement.** That is
the gap the `referee/` claim occupies, and after this sweep it is a sweep-supported
statement rather than an untested assumption.

`LIMITATION, and it is real:` this is a sweep of the papers reachable in one pass from
Jenkins' citations, his citers, and keyword search. It is **not** a complete citation graph
— I have no indexed citation database here, and `arXiv:1411.4111` and the Integers version
are indexed separately, so a paper citing only the Integers version by journal reference can
be invisible to a preprint-ID search. `EVIDENCE CLASS: BOUNDED_PROXY` for the
"nothing found" claim specifically. A library search on the Integers citation remains the
right next step and has not been done.

## 5. The strongest support for the claim, and it is in Jenkins' own words

Jenkins' §3 states that an **effective** form of Siegel's theorem would let one bound the
height of the integral points, and that no such form is available; that Baker's effective
methods for genus-1 curves give **triple-exponential** bounds, "too large to be useful";
and that an effective Schmidt subspace theorem is not available either.

So the author of the closest paper names the absence of an effective bound as *the*
obstruction, and names the best available effective tool as triple-exponential.

## 6. And the risk that same fact creates, which is larger than the support

Our bound is `n < 200 t²` — polynomial. It is obtained by an elementary route: a logarithmic
expansion of a ratio of products, a remainder estimate, and a congruence restriction mod 24.
No Diophantine geometry, no transcendence method, no Siegel.

A Berkeley number theorist, writing on exactly this family, said the effective bounds
available to him were triple-exponential. If a polynomial bound follows from elementary
manipulation, then **the prior probability that the elementary argument has a gap goes up,
not down.** The sweep finding "nothing published" is consistent with two very different
worlds: a real gap in the literature, or a real gap in our proof.

This cuts against the result and belongs in the record for exactly that reason. It is also
the honest reading of §5: the support and the risk come from the same sentence.

`WHAT WOULD DISCRIMINATE:` an external referee, or a search for a counterexample above the
bound in a range the bound forbids and the literature has already searched — de Weger's
computations reach `n <= 10^6` and `C(n,k) <= 10^60`, so for small `t` our bound is already
inside territory someone has swept, and a conflict would show up there rather than in theory.

### 6a. That check, run

`tools/lit02_bound_vs_literature.py`, exit 0. It could only have refuted the bound; it did
not, and what it actually establishes is narrower than "the bound holds".

| `t` | `200t²` | solutions found | exact integer tests | reach past the bound |
| --- | --- | --- | --- | --- |
| 2 | 800 | 0 | 788 | 25.0× |
| 3 | 1800 | 0 | 522 | 11.1× |
| 4 | 3200 | 0 | 395 | 6.2× |
| 5 | 5000 | 0 | 316 | 4.0× |
| 6 | 7200 | 0 | 262 | 2.8× |
| 7 | 9800 | 0 | 223 | 2.0× |
| 8 | 12800 | 0 | 203 | 1.6× |
| 9 | 16200 | 0 | 174 | 1.2× |
| 10 | 20000 | 0 | 157 | 1.0× |
| 11 | 24200 | 0 | 143 | **0.83× — vacuous** |
| 12 | 28800 | 0 | 130 | **0.69× — vacuous** |

> **Extended 2026-11-27 to `2 <= t <= 20`, `n <= 100000`.** The table above is the
> original run; the extended one is **discriminating for every `t` from 2 to 20, with no
> vacuous row** — reach ranges from 125× past the bound at `t = 2` to 1.2× at `t = 20`.
> Still 0 solutions, still 0 violations.
>
> It needed a different exact test, not a bigger budget. With `comb()` the run could not
> finish: the float guard admits more candidates as `n` grows, because the minimum
> separation shrinks, and each admitted candidate cost a comparison of ~30,000-digit
> integers. Cancelling the factorials first,
> `∏_{i<t}(n−i) · ∏_{j≤t}(k+j) = ∏_{l<2t}(n−k−l)`, makes the exact test `4t`
> multiplications of integers bounded by `n`. Measured at `n = 100000, t = 20`: 2000 tests
> in **0.011 s** factored versus **173 s** with `comb()` — **15,483×**. Verified against
> `comb()` before replacing it, on all **250,347** triples with `t ≤ 6`, `n < 420` —
> **0 disagreements** — and on the whole `t = 1` family.
>
> And the extended range found a **fifth** member of the `t = 1` control family:
> `(15,5), (104,39), (714,272), (4895,1869), ` **`(33552, 12815)`**. Three of the five
> exceed `200·1²`, so the `t >= 2` hypothesis is load-bearing against a larger family than
> the original run could see.

`WHAT WAS MEASURED:` existence of any `(n,k)` in canonical position with
`C(n,k) = C(n-t,k+t)`. `SCOPE:` `2 <= t <= 20`, `n <= 100000`, `1 <= k <= (n-3t)/2`.
`EVIDENCE: 0` solutions at any `t >= 2`, and so **0 violations** — but also nothing for the
bound to forbid, which is the honest reading. `EVIDENCE CLASS: BOUNDED_PROXY`, and
**genuinely discriminating only for `t <= 10`**: at `t = 11, 12` the bound exceeds the search
window, so no counterexample was reachable and the PASS carries no information there. The
script prints that column itself rather than leaving a reader to infer it.

`METHOD, and why it is rigorous rather than a sample.` Let
`g(k) = log C(n,k) - log C(n-t,k+t)`. Then

```
g(k+1) - g(k) = log[(n-k)(k+t+1)] - log[(k+1)(n-k-2t)],
```

and the two arguments differ by exactly

```
(n-k)(k+t+1) - (k+1)(n-k-2t) = t(n+k+2) > 0.
```

In canonical position `k <= (n-3t)/2`, so `n-k-2t >= (n-t)/2 > 0` and both arguments are
positive. Hence **`g` is strictly increasing in `k` for every `n` and every `t >= 1`**, so it
has at most one zero and **at most one `k` per `(n,t)` can solve the equation**. Binary
search on `sign(g)` locates it; the candidate and its neighbours are then confirmed with
exact integer `comb()`. The identity `t(n+k+2)` is re-verified at every `(n,t)` the search
visits — 0 failures — so the fact the method rests on is under test, not asserted.

`THE CONTROL THAT CARRIES THE MOST INFORMATION.` At `t = 1`, excluded by hypothesis, the
search finds `(15,5), (104,39), (714,272), (4895,1869)` — the Lind/Singmaster family, the
`(1,1)` class, Jenkins' unsettled `a = b`. Two of them, `n = 714` and `n = 4895`, **exceed**
`200·1² = 200`. So the hypothesis `t >= 2` is load-bearing and not cosmetic: drop it and the
bound is false immediately, against a family known since 1968.

`FOUR VERSIONS, THREE DISCARDED, AND WHY THAT IS PART OF THE RESULT.`
v1 tested every `(n,k)` with exact `comb()`: ~10⁸ comparisons of integers with thousands of
digits; it ran nine minutes and was abandoned — this record had asked for a *cheap* check and
the first thing written was the opposite. v2 added a float prune; still ~10⁸ Python-level
iterations. v3 introduced the binary search but kept exact tests on every candidate; ten
minutes, abandoned. v4 added a float guard, and this is the part worth recording: the guard
was first set at `1e-9`, the run reported **`min|g| = 1.07e-9`**, and so **zero** exact
comparisons executed — the whole absence claim rested on a float separation that had cleared
its own threshold by a factor of 1.07. A threshold a result barely clears is a threshold
chosen to clear it. Raised to `1e-5`, four orders above, and `3,313` exact integer
comparisons now run and all confirm. The claim is bound to exact arithmetic rather than to a
margin.

---

## What this record asks for

1. **Citation fix, mechanical:** every record in this lane citing `arXiv:1411.4111` should
   cite `Integers 16 (2016), Paper No. A69` and may keep the arXiv ID as the preprint.
   `referee/V1–V3` are frozen and must not be edited; the fix applies to unfrozen records,
   and this entry is the note a referee needs.
2. **`referee/V4` is warranted, for §2 only,** to name Beukers–Shorey–Tijdeman 1999 as the
   earlier ineffective-finiteness precedent. I am not issuing it: §2 states what the
   *contribution* is, the derivation is TOTO's, and reframing a joint contribution claim
   alone is the kind of thing that should not be done by one seat. **Routed to TOTO.** V3's
   two rows — effectivity uniformly new, finiteness new only for `t >= 3` — are unaffected
   and should not change.
3. **The §6 check is run, in §6a** — `tools/lit02_bound_vs_literature.py`, exit 0. It did
   not refute the bound, and it is genuinely discriminating only for `t <= 10`; at
   `t = 11, 12` the bound exceeds the search window and the PASS carries no information.
   What remains is a run at larger `t`. The `t = 1` control is the informative part: two of
   the four Lind/Singmaster solutions exceed `200·1²`, so the `t >= 2` hypothesis is
   load-bearing.
4. **The sweep is not closed.** `BOUNDED_PROXY`, for the reason in §4.

## Sources

- [Jenkins, *Repeated Binomial Coefficients and High-Degree Curves*, Integers 16 (2016) #A69](https://math.colgate.edu/~integers/q69/q69.pdf) — published version; 25 references; [volume index](https://math.colgate.edu/~integers/vol16.html)
- [Jenkins, arXiv:1411.4111](https://arxiv.org/abs/1411.4111) — submitted version ([PDF](https://arxiv.org/pdf/1411.4111))
- [Matomäki, Radziwiłł, Shao, Tao, Teräväinen, *Singmaster's conjecture in the interior of Pascal's triangle*, arXiv:2106.03335](https://arxiv.org/abs/2106.03335) — [journal version, Q. J. Math.](https://academic.oup.com/qjmath/article/73/3/1137/6563541)
- [*Binomial collisions and near collisions*, arXiv:1707.06893](https://arxiv.org/html/1707.06893)
- [de Weger, *Equal binomial coefficients: some elementary considerations*, J. Number Theory (1997)](https://research.tue.nl/en/publications/equal-binomial-coefficients-some-elementary-considerations/)
- Beukers, Shorey, Tijdeman (1999) — located through Jenkins' reference [4] and MRSTT's reference [4]; **the paper itself was not read**, and §2's description of it is taken from how those two sources describe it. `EVIDENCE CLASS: DERIVED, secondary.`
- [*Repetitions of multinomial coefficients and a generalization of Singmaster's conjecture*, arXiv:2107.09107](https://arxiv.org/pdf/2107.09107) — checked and **not** relevant: bounds `N_k(a)` for multinomials, no displacement equation, does not cite Jenkins

---

# Addendum, 2026-11-27 — the indexed citation search, run and its blind spot measured

§4 left the sweep at `BOUNDED_PROXY` with the reason stated: *"I have no indexed citation
database here, and `arXiv:1411.4111` and the Integers version are indexed separately, so a
paper citing only the Integers version by journal reference can be invisible to a
preprint-ID search. A library search on the Integers citation remains the right next step
and has not been done."*

It has now been attempted. The result is not a list of new citers; it is a **measurement of
why the search cannot be completed from here**, which is a better outcome than another
undated promise.

## What was reachable, and what refused

| route | outcome |
| --- | --- |
| Semantic Scholar API | refused at the network layer — `CONNECT tunnel failed, 403`. Not an allowed host in this runtime. **Not routed around.** |
| Semantic Scholar web search | `robots_disallowed` |
| Crossref API | permission request for the host went unanswered and was withdrawn |
| **OpenAlex API** | **worked** |

## What OpenAlex says

**Jenkins has exactly one indexed citation.**

- Record `W1799505236`, *Repeated Binomial Coefficients and High-Degree Curves*, Hugo
  Jenkins, 2014, `doi:10.48550/arXiv.1411.4111`, **`cited_by_count: 1`**.
- The single citer: **Matomäki, Radziwiłł, Shao, Tao, Teräväinen,
  *Singmaster's Conjecture In The Interior Of Pascal's Triangle*, Q. J. Math. 73 (2022),
  `doi:10.1093/qmath/haac006`** — already read in §4 of this record.
- A search of all 214 works under the author name returns **no separate Integers 2016
  record**. OpenAlex holds the `submittedVersion` only, marked `arXiv` as venue, with no
  accepted or published version attached.

So on the evidence reachable from here, **nothing cites Jenkins except the one paper this
record already read.**

## And the measured reason that is not conclusive

`filter=primary_location.source.issn:1553-1732` — the ISSN of *Integers*, confirmed from the
journal's own front page — returns **`meta.count = 0`**.

**OpenAlex indexes zero works from the journal Integers.**

That is the blind spot §4 predicted, now measured rather than suspected, and it is worse
than a gap in one record:

1. Jenkins' own published version is **not** in OpenAlex — only his preprint is, which is
   why the citation count attaches to a 2014 arXiv entry and not to `Integers 16 #A69`.
2. **Any paper published in Integers that cites Jenkins is invisible to this search.** And
   *Integers* is a journal of combinatorial number theory — the natural venue for follow-up
   work on repeated binomial coefficients. The one index that answered is structurally blind
   to the most likely place a competing result would appear.

So "one citation" is a **lower bound on an index with a known hole in exactly the wrong
place**, not a count of the literature.

## Status of the open item

`EVIDENCE CLASS: MEASURED` for the OpenAlex figures, the ISSN, the zero-count, and which
routes refused. `BOUNDED_PROXY` for the sweep's conclusion, **unchanged** — the reason is now
specific instead of general.

**What would close it, and none of it is reachable from this runtime:** MathSciNet or zbMATH,
both of which cover *Integers* and neither of which is an open API; or a direct read of the
Integers volumes after 2016 looking for the citation by hand, which is a bounded and finite
task — about ten volumes — and is the cheapest honest route left.

The originality claim in `referee/` therefore still rests on a sweep with a named hole. That
is a weaker statement than §4 made it sound, and it is the accurate one.

---

# Addendum 2, 2026-11-27 — the Integers hand read, done; and the one paper it was worth doing for

The first addendum named the route left: *"a direct read of the Integers volumes after 2016
looking for the citation by hand, which is a bounded and finite task — about ten volumes —
and is the cheapest honest route left."* This is that read, completed.

## Method, so a second reader can repeat it

Volumes **17 (2017) through 26 (2026)** — every volume after Jenkins' own 16 — were screened
from the journal's own volume index pages, `https://math.colgate.edu/~integers/vol<N>.html`,
one per volume. Screening was **by title**: any paper whose title put it in binomial
coefficients, Pascal's triangle, equal or near-equal binomial values, or Diophantine
equations in factorials/binomials was then fetched and read in full. Everything else was
left unread.

The journal's own pages are reachable only through the fetch tool in this runtime; the shell
is refused at the egress proxy for `math.colgate.edu` (`connect_rejected, HTTP 403`). That is
the same channel split already recorded for this lane and was **not routed around**.

**The limitation this method has, stated plainly:** title screening finds a paper *about* the
problem. It cannot find a paper with an unrelated title that cites Jenkins once in passing.
Closing that would require full text of ~10 volumes, roughly 600 papers, which is not a
bounded task here. So what follows is a result about the **problem**, not a certified
citation count.

## What the ten volumes contain in this territory

| volume | paper | relation to equal displacement |
| --- | --- | --- |
| 17 (2017) A64 | Blokhuis, Brouwer, de Weger, *Binomial Collisions and Near Collisions* | = `arXiv:1707.06893`, already read in §4 |
| 20 (2020) A13 | **Katsipis, *Diophantine Equations Coming From Binomial Near-collisions*** | near collisions at **fixed column pairs**, not equal displacement — read in full below |
| 21 (2021) A34 | de Koninck, Doyon, Verreault | = `arXiv:2107.09107`, already read and not relevant |
| 18, 19, 22, 23, 24, 25 | — | nothing in this territory |
| 26 (2026) A26 | Allen, *Solvability of `C(2k,k) = C(2a,a)·C(x+2b,b)`* | read in full; see below |

**No paper found in the ten volumes cites Jenkins.** Not Katsipis, not Allen, not the two
already known. The originality of the displacement bound survives the hand read.

## Volume 26 A26 — Allen, and why it is not a precedent

Meaghan Allen, *Solvability of* `C(2k,k) = C(2a,a)·C(x+2b,b)`, Integers 26 (2026) #A26.
Theorem 1: with `k = a + b`, the equation holds **iff `x = a = 1`**. Proof splits into
`x >= a`, `x = 1`, and `x >= 2 with k >= 150`, with Maple checks for the small range.
References: Erdős, Hanson, Laishram–Shorey, Moser, Nair–Shorey, Stănică. **No Jenkins, no
Singmaster, no Beukers–Shorey–Tijdeman.**

It is a *product* equation with a central coefficient on the left, not a repeat of one value
at two positions. The `k >= 150` threshold is a threshold in the paper's own parameter, not a
bound on `n` of our kind. Nothing in it touches `referee/`.

## Volume 20 A13 — Katsipis, and why it is the one finding that matters

Katsipis studies `C(m,l) − C(n,k) = d` for **fixed column pairs** `(l,k) = (3,6), (6,3),
(8,2)`. Not equal displacement: the columns are constants, not `k` and `k+t`, and the
right-hand side is a non-zero difference. **It does not cite Jenkins.** So it is not a
precedent either, and the originality conclusion above is unaffected.

What it *is*, is a **measurement of the thing `referee/ §6` is risking.** Jenkins' own
objection to the effective route is that the constants are "too large to be useful." That is
a qualitative sentence in our records. Katsipis puts numbers on it, for three concrete cases
of a near neighbour of our equation, using elliptic logarithms with S. David's Baker-type
bounds:

| quantity | value |
| --- | --- |
| `c_12` | ≈ `1.21 · 10^27` |
| `c_13` | ≈ `1.34 · 10^281` |
| bound on `M` before reduction | `< 6.86 · 10^147` |
| after LLL reduction | `M <= 27` |

Two things follow for this lane, and the second is the uncomfortable one.

1. **The LLL column is the encouraging half.** `10^147` collapsing to `27` is what reduction
   does for a *fixed, small* instance. It is an instance-by-instance collapse — three column
   pairs, each reduced on its own — not a uniform bound over a family.

2. **The `10^147` column is the warning.** Our claim is `n < 200t^2` — polynomial, uniform in
   `t`, with a constant of order `10^2`. The nearest effective work in the literature, on a
   *strictly easier* problem (fixed columns, one unknown pair at a time), needs intermediate
   constants at `10^147` to `10^281` before any reduction. A polynomial bound with a small
   constant over the whole family is therefore **not a small improvement on the literature's
   effective methods; it is a different order of result.** That raises, rather than lowers,
   the standard of proof §6 has to meet. §6's risk entry should be read with these numbers
   next to it.

This is not a refutation of anything in `referee/`. It is the first *quantitative* anchor we
have for "too large to be useful," and it says the gap our claim has to cross is 145 orders
of magnitude wide on the nearest comparable problem.

## Status of the open item, after the hand read

`EVIDENCE CLASS: DERIVED` for every reading above — each is a reading of a primary source at
a named locator, and a second reader can disagree from the same locators. The volume
enumeration (which volumes exist, which papers each index lists) is `MEASURED`.

The sweep's conclusion moves, but not to closed:

- **Before:** `BOUNDED_PROXY` — one index answered, and it was blind to the most likely venue.
- **Now:** the blind venue has been read by hand, by title, and holds no citer. The remaining
  hole is **no longer a venue**; it is a **method** hole: incidental citations in papers whose
  titles are off-topic, anywhere in the literature, and the two indexes that cover *Integers*
  (MathSciNet, zbMATH) are still not reachable from this runtime.
- So: **`BOUNDED_PROXY` still, with a smaller and differently-shaped bound.** The honest
  sentence for `referee/` is now *"no paper about this problem, in the journal where such a
  paper would appear, cites Jenkins"* — which is a real statement — and **not** *"nothing
  cites Jenkins,"* which is still not supported.

The §4 open item is therefore **narrowed and recorded as narrowed, not closed.** I am not
upgrading it further from this runtime, and the §6 risk entry now has Katsipis' constants
attached to it.

## Sources added by this addendum

- [Katsipis, *Diophantine Equations Coming From Binomial Near-collisions*, Integers 20 (2020) #A13](https://math.colgate.edu/~integers/u13/u13.pdf) — read in full; does not cite Jenkins
- [Allen, *Solvability of* `C(2k,k) = C(2a,a)C(x+2b,b)`, Integers 26 (2026) #A26](https://math.colgate.edu/~integers/aa26/aa26.pdf) — read in full; does not cite Jenkins
- Integers volume indexes 17–26, `https://math.colgate.edu/~integers/vol<N>.html` — the screening surface
