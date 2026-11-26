#!/usr/bin/env python3
"""R14 verification certificate — exact, dependency-free, runnable.

Checks four things about the R14 argument for  C(n,k) = C(n-t, k+t),  t >= 2,
without reusing its algebra and without floating point:

  1. the four discrete sum identities the derivation rests on;
  2. the integrality step, 24(U-Q^2)+5t^2+1 == 6v^2-30w^2-24w+5t^2-5;
  3. the expansion coefficients a2, a3 — and three further ones, a4, a5, a6,
     which the derivation did not reach;
  4. a brute-force solution scan, with t=1 as the instrument test.

Why this is independent of the original derivation: that one goes through the
analytic (Gamma) continuation and a logarithmic expansion. This one never
leaves the rationals. Cancelling factorials turns the equation into the
POLYNOMIAL identity

    prod_{i=0}^{t-1}(n-i) * prod_{j=1}^{t}(k+j) = prod_{r=0}^{2t-1}(n-k-r)

Centre each product on its own midpoint:

    N = n - (t-1)/2,   K = k + (t+1)/2,   Q = (n-k) - t + 1/2

Then {i-(t-1)/2 : i<t} and {j-(t+1)/2 : 1<=j<=t} are the SAME symmetric set S
of t points, and {r-(2t-1)/2 : r<2t} is a symmetric set T of 2t points:

    prod_{s in S}(N-s) * prod_{s in S}(K-s) = prod_{u in T}(Q-u)

The left side is symmetric in N and K, so with U = N*K and p = N+K it is
prod_{s in S}(U + s^2 - s*p); S is symmetric, so s and -s pair into
(U+s^2)^2 - s^2 p^2 and only p^2 survives, and p^2 = (Q-1/2)^2 + 4U because
N-K = n-k-t = Q-1/2. Everything is then an exact polynomial in U and Q.

Setting U = Q^2 + A with A = a2 + a3/Q + a4/Q^2 + ... and expanding in w = 1/Q,
each order's equation is AFFINE in its one new unknown, so every a_m is pinned
exactly by evaluating that order at two trial values. Nothing is approximated.

Run:  python3 singmaster_r14_series.py
"""
from fractions import Fraction as F
from math import comb, gcd

TRUNC = 24


class L:
    """Laurent series in w = 1/Q over the rationals, truncated above TRUNC."""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = dict(c or {})

    @staticmethod
    def mono(e, v=1):
        return L({e: F(v)})

    def __add__(s, o):
        o = o if isinstance(o, L) else L.mono(0, o)
        r = dict(s.c)
        for e, v in o.c.items():
            r[e] = r.get(e, F(0)) + v
            if r[e] == 0:
                del r[e]
        return L(r)

    __radd__ = __add__

    def __neg__(s):
        return L({e: -v for e, v in s.c.items()})

    def __sub__(s, o):
        return s + (-(o if isinstance(o, L) else L.mono(0, o)))

    def __rsub__(s, o):
        return (-s) + o

    def __mul__(s, o):
        o = o if isinstance(o, L) else L.mono(0, o)
        lo = min(s.c, default=0) + min(o.c, default=0)
        r = {}
        for e1, v1 in s.c.items():
            for e2, v2 in o.c.items():
                e = e1 + e2
                if e > lo + TRUNC:
                    continue
                r[e] = r.get(e, F(0)) + v1 * v2
        return L({e: v for e, v in r.items() if v != 0})

    __rmul__ = __mul__

    def coeff(s, e):
        return s.c.get(e, F(0))


def curve_series(t, A):
    """The curve's polynomial as a Laurent series in w, given A as a series."""
    Q = L.mono(-1)
    U = Q * Q + A
    p2 = (Q - F(1, 2)) * (Q - F(1, 2)) + 4 * U
    lhs, seen = L.mono(0, 1), set()
    for s in (F(i) - F(t - 1, 2) for i in range(t)):
        if s == 0:
            lhs = lhs * U
        elif s not in seen:
            seen.add(s); seen.add(-s)
            lhs = lhs * ((U + s * s) * (U + s * s) - (s * s) * p2)
    rhs, seenT = L.mono(0, 1), set()
    for u in (F(r) - F(2 * t - 1, 2) for r in range(2 * t)):
        if u == 0:
            rhs = rhs * Q
        elif u not in seenT:
            seenT.add(u); seenT.add(-u)
            rhs = rhs * (Q * Q - u * u)
    return lhs - rhs


