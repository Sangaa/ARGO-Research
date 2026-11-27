#!/usr/bin/env python3
"""Exact arithmetic certificate for the R24 tightening of the scoped bound."""
from fractions import Fraction as F

# The factorwise Taylor remainder table in frozen V3 sums to 9/4, so the
# normalized logarithmic error is bounded by 24*(9/4) = 54.
assert F(9, 4) < 3
assert 24 * F(9, 4) == 54

# Choose Q >= C*t^2 with C=113/2. These are the exact endpoint margins.
C = F(113, 2)
err_nonzero = F(54, 1) / C**2
lower_endpoint_upper = -1 + F(1, 1) / C + err_nonzero
upper_endpoint_lower = 1 - err_nonzero

assert lower_endpoint_upper < 0
assert upper_endpoint_lower > 0

# W=0 is an upper endpoint only for t == +/-1 (mod 6); for t >= 2 the
# smallest such t is 5. The bound is increasing in t^2.
zero_coefficient = 1 - F(54, 1) / C
assert zero_coefficient == F(5, 113)
zero_endpoint_lower_at_5 = zero_coefficient * 25 - 1
assert zero_endpoint_lower_at_5 == F(12, 113) > 0

# Canonical position gives n <= 2Q-t-1; Q < (113/2)t^2 then implies n<113t^2.
assert 2 * C == 113

print("remainder coefficient: 9/4 per factor sum; normalized constant: 54")
print(f"Q threshold C: {C}")
print(f"lower endpoint upper margin: {lower_endpoint_upper}")
print(f"positive endpoint lower margin: {upper_endpoint_lower}")
print(f"W=0 lower margin at smallest allowed t=5: {zero_endpoint_lower_at_5}")
print("all rational inequalities pass; scoped conclusion: n < 113 t^2")
