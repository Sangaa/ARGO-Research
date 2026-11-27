from fractions import Fraction as F
from itertools import combinations


def gaps(T,m):
    return tuple((i+1)*T//m-i*T//m for i in range(m))


def delay(g,s):
    m=len(g);T=sum(g);r=1-s
    first=F(sum(x*(x-1) for x in g),2)
    extra=sum(r**j*sum(g[i]*g[(i+j)%m] for i in range(m)) for j in range(1,m+1))/(1-r**m)
    return (first+extra)/T


def compositions(T,m):
    for cuts in combinations(range(1,T),m-1):
        yield tuple(b-a for a,b in zip((0,*cuts),(*cuts,T)))


def main():
    cases=checks=0
    for T in range(1,13):
        for m in range(1,T+1):
            g=gaps(T,m)
            for l in range(1,2*m+1):
                a=[sum(g[(i+j)%m] for j in range(l)) for i in range(m)]
                assert max(a)-min(a)<=1
            for s in (F(1),F(3,4),F(1,2),F(1,5)):
                opt=delay(g,s)
                for h in compositions(T,m):
                    assert delay(h,s)>=opt
                    checks+=1
                bound=F(T,m)*(2-s)/(2*s)-F(1,2)
                assert opt>=bound and (opt==bound)==(T%m==0)
                cases+=1
    print('period/rate cases:',cases,'exact composition comparisons:',checks)
    print('period 30, audits 5: balanced versus clustered')
    for s in (F(1),F(3,4),F(1,2),F(1,5)):
        print(s,delay((6,)*5,s),delay((1,1,1,1,26),s))
    print('all assertions passed')


if __name__=='__main__':main()
