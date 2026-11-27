from itertools import combinations, product
from fractions import Fraction as Q
from math import sqrt


def n2(v): return sum(x*x for x in v)
def summ(vs): return tuple(map(sum,zip(*vs)))

def trap(q):
    k=q+1
    e=Q(1,8*k*q**3)
    a=(Q(1,2),Q(0))
    b=(a[0]-e,Q(1,2)); c=(a[0]-e,-Q(1,2*q))
    assert all(n2(v)<1 for v in (a,b,c))
    base=n2((k*a[0],0)); checks=0
    for j in range(2):
        for l in range(q+1):
            m=j+l
            if not m: continue
            score=n2((k*a[0]-m*e,j*b[1]+l*c[1]))
            if m<k: assert score>base; checks+=1
            else: assert score<base
    return checks, e


def main():
    count=0
    for q in (1,2,3,4,8,16,32,64,128):
        c,e=trap(q);count+=c
        print('exchange radius',q,'budget',q+1,'strict trapped count patterns',c,'epsilon',e)
    print('strict partial exchange patterns:',count)
    # small exact grid: test all subsets for one-swap optimality, and bound
    # r>2R: (r-2R)*(kR-d) <= (r+2R)*(kR-r).
    # Equivalent r*(r-d) <= 2R*(2*kR-r-d).
    # Use exact rational inequalities from the proof directly for all matching pairs.
    grid=[(-1,0),(0,-1),(0,0),(0,1),(1,0),(-Q(1,2),Q(1,2)),(Q(1,2),Q(1,2)),(Q(1,2),-Q(1,2))]
    cases=locals_=bad=0
    for k in (2,3,4):
        for vs in combinations(grid,2*k):
            sets=list(combinations(range(len(vs)),k)); scores={s:n2(summ(vs[i] for i in s)) for s in sets}; opt=min(scores.values())
            for s in sets:
                cases+=1
                if any(scores[t]<scores[s] for t in sets if len(set(s)-set(t))==1): continue
                locals_+=1;bad+=scores[s]>opt
                r=sqrt(scores[s]); d=sqrt(opt)
                if k>2:
                    bound=1-(sqrt(1+4*k)-1)/k
                    assert k-r+1e-12>=bound*(k-d)
                elif k==2:
                    # exact quarter check: 4 sqrt(g) <= 6 + sqrt(d)
                    w=16*scores[s]-36-opt
                    assert w<=0 or w*w<=144*opt
    print('grid selections:',cases,'one-swap local:',locals_,'nonoptimal local:',bad)
    print('general k bound checked numerically on grid; proof separate')
    print('all assertions passed')

if __name__=='__main__':main()
