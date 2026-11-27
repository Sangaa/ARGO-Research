# ARGO Gold Market — route index

**Status:** SESSION-DERIVED / NON-CANONICAL / SOURCE-ONLY / NOT EMPIRICALLY VALIDATED. This transfer preserves the original records; it does not make a new forecast or activate a model.

## Why the lane exists
Track falsifiable global XAU/USD and Egypt retail-gold forecasts prospectively, score them against frozen naive baselines, and preserve source timing, failures, corrections, and abstentions. R01 paper capital is only a benchmark, not authorization to trade.

## Route map
- [R01 frozen baseline](records/R01_issue_871.md) — exact issue body from private Sangaa/ARGO-KOP#871.
- [R02 preregistration](R02/R02_2026-11-22_PROSPECTIVE_MODEL_REGISTER.md), [issuance gates](R02/R02a_2026-11-22_ISSUANCE_GATES_AND_SHADOW.md), and [source-timing correction](R02/R02a_CORRECTION_2026-11-22_SOURCE_TIMING.md).
- [R02 verifier histories](archive/) — distinct R02b–R02h design, checkpoint, and verifier snapshots, each kept under its originating branch. Do not infer a linear history beyond recorded parent references.
- [R03 method comparison](R03/R03_2026-11-24_EXTERNAL_METHODS_AND_WEIGHT_CHALLENGER.md) and shadow candidate.
- [R04 indicator register](R04/R04_2026-11-24_MARGINAL_INDICATOR_REGISTER.json) — COT and options-skew candidates, still shadow only.
- [Source records](records/) — verbatim issue body and selected append-only comments, including P001 outcome.
- [Source manifest](source_manifest.json) and [archive verifier](verify_archive.py) — provenance and content-integrity certificate.
- [Migration and reassessment](MIGRATION_AND_REASSESSMENT.md) — bounded conclusions and next work.

## Current supported reading
The only scored global R01 outcome in these records is worse than frozen B0 for that target. Egypt P001 remains unscored because the closing quote convention is not comparable. One outcome establishes neither forecasting skill nor learning.

R02 is not ready for an official forecast: release/vintage and calendar authority, immutable real-data snapshots, comparable Egypt observations, and replay defects remain open. R03/R04 are heuristics, not fitted weights.

## Evidence discipline and provenance
Original files are preserved byte-for-byte. Historical claims keep their original source links and limitations. The imported verifier reports are not represented as reruns here. Source artifacts originated in private Sangaa/ARGO-KOP; commit/blob references are in the manifest. This public lane is an archival copy, not a claim that private source records were deleted or superseded.
