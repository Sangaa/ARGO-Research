#!/usr/bin/env python3
"""R17 certificate: the arithmetic lattice, the widened bracket, and the scan.

Self-contained, exact, no dependencies. Run: python3 <this file>

Three things, each of which exits non-zero on disagreement:

  A. W = 6v^2 - 30w^2 - 24w + 5t^2 - 5 is congruent to 5(t^2-1) mod 6, and with
     the parity tie v + w = 1 + t (mod 2) the achievable residues mod 24 leave a
     WIDER value-free interval around 0 than the (-1,0) the R16 argument used.
  B. At the endpoint W = w_0 the Q^(2t-2) coefficient of P_t is +t*w_0/24, so a
     permitted positive endpoint is non-degenerate while W = 0 is not.
  C. The scan is O(log n) per row, because after factorials cancel

         L(k) = prod_{i<t}(n-i) * prod_{j=1..t}(k+j) - prod_{r<2t}(n-k-r)

     is STRICTLY INCREASING in k on the admissible range - the first product
     grows with k, the second shrinks - so each row has at most one root and
     bisection finds it with small integers and no binomials. That is what makes
     an exhaustive scan to each t's own proved bound feasible.

An exhaustive scan to an arbitrary limit proves nothing. A scan to the proved
bound proves non-existence, which is why the bound and the scan are in one file.
"""
from fractions import Fraction as F
import sys

# ---------- A. the lattice ----------

def achievable_residues(t, M):
    """{W mod M} over integers v,w obeying v + w = 1 + t (mod 2)."""
    out = set()
    for v in range(2 * M):
        for w in range(2 * M):
            if (v + w - 1 - t) % 2:
                continue
            out.add((6 * v * v - 30 * w * w - 24 * w + 5 * t * t - 5) % M)
    return out


def free_interval(residues, M):
    """Largest open (-L, R) containing no integer in those classes."""
    inside = lambda x: (x % M) in residues
    R = 0
    while not inside(R):
        R += 1
    L = 1
    while not inside(-L):
        L += 1
    return L, R

# ---------- B. the endpoint polynomials ----------

def endpoint_poly(t, w0):
    """P_t at W = w0, i.e. U = Q^2 + (w0 - 5t^2 - 1)/24. Coefficients in Q."""
    def mul(a, b):
        r = [F(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        r[i + j] += x * y
        return r
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
    out = [(left[i] if i < len(left) else F(0)) - (right[i] if i < len(right) else F(0))
           for i in range(n)]
    while out and out[-1] == 0:
        out.pop()
    return out


def cauchy_threshold(p):
    """Q > this fixes sign(P) = sign(leading coefficient). Explicit and proved."""
    return 1 + max((abs(c) for c in p[:-1]), default=F(0)) / abs(p[-1])


def factors_positive_from(t, w0):
    """Smallest half-integer Q making every factor positive at this endpoint."""
    c = F(w0 - 5 * t * t - 1, 24)
    for m in range(0, 400):
        q = F(2 * m + 1, 2)
        if all(q * q + (F(i) - F(t - 1, 2)) * q
               + (c - (F(i) - F(t - 1, 2)) / 2 - (F(i) - F(t - 1, 2)) ** 2) > 0
               for i in range(t)):
            return q
    return None

# ---------- C. the scan ----------

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
    """The unique admissible k with _diff = 0, by bisection on the monotone L."""
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

    print("A. the arithmetic lattice W lives on")
    print(f"  {'t':>3} {'t%6':>4} {'W mod 6':>9} {'mod-6 free':>12} {'mod-24 free':>13}")
    brackets = {}
    for t in range(1, 15):
        r6 = achievable_residues(t, 6)
        l6, u6 = free_interval(r6, 6)
        l24, u24 = free_interval(achievable_residues(t, 24), 24)
        brackets[t] = (l24, u24)
        expect6 = (5 * (t * t - 1)) % 6
        if r6 != {expect6}:
            bad.append(f"residues mod 6 at t={t}")
        if (l24, u24) < (l6, u6):
            bad.append(f"mod 24 narrower than mod 6 at t={t}")
        print(f"  {t:3d} {t%6:4d} {expect6:9d} {'(-'+str(l6)+','+str(u6)+')':>12}"
              f" {'(-'+str(l24)+','+str(u24)+')':>13}")
    print("  The parity tie v+w = 1+t (mod 2) is what lets modulus 24 say more")
    print("  than modulus 6. Where 0 is itself permitted the upper end stays at 0.")
    print()

    print("B. endpoint degrees, leading coefficients, positivity and thresholds")
    print(f"  {'t':>3} {'bracket':>10} {'lead at -L':>13} {'lead at +R':>13}"
          f" {'minQ pos':>9} {'t+1':>4} {'n bound':>14}")
    bounds = {}
    for t in range(2, 11):
        L, R = brackets[t]
        pl, pr = endpoint_poly(t, -L), endpoint_poly(t, R)
        ll, lr = pl[-1], pr[-1]
        if ll != F(-t * L, 24) or ll >= 0:
            bad.append(f"lower leading coefficient at t={t}")
        if R > 0 and (lr != F(t * R, 24) or lr <= 0):
            bad.append(f"upper leading coefficient at t={t}")
        if R == 0 and (lr != F(t * (t * t - 1), 24) or lr <= 0):
            bad.append(f"degenerate upper leading coefficient at t={t}")
        mq = max(factors_positive_from(t, -L), factors_positive_from(t, R))
        if mq is None or mq > t + 1:
            bad.append(f"endpoint positivity at t={t}")
        q0 = max(cauchy_threshold(pl), cauchy_threshold(pr))
        nb = int(2 * q0 - t - 1) + 1
        bounds[t] = nb
        print(f"  {t:3d} {'(-'+str(L)+','+str(R)+')':>10} {str(ll):>13} {str(lr):>13}"
              f" {str(mq):>9} {t+1:>4} {nb:>14}")
    print("  lead at W=-L is -tL/24 < 0 and at W=+R is +tR/24 > 0; where R = 0 the")
    print("  degree drops to 2t-3 with leading t(t^2-1)/24 > 0 (t >= 2).")
    print()

    print("C. exhaustive scan to each t's OWN proved bound")
    control = scan(1, 1200)
    print(f"  control t=1 to n=1200: {control}")
    if len(control) < 3:
        bad.append("the t=1 control did not reproduce the known family")
    closed = []
    for t in range(2, 11):
        nb = bounds[t]
        if nb > 200000:
            print(f"  t={t}: proved bound {nb} is beyond this file's budget - not claimed")
            continue
        hits = scan(t, nb)
        if hits:
            bad.append(f"solution found at t={t}: {hits}")
            print(f"  t={t}: SOLUTIONS FOUND to n={nb}: {hits}")
        else:
            closed.append(t)
            print(f"  t={t}: no solution up to the proved bound n={nb}  -> CLOSED")
    print()
    print(f"  non-existence established for t = {closed}")
    if bad:
        print("\nFAILED:")
        for b in bad:
            print("  -", b)
        return 1
    print("\nALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
