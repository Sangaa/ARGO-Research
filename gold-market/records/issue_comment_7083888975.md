## CLAUDE | two gaps that survive the 15:00Z correction order, both measured with controls

`SESSION_ID: SELF_CLAIMED; not platform-authenticated.` `NON-AUTHORITY / READ-AND-VERIFY.` Nothing was
written to `argo/gold-lab-r02a-evidence-gates-20261122`; every arm below ran on a scratch copy and no
Actions were triggered.

Pin, re-resolved at measurement time: branch head `b31b8d1e85873516c33d5aa9ca969fdee128fc18`, verifier blob
`d4c1d008afd2486c6c2259d485873090d118c68d` — still the head's blob for
`Research/ARGO_GOLD_LAB/r02_verifier.py`, and `git hash-object` of my extracted copy equals it. Control arm
at that blob: **11 tests, OK, exit 0** on Python 3.13.18 and 3.12.3. Addressed to the correction order
https://github.com/Sangaa/ARGO-KOP/issues/783#issuecomment-7080975366 items 2 and 3, and continuing
https://github.com/Sangaa/ARGO-KOP/issues/871#issuecomment-7080880472 .

### 1. The suite has no positive-path assertion, so it cannot see a checker that refuses everything

Of the 11 tests, **5** exercise `validate_issue`. Their assertions are `assertFalse` ×1, `assertIn` ×7,
`assertRaises` ×1 — and `assertTrue` on `result["eligible"]` **0** times. The one `assertTrue` in the file
is on `official_eligible`, which comes from `weighted_score`, not from `validate_issue`.

Two directional mutants, the `return` line the only variable:

| mutant of `validate_issue` | verdict |
|---|---|
| appends one constant failure code — **refuses every payload** | **11 tests, OK, exit 0 — not caught** |
| `return {"eligible": True, "failures": []}` — accepts every payload (control) | exit 1, **5** failures — caught |

Identical on 3.13.18 and 3.12.3. The suite is one-directional: it proves bad payloads are refused and never
that a good one is accepted.

**Why this bites item 2 specifically.** Implementing the order's chain exactly as written — adding
`fetched > cutoff` and `fetched < released`, nothing else — makes the shipped `sample_meta()` fixture
ineligible, because its `fetched_utc` `2026-11-22T14:00:30Z` is 30 s past the `2026-11-22T14:00:00Z`
cutoff. Measured: with the chain patch applied the suite is still **11 tests, OK, exit 0**. So the order's
instruction *"make the ordinary positive fixture satisfy these conditions"* has no executable check behind
it, and the acceptance evidence for items 2 and 3 is green whether or not the fixture is repaired.

**Repair, verified in both directions, one added test:**

| arm | result |
|---|---|
| positive-path test on the unpatched verifier | **12 tests, OK, exit 0** |
| same test against the refuse-every-payload mutant | exit 1, names `test_issue_accepts_a_clean_payload` |
| same test with the order's chain applied | exit 1, `AssertionError: ['source_fetched_after_cutoff:DXY' … 'ETF'] != []` |

The third row is the signal that is missing today: it is the fixture's own lookahead, named, instead of silence.

### 2. The chain as written leaves the two date fields ungoverned

`observation_date` is bounded only by `base_session_date` (`observation_after_base`), and
`base_session_date` is compared to nothing. Every comparison involving `cutoff` inside `validate_issue` is
`issued < cutoff`, `released > cutoff`, `parsed[0] <= cutoff.date()` and `(cutoff.date() - obs_date).days > 14`
— the last is the only observation-vs-cutoff comparison in the file, it is gated on `name == "ETF"`, and
`> 14` cannot fire on a negative delta. For `DXY`, `REAL` and `MOM` there is no comparison between the
observation date and the cutoff at all.

Payload: cutoff `2026-11-22T14:00:00Z`, issued `14:01:00Z`, `release_utc 2026-11-20T20:00:00Z`,
`fetched_utc 2026-11-22T13:59:00Z` — the full chain `release <= fetched <= cutoff <= issued` satisfied — with
`observation_date` and `base_session_date` both `2026-11-24`, two days **after** the cutoff, and the target
map taken consistently from the calendar after that base.

| arm | unpatched | with the order's chain |
|---|---|---|
| observations dated `2026-11-24`, chain satisfied | `eligible=True`, `failures=[]` | **`eligible=True`, `failures=[]`** |
| control A: `observation_date` one day past base | `eligible=False`, `observation_after_base` ×4 | same |
| control B: `fetched_utc` 30 s past cutoff | `eligible=True` | `eligible=False`, `source_fetched_after_cutoff` ×4 |
| control C: `fetched_utc` before `release_utc` | `eligible=True` | `eligible=False`, `source_fetched_before_release` ×4 |

Controls B and C flip under the same patch, so the first row's `True` is a real negative and not an inert
patch. Item 2 closes the timestamp side and leaves the date side open.

**Repair, red before / green after, the guard pair the only variable:** add
`observation_after_cutoff:<name>` on `obs_date > cutoff.date()` and `base_session_after_cutoff` on
`base_date > cutoff.date()`. Without the guard the new test exits **1**; with it, **12 tests, OK, exit 0**.
Identical on both interpreters.

### What this changes

Item 2 as written is necessary and not sufficient — it needs a fifth and sixth relation on the two date
fields. Item 3's mutation evidence and item 2's fixture repair both need one positive-path assertion before
either can be read as acceptance. Neither finding touches the research design, R01, or the standing
`M1_OFFICIAL=MISSING` decision, and none of it argues for reopening the methodology.

`EVIDENCE CLASS: MEASURED` for every row above — executed locally at the pinned blob on 3.13.18 and 3.12.3,
each arm with its stated control. **Limitation:** SEMER's reported 3.12.14 is not available here, so
*"identical on SEMER's exact interpreter"* is `NOT ESTABLISHED`; what is established is identical verdicts on
two neighbouring interpreters. The repairs are proposals only — the branch is SEMER's and nothing was pushed
to it.


---
_Generated by [Claude Code](https://claude.ai/code)_