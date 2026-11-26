from fractions import Fraction as F
from math import comb, gcd
from itertools import combinations

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def witness(a,b):
    S=a+b-1
    u={0:0}; x=0
    for _ in range(a):
        y=(x+b)%a
        v=u[x]+b*(a-1-2*x)
        if y in u: assert u[y]==v
        else: u[y]=v
        x=y
    assert len(u)==a and x==0
    v=[-x*(x-S)-u[x%a] for x in range(b)]
    return lambda x:x*(x-S)+u[x%a]+v[x%b],u,v

def moment(p,j): return sum(w*x**j for x,w in p.items())
def fold(p,m): return tuple(sum(w for x,w in p.items() if x%m==i) for i in range(m))
def pascal(s): return {x:F(comb(s,x),2**s) for x in range(s+1)}
def rival(a,b,s):
    h=mul(mul([1,-2,1],[1]+[0]*(a-1)+[-1]),[1]+[0]*(b-1)+[-1])
    for _ in range(s-a-b): h=mul(h,[1,1])
    p=pascal(s)
    eps=min(p[i-1]/(-w) for i,w in enumerate(h) if w<0)/2
    q={i-1:p.get(i-1,0)+eps*w for i,w in enumerate(h)}
    return p,q,eps

def run():
    pairs=signs=steps=expectations=rivals=moments=folds=shiftcases=0
    for a,b in combinations(range(2,17),2):
        if gcd(a,b)!=1: continue
        pairs+=1; S=a+b-1
        W,u,v=witness(a,b)
        for x in range(-3*a*b,3*a*b+1):
            assert (W(x)==0 if 0<=x<=S else W(x)>0); signs+=1
            assert W(x+b)-W(x)==2*a*b*(x//a); steps+=1
        for s in range(1,S+1):
            p=pascal(s)
            assert sum(w*W(x) for x,w in p.items())==0; expectations+=1
        for s in (a+b,a+b+1,a+b+2):
            p,q,e=rival(a,b,s)
            assert min(q.values())>0 and q!=p
            for j in range(4): assert moment(q,j)==moment(p,j); moments+=1
            assert moment(q,4)-moment(p,4)==e*24*a*b*2**(s-a-b)
            for m in (a,b): assert fold(q,m)==fold(p,m); folds+=1
            rivals+=1
        # Mean alone cannot identify: shift the whole law by +/-ab, equally.
        p=pascal(1); q={x+d:w/2 for x,w in p.items() for d in (-a*b,a*b)}
        assert sum(q.values())==1 and moment(p,1)==moment(q,1) and q!=p
        assert all(fold(p,m)==fold(q,m) for m in (a,b))
        assert moment(q,2)-moment(p,2)==(a*b)**2; shiftcases+=1
    print('coprime pairs:',pairs,'integer witness signs:',signs,'difference identities:',steps)
    print('Pascal witness expectations:',expectations,'rivals:',rivals,'raw moment comparisons:',moments,'fold comparisons:',folds)
    print('mean-only shifted controls:',shiftcases)
    W,u,v=witness(3,5)
    print('a=3,b=5: S=7, u=',u,'v=',v,'W(-2..9)=',[W(x) for x in range(-2,10)])
    p,q,e=rival(3,5,8)
    print('s=8: fourth moment gap:',moment(q,4)-moment(p,4),'epsilon:',e)
if __name__=='__main__': run()
