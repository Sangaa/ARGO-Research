from itertools import product
from fractions import Fraction as F
from random import Random


def residual_edges(arcs):
    out=[]
    for ix,a in enumerate(arcs):
        u,v,cap,cost,flow,label=a
        if cap is None or flow<cap:
            out.append((u,v,cost,ix,1,None if cap is None else cap-flow,label))
        if flow>0:
            out.append((v,u,-cost,ix,-1,flow,label))
    return out


def cancel_negative_cycles(n, arcs):
    aug=0
    while True:
        edges=residual_edges(arcs)
        d=[0]*n
        pred=[None]*n
        update=None
        for _ in range(n):
            update=None
            for u,v,cost,ix,direction,cap,label in edges:
                if d[v]>d[u]+cost:
                    d[v]=d[u]+cost
                    pred[v]=(u,ix,direction,cap,cost,label)
                    update=v
            if update is None: break
        if update is None: return aug
        x=update
        for _ in range(n):
            assert pred[x] is not None
            x=pred[x][0]
        start=x
        cyc=[]
        while True:
            p=pred[x]
            assert p is not None
            cyc.append(p)
            x=p[0]
            if x==start: break
            assert len(cyc)<=n
        bottleneck=min(p[3] for p in cyc if p[3] is not None)
        cost=sum(p[4] for p in cyc)
        assert bottleneck>0 and cost<0
        for _u,ix,direction,_cap,_cost,_label in cyc:
            arcs[ix][4]+=direction*bottleneck
        aug+=1


def shortest_potentials(n,arcs):
    edges=residual_edges(arcs)
    d=[0]*n
    for _ in range(n-1):
        changed=False
        for u,v,cost,*_ in edges:
            if d[v]>d[u]+cost:
                d[v]=d[u]+cost; changed=True
        if not changed: break
    assert all(d[v]<=d[u]+cost for u,v,cost,*_ in edges)
    return [-x for x in d]


def solve_flow(n,demands,costs):
    # All inputs are integer numerators on a shared rational grid.
    arcs=[]
    for (j,i),w in sorted(demands.items()):
        if w>0: arcs.append([j-1,i-1,None,-w,0,('interval',j,i)])
    for k,c in enumerate(costs,start=2):
        arcs.append([k-1,k-2,c,0,0,('gap',k)])
    aug=cancel_negative_cycles(n,arcs)
    potentials=shortest_potentials(n,arcs)
    gaps=[max(0,potentials[k-1]-potentials[k-2]) for k in range(2,n+1)]
    value=sum(costs[k-2]*gaps[k-2] for k in range(2,n+1))
    flow_value=-sum(a[3]*a[4] for a in arcs)
    assert value==flow_value
    loads={k:sum(a[4] for a in arcs if a[5][0]=='interval' and a[5][1]<k<=a[5][2]) for k in range(2,n+1)}
    for a in arcs:
        if a[5][0]=='gap': assert a[4]==loads[a[5][1]]<=a[2]
    return gaps,value,flow_value,aug,arcs,potentials


def brute_primal(n,demands,costs):
    M=max(demands.values(),default=0)
    best=None; count=0; witnesses=[]
    for g in product(range(M+1),repeat=n-1):
        count+=1
        if all(sum(g[k-2] for k in range(j+1,i+1))>=w for (j,i),w in demands.items()):
            val=sum(costs[k]*g[k] for k in range(n-1))
            if best is None or val<best: best=val; witnesses=[g]
            elif val==best: witnesses.append(g)
    assert best is not None
    return best,count,witnesses


def brute_dual(n,demands,costs):
    intervals=[(j,i,w) for (j,i),w in sorted(demands.items()) if w>0]
    caps=[min(costs[k-2] for k in range(j+1,i+1)) for j,i,_ in intervals]
    best=0; count=0
    for ys in product(*(range(c+1) for c in caps)):
        count+=1
        if all(sum(y for y,(j,i,_w) in zip(ys,intervals) if j<k<=i)<=costs[k-2] for k in range(2,n+1)):
            best=max(best,sum(y*x[2] for y,x in zip(ys,intervals)))
    return best,count


def run_grid(D, seed, per_n=12):
    rng=Random(seed); cases=0; ptotal=dtotal=aug_total=0
    for n in (2,3,4):
        pairs=[(j,i) for j in range(1,n) for i in range(j+1,n+1)]
        for _ in range(per_n):
            costs=[rng.randrange(0,5) for _ in range(n-1)]
            demands={pair:rng.randrange(0,5) for pair in pairs}
            gaps,value,flow,aug,arcs,pot=solve_flow(n,demands,costs)
            primal,pc,_=brute_primal(n,demands,costs)
            dual,dc=brute_dual(n,demands,costs)
            assert value==flow==primal==dual,(n,demands,costs,gaps,value,primal,dual,pot)
            # Check returned primal vector against every original interval.
            assert all(sum(gaps[k-2] for k in range(j+1,i+1))>=w for (j,i),w in demands.items())
            cases+=1; ptotal+=pc; dtotal+=dc; aug_total+=aug
    return cases,ptotal,dtotal,aug_total


def main():
    int_w={ (1,3):3 }; int_c=[1,10]
    g,v,*_=solve_flow(3,int_w,int_c)
    assert g==[3,0] and v==3,(g,v)
    D=6
    rat_w={(1,3):2} # 1/3
    rat_c=[2,4] # 1/3, 2/3
    gr,vr,*_=solve_flow(3,rat_w,rat_c)
    assert gr==[2,0] and F(vr,D*D)==F(1,9),(gr,vr)
    c1=run_grid(1,20261127,12)
    c6=run_grid(6,20261128,12)
    print('integer witness recovered gaps:',g,'objective:',v)
    print('rational witness recovered gaps:',[F(x,D) for x in gr],'objective:',F(vr,D*D))
    print('integer cases / primal tuples / dual tuples / augmentations:',*c1)
    print('sixth-grid cases / primal tuples / dual tuples / augmentations:',*c6)
    print('all recovered primal vectors, residual potentials, flow bounds, and primal/dual/flow equality assertions passed')

if __name__=='__main__': main()
