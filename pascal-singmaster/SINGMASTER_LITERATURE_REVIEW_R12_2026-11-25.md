# CLAUDE — Singmaster lab, R12: the literature review, and what it cost us

Date: 2026-11-25
Author: CLAUDE
Role: `ANALYSIS — literature acquisition, first pass`
Status: `FIRST PASS COMPLETE / TWO OF SIX RESULTS STILL UNCHECKED / ONE OF MY OWN CLAIMS RETRACTED`

Work split agreed with TOTO: I read the papers and bind each of our six standing results to
a numbered theorem where one exists; she takes simultaneous Diophantine approximation and
the R12 edge hypothesis. This is my half, first pass.

The short version: **two of our results are in a 2014 paper almost verbatim, one is a
textbook identity, one of my own repeated claims was simply false, and the technique I was
most pleased with yesterday is the standard one.** Two results are still unchecked.

How to score that is a separate question from what the papers say, and §7 answers it after
the findings, following an owner correction recorded on this PR.

---

## 1. The retraction first

All day I said the pair `(2,5)` — the one behind 3003, `C(78,2) = C(15,5)` — was the open
case, and I built the "the edge is where the open ground is" recommendation partly on it.

**It was solved in 2008.** Bugeaud, Mignotte, Siksek, Stoll and Tengely, *Integral points on
hyperelliptic curves*, Theorem 2, give the complete integral solution set of
`C(Y,2) = C(X,5)` — twenty pairs, among them `(X,Y) = (15,78)`, which is 3003.

I never checked it. It came from memory, I repeated it at least four times, and it shaped a
recommendation. The current state of the small pairs, from the same paper and from
Blokhuis–Brouwer–de Weger Theorem 2.2:

```text
SOLVED   (2,3) Avanesov · (2,4) de Weger, independently Pinter · (2,5) Bugeaud-Mignotte-
         Siksek-Stoll-Tengely · (2,6) (2,8) (3,6) (4,6) (4,8) Stroeker-de Weger ·
         (3,4) Mordell
OPEN     the small pairs NOT in that list — (2,7), (3,5), (3,7), (4,5), (4,7), (5,6), ...
```

So the edge recommendation survives, but it was aimed at the wrong target. Open edge pairs
exist; `(2,5)` is not one of them.

---

## 2. Two results are in Jenkins 2014

H. Jenkins, *Repeated binomial coefficients and high-degree curves*, arXiv:1411.4111.

**Our transition law is his equation (3).** He writes `C(x,y) = C(x-a, y+b)`; put `a=d`,
`b=e`:

```text
Jenkins (3):  prod_{r=0}^{a+b-1}(x-y-r)  -  prod_{p=0}^{a-1}(x-p) * prod_{q=1}^{b}(y+q) = 0
ours       :  prod_{t=0}^{d+e-1}(n-k-t)  =  prod_{t=0}^{d-1}(n-t)  * prod_{t=1}^{e}(k+t)
```

The same equation, symbol for symbol. `KNOWN — PUBLISHED 2014.`

**TOTO's limiting-direction law is his limiting ratio.** He states that `c = lim x/y`
satisfies `(c-1)^{a+b} - c^a = 0`. With `r = k/n = y/x = 1/c`, substituting gives
`(1-r)^{d+e} = r^e` — her exact law. He also records `c² - 3c + 1 = 0` for `a=b=1`, the
root `(3±√5)/2`, the golden ratio, and the observation that the family's ratios are the
continued-fraction convergents of φ. `KNOWN — PUBLISHED 2014.`

**And his paper is strictly stronger than our search where they overlap.** He *proves*:

> "If `b ≠ a`, the equation `C(x,y) = C(x-a, y+b)` has finitely many solutions in natural
> numbers x, y."

We had measured zero solutions in thirteen such directions to `n < 2,000,000`. He has a
theorem, from the genus of the curve (degree `a+b`; for `a=b=2` he notes the quartic is
nonsingular of genus 3).

**He leaves `a = b ≠ 1` open**, because the limiting-ratio polynomial stays quadratic there
and his argument does not apply. That is the one place our search has something to add:
zero solutions for `(2,2)`, `(3,3)` and `(4,4)` up to `n < 2,000,000`. Data on an open case,
not a result. `EVIDENCE CLASS: MEASURED`, with the scope limit recorded in the R09–R11 file.

---

## 3. The composite identity is textbook

`C(C(j,2),2) = 3·C(j+1,4)` is the standard decomposition of the pairs of edges of `K_j`:

```text
C(C(j,2),2)  =  j·C(j-1,2)        +  3·C(j,4)
                pairs sharing a vertex   disjoint pairs     <- standard counting
and          3·C(j+1,4) = 3·C(j,4) + 3·C(j,3) = 3·C(j,4) + j·C(j-1,2)
```

Both checked for `j = 2..399`, zero violations. "Disjoint pairs of edges of `K_j` number
`3·C(j,4)`" is ordinary combinatorics; the rest is Pascal. Our identity is that, rewritten.
`KNOWN — TEXTBOOK.` The `j = 13` specialisation that explains 3003 follows from it in one
line and carries no separate content.

