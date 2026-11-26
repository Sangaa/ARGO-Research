#!/usr/bin/env python3
"""Smoothness and genus of the equal-displacement Pascal curve, with a printable certificate.

    F_t(n,k) = prod_{i=0}^{2t-1}(n-k-i)  -  prod_{i=0}^{t-1}(n-i) * prod_{j=1}^{t}(k+j)

is the curve of C(n,k) = C(n-t, k+t). This decides smoothness over a finite field and
reports the genus-degree value, printing every intermediate quantity a reader needs to
redo the check. No third-party dependencies: this runtime has no CAS and no package index.

Run:  python3 singmaster_curve_genus.py [t_max] [prime ...]

The prime must exceed the resultant's degree bound, because the resultant in n is
recovered by interpolation. A prime that is too small wraps the evaluation points and the
run then reports a smooth curve as singular; the guard below refuses instead. This is why
p=101 is fine for a Groebner-basis method and wrong for this one.

Why a finite field is enough: each obstruction is the vanishing of an integer-coefficient
quantity. If the gcd of the two resultants is a nonzero CONSTANT mod p, and p divides
neither resultant's leading coefficient, then the gcd over Q is a constant too, since
reduction cannot lower a gcd's degree under that condition. So a clean run at one good
prime is a certificate, not a sample. Both leading coefficients are printed for checking.

CLAUDE, 2026-11-25. Written for ARGO-KOP Execution/Research/CLAUDE.
"""
import sys

def make(p):
    def pmul(A, B):
        C = {}
        for (a, b), u in A.items():
            for (c, d), v in B.items():
                e = (a + c, b + d); C[e] = (C.get(e, 0) + u * v) % p
        return {e: c for e, c in C.items() if c}

    def psub(A, B):
        C = dict(A)
        for e, v in B.items():
            C[e] = (C.get(e, 0) - v) % p
        return {e: c for e, c in C.items() if c}

    def pdiff(A, var):
        C = {}
        for (i, j), c in A.items():
            e = i if var == 0 else j
            if e:
                key = (i - 1, j) if var == 0 else (i, j - 1)
                C[key] = (C.get(key, 0) + c * e) % p
        return {e: c for e, c in C.items() if c}

    def deg(A, var):  return max((e[var] for e in A), default=-1)
    def tdeg(A):      return max((i + j for i, j in A), default=-1)

    def F_t(t):
        A = {(0, 0): 1}
        for i in range(2 * t):
            A = pmul(A, {(1, 0): 1, (0, 1): p - 1, (0, 0): (-i) % p})
        Q = {(0, 0): 1}
        for i in range(t):
            Q = pmul(Q, {(1, 0): 1, (0, 0): (-i) % p})
        R = {(0, 0): 1}
        for j in range(1, t + 1):
            R = pmul(R, {(0, 1): 1, (0, 0): j % p})
        return psub(A, pmul(Q, R))

    # ---- univariate over F_p, coefficients low -> high ----
    def trim(a):
        while a and a[-1] == 0: a.pop()
        return a

    def divmod_(a, b):
        a = a[:]; q = [0] * max(len(a) - len(b) + 1, 0)
        inv = pow(b[-1], p - 2, p)
        while len(a) >= len(b) and a:
            s = len(a) - len(b); f = a[-1] * inv % p; q[s] = f
            for i, c in enumerate(b): a[s + i] = (a[s + i] - f * c) % p
            trim(a)
        return q, a

    def gcd(a, b):
        a = trim(a[:]); b = trim(b[:])
        while b: a, b = b, divmod_(a, b)[1]
        if a:
            inv = pow(a[-1], p - 2, p); a = [c * inv % p for c in a]
        return a

    def res(a, b):
        a = trim(a[:]); b = trim(b[:])
        if not a or not b: return 0
        out = 1
        while len(b) > 1:
            da, db = len(a) - 1, len(b) - 1
            r = trim(divmod_(a, b)[1])
            if not r: return 0
            if (da * db) % 2: out = (-out) % p
            out = out * pow(b[-1], da - (len(r) - 1), p) % p
            a, b = b, r
        if not b: return 0
        return out * pow(b[0], len(a) - 1, p) % p

    def slice_k(A, nval):
        out = [0] * (deg(A, 1) + 1)
        for (i, j), c in A.items(): out[j] = (out[j] + c * pow(nval, i, p)) % p
        return trim(out)

    def res_k(A, B, bound):
        """Res_k(A,B) as a polynomial in n, by evaluation and Lagrange interpolation.

        Needs bound+1 DISTINCT nonzero points, so the prime must exceed bound+1. Without
        this guard a small prime silently wraps the evaluation points, the interpolation is
        then garbage, and the run reports a smooth curve as singular. Found at p=101, t=4.
        """
        if p <= bound + 1:
            raise ValueError(
                f"prime {p} is too small: interpolating a degree-{bound} resultant needs "
                f"{bound + 1} distinct nonzero points, so p must exceed {bound + 1}. "
                "Use a larger prime, or an elimination method that does not interpolate.")
        xs = list(range(1, bound + 2))
        ys = [res(slice_k(A, x), slice_k(B, x)) for x in xs]
        coef = [0] * (bound + 1)
        for i in range(len(xs)):
            num = [1]; den = 1
            for j in range(len(xs)):
                if i == j: continue
                new = [0] * (len(num) + 1)
                for a, c in enumerate(num):
                    new[a] = (new[a] - xs[j] * c) % p
                    new[a + 1] = (new[a + 1] + c) % p
                num = new; den = den * (xs[i] - xs[j]) % p
            f = ys[i] * pow(den, p - 2, p) % p
            for a, c in enumerate(num): coef[a] = (coef[a] + f * c) % p
        return trim(coef)

    return dict(F_t=F_t, pdiff=pdiff, deg=deg, tdeg=tdeg, gcd=gcd, res_k=res_k, trim=trim)


