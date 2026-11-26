from math import comb, factorial
from fractions import Fraction as F
from collections import defaultdict
# Pascal nested choice vs independent polynomial propagation on count lattice.
weights=[(1,1,1),(1,2,3),(3,6,9),(1,0,2),(0,4,5),(1,2,6)]
count=projection=rotation=0
for w in weights:
    state={(0,0,0):1}; cyc=[1,0,0]
    for n in range(41):
        v=[0,0,0]; mass=0
        for a in range(n+1):
            for b in range(n-a+1):
                c=n-a-b
                M=comb(n,a)*comb(n-a,b)
                assert M==factorial(n)//(factorial(a)*factorial(b)*factorial(c))
                u=M*w[0]**a*w[1]**b*w[2]**c
                assert state.get((a,b,c),0)==u
                v[(b+2*c)%3]+=u; mass+=u; count+=1
                if w==(1,1,1):
                    assert state[(b,c,a)]==u and state[(c,a,b)]==u
                    rotation+=1
        assert mass==sum(w)**n
        assert v==cyc; projection+=3
        nxt=defaultdict(int)
        for abc,val in state.items():
            for i,wi in enumerate(w):
                if wi:
                    p=list(abc);p[i]+=1;nxt[tuple(p)]+=val*wi
        state=nxt
        cyc=[sum(w[j]*cyc[(r-j)%3] for j in range(3)) for r in range(3)]
# exact rational covariance in coordinates (x, y/sqrt(3)).
# complex plane vertices (1,0),(-1/2,sqrt(3)/2),(-1/2,-sqrt(3)/2)
pts=[(F(1),F(0)),(F(-1,2),F(1,2)),(F(-1,2),F(-1,2))]
cc=0
for a in range(11):
 for b in range(11):
  for c in range(11):
   S=a+b+c
   if not S:continue
   p=[F(i,S) for i in (a,b,c)]
   x=sum(pi*v[0] for pi,v in zip(p,pts)); y=sum(pi*v[1] for pi,v in zip(p,pts))
   xx=sum(pi*(v[0]-x)**2 for pi,v in zip(p,pts)); yy=3*sum(pi*(v[1]-y)**2 for pi,v in zip(p,pts)); xy0=sum(pi*(v[0]-x)*(v[1]-y) for pi,v in zip(p,pts))
   D=a*a+b*b+c*c-a*b-b*c-c*a
   assert x*x+3*y*y==F(D,S*S)
   assert xx+yy==1-F(D,S*S)
   assert xx*yy-3*xy0*xy0==F(27,4)*p[0]*p[1]*p[2]
   if (a,b,c) in [(1,1,1),(1,2,3),(3,6,9)]: print('cov', (a,b,c), 'mean',x,y,'trace',xx+yy,'det',xx*yy-3*xy0*xy0)
   cc+=1
print('lattice coefficients',count,'cyclic projection entries',projection,'rotation',rotation,'covariance cases',cc)
# Fixed-sum barycentric triangle rotation count, independent enumeration by orbit.
for n in range(101):
    points={(a,b,n-a-b) for a in range(n+1) for b in range(n-a+1)}
    orbits={min(v,(v[1],v[2],v[0]),(v[2],v[0],v[1])) for v in points if len(set(v))>1}
    assert len(orbits)==(comb(n+2,2)-int(n%3==0))//3
print('centered orbit counts 101/101')
