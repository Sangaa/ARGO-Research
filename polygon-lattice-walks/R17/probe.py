from collections import Counter
from itertools import product
from math import comb,isqrt,pi,sqrt
from fractions import Fraction

CAP=2500

def forms(k):
    a,b,c,d=k
    A=2*sum(x*x for x in k)-(a*b+a*c+a*d+b*c+b*d+c*d)
    B=a*b+b*c+c*d-a*c-a*d-b*d
    return A,B

def mulrho(k):
    a,b,c,d=k
    return a+d,b-a+d,c-b+d,2*d-c

def coeff(n):
    h=10;p=2
    while p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:
            f=1 if p%5==1 or p==5 else 2 if p%5==4 else 4
            g=1 if p==5 else 4//f
            if e%f:return 0
            h*=comb(e//f+g-1,g-1)
        if p*p>n and n>1:p=n
        else:p+=1
    return h

def direct():
    L=isqrt(isqrt(36*CAP));D=Counter();P=Counter();pop=0
    for k in product(range(-L,L+1),repeat=4):
        pop+=1;A,B=forms(k)
        if not A or B<0 or 3*B>=A:continue
        assert (A*A-5*B*B)%4==0
        N=(A*A-5*B*B)//4
        if N<=CAP:
            assert (sum(k)%5==0)==(N%5==0)
            D[N]+=1
            if sum(k)%5==0:P[N]+=1
    for n in range(1,CAP+1):
        assert D[n]==coeff(n)
        assert P[n]==(coeff(n//5) if n%5==0 else 0)
    for n in range(1,CAP//5+1):assert P[5*n]==D[n]
    print('vectors scanned:',pop,'box radius:',L)
    print('norm comparisons:',2*CAP,'rescaled spectrum comparisons:',CAP//5)
    print('D norm classes:',len(D),'orbits:',sum(D.values()),'P norm classes:',len(P),'orbits:',sum(P.values()))
    print('first nonzero decagon norm classes:',sorted(D.items())[:12])
    print('first nonzero pentagon norm classes:',sorted(P.items())[:12])

def advance(p,steps):
    q=Counter()
    for k,v in p.items():
        for d in steps:q[tuple(a+b for a,b in zip(k,d))]+=v
    return q

def walk():
    P=[tuple(int(i==j) for i in range(4)) for j in range(4)]+[(-1,)*4]
    D=P+[tuple(-x for x in k) for k in P]
    p=q=Counter({(0,)*4:1})
    print('n pentagon exact collision decagon exact collision ratio_P/D')
    for n in range(1,11):
        p=advance(p,P);q=advance(q,D)
        assert sum(p.values())==5**n and sum(q.values())==10**n
        assert all(sum(k)%5==n%5 for k in p)
        cp=Fraction(sum(v*v for v in p.values()),5**(2*n))
        cd=Fraction(sum(v*v for v in q.values()),10**(2*n))
        print(n,format(float(cp),'.10g'),format(float(cd),'.10g'),format(float(cp/cd),'.9f'))

if __name__=='__main__':
    for k in product(range(-3,4),repeat=4):
        A,B=forms(k);C,D=forms(mulrho(k))
        assert (2*C,2*D)==(5*A-5*B,5*B-A)
        assert sum(mulrho(k))%5==0
    print('rho multiplication checks:',7**4)
    direct();walk()
