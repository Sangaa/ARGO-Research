# Retrospective round dependency audit: R09–R19

**Audit timing:** completed after the lane move. This is a retrospective source review, not evidence that every dependency was checked before moving the files. The move preserved the historical commits; this audit adds a readable dependency map without rewriting round evidence. Polygon-walk R20 was added after the move and is outside this R09–R19 audit.

| Round | Mathematical premise / dependency | Reuse-only or navigation context | Classification |
|---|---|---|---|
| R09 | Octagonal walk model and exact collision enumeration are established in its own record. | Reads R08/review as context; no Pascal/Singmaster theorem is a mathematical premise. | Self-contained lane entry; retrieval context only. |
| R10 | R09 octagonal geometry and collision setup. | R07 experience card supplies method caution only. | Actual mathematical continuation from R09. |
| R11 | R09 zero-radius result and R10 geometry. | R10 experience card is methodological. | Actual continuation. |
| R12 | R09–R11 model; R10 Pell geometry. | R11 card is experience reuse. | Actual continuation. |
| R13 | R12 lattice/local-limit/envelope; R10 quadratic forms. | R12 card is experience reuse. | Actual continuation. |
| R14 | R13 profile and R12 lattice/norm structure. | R13 card is experience reuse. | Actual continuation. |
| R15 | R14 orbit sum; R12 lattice/norm facts. | R14 card is experience reuse. | Actual continuation. |
| R16 | R15 norm factorization/completeness; R12/R13 local-limit methods. | R14 comparison kernel and R15 card. | Actual continuation with methodological reuse. |
| R17 | R16 two embeddings/local-limit profile; R13 profile. | R16 card is experience reuse; R09's non-transferable symmetry shortcut is a method caution explicitly not used as a premise. | Actual continuation; R09 is contextual caution only. |
| R18 | R16 phase function and local-limit identification. | Reads R17 to avoid repeating a same-field result; R17 is not a proof premise. | Mathematical dependency on R16 only; R17 is reuse/navigation. |
| R19 | Exact moment derivation is self-contained within its specified equal-step regular-polygon family. | R17 motivates an additional observable; R07 is a stability caution. R18 appears in the contemporaneous record because of a round-title collision, not as a mathematical premise. | Independent derivation; contextual/methodological reuse only. |

## Preservation and corrected provenance

The move retained round history and old-path commits. The `R18/REUSE.md` note cites immutable pre-move source commits for R16 and R17; those links are historical provenance, not current-path links. The R09 relative link and R18 heading were corrected in the moved lane; original blobs remain in history.

“HORUS reviewed R18” means an internal analytical collaboration agent participated in this workflow. No standalone ChatGPT conversation was opened and no provider session ID exists for that review. It was model-side analysis, not human peer review or an external-provider session. See `R18/REVIEW_PROVENANCE.md` for the explicit correction.
