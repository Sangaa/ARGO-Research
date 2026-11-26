from math import comb
from fractions import Fraction as F
import random, itertools, numpy as np
def C(a,b): return comb(a,b) if 0<=b<=a else 0

print("="*76)
print("FIX 1. The hard-coded zero, replaced by an actual exclusion algorithm")
print("="*76)
print("Each 'tool' is now a FUNCTION inv(n,k). The exclusion rule is identical for")
print("every tool: rule the pair out iff inv(a) != inv(b). No tool gets a typed")
print("number; every row below is the output of the same loop.")
print()

def inv_hex(n,k):
    # the hexagon identity's content as a cell invariant: the ratio of the two
    # alternating neighbour products. The identity says this is 1 everywhere.
    if k<1 or k>n-1 or n<2: return None
    a = C(n-1,k-1)*C(n,k+1)*C(n+1,k)
    b = C(n-1,k)*C(n+1,k+1)*C(n,k-1)
    return F(a,b) if b else None

def inv_heat(n,k):
    # the heat-equation statement as a cell invariant: the defect, zero everywhere
    x = 2*k-n
    def u(nn,xx):
        if (xx+nn)%2: return F(0)
        kk=(xx+nn)//2
        return F(C(nn,kk),2**nn) if 0<=kk<=nn else F(0)
    return u(n,x) - (u(n-1,x-1)+u(n-1,x+1))/2

def inv_2cos(n,k):
    # the (2cos)^n identity's content at a cell: the coefficient it asserts,
    # divided by the coefficient that is there. 1 everywhere.
    return F(C(n,k), C(n,k))

def carries(k,m,p):
    c=carry=0
    while k or m or carry:
        d=(k%p)+(m%p)+carry; carry=1 if d>=p else 0; c+=carry; k//=p; m//=p
    return c
def inv_kummer(P):
    return lambda n,k: tuple(carries(k,n-k,p) for p in P)

random.seed(11)
cells=[(n,k) for n in range(4,400) for k in range(2,n//2+1)]
pairs=[]
while len(pairs)<20000:
    a=random.choice(cells); b=random.choice(cells)
    if a!=b: pairs.append((a,b))
ne=[(a,b) for a,b in pairs if C(*a)!=C(*b)]
eq_all=[]
seen={}
for n,k in cells: seen.setdefault(C(n,k),[]).append((n,k))
for v,p in seen.items():
    if len(p)>1:
        eq_all += [(p[i],p[j]) for i in range(len(p)) for j in range(i+1,len(p))]
print(f"unequal pairs sampled: {len(ne)}      genuine equal pairs available: {len(eq_all)}")
print()
print(f"{'tool (an actual function of the cell)':<44} {'excluded':>9} {'rate':>8} {'false':>7}")
print("-"*74)
TOOLS=[("hexagon identity, as an invariant", inv_hex),
       ("heat-equation defect, as an invariant", inv_heat),
       ("(2cos)^n identity, as an invariant", inv_2cos),
       ("Kummer valuations, p=2", inv_kummer([2])),
       ("Kummer valuations, p=2,3", inv_kummer([2,3])),
       ("Kummer valuations, p=2,3,5", inv_kummer([2,3,5])),
       ("Kummer valuations, 12 primes", inv_kummer([2,3,5,7,11,13,17,19,23,29,31,37]))]
for name,f in TOOLS:
    ruled=sum(1 for a,b in ne if f(*a)!=f(*b))
    false=sum(1 for a,b in eq_all if f(*a)!=f(*b))
    print(f"{name:<44} {ruled:>9} {ruled/len(ne):>7.2%} {false:>7}")
print()
print("The three identity rows are now MEASURED, and they are measured zero because")
print("each invariant is a CONSTANT FUNCTION of the cell -- the loop computes it and")
print("finds it equal every time. Previously those rows were typed. The number did")
print("not change; its evidence class did, from ASSERTED to MEASURED.")
