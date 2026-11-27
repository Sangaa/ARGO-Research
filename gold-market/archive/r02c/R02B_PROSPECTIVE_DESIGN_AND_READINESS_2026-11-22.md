# ARGO GOLD LAB — R02b prospective design and readiness contract
Date: 2026-11-22 (Cairo)
Status: SOURCE-ONLY DESIGN AMENDMENT; NOT R02 ISSUANCE; NOT LAB_READY; NOT LEARNING PROOF

## Provenance and frozen boundaries

This is a prospective addendum to the R02-v0.1 candidate. It does not alter frozen R01, the original R02 register, any historic shadow arithmetic, or the model weights. It records a method choice before any valid R02 forecast. Candidate coefficients remain hypotheses, not estimated causal effects:

- DXY 0.30; real yield 0.35; momentum 0.20; physical ETF flow 0.15.
- Existing formula, clipping, amplitude and baseline remain as frozen in R02.
- Every result must preserve source timestamps, missingness, and the distinction between official issue, shadow, missing, and scored outcome.

No valid R02 forecast is evidenced at this addendum's creation. Existing R02 status remains MISSING.

## Primary endpoint and registered comparison

Primary confirmatory comparison: frozen M1-v0.1 against global persistence B0-G, XAU/USD closing price, h=3 completed XAU trading sessions. Primary statistic is the paired mean absolute-error difference:

D = mean(|actual - M1| - |actual - B0-G|)

Negative D favors M1. Both forecasts must use the same target close and the same eligible issue cohort. Report the full paired observations, D, median paired difference, MAE of each method, relative MAE reduction, missing/abstained slots, and an uncertainty interval. Other model/baseline pairs, Egypt/local-price decomposition, h=10 and h=22 results, direction accuracy, and feature ablations are secondary or exploratory and cannot replace the primary endpoint after results are seen.

Expected result registered in advance: no improvement over B0-G is plausible and is an acceptable study outcome. Twenty paired, forward, non-overlapping h=3 target observations are a minimum review gate, not a power guarantee. At that fixed N, if D is zero or positive, close this version's primary cohort as “no observed MAE improvement on this registered sample.” If D is negative but the predeclared uncertainty interval includes zero, report “promising but inconclusive.” Do not extend, change the endpoint, or choose a new horizon in response to a near miss. A later cohort requires a new dated amendment before its first target exists. Do not claim that this result proves the feature set cannot predict.

Before the first official issue, the uncertainty method and interval level still require an explicit executable specification and an independent preflight. Small-sample intervals must not be presented as proof; serial dependence and regime changes remain limitations. Until this gate is closed, no confirmatory improvement claim is allowed.

## Issuance cadence and calendar

The existing every-three-calendar-days automation is retained as a readiness, source-availability, due-score, and checkpoint cycle. Its recurrence is not an issuance calendar and must not cause a forecast. A missed/invalid source gate is recorded as MISSING at that scheduled checkpoint.

Before any official issue, publish a fixed prospective issue-slot calendar that is compatible with verified release times for every required source. Each slot must identify its UTC cutoff, issue time, completed XAU base close, and exact next 3/10 XAU trading-session targets. h=22 remains exploratory only; it is outside the current checker and cannot support a release claim until separately specified and tested. The slots must be fixed before observing the feature values or choosing a date based on data arrival. If no eligible fixed slot exists for a cycle, write MISSING; do not slide the cutoff or issue later opportunistically. Keep original R01 calendar dates unchanged.

The calendar cannot be considered authoritative from a hand-entered list alone. Its source, version, timezone, holiday rules, retrieval timestamp, payload bytes and SHA-256 must be pinned and independently checked. Exact five-session feature lookbacks must use source-specific completed observations and record every contributing date.

## Source and forecast archive contract

For each feature and each contributing observation, retain:

