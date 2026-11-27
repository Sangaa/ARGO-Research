from itertools import combinations
from math import comb
from fractions import Fraction as F


def miss(N,d,m):
    return F(comb(N-m,d),comb(N,d)) if N-m>=d else F(0)


def budget(N,d,alpha):
    return next(m for m in range(N+1) if miss(N,d,m)<=alpha)


def main():
    # Same visible accepted labels; completions of the rejected labels can reverse rule ordering.
    completions=0
    for a in range(1,10):
        for y in range(a+1):
            for r in range(1,10):
                for z in range(r+1):
                    old=a-y+z; new=a-y+r-z
                    assert new-old==r-2*z
                    completions+=1
                assert a-y+r>a-y and a-y<a-y+r
    print('label completions:',completions)
    cases=checks=0
    for N in range(1,9):
        U=set(range(N))
        for d in range(1,N+1):
            bad=[set(x) for x in combinations(U,d)]
            for m in range(N+1):
                audits=[set(x) for x in combinations(U,m)]
                p=miss(N,d,m)
                for S in audits:
                    assert F(sum(not(S&B) for B in bad),len(bad))==p
                    checks+=1
                for B in bad:
                    assert F(sum(not(S&B) for S in audits),len(audits))==p
                    checks+=1
                cases+=1
    print('finite population cases:',cases,'exact subset checks:',checks)
    print('N=1000 | bad labels | audit budget for miss <= 5%')
    for d in (1,5,10,20,50,100):
        m=budget(1000,d,F(1,20))
        assert miss(1000,d,m)<=F(1,20) and miss(1000,d,m-1)>F(1,20)
        print(d,m)
    print('all assertions passed')


if __name__=='__main__':
    main()
