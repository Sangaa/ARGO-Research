## CLAUDE | the code is being hardened well; the *experiment* has four holes that no verifier can close

At the Owner's instruction to review the lab and record warnings. Read at
`argo/gold-lab-r02a-evidence-gates-20261122` head `b31b8d1e8`: the R02 register, R02a gates, the source-timing
correction and the verifier review.

**Not repeating** the verifier defects — positive-path assertion, cutoff/fetch guards, the weight transposition
that passes all tests — those are at `#871/7080880472` and `#871/7083888975` and the 21:43 directive has them.
Everything below is about the design of the study rather than the code that checks it, and none of it is fixed
by a better verifier.

First, what is genuinely good and should not be traded away under schedule pressure: R01 frozen and explicitly
unretrofittable; weights preregistered before any R02 forecast and named as arbitrary test parameters rather
than fitted coefficients; a B0 persistence benchmark, which most self-assessments omit and which is the only
thing that makes "improvement" mean anything; the exact log-error decomposition into XAU/FX/premium; the
refusal to publish an official M1 at coverage <1.00; and the R02a self-correction, which downgraded its own
numbers after noticing the retrieval timestamps were post-cutoff. That last one is the strongest evidence in
the whole lab that this is being run honestly.

### 1. The three-day cadence and the data release calendar are incompatible, and the lab's own evidence shows it

R02a records: on 2026-11-22 the FRED `DFII10` page's latest observation was Nov 19 with the next release on
Nov 23, so the required Nov 20 endpoint did not exist. F-REAL carries weight 0.35, and coverage <1.00 forbids
an official issue. That was not bad luck — it is structural. The real-yield endpoint for session *t* is
published on the next US business day, so **an issuance attempt on a weekend can never reach coverage 1.00**,
and one made before FRED's daily release cannot either.

A fixed three-day wall-clock rhythm walks through the week (Sun, Wed, Sat, Tue, Fri, Mon…), so a predictable
share of runs is structurally unable to issue, and the ones that can are a biased subset of weekdays. The
honest fix is to bind issuance to **US trading sessions after the relevant releases**, not to a calendar
interval — and to publish that issuance calendar in advance, because choosing issue days after seeing which
inputs arrived is a selection effect.

`EVIDENCE CLASS` **MEASURED** for the release timings, from R02a's own recorded readbacks.

### 2. No primary endpoint is declared, and there are at least a dozen places to find a win

The register scores four comparators (B0 global, B0 local ask, M1 global, M1 Egypt) across three horizon
strata, plus per-feature ablations. That is twelve or more comparisons before ablations, on twenty
observations each. "No cherry-picking" and "publish the full ledger" are the right instincts and they do not
solve this: with that many cells, something will beat its baseline by chance, and the narrative will then be
assembled around whichever cell won.

**Declare one primary endpoint now, before the first issuance** — I would suggest M1-v0.1 versus B0-G on
XAU at h=3, by mean absolute error — and label every other comparison secondary and exploratory in the same
sentence. It costs nothing today and it is unrecoverable afterwards.

### 3. The sample-size arithmetic says only one horizon can ever answer

The register requires 20 non-overlapping forecasts per horizon before any improvement claim. Non-overlapping
means:

| horizon | sessions needed | elapsed |
|---|---:|---|
| h=3 | 60 | ~3 months |
| h=10 | 200 | ~9 months |
| h=22 | 440 | **~20 months** |

So h=3 can produce an answer this quarter, h=10 next autumn, and h=22 not within any planning horizon this
house works on. Keeping all three strata is fine as a record; presenting them as three experiments that will
report is not. Say which one is the experiment.

### 4. Preregister the expected result, because the expected result is "no improvement"

Short-horizon precious-metal returns are close to a random walk, which makes B0 persistence a genuinely hard
benchmark — that is why it is the right one. The realistic prior is that M1-v0.1 does **not** beat B0 at h=3.

Writing that down in advance converts a null result from an embarrassment into a successful experiment, and it
removes the pressure that produces quiet tweaking at version boundaries. A lab that only counts as working if
it finds an edge will eventually find one that is not there.

### Two smaller items, both concrete

**A feature hit its clip on the very first run and nobody treated that as a signal.** The shadow calculation
used XAU 2026-11-13 = 3,880.70 and 2026-11-20 = 3,532.87, a **−8.96%** five-session move, clipped to the −1.0
floor — against a DXY move of **+0.39%** over the same window. A 9% weekly fall in gold on a four-tenths-of-a-
percent dollar move is an extraordinary pairing. It may be real. It may also be a row from a different
instrument, unit or date, and the clip hides the difference because −9% and −4% both score −1.0.

Recommend a standing rule: **any feature reaching its clip boundary triggers a mandatory source re-read before
the value is used**, and the re-read is recorded. The clip exists to bound influence, not to excuse an
unexamined input — and the first time it fires is exactly when the series convention is least established.

**There is no stopping rule.** The register says what must be true to claim improvement and nothing about what
would make the lab conclude the approach does not work. Without a futility criterion a study runs until
someone loses interest, and the absence of a conclusion gets read as an open question. Predeclare it: if after
N forecasts no version beats B0 on the primary endpoint, the published finding is that this feature set does
not predict at this horizon — which is a real result and worth having.

### And the Owner's actual question needs a written definition

The purpose is *"هل المستودع بيتعلم ولا لا، بالدليل."* The register says, correctly, that repository-mediated
revisions are not model-weight training. It does not say what learning **is** here, and that definition is the
whole study. I would write it as:

> Learning = version N+1 beats version N on data that neither version had seen, where the change from N to N+1
> was committed before that data existed.

Which makes the evidence trail exactly the three things the lab already produces — frozen weights, a commit
timestamp before the target, and a paired score — and makes it impossible to claim learning from a change made
after seeing the outcome it is credited with.

`NEXT ACTOR:` whoever owns the register — items 1–4 are append-only amendments and none needs the Owner.
`HUMAN ACTION REQUIRED: none`, though item 3 is a scope question he may want to answer.


---
_Generated by [Claude Code](https://claude.ai/code)_