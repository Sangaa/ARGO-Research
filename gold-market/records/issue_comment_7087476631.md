## SEMER R02g update | synthetic NOT_FORWARD dry-run | 2026-11-23

Continued on source-only branch `argo/gold-lab-r02g-not-forward-dryrun-20261123`, now at `36ad634d0e17f557eb3d1b13daeddf9516009f68`.

One synthetic end-to-end run now covers clean eligibility; source payload manifests; immutable M1/B0 records; target-linked outcome and paired score replay; missing ETF recorded as MISSING without a forecast; and a revised REAL payload rejected against the old digest while V1 remains readable. On DESKTOP-F7FF127 / Python 3.12.10, the full suite is **25/25 PASS**. Exact source/design/checkpoint readback matches. No workflow runs were created.

This completes the synthetic NOT_FORWARD replay only. There is no historical/vendor replay or market verification. External calendar/release authority, real payload/vintage capture, trusted durable ledger, approved uncertainty method and independent review remain open. R02=MISSING; PARTIAL_READINESS; LEARNING_PROVEN=false; main unchanged; no PR/merge/Actions.