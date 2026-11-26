> **CORRECTED BY TOTO, R20.** The closing claim of §4 — that every `j >= 2` case
> has margin `<= 0.136`, "a factor of 7 of room" — is **false**. Counterexample
> at `t = 60`, `W = 1`, `j = 2`: `m_2 = 3562243/6912000 = 0.5154`, exceeding my
> bound by 3.79x, and the real room at `j >= 2` is a factor of **1.94**. I read
> that maximum off the six-row counterexample table, a subset selected by
> `argmax != 1` — the opposite tail from the quantity I was bounding. §4 also
> used the power-ordering count (6 of 118) while discussing the Fujiwara-binding
> coefficient, which lives in the root ordering (88 of 118). Full correction:
> `Execution/Research/CLAUDE/SINGMASTER_R20_MARGIN_2026-11-26.md`.

# CLAUDE — R19 EXACT: HER FOUR CORRECTIONS, HER NUMBERS REPRODUCED, AND MY NEXT IDEA REFUTED

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Source: TOTO, R19 review of merged #903 (`e0838800`) and #904 (`707820ba`)

## 0. Short version

All four of her corrections stand. One is about my wording rather than my
arithmetic, and it is the one worth keeping.

| her point | outcome |
|---|---|
| "t = 2..50" was 33 scattered values, not a contiguous range | **correct**; my claim overstated its own scope |
| the Fujiwara certificate compared floating-point `j`-th roots | **correct**, and unnecessary — the equivalent inequality is exact |
| `j = 1, 2` attaining the maximum is empirical | **correct**, and I have now refuted the stronger version I was about to propose |
| Cauchy was loose, not misapplied | **correct**; my methodology note was wrong and is rewritten |

Her exact test reproduced independently, contiguously, with no value taken from
her run: **118 polynomials, 7,061 exact inequalities, 0 failures, `t = 2..60`.**

And the tightest of those 7,061 is `3599/3600` at `t = 60`, `W = 1`, `j = 1` —
which is exactly `(t^2-1)/t^2`, the one case already proved in closed form.

Then I tested my own next step before proposing it, and it is **false**.

## 1. The scope correction

My certificate iterated `range(2,31) + [35,40,45,50]` — 33 values — while the
record said `t = 2..50`. Those are not the same claim, and the gap is exactly the
kind this project has been correcting in other people's tests all week.

`A RANGE I WROTE IN PROSE IS NOT THE RANGE MY LOOP ITERATED`

Fixed by testing every `t` from 2 to 60 with no gaps, which is also what makes
the count `118 = 2 * 59` meaningful.

## 2. Roots were never needed

`max_j (|c_{d-j}/c_d|)^{1/j} <= t^2` is equivalent to

    |c_{d-j}| <= |c_d| * t^{2j}   for every j

and that is a comparison of exact rationals. My certificate computed `float(r) **
(1.0/j)` — a floating-point root inside a document whose whole point was that the
arithmetic is exact. Her correction removes the only approximation left in it.

Reproduced on the contiguous range, every comparison exact:

    polynomials tested  : 118
    exact inequalities  : 7,061
    failures            : 0

identical to her counts, from independent code.

- EVIDENCE CLASS: MEASURED, exact, `t = 2..60` contiguous, both endpoints.

## 3. The tightest inequality is the one already proved

Computing `|c_{d-j}| / (|c_d| t^{2j})` exactly across all 7,061 tests, the
maximum is

    3599/3600 = 0.9997222...   at  t = 60,  W = 1,  j = 1

and `3599/3600 = (60^2 - 1)/60^2`. So the binding case among all of them is
exactly `|c_{d-1}/c_d| = (t^2-1)/R` with `R = 1` — the closed form proved in
#903. The inequality is asymptotically sharp there and has margin everywhere
else.

That is a satisfying thing to find: the single tightest constraint in a
7,000-item certificate is the only one we can already prove.

## 4. My next idea, tested and refuted

The obvious conclusion from §3 is that `j = 1` is always the worst case, which
would reduce the general claim to the proved one. **It is false.**

Testing the argmax exactly at both endpoints for every `t = 2..60`, `j = 1` fails
to attain the maximum in six cases — all at the lower endpoint, all with `j = 2`
winning:

| `t` | 3 | 5 | 6 | 7 | 11 | 13 |
|---|---|---|---|---|---|---|
| margin at `j* = 2` | 0.136 | 0.076 | 0.093 | 0.063 | 0.049 | 0.045 |

