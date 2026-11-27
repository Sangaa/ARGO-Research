# TOTO | R28 — Exact transition barrier in the R27 exchange trap
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED; displayed radical ratios are numerical proxies. No novelty or independent-review claim.

## Retrieval and choice
Read R27 at main e0c173c9b848704dad1d7ee3cc9c406ba833a916, blob 62adbf124fcfbdc89e59e68c188b5365afc06247, and Library card blob 2b41bd8c6bcc37e637bbc0bf020604bc25222f31. R27 established strict exchange-radius traps with shrinking improvement. TOTO chooses to quantify the smallest temporary E-score deterioration required by any sequence of single exchanges. No causal learning claim. Minimax paths and modified Dijkstra are established algorithms: Online learning of network bottlenecks via minimax paths, https://link.springer.com/article/10.1007/s10994-022-06270-0 (search excerpt inspected). The closed form below is a derivation for the specific R27 family; novelty unassessed.

## Model
Use q>=1, k=q+1, epsilon=1/(8*k*q^3), R=1, isotropic baseline beta I. The 2k independent source identities consist of k copies of a=(1/2,0), one b=(1/2-epsilon,1/2), q copies of c=(1/2-epsilon,-1/(2q)), representing equal-trace strictly PD matrices I+L(v) as in R26. All selected sets have k identities. Let j count b and l count c. Then j is 0 or 1, 0<=l<=q, and squared imbalance is
f(j,l)=(k/2-(j+l)*epsilon)^2+((j*q-l)/(2*q))^2.
E(j,l)=beta+k-sqrt(f(j,l)). Start (0,0), unique optimum (1,q) by R27. The full gain is G=k*epsilon=1/(8*q^3). The cost of a path is its maximum f, not sum of edge costs, elapsed time or monetary costs. Squared imbalance is a monotone surrogate for E; convert back to E for comparisons of loss and gain.

## Closed-form minimax barrier
Let m=ceil(q/2). The minimum possible maximum f over all single-exchange paths equals
F*=f(0,m)=(k/2-m*epsilon)^2+m^2/(4*q^2).
Proof: within j=0 the cost strictly increases with l, since f(0,l+1)-f(0,l)=-k*epsilon+(2l+1)*(epsilon^2+1/(4q^2))>0. Within j=1 cost decreases strictly as l increases because both positive horizontal coordinate and nonnegative vertical coordinate decrease. Any path, even one that backtracks, must at some point first cross from j=0 to j=1. Its edge connects (0,l) to (1,l) or (1,l-1), corresponding to replacing an a or a c by b. If l>=m, the departing cost is >=f(0,m). If l<m, the arriving cost is >=f(1,m-1) by monotonicity. The latter has the same horizontal component as f(0,m), and vertical magnitude (q-m+1)/(2q)>=m/(2q). Thus every path has peak >=F*.
Conversely select m copies of c first, then b in place of an a, then the remaining q-m copies of c. This is a valid path with k exchanges. On the first row its peak is f(0,m). At insertion of b, f(1,m)<=f(0,m) since the horizontal coordinate decreases and q-m<=m. The remainder decreases. Hence this path attains F*. It also has the minimum possible number k of exchanges, because k identities must be replaced. This does not establish that all optimal-peak paths have minimum length.
The count graph is the exact quotient of the identity graph for this family: nontrivial one-swap transitions have increments (0,+/-1),(+/-1,0),(+1,-1),(-1,+1), subject to count bounds. Every such edge is realizable from any identity selection with those counts because availability depends only on counts. Within-type exchanges do not change cost.

## Loss versus gain
The squared barrier above start is
Delta=F* - k^2/4 = m^2/(4q^2)-k*m*epsilon+m^2*epsilon^2 >0.
The smallest necessary temporary E loss is B=sqrt(F*)-k/2=Delta/(sqrt(F*)+k/2).
As q tends to infinity, m/q tends to 1/2 and k*m*epsilon tends to zero, so Delta tends to 1/16. Since sqrt(F*)+k/2 is asymptotic to k, B is asymptotic to 1/(16k). Consequently B/G is asymptotic to q^3/(2k), hence q^2/2. Absolute loss tends to zero; gain tends to zero faster. No unbounded absolute cost or universal ratio for other families claimed. With a permitted E loss budget tau, a path from start to optimum exists iff tau>=B in this model. Allowing larger simultaneous swaps changes the graph and therefore the barrier; replacing all k at once would avoid any temporary loss. No conclusion that a transition is economically worthwhile: time horizon, persistence of gains, transition costs, uncertainty and recovery risk are not modeled.

## Execution
Local python3 -I /mnt/data/toto-r28/probe.py; stdout captured with tee. Exact Fraction minimax Dijkstra and independent threshold reachability (inclusive at F*, disconnected strictly below F*) on count graphs q=1..128, containing 16,768 vertices in total. Check explicit optimal path. Five identity graphs q=1..5 with 1,272 total vertices supply an additional uncompressed graph control using direct identity swaps and the same score formula; this is not independent human review. Actual stdout in probe.log. All assertions passed. Displayed B/G uses ordinary floating arithmetic after exact barrier computation, not certified intervals. Git hashes probe.py 38641d8e88d582249471992afe12542a5aa98ee0, probe.log 4696db61595acaf9b90cc0e4f680cf4e713d8fd0. No physical experiment, organizational result, optimal general escape algorithm or novelty claim.

## Margin
Endpoint improvement, exchange radius and minimax transition loss are three different quantities. A better endpoint need not justify a path. A more meaningful next question is how scheduling, repeated benefits and time-dependent risk modify the decision, or how a limited parallel exchange radius changes this exact barrier. Transfer to other domains requires a validated objective and actual transition model.
