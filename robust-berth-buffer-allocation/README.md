# Robust berth buffer allocation | تخصيص هوامش الأرصفة تحت عدم اليقين

Independent operations-research lane. This is not a continuation of Pascal/Singmaster, polygon walks, or another existing ARGO research round. It reuses only general methodological experience: state the uncertainty set, derive the worst case, preserve counterexamples, and separate guarantees from statistical claims.

## R01 question

For a fixed sequence of vessels using one berth, with bounded late arrivals and handling overruns, what is the minimum total idle buffer between vessels that guarantees every departure delay is at most a target H under every allowed realization? The precise scope and recurrence are in [R01](R01/ROBUST_BERTH_BUFFER_R01.md).

## Current result and status

In this bounded model, worst-case delays have an exact max-plus expression. For a common target H, required buffer placement becomes a longest-path problem on a directed acyclic graph and can be solved in O(n²). A three-vessel example shows that equal total slack placed at different positions does not give the same guarantee. A standard-library certificate exhaustively checks 2,430 small integer instances against brute force.

This is a derived special-case formulation and computational check, not a novelty claim, peer-reviewed result, or operational recommendation. Robust scheduling and berth-buffer insertion are established areas; see [literature review](LITERATURE_REVIEW.md). Literature search is preliminary; broader review remains open.

## Evidence and resumption

- [Derivation and limits](R01/ROBUST_BERTH_BUFFER_R01.md)
- [Executable certificate](R01/probe.py)
- [Captured stdout](R01/probe.log)
- [Literature review](LITERATURE_REVIEW.md)
- [Retrieved experience and use log](EXPERIENCE_REUSE.md)

Status: SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION. No field data were used.
