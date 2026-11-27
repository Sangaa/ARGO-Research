## SEMER R02d update | candidate uncertainty replay | 2026-11-23

Continued from R02c on a source-only successor branch `argo/gold-lab-r02d-interval-replay-20261123`, now at `82184a40b5e302f0e932772a2c61b31cd6f2b988`.

- Added a fixed, replayable candidate 95% percentile moving-block interval for exactly 20 paired h=3 loss differences: block length 3, 20,000 replicates, non-circular blocks, seed 20261123, linear quantiles. The cohort rule is now the first 20 preregistered slots, with missing/abstained slots retained and not replaced; fewer than 20 paired outcomes means incomplete/descriptive.
- The interval implementation and cohort check are covered by tests. DESKTOP-F7FF127, Python 3.12.10: **19/19 PASS**. The exact verifier and design were fetched back and matched the tested text; no workflow runs followed the commits.
- The method is explicitly a **candidate only**. The stationary bootstrap reference's asymptotic conditions are not established by a fixed 20-pair/3-observation setting; regime shifts and interval calibration remain unresolved. Independent protocol review must accept or reject the exact algorithm before any official issue.
- Added the citation in the design to Künsch (1989), DOI 10.1214/aos/1176347265. The fixed 09:00 Cairo automation remains readiness-only and no issue slot is selected.

No market data or forecast was created. R02 remains MISSING; PARTIAL_READINESS; LEARNING_PROVEN=false. Main remains `ce0a6e441c71f6ee480d0a9538323113c251366a`; no PR, merge, or hosted Actions run.