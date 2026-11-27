#!/usr/bin/env python3
"""S10 -- the identifiability question S03 left open, in two halves.

S03 recovered (s, L) from (sigma^2, gamma_2) INSIDE the Pascal family and then
asked the model-selection question: is there a non-Pascal step law with the same
two cumulants? It proved no for s = 1 (extremal kurtosis) and no for s = 2, L = 1
against INTEGER-mean rivals, and left two cases open:

    (i)  s = 2, L = 1 against half-integer-mean rivals -- probed, not refuted;
    (ii) s >= 3 -- open, with the note that mu4 - mu2 > 0 leaves room.

This script settles both, in opposite directions, and is explicit about which
statements are proofs and which are bounded LP measurements.

Run: python3 -I s10_identifiability.py      Exit 0 iff every stated check holds.

Conventions. A step law is a probability law on the real line, CENTRED (mean 0).
Pascal(s, L) is the centred law of the symbol c z^m (1+z^L)^s / 2^s, i.e. the sum
of s independent steps uniform on {-L/2, +L/2}. mu_r is the r-th centred moment.
Closed forms from S03: mu2 = s L^2 / 4, mu4 = s L^4 (3s-2) / 16.
"""
from fractions import Fraction as F
from math import comb, sqrt
import sys

import numpy as np
from scipy.optimize import linprog

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
    return cond


def pascal(s, L=1):
    w = {}
    for j in range(s + 1):
        x = F(L * (2 * j - s), 2)
        w[x] = w.get(x, 0) + F(comb(s, j), 2 ** s)
    return w


def mom(w, r):
    return sum(p * x ** r for x, p in w.items())


def lp_min_mu4(beta, target_mu2, window=40, maximise=False):
    """min (or max) mu4 over centred laws on beta+Z, |x| <= window, with mu2 fixed."""
    x = np.arange(-window, window + 1) + beta
    c = x ** 4 * (-1 if maximise else 1)
    r = linprog(c=c, A_eq=[np.ones_like(x), x, x ** 2],
                b_eq=[1.0, 0.0, float(target_mu2)], bounds=(0, None))
    if r.status != 0:
        return None, None
    val = -r.fun if maximise else r.fun
    sup = [(float(x[i]), float(r.x[i])) for i in np.nonzero(r.x > 1e-10)[0]]
    return val, sup


# ---------------------------------------------------------------- A
print(__doc__.split("Run:")[0].rstrip())
print("\n" + "=" * 74)
print("A. the closed forms S03 recovers, re-derived from the symbol, exactly")
bad = 0
for s in range(1, 9):
    for L in range(1, 5):
        w = pascal(s, L)
        if (mom(w, 2), mom(w, 4)) != (F(s * L * L, 4),
                                      F(s * L ** 4 * (3 * s - 2), 16)):
            bad += 1
check(bad == 0, "Pascal moments disagree with S03's closed forms")
print(f"   ok   32 (s,L) pairs, exact fractions, {bad} mismatch")

# ---------------------------------------------------------------- B
print("\nB. case (i): s = 2, L = 1. Target mu2 = mu4 = 1/2.")
print("""   RELAXATION. mu2 and mu4 depend only on m = x^2, so drop the mean-zero
   constraint; that enlarges the feasible set, so any bound it yields is valid
   a fortiori. What is left is a linear objective under two equality
   constraints, whose optimum sits at a vertex with at most two support points,
   and for a two-point mix bracketing the mean,

       V(m1, m2) = (m1 + m2)/2 - m1*m2 ,   m1 <= 1/2 <= m2 .

   dV/dm2 = 1/2 - m1 >= 0 and dV/dm1 = 1/2 - m2 <= 0, so V is minimised by the
   pair bracketing 1/2 most tightly. That pair is computable: no search.""")
print(f"\n   {'offset':>7} {'m1':>10} {'m2':>10} {'relaxed V':>14} "
      f"{'excludes?':>9} {'LP, mean=0':>11} {'1/2+3b^4':>10}")
proved = []
for bs in ("0", "1/8", "1/4", "1/3", "2/5", "17/40", "9/20", "1/2"):
    b = F(bs)
    S = sorted({(b + n) ** 2 for n in range(-8, 9)})
    m1, m2 = max(m for m in S if m <= F(1, 2)), min(m for m in S if m >= F(1, 2))
    V = (m1 + m2) / 2 - m1 * m2
    lp, _ = lp_min_mu4(float(b), F(1, 2))
    pred = 0.5 + 3 * float(b) ** 4
    check(lp is not None and abs(lp - pred) < 1e-9,
          f"LP min mu4 at beta={bs} is {lp}, closed form predicts {pred}")
    if V > F(1, 2):
        proved.append(bs)
    print(f"   {bs:>7} {str(m1):>10} {str(m2):>10} {str(V):>14} "
          f"{'YES':>9} " if V > F(1, 2) else
          f"   {bs:>7} {str(m1):>10} {str(m2):>10} {str(V):>14} {'no':>9} ",
          end="")
    print(f"{lp:>11.8f} {pred:>10.6f}")