- vendor/source and series/instrument identifier, retrieval URL, quote currency/unit/type and vintage/version;
- observation date, independently evidenced public release timestamp, retrieval timestamp, frozen UTC cutoff and issue timestamp;
- exact raw response bytes, archived before scoring, with SHA-256 computed from those bytes and verified on readback;
- feature value, transformation, unit, clip boundary, source dates used, score, frozen weight, contribution and missingness reason.

A digest-shaped string alone is not proof of archived bytes. The R02b verifier now rejects a payload whose supplied digest does not match the supplied bytes, but it does not fetch vendors, prove a release timestamp, certify a source vintage, or establish a calendar's authority. These remain external acceptance gates.

Forecast and outcome records must be append-only, carry unique IDs, and store canonical serialized bytes plus digest. Any edit to a frozen forecast must fail; corrections are new linked records preserving the original. A later outcome may be joined only after its target close is complete and its source vintage is recorded.

## Matched scoring and learning boundary

B0-G and M1 use the same base close, cutoff, issue slot and target close. Keep abstentions and missing inputs in the schedule ledger; do not silently drop them when reporting availability. Only eligible official forecasts enter the primary paired MAE cohort. Report all scheduled slots and explain any unscorable target.

For Egypt, compare matched buy/ask quotes and contemporaneous USD/EGP convention, then report XAU, FX and local-premium log-error components as accounting decomposition. Do not infer causation from the decomposition.

Repository-mediated method learning may be claimed only when a documented failure changes a prospective method version before unseen target data, the new version is frozen before those targets, and its matched forward holdout is compared with both the prior version and B0 under the same registered endpoint. This is not LLM/model-weight training. A code edit, experience note, retrospective shadow, or passing synthetic tests alone is not learning proof.

## Current bounded readiness disposition and exit gates

R02b is not yet LAB_READY. The isolated arithmetic/issuance checker can exercise local fail-closed invariants, but the following gates remain open:

1. A completed, independently pinned authoritative session calendar and release-aware fixed issue-slot map.
2. Real vendor raw payload archive, verified byte hashes, release/vintage evidence and exact source/lookback conventions for XAU, DXY, TIPS and weekly physical ETF flows.
3. Verified completed XAU base close and exact next target-session mapping; comparable Egypt seller ask and FX quote conventions for any Egypt output.
4. An executable immutable forecast-ledger readback and target-join/scoring replay.
5. Frozen interval procedure, exact cutoff/issue-slot format, and independent preflight of the complete protocol.
6. A synthetic/historical NOT_FORWARD replay proving both clean acceptance and adverse rejection gates at one recorded exact source SHA.

Until all gates close, classification is PARTIAL_READINESS; official M1 remains MISSING, and LEARNING_PROVEN remains false. The next scheduled cycle may audit readiness and due outcomes but may not manufacture source data or issue an unregistered forecast.

## Review provenance

This is a repository-authored prospective design amendment informed by current source comments and tool-generated challenge reviews. Reviewer comments are not authenticated MAAT/HORUS/THOTH seat approval. This document does not assert that any independent provider session ran, that field data was validated, or that the lab achieved release readiness.


## 2026-11-23 clarification — review slot is not an issuance slot

The preserved recurring checkpoint at 09:00 Africa/Cairo is readiness/scoring only. On the currently recorded 2026-11-25 run it maps to 07:00 UTC; the current evidence says that is before the US session/release window needed to establish the latest eligible real-yield observation. Therefore this time must never be treated as a forecast issuance slot. See the source-timing warning in #783/7086880641. No replacement UTC issuance time is selected here: first pin authoritative calendars and source-specific publication/retrieval rules, then preregister fixed UTC cutoffs and issue times prospectively. If no such slot is verified, record MISSING.

The uncertainty method remains OPEN pending the executable specification and independent protocol preflight. This clarification does not close any external-source, archival, ledger, local-quote, scoring, or reviewer gate and does not change R01 or any forecast.
