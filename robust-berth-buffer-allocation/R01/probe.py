#!/usr/bin/env python3
"""Exact certificate for bounded fixed-order single-berth buffer allocation."""
from itertools import product


def worst_delays(arrival_bounds, overrun_bounds, gaps):
    delays = [arrival_bounds[0] + overrun_bounds[0]]
    for i in range(1, len(arrival_bounds)):
        delays.append(max(arrival_bounds[i], delays[-1] - gaps[i]) + overrun_bounds[i])
    return delays


def interval_formula(arrival_bounds, overrun_bounds, gaps):
    result = []
    for i in range(len(arrival_bounds)):
        result.append(max(
            arrival_bounds[j] + sum(overrun_bounds[j:i + 1]) - sum(gaps[j + 1:i + 1])
            for j in range(i + 1)
        ))
    return result


def min_buffers(arrival_bounds, overrun_bounds, target):
    n = len(arrival_bounds)
    if len(overrun_bounds) != n or n == 0:
        raise ValueError("bound vectors must have the same positive length")
    if any(a < 0 for a in arrival_bounds) or any(b < 0 for b in overrun_bounds):
        raise ValueError("uncertainty bounds must be nonnegative")
    if any(a + b > target for a, b in zip(arrival_bounds, overrun_bounds)):
        return None

    # Prefix buffer G[i] is the total idle buffer before ship i; G[0]=0.
    prefix = [0] * n
    overrun_prefix = [0]
    for b in overrun_bounds:
        overrun_prefix.append(overrun_prefix[-1] + b)

    for i in range(1, n):
        # Zero-weight edge (i-1)->i enforces nonnegative individual buffers.
        prefix[i] = prefix[i - 1]
        for j in range(i):
            demand = arrival_bounds[j] + (overrun_prefix[i + 1] - overrun_prefix[j]) - target
            if demand > 0:
                prefix[i] = max(prefix[i], prefix[j] + demand)

    gaps = [0] + [prefix[i] - prefix[i - 1] for i in range(1, n)]
    delays = worst_delays(arrival_bounds, overrun_bounds, gaps)
    assert all(d <= target for d in delays)
    assert delays == interval_formula(arrival_bounds, overrun_bounds, gaps)
    return gaps, prefix[-1], delays


def exhaustive_small_check():
    cases = 0
    for n in (2, 3):
        values = range(3)
        for pair in product(values, repeat=2 * n):
            a, b = list(pair[:n]), list(pair[n:])
            low = max(x + y for x, y in zip(a, b))
            for target in range(low, low + 3):
                answer = min_buffers(a, b, target)
                assert answer is not None
                gaps, optimum, delays = answer
                assert all(d <= target for d in delays)
                bound = sum(b) + max(a) + target + 1
                brute = min(
                    sum(g)
                    for g in product(range(bound + 1), repeat=n - 1)
                    if max(worst_delays(a, b, [0] + list(g))) <= target
                )
                assert optimum == brute, (a, b, target, gaps, optimum, brute)
                cases += 1
    return cases


def main():
    # Same total inserted idle time, different placement, different guarantee.
    a = [0, 0, 0]
    b = [5, 2, 0]
    target = 5
    good = [0, 2, 0]
    misplaced = [0, 0, 2]
    good_delays = worst_delays(a, b, good)
    misplaced_delays = worst_delays(a, b, misplaced)
    assert good_delays == [5, 5, 5]
    assert misplaced_delays == [5, 7, 5]

    result = min_buffers(a, b, target)
    assert result == (good, 2, good_delays)
    checked = exhaustive_small_check()

    print("model: fixed one-berth order; independent bounded lateness and overrun")
    print("example bounds A:", a, "B:", b, "target H:", target)
    print("buffer vector [before ship 1..3]:", good, "worst departure delays:", good_delays)
    print("same total buffer, misplaced:", misplaced, "worst departure delays:", misplaced_delays)
    print("minimum total buffer:", result[1], "exact placement:", result[0])
    print("exhaustive integer instances checked:", checked)
    print("all exact assertions passed")


if __name__ == "__main__":
    main()
