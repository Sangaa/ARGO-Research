from itertools import combinations, product
from fractions import Fraction as Q


def add(a,b):return tuple(x+y for x,y in zip(a,b))
def det(a):return a[0]*a[2]-a[1]**2
def score(a):
    assert a[1]==0
    return min(a[0],a[2])


def select(items,k,objective):
    s=(1,0,1);chosen=[]
    for _ in range(k):
        j=max((i for i in range(len(items)) if i not in chosen),key=lambda i:objective(add(s,items[i])))
        chosen.append(j);s=add(s,items[j])
    return s,chosen


def optimum(items,k,objective):
    return max(objective(total(items,c)) for c in combinations(range(len(items)),k))


def total(items,indices):
    s=(1,0,1)
    for i in indices:s=add(s,items[i])
    return s


def main():
    print('M E-greedy E-opt ratio D-greedy E-score')
    for m in (4,10,100,1000,1000000):
        a=((2,0,2),(m,0,1),(1,0,m))
        s,c=select(a,2,score);o=optimum(a,2,score)
        t,d=select(a,2,det)
        assert c[0]==0 and score(s)==4 and o==m+2 and score(t)==o
        print(m,score(s),o,Q(score(s),o),score(t))
    # D-optimal and E-optimal can disagree even for a single choice.
    for k in (3,10,100,1000):
        a=((4*k*k,0,1),(k,0,k))
        t,c=select(a,1,det)
        assert c==[0] and score(t)==2 and optimum(a,1,score)==k+1
        print('D vs E, k=',k,'E-ratio',Q(2,k+1))
    grid=[(a,0,b) for a,b in product(range(1,6),repeat=2)]
    cases=bad=0;worst=Q(1)
    for a in combinations(grid,3):
        s,_=select(a,2,score);o=optimum(a,2,score);ratio=Q(score(s),o)
        worst=min(worst,ratio);bad+=ratio<1;cases+=1
    print('diagonal triple cases:',cases,'E-greedy suboptimal:',bad,'worst ratio:',worst)
    # Exact determinant ratio comparisons for diminishing marginal log-det gains.
    items=((4,0,0),(0,0,3),(1,1,1),(4,-2,1),(2,0,2))
    subsets=[frozenset(c) for k in range(6) for c in combinations(range(5),k)]
    checks=0
    for a in subsets:
        for b in subsets:
            if not a<=b:continue
            for i in set(range(5))-b:
                x,y=total(items,a),total(items,b)
                assert det(add(x,items[i]))*det(y)>=det(add(y,items[i]))*det(x)
                checks+=1
    print('log-det diminishing-return comparisons:',checks)
    for k in range(1,6):
        s,_=select(items,k,det);o=optimum(items,k,det)
        # Exact form of finite-k guarantee: D_g^k^k >= D_opt^(k^k-(k-1)^k), baseline det=1.
        assert det(s)**(k**k)>=o**(k**k-(k-1)**k)
    print('finite-k guarantee checks: 5')
    print('all exact assertions passed')


if __name__=='__main__':main()
