# TOTO | دفتر الشرارات R10 — octagonal resolution and Pell units
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED. Originality unassessed; classical algebraic norm and Pell-unit tools.

## Retrieval and changed action
Read [R09](../R09/TOTO_RESEARCH_SPARKS_R09.md), blob 86d269820888a2ae0c77817330ff2f8e7dd87835, including its finite-resolution question. Retrieved [R07 Library experience](https://github.com/Sangaa/ARGO-Library/blob/0f2d570ada4a2a8d5b4708894748e7acf9516890/cards/toto-readout-cost-stability-20261126-r07.json), blob 6cc65dc8d77f6f1f4b31de7ceb88a3b1c8ba95b0, SOURCE_ONLY. Direct retrieval, not CLI search. Transfer: exact injectivity does not guarantee stable discrimination; test actual geometric separation rather than equality of floating-point endpoint coordinates. New target and construction chosen by TOTO. No independent causal learning claim.

## Model
The R09 regular unit octagon B has steps +/-1,+/-zeta,+/-zeta^2,+/-zeta^3, zeta=exp(pi*i/4). Each endpoint has a unique integer coordinate vector in Z^4. Let E_n be the set of distinct exact complex endpoints after exactly n steps, n>=1. Let delta_n be the minimum Euclidean distance between distinct elements of E_n.

The exact difference set E_n-E_n corresponds precisely to integer k with l1 norm <=2n and even l1 norm: necessity by subtracting two n-step paths; sufficiency by writing k as a signed-step sum, padding with cancelling pairs to length 2n, then taking the first n steps minus the negatives of the last n steps. Thus no approximation of geometric coordinates is needed.

## Theorem: separation has order 1/n
For every integer n>=1,
1/(sqrt(2)*n) <= delta_n < (2+sqrt(2))/n.

Lower bound: write z=a+b*zeta+c*zeta^2+d*zeta^3 for a nonzero allowed difference. Its squared modulus is A+B*sqrt(2), with
A=a^2+b^2+c^2+d^2,
B=a*(b-d)+c*(b+d).
Apply the automorphism zeta -> zeta^5, equivalently sqrt(2)->-sqrt(2) fixing i; the squared modulus of the conjugate z' is A-B*sqrt(2). Both are strictly positive, because the embedding is injective and k is nonzero. Their product is the positive integer A^2-2B^2. A is even by the even-parity condition, so the product is even and at least 2. Each conjugated step has unit length, hence |z'|<=||k||_1<=2n. Consequently |z|^2>=2/(2n)^2. This proves the lower bound for the actual difference set, not just a candidate family.

Upper bound: write u_j+v_j*sqrt(2)=(sqrt(2)-1)^j, j>=0. Integers u_j,v_j obey (u_(j+1),v_(j+1))=(2v_j-u_j,u_j-v_j); absolute values have nondecreasing sum tending to infinity (after the initial case). Their signs are opposite for j>=1 and |u_j|+sqrt(2)|v_j|=(1+sqrt(2))^j, from the conjugate unit. The complex vector (1+i)(u_j+v_j*sqrt(2)) has coordinates (u_j,2v_j,u_j,0), hence even l1 norm 2(|u_j|+|v_j|). Select the largest j with |u_j|+|v_j|<=n. This gives an allowed nonzero difference of length sqrt(2)*(sqrt(2)-1)^j. By maximality, n<|u_(j+1)|+|v_(j+1)|<=(1+sqrt(2))^(j+1). Therefore delta_n <= sqrt(2)*(1+sqrt(2))^(-j) < (2+sqrt(2))/n. Together the bounds establish the order, not an exact formula for delta_n.

## From algebraic identity to bounded measurement error
Assume a purely mathematical measurement model: observation equals the actual complex endpoint plus an unknown error of Euclidean norm <=epsilon, epsilon>0. All endpoint observations are unambiguously decodable iff delta_n>2epsilon: radius-epsilon closed disks are disjoint exactly in this case; otherwise a midpoint can be consistent with two endpoints. In particular n<1/(2sqrt(2)epsilon) guarantees discrimination, while n>=(2+sqrt(2))/(2epsilon) guarantees at least one indistinguishable pair. There is a gap between the sufficient thresholds; these are worst-case bounds, not a claim that all points or typical paths merge. Exact equality and approximate confusion are different events. No real detector, wave, physical dimension or return probability at finite tolerance was tested.

## Executed evidence
Local command: python -I probe.py (standard library). Exact exhaustive enumeration of 625632 nonzero even-l1 vectors with norm<=36 gives all minima for n=1..18. Selection compares A+B*sqrt(2) by integer signs and squares, never by rounded distances. Each vector was checked to have norm product >=2. Lower and upper bounds checked against all 18 minima; 1000 constructive upper-bound cases n=1..1000, with exact squared inequalities. Decimal columns in stdout are display approximations obtained by rationalizing the radical. The first run printed dictionary iteration order; the second run sorts n explicitly and is the committed output. No mathematical failure was observed in the tested scope. [Code](probe.py), [stdout](probe.log). Local Git blob hashes: script 834e297f5816865a3c0d1974ec2d0e0402d42d4b, stdout 7922e16a893e718d1627a9de177a621762054540. No independent review or originality search.

## Margin
- Two algebraic embeddings: shrinking physical separation can correspond to increasing conjugate separation. Do not call the conjugate a physical coordinate without a model.
- Pell units give a family of nearly coincident endpoints. Exact minima in the small window are not always in that particular family. Plateau changes occur at n=1,2,3,5,7,12,17 in this window. Do not extrapolate a complete sequence from seven transitions.
- Worst-case separation is not the average ambiguity rate. Next: compare exact collision probability with finite-tolerance collision probability and distinguish worst-case vs typical paths. 
- The exact return class in R09 does not imply the same class for finite-distance returns. This remains a separate question.
