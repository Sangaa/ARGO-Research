from collections import Counter
from itertools import product
from math import isqrt, comb, exp, cosh, sqrt, log, fsum, pi

CAP=2000

def forms(k):
    a,b,c,d=k
    return a*a+b*b+c*c+d*d+a*c+b*d, a*b+b*c+c*d

def unit(k):
    # multiply by 1+z, z^4=z^2-1
    a,b,c,d=k
    return a-d,a+b,b+c+d,c+d

def coeff(n):
    a=1;p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:
            if p in (2,3):
                if e%2:return 0
            elif p%12==1:a*=comb(e+3,3)
            elif e%2:return 0
            else:a*=e//2+1
        p+=1
    if n>1:
        if n%12!=1:return 0
        a*=4
    return 12*a

def direct(cap):
    L=isqrt(isqrt(16*cap));h=Counter();pop=0
    for k in product(range(-L,L+1),repeat=4):
        pop+=1;A,B=forms(k)
        if not A or B<0 or 2*B>=A:continue
        N=A*A-3*B*B
        if N<=cap:h[N]+=1
    return h,L,pop

def k0(x,panels=1024):
    h=8/panels
    return h/3*fsum((1 if i in (0,panels) else 4 if i%2 else 2)*exp(-x*cosh(i*h)) for i in range(panels+1))

def main():
    tests=0
    for k in product(range(-3,4),repeat=4):
        A,B=forms(k)
        assert forms(unit(k))==(2*A+3*B,A+2*B)
        tests+=1
    print('unit form checks:',tests)
    h,L,pop=direct(CAP)
    for n in range(1,CAP+1):assert h[n]==coeff(n),(n,h[n],coeff(n))
    print('cap:',CAP,'box radius:',L,'vectors scanned:',pop)
    print('norm comparisons:',CAP,'nonzero classes:',len(h),'representatives:',sum(h.values()))
    print('first nonzero norm multiplicities:',sorted(h.items())[:18])
    T=log(2+sqrt(3))/2
    for cap in (100,400,1600,10000):
        v=1+fsum(coeff(n)*k0(sqrt(n)) for n in range(1,cap+1) if coeff(n))/T
        print('Bessel norm cap:',cap,'mean proxy:',format(v,'.12f'))
    # phase profile at two symmetry points, finite box, not certified
    for L in (4,6,8):
        h=Counter(forms(k) for k in product(range(-L,L+1),repeat=4))
        vals=[]
        for s in (0,T/2):
            t=exp(2*s)
            vals.append(fsum(c*exp(-((a+b*sqrt(3))*t+(a-b*sqrt(3))/t)/2) for (a,b),c in h.items()))
        print('phase box:',L,'F(1), F(sqrt(period factor)):',*(format(v,'.12f') for v in vals))
    print('no finite-time path simulation; quadrature and phase values are numerical proxies')
if __name__=='__main__':main()
