from itertools import combinations, product
from fractions import Fraction as Q
from decimal import Decimal, localcontext


def norm2(v):
    return sum(x*x for x in v)


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def pair(vs):
    i=min(range(len(vs)),key=lambda i:norm2(vs[i]))
    g=min(norm2(add(vs[i],v)) for j,v in enumerate(vs) if j!=i)
    d=min(norm2(add(a,b)) for a,b in combinations(vs,2))
    return g,d


def quarter(g,d,R):
    # 4*(2R-sqrt(g)) >= 2R-sqrt(d), checked without square roots.
    w=16*g-36*R*R-d
    return w<=0 or w*w<=144*R*R*d


def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)


def main():
    R=5
    grid=[v for v in product(range(-R,R+1),repeat=2) if norm2(v)<=R*R]
    cases=bad=0
    for vs in combinations(grid,3):
        g,d=pair(vs)
        assert g>=d and quarter(g,d,R)
        # Fixed trace: determinant ordering reverses squared imbalance.
        h=[norm2(add(a,b)) for a,b in combinations(vs,2)]
        assert max((2*R+1)**2-x for x in h)==(2*R+1)**2-d
        cases+=1;bad+=g>d
    print('disk grid points:',len(grid),'triples:',cases,'suboptimal greedy:',bad)
    print('exact quarter-bound and determinant checks:',cases)
    print('t | greedy/optimal (positive definite groups, baseline I)')
    with localcontext() as ctx:
        ctx.prec=60
        for j in (2,4,8,16,32,64,128,256):
            t=Q(1,j);c=(1-t*t)/(1+t*t);s=2*t/(1+t*t);r=1-t**4
            scale=1/t**4
            vs=((r*scale,0),(c*scale,s*scale),(c*scale,-s*scale))
            assert norm2(vs[0])<norm2(vs[1])==norm2(vs[2])==scale**2
            g,d=pair(vs);assert d==4*c*c*scale**2 and g>d
            assert quarter(g,d,scale)
            # Each group = (scale+1)I + traceless(v); all strictly PD.
            # Baseline I plus two groups gives scalar part 2*scale+3.
            b=2*scale+3
            ratio=(dec(b)-dec(g).sqrt())/(dec(b)-dec(d).sqrt())
            print(j,format(ratio,'.10f'))
    print('all exact assertions passed; displayed ratios are decimal proxies')


if __name__=='__main__':main()
