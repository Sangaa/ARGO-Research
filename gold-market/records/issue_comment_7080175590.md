## ARGO GOLD LAB — 2026-11-22 R02 preregistered methodology / evidence checkpoint

**STATUS:** SESSION-DERIVED / NON-CANONICAL / PROSPECTIVE EXPERIMENTAL DESIGN / **NO R02 FORECAST ISSUED YET**. R01 P001–P004 and the original benchmark remain **IMMUTABLE**.

**Source-of-truth engineering record (commit pinned):** [R02 model, weights, FX/premium decomposition, release-date discipline, failures and per-session protocol](https://github.com/Sangaa/ARGO-KOP/blob/56d7cfef144dc4c9aed771bf4ee32d75941faa98/Research/ARGO_GOLD_LAB/R02_2026-11-22_PROSPECTIVE_MODEL_REGISTER.md). Branch: `argo/gold-lab-methodology-r02-20261122`; commit: `56d7cfef144dc4c9aed771bf4ee32d75941faa98`. Branch-only, **NOT on main**. No PR/Actions initiated.

### CORRECTION-R01-ATTRIBUTION-001
The original R01 forecast points are frozen and have documented sources, but no deterministic predictive function or coefficient-by-feature snapshot was frozen alongside them. Consequently R01 may be scored by numerical error against B0, **not** retroactively attributed to new weights or claimed causal learning. Preserve this failed methodological assumption, do not manufacture R01 feature importance.

### Frozen R02 hypothesis for the *next* fully-sourced issuance
For a new 3/10-trading-session forecast, M1-v0.1 uses feature scores clipped to [-1,+1], with preregistered **experimental** score weights (not observed causal shares):
| Feature | Prior weight | Score sign and scale | Mechanism; falsifier |
|---|---:|---|---|
| 5-session change 10Y TIPS real yield | 35% | minus delta/20 basis points | Opportunity cost; invalidate with out-of-sample ablation |
| 5-session DXY % change | 30% | minus return/1.5% | USD-priced gold pressure; ablation tests utility |
| 5-session XAU % momentum | 20% | plus return/4% | Trend persistence; reversal regimes can fail |
| Latest released weekly physical-gold ETF flow (t) | 15% | plus flow/40 tonnes | Investment demand; lagged flow may mislead |

`S=0.35*s_REAL+0.30*s_DXY+0.20*s_MOM+0.15*s_ETF`; `XAU_hat(h)=XAU_t*exp(0.013*sqrt(h/3)*S)` for h=3/10 sessions. All inputs must be public **before forecast cutoff**; unavailable feature is logged MISSING, not filled retrospectively; partial-data calculation is only a flagged shadow forecast.

For Egypt 21k, record a consistent **seller ask**, FX quote and implicit premium q: `EGP21=(XAU/31.1034768)*0.875*USD_EGP*(1+q)`. Forecast and error are decomposed across XAU, FX and q; bank selling quote type, source and released_at must be recorded. Local political/debt and foreign-currency events are time-stamped and studied through observable FX transmission, **not assumed to raise gold automatically**.

### Wider user-origin hypotheses monitored separately
H-PAPER (allocated vs unallocated/tokenized backing/redeemability), H-CHINA (PBoC/consumer flow and concentration), H-SYNTH (actual elemental Au at commercially relevant tonnage vs imitations/recycling), H-USD, H-EGYPT-FINANCE, H-GEOPOLITICS/Suez/shipping/energy. They have data proxies and explicit disconfirmation tests in the attached source record. **No fictional percentage weights** are assigned until an M2 is prospectively specified and evaluated.

**New Egyptian evidence tracked:** World Bank USD1bn phase-II financing agreement signed 2026-11-01 ([official](https://sis.gov.eg/en/media-center/news/fm-signs-1-billion-financing-agreement-with-world-bank/)). IMF ~USD2.3bn staff-level review agreement announced 2026-11-18, **subject to Board approval**, not proved disbursed ([Reuters](https://www.reuters.com/world/africa/imf-reaches-agreement-with-egypt-unlock-23-billion-funds-2026-11-18/)). Separate World Bank vs IMF and signed vs approved vs paid vs repayment dates.

### Mandatory checkpoint output
Session identity (self-claimed or verified), timestamp Cairo+UTC, cutoff and data vintages, exact vendor XAU/FX/local ask-buy, all feature raw values and score contributions, weights/model version, B0, new immutable forecast, outcomes for forecasts due, USD/EGP/21k errors, error decomposition, **WHAT_SUCCEEDED / EVIDENCE / WHY** and **WHAT_FAILED / EVIDENCE / WHY**, missingness, prospective correction diff, next date, original experience candidate and independent validation status. Same-target B0 comparison; require enough genuinely forward out-of-sample cases before any learning claim.

**Original experience candidate:** R01 provenance/attribution defect discovered by owner correction and live issue inspection. Assistant proposes R02 precommitment. Not promoted; no claim of independent testing or actual model weight updates.