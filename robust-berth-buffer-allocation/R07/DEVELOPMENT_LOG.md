# R07 development and evidence log

Date: 2026-11-27 (Africa/Cairo). Exact work-clock time: not recorded. SESSION_ID=UNKNOWN/UNREGISTERED; no provider-issued session ID was exposed. TASK_ID=USER-DIRECTED CONTINUATION / R07 FINITE HOLDING CAPACITY.

## Input retrieved and use

- Owner-provided analogy, recovered from recent conversation record c379364222: a temporarily empty cup/variable can be used to transfer contents while preserving part of the original. It prompted a precise question about the capacity of an off-berth holding buffer.
- Applied R06's event separation: handling completion, berth release, and channel entry are distinct. R07 measures the effect of finite holding capacity K on those event times.
- The analogy is a question-generating experience, not evidence about a port's actual holding rules.

## Model and measured bounded probe

Three vessels; fixed service order; all ready at time zero; one time unit per handling; first channel entry at T=10; one entry per time unit thereafter; K counts whole vessels that can wait off-berth. A holding slot is freed at channel entry. There is no unmooring/transfer time.

Read exact branch files and ran:

    python3 -I probe.py

Probe blob: 07d088f6d113bb27b18fc29a2096218068e9bb80.
Report blob: 503c3425ddeb3f8686c2047ffc3a7e253f5070c4.
Captured output at probe.log matches the read-back run exactly (exit 0).

Observed deterministic cases K=0,1,2,3:
- K=0: starts 0,10,11; handling completions 1,11,12; releases 10,11,12.
- K=1: starts 0,1,10; completions 1,2,11; releases 1,10,11.
- K=2: starts 0,1,2; completions 1,2,3; releases 1,2,10.
- K=3: starts 0,1,2; completions 1,2,3; releases 1,2,3.
All four cases have channel entries 10,11,12.

## Bounded derivation

For N vessels all ready at zero, fixed order, and all ideal no-block handling completions strictly before T, K>=N-1 preserves every handling-completion time; the final completed vessel may still occupy the berth. K>=N is needed and sufficient to clear all N vessels before T when no channel entry occurs before T. This count argument is limited to whole-vessel slots, no transfer time, and the stated deterministic schedule. Exact tie-at-T behavior is excluded by the strict-before-T condition.

HORUS reviewed the event arithmetic and threshold logic as an internal analytical agent. There was no standalone provider conversation or provider-issued session ID. Review is model-side, not human peer review.

## Literature and status

Duan et al. (2026), European Journal of Operational Research 330(1), DOI 10.1016/j.ejor.2025.09.016, explicitly models restricted channel width, tide/hydrology, finite inner anchorage, vessel traffic and berth allocation. Publisher/institutional abstract and metadata were checked, not the full paper. Finite buffer and blocking effects are established concepts; R07 makes no novelty claim.

No field data, actual port rule, policy recommendation, predictive result, or canonical knowledge promotion. The owner-provided analogy remains USER_REPORTED; the numeric schedule remains a deterministic bounded illustration.


## Exact-head review disposition

HORUS returned ACCEPT_BOUNDED for document blob 503c3425ddeb3f8686c2047ffc3a7e253f5070c4 at branch head 4935f1186f155e80f5cdc4b898ad40a754b19afe. The review confirmed the event order, slot-freed-at-entry convention, zero-transfer-time assumption, N=1/K=0 case, strict-before-T threshold scope, and K=0..3 table. HORUS reran the published probe with python3 -I; output matched probe.log byte-for-byte. This was internal analytical-agent review, not a separate provider conversation or human peer review.