print("""
   beta = 1/2 is the half-integer case S03 left open, and the relaxation alone
   settles it: m1 = 1/4, m2 = 9/4 -- the lattice Z+1/2 holds no squared value
   between them -- so V = 5/4 - 9/16 = 11/16 > 1/2. Symmetry makes the dropped
   mean-zero constraint free there. PROVED: no law on Z+1/2 with mu2 = 1/2 has
   mu4 = 1/2. The gap is exactly 3/16, which is the same 3/16 S03 noticed as
   the value of x^2(x^2-1) at |x| = 1/2 -- the caveat and the closure are the
   same number seen from two sides.""")
check("1/2" in proved, "the relaxed bound fails to exclude beta = 1/2")

u0 = (3 - sqrt(7)) / 2
b0 = sqrt(u0)
print(f"""   How far the proof reaches. For beta in [1-1/sqrt2, 1/2] the bracketing pair
   is (1-beta)^2, (1+beta)^2, so with u = beta^2, V = 3u - u^2, and V > 1/2 iff
   u > (3-sqrt7)/2. So the relaxation PROVES exclusion for every offset above
   beta* = sqrt((3-sqrt7)/2) = {b0:.10f}, which is {(0.5-b0)/0.5*100:.1f}% of
   the offset range and contains the open case. Below beta* the relaxation is
   too weak and the exclusion rests on the LP.""")
check(abs((3 * u0 - u0 * u0) - 0.5) < 1e-12, "beta* does not satisfy V = 1/2")

# ---------------------------------------------------------------- C
print("\nC. case (i), the offsets the proof does not reach: a dense LP scan")
worst, breached = (0.0, None), None
for i in range(1, 201):
    bf = i / 400.0
    lp, sup = lp_min_mu4(bf, F(1, 2))
    if lp is None or lp <= 0.5:
        breached = (bf, lp)
        break
    d = abs((lp - 0.5) - 3 * bf ** 4)
    if d > worst[0]:
        worst = (d, bf)
check(breached is None, f"mu4 = 1/2 became reachable at beta = {breached}")
print(f"   ok   200 offsets in (0, 1/2], step 1/400, window |x| <= 40:")
print(f"        min mu4 > 1/2 at every one; worst deviation from the closed form")
print(f"        1/2 + 3*beta^4 is {worst[0]:.2e}, at beta = {worst[1]}.")
_, sup = lp_min_mu4(0.3, F(1, 2))
print(f"        minimiser at beta = 0.3: {[(round(a,4), round(b,5)) for a, b in sup]}")
print("        -- the three lattice points nearest the origin, every time.")
print("   EVIDENCE CLASS: MEASURED. The optimality of that three-point support,")
print("   and therefore the closed form 1/2 + 3*beta^4, is LP evidence on a")
print("   finite window and a finite offset grid. It is not a theorem.")

# exact value on that support
print("\n   the attained value on {beta-1, beta, beta+1}, in exact arithmetic:")
for bs in ("0", "1/4", "1/3", "2/5", "1/2"):
    b = F(bs)
    xs = [b - 1, b, b + 1]
    A = [[F(1)] * 3 + [F(1)], xs + [F(0)], [x * x for x in xs] + [F(1, 2)]]
    for i in range(3):
        piv = next(r for r in range(i, 3) if A[r][i] != 0)
        A[i], A[piv] = A[piv], A[i]
        A[i] = [v / A[i][i] for v in A[i]]
        for r in range(3):
            if r != i and A[r][i] != 0:
                f_ = A[r][i]
                A[r] = [a - f_ * c for a, c in zip(A[r], A[i])]
    w = [A[i][3] for i in range(3)]
    m4 = sum(wi * x ** 4 for wi, x in zip(w, xs))
    check(m4 == F(1, 2) + 3 * b ** 4, f"exact mu4 at beta={bs} is {m4}")
    check(all(wi >= 0 for wi in w), f"negative weight at beta={bs}")
    ws = str([str(v) for v in w])
    print(f"     beta = {bs:>4}: w = {ws:<34} mu4 = {str(m4):>10} "
          f"= 1/2 + 3*({bs})^4")

