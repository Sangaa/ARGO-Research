from fractions import Fraction as F
from math import comb, gcd, lcm
from itertools import combinations_with_replacement

def mul(p,q):
    r={}
    for i,u in p.items():
        for j,v in q.items(): r[i+j]=r.get(i+j,0)+u*v
    return {i:v for i,v in r.items() if v}
def moment(p,j): return sum(v*x**j for x,v in p.items())
def fold(p,m): return tuple(sum(v for x,v in p.items() if x%m==r) for r in range(m))
def rival(a,b,c,s):
    assert 2<=a<=b<=c and s>=b+c
    h=mul(mul({0:1,a:-1},{0:1,a:-1}),mul({0:1,b:-1},{0:1,c:-1}))
    h={x-a:v for x,v in h.items()}
    p={x:F(comb(s,x),2**s) for x in range(s+1)}
    assert all(0<=x<=s for x,v in h.items() if v<0)
    e=min(p[x]/(-v) for x,v in h.items() if v<0)/2
    q={x:p.get(x,0)+e*h.get(x,0) for x in sorted(p.keys()|h.keys())}
    return p,q,e,h

def run():
    triples=coprime=noncoprime=rivals=checks=folds=powerchecks=0
    for a,b,c in combinations_with_replacement(range(2,17),3):
        triples+=1; coprime+=gcd(b,c)==1; noncoprime+=gcd(b,c)>1
        for s in (b+c,b+c+1,b+c+2):
            p,q,e,h=rival(a,b,c,s)
            assert min(q.values())>0 and p!=q and sum(q.values())==1
            for j in range(4): assert moment(p,j)==moment(q,j); checks+=1
            assert moment(q,4)-moment(p,4)==24*e*a*a*b*c
            for m in (a,b,c): assert fold(p,m)==fold(q,m); folds+=1
            rivals+=1
    p,q,e,h=rival(3,5,7,12)
    print('triples:',triples,'largest pair coprime:',coprime,'not coprime:',noncoprime)
    print('rivals:',rivals,'moment checks:',checks,'fold checks:',folds)
    print('example 3,5,7 row 12: epsilon:',e,'fourth moment gap:',moment(q,4)-moment(p,4))
    print('example perturbation:',sorted(h.items()))
    print('example mod 11 differs:',fold(p,11)!=fold(q,11))
    x=y={0:F(1)}
    for n in range(1,7):
        x,y=mul(x,p),mul(y,q)
        assert all(moment(x,j)==moment(y,j) for j in range(4))
        assert all(fold(x,m)==fold(y,m) for m in (3,5,7))
        assert moment(y,4)-moment(x,4)==24*n*e*3*3*5*7
        powerchecks+=1
    print('convolution steps checked:',powerchecks)
if __name__=='__main__': run()
