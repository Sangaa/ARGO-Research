# Literature note — vessel-specific delay caps

Focused search date: 2026-11-27. This is a preliminary check, not an exhaustive review.

A 2022 distributionally robust berth-allocation paper models uncertain handling times and imposes the same maximum-delay upper bound on every vessel (rather than a vessel-specific vector H_i): [Rodrigues et al., *Distributionally robust optimization for the berth allocation problem under uncertainty*, Transportation Research Part B 164 (2022), DOI 10.1016/j.trb.2022.07.009](https://doi.org/10.1016/j.trb.2022.07.009). Earlier work also studies robust berth allocation with arrival-delay/handling-time uncertainty and inserted buffers: [Xu, Chen & Quan (2012), DOI 10.1007/s10479-010-0820-0](https://doi.org/10.1007/s10479-010-0820-0).

This confirms that per-vessel delay limits and robust berth buffers are established modeling ingredients. The present R02 restricts to a fixed order on one berth, rectangular bounds, and unit buffer cost, then derives a closed longest-path expression for the minimum total idle gaps under endpoint-specific caps. The focused search did not establish whether that exact specialization is already in the literature. Novelty is UNRESOLVED; no originality claim is made.

Before any novelty statement, compare the exact recurrence and optimization against the full papers and their references, and search fixed-sequence single-machine robust scheduling and interval-covering formulations.
