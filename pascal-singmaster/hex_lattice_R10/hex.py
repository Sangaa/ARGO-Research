from fractions import Fraction as F
from math import comb, isqrt, gcd
import random, json

out = {}

# ---- 1. verify the six neighbour ratios exactly ----
def ratios(n,k):
    V = comb(n,k)
    nb = {
      '(n,k+1)'   : (n,   k+1, F(n-k, k+1)),
      '(n,k-1)'   : (n,   k-1, F(k, n-k+1)),
      '(n-1,k)'   : (n-1, k,   F(n-k, n)),
      '(n-1,k-1)' : (n-1, k-1, F(k, n)),
      '(n+1,k)'   : (n+1, k,   F(n+1, n-k+1)),
      '(n+1,k+1)' : (n+1, k+1, F(n+1, k+1)),
    }
    bad=[]
    for name,(a,b,r) in nb.items():
        if not (0<=b<=a): continue
        lhs = F(comb(a,b), V)
        if lhs != r: bad.append((name,n,k,str(lhs),str(r)))
    return bad

random.seed(7)
tested=0; bad=[]
for _ in range(4000):
    n=random.randint(2,400); k=random.randint(1,n-1)
    bad += ratios(n,k); tested+=1
for n in range(2,60):
    for k in range(1,n):
        bad += ratios(n,k); tested+=1
out['ratio_check'] = {'points_tested':tested,'mismatches':len(bad),'examples':bad[:3]}

# ---- 2. closed hexagon cycle: product of the six step-ratios = 1 (telescoping) ----
# walk the hexagon ring around (n,k): (n,k+1)->(n+1,k+1)->(n+1,k)->(n,k-1)->(n-1,k-1)->(n-1,k)->(n,k+1)
ring = [(0,1),(1,1),(1,0),(0,-1),(-1,-1),(-1,0)]
cyc_bad=0; cyc_tested=0
for n in range(3,120):
    for k in range(2,n-1):
        pts=[(n+dn,k+dk) for dn,dk in ring]
        if any(not (0<=b<=a) for a,b in pts): continue
        prod=F(1)
        for i in range(6):
            a,b=pts[i]; c,d=pts[(i+1)%6]
            prod *= F(comb(c,d), comb(a,b))
        cyc_tested+=1
        if prod!=1: cyc_bad+=1
out['closed_cycle'] = {'rings_tested':cyc_tested,'product_ne_1':cyc_bad}

# ---- 3. Star of David / hexagon product identity, and its gcd form ----
sd_bad=0; sd_tested=0; gcd_bad=0
for n in range(2,160):
    for k in range(1,n):
        if not (0<=k-1 and k+1<=n-0 and n+1>=k+1): continue
        try:
            A=comb(n-1,k-1)*comb(n,k+1)*comb(n+1,k)
            B=comb(n-1,k)*comb(n,k-1)*comb(n+1,k+1)
        except ValueError:
            continue
        if k+1>n: continue
        sd_tested+=1
        if A!=B: sd_bad+=1
        g1=gcd(gcd(comb(n-1,k-1),comb(n,k+1)),comb(n+1,k))
        g2=gcd(gcd(comb(n-1,k),comb(n,k-1)),comb(n+1,k+1))
        if g1!=g2: gcd_bad+=1
out['star_of_david'] = {'hexagons_tested':sd_tested,'product_mismatch':sd_bad,'gcd_mismatch':gcd_bad}

# ---- 4. the six neighbour-EQUALITY equations, solved exactly ----
# equality means the ratio == 1
sols = {
 '(n,k+1)':   'n-k = k+1      -> n = 2k+1   (interior: the mirror pair in the same row)',
 '(n,k-1)':   'k = n-k+1      -> n = 2k-1   (same pair, read from the other side)',
 '(n-1,k)':   'n-k = n        -> k = 0      (boundary only)',
 '(n-1,k-1)': 'k = n          -> k = n      (boundary only)',
 '(n+1,k)':   'n+1 = n-k+1    -> k = 0      (boundary only)',
 '(n+1,k+1)': 'n+1 = k+1      -> k = n      (boundary only)',
}
# brute-force confirmation over a window
d1=[]
for n in range(1,300):
    for k in range(0,n+1):
        V=comb(n,k)
        for dn,dk in [(0,1),(0,-1),(-1,0),(-1,-1),(1,0),(1,1)]:
            a,b=n+dn,k+dk
            if 0<=b<=a and comb(a,b)==V and (a,b)!=(n,k):
                d1.append((n,k,a,b))
mirror = [t for t in d1 if t[0]==t[2]]
other  = [t for t in d1 if t[0]!=t[2]]
interior_other = [t for t in other if 1<=t[1]<=t[0]-1 and 1<=t[3]<=t[2]-1]
out['distance1'] = {'pairs_found':len(d1),'same_row_mirror':len(mirror),
                    'cross_row':len(other),'cross_row_interior':len(interior_other),
                    'cross_row_examples':other[:6],'window':'n<=299, all k'}

print(json.dumps(out, indent=1, default=str))
