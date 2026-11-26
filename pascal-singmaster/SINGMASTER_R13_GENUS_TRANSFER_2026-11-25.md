# CLAUDE — Singmaster lab, R13: using the tool we read, on a case the source left open

Date: 2026-11-25
Author: CLAUDE
Role: `ANALYSIS — knowledge-transfer test proposed by TOTO`
Status: `COMPUTER-VERIFIED FOR t <= 5 / NOT A SYMBOLIC PROOF / ORIGINALITY UNRESOLVED`

TOTO designed R13 as a transfer test rather than a research step: reproduce Jenkins'
`t = 2` result to show the tool is understood, then apply the same tool at `t = 3`, where
his paper stops. Reading a method and using it are different claims, and only the second
is evidence of learning. This is that test.

Her correction to me is accepted and is the reason the test is shaped this way: I had said
the difference between `t = 1` and `t >= 2` "is the degree." Degree fixes the genus only for
a smooth irreducible plane curve. Singularities and reducibility are exactly what has to be
checked, not assumed.

---

## 1. What was computed

For `F_t(n,k) = prod_{i=0}^{2t-1}(n-k-i) - prod_{i=0}^{t-1}(n-i) * prod_{j=1}^{t}(k+j)`,
the curve of the equal-displacement transition `C(n,k) = C(n-t, k+t)`:

```text
 t   deg D   smooth   genus   integral points
 1     2      yes       0     not settled by genus alone - and in fact infinite
 2     4      yes       3     finitely many, by Siegel
 3     6      yes      10     finitely many, by Siegel
 4     8      yes      21     finitely many, by Siegel
 5    10      yes      36     finitely many, by Siegel
```

Identical under three independent primes: `2^61 - 1`, `2^31 - 1` and `1000003`. The runnable
certificate is `tools/singmaster_curve_genus.py` beside this file; it prints the degree, the
top form's squarefreeness, both resultant degrees, their leading coefficients and the gcd
degree, so a reader can redo the check rather than take the table on trust.

**Correction from TOTO, accepted.** The first version of this file said genus 0 means Siegel
"gives nothing". That is wrong as a general statement: Siegel gives finiteness for genus 0
too, once the curve has at least three points at infinity. Genus 0 with fewer is the case
that can carry infinitely many integral points, and `t = 1` is exactly that case. So the
right reading of the `t = 1` row is that the genus alone does not settle it, and the known
Fibonacci family settles it the other way.

**`t = 2` reproduces Jenkins**: smooth quartic, genus 3, finiteness by Siegel. That is the
check that the tool is being used correctly rather than invoked.

**`t = 1` is the control, and it is the better validation.** The tool returns genus 0 — where
Siegel says nothing — and `t = 1` is precisely the case with the known infinite Fibonacci
family. A method that returned "finite" there would have been refuted on the spot by a fact
we already had. It separates the known infinite case from the finite ones without being told
which is which.

**`t = 3, 4, 5` are new outputs of the same tool.** Jenkins settles `a = b = 2` in his
Section 3 and says of the general equal case: *"If a=b, it is quadratic, and there is no
apparent way to prove that Nagell's criterion cannot be satisfied,"* calling the extension to
`a = b != 1` "the most obvious extension" of his work. `a = b >= 3` is neither proved nor
conjectured there.

The genus values `0, 3, 10, 21, 36` are the ones TOTO tabulated as *conditional* on
smoothness and irreducibility. The condition is what was tested here, for `t <= 5`.

---

## 2. How, since there is no computer algebra in this runtime

No CAS is installed and the package index is unreachable, so the toolkit was written for
this: bivariate polynomials over `F_p` as coefficient dictionaries, derivatives, univariate
Euclid, resultants via the Euclidean algorithm with leading-coefficient bookkeeping, and
`Res_k(F, ·)` recovered as a polynomial in `n` by evaluation at `deg+1` points and Lagrange
interpolation.

Smoothness is then three checks:

- **no affine singularity** — `gcd(Res_k(F, F_n), Res_k(F, F_k))` is a nonzero constant. A
  singular point forces both resultants to vanish at its `n`, so a constant gcd rules them
  out. One-directional, which is the direction needed.
- **no singularity at infinity** — the top-degree form is squarefree, so it has no repeated
  root, so no point at infinity can have all partials vanish.
- **irreducibility** — follows from smoothness: two components would meet by Bézout and the
  intersection would be singular. This is Jenkins' own argument.

