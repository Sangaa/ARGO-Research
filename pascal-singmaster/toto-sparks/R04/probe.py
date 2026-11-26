from fractions import Fraction as F
from math import comb, gcd
from itertools import combinations_with_replacement

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def witness(a,b):
    g=gcd(a,b); A=a//g; B=b//g; S=A+B-1
    u={0:0}; x=0
    for _ in range(A):
        y=(x+B)%A; v=u[x]+B*(A-1-2*x)
        if y in u: assert u[y]==v
        else: u[y]=v
        x=y
    assert len(u)==A and x==0
    v=[-x*(x-S)-u[x%A] for x in range(B)]
    def w(y): return y*(y-S)+u[y%A]+v[y%B]
    def W(x):
        y,t=divmod(x,g)
        return g*((g-t)*w(y)+t*w(y+1))
    return W

def pascal(s): return {x:F(comb(s,x),2**s) for x in range(s+1)}
def moment(p,j): return sum(w*x**j for x,w in p.items())
def fold(p,m): return tuple(sum(w for x,w in p.items() if x%m==r) for r in range(m))
def rival(a,b,s):
    g=gcd(a,b); L=a+b-g
    h=mul([1,-3,3,-1],mul([1]+[0]*(a-1)+[-1],[int(i%g==0) for i in range(b-g+1)]))
    for _ in range(s-L-1): h=mul(h,[1,1])
    p=pascal(s); e=min(p[i-1]/(-v) for i,v in enumerate(h) if v<0)/2
    q={i-1:p.get(i-1,0)+e*v for i,v in enumerate(h)}
    return p,q,e

def run():
    pairs=noncoprime=equal=signs=periods=expectations=rivals=moments=folds=0
    for a,b in combinations_with_replacement(range(2,17),2):
        g=gcd(a,b); L=a+b-g; W=witness(a,b)
        pairs+=1; noncoprime+=g>1; equal+=a==b
        for x in range(-2*a*b,2*a*b+1):
            assert (W(x)==0 if 0<=x<=L else W(x)>0); signs+=1
            # The periodic part is additive in the two residue variables.
            f=lambda k:W(k)-k*(k-L)
            assert f(x+a+b)-f(x+a)-f(x+b)+f(x)==0; periods+=1
        for s in range(1,L+1):
            p=pascal(s); assert sum(v*W(x) for x,v in p.items())==0; expectations+=1
        for s in (L+1,L+2,L+3):
            p,q,e=rival(a,b,s)
            assert min(q.values())>0 and q!=p
            for j in range(4): assert moment(p,j)==moment(q,j); moments+=1
            assert moment(q,4)-moment(p,4)==24*e*F(a*b,g)*2**(s-L-1)
            for m in (a,b): assert fold(p,m)==fold(q,m); folds+=1
            rivals+=1
    print('pairs:',pairs,'noncoprime:',noncoprime,'equal:',equal)
    print('witness signs:',signs,'mixed periodic differences:',periods,'expectations:',expectations)
    print('rivals:',rivals,'moment comparisons:',moments,'fold comparisons:',folds)
    W=witness(4,6); print('4,6: W(-2..10):',[W(x) for x in range(-2,11)])
    p,q,e=rival(4,6,9); print('4,6,s=9: epsilon:',e,'fourth moment gap:',moment(q,4)-moment(p,4))
if __name__=='__main__': run()
