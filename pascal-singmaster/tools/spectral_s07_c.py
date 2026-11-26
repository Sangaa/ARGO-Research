from math import comb
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def S(n,r): return sum(C(n,k) for k in range(n+1) if k%5==r)

print("HER R35 CLAIM:  max_r S_r(n) - min_r S_r(n) = F_(n+1)  for mod 5, all n>=0")
F=[0,1]
for i in range(2,260): F.append(F[-1]+F[-2])
bad=[]
for n in range(0,201):
    sp=max(S(n,r) for r in range(5))-min(S(n,r) for r in range(5))
    if sp!=F[n+1]: bad.append((n,sp,F[n+1]))
print(f"  n = 0..200, exact integers: {'HOLDS, 0 exceptions' if not bad else bad[:4]}")
print(f"  her worked example, row 6: max={max(S(6,r) for r in range(5))}, "
      f"min={min(S(6,r) for r in range(5))}, diff="
      f"{max(S(6,r) for r in range(5))-min(S(6,r) for r in range(5))}, F_7={F[7]}")

print()
print("HER MATRIX:  (x',y') = [[1,1],[1,2]] (x,y)  after two Pascal steps,")
print("             and [[1,1],[1,2]] = [[0,1],[1,1]]^2")
import numpy as np
Fm=np.array([[0,1],[1,1]])
print(f"  [[0,1],[1,1]]^2 = {(Fm@Fm).tolist()}  -> equals [[1,1],[1,2]]? "
      f"{(Fm@Fm).tolist()==[[1,1],[1,2]]}")
# check the x,y recursion on real data at even rows
print(f"  {'n':>4} {'sorted S_r':<34} {'x=A-B':>7} {'y=B-C':>7} {'next (x,y) predicted':>22}")
ok=True
for n in range(4,16,2):
    v=sorted((S(n,r) for r in range(5)), reverse=True)
    A,B,C_,_,_=v
    x,y=A-B,B-C_
    v2=sorted((S(n+2,r) for r in range(5)), reverse=True)
    A2,B2,C2,_,_=v2
    x2,y2=A2-B2,B2-C2
    pred=(x+y, x+2*y)
    if (x2,y2)!=pred: ok=False
    print(f"  {n:>4} {str(v):<34} {x:>7} {y:>7} {str(pred):>22}  actual {(x2,y2)}")
print(f"  two-step map [[1,1],[1,2]] reproduces (x,y) at even rows: {ok}")

print()
print("HER CORRECTION TO MY S06 WORDING:")
print("  I wrote: 'every eigenvalue becomes real after m steps. That is the")
print("  ENTIRE REASON sampling gives an integer recurrence.'")
print("  She: real is not sufficient - you also need algebraic integrality and")
print("  stability of the polynomial under Galois conjugation.")
print("  SHE IS RIGHT, and the counterexample is easy: 2cos(pi/5) = phi is real")
print(f"  and (2cos(pi/5))^1 = {2*np.cos(np.pi/5):.6f} is NOT an integer. Real alone")
print("  buys nothing. What buys integrality is that the FULL SET of conjugates")
print("  appears, so the symmetric functions are Galois-invariant rationals, and")
print("  algebraic integers, hence rational integers.")
print("  My section 2 headline overstated; my own later sentence had it right.")
print("  The headline is the one a reader keeps.")