Then genus `= (D-1)(D-2)/2`, and Siegel's theorem for genus `>= 1`.

---

## 3. What this is not

**A certificate, not a sample — TOTO's second correction, also accepted.** I had called this
"computer-verified, not a proof". That undersold it. Each obstruction is the vanishing of an
integer-coefficient quantity, so a clean result at one prime that divides neither resultant's
leading coefficient *is* a characteristic-zero certificate: reduction cannot lower a gcd's
degree under that condition. The script asserts the leading-coefficient condition rather than
assuming it. What remains fair to say is narrower: the implementation is mine and has not been
reviewed, which is a software risk, not a mathematical gap — and §5 is what that risk looked
like in practice.

**Not effective.** Siegel's theorem gives finiteness with no computable bound on the size of
a solution. These results do not tell anyone where to stop searching, and MRSTT call exactly
this kind of bound *"completely ineffective."*

**Not uniform, which is the whole point.** `t <= 5` is five cases. The open problem Jenkins
names is a single argument covering all `t >= 2`, and the pattern here — smooth at every `t`
tried, genus growing — is a reason to look for one, not a substitute. Our earlier search
(zero solutions for `(2,2)`, `(3,3)`, `(4,4)` to `n < 2,000,000`) is consistent with
finiteness and proves nothing about it.

**Not deep.** Any reviewed CAS does this in minutes. The content of R13 is not the result; it
is that a tool read this morning was applied this afternoon to a case its source paper left
alone, and that the method announced its own control correctly.

**Originality unresolved.** Jenkins is 2014. Whether someone has since settled `a = b >= 3`,
or done it uniformly, has not been checked. The claim that his paper leaves it open rests on
a fetched reading of his Section 4, not on my own full reading of the paper.

---

## 4. One error worth recording, because the tool caught it

The first version of the reporting code printed, for `t = 1`: *"genus 0 >= 1, so Siegel's
theorem gives finitely many integral points."* Genus 0 is not `>= 1`, and `t = 1` has an
infinite family — so the line was both a coding error and a false mathematical statement,
contradicting a fact already in our own records.

It was caught because the control case had a known answer. A test whose control has a known
answer catches the bug in the test; one without a control reports the bug as a result.

```text
WHAT I AM NOT CLAIMING : smoothness for any t > 5; an effective bound; originality for
                         anything here; that the reduction in section 6 proves smoothness;
                         progress on Singmaster's conjecture itself.
HUMAN ACTION REQUIRED  : NONE
```

`READING A TOOL IS NOT HOLDING IT — RUN IT ON A CASE THE SOURCE DID NOT`

`A CONTROL WITH A KNOWN ANSWER CATCHES THE BUG IN THE TEST`

---

## 5. The small-prime bug, which nearly went into the repository as mathematics

TOTO ran her independent check over `F_101` with Gröbner bases. I ran mine at 101 to compare,
and it reported `t = 4` and `t = 5` as **singular** — contradicting my own earlier runs at two
large primes.

The mathematics was fine; my code was not. `Res_k` is recovered by evaluating at
`n = 1, 2, ... , bound+2` and interpolating, which needs that many *distinct* points. For
`t = 4` the bound is 114, so at `p = 101` the points wrap around, repeat, and the interpolation
returns noise — reported as a nonconstant gcd, which reads exactly like a singular curve.

The script now refuses a prime that is too small instead of answering:

```text
ValueError: prime 101 is too small: interpolating a degree-114 resultant needs 115 distinct
nonzero points, so p must exceed 115. Use a larger prime, or an elimination method that does
not interpolate.
```

This is why 101 is a fine prime for her method and a wrong one for mine. Had she not named her
prime, I would not have run mine there, and a silent failure mode would have stayed in a tool
whose output I was publishing as a result.

## 6. A uniform reduction of the affine singular locus

TOTO's unconditional result removes infinity for every `t`: the top form
`H_t(n,k) = (n-k)^{2t} - (nk)^t` has no repeated projective root, by her argument through
`q(r) = (1-r)^2/r`, whose derivative vanishes only at `r = ±1`, where `q` is `0` and `-4`,
neither a root of unity. That is hers, and it is the better half of the problem. What is left
is the affine part, which she named as the next step. Here is a reduction of it, uniform in `t`.

Write `F_t = P(u) - Q(n)R(k)` with `u = n - k`,
`P(u) = prod_{i=0}^{2t-1}(u-i)`, `Q(n) = prod_{i=0}^{t-1}(n-i)`, `R(k) = prod_{j=1}^{t}(k+j)`.

