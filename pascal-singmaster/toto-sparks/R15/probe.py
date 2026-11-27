from collections import Counter
from itertools import product
from math import isqrt, comb, exp, cosh, sqrt, log, fsum, pi

CAP=2000

def coeff(n):
    if n%2:return 0
    while n%2==0:n//=2
    a=1;p=3
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:
            if p%8==1:a*=comb(e+3,3)
            elif e%2:return 0
            else:a*=e//2+1
        p+=2
    if n>1:
        if n%8!=1:return 0
        a*=4
    return 8*a

def direct(cap):
    # A < 3 sqrt(N) for a representative; hence each coordinate squared < 3 sqrt(cap).
    L=isqrt(isqrt(9*cap));h=Counter();pop=0
    for a,b,c,d in product(range(-L,L+1),repeat=4):
        pop+=1
        if (a+b+c+d)%2:continue
        A=a*a+b*b+c*c+d*d;B=a*(b-d)+c*(b+d)
        if not A or B<0 or 3*B>=2*A:continue
        N=A*A-2*B*B
        if N<=cap:h[N]+=1
    return h,L,pop

def k0(x,panels=1024):
    h=8/panels
    return h/3*fsum((1 if i in (0,panels) else 4 if i%2 else 2)*exp(-x*cosh(i*h)) for i in range(panels+1))

def main():
    h,L,pop=direct(CAP)
    for n in range(1,CAP+1):assert h[n]==coeff(n),(n,h[n],coeff(n))
    print('cap:',CAP,'box radius:',L,'vectors scanned:',pop)
    print('norm comparisons:',CAP,'nonzero classes:',len(h),'representatives:',sum(h.values()))
    print('first nonzero norm multiplicities:',sorted(h.items())[:18])
    T=log(1+sqrt(2))
    for cap in (100,400,1600,10000):
        v=1+fsum(coeff(n)*k0(sqrt(n)) for n in range(2,cap+1,2) if coeff(n))/T
        print('Bessel norm cap:',cap,'mean proxy:',format(v,'.12f'))
    # K0(sqrt(N)) <= sqrt(pi/(2sqrt(N))) exp(-sqrt(N)).
    # coeff(N)<=8*N**3; T>1/2; sqrt(pi/2)<2; group N by floor(sqrt(N)).
    # For j>=100, block contribution <=96*(j+1)**7*exp(-j).
    # Successive term ratio <= (102/101)^7 / e < 1/2.
    # e>2, so upper bound <=192*101**7/2**100.
    assert 6*102**7 < 8*101**7 # e>8/3, sufficient for ratio <1/2
    from fractions import Fraction
    bound=Fraction(192*101**7,2**100)
    assert bound<Fraction(1,10**12)
    print('certified omitted norm tail beyond 10000:',format(float(bound),'.8g'))
    print('quadrature error NOT certified; mean decimals are proxies')
if __name__=='__main__':main()
