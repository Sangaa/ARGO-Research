from itertools import product
from collections import Counter
from fractions import Fraction as F
from math import sqrt, exp, fsum

L=8

def forms(k):
    a,b,c,d=k
    return sum(x*x for x in k),a*(b-d)+c*(b+d)

def exp_bounds(x):
    term=F(1);s=term
    for j in range(1,21):
        term*= -x/j;s+=term
    return s+term*(-x/21),s

def enclosure(hist,lo,hi):
    return (sum(v*lo**k for k,v in hist.items()),sum(v*hi**k for k,v in hist.items()))

def run():
    h0=Counter();h1=Counter(); terms=[]
    for k in product(range(-L,L+1),repeat=4):
        if sum(k)%2:continue
        A,B=forms(k)
        assert A+B>=0 and (A+B>0 or A==0)
        h0[A]+=1;h1[A+B]+=1;terms.append((A,B))
    assert sum(h0.values())==sum(h1.values())==len(terms)
    lo0,hi0=exp_bounds(F(1))
    a,b=F(1414213,10**6),F(1414214,10**6)
    assert a*a<2<b*b
    lo1=exp_bounds(b)[0];hi1=exp_bounds(a)[1]
    # Each base bounded by .7 for exp(-.4), by 1+.4+.4^2/2 > 10/7.
    assert 1+F(2,5)+F(2,5)**2/2>F(10,7)
    q=F(7,10);tail=8*q**((L+1)**2)/(1-q)*(1+2*q/(1-q))**3
    assert tail<F(1,10**8)
    x,y=enclosure(h0,lo0,hi0);u,v=enclosure(h1,lo1,hi1)
    assert F(49409,10000)<x<=y+tail<F(49410,10000)
    assert F(49716,10000)<u<=v+tail<F(49718,10000)
    assert u-y-tail>F(3,100)
    print('even lattice vectors:',len(terms),'box radius:',L)
    print('certified outside-box bound:',format(float(tail),'.10g'))
    print('F(1) certified interval: (4.9409, 4.9410)')
    print('F(sqrt(lambda)) certified interval: (4.9716, 4.9718)')
    print('certified difference > 0.03')
    lam=1+sqrt(2)
    for i in range(9):
        phase=i/8;t=lam**phase
        val=fsum(exp(-0.5*(t*t*(A+B*sqrt(2))+(A-B*sqrt(2))/(t*t))) for A,B in terms)
        print('phase',format(phase,'.3f'),'box sum',format(val,'.10f'))
if __name__=='__main__':run()
