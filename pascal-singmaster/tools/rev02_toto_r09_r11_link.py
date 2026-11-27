"""REV-02: the one mechanism behind TOTO's R09, R10 and R11, measured.

R11 reports that its fixed-radius asymptotic C_r(n) ~ r^2/(2n) converges slowly and
NON-monotonically at small r -- the normalized ratio for r = 1/8 runs
0.677 (n=40) -> 0.579 (n=80) -> 0.719 (n=160) -- and says, correctly, that this "is
not a failure of a fixed-radius asymptotic, nor evidence of monotonic convergence".
It does not say what the mechanism is.

This script measures it. The claim it establishes:

  FOR r <= 1/2, THE l1 THRESHOLD OF THE DISK IS SET BY THE OBJECTS R09 AND R10
  ALREADY FOUND, AND IT DOES NOT DEPEND ON n.

The restriction to r <= 1/2 is not cosmetic and was not in the first draft of this
script. The first draft asserted the identification at every radius and FAILED on
its own r = 1 row: there the threshold l1 = 2 is realised by (-1,0,0,-1), while
R10's Pell vector of that same l1, (1,0,1,0), has |z| = 1.414 and does not fit
inside radius 1 at all. A generic short vector suffices when the disk is wide. So
r = 1 is the control showing the mechanism switches on BELOW a radius, and it is
also the row R11 measures as converging best. The claim was narrowed to what the
measurement supports instead of the test being loosened to let it pass.

Specifically, for the exact difference set of the regular-octagon walk:
  * min { ||k||_1 : k != 0, ||k||_1 even, |z(k)| <= r } is a step function of r
    ALONE. Measured identical at M = 20, 40, 80 (that is n = 10, 20, 40).
  * at r = 1/2 the minimisers are R09's shortest kernel generators, l1 = 6;
  * at r = 1/4 the minimiser is R10's Pell vector j = 2, (3,-4,3,0), exactly;
  * at r = 1/8 it is R10's Pell vector j = 3, (7,-10,7,0), exactly;
  * each threshold is realised by exactly 8 vectors -- one symmetry orbit.

A PREDICTION OF THIS RECORD'S OWN FIRST DRAFT, AND ITS REFUTATION.
The first draft concluded that R10's Pell family indexes the threshold at every
small radius, and predicted l1 = 58 (R10's j = 4) at r = 1/16. Measured: the
threshold is 34, realised by (-12,5,5,-12), which is not in R10's family at all.
The prediction was wrong and was tested here before being offered to TOTO.

The corrected picture is better. There are TWO interleaved extremal families:
  A = R10's (u_j, 2v_j, u_j, 0), with algebraic norm A^2-2B^2 = 4;
  B = (-P_(i+1), P_i, P_i, -P_(i+1)) over Pell numbers P, with norm 2.
Taking min(A, B) predicts the measured threshold EXACTLY at every radius tested
from 1/2 down to 1/128 -- SEVEN radii, no exception. The winner alternates
B, A, A, B, B, B, A as r halves, with no pattern established for the alternation.

At r = 1/128 the measured minimiser is (-140, 99, 0, -99), of shape (-p, q, 0, -q)
rather than family A's (u, 2v, u, 0). Same l1 = 338 and same norm 4: it is a
symmetry image of family A's j = 6 vector, not a third family. The octagon's
8-element symmetry group permutes coordinates, so each threshold is realised by a
whole orbit and the representative the search returns first is arbitrary.

Why two: R10 asks "given l1 <= 2n, how small can |z| be" and the answer is the
Pell UNITS. The disk asks the dual question, "given |z| <= r, how small can l1
be", and the dual optimum is a different family. Conflating the two is what made
the first prediction fail.

Consequence, and this is why R11's small-r rows are slow: the path multiplicity
w(k) of the 2n-step walk is overwhelmingly concentrated at small l1, and a disk of
radius 1/8 contains NO vector with l1 < 24 at any n. It therefore misses the
dominant mass by construction rather than by sampling noise. Measured below: at
n = 40 the r = 1/8 disk carries 6.0e-4 of the r = 1 mass where its area ratio is
1/64 = 1.56e-2 -- a deficit of about 26x -- while r = 1/2 and r = 1/4 have already
reached their area ratios to within 2%.

So the small-r convergence rate is governed by how well sqrt(2) is approximated by
rationals, through the Pell units of Z[sqrt(2)]. It is a Diophantine effect, not a
statistical one, and R10 had already computed the governing family.

python3 -I tools/rev02_toto_r09_r11_link.py   -- standard library only, no network.
Exits non-zero if any claim fails. Every population size is printed by the script.
"""
from math import comb

