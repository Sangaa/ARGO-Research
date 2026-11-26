from fractions import Fraction as F
from math import comb
import itertools
def C(a,b): return comb(a,b) if 0<=b<=a else 0

def cumulants(p, J=8):
    """exact cumulants k_1..k_J of a lattice distribution p={pos:prob}"""
    mu=[sum(w*F(d)**j for d,w in p.items()) for j in range(J+1)]   # raw moments
    k=[F(0)]*(J+1)
    for n in range(1,J+1):
        s=mu[n]
        for m in range(1,n):
            s-=F(C(n-1,m-1))*k[m]*mu[n-m]
        k[n]=s
    return k
def stats(p):
    k=cumulants(p)
    var=k[2]
    g2=k[4]/var**2 if var else None          # excess kurtosis
    g1=k[3]/var**F(3,2) if var else None
    return var,k[4],g2

print("HER CUMULANT TABLE, recomputed independently with exact fractions")
TAB={"Pascal binary        (s=1,L=1)": {0:F(1,2),1:F(1,2)},
     "Pascal ternary       (s=2,L=1)": {0:F(1,4),1:F(1,2),2:F(1,4)},
     "symmetric non-Pascal (1,4,1)/6": {-1:F(1,6),0:F(4,6),1:F(1,6)},
     "unbalanced binary    p=1/3":     {0:F(2,3),1:F(1,3)}}
HERS={"Pascal binary        (s=1,L=1)": (F(1,4),F(-1,8),F(-2)),
      "Pascal ternary       (s=2,L=1)": (F(1,2),F(-1,4),F(-1)),
      "symmetric non-Pascal (1,4,1)/6": (F(1,3),F(0),F(0)),
      "unbalanced binary    p=1/3":     (F(2,9),F(-2,27),F(-3,2))}
print(f"{'generator':<32} {'variance':>10} {'kappa_4':>10} {'excess kurt':>12}  matches hers?")
print("-"*82)
allok=True
for name,p in TAB.items():
    v,k4,g2=stats(p)
    ok=(v,k4,g2)==HERS[name]; allok&=ok
    print(f"{name:<32} {str(v):>10} {str(k4):>10} {str(g2):>12}  {'YES' if ok else 'NO '}")
print(f"all four reproduced exactly: {allok}")

print()
print("HER RECOVERY FORMULAS, tested across the family f(z)=c z^m (1+z^L)^s")
print(f"{'s':>3} {'L':>3} {'sigma^2':>10} {'sL^2/4':>10} {'gamma_2':>10} {'-2/s':>8}  ok?")
print("-"*60)
ok=True
for s in range(1,7):
    for L in range(1,5):
        p={}
        for j in range(s+1): p[j*L]=F(C(s,j),2**s)
        v,k4,g2=stats(p)
        a=(v==F(s*L*L,4)); b=(g2==F(-2,s)); ok&=a and b
        print(f"{s:>3} {L:>3} {str(v):>10} {str(F(s*L*L,4)):>10} {str(g2):>10} "
              f"{str(F(-2,s)):>8}  {'ok' if a and b else 'MISMATCH'}")
print(f"\nsigma^2 = sL^2/4 and gamma_2 = -2/s hold on all 24 cases: {ok}")
print("So s = -2/gamma_2 and L^2 = 4 sigma^2 / s do recover the parameters.")
