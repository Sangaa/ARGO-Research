#!/usr/bin/env python3
"""R16 certificate: the two endpoint leading coefficients, derived and checked.

Self-contained, exact, no dependencies. Run: python3 <this file>

The curve, after factorials cancel and TOTO's pairing of (n-i) with (k+i+1):

    P_t(U,Q) = prod_{i<t} (U + b_i) - prod_{i<t} [Q^2 - (i+1/2)^2],
    b_i = (Q - 1/2) s_i - s_i^2,   s_i = i - (t-1)/2

At the bracket endpoints U = Q^2 + c with c = -(5t^2+1+eps)/24, eps in {0,1},
each left factor is the monic quadratic Q^2 + s_i Q + d_i, d_i = c - s_i/2 - s_i^2.

Powers of Q come from choosing Q^2 (weight 2), s_i Q (weight 1) or d_i (weight 0)
per factor, so:

  coeff(Q^{2t})   both sides 1, cancels
  coeff(Q^{2t-1}) = sum s_i = 0 on the left, 0 on the right (even), cancels
  coeff(Q^{2t-2}) = e_2(s) + sum_i d_i  on the left, -sum_i h_i^2 on the right
                  = -t*eps/24           after the identities below
  coeff(Q^{2t-3}) = e_3(s) - sum_i s_i d_i = t(t^2-1)/24   (left; right is even)

using, all from S being symmetric about 0 plus one Faulhaber sum:

    sum s_i = 0,  sum s_i^3 = 0,  e_1(s) = e_3(s) = 0,
    sum s_i^2 = t(t^2-1)/12,  sum (i+1/2)^2 = t(4t^2-1)/12

so the endpoint signs are decided for every t, with no asymptotics anywhere:

    P_t(U_{-1}, Q) ~ -(t/24)        Q^{2t-2} < 0
    P_t(U_0,    Q) ~ (t(t^2-1)/24)  Q^{2t-3} > 0   for t >= 2, and = 0 at t = 1

This file recomputes both from the product, independently of the derivation, and
exits non-zero on any disagreement.
"""
from fractions import Fraction as F
import sys


def endpoint_poly(t, eps):
    """P_t at U = Q^2 - (5t^2+1+eps)/24, as coefficients in Q, ascending."""
    def mul(a, b):
        r = [F(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        r[i + j] += x * y
        return r
    c = F(-(5 * t * t + 1 + eps), 24)
    left = [F(1)]
    for i in range(t):
        s = F(i) - F(t - 1, 2)
        left = mul(left, [c - s / 2 - s * s, s, F(1)])
    right = [F(1)]
    for i in range(t):
        h = F(2 * i + 1, 2)
        right = mul(right, [-h * h, F(0), F(1)])
    n = max(len(left), len(right))
    out = [(left[i] if i < len(left) else F(0)) - (right[i] if i < len(right) else F(0))
           for i in range(n)]
    while out and out[-1] == 0:
        out.pop()
    return out


def e_k(xs, k):
    """Elementary symmetric polynomial, exactly."""
    acc = [F(1)] + [F(0)] * k
    for x in xs:
        for j in range(k, 0, -1):
            acc[j] += acc[j - 1] * x
    return acc[k]


def main() -> int:
    bad = []
    print(f"{'t':>3} | {'deg':>4} {'lead at W=0':>14} {'t(t^2-1)/24':>14} "
          f"| {'deg':>4} {'lead at W=-1':>14} {'-t/24':>8} | {'e3(s)':>6} {'sum s_i d_i':>14}")
    print("-" * 110)
    for t in range(2, 19):
        p0, p1 = endpoint_poly(t, 0), endpoint_poly(t, 1)
        d0, l0 = len(p0) - 1, p0[-1]
        d1, l1 = len(p1) - 1, p1[-1]
        w0, w1 = F(t * (t * t - 1), 24), F(-t, 24)
        s = [F(i) - F(t - 1, 2) for i in range(t)]
        c = F(-(5 * t * t + 1), 24)
        d = [c - x / 2 - x * x for x in s]
        E3 = e_k(s, 3)
        sd = sum(x * y for x, y in zip(s, d))
        derived = E3 - sd
        ok = (d0 == 2 * t - 3 and l0 == w0 and l0 > 0
              and d1 == 2 * t - 2 and l1 == w1 and l1 < 0
              and derived == l0 and E3 == 0)
        if not ok:
            bad.append(t)
        print(f"{t:3d} | {d0:4d} {str(l0):>14} {str(w0):>14} "
              f"| {d1:4d} {str(l1):>14} {str(w1):>8} | {str(E3):>6} {str(sd):>14}"
              f"  {'' if ok else '<-- MISMATCH'}")
    print()
    print("Also: at t = 1 the positive coefficient t(t^2-1)/24 is 0, which is the")
    print("same (t^2-1) degeneracy that makes A_int vanish identically on the t=1")
    print("curve. The hypothesis t >= 2 enters the effective argument at exactly")
    print("this one place.")
    if bad:
        print(f"\nFAILED at t = {bad}")
        return 1
    print("\nALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
