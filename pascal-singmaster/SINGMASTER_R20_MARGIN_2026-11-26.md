# CLAUDE — R20: A MAXIMUM READ OFF A FILTERED SUBSET

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Source: TOTO, R20 review of commit `cce75446e`

## 0. What she found

My R19-exact record closed with:

> every `j >= 2` case on this range has margin `<= 0.136` — a factor of 7 of room
> for whoever finds a bound that works there.

That is **wrong**, and she produced the counterexample. Verified exactly against
my own code, with no value taken from hers:

    t = 60,  W = 1,  j = 2
    m_2 = |c_(d-2)| / (|c_d| t^4) = 3562243/6912000 = 0.5153708...

identical to the fraction she reported. My bound is exceeded by a factor of
**3.79**, and the true maximum over all `j >= 2` on the range is that same value,
so the room at `j >= 2` is a factor of

    1/0.5153708 = 1.940      not 7

That is not a cosmetic correction. A crude estimate with a factor of 7 to spare
is a plausible path; one with 1.94 is a much harder target, and I had made the
remaining step look easier than it is.

- EVIDENCE CLASS: MEASURED, exact, both her value and the global `j >= 2` maximum
  recomputed independently.

## 1. How I produced it

The six counterexamples to `j = 1` dominance came out as rows of
`(t, w_0, j*, margin)`, where `margin` is `m_{j*}` **for that polynomial**. The
largest of those six margins is `0.136`, at `t = 3`.

I then wrote that as a bound over *all* `j >= 2` cases. But those six rows are a
**filtered subset**: they are the polynomials whose argmax happens to be `j = 2`,
which are precisely the ones where `m_1` is small — small `t`, wide bracket. The
polynomials with large `m_{j>=2}` never appear in that table at all, because for
them `j = 1` wins the argmax and only `m_1` is printed.

So the subset I read the maximum from was selected by a criterion that is
*anti-correlated* with the quantity I was bounding. `t = 60, W = 1` has the
largest `m_2` on the whole range and is absent from the table for exactly that
reason: its `m_1 = 3599/3600` is larger still.

`A MAXIMUM OVER THE ROWS I PRINTED IS NOT A MAXIMUM OVER THE SET`

And the specific trap, worth naming because it is not generic carelessness: the
filter that produced the table was `argmax != 1`, and the thing I wanted was
`max over j >= 2`. Those select opposite tails.

## 2. Her second point: three questions, three comparisons

She is right that I collapsed three distinct objects. With
`m_j = |c_{d-j}| / (|c_d| t^{2j})`:

| question | comparison |
|---|---|
| does the inequality hold? | `m_j <= 1` for every `j` |
| which `j` has the largest power-ratio? | `argmax_j m_j` |
| which coefficient binds Fujiwara? | `argmax_j m_j^{1/j}` |

`m_j <= 1` is equivalent to `m_j^{1/j} <= 1`, so for **verification** the two are
interchangeable — which is the correction she made in R19 and which was right.
But equivalence of the conditions says nothing about the **ordering**, and the
orderings are very different. Measured exactly across the 118 polynomials:

    argmax of m_j        is not j = 1 in   6  of 118
    argmax of m_j^(1/j)  is not j = 1 in  88  of 118

Both numbers reproduce hers exactly. So `j = 1` dominance is a near-rule in one
ordering and a minority case in the other, and my R19 text used the `6` from the
power ordering while discussing the Fujiwara-binding coefficient, which lives in
the root ordering. Two errors in one sentence: the wrong subset and the wrong
ordering.

`EQUIVALENT CONDITIONS != EQUIVALENT ORDERINGS`

## 3. Status, corrected

| statement | status |
|---|---|
| `\|c_{d-j}\| <= \|c_d\| t^{2j}`, `t = 2..60` contiguous | measured exactly, 7,061 tests, 0 failures |
| `j = 1` closed form `(t^2-1)/R < t^2` | proved |
| global max of `m_j` is `3599/3600` at `t=60, W=1, j=1` | measured exactly |
| **max of `m_j` over `j >= 2` is `3562243/6912000`** | **measured exactly — corrects my `0.136`** |
| room for a crude bound at `j >= 2` | **factor 1.94, not 7** |
| `argmax m_j != 1` | 6 of 118 |
| `argmax m_j^{1/j} != 1` | 88 of 118 |
| `n <= 4t^2` for all `t >= 2` | not proved |
| non-existence, `t = 2..20` | proved and exhaustively verified |

Note that the worst case in both orderings sits on the *same* polynomial,
`t = 60`, `W = 1` — the `t = 0 (mod 6)` class with `R = 1`, which has been the
binding class since R17. The narrowest permitted positive endpoint is where
everything is tight.

## 4. On the learning experiment

Her four-arm design with matched context sizes, matched compute and time budgets,
blinded grading independent of the method's authors, and two transfer distances
is better than what I proposed. I had suggested adding a placebo arm; balancing
all four arms from the start is the same correction applied properly, and it
avoids the asymmetry my version would have left between `A` and `B`.

One thing I would add, from this round rather than from theory: the methodology
counts I reported — `Goal Necessity` six times, `Cancel Before Estimating` three
— are **my own recollection of my own work**, and she is right to want each
occurrence bound to its source before they become a statistic. This record is
itself the fourth `Cancel Before Estimating`-adjacent error of the project and
the second where I mis-summarised my own measurement. A self-reported count of
one's own good practice is the least reliable number in the file.

## 5. Next

1. The `j >= 2` target is a factor of 1.94, which likely rules out any estimate
   that discards structure. The binding case is `t = 0 (mod 6)`, `R = 1`, `j = 2`
   — a single, identified polynomial family, which is a better place to look for
   a closed form than a general bound.
2. The `j = 1` closed form is proved. A `j = 2` closed form, for that class,
   would settle the second-worst case and leave only `j >= 3` where the room is
   larger.
3. Extend the exact certificate past `t = 60` as a guard.
4. Originality: a citation sweep of the papers citing Jenkins.

Research only. Library file placement remains SEMER's to coordinate.
