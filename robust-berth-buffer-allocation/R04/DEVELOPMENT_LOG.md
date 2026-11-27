# R04 development and checkpoint log

## Search and implementation

The key modeling risk was the direction of the time arcs. Forward interval arcs must be paired with backward gap arcs so that circulation conservation makes the backward flow equal the number/amount of selected intervals crossing that gap. A deliberate reversed-gap negative control returned value 0 instead of the R03 witness value 3; it is preserved in `probe.log` and asserted in `probe.py`.

No failed R04 solver execution has occurred in the recorded run. The negative control is a falsifier for a wrong network orientation, not a failed run of the correct model.

## First-person experience candidate

I reused R03's warning that objective changes invalidate optimality transfer, then mapped its interval-packing dual into a circulation. I initially treated edge orientation as the central implementation hazard, so I retained a reversed-direction control instead of reporting only successful flow instances. The control's mismatch changed the certificate: orientation now has an explicit negative assertion. This is a session-derived candidate, not a validated default practice.

## Entry/checkpoint provenance

- `SESSION_ID=UNKNOWN/UNREGISTERED`; no authenticated provider conversation ID or prior registered per-chat ID was exposed in this runtime.
- `SEAT_ID`: user-addressed “TOTO” research collaborator; not verified as a formal KOP role/seat.
- `TASK_ID`: user-directed continuation of the independent berth-buffer research; no separate registered task ID was supplied.
- Authorization: the user's explicit “كملوا” continues the previously directed research and repository documentation task. KOP `PROJECT_REENTRY_STATE.md` says no automatic next; this user instruction is the explicit continuation.
- Latest inspected ARGO-KOP main at re-entry: `3b3597f3e9ccc5eff32c0a3d67636053858f7b9e`; it authorizes THOTH's free scientific research lane as non-mutating by default, but does not establish TOTO as a formal seat or grant governance authority.
- Latest inspected ARGO-Research main before R04 work: `9f725a25867b39a4dfdf0a75b9cda523db9318d5`, which includes R03 merge `6bb3a345f4ee0ebadd1062a952953127bd68e9a8` and an unrelated polygon R24 merge. No open berth-buffer PR or R04 branch was found in the bounded GitHub check.
- `MEMORY_DELTA=PRESENT` planned: add an immutable SOURCE_ONLY R04 experience card after research source is merged and pinned. No promotion to canonical knowledge or claim of model-weight learning.
- Next action: internal HORUS review, corrections if needed, merge/read back Research R04, then add and read back its Library card. This checkpoint is a draft until the review and source merges close.


## CHECKPOINT — 2026-11-27 18:xx UTC

- `SESSION_ID=UNKNOWN/UNREGISTERED`; no authenticated provider conversation ID is exposed.
- `TASK_ID=USER-DIRECTED CONTINUATION; separately registered ID unavailable`.
- Current work ref: `PR #39`, branch `toto/robust-berth-r04-flow-reduction-20261127`, review pending.
- Last source evidence: `ARGO-Research branch head a67088e51c38baac9f25988d6258051fad387c1d`; R04 certificate stdout has 144 deterministic instances, 6,266 primal placements, 8,005 dual packings, flow and orientation assertions passing. This is bounded execution evidence, not a proof of the general mapping.
- Experience used: R03 SOURCE_ONLY Library card `robust-berth-weighted-gap-costs-20261127-r03`; its objective-change and dual-feasibility lessons altered the R04 checks.
- `MEMORY_DELTA=PENDING`; R04 card will be written only after the source revision is merged and pinned. R03 card remains SOURCE_ONLY; no canonical promotion or model-weight learning claim.
- Next: await internal HORUS review at exact R04 head; correct bounded findings; merge/read back R04 and then add/read back its Library card.
- This checkpoint is branch-published and remains `SOURCE_ONLY` until merge/readback.


## Append-only correction and checkpoint — 2026-11-27

Correction: the earlier checkpoint heading included the template string `18:xx UTC`, which was not a measured time. Treat its date as 2026-11-27 only; the exact clock time is unavailable. This correction preserves the original mistake rather than presenting the placeholder as a timestamp.

Checkpoint: `SESSION_ID=UNKNOWN/UNREGISTERED`; provider conversation ID unavailable. `TASK_ID` remains the user-directed R04 continuation, with no separately registered identifier. Current ref is PR #39, branch `toto/robust-berth-r04-flow-reduction-20261127`, at pre-correction head `9cedef7c9292d305acbf75bcf0cfc8fa7c178e94`. HORUS returned REVISE at head `a67088e51c38baac9f25988d6258051fad387c1d`; two bounded fixes are being applied: add the R04 derivation to the lane's Rounds route, and state R02's required local feasibility test `A_i+B_i<=H_i`. The certificate remains unchanged and its logged 144 cases passed. R03's SOURCE_ONLY experience card was read and used; R04 Library memory remains pending source merge and pinning. Next: publish the fixes, request exact-head HORUS recheck, then merge/read back Research and Library records. This event is branch-published and remains SOURCE_ONLY.
