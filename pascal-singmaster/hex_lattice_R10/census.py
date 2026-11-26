import sys
sys.set_int_max_str_digits(200000)
from math import comb, gcd
from collections import defaultdict
import json

N = 1000              # rows enumerated: 0..N
# canonical representatives: k <= n/2  (the mirror k -> n-k is the trivial symmetry)
val = defaultdict(list)
for n in range(0, N+1):
    for k in range(0, n//2 + 1):
        val[comb(n,k)].append((n,k))

def hexdist2(p,q):
    dn=q[0]-p[0]; dk=q[1]-p[1]
    return dn*dn - dn*dk + dk*dk

res={}
res['census'] = {'N_rows':N,'entries':sum(len(v) for v in val.values()),
                 'distinct_values':len(val)}

# multiplicity over canonical representatives
mult=defaultdict(int)
for v,ps in val.items(): mult[len(ps)]+=1
res['multiplicity_canonical'] = dict(sorted(mult.items()))

# --- all coincidence pairs, split by whether a k<=1 representative is involved ---
pairs=[]
for v,ps in val.items():
    if len(ps)<2 or v==1: continue
    for i in range(len(ps)):
        for j in range(i+1,len(ps)):
            pairs.append((v,ps[i],ps[j]))
triv=[p for p in pairs if p[1][1]<=1 or p[2][1]<=1]
nontriv=[p for p in pairs if p[1][1]>=2 and p[2][1]>=2]
res['pairs'] = {'all':len(pairs),'with_a_k_le_1_leg':len(triv),'both_k_ge_2':len(nontriv)}

# --- hex-distance spectrum ---
import math
def spec(ps):
    d2=[hexdist2(a,b) for _,a,b in ps]
    return {'min_d2':min(d2),'max_d2':max(d2),'min_dist':round(math.sqrt(min(d2)),4),
            'max_dist':round(math.sqrt(max(d2)),4)} if d2 else None
res['distance_spectrum_nontrivial']=spec(nontriv)
res['distance_spectrum_all']=spec(triv+nontriv)
res['nontrivial_pairs_listed']=[{'V':str(v)[:24]+('…' if len(str(v))>24 else ''),
                                 'p':a,'q':b,'d2':hexdist2(a,b)} for v,a,b in sorted(nontriv,key=lambda t:hexdist2(t[1],t[2]))]

# --- control: 3003 ---
reps3003=[ (n,k) for n in range(0,3004) for k in (0,1,2) if comb(n,k)==3003 ]
reps3003 += [ p for p in val.get(3003,[]) ]
reps3003 = sorted(set(reps3003))
res['control_3003'] = {'canonical_reps_within_N':val.get(3003,[]),
                       'all_reps_any_n':reps3003,
                       'full_multiplicity_with_mirrors': 2*len(reps3003) - sum(1 for n,k in reps3003 if 2*k==n)}

# --- control: Singmaster's Fibonacci family C(F(2i+2)F(2i+3), F(2i)F(2i+3)) = C(n-1,k+1) ---
fib=[0,1]
while len(fib)<40: fib.append(fib[-1]+fib[-2])
fam=[]
for i in range(1,7):
    n=fib[2*i+2]*fib[2*i+3]; k=fib[2*i]*fib[2*i+3]
    ok = comb(n,k)==comb(n-1,k+1)
    fam.append({'i':i,'n':n,'k':k,'identity_holds':ok,
                'd2_between_the_two_cells':hexdist2((n,k),(n-1,k+1)),
                'V_digits':len(str(comb(n,k)))})
res['control_singmaster_family']=fam

# --- EXCLUSIONARY POWER (lesson 37's own test) ---
# candidate population = every ordered coincidence pair found above.
# constraint H1: product of the six step-ratios around any closed hexagon == 1
# constraint H2: Star-of-David equal-triple-products
# Both are identities in (n,k): they are satisfied by every cell, so they cannot
# reject any candidate.  Measure it rather than assert it.
def h1_ok(n,k):
    from fractions import Fraction as Fr
    ring=[(0,1),(1,1),(1,0),(0,-1),(-1,-1),(-1,0)]
    pts=[(n+dn,k+dk) for dn,dk in ring]
    if any(not (0<=b<=a) for a,b in pts): return None
    pr=Fr(1)
    for t in range(6):
        a,b=pts[t]; c,d=pts[(t+1)%6]
        pr*=Fr(comb(c,d),comb(a,b))
    return pr==1
def h2_ok(n,k):
    if not (1<=k<=n-1): return None
    return comb(n-1,k-1)*comb(n,k+1)*comb(n+1,k)==comb(n-1,k)*comb(n,k-1)*comb(n+1,k+1)

tested=0; rejected=0; inapplicable=0
for v,a,b in nontriv+triv[:4000]:
    for p in (a,b):
        r1=h1_ok(*p); r2=h2_ok(*p)
        if r1 is None and r2 is None: inapplicable+=1; continue
        tested+=1
        if (r1 is False) or (r2 is False): rejected+=1
res['exclusionary_power']={'candidate_cells_tested':tested,'rejected_by_H1_or_H2':rejected,
                           'inapplicable_boundary_cells':inapplicable,
                           'candidate_pairs_in_population':len(nontriv)+min(4000,len(triv))}
print(json.dumps(res,indent=1,default=str))