def coefficients(t, how_many=6):
    """a2, a3, ... exactly. Each order's equation is affine in its new unknown."""
    a = []
    for m in range(how_many):
        def order_m(trial):
            A = L({i: a[i] for i in range(len(a)) if a[i] != 0}) + L.mono(m, trial)
            return curve_series(t, A)
        g0, g1 = order_m(F(0)), order_m(F(1))
        target = next((e for e in sorted(set(g0.c) | set(g1.c))
                       if g0.coeff(e) != g1.coeff(e)), None)
        if target is None:
            a.append(F(0))
            continue
        c0, c1 = g0.coeff(target), g1.coeff(target)
        a.append(-c0 / (c1 - c0))
    return a


def lagrange(xs, ys):
    """Exact interpolating polynomial, ascending coefficients."""
    n = len(xs)
    out = [F(0)] * n
    for i in range(n):
        num = [F(1)]
        for j in range(n):
            if j == i:
                continue
            num = [(num[k - 1] if k > 0 else F(0))
                   - xs[j] * (num[k] if k < len(num) else F(0))
                   for k in range(len(num) + 1)]
        den = F(1)
        for j in range(n):
            if j != i:
                den *= xs[i] - xs[j]
        for k in range(min(len(num), n)):
            out[k] += ys[i] * num[k] / den
    return out


def show_poly(c):
    dens = [x.denominator for x in c if x != 0]
    D = 1
    for d in dens:
        D = D * d // gcd(D, d)
    body = " + ".join(f"{int(x * D)}t^{i}" for i, x in enumerate(c) if x != 0)
    return f"({body}) / {D}"


def fit_and_hold_out(vals, deg, ts, label):
    fit, test = ts[:deg + 1], ts[deg + 1:]
    c = lagrange([F(t) for t in fit], [vals[t] for t in fit])
    ev = lambda t: sum(x * F(t) ** i for i, x in enumerate(c))
    bad = [t for t in test if ev(t) != vals[t]]
    print(f"  {label} = {show_poly(c)}")
    print(f"    fitted on t={fit[0]}..{fit[-1]}, held out t={test[0]}..{test[-1]}"
          f" -> {'all agree' if not bad else 'MISMATCH at ' + str(bad)}")
    return c, not bad


def part1_sums():
    print("1. the four discrete sum identities")
    S = lambda t, m: sum((F(i) - F(t - 1, 2)) ** m for i in range(t))
    H = lambda t: sum((F(i) + F(1, 2)) ** 2 for i in range(t))
    rows = [("(1/t) sum s_i      = 0", lambda t: S(t, 1) / t, lambda t: F(0), 2),
            ("(1/t) sum s_i^2    = (t^2-1)/12", lambda t: S(t, 2) / t, lambda t: F(t * t - 1, 12), 3),
            ("(1/t) sum s_i^3    = 0", lambda t: S(t, 3) / t, lambda t: F(0), 4),
            ("(1/t) sum (i+1/2)^2 = (4t^2-1)/12", lambda t: H(t) / t, lambda t: F(4 * t * t - 1, 12), 3)]
    allok = True
    for name, lhs, rhs, deg in rows:
        bad = [t for t in range(1, 41) if lhs(t) != rhs(t)]
        allok &= not bad
        print(f"  {name:36s} deg<={deg}, {deg+1} pts suffice, 40 checked -> "
              f"{'identity' if not bad else 'FAILS at ' + str(bad[:4])}")
    print("  By Faulhaber each side is a polynomial in t of the stated degree, so")
    print("  agreement on more than deg+1 points IS the identity, not a sample.\n")
    return allok


