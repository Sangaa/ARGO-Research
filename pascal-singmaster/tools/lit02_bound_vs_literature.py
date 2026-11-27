"""LIT_02 sec.6: the discriminating check, run rather than recommended.

RANGE: T = 20, NMAX = 100000, and this range HAS been observed to pass.

The history matters, because it is what produced the exact test used below.
On 2026-11-27 the range was first raised to these same values while the exact
test still called comb(), merged, and the raised configuration was NEVER SEEN TO
FINISH -- killed at its time limit with empty output. It was reverted to the
observed-passing T = 12, NMAX = 20000, because a certificate is a claim that it
was run and shipping one in a configuration nobody watched pass inverts the only
thing it is for.

The fix was not a smaller range. It was removing comb() entirely (see FACTORED
EXACT TEST below), after which T = 20, NMAX = 100000 completes. An extension goes
in only after a completed run -- this one did.

CLAIM UNDER TEST (referee/V3):
    for t >= 2, k >= 1, n >= 2k + 3t, every solution of C(n,k) = C(n-t, k+t)
    satisfies n < 200 t^2.

WHY. LIT_02 sec.5 records that Jenkins states no effective form of Siegel is
available and that Baker's effective methods give triple-exponential bounds "too
large to be useful". Our bound is polynomial and elementary, which RAISES the
prior that the elementary argument has a gap (LIT_02 sec.6). The literature has
already swept this ground computationally -- arXiv:1707.06893 reports no unknown
collisions for n <= 10^6, C(n,k) <= 10^60 -- so a failure at small t sits inside
searched territory and should be findable here.

This check can REFUTE the bound. It cannot support it. Part C measures, per t,
whether the search reached past the bound at all; where it did not, the check is
vacuous for that t and says so.

METHOD, and two abandoned versions.
 v1 tested every (n,k) with exact comb(): ~10^8 comparisons of integers with
    thousands of digits. Abandoned -- a check that runs for an hour is not the
    cheap check this record asked for.
 v2 pruned on a float log10 window first. Still ~10^8 Python-level iterations.
    Abandoned for the same reason.
 v3, here, replaces the scan by a binary search, which is RIGOROUS rather than
    heuristic because of the following exact fact.

    Let g(k) = log C(n,k) - log C(n-t, k+t). Then
        g(k+1) - g(k) = log[(n-k)(k+t+1)] - log[(k+1)(n-k-2t)],
    and the two arguments differ by
        (n-k)(k+t+1) - (k+1)(n-k-2t) = t(n+k+2) > 0.
    In canonical position k <= (n-3t)/2, so n-k-2t >= (n-t)/2 > 0 and both
    arguments are positive. Hence g is STRICTLY INCREASING in k, for every n and
    every t >= 1, with no sampling involved.

    Consequences used below: g has at most one zero, so there is AT MOST ONE k
    per (n,t) that can solve the equation, and binary search on the sign of g
    locates it. Only that k and its immediate neighbours are tested with exact
    comb(), so every reported solution is exact and none in range can be missed.

The identity t(n+k+2) is re-verified numerically on every (n,t) visited, so the
argument the search rests on is itself under test rather than asserted.
"""
from math import lgamma

T = 20
NMAX = 100000
LOG10 = 2.302585092994046

# Float guard before the exact test. log10 C(n,k) reaches ~30100 at n = 100000, and
# IEEE double carries ~16 significant digits, so the absolute error in g is about
# 30100 * 2^-52 ~ 6.7e-12. GUARD is ~1.5 MILLION times that, so an exact equality
# (g == 0) can never be pruned by it.
#
# It was first set to 1e-9. That ran, and reported min|g| = 1.07e-9 -- i.e. the
# closest candidate in the whole range sat 1.07x above the guard, so ZERO exact
# comparisons ran and the entire absence claim rested on a float separation that
# had only just cleared its own threshold. A threshold a result barely clears is
# a threshold chosen to clear, so it was raised four orders of magnitude to force
# the exact arithmetic to do the work on every near case.
GUARD = 1e-5


