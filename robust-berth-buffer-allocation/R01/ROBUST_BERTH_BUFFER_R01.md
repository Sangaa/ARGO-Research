# R01 — Minimum total berth buffer for a fixed sequence under bounded delay

**Status:** DERIVED / SOURCE-ONLY / NON-CANONICAL. **Originality:** UNRESOLVED. No field data; no human specialist review.

## Question and scope

For a fixed vessel sequence on one berth, how should nonnegative idle gaps be placed to minimize their sum while guaranteeing each departure delay is at most H for every allowed combination of vessel lateness and handling-time overrun?

Assumptions: one berth; fixed order and no overtaking; no reassignment; independent rectangular uncertainty `0 <= a_i <= A_i`, `0 <= u_i <= B_i`; no contractual time windows that prevent baseline retiming; same relative uncertainty bounds after retiming. This is a deliberately restricted mathematical model, not a port operating plan.

## Model

Let `p_i` be baseline handling duration, `s_i` planned start, and `g_i = s_i - (s_(i-1)+p_(i-1)) >= 0` the idle gap before vessel i, with `g_1=0`. Actual completion obeys `C_i = max(s_i+a_i, C_(i-1)) + p_i + u_i`. Departure delay is `D_i=C_i-(s_i+p_i)`, so `D_1=a_1+u_1` and `D_i=max(a_i,D_(i-1)-g_i)+u_i`.

## Derivation

Taking the worst case over the independent bounds and unrolling the recurrence gives

`D_i* = max_(1<=j<=i) [ A_j + sum_(k=j..i) B_k - sum_(k=j+1..i) g_k ]`.

Therefore `D_i* <= H` exactly when each same-index term satisfies `A_i+B_i<=H`, and for every `j<i`,

`sum_(k=j+1..i) g_k >= A_j + sum_(k=j..i) B_k - H`.

Let `G_i=sum_(k=2..i)g_k`, `G_1=0`. Each condition is `G_i-G_j >= w_(j,i)`, together with monotonicity `G_i-G_(i-1)>=0`. The least feasible prefixes are longest-path distances in the forward DAG with zero-weight edges `(i-1)->i` and edge `j->i` of weight `w_(j,i)` when positive. Then `g_i=G_i-G_(i-1)` and the minimum total buffer is `G_n`. There are O(n²) possible edges.

This is a standard difference-constraint / longest-path construction applied to this stated recurrence. No claim is made that the graph algorithm is new.

## Negative result and certificate

For A=[0,0,0], B=[5,2,0], H=5, putting gaps [0,2,0] gives worst delays [5,5,5]. The same total buffer misplaced as [0,0,2] gives [5,7,5]. Thus total slack alone does not certify the target; placement matters.

`probe.py` independently enumerates 2,430 small integer model instances and compares the graph solution to brute-force feasible placements within the stated finite search bound. Its stdout records the actual counts. The check supports the implementation on that finite domain; it does not prove the recurrence or cover real port operations.

## Limits / next checks

- Derivation assumes independent rectangular uncertainty; correlations or shared weather/resource effects change the uncertainty set.
- A common H is used; vessel-specific caps can be represented by replacing H at the relevant endpoint, but that extension is not certified here.
- No service windows, berth assignment choice, crane coupling, stochastic objective, cost heterogeneity or regulatory constraints are modeled.
- Full literature review and domain-specialist review are required before any originality or operational claim.