# ---------------------------------------------------------------- D
print("\nD. case (i), the limit of the whole result: the LATTICE is load-bearing")
print("""   Off a lattice a rival does exist, and it is small enough to write down.
   Symmetric four-point law, mass P/2 at each of +-1/2 and Q/2 at each of +-u:
   P + Q = 1, P/4 + Q u^2 = 1/2, P/16 + Q u^4 = 1/2 force 8u^4 - 14u^2 + 3 = 0,
   so u^2 = 3/2 (the root u^2 = 1/4 is the first point again).""")
u2 = F(3, 2)
Q = F(1, 4 * u2 - 1)
P = 1 - Q
m2_, m4_ = P * F(1, 4) + Q * u2, P * F(1, 16) + Q * u2 ** 2
m6_ = P * F(1, 64) + Q * u2 ** 3
check((m2_, m4_) == (F(1, 2), F(1, 2)), "the off-lattice witness misses the target")
check(P > 0 and Q > 0, "the off-lattice witness has a non-positive weight")
print(f"   P = {P}, Q = {Q}: mass {P/2} at each of +-1/2, {Q/2} at each of "
      f"+-sqrt(3/2)")
print(f"   mu2 = {m2_}, mu4 = {m4_}  -- both hit the Pascal s=2, L=1 target")
print(f"   mu6 = {m6_} against Pascal's {mom(pascal(2,1), 6)}: the sixth moment")
print(f"   separates it. sqrt(3/2) - 1/2 is irrational, so this law lies on no")
print(f"   unit lattice. The identifiability claim is therefore conditional on")
print(f"   the lattice, and S03's phrase 'lattice distributions' is doing work.")

# ---------------------------------------------------------------- E
print("\nE. case (ii): s >= 3. A rival EXISTS, in closed form. Not identifiable.")
print("""   Symmetric law on {0, +-1, +-2} with w(+-1) = a, w(+-2) = b:
       2a +  8b = s/4           (mu2)
       2a + 32b = s(3s-2)/16    (mu4)
   =>  b = s(s-2)/128 ,  a = s(6-s)/32 ,  w(0) = (3s^2 - 22s + 64)/64 ,
   and 3s^2 - 22s + 64 has negative discriminant, so w(0) > 0 always.""")
print(f"\n   {'s':>3} {'w(0)':>12} {'a':>10} {'b':>10} {'valid':>6} "
      f"{'hits mu2,mu4':>13}  equals Pascal(s,1)?")
rivals = {}
for s in range(2, 8):
    a, b = F(s * (6 - s), 32), F(s * (s - 2), 128)
    w = {F(0): 1 - 2 * a - 2 * b, F(1): a, F(-1): a, F(2): b, F(-2): b}
    w = {x: p for x, p in w.items() if p != 0}
    ok = all(p >= 0 for p in w.values()) and sum(w.values()) == 1
    hits = (mom(w, 2), mom(w, 4)) == (F(s, 4), F(s * (3 * s - 2), 16))
    same = (w == pascal(s, 1))
    check(hits, f"the closed-form law at s={s} misses the target moments")
    if ok and hits and not same:
        rivals[s] = w
    print(f"   {s:>3} {str(1-2*a-2*b):>12} {str(a):>10} {str(b):>10} "
          f"{'yes' if ok else 'NO':>6} {str(hits):>13}  {same}")
print("""
   s = 2 and s = 4 return Pascal itself -- for even s Pascal already lives on
   the integer lattice, so this particular closed form lands on it rather than
   beside it. s = 3, 5, 6 give genuine non-Pascal rivals. The LP below supplies
   the rest: s >= 7, where this support runs out of room (a < 0), AND s = 4,
   where the two constraints leave a one-parameter family and the closed form
   merely happened to pick the Pascal point in it.""")
check(3 in rivals and 5 in rivals and 6 in rivals,
      "the closed form failed to produce rivals at s = 3, 5, 6")

