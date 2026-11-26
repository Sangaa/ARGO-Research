from math import comb,cos,sin,pi,sqrt,prod
from cmath import exp
from collections import defaultdict
import numpy as np
# Integer measured frequency entries, not independent: two alloys and three nominal observations.
bronze=[538,1144,1306,1643,2193]
albronze=[510,1142,1285,1541,2165]
nominal=[1645,952,832]
values=bronze+albronze+nominal
# Full non-edge membership up to 10000; C(n,k)>=C(n,2) for 2<=k<=n/2.
lookup=defaultdict(list)
for n in range(4,143):
 for k in range(2,n//2+1):
  c=comb(n,k)
  if c>10000:break
  lookup[c].append((n,k))
for x in [3,6,7,8,9,13,19,26,29,54,56,57,58,63,64,65,133,1729]+values:
 print('pascal',x,lookup[x])
print('measured exact',sum(bool(lookup[x]) for x in values),len(values))
for tol in [1,5,10]:
 hit=lambda x:any(lookup[y] for y in range(x-tol,x+tol+1))
 print('tolerance',tol,'data',sum(hit(x) for x in values),'of',len(values),'baseline integer 500..2200',sum(hit(x) for x in range(500,2201)),'of',1701)
# Compare similarity scaling using independent published diameter & nominal values.
d=np.array([.2,.64,.89,.99]); f=np.array([6054.5,1645,952,832]); print('D*f',d*f)
for p in [1,2]:
 errs=[]
 for i in range(4):
  mask=np.arange(4)!=i
  C=np.exp(np.mean(np.log(f[mask]*d[mask]**p)))
  errs.append(100*(C/d[i]**p/f[i]-1))
 print('LOO fixed power',p,'errors percent',np.round(errs,2),'MAPE',np.mean(np.abs(errs)))
# Three equally spaced pickups, exact analytic gains compare complex direct sums.
weights={'equal':(1,1,1),'pascal2':(1,2,1),'123':(1,2,3),'369':(3,6,9),'signed':(1,-2,1)}
count=0
for name,w in weights.items():
 scale=sum(map(abs,w)); expected={'equal':(1,0),'pascal2':(1,.25),'123':(1,1/(2*sqrt(3))),'369':(1,1/(2*sqrt(3))),'signed':(0,.75)}[name]
 for j in range(65):
  H=sum(w[k]*exp(2j*pi*j*k/3) for k in range(3))/scale
  assert abs(abs(H)-expected[j%3!=0])<1e-12
  count+=1
 print('gain',name,expected)
print('three sensors checks',count)
# Exact discrete biharmonic: fourth signed Pascal row; periodic Laplacian square independent direct operations.
count=0
for m in range(3,67):
 for seed in [0,1,2]:
  u=[(r*r+7*r+seed*r**3)%23-11 for r in range(m)]
  lap=lambda v:[v[(i-1)%m]-2*v[i]+v[(i+1)%m] for i in range(m)]
  a=lap(lap(u)); b=[sum((-1)**k*comb(4,k)*u[(i+k-2)%m] for k in range(5)) for i in range(m)]
  assert a==b;count+=m
print('exact biharmonic component checks',count)
# Ring model negative control: normalized to measured nominal, compare two RIR modes, no fitting besides scale.
for name,obs in [('CuSn20',[538,1306,2193]),('CuAl',[510,1285,2165]),('Mafra',[1489.2,3593.9,6054.5])]:
 for model,g in [('n^2',lambda n:n*n),('thin ring',lambda n:n*(n*n-1)/sqrt(n*n+1))]:
  pred=[obs[-1]*g(n)/g(4) for n in [2,3,4]]
  print('ring control',name,model,'pred',np.round(pred,2),'error%',np.round(100*(np.array(pred)/obs-1),2))
