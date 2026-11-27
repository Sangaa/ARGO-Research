#!/usr/bin/env python3
"""Exact rational certificate that the R16 dodecagon phase function varies."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt

L = 12
SCALE = 10**30
Q = F(4, 5)
OMITTED_EXPONENT = F(2, 5) ** 50


def exp_neg_bounds(x):
    """Enclose exp(-x) by alternating Taylor bounds after binary scaling."""
    assert x >= 0
    if x == 0:
        return F(1), F(1)
    r = 0
    while x / (2**r) > F(1, 4):
        r += 1
    y = x / (2**r)

    def partial(degree):
        term = F(1)
        total = term
        for j in range(1, degree + 1):
            term *= -y / j
            total += term
        return total

    low = partial(15)   # odd partial sum is below exp(-y)
    high = partial(14)  # even partial sum is above exp(-y)
    assert 0 < low <= high
    power = 2**r
    return low**power, high**power


def scaled_floor(x):
    return (x * SCALE).numerator // (x * SCALE).denominator


def scaled_ceil(x):
    y = x * SCALE
    return (y.numerator + y.denominator - 1) // y.denominator


def exact_sum_enclosure(hist, exponent_lo, exponent_hi, cutoff):
    low_units = high_units = omitted = 0
    for m, count in hist.items():
        if m >= cutoff:
            omitted += count
            continue
        lo, _ = exp_neg_bounds(exponent_hi * m)
        _, hi = exp_neg_bounds(exponent_lo * m)
        low_units += count * scaled_floor(lo)
        high_units += count * scaled_ceil(hi)
    return F(low_units, SCALE), F(high_units, SCALE), omitted


def forms(a, b, c, d):
    A = a*a + b*b + c*c + d*d + a*c + b*d
    B = a*b + b*c + c*d
    return A, A + B


def main():
    # c = sqrt(6)/2, enclosed using integer square root at 10^-18 scale.
    d = 10**18
    s = isqrt(6 * d * d)
    c_lo, c_hi = F(s, 2*d), F(s+1, 2*d)
    assert c_lo*c_lo < F(3, 2) < c_hi*c_hi
    assert c_lo > F(6, 5)  # used to bound the omitted U >= 42 terms
    assert F(1) + F(1) + F(1, 2) == F(5, 2)  # the next positive term gives e > 5/2

    hist_A, hist_U = Counter(), Counter()
    population = 0
    for a, b, c, d0 in product(range(-L, L+1), repeat=4):
        A, U = forms(a, b, c, d0)
        assert A >= 0 and U >= 0
        if (a, b, c, d0) != (0, 0, 0, 0):
            assert A > 0 and U > 0
        hist_A[A] += 1
        hist_U[U] += 1
        population += 1
    assert population == (2*L+1)**4

    # At t=1 the exponent is A. At t=sqrt(lambda), it is (sqrt(6)/2)*U.
    # For the second sum use monotonicity with c_lo <= sqrt(6)/2 <= c_hi.
    A_lo, A_hi, A_omitted = exact_sum_enclosure(hist_A, F(1), F(1), 50)
    H_lo, H_hi, H_omitted = exact_sum_enclosure(hist_U, c_lo, c_hi, 42)
    assert A_omitted + H_omitted <= population*2

    # Positive-definite Gaussian envelope for both phases:
    # A >= ||k||^2/2, and (sqrt(6)/2)(A+B) > ||k||^2/4.
    # The latter follows from lambda_min(A+B)=(5-sqrt(17))/4 and
    # sqrt(6)*(5-sqrt(17))/8 > 1/4, equivalent to 62^2 > 15^2*17.
    assert 62**2 > 15**2 * 17
    # e^(1/4) > 1+1/4 = 5/4, hence exp(-||k||^2/4) < (4/5)^||k||^2.
    assert 1 + F(1, 4) == F(5, 4)  # the next positive term gives exp(1/4) > 5/4
    box_tail = 8 * Q**((L+1)**2) / (1-Q) * (1 + 2*Q/(1-Q))**3
    assert box_tail < F(1, 10**10)
    omitted_tail = population * OMITTED_EXPONENT

    F1_lo = A_lo
    F1_hi = A_hi + A_omitted*OMITTED_EXPONENT + box_tail
    Fh_lo = H_lo
    Fh_hi = H_hi + H_omitted*OMITTED_EXPONENT + box_tail
    gap_lo = F1_lo - Fh_hi
    assert gap_lo > F(1, 10**4)

    print("box radius:", L)
    print("lattice vectors counted:", population)
    print("distinct A exponents:", len(hist_A), "distinct U=A+B exponents:", len(hist_U))
    print("omitted in-box terms, phase 1:", A_omitted, "phase sqrt(lambda):", H_omitted)
    print("certified outside-box tail per phase < 1e-10:", box_tail < F(1, 10**10))
    print("certified F(1) - F(sqrt(lambda)) > 1/10000:")
    print("  checked by exact rational comparison:", gap_lo > F(1, 10**4))
    print("ALL EXACT INTERVAL CHECKS PASS")


if __name__ == "__main__":
    main()
