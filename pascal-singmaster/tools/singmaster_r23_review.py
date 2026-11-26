#!/usr/bin/env python3
"""R23 - independent review certificate for TOTO's n < 200t^2 bound.

Her derivation (verbatim structure, PR #904 comment 7186682861):

    x = 1/Q,  z_i = s_i x + d_i x^2,  r_i = -h_i^2 x^2
    s_i = i - (t-1)/2,  h_i = i + 1/2,  d_i = (W - 5t^2 - 1)/24 - s_i/2 - s_i^2
    A = prod_i (Q^2 + s_i Q + d_i),   B = prod_i (Q^2 - h_i^2)
    log(A/B) = t W x^2 / 24  +  t(t^2-1) x^3 / 24  +  E,   |E| <= 3 t^5 x^4
    at Q >= 100 t^2 the sign of log(A/B) is decided at each bracket endpoint
    => Q < 100 t^2 => n < 200 t^2

This script checks the parts that could hide an error. It exits non-zero if any
check fails, so a passing run is the evidence and a failing run is visible.

  1. the two retained coefficients, exactly

Every population size below is PRINTED BY THE RUN, not written into the prose.
The first version of this certificate reported "480 polynomials" where the loop
iterates 59 t-values times 8 W-values = 472; TOTO caught the arithmetic. A count
a human multiplies is a count that can disagree with the loop, so the loop says it.
  2. her per-factor magnitude bounds |s|<=t/2, |d|<=t^2, |h|<=t
  3. the actual |E| against 3 t^5 x^4, in 80-digit arithmetic
  4. the three sign conclusions at Q = 100 t^2
  5. positivity of every factor of A and B (she asserts it; this supplies it)
  6. her algebraic closure of the j=2 lower endpoints, L^2-326L+369 < 0
  7. her W=1 formula against the one proved in R22

WHAT WAS MEASURED / SCOPE / METHOD / EVIDENCE CLASS are stated per section in
the accompanying record SINGMASTER_R23_TOTO_BOUND_REVIEW_2026-11-26.md.
"""
import sys
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 80

fail = []
def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' - ' + detail) if detail else ''}")
    if not ok: fail.append(name)

def pieces(t, W):
    c = F(W - 5*t*t - 1, 24)
    s = [F(i) - F(t-1, 2) for i in range(t)]
    h = [F(2*i+1, 2) for i in range(t)]
    d = [c - x/2 - x*x for x in s]
    return s, h, d

BRACKET_W = (-24, -11, -8, -3, 0, 1, 9, 16)   # R17 endpoints, both signs

print("1. the two retained coefficients (exact rationals)")
bad = []
n_poly = 0
for t in range(2, 61):
    for W in BRACKET_W:
        n_poly += 1
        s, h, d = pieces(t, W)
        x2 = sum(d) - sum(v*v for v in s)/2 + sum(v*v for v in h)
        x3 = sum(v**3 for v in s)/3 - sum(a*b for a, b in zip(s, d))
        if x2 != F(t*W, 24) or x3 != F(t*(t*t-1), 24):
            bad.append((t, W))
check("x^2 coeff == tW/24 and x^3 coeff == t(t^2-1)/24, t=2..60, 8 W values",
      not bad, f"{len(bad)} mismatches" if bad else f"{n_poly} polynomials")

print("2. her per-factor magnitude bounds")
bad = []
for t in range(2, 201):
    for W in BRACKET_W:
        s, h, d = pieces(t, W)
        if max(abs(v) for v in s) > F(t, 2):  bad.append(("s", t, W))
        if max(abs(v) for v in d) > F(t*t):   bad.append(("d", t, W))
        if max(abs(v) for v in h) > F(t):     bad.append(("h", t, W))
check("|s_i|<=t/2, |d_i|<=t^2, |h_i|<=t, t=2..200, 8 W values", not bad,
      f"{len(bad)} violations" if bad else "all three hold")

print("3. the actual |E| against her bound 3 t^5 x^4")
worst, worst_at, n_pts = F(0), None, 0
for t in (2, 3, 4, 5, 7, 10, 15, 20, 30, 40, 60):
    for W in BRACKET_W:
        for Qf in (2*t, 4*t, 10*t, 10*t*t, 100*t*t):
            if F(t, Qf) > F(1, 2):    # her hypothesis tx <= 1/2
                continue
            Q = Decimal(Qf); x = 1/Q
            s, h, d = pieces(t, W)
            tot = Decimal(0)
            for si, hi, di in zip(s, h, d):
                z = (Decimal(si.numerator)/Decimal(si.denominator))*x \
                  + (Decimal(di.numerator)/Decimal(di.denominator))*x*x
                r = -(Decimal(hi.numerator)/Decimal(hi.denominator))**2*x*x
                if z <= -1 or r <= -1:
                    print(f"  [FAIL] log undefined at t={t} W={W} Q={Qf}")
                    fail.append("log domain"); continue
                tot += (1+z).ln() - (1+r).ln()
            main = Decimal(t*W)/24*x*x + Decimal(t*(t*t-1))/24*x**3
            E = abs(tot - main)
            bound = 3*Decimal(t)**5*x**4
            ratio = F(int(E*10**30), int(bound*10**30)) if bound > 0 else F(0)
            n_pts += 1
            if ratio > worst: worst, worst_at = ratio, (t, W, Qf)
