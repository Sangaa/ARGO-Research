from collections import Counter
from itertools import product
from fractions import Fraction as F

P=((0,0),(1,0),(0,2))
Q=((0,0),(4,0),(0,5))

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def conv(a,b):
    c=Counter()
    for x,u in a.items():
        for y,v in b.items():c[add(x,y)]+=u*v
    return c

def rev(a):return Counter({neg(x):v for x,v in a.items()})
def center3(a):
    mu=tuple(F(sum(k[i]*v for k,v in a.items()),sum(a.values())) for i in range(2))
    assert all((3*x).denominator==1 for x in mu)
    return Counter({tuple(3*k[i]-int(3*mu[i]) for i in range(2)):v for k,v in a.items()})
def hull(points):
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    p=sorted(points)
    def half(p):
        h=[]
        for k in p:
            while len(h)>=2 and cross(h[-2],h[-1],k)<=0:h.pop()
            h.append(k)
        return h
    return half(p)[:-1]+half(p[::-1])[:-1]
def triple(a):
    c=Counter()
    for x,y,z in product(a,repeat=3):c[sub(x,y),sub(x,z)]+=a[x]*a[y]*a[z]
    return c

def main():
    p,q=Counter(P),Counter(Q)
    a,b=map(center3,(conv(p,q),conv(p,rev(q))))
    assert len(a)==len(b)==9 and set(a.values())==set(b.values())=={1}
    assert all(sum(k[i] for k in w)==0 for i in range(2) for w in (a,b))
    ha,hb=hull(a),hull(b)
    assert len(ha)==4 and len(hb)==6
    print('A:',sorted(a));print('B:',sorted(b));print('convex hull vertices:',len(ha),len(hb))
    aa,bb=Counter({(0,0):1}),Counter({(0,0):1})
    checks=0
    for n in range(1,6):
        aa,bb=conv(aa,a),conv(bb,b)
        da,db=conv(aa,rev(aa)),conv(bb,rev(bb))
        assert da==db and sum(da.values())==9**(2*n)
        checks+=len(da)
        print('n',n,'endpoints',len(aa),len(bb),'difference bins',len(da),'collision',str(F(da[(0,0)],9**(2*n))))
    print('exact difference-bin comparisons:',checks)
    ta,tb=triple(a),triple(b)
    assert sum(ta.values())==sum(tb.values())==9**3
    keys=ta.keys()|tb.keys();bad=sorted(k for k in keys if ta[k]!=tb[k])
    assert bad
    w=bad[0]
    print('triple bins union:',len(keys),'different:',len(bad),'first witness:',w,'counts:',ta[w],tb[w])
    def moment(t):return F(sum(u[0]**2*v[0]*c for (u,v),c in t.items()),9**3)
    ma,mb=moment(ta),moment(tb)
    assert ma==F(sum(k[0]**3 for k in a),9) and mb==F(sum(k[0]**3 for k in b),9)
    assert ma-mb==256
    print('mixed triple moment:',ma,mb,'gap:',ma-mb)
    print('all assertions passed')
if __name__=='__main__':main()
