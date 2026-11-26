from fractions import Fraction as F
from math import comb

def conv(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items(): out[i+j]=out.get(i+j,F(0))+a*b
    return out

def moment(p,j): return sum(v*x**j for x,v in p.items())

def construct(s):
    d=2*((s+2)//2)
    p={i:F(comb(s,i),2**s) for i in range(s+1)}
    h={i-1:F((-1)**i*comb(d,i)) for i in range(d+1)}
    if s+2-d==1: h=conv(h,{0:F(1),1:F(1)})
    e=min(p[x]/(-v) for x,v in h.items() if v<0)/2
    q={x:p.get(x,F(0))+e*h.get(x,F(0)) for x in range(-1,s+2)}
    return d,p,q,e

def run():
    old_p={i-2:F(comb(4,i),16) for i in range(5)}
    old_q={i-3:F(v,192) for i,v in enumerate([1,6,63,52,63,6,1])}
    print('prior example P,Q moments 0..6:',[(j,str(moment(old_p,j)),str(moment(old_q,j))) for j in range(7)])
    assert all(moment(old_p,j)==moment(old_q,j) for j in range(6))
    assert moment(old_q,6)-moment(old_p,6)==F(15,4)
    assert [192*(old_q.get(x,0)-old_p.get(x,0)) for x in range(-3,4)]==[1,-6,15,-20,15,-6,1]
    count=0; layers=0; poly_checks=0
    for s in range(1,33):
        d,p,q,e=construct(s)
        assert all(v>0 for v in q.values())
        assert q!=p and sum(q.values())==1
        assert all(q[x]==q[s-x] for x in q)
        for j in range(d):
            assert moment(p,j)==moment(q,j),(s,j)
            count+=1
        from math import factorial
        assert moment(q,d)-moment(p,d)==e*2**(s+2-d)*factorial(d)
        # witness polynomial nonnegative on integer lattice; bounded check of sign
        for x in range(-50,s+51):
            val=1
            for a in range(s+1): val*=x-a
            if s%2==0: val*=x
            assert val>=0 and (val==0)==(0<=x<=s)
            poly_checks+=1
        if s<=10:
            pn=qn={0:F(1)}
            for n in range(1,7):
                pn=conv(pn,p); qn=conv(qn,q)
                assert all(moment(pn,j)==moment(qn,j) for j in range(d))
                assert moment(qn,d)-moment(pn,d)==n*(moment(q,d)-moment(p,d))
                layers+=1
    print('s=1..32; moment comparisons below d:',count)
    print('first differing moment exactly matched predicted formula: 32/32')
    print('positive symmetric rival and normalized mass: 32/32')
    print('witness polynomial integer sign checks:',poly_checks)
    print('s=1..10, convolution powers n=1..6:',layers,'cases; zero mismatches')
    for s in [1,2,3,4,5,8,16,32]:
        d,p,q,e=construct(s)
        print('s=',s,'d=',d,'eps=',e,'first moment gap=',moment(q,d)-moment(p,d))
    sizes=0
    for m in range(3,121):
        ds=[d for d in range(3,m+1) if m%d==0 and d%2==0]
        good=[s for s in range(m) if all((s-2*r-d//2)%d!=0 for r in range(m) for d in ds)]
        expect=not (m%4==0 and m&(m-1)!=0)
        assert bool(good)==expect,(m,good)
        assert all(any((s-2*r-d//2)%d!=0 for s in (0,1)) for r in range(m) for d in ds)
        sizes+=1
    print('common-phase criterion: sizes 3..120,',sizes,'sizes; zero mismatches')
if __name__=='__main__': run()
