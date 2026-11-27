from fractions import Fraction as F
from math import sqrt


def params(q):
    k=q+1
    return k,F(1,8*k*q**3)


def xy(q,j,l):
    k,e=params(q)
    return F(k,2)-(j+l)*e,F(j*q-l,2*q)


def needed(q,j,l):
    k,_=params(q); x,y=xy(q,j,l); r=F(k,2)
    return max(F(0),(x*x+y*y-r*r)/(r+x))


def neighbors(q,u):
    j,l=u
    for a,b in ((0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1)):
        v=j+a,l+b
        if 0<=v[0]<=1 and 0<=v[1]<=q:yield v


def reachable(q,threshold,strict=False):
    ok=lambda u:needed(q,*u)<threshold if strict else needed(q,*u)<=threshold
    start=(0,0); end=(1,q)
    if not ok(start):return False
    todo=[start]; seen={start}
    while todo:
        u=todo.pop()
        if u==end:return True
        for v in neighbors(q,u):
            if v not in seen and ok(v):seen.add(v);todo.append(v)
    return False


def main():
    states=checks=0
    print('q directional trace, isotropic trace (decimal), directional/gain (decimal)')
    for q in range(1,129):
        k,e=params(q); m=(q+1)//2; r=F(k,2)
        x,y=xy(q,0,m); delta=x*x+y*y-r*r
        w=delta/(r+x)
        assert 0<w<1
        # B = sqrt(r*r+delta)-r, and B<=w<=2B using exact squares.
        assert delta<=2*r*w+w*w
        assert delta>=r*w+w*w/4
        # Balanced full-strength temporary group I suffices for all count states.
        for j in (0,1):
            for l in range(q+1):
                a,b=xy(q,j,l)
                assert a*a+b*b<=(r+1)**2
                # PSD determinant test of H+diag(0,w)-E_start I.
                assert ((r+a)*(r-a+w)>=b*b)==(needed(q,j,l)<=w)
                states+=1
        assert reachable(q,w) and not reachable(q,w,True)
        checks+=2
        path=[(0,l) for l in range(m+1)]+[(1,l) for l in range(m,q+1)]
        assert max(needed(q,*u) for u in path)==w
        assert all(v in list(neighbors(q,u)) for u,v in zip(path,path[1:]))
        if q in (1,4,8,16,32,64,128):
            B=float(delta)/(sqrt(float(r*r+delta))+float(r))
            print(q,format(float(w),'.10g'),format(2*B,'.10g'),format(float(w/(k*e)),'.8f'))
    print('count states:',states,'exact connectivity checks:',checks)
    print('all exact assertions passed; displayed decimals are numerical proxies')


if __name__=='__main__':main()
