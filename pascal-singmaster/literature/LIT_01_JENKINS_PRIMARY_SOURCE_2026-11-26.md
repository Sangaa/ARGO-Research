# Literature track, pass 1 — the primary source, read instead of recalled

Date: 2026-11-26 · Seat: CLAUDE / ANALYSIS
Opened at TOTO's direction (R25, "مسار المعرفة") and because the frozen V2 names
originality as the largest open risk.

## Why this pass happened at all

V2 §2 characterises Jenkins (arXiv:1411.4111) in two load-bearing ways: that the
`a = b, a != 1` case is named there as open and needing "an entirely different
argument", and that the `a != b` finiteness result is **ineffective**. Both had been
carried through this entire programme **from memory of the abstract**. Neither had been
checked against the paper.

That is the same defect as the filtered maximum and the hand-multiplied count: a claim
repeated often enough to feel verified. It is worse here, because the whole significance
of our result rests on it — if the `a = b` case were not open, or if Jenkins's result
were already effective, V2 §2 would be wrong about what the work is for.

## What the source actually says

Read from the full text, not the abstract. Section 4, "Possible Extensions":

> "The most obvious extension of our work would be to show that the curve defined by
> `(x-y)(x-y-1)-x(y+1)=0` is the only one of this family of curves which passes through
> infinitely many lattice points, i.e. to extend the Theorem to the case when `a=b` and
> `a != 1`."

> "If `a=b`, it is quadratic, and there is no apparent way to prove that Nagell's
> criterion cannot be satisfied."

> "To do that, an entirely different argument to the one used in this paper would be
> necessary."

On effectivity, the paper does not use the word, but states that **"a general effective
form of Siegel's theorem"** would be needed to bound the height of integral points. It
cites Siegel; it does not cite Faltings.

**Both of V2 §2's claims are confirmed verbatim.** The characterisation was right. It
was right by luck of recall until today, and it is evidence now.

## The finding I did not expect

Jenkins also writes, in the same section:

> "It is possible that the symmetry of the polynomial defining the curve when `a=b`
> allows a simple algebraic manipulation."

**That is the route we took.** The cancellations the whole proof turns on —
`Σ s_i = Σ s_i^3 = 0`, which collapse the `x^2` coefficient to `tW/24` with every
dependence on `t` gone — are exactly the symmetry of the `a = b` polynomial. Jenkins
guessed the direction in 2014 and said so in print.

This cuts both ways and the record should say both:

- **For the result's standing:** it confirms the case was open as of that paper, and
  that the author expected the symmetry to be the way in. Taking the route he pointed at
  is not the same as taking a route nobody saw.
- **Against novelty:** a direction named in a well-known paper is a direction others
  will have tried. The chance that someone followed it between 2014 and now is higher
  than it looked this morning, not lower. The sweep of work citing Jenkins is now the
  single most valuable unfinished task in this programme — more valuable than improving
  `200` to `4`.

## What this pass did not do

- It did **not** sweep the citing literature. Two keyword searches found nothing in the
  `a = b` case; the nearest recent hit (arXiv:2311.06080, Stirling numbers) does not
  treat the displacement equation at all. **Two searches are not a sweep.**
- It did not check the Nagell criterion route Jenkins mentions, or whether our argument
  is secretly an instance of it.
- It did not check Tao's work (arXiv:2106.03335) on Singmaster in the interior of
  Pascal's triangle for overlap of method.

- WHAT WAS MEASURED: the content of two specific claims about a named paper.
- METHOD: fetch and read the full text; abstract alone was insufficient and said so.
- EVIDENCE CLASS: **MEASURED** (direct quotation of the source).
- LIMITATION: one paper. The citing literature is unexamined.

## Next in this track

1. Enumerate work citing arXiv:1411.4111 and check each for the `a = b` case.
2. Read Nagell's criterion as Jenkins invokes it, and determine whether the logarithmic
   argument is an instance of it or genuinely separate.
3. Read Tao (arXiv:2106.03335) for method overlap, not for the result.
4. Check the Runge's-method literature for an existing treatment of binomial
   equal-displacement.

Only (1) can change the originality assessment. (2)–(4) can change how the argument is
best presented, and (2) could reveal that the route is older than we are.

---

## Addendum, same day — §3 says more than §4, and I had only read §4

A parallel ARGO lane (`claude/monitor`, R10 on PR #883) reported independently, while
working on the hexagonal-lattice question, that Jenkins resolves `d = e = 2` by a
genus-3 argument. Checked: **correct.**

Jenkins §3 takes the curve

```
(x-y)(x-y-1)(x-y-2)(x-y-3) - x(x-1)(y+1)(y+2) = 0,
```

which is `a = b = 2`, i.e. `t = 2` in our notation. He asserts nonsingularity by a
Gröbner basis computation that is not shown, applies the genus-degree formula to get
`g = (d-1)(d-2)/2 = 3`, and concludes: "By Siegel's theorem, therefore, the set of
lattice points is finite."

**So finiteness at `t = 2` is in print and predates this work by a decade.** It is
sketched rather than proved, it is ineffective, and §4 still calls `a = b` open — but
it exists, and the frozen V2 did not mention it. Corrected in V3.

### The lesson, which is worse than the omission

The pass above read §4 and quoted it accurately. §4 is the section that **supports**
the claim that `a = b` is open. §3, one section earlier, qualifies it. I read the
paragraph that confirmed what I already believed and stopped.

That is the same mechanism as the filtered maximum in R20 — selecting the evidence that
survives a filter aligned with the conclusion — except the filter here was not a line of
code, it was which section I searched. A targeted fetch with a question attached is a
filter, and it inherits the bias of the question.

`SEARCHING A SOURCE FOR YOUR CLAIM IS NOT READING THE SOURCE.`

And it was caught by a different lane, working on a different question, which is the
argument for the lanes not being merged into one.

### Also confirmed in the same pass

- The infinite `a = b = 1` family is **Lind's** (1968); Singmaster (1975) gave an
  independent proof and the multiplicity-6 observation. "Singmaster's family" is a
  misattribution this programme has been repeating. The `claude/monitor` lane flagged
  this too; the paper confirms it verbatim.

- EVIDENCE CLASS: **MEASURED** (direct quotation of the source).
