from fractions import Fraction as F
from math import sqrt
# frequencies from Cekus et al Table 5 (frequency analyzer and Wavanal)
data={'CuSn20 analyzer':(538,1306,2193),'CuAl analyzer':(510,1285,2165),'CuSn20 Wavanal':(538,1307,2194),'CuAl Wavanal':(514,F('1281.5'),2155)}
# fit f^2=A*x+B*x^2 on modes 2,4; mode 3 not used in fitting
for name,vals in data.items():
 y,z,w=map(F,vals)
 print(name,'ratios nominal/hum',float(w/y))
 for label,x in [('unshifted',(4,9,16)),('shifted',(3,8,15))]:
  p,q,r=map(F,x)
  B=(w*w/r-y*y/p)/(r-p); A=y*y/p-B*p
  pred=sqrt(float(A*q+B*q*q))
  print(label,'A,B',float(A),float(B),'pred',pred,'observed',float(z),'err%',100*(pred/float(z)-1))
 # one-parameter baseline calibrated only on nominal
 print('n^2 baseline',float(w)*9/16,'error%',100*(float(w)*9/16/float(z)-1))
 print('same geometry scale ratio comparison follows')
# synthetic exact verification for positive integer coefficients; no sample data chosen by output
count=0
for A in range(0,21):
 for B in range(0,21):
  if A==B==0:continue
  for p,q,r in [(4,9,16),(3,8,15),(1,4,9),(9,16,25)]:
   yp=A*p+B*p*p;yr=A*r+B*r*r
   bh=(F(yr,r)-F(yp,p))/(r-p); ah=F(yp,p)-bh*p
   assert (ah,bh)==(A,B)
   assert ah*q+bh*q*q==A*q+B*q*q
   assert F(r,p)<=F(yr,yp)<=F(r*r,p*p)
   count+=1
print('synthetic exact cases',count)
s=sqrt((110/7530)/(117/8640))
print('elastic scale Al/Sn',s,'measured analyzer ratios', [b/a for a,b in zip((538,1144,1306,1643,2193),(510,1142,1285,1541,2165))])
# Amplitude-only degeneracy: integer triple spectrum mass and squared radius.
from collections import defaultdict
from itertools import combinations_with_replacement
classes=defaultdict(list)
for a,b,c in combinations_with_replacement(range(21),3):
 classes[(a+b+c,a*a+b*b+c*c-a*b-b*c-c*a)].append((a,b,c))
amb=[v for v in classes.values() if len(v)>1]
print('triples',sum(map(len,classes.values())),'classes',len(classes),'ambiguous classes',len(amb),'members',sum(map(len,amb)))
print('example key (9,21)',classes[(9,21)])
print('369 key (18,27)',classes[(18,27)])
# for real cyclic convolution lambda = (2a-b-c)/2 + i*sqrt(3)*(b-c)/2
# use exact integers U=2 Re lambda, V=2 Im lambda/sqrt(3), S=total
count=0
for a in range(21):
 for b in range(21):
  for c in range(21):
   S=a+b+c; U=2*a-b-c; V=b-c
   assert (F(S+U,3),F(2*S-U+3*V,6),F(2*S-U-3*V,6))==(a,b,c)
   count+=1
print('complex spectral reconstruction exact',count)
