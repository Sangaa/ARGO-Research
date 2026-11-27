# ARGO GOLD LAB — R02 prospective model register and evidence protocol

- Issued: 2026-11-22, Cairo (Africa/Cairo); scientific experiment, not investment advice.
- Status: SESSION-DERIVED / NON-CANONICAL / EXPERIMENTAL / NOT BACKTESTED / NOT INDEPENDENTLY VALIDATED.
- Owner-origin hypothesis families: paper/digital gold, China buying and market power, manufactured/synthetic gold, dollar instability, Egypt financing/geopolitical exposures. The assistant proposes the measurement design and initial experimental coefficients.
- Parent frozen ledger: https://github.com/Sangaa/ARGO-KOP/issues/871
- Frozen R01 forecasts: P001 (2026-11-25 $3450 / EGP 5376), P002 (2026-12-07 $3490 / EGP 5437), P003 (2026-12-22 $3550 / EGP 5532), P004 (2027-02-22 $3700 / EGP 5765). **DO NOT MODIFY R01**.
- No real order or trade. EGP 1m is a PAPER capital comparison only.

## 1. Scientific-integrity finding: original predictions lack feature attribution

R01 forecasts were recorded with inputs, sources, market context and scenario judgments. They did **not** preregister a deterministic model, numeric explanatory weights or feature snapshots that reproduce P001–P004. R01 is scorable as forecast error vs its contemporaneous B0 persistence benchmark. It is **NOT** legitimate to retrofit model weights to R01 after publication, or to say one factor caused its eventual success/failure. This gap is the first original session-derived failure/correction candidate.

R02 describes the **first prospective weighted candidate**, registered after R01 but before any R02 point forecast. The weights below are ASSISTANT-PROPOSED HEURISTICS, NOT fitted market coefficients, causal estimates, or model-weight training. A new R02 forecast counts only when a separate immutable forecast record contains the available feature values, data vintage, computed score and model version before the target period.

## 2. Locked measurement clock and markets

- Each run records recorded_at_utc, observed_at_Cairo, raw source publication/release date, trading-session date, snapshot/reference URLs, unit, status and data availability. Store fetched_at separately from when the observation was valid.
- XAU/USD: single fixed close convention and historical provider (R01 used Investing historical), with the completed UTC trading session; never silently substitute an intraday quote.
- Egypt 21K: seller ask, dealer buy, invoice/making charge if actually quoted, and dealer/source separately. Match comparable vendor and quote type over time; record source dispersion instead of blending unlike observations.
- USD/EGP: fixed institutional quote type (e.g. CBE USD selling) and as-of time; do not mix parallel-market or mid with bank sell.
- If a quote is missing, mark MISSING; no interpolation represented as an observation. Record weekend/holiday target handling prospectively.
- Build distinct 3-, 10- and 22-trading-session experiment strata; do not pool their accuracy as interchangeable independent samples. R01 calendar target dates remain unchanged.

## 3. Decomposed physical-price identity — NOT a causal prediction

For matching timestamps and ask conventions:

  theoretical_EGP_per_g21 = (XAU_USD_per_troy_oz / 31.1034768) * 0.875 * USD_EGP
  observed_premium_q = Egypt21_ask / theoretical_EGP_per_g21 - 1
  Egypt21_ask = theoretical_EGP_per_g21 * (1 + q)

Do not call q a pure scarcity premium: it may include vendor spread, taxes, timing, liquidity, and source mismatch. Track this decomposition separately from any retail product making charge.

At target, local log-price forecast error decomposes exactly when all comparable observations exist:

  ln(P_actual / P_predicted)
    = ln(XAU_actual / XAU_predicted)
    + ln(FX_actual / FX_predicted)
    + ln((1+q_actual) / (1+q_predicted))

This allows a factual attribution of **accounting forecast error** into global price, FX, and premium. It does not prove the causal origin of market movements.

## 4. Predeclared experimental global short-horizon model M1-v0.1

Benchmark B0-G: forecast XAU(target) = latest completed XAU close at issuance.

