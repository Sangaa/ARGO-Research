## SEMER R02h outcome-identity repair | 2026-11-23

I re-entered from #783/7091133173 and read the full #871/7090219101 report before changing code. The lab was online; no active remote terminal session was listed. I used only `D:\Temp\ARGO_GOLDLAB_OUTCOME_JOIN_20261123`, not a shared checkout.

- Pre-fix probe against R02g blob `8b546f82aee8db56b0e444a6f5778ccc7806236e` demonstrated that an outcome with correct record refs/target but missing `cohort_id`, `issue_slot_id`, and `base_session_id` was accepted and scored `-1.0`.
- Successor branch `argo/gold-lab-r02h-outcome-identity-20261123`, latest commit `1e484eb47ea730efa5c075ba15dca983651251ca`; verifier blob `6a0817b71b543d0af8246c565073b5d6ab5f0dba`.
- Replay now requires all outcome identities (`cohort_id`, `issue_slot_id`, `base_session_id`, `target_key`) to match both forecast records. Migrated the three clean outcome fixtures. Added hash-recomputed negative records for missing cohort and wrong cohort/slot/base; positive clean scoring remains green.
- Lab Python 3.12.10: **26/26 PASS**. Removing the outcome-identity guard caused **4 expected subtest failures**. Exact committed code/design were read back; main stays `ce0a6e441c71f6ee480d0a9538323113c251366a`; zero workflow runs.
- The method repair is synthetic record integrity only. R02=MISSING; PARTIAL_READINESS; LEARNING_PROVEN=false.

CLAUDE's two-interpreter report in #871/7090219101 is preserved as separately attributed evidence; my measurements above are only the lab Python 3.12.10 run.