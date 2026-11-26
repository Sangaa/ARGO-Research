import sys; sys.set_int_max_str_digits(200000)
from math import comb, isqrt
import json
res={}
# Pell reduction of the distance-sqrt(3) locus
sols=[(15,5),(104,39),(714,272),(4895,1869),(33552,12815),(229970,87840)]
rows=[]
for n,k in sols:
    D=5*k*k+8*k+4; m=isqrt(D); X=5*k+4
    rows.append({'n':n,'k':k,'5k^2+8k+4':D,'is_square':m*m==D,'m':m,
                 'X=5k+4':X,'X^2-5m^2':X*X-5*m*m})
res['pell_reduction']={'claim':'C(n,k)=C(n-1,k+1)  <=>  n=(3k+2+m)/2 with m^2=5k^2+8k+4  <=>  X^2-5m^2=-4, X=5k+4',
                       'rows':rows,
                       'all_X2_minus_5m2_equal_minus4':all(r['X^2-5m^2']==-4 for r in rows)}

# de Moivre / multiple-angle slices: coefficients of cos(n t), sin(n t) expansions are C(n,2j), C(n,2j+1)
# question: do coincidences *within* those slices add any pair the full census does not already contain?
N=1000
from collections import defaultdict
full=defaultdict(list); even=defaultdict(list); odd=defaultdict(list)
for n in range(0,N+1):
    for k in range(0,n//2+1):
        v=comb(n,k); full[v].append((n,k))
        (even if k%2==0 else odd)[v].append((n,k))
def pairs(d):
    out=[]
    for v,ps in d.items():
        if v==1 or len(ps)<2: continue
        for i in range(len(ps)):
            for j in range(i+1,len(ps)):
                out.append((v,ps[i],ps[j]))
    return out
pf,pe,po=pairs(full),pairs(even),pairs(odd)
setf={(a,b) for _,a,b in pf}
res['de_moivre_slices']={'full_census_pairs':len(pf),'even-k_slice_pairs':len(pe),'odd-k_slice_pairs':len(po),
  'slice_pairs_not_in_full_census':len([1 for _,a,b in pe+po if (a,b) not in setf]),
  'note':'cos/sin multiple-angle coefficient families are the k-even and k-odd slices of the same rows; their coincidence sets are subsets by construction, measured here rather than assumed'}

# general transition law, verified as a polynomial identity on real cells
from fractions import Fraction as Fr
def law(n,k,d,e):
    num=1
    for i in range(d+e): num*= (n-k-i)
    den=1
    for i in range(d): den*= (n-i)
    for j in range(1,e+1): den*= (k+j)
    return Fr(num,den)
bad=0; tested=0
for n in range(5,80):
    for k in range(1,n//2+1):
        for d in range(1,5):
            for e in range(1,5):
                nn,kk=n-d,k+e
                if not (0<=kk<=nn): continue
                tested+=1
                if law(n,k,d,e)!=Fr(comb(nn,kk),comb(n,k)): bad+=1
res['general_transition_law']={'formula':'C(n-d,k+e)/C(n,k) = prod_{i=0}^{d+e-1}(n-k-i) / [ prod_{i=0}^{d-1}(n-i) * prod_{j=1}^{e}(k+j) ]',
  'cells_tested':tested,'mismatches':bad,
  'consequence':'equality at displacement (d,e) is the integer-point set of ONE algebraic curve of total degree d+e; hex distance of that class is sqrt(d^2+de+e^2)'}
print(json.dumps(res,indent=1,default=str))