**`P` depends only on `u`, so `P_n + P_k = 0` identically** — verified symbolically for
`t = 1..6`, zero surviving terms. Therefore at any affine singular point:

```text
Q'(n) R(k) + Q(n) R'(k) = 0
```

one equation of degree `2t-1`, in place of the third degree-`2t` equation.

**And neither factor can vanish there.** If `Q(n) = 0` then `F = 0` forces `P(u) = 0`; but `P`
is a product of distinct linear factors, so `P'(u) != 0` at any root — while `F_k = 0` says
`-P'(u) = Q(n)R'(k) = 0`. Contradiction. The same argument rules out `R(k) = 0`. So the
logarithmic form is legitimate everywhere on the singular locus, and the locus is exactly:

```text
(i)    sum_{i=0}^{2t-1} 1/(n-k-i)   =   sum_{i=0}^{t-1} 1/(n-i)
(ii)   sum_{i=0}^{t-1} 1/(n-i)   +   sum_{j=1}^{t} 1/(k+j)   =   0
(iii)  P(n-k) = Q(n) R(k)
```

Two equations in two unknowns, with a third condition on top — which is the shape of a
generically empty set, though "generically" is not a proof and this does not establish
smoothness for any `t`.

**One consequence comes free, and it is uniform.** For `n > t-1` and `k > -1` every term in
(ii) is strictly positive, so (ii) has no solution there. So `F_t` has no *real* affine
singular point in the region where the arithmetic lives, for every `t`. Smoothness needs all
of `C^2`, so this does not finish it; it does say the singular locus, if any, is complex or
sits outside the triangle.

I also ran a random-point probe over `F_p` to "confirm" the reduction and it returned zero
failures in 16,000 draws. That probe is worthless — a random point is essentially never
singular, so it could not have failed — and it is recorded here only because reporting it as
support would have been the same mistake as the 0% test in R11. The symbolic check in the
first paragraph is the one that carries weight.

---

## 7. TOTO's symmetry, verified, and what `w = v^2` buys

All three of her claims check out. Verified independently here, and in each case the random
probe is a polynomial-identity test — a false identity fails at a random point of a field of
order `2^61-1` — which is the opposite of the vacuous singularity probe discarded in §6.

**The involution.** `(n,k) -> (-k-1, -n-1)` preserves `F_t` exactly: it fixes `u = n-k`, and
`Q(n') = (-1)^t R(k)`, `R(k') = (-1)^t Q(n)`, so the two signs cancel in the product. Zero
failures over 3,000 random points for each `t = 1..7`.

**The `v^2` form.** `4^t F_t = 4^t prod_{i<2t}(u-i) - prod_{i<t}[v^2 - (u-2i-1)^2]` with
`u = n-k`, `v = n+k+1`. Pairing `(n-i)` with `(k+i+1)` gives
`[v + (u-2i-1)][v - (u-2i-1)]/4` term by term. Zero failures, `t = 1..7`. The involution is
`v -> -v`, so the curve is even in `v`, as she says.

**The axis.** Her argument holds, and the step she passed over connects to §6. Writing
`N = prod(u-2i)` and `D = prod(u-2i-1)`:

```text
Phi(u,0) = D(u) * [ 4^t N(u) - (-1)^t D(u) ]
```

A root of `D` is a double root of `Phi(u,0)` only if it also kills the bracket, i.e. only if
`N(2i+1) = 0` — but `N(2i+1)` is a product of odd numbers, never zero. So `D`'s roots are
simple. Those points are exactly `n = i`, `k = -i-1`, which is `Q(n) = 0`, the case §6's lemma
already excluded. The bracket's roots are her `G_t(u) = (-1)^t/4^t`, simple because
`G_t = 1 + sum A_i/(u-2i-1)` has every `A_i > 0` (computed exactly for `t = 1..8`; the
partial-fraction identity verified at four rational points each). So `Phi(u,0)` has only
simple roots, and since `dF/dv = 2v Phi_w` vanishes identically on `v = 0`, a point there is
singular precisely when it is a repeated root. **No singularity on the axis, any `t`.**

### What the new variable does

`F_t = Phi(u, v^2)/4^t` with `Phi(u,w) = 4^t P(u) - M(u,w)`, `M = prod_{i<t}[w - a_i^2]`,
`a_i = u-2i-1`. Then `dF/dv = Phi_w * 2v`, so away from the axis:

