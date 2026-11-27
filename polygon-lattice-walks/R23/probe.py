from fractions import Fraction as Q
from itertools import combinations, product
from math import ceil, log


def ds(a,b):
    return sum((x-y)**2 for x,y in zip(a,b))


def signature(t):
    return tuple(sorted(ds(a,b) for a,b in combinations(t,2)))


def margin(s, t):
    ref=signature(t)
    rivals=[signature(q) for q in combinations(s,3) if set(q)!=set(t)]
    return min(max(abs(x-y) for x,y in zip(ref,r)) for r in rivals)


def locate(d,L,c,h):
    x=(d[0]-d[1]+L*L)/(2*L)
    y=(d[0]-d[2]+c*c+h*h-2*c*x)/(2*h)
    return x,y


def main():
    a=(Q(0),Q(0));b=(Q(2),Q(0));p=(Q(3,4),Q(1,4));q=(p[0],-p[1])
    checks=0
    print('h anchor_margin alternative_margin max_vertical_gain alternative_gain ambiguous_noise')
    for k in range(3,13):
        h=Q(1,2**k);c=(Q(1,2),h);anchors=(a,b,c)
        s=anchors+(p,);t=anchors+(q,)
        g=margin(s,anchors);g2=margin(t,anchors);alt=margin(s,(a,b,p))
        assert g>=Q(23,64) and g2>=Q(23,64) and alt>0
        assert len(set(signature(anchors)))==3
        dp=tuple(ds(p,x) for x in anchors);dq=tuple(ds(q,x) for x in anchors)
        assert locate(dp,Q(2),Q(1,2),h)==p and locate(dq,Q(2),Q(1,2),h)==q
        assert max(abs(x-y) for x,y in zip(dp,dq))==h
        mid=tuple((x+y)/2 for x,y in zip(dp,dq))
        assert all(abs(x-y)<=h/2 for d in (dp,dq) for x,y in zip(mid,d))
        assert locate(mid,Q(2),Q(1,2),h)==(p[0],Q(0))
        # exact bounded noise vertices for both possible reference triangles
        for ref,target in ((anchors,p),((a,b,p),c)):
            cc,hh=ref[2];base=tuple(ds(target,x) for x in ref);eta=Q(1,1000)
            gains=[]
            for e in product((-eta,eta),repeat=3):
                x,y=locate(tuple(u+v for u,v in zip(base,e)),Q(2),cc,hh)
                assert abs(x-target[0])<=eta/2 and abs(y-target[1])<=eta/hh
                gains.append(abs(y-target[1])/eta);checks+=1
            assert max(gains)==1/hh
        print(str(h),str(min(g,g2)),str(alt),str(1/h),4,str(h/2))
    print('exact noise vertex checks:',checks)
    print('N expected unique triangle quadruples 95pct all points sufficient bound')
    for N in (4,10,20,50,100):
        # 6/N^3 chance of unordered anchor event; conditional fourth point uniform.
        K=ceil(N**4/6*log(20*N))
        print(N,str(Q(N**3,6)),K)
    print('all exact assertions passed; sample counts are formula evaluations, not simulation')

if __name__=='__main__':main()