check("|E| <= 3 t^5 x^4 everywhere tested", worst <= 1,
      f"worst ratio {float(worst):.4f} at t,W,Q = {worst_at}; {n_pts} points")

print("4. the three sign conclusions at Q = 100 t^2")
bad = []
for t in range(2, 201):
    x = F(1, 100*t*t)
    err = F(72)*t**4*x*x                      # |24 E / (t x^2)| <= 72 t^4 x^2
    if not (-1 + (t*t-1)*x + err < 0):  bad.append(("W=-L", t))
    if not (1 - err > 0):               bad.append(("W=+R", t))
    if not (F(t*t-1) - F(72)*t**4*x > 0): bad.append(("W=0", t))
check("W<=-1 negative, W>=1 positive, W=0 positive, t=2..200", not bad,
      f"{bad[:3]}" if bad else "all three cases decided")

print("5. positivity of the factors (asserted by her; supplied here)")
bad = []
for t in range(2, 201):
    for W in BRACKET_W:
        s, h, d = pieces(t, W)
        Q = F(100*t*t)
        if min(Q*Q + si*Q + di for si, di in zip(s, d)) <= 0: bad.append(("A", t, W))
        if min(Q*Q - hi*hi for hi in h) <= 0:                 bad.append(("B", t, W))
check("every factor of A and of B is > 0 at Q = 100t^2, t=2..200", not bad,
      "so the logarithms are legitimate and dA/dW > 0" if not bad else f"{bad[:3]}")
# and the threshold at which it first holds, independent of the 100t^2 hypothesis
bad = []
for t in range(2, 201):
    Q = F(2*t)      # Q >= 2t suffices; t(1+sqrt(17))/4 = 1.2808 t is the true root
    for W in BRACKET_W:
        s, h, d = pieces(t, W)
        if min(Q*Q + si*Q + di for si, di in zip(s, d)) <= 0: bad.append((t, W))
check("positivity already holds at Q = 2t (far below 100t^2)", not bad,
      f"{bad[:3]}" if bad else "the hypothesis is not what buys positivity")

print("6. her algebraic closure of the j=2 lower endpoints")
bad = [L for L in (3, 8, 11, 24) if not (L*L - 326*L + 369 < 0)]
check("L^2 - 326L + 369 < 0 for L in {3,8,11,24}", not bad,
      "values -600, -2175, -3096, -6879")
bad = []
for L in (3, 8, 11, 24):
    rhs = F(L*L + 58*L + 369, 8)
    for t in range(2, 3001):
        P = 25*t**3 + (16*L+25)*t**2 + (23-2*L)*t + L*L - 6*L + 23
        if F(t-1)*F(P)/F(t)**4 > rhs: bad.append((t, L))
check("her chain (t-1)P/t^4 <= (L^2+58L+369)/8 is a true upper bound, t=2..3000",
      not bad, f"{bad[:3]}" if bad else "chain valid")
bad = []
for L in (3, 8, 11, 24):
    for t in range(2, 3001):
        P = 25*t**3 + (16*L+25)*t**2 + (23-2*L)*t + L*L - 6*L + 23
        if F(t-1)*F(P) / (F(48)*F(L)*F(t)**4) >= 1: bad.append((t, L))
check("exact m_2 < 1 at every lower endpoint, t=2..3000", not bad,
      f"{bad[:3]}" if bad else "consistent with the algebraic closure")

print("7. her W=1 formula against the one proved in R22")
bad = []
for t in range(2, 3001):
    her  = F(t-1)*F(25*t**3 + 9*t**2 + 25*t + 30) / F(48*t**4)
    mine = F(25*t**5 - 16*t**4 + 16*t**3 + 5*t**2 - 30*t) / F(48*t**5)
    if her != mine: bad.append(t)
check("her m_2(W=1) == the R22 closed form, t=2..3000", not bad,
      f"{bad[:3]}" if bad else "identical as exact rationals")
bad = [t for t in range(1, 3001)
       if not (23*t**4 + 16*t**3 - 16*t**2 - 5*t + 30 > 0)]
check("1 - m_2 numerator 23t^4+16t^3-16t^2-5t+30 > 0, t=1..3000", not bad)

print()
if fail:
    print(f"FAILED: {len(fail)} check(s): {fail}")
    sys.exit(1)
print("ALL CHECKS PASS - the derivation's arithmetic stands as reviewed.")
print("Scope and the two write-up gaps are in the accompanying record; a passing")
print("certificate is not a claim that the proof is complete as written.")
