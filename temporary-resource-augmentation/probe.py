#!/usr/bin/env python3
"""Exact arithmetic for a temporary-unit proportional allocation example."""
from fractions import Fraction

original = 7
shares = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8))
share_sum = sum(shares, Fraction(0, 1))
temporary = Fraction(original) * (1 - share_sum) / share_sum
augmented = Fraction(original) + temporary
allocations = [share * augmented for share in shares]
allocated = sum(allocations, Fraction(0, 1))
residual = augmented - allocated

print("original=7")
print("shares_of_augmented_total=1/2,1/4,1/8")
print("share_sum=" + str(share_sum))
print("temporary_addition=" + str(temporary))
print("augmented_total=" + str(augmented))
print("allocations=" + str([int(x) for x in allocations]))
print("allocated_total=" + str(allocated))
print("residual=" + str(residual))
print("exact_conservation=" + str(allocated == original and residual == temporary))
