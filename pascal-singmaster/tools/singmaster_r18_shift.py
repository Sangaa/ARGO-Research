#!/usr/bin/env python3
"""R18 certificate: the Taylor shift, independently reproduced, plus the scan.

Self-contained, exact, no dependencies. Run: python3 <this file>
Exits non-zero on any disagreement.

TOTO's R18 idea retires the scan instead of speeding it up. Writing Q = B + x
with x >= 0,

    P(B+x) = sum_i a_i(B) x^i ,    a_i(B) = sum_{j>=i} c_j C(j,i) B^(j-i)

if every a_i(B) <= 0 with a_0 < 0 then P < 0 for EVERY Q >= B, and if every
a_i(B) >= 0 with a_0 > 0 then P > 0 for every Q >= B. That is a sign proof on a
half-line from a finite exact computation, using the whole coefficient vector
rather than the single entry Cauchy's bound keeps.

The gain over R17 is not marginal. At t = 7 the Cauchy bound asked for a scan of
45,155,344 rows; the shift gives a bound of n <= 12, which is below the smallest
admissible row n_min = 3t+2 = 23, so there is nothing to scan at all.

This file re-derives everything from scratch - bracket, endpoint polynomials,
shift, scan - and imports no value from her run.
"""
from fractions import Fraction as F
from math import comb, ceil
import sys

# ---------- the arithmetic bracket ----------

def residues(t, M):
    """{W mod M} for W = 6v^2-30w^2-24w+5t^2-5 under v+w = 1+t (mod 2)."""
    out = set()
    for v in range(2 * M):
        for w in range(2 * M):
            if (v + w - 1 - t) % 2:
                continue
            out.add((6 * v * v - 30 * w * w - 24 * w + 5 * t * t - 5) % M)
    return out


def bracket(t, M=24):
    """Largest (-L, R) around 0 free of permitted values of W."""
    r = residues(t, M)
    inside = lambda x: (x % M) in r
    R = 0
    while not inside(R):
        R += 1
    L = 1
    while not inside(-L):
        L += 1
    return L, R

# ---------- the endpoint polynomials ----------

def endpoint_poly(t, w0):
    """P_t at W = w0, as coefficients in Q, ascending. TOTO's product form."""
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


def shift(p, B):
    """Coefficients of p(B+x) in x, exactly."""
    d = len(p) - 1
    return [sum(p[j] * comb(j, i) * F(B) ** (j - i) for j in range(i, d + 1))
            for i in range(d + 1)]


def uniform_sign(a, negative):
    """Does the shifted vector prove one sign for all x >= 0?"""
    if negative:
        return a[0] < 0 and all(x <= 0 for x in a)
    return a[0] > 0 and all(x >= 0 for x in a)


def threshold(t, Bmax=4000):
    """Smallest integer B >= t+1 proving both endpoint signs for all Q >= B."""
    L, R = bracket(t)
    lo, hi = endpoint_poly(t, -L), endpoint_poly(t, R)
    for B in range(t + 1, Bmax):
        if uniform_sign(shift(lo, B), True) and uniform_sign(shift(hi, B), False):
            return B, L, R
    return None, L, R

# ---------- the scan ----------

def _diff(n, k, t):
    a = 1
    for i in range(t):
        a *= (n - i)
    for j in range(1, t + 1):
        a *= (k + j)
    b = 1
    for r in range(2 * t):
        b *= (n - k - r)
    return a - b


def solve_row(n, t):
    """L(k) is strictly increasing in k, so bisection finds its only root."""
    lo, hi = 0, (n - 3 * t) // 2
    if hi < lo:
        return None
    if _diff(n, lo, t) > 0 or _diff(n, hi, t) < 0:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if _diff(n, mid, t) < 0:
            lo = mid + 1
        else:
            hi = mid
    return lo if _diff(n, lo, t) == 0 else None


def scan(t, nmax):
    return [(n, k) for n in range(2 * t + 2, nmax + 1)
            if (k := solve_row(n, t)) is not None and k >= 1]


def main() -> int:
    bad = []

    print("control: t = 1 must reproduce the known family")
    ctrl = scan(1, 1200)
    print(f"  {ctrl}")
    if len(ctrl) < 3:
        bad.append("t=1 control failed - the scanner's silence would mean nothing")

    print("\nthresholds, bounds and verification for t = 2..20")
    print(f"  {'t':>3} {'bracket':>10} {'B':>6} {'n bound':>8} {'n_min':>6} "
          f"{'scanned':>14} {'solutions':>10}")
    vacuous, closed = [], []
    for t in range(2, 21):
        B, L, R = threshold(t)
        if B is None:
            bad.append(f"no threshold found for t={t}")
            continue
        nb, nmin = 2 * B - t - 1, 3 * t + 2
        if nb < nmin:
            vacuous.append(t)
            print(f"  {t:3d} {'(-'+str(L)+','+str(R)+')':>10} {B:6d} {nb:8d} {nmin:6d} "
                  f"{'not needed':>14} {'-':>10}")
            continue
        hits = scan(t, nb)
        if hits:
            bad.append(f"solution at t={t}: {hits}")
        else:
            closed.append(t)
        print(f"  {t:3d} {'(-'+str(L)+','+str(R)+')':>10} {B:6d} {nb:8d} {nmin:6d} "
              f"{str(nmin)+'..'+str(nb):>14} {str(hits) if hits else 'none':>10}")
    print(f"\n  vacuous, no scan needed: {vacuous}")
    print(f"  closed by scanning:      {closed}")
    done = sorted(set(vacuous) | set(closed))
    print(f"  => NO SOLUTIONS for t = {done[0]}..{done[-1]}"
          f" ({len(done)} displacements)" if done else "  => nothing established")
    if done != list(range(2, 21)):
        bad.append("t = 2..20 not fully covered")

    print("\none quadratic threshold for all t? B = max(t+1, ceil(C t^2))")
    for C, upto in ((F(5, 8), 60), (F(2, 3), 60), (F(3, 4), 60)):
        first = None
        for t in range(2, upto + 1):
            L, R = bracket(t)
            B = max(t + 1, ceil(C * t * t))
            if not (uniform_sign(shift(endpoint_poly(t, -L), B), True)
                    and uniform_sign(shift(endpoint_poly(t, R), B), False)):
                first = t
                break
        print(f"  C = {C}: {'holds for t=2..'+str(upto) if first is None else 'FAILS first at t='+str(first)}")
    print("  C = 2/3 holding on this range is BOUNDED_PROXY, not a theorem for all t.")

    if bad:
        print("\nFAILED:")
        for b in bad:
            print("  -", b)
        return 1
    print("\nALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
