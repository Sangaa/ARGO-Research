# CLAUDE — Singmaster lab, rounds R09–R11: what I measured, and one retraction

Date: 2026-11-25
Author: CLAUDE
Role: `ANALYSIS — participant, not owner of the research line`
Status: `RECORD OF MY OWN CONTRIBUTIONS / NOT A CLOSURE / LITERATURE REVIEW STILL OPEN`

Co-investigators: Human Authority (Essam), who set the direction at each turn, and TOTO,
who reviewed every round and corrected me more than once. TOTO keeps the cumulative
research log (`SINGMASTER_R01–R11`); this file records only my side, so that my claims
carry their own evidence and their own limits.

Nothing here is offered as original. Five results below are, as far as this lab has
checked, correct and unrefuted; **none of them has been checked against the literature**,
and for a problem worked on since 1971 that is the likeliest place they already live.

---

## 1. R09 — the premise of "composing two generating mechanisms" does not hold

TOTO proposed studying whether several generating mechanisms can meet at one number and
accumulate representations without bound — a possible constructive route to *disproving*
the conjecture. The proposal rested on 3003 being an actual example of two mechanisms
meeting. I tested that premise before deriving anything, and it failed.

Row 14 at k = 4,5,6 is `1001, 2002, 3003` — ratio exactly `1 : 2 : 3`.

```text
G1 (Pascal / Singmaster family) uses   1 + 2 = 3   ->  C(15,5) = C(14,4)+C(14,5) = C(14,6)
G2 (the composite-binomial identity)   3 = 3 x 1   ->  C(78,2) = 3*C(14,4)       = C(14,6)
```

These are two readings of one ratio vector, not two independent coincidences. And the
ratio itself is forced, not lucky: solving `r_k = (n-k)/(k+1) = 2` together with
`r_{k+1} = 3/2` has the single solution `(n,k) = (14,4)` — the only place in the triangle
where three consecutive entries stand in ratio 1:2:3. So R09 had no example to generalise
from.

`EVIDENCE CLASS: MEASURED` — all n < 4000 searched for the pair of ratio conditions; one
solution. Scope limit: n < 4000, not all n.

### 1b. There is no third generator of that family

TOTO asked whether other composite-binomial identities of the same shape exist. I searched
every `C(C(j,a),b) = L * C(j+c,d)`, for a,b ≤ 5 — the degree forces `d = a*b`, and two
degree-d polynomials agreeing at d+1 points are identical, so the test is exact.

**One identity in all sixteen (a,b) pairs**: `C(C(j,2),2) = 3*C(j+1,4)`. The obstruction is
sharp: `C(C(j,2),b)` needs `C(j,2) - t` to factor over Z for every `t < b`, i.e. `1 + 8t`
a perfect square. `t=0` gives 1 and `t=1` gives 9, but `t=2` gives 17. So `b = 2` is the
last case that works, and `a >= 3` fails at the first step.

`EVIDENCE CLASS: MEASURED` (exact polynomial identity test over a,b ≤ 5).

---

## 2. R10 — TOTO's limiting-direction law is correct, and it excludes nothing

TOTO generalised the asymptotic slope of the known family to any fixed transition
`(n,k) -> (n-d, k+e)`:

```text
(1 - r)^(d+e) = r^e ,     r = k/n
```

I re-derived it from the transition law (`LHS ~ n^(d+e)(1-r)^(d+e)`, `RHS ~ n^d (rn)^e`) and
it is right. Her value for `d=8, e=1` reproduces to eight decimals (`0.17569944`), and
`d=e=1` gives `(3-sqrt5)/2 = 1/phi^2` — which is *why* the known family is Fibonacci: the
condition `1 + t = t^2` is the definition of phi. The accompanying angle, 20.529°, matches
none of the four conventions I tried (atan r = 9.965°, equilateral-from-vertical = 17.968°,
atan(e/d) = 7.125°, 60°-lattice = 5.818°); it needs its convention stated.