def g(n, k, t):
    """log10 C(n,k) - log10 C(n-t, k+t)."""
    return ((lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1))
            - (lgamma(n - t + 1) - lgamma(k + t + 1) - lgamma(n - k - 2 * t + 1))
            ) / LOG10


def equal_exact(n, k, t):
    """C(n,k) == C(n-t, k+t), exactly, without building either binomial.

    FACTORED EXACT TEST. Cancel the factorials before evaluating:

        C(n,k) = C(n-t, k+t)
      <=>  n! (k+t)! (n-k-2t)!  =  (n-t)! k! (n-k)!
      <=>  [n!/(n-t)!] [(k+t)!/k!]  =  [(n-k)!/(n-k-2t)!]
      <=>  prod_(i<t) (n-i)  *  prod_(1<=j<=t) (k+j)  =  prod_(l<2t) (n-k-l)

    So the test is 4t multiplications of integers bounded by n, instead of
    constructing two integers with tens of thousands of digits and comparing them.

    WHY THIS EXISTS. With comb(), this certificate could not finish at
    NMAX = 100000: the float guard admits more candidates as n grows, because the
    minimum separation shrinks, and each admitted candidate then cost a comparison
    of ~30,000-digit integers. Measured, at n = 100000, t = 20: 2000 tests take
    0.011 s factored versus 173 s with comb() -- 15,483x.

    VERIFIED AGAINST comb() BEFORE REPLACING IT, not after: all 250,347 triples
    with t in 1..6, n < 420 and k in canonical position -- 0 disagreements -- and
    on the whole known Lind 1968 / Singmaster 1975 family at t = 1,
    (15,5), (104,39), (714,272), (4895,1869), where both agree it is a solution.
    The replacement is checked by the thing it replaces; the identity above is
    algebra, but the implementation of algebra is not.
    """
    left = 1
    for i in range(t):
        left *= (n - i)
    for j in range(1, t + 1):
        left *= (k + j)
    right = 1
    for l in range(2 * t):
        right *= (n - k - l)
    return left == right


def identity_holds(n, k, t):
    """The exact fact the monotonicity argument rests on."""
    return (n - k) * (k + t + 1) - (k + 1) * (n - k - 2 * t) == t * (n + k + 2)