```text
F_t = 0 is singular  <=>  Phi(u,w) = 0 is singular
```

The remaining problem is the smoothness of a curve of **degree `t` in `w`** rather than `2t`
in `v`. That is what `w` buys, stated exactly.

### And it closes the real case

`Phi_w = -M_w`, so an off-axis singular point needs `w` to be a **critical point of
`M(w) = prod(w - a_i^2)`**. By Gauss–Lucas those lie in the convex hull of `{a_i^2}`.

For **real** `u` every `a_i^2` is real and non-negative, so the hull sits in `[0, inf)`, so `w`
is real and non-negative, so `v = ±sqrt(w)` is real — and the singular point is a *real* point
of the plane. Checked on 11,200 critical points over random real `u`, `t = 2..8`: none
non-real, none negative.

Real points are where §6 bites. Condition (ii) has every term strictly positive when
`n > t-1` and `k > -1`, and strictly negative when `n < 0` and `k < -t`, so neither region can
hold one. **Those two exclusions are one statement seen twice**: her involution maps the first
region exactly onto the second, so they are not independent results and should not be counted
as two.

### Two errors of mine in this section, both found by TOTO's objection

**First: the case list was incomplete, so the conclusion did not follow.** I wrote that this
leaves "non-real `u`" as the only open case. That is wrong. Gauss–Lucas gives *real `u` implies
the singular point is real*, and §6 excludes only **two regions** of the real plane, not the
whole of it. The real plane outside those regions stays open, so the remaining cases are both
"non-real `u`" and "the rest of the real plane". Every step was sound; the enumeration was not,
which is a different kind of failure and the one that produced a false summary.

**Second, found while measuring the first: §6's condition (ii) is not independent of her axis
result.** Since `v = n+k+1`, moving along `(1,1)` raises `v` and fixes `u`, so
`F_n + F_k = 2 dF/dv`. Condition (ii) *was* `F_n + F_k = 0`. Therefore

```text
(ii)  <=>  dF/dv = 0  <=>  v = 0  or  Phi_w = 0
```

and on the axis `T(-n-1) = -S(n)` identically, so (ii) holds along the entire axis for free.
That is why a numerical hunt for solutions of (ii) kept returning points with `k = -n-1`: it
was rediscovering the axis. So (ii) says nothing new there — TOTO had already closed it. What
(ii) does add, and only this: **`Phi_w = 0` has no real point in regions A or B.**

Off-axis real solutions of (ii) do exist, so the open region is not empty: at `t = 2`,
`n = 0.3, k = -2.75` gives `v = -1.45` and `S + T = 0`.

### Corrected standing

```text
infinity                                   closed for all t   TOTO
the axis v = 0                             closed for all t   TOTO, + the D-root step from §6
real plane, n > t-1 and k > -1             excluded           §6
real plane, n < 0 and k < -t               excluded           §6, and it is region A under
                                                              her involution, not a second result
real plane, the two opposite-sign quadrants OPEN              non-empty, example above
non-real u                                 OPEN
```

Nothing here proves smoothness for any `t`, and the honest description of what this section
achieved is narrower than what I first wrote: `w = v^2` **simplified** the problem (degree `t`
instead of `2t`), Gauss–Lucas **moved** a constraint from one space to another, and the
partial-fraction argument — hers — is the only step in the round that **eliminated** anything
for all `t`. Those are three different kinds of progress and collapsing them into one word is
how the bad summary got written.

`A VALID CHAIN OF STEPS PROVES NOTHING IF THE CASE LIST IS INCOMPLETE`

`VARY THE PARAMETER THAT SHOULD NOT MATTER — IF THE ANSWER FOLLOWS IT, YOU MEASURED THE TOOL`

`DO NOT CALL A CASE SPACE CLOSED UNTIL THE REMAINING CASES ARE WRITTEN OUT`

---

## 8. Audit of TOTO's case map, and one gap in it

She asked me to check her case map for completeness and overlap before any new derivation.
That is the right order, and it is the check I failed in §7.

**The map is a genuine partition.** The branching is: points at infinity, then affine split by
`v = 0` or not, then by `u` real or not, then by `v` real or not, then by inside `A ∪ B` or
not. Every point of the projective curve lands in exactly one row, and no row overlaps
another. Verified branch by branch.

**She also avoided the double count I made**: `A` and `B` are one row in her map, not two.

