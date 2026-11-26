import sys; sys.set_int_max_str_digits(200000)
from math import comb
from fractions import Fraction as Fr
import json
res={}

# the distance-sqrt(3) class, d=e=1: C(n,k) = C(n-1,k+1)
# ratio C(n-1,k+1)/C(n,k) = (n-k)(n-k-1) / ((k+1) n)
def conic(n,k): return (n-k)*(n-k-1) - n*(k+1)
sols=[(n,k) for n in range(2,200001) for k in ([] if n<2 else [])]  # placeholder
# solve the conic directly: for each k, solve quadratic in n
import math
conic_sols=[]
for k in range(0,200000):
    # (n-k)(n-k-1) = n(k+1)  ->  n^2 - n(2k+1) + k^2+k = n(k+1)
    # n^2 - n(3k+2) + k(k+1) = 0
    D=(3*k+2)**2 - 4*k*(k+1)
    s=math.isqrt(D)
    if s*s==D:
        for n in ((3*k+2+s)//2, (3*k+2-s)//2):
            if (3*k+2+s)%2==0 and n>k+1 and conic(n,k)==0:
                conic_sols.append((n,k))
conic_sols=sorted(set(conic_sols))
res['class_d1e1_conic']={'equation':'n^2 - (3k+2) n + k(k+1) = 0   [ (n-k)(n-k-1) = n(k+1) ]',
  'integer_solutions_k_lt_200000':conic_sols,
  'check_all_satisfy_binomial_equality':all(comb(n,k)==comb(n-1,k+1) for n,k in conic_sols if n<=5000)}

# per-displacement-class solution counts, window n<=600, k>=2, k<=n/2
NW=600
rows={n:[comb(n,k) for k in range(0,n+1)] for n in range(0,NW+1)}
cls={}
for d in range(1,9):
    for e in range(1,9):
        hits=[]
        for n in range(d+2,NW+1):
            for k in range(2,n//2+1):
                kk=k+e; nn=n-d
                if 0<=kk<=nn and rows[n][k]==rows[nn][kk]:
                    hits.append((n,k))
        if hits: cls[f'd={d},e={e} (d2={d*d+d*e+e*e})']=hits
res['displacement_classes_window_n_le_600_k_ge_2']=cls
res['classes_tested']=64
res['classes_with_any_solution']=len(cls)
print(json.dumps(res,indent=1,default=str))
