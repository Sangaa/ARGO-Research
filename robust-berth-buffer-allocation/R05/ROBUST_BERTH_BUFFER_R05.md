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

Thus the recovered vector is primal feasible. Let \(z_k\) be the flow on gap arc \(k\to k-1\), and put \(\Delta_k=P_k-P_{k-1}\). If \(0\le z_k<c_k\), the forward residual edge gives \(\Delta_k\le0\), hence \(g_k=0\). If \(0<z_k<c_k\), the reverse residual edge also exists, giving \(\Delta_k=0\). If \(z_k=c_k>0\), the reverse residual edge gives \(\Delta_k\ge0\), so \(z_k\Delta_k=c_kg_k\). When \(c_k=0\), necessarily \(z_k=0\); no residual edge is required and both objective terms \(z_k\Delta_k\) and \(c_kg_k\) are zero, even if \(g_k>0\). Thus in every case \(z_k\Delta_k=c_kg_k\). On an interval with positive flow, its forward and reverse residual edges force \(P_i-P_j=w_{j,i}\). Summing potential differences against a circulation cancels at every node, so \(\sum w_{j,i}y_{j,i}=\sum z_k\Delta_k=\sum c_kg_k\). This proves objective equality. The potentials are not interpreted as buffer amounts themselves.

The extraction depends on **uncapped** interval arcs. Adding finite redundant interval upper bounds adds dual variables; raw node potentials alone then need not recover the primal objective. It also depends on the stated sign convention. Always verify the extracted vector against the original interval constraints and objective.

## Exact bounded certificate

`probe.py` implements integer-scaled negative-cycle cancellation on the uncapped-interval circulation, computes residual shortest-path potentials, extracts the gap vector, and independently enumerates the primal placements and dual packings. All arithmetic is integer exact; the rational family is represented on a common denominator-six grid. Scaling demands and prices by the same denominator gives integer numerators. R03 proves the interval constraint matrix is totally unimodular, so an integral optimum exists in the scaled primal; the scaled network likewise has integral capacities and an integral optimal circulation. The enumerations therefore cover each displayed grid optimum, not arbitrary rational inputs.

- Integer witness: one demand \(w_{1,3}=3\), costs \((c_2,c_3)=(1,10)\); recovered \((g_2,g_3)=(3,0)\), objective 3.
- Rational witness: demand \(1/3\), costs \((1/3,2/3)\); recovered \((g_2,g_3)=(1/3,0)\), objective \(1/9\).
- 36 deterministic integer instances and 36 sixth-grid rational instances, each for \(n=2,3,4\), were checked. The program compares the flow value, extracted primal objective, brute-force primal optimum, and brute-force dual optimum; every original interval constraint and capacity is asserted.
- Exact enumeration totals and all assertions are printed by the script. These small cases test implementation and sign/index conventions; the written duality proof supports the general statement.

This negative-cycle-canceling prototype is not claimed to be polynomial or production-ready. No field data, random-sampling inference, or operational recommendation is present.

## Recorded failures and corrections

The first local implementation check used a node-indexed vector with a leading dummy zero, then compared it with a gap-indexed witness. The objective was correct, but the assertion compared `[0,3,0]` with `[3,0]`, two encodings of the same `g_2=3, g_3=0`. The corrected probe stores gaps in order `g_2,...,g_n` and checks the original constraints. This was an indexing/test failure, not a counterexample.

A separate 201-line draft from the scratch workspace used `costs[k-1]` for an `n-1` length gap-price vector; `python3 -I` stopped with `IndexError` before its first witness completed. That exact draft (SHA-256 `90ae9081611601faf1be9569a9d666296fb512d4d3ffab80f6c0a7e909b0aaef`) and traceback are preserved as [failed attempt 01](failed-attempt-01.py) and [captured failure](failed-attempt-01.log). It is distinct from the 144-line candidate `probe.py`, whose exact branch copy passes. The stale draft is retained as failure evidence and is not used as proof or measured output.

## Prior-work and scope boundary

Residual node potentials and complementary slackness are standard network-optimization tools. R04's focused literature note already establishes weighted interval flow and weighted time-buffer scheduling as prior work. R05 applies the ordinary network dual to recover a primal vector in this specific model; it claims no new flow algorithm, theorem of general scope, or originality. Whether the berth specialization is already published remains unresolved; see the inherited [literature note](../R04/LITERATURE_NOTE.md).

The model remains one berth, fixed vessel order, bounded rectangular arrival/handling uncertainty, endpoint-specific delay caps, and nonnegative linear gap prices. Berth assignment, sequence choice, stochastic recourse, nonlinear costs, and operational data remain outside scope.

## Review and provenance

Horus participation is an internal analytical-agent review requested for this exact candidate head; it is not a separately opened provider conversation and has no independent provider session ID. Session/task identifiers are `UNKNOWN/UNREGISTERED` where the platform did not expose them. No human peer review is claimed. Any review disposition must be appended with the exact reviewed head before merge.
