# Robust berth buffer allocation | تخصيص هوامش الأرصفة تحت عدم اليقين

Independent operations-research lane. This is not a continuation of Pascal/Singmaster, polygon walks, or another existing ARGO research round. It reuses only general methodological experience: state the uncertainty set, derive the worst case, preserve counterexamples, and separate guarantees from statistical claims.

## R01 question

For a fixed sequence of vessels using one berth, with bounded late arrivals and handling overruns, what is the minimum total idle buffer between vessels that guarantees every departure delay is at most a target H under every allowed realization? The precise scope and recurrence are in [R01](R01/ROBUST_BERTH_BUFFER_R01.md).

## Current result and status

In this bounded model, worst-case delays have an exact max-plus expression. For a common target H, required buffer placement becomes a longest-path problem on a directed acyclic graph and can be solved in O(n²). A three-vessel example shows that equal total slack placed at different positions does not give the same guarantee. A standard-library certificate exhaustively checks 2,430 small integer instances against brute force.

This is a derived special-case formulation and computational check, not a novelty claim, peer-reviewed result, or operational recommendation. Robust scheduling and berth-buffer insertion are established areas; see [literature review](LITERATURE_REVIEW.md). Literature search is preliminary; broader review remains open.

## Rounds

- [R01 — common delay cap](R01/ROBUST_BERTH_BUFFER_R01.md): exact minimum total buffer under a common cap.
- [R02 — vessel-specific caps](R02/ROBUST_BERTH_BUFFER_R02.md): longest-path solution when each vessel has its own delay cap; a tighter cap can force more buffer upstream.
- [R03 — nonuniform gap costs](R03/ROBUST_BERTH_BUFFER_R03.md): R02's unit-cost placement can be weighted-cost suboptimal; interval-covering LP, dual and integer-primal result.

## Evidence and resumption

- [Derivation and limits](R01/ROBUST_BERTH_BUFFER_R01.md)
- [Executable certificate](R01/probe.py)
- [Captured stdout](R01/probe.log)
- [Literature review](LITERATURE_REVIEW.md)
- [R01 retrieved experience and use log](EXPERIENCE_REUSE.md)
- [R02 certificate](R02/probe.py) and [stdout](R02/probe.log)
- [R02 literature note](R02/LITERATURE_NOTE.md) and [experience reuse](R02/EXPERIENCE_REUSE.md)
- [R03 certificate](R03/probe.py), [stdout](R03/probe.log), [development correction](R03/DEVELOPMENT_LOG.md), [literature note](R03/LITERATURE_NOTE.md), and [experience reuse](R03/EXPERIENCE_REUSE.md)

Status: SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION. No field data were used.