### The gap: no row states its `t`

Every status in the map depends on `t`, and the map has no `t` column. For `t = 1..5` the
certificate in `tools/singmaster_curve_genus.py` says `F_t` has **no singular point anywhere**
— affine or at infinity — so both "open" rows are empty for those `t`. Read as written, the
map claims those cases are open, which overstates what is open by five values of `t`.

Corrected, the two open rows are open **for `t >= 6` only**. This is the same failure class as
mine in §7: a table every row of which is true, whose scope is not stated.

### A refinement to her own protocol

Her six tests include Independence — does a result add a constraint independent of the ones
already held. Her map passes that test at the level of *cases*, since the rows are disjoint.
But rows 2 and 5 rest on **overlapping evidence**: §7 showed `(ii) <=> (v = 0 or Phi_w = 0)`,
so the log-derivative argument behind row 5 already contains the axis case of row 2.

So Independence needs applying to the evidence column, not only to the result. A map can
partition the cases correctly and still count one argument's strength twice — which is exactly
the error I made, surviving into a table that is itself correct.

### The seventh column, filled with what is actually measured

```text
CASE                                    STATUS   t      BASIS
points at infinity                      closed   all    H_t squarefree, proved (TOTO)
affine, v = 0                           closed   all    partial fractions (TOTO) + the
                                                        D-root step, §7
off axis, u real, v non-real            empty    all    Gauss-Lucas; 11,200 critical points
                                                        checked, none non-real or negative
off axis, real, inside A u B            closed   all    log-derivative signs, §6
off axis, real, outside A u B           closed   <=6    certificate, 3 primes (t<=5);
                                        OPEN     >=6    non-empty region, example in §7
off axis, u non-real                    closed   <=5    same certificate
                                        OPEN     >=6    no argument of any kind
```

### My own contribution this round, downgraded twice

I claimed the open real case reduces to one dimension: `Phi = 0` and `Phi_w = 0` are two
equations in two unknowns, so finitely many `(u,w)`, and for real `u` both are real.

**First correction, mine:** I had dropped `Phi_u = 0`. The correct procedure is to solve
`{Phi = 0, Phi_w = 0}` exactly and then test `Phi_u` on that finite set. That is decisive, and
cheaper than the genus route — **but still per `t`**. It does not unlock the uniform case,
which is what the round was for.

**Second correction, also mine:** my first scan of the gap `|M(w) - 4^t P(u)|` returned exact
zeros, at `u = 2, 3, 5, 8` for various `t`. Those are the degenerate points where `P(u) = 0`
and two `a_i^2` collide — the `Q(n) = 0` points the simple-root lemma already excluded. The
scan was measuring the excluded set.

**Third correction: the repaired scan is worthless too, and I measured that rather than
guessing it.** Scanning away from the degenerate points gave minimum relative gaps of
`2.4e-4, 1.2e-4, 9.3e-6, 2.3e-6, 4.1e-7` for `t = 2..6` — small, and shrinking fast, which
reads like an approach to a crossing. So I tested the instrument: if those minima are only the
tails of the excluded zeros, widening the exclusion radius must raise them in step; if they
are a real near-crossing in the interior, the radius cannot matter.

```text
 t    radius 1e-3    radius 1e-2    radius 1e-1    radius 3e-1
 2      3.634e-06      3.634e-06      3.634e-06      2.507e-01
 3      1.371e-04      1.371e-04      1.371e-04      3.644e-02
 4      9.326e-06      9.326e-06      1.297e-04      1.297e-04
 5      1.140e-06      1.140e-06      1.543e-04      2.233e-04
 6      4.331e-05      4.663e-05      4.663e-05      4.663e-05
```

The minima move by three orders of magnitude with the radius alone. They also differ from the
previous run's figures at the same radius, because that run used a different window and grid
resolution. So the scan reports **how close I allowed it to approach the excluded points**,
and nothing about the curve.

Grid scanning is simply the wrong instrument here: the quantity has exact zeros at known
excluded points, so any minimum away from them is fixed by the exclusion radius and the grid
step. The decisive method is the exact one — eliminate `w` between `Phi` and `Phi_w`, then test
`Phi_u` on the finite root set — which remains per `t`.

Three contaminated measurements of one question in a row. What ended it was not a better scan
but a test of the scan: vary the one parameter that should not matter, and see whether the
answer follows it.

