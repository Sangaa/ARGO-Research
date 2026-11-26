from math import comb
from fractions import Fraction as F
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def nstep(st,n):
    poly={0:F(1)}
    for _ in range(n):
        new={}
        for d,c in poly.items():
            for e,a in st.items(): new[d+e]=new.get(d+e,F(0))+c*a
        poly={k:v for k,v in new.items() if v}
    return poly
def is_binomial_row(co):
    ks=sorted(co); v=[co[k] for k in ks]; m=len(v)-1
    if m<1: return True
    r=v[0]
    return all(v[i]==r*C(m,i) for i in range(m+1))

print("MY CLAIM WAS WRONG IN BOTH DIRECTIONS, and my own table showed it:")
print("  * 3-point (1/4,1/2,1/4) DID give exact Pascal -- because it is")
print("    (1+z)^2/4, a binomial symbol SQUARED. Three points, still Pascal.")
print("  * 2-point BIASED (1/3,2/3) did NOT -- the weights are C(n,k)p^k q^(n-k),")
print("    binomially DISTRIBUTED but not proportional to C(n,k).")
print("  'Two points in the stencil' was the wrong invariant. I counted points")
print("  when the condition is about the SYMBOL's factorisation.")
print()
print("CORRECTED CLAIM: the n-step kernel is proportional to a Pascal row for")
print("every n  <=>  f(z) = c * z^m * (1 + z^L)^s  for some c, m, L>=1, s>=1.")
print("  (the lattice spacing L is invisible once you list nonzero coefficients)")
print()
TESTS = {
 "(1+z)/2              -> s=1":        ({0:F(1,2),1:F(1,2)}, True),
 "(1+z)^2/4            -> s=2":        ({-1:F(1,4),0:F(1,2),1:F(1,4)}, True),
 "(1+z)^3/8            -> s=3":        ({0:F(1,8),1:F(3,8),2:F(3,8),3:F(1,8)}, True),
 "(1+z^3)/2            -> L=3":        ({0:F(1,2),3:F(1,2)}, True),
 "(1+z^2)^2/4          -> L=2,s=2":    ({0:F(1,4),2:F(1,2),4:F(1,4)}, True),
 "z^5(1+z)/2           -> shifted":    ({5:F(1,2),6:F(1,2)}, True),
 "7(1+z)/2             -> unnormalised":({0:F(7,2),1:F(7,2)}, True),
 "(1/3,2/3)  biased":                  ({0:F(1,3),1:F(2,3)}, False),
 "(1+z+z^2)/3":                        ({0:F(1,3),1:F(1,3),2:F(1,3)}, False),
 "(1+z)(1+2z)/6":                      ({0:F(1,6),1:F(3,6),2:F(2,6)}, False),
 "uniform 4-point":                    ({0:F(1,4),1:F(1,4),2:F(1,4),3:F(1,4)}, False),
 "(1+z)^2/4 + tiny 3rd point":         ({-1:F(1,4),0:F(1,2),1:F(24,100),2:F(1,100)}, False),
}
print(f"{'symbol':<38} {'predicted':>10} {'n=2..9 all Pascal?':>20}  verdict")
print("-"*82)
ok=True
for name,(st,pred) in TESTS.items():
    got=all(is_binomial_row(nstep(st,n)) for n in range(2,10))
    agree = (got==pred)
    ok &= agree
    print(f"{name:<38} {str(pred):>10} {str(got):>20}  {'ok' if agree else 'MISMATCH'}")
print()
print(f"corrected claim agrees with measurement on all {len(TESTS)} symbols: {ok}")
print()
print("WHY, in one line: f^n = c^n z^{mn} (1+z^L)^{sn}, and the binomial theorem")
print("gives coefficients C(sn, k) directly. Nothing else expands that way.")
print()
print("AND THE PHYSICAL READING IS BETTER THAN MY FIRST ONE:")
print("  Pascal does not require two branches. It requires that one step be an")
print("  INTEGER POWER OF A SINGLE UNBIASED TWO-WAY SPLIT -- s splits of equal")
print("  weight, at one spacing, with no other path. A cascade of balanced 50/50")
print("  splitters qualifies for any s. An unbalanced splitter does NOT, and")
print("  neither does any stray third path, however small: the 1% leak in the")
print("  last row kills it. That is a sharp, falsifiable statement about an")
print("  apparatus, and it says balance matters as much as branch count.")
