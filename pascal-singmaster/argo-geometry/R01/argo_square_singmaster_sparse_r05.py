from math import comb,isqrt
from collections import Counter
M=10**10
P=Counter();I=Counter()
for n in range(4,isqrt(2*M)+3):
    if comb(n,2)>M:break
    for k in range(2,n//2+1):
        t=comb(n,k)
        if t>M:break
        P[t]+=1 if n==2*k else 2
for n in range(2,isqrt(M)+1):
    r=[]
    for k in range(1,n//2+1):
        a=comb(n,k)
        if a*n>M:break
        r.append((a,1 if n==2*k else 2))
    for j,(a,ma) in enumerate(r):
        for k in range(j,len(r)):
            b,mb=r[k];t=a*b
            if t>M:break
            I[t]+=ma*mb*(1 if j==k else 2)
keys=P.keys()|I.keys()|{2,3}
for cap in [10**6,10**7,10**8,10**9,10**10]:
    best=max(4*(P[t]+(1 if t==2 else 2))+I[t] for t in keys if t<=cap)
    pmax=max(P[t]+(1 if t==2 else 2) for t in keys if t<=cap)
    print(cap,'Pmax',pmax,'Qmax',best,'winners',sorted(t for t in keys if t<=cap and 4*(P[t]+(1 if t==2 else 2))+I[t]==best))
imax=max(I.values()); print('max interior',imax,'values',sorted(t for t,v in I.items() if v==imax)[:20])
print('sparse exceptional keys',len(keys))
