from math import comb, cos, pi, gcd
from fractions import Fraction as F
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def S(n,m,r): return sum(C(n,k) for k in range(n+1) if k%m==r)
def W(n,m,r): return m*S(n,m,r)-2**n
def pmul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return r
def pstr(p):
    t=[]
    for i in range(len(p)-1,-1,-1):
        c=p[i]
        if c==0: continue
        s=("" if c==1 and i>0 else ("-" if c==-1 and i>0 else f"{c}"))
        t.append(s+("" if i==0 else ("x" if i==1 else f"x^{i}")))
    out=" + ".join(t).replace("+ -","- ")
    return out if out else "0"

print("="*78)
print("HIS FACTORISATIONS vs MY S06 POLYNOMIALS (computed from Pascal data by")
print("solving linear systems - a completely different route from his resultants)")
print("="*78)
MINE={  # from S06: W(n+deg*m) = sum c_i W(...)  ->  monic poly with zero roots included
 3:[1,1],                                   # x + 1
 5:[-1,11,1],                               # x^2 + 11x - 1
 6:[0,-27,26,1],                            # x^3 + 26x^2 - 27x
 7:[-1,-289,57,1],                          # x^3 + 57x^2 - 289x - 1
 8:[0,-256,-2160,120,1],                    # x^4 + 120x^3 - 2160x^2 - 256x
 9:[1,-13604,-13359,247,1],                 # x^4 + 247x^3 - 13359x^2 - 13604x + 1
}
HIS={3:[[1,1]], 5:[[-1,11,1]], 6:[[-1,1],[27,1]], 7:[[-1,-289,57,1]],
     8:[[-16,1],[16,136,1]], 9:[[1,1],[1,-13605,246,1]]}
for m in sorted(HIS):
    prod=[1]
    for f in HIS[m]: prod=pmul(prod,f)
    mine=MINE[m]
    # strip zero roots from mine (the j with 2cos = 0, i.e. m even and j = m/2)
    stripped=mine[:]
    while stripped and stripped[0]==0: stripped=stripped[1:]
    match = stripped==prod
    print(f"  m={m:>2}  his factors -> {pstr(prod)}")
    print(f"        mine (zero roots stripped) -> {pstr(stripped)}   {'MATCH' if match else 'DIFFER'}")

print()
print("="*78)
print("HIS DEGREE LAW:  deg F_(m,d) = phi(d)/2,  and Q_m = prod over d | m, d > 2")
print("="*78)
def phi(n): return sum(1 for k in range(1,n+1) if gcd(k,n)==1)
print(f"  {'m':>3} {'divisors d>2':<18} {'sum phi(d)/2':>13} {'my deg (zeros stripped)':>24}  ok?")
print("  "+"-"*66)
for m in sorted(MINE):
    ds=[d for d in range(1,m+1) if m%d==0 and d>2]
    tot=sum(phi(d)//2 for d in ds)
    st=MINE[m][:]
    while st and st[0]==0: st=st[1:]
    deg=len(st)-1
    print(f"  {m:>3} {str(ds):<18} {tot:>13} {deg:>24}  {'ok' if tot==deg else 'DIFFER'}")

print()
print("  WHY, and it is exactly the point TOTO raised about Galois:")
print("  the roots are (-1)^j (2cos(pi j/m))^m. Write j/m in lowest terms as")
print("  j'/d with d | m. The roots sharing a given d form one Galois orbit, of")
print("  size phi(d)/2 after pairing j with m-j. So each divisor contributes an")
print("  irreducible factor of degree phi(d)/2, and d=1,2 give the trivial and")
print("  zero eigenvalues, which is why his product starts at d > 2.")
print("  'Real after m steps' was never the reason - THIS is.")
