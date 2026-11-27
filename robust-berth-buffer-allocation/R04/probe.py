#!/usr/bin/env python3
"""Exact small-instance check of the interval-packing/min-cost-circulation map.

Standard-library only. The cycle-canceling routine is a finite certificate
solver for integer capacities, not a claimed strongly-polynomial algorithm.
"""
from itertools import product
from random import Random


def min_cost_circulation(node_count, arcs):
    """Negative-cycle cancellation on finite integer-capacity arcs.

    Each mutable arc is [u, v, capacity, cost, flow, label].
    Returns number of augmentations; final residual network has no negative
    cycle, hence the circulation is minimum-cost.
    """
    augmentations = 0
    while True:
        dist = [0] * node_count  # implicit zero-cost super-source to all nodes
        pred = [None] * node_count
        updated = None
        for _ in range(node_count):
            updated = None
            for ix, arc in enumerate(arcs):
                u, v, cap, cost, flow, _label = arc
                if flow < cap and dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    pred[v] = (ix, 1, u)
                    updated = v
                if flow > 0 and dist[u] > dist[v] - cost:
                    dist[u] = dist[v] - cost
                    pred[u] = (ix, -1, v)
                    updated = u
            if updated is None:
                break
        if updated is None:
            return augmentations

        on_cycle = updated
        for _ in range(node_count):
            entry = pred[on_cycle]
            assert entry is not None
            on_cycle = entry[2]

        cycle = []
        at = on_cycle
        while True:
            entry = pred[at]
            assert entry is not None
            cycle.append(entry)
            at = entry[2]
            if at == on_cycle:
                break
            assert len(cycle) <= node_count

        residual = []
        cycle_cost = 0
        for ix, direction, _from in cycle:
            arc = arcs[ix]
            cap, cost, flow = arc[2], arc[3], arc[4]
            residual.append(cap - flow if direction == 1 else flow)
            cycle_cost += cost if direction == 1 else -cost
        delta = min(residual)
        assert delta > 0 and cycle_cost < 0
        for ix, direction, _from in cycle:
            arcs[ix][4] += direction * delta
        augmentations += 1


def build_network(n, demands, costs):
    """Prefix nodes 0..n-1; interval arcs forward, priced gaps backward."""
    arcs = []
    for (j, i), w in sorted(demands.items()):
        if w <= 0:
            continue
        span = [costs[k - 2] for k in range(j + 1, i + 1)]
        arcs.append([j - 1, i - 1, min(span), -w, 0, ("interval", j, i)])
    for k in range(2, n + 1):
        c = costs[k - 2]
        arcs.append([k - 1, k - 2, c, 0, 0, ("gap", k)])
    return arcs


def primal_optimum(n, demands, costs):
    max_w = max(demands.values(), default=0)
    best = None
    checked = 0
    for gaps in product(range(max_w + 1), repeat=n - 1):
        checked += 1
        if all(sum(gaps[k - 2] for k in range(j + 1, i + 1)) >= w
               for (j, i), w in demands.items()):
            value = sum(costs[k] * gaps[k] for k in range(n - 1))
            if best is None or value < best:
                best = value
    assert best is not None  # setting each gap to max_w is feasible
    return best, checked


def dual_optimum(n, demands, costs):
    intervals = [(j, i, w) for (j, i), w in sorted(demands.items()) if w > 0]
    bounds = [min(costs[k - 2] for k in range(j + 1, i + 1))
              for j, i, _w in intervals]
    best = 0
    checked = 0
    for ys in product(*(range(cap + 1) for cap in bounds)):
        checked += 1
        if all(sum(y for y, (j, i, _w) in zip(ys, intervals)
                   if j < k <= i) <= costs[k - 2]
               for k in range(2, n + 1)):
            value = sum(y * interval[2] for y, interval in zip(ys, intervals))
            best = max(best, value)
    return best, checked


def verify_case(n, demands, costs):
    arcs = build_network(n, demands, costs)
    augmentations = min_cost_circulation(n, arcs)
    flow_cost = sum(arc[3] * arc[4] for arc in arcs)

    node_balance = [0] * n
    for u, v, cap, _cost, flow, _label in arcs:
        assert 0 <= flow <= cap
        node_balance[u] -= flow
        node_balance[v] += flow
    assert node_balance == [0] * n

    interval_y = {(arc[5][1], arc[5][2]): arc[4]
                  for arc in arcs if arc[5][0] == "interval"}
    gap_z = {arc[5][1]: arc[4] for arc in arcs if arc[5][0] == "gap"}
    for k in range(2, n + 1):
        load = sum(y for (j, i), y in interval_y.items() if j < k <= i)
        assert gap_z[k] == load <= costs[k - 2]

    circulation_value = -flow_cost
    direct_dual, dual_points = dual_optimum(n, demands, costs)
    primal, primal_points = primal_optimum(n, demands, costs)
    assert circulation_value == direct_dual == primal
    return augmentations, primal_points, dual_points


def main():
    # R03 witness: one profitable interval crosses a cheap and an expensive gap.
    witness_demands = {(1, 3): 3}
    witness_costs = [1, 10]
    witness = build_network(3, witness_demands, witness_costs)
    witness_augments = min_cost_circulation(3, witness)
    witness_value = -sum(a[3] * a[4] for a in witness)
    witness_y = next(a[4] for a in witness if a[5] == ("interval", 1, 3))
    assert witness_value == 3 and witness_y == 1
    wrong_orientation = build_network(3, witness_demands, witness_costs)
    for arc in wrong_orientation:
        if arc[5][0] == "gap":
            arc[0], arc[1] = arc[1], arc[0]  # deliberately point gaps forward
    min_cost_circulation(3, wrong_orientation)
    wrong_value = -sum(a[3] * a[4] for a in wrong_orientation)
    assert wrong_value == 0 and wrong_value != witness_value

    rng = Random(20261127)
    cases = 0
    total_augmentations = 0
    total_primal_points = 0
    total_dual_points = 0
    for n in (2, 3, 4):
        pairs = [(j, i) for j in range(1, n) for i in range(j + 1, n + 1)]
        for _ in range(48):
            costs = [rng.randrange(4) for _ in range(n - 1)]
            demands = {pair: rng.randrange(5) for pair in pairs}
            aug, pcount, dcount = verify_case(n, demands, costs)
            cases += 1
            total_augmentations += aug
            total_primal_points += pcount
            total_dual_points += dcount

    print("network: interval arc j->i at cost -w; gap arc k->k-1 at capacity c_k")
    print("R03 witness: interval (1,3), costs [1,10], flow y=", witness_y,
          "dual/circulation value=", witness_value,
          "augmentations=", witness_augments)
    print("negative control (gap arcs wrongly point forward): value=", wrong_value,
          "expected mismatch confirmed")
    print("random deterministic cases checked:", cases, "(n=2,3,4; integer demands/costs 0..4/0..3)")
    print("cycle-canceling augmentations:", total_augmentations)
    print("brute-force primal placements:", total_primal_points)
    print("brute-force dual packings:", total_dual_points)
    print("all flow, capacity, primal, dual and objective assertions passed")


if __name__ == "__main__":
    main()
