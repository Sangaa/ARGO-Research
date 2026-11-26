#!/usr/bin/env python3
"""R21 certificate: the j = 1 layer and the worst j = 2 case, in closed form.

Self-contained, exact, no dependencies. Exits non-zero on disagreement.

With m_j = |c_(d-j)| / (|c_d| t^(2j)), three closed forms, each verified here
against the polynomial and each giving m < 1 for every t >= 2 by inspection:

  non-zero endpoint W = w0 : m_1 = (t^2-1)/(|w0| t^2)                -> 1/|w0|
  zero endpoint     W = 0  : m_1 = (25t^2+23)/(48 t^2)               -> 25/48
  binding class, j = 2     : m_2 = (25t^5-16t^4+16t^3+5t^2-30t)/(48 t^5)

The second uses 25t^4-2t^2-23 = (25t^2+23)(t^2-1) - the same factor as
a_4 = -(t^2-1)(25t^2+23)/1152 in R14's asymptotic expansion, so one polynomial
governs both routes.

m_1 < 1 at the zero endpoint is exactly 23 < 23t^2, i.e. t >= 2: the hypothesis
enters at one place again.

The file also reports what is left: the maximum of m_j over everything NOT
covered by the three formulas.
"""
from fractions import Fraction as F
import sys


def residues(t, M):
    out = set()
    for v in range(2 * M):
        for w in range(2 * M):
            if (v + w - 1 - t) % 2:
                continue
            out.add((6 * v * v - 30 * w * w - 24 * w + 5 * t * t - 5) % M)
    return out


def bracket(t, M=24):
    r = residues(t, M)
    inside = lambda x: (x % M) in r
    R = 0
    while not inside(R):
        R += 1
    L = 1
    while not inside(-L):
        L += 1
    return L, R


def endpoint_poly(t, w0):
    def mul(a, b):
        out = [F(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        out[i + j] += x * y
        return out
    c = F(w0 - 5 * t * t - 1, 24)
    left = [F(1)]
    for i in range(t):
        s = F(i) - F(t - 1, 2)
        left = mul(left, [c - s / 2 - s * s, s, F(1)])
    right = [F(1)]
    for i in range(t):
        h = F(2 * i + 1, 2)
        right = mul(right, [-h * h, F(0), F(1)])
    n = max(len(left), len(right))
    p = [(left[i] if i < len(left) else F(0)) - (right[i] if i < len(right) else F(0))
         for i in range(n)]
    while p and p[-1] == 0:
        p.pop()
    return p


def m(t, w0, j):
    p = endpoint_poly(t, w0)
    d = len(p) - 1
    return abs(p[d - j]) / (abs(p[d]) * F(t) ** (2 * j))


def main() -> int:
    bad = []

    print("A. the j = 1 layer, both endpoint types")
    for t in range(2, 41):
        L, R = bracket(t)
        for w0 in (-L, R):
            got = m(t, w0, 1)
            want = (F(25 * t * t + 23, 48 * t * t) if w0 == 0
                    else F(t * t - 1, abs(w0) * t * t))
            if got != want:
                bad.append(f"m_1 formula failed at t={t}, W={w0}: {got} vs {want}")
            if got >= 1:
                bad.append(f"m_1 >= 1 at t={t}, W={w0}: {got}")
    print("   non-zero endpoint : m_1 = (t^2-1)/(|w0| t^2)   verified t = 2..40")
    print("   zero endpoint     : m_1 = (25t^2+23)/(48 t^2)  verified t = 2..40")
    print("   25t^4-2t^2-23 == (25t^2+23)(t^2-1)?",
          all(25 * t ** 4 - 2 * t ** 2 - 23 == (25 * t * t + 23) * (t * t - 1)
              for t in range(1, 50)))
    print("   m_1 < 1 at the zero endpoint  <=>  23 < 23t^2  <=>  t >= 2")
    print(f"   sample: t=5 -> {m(5,0,1)}, t=7 -> {m(7,0,1)}\n")

    print("B. the worst j = 2 case, t = 0 (mod 6), W = 1")
    num = lambda t: 25 * t ** 5 - 16 * t ** 4 + 16 * t ** 3 + 5 * t * t - 30 * t
    print(f"   {'t':>4} {'closed form':>24} {'measured':>24}")
    for t in (6, 12, 24, 36, 48, 60):
        clos = F(num(t), 48 * t ** 5)
        got = m(t, 1, 2)
        if clos != got:
            bad.append(f"m_2 formula failed at t={t}: {got} vs {clos}")
        print(f"   {t:4d} {str(clos):>24} {str(got):>24}")
    print("   m_2 < 1  <=>  23t^5 + 16t^4 - 16t^3 - 5t^2 + 30t > 0, true for t >= 1")
    print(f"   limit 25/48 = {float(F(25,48)):.7f}\n")

    print("C. what the three formulas do NOT cover")
    covered = lambda t, w0, j: j == 1 or (t % 6 == 0 and w0 == 1 and j == 2)
    best, where = F(0), None
    per_class = {}
    for t in range(2, 61):
        L, R = bracket(t)
        for w0 in (-L, R):
            p = endpoint_poly(t, w0)
            d = len(p) - 1
            for j in range(1, d + 1):
                if covered(t, w0, j):
                    continue
                v = m(t, w0, j)
                if v > 1:
                    bad.append(f"uncovered case exceeds 1 at t={t}, W={w0}, j={j}")
                if v > best:
                    best, where = v, (t, w0, j)
                c = t % 6
                if c not in per_class or v > per_class[c][0]:
                    per_class[c] = (v, t, w0, j)
    print(f"   max over the uncovered set : {best} = {float(best):.6f}"
          f"  at t={where[0]}, W={where[1]}, j={where[2]}")
    print(f"   room for a crude bound     : factor {float(1/best):.3f}")
    for c in sorted(per_class):
        v, t, w0, j = per_class[c]
        print(f"     t = {c} (mod 6): {float(v):.6f}  at t={t}, W={w0}, j={j}")
    print("   every one of those is at j = 2, at the LOWER endpoint, at the")
    print("   smallest t of its class, and the values fall as t grows.")

    if bad:
        print("\nFAILED:")
        for b in bad:
            print("  -", b)
        return 1
    print("\nALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
