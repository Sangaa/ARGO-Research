# R06 — When does the departure queue block the berth?

**Status:** DERIVED / SMALL DETERMINISTIC PROBE / SESSION-DERIVED / NON-CANONICAL. **Originality:** UNRESOLVED; no novelty claim. No port data or operating rule was supplied.

## Why this round opened

Owner feedback identified missing model boundaries: weather, port or canal sailing instructions, convoy order, route width/capacity, and ambiguity about whether “departure” means clearing the berth, reaching a waiting place, entering/passing a channel, or leaving port.

This feedback changes the interpretation of R01–R05. In R01, the quantity called departure delay is D_i=C_i-(s_i+p_i), where C_i is completion of handling. It does **not** represent berth clearance, channel entry, arrival at an anchorage, or port exit. R06 clarifies this scope without rewriting the frozen earlier records.

## Question

When can a fixed-order berth-buffer calculation be done independently of outbound channel scheduling, and when does waiting for a convoy/channel slot hold the berth and delay the next vessel?

## Minimal two-stage model

For vessel i, let S_i be handling start, C_i=S_i+p_i handling completion, R_i physical release of the berth, and X_i entry into an outbound channel slot. Let g_i >= 0 be a planned gap, a_i the ready time, p_i handling duration, tau_i an earliest assigned channel slot, and h a fixed separation between channel entries. In this intentionally small ordered-channel illustration,

    S_i = max(a_i, R_(i-1) + g_i)
    C_i = S_i + p_i
    X_i = max(C_i, tau_i, X_(i-1) + h)

The physical release rule is the key distinction:

- **A — clear berth, wait elsewhere:** R_i=C_i. If an independent holding area can accept every vessel and no shared pilot, tug, maneuvering, or other constraint feeds back into berth service, the berth schedule is independent of channel slots. Channel times can be calculated afterward for a berth-only objective. A total port-exit objective or deadline still needs the channel stage.
- **B — berth remains occupied until channel slot:** R_i=X_i. Then X_i determines when vessel i+1 can start; the berth and channel queues are coupled.

These cases are alternatives, not claims about any named port. If a vessel clears the berth but waits at a limited anchorage, or needs a shared tug/pilot to clear, neither simplified case alone is sufficient; the holding and maneuvering resources need explicit constraints.

## Exact two-vessel counterexample

Set two vessels in fixed service order; a_1=a_2=0, p_1=p_2=1, g_2=0, channel earliest slots tau_1=10,tau_2=0, headway h=1, and require the second vessel to complete handling by time 3.

The probe computes:

| Assumption | Handling completion C_1,C_2 | Berth release R_1,R_2 | Channel entry X_1,X_2 | C_2 <= 3? |
|---|---|---|---|---|
| A: clear berth, hold elsewhere | 1, 2 | 1, 2 | 10, 11 | Yes |
| B: remain on berth for slot | 1, 11 | 10, 11 | 10, 11 | No |

The same channel slots produce different berth completion schedules solely because the physical holding rule differs. This is a deterministic model counterexample, not an observation of port practice.

Run python3 -I probe.py; the captured output is in [probe.log](probe.log). It prints the two cases; it is not a statistical study or an exhaustive test of port schedules.

## Weather, convoy, and route capacity

R01's independent rectangular arrival/handling bounds do not encode a common weather event. Weather could change handling duration and channel availability together; representing that requires a stated scenario set or another justified joint uncertainty model. Likewise, a fixed channel headway h is only a placeholder: direction changes, convoy windows, vessel dimensions, draft/tide limits, closures, and channel geometry can produce sequence- and vessel-dependent feasibility. None is inferred here.

The event chain must be specified before applying a result:

1. handling complete C_i;
2. berth physically clear R_i;
3. channel entry X_i;
4. arrival at a designated waiting location or passage beyond a stated port boundary.

“Departure” should name one of these events in future models.

## Literature check and originality boundary

A focused publisher search found established integrated berth/channel scheduling:

- Corry and Bierwirth (2019), [The Berth Allocation Problem with Channel Restrictions](https://doi.org/10.1287/trsc.2018.0865), jointly schedules channel movements and berth allocation/sequencing, including direction and tidal constraints.
- Liu, Li and Wang (2022), [A two-stage stochastic programming model for seaport berth and channel planning with uncertainties in ship arrival and handling times](https://doi.org/10.1016/j.tre.2022.102919), integrates berth decisions with channel lane, tug, and vessel-sequencing decisions under arrival/handling uncertainty.
- Zhao et al. (2025), [Robust vessel traffic scheduling with uncertain Berth Service Times in a Seaport](https://doi.org/10.1016/j.trb.2025.103294), includes tidal windows, channel capacity, and uncertain berth service times.

Only publisher abstracts/metadata were reviewed in this round, not full texts. Broad berth/channel integration is established; this R06 boundary exercise makes no novelty claim. Whether any narrower formulation is new remains unresolved and would require full literature comparison.

## Review, reuse, and next boundary

HORUS reviewed the two-stage distinction and the two-vessel arithmetic as an **internal analytical agent**. There was no standalone provider conversation or provider-issued session ID. This is model-side analysis, not human peer review.

The next domain input needed is the physical release rule: after handling, can a vessel clear the berth to an available holding place while awaiting its assigned channel/convoy movement, or does it occupy the berth until that movement is permitted? The answer is port-specific and is not assumed by this record.
