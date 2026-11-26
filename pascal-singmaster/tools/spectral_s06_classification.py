from math import comb
from fractions import Fraction as F
def S(n,m,r): return sum(comb(n,k) for k in range(n+1) if k%m==r)
def W(n,m,r): return m*S(n,m,r)-2**n

def solve(A,b):
    n=len(A); M=[A[i][:]+[b[i]] for i in range(n)]
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=0), None)
        if p is None: return None
        M[c],M[p]=M[p],M[c]; pv=M[c][c]; M[c]=[x/pv for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[x-f*y for x,y in zip(M[r],M[c])]
    return [M[i][n] for i in range(n)]

def fit(m,deg,off=1):
    A=[[F(W(n+(deg-i)*m,m,0)) for i in range(1,deg+1)] for n in range(off,off+deg)]
    b=[F(W(n+deg*m,m,0)) for n in range(off,off+deg)]
    sol=solve(A,b)
    if sol is None: return None
    ok=all(W(n+deg*m,m,r)==sum(sol[i-1]*W(n+(deg-i)*m,m,r) for i in range(1,deg+1))
           for n in range(0,20*m) for r in range(m))
    return sol if ok else None

print("Exact integer recurrences for W(n) = m*S_r(n) - 2^n, sampled every m rows.")
print("Coefficients solved exactly from a few rows, then re-verified on EVERY")
print("residue class and every n in range.")
print()
print(f"{'m':>3} {'deg':>4}  recurrence                                            cases  integer?")
print("-"*92)
for m in range(2,10):
    hit=False
    for deg in range(1, m//2+2):
        for off in (0,1,2,3):
            sol=fit(m,deg,off)
            if sol is not None:
                terms=" ".join(f"{'+' if c>=0 else '-'} {abs(c)}*W(n+{(deg-i-1)*m})"
                               for i,c in enumerate(sol))
                allint=all(c.denominator==1 for c in sol)
                nchk=20*m*m
                print(f"{m:>3} {deg:>4}  W(n+{deg*m}) = {terms:<42} {nchk:>6}  "
                      f"{'yes' if allint else 'NO'}")
                hit=True; break
        if hit: break
    if not hit: print(f"{m:>3}    -   none found up to degree {m//2+1}")
print()
print("Reading it:")
print("  m=2: W identically 0 - Pascal's row splits exactly in half, no content.")
print("  m=3: W(n+3) = -W(n), so PERIOD 6. That is her '6-step cycle for the")
print("       centred Pascal part', derived instead of observed.")
print("  m=5: W(n+10) = -11 W(n+5) + W(n) - her R33 exactly, and 11 = L_5 because")
print("       the two roots are -phi^5 and phi^-5.")
print()
print("  Integrality is forced, not lucky: the roots (-1)^j (2cos(pi j/m))^m are")
print("  a full set of algebraic conjugates, so the symmetric functions are")
print("  rational integers. That is the general answer to her question.")
