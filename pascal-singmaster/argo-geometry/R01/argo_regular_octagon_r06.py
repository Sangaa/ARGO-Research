from math import factorial,comb,prod
from collections import Counter,defaultdict
from itertools import product
T=300
F=[factorial(i) for i in range(T+1)]
def parts(m,lo=0,k=4):
    if k==1:
        if m>=lo: yield (m,)
        return
    for a in range(lo,m//k+1):
        for b in parts(m-a,a,k-1):yield (a,)+b
def compositions(h):
    for a in range(h+1):
        for b in range(h-a+1):
            for c in range(h-a-b+1):yield (a,b,c,h-a-b-c)
def coefficient(n,k,h):
    v=0
    for r in compositions(h):
        v+=F[n]//prod(F[x+y]*F[y] for x,y in zip(k,r))
        if v>T:return T+1
    return v
hist=Counter(); layer={}
for n in range(1,T+1):
    H=Counter()
    if n>=26: H[1]=8;H[n]=48
    else:
        for h in range(n//2+1):
            for k in parts(n-2*h):
                v=coefficient(n,k,h)
                if v<=T:
                    mult=F[4]//prod(F[c] for c in Counter(k).values())*2**sum(x>0 for x in k)
                    H[v]+=mult
    hist.update({t:c for t,c in H.items() if 1<t<=T});layer[n]=H
    assert H[1]==8
# Independent dictionary DP in Z^4, 8 signed directions.
D={(0,0,0,0):1}
for n in range(1,10):
    E=defaultdict(int)
    for k,c in D.items():
        for j in range(4):
            for s in [-1,1]:
                kk=list(k);kk[j]+=s;E[tuple(kk)]+=c
    D=E
    assert sum(D.values())==8**n
    assert Counter(c for c in D.values() if c<=T)==layer[n]
print('independent layers 9/9 PASS')
for t in [2,3,4,6,8,9,12,13,19,24,36,56,63,64,65,120,168,210,252,300]: print(t,hist[t],[(n,H[t]) for n,H in layer.items() if H[t]])
for cap in [10,100,300]:
    m=max(hist[t] for t in range(2,cap+1));print('cap',cap,'max',m,'at',[t for t in range(2,cap+1) if hist[t]==m])
