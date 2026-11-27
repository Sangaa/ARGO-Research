# R03 — Cost-sensitive buffer placement

**Status:** DERIVED / SOURCE-ONLY / NON-CANONICAL. **Originality:** UNRESOLVED. No field data; no human specialist review.

## Question

R02 minimizes the sum of idle gaps, as if every minute in every gap costs the same. If each gap k has its own nonnegative unit cost c_k, what is the exact optimization problem, and can the R02 longest-path placement still be treated as cost-optimal?

## Exact formulation

Keep R02's endpoint-specific interval demands

`w_(j,i)=A_j+sum_(k=j..i)B_k-H_i`, for `j<i`.

Discard nonpositive demands, since gaps are nonnegative. Let `I` contain the remaining intervals. For each `(j,i)` in I, define `M_((j,i),k)=1` if `j<k<=i`, and 0 otherwise. Then the weighted buffer problem is exactly

`minimize sum_(k=2..n) c_k g_k`

subject to

`sum_(k=j+1..i) g_k >= w_(j,i)` for each `(j,i)` in I, and `g_k>=0`.

In matrix form this is `min c^T g` subject to `M g>=w`, `g>=0`. Its LP dual is

`maximize sum_(j,i in I) w_(j,i)y_(j,i)`

subject to

`sum_((j,i) in I: j<k<=i) y_(j,i) <= c_k` for each gap k, and `y>=0`.

The dual is an interval-packing interpretation: every interval demand has value w, and each gap supplies capacity c_k to the intervals crossing it. Strong duality gives equality of the two optima when the buffer problem is feasible.

Every row of M is a consecutive block of ones, so M is an interval matrix and is totally unimodular. With integer demands w, the weighted primal has an integral optimal gap vector even for nonintegral nonnegative costs c. (If costs are also integral, the dual has an integral optimum as well.) This is a structural LP result, not a proposed specialized fast algorithm.

## Counterexample: the R02 path is not weighted-cost optimal in general

Take `A=[0,0,0]`, `B=[5,0,0]`, caps `H=[5,5,2]`. The only positive interval demand is `g_2+g_3>=3`. R02's least-prefix longest-path rule returns gaps `[0,0,3]` (including g_1=0), which meets the caps but costs 30 when `(c_2,c_3)=(1,10)`.

The weighted optimum is `[0,3,0]`: it costs 3, satisfies all three caps with worst delays `[5,2,2]`, and is optimal because the lone constraint requires at least three units in gaps whose cheapest cost is 1. The dual value `3*y_(1,3)` with `y_(1,3)=1` equals this primal cost, giving a matching lower-bound certificate.

Thus the longest-path solution minimizes total buffer for unit costs, but it does not solve the general weighted-cost problem. The dual / interval-LP formulation replaces it; a specialized algorithm and broader complexity characterization remain open.

## Certificate and limits

`probe.py` checks the R02 placement, the weighted alternative, the actual recurrence delays, the lone interval demand, and equality of the displayed primal and dual costs. It then enumerates integer placements through the stated finite bound for this three-vessel instance. This verifies the counterexample and its tiny LP certificate, not the general total-unimodularity theorem or a general-purpose optimizer.

Assumptions remain R02's fixed order, single berth, rectangular uncertainty, endpoint-specific caps, and no service-window or berth-assignment decisions. Costs are linear per idle minute; fixed setup costs, nonlinear tariffs, or costs dependent on start time are outside this model.

## Next open work

Implement and compare a general exact algorithm for interval covering / its dual on larger schedules; quantify when the R02 longest-path placement remains optimal (e.g. equal costs or dominance conditions); then compare against published weighted-buffer scheduling formulations. No originality or operational-performance claim is made.
