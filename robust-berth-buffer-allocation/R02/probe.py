#!/usr/bin/env python3
"""Exact bounded certificate for vessel-specific robust delay caps."""
from itertools import product


def worst_delays(a, b, gaps):
    d = [a[0] + b[0]]
    for i in range(1, len(a)):
        d.append(max(a[i], d[-1] - gaps[i]) + b[i])
    return d


def interval_formula(a, b, gaps):
    return [max(a[j] + sum(b[j:i + 1]) - sum(gaps[j + 1:i + 1])
                for j in range(i + 1)) for i in range(len(a))]


def min_buffers(a, b, caps):
    n = len(a)
    if not n or len(b) != n or len(caps) != n:
        raise ValueError("bound and cap vectors must have the same positive length")
    if any(x < 0 for x in a + b) or any(h < 0 for h in caps):
        raise ValueError("bounds and caps must be nonnegative")
    if any(x + y > h for x, y, h in zip(a, b, caps)):
        return None

    bprefix = [0]
    for x in b:
        bprefix.append(bprefix[-1] + x)
    prefix = [0] * n  # G_1=0, then least feasible prefix distances
    for i in range(1, n):
        prefix[i] = prefix[i - 1]  # zero-weight edge (i-1)->i
        for j in range(i):
            demand = a[j] + bprefix[i + 1] - bprefix[j] - caps[i]
            if demand > 0:
                prefix[i] = max(prefix[i], prefix[j] + demand)

    gaps = [0] + [prefix[i] - prefix[i - 1] for i in range(1, n)]
    delays = worst_delays(a, b, gaps)
    assert all(d <= h for d, h in zip(delays, caps))
    assert delays == interval_formula(a, b, gaps)
    return gaps, prefix[-1], delays


def exhaustive_small_check():
    checked = 0
    for n in (2, 3):
        for values in product(range(3), repeat=2 * n):
            a, b = list(values[:n]), list(values[n:])
            for offsets in product(range(2), repeat=n):
                caps = [x + y + z for x, y, z in zip(a, b, offsets)]
                result = min_buffers(a, b, caps)
                assert result is not None
                gaps, optimum, delays = result
                assert all(d <= h for d, h in zip(delays, caps))
                bound = sum(b) + max(a) + max(caps) + 1
                brute = min(
                    sum(g)
                    for g in product(range(bound + 1), repeat=n - 1)
                    if all(d <= h for d, h in zip(worst_delays(a, b, [0] + list(g)), caps))
                )
                assert optimum == brute, (a, b, caps, gaps, optimum, brute)
                checked += 1
    return checked


def main():
    a, b = [0, 0, 0], [5, 2, 0]
    common = min_buffers(a, b, [5, 5, 5])
    heterogeneous = min_buffers(a, b, [5, 4, 3])
    assert common == ([0, 2, 0], 2, [5, 5, 5])
    assert heterogeneous == ([0, 3, 1], 4, [5, 4, 3])
    assert min_buffers([2], [1], [2]) is None
    checked = exhaustive_small_check()
    assert checked == 6156

    print("model: fixed one-berth order; independent bounded arrival and handling overrun")
    print("bounds A:", a, "B:", b)
    print("common caps [5,5,5]: minimum gaps:", common[0], "total:", common[1], "worst delays:", common[2])
    print("vessel caps [5,4,3]: minimum gaps:", heterogeneous[0], "total:", heterogeneous[1], "worst delays:", heterogeneous[2])
    print("infeasible first-vessel cap detected:", min_buffers([2], [1], [2]) is None)
    print("exhaustive feasible instances checked:", checked)
    print("all exact assertions passed")


if __name__ == "__main__":
    main()
