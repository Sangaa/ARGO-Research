# R07 — A finite holding place sends delay back to the berth

**Status:** DERIVED / SMALL DETERMINISTIC SIMULATION / SESSION-DERIVED / NON-CANONICAL. **Originality:** UNRESOLVED; no novelty claim. No port data or actual port rule was supplied.

## Question

R06 separated two extremes: enough external holding space to clear a vessel from the berth, or no ability to clear until a channel slot. What changes when the external holding area has finite capacity K?

This connects to the owner's analogy of using a temporarily empty cup/variable to transfer contents while preserving the rest. Here the holding area is a temporary buffer between berth service and channel passage. The analogy motivates the capacity question; it is not evidence for the equations.

## Simplified event model

Three vessels are served in fixed order at one berth. All are ready at time 0; each handling duration is 1. Outbound channel entry starts at time T=10 and then allows one vessel per unit time in the same fixed order. Capacity K is the number of completed vessels that can wait off-berth before channel entry.

A vessel leaves the berth at handling completion if a holding space is free. If the holding area is full, it remains on the berth until either a holding space opens or its own channel entry is available. This makes K=0 the no-holding case. The example has no stochasticity, climate, variable vessel size, convoy rule beyond a fixed order, or shared tug/pilot constraint.

## Bounded result

For this three-vessel instance, the exact probe gives:

| Holding capacity K | Handling starts | Handling completions | Berth releases | Channel entries | Third handling complete by 3? |
|---:|---|---|---|---|---|
| 0 | 0, 10, 11 | 1, 11, 12 | 10, 11, 12 | 10, 11, 12 | No |
| 1 | 0, 1, 10 | 1, 2, 11 | 1, 10, 11 | 10, 11, 12 | No |
| 2 | 0, 1, 2 | 1, 2, 3 | 1, 2, 10 | 10, 11, 12 | Yes |
| 3 | 0, 1, 2 | 1, 2, 3 | 1, 2, 3 | 10, 11, 12 | Yes |

Under these assumptions, K=2 is enough to preserve all three **handling completion times**, but the third ship still occupies the berth until time 10. K=3 is required to clear all three vessels from the berth before the first channel entry. Thus the threshold depends on what the objective measures: service completion, berth release, or channel passage.

## General threshold for this restricted family

Suppose N vessels are all ready at time 0, use one berth in fixed order, have positive handling durations p_i, and all unblocked handling would finish before the first outbound channel slot T. If the holding area counts one whole vessel per space and no vessel can enter the channel before T:

- K >= N-1 is sufficient to preserve all N handling-completion times, because only the final vessel can finish while all earlier N-1 ships occupy holding spaces.
- K >= N is necessary and sufficient to clear all N ships from the berth before T, because all N completed ships must be somewhere off the berth while none has yet entered the channel.

The holding slot is freed when the vessel enters the channel, not when it exits. The probe gives zero unmooring/transfer time and processes a slot-freeing entry before a simultaneous blocked-vessel release. For N=1, K=0 preserves the only handling completion and K=1 is needed to clear the berth before T. If a handling completion occurs exactly at T, direct transfer to that slot can change the release-at-T case; the threshold statement assumes strict completion before T.

This threshold is specific to the stated deterministic, fixed-order, unblocked-through-T family. It does not cover uncertain durations crossing T, partial service, heterogeneous vessel footprints, multiple holding areas, channel closures, shared maneuvering resources, or objectives that price channel waiting.

## Interpretation

A temporary buffer can separate two queues only while it has room. When it fills, the downstream channel wait propagates upstream: first it delays berth release, then it delays the next handling start. Increasing K can therefore preserve one performance measure while leaving another delayed.

The 0–3 example is an exact finite calculation, not a field observation, forecast, or port recommendation. Script and captured output: [probe.py](probe.py), [probe.log](probe.log).

## Literature and originality

Finite anchorage capacity, channel width, tide, and integrated berth/traffic decisions are already considered in port-scheduling literature. Duan et al. (2026), [Integrated vessel traffic scheduling and berth allocation with restricted channel widths](https://doi.org/10.1016/j.ejor.2025.09.016), explicitly includes restricted inner-anchorage capacity together with channel-width and hydrological constraints. Only the publisher/institutional abstract and metadata were checked here, not the full paper.

Finite buffers and upstream blocking are established scheduling concepts. R07 makes no originality claim; any narrower contribution would need a full literature comparison and domain review.

## Experience status and next boundary

The empty-cup analogy is owner-provided experience, retained here as a useful question generator: identify the temporary buffer, its capacity, and the exact event that frees a slot. It is not a validated port rule or canonical ARGO knowledge.

For a port-specific model, obtain the actual holding capacity and rule for when a ship can clear the berth. Without those facts, K remains a hypothetical parameter.
