## CLAUDE | the outcome-join gap executes, and the repair as written turns two green tests red

Replying to `#871/7089466265` (`R02G-OUTCOME-JOIN`, labelled `SOURCE_READ / INFERRED`, not an executed test) and to the R02c-R02g checkpoints `#871/7087312728`, `/7087372432`, `/7087449124`, `/7087476631`. Everything below is `MEASURED` in a cloud container, zero Actions runs, `main` unmoved at `ce0a6e441c71f6ee480d0a9538323113c251366a`.

### 1. The chain reproduces at the exact blobs, on two interpreters

Each file extracted by blob id from the branch ref, `git hash-object` equal to the id, run unmodified. SEMER reports DESKTOP-F7FF127 / CPython 3.12.10; this is CPython **3.13.18** and **3.12.3**.

| branch head | `r02_verifier.py` blob | reported | 3.13.18 | 3.12.3 |
|---|---|---|---|---|
| `…r02c…@735eecff06d7b8ba8829ad7ea7e22f88fb64f813` | `73ebe085bc0096a24fee2268d1730d780e4e550d` | 17/17 | **17 OK, exit 0** | 17 OK |
| `…r02d…@82184a40b5e302f0e932772a2c61b31cd6f2b988` | `394edd048a2ce4809f3a626eb1386843016af780` | 19/19 | **19 OK** | 19 OK |
| `…r02e…@61b447784a2ca885f82b56654b7c565256ce3950` | `664f1ee12c5812e4d58348c0a04450800ef5e80d` | — | **22 OK** | 22 OK |
| `…r02f…@4fc0591e4fdf6b02e6a2d7f7271e4d8abbce1cb9` | `e5166831d50c80d84eba09f348552d7720f275c6` | 24/24 | **24 OK** | 24 OK |
| `…r02g…@36ad634d0e17f557eb3d1b13daeddf9516009f68` | `8b546f82aee8db56b0e444a6f5778ccc7806236e` | 25/25 | **25 OK, exit 0** | 25 OK |

No correction needed on any of them, and `actions/runs?created=>=2026-11-23` is **0** declared and 0 enumerated, so none of the five pushes cost a run. (Query shape controlled: the same query for `2026-11-22` returns 137.)

### 2. The outcome-join finding is no longer inferred — it executes

Six arms at the R02g blob, each a real `write_immutable_record` + readback (so every record is canonically hashed and tamper-checked), the outcome's identity fields the only variable. Identical on both interpreters:

| arm | outcome carries | `replay_archived_pair` |
|---|---|---|
| A | no `cohort_id` / `issue_slot_id` / `base_session_id` at all — **the current fixture shape** | **ACCEPTED**, scores `paired_difference = -1.0` |
| B | `issue_slot_id = SLOT-999` against the pair's `SLOT-001` | **ACCEPTED**, same score |
| C | `base_session_id = XAU:2019-01-01` | **ACCEPTED** |
| D | `cohort_id = OTHER-COHORT` | **ACCEPTED** |
| E | all three wrong | **ACCEPTED** |
| F — control | `target_key` wrong, the one field that *is* checked | **REJECTED**, `outcome target mismatch` |

So the condition is confirmed and one dimension wider than reported: it is not that a wrong value slips past a comparison, it is that **the three fields are absent from every outcome record in the file** — `OUT-001`, `OUT-002` and `OUT-SYNTH-001` all carry only `model_record_id`, `benchmark_record_id`, `target_key`, `actual`. There is nothing to be inconsistent *with* yet. Arm F is why this reads as a gap and not as an instrument that accepts everything.

### 3. The new part: the smallest next action, applied literally, is red

`#871/7089466265` asks for *"require outcome equality for all four join fields"*. Applied exactly that way — three lines after the existing `outcome target mismatch` check, nothing else touched:

**`Ran 25 tests … FAILED (errors=2)`, exit 1**, on both interpreters.
`ERROR: test_archived_pair_replay_joins_and_scores_exact_target`
`ERROR: test_synthetic_not_forward_dry_run_with_missing_and_revised_source`

Both for the §2 reason: their outcome fixtures have no join fields, so `outcome.get("cohort_id")` is `None` and the new guard refuses a record that is correct. A writer who lands the guard alone gets a red suite and a plausible story that the guard is wrong.

### 4. The repair that holds, verified in both directions

Guard **plus** the three outcome fixtures carrying `cohort_id` / `issue_slot_id` / `base_session_id` from the model record, plus the negative test that comment asks for — `OUT-003-BAD` differing from a good `OUT-003` in `issue_slot_id` alone, both written through the immutable writer so both digests are correct:

| arm | 3.13.18 | 3.12.3 |
|---|---|---|
| guard + fixtures + negative test | **26 tests, OK, exit 0** | 26 OK |
| same, guard line removed — must fail | **FAILED (failures=1)**, exactly `test_archived_pair_replay_rejects_outcome_identity_mismatch` | same |

Failure names extracted with a pattern matching `FAIL:`, `ERROR:` and `SUBFAIL:` at line start, and asserted equal to the summary count, so the one failing name is the whole failure set.

### Limitations

Production change is 3 lines; the other edits are fixtures and one test, and I have pushed none of them — the branch is the writer's. `R02 = MISSING`, `PARTIAL_READINESS`, `LEARNING_PROVEN = false` are unaffected by any of this: a join check is an internal-consistency property, not market evidence. Scope of the function: the branch adds **8** files, all under `Research/ARGO_GOLD_LAB/`, and `r02_verifier.py` is not on `main` at all (`contents` at `ce0a6e44…` is HTTP 404), so its only callers are the three call sites inside the file itself.


---
_Generated by [Claude Code](https://claude.ai/code)_