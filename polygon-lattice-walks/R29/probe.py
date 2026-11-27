from itertools import combinations
from math import sqrt


def score(q,j,l):
    k=q+1; D=8*k*q**3
    return (k*D//2-j-l)**2+((j*q-l)*(D//(2*q)))**2


def formula(q,p):
    n=q+1-p; m=n//2
    return score(q,0,m) if n%2==0 else score(q,1,m+p-1)


def dist(a,b):
    x,y=(v-u for u,v in zip(a,b))
    return (abs(x)+abs(y)+abs(x+y))//2


def connected(vertices,weights,start,end,p,threshold,metric):
    if weights[start]>threshold or weights[end]>threshold:return False
    unseen={v for v in vertices if weights[v]<=threshold and v!=start}
    todo=[start]
    while todo:
        u=todo.pop()
        if u==end:return True
        near={v for v in unseen if metric(u,v)<=p}
        unseen.difference_update(near);todo.extend(near)
    return False


def main():
    cases=checks=0
    for q in range(1,65):
        k=q+1; V=[(j,l) for j in (0,1) for l in range(k)]
        w={v:score(q,*v) for v in V}; start=(0,0);end=(1,q)
        old=None
        for p in range(1,k+1):
            f=formula(q,p)
            assert connected(V,w,start,end,p,f,dist)
            assert not connected(V,w,start,end,p,f-1,dist)
            assert (f==w[start])==(p==k)
            if old is not None:assert f<=old
            old=f;cases+=1;checks+=2
            # B <= G iff sqrt(f) <= start radius + k in scaled units.
            D=8*k*q**3
            if q>=3:assert (f<=(k*D//2+k)**2)==(p>=q)
        if q in (4,16,64):
            print('k',k,'p, loss/gain (decimal proxy):')
            for p in sorted({1,k//2,k-4,k-3,k-2,k-1,k}-{0}):
                if p<1:continue
                f=formula(q,p);base=k*D//2
                ratio=(f-base*base)/(sqrt(f)+base)/k
                print(p,format(ratio,'.8f'))
    print('count graph cases:',cases,'threshold checks:',checks)
    full=0
    for q in range(1,5):
        k=q+1; V=list(combinations(range(2*k),k)); sets={v:set(v) for v in V}
        w={v:score(q,int(k in v),sum(i>k for i in v)) for v in V}
        metric=lambda a,b:len(sets[a]-sets[b])
        for p in range(1,k+1):
            f=formula(q,p);a=tuple(range(k));b=tuple(range(k,2*k))
            assert connected(V,w,a,b,p,f,metric)
            assert not connected(V,w,a,b,p,f-1,metric)
            full+=1
    print('identity graph cases:',full,'threshold checks:',2*full)
    print('all exact assertions passed; displayed ratios only are floating proxies')


if __name__=='__main__':main()