Use four contemporaneously available directional features, each clipped to [-1,1]. Record raw value, transformed score, lag, release timestamp and source.

| ID | Feature, computed strictly using information released by issuance | Score = [-1,1] clip(...) | Score weight | Hypothesized sign |
| --- | --- | --- | ---: | --- |
| F-DXY | Five completed trading-session percentage change in US Dollar Index DXY | negative of DXY 5d return divided by 1.5% | 0.30 | Stronger USD often pressures USD gold |
| F-REAL | Five completed sessions change in US 10y TIPS real yield, **in basis points** | negative of real yield 5d change divided by 20 bp | 0.35 | Higher real yield raises gold opportunity cost |
| F-MOM | Five completed trading-session XAU percentage return | gold 5d return divided by 4% | 0.20 | Short-term trend persistence (falsifiable) |
| F-ETF | Latest publicly released **weekly net change in physical gold ETF tonnes** | ETF net inflow tonnes divided by 40t | 0.15 | Net inflows may support spot demand |

Initial weights sum to 1.00. Their units are **weights of a constructed forecast score**, not empirically discovered market-explanation percentages. They are arbitrary ex ante test parameters, selected so the model can be falsified and ablated.

  S = 0.30*s_DXY + 0.35*s_REAL + 0.20*s_MOM + 0.15*s_ETF
  predicted_log_return(h) = 0.013 * sqrt(h/3) * S
  M1-XAU(target,h) = XAU(last_completed_close) * exp(predicted_log_return(h))

h = 3 or 10 completed market sessions for the official M1-v0.1 evaluation. The 1.3%-at-three-session amplitude and sqrt scaling are **heuristic test settings, not statistical confidence bounds**. Do not label arbitrary +/- bands as 80% confidence intervals.

Freshness and missingness: DXY/real yields/XAU 5d scores require exact 5 completed sessions with releases available at issue-time; ETF observation must have a published source no older than 14 calendar days. If any factor is unavailable, log MISSING and its weighted coverage; set that score to zero solely for a diagnostic shadow forecast. **Do not publish a full-coverage official M1 prediction when coverage <1.00**; still score B0 and any explicitly named shadow model. No retrospective filling with future releases.

M1-v0.1 does not assign quantified effects to every narrative factor. The purpose is to provide an honestly reproducible starting model, not to claim macroeconomics is fully captured.

## 5. Egyptian FX and premium models: separate baselines

B0-FX: last same-convention USD/EGP quote persists. B0-q: last comparably observed local premium persists.

Exploratory FX model M1-FX-v0.1 (only if six same-convention completed observations exist):

  u = clamp( ln(FX_t / FX_t_minus_5_sessions), -0.08, +0.08 )
  FX_pred(h) = FX_t * exp(0.25 * sqrt(h/5) * u)

The 0.25 sensitivity and +/-8% cap are predeclared provisional values, not demonstrated optimal FX coefficients. q_pred = last available q, with an explicit alert if premium changes by >=2 percentage points or underlying source/quote convention differs. Egypt model M1-EGP multiplies M1-XAU * M1-FX * purity / troy conversion * (1+q_pred).

Report four comparators separately: B0 global; B0 local ask persistence; M1 global; and M1 decomposed Egypt local. For the Egypt error, publish the exact log-error attribution (XAU / FX / premium) above when all target observations are available.

## 6. Wider coupled hypothesis register — researched but NOT silently inserted into M1 weights

Each claim has USER_ORIGIN / ASSISTANT_INFERENCE / DIRECT_SOURCE / UNVERIFIED provenance, observable proxy, source lag, measurement unit, hypothesized direction, counter-scenario and trigger that could make it predictive. Evaluate a later **preregistered model M2** with ablations; no post hoc factor insertion into already issued forecasts.