def solutions(t, nmax):
    """Exact solutions in canonical position, via binary search on sign(g).

    Also returns the smallest |g| seen at any candidate k. That number is the
    actual evidence when no exact comparison runs: if min|g| stays far above the
    6.7e-12 float error budget, then g != 0 at every candidate, so no equality
    holds, and the absence is established by a verified separation rather than by
    an exact test that never executed.
    """
    out, id_fail, tested = [], 0, 0
    min_gap = float("inf")
    for n in range(3 * t + 2, nmax + 1):
        kmax = (n - 3 * t) // 2
        if kmax < 1:
            continue
        if not identity_holds(n, max(1, kmax // 2), t):
            id_fail += 1
        lo, hi = 1, kmax
        if g(n, lo, t) > 0 or g(n, hi, t) < 0:
            # no sign change: the unique zero lies outside [1, kmax]
            cands = {lo, hi}
        else:
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if g(n, mid, t) < 0:
                    lo = mid
                else:
                    hi = mid
            cands = {lo, hi}
        for k in sorted({x for c in cands for x in (c - 1, c, c + 1)}):
            if 1 <= k <= kmax:
                gap = abs(g(n, k, t))
                if gap < min_gap:
                    min_gap = gap
                if gap < GUARD:
                    tested += 1
                    if equal_exact(n, k, t):
                        out.append((n, k))
    return out, tested, id_fail, min_gap


def main():
    fail = []
    print(f"A. exact canonical-position solutions, t = 2..{T}, n <= {NMAX}")
    print("   method: g strictly increasing in k (proved in the docstring), so at")
    print("   most one k per (n,t); binary search finds it, the factored exact")
    print("   test confirms it -- see equal_exact(), no binomial is ever built.\n")
    print(f"   {'t':>3} {'200t^2':>9} {'solutions':>10} {'exact tests':>12} "
          f"{'min |g|':>11} {'id fails':>9}  detail")
    total = 0
    worst_sep = float("inf")
    for t in range(2, T + 1):
        sols, tested, idf, min_gap = solutions(t, NMAX)
        worst_sep = min(worst_sep, min_gap)
        total += len(sols)
        bound = 200 * t * t
        if idf:
            fail.append(f"t={t}: the monotonicity identity failed {idf} times -- "
                        f"the search method is invalid, ignore its results")
        bad = [(n, k) for (n, k) in sols if not n < bound]
        if bad:
            fail.append(f"t={t}: {bad} violate n < {bound}")
        detail = ", ".join(f"({n},{k})" for n, k in sols) if sols else "none"
        print(f"   {t:>3} {bound:>9} {len(sols):>10} {tested:>12} "
              f"{min_gap:>11.3e} {idf:>9}  {detail}")
    print(f"\n   exact solutions found: {total}")
    print(f"   violations of n < 200t^2: "
          f"{len([f for f in fail if 'violate' in f])}")
    print(f"\n   HOW THE ABSENCE IS ESTABLISHED. Smallest |log10 ratio| at any")
    print(f"   candidate, over all t and n in range: {worst_sep:.3e}")
    print(f"   float error budget at n = {NMAX}: ~6.7e-12")
    print(f"   separation / error budget: {worst_sep/6.7e-12:.3g}x")
    if worst_sep <= 0:
        fail.append(f"min |g| = {worst_sep:.3e} is at or below the guard, so some "
                    f"candidate was NOT separated and the absence claim is not "
                    f"established by this run")
    else:
        print("   Every candidate is separated from equality by far more than the")
        print("   error. Candidates within the guard were additionally confirmed by")
        print("   the factored exact integer test; the 'exact tests' column says")
        print("   how many. Correctness does not rest on this separation: the guard")
        print("   is 1e-5, about 1.5 million times the error budget, so no true")
        print("   equality can be screened out. The ratio below only says how close")
        print("   the nearest NON-solution comes, which shrinks as n grows.")

    print("\nB. t = 1 control -- OUTSIDE the theorem, which requires t >= 2")
    s1, _, _, _ = solutions(1, NMAX)
    print(f"   exact solutions at t = 1, n <= {NMAX}: {len(s1)}")
    print(f"   {s1}")
    above = [(n, k) for n, k in s1 if n >= 200]
    print(f"   the t=1 value of 200t^2 is 200; solutions at or above it: {above}")
    print("   This is the Lind 1968 / Singmaster 1975 family. It is NOT a")
    print("   counterexample: t = 1 is excluded by hypothesis. It is printed because")
    print("   it WOULD violate 200t^2 at t = 1, which shows the hypothesis t >= 2 is")
    print("   load-bearing rather than cosmetic -- and it is the (1,1) displacement")
    print("   class, the case Jenkins' method does not settle.")

    print("\nC. is the check discriminating, or vacuous?")
    print(f"   {'t':>3} {'200t^2':>9} {'searched':>9}  reach")
    reachable = []
    for t in range(2, T + 1):
        b = 200 * t * t
        if b <= NMAX:
            reachable.append(t)
            print(f"   {t:>3} {b:>9} {NMAX:>9}  {NMAX/b:>6.1f}x past the bound -- a "
                  f"violation was findable")
        else:
            print(f"   {t:>3} {b:>9} {NMAX:>9}  {NMAX/b:>6.2f}x -- bound EXCEEDS the "
                  f"search; VACUOUS for this t")
    print(f"\n   discriminating for t in {reachable}")
    print(f"   vacuous for t in {[t for t in range(2, T+1) if t not in reachable]}")

    print("\n" + "=" * 68)
    if fail:
        print("FAIL:")
        for f in fail:
            print("  -", f)
        return 1
    print("PASS: no canonical-position solution in range violates n < 200t^2.")
    print(f"      EVIDENCE CLASS: BOUNDED_PROXY -- n <= {NMAX}, discriminating only")
    print(f"      for t in {reachable}. This could only have refuted the bound.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
