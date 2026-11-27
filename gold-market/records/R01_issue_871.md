# ARGO GOLD LAB | R01 frozen baseline (2026-11-22)
**Status:** SESSION-DERIVED / NON-CANONICAL / SOURCE-ONLY / NOT BACKTESTED / REQUIRES VALIDATION
**User intent:** observe the global gold market and Egypt retail market every few days, issue timestamped falsifiable forecasts, assess their errors, preserve failures and evidence, and improve methodology prospectively. This is an independent research experiment, **not** a claim of ARGO knowledge promotion or model-weight training.
**Capital:** EGP 1,000,000 is only a **paper benchmark**. No real purchases are authorized.

## Frozen reference and source identity
- XAU/USD historical daily close **2026-11-20** = **$3,532.87/oz**, Investing.com historical data: https://www.investing.com/currencies/xau-usd-historical-data
- Egypt 21k **2026-11-22 indicative retail ask EGP 5,505/g**, dealer buy EGP 5,405/g, USD/EGP EGP 53.81 according to one aggregator: https://www.egyptgoldprice.com/ar/blog/gold-price-egypt-2026-11-22
- Local vendors differ, including EGP 5,530 quote at https://3omlat.app/gold/gold-21k?range=1w . These are **indicative**, not executable transaction offers.
- Cross-source theoretical local 21k price ~EGP 5,347.98; hybrid-observation implicit premium **2.936%**. Observe different source timestamps.
- XAU 21 recent daily log returns sigma ~1.856%/session; volatile, short historical window, not validated forward.

## Precommitted initial forecasts: DO NOT EDIT / RETROSPECTIVELY REFIT
| ID | Target session | XAU point ($/oz) | Global experimental range | Egypt21 point (EGP/g) | Egypt experimental range |
| --- | --- | ---: | --- | ---: | --- |
| P001 | 2026-11-25 | 3,450 | 3,300–3,760 | 5,376 | 4,900–6,000 |
| P002 | 2026-12-07 | 3,490 | 3,000–4,000 | 5,437 | 4,500–6,500 |
| P003 | 2026-12-22 | 3,550 | 2,800–4,200 | 5,532 | 4,200–7,000 |
| P004 | 2027-02-22 | 3,700 | 2,400–4,700 | 5,765 | 3,800–7,900 |

Egypt point forecasts mechanically assume USD/EGP **53.81** and premium **2.936%** unchanged. The forecast ranges are **uncalibrated exploratory bands**, not probabilistically validated 80% intervals.
If a target date falls on a market holiday, use the next fully traded relevant day and record exact source-as-of.

**Benchmark B0** forecasts XAU $3,532.87 and Egypt21 EGP 5,505 at all horizons. At each target, compute ABS(actual - prediction) vs ABS(actual - B0), separately in $/oz and EGP/g. Record directional hit, interval coverage and whether M1 beats B0 on the same target. No aggregate win/learning declaration until enough out-of-sample results (aim >=20).

## Hypotheses to investigate, not endorse
- **H-PAPER** (user-origin): electronic/tokenised and unallocated gold, custody and backing mismatch. Differentiate *unallocated creditor claims* from physically backed ETFs, and issuer-specific token redemption, audit and bar lists. Source: https://www.lbma.org.uk/publications/the-otc-guide/precious-metal-accounts/ and https://www.gold.org/goldhub/research/digital-gold-market-report . No proven systemic unbacked shortfall.
- **H-CHINA** (user-origin): official/retail purchasing, marginal-market power. PBoC reported +26t October 2026, 2,435t total, 24 monthly additions: https://www.gold.org/goldhub/gold-focus/2026/11/china-gold-market-update-robust-demand-october . *Monopoly not verified*.
- **H-SYNTH** (user-origin): manufactured real Au atoms, substitutes, or fabricated/recycled gold. CERN LHC transmutation produced 29 picograms in Run 2, not commercially material: https://alice-collaboration.web.cern.ch/2025-alice-lead-to-gold . Test actual mass scaling/cost before assigning supply impact.
- **H-USD** (user-origin): currency reserve diversification and possible dollar crisis. IMF 2026Q2 USD reserves share 56.70% vs 57.18% prior quarter: https://data.imf.org/en/news/imf%20data%20brief%20september%2030 . *Not evidence of imminent collapse*.
- **H-EGYPT** (assistant-proposed): local FX, local premium, product manufacturing charges and dealer spread may outweigh international movements.
- World Gold Council Q3 2026: CB net buys 321t, physically backed ETF inflows 211t: https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-q3-2026

## Checkpoint contract (append-only)
For each checkpoint: exact Cairo observation time; global source + completed trading session + spot close; local seller ask/dealer buy quote + local source timestamp; USD/EGP; calculated premium; primary China/ETF/digital/physical supply/real-yield signals; news and alternative explanations; **prior forecast IDs due**, numerical errors and B0 comparison; false assumptions and corrections; new prospectively dated forecasts (R02+) **without changing R01**.

Provisional scenario invalidators: >$3,760 sustained weekly closes weakens short-term bear thesis; <$3,400 sustained weekly closes weakens consolidation thesis; FX >5% away from 53.81 or local premium ±2 pp requires **new prospective Egyptian model**; proven gold delivery/audit problems would elevate H-PAPER; commercial tonne-scale synthetic Au is required for an H-SYNTH supply shock.

**Governance:** no Actions, no repo code changes, no production/knowledge promotion, no claim of independent experimental validation merely from internal self-review. Future auto-checks must cite source date, never rewrite old findings; if sources fail, report MISSING.