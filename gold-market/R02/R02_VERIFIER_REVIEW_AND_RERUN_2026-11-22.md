# R02 verifier — review corrections and bounded rerun

- Recorded: 2026-11-22.
- Status: SESSION-DERIVED / NON-CANONICAL / BRANCH-ONLY EVIDENCE.
- Exact verifier under review: Research/ARGO_GOLD_LAB/r02_verifier.py at commit d2d5e325e2d0260c3b5fb1ed71f547b7f2e2b5b2, blob d4c1d008afd2486c6c2259d485873090d118c68d.
- Reviewer: separate tool-generated read-only code review, not authenticated HERMUZ and not a blinded independent provider seat.
- Runtime: Python 3.12.14; standard library; no Actions or network during tests.

## Preserved initial review failure

The first verifier version (commit 3433ac5645ab3162a10e5da40b8046847e5ce7e1, blob 8da7a7a0dc1c76b4899b8139cfcd698ce7359729) passed 9/9 tests, but static review found that it accepted timezone-naive timestamps and did not require the next exact session rows after a base date. The first version also had only a calculated mutant comparison, not an executed mutation.

## Correction and exact rerun

The code author changed the decision/action in response to that review:
- UTC parser now requires an explicit offset and normalizes to UTC.
- Issue guard checks release times, fetch-before-issue, observation not after base, ETF <=14-day freshness, and exact next H unique ordered dates from the supplied session calendar after the base date.
- Snapshot SHA shape must be 64 hexadecimal characters.
- Tests now cover missing features, malformed target mapping/calendar, timezone absence, cutoff order, fetch timing, and invalid feature units.

Read-back from GitHub at the exact commit above was run locally.

- Unmutated verifier: 11/11 unit tests passed; exit 0.
- Executed mutation: in a temporary copy, the weighted sum was changed to divide by available weight coverage. The test suite rejected that deliberately broken implementation in test_missing_feature_is_zero_weight_shadow_without_renormalizing (expected S=-0.15; mutant produced -0.5); exit 1. Temporary mutation was not committed.
- Separate static review of the updated blob confirmed the guards improved and found remaining limitations listed below.

## Remaining limits from the reviewer and this session

- Calendar membership is conditional on a supplied list; the verifier does not authenticate the calendar provider or compute real-world market sessions independently.
- Base session date is caller-provided and is not tied to an independently verified completed XAU close/time.
- SHA format is checked only; the code does not hash response bytes or bind raw feature values to a payload.
- Metadata fields are shape-checked, not independently validated against the source. The verifier does not establish public availability/vintage, source revisions, exact five-session lookback construction, or ETF aggregate completeness.
- It does not freeze/verify an immutable forecast record or prove append-only GitHub storage. Paired score only compares caller-supplied identical target keys; no MAE/ablation/prospective outcome pipeline is implemented.
- This is therefore an arithmetic and issuance-shape guard, not source validation, a market-calendar authority, scientific validation, or proof of forecast improvement.

The source-timing error in the first R02a record remains separately preserved at R02a_CORRECTION_2026-11-22_SOURCE_TIMING.md. Current gold-market status remains MISSING official R02; no valid forecast is created by this code evidence.
