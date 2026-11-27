# R02 — integer-feasibility gate and literature boundary

## Question

For an original integer stock M, when can rational shares of an augmented total be allocated as whole units and the borrowed whole units returned exactly?

## Exact criterion

Let r_i be nonnegative rational shares of the augmented total and q = sum(r_i). If the augmented total is T = M + b, then giving each recipient its exact share means x_i = r_i T. Returning exactly the borrowed amount and leaving the original M requires

    sum(x_i) = qT = M
    T = M/q
    b = T - M = M(1-q)/q

For M > 0, a positive borrowed amount requires 0 < q < 1. Exact whole-unit feasibility has two separate gates:

    T = M/q is an integer
    x_i = M r_i/q is an integer for every i

These are necessary and sufficient under the stated exact-share model. If both hold, the allocated total is M and the residual is the integer T-M=b. An integer b alone does not guarantee integer allocations; integer allocations alone do not guarantee that the borrowed amount is a whole unit.

For a common denominator r_i = p_i/D, with P = sum(p_i) and 0 < P < D, this is equivalent to

    P divides M D
    P divides M p_i for every i

because T=MD/P and x_i=Mp_i/P. Use exact integer arithmetic; do not round quotas.

## Cases

| M | Shares | q | T | b | Allocations | Outcome |
|---:|---|---:|---:|---:|---|---|
| 7 | 1/2, 1/4, 1/8 | 7/8 | 8 | 1 | 4, 2, 1 | Both gates pass |
| 3 | 3/11, 6/11 | 9/11 | 11/3 | 2/3 | 1, 2 | Allocations are whole, but borrowed amount is fractional |
| 2 | 1/3, 1/6 | 1/2 | 4 | 2 | 4/3, 2/3 | Borrowed amount is whole, but allocations are fractional |

Boundary checks: q=0 cannot satisfy qT=M for M>0; q=1 yields b=0; q>1 would require a negative b. The exact arithmetic probe records these two independent failure modes.

## Literature check and correction

The exact seven-camel variant is already published: Ian Stewart's *Scientific American* puzzle column reproduced in the [OEIS A002966 source scan](https://oeis.org/A002966/a002966_1.pdf) explicitly gives seven camels and shares 1/2, 1/4, and 1/8 (scan pp. 6–7). The same column discusses the familiar 17-camel variant and explains the leftover through shares summing to less than one. Sarah Hart's [Gresham College lecture](https://www.gresham.ac.uk/watch-now/maths-puzzles) summarizes that puzzle family and its history.

Integer apportionment of indivisible resources is an established neighboring literature. Bautista, Companys and Corominas, [“Solving the generalized apportionment problem through the optimization of discrepancy functions”](https://doi.org/10.1016/S0377-2217(00)00110-7), formalize integer allocations close to given quotas and describe applications to indivisible resources. That broad field is related, but the reviewed abstract does not establish whether this exact-return formulation has been studied as a distinct problem.

Correction to the R01 scope: the user supplied an exact variant that is already in print. R01 made no originality claim, but lacked this literature pointer and a separated integer-feasibility test. R02 records both. This is a bounded reconnaissance, not an exhaustive literature review. The formula is elementary conservation algebra; no novelty claim is made.

## Scope and status

This is an exact bounded arithmetic note, not an allocation recommendation, physical-capacity model, or claim that a real temporary resource is freely available. It is distinct from the berth lane: a mathematical borrowed unit is immediately returned; a physical holding slot remains occupied over time and can induce backpressure.

Evidence class: `DERIVED` for the formula and exact cases; the cited-source match is verified within the inspected scan; literature coverage is bounded and originality is not assessed or claimed.
