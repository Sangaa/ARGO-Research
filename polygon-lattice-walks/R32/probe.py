from fractions import Fraction as F
from itertools import product


def layers(k):
    q=k-1;e=F(1,8*k*q**3)
    return [max(F(0),(F(min(n,k-n)**2,4*q*q)-k*n*e+n*n*e*e)/(k-n*e)) for n in range(k+1)]


def envelope(z,r):
    w=z[:]
    for i in range(1,len(w)):w[i]=max(w[i],w[i-1]-r)
    for i in range(len(w)-2,-1,-1):w[i]=max(w[i],w[i+1]-r)
    return w


def main():
    cases=checks=0
    for k in range(2,130):
        z=layers(k);p=max(z)
        r0=max(z[i]/min(i,k-i) for i in range(1,k))
        r1=max(abs(b-a) for a,b in zip(z,z[1:]))
        assert r0<=r1
        for r in (0,r0/2,r0,(r0+r1)/2,r1,2*r1):
            w=envelope(z,r)
            assert w==[max(v-r*abs(i-j) for j,v in enumerate(z)) for i in range(k+1)]
            assert max(w)==p and all(a>=b for a,b in zip(w,z))
            assert all(abs(b-a)<=r for a,b in zip(w,w[1:]))
            assert (w[0]==w[-1]==0)==(r>=r0)
            assert (w==z)==(r>=r1)
            checks+=1
        cases+=1
        if k in (5,9,17,33,65,129):
            print(k,*(f'{float(v):.9f}' for v in (k*k*r0,k*k*r1,sum(envelope(z,r0)),sum(z))))
    # Exhaustive discrete schedules: enumerate all interior integer levels 0..4.
    brute=0
    for interior in product(range(5),repeat=3):
        z=[0,*interior,0]
        for r in range(5):
            w=envelope(z,r);costs=[]
            for mid in product(range(5),repeat=3):
                v=[0,*mid,0]
                if all(a>=b for a,b in zip(v,z)) and all(abs(a-b)<=r for a,b in zip(v,v[1:])):costs.append(sum(v))
            assert bool(costs)==(w[0]==w[-1]==0)
            if costs:assert min(costs)==sum(w)
            brute+=1
    print('family sizes:',cases,'exact envelope checks:',checks,'brute integer schedule cases:',brute)
    print('all assertions passed; printed decimals are numerical proxies')


if __name__=='__main__':main()
