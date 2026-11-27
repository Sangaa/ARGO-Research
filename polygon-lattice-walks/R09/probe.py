from collections import defaultdict
from itertools import product
from math import factorial, comb, pi
from fractions import Fraction

STEPS=((2,1),(1,2),(-1,2),(-2,1))
def image(k): return tuple(sum(k[i]*STEPS[i][j] for i in range(4)) for j in range(2))
def norm(k): return sum(abs(x) for x in k)
def advance(p,steps):
    q=defaultdict(int)
    for x,v in p.items():
        for d in steps: q[tuple(a+b for a,b in zip(x,d))]+=v
    return dict(q)
def collision(p): return sum(v*v for v in p.values())
def return4(n):
    # 2n steps; balanced counts on each axis
    f=[factorial(i) for i in range(n+1)]
    return sum(factorial(2*n)//(f[a]*f[b]*f[c]*f[n-a-b-c])**2
               for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1))
def run():
    zero=(0,0,0,0); steps4=[tuple(s*(i==j) for j in range(4)) for i in range(4) for s in (-1,1)]
    steps2=[image(x) for x in steps4]
    short=[k for k in product(range(-6,7),repeat=4) if 0<norm(k)<=6 and image(k)==(0,0)]
    assert set(short)=={(1,-2,2,-1),(-1,2,-2,1),(2,-1,-1,2),(-2,1,1,-2)}
    print('short kernel vectors:',short)
    p={zero:1}; q={(0,0):1}
    for n in range(1,9):
        p=advance(p,steps4); q=advance(q,steps2)
        folded=defaultdict(int)
        for k,v in p.items(): folded[image(k)]+=v
        assert dict(folded)==q and sum(p.values())==8**n
        cb,ca=collision(p),collision(q)
        assert cb==return4(n) and ca>=cb
        if n<=2: assert len(p)==len(q) and ca==cb
        if n==3: assert ca-cb==720
        print('step',n,'states',len(p),len(q),'collision counts',cb,ca,'gap',ca-cb)
    print('half-step n, return_B, return_A, ratio_A/B, ratio/(pi*n/10)')
    q={(0,0):1}
    for n in range(1,41):
        q=advance(advance(q,steps2),steps2)
        if n in (1,2,3,5,10,20,40):
            cb,ca=return4(n),q[(0,0)]
            assert ca>=cb
            print(n,cb,ca,format(ca/cb,'.9f'),format((ca/cb)/(pi*n/10),'.9f'))
if __name__=='__main__':run()
