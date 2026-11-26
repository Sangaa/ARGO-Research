from math import comb, cos, pi
from fractions import Fraction as F
def C(a,b): return comb(a,b) if 0<=b<=a else 0

print("="*76)
print("HER OBJECTION 1: inv_2cos returned C(n,k)/C(n,k). A tautology, not a")
print("measurement. Executed inside the loop, but the loop re-derived the number.")
print("="*76)
print("  The other two were genuinely independent and I should say so:")
print("    inv_hex  computes TWO different products and divides -> 1 is the content")
print("    inv_heat computes u(n,x) and the average of two OTHER binomials -> 0 is")
print("  Only inv_2cos was circular. Fixing it by computing the spectral coefficient")
print("  from the WAVE SIDE, by numerical integration, never touching C(n,k):")
print()
def coeff_by_integration(n,k,M=20000):
    # (1/2pi) * integral (2cos t)^n e^{-i(n-2k)t} dt  -- real by symmetry
    m=n-2*k; s=0.0
    for j in range(M):
        t=2*pi*j/M
        s+=(2*cos(t))**n * cos(m*t)
    return s/M
print(f"  {'n':>3} {'k':>3} {'integral of (2cos t)^n e^-i(n-2k)t':>36} {'C(n,k)':>10} {'ratio':>12}")
print("  "+"-"*68)
worst=0.0
for n,k in ((4,1),(6,2),(8,3),(10,5),(12,4)):
    v=coeff_by_integration(n,k); c=C(n,k)
    worst=max(worst,abs(v/c-1))
    print(f"  {n:>3} {k:>3} {v:>36.6f} {c:>10} {v/c:>12.9f}")
print(f"  worst deviation of ratio from 1: {worst:.2e}")
print("  -> NOW the 1 is a measurement: the spectral side was computed by")
print("     integration and the combinatorial side by comb(), independently.")
print("     The invariant is still constant, so exclusion power is still 0 --")
print("     but that zero is now earned instead of defined.")

print()
print("="*76)
print("HER OBJECTION 2: is_binomial_row ignores WHERE the coefficients sit.")
print("="*76)
def nstep(st,n):
    poly={0:F(1)}
    for _ in range(n):
        new={}
        for d,c in poly.items():
            for e,a in st.items(): new[d+e]=new.get(d+e,F(0))+c*a
        poly={k:v for k,v in new.items() if v}
    return poly
def pascal_values(co):
    ks=sorted(co); v=[co[k] for k in ks]; m=len(v)-1
    if m<1: return True
    return all(v[i]==v[0]*C(m,i) for i in range(m+1))
def evenly_spaced(co):
    ks=sorted(co)
    if len(ks)<3: return True
    d=ks[1]-ks[0]
    return all(ks[i+1]-ks[i]==d for i in range(len(ks)-1))

TESTS={ "(1+z)/2":{0:F(1,2),1:F(1,2)},
        "(1+z^3)/2  spaced":{0:F(1,2),3:F(1,2)},
        "(1+z)^2/4":{-1:F(1,4),0:F(1,2),1:F(1,4)},
        "(1+z)(1+z^5)/4  two spacings":{0:F(1,4),1:F(1,4),5:F(1,4),6:F(1,4)},
        "(1+z+z^2)/3":{0:F(1,3),1:F(1,3),2:F(1,3)} }
print(f"  {'symbol':<32} {'values Pascal?':>15} {'evenly spaced?':>15}")
print("  "+"-"*64)
for name,st in TESTS.items():
    vals=all(pascal_values(nstep(st,n)) for n in range(2,8))
    even=all(evenly_spaced(nstep(st,n)) for n in range(2,8))
    print(f"  {name:<32} {str(vals):>15} {str(even):>15}")
print()
print("  -> she is right that the two are different questions, and the search")
print("     below asks the sharper one: can the VALUES be a Pascal row while the")
print("     POSITIONS are irregular? If yes, my characterisation is incomplete.")
import itertools
found=[]
for support in itertools.combinations(range(0,7), 3):
    for num in itertools.product(range(1,5), repeat=3):
        st={d:F(a,sum(num)) for d,a in zip(support,num)}
        if all(pascal_values(nstep(st,n)) for n in range(2,7)):
            if not all(evenly_spaced(nstep(st,n)) for n in range(2,7)):
                found.append((support,num))
print(f"  searched all 3-point supports in [0,6] x weights in [1,4]^3: "
      f"{len(found)} cases with Pascal VALUES but irregular POSITIONS")
print(f"  -> {'NONE FOUND; values and even spacing coincided in this search space' if not found else found[:3]}")
print("     Not a proof. Stated as the bounded search it is.")
