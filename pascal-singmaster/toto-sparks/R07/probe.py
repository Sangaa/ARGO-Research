"""R07: exact readout cost and numerical noise conditioning; requires NumPy."""
from itertools import product, combinations
from math import gcd
import numpy as np

BASE=((1,0),(0,1),(1,1),(1,-1))

def block(s,a,b):
    keys=[a*i+b*j for i,j in product(range(s+1),repeat=2)]
    vals=sorted(set(keys)); ix={v:k for k,v in enumerate(vals)}
    A=np.zeros((len(vals),len(keys)))
    A[[ix[v] for v in keys],range(len(keys))]=1
    return A

def nullity(s,ds):
    return max(0,s+1-sum(abs(b) for a,b in ds))*max(0,s+1-sum(abs(a) for a,b in ds))

def cost(s,a,b):
    N=s+1
    return N*N-max(0,N-abs(a))*max(0,N-abs(b))

def run():
    checks=0
    for s in range(1,13):
        for a,b in product(range(1,13),repeat=2):
            if gcd(a,b)!=1: continue
            assert block(s,a,b).shape[0]==cost(s,a,b)
            checks+=1
    print('exact distinct-bin checks:',checks)
    s=9; N=s+1
    base=np.vstack([block(s,*d) for d in BASE])
    print('grid:',N,'x',N,'base bins:',len(base),'base nullity:',nullity(s,BASE))
    dirs=[(a,b) for a in range(1,11) for b in range(1,11) if gcd(a,b)==1 and (a,b)!=(1,1)]
    mats={d:block(s,*d) for d in dirs}
    records=[]; rankchecks=0
    # Positive normals only; this is a bounded comparison, not a global optimum for conditioning.
    for d in dirs:
        A=np.vstack((base,mats[d])); sig=np.linalg.svd(A,compute_uv=False)
        k=nullity(s,BASE+(d,)); rank=int(sum(sig>1e-10))
        assert rank==N*N-k; rankchecks+=1
        if k==0: records.append((len(mats[d]),float(sig[-1]),d,float(sig[0]/sig[-1])))
    print('single-direction numerical rank checks:',rankchecks,'injective:',len(records))
    print('minimum single cost:',min(x[0] for x in records))
    for d in [(1,7),(2,7),(3,7),(1,8),(1,9),(1,10)]:
        r=next(x for x in records if x[2]==d)
        print('direction',d,'bins',r[0],'sigma_min',format(r[1],'.9f'),'condition',format(r[3],'.9f'))
    for budget in (73,76,80,90,100):
        feasible=[r for r in records if r[0]<=budget]
        best=max(feasible,key=lambda r:r[1]); print('single budget',budget,'best',best[2],'bins',best[0],'sigma_min',format(best[1],'.9f'))
    # Scan 2-direction designs within 100 additional bins. No negative slopes in scan.
    pairs=[]; pairchecks=0
    for d,e in combinations(dirs,2):
        c=len(mats[d])+len(mats[e])
        if c>100: continue
        A=np.vstack((base,mats[d],mats[e])); sig=np.linalg.svd(A,compute_uv=False)
        k=nullity(s,BASE+(d,e)); rank=int(sum(sig>1e-10)); assert rank==N*N-k; pairchecks+=1
        if k==0: pairs.append((c,float(sig[-1]),d,e))
    print('pair rank checks:',pairchecks,'injective:',len(pairs))
    for budget in (83,90,100):
        feasible=[r for r in pairs if r[0]<=budget]
        if feasible:
            best=max(feasible,key=lambda r:r[1]); print('pair budget',budget,'best',best[2:],'bins',best[0],'sigma_min',format(best[1],'.9f'))
    # Exact (integer) collision direction for base + (1,6); direct check.
    print('base plus (1,6) nullity:',nullity(s,BASE+((1,6),)))
    print('numpy:',np.__version__)
if __name__=='__main__':run()