def part2_integrality():
    print("2. the integrality step")
    direct = lambda n, k, t: 24 * ((F(n) - F(t - 1, 2)) * (F(k) + F(t + 1, 2))
                                  - (F(n) - F(k) - t + F(1, 2)) ** 2) + 5 * t * t + 1
    claimed = lambda n, k, t: 6 * (n + k + 1) ** 2 - 30 * (n - k - t) ** 2 - 24 * (n - k - t) + 5 * t * t - 5
    bad = [(n, k, t) for t in range(1, 9) for n in range(-6, 30) for k in range(-6, 30)
           if direct(n, k, t) != claimed(n, k, t)]
    print(f"  24(U-Q^2)+5t^2+1 == 6v^2-30w^2-24w+5t^2-5 on {8*36*36} integer triples -> "
          f"{'identity' if not bad else 'FAILS e.g. ' + str(bad[:3])}")
    print("  Both sides are degree 2 in n and k, so this grid settles it. v and w")
    print("  are integers, so A is an integer — the step the contradiction needs.\n")
    return not bad


def part3_coefficients(ts=tuple(range(2, 16))):
    print("3. the expansion coefficients")
    A = {t: coefficients(t, 6) for t in ts}
    ok = True
    a2bad = [t for t in ts if A[t][0] != F(-(5 * t * t + 1), 24)]
    a3bad = [t for t in ts if A[t][1] != F(-(t * t - 1), 24)]
    print(f"  a2 == -(5t^2+1)/24 for t={ts[0]}..{ts[-1]} -> {'yes' if not a2bad else 'NO at ' + str(a2bad)}")
    print(f"  a3 == -(t^2-1)/24  for t={ts[0]}..{ts[-1]} -> {'yes' if not a3bad else 'NO at ' + str(a3bad)}")
    ok &= not a2bad and not a3bad
    print("  beyond the derivation:")
    for idx, name, deg in ((2, "a4", 4), (3, "a5", 4), (4, "a6", 6)):
        vals = {t: A[t][idx] for t in ts}
        _, good = fit_and_hold_out(vals, deg, list(ts), name)
        q = {t: vals[t] / F(t * t - 1) for t in ts}
        _, goodq = fit_and_hold_out(q, deg - 2, list(ts), f"{name}/(t^2-1)")
        print(f"    => (t^2-1) divides {name}: {'yes' if goodq else 'not established'}")
        ok &= good and goodq
    print("  a3..a6 all carry the factor (t^2-1), which is exactly 0 at t=1 — the")
    print("  one case the theorem excludes, and the one with a known infinite family.\n")
    return ok


