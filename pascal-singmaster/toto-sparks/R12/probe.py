from math import comb, isqrt, sqrt, exp, pi, floor
from collections import defaultdict
from itertools import product

# Sign in Q(sqrt(2)), without rounded comparisons.
def sign(a,b):
    if not a:return (b>0)-(b<0)
    if not b or (a>0)==(b>0):return (a>0)-(a<0)
    d=a*a-2*b*b
    return ((d>0)-(d<0))*((a>0)-(a<0))

def mul(p,q):
    a,b=p;c,d=q
    return a*c+2*b*d,a*d+b*c

def sq(k):
    a,b,c,d=k
    return sum(x*x for x in k),a*(b-d)+c*(b+d)

def unit(k):
    a,b,c,d=k
    return b-d-a,a+c-b,b+d-c,c-a-d

def lift(k,j):
    for _ in range(j): k=unit(k)
    return k

def floor_scaled(t):
    return isqrt(t*t//2) if t>=0 else -isqrt(t*t//2)-1

def candidates(n):
    M=2*n
    for b in range(-M,M+1):
        for d in range(-M+abs(b),M-abs(b)+1):
            R=M-abs(b)-abs(d)
            x,y=floor_scaled(d-b),floor_scaled(-b-d)
            for a in (x,x+1):
                for c in (y,y+1):
                    l=abs(a)+abs(c)
                    if l<=R and (l+abs(b)+abs(d))%2==0:
                        A,B=sq((a,b,c,d))
                        if sign(n*A-1,n*B)<=0:yield a,b,c,d

def count(k,M,C):
    a,b,c,d=k
    u,v=abs(a+c),abs(a-c);w,z=abs(b+d),abs(b-d)
    return sum(C[M][m]*C[m][(m+u)//2]*C[m][(m+v)//2]*C[M-m][(M-m+w)//2]*C[M-m][(M-m+z)//2] for m in range(max(u,v),M-max(w,z)+1,2))

def table(M):
    rows=[(1,)]
    for m in range(1,M+1):
        old=rows[-1];rows.append((1,)+tuple(a+b for a,b in zip(old,old[1:]))+(1,))
    return rows

def threshold(j):
    # n* = lambda^(2j)/(2-sqrt(2)); exact floor via integer sqrt.
    A,B=1,0
    for _ in range(j):A,B=mul((A,B),(3,2))
    A,B=mul((A,B),(2,1))
    return (A+isqrt(2*B*B))//2

def main():
    tests=0
    for k in product(range(-3,4),repeat=4):
        A,B=sq(k);h=unit(k)
        assert sq(h)==mul((A,B),(3,-2)) and sum(k)%2==sum(h)%2
        tests+=1
    print('unit identities:',tests)
    # Boundary |w|^2 = 2-sqrt(2); exact enumeration because A=2.
    boundary=[k for k in product(range(-1,2),repeat=4) if sq(k)==(2,-1)]
    print('boundary multiplicity:',len(boundary),'jump in ratio:',format(len(boundary)/exp(1),'.10f'))
    # Numerical proxy for limiting sum, truncated by coordinate box.
    for L in (8,16,24):
        base=0.;num=0
        for b,d in product(range(-L,L+1),repeat=2):
            x,y=floor_scaled(d-b),floor_scaled(-b-d)
            for a,c in product((x,x+1),(y,y+1)):
                if max(abs(a),abs(c))>L or (a+b+c+d)%2:continue
                A,B=sq((a,b,c,d))
                if sign(A-2,B+1)<0:
                    base+=exp(-(A-B*sqrt(2))*(2-sqrt(2))/2)
                    num+=1
        print('truncated phase sum box',L,'strict terms',num,'right',format(base,'.10f'),'left',format(base+len(boundary)/exp(1),'.10f'))
    print('j n side exact_candidate_count ratio_to_exact')
    for j in (1,2,3):
        lower=threshold(j)
        for n in (lower,lower+1):
            M=2*n;C=table(M);ks=list(candidates(n));den=count((0,0,0,0),M,C)
            total=sum(count(k,M,C) for k in ks)
            boundary_lifts=[lift(k,j) for k in boundary]
            assert all((k in ks)==(n==lower) for k in boundary_lifts)
            print(j,n,'left' if n==lower else 'right',len(ks),format(total/den,'.10f'))
if __name__=='__main__':main()
