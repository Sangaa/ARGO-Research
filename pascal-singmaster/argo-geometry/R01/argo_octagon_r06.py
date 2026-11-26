from collections import Counter,defaultdict
from math import comb
import numpy as np
# lattice octagon: eight extreme points, D4 symmetry
V=[(a,b) for a,b in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]]
T=300
# exact counts up to T, saturated at T+1; all nonunit entries >= n
hist=Counter(); rows=defaultdict(list); A=np.ones((1,1),dtype=np.int32)
for n in range(1,T+1):
    L=A.shape[0]; B=np.zeros((L+4,L+4),dtype=np.int32)
    for x,y in V: B[x+2:x+2+L,y+2:y+2+L]+=A
    np.minimum(B,T+1,out=B); A=B
    counts=np.bincount(A.ravel(),minlength=T+2)
    assert counts[1]==8
    assert not counts[2:n].any()
    for t in np.flatnonzero(counts[2:T+1])+2:
        hist[int(t)]+=int(counts[t]); rows[int(t)].append((n,int(counts[t])))
    if n<=5: print('layer',n,'nonzero',np.count_nonzero(A),'value counts',[(i,int(c)) for i,c in enumerate(counts[:T+1]) if i>0 and c][:25])
# independent exact dictionary generation and comparison to saturated array for n<=12
D={(0,0):1}; A=np.ones((1,1),dtype=np.int32)
for n in range(1,13):
    E=defaultdict(int)
    for (x,y),c in D.items():
        for u,v in V: E[x+u,y+v]+=c
    D=E; L=A.shape[0]; B=np.zeros((L+4,L+4),dtype=np.int32)
    for x,y in V: B[x+2:x+2+L,y+2:y+2+L]+=A
    np.minimum(B,T+1,out=B); A=B
    assert sum(D.values())==8**n
    assert len(D)==np.count_nonzero(A)
    assert all(A[x+2*n,y+2*n]==min(c,T+1) for (x,y),c in D.items())
    assert all(D[x,y]==D[-y,x]==D[-x,y] for x,y in D)
print('Independent exact layers 12/12 PASS')
P=Counter(); Q=Counter()
for n in range(1,T+1):
    r=[comb(n,k) for k in range(n+1)]
    P.update(v for v in r if 1<v<=T)
    small=Counter(v for v in r if v<=T)
    for a,ca in small.items():
        for b,cb in small.items():
            if 1<a*b<=T: Q[a*b]+=ca*cb
print('t P Q O layer_breakdown')
for t in [2,3,4,6,8,9,12,13,19,24,36,56,63,64,65,120,168,210,252,300]: print(t,P[t],Q[t],hist[t],rows[t])
for cap in [10,100,300]:
    print('cap',cap,[(max(h[t] for t in range(2,cap+1)),[t for t in range(2,cap+1) if h[t]==max(h[u] for u in range(2,cap+1))]) for h in [P,Q,hist]])
print('octagon top',hist.most_common(15))
