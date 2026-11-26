from math import comb
from fractions import Fraction as F
import numpy as np, itertools
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def kraw(j,x,n): return sum((-1)**s*C(x,s)*C(n-x,j-s) for s in range(j+1))

print("="*76)
print("FIX 2. Her claim: Krawtchouk IS Fourier, on (Z/2Z)^n. Built and checked.")
print("="*76)
for n in (3,4,5,6):
    N=2**n
    H=np.empty((N,N))
    for a in range(N):
        for b in range(N):
            H[a,b]=(-1)**bin(a&b).count('1')
    H/= N**0.5
    print(f"  n={n}: Walsh-Hadamard H on (Z/2Z)^{n}:  H^2 = I ? "
          f"{np.allclose(H@H,np.eye(N),atol=1e-10)}   "
          f"eigenvalues {sorted(set(np.round(np.linalg.eigvals(H).real,6)))}")
print("  -> THE FOURIER TRANSFORM OF (Z/2Z)^n IS ITSELF AN INVOLUTION.")
print("     Every element of the group is its own inverse, so F = F^-1 and the")
print("     spectrum is {+1,-1}. The 4th roots {1,i,-1,-i} belong to Fourier on")
print("     Z/N or on R, NOT on the binary cube.")
print()
print("  So my P2 compared Krawtchouk against the WRONG Fourier transform and")
print("  'refuted' a claim that was never the right one. She is correct.")
print()
print("  Now the actual claim: restrict H to RADIAL functions (depending only on")
print("  Hamming weight) and the matrix should BE the Krawtchouk transform.")
for n in (3,4,5,6,7):
    N=2**n
    H=np.empty((N,N))
    for a in range(N):
        for b in range(N):
            H[a,b]=(-1)**bin(a&b).count('1')
    H/= N**0.5
    # radial projector: average over each Hamming-weight shell
    wt=[bin(a).count('1') for a in range(N)]
    R=np.zeros((n+1,N))
    for a in range(N): R[wt[a],a]=1.0
    shell=np.array([C(n,w) for w in range(n+1)],dtype=float)
    Rn = R/shell[:,None]                      # average over shell
    Hrad = Rn @ H @ R.T                       # H restricted to radial functions
    # the Krawtchouk transform in the SAME (unnormalised, shell-averaged) convention
    Kt = np.array([[kraw(j,x,n)/ (N**0.5) for x in range(n+1)] for j in range(n+1)])
    # compare: Hrad[w, x] should be K_w(x)/sqrt(N) * C(n,x)/C(n,w) ... check directly
    pred = np.array([[kraw(w,x,n)*C(n,x)/(C(n,w)*N**0.5) for x in range(n+1)]
                     for w in range(n+1)])
    print(f"  n={n}: H restricted to radial functions == Krawtchouk kernel? "
          f"{np.allclose(Hrad,pred,atol=1e-9)}")
print("  -> CONFIRMED. Krawtchouk IS the Fourier transform of the binary cube,")
print("     seen on the radial (Hamming-weight) subspace. Not an analogue of it.")

print()
print("="*76)
print("FIX 3. Her peeling formula, checked exactly")
print("="*76)
print("  claim: q = n-2k is invariant under (n,k) -> (n+2r, k+r), and")
print("         u_{n+2r}(q) = sum_{j=-r}^{r} C(2r,r+j)/4^r * u_n(q-2j)")
def u(nn,xx):
    if (xx+nn)%2: return F(0)
    kk=(xx+nn)//2
    return F(C(nn,kk),2**nn) if 0<=kk<=nn else F(0)
inv_ok=all((n+2*r)-2*(k+r)==n-2*k for n in range(50) for k in range(n+1) for r in range(5))
print(f"  invariance of q: {inv_ok}")
bad=[]
for n in range(0,40):
    for r in range(0,6):
        for q in range(-(n+2*r), n+2*r+1):
            lhs=u(n+2*r,q)
            rhs=sum(F(C(2*r,r+j),4**r)*u(n,q-2*j) for j in range(-r,r+1))
            if lhs!=rhs: bad.append((n,r,q))
print(f"  convolution identity, n=0..39, r=0..5, every q, exact rationals: "
      f"{'HOLDS, 0 exceptions' if not bad else bad[:4]}")
print("  -> HER FORMULA IS CORRECT. Peeling = advancing diffusion time by 2r at")
print("     fixed spatial coordinate. That is a genuinely better reading of the")
print("     owner's peeling idea than anything I had.")
