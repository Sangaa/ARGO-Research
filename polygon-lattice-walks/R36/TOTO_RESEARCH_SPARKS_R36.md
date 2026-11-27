# TOTO | R36 — Audit cadence under persistent change and imperfect detection
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED exact finite controls. No originality or independent review claim.

## Retrieval and choice
Read R35 at main 1cc9ea6cf291ab08bbfc7d555a0bc85e215c7f46, note blob 121e679aa2652a3489766c9e49bb3fbbe48596e2. The owner stated that rules and reviewers must themselves be periodically reviewed as knowledge increases. This is design intent, not a verified production guarantee. TOTO chooses the audit-cadence question from R35's margin. Related established literature on imperfect inspections: https://www.sciencedirect.com/science/article/pii/S0377221700001156 ; balanced words in production and maintenance scheduling: https://doi.org/10.1080/0740817X.2011.602660 . Search abstracts consulted, not a comprehensive comparison. The following proof is specialized to the stated assumptions.

## Time provenance
A present failure alone does not distinguish an originally defective rule from a formerly valid rule whose environment changed. For example a fixed rule predicts label 0; the current externally checked label is 1. World A had label 1 all along; world B had label 0 before a change. The current observation is identical. A reliable historical label for the same well-defined item and evaluation condition distinguishes these two specific worlds; a stored rule version alone does not. A changed metric or changed task distribution is another possible explanation; do not infer causality solely from the timestamp. This is an illustrative equivalence, not an empirical ARGO finding.

## Model
Integer time, periodic deterministic audit calendar of period T>=1 and m in [1,T] distinct audit times per period; cyclic positive integer gaps g_i, sum g_i=T. A persistent detectable defect starts at an integer time whose phase is uniform modulo T. Audit at the onset time counts as immediate. Each post-onset audit independently detects with constant probability s in (0,1]; no false positives, no pre-onset alerts, no repair time or transient defects. The calendar is repeated until detection. Cost is mean detection delay in time steps, not inspection expense or harm.

Put r=1-s. With g_i the gap ending at audit i, there are g_i equally probable onset phases whose next audit is i, and their initial waits are 0,...,g_i-1. After j consecutive misses, the next gap g_(i+j) is incurred with probability r^j. Thus
D(g)=(sum_i g_i(g_i-1)/2 + sum_(j>=1) r^j sum_i g_i*g_(i+j))/T.
Indices are cyclic; the infinite geometric sum is evaluated exactly by summing j=1..m and dividing by 1-r^m. Finite because s>0.

## Balanced schedule minimizes mean detection delay
Let B_l=sum_i (sum_(j=0)^(l-1) g_(i+j))^2 for l>=1. Expand squares, including cyclic repeats when l>m:
B_l=l sum_i g_i^2 + 2 sum_(j=1)^(l-1)(l-j)sum_i g_i*g_(i+j).
Since sum_(l>=1) s^2*r^(l-1)*l=1 and sum_(l>j) s^2*r^(l-1)*(l-j)=r^j,
D(g)+1/2=(s^2/(2T))*sum_(l>=1)r^(l-1) B_l.
For s=1 only l=1 contributes. All coefficients nonnegative, all series converge.

For each l the m integer block sums total l*T. Among m integers with that sum the sum of squares is minimized by values differing by at most one (move one unit from larger to smaller if their difference >=2). The mechanical schedule g_i=floor((i+1)T/m)-floor(i*T/m), extended periodically, attains this minimum for EVERY l simultaneously: telescoping gives floor((i+l)T/m)-floor(i*T/m), either floor(l*T/m) or ceil(l*T/m). This includes l>m. Therefore this schedule minimizes D over all positive integer cyclic gap schedules, for every s in (0,1]. No uniqueness claim. It need not optimize nonuniform onset, varying or dependent sensitivity, false alarms, audit costs, adaptive calendars, or simultaneous defects.

By the square mean inequality B_l>=m*(l*T/m)^2. Summing the geometric second moment yields
D(g) >= (T/m)*(2-s)/(2*s)-1/2.
When m divides T, equal gaps attain equality. Otherwise the l=1 square bound is strict, so the optimal integer schedule is strictly above this real-spacing bound. The exact integer optimum is given by substituting the mechanical gaps into D. For perfect detection, the bound is half the uniform gap minus half a time step. For independent imperfect detection, repeated misses add (T/m)*(1-s)/s when equal gaps are used. The discrete -1/2 is due to allowing same-step detection. For s=0 detection never occurs and the theorem is inapplicable.

## Actual execution
Ran python3 -I /mnt/data/toto-r36/probe.py locally in the container, stdout captured with tee and pipefail. Standard library only. Enumerated all positive integer ordered compositions T=1..12, m=1..T, four sensitivities 1,3/4,1/2,1/5: 312 period/rate cases and 16,380 exact Fraction comparisons to the mechanical schedule. Checked block balance through l=2m and lower-bound equality condition. All assertions passed. T=30,m=5 example compares gaps (6,6,6,6,6) to (1,1,1,1,26). Script blob ccb375664d43def85680882b7cf83e04f448b851 and stdout blob aa91845bcded788fffdb7a395e6ca819fccf453e. No human independent review, production experiment, claim of novelty or automatic policy change.

## Margin
Revisability, evidence coverage, sensitivity and cadence are distinct. A high inspection count cannot guarantee short detection delay if all inspections cluster. If errors are systematic and dependent, the independence premise can fail completely; a repeated blind test may never see a defect. Next study correlated audit failures, using heterogeneous tests or independently selected audit regions, and the distinction between detecting change and diagnosing its cause. Research only.
