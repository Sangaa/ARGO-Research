#!/usr/bin/env python3
"""Small exact witness that nonuniform gap costs change the optimum."""
from itertools import product


def delays(a, b, gaps):
    out = [a[0] + b[0]]
    for i in range(1, len(a)):
        out.append(max(a[i], out[-1] - gaps[i]) + b[i])
    return out


def feasible(a, b, caps, gaps):
    return all(d <= h for d, h in zip(delays(a, b, gaps), caps))


def main():
    a = [0, 0, 0]
    b = [5, 0, 0]
    caps = [5, 5, 2]
    costs = [None, 1, 10]  # g1 is fixed at zero; then c2 and c3
    unit_cost_path = [0, 0, 3]
    weighted_candidate = [0, 3, 0]

    assert feasible(a, b, caps, unit_cost_path)
    assert delays(a, b, unit_cost_path) == [5, 5, 2]
    assert feasible(a, b, caps, weighted_candidate)
    assert delays(a, b, weighted_candidate) == [5, 2, 2]
    assert sum(costs[k] * weighted_candidate[k] for k in (1, 2)) == 3
    assert sum(costs[k] * unit_cost_path[k] for k in (1, 2)) == 30

    feasible_integer = []
    for g2, g3 in product(range(7), repeat=2):
        gaps = [0, g2, g3]
        if feasible(a, b, caps, gaps):
            feasible_integer.append((costs[1] * g2 + costs[2] * g3, gaps))
    brute_value, brute_gaps = min(feasible_integer)
    assert (brute_value, brute_gaps) == (3, weighted_candidate)

    interval_demand = a[0] + sum(b[0:3]) - caps[2]
    primal_value = costs[1] * weighted_candidate[1] + costs[2] * weighted_candidate[2]
    dual_y_13 = 1
    # The sole dual variable crosses both available gaps; check each capacity.
    assert dual_y_13 <= costs[1]
    assert dual_y_13 <= costs[2]
    dual_value = interval_demand * dual_y_13
    assert interval_demand == 3
    assert primal_value == dual_value == 3

    print("model: fixed one-berth order; vessel-specific delay caps; linear gap costs")
    print("A:", a, "B:", b, "caps:", caps, "gap costs c2,c3:", costs[1:])
    print("positive interval demand: g2+g3 >=", interval_demand)
    print("unit-cost longest-path gaps:", unit_cost_path, "weighted cost:", 30,
          "worst delays:", delays(a, b, unit_cost_path))
    print("weighted optimum gaps:", weighted_candidate, "weighted cost:", primal_value,
          "worst delays:", delays(a, b, weighted_candidate))
    print("dual y(1,3):", dual_y_13, "dual value:", dual_value)
    print("brute-force placements checked:", len(feasible_integer),
          "best:", brute_gaps, "cost:", brute_value)
    print("all exact assertions passed")


if __name__ == "__main__":
    main()
