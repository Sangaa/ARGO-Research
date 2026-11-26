#!/usr/bin/env python3
"""R19 certificate: Cauchy's raw ratio vs the j-th root bound.

Self-contained, exact where it matters, no dependencies. Exits non-zero on
disagreement. Run: python3 <this file>

R17 used Cauchy's bound in the form max_j |c_{d-j}/c_d|, a RAW ratio. Since
|c_{d-j}/c_d| grows like t^(2j), the maximum over j = 1..d with d = 2t-2 is
super-exponential in t - which is the whole of R17's blow-up. The standard root
bound takes the j-th root first (Fujiwara):

    every root rho satisfies |rho| <= 2 * max_j ( |c_{d-j}/c_d| )^(1/j)

and each of those is then O(t^2) again. Measured below: the maximum over j,
divided by t^2, never exceeds 1 on the range checked, so Q_0 <= 2t^2 and
n <= 4t^2 - R19's target shape with C = 4.

The binding term is identified, not merely observed: for the t = 0 (mod 6) class
the bracket is (-11, 1), so the upper endpoint has R = 1, c_d = t/24 and
c_{d-1} = t(t^2-1)/24, giving |c_{d-1}/c_d| = (t^2-1)/R = t^2-1, strictly below
t^2 for every t. 1 - 1/900 = 0.998888... is the t = 30 row.
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


def margins(t, w0):
    """Exact |c_(d-j)| / (|c_d| t^(2j)) for every j. No roots, no floats.

    TOTO's R19 correction: max_j (|c_(d-j)/c_d|)^(1/j) <= t^2 is equivalent to
    |c_(d-j)| <= |c_d| t^(2j) for every j, which is a comparison of exact
    rationals. The previous version of this file computed float(r)**(1.0/j) -
    a floating-point root inside a certificate whose point was exactness.
    """
    p = endpoint_poly(t, w0)
    d = len(p) - 1
    cd = abs(p[d])
    return [(abs(p[d - j]) / (cd * F(t) ** (2 * j)), j) for j in range(1, d + 1)]


def main() -> int:
    bad = []
    print("A. Cauchy's raw ratio against the j-th root bound, at t = 7")
    L, R = bracket(7)
    p = endpoint_poly(7, -L)
    d = len(p) - 1
    raw = max(abs(c) / abs(p[d]) for c in p[:-1])
    # the j-th-root quantity, reported for comparison only; every TEST below is
    # the equivalent exact inequality, so no float enters a verdict
    rt = max(float(abs(p[d - j]) / abs(p[d])) ** (1.0 / j)
             for j in range(1, d + 1) if p[d - j] != 0)
    print(f"  raw  max_j |c_(d-j)/c_d|        = {float(raw):.3e}   (Cauchy, what R17 used)")
    print(f"  root max_j |c_(d-j)/c_d|^(1/j) = {rt:.3f}          (Fujiwara)")
    print("  Same coefficients. Both bounds are CORRECT; the raw ratio is simply")
    print("  loose when the ratios grow like t^(2j), because it discards the degree")
    print("  information the j-th root keeps. Six orders of magnitude of method,")
    print("  not of mathematics - and R17's 45-million-row scan was its price.")
    print("  (TOTO's R19 correction: this was a loose bound, NOT a misapplied one.)\n")

    print("B. |c_(d-j)| <= |c_d| t^(2j) ?   exact, contiguous t = 2..60")
    polys = ineqs = 0
    worst, where = F(0), None
    argmax_not_1 = []
    for t in range(2, 61):
        L, R = bracket(t)
        for w0 in (-L, R):
            polys += 1
            ms = margins(t, w0)
            ineqs += len(ms)
            for r, j in ms:
                if r > 1:
                    bad.append(f"inequality failed at t={t}, W={w0}, j={j}: {r}")
                if r > worst:
                    worst, where = r, (t, w0, j)
            mx = max(ms)
            if mx[1] != 1:
                argmax_not_1.append((t, w0, mx[1], float(mx[0])))
    print(f"  polynomials tested : {polys}")
    print(f"  exact inequalities : {ineqs}")
    print(f"  failures           : {len(bad)}")
    print(f"  tightest margin    : {worst} = {float(worst):.6f}"
          f"  at t={where[0]}, W={where[1]}, j={where[2]}")
    print(f"  and {where[0]}^2-1 over {where[0]}^2 = {F(where[0]**2-1, where[0]**2)}"
          f"  -> the tightest of all of them is the one case already PROVED")
    print(f"  => Q_0 <= 2t^2 and n <= 4t^2 on this range (BOUNDED_PROXY, not all t)")
    print()
    print("  my own next idea, refuted before proposing it:")
    print(f"  j = 1 is NOT always the argmax - {len(argmax_not_1)} counterexamples,"
          f" all at the lower end with j = 2:")
    for t, w0, j, m in argmax_not_1:
        print(f"    t={t:3d} W={w0:4d} j*={j} margin={m:.3f}")
    print("  so the general claim does not reduce to the proved j = 1 case.")
    # TOTO's R20 correction: 0.136 was the largest margin among the SIX rows
    # above, a subset filtered by argmax != 1 - which selects polynomials where
    # m_1 is small, the opposite tail from the quantity being bounded. The true
    # maximum over all j >= 2 is computed here instead.
    mx2, w2 = F(0), None
    for t in range(2, 61):
        L2, R2 = bracket(t)
        for w in (-L2, R2):
            for r, j in margins(t, w):
                if j >= 2 and r > mx2:
                    mx2, w2 = r, (t, w, j)
    print(f"  true max of m_j over ALL j >= 2 : {mx2} = {float(mx2):.7f}"
          f"  at t={w2[0]}, W={w2[1]}, j={w2[2]}")
    print(f"  so the room for a crude bound at j >= 2 is a factor of"
          f" {float(1/mx2):.3f}, NOT 7 as an earlier version of this file said.")
    print("  (That claim read a maximum off the filtered table above. The worst")
    print("   j >= 2 case is absent from it because its j = 1 margin is larger.)\n")

    print("C. the binding term in closed form: (t^2-1)/R for the t=0 (mod 6) class")
    print(f"  {'t':>4} {'R':>3} {'measured |c_(d-1)/c_d|':>24} {'(t^2-1)/R':>12}")
    for t in (6, 12, 18, 24, 30):
        L, R = bracket(t)
        p = endpoint_poly(t, R)
        d = len(p) - 1
        got = abs(p[d - 1]) / abs(p[d])
        want = F(t * t - 1, R) if R else None
        if want is not None and got != want:
            bad.append(f"closed form for j=1 failed at t={t}: {got} vs {want}")
        print(f"  {t:4d} {R:3d} {str(got):>24} {str(want):>12}"
              f"   {'ok' if want is None or got == want else 'MISMATCH'}")
    print("  (t^2-1)/t^2 -> 1 from below, so j = 1 never reaches t^2. That case is")
    print("  PROVED; the bound for general j is not.")

    if bad:
        print("\nFAILED:")
        for b in bad:
            print("  -", b)
        return 1
    print("\nALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