**My test of the law's strength.** Admissibility needs `r` in `(0, 1/2]`. With
`f(r) = (1-r)^(d+e) - r^e`: `f(0+) = 1 > 0`, `f(1/2) = 2^-(d+e) - 2^-e < 0` for `d >= 1`, and
f is strictly decreasing there. So **every** `(d,e)` with `d,e >= 1` has exactly one
admissible direction — checked on all 144 pairs with d,e ≤ 12, zero exclusions. The law is
a necessary condition that every direction satisfies. It cannot bound `N(a)`. Its value is
as a search heuristic.

`EVIDENCE CLASS: MEASURED` (144 pairs) for the non-exclusion; `DERIVED` for the law.

### 2b. Using it as a heuristic, and what that found

The transition law is **polynomial**, so no binomial coefficients need computing — which
lifts the search far past where binomial arithmetic stalls. Searching `k ~ r(d,e)*n` for
sixteen directions, `n < 2,000,000`:

```text
(1,1)  six solutions: (15,5) (104,39) (714,272) (4895,1869) (33552,12815) (229970,87840)
(1,3)  one: (15,5)   — 3003 again, through the mirror C(14,8)=C(14,6)
(2,1)  one: (6,1)    — the trivial 6 = C(4,2)
other thirteen directions: none
```

The sixth `(1,1)` member is `F14*F15, F12*F15` — exactly the next term of Singmaster's
published Fibonacci family, so this is a validation that the method reproduces the known
family, **not a discovery**. Across sixteen directions and two million rows, no new family.

`EVIDENCE CLASS: MEASURED`, with a scope limit that matters: the search tests integer
candidates `k0-1 .. k0+2` around the predicted slope, so a family whose k drifts further
from `r*n` than two units would be missed.

That shortcut needs its own check, since the whole two-million-row reach depends on the
polynomial form standing in for the binomial equality. Brute force over **every** k for
`n < 3000`, comparing actual binomial coefficients, returns exactly the same hits in exactly
the same directions — `(1,1)` three times, `(1,3)` at (15,5), `(2,1)` at (6,1), and nothing
anywhere else. The fast path and the slow path agree wherever both can run.

**And TOTO's correction to this, which I accept:** a fixed direction forces `k ≍ n`, i.e.
the deep interior, where Matomäki–Radziwiłł–Shao–Tao–Teräväinen (2022) already bound the
number of representations. So a negative result there was substantially expected, and is
weaker evidence than it first looks. Her narrower point is also right, and limits my
concession: that theorem bounds representations, it does not classify the mechanisms that
produce them, so fixed-direction study is not worthless — only poorly aimed.

---

## 3. R11 — her row-window bound: correct, and one retraction of mine

For `x = C(n,k)` with `k` known, put `z = (x * k!)^(1/k)` and `a = (k-1)/2`:

```text
z + a  <=  n  <=  sqrt(z^2 + a^2) + a ,     window width  W <= (k-1)^2 / (8z)
```

**Proof, shorter than the one in her note.** `x*k! = prod_{j<k} (n-j)`, and those factors are
symmetric about `m = n - a`, so the product is `prod (m^2 - c_i^2)` with `0 <= c_i <= a`.
Each factor is `<= m^2`, giving `z <= m`; each is `>= m^2 - a^2`, giving `z^2 >= m^2 - a^2`.
The width follows from `sqrt(z^2+a^2) - z = a^2 / (sqrt(z^2+a^2) + z) <= a^2/(2z)`, an exact
inequality rather than an asymptotic one.

Verified on every `(n,k)` with `n <= 1200, k <= n/2` in exact integer arithmetic:
**360,000 cases, zero violations** (her own run covered 22,500 cases to row 300). Separately,
the window never *misses* a true representation: 39,402 true pairs to row 400, zero missed.

`EVIDENCE CLASS: MEASURED` within `n <= 1200`; `DERIVED` in general, from the proof above.

### 3a. As a bound on N(x) it yields only the trivial bound

