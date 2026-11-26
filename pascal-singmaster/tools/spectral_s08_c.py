from math import comb, cos, pi, gcd
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def S(n,m,r): return sum(C(n,k) for k in range(n+1) if k%m==r)
def W(n,m,r): return m*S(n,m,r)-2**n
def monic_int(rs):
    p=[1.0]
    for r in rs:
        np_=[0.0]*(len(p)+1)
        for i,c in enumerate(p): np_[i]+=c*(-r); np_[i+1]+=c
        p=np_
    return [round(c) for c in p]
def Q(m):
    g={}
    for j in range(1,m):
        d=m//gcd(j,m)
        if d<=2: continue
        v=((-1)**j)*(2*cos(pi*j/m))**m
        g.setdefault(d,[]).append(v)
    allr=[]
    for d,vs in g.items():
        seen=[]
        for v in vs:
            if not any(abs(v-s)<1e-6*max(1,abs(v)) for s in seen): seen.append(v)
        allr+=seen
    return monic_int(allr)

print("Is the m=10 / m=12 failure HIS error or the even-m transient?")
print(f"{'m':>3} {'deg':>4} {'failures n=0..':>16} {'at n=0':>8} {'at n>=1':>9}  verdict")
print("-"*72)
for m in (6,8,10,12,14,15,9,7):
    p=Q(m); deg=len(p)-1
    bad=[(n,r) for n in range(0,25*m) for r in range(m)
         if sum(p[i]*W(n+i*m,m,r) for i in range(deg+1))!=0]
    z=[x for x in bad if x[0]==0]; nz=[x for x in bad if x[0]>=1]
    v=("clean" if not bad else
       "transient at n=0 only" if not nz else "REAL FAILURE")
    print(f"{m:>3} {deg:>4} {len(bad):>16} {len(z):>8} {len(nz):>9}  {v}")
print()
print("So: his factorisations are RIGHT. The failures are exactly the even-m")
print("transient from the zero eigenvalue (d=2), which his product deliberately")
print("excludes - and which only bites at row 0. Multiply by the missing x and")
print("it holds from n=0:")
for m in (10,12):
    p=[0]+Q(m); deg=len(p)-1
    bad=[(n,r) for n in range(0,25*m) for r in range(m)
         if sum(p[i]*W(n+i*m,m,r) for i in range(deg+1))!=0]
    print(f"   m={m}: x*Q_{m} verified over {25*m*m} cases -> "
          f"{'HOLDS' if not bad else bad[:3]}")
print()
print("I nearly reported his m=10 and m=12 as failing. Same shape as the")
print("mistake I nearly made on her matrix an hour ago: the data looked wrong,")
print("and the cause was my framing, not their result.")
