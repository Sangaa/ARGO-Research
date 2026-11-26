from math import comb
from fractions import Fraction as F
import numpy as np
def C(a,b): return comb(a,b) if 0 <= b <= a else 0
def kraw(j,x,n): return sum((-1)**s * C(x,s) * C(n-x, j-s) for s in range(j+1))

print("P2.  Is the Krawtchouk transform a Fourier transform?")
print("     T[j,x] = K_j(x;n) sqrt(C(n,x)) / ( sqrt(C(n,j)) 2^(n/2) )")
for n in (4, 8, 12, 16, 24):
    K = np.array([[float(kraw(j,x,n)) for x in range(n+1)] for j in range(n+1)])
    cn = np.array([float(C(n,i)) for i in range(n+1)])
    T = K * np.sqrt(cn)[None,:] / (np.sqrt(cn)[:,None] * 2.0**(n/2))
    orth = np.allclose(T @ T.T, np.eye(n+1), atol=1e-8)
    invol = np.allclose(T @ T, np.eye(n+1), atol=1e-8)
    ev = np.round(np.linalg.eigvals(T).real, 6)
    print(f"  n={n:2d}: T T^T=I? {orth}   T^2=I? {invol}   "
          f"eigenvalues: {sorted(set(ev))}  multiplicities "
          f"{ {v:int((ev==v).sum()) for v in sorted(set(ev))} }")
print("  -> real orthogonal INVOLUTION. spectrum {+1,-1}, not {1,i,-1,-i}.")
print("     Pascal/Krawtchouk reproduces the Fourier transform's SQUARE (parity),")
print("     not F itself. The bridge is real and it is PARTIAL. Saying 'Pascal is")
print("     a Fourier transform' would be false; saying it carries F^2 is true.")

print()
print("P3.  Do Pascal's rows solve the discrete heat equation exactly?")
def u(nn,xx):
    if (xx+nn) % 2: return F(0)
    kk = (xx+nn)//2
    return F(C(nn,kk), 2**nn) if 0 <= kk <= nn else F(0)
bad=[]; N=80
for n in range(N):
    for x2 in range(-(n+1), n+2):
        if u(n+1,x2) != (u(n,x2-1)+u(n,x2+1))/2: bad.append((n,x2))
print(f"  u_(n+1)(x) = (u_n(x-1)+u_n(x+1))/2 over rows 0..{N}, every position,")
print(f"  exact rationals: {'HOLDS EXACTLY, 0 exceptions' if not bad else bad[:3]}")
print("  -> Pascal's triangle IS the discrete heat kernel on Z. Not an analogy.")

print()
print("P4.  THE DECIDING TEST: does any of this EXCLUDE a repetition?")
seen={}
for n in range(2,200):
    for k in range(1,n//2+1): seen.setdefault(C(n,k),[]).append((n,k))
rep={v:p for v,p in seen.items() if len(p)>1}
print(f"  repeated interior values, n<200: {len(rep)}")
for v,p in sorted(rep.items())[:5]: print(f"     {v:>8} at {p}")
cross=[v for v,p in rep.items() if len({n for n,_ in p})>1]
print(f"  of those, pairs living at DIFFERENT n (different diffusion times): "
      f"{len(cross)} / {len(rep)}")
print("  The heat kernel compares values at the SAME time, or the same x/n ray.")
print("  Every repetition sits at different times AND different positions, where")
print("  the kernel gives no comparison at all. EXCLUSION POWER = 0 - the same")
print("  verdict the hexagonal identities got, for the same structural reason:")
print("  a TRUE statement about every cell cannot rule out any cell.")
