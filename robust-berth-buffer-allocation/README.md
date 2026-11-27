# Robust berth buffer allocation | تخصيص هوامش الأرصفة تحت عدم اليقين

Independent operations-research lane. This is not a continuation of Pascal/Singmaster, polygon walks, or another existing ARGO research round. It reuses only general methodological experience: state the uncertainty set, derive the worst case, preserve counterexamples, and separate guarantees from statistical claims.

## R01 question

For a fixed sequence of vessels using one berth, with bounded late arrivals and handling overruns, what is the minimum total idle buffer between vessels that guarantees every departure delay is at most a target H under every allowed realization? The precise scope and recurrence are in [R01](R01/ROBUST_BERTH_BUFFER_R01.md).

## Current result and status

In this bounded model, worst-case delays have an exact max-plus expression. R01's common-cap placement becomes a longest-path problem. R03 formulates nonuniform gap prices as an interval-covering LP; R04 maps its dual to a maximum-cost circulation with n nodes and O(n²) arcs. The standard-library R04 certificate compares 144 small integer cases with direct primal and dual enumeration and keeps a reversed-orientation negative control. These are bounded checks; the general correspondence rests on the written proof.

This is a derived special-case formulation and computational check, not a novelty claim, peer-reviewed result, or operational recommendation. Robust scheduling and berth-buffer insertion are established areas; see [literature review](LITERATURE_REVIEW.md). Literature search is preliminary; broader review remains open.

## Rounds

- [R01 — common delay cap](R01/ROBUST_BERTH_BUFFER_R01.md): exact minimum total buffer under a common cap.
- [R02 — vessel-specific caps](R02/ROBUST_BERTH_BUFFER_R02.md): longest-path solution when each vessel has its own delay cap; a tighter cap can force more buffer upstream.
- [R03 — nonuniform gap costs](R03/ROBUST_BERTH_BUFFER_R03.md): the R02 unit-cost placement can be suboptimal under nonuniform prices; gives an interval-covering LP, dual, and an integrality result for integer demands.
- [R04 — exact circulation reduction](R04/ROBUST_BERTH_BUFFER_R04.md): maps the R03 interval-packing dual to maximum-cost circulation, preserving arbitrary nonnegative gap capacities.\n- [R05 — primal recovery from potentials](R05/ROBUST_BERTH_BUFFER_R05.md): extracts the actual optimal gap vector, then checks its objective against the flow value and direct primal/dual enumeration on bounded exact instances.

## Evidence and resumption

- [Derivation and limits](R01/ROBUST_BERTH_BUFFER_R01.md)
- [Executable certificate](R01/probe.py)
- [Captured stdout](R01/probe.log)
- [Literature review](LITERATURE_REVIEW.md)
- [R01 retrieved experience and use log](EXPERIENCE_REUSE.md)
- [R02 certificate](R02/probe.py) and [stdout](R02/probe.log)
- [R02 literature note](R02/LITERATURE_NOTE.md) and [experience reuse](R02/EXPERIENCE_REUSE.md)
- [R03 certificate](R03/probe.py), [stdout](R03/probe.log), [development correction](R03/DEVELOPMENT_LOG.md), [literature note](R03/LITERATURE_NOTE.md), and [experience reuse](R03/EXPERIENCE_REUSE.md)
- [R04 certificate](R04/probe.py), [stdout](R04/probe.log), [development/checkpoint log](R04/DEVELOPMENT_LOG.md), [literature note](R04/LITERATURE_NOTE.md), and [experience reuse](R04/EXPERIENCE_REUSE.md)\n- [R05 certificate](R05/probe.py), [stdout](R05/probe.log), [development/error log](R05/DEVELOPMENT_LOG.md), [literature note](R05/LITERATURE_NOTE.md), and [experience reuse](R05/EXPERIENCE_REUSE.md)

Status: SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION. No field data were used.

