from fractions import Fraction as F
from math import comb, gcd
from itertools import combinations

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def div(a,b):
    a=list(a); q=[0]*(len(a)-len(b)+1)
    for i in range(len(q)-1,-1,-1):
        assert a[i+len(b)-1]%b[-1]==0
        q[i]=a[i+len(b)-1]//b[-1]
        for j,x in enumerate(b): a[i+j]-=q[i]*x
    assert not any(a)
    return q

def cyclo(n):
    p=[-1]+[0]*(n-1)+[1]
    for k in range(1,n):
        if n%k==0: p=div(p,cyclo(k))
    return p

def moment(p,j): return sum(v*x**j for x,v in p.items())
def fold(p,m): return tuple(sum(v for x,v in p.items() if x%m==r) for r in range(m))
def conv(p,q):
    r={}
    for x,a in p.items():
        for y,b in q.items(): r[x+y]=r.get(x+y,0)+a*b
    return r

def make(d,ms,s):
    ds={k for m in ms for k in range(2,m+1) if m%k==0}
    h=[(-1)**i*comb(d,i) for i in range(d+1)]
    for k in sorted(ds): h=mul(h,cyclo(k))
    D=len(h)-1
    assert s+2>=D
    for _ in range(s+2-D): h=mul(h,[1,1])
    p={x:F(comb(s,x),2**s) for x in range(s+1)}
    e=min(p[i-1]/(-v) for i,v in enumerate(h) if v<0)/2
    q={i-1:p.get(i-1,0)+e*v for i,v in enumerate(h)}
    return p,q,D,e

def run():
    cases=checks=folds=powers=0
    for count in (1,2,3):
        for ms in combinations(range(2,9),count):
            for d in (2,4,6):
                D=d+sum(sum(gcd(i,k)==1 for i in range(1,k+1)) for k in {k for m in ms for k in range(2,m+1) if m%k==0})
                for s in (D-2,D-1,D):
                    p,q,degree,e=make(d,ms,s)
                    assert D==degree and min(q.values())>0 and p!=q
                    assert sum(q.values())==1
                    for j in range(d):
                        assert moment(p,j)==moment(q,j); checks+=1
                    assert moment(q,d)>moment(p,d)
                    for m in ms: assert fold(p,m)==fold(q,m); folds+=1
                    cases+=1
    p,q,D,e=make(4,(3,5),8)
    a,b={0:F(1)},{0:F(1)}
    for n in range(1,7):
        a,b=conv(a,p),conv(b,q)
        assert all(moment(a,j)==moment(b,j) for j in range(4))
        assert fold(a,3)==fold(b,3) and fold(a,5)==fold(b,5)
        assert moment(b,4)-moment(a,4)==n*(moment(q,4)-moment(p,4))
        powers+=1
    print('rivals:',cases,'moment comparisons:',checks,'residue vectors:',folds)
    print('example degree:',D,'epsilon:',e,'weights:',list(q.items()))
    print('first moment gap:',moment(q,4)-moment(p,4),'mod7 differs:',fold(p,7)!=fold(q,7))
    print('convolution steps checked:',powers)
if __name__=='__main__': run()
