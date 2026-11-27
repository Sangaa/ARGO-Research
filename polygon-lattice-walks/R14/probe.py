from collections import Counter
from itertools import product
from math import sqrt, log, exp, fsum, cosh, pi
from fractions import Fraction as Q

LAM=1+sqrt(2)
T=log(LAM)
L=8

def forms(k):
    a,b,c,d=k
    return sum(x*x for x in k),a*(b-d)+c*(b+d)

def sign(a,b):
    if not a:return (b>0)-(b<0)
    if not b or (a>0)==(b>0):return (a>0)-(a<0)
    return ((a*a>2*b*b)-(a*a<2*b*b))*((a>0)-(a<0))

def hist(L):
    return Counter(forms(k) for k in product(range(-L,L+1),repeat=4) if sum(k)%2==0)

def phase(h,x):
    # Fold exact theoretical symmetries before truncating.
    x=x%1;x=min(x,1-x)
    t=exp(2*T*x)
    return fsum(c*exp(-((a+b*sqrt(2))*t+(a-b*sqrt(2))/t)/2) for (a,b),c in h.items())

def orbit_hist(h):
    # One representative per unit orbit: 1<= |z|/|z'| < lambda^2.
    # Equivalent to B>=0 and (A+B sqrt2)<lambda^4 (A-B sqrt2).
    out=Counter()
    for (a,b),c in h.items():
        if a and b>=0 and sign(16*a-24*b,12*a-18*b)>0:
            out[a*a-2*b*b]+=c
    return out

def k0(x,N=2048):
    # Numerical proxy only: Simpson quadrature for integral_0^8 exp(-x*cosh(v)) dv.
    d=8/N
    return d/3*fsum((1 if i in (0,N) else 4 if i%2 else 2)*exp(-x*cosh(i*d)) for i in range(N+1))

def main():
    h=hist(L)
    print('even lattice vectors:',sum(h.values()),'distinct form pairs:',len(h))
    q=Q(7,10);tail=8*q**((L+1)**2)/(1-q)*(1+2*q/(1-q))**3
    assert tail<Q(1,10**8)
    print('uniform real box tail bound after phase reduction:',format(float(tail),'.12g'))
    # 2*pi*(pi/8)/log(lambda)>2.7; conservative verified bounds:
    # pi>3.14, log(lambda)<.9, lambda<2.42, cos(pi/4)> .7.
    assert Q(314,100)**2/(4*Q(9,10))>Q(27,10)
    assert sum(Q(9,10)**i/Q(__import__('math').factorial(i)) for i in range(5))>Q(242,100)
    assert Q(142,100)**2>2 and Q(7,10)**2<Q(1,2)
    assert Q(7,10)/Q(242,100)>Q(1,4)
    assert sum(Q(27,10)**i/Q(__import__('math').factorial(i)) for i in range(8))>14
    phases=[i/32 for i in range(32)]
    mean=fsum(phase(h,i/256) for i in range(256))/256
    print('256-node mean (proxy):',format(mean,'.12f'))
    print('nodes measured_spread conservative_alias_bound')
    for m in (1,2,3,4,8,12):
        vals=[fsum(phase(h,x+j/m) for j in range(m))/m for x in phases]
        bound=Q(1250,14**m-1)
        assert max(abs(v-mean) for v in vals)<float(bound)+2*float(tail)+1e-12
        print(m,format(max(vals)-min(vals),'.12g'),format(float(bound),'.12g'))
    for r in (4,6,8):
        hh=orbit_hist(hist(r));value=1+fsum(c*k0(sqrt(a)) for a,c in hh.items())/T
        print('orbit box',r,'representatives',sum(hh.values()),'norm classes',len(hh),'mean proxy',format(value,'.12f'))
    print('No finite-time paths evaluated; quadrature and orbit sums are numerical proxies.')
if __name__=='__main__':main()
