# Literature note — interval circulation reduction

Search date: 2026-11-27. Focused search only; not an exhaustive survey.

- Arkin & Silverberg (1987), [“Scheduling jobs with fixed start and end times”](https://doi.org/10.1016/0166-218X(87)90037-0), reduce weighted interval scheduling on identical machines to minimum-cost flow and give a polynomial-time algorithm. This establishes that flow reductions for weighted interval packing/scheduling are not new. Their standard fixed machine-count setting is not identical to R04's arbitrary gap capacities and R02-derived interval demands.
- Briskorn, Leung & Pinedo (2011), [“Robust scheduling on a single machine using time buffers”](https://doi.org/10.1080/0740817X.2010.505123), explicitly studies weighted buffer times. Weighted-buffer optimization itself is established.
- Agra & Rodrigues (2022), [“Distributionally robust optimization for the berth allocation problem under uncertainty”](https://doi.org/10.1016/j.trb.2022.07.009), studies berth allocation under uncertain handling times and vessel delay limits. It is a richer allocation/recourse model than R04's fixed sequence.

The focused search did not resolve whether the specific variable-gap-capacity circulation reduction in R04, paired with R02's endpoint-specific rectangular uncertainty demands, is already stated in the berth literature. This is not evidence of novelty. No originality claim is made; broader review and formulation-level comparison remain open.
