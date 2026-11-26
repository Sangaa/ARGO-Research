from math import gcd, comb
from functools import reduce
import sympy as sp

def conv(a,b,M=None):
    n=len(a); c=tuple(sum(a[j]*b[(r-j)%n] for j in range(n)) for r in range(n))
    return c if M is None else tuple(x%M for x in c)
def power(a,n,M=None):
    v=(1,)+(0,)*(len(a)-1)
    for _ in range(n): v=conv(v,a,M)
    return v
def orbit(a,M):
    v=(1,)+(0,)*(len(a)-1); seen={}; seq=[]
    while v not in seen:
        seen[v]=len(seq); seq.append(v); v=conv(v,a,M)
    return seen[v],len(seq)-seen[v],seq
A=(1,2,3); G=(3,6,9)
print('A6',power(A,6),'G6',power(G,6))
print('mod19 states',orbit(G,19))
print('8 powers mod19',[pow(8,i,19) for i in range(7)])
for p in (7,13,19,133): print('mod',p,'A/G',orbit(A,p)[:2],orbit(G,p)[:2])
for k in range(1,9):
    u,t,_=orbit(G,2**k);print('power2',k,u,t);assert (u,t)==(k,3*2**(k-1))
count=0
for a in range(1,8):
    m=2**a
    for k in range(1,13):
        M=2**k;v=(1,)+(0,)*(m-1);n=0
        while any(v):
            v=tuple((v[r]+v[(r-1)%m])%M for r in range(m)); n+=1
            assert n<=2**(a-1)*(k+1), (a,k,n)
        assert n==2**(a-1)*(k+1),(a,k,n)
        count+=1
print('nilpotence',count)
for b in range(1,31):
    for d in range(b+1):
        B=9*(3*b*b+d*d)*(3*b*b+3*b*d+d*d)*(3*b*b-3*b*d+d*d)
        assert power((b-d,b,b+d),6)==(B-27*d**6,B,B)
print('AP tests',sum(b+1 for b in range(1,31)))
for m in (8,19):
    x,z=sp.symbols('x z'); Q=sp.Poly(1,x)
    for d in sp.divisors(m):
        if d<=2:continue
        R=sp.Poly(sp.resultant(sp.cyclotomic_poly(d,z),x-(1+z)**m,z),x)
        c,fs=sp.factor_list(R);assert c==1 and len(fs)==1 and fs[0][1]==2
        Q*=fs[0][0]
    v=[tuple(m*sum(comb(n,k) for k in range(r,n+1,m))-2**n for r in range(m)) for n in range(251)]
    coeff=list(reversed(Q.all_coeffs())); count=0
    for n in range(int(m%2==0),251-m*Q.degree()):
        for r in range(m):
            assert sum(c*v[n+i*m][r] for i,c in enumerate(coeff))==0
            count+=1
    print('Q',m,Q.as_expr(),'checks',count)
print('G6 return moduli',sp.divisors(reduce(gcd,[power(G,6)[0]-1,*power(G,6)[1:]])))
print('PASS')
x=sp.symbols('x'); P=sp.Poly((x-6)*(x*x+3*x+3),x)
primes=list(sp.primerange(5,1000)); matches=[]
for p in primes:
    f=sp.Poly(P,x,modulus=p)
    if sp.gcd(f,f.diff()).degree()>0: matches.append(p)
assert matches==[19]
print('prime scan',len(primes),matches)
assert [M for M in range(2,1001) if power(G,6,M)==(1,0,0)]==[7,19,133]
print('moduli scan 2..1000 PASS')
count=0
for n in range(1,101):
    for p in sp.factorint(3*n*(n+1)+1):
        r=(n+1)*pow(n,-1,p)%p
        assert r!=1 and pow(r,3,p)==1 and p%3==1
        count+=1
print('hexagonal prime factors',count)
# G^3 in the nonprincipal quotient omega^2+omega+1=0:
v=power(G,3);print('G3 quotient',v[0]-v[2],v[1]-v[2], 'mod4',((v[0]-v[2])%4,(v[1]-v[2])%4))
