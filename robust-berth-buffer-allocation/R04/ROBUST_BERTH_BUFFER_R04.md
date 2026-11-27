# R04 — Exact min-cost-circulation reduction

**Status:** DERIVED / SOURCE-ONLY / NON-CANONICAL. **Originality:** UNRESOLVED. No field data; no human specialist review.

## Question

R03 writes the weighted buffer problem as an interval-covering LP. Can its dual be represented as a standard network optimization problem, giving an exact algorithmic route for the minimum weighted buffer cost?

## Inherited model

For each positive R02 interval demand

`w_(j,i)=A_j+sum_(k=j..i)B_k-H_i > 0`,

the gap variables satisfy

`sum_(k=j+1..i) g_k >= w_(j,i)`, `g_k>=0`,

and the objective is `min sum_(k=2..n)c_k g_k`, with `c_k>=0`. R03's dual is

`max sum_(j,i) w_(j,i)y_(j,i)`

subject to `sum_(j<k<=i)y_(j,i)<=c_k` for each gap k and `y>=0`.

Intervals with nonpositive demand can be omitted: their dual objective contribution is nonpositive and the dual can choose `y=0`.

## Network construction

Create one node for each prefix position `1,...,n`. For every positive-demand interval `(j,i)`, add a forward arc `j -> i` with profit `w_(j,i)` and no effective upper bound. For every buffer gap `k=2,...,n`, add a backward arc `k -> k-1` with capacity `c_k` and zero profit.

For computation, an interval arc may be assigned the finite redundant capacity `min(c_(j+1),...,c_i)`: every feasible interval flow is already bounded by each gap it crosses.

## Exact correspondence

Let `y_(j,i)` be flow on an interval arc and `z_k` be flow on the backward gap arc. Flow conservation at each prefix node forces

`z_k = sum_(j<k<=i) y_(j,i)`.

Thus the backward-arc capacity constraints are exactly the R03 dual constraints. Conversely, any dual-feasible `y` defines a circulation by setting each `z_k` to its interval load. The circulation profit is exactly `sum w_(j,i)y_(j,i)`. Therefore the maximum-cost circulation value equals the R03 dual optimum, and by strong duality equals the minimum weighted buffer cost.

The network has `n` nodes and at most `n(n-1)/2 + (n-1)` arcs. General min-cost/max-cost circulation algorithms therefore provide an exact polynomial-time solution in the usual rational-input model. This is a reduction to an established algorithmic class, not a new min-cost-flow algorithm or a complexity bound for the prototype script.

For integral gap prices `c_k`, the network capacities are integral, so an integral optimal circulation exists; this recovers the R03 dual-integrality condition. R03's separate interval-matrix argument gives an integral primal gap optimum for integer demands, even when costs are nonintegral.

## Recovering the actual gap vector

The circulation's flow is the dual witness; its objective alone is not a buffer schedule. The min-cost-circulation dual has node potentials and gap-capacity prices. Its interval-arc inequalities require `P_i-P_j >= w_(j,i)`. For each gap, the nonnegative capacity price can be chosen at least `P_k-P_(k-1)`. These prices form a feasible R03 gap vector, and strong duality makes an optimal dual solution an optimal gap vector. Equivalently, solve R03's primal at the circulation's certified optimum value. The prototype certificate below checks objective equality and flow mapping; it does not emit recovered gap vectors from node potentials.

## Bounded certificate

`probe.py` uses only the Python standard library. A negative-cycle-canceling min-cost circulation routine is checked against direct enumeration of both the primal gap placements and dual interval packings on 144 deterministic small integer instances (`n=2,3,4`, demands `0..4`, gap prices `0..3`). It checks node conservation, arc bounds, interval-load mapping, and equality of primal, dual and circulation values. For the R03 witness it obtains value 3. A deliberate negative control that points gap arcs forward obtains 0 and fails to match the witness, showing that edge orientation is material.

The negative-cycle-canceling code is a finite small-instance certificate routine, not a claimed strongly-polynomial implementation. These checks do not prove the correspondence for all instances; that rests on the conservation argument above. The route also relies on standard min-cost-circulation solvability, not a newly implemented production solver.

## Literature boundary and limits

Minimum-cost-flow reductions for weighted interval scheduling on identical machines are established; see Arkin and Silverberg (1987). R03's weighted time buffers are likewise adjacent to established robust scheduling. These precedents make a novelty claim inappropriate. The focused search did not establish whether this exact variable-gap-capacity circulation construction for R02's endpoint-specific robust-delay demands has appeared; originality remains unresolved.

The model still fixes one berth, vessel order, bounded rectangular arrival/handling uncertainty, endpoint-specific caps, and nonnegative linear gap prices. It excludes berth assignment, sequence decisions, stochastic/distributionally robust objectives, recourse, nonlinear costs, and operational data.

## Next work

Have HORUS inspect the circulation sign/orientation proof and primal recovery; compare the exact variable-capacity model with interval scheduling and robust berth literature; then validate an independent implementation that returns both the optimal flow and a primal buffer vector on broader rational instances. Do not describe the prototype's cycle-canceling runtime as polynomial.