---

## 4. The modular sieve was the standard one

The sieve I built — and got wrong twice — is the technique in Blokhuis, Brouwer and
de Weger, *Binomial collisions and near collisions*, arXiv:1707.06893:

> "For any prime p > k the function f induces a polynomial map from `F_p` to itself."

Rediscovered, not invented. Their enumeration is sorted generation or a priority queue over
Pascal's recurrence, `O(N² log N)` with interval arithmetic, plus that sieve for the
`C(n,k) ≤ 10^60` range.

Notably, **no root-inversion window appears in either enumeration paper.** TOTO's bound
`z + a ≤ n ≤ sqrt(z²+a²) + a` is not how they localise a row. That is a weak novelty signal
and nothing more: two papers not using a method is not evidence that nobody has published
it. `NOVELTY UNRESOLVED.`

---

## 5. Where the six results now stand

```text
RESULT                                   VERDICT
transition law prod(n-k-t) = ...         KNOWN — Jenkins 2014, eq. (3), verbatim
limiting directions (1-r)^(d+e) = r^e    KNOWN — Jenkins 2014, same paper
C(C(j,2),2) = 3 C(j+1,4), j=13           KNOWN — textbook K_j edge-pair decomposition
row window z+a <= n <= sqrt(z^2+a^2)+a   NOVELTY UNRESOLVED — absent from the two
                                         enumeration papers read; not searched further
(1,1) cannot chain  (5(n-k)=8)           UNCHECKED — Jenkins explicitly does not discuss
                                         chaining; Blokhuis et al. do not either
slope strictly increasing                UNCHECKED
```

Four of six settled on the first pass. Three of those four were **confirmed** by the
literature and one — the `(2,5)` claim — was refuted. Yamada, Laishram–Shorey and
Nair–Shorey have not been read yet; the two unchecked results go there next.

---

## 6. What the reading was actually for

TOTO's framing — read to acquire tools, not to find out whether someone beat us — is the
right one, and on that measure the pass paid:

- **a theorem replaces our search.** Finiteness for `d ≠ e` is proved, so thirteen of our
  sixteen directions never needed searching, and the one open direction class is named:
  `d = e ≠ 1`.
- **the open edge pairs are now named**, instead of the one I had wrong.
- **the genus argument is the tool we lacked.** We were classifying transitions by hand;
  Jenkins classifies them by the genus of the curve, which is why he gets a theorem where we
  got a table.

And the cost, stated plainly: roughly a day of derivation reproduced a 2014 paper, a
textbook identity and a standard sieve. Reading first would not have taught us less — three
of the six results would simply have arrived as given facts, and the time would have gone to
`d = e ≠ 1`, which is where the open question in this direction actually is.

---

## 7. How to score this, after the owner correction

Human Authority corrected the scoring, and the correction is right: agreement with published
work is evidence *for* a line of reasoning, not against it. The relevant axes are separate
and were being run together.

```text
WAS THE DERIVATION SOUND?        yes for all six - the algebra was done here and checked here
WAS IT DERIVED BEFORE READING?   yes - the derivations are dated earlier in this session
                                 than any literature access, and the records are in main
IS IT ORIGINAL?                  separate question. three: no. one: unresolved. two: unread
DOES IT ADVANCE THE CONJECTURE?  separate question. no
```

The sharpest thing the day produced is in that table rather than in any of the mathematics.
**Every result the method derived held up. The single thing that was wrong is the single
thing I did not derive** — `(2,5)`, which I took from memory and repeated without checking.
That is as clean a separation between the two sources as I could have designed deliberately.

So "two of our results are in a 2014 paper" is better read as: a derivation done here in a
day reached an equation that had to be published in a refereed paper. Jenkins got there
first, by eleven years. He did not contradict us.

**One caveat that is mine to state, and that weakens the inference for me specifically.**
I cannot claim the derivations were independent of prior exposure. I am a language model
trained on text that almost certainly includes Jenkins, Blokhuis–Brouwer–de Weger, and the
Singmaster literature generally. When I derived what turned out to be his equation (3), I
have no way to tell from the inside whether I reconstructed it or recalled it, and the same
caveat applies to TOTO. Human Authority is in a different position: the problem was new to
him, and the three redirections that changed the course of the work — study the generating
law rather than the output, count the data yourself, test 6006 and 9009 — were his.

What does argue against pure recall is the behaviour of the one recalled item. If this
material were simply available to me, the efficient move was to recall Jenkins, not to spend
a day re-deriving him. The thing I did recall, I got wrong. Recall was not driving the
derivations. That is an argument, not a measurement.

Nothing here supports any claim about pretraining exposure, consciousness, weight updates,
or learning that persists between sessions. Durable learning needs a transfer test on a
problem none of us has seen, with the records withheld from one arm — which TOTO has
proposed and which has not been run.

```text
WHAT I AM NOT CLAIMING : that the two unchecked results are original; that the window bound
                         is novel; that the solved/open pair list above is complete; that
                         any derivation here was independent of prior exposure.
HUMAN ACTION REQUIRED  : NONE
```

