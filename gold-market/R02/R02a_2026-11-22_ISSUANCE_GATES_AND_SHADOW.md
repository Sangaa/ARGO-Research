# ARGO GOLD LAB — R02a issuance gates and first shadow snapshot

- Issued: 2026-11-22 14:11:38 UTC / 16:11:38 Africa/Cairo.
- Status: SESSION-DERIVED / NON-CANONICAL / PROPOSED APPEND-ONLY AMENDMENT / NOT INDEPENDENTLY VALIDATED.
- Parent methodology remains immutable: R02 register at 56d7cfef144dc4c9aed771bf4ee32d75941faa98, blob a0327b2190bf5fce21172840443e132cbee424c7, linked from #871 comment 7080175590.
- This file does not change R01 P001–P004, the prior R02 coefficients, or any forecast. It records a prospective issuance gate and a diagnostic shadow snapshot only.
- No trade, hosted Actions, PR, or canonical promotion.

## 1. Review result

The R02 equation is internally computable, but the frozen register did not yet select operational source/vintage procedures, a deterministic cutoff protocol, target-session mapping, or full quote conventions. Two read-only reviews reached the same bounded conclusion:

- Scientific-integrity review: current evidence does not support a reproducible official M1 issue.
- Arithmetic review: one synthetic calculation is consistent with the stated equation; this is not runtime verification.
- Reviewer identity: tool-generated review; no authenticated MAAT/HERMUZ seat or blinded independence was established.

## 2. Coverage / provenance matrix

| Requirement | Current evidence | Status | Decision effect |
|---|---|---|---|
| R01 fixed and not retrofitted | R01 points are frozen in #871; R01 attribution failure is explicit in #871/7080175590 | PRESENT / PINNED | Score R01 numerically vs its original B0 only |
| M1 formula, signs, weights and clipping | R02 register at exact commit above; weights sum to 1.00 | PRESENT / SOURCE-READ | Permits formula calculation, not model validation |
| Five-session XAU and DXY observations | Investing historical rows for Nov 13 and Nov 20 captured below | PARTIAL / WEB READBACK | Two feature scores can be computed |
| Five-session real-yield change | FRED DFII10 page showed latest observation Nov 19, next release Nov 23; no Nov 20 endpoint at cutoff | MISSING | Full M1 blocked (weight 0.35) |
| Latest public global weekly physical ETF net flow | WGC says weekly data update Monday following the week; page dated Nov 16 and chart values were not retrievable in this read | MISSING | Full M1 blocked (weight 0.15); no fund-subset substitution |
| Egypt 21K ask and FX | Existing R01 aggregator quotes are not a locked same-dealer/same-time series; no fixed bank sell source/readback bound here | MISSING | No Egypt21 forecast or error decomposition |
| Target session dates | R02 says 3/10 sessions but does not bind this issuance to exact target-close dates/calendar | MISSING | Shadow numbers are horizon diagnostics only; not a date-bound issued forecast |
| Independent arithmetic | Synthetic hand calculation below; no executable verifier/mutation test was run | PARTIAL | Formula check only; not runtime evidence |
| Independent reviewer | Two separate tool-generated read-only outputs; seat identities/blinding not authenticated | PARTIAL | Challenge recorded; not an independent MAAT approval |

## 3. First R02 availability decision at the stated cutoff

The cutoff is the immutable timestamp in the header. Only source observations publicly available by that cutoff may contribute. A subsequent release, page revision, or provider substitution cannot be backdated. fetched_at and the observation/release time must both be retained for every later official issuance.

### Retrieved values

- XAU/USD, Investing.com historical close: 2026-11-13 = 3,880.70; 2026-11-20 = 3,532.87 USD/troy oz. Source: https://www.investing.com/currencies/xau-usd-historical-data — retrieved 2026-11-22 at the cutoff above. Historical rows are the source readback; no page-body hash was captured.
- DXY, Investing.com historical close: 2026-11-13 = 103.41; 2026-11-20 = 103.81. Source: https://www.investing.com/indices/usdollar-historical-data — retrieved 2026-11-22 at the cutoff above. Historical rows are the source readback; no page-body hash was captured.
- 10-year TIPS real yield, FRED series DFII10: latest page observation = 2026-11-19 at 2.88%; page showed next release 2026-11-23. Required 2026-11-20 endpoint unavailable at cutoff. Source: https://fred.stlouisfed.org/series/DFII10 .
- Global weekly physical ETF flows: World Gold Council states weekly data update on Monday following the week, except monthly update; current page displayed 16 November 2026. The numeric global weekly flow was not retrievable in this read, and the Nov 20 week had not yet been published by the stated schedule. Source: https://www.gold.org/goldhub/data/gold-etfs-holdings-and-flows .

### Diagnostic SHADOW (not official M1; no target dates locked)

