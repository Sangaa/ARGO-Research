from collections import defaultdict
from itertools import product
from math import sqrt
import numpy as np

BASE=((1,0),(0,1),(1,1),(1,-1))

def mul(p,q):
    out=defaultdict(int)
    for i,a in p.items():
        for j,b in q.items(): out[i+j]+=a*b
    return {i:v for i,v in out.items() if v}

def witness(s):
    k=(s+2)//4; t=s-2
    u=dict.fromkeys(range(k),1)
    f={0:1,1:-1}
    for _ in range(4): f=mul(f,u)
    v=defaultdict(int)
    for i,a in enumerate((1,-2,1)):
        for j,b in f.items():
            v[i,j+1]+=a*b
            v[i+t,j]-=a*b
    return k,f,{ij:w for ij,w in v.items() if w}

def proj(v,a,b):
    out=defaultdict(int)
    for (i,j),w in v.items(): out[a*i+b*j]+=w
    return {i:w for i,w in out.items() if w}

def sq(v):return sum(w*w for w in v.values())

def block(s,a,b):
    keys=[a*i+b*j for i,j in product(range(s+1),repeat=2)]
    lookup={v:i for i,v in enumerate(sorted(set(keys)))}
    A=np.zeros((len(lookup),len(keys)))
    A[[lookup[v] for v in keys],range(len(keys))]=1
    return A

def main():
    cases=zero=norm=0
    for s in range(5,101):
        k,f,v=witness(s)
        assert all(0<=i<=s and 0<=j<=s for i,j in v)
        for d in ((1,0),(0,1),(1,s-2)):
            assert not proj(v,*d);zero+=1
        assert sq(v)==12*sq(f);norm+=1
        dd=mul(f,{0:1,1:-2,2:1})
        assert sq(dd)==20*k;norm+=1
        assert 20*sq(f)>=k**5;norm+=1
        out=sum(sq(proj(v,*d)) for d in BASE+((1,s-2),))
        assert out<=8*sq(dd);norm+=1
        assert 3*k**4*out<=800*sq(v);norm+=1
        cases+=1
    print('sizes:',cases,'exact zero projections:',zero,'exact norm checks:',norm)
    print('s N cheapest_sigma_min witness_ratio identity_sigma_min')
    for s in (5,9,13,17,21,25,29):
        _,_,v=witness(s)
        dirs=BASE+((1,s-2),)
        A=np.vstack([block(s,*d) for d in dirs])
        sig=np.linalg.svd(A,compute_uv=False)
        w=sqrt(sum(sq(proj(v,*d)) for d in dirs)/sq(v))
        I=np.vstack([block(s,*d) for d in BASE+((1,s+1),)])
        direct=np.linalg.svd(I,compute_uv=False)[-1]
        assert sig[-1]>0 and sig[-1]<=w+1e-10 and abs(direct-1)<1e-10
        print(s,s+1,format(sig[-1],'.9g'),format(w,'.9g'),format(direct,'.9g'))
    print('numpy:',np.__version__)
if __name__=='__main__':main()
