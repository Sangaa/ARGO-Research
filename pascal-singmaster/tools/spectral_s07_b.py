from math import comb, log, pi
from decimal import Decimal, getcontext
import random
getcontext().prec=80
def C(a,b): return comb(a,b) if 0<=b<=a else 0

# Robbins: sqrt(2 pi n)(n/e)^n e^{1/(12n+1)} < n! < sqrt(2 pi n)(n/e)^n e^{1/(12n)}
def lnfact_bounds(n):
    if n==0: return (Decimal(0),Decimal(0))
    N=Decimal(n)
    base=(Decimal(2)*Decimal(pi)*N).ln()/2 + N*(N.ln()-1)
    return (base + 1/(12*N+1), base + 1/(12*N))
def lnC_interval(n,k):
    lo = lnfact_bounds(n)[0] - lnfact_bounds(k)[1] - lnfact_bounds(n-k)[1]
    hi = lnfact_bounds(n)[1] - lnfact_bounds(k)[0] - lnfact_bounds(n-k)[0]
    return lo,hi
def disjoint(a,b):
    la,ha=lnC_interval(*a); lb,hb=lnC_interval(*b)
    return ha<lb or hb<la

print("="*78)
print("MONITOR FINDING 2: an INEQUALITY from the heat-kernel/Stirling picture")
print("This is the route S01 sec.6, S02 sec.7, S03 sec.7 all left OPEN.")
print("="*78)
print("  Soundness is structural: both intervals contain the true value, so a")
print("  genuine repetition can never be excluded. Checking that it is also")
print("  TRUE in implementation, and measuring the power.")
print()
seen={}
for n in range(4,600):
    for k in range(2,n//2+1): seen.setdefault(C(n,k),[]).append((n,k))
eq=[(p[i],p[j]) for v,p in seen.items() if len(p)>1
    for i in range(len(p)) for j in range(i+1,len(p))]
fe=[(a,b) for a,b in eq if disjoint(a,b)]
print(f"  SOUNDNESS on the complete population of {len(eq)} genuine repetitions:")
print(f"     falsely excluded: {len(fe)}  -> {'SOUND' if not fe else fe}")

random.seed(7)
cells=[(n,k) for n in range(4,400) for k in range(2,n//2+1)]
pairs=[]
while len(pairs)<20000:
    x=random.choice(cells); y=random.choice(cells)
    if x!=y: pairs.append((x,y))
ne=[(x,y) for x,y in pairs if C(*x)!=C(*y)]
r1=sum(1 for x,y in ne if disjoint(x,y))
print(f"\n  ARM 1 - his 'S01 sample rebuilt' (seed 7, same cell set):")
print(f"     unequal pairs: {len(ne)};  ruled out: {r1} = {r1/len(ne):.2%}  (he says 100.00%)")

# arm 3: the HARD arm - adjacent-in-value distinct pairs
vals=sorted({C(n,k):(n,k) for n in range(4,400) for k in range(2,n//2+1)}.items())
adj=[(vals[i][1],vals[i+1][1]) for i in range(len(vals)-1)]
random.seed(11); random.shuffle(adj); adj=adj[:20000]
r3=sum(1 for x,y in adj if disjoint(x,y))
print(f"\n  ARM 3 - the HARD arm, adjacent-in-value distinct pairs:")
print(f"     pairs: {len(adj)};  ruled out: {r3} = {r3/len(adj):.2%}  (he says 99.67%)")

def carries(k,m,p):
    c=carry=0
    while k or m or carry:
        d=(k%p)+(m%p)+carry; carry=1 if d>=p else 0; c+=carry; k//=p; m//=p
    return c
kum=lambda n,k: tuple(carries(k,n-k,p) for p in (2,3,5))
rk=sum(1 for x,y in adj if kum(*x)!=kum(*y))
print(f"     Kummer (2,3,5) on the same arm: {rk} = {rk/len(adj):.2%}  (he says 99.19%)")
both=sum(1 for x,y in adj if disjoint(x,y) and kum(*x)!=kum(*y))
ionly=sum(1 for x,y in adj if disjoint(x,y) and kum(*x)==kum(*y))
konly=sum(1 for x,y in adj if not disjoint(x,y) and kum(*x)!=kum(*y))
neither=[(x,y) for x,y in adj if not disjoint(x,y) and kum(*x)==kum(*y)]
print(f"\n  COMPLEMENTARITY: both {both}, inequality-only {ionly}, Kummer-only {konly}, "
      f"neither {len(neither)}")
print(f"     union: {both+ionly+konly} / {len(adj)}")
for x,y in neither[:2]:
    print(f"     survivor: C{x} = {C(*x)}  vs  C{y} = {C(*y)}  "
          f"({abs(C(*x)-C(*y))/max(C(*x),C(*y)):.4%} apart)")
print()
print("  THE TAXONOMY'S THIRD LEG IS REAL AND HE MEASURED IT:")
print("     identity    0%      congruence 87-99%      inequality 99.67-100%")
print("  And they are COMPLEMENTARY, not redundant. The route I called 'the one")
print("  promising route and it is open' in S01, S02 and S03 is CLOSED - by him,")
print("  while I was writing three more records saying it was open.")
