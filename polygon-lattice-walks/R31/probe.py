from fractions import Fraction as F
from heapq import heappop, heappush


def need(q,j,l):
    k=q+1; e=F(1,8*k*q**3); a=j+l
    return max(F(0),(F((j*q-l)**2,4*q*q)-k*a*e+a*a*e*e)/(k-a*e))


def adj(q,u):
    j,l=u
    for a,b in ((0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1)):
        v=j+a,l+b
        if 0<=v[0]<=1 and 0<=v[1]<=q:yield v


def shortest(s,t,adj,w,combine):
    best={s:w(s)}; heap=[(w(s),s)]
    while heap:
        c,u=heappop(heap)
        if c!=best[u]:continue
        if u==t:return c
        for v in adj(u):
            z=combine(c,w(v))
            if v not in best or z<best[v]:
                best[v]=z;heappush(heap,(z,v))
    raise AssertionError('disconnected')


def main():
    states=checks=0
    print('k peak capacity cumulative capacity fixed/active ratio adaptive/fixed')
    for q in range(1,129):
        k=q+1;e=F(1,8*k*q**3);m=k//2
        w=lambda u:need(q,*u);a=lambda u:adj(q,u)
        s,t=(0,0),(1,q)
        path=[(0,l) for l in range(m+1)]+[(1,l) for l in range(m,q+1)]
        # Each integer layer must be visited, and this path realizes its cheapest state.
        layers=[]
        for n in range(k+1):
            candidates=[(j,n-j) for j in (0,1) if 0<=n-j<=q]
            z=max(F(0),(F(min(n,k-n)**2,4*q*q)-k*n*e+n*n*e*e)/(k-n*e))
            assert z==min(map(w,candidates))==w(path[n]);layers.append(z)
            states+=len(candidates)
        assert all(z>0 for z in layers[1:-1]) and layers[0]==layers[-1]==0
        assert all(v in list(a(u)) for u,v in zip(path,path[1:]))
        C=sum(layers);P=max(layers)
        assert shortest(s,t,a,w,lambda x,y:x+y)==C
        assert shortest(s,t,a,w,max)==P==need(q,0,m)
        assert shortest(s,t,a,lambda u:int(w(u)>0),lambda x,y:x+y)==q
        assert C<=q*P
        checks+=3
        if q in (1,4,8,16,32,64,128):
            print(k,format(float(P),'.10g'),format(float(C),'.10g'),format(float(q*P/C),'.8f'),format(float(C/(q*P)),'.8f'))
    print('count states:',states,'shortest path objective checks:',checks)
    # Abstract graph counterexample: min peak and min sum select different paths.
    graph={'s':('a','d'),'a':('b',),'b':('c',),'c':('t',),'d':('t',),'t':()}
    w={'s':0,'a':2,'b':2,'c':2,'d':3,'t':0}
    assert shortest('s','t',graph.__getitem__,w.__getitem__,max)==2
    assert shortest('s','t',graph.__getitem__,w.__getitem__,lambda x,y:x+y)==3
    print('abstract graph: min peak 2; min sum 3 (different paths)')
    print('all exact assertions passed; displayed decimals are numerical proxies')


if __name__=='__main__':main()