def certify(t, p):
    m = make(p)
    F = m["F_t"](t); D = m["tdeg"](F)
    Fn = m["pdiff"](F, 0); Fk = m["pdiff"](F, 1)

    # --- infinity: top-degree form squarefree, and [1:0] off the curve ---
    top = {(i, j): c for (i, j), c in F.items() if i + j == D}
    f = [0] * (D + 1)
    for (i, j), c in top.items(): f[i] = (f[i] + c) % p
    f = m["trim"](f)
    df = m["trim"]([(i * c) % p for i, c in enumerate(f)][1:])
    top_sqfree = len(m["gcd"](f, df)) <= 1
    c_nD = next((c for (i, j), c in top.items() if j == 0), 0) % p

    # --- affine: gcd of the two resultants ---
    b1 = m["deg"](F, 1) * m["deg"](Fn, 0) + m["deg"](Fn, 1) * m["deg"](F, 0) + 2
    b2 = m["deg"](F, 1) * m["deg"](Fk, 0) + m["deg"](Fk, 1) * m["deg"](F, 0) + 2
    R1 = m["res_k"](F, Fn, b1)
    R2 = m["res_k"](F, Fk, b2)
    g = m["gcd"](R1, R2)

    smooth = top_sqfree and c_nD != 0 and len(g) <= 1
    return dict(t=t, p=p, D=D, top_sqfree=top_sqfree, c_nD=c_nD,
                degR1=len(R1) - 1, degR2=len(R2) - 1,
                lcR1=R1[-1] if R1 else 0, lcR2=R2[-1] if R2 else 0,
                deg_gcd=len(g) - 1, smooth=smooth,
                genus=(D - 1) * (D - 2) // 2 if smooth else None)


def main(argv):
    tmax = int(argv[1]) if len(argv) > 1 else 5
    primes = [int(x) for x in argv[2:]] or [(1 << 61) - 1, (1 << 31) - 1, 101]
    print(f"F_t(n,k) = prod(n-k-i, i<2t) - prod(n-i, i<t)*prod(k+j, 1<=j<=t)\n")
    for p in primes:
        print(f"--- prime p = {p} ---")
        print(f"{'t':>2} {'deg D':>6} {'top sqfree':>11} {'lead n^D':>9} "
              f"{'deg R1':>7} {'deg R2':>7} {'deg gcd':>8} {'smooth':>7} {'genus':>6}")
        for t in range(1, tmax + 1):
            c = certify(t, p)
            print(f"{c['t']:>2} {c['D']:>6} {str(c['top_sqfree']):>11} {c['c_nD']:>9} "
                  f"{c['degR1']:>7} {c['degR2']:>7} {c['deg_gcd']:>8} "
                  f"{str(c['smooth']):>7} {str(c['genus']):>6}")
            assert c["lcR1"] % p and c["lcR2"] % p, (
                f"p divides a resultant's leading coefficient at t={t}; "
                "the characteristic-zero inference does not go through at this prime")
        print()
    print("Siegel: an affine curve has finitely many integral points when its genus is >= 1,")
    print("and also when the genus is 0 with at least three points at infinity. Genus 0 with")
    print("fewer is the case that can carry infinitely many - and t=1 is exactly that case,")
    print("with the known Fibonacci family. Do not read 'genus 0' as 'Siegel says nothing'.")

if __name__ == "__main__":
    main(sys.argv)
