# R02 verifier — execution and mutation-sensitivity record

- Recorded: 2026-11-22.
- Status: SESSION-DERIVED / NON-CANONICAL / BRANCH-ONLY TEST EVIDENCE.
- Source code: Research/ARGO_GOLD_LAB/r02_verifier.py, commit 3433ac5645ab3162a10e5da40b8046847e5ce7e1, blob 8da7a7a0dc1c76b4899b8139cfcd698ce7359729.
- Test runtime: Python 3.12.14, standard library only, no network, hosted CI, or repository mutation during execution.

## Exact run

The source file was read back from GitHub at the pinned commit and written to a temporary local file for execution.

- Unmutated script: 9/9 unittest cases passed; process exit 0.
- Mutation check: a temporary copy changed the scoring line to divide the weighted sum by available weight coverage (incorrectly renormalizing a partial feature set). The same suite failed as expected in test_missing_feature_is_zero_weight_shadow_without_renormalizing: expected S=-0.15, observed mutant S=-0.5; process exit 1.
- The mutation existed only in a temporary file and was not committed or pushed.

The tests cover weight sum, units/sign/clipping, synthetic forecast arithmetic, missing-feature shadow/no-renormalization, release-time and snapshot guards, required target list/calendar membership, same-target B0 pairing, and exact local log-error decomposition.

## Limits

- The tests do not prove the supplied session calendar is an authoritative real-world market calendar; they only check membership in the calendar supplied to the function.
- The source-snapshot hash is a caller-provided non-empty marker; the script does not fetch sources or verify a cryptographic snapshot.
- The script does not verify vendor release timestamps, revisions, forecast immutability on GitHub, local dealer quote comparability, confidence intervals, or predictive performance.
- A passing arithmetic/gate suite does not make the currently missing inputs available. No valid first R02 forecast is issued by this test record.
- This is a ChatGPT/SEMER-context execution using the connected repository API and local Python runner. GitHub commit metadata reflects the authenticated repository account; it does not authenticate a SEMER or HERMUZ provider seat.

## Next

A source owner must bind the exact calendar, source series and retrieval/vintage evidence. A reviewer other than the code author must inspect this exact blob before any code integration or official issuance. Keep MISSING status until all four registered features are captured before a frozen cutoff and exact target dates are set.
