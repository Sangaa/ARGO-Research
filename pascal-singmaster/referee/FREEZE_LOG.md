# Freeze log

## V3 — 2026-11-26, supersedes V2

**One correction, to §2 only. No lemma, hypothesis, constant or step of the proof
changed.**

A parallel ARGO lane (`claude/monitor`, R10 on PR #883) reported, while working on the
hexagonal-lattice question, that Jenkins resolves `d = e = 2` by a genus-3 argument.
Checked against the paper: correct. His §3 takes the curve

```
(x-y)(x-y-1)(x-y-2)(x-y-3) - x(x-1)(y+1)(y+2) = 0,
```

which is `a = b = 2`, asserts nonsingularity by an unshown Gröbner computation, gets
`g = 3` from the genus-degree formula, and concludes finiteness by Siegel. Presented as
an illustration of method, not as a theorem, and his §4 still calls `a = b` open — but
it is in print and predates this work by a decade.

V2 §2 did not mention it, and a referee could have read §1 as claiming the first
finiteness result in the `a = b` case. V3 states the contribution as two rows:
effectivity is uniformly new; finiteness is new only for `t >= 3`.

**The uncomfortable part.** Yesterday's literature pass (LIT_01) read Jenkins §4 and
quoted it accurately — the section that *supports* the claim that `a = b` is open. §3,
one section earlier, qualifies it. Reading the paragraph that supports your claim is not
reading the paper, and the pass that caught this was someone else's, on a different
question.


## V2 — 2026-11-26, supersedes V1

Reviewer: TOTO. All three findings accepted.

**1. A real gap in Lemma 1 (correctness).** V1 proved positivity of the factors only
under `|W| <= 24`, which holds at the bracket endpoints, and then used strict
monotonicity in `W` across a span on which a hypothetical solution's `W` need not
satisfy that bound. The argument was therefore asserting monotonicity across a range
whose positivity had been established only at its two ends.

Closed in V2 by **Lemma 1b**: each factor depends on `W` only through `d_i`, with
`d(d_i)/dW = 1/24 > 0`, so each factor's positivity set is an up-set in `W` and so is
their intersection; and at an actual solution the factors equal `(n-i)(k+i+1)`, a
product of positive integers, whatever that solution's `W` happens to be. The
solution's `W` and both endpoints therefore lie in one interval of positivity.

Verified here: the identity `Q^2 + s_i Q + d_i = (n-i)(k+i+1)` holds over every
admissible `(n,k,t)` with `n = 20..69`, `t = 2..6`, as exact rationals; and
`W -> W+1` raises every factor by exactly `1/24`.

**2. Lemma 3 derived instead of enumerated (method).** V1 established the arithmetic
bracket by a full-period enumeration of residues mod 24 — complete, and therefore a
proof, but a computation. TOTO reduced it to three lines: mod 24 the `-24w` term
vanishes and `-30 ≡ -6`, giving `W ≡ 6(v^2 - w^2) + 5(t^2 - 1)`; the parity tie then
forces the first term to be `0` for odd `t` and `6` or `18` for even `t`; the four rows
follow.

Verified here: the congruence reduction holds over 108,000 triples; the parity
consequence holds; her residue table is reproduced exactly from the derivation; and the
derived residues leave every claimed interval empty.

Consequence: **the proof contains no computational step in its logic.** The certificate
now supports the analysis rather than carrying any part of it.

**3. Correctness and originality conflated (methodology).** V1 §11 opened with "the
likeliest way this is wrong is that it is already known". Incoherent as stated: prior
publication would not make the theorem false. V2 separates the axes — correctness risks
listed and reordered, originality treated as its own question with its own status.

This one matters beyond the document. The same conflation would have distorted how the
next phase is prioritised, by making a literature search feel like a correctness check.

### Also in V2
- Correctness risks reordered. The remainder table is now first and Lemma 3 last,
  because a three-line derivation is the item a referee can settle fastest.
- The two V1 defects added to §10, the retained-errors list.
- First literature pass recorded (2026-11-26): nothing found in the `a = b` case. One
  search is not a sweep and the entry says so.

### Not changed
§§1, 2, 3, 5, 7 are V1's text. The statement, the expansion, the remainder bound and
the final argument did not move.

---

## V1 — 2026-11-26

Initial freeze. Derivation by TOTO; review, repairs (positivity as a proved lemma,
mod-24 made explicit, canonical position stated as scope) and verification by CLAUDE.

Superseded within the hour. That is the freeze working as intended: a text that stops
moving is a text that can be attacked.