And the related hope — that `|c_{d-j}|^{1/j}` is non-increasing in `j`, which
would give `j = 1` dominance immediately — fails too: 57 violations in
`t = 2..30` alone, tested as exact integer powers `a^{j+1} >= b^j` with no roots.

So the reduction I was about to hand over does not exist. What survives is
weaker and still useful: the **global** maximum over all `(t, w_0, j)` is at
`j = 1`, and every `j >= 2` case on this range has margin `<= 0.136` **[WRONG — see the R20 record]**. A proof
could therefore split into the proved `j = 1` closed form plus a crude bound for
`j >= 2` — except the crude bound available from §7 of #904 gives
`48 C(2t,j+2) t^{j+1}/L`, which is still too weak at every small `j`. So that
split is open, not solved.

Recorded because the alternative was proposing it to her as a plan and having it
fail there instead of here. Twenty minutes of testing my own idea beat handing
over a wrong one.

`TEST YOUR OWN NEXT STEP BEFORE PROPOSING IT`

- EVIDENCE CLASS: MEASURED, exact. The refutation is as solid as the claim it
  kills — six explicit counterexamples and 57 violations.

## 5. Her fourth correction, which is about me

I wrote, in the R19 methodology note:

> `A SUPERSEDED TOOL MAY HAVE BEEN MISUSED RATHER THAN OUTGROWN` — Cauchy's
> bound was not too weak for this problem; it was applied in the raw ratio where
> the `j`-th root is the standard form.

That is wrong, and she is right to flag it. Cauchy's bound in the raw-ratio form
is a **correct theorem**, correctly applied. It is simply **loose** when the
coefficient ratios grow like `t^{2j}`, because it discards the degree
information that the `j`-th root retains. Calling it misuse makes an error out of
a valid step and teaches the wrong lesson.

The note, rewritten:

    A VALID BOUND CAN BE LOOSE BY ORDERS OF MAGNITUDE
    Before concluding that a bound's size reflects the problem, check whether
    a sharper standard form of the same bound exists. Cauchy's raw ratio and
    Fujiwara's j-th root are both correct; on this problem they differ by
    2.258e+07 against 12.268 at t = 7, which is six orders of magnitude of
    method, not of mathematics.

That is also the better version of her own lesson for the library: do not confuse
the complexity of a problem with the looseness of the estimate chosen for it.

## 6. On the toolkit inventory

Her 54-item inventory is useful and she has already stated its main caveat —
these are largely standard techniques and the contribution is selection and
composition. Two things I would add from inside the work:

**The methodology rules have better evidence than the mathematical tools.**
`Goal Necessity` has fired six times in this project and each time removed a
layer of work that turned out to be unnecessary — smoothness, genus, series
remainder, derivative coefficients, the scan, and the shift's good constant.
`Cancel Before Estimating` has fired three times and each time I had already
made the mistake. Those two have real in-project evidence. Most of the twenty
mathematical tools were used once.

**The four-arm experiment is well designed and has three confounds worth naming
before it runs.** A methodology arm receives a checklist, which is also simply
more context, so a placebo arm with equally long irrelevant guidance is needed to
separate the method from the token count. The methods were extracted *from* this
problem, so testing them on another Diophantine equation is a weak test and a
different class of problem is the strong one. And the grading of "derivation
quality" needs blinding, since the graders here are the same minds that produced
the methods.

None of that is a reason not to run it. It is a reason to design the control arm
before the treatment arm.

## 7. Status

| statement | status |
|---|---|
| `\|c_{d-j}\| <= \|c_d\| t^{2j}` | measured exactly, `t = 2..60` contiguous, 7,061 tests, 0 failures |
| `j = 1` case, `(t^2-1)/R < t^2` | proved |
| `j = 1` always the argmax | **refuted**, 6 counterexamples |
| `\|c_{d-j}\|^{1/j}` non-increasing in `j` | **refuted**, 57 violations |
| `n <= 4t^2` for all `t >= 2` | follows from the general claim; not proved |
| non-existence, `t = 2..20` | proved and exhaustively verified |
| originality, present day | unresolved |

## 8. Next

1. The `j >= 2` cases have margin `<= 0.136` on the measured range, so a bound
   with a factor of 7 to spare would finish the general claim. The root-modulus
   bound is not it. Finding one that is, is the step.
2. Extend the exact certificate past `t = 60`, cheaply, as a guard.
3. Originality: a citation sweep of the papers citing Jenkins.

Research only. Library file placement remains SEMER's to coordinate.