The window pins `n` once `k` is known, so `N(x)` is at most the number of admissible
columns, and a column is admissible only while `C(2k,k) <= x`, i.e. `k` of order `log x`.
That is the classical `O(log x)` bound, which Abbott, Erdős and Hanson improved to
`O(log x / log log x)` in 1974.

**TOTO's correction, which I accept and which matters:** "this bound implies nothing better
than 1974" is not the same claim as "this formula is itself known since 1974." The second is
a question about the literature that nobody here has answered. I had run the two together.

### 3b. RETRACTION — my "78x speedup" was wrong

I reported that her window beats binary search by 78x at enumerating all representations of
x. TOTO's reservation — an empirical figure on one input family is not a general guarantee —
was right, and the truth is worse than her reservation. Two faults:

1. The thing I timed was **not her bound**. It used a low-precision `z` and then tested three
   integers near it — an unproven heuristic window, not the proven one. It happened to agree
   with binary search on all 660 inputs, which is why I did not notice.
2. My sample was one narrow band of magnitudes.

Re-measured with the proven window, computed to 96 bits of precision so the interval is
genuinely the one in the theorem:

```text
x digits      cases   window      bisect      ratio
   5 - 8        25    0.002 s     0.001 s      0.3x   (a 3x SLOWDOWN)
  11 - 15       25    0.012 s     0.012 s      1.0x
  23 - 30       25    0.089 s     0.264 s      3.0x
```

Results identical to binary search throughout. So the honest statement is: the window is a
slowdown on small inputs and a modest speedup that grows with the size of x — not 78x, and
not a uniform win. The earlier figure should not be carried forward.

`EVIDENCE CLASS: MEASURED`, 25 inputs per band, one machine, CPython; a different language or
a cheaper exact k-th root would move these numbers.

### 3c. Her column-rejection idea does hold up

TOTO proposed rejecting a whole column when its window contains no integer, without ever
computing a binomial coefficient. On 160 values spanning 3,629 columns:

```text
columns killed by an empty window (k-th root only):  1,900  = 52.4%
columns still needing a binomial check:              1,729  = 47.6%
```

So just over half the work disappears before any binomial is formed. This is the part of R11
that survives as a practical gain.

`EVIDENCE CLASS: MEASURED` (3,629 columns). My first attempt at this test returned 0% and I
briefly reported the idea as confirmed anyway — the test was invalid, because an imprecise
`z` had inflated the window to a full unit so that it always contained an integer. A test
that cannot reject is not a test, and I had printed its conclusion before reading its number.

---

## 4. Standing position

```text
RESULT                                   STATUS
transition law  prod(n-k-t) = ...        derived, used throughout, LITERATURE UNCHECKED
(1,1) cannot chain  (5(n-k)=8)           proved two ways,          LITERATURE UNCHECKED
slope strictly increasing                proved (trigamma),        LITERATURE UNCHECKED
C(C(j,2),2) = 3 C(j+1,4), and j=13       proved; reviewed by TOTO, LITERATURE UNCHECKED
limiting directions (1-r)^(d+e) = r^e    TOTO's; re-derived here,  LITERATURE UNCHECKED
row window  z+a <= n <= sqrt(z^2+a^2)+a  TOTO's; re-proved here,   LITERATURE UNCHECKED
```

The conjecture is not solved and nothing here approaches solving it. What the lab has is a
set of correct, small, mutually consistent results and a sharper sense of where the open
ground is: the **edges** (small k), where the window bound is tightest and where the one
genuinely open collision pair — (2,5), the pair behind 3003 — still sits.

**The next step is reading, not deriving.** Twice in one day a cheap literature check would
have saved the work: the `O(log x)` bound was settled in 1974, and the interior region in
2022. Yamada, Laishram–Shorey and Nair–Shorey are where the six results above should be
taken before any of them is called new.

```text
WHAT I AM NOT CLAIMING : no originality for any result here; no progress on the conjecture;
                         no literature review performed.
HUMAN ACTION REQUIRED  : NONE
```

`A TEST THAT CANNOT REJECT IS NOT A TEST`

`NOT BETTER THAN 1974 != PUBLISHED IN 1974`
