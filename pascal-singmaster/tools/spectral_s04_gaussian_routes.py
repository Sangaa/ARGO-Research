from math import exp, pi, cos, sqrt, log
print("HER OBJECTION TO 'SINK': she says not every Gaussian comes from summing")
print("independent variables -- some come from PDEs, some from spectral symmetry,")
print("some from max-entropy. Checking whether those are really independent.")
print()
print("1. Gaussian is a FIXED POINT of the Fourier transform (not a CLT fact):")
def ft(f,xi,M=40000,R=8.0):
    s=0.0; h=2*R/M
    for i in range(M):
        x=-R+i*h
        s+=f(x)*cos(2*pi*x*xi)*h
    return s
g=lambda x: exp(-pi*x*x)
worst=max(abs(ft(g,xi)-g(xi)) for xi in (0.0,0.3,0.7,1.2))
print(f"   max |FT(e^-pi x^2)(xi) - e^-pi xi^2| over 4 points: {worst:.2e}  -> FIXED POINT")
print()
print("2. Gaussian is the MAXIMUM-ENTROPY density at fixed variance (not a CLT fact):")
import random
random.seed(5)
def ent_disc(p): return -sum(w*log(w) for w in p if w>0)
# compare differential entropy numerically among densities with the same variance
def discretise(f,R=8.0,M=4000):
    h=2*R/M; xs=[-R+i*h for i in range(M)]
    w=[f(x)*h for x in xs]; t=sum(w); w=[q/t for q in w]
    var=sum(q*x*x for q,x in zip(w,xs))-(sum(q*x for q,x in zip(w,xs)))**2
    return w,var,h
cands={"gaussian":lambda x: exp(-x*x/2),
       "laplace":lambda x: exp(-abs(x)*sqrt(2)),
       "uniform":lambda x: 1.0 if abs(x)<sqrt(3) else 0.0,
       "triangle":lambda x: max(0.0,1-abs(x)/sqrt(6))}
print(f"   {'density':<10} {'variance':>10} {'differential entropy':>22}")
best=None
for nm,f in cands.items():
    w,var,h=discretise(f)
    H=ent_disc(w)+log(h)
    print(f"   {nm:<10} {var:>10.4f} {H:>22.6f}")
    if best is None or H>best[1]: best=(nm,H)
print(f"   highest entropy at variance 1: {best[0]}  -> MAX-ENTROPY")
print()
print("3. Are these independent reasons, or the same reason wearing hats?")
print("   The CLT fixed point and the Fourier fixed point are LINKED: Fourier")
print("   turns convolution into multiplication, so the attractor of 'add and")
print("   rescale' has to be a Fourier fixed point. Not a coincidence.")
print("   Max-entropy is a genuinely DIFFERENT route - it is a variational")
print("   statement, not a dynamical one, and it needs no limit at all.")
print()
print("   SO SHE IS RIGHT and my label was too flat. The Gaussian is a sink for")
print("   the question 'what generated this?' -- that part stands, and it is why")
print("   it has no exclusion power. But the fact that a dynamical attractor, a")
print("   spectral fixed point and a variational optimum land on the SAME object")
print("   is itself structure, and it deserves its anchor. What it does NOT")
print("   deserve is to be read backwards: seeing a Gaussian still tells you")
print("   nothing about which of the three routes produced it.")
