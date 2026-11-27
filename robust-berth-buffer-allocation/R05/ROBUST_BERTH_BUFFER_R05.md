# R05 — Recovering the buffer vector from circulation potentials

**Status:** DERIVED / BOUNDED CERTIFICATE / SESSION-DERIVED / NON-CANONICAL. **Originality:** UNRESOLVED; no new algorithm or novelty claim. No field data or human specialist review.

## Question

R04's maximum-cost circulation certifies the optimum value and an interval-packing witness. Can one recover an actual optimal buffer vector from the same uncapped-interval network's residual node potentials, then check it independently against the primal problem?

## Inherited model

Use R02's positive endpoint-specific interval demands (w_{j,i}=A_j+\sum_{k=j}^{i}B_k-H_i>0), after first checking (A_i+B_i\le H_i) for every vessel. The primal is

\[
\min \sum_{k=2}^n c_k g_k\quad\text{s.t.}\quad \sum_{k=j+1}^{i}g_k\ge w_{j,i},\quad g_k\ge0,
\]

with nonnegative gap prices (c_k\). R03's dual is interval packing: maximize \(\sum w_{j,i}y_{j,i}\), with each gap load at most \(c_k\). R04 represents each interval as an uncapped forward arc \(j\to i\) of profit \(w_{j,i}\), and each gap as a backward arc \(k\to k-1\) of capacity \(c_k\) and zero profit. Flow conservation equates gap flow and interval load.

## Recovery theorem

Let \(P_1,\ldots,P_n\) be optimal max-cost-circulation node potentials under the convention that every residual arc \(u\to v\) of profit \(p\) satisfies \(P_v-P_u\ge p\). Define

\[
g_k=\max(0,P_k-P_{k-1}),\qquad k=2,\ldots,n.
\]

Every uncapped interval arc has forward residual capacity, so \(P_i-P_j\ge w_{j,i}\). Summing positive parts of adjacent potential differences telescopes to at least the net difference:

\[
\sum_{k=j+1}^{i}\max(0,P_k-P_{k-1})\ge P_i-P_j\ge w_{j,i}.
\]

Thus the recovered vector is primal feasible. For a gap arc, if its capacity is not tight, its forward residual edge forces \(P_{k-1}\ge P_k\), so \(g_k=0\). If \(g_k>0\), the reverse residual edge implies the gap arc is saturated. For every interval with positive flow, its reverse residual edge makes the interval potential inequality tight. These complementary-slackness conditions make the recovered primal objective equal the circulation optimum. A direct proof is given by the same LP duality; the potentials are not interpreted as buffer amounts themselves.

The extraction depends on **uncapped** interval arcs. Adding finite redundant interval upper bounds adds dual variables; raw node potentials alone then need not recover the primal objective. It also depends on the stated sign convention. Always verify the extracted vector against the original interval constraints and objective.

## Exact bounded certificate

`probe.py` implements integer-scaled negative-cycle cancellation on the uncapped-interval circulation, computes residual shortest-path potentials, extracts the gap vector, and independently enumerates the primal placements and dual packings. All arithmetic is integer exact; the rational family is represented on a common denominator-six grid.

- Integer witness: one demand \(w_{1,3}=3\), costs \((c_2,c_3)=(1,10)\); recovered \((g_2,g_3)=(3,0)\), objective 3.
- Rational witness: demand \(1/3\), costs \((1/3,2/3)\); recovered \((g_2,g_3)=(1/3,0)\), objective \(1/9\).
- 36 deterministic integer instances and 36 sixth-grid rational instances, each for \(n=2,3,4\), were checked. The program compares the flow value, extracted primal objective, brute-force primal optimum, and brute-force dual optimum; every original interval constraint and capacity is asserted.
- Exact enumeration totals and all assertions are printed by the script. These small cases test implementation and sign/index conventions; the written duality proof supports the general statement.

This negative-cycle-canceling prototype is not claimed to be polynomial or production-ready. No field data, random-sampling inference, or operational recommendation is present.

## Recorded failure and correction

The first local check stored gap variables in a node-indexed list with a leading dummy zero, then compared it to a gap-indexed witness. The computed objective was correct, but the witness assertion failed on representation: output `[0,3,0]` versus the same (g_2=3,g_3=0) vector in the expected two-gap convention. The probe now stores gaps in order (g_2,\ldots,g_n) and checks the original constraints. This was an indexing/test failure, not a counterexample to R04 or this recovery claim.

## Prior-work and scope boundary

Residual node potentials and complementary slackness are standard network-optimization tools. R04's focused literature note already establishes weighted interval flow and weighted time-buffer scheduling as prior work. R05 applies the ordinary network dual to recover a primal vector in this specific model; it claims no new flow algorithm, theorem of general scope, or originality. Whether the berth specialization is already published remains unresolved; see the inherited [literature note](../R04/LITERATURE_NOTE.md).

The model remains one berth, fixed vessel order, bounded rectangular arrival/handling uncertainty, endpoint-specific delay caps, and nonnegative linear gap prices. Berth assignment, sequence choice, stochastic recourse, nonlinear costs, and operational data remain outside scope.

## Review and provenance

Horus participation is an internal analytical-agent review requested for this exact candidate head; it is not a separately opened provider conversation and has no independent provider session ID. Session/task identifiers are `UNKNOWN/UNREGISTERED` where the platform did not expose them. No human peer review is claimed. Any review disposition must be appended with the exact reviewed head before merge.
