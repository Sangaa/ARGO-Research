from math import comb, cos, pi
from fractions import Fraction as F
import cmath

print("="*76)
print("1. HER FORMULA  S_r(n) = (2^n + 2cos((n*pi - 2*r*pi)/3)) / 3")
print("="*76)
bad=[]
for n in range(0,401):
    for r in range(3):
        exact=sum(comb(n,k) for k in range(n+1) if k%3==r)
        approx=(2**n + 2*cos((n*pi-2*r*pi)/3))/3
        if abs(exact-approx) > 1e-6*max(1,abs(exact)): bad.append((n,r))
print(f"   checked n=0..400, r=0,1,2  ({401*3} cases): "
      f"{'ALL MATCH' if not bad else bad[:3]}")
print("   and it is DERIVED, not fitted: the roots-of-unity filter gives")
print("     S_r = (1/3) sum_j w^(-jr) (1+w^j)^n,  w = e^(2 pi i/3)")
print("   with 1+w = e^(i pi/3) exactly, so the two non-trivial terms have")
print("   MODULUS 1 and contribute 2cos(n pi/3 - 2 pi r/3). Nothing else.")

print()
print("="*76)
print("2. HER CLAIM: 3 is the LARGEST modulus whose residue sums stay within 1")
print("="*76)
print("   This is TRUE, and the reason is one line rather than a scan.")
print("   For modulus m:  S_r(n) = (1/m) sum_j w^(-jr) (1+w^j)^n, w = e^(2 pi i/m)")
print("   and  |1 + w^j| = 2|cos(pi j/m)|.  The spread is driven by the largest")
print("   of these over j != 0, which is 2cos(pi/m).")
print()
print(f"   {'m':>3} {'2cos(pi/m)':>12} {'bounded?':>10}   measured max spread over n=1..40")
print("   "+"-"*72)
for m in range(2,13):
    lam=2*cos(pi/m)
    spreads=[]
    for n in range(1,41):
        S=[sum(comb(n,k) for k in range(n+1) if k%m==r) for r in range(m)]
        spreads.append(max(S)-min(S))
    tag="YES" if lam<=1+1e-12 else "no"
    print(f"   {m:>3} {lam:>12.6f} {tag:>10}   n=1..10: {spreads[:10]}")
print()
print("   2cos(pi/m) <= 1  <=>  pi/m >= pi/3  <=>  m <= 3.   That is the whole")
print("   content of '3 is special here'. m=2 gives |1+w|=0, spread exactly 0;")
print("   m=3 gives modulus exactly 1, spread bounded forever; m>=4 gives a")
print("   modulus above 1, so the spread grows like (2cos(pi/m))^n.")
print()
print("   The exact bound at m=3:  |S_r - 2^n/3| = |2cos(...)|/3 <= 2/3,")
print("   so max-min <= 4/3, hence <= 1 for integers. Verified above.")
