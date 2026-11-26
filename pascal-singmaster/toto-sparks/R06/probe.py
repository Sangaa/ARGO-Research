from fractions import Fraction as F
from itertools import combinations, product
from math import comb

AXES = ((1, 0), (0, 1))
EXTRA = ((1, 1), (1, -1), (1, 2), (2, -1))

def mul(p, q):
    out = {}
    for (i,j),v in p.items():
        for (k,l),w in q.items():
            key = (i+k,j+l)
            out[key] = out.get(key,0)+v*w
    return {k:v for k,v in out.items() if v}

def factor(a,b):
    return {(max(b,0),max(-a,0)):1,(max(-b,0),max(a,0)):-1}

def switching(dirs):
    h = {(0,0):1}
    for a,b in dirs:
        h = mul(h,factor(a,b))
    return h

def project(p,a,b):
    out = {}
    for (i,j),v in p.items():
        key = a*i+b*j
        out[key] = out.get(key,0)+v
    return {k:v for k,v in out.items() if v}

def moment(p,u,v):
    return sum(w*i**u*j**v for (i,j),w in p.items())

def rank(rows):
    piv = {}
    for row in rows:
        r = {i:F(v) for i,v in row.items() if v}
        while r:
            k = min(r)
            if k not in piv:
                t = r[k]
                piv[k] = {j:v/t for j,v in r.items()}
                break
            t = r[k]
            for j,v in piv[k].items():
                z = r.get(j,0)-t*v
                if z: r[j]=z
                else: r.pop(j,None)
    return len(piv)

def projection_rows(n,m,dirs):
    cells = list(product(range(n+1),range(m+1)))
    rows = []
    for a,b in dirs:
        groups = {}
        for k,(i,j) in enumerate(cells):
            groups.setdefault(a*i+b*j,{})[k]=1
        rows.extend(groups.values())
    return rows

def pascal(n,m):
    return {(i,j):F(comb(n,i)*comb(m,j),2**(n+m))
            for i,j in product(range(n+1),range(m+1))}

def rival(n,m,dirs):
    p = pascal(n,m)
    h = switching(dirs)
    assert set(h)<=set(p)
    eps = min(p[k]/(-w) for k,w in h.items() if w<0)/2
    q = {k:w+eps*h.get(k,0) for k,w in p.items()}
    assert min(q.values())>0 and q!=p and sum(q.values())==1
    return p,q,h,eps

def run():
    rank_cases = rivals = folds = moments = 0
    for k in range(len(EXTRA)+1):
        for ex in combinations(EXTRA,k):
            dirs = AXES+ex
            Bx = sum(abs(b) for a,b in dirs)
            By = sum(abs(a) for a,b in dirs)
            for n,m in product(range(6),repeat=2):
                r = rank(projection_rows(n,m,dirs))
                assert (n+1)*(m+1)-r == max(0,n-Bx+1)*max(0,m-By+1)
                rank_cases += 1
            for dn,dm in product(range(2),repeat=2):
                p,q,h,eps = rival(Bx+dn,By+dm,dirs)
                for a,b in dirs:
                    assert project(p,a,b)==project(q,a,b)
                    folds += 1
                for u in range(len(dirs)):
                    for v in range(len(dirs)-u):
                        assert moment(p,u,v)==moment(q,u,v)
                        moments += 1
                rivals += 1
    dirs = AXES+EXTRA[:2]
    p,q,h,eps = rival(3,3,dirs)
    assert moment(p,3,1)!=moment(q,3,1)
    assert project(p,1,2)!=project(q,1,2)
    print('rank comparisons:',rank_cases,'constructed rivals:',rivals)
    print('projection comparisons:',folds,'mixed moment comparisons:',moments)
    print('four-direction example epsilon:',eps)
    print('P and Q times 128, rows i=0..3:')
    for i in range(4):
        print([str(128*p[i,j]) for j in range(4)], [str(128*q[i,j]) for j in range(4)])
    print('moment (3,1) gap:',moment(q,3,1)-moment(p,3,1))
    print('projection (1,2) differs:',project(p,1,2)!=project(q,1,2))
    a=b={(0,0):F(1)}
    for n in range(1,5):
        a,b=mul(a,p),mul(b,q)
        assert all(project(a,u,v)==project(b,u,v) for u,v in dirs)
        assert moment(b,3,1)-moment(a,3,1)==n*(moment(q,3,1)-moment(p,3,1))
    print('convolution powers checked:',n)
if __name__=='__main__': run()
