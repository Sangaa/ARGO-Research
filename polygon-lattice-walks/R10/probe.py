from itertools import product
from math import sqrt
from collections import defaultdict

def sign(a,b):
    # sign of a+b sqrt(2), exactly
    if a==0: return (b>0)-(b<0)
    if b==0 or (a>0)==(b>0): return (a>0)-(a<0)
    d=a*a-2*b*b
    return ((d>0)-(d<0))*((a>0)-(a<0))

def sq(k):
    a,b,c,d=k
    return sum(v*v for v in k), a*(b-d)+c*(b+d)

def exact_minima(N):
    best={}; pop=0
    M=2*N
    for a in range(-M,M+1):
        for b in range(-(M-abs(a)),M-abs(a)+1):
            R=M-abs(a)-abs(b)
            for c in range(-R,R+1):
                S=R-abs(c)
                for d in range(-S,S+1):
                    l=abs(a)+abs(b)+abs(c)+abs(d)
                    if not l or l%2: continue
                    pop+=1
                    k=(a,b,c,d); A,B=sq(k)
                    assert A*A-2*B*B>=2
                    n=l//2
                    if n not in best or sign(A-best[n][0],B-best[n][1])<0: best[n]=(A,B,k)
    prev=None
    for n in range(1,N+1):
        cur=best[n]
        if prev is not None and sign(cur[0]-prev[0],cur[1]-prev[1])>=0: cur=prev
        best[n]=prev=cur
        A,B,_=cur
        # delta^2 >= 1/(2*n^2)
        assert sign(2*n*n*A-1,2*n*n*B)>=0
    return best,pop

def witness(n):
    # (1+i)*(sqrt(2)-1)^j: k=(a,2b,a,0)
    a,b=1,0;j=0
    while True:
        c,d=2*b-a,a-b
        if abs(c)+abs(d)>n: break
        a,b=c,d;j+=1
    return j,(a,2*b,a,0)

def run():
    N=18
    best,pop=exact_minima(N)
    print('exact even nonzero difference vectors:',pop,'sizes:',N)
    print('n min_squared_A min_squared_B witness_k min_distance n_times_distance')
    for n in range(1,N+1):
        A,B,k=best[n]
        j,w=witness(n); C,D=sq(w)
        assert sum(map(abs,w))<=2*n and sum(w)%2==0
        assert sign(C-A,D-B)>=0
        # upper bound squared: 2*(1+sqrt(2))^2/n^2 = (6+4sqrt(2))/n^2
        assert sign(6-n*n*C,4-n*n*D)>0
        delta=sqrt((A*A-2*B*B)/(A-B*sqrt(2)))
        print(n,A,B,k,format(delta,'.10f'),format(n*delta,'.10f'))
    for n in range(1,1001):
        j,w=witness(n); C,D=sq(w)
        assert sum(map(abs,w))<=2*n and sum(w)%2==0
        assert sign(6-n*n*C,4-n*n*D)>0
    print('constructive upper-bound checks:',1000)
if __name__=='__main__':run()