Using decimal percentage returns and the frozen R02 weights without renormalization:

- DXY return (103.81 / 103.41 − 1) = +0.3868098%; score = −0.2578732; weighted contribution = −0.0773620.
- XAU 5-session return (3,532.87 / 3,880.70 − 1) = −8.9630737%; score clipped to −1.0000000; weighted contribution = −0.2000000.
- Real-yield score/contribution = MISSING / 0.0000000 for shadow only.
- ETF-flow score/contribution = MISSING / 0.0000000 for shadow only.
- Available weight coverage = 0.50; shadow score S = −0.27736196. No renormalization.
- Shadow XAU values from XAU_t * exp(0.013 * sqrt(h/3) * S): h=3 → USD 3,520.15445; h=10 → USD 3,509.68919.
- Same-horizon persistence B0-G = USD 3,532.87 for each horizon.
- Classification: MISSING_OFFICIAL_M1 / DIAGNOSTIC_SHADOW_ONLY / NOT_DATE_BOUND / NOT_SCORABLE_YET. Do not treat these as a full-coverage R02 issuance, calibrated range, investment advice, or evidence of improvement.

Egypt21 remains MISSING; do not multiply by the prior indicative EGP quote because the quote/source/time conventions were not fixed.

## 4. Prospective gates before any official R02 issuance

1. Freeze before looking up inputs: publish a unique Forecast_ID, exact cutoff in UTC and Cairo, model version, h, and concrete target-session close date. Do not choose or alter the target after seeing feature values.
2. Session convention: name the price series whose completed daily rows define XAU sessions, the date/time zone represented by each row, and the rule mapping the next 3/10 distinct completed rows to target dates. No row for a weekend/holiday is not a session. Store the resulting dates in the forecast record; never remap R01.
3. Source/vintage lock: record for each series its exact source/series ID, raw value, observation date, publication/release timestamp, retrieval timestamp, unit, URL, and archived response/hash where available. If a revised series has no usable as-of vintage, disclose that limitation; never imply the revision history was frozen.
4. No source substitution: continue XAU from the R02 named historical provider; select and pin exact DXY series, FRED DFII10 vintage retrieval, and global weekly physical ETF aggregate before issue. If the latest public ETF value is paywalled, aggregate coverage is unclear, or release timestamp is unprovable, set MISSING. Do not substitute GLD-only or other partial funds for the registered global feature.
5. Units: store percent returns as decimals and also display percent; store TIPS difference in bp; ETF flow in net tonnes. Apply clip(x, -1, +1) to normalized scores. Preserve raw value, score, frozen weight, and contribution. Missing score is zero only in a clearly labeled shadow; never renormalize.
6. Egypt quote lock: name one seller/source for both ask and dealer bid, quote timestamp/time zone, whether taxes/making charges are included, and one fixed USD/EGP institutional quote convention and source. Compute q only from contemporaneous comparable observations. If unavailable, keep the Egypt track MISSING.
7. Scoring: every eligible frozen prediction is paired with the same exact target observation and B0. Show all issued, shadow, abstained/MISSING, and unscorable records. Accuracy denominator is the count of eligible forecast-and-target pairs; publish excluded/missing counts and reasons. B0 may be scored when its target exists even if M1 abstained. No calibrated interval exists yet, so interval coverage is NOT_APPLICABLE, not zero. Use non-overlapping targets for each horizon; after any model change, start a distinct holdout. No improvement claim before the predeclared minimum and paired loss-uncertainty analysis in R02 are satisfied.

## 5. Synthetic arithmetic check (not live market evidence)

Read-only reviewers used this illustrative vector: XAU=2000; DXY +0.75%; TIPS +10 bp; XAU momentum +2%; ETF +20 tonnes. Scores are −0.5, −0.5, +0.5, +0.5; weighted contributions are −0.150, −0.175, +0.100, +0.075; S=−0.15. Formula output: h=3, 1,996.103800; h=10, 1,992.892267. This matches the written equation by manual calculation. It is not a repository test, runtime verification, backtest, or independent blinded check.

## 6. Next step

Before a date-bound official M1 forecast: freeze the source/calendar/quote choices and a raw snapshot protocol in an append-only successor; then run a tiny deterministic local verifier with unit, clipping, missingness, same-target B0, and broken-checker mutation cases. Reconcile its exact output independently. If any required input or target date remains unavailable, publish MISSING/shadow again with the named missing fields. No owner market judgment is needed for this gate.

## Experience / memory boundary

EXPERIENCE_CANDIDATE = R01 lacked frozen numerical attribution, so later weights cannot explain it; captured as CORRECTION-R01-ATTRIBUTION-001 in #871/7080175590. This issue already carries the original source. No duplicate memory/index entry is created here; no independent learning, canonical status, or model-weight update is claimed.
