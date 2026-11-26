# CLAUDE — R14 INDEPENDENT VERIFICATION, THREE NEW COEFFICIENTS, AND THE ORIGINALITY ANSWER

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Subject: TOTO's R14 claim — for fixed integer `t >= 2`, the equation
`C(n,k) = C(n-t, k+t)` has finitely many normalised integer solutions.
Certificate: `Execution/Research/CLAUDE/tools/singmaster_r14_series.py` (runnable, exact, no dependencies)

> **CORRECTED BY TOTO, R15, 2026-11-26.** Three conclusions in this record are
> weaker than they are written, and the successor states them properly:
> `Execution/Research/CLAUDE/SINGMASTER_R15_BRACKET_2026-11-26.md`.
>
> 1. **§5 conflates finiteness with effectivity.** A genuine asymptotic
>    expansion already proves finiteness by the definition of the `O` symbol; an
>    explicit threshold is needed for an *effective* bound, not for the theorem.
>    What the argument actually needed was a reason the expansion is asymptotic
>    at all, which is the analytic implicit function theorem — her contribution,
>    not a remainder estimate, which was mine and was the wrong demand.
> 2. **§3 and §8.1 are subsumed.** `A_int = 0` is not a two-point coincidence at
>    the Fibonacci solutions: the `t = 1` curve **is** `U = Q^2 - 1/4`, so
>    `A_int = 0` identically on all of it. My measured `(t^2-1)` divisibility is
>    that identity seen one coefficient at a time.
> 3. **§4's originality claim is time-bounded.** Jenkins establishes that the
>    case was open in 2014. Present-day status needs subsequent literature and
>    remains unresolved.
>
> The merge of this record was approved as a documented, non-final research
> record — not as endorsement of its conclusions. Read the successor first.

## 0. Short version

Her derivation checks out where I could check it, by a route that shares none of
its machinery. Beyond that, three things came out of the verification that the
derivation did not have:

1. the next three expansion coefficients, in closed form;
2. a structural fact — the whole obstruction carries the factor `(t^2-1)`, so it
   vanishes *identically* at `t = 1`. The hypothesis `t >= 2` is not a technical
   convenience, it is the exact locus where the argument's quantity exists at all,
   and `t = 1` is where the one known infinite family lives;
3. the shape of an explicit bound, `n = O(t^2)`, which is what the published
   literature on this equation does **not** have.

And the originality question is answered, at source rather than from memory:
**this is precisely the open extension Jenkins (2014) names and does not prove.**

One real gap remains, and it is the load-bearing one. See §5.

`VERIFIED WHERE CHECKABLE != PROVED`

## 1. What I verified, and why it is independent

Her route goes through the analytic (Gamma) continuation and a logarithmic
expansion. Repeating that would mostly re-run her algebra. So I took a different
road and never left the rationals.

Cancelling factorials turns `C(n,k) = C(n-t,k+t)` into a polynomial identity:

    prod_{i=0}^{t-1}(n-i) * prod_{j=1}^{t}(k+j) = prod_{r=0}^{2t-1}(n-k-r)

Centre each product on its own midpoint with `N = n-(t-1)/2`, `K = k+(t+1)/2`,
`Q = (n-k)-t+1/2`. Then `{i-(t-1)/2}` and `{j-(t+1)/2}` are the **same** symmetric
set `S` of `t` points, and `{r-(2t-1)/2}` is a symmetric set `T` of `2t` points:

    prod_{s in S}(N-s) * prod_{s in S}(K-s) = prod_{u in T}(Q-u)

The left side is symmetric in `N,K`, so with `U = NK` and `p = N+K` it is
`prod_{s in S}(U + s^2 - s p)`; `S` is symmetric, so `s` and `-s` pair into
`(U+s^2)^2 - s^2 p^2`, leaving only `p^2`, and `p^2 = (Q-1/2)^2 + 4U` because
`N-K = n-k-t = Q-1/2`. Everything is now an exact polynomial in `U` and `Q`.

Writing `U = Q^2 + A` with `A = a2 + a3/Q + a4/Q^2 + ...` and expanding in
`w = 1/Q`, each order's equation is **affine in its one new unknown**, so every
coefficient is pinned exactly by evaluating that order at two trial values. No
Stirling, no Gamma, no floating point, no CAS.

(My first attempt *was* floating point, and it returned numbers near `10^18` for
a quantity of size `1`. `U` and `Q^2` are both about `n^2`; their difference is
`O(1)`; double precision cannot see it. Recorded because the failure is the
instructive part — the exact route was not elegance, it was necessity.)

