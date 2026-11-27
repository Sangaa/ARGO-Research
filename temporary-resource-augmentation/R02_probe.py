#!/usr/bin/env python3
"""Exact feasibility gates for borrowed-unit proportional allocation."""
from fractions import Fraction

cases = [
    ("seven_camels", 7, (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8))),
    ("whole_allocations_fractional_borrow", 3, (Fraction(3, 11), Fraction(6, 11))),
    ("whole_borrow_fractional_allocations", 2, (Fraction(1, 3), Fraction(1, 6))),
]
expected = {
    "seven_camels": (Fraction(8), Fraction(1), [Fraction(4), Fraction(2), Fraction(1)], "FEASIBLE"),
    "whole_allocations_fractional_borrow": (Fraction(11, 3), Fraction(2, 3), [Fraction(1), Fraction(2)], "FAIL_FRACTIONAL_BORROW"),
    "whole_borrow_fractional_allocations": (Fraction(4), Fraction(2), [Fraction(4, 3), Fraction(2, 3)], "FAIL_FRACTIONAL_ALLOCATION"),
}
for name, original, shares in cases:
    q = sum(shares, Fraction())
    assert Fraction(0) < q < Fraction(1)
    augmented = Fraction(original) / q
    borrowed = augmented - original
    allocations = [share * augmented for share in shares]
    feasible = augmented.denominator == 1 and all(x.denominator == 1 for x in allocations)
    status = "FEASIBLE" if feasible else (
        "FAIL_FRACTIONAL_BORROW" if augmented.denominator != 1 else "FAIL_FRACTIONAL_ALLOCATION"
    )
    actual = (augmented, borrowed, allocations, status)
    assert actual == expected[name], (name, actual, expected[name])
    print(
        f"{name}: M={original}; q={q}; T={augmented}; b={borrowed}; "
        f"allocations={allocations}; status={status}"
    )
print("boundary_q=0: IMPOSSIBLE_FOR_M_POSITIVE")
print("boundary_q=1: ZERO_BORROW")
print("boundary_q_gt_1: NEGATIVE_BORROW")
print("all_exact_checks=True")
