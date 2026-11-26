from math import comb, cos, pi, gcd
from decimal import Decimal, getcontext
getcontext().prec=60
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def S(n,m,r): return sum(C(n,k) for k in range(n+1) if k%m==r)
def W(n,m,r): return m*S(n,m,r)-2**n
def phi(n): return sum(1 for k in range(1,n+1) if gcd(k,n)==1)

def roots(m):
    """non-principal, non-zero roots (-1)^j (2cos(pi j/m))^m, grouped by d = m/gcd(j,m)"""
    g={}
    for j in range(1,m):
        d=m//gcd(j,m)
        if d<=2: continue
        v=((-1)**j)*(2*cos(pi*j/m))**m
        g.setdefault(d,[]).append(v)
    # dedupe the j <-> m-j pairing
    out={}
    for d,vs in g.items():
        seen=[]
        for v in vs:
            if not any(abs(v-s)<1e-6*max(1,abs(v)) for s in seen): seen.append(v)
        out[d]=seen
    return out

def poly_from(rs):
    p=[1.0]
    for r in rs:
        p=[0.0]+p
        q=[c*(-r) for c in ([x for x in p[1:]]+[0.0])]
        p=[a+b for a,b in zip(p,q)]
    return p
def monic_int(rs):
    p=[1.0]
    for r in rs:
        np_=[0.0]*(len(p)+1)
        for i,c in enumerate(p):
            np_[i]+=c*(-r); np_[i+1]+=c
        p=np_
    return [round(c) for c in p]        # ascending powers
def pstr(p):
    t=[]
    for i in range(len(p)-1,-1,-1):
        c=p[i]
        if c==0: continue
        s=("" if c==1 and i>0 else ("-" if c==-1 and i>0 else f"{c}"))
        t.append(s+("" if i==0 else ("x" if i==1 else f"x^{i}")))
    return (" + ".join(t)).replace("+ -","- ") or "0"

print("Cases neither of us had computed, built from the root structure and then")
print("VERIFIED against exact Pascal integers.")
print()
HIS={10:"(x^2 - 123x + 1)(x^2 + 625x + 3125)",
     12:"(x - 1)(x + 64)(x - 729)(x^2 + 2702x + 1)",
     15:"(his: 15 not tabulated, predicted by the law)"}
for m in (10,12,15):
    g=roots(m)
    print(f"  m={m}:  divisors d>2 -> {sorted(g)}")
    full=[1]
    for d in sorted(g):
        f=monic_int(g[d])
        exp=phi(d)//2
        full_=[0]*(len(full)+len(f)-1)
        for i,a in enumerate(full):
            for j,b in enumerate(f): full_[i+j]+=a*b
        full=full_
        print(f"     d={d:>3}  deg {len(f)-1} (phi(d)/2 = {exp})   F = {pstr(f)}")
    print(f"     Q_{m} = {pstr(full)}")
    if m in HIS and not HIS[m].startswith("(his:"): print(f"     his : {HIS[m]}")
    # verify the recurrence on exact Pascal integers
    deg=len(full)-1
    bad=[n for n in range(0,30*m) for r in range(m)
         if sum(full[i]*W(n+i*m,m,r) for i in range(deg+1))!=0]
    print(f"     verified on exact Pascal integers, {30*m*m} cases: "
          f"{'HOLDS' if not bad else str(bad[:3])+' FAILS'}")
    print()

print("AND THE POINT HE MAKES ABOUT NESTING, CHECKED:")
print("  He says the 3-cycle appears INSIDE Q_9 'as a complete factor'. True:")
print("  d=3 inside m=9 gives root (-1)^3 (2cos(pi/3))^9 = -1, and Q_3's root is")
print("  (-1)^1 (2cos(pi/3))^3 = -1. Same root, same factor (x+1).")
print("  BUT that is special to 2cos(pi/3) = 1, where every power is 1.")
print("  For d=5 inside m=10 the root is (2cos(pi/5))^10 = phi^10, while Q_5's")
print("  d=5 root is -(2cos(pi/5))^5 = -phi^5. DIFFERENT roots, so Q_5 does NOT")
print("  appear inside Q_10 - only the same Galois orbit does, raised differently.")
print("  He says this himself ('after transforming their eigenvalues'), and the")
print("  distinction is worth keeping sharp: the DIVISOR structure is inherited,")
print("  the POLYNOMIALS are not.")