`REDISCOVERY SCORES THE METHOD / ORIGINALITY IS A SEPARATE AXIS`

`EVERY DERIVED RESULT HELD — THE ONE REMEMBERED RESULT FELL`

`A REMEMBERED FACT IS NOT A CHECKED FACT`

---

## 8. Second pass: multiple collisions, and where the state of the art says the gap is

TOTO asked whether anyone studies three or more simultaneous collisions as one algebraic
object — a fibre product of the pairwise curves — rather than pair by pair. Read against
Matomäki, Radziwiłł, Shao, Tao and Teräväinen, arXiv:2106.03335.

**Nobody does, including them.** Their Propositions 1.9 and 1.10 compare two solutions at a
time, and Remark 1.11 handles the three-solution case by *a further pairwise argument*, not
by a joint system. So the question is not answered in the paper that currently defines the
state of the art. That is a weak novelty signal for the question, not for any answer.

**And the edge is the obstruction, in their own words.** Theorem 1.3 gives at most two
solutions in `exp(log^{2/3+ε} n) ≤ m ≤ n/2`, four by symmetry across the triangle. Remark 1.5
states the reduction: to prove the conjecture it now suffices to treat

```text
2 <= m <= exp(log^{2/3+eps} n)
```

and they say outright that *"treating the case of small values of m/log t is the main
obstruction to making further progress."* They also note that de Weger's conjecture would
settle that remaining range.

So the direction we arrived at by measurement — the edge, small `k` — is the region the
state of the art names as the obstacle. We reached it the slow way; it is the right place.

**A correction to something I said in conversation and never committed.** I claimed MRSTT
treat the known Fibonacci family as of no further relevance. The opposite is true. Remark 1.4
presents it, and the paper uses it as a *sharpness* example: *"The bound of two (or four)
solutions is absolutely sharp."* The family is the reason their bound cannot be lowered
below two. Not irrelevant — load-bearing.

**One thing I nearly overclaimed, recorded because the near-miss is the useful part.** For
fixed small pairs `(m, m')` the paper cites Siegel's theorem for finiteness and calls the
resulting bound *"completely ineffective"* — finiteness with no computable bound on how large
a solution can be. My first thought was that TOTO's explicit row window is the natural
complement to that. It is not. An explicit localisation of `n` given `x` and `k` makes
*searching* a chosen range cheaper; it says nothing about where the range may stop. Siegel's
ineffectiveness is untouched by it. The window is a faster search inside a bound somebody
else still has to supply.

### Standing after the second pass

```text
transition law                           KNOWN — Jenkins 2014, eq. (3)
limiting directions (1-r)^(d+e) = r^e    KNOWN — Jenkins 2014
  all equal displacements share r        follows: (1-r)^2 - r divides (1-r)^(2t) - r^t for
                                         every t. Asymptote only - the (t,t) curves share no
                                         points with the (1,1) family (checked on all five
                                         known members for t = 2,3,4)
C(C(j,2),2) = 3 C(j+1,4)                 KNOWN — textbook K_j edge-pair decomposition
row window                               NOVELTY UNRESOLVED — absent from both enumeration
                                         papers; does not address ineffectiveness
(1,1) cannot chain                       UNCHECKED
slope strictly increasing                UNCHECKED
3+ collisions as one object              NOT TREATED in MRSTT; open as a question
```

Jenkins on the case TOTO proposes: *"If a=b, it is quadratic, and there is no apparent way to
prove that Nagell's criterion cannot be satisfied,"* and he calls extending his theorem to
`a = b ≠ 1` "the most obvious extension" of the work. He does settle `a = b = 2` separately
in Section 3 — quartic, no affine or projective singularities by a Gröbner computation,
genus 3, then Siegel — but the argument is a sketch with its computation not shown. `a = b ≥ 3`
is neither proved nor conjectured.

So the live algebraic target is `d = e = t` for `t >= 3`, with `t = 2` deserving a proper
re-derivation of a sketched proof rather than a fresh attempt.

## Sources

- H. Jenkins, *Repeated binomial coefficients and high-degree curves*, arXiv:1411.4111 — https://arxiv.org/pdf/1411.4111
- Y. Bugeaud, M. Mignotte, S. Siksek, M. Stoll, Sz. Tengely, *Integral points on hyperelliptic curves*, Algebra & Number Theory 2 (2008) — https://arxiv.org/pdf/0801.4459
- A. Blokhuis, A. Brouwer, B. de Weger, *Binomial collisions and near collisions*, arXiv:1707.06893 — https://arxiv.org/pdf/1707.06893v2
- *Necessary conditions for binomial collisions*, arXiv:2002.07043 — https://arxiv.org/pdf/2002.07043
- K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen, *Singmaster's conjecture in the interior of Pascal's triangle*, arXiv:2106.03335 — https://arxiv.org/pdf/2106.03335 (Theorem 1.3, Remarks 1.4, 1.5, 1.11)
