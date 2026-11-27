# R02a correction — source retrieval timing and shadow classification

- Correction recorded: 2026-11-22, immediately after R02a creation.
- Applies to: Research/ARGO_GOLD_LAB/R02a_2026-11-22_ISSUANCE_GATES_AND_SHADOW.md at parent commit fc1b7fb10c8e8ade53c8cd9d8f3d3eb4d42bce3b.
- Status: SESSION-DERIVED / NON-CANONICAL / APPEND-ONLY PROVENANCE CORRECTION.

## Preserved error

The R02a file stated that Investing, FRED and World Gold Council values had been “retrieved at” the 14:11:38 UTC cutoff. The clock was read at that time, but the web source reads occurred in later tool calls. Exact retrieval timestamps were not returned by the web connector, and no archived response bytes or page hashes were captured.

## Corrected interpretation

The listed source rows are post-cutoff web readbacks of historical values. They are useful for identifying likely missing inputs and checking arithmetic, but they do not prove a point-in-time snapshot available at the declared cutoff. Therefore:

- Downgrade the numeric h=3/h=10 values from DIAGNOSTIC_SHADOW_ONLY to RETROSPECTIVE_SHADOW_CALCULATION / NOT A FROZEN FORECAST.
- Keep official M1 status MISSING; no valid first R02 prediction was issued.
- Do not score the shadow values or describe them as prospective predictions.
- Preserve the numeric arithmetic as an illustration only. R02’s immutable issuance gate remains unmet.
- A later valid issue must freeze its cutoff first, capture each source with retrievable as-of/release evidence and retrieval timestamp, store the raw snapshot/hash when possible, and then issue the forecast before its target.

This correction supersedes the shadow classification in the parent R02a record without deleting or hiding the initial overstatement. It does not alter R01, R02 weights, or market forecasts.