# ---------------------------------------------------------------- exact predicates
def AB(k):
    """|z|^2 = A + B*sqrt(2) for z = a + b*zeta + c*zeta^2 + d*zeta^3."""
    a, b, c, d = k
    return a*a + b*b + c*c + d*d, a*(b - d) + c*(b + d)


def leq_r2(k, num, den):
    """Exact test |z(k)|^2 <= num/den, by integer comparison of radicals."""
    A, B = AB(k)
    L = den*A - num          # want L <= -den*B*sqrt(2), i.e. L <= Rb*sqrt(2)
    Rb = -den*B
    if Rb >= 0:
        return L <= 0 or L*L <= 2*Rb*Rb
    return L <= 0 and L*L >= 2*Rb*Rb


def disk(M, num, den):
    """Every reachable difference vector with l1 <= M, even l1, inside radius r.

    Reachability: R10 proves the exact difference set after n steps is exactly the
    integer k with even l1 norm and ||k||_1 <= 2n, so M = 2n here.
    """
    out = []
    for b in range(-M, M + 1):
        for d in range(-M, M + 1):
            if abs(b) + abs(d) > M:
                continue
            rem = M - abs(b) - abs(d)
            ca = int(-(b - d)/2**0.5)
            cc = int(-(b + d)/2**0.5)
            for a in range(ca - 2, ca + 3):
                if abs(a) > rem:
                    continue
                for c in range(cc - 2, cc + 3):
                    if abs(a) + abs(c) > rem:
                        continue
                    k = (a, b, c, d)
                    if sum(map(abs, k)) % 2 or not any(k):
                        continue
                    if leq_r2(k, num, den):
                        out.append(k)
    return out


def weight(k, M):
    """Exact count of M-step octagon paths ending at k -- R11's own formula."""
    a, b, c, d = k
    tot = 0
    for m in range(M + 1):
        if m < abs(a) + abs(c) or (m - (abs(a) + abs(c))) % 2:
            continue
        j2 = M - m
        if j2 < abs(b) + abs(d) or (j2 - (abs(b) + abs(d))) % 2:
            continue

        def sq(j, x, y):
            if (j + x + y) % 2 or (j + x - y) % 2:
                return 0
            i1, i2 = (j + x + y)//2, (j + x - y)//2
            if not (0 <= i1 <= j and 0 <= i2 <= j):
                return 0
            return comb(j, i1)*comb(j, i2)

        tot += comb(M, m)*sq(m, a, c)*sq(j2, b, d)
    return tot


def pell_family(terms=10):
    """R10's construction: (sqrt2-1)^j = u + v*sqrt2  ->  k = (u, 2v, u, 0)."""
    fam, u, v = {}, 1, 0
    for j in range(terms):
        k = (u, 2*v, u, 0)
        A, B = AB(k)
        fam[sum(map(abs, k))] = (j, k, (A + B*2**0.5)**0.5)
        u, v = 2*v - u, u - v
    return fam


R09_KERNEL = {(1, -2, 2, -1), (-1, 2, -2, 1), (2, -1, -1, 2), (-2, 1, 1, -2)}


def pell_numbers(n=14):
    P = [0, 1]
    while len(P) < n:
        P.append(2*P[-1] + P[-2])
    return P


def family_B(terms=10):
    """The SECOND extremal family, found by this record after its first
    prediction failed: k = (-P_{i+1}, P_i, P_i, -P_{i+1}), norm A^2-2B^2 = 2.

    R10's family (u_j, 2v_j, u_j, 0) has norm 4 and answers "given l1 <= 2n,
    how small can |z| be". The disk asks the DUAL question, "given |z| <= r,
    how small can l1 be", and the dual optimum is a different family.
    """
    P = pell_numbers()
    fam = {}
    for i in range(1, terms):
        k = (-P[i+1], P[i], P[i], -P[i+1])
        A, B = AB(k)
        fam[sum(map(abs, k))] = (i, k, (A + B*2**0.5)**0.5, A*A - 2*B*B)
    return fam

