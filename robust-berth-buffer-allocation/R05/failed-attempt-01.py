#!/usr/bin/env python3
"""Recover an exact primal gap vector from an uncapped-interval circulation.

Fractions and the Python standard library only. The cycle-canceling routine is
for certificate-sized networks; no production runtime bound is claimed.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def residual_edges(arcs):
    edges = []
    for ix, (u, v, cap, cost, flow, _label) in enumerate(arcs):
        if cap is None or flow < cap:
            edges.append((u, v, cost, ix, 1, None if cap is None else cap - flow))
        if flow > 0:
            edges.append((v, u, -cost, ix, -1, flow))
    return edges


def cancel_one_negative_cycle(node_count, arcs):
    dist = [F(0) for _ in range(node_count)]
    pred = [None] * node_count
    last = None
    edges = residual_edges(arcs)
    for _ in range(node_count):
        last = None
        for u, v, cost, ix, direction, capacity in edges:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                pred[v] = (ix, direction, u, capacity)
                last = v
        if last is None:
            return 0

    on_cycle = last
    for _ in range(node_count):
        item = pred[on_cycle]
        assert item is not None
        on_cycle = item[2]

    cycle = []
    at = on_cycle
    while True:
        item = pred[at]
        assert item is not None
        cycle.append(item)
        at = item[2]
        if at == on_cycle:
            break
        assert len(cycle) <= node_count

    finite = [item[3] for item in cycle if item[3] is not None]
    assert finite, "an improving cycle must meet a finite gap or reverse-flow capacity"
    delta = min(finite)
    cycle_cost = sum(arcs[ix][3] * direction for ix, direction, _u, _cap in cycle)
    assert delta > 0 and cycle_cost < 0
    for ix, direction, _u, _cap in cycle:
        arcs[ix][4] += direction * delta
    return 1


def optimize_uncapped_interval_circulation(n, demands, costs):
    """Minimize cost on the network; unbounded interval arcs, finite gap arcs."""
    arcs = []
    for (j, i), w in sorted(demands.items()):
        if w > 0:
            arcs.append([j - 1, i - 1, None, -w, F(0), ("interval", j, i)])
    for k in range(2, n + 1):
        arcs.append([k - 1, k - 2, costs[k - 2], F(0), F(0), ("gap", k)])

    augmentations = 0
    while True:
        changed = cancel_one_negative_cycle(n, arcs)
        if not changed:
            break
        augmentations += changed

    # Shortest residual labels give min-cost node potentials; negate them to
    # obtain max-profit potentials P satisfying P_v >= P_u + profit(u,v).
    dist = [F(0) for _ in range(n)]
    edges = residual_edges(arcs)
    for _ in range(n - 1):
        changed = False
        for u, v, cost, _ix, _direction, _capacity in edges:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                changed = True
        if not changed:
            break
    assert all(dist[v] <= dist[u] + cost for u, v, cost, *_rest in edges)
    potentials = [-x for x in dist]

    gaps = [F(0)]
    for k in range(2, n + 1):
        gaps.append(max(F(0), potentials[k - 1] - potentials[k - 2]))

    profit = -sum(cost * flow for _u, _v, _cap, cost, flow, _label in arcs)
    return arcs, potentials, gaps, profit, augmentations


def primal_optimum_by_grid(n, demands, costs, step):
    max_w = max((w for w in demands.values() if w > 0), default=F(0))
    upper = int(max_w / step)
    best = None
    checked = 0
    for counts in product(range(upper + 1), repeat=n - 1):
        checked += 1
        gaps = [F(0)] + [step * count for count in counts]
        feasible = all(sum(gaps[k - 1] for k in range(j + 1, i + 1)) >= w
                       for (j, i), w in demands.items())
        if feasible:
            value = sum(costs[k - 1] * gaps[k - 1] for k in range(2, n + 1))
            if best is None or value < best:
                best = value
    assert best is not None
    return best, checked


def check_instance(n, demands, costs, grid):
    # R02's local feasibility conditions are checked before constructing the
    # j<i interval demands. The test input is already in that reduced form.
    arcs, potentials, gaps, flow_value, augmentations = optimize_uncapped_interval_circulation(n, demands, costs)

    balances = [F(0) for _ in range(n)]
    interval_y = {}
    gap_z = {}
    for u, v, cap, _cost, flow, label in arcs:
        assert flow >= 0 and (cap is None or flow <= cap)
        balances[u] -= flow
        balances[v] += flow
        if label[0] == "interval":
            interval_y[(label[1], label[2])] = flow
        else:
            gap_z[label[1]] = flow
    assert balances == [F(0) for _ in range(n)]

    for k in range(2, n + 1):
        load = sum(y for (j, i), y in interval_y.items() if j < k <= i)
        assert gap_z[k] == load <= costs[k - 2]

    for (j, i), w in demands.items():
        assert sum(gaps[k - 1] for k in range(j + 1, i + 1)) >= w
    primal_value = sum(costs[k - 2] * gaps[k - 1] for k in range(2, n + 1))
    brute_value, brute_count = primal_optimum_by_grid(n, demands, costs, grid)
    assert primal_value == flow_value == brute_value
    return gaps, primal_value, augmentations, brute_count


def main():
    # The R03 witness now returns an optimal primal gap vector, not only value 3.
    witness_demands = {(1, 3): F(3)}
    witness_costs = [F(1), F(10)]
    witness = check_instance(3, witness_demands, witness_costs, F(1))
    assert witness[0] == [F(0), F(3), F(0)] and witness[1] == F(3)

    # A genuinely fractional witness checks exact rational prices and buffer.
    rational_demands = {(1, 3): F(1, 3)}
    rational_costs = [F(1, 3), F(2, 3)]
    rational = check_instance(3, rational_demands, rational_costs, F(1, 6))
    assert rational[0] == [F(0), F(1, 3), F(0)]
    assert rational[1] == F(1, 9)

    rng = Random(20261127)
    integer_cases = 0
    rational_cases = 0
    integer_placements = 0
    rational_placements = 0
    total_augmentations = 0
    for n in (2, 3, 4):
        pairs = [(j, i) for j in range(1, n) for i in range(j + 1, n + 1)]
        for _ in range(24):
            costs = [F(rng.randrange(4)) for _ in range(n - 1)]
            demands = {pair: F(rng.randrange(5)) for pair in pairs}
            _g, _value, aug, count = check_instance(n, demands, costs, F(1))
            integer_cases += 1
            total_augmentations += aug
            integer_placements += count
        for _ in range(12):
            # All data are exact multiples of 1/6, so the TU primal has a
            # grid vertex on this mesh; enumerate that bounded mesh exactly.
            costs = [F(rng.randrange(7), 6) for _ in range(n - 1)]
            demands = {pair: F(rng.randrange(7), 6) for pair in pairs}
            _g, _value, aug, count = check_instance(n, demands, costs, F(1, 6))
            rational_cases += 1
            total_augmentations += aug
            rational_placements += count

    print("algorithm: uncapped interval arcs; finite gap capacities; exact residual potentials")
    print("integer witness gaps:", witness[0], "cost:", witness[1])
    print("rational witness gaps:", rational[0], "cost:", rational[1])
    print("integer instances:", integer_cases, "rational instances:", rational_cases)
    print("integer primal placements enumerated:", integer_placements)
    print("rational primal placements enumerated:", rational_placements)
    print("negative-cycle augmentations:", total_augmentations)
    print("all exact feasibility, capacity, flow, potential and optimality assertions passed")


if __name__ == "__main__":
    main()