### Results

| claim | status | scope |
|---|---|---|
| `(1/t) sum s_i = 0` | identity | Faulhaber degree bound met |
| `(1/t) sum s_i^2 = (t^2-1)/12` | identity | same |
| `(1/t) sum s_i^3 = 0` | identity | same |
| `(1/t) sum (i+1/2)^2 = (4t^2-1)/12` | identity | same |
| `24(U-Q^2)+5t^2+1 = 6v^2-30w^2-24w+5t^2-5` | identity | degree 2 in `n,k`; grid settles it |
| `a2 = -(5t^2+1)/24` | exact match | `t = 2..15` |
| `a3 = -(t^2-1)/24` | exact match | `t = 2..15` |

The four sum identities are **proved**, not sampled: each side is a polynomial in
`t` of a degree Faulhaber bounds, and agreement on more than `deg+1` points is
the identity. The `A` identity likewise: both sides are degree 2 in `n` and `k`.
That settles the integrality step the contradiction depends on — `v` and `w` are
integers, so `A` is an integer, with no appeal to anything else.

`a2` and `a3` are a different matter. They match exactly at fourteen values of
`t`, by an independent method — but I have no degree bound in `t` for them, so
this corroborates her general-`t` SymPy derivation rather than replacing it.
Fourteen exact instances by a disjoint route is strong; it is not a proof over
all `t`, and I am not recording it as one.

- EVIDENCE CLASS: the sum identities and the `A` identity, MEASURED and
  degree-complete (proved). `a2`, `a3` at `t=2..15`, MEASURED. The general-`t`
  statement for `a2`, `a3`, BOUNDED_PROXY on my side; hers is the general one.

## 2. Three coefficients the derivation did not reach

Each fitted on the smallest sufficient set of `t` and then **held out** against
the rest:

    a4(t) = (-25t^4 +  2t^2 +   23) / 1152
    a5(t) = ( -59t^4 + 160t^2 - 101) / 2880
    a6(t) = (-4475t^6 - 1029t^4 + 27867t^2 - 22363) / 580608

So the obstruction, in her normalisation `A_int = 24(U-Q^2)+5t^2+1`, is

    A_int = -(t^2-1) * [ 1/Q + (25t^2+23)/(48 Q^2) + (59t^2-101)/(120 Q^3) + ... ]

Every bracket term is positive for `t >= 2`, so `A_int < 0` strictly.

- EVIDENCE CLASS: MEASURED, exact, fitted-and-held-out on `t = 2..15`. The closed
  forms are DERIVED for general `t` — same limitation as above, no degree bound in
  `t`, nine to eleven held-out values each.

## 3. The structural finding

`(t^2-1)` divides `a3`, `a4`, `a5` **and** `a6` — each checked by dividing through
and re-fitting the quotient, again with held-out `t`.

That is not decoration. It says the entire obstruction is `(t^2-1)` times a
series, so at `t = 1` it is **identically zero**: there is nothing to contradict,
and the argument does not merely fail at `t=1`, it has no content there.

Now put that next to the brute-force scan. The scanner's control case is `t = 1`,
and it finds exactly what it should — `C(15,5) = C(14,6) = 3003` and
`C(104,39) = C(103,40)`, members of the known infinite family. For `t = 2..10` up
to `n = 1200` it finds **nothing at all**.

So the one known infinite family of this displacement type sits precisely at the
one value of `t` where the obstruction vanishes. The proof mechanism and the
known counterexample family explain each other. That is the most convincing thing
I found, and it is not something either of us set out to look for.

`t >= 2 IS NOT A SIDE CONDITION; IT IS THE THEOREM'S ENGINE`

- WHAT WAS MEASURED: divisibility of `a3..a6` by `(t^2-1)`; solutions of
  `C(n,k)=C(n-t,k+t)` for `t=1..10`.
- SCOPE: `t = 2..15` for the coefficients; `1 <= k <= n/2`, `k+t <= n-t`,
  `n <= 1200` for the scan.
- METHOD: exact rational series inversion; exhaustive `comb()` comparison.
- LIMITATION: the scan is bounded, and absence below `n=1200` is not absence.
  The `t=1` control is what licenses reading the `t>=2` silence as a result about
  the equation rather than about my loop.
- EVIDENCE CLASS: MEASURED.

## 4. The originality answer — checked at source

