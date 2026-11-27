from math import comb,isqrt,pi
from collections import defaultdict
from fractions import Fraction

RADII=(Fraction(0),Fraction(1,8),Fraction(1,4),Fraction(1,2),Fraction(1))
NS=(1,2,3,5,10,20,40,80,160)

def sign(a,b):
    if not a:return (b>0)-(b<0)
    if not b or (a>0)==(b>0):return (a>0)-(a<0)
    d=a*a-2*b*b
    return ((d>0)-(d<0))*((a>0)-(a<0))

def sq(k):
    a,b,c,d=k
    return sum(v*v for v in k),a*(b-d)+c*(b+d)

def inside(k,r):
    a,b=sq(k);p,q=r.numerator,r.denominator
    return sign(q*q*a-p*p,q*q*b)<=0

def floor_scaled(t):
    # floor(t/sqrt(2)); irrational for nonzero integer t
    return isqrt(t*t//2) if t>=0 else -isqrt(t*t//2)-1

def candidates(M):
    for b in range(-M,M+1):
        for d in range(-M+abs(b),M-abs(b)+1):
            R=M-abs(b)-abs(d)
            x,y=floor_scaled(d-b),floor_scaled(-b-d)
            for a in range(x-1,x+2):
                for c in range(y-1,y+2):
                    l=abs(a)+abs(c)
                    if l<=R and (l+abs(b)+abs(d))%2==0 and inside((a,b,c,d),RADII[-1]):
                        yield a,b,c,d

def table(M):
    return [tuple(comb(m,j) for j in range(m+1)) for m in range(M+1)]

def count(k,M,C):
    a,b,c,d=k
    u,v=abs(a+c),abs(a-c)
    w,z=abs(b+d),abs(b-d)
    low=max(u,v);high=M-max(w,z)
    return sum(C[M][m]*C[m][(m+u)//2]*C[m][(m+v)//2]*C[M-m][(M-m+w)//2]*C[M-m][(M-m+z)//2] for m in range(low,high+1,2))

def advance(p):
    q=defaultdict(int)
    for k,v in p.items():
        for i in range(4):
            for s in (-1,1):
                h=list(k);h[i]+=s;q[tuple(h)]+=v
    return q

def main():
    p={(0,0,0,0):1};checks=0
    for M in range(1,13):
        p=advance(p)
        if M%2:continue
        C=table(M);ks=set(candidates(M))
        assert ks=={k for k in p if inside(k,RADII[-1])}
        for k in ks:assert count(k,M,C)==p[k];checks+=1
        assert sum(p.values())==8**M
    print('DP cross-checks: 6 full candidate sets;',checks,'endpoint coefficients')
    print('n candidate_count exact_p scaled_r1/8 scaled_r1/4 scaled_r1/2 scaled_r1 near1/4_over_exact')
    for n in NS:
        M=2*n; C=table(M);den=8**M
        totals=[0]*len(RADII);pop=0
        for k in candidates(M):
            v=count(k,M,C);assert v>0;pop+=1
            for i,r in enumerate(RADII):
                if inside(k,r):totals[i]+=v
        assert totals[0]==count((0,0,0,0),M,C)
        assert totals==sorted(totals) and totals[-1]<=den
        print(n,pop,format(totals[0]/den,'.10g'),*(format(2*n*totals[i]/den/float(r*r),'.8f') for i,r in enumerate(RADII) if r),format(totals[2]/totals[0],'.8f'))
if __name__=='__main__':main()