def part4_scan(nmax=1200, tmax=10):
    """Scope is the DEFAULT, not a smaller run described as a larger one.

    TOTO's R15 review caught this file reporting a scan to n=1200 over t<=10
    while defaulting to n=600 over t<=8, and caught the scan not failing when
    it met a solution it did not expect. Both are fixed here: the defaults are
    the reported scope, and an unexpected hit returns False, which the exit
    status below turns into a non-zero exit.
    """
    print(f"4. brute-force scan, n <= {nmax}, t <= {tmax}  (this is the default scope)")

    def scan(t):
        out = []
        for n in range(2 * t + 2, nmax + 1):
            for k in range(1, n // 2 + 1):
                l = k + t
                if l > n - t:
                    break
                if comb(n, k) == comb(n - t, l):
                    out.append((n, k))
        return out

    control = scan(1)
    print(f"  t=1 (instrument test — known solutions must appear): "
          f"{', '.join(f'C({n},{k})=C({n-1},{k+1})' for n, k in control) or 'NONE FOUND — SCANNER BROKEN'}")
    if not control:
        print("  FAIL: the scanner found none of the known t=1 solutions, so its")
        print("        silence at t>=2 would say nothing about the equation.")
        return False
    surprises = {}
    for t in range(2, tmax + 1):
        hits = scan(t)
        print(f"  t={t}: {hits if hits else 'no solution'}")
        if hits:
            surprises[t] = hits
    if surprises:
        print(f"  FAIL: solutions found for t>=2: {surprises}")
        print("        That is a counterexample to the expectation this file was")
        print("        written to test. It must stop the run, not be narrated.")
        return False
    print("  The only hits are at t=1, where the obstruction above vanishes.\n")
    return True


# ---------------------------------------------------------------------------
# Added after TOTO's R15 review. Her two claims, checked rather than accepted,
# and the two steps that close the finiteness argument.
# ---------------------------------------------------------------------------

def _pmul(a, b):
    r = {}
    for (i1, j1), v1 in a.items():
        for (i2, j2), v2 in b.items():
            k = (i1 + i2, j1 + j2)
            r[k] = r.get(k, F(0)) + v1 * v2
    return {k: v for k, v in r.items() if v != 0}


def _padd(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, F(0)) + s * v
        if r[k] == 0:
            del r[k]
    return r


_ONE = {(0, 0): F(1)}


def curve_poly(t, in_W=False):
    """The curve as an exact polynomial. Variables (U,Q), or (W,Q) with W = A_int."""
    Q = {(0, 1): F(1)}
    if in_W:
        W = {(1, 0): F(1)}
        U = _padd(_pmul(Q, Q), _padd(W, _ONE, F(-(5 * t * t + 1))), F(1, 24))
    else:
        U = {(1, 0): F(1)}
    p2 = _padd(_pmul(_padd(Q, _ONE, -F(1, 2)), _padd(Q, _ONE, -F(1, 2))), U, 4)
    lhs, seen = dict(_ONE), set()
    for sv in (F(i) - F(t - 1, 2) for i in range(t)):
        if sv == 0:
            lhs = _pmul(lhs, U)
        elif sv not in seen:
            seen.add(sv); seen.add(-sv)
            Us2 = _padd(U, _ONE, sv * sv)
            lhs = _pmul(lhs, _padd(_pmul(Us2, Us2), p2, -(sv * sv)))
    rhs, seenT = dict(_ONE), set()
    for uv in (F(r) - F(2 * t - 1, 2) for r in range(2 * t)):
        if uv == 0:
            rhs = _pmul(rhs, Q)
        elif uv not in seenT:
            seenT.add(uv); seenT.add(-uv)
            rhs = _pmul(rhs, _padd(_pmul(Q, Q), _ONE, -(uv * uv)))
    return _padd(lhs, rhs, -1)


def part5_branch(ts=tuple(range(1, 10))):
    """TOTO: with h=1/Q and z=U/Q^2, G_t(z,0) = z^t - 1 and dG/dz(1,0) = t != 0.

    Also proved in general, not only checked here: under the grading
    deg U = 2, deg Q = 1, the top-degree part of the curve is U^t - Q^(2t),
    which becomes Q^(2t)(z^t - 1). The loop confirms the algebra per t.
    """
    print("5. the normalised branch (TOTO's R15 item 2)")
    ok = True
    for t in ts:
        C = curve_poly(t)
        M = max(2 * i + j for (i, j) in C)
        g = {}
        for (i, j), v in C.items():
            if 2 * i + j == M:
                g[i] = g.get(i, F(0)) + v
        g = {k: v for k, v in g.items() if v != 0}
        lead = g[max(g)]
        gn = {k: v / lead for k, v in g.items()}
        want = {t: F(1), 0: F(-1)}
        at1 = sum(gn.values())
        dz1 = sum(k * v for k, v in gn.items())
        good = gn == want and at1 == 0 and dz1 == t
        ok &= good
        print(f"  t={t:2d}  G_t(z,0) = z^{t} - 1 : {'yes' if gn == want else 'NO'}   "
              f"G_t(1,0) = {at1}   dG/dz(1,0) = {dz1}  {'ok' if good else 'FAIL'}")
    print("  So the implicit function theorem applies at (z,h)=(1,0) and supplies a")
    print("  genuine convergent branch - which is what makes the expansion asymptotic")
    print("  rather than formal, and therefore what proves finiteness.\n")
    return ok


def part6_t1_identity():
    """TOTO: at t=1 the curve IS U = Q^2 - 1/4, so A_int = 0 on all of it."""
    print("6. t=1 (TOTO's R15 item 3)")
    C = curve_poly(1)
    target = {(1, 0): F(1), (0, 2): F(-1), (0, 0): F(1, 4)}   # U - Q^2 + 1/4
    same = C == target
    print(f"  curve(1) == U - Q^2 + 1/4 as polynomials: {'yes' if same else 'NO'}")
    print(f"  hence A_int = 24(U-Q^2) + 5 + 1 = 24*(-1/4) + 6 = {24 * F(-1, 4) + 6}"
          f" identically on the whole curve")
    print("  My own earlier finding was A_int = 0 at the two known solutions. That")
    print("  was the two-point shadow of this exact identity, which is hers.\n")
    return same


def part7_z_range(nmax=400, tmax=10):
    """0 < z < 2 on the admissible range, so z approaches a POSITIVE root of z^t=1.

    Proved in general too: k+t <= n-t-(k+t) gives k <= (n-3t)/2, hence
    K <= (n-2t+1)/2, N <= n and Q >= (n+t+1)/2, so
        z = NK/Q^2 <= 2n(n-2t+1)/(n+t+1)^2 < 2.
    The only positive real root of z^t = 1 is z = 1, so z -> 1 is forced and no
    other root of the limit polynomial can be approached.
    """
    print(f"7. the admissible range of z = U/Q^2  (n <= {nmax}, t <= {tmax})")
    ok = True
    for t in range(1, tmax + 1):
        lo = hi = None
        for n in range(2 * t + 2, nmax + 1):
            for k in range(0, n + 1):
                if k + t > n - t - (k + t):
                    break
                N = F(n) - F(t - 1, 2)
                K = F(k) + F(t + 1, 2)
                Q = F(n) - F(k) - t + F(1, 2)
                if Q <= 0:
                    continue
                z = N * K / (Q * Q)
                lo = z if lo is None or z < lo else lo
                hi = z if hi is None or z > hi else hi
        good = lo is not None and lo > 0 and hi < 2
        ok &= good
        print(f"  t={t:2d}  z in ({float(lo):.6f}, {float(hi):.6f})  "
              f"{'0 < z < 2' if good else 'OUT OF RANGE'}")
    print("  z lies in (0,2), whose closure [0,2] IS compact, so limit points exist")
    print("  there; 0 and 2 are not roots of z^t = 1, so the limit point is interior")
    print("  and equals 1. (TOTO's item 4: (0,2) itself is not compact. Corrected.)\n")
    return ok


def _poly_Q(t, eps):
    """P_t(U,Q) at U = Q^2 - (5t^2+1+eps)/24, as coefficients in Q (ascending).

    TOTO's product form, which is better than the one I had: pairing (n-i) with
    (k+i+1) gives (N-s_i)(K+s_i) = U + s_i(Q-1/2) - s_i^2, LINEAR in U, so no
    p = N+K ever appears and no p^2 substitution is needed.
    """
    def mul(a, b):
        r = [F(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        r[i + j] += x * y
        return r
    c = F(-(5 * t * t + 1 + eps), 24)
    lhs = [F(1)]
    for i in range(t):
        sv = F(i) - F(t - 1, 2)
        lhs = mul(lhs, [c - sv / 2 - sv * sv, sv, F(1)])
    rhs = [F(1)]
    for i in range(t):
        h = F(2 * i + 1, 2)
        rhs = mul(rhs, [-h * h, F(0), F(1)])
    n = max(len(lhs), len(rhs))
    out = [(lhs[i] if i < len(lhs) else F(0)) - (rhs[i] if i < len(rhs) else F(0))
           for i in range(n)]
    while out and out[-1] == 0:
        out.pop()
    return out


def part8_bracket(tmax=18):
    """R16. The bracket, from leading coefficients rather than a grid.

    TOTO's R15 items 2 and 3 were right about the previous version of this: a
    FIRST sign change does not establish persistent separation, and sampling
    dP/dW on a grid while discarding zeros is not monotonicity. Both are gone.
    What replaces them is exact and general:

      * monotonicity:  dP/dU = sum_i prod_{j!=i}(U+b_j) > 0 wherever every
        factor is positive. On an admissible integer solution each factor IS
        (n-i)(k+i+1), a product of positive integers, so it holds with no
        condition; at the bracket endpoints Q >= t+1 suffices, checked below.
      * endpoint signs: both endpoint polynomials have an exact degree and an
        exact leading coefficient, so their sign for large Q is decided, not
        sampled. Cauchy's bound then turns that into an EXPLICIT threshold.
    """
    print("8. the direct bracket, from exact leading coefficients (R16)")
    ok = True
    print(f"  {'t':>3} {'deg/lead at W=0':>26} {'deg/lead at W=-1':>22} {'minQ all factors>0':>19}")
    for t in range(2, tmax + 1):
        p0, p1 = _poly_Q(t, 0), _poly_Q(t, 1)
        d0, l0, d1, l1 = len(p0) - 1, p0[-1], len(p1) - 1, p1[-1]
        want0, want1 = F(t * (t * t - 1), 24), F(-t, 24)
        good = (d0 == 2 * t - 3 and l0 == want0 and d1 == 2 * t - 2 and l1 == want1
                and l0 > 0 and l1 < 0)
        minq = None
        for m in range(0, 200):
            q = F(2 * m + 1, 2)
            if all(q * q + (F(i) - F(t - 1, 2)) * q
                   + (F(-(5 * t * t + 1 + e), 24) - (F(i) - F(t - 1, 2)) / 2
                      - (F(i) - F(t - 1, 2)) ** 2) > 0
                   for e in (0, 1) for i in range(t)):
                minq = q
                break
        good &= minq is not None and minq <= t + 1
        ok &= good
        if t <= 8 or t == tmax:
            print(f"  {t:3d} {str(d0) + ' / ' + str(l0):>26} {str(d1) + ' / ' + str(l1):>22}"
                  f" {str(minq):>19}  {'ok' if good else 'FAIL'}")
    print("  deg/lead at W=0  == 2t-3 and t(t^2-1)/24 = C(t+1,3)/4 > 0 for t >= 2")
    print("  deg/lead at W=-1 == 2t-2 and -t/24 < 0")
    print("  t(t^2-1)/24 is exactly -t*a3, so it vanishes at t=1: the same")
    print("  obstruction gates the effective argument as gates the asymptotic one.")
    print("  Q >= t+1 puts both endpoints inside the positivity half-line.")
    print()
    print("  explicit PROVED thresholds (Cauchy: Q > 1 + max|c_j|/|c_d| fixes the sign)")
    print(f"  {'t':>3} {'Q0 proved':>16} {'n <= 2Q0-t-1':>16} {'within the scan below?':>23}")
    for t in range(2, 7):
        qs = []
        for eps in (0, 1):
            p = _poly_Q(t, eps)
            qs.append(1 + max((abs(c) for c in p[:-1]), default=F(0)) / abs(p[-1]))
        q0 = max(qs)
        nb = 2 * q0 - t - 1
        print(f"  {t:3d} {float(q0):16.1f} {float(nb):16.1f} {('yes' if nb <= 1200 else 'no'):>23}")
    print("  Cauchy is a worst-case bound, so these sit far above the first sign")
    print("  change. They are crude and PROVED; the observed threshold is sharp and")
    print("  is NOT. Only the proved ones may be combined with the scan.\n")
    return ok


if __name__ == "__main__":
    import sys
    checks = [
        ("sum identities", part1_sums),
        ("integrality", part2_integrality),
        ("coefficients", part3_coefficients),
        ("normalised branch", part5_branch),
        ("t=1 is exactly U=Q^2-1/4", part6_t1_identity),
        ("0 < z < 2 on the admissible range", part7_z_range),
        ("bracket and monotonicity", part8_bracket),
        ("brute-force scan", part4_scan),
    ]
    failed = [name for name, fn in checks if not fn()]
    if failed:
        print("FAILED: " + ", ".join(failed))
        sys.exit(1)
    print("ALL CHECKS PASSED")
    sys.exit(0)
