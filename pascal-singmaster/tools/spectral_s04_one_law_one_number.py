from fractions import Fraction as F
from math import comb, cos, sin, pi, isclose
def C(a,b): return comb(a,b) if 0<=b<=a else 0

print("="*78)
print("HER FAMILY, verified:  P_n(a,b) = sum_k C(n-k,k) a^(n-2k) b^k")
print("="*78)
def P_sum(n,a,b): return sum(C(n-k,k)*a**(n-2*k)*b**k for k in range(n//2+1))
def P_rec(n,a,b):
    x,y=1,0      # P_0 = 1, P_-1 = 0
    for _ in range(n): x,y=a*x+b*y,x
    return x
bad=[]
for a in range(-3,4):
    for b in range(-3,4):
        for n in range(0,16):
            if P_sum(n,a,b)!=P_rec(n,a,b): bad.append((a,b,n))
print(f"  P_n = a P_(n-1) + b P_(n-2) for all a,b in [-3,3], n=0..15: "
      f"{'HOLDS' if not bad else bad[:3]}")
NAMED={(1,1):"Fibonacci",(2,1):"Pell",(1,2):"Jacobsthal",(2,-1):"linear",(1,-1):"periodic"}
print(f"\n  {'(a,b)':>8} {'name':<12} {'P_1..P_8':<42}")
for (a,b),nm in NAMED.items():
    seq=[P_rec(n,a,b) for n in range(1,9)]
    print(f"  {str((a,b)):>8} {nm:<12} {str(seq):<42}")
print("  (these are P_n = F_(n+1) etc - the shifted index, as her formula gives)")

print()
print("="*78)
print("HER WAVE SPECIALISATION:  a = 2cos(t), b = -1  =>  P_n = sin((n+1)t)/sin(t)")
print("="*78)
worst=0.0
for t in (0.3,0.7,1.1,1.9,2.6):
    for n in range(0,12):
        lhs=P_rec(n,2*cos(t),-1); rhs=sin((n+1)*t)/sin(t)
        worst=max(worst,abs(lhs-rhs))
print(f"  max |P_n - sin((n+1)t)/sin(t)| over 5 angles, n=0..11: {worst:.2e}")
print("  -> CONFIRMED. That is the Chebyshev U polynomial, and her family")
print("     contains Fibonacci, Pell, Jacobsthal AND harmonic oscillation.")

print()
print("="*78)
print("WHAT I THINK SHE UNDER-SOLD: her six anchor points are not six.")
print("="*78)
print("  P_n = a P_(n-1) + b P_(n-2) IS the companion matrix [[a,b],[1,0]].")
print("  So A03 (Fibonacci/Pell), A04 (eigenvalues) and A05 (oscillation) are")
print("  ONE anchor seen three ways, and the axis is the DISCRIMINANT a^2+4b.")
print()
print(f"  {'(a,b)':>9} {'a^2+4b':>8} {'eigenvalues':<34} {'behaviour':<22}")
print("  "+"-"*76)
import cmath
for a,b in [(2,-1),(1,1),(2,1),(1,2),(1,-1),(0,-1),(3,-2),(1,-2)]:
    D=a*a+4*b
    r1=(a+cmath.sqrt(D))/2; r2=(a-cmath.sqrt(D))/2
    if D>0:   beh="exponential"
    elif D==0:beh="polynomial (unipotent)"
    else:     beh="oscillation"
    ev=f"{r1:.4f}, {r2:.4f}".replace("+0.0000j","").replace("(","").replace(")","")
    print(f"  {str((a,b)):>9} {D:>8} {ev:<34} {beh:<22}")
print()
print("  AND THE PASCAL CASE SITS EXACTLY ON THE BOUNDARY.")
print("  (a,b) = (2,-1) gives a^2+4b = 0: repeated eigenvalue 1, the UNIPOTENT")
print("  matrix, polynomial growth - which is what I measured for Pascal earlier.")
print("  And a = 2cos(t) -> 2 as t -> 0, so her oscillating branch approaches the")
print("  Pascal point from the D<0 side. One axis, three regimes, Pascal on the")
print("  knife edge between oscillation and exponential growth.")
print()
print("  So the map does not need six pins. It needs one law and one number.")
