## SEMER source/method review — R03 decision and R02h gate | 2026-11-24 Cairo

**Scope/status:** cloud-only read of R03 at `argo/gold-lab-r03-external-weights-review-20261124@8f7546286385d18d0809293579e0f03ebeacfeaa`, exact `main@35f276b7428ed2b936ac4e8dd35caa4c91fc7ed3`. No PR currently exists for R03. This is a bounded source/method review, not an authenticated independent MAAT review or a performance validation.

### R03 disposition: retain as research-only; no PR or activation
- The comparison correctly separates WGC's historical driver attribution and scenario tools from fixed short-horizon weights. TradingView's disclosed 50:50 is a technical-signal-group aggregation, not economic or causal factor coefficients.
- VIX is an equity-volatility proxy; its sign for gold is context-dependent, including possible liquidation episodes. The R03 rationale is a testable idea, not evidence for the chosen sign.
- The two within-day iSagha 21k readings establish quote/time/source-definition fragility; without exact publication times and a consistent dealer ask/bid convention, they cannot validate an executable Egypt price or overwrite R01's different-source frozen point.
- The proposed M2 vector (30/20/25/10/15), its clipping/scales and 0.013 amplitude are explicit heuristic priors. No cited comparator identifies or validates those values; no forecast or out-of-sample gain was demonstrated.
- Therefore keep M1/R01 frozen, M2 marked NON-ACTIVE, and R03 branch-only. A PR would add no evidence and can trigger repository workflows; the current no-paid-Actions direction leaves no authorized CI route.

### R02h: hold, no write to the branch
- Exact head remains `1e484eb47ea730efa5c075ba15dca983651251ca`; compare with current main is DIVERGED, 32 ahead / 6 behind (merge base `ce0a6e441c71f6ee480d0a9538323113c251366a`). No PR found.
- No current writer/lease ACK is visible. Historical “no active terminal” evidence is not current ownership proof; I did not infer a seat or modify the branch.
- The 26/26 result remains reported branch/lab evidence, not my rerun. R02 is still MISSING / PARTIAL_READINESS / LEARNING_PROVEN=false. Existing source review also leaves the `target_key` negative arm untested and reports non-positive archived prices can be scored by replay. These are synthetic verifier gates, not market-data failures.

**Decision-changing correction:** public method labels and comparator reports do not supply transferable short-horizon coefficient vectors. That rules out claiming M2 was externally derived; it remains a prospective challenger only. No forecast, merge, workflow, device action, or canonical promotion was made.