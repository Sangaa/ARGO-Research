# TOTO | R34 — Rumor, leak, imperfect warning and source dependence
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED exact finite controls. No originality or independent review claim.

## Origin and retrieval
Owner asked, after R33's perfect-warning model, what happens if the information is a rumor or a leak. This is owner-provided research direction, not an assistant discovery. Read R33 at main c15110e936338e4f38e9e059346abfb27d248ec3, blob 38d975709042687e35a9bfc415460f7f34c7a8d3. TOTO separates signal truth, availability before a decision deadline, source dependence and possible behavioral effects. Rumor and leak are not calibrated reliability categories. A leak can be true or fabricated; a rumor can precede confirmation. No empirical signal accuracy assumed. No operational authorization.

## Hard guarantee versus expected loss
Let E be an exogenous binary event, prior p, and S an early binary signal. Sensitivity s=P(S+|E), false positive rate f=P(S+|not E). Prepare fully at cost c>=0 or do not prepare and pay loss L>=0 if E occurs. Full preparation eliminates that modeled loss. Both actions feasible before the deadline, signal cost zero; probabilities and costs known, no partial actions. Without signal the minimum expected cost is min(c,pL). With signal it is
min(c*(ps+(1-p)f), Lps) + min(c*(p(1-s)+(1-p)(1-f)), Lp(1-s)).
Prepare in an observed branch iff its posterior event probability times L is at least c, with either action optimal at equality. The minimum is no larger than the no-signal minimum since constant policies remain available. This is elementary Bayesian decision theory, not a novel theorem. If p>0 and 0<s<1, both signal branches contain a possible event; under robust zero-shortfall requirements both must prepare. Thus an imperfect signal may reduce expected cost under allowed risk, yet fail to reduce mandatory robust reserve. The signal does not remove modeled possibilities merely by assigning them small probabilities. If a signal arrives after an irrevocable preparation decision, it cannot improve that decision; it may still inform other decisions. No dynamic pulse-cost formula for general noisy warnings is claimed.

Example p=1/5, s=4/5, f=1/5, c=2, L=10. Baseline minimum cost 2. Positive posterior 1/2, negative posterior 1/17. Prepare on positive only: probability of preparation 8/25, probability of an unprepared event 1/25; cost 26/25, saving 24/25. This policy allows an unconditional 4% missed-event probability (20% conditional on the event). It is NOT a robust guarantee. A perfect warning after the decision deadline cannot achieve this saving for that decision. Values are invented mathematical parameters, not estimates of actual leaks or rumors.

## Source dependence
Five exact copies of the same positive signal carry the same information as one copy, so in the example the posterior remains 1/2. Falsely treating them as conditionally independent with the same s,f gives posterior 256/257, approximately 99.61%. This illustrates false confidence from duplicate propagation, not an empirical statistic. Different outlets do not establish source independence. Track origin, timestamp, lineage, verification and unknown dependence. Do not count repeated claims as independent evidence without justification.

## Behavior versus content: next hypothesis
A false claim can still affect behavior if people act on it. Model content truth E separately from a response variable A influenced by exposure, belief and decisions. Observing A does not by itself establish E; if the signal changes the event's probability through feedback, the exogenous-event decision model above is insufficient. This is a proposed research extension, not a measured causal effect or market forecast. A possible next model separates P(E|S) from P(A|S,E) and evaluates consequences in both true and false branches. Reliability, urgency, reach and effect size require evidence, not labels. No advice to trade on rumors.

## Actual execution
Local python3 -I /mnt/data/toto-r34/probe.py, standard library, stdout captured with tee and pipeline failure propagation. Exhaustive 14,641 exact Fraction combinations p,s,f,c in {0,0.1,...,1}, L=1; enumerate four deterministic binary decision policies, verify optimal expected cost formula and no-signal bound, and robust action characterization for interior p,s. Exact example and duplicated-signal control. All assertions passed. Script Git blob ef73dd1d7084340bd3fa01bb7593e204d3ee57bc; stdout blob b12a4c09f322c8168710ee1f1a95daa64ce55d8f. No empirical forecasting, source calibration, causal behavior simulation, independent review or originality assessment.

## Margin
Truth probability and impact probability need not move together. A warning can be informative but not actionable in time; a repeated rumor can be influential without adding truth evidence. Test correlated cascades, endogenous behavior and verified signal timing separately. Research only.