So by her own six tests, this round's contribution from me scores: Correctness pass,
Originality unknown, **Utility low** (a cheaper per-`t` certificate, no new exclusion),
Independence pass, Interpretation now corrected twice, Completeness pass only after §7's
repair. The one result in the round that eliminated anything for all `t` is hers.

---

## 9. The sensitivity rule, corrected — and it was partly vacuous

TOTO sharpened my rule and she is right, with a worse consequence than she stated. Her
version:

> Vary a parameter the scientific conclusion is supposed to be independent of. If the result
> changes strongly, analyse the instrument before reading the change as a property of the
> object.

And the correction that matters: widening the exclusion radius **shrinks the search domain**,
and the minimum of a function over a shrinking domain is non-decreasing. So the *direction* of
the change was a theorem, not a finding. My test could not have come out any other way, which
makes it another check that could not fail.

What did carry information was the **magnitude and the location**: `t = 2` jumped three orders
of magnitude between radius `1e-1` and `3e-1`, which places the minimiser within `0.3` of an
excluded point. Had the minimiser been interior, a small widening would have moved nothing. So
the repaired statement is about *where* the minimum sits, not that it moved:

`THE MINIMUM MOVED IS A THEOREM — WHERE THE MINIMISER SITS IS THE FINDING`

Her reviewer's distinction is the operative one: `t` is a **scientific** parameter and change
with it is expected; exclusion radius, grid step and window width are **instrument**
parameters, and a conclusion must be stable under all of them before it is used as evidence.

## 10. The assignment: what the sequence's regularity gives — and does not

`a_i = u - 2i - 1` is an arithmetic progression of difference `-2` centred at `c = u - t`, so
`a_i = c + d_i` with `d_i` running over the **symmetric** set `S = {t-1, t-3, ..., -(t-1)}`.
Three things follow, all verified exactly over random rationals for `t = 1..8`, zero
violations:

**Root differences factor completely.** `b_i - b_j = 4(j-i)(u-i-j-1)`.

**`M` splits into two copies of one polynomial.** With `F(x) = prod_{d in S}(x-d)`:

```text
M(u, v^2) = F(v - c) * F(v + c)
```

**The evenness in `v` becomes a one-line fact.** `S = -S` gives `F(-x) = (-1)^t F(x)`, so
`v -> -v` sends `F(v-c)F(v+c)` to `(-1)^{2t}` times itself. TOTO's involution, free.

### And it fails the Independence test

From `Phi = 4^t P(u) - F(v-c)F(v+c)` and `dPhi/dv = 2v Phi_w`, off the axis `Phi_w = 0` is

```text
sum_{d in S} 1/(v-c-d)  +  sum_{d in S} 1/(v+c-d)  =  0
```

and translating back — `v - c = 2k+1+t`, `v + c = 2n+1-t`, `F(2n+1-t) = 2^t Q(n)`,
`F(2k+1+t) = 2^t R(k)`, all verified — this **is** condition (ii),
`sum 1/(n-i) + sum 1/(k+j) = 0`.

So the regularity re-derives the factorisation and the involution more cleanly than before and
adds **no constraint independent of (ii)**. Correctness pass, Utility zero, Independence fail.

Her standing instruction for that outcome is to return to exact algebraic elimination, keeping
the target a general argument in `t` rather than more computed cases. That is where this goes
next, and the grid-scan file is closed as evidence about the instrument, not about the curve.

### On naming the seven axes

She is right that calling them "seven errors" is wrong: rediscovering a published result is not
an error, and neither is a correct result that does not help. They are **audit axes** —
Correctness, Originality, Utility, Independence, Interpretation, Completeness, and the seventh
the reviewer named, **Measurement Validity**: can the instrument resolve the question it is
being asked? That seventh is the one that closed the scan, and it is the only axis on which
nothing I did today passed on the first attempt.

## Sources

- H. Jenkins, *Repeated binomial coefficients and high-degree curves*, arXiv:1411.4111 (Section 3 for `a=b=2`, Section 4 for the open equal case) — https://arxiv.org/pdf/1411.4111
- K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen, arXiv:2106.03335, Remark 1.5 on ineffectiveness — https://arxiv.org/pdf/2106.03335
- TOTO, independent R13 review on this PR: SymPy elimination for `t = 1,2,3`, Gröbner bases over `F_101` for `t = 2..5`, the `H_t` result for all `t`, and the Siegel correction — https://github.com/Sangaa/ARGO-KOP/pull/890#issuecomment-7155712398
