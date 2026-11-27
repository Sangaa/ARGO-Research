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
