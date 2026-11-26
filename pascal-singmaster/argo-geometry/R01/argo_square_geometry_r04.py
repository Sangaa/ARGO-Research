from fractions import Fraction as F
from math import comb
from itertools import product

def step(v,w):
 a,b,c,d=w; out={}
 for (i,j),u in v.items():
  for (di,dj),t in zip(((0,0),(1,0),(0,1),(1,1)),w):
   q=(i+di,j+dj);out[q]=out.get(q,0)+u*t
 return out

def check(v,w,n):
 a,b,c,d=w; S=sum(w); X=b+d;Y=c+d
 mass=S**n
 assert sum(v.values())==mass
 for i in range(n+1):
  assert sum(v.get((i,j),0) for j in range(n+1))==comb(n,i)*X**i*(S-X)**(n-i)
  assert sum(v.get((j,i),0) for j in range(n+1))==comb(n,i)*Y**i*(S-Y)**(n-i)
 ex=F(n*X,S); ey=F(n*Y,S)
 cov=F(sum(i*j*z for (i,j),z in v.items()),mass)-ex*ey
 assert cov==F(n*(a*d-b*c),S*S)
 assert F(sum((i+j)**2*z for (i,j),z in v.items()),mass)-(ex+ey)**2==F(n*(X*(S-X)+Y*(S-Y)+2*(a*d-b*c)),S*S)
 if n:
  D=cov/n
  assert F(X*Y,S*S)+D==F(d,S)
 return cov

cases=rows=0
for w in product(range(4),repeat=4):
 if not sum(w):continue
 v={(0,0):1}
 for n in range(1,11):
  v=step(v,w);check(v,w,n);cases+=1;rows+=2*(n+1)
print('general exact moment/inversion cases',cases,'marginal entries',rows)
for w in [(1,3,3,1),(2,2,2,2),(3,1,1,3),(3,6,9,12),(3,6,9,18)]:
 v={(0,0):1}
 for n in range(1,21):v=step(v,w);check(v,w,n)
 a,b,c,d=w;S=sum(w)
 print('w',w,'det',a*d-b*c,'cov/step',F(a*d-b*c,S*S),'diag variance/step',F((b+d)*(a+c)+(c+d)*(a+b)+2*(a*d-b*c),S*S))
 if w in [(1,3,3,1),(2,2,2,2),(3,1,1,3)]:
  print('n=20 P(X=Y)',float(F(sum(v.get((i,i),0) for i in range(21)),S**20)))
# independent expansion along y, binomial product of (a+b x)^(n-j)(c+d x)^j
checks=0
for w in [(1,3,3,1),(2,2,2,2),(3,1,1,3),(3,6,9,12),(3,6,9,18)]:
 a,b,c,d=w;v={(0,0):1}
 for n in range(21):
  for i,j in product(range(n+1),repeat=2):
   z=comb(n,j)*sum(comb(n-j,i-l)*comb(j,l)*a**(n-j-i+l)*b**(i-l)*c**(j-l)*d**l for l in range(max(0,i-(n-j)),min(i,j)+1))
   assert v.get((i,j),0)==z;checks+=1
  v=step(v,w)
print('independent coefficient comparisons',checks)
