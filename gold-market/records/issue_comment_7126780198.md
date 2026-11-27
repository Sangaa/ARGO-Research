## ARGO GOLD LAB — R03 global/Egypt methods and weight challenger | 2026-11-24

**OWNER REQUEST:** Compare current gold-analysis platforms and analyst reports locally/globally; contrast published methods and disclosed numerical weights with ARGO's, and update the experimental lab without falsifying the existing test.

**Verified repository action (source-only, not main/approved):**
- New branch from `main@35f276b7428ed2b936ac4e8dd35caa4c91fc7ed3`: `argo/gold-lab-r03-external-weights-review-20261124`
- Head `8f7546286385d18d0809293579e0f03ebeacfeaa`.
- [R03 comparative review](https://github.com/Sangaa/ARGO-KOP/blob/8f7546286385d18d0809293579e0f03ebeacfeaa/Research/ARGO_GOLD_LAB/R03_2026-11-24_EXTERNAL_METHODS_AND_WEIGHT_CHALLENGER.md), blob `c51fcb631793ea1a96e0b722710e5e6098143cba`.
- [Machine-readable NON-ACTIVE M2 shadow configuration](https://github.com/Sangaa/ARGO-KOP/blob/8f7546286385d18d0809293579e0f03ebeacfeaa/Research/ARGO_GOLD_LAB/R03_2026-11-24_M2_SHADOW_CANDIDATE.json), blob `53a26c806eef1eb4f13de48e8b27ade49188787f`. GitHub readback and JSON parsing confirmed; both weight vectors sum to 1 (floating-point tolerance).
- No code/main change, no PR/Actions, no new market forecast, no trade and no independent acceptance claim.

### Comparators (direct source references in R03 document)
WGC GRAM = historical weekly/monthly regression attribution to expansion/risk/opportunity-cost/momentum, not transferable fixed 3-day coefficients; WGC Qaurum = scenario-based medium horizon; LBMA experts/Goldman/Reuters = varying named macro/physical drivers but no public comparable four-factor normalized weights; TradingView = **published 50/50 MA-vs-oscillator signal-group aggregation** (not economic causal weights); Investing technical signal tools; CFTC weekly positioning/CME FedWatch policy probabilities are data sources not 3-day XAU forecasts; local Gold Bullion/iSagha technical/macro/fair-value gap vs EgyptGoldPrice/3omlat derived or median local reference prices. No fictional external 35/30 weights were assigned.

**Critical Egyptian source-definition warning:** iSagha published different within-day Nov 23 21K readings (EGP 5,635 and later EGP 5,750), plus a Nov 22 comparator EGP 5,565, while original R01 froze a different-source Nov 22 EGP 5,505. Preserve all with source-vintage/observation-time difference; do not retroactively amend R01. Treat aggregator/calculated price differently from actual dealer ask/bid and avoid invented premium or double-counting spread.

### Proposed prospective competitor (hypothesis, NOT new empirical weights)
| Feature | Frozen M1 | R03 proposed M2-SHADOW-v0.1 |
|---|---:|---:|
| REAL | 35% | 30% |
| DXY | 30% | 20% |
| MOM | 20% | 25% |
| ETF | 15% | 10% |
| VIX risk proxy | 0% | 15% |

**Reasoning & uncertainty:** Need test if REAL/DXY share information; weekly ETF is delayed for h=3; MOM might capture tactical flow; WGC includes risk dimension missing from M1. Cboe VIX is equity volatility, not gold's own, and positive shock can paradoxically pressure gold in a liquidation. Proposed sign, clipping, 0.013 amplitude, source cutoff/coverage and negative controls are fully written before any result in the source JSON/doc. These are **assistant-proposed heuristic weights**, NOT inferred from WGC/Goldman, NOT fitted, and NOT official or active. No R03 performance evidence exists.

### Decision and next verification
1. **Freeze R01 and M1-v0.1 fully**; retain primary M1-vs-B0 XAU h=3 precommitted 20-slot endpoint. No post-outcome switching.
2. M2 remains research shadow, requires independent protocol/source-vintage/5-session lookback validation, authorized separate implementation and future holdout. If it ever wins, post-selection evidence alone is insufficient to prove learning.
3. Correct local monitoring source classification: DERIVED_REFERENCE vs MULTI_VENDOR_MEDIAN vs DEALER_ASK_BID vs EXECUTABLE, and record observations/publication timestamps and same-vendor quotes before local scoring.
4. R02h earlier 26/26 synthetic evidence remains bounded; R02 official = MISSING, LAB = PARTIAL_READINESS, LEARNING_PROVEN = false until actual field evidence. Do not use this R03 source documentation to assert market outcome or readiness.
5. SEMER can source-review this add-only branch and decide a safe PR/integration path under main protections; no automatic claim of seat ACK or independent MAAT review.

**Original experience candidate:** Public analyst factor mentions/long-term targets/technical signal averages are not publishable short-horizon predictor coefficients. Preserve comparison by target/horizon/provenance rather than creating pseudo-scientific 'industry weights'. This correction changed our decision from overwriting M1 to pinning M2 as candidate-only and isolating Egyptian quote classes. SESSION_DERIVED / NON_CANONICAL / REQUIRES VALIDATION.

**WHAT SUCCEEDED:** Platform-method catalogue, concrete source contrast, transparent candidate weight rationale, JSON/readback. **NOT YET VERIFIED:** any empirical gain, live forecast, vendor archives, or independent model preflight.