| Hypothesis | Observable data, test or split | Key unresolved question / invalidator |
| --- | --- | --- |
| H-PAPER / tokenized gold | Issuer-level bar lists, allocated vs unallocated claims, liabilities, independent assurance, redemption terms, proven failures and delivery premia | Unallocated exposure is not proof of aggregate shortage; issuer-specific verified mismatches needed |
| H-CHINA | Official PBoC monthly net tonnes, China ETF tonnage, SGE spot premium, jewellery vs bar/coin demand, net imports, WGC and PBoC data vintage | Buying does not establish monopoly or one-way price control; segregate China's CB flow from global CB flow |
| H-SYNTH-AU | Mass of **actual elemental Au** made through nuclear transmutation, marginal USD/g, energy and throughput, commercial annual tonne capacity | CERN picograms are not market supply; do not conflate Au atoms with visually similar alloy/metal plating |
| H-RECYCLE / ALTERNATIVES | Recycled gold tonnes, mine output, demand substitution, assay results | Substitutes can change jewellery demand without expanding real gold supply |
| H-USD-SYSTEM | IMF COFER dollar share, trade settlement, sovereign debt and reserve flows, US real yields, DXY | Reserve diversification is not proof of imminent dollar collapse; distinguish levels from changes |
| H-EGYPT-FX | CBE interbank rate; reserves; inflation; policy rate; foreign inflows/outflows; tourism; Suez Canal FX receipts; imports and maturity calendar | Finance inflows can support near-term EGP even as future service burdens rise; record both signs |
| H-EGYPT-FINANCE | Funding events: agreement, board approval, actual cash disbursement, repayment/maturity, debt stock and maturity | **Do not call a signed loan a completed disbursement**; do not confuse World Bank and IMF |
| H-GEOPOLITICS | Timestamped conflict/sanction/shipping/oil shock log, announced policy vs enacted rule, energy costs, shipping disruptions, objective risk index if available | No invented probabilities or positive/negative sign without a specified transmission mechanism |
| H-EGYPT-RETAIL | Comparable Egyptian dealer ask/buy spread; premium q; inventories and making charges | A local spike may be FX or retail liquidity rather than international bullion demand |

Sources and observed events at registration (not as-of inputs for any future forecast by themselves):
- World Gold Council 2026 Q3: global official demand 321 tonnes, physically backed ETF inflows 211 tonnes, both quarterly and **not** daily predictors: https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-q3-2026
- LBMA allocated/unallocated legal distinction: https://www.lbma.org.uk/publications/the-otc-guide/precious-metal-accounts/
- China October PBoC activity / original source in R01: https://www.gold.org/goldhub/gold-focus/2026/11/china-gold-market-update-robust-demand-october
- World Bank approved $1bn financing 2026-05-08, signed Egypt phase-II agreement 2026-11-01: https://www.worldbank.org/en/news/press-release/2026/05/08/new-us-1-billion-world-bank-group-development-financing-to-support-egypt-s-private-sector-led-job-creation-macroeconomic and https://sis.gov.eg/en/media-center/news/fm-signs-1-billion-financing-agreement-with-world-bank/
- IMF-Egypt staff-level agreement reported 2026-11-18 for approximately $2.3bn, **pending Board approval**, not a proven cash inflow: https://www.reuters.com/world/africa/imf-reaches-agreement-with-egypt-unlock-23-billion-funds-2026-11-18/
- CERN nuclear-transmutation research, picogram-scale: https://alice-collaboration.web.cern.ch/2025-alice-lead-to-gold

These different release frequencies mean e.g. October China demand cannot be treated as a November 25 intraday shock. Historical correlation, forward causal effect, and evidence of a real-time market surprise are separate claims.

## 7. Append-only forecast issuance record: required fields (R02 and after)

Forecast_ID | Model_version | Parent_issue/commit | Session_ID and executor identity (self-claimed vs authenticated) | task | created_at_UTC | Cairo date | cutoff | target session/horizon | requested instrument | source URLs and as-of | XAU close | FX quote | Egypt21 vendor ask/buy | premium q | **each raw feature** | **each transformed feature s_i** | **each frozen weight w_i** | data coverage | intermediate score S | point forecast | scenario alternatives | baseline B0 | expected direction | uncertainty assumption | **reason for each nonzero contribution and weight status** | falsification conditions | hash/immutable comment link.