print("\n   LP over symmetric integer-lattice laws, |x| <= K, s = 1..20:")
print(f"   {'s':>3} {'K':>3} {'status':>9}  rival found?")
verdict = {}
for s in range(1, 21):
    t2, t4 = F(s, 4), F(s * (3 * s - 2), 16)
    hit = None
    for K in (3, 4, 6, 10):
        j = np.arange(0, K + 1, dtype=float)
        r = linprog(c=-(j ** 6), A_eq=[np.ones_like(j), j ** 2, j ** 4],
                    b_eq=[1.0, float(t2), float(t4)], bounds=(0, None))
        if r.status == 0:
            hit = (K, r, j)
            break
    if hit is None:
        verdict[s] = "infeasible"
        print(f"   {s:>3} {'-':>3} {'INFEAS':>9}  no symmetric integer-lattice law at all")
        continue
    K, r, j = hit
    v = r.x
    w = {F(0): v[0]}
    for i in range(1, K + 1):
        if v[i] > 1e-11:
            w[F(i)] = w[F(-i)] = v[i] / 2
    w = {x: p for x, p in w.items() if p > 1e-11}
    pas = {float(x): float(p) for x, p in pascal(s, 1).items()}
    same = (set(pas) == {float(x) for x in w}
            and all(abs(pas[float(x)] - p) < 1e-9 for x, p in w.items()))
    m2 = float((v * j ** 2).sum())
    m4 = float((v * j ** 4).sum())
    check(abs(m2 - float(t2)) < 1e-9 and abs(m4 - float(t4)) < 1e-9,
          f"LP witness at s={s} misses the target moments")
    verdict[s] = "pascal only" if same else "rival"
    print(f"   {s:>3} {K:>3} {'feasible':>9}  "
          f"{'NO -- the only vertex found is Pascal' if same else 'YES, non-Pascal'}")
check(verdict[1] == "infeasible", "s=1 unexpectedly feasible on the integer lattice")
check(verdict[2] == "pascal only", "s=2 produced a non-Pascal integer-lattice law")
check(all(verdict[s] == "rival" for s in range(3, 21)),
      "some s >= 3 failed to produce a rival")

# ---------------------------------------------------------------- F
print("\nF. the collision at s = 3, and the question S03 could not measure")
print("   S03 asked how many cumulants separate two families when two do not,")
print("   and could not answer because it had no collision. Here is one.")
P3, R3 = pascal(3, 1), rivals[3]
for name, w in (("Pascal(3,1) = (1,3,3,1)/8", P3), ("rival on {0,+-1,+-2}", R3)):
    print(f"\n     {name}")
    print(f"       support {[str(x) for x in sorted(w)]}")
    print(f"       weights {[str(w[x]) for x in sorted(w)]}")
    print(f"       mu2 {mom(w,2)}   mu4 {mom(w,4)}   mu6 {mom(w,6)}   mu8 {mom(w,8)}")
g2 = lambda w: mom(w, 4) / mom(w, 2) ** 2 - 3
check(mom(P3, 2) == mom(R3, 2) and mom(P3, 4) == mom(R3, 4),
      "the s=3 collision does not actually collide")
check(mom(P3, 6) != mom(R3, 6), "mu6 fails to separate the s=3 collision")
print(f"\n     sigma^2 equal: {mom(P3,2) == mom(R3,2)}      "
      f"excess kurtosis equal: {g2(P3)} = {g2(R3)}")
print(f"     mu6 differs: {mom(P3,6)} vs {mom(R3,6)}  "
      f"(ratio {float(mom(R3,6)/mom(P3,6)):.6f})")
print("     ANSWER, on this collision: two even moments do not separate, three")
print("     do. The first separating cumulant is the sixth. One collision is")
print("     not a theorem about the family, and no claim is made beyond it.")

# ---------------------------------------------------------------- summary
print("\n" + "=" * 74)
print("""SUMMARY -- what S03's table becomes

  s = 1, any L                       identifiable, proved         (S03, unchanged)
  s = 2, L = 1, integer-mean rival   identifiable, proved         (S03, unchanged)
  s = 2, L = 1, half-integer rival   identifiable, PROVED HERE    (was open)
  s = 2, L = 1, any unit lattice     excluded, LP-MEASURED HERE   (not asked)
  s = 2, L = 1, off any lattice      NOT identifiable, witness    (not asked)
  s >= 3, L = 1                      NOT identifiable, witnesses  (was open)

  The direction matters: case (i) closes positively and case (ii) closes
  negatively. S03 wrote that for s >= 3 "mu4 - mu2 is strictly positive and
  there is room for a rival. Whether one exists is unknown." The room is real
  and the rival is explicit, so the recovery formulas sigma^2 = sL^2/4 and
  gamma_2 = -2/s remain parameter recovery inside the family and are NOT a
  model-selection test for s >= 3. Both reviewers' objection was right, and it
  is right for a sharper reason than either of them gave.""")
print("=" * 74)
if FAIL:
    print(f"FAIL ({len(FAIL)}):")
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print(f"PASS -- every stated check holds ({0} failures). Exact arithmetic where")
print("the claim is exact; LP with its window and grid stated where it is not.")
sys.exit(0)
