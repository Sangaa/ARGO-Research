# R02 — Minimum buffer with vessel-specific delay caps

**Status:** DERIVED / SOURCE-ONLY / NON-CANONICAL. **Originality:** UNRESOLVED. No field data; no human specialist review.

## Question

R01 treated every vessel with one common worst-case departure-delay cap H. What changes if a fixed one-berth sequence has a different cap H_i for each vessel, while the arrival/overrun bounds, fixed-order recurrence, and unit cost per idle minute remain as in R01?

The motivating distinction is operational: the same upstream disruption may be acceptable for one vessel and unacceptable for another. This is a model extension within the new berth-buffer project, not a continuation of Pascal, Singmaster, or polygon-walk research.

## Model and result

Keep R01 notation and recurrence:

`D_1=A_1+B_1`, `D_i=max(A_i,D_(i-1)-g_i)+B_i`, with `g_1=0`, `g_i>=0`.

For each vessel i, require its worst-case delay to satisfy its own cap H_i. Unrolling the recurrence gives

`D_i* = max_(1<=j<=i) [ A_j + sum_(k=j..i) B_k - sum_(k=j+1..i) g_k ]`.

Therefore feasibility is equivalent to:

- `A_i+B_i<=H_i` for every i; if this fails, no buffer placement can repair the vessel's own arrival-plus-handling delay.
- For every `j<i`, `sum_(k=j+1..i) g_k >= A_j+sum_(k=j..i)B_k-H_i`.

Define `G_i=sum_(k=2..i)g_k`, `G_1=0`. The second conditions are forward difference constraints `G_i-G_j>=w_(j,i)`, with adjacent zero-weight edges enforcing nondecreasing prefixes. The componentwise least feasible prefixes are longest-path distances in this DAG. Thus the minimum total buffer under unit cost is `G_n`, and each gap is `g_i=G_i-G_(i-1)`. Complexity is O(n²).

This is an exact extension of R01's derivation to endpoint-specific caps. The graph method is standard; no algorithmic novelty is claimed.

## Discriminating example

For `A=[0,0,0]`, `B=[5,2,0]`:

- With common caps `[5,5,5]`, minimum gaps are `[0,2,0]`, total 2, and worst delays `[5,5,5]`.
- With vessel-specific caps `[5,4,3]`, minimum gaps become `[0,3,1]`, total 4, and worst delays `[5,4,3]`.

The tighter caps on later vessels force buffer to be placed before them; a single common cap would understate the necessary total and put it in the wrong gaps.

## Certificate and limits

`probe.py` checks the hand example, an immediately infeasible first-vessel case, the interval formula against the recurrence, and 6,156 exhaustive small integer instances against brute-force gap placements. Generated instances have n=2 or 3, A_i and B_i in `{0,1,2}`, and each feasible H_i is either the local minimum `A_i+B_i` or one larger. The brute-force search bound is explicit in the script. This is finite implementation evidence only; the general result rests on the unrolled recurrence and longest-path argument.

No changing vessel order, multiple berths, service windows, uncertain/correlated bounds, non-unit buffer costs, cranes, channel windows, or stochastic objectives are modeled. Weighted buffer costs are left as a distinct open problem rather than treated as if the longest-path solution still optimized them.

No originality, operational-validity, or field-performance claim. See the preliminary literature review.
