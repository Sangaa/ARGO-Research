from fractions import Fraction as F
from math import comb
import itertools
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def cumulants(p,J=10):
    mu=[sum(w*F(d)**j for d,w in p.items()) for j in range(J+1)]
    k=[F(0)]*(J+1)
    for n in range(1,J+1):
        s=mu[n]
        for m in range(1,n): s-=F(C(n-1,m-1))*k[m]*mu[n-m]
        k[n]=s
    return k
def sig(p,J=10):
    k=cumulants(p,J); v=k[2]
    return tuple(k[j]/v**F(j,2) for j in range(3,J+1)), v

print("="*78)
print("IDENTIFIABILITY. s = -2/gamma_2 recovers s INSIDE the family. Does the")
print("observable pair (variance, excess kurtosis) pick the family out at all?")
print("="*78)
TARGETS={}
for s in range(1,5):
    for L in range(1,4):
        p={j*L:F(C(s,j),2**s) for j in range(s+1)}
        k=cumulants(p); TARGETS[(s,L)]=(k[2], k[4]/k[2]**2)
print("Pascal-family targets (variance, excess kurtosis):")
for (s,L),t in sorted(TARGETS.items())[:6]:
    print(f"   s={s}, L={L}:  sigma^2={t[0]}, gamma_2={t[1]}")
print()
print("Searching SYMMETRIC 5-point lattice generators on {-2..2} with integer")
print("weights over a common denominator, for any that hit a Pascal target in")
print("BOTH variance and excess kurtosis while NOT being (1+z^L)^s themselves.")
hits=[]
for a,b,c in itertools.product(range(0,25), repeat=3):      # weights for |d|=2,1,0
    tot=2*a+2*b+c
    if tot==0: continue
    p={-2:F(a,tot),-1:F(b,tot),0:F(c,tot),1:F(b,tot),2:F(a,tot)}
    p={d:w for d,w in p.items() if w}
    k=cumulants(p)
    if k[2]==0: continue
    g2=k[4]/k[2]**2
    for (s,L),(v0,g0) in TARGETS.items():
        if k[2]==v0 and g2==g0:
            pas={j*L:F(C(s,j),2**s) for j in range(s+1)}
            # compare as centred distributions (shift-invariant)
            m1=sum(d*w for d,w in pas.items())
            if m1.denominator==1:
                pasc={int(d-m1):w for d,w in pas.items()}
            else: pasc=None
            same = (pasc=={d:w for d,w in p.items()}) if pasc else False
            if not same: hits.append((a,b,c,tot,s,L,k[2],g2))
print(f"  distinct non-Pascal generators matching a Pascal target in (var, g2): "
      f"{len(hits)}")
seen=set(); show=[]
for h in hits:
    key=(h[4],h[5])
    if key not in seen: seen.add(key); show.append(h)
for a,b,c,tot,s,L,v,g2 in show[:5]:
    print(f"    weights ({a},{b},{c},{b},{a})/{tot} on (-2..2)  ==  Pascal s={s},L={L}"
          f"   sigma^2={v}, gamma_2={g2}")
print()
if hits:
    print("  -> IDENTIFIABILITY FAILS at two cumulants. The pair (sigma^2, gamma_2)")
    print("     does NOT determine the generator. Her recovery formula is correct")
    print("     and is a PARAMETER recovery inside an assumed family, exactly as")
    print("     she and the other reviewer both said. It is not model selection.")
    print()
    print("  How many cumulants separate them? Taking the first collision:")
    a,b,c,tot,s,L,v,g2 = show[0]
    p={-2:F(a,tot),-1:F(b,tot),0:F(c,tot),1:F(b,tot),2:F(a,tot)}
    p={d:w for d,w in p.items() if w}
    pas={j*L:F(C(s,j),2**s) for j in range(s+1)}
    s1,_=sig(p); s2,_=sig(pas)
    for i,(x,y) in enumerate(zip(s1,s2), start=3):
        if x!=y:
            print(f"     first standardised cumulant that differs: j={i}  "
                  f"({x} vs {y})")
            break
    else:
        print("     identical through j=10 -- would need more")
