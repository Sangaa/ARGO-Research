from collections import Counter
from itertools import combinations, product
from fractions import Fraction

M=18
A=(0,1,2,3,4,6,8,14,15)
B=(0,1,2,3,5,6,7,9,13)

def canonical(s,m):
    return min(tuple(sorted((e*x+t)%m for x in s)) for e in (1,-1) for t in range(m))

def dist(x,y,m):
    d=(x-y)%m
    return min(d,m-d)

def triangles(s,m):
    return Counter(tuple(sorted(dist(x,y,m) for x,y in combinations(t,2))) for t in combinations(s,3))

def full(s,m,k):
    return Counter(tuple(dist(t[i],t[j],m) for i,j in combinations(range(k),2)) for t in product(s,repeat=k))

def deck(s,m):
    return Counter(((y-x)%m,(z-x)%m) for x,y,z in product(s,repeat=3))

def search():
    tested=0
    for m in range(6,19):
        for k in range(3,m//2+1):
            seen={}
            for tail in combinations(range(1,m),k-1):
                s=(0,)+tail
                if s!=canonical(s,m):continue
                tested+=1;h=tuple(sorted(triangles(s,m).items()))
                if h in seen:
                    assert (m,k,seen[h],s)==(M,len(A),A,B)
                    return tested
                seen[h]=s
    raise AssertionError('not found')

def main():
    assert canonical(A,M)!=canonical(B,M)
    print('first collision in stated search order:',M,len(A),'canonical subsets tested:',search())
    print('A',A,'B',B)
    a,b=full(A,M,3),full(B,M,3)
    assert a==b and sum(a.values())==9**3
    print('ordered triangle bins:',len(a),'draws per law:',sum(a.values()))
    da,db=deck(A,M),deck(B,M)
    print('oriented cyclic triple bins differing:',sum(da[k]!=db[k] for k in da.keys()|db.keys()))
    a,b=full(A,M,4),full(B,M,4)
    diff=sorted(k for k in a.keys()|b.keys() if a[k]!=b[k]);assert diff
    w=diff[0]
    print('ordered quadruple bins union:',len(a.keys()|b.keys()),'differing:',len(diff),'draws per law:',sum(a.values()))
    print('first witness (01,02,03,12,13,23):',w,'counts:',a[w],b[w])
    # Distinct-point event with maximal certainty, if any.
    only=next(k for k in diff if min(k)>0 and (not a[k] or not b[k]))
    print('distinct-point exclusive witness:',only,'counts:',a[only],b[only])
    print('all assertions passed')
if __name__=='__main__':main()