RADII = ((1, 1, "1"), (1, 4, "1/2"), (1, 16, "1/4"), (1, 64, "1/8"))


def main():
    fails = []
    fam = pell_family()
    print("R10's Pell family, recomputed here:")
    print(f"  {'j':>2} {'k':>18} {'l1':>4} {'|z|':>12}")
    for l1, (j, k, m) in sorted(fam.items()):
        print(f"  {j:>2} {str(k):>18} {l1:>4} {m:>12.6f}")

    # ---- CLAIM 1: the l1 threshold does not depend on n
    print("\n[1] min l1 inside the disk, at three different n")
    print(f"  {'r':>5} " + " ".join(f"{'n='+str(n):>8}" for n in (10, 20, 40))
          + "   verdict")
    thresholds = {}
    for num, den, rl in RADII:
        row = []
        for n in (10, 20, 40):
            pts = disk(2*n, num, den)
            row.append(min((sum(map(abs, k)) for k in pts), default=None))
        same = len({x for x in row if x is not None}) == 1
        thresholds[rl] = row[-1]
        print(f"  {rl:>5} " + " ".join(f"{str(x):>8}" for x in row)
              + f"   {'n-independent' if same else 'VARIES WITH n'}")
        if not same:
            fails.append(f"r={rl}: min l1 varies with n ({row}) -- the threshold is "
                         f"not a function of r alone and claim 1 is false")

    # ---- CLAIM 2: the minimisers ARE R09's and R10's objects
    print("\n[2] which vectors realise each threshold")
    for num, den, rl in RADII:
        pts = disk(80, num, den)
        if not pts:
            continue
        m = min(sum(map(abs, k)) for k in pts)
        win = sorted(k for k in pts if sum(map(abs, k)) == m)
        orbit = len(win)
        src = "—"
        if m in fam:
            j, pk, pm = fam[m]
            if any(tuple(map(abs, k)) == tuple(map(abs, pk)) for k in win):
                src = f"R10 Pell j={j}, {pk}, |z|={pm:.6f}"
        if any(k in R09_KERNEL for k in win):
            src = f"R09 shortest kernel generator"
        print(f"  r={rl:<4} l1={m:>3}  orbit size={orbit:>2}  example={win[0]}")
        print(f"            identified as: {src}")
        if orbit != 8:
            fails.append(f"r={rl}: orbit size {orbit}, expected 8")
        if src == "—":
            if rl == "1":
                # EXPECTED, and it is the control. At r = 1 the disk is wide enough
                # for a generic short vector: l1 = 2 is realised by (-1,0,0,-1) and
                # its orbit, while R10's Pell vector of the same l1, (1,0,1,0), has
                # |z| = 1.414 and does NOT fit. So no Diophantine object is needed,
                # and r = 1 is exactly the row R11 measures as converging best
                # (0.995 at n = 160). The mechanism switches ON below some radius
                # rather than operating at every radius -- which is a narrower claim
                # than the one this script was first written to assert, and the one
                # the measurement actually supports.
                print("            (expected: the control radius -- see note in source)")
            else:
                fails.append(f"r={rl}: threshold vector at l1={m} matches neither "
                             f"R09's kernel generators nor R10's Pell family")

    # ---- CLAIM 2b: the TWO families together predict the threshold
    print("\n[2b] two interleaved families, and which one wins")
    famB = family_B()
    print("  family A (R10):  k = (u_j, 2v_j, u_j, 0),  norm A^2-2B^2 = 4")
    for l1, (j, k, m) in sorted(fam.items())[:6]:
        print(f"     l1={l1:>4} {str(k):>22} |z|={m:.8f}")
    print("  family B (this record):  k = (-P_(i+1), P_i, P_i, -P_(i+1)),  norm = 2")
    for l1, (i, k, m, N) in sorted(famB.items())[:6]:
        print(f"     l1={l1:>4} {str(k):>22} |z|={m:.8f}")
    print()
    print(f"  {'r':>7} {'A gives':>9} {'B gives':>9} {'min(A,B)':>9} {'measured':>9} "
          f"{'agree':>7}")
    # Extended 2026-11-27 to 1/64 and 1/128, closing this record's own sec.5-1
    # item ("I did not run them, so the pattern is established at five points and
    # no more"). The window M must grow with 1/r or the disk comes back empty and
    # the row proves nothing -- M = 760 and 1800 are the first that contain the
    # predicted vector.
    RAD = ((1, "1", 1.0, 240), (4, "1/2", .5, 240), (16, "1/4", .25, 240),
           (64, "1/8", .125, 240), (256, "1/16", .0625, 240),
           (1024, "1/32", .03125, 320), (4096, "1/64", .015625, 760),
           (16384, "1/128", .0078125, 1800))
    for den, rl, rv, M in RAD:
        a = min((l1 for l1, (j, k, m) in fam.items() if m <= rv), default=None)
        b = min((l1 for l1, (i, k, m, N) in famB.items() if m <= rv), default=None)
        pred = min(x for x in (a, b) if x is not None) if (a or b) else None
        pts = disk(M, 1, den)
        meas = min(sum(map(abs, k)) for k in pts) if pts else None
        agree = pred == meas
        print(f"  {rl:>7} {str(a):>9} {str(b):>9} {str(pred):>9} {str(meas):>9} "
              f"{'yes' if agree else 'NO':>7}")
        if not agree and rl != "1":
            fails.append(f"r={rl}: two-family prediction {pred} != measured {meas}")
    print("  r=1 is expected to disagree: the disk is wide enough for the generic")
    print("  l1=2 vector (-1,0,0,-1), which is in neither family. Both families")
    print("  start at l1 >= 4, so min(A,B) cannot reach 2. Control, not a failure.")

    # ---- CLAIM 3: the mass the small disk misses
    print("\n[3] captured multiplicity mass, against the area ratio it should reach")
    print(f"  {'n':>4} {'r':>5} {'points':>7} {'min l1':>7} {'mass/mass(r=1)':>16} "
          f"{'area ratio':>11} {'deficit':>9}")
    for n in (20, 40):
        base = None
        for num, den, rl in RADII:
            pts = disk(2*n, num, den)
            if not pts:
                print(f"  {n:>4} {rl:>5}   empty disk -- no reachable vector inside")
                continue
            mass = sum(weight(k, 2*n) for k in pts)
            if rl == "1":
                base = mass
            frac = mass/base
            area = num/den          # r^2 for r = 1 normalisation
            print(f"  {n:>4} {rl:>5} {len(pts):>7} "
                  f"{min(sum(map(abs,k)) for k in pts):>7} {frac:>16.6f} "
                  f"{area:>11.6f} {area/frac if frac else float('inf'):>8.1f}x")
    print("\n  r=1/2 and r=1/4 sit within a few percent of their area ratios, which is")
    print("  why R11's normalized columns for them are already near 1. r=1/8 is short")
    print("  by more than an order of magnitude, because it contains no vector below")
    print("  l1 = 24 at any n and the multiplicity is concentrated far below that.")

    print("\n" + "="*74)
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print("  -", f)
        return 1
    print("PASS")
    print("  The l1 threshold of the disk is a function of r alone, realised by exactly")
    print("  one 8-element orbit, and that orbit is R09's kernel generator at r=1/2 and")
    print("  R10's Pell vectors j=2, j=3 at r=1/4, r=1/8.")
    print("  EVIDENCE CLASS: MEASURED for every number above; the identification with")
    print("  R09/R10 is exact vector equality, not resemblance. DERIVED for the claim")
    print("  that this is WHY R11's small-r rows converge slowly -- the mechanism is")
    print("  measured, the causal attribution is an argument.")
    print("  LIMITATION: three values of n (10, 20, 40) and four radii. No claim that")
    print("  the threshold family is exhausted by R09+R10 at every radius: r=1 and")
    print("  r=1/2 are realised by kernel vectors, and only r=1/4 and r=1/8 by Pell")
    print("  vectors, so the pattern at smaller radii is untested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
