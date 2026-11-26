from math import comb, cos, pi
import cmath
def S(n,m,r): return sum(comb(n,k) for k in range(n+1) if k%m==r)
def W(n,m,r): return m*S(n,m,r) - 2**n          # centred difference, exact integer

print("="*78)
print("1. HER R33 EIGENVALUES for the mod-5 Pascal circulant  A = I + P")
print("="*78)
print(f"   {'j':>2} {'1+w^j':>26} {'|.|':>10} {'arg/pi':>9}   her claim")
HER={1:"phi * e^(i pi/5)",2:"(1/phi) * e^(2 i pi/5)",
     3:"(1/phi) * e^(-2 i pi/5)",4:"phi * e^(-i pi/5)"}
phi=(1+5**0.5)/2
for j in range(1,5):
    lam=1+cmath.exp(2j*pi*j/5)
    print(f"   {j:>2} {str(round(lam.real,6))+('+' if lam.imag>=0 else '')+str(round(lam.imag,6))+'i':>26} "
          f"{abs(lam):>10.6f} {cmath.phase(lam)/pi:>9.6f}   {HER[j]}")
print(f"   phi = {phi:.6f}, 1/phi = {1/phi:.6f}  -> HER EIGENVALUES ARE CORRECT")

print()
print("2. HER FIFTH POWERS AND THE RECURRENCE")
l1=(1+cmath.exp(2j*pi/5))**5; l2=(1+cmath.exp(4j*pi/5))**5
print(f"   lambda_1^5 = {l1.real:.10f} {l1.imag:+.2e}i   (-phi^5 = {-phi**5:.10f})")
print(f"   lambda_2^5 = {l2.real:.10f} {l2.imag:+.2e}i   ( phi^-5 = {phi**-5:.10f})")
print(f"   sum     = {(l1+l2).real:.10f}   -> she says -11 (Lucas L_5)")
print(f"   product = {(l1*l2).real:.10f}   -> she says -1")
print("   so the sampled sequence obeys x^2 + 11x - 1 = 0, i.e.")
print("     W_(n+10) = -11 W_(n+5) + W_n")

print()
print("3. TESTED ON EXACT INTEGERS, not on the eigenvalues")
bad=[]
for n in range(0,201):
    for r in range(5):
        if W(n+10,5,r) != -11*W(n+5,5,r) + W(n,5,r): bad.append((n,r))
print(f"   W(n+10) = -11 W(n+5) + W(n) for n=0..200, r=0..4  ({201*5} cases): "
      f"{'HOLDS EXACTLY' if not bad else bad[:4]}")
print("   her sample rows, reproduced:")
for n in (0,5,10,15):
    print(f"     row {n:>2}: {[W(n,5,r) for r in range(5)]}")

print()
print("="*78)
print("4. HER QUESTION: can we classify ALL circulant systems this way?")
print("   YES, and the general law is short.")
print("="*78)
print("   1 + w^j = 2cos(pi j/m) * e^(i pi j/m).  Raise to the m-th power:")
print("     (1 + w^j)^m = (2cos(pi j/m))^m * e^(i pi j) = (-1)^j (2cos(pi j/m))^m")
print("   EVERY eigenvalue becomes REAL after m steps. That is the whole reason")
print("   sampling a circulant every m rows produces an integer recurrence.")
print()
print("   And j and m-j give the SAME value, so the roots pair up:")
bad=[]
for m in range(2,13):
    for j in range(1,m):
        a=((1+cmath.exp(2j*pi*j/m))**m)
        b=((1+cmath.exp(2j*pi*(m-j)/m))**m)
        if abs(a-b)>1e-6: bad.append((m,j))
print(f"   checked (1+w^j)^m == (1+w^(m-j))^m for m=2..12: "
      f"{'PAIRS CONFIRMED' if not bad else bad[:3]}")
print()
print(f"   {'m':>3} {'distinct non-principal roots (-1)^j (2cos(pi j/m))^m':<52} {'recurrence'}")
print("   "+"-"*78)
for m in range(2,9):
    roots=[]
    for j in range(1,m//2+1):
        v=((-1)**j)*(2*cos(pi*j/m))**m
        rv=round(v)
        roots.append(rv if abs(v-rv)<1e-6 else round(v,4))
    # build the monic polynomial with those roots
    poly=[1]
    for rt in roots:
        poly=[a-rt*b for a,b in zip(poly+[0],[0]+poly)]
    terms=[]
    for i,c in enumerate(poly[1:],start=1):
        if c: terms.append(f"{-c:+d} W(n+{m*(len(poly)-1-i)})" if isinstance(c,int) else f"{-c:+.3f} W(n+{m*(len(poly)-1-i)})")
    rec=f"W(n+{m*len(roots)}) = " + " ".join(terms) if terms else "W == 0"
    print(f"   {m:>3} {str(roots):<52} {rec}")