Never revise existing predictions or coefficients inside an issued forecast; append a new version and link superseded candidate. A source released after cutoff is excluded even if a later revision says it applied to an earlier economic period. Keep data-vintage identity.

## 8. Evaluation and learning proof

At each checkpoint:
1. Read old frozen forecast(s) before viewing target outcomes; authenticate snapshot/cutoff as available. Record unscorable forecasts, don't delete them.
2. Capture target global close/local ask and FX using comparable conventions and dates; compute absolute USD error, absolute EGP error, percentage errors, direction correctness and whether exploratory intervals cover the target.
3. Compare SAME forecast horizon, target date and instruments against B0 persistence, plus M1 and any preregistered ablations; no cherry-picking of winners. Publish full ledger even when M1 underperforms.
4. Log forecast **decomposition** into XAU/FX/premium accounting errors, feature sign contributions from issued snapshot, and source-backed event surprises. Unknown mechanisms remain unresolved, not asserted causes.
5. Classify outcome by: WHAT_SUCCEEDED + evidence and likely reason; WHAT_FAILED + evidence and likely reason; UNKNOWN; error in data/source/measurement vs model vs regime vs execution.
6. Add correction prospectively to version M1-v0.2+, with prior version and exact changed weight, hypothesized mechanism, why justified, what would disprove; perform ablation dropping each feature in one predeclared evaluation. **Never modify R01 or retroactively refit evaluated forecasts.**
7. To claim improvement: at least 20 **non-overlapping** genuinely forward forecasts per horizon, same-data B0 and prior-version comparisons, holdout after change, MAE/MAPE deltas, directional stats, interval coverage if calibrated, sampling uncertainty; preferably confidence interval for loss improvement above zero. Report if insufficient.
8. Promote no result to canonical ARGO and claim no model-parameter or weight training absent explicit governed proof. Repository-mediated strategy revisions are not LLM weight updates.

### Session closeout block (publish per run)

- CHECKPOINT / timestamp Cairo / Session_ID (verified or self-claimed) / Task_ID / source branch+SHA or issue comment ID
- RAW_MARKET: XAU, Egypt21 ask/buy, USD/EGP, q, source timestamp, gaps
- PREVIOUS_FORECASTS_DUE: IDs; target actuals; B0 vs M1 error table; non-scorable reasons
- SUCCESS: what worked and precise evidence, not self-congratulation
- FAILURE: what failed, how measured, source/feature/model/execution attribution and alternative explanations
- NEXT_CHANGE: specific old→new weight/feature rule, isolated reason, counterfactual test, prospective effective date
- ORIGINAL_EXPERIENCE: first-person candidate / NO_NEW_MEMORY, source identity; non-canonical and review status
- NEXT_ACTION: next issuance with complete snapshot + weights, or precise blocker; no claim of external reviewer sessions automatically running

## 9. Controls

- This document is experimental and add-only; currently branch-only until governed integration. Parent issue #871 is the immediately visible log.
- No Actions or paid CI, no modification of governance, no direct main mutation, no automatic trading, no production/canonical promotion.
- Roles may be assigned later explicitly: source/data owner, HORUS for competing mechanisms, THOTH for candidate learning, MAAT for independent scientific integrity, HERMUZ for test harness; naming roles **does not** start, authenticate or prove sessions.
- Owner authority can change study scope prospectively; published failed predictions stay visible.

## 10. Current specific failure/correction captured

FAILURE-R01-ATTRIBUTION-001: R01 had transparent inputs and 4 forecast points but lacked locked numerical coefficients/feature snapshot. EFFECT: future outcomes can score price accuracy, not causal contribution or weight realism. CORRECTION-R02: pre-register deterministic M1-v0.1 and timestamped feature data per issuance; compare with B0 and ablated variants on the same observations. CURRENT STATUS: methodology published; R02 market forecast NOT YET ISSUED; no proof of predictive improvement.
