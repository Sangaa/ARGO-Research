from math import comb
from fractions import Fraction as Q


def baseline(n,K):
    # Uniform circle: only diagonal mixed moments are nonzero.
    v=[1]+[0]*K
    for _ in range(2*n):
        v=[sum(comb(k,j)**2*v[k-j] for j in range(k+1)) for k in range(K+1)]
    return v


def mixed(m,n,K):
    # Independent signed regular-polygon steps; exact mixed moments.
    C=[[comb(p,a) for a in range(p+1)] for p in range(K+1)]
    v=[[0]*(K+1) for _ in range(K+1)];v[0][0]=1
    for s in [1]*n+[-1]*n:
        w=[[0]*(K+1) for _ in range(K+1)]
        for p in range(K+1):
            for q in range(K+1):
                w[p][q]=sum(C[p][a]*C[q][b]*s**(a+b)*v[p-a][q-b]
                            for a in range(p+1) for b in range(q+1) if (a-b)%m==0)
        v=w
    return v


def single_pair(m,k):
    # Independent check: |1-zeta^j|^(2k)=(-1)^k zeta^(-jk)(1-zeta^j)^(2k).
    return sum((-1)**(k+j)*comb(2*k,j) for j in range(2*k+1) if (j-k)%m==0)


def main():
    lower=first=calibration=pair=0
    for m in range(3,13):
        for n in range(1,6):
            v=mixed(m,n,m);b=baseline(n,m)
            radial=[v[k][k] for k in range(m+1)]
            for k in range(m):
                assert radial[k]==b[k];lower+=1
            gap= -2*n if m%2 else 2*n*(2*n-1)
            assert radial[m]-b[m]==gap;first+=1
            if n==1:
                for k in range(m+1):
                    assert radial[k]==single_pair(m,k);pair+=1
            for r in (Q(1,3),Q(1),Q(5,2)):
                u=radial[1]*r*r;w=radial[2]*r**4
                nh=1/(2*(2-w/u**2))
                assert nh==n and u/(2*nh)==r*r
                calibration+=1
    print('polygon/time cases:',first,'lower radial comparisons:',lower)
    print('first-deviation checks:',first,'independent one-pair checks:',pair,'scale/time recovery checks:',calibration)
    print('n circle_M5 pentagon_M5 decagon_M5 pentagon_gap')
    for n in (1,2,3,5,10):
        b=baseline(n,5)[5];p=mixed(5,n,5)[5][5];d=mixed(10,n,5)[5][5]
        assert d==b and p-d==-2*n
        print(n,b,p,d,p-d)
    print('n standardized pentagon-minus-decagon M5')
    for n in (1,2,3,5,10):
        print(n,str(Q(-2*n,(2*n)**5)))
    print('all assertions passed')

if __name__=='__main__':main()