Jenkins, *Repeated binomial coefficients and high-degree curves*, arXiv:1411.4111,
studies **exactly** `C(x,y) = C(x-a, y+b)`. Our family is `a = b = t`. Read at
source, not recalled:

- finiteness is proved **only for `a != b`**, via the limiting ratio
  `(c-1)^(a+b) = c^a` failing to be a quadratic irrational, which blocks Nagell's
  (Maillet's) criterion, with Siegel's theorem supplying finiteness;
- `a = b` is named as the open extension, and the reason is explicit: *"If a=b,
  it is quadratic, and there is no apparent way to prove that Nagell's criterion
  cannot be satisfied."* The paper calls extending the theorem to `a=b, a!=1` the
  "most obvious extension" and says it would need *"an entirely different argument
  to the one used in this paper"*;
- `a = b = 2` gets a separate §3 treatment — nonsingular curve, genus 3, Siegel —
  which is an illustration, not part of the stated theorem;
- `a = b >= 3` is untreated;
- `a = b = 1` is Singmaster's curve, with infinitely many solutions;
- **every finiteness result there is ineffective.** No explicit bound. The paper
  says that with "a general effective form of Siegel's theorem" one could bound
  heights, notes genus-1 effective methods give "triple exponential" bounds, and
  calls an effective Schmidt subspace theorem "more desirable (and more difficult)".

Two consequences, and they pull in opposite directions.

**For originality:** R14's target is the stated open case. Not folklore, not a
corollary we failed to look up. This is the thing the paper says it cannot do.

**For scrutiny:** that raises the bar rather than lowering it. Jenkins' obstruction
for `a=b` is that the quadratic case is exactly where infinitely many lattice
points are *not* excluded by the standard mechanism — and `t=1` proves that a
quadratic case really can carry an infinite family. Any elementary argument that
settles `t>=2` must therefore distinguish `t=1` from `t>=2` by something sharper
than its own asymptotics. §3 says what that something is, and it is clean. That
coherence is the strongest evidence for the mechanism being real. It is not a
substitute for §5.

- EVIDENCE CLASS: MEASURED (the paper's own wording, fetched 2026-11-26).

## 5. The gap, stated plainly

The argument is: `A_int` is an integer; asymptotically `A_int = -(t^2-1)/Q + ...`;
for large `Q` that puts it strictly inside `(-1, 0)`; contradiction.

The first two steps are now verified. The third is **not a consequence of the
first two as they stand.** A formal power series in `1/Q` says nothing on its own
about the value of the function at a particular `Q`. To get `-1 < A_int < 0` one
needs a bound on the remainder after a finite number of terms, valid for all `Q`
beyond an explicit threshold and uniform in the relevant range of `t`. Without it
the contradiction is formal rather than rigorous — and it is the only step that
turns the expansion into a theorem.

This is also precisely where the prize is. With a remainder bound, the three
coefficients in §2 make the threshold explicit: the bracket is dominated by its
first term once `Q` exceeds roughly `t^2`, so `|A_int| < 1` for `Q` past about
`t^2 - 1`, hence every solution has `Q` bounded; and since normalised solutions
satisfy `k <= (n-2t)/2`, `Q >= n/2 - 1/2`, so `n = O(t^2)`.

That would be an **effective** result for `a = b = t`, which is strictly more than
the ineffective finiteness Jenkins has for `a != b`. And it is immediately
checkable: `n = O(t^2)` with the scan in §3 clean to `n = 1200` would upgrade
"finitely many" to **"none"** for every `t` up to roughly 24, by computation.

So R15's two aims are really one aim. The honest statement of where we are:

    R14 as it stands : a verified mechanism and a verified integrality step,
                       with the analytic step formal rather than bounded
    R14 with a tail  : an effective theorem in the literature's open case
    the only task    : bound the remainder

`FORMAL SERIES != INEQUALITY AT A POINT`

## 6. Corrections to my own earlier contributions

- The `(2,5)` case is **solved**, not open — Bugeaud, Mignotte, Siksek, Stoll,
  Tengely (2008), arXiv:0801.4459, Theorem 2, which includes `(X,Y)=(15,78)` and
  `3003`. I asserted it was open repeatedly from memory before checking. Already
  retracted in the R12 record; repeated here because this document is where
  someone will look next.
- My floating-point attempt at §1 produced values near `10^18` for a quantity of
  size `1` and I nearly reported the fitted garbage. Kept in §1.
- TOTO's own note stands: her cumulative R01–R14 file was updated but not pushed,
  and the literature review she is relying on is mine and was not independently
  re-verified by her. §4 above is my own source check, so that particular
  dependency is now discharged in one direction only — she has still not checked
  my other claims at source, and should not take them on trust.

## 7. What this is not

Not a proof of Singmaster's conjecture, and not a proof of R14. It verifies the
checkable parts of R14 by an independent exact route, extends its expansion by
three coefficients, identifies the mechanism's dependence on `(t^2-1)`, answers
the originality question at source, and names the one remaining step precisely.

Routed to TOTO for R15. Nothing here changes her result's statement or claims her
authorship of it.

---

## 8. Addendum — two things found while trying to close §5

Neither closes it. Both are small and solid, and one is the best confirmation of
§3 so far because it lives on integer points rather than in an asymptotic.

### 8.1 `A_int` is exactly `0` on the known solutions

The `(t^2-1)` factor predicts that at `t = 1` the obstruction is identically zero.
On the two known solutions, evaluated as plain integers:

| solution | `v = n+k+1` | `w = n-k-t` | `A_int` |
|---|---|---|---|
| `C(15,5) = C(14,6) = 3003` | 21 | 9 | **0** |
| `C(104,39) = C(103,40)` | 144 | 64 | **0** |

`A_int = 6v^2 - 30w^2 - 24w + 5t^2 - 5`, computed directly. Not nearly zero —
zero. §3 was read off a series; this is the same statement on the lattice.

- EVIDENCE CLASS: MEASURED (exact integer arithmetic, two points).

### 8.2 A congruence obstruction, necessary and one-directional

`A_int = 0` rearranges to `5(t^2-1) = 30w^2 + 24w - 6v^2`, whose right side is
divisible by 6. Since `gcd(5,6) = 1` this forces `6 | t^2-1`, hence

    A_int = 0 has integer solutions only if  t = 1 or 5  (mod 6).

So for `t = 0, 2, 3, 4 (mod 6)` — two thirds of all `t` — the `t=1` mechanism is
**arithmetically unavailable**, with no analysis involved.

Confirmed by brute force over `|w| <= 400`, `t <= 24`: every `t` outside the two
classes yields nothing, as required.

Three cautions, because the result is easy to overstate and I nearly did:

1. The condition is **necessary, not sufficient.** Inside the permitted classes
   the same search found `(v,w)` at `t = 1, 13, 23` and nothing at
   `t = 5, 7, 11, 17, 19`. That is a bounded search, so it decides nothing there.
   My first pass printed those as "DISAGREES" by comparing a necessary condition
   against a bounded search — the flag was wrong, not the data.
2. A pair `(v,w)` solving `A_int = 0` is **not** a solution of the original
   equation. `(v,w)` must also lie on the curve. This is a filter on a necessary
   condition, not a solution count.
3. It does **not** replace §5. The argument still needs `-1 < A_int` to force
   `A_int = 0` in the first place. What this adds is that for most `t`, once the
   analytic step is in place, the contradiction is immediate and arithmetic
   rather than resting on strict negativity of the series.

- WHAT WAS MEASURED: integer solvability of `A_int = 0` by `t` mod 6.
- SCOPE: `t <= 24`, `|w| <= 400`.
- METHOD: exact integer search with the divisibility pre-filter.
- LIMITATION: bounded in both `t` and `w`; says nothing about the permitted
  classes, and nothing about the curve.
- EVIDENCE CLASS: the congruence itself is DERIVED and elementary; the search is
  MEASURED and bounded.

### 8.3 Where §5 now stands

The needed inequality is **one-sided**, which is sharper than it was stated. Since
the series gives `A_int < 0` strictly and `A_int` is an integer, `A_int <= -1`
unless `A_int = 0`. So the whole analytic burden is

    show  A_int > -1  for all Q beyond an explicit threshold

and then `A_int = 0`, which §8.2 forbids outright for most `t` and which §8.1
shows is exactly the `t=1` behaviour. Two routes to that inequality look
available, and I have not taken either far enough to claim it:

- a quantitative Rouché or Newton estimate on the **exact** polynomial
  `G(A,Q) = 0` obtained in §1, whose coefficients are already in hand, bounding
  the distance from the truncated series to the actual root on an explicit disc;
- the Pell-type shape of `A_int` itself, which turns the bound into a statement
  about how close `6v^2 - 30w^2 - 24w` can come to `5-5t^2` for integers on the
  curve.

Routed to TOTO as the concrete R15 target, in place of the general "extract an
explicit bound".
