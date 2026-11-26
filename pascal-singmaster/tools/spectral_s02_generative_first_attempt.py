from math import comb, log, sqrt, pi, exp
from fractions import Fraction as F
import numpy as np
def C(a,b): return comb(a,b) if 0<=b<=a else 0

print("="*78)
print("THE REFRAMED QUESTION: what makes a discrete system GENERATE Pascal,")
print("and what makes it deviate? (their question, answered sharply)")
print("="*78)
print("Setup: a translation-invariant one-step evolution on Z with stencil a_d,")
print("       u_{n+1}(x) = sum_d a_d u_n(x-d).  The n-step kernel is the sequence")
print("       of coefficients of f(z)^n where f(z) = sum_d a_d z^d.")
print()
print("CLAIM: the n-step kernel is EXACTLY a row of Pascal (up to shift and scale)")
print("       for all n  <=>  f has exactly TWO terms.  Any third point breaks it.")
print()

def nstep(sten, n):          # exact rational coefficients of f(z)^n
    poly={0:F(1)}
    for _ in range(n):
        new={}
        for d,c in poly.items():
            for e,a in sten.items():
                new[d+e]=new.get(d+e,F(0))+c*a
        poly={k:v for k,v in new.items() if v}
    return poly

STENCILS={
 "2-point  (1/2, 1/2)        [Pascal]":      {0:F(1,2), 1:F(1,2)},
 "2-point  (1/3, 2/3)  biased":              {0:F(1,3), 1:F(2,3)},
 "2-point  spaced d=0,3":                    {0:F(1,2), 3:F(1,2)},
 "3-point  (1/4, 1/2, 1/4)":                 {-1:F(1,4), 0:F(1,2), 1:F(1,4)},
 "3-point  (1/3, 1/3, 1/3)":                 {-1:F(1,3), 0:F(1,3), 1:F(1,3)},
 "4-point  uniform":                         {0:F(1,4),1:F(1,4),2:F(1,4),3:F(1,4)},
}
def is_binomial_row(coeffs):
    """is the coefficient list proportional to some row C(m,0..m) ?"""
    ks=sorted(coeffs); v=[coeffs[k] for k in ks]; m=len(v)-1
    if m<1: return True
    r=v[0]/F(C(m,0))
    return all(v[i]==r*C(m,i) for i in range(m+1))

print(f"{'stencil':<40} {'n=2':>6} {'n=3':>6} {'n=5':>6} {'n=8':>6}  exact Pascal?")
print("-"*78)
for name,st in STENCILS.items():
    res=[is_binomial_row(nstep(st,n)) for n in (2,3,5,8)]
    print(f"{name:<40} {str(res[0]):>6} {str(res[1]):>6} {str(res[2]):>6} "
          f"{str(res[3]):>6}  {'YES' if all(res) else 'NO'}")
print()
print("-> EXACT Pascal structure is a KNIFE EDGE: exactly two points in the")
print("   stencil, at any spacing, with any bias. A third point destroys it at")
print("   n = 2 already. That is the generative condition, and it is sharp.")
print()
print("="*78)
print("BUT: how universal is the LIMIT? (the distinction they asked for)")
print("="*78)
print("Measured: max |CDF_n - Gaussian CDF| after standardising, per stencil.")
print(f"{'stencil':<40} {'n=8':>9} {'n=32':>9} {'n=128':>9} {'n=512':>9}")
print("-"*78)
from statistics import NormalDist
nd=NormalDist()
for name,st in STENCILS.items():
    row=[]
    for n in (8,32,128,512):
        ks=sorted(st); 
        # use floats for large n
        poly=np.zeros(1); poly[0]=1.0
        base=np.zeros(max(ks)-min(ks)+1)
        for d,a in st.items(): base[d-min(ks)]=float(a)
        for _ in range(n): poly=np.convolve(poly,base)
        xs=np.arange(len(poly))+n*min(ks)
        mu=(xs*poly).sum(); sd=sqrt(((xs-mu)**2*poly).sum())
        cdf=np.cumsum(poly)
        z=(xs+0.5-mu)/sd
        row.append(float(np.max(np.abs(cdf-np.array([nd.cdf(t) for t in z])))))
    print(f"{name:<40} {row[0]:>9.4f} {row[1]:>9.4f} {row[2]:>9.4f} {row[3]:>9.4f}")
print()
print("-> EVERY stencil converges to the same Gaussian, at the same O(1/sqrt n)")
print("   rate. The LIMIT is universal; the EXACT combinatorics is not.")
print()
print("="*78)
print("THE ANSWER TO 'UNIVERSAL STRUCTURE OR COINCIDENTAL APPEARANCE?'")
print("="*78)
print("  BOTH, at different resolutions, and the distinction is now sharp:")
print()
print("  * Seeing a GAUSSIAN in a physical system tells you almost nothing about")
print("    Pascal. Any finite-variance local rule gives one. Universal, cheap.")
print("  * Seeing EXACT BINOMIAL weights tells you something strong and specific:")
print("    the generator has exactly TWO branches per step. Knife-edge, informative.")
print()
print("  So her cascade model (each stage splits into two delayed paths, H(w) =")
print("  cos^2(w tau)) produces Pascal NOT by analogy but because a 2-way splitter")
print("  IS a 2-point stencil. And it would stop producing Pascal the moment a")
print("  third path appears - which is a measurable, falsifiable prediction about")
print("  a real apparatus, not a resemblance.")
