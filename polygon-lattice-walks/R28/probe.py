from fractions import Fraction as F
from itertools import combinations
from heapq import heappop, heappush
from math import sqrt


def params(q):
    k=q+1
    return k,F(1,8*k*q**3)


def cost(q,j,l):
    k,e=params(q)
    return (F(k,2)-(j+l)*e)**2+F(j*q-l,2*q)**2


def neighbors(q,p):
    j,l=p
    for a,b in ((0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1)):
        x,y=j+a,l+b
        if 0<=x<=1 and 0<=y<=q:yield x,y


def minimax(start,end,weight,adj):
    best={start:weight(start)};heap=[(best[start],start)]
    while heap:
        c,u=heappop(heap)
        if best[u]!=c:continue
        if u==end:return c
        for v in adj(u):
            z=max(c,weight(v))
            if v not in best or z<best[v]:
                best[v]=z;heappush(heap,(z,v))
    raise AssertionError('disconnected')


def reachable(start,end,weight,adj,threshold,strict=False):
    ok=lambda u:weight(u)<threshold if strict else weight(u)<=threshold
    if not ok(start):return False
    seen={start};todo=[start]
    while todo:
        u=todo.pop()
        if u==end:return True
        for v in adj(u):
            if v not in seen and ok(v):seen.add(v);todo.append(v)
    return False


def main():
    count=0;states=0
    for q in range(1,129):
        w=lambda p:cost(q,*p); adj=lambda p:neighbors(q,p)
        s,t=(0,0),(1,q);m=(q+1)//2
        peak=w((0,m))
        path=[(0,l) for l in range(m+1)]+[(1,l) for l in range(m,q+1)]
        assert all(v in list(adj(u)) for u,v in zip(path,path[1:]))
        assert max(map(w,path))==peak
        assert minimax(s,t,w,adj)==peak
        assert reachable(s,t,w,adj,peak) and not reachable(s,t,w,adj,peak,True)
        count+=1;states+=2*(q+1)
        if q in (1,2,4,8,16,32,64,128):
            k,e=params(q);delta=peak-w(s)
            loss=float(delta)/(sqrt(float(peak))+k/2)
            gain=float(k*e)
            print('q',q,'squared barrier',str(delta),'loss/gain',format(loss/gain,'.8f'))
    print('count-graph cases:',count,'states:',states)
    # Independent identity graph; enumerate all k-subsets, not quotient transitions.
    total=0
    for q in range(1,6):
        k,e=params(q);pool=set(range(2*k));start=tuple(range(k));end=tuple(range(k,2*k))
        def w(s):
            j=int(k in s);l=sum(i>k for i in s)
            return cost(q,j,l)
        def adj(s):
            a=set(s)
            for x in a:
                for y in pool-a:yield tuple(sorted(a-{x}|{y}))
        peak=cost(q,0,(q+1)//2)
        assert minimax(start,end,w,adj)==peak
        assert not reachable(start,end,w,adj,peak,True)
        total+=sum(1 for _ in combinations(pool,k))
    print('identity graph cases: 5; total vertices:',total)
    print('all exact assertions passed; loss/gain displays are floating proxies')


if __name__=='__main__':main()
