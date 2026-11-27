from itertools import product
from fractions import Fraction as F


def policy(parent,z,up,down):
    w=list(z)
    for i in range(len(w)-1,0,-1):
        p=parent[i];w[p]=max(w[p],w[i]-up)
    for i in range(1,len(w)):
        w[i]=max(w[i],w[parent[i]]-down)
    return w


def pulse(m,lead):
    T=2*m+2;end=T+m; a=T-lead
    par=[-1]; z=[0]; paths=[[],[]]
    paths[0].append(0);paths[1].append(0)
    for t in range(1,end+1):
        if t<a:
            i=len(z);par.append(paths[0][-1]);z.append(0)
            for path in paths:path.append(i)
        else:
            for b in (0,1):
                i=len(z);par.append(paths[b][-1]);z.append(m if b and t==T else 0);paths[b].append(i)
    w=policy(par,z,1,1)
    assert w[0]==0 and all(w[x[-1]]==0 for x in paths)
    assert all(w[i]>=z[i] for i in range(len(w)))
    assert all(abs(w[i]-w[par[i]])<=1 for i in range(1,len(w)))
    sums=[sum(w[i] for i in x) for x in paths]
    n=max(0,m-lead-1)
    assert sums==[n*n,m*m]
    for p in (F(1,10),F(1,2),F(9,10)):
        assert (1-p)*sums[0]+p*sums[1]-p*m*m==(1-p)*n*n
    return sums


def main():
    # root -> shared node -> two branches -> terminal nodes
    parent=[-1,0,1,1,2,3]; cases=feasible=0
    for req in product(range(4),repeat=3):
        z=[0,*req,0,0]
        for up,down,cap in product(range(4),repeat=3):
            w=policy(parent,z,up,down)
            ok=w[0]==w[4]==w[5]==0 and max(w)<=cap
            valid=[]
            for mid in product(range(cap+1),repeat=3):
                v=[0,*mid,0,0]
                if all(x>=y for x,y in zip(v,z)) and all(-down<=v[i]-v[parent[i]]<=up for i in range(1,6)):
                    valid.append(v)
            assert bool(valid)==ok
            if ok:
                assert w in valid and all(all(x<=y for x,y in zip(w,v)) for v in valid)
                feasible+=1
            cases+=1
    print('exhaustive tree instances:',cases,'feasible:',feasible)
    pulses=0
    for m in range(1,33):
        for lead in range(m+2):pulse(m,lead);pulses+=1
    print('pulse instances:',pulses,'expected-cost checks:',3*pulses)
    print('m=10, p=1/5, lead | no-event use | expected excess')
    for lead in (0,1,3,5,7,9,10):
        s=pulse(10,lead);print(lead,s[0],F(4,5)*s[0])
    print('all exact assertions passed')


if __name__=='__main__':main()
