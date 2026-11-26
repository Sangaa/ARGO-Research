from fractions import Fraction as F
from math import comb
import itertools
def C(a,b): return comb(a,b) if 0<=b<=a else 0

print("="*78)
print("I went looking for NON-identifiability and found RIGIDITY. With a reason.")
print("="*78)
print("For a Pascal generator (s,L): sigma^2 = sL^2/4 and gamma_2 = -2/s, so a")
print("rival must match the centred moments")
print("    mu_2 = sL^2/4      and      mu_4 = kappa_4 + 3 sigma^4 = s L^4 (3s-2)/16")
print()
print("CASE s=1 is settled by a classical extremal fact, no search needed:")
print("    excess kurtosis >= -2 for EVERY distribution, with equality iff the")
print("    distribution is two-point with equal weights.")
print("    gamma_2 = -2 therefore FORCES a balanced two-point step. Identifiable.")
ok=True
import random
random.seed(3)
for _ in range(4000):
    m=random.randint(2,6)
    xs=random.sample(range(-6,7),m)
    ws=[F(random.randint(1,9)) for _ in range(m)]
    t=sum(ws); ws=[w/t for w in ws]
    mu=sum(w*x for w,x in zip(ws,xs))
    m2=sum(w*(x-mu)**2 for w,x in zip(ws,xs))
    if m2==0: continue
    m4=sum(w*(x-mu)**4 for w,x in zip(ws,xs))
    if m4/m2**2-3 < -2: ok=False
print(f"    checked gamma_2 >= -2 on 4000 random lattice distributions: {ok}")
print()
print("CASE s=2, L=1 (targets mu_2 = 1/2, mu_4 = 1/2). Solved, not searched:")
print("    mu_4 - mu_2 = sum_x w_x * x^2 (x^2 - 1)")
print("    On the INTEGER lattice x^2(x^2-1) is 0 for x in {-1,0,1} and >= 12")
print("    otherwise. Here mu_4 - mu_2 = 0, so every point with |x| >= 2 must")
print("    carry zero weight. Support is forced into {-1,0,1}; then mu_2 = 1/2")
print("    and centring give exactly (1/4, 1/2, 1/4). UNIQUE.")
# verify the identity and the forcing numerically
bad=[]
for _ in range(3000):
    m=random.randint(2,5); xs=random.sample(range(-5,6),m)
    ws=[F(random.randint(1,9)) for _ in range(m)]; t=sum(ws); ws=[w/t for w in ws]
    mu=sum(w*x for w,x in zip(ws,xs))
    if mu.denominator!=1: continue
    mu=int(mu)
    m2=sum(w*F(x-mu)**2 for w,x in zip(ws,xs))
    m4=sum(w*F(x-mu)**4 for w,x in zip(ws,xs))
    lhs=m4-m2
    rhs=sum(w*F(x-mu)**2*(F(x-mu)**2-1) for w,x in zip(ws,xs))
    if lhs!=rhs: bad.append(1)
print(f"    identity mu_4 - mu_2 = sum w x^2(x^2-1) verified on 3000 cases: {not bad}")
print()
print("THE GENERAL SHAPE. Define D(s,L) = mu_4 - mu_2 for the Pascal target:")
print(f"    {'s':>3} {'L':>3} {'mu_2':>9} {'mu_4':>11} {'mu_4 - mu_2':>13}  support forced?")
print("    "+"-"*62)
for s in range(1,6):
    for L in (1,2):
        m2=F(s*L*L,4); m4=F(s*L**4*(3*s-2),16)
        D=m4-m2
        print(f"    {s:>3} {L:>3} {str(m2):>9} {str(m4):>11} {str(D):>13}  "
              f"{'YES - support subset {-1,0,1}' if D==0 else 'no, D>0 leaves room'}")
print()
print("  So the rigidity is NOT general. It is exactly the D = 0 cases that are")
print("  pinned, and D = 0 only when s L^2 (3s-2) = 4 s L^2 / L^2 ... i.e. for")
print("  small (s,L). Everywhere else there IS room, and whether a rival exists")
print("  is open. I DID NOT establish non-identifiability, and I did not")
print("  establish identifiability either, except in the two cases above.")
print()
print("  HONEST STATUS:")
print("    s = 1, any L : IDENTIFIABLE, by the gamma_2 >= -2 extremal fact. Proved.")
print("    s = 2, L = 1 : IDENTIFIABLE on the integer lattice. Proved above.")
print("    everything else : OPEN. My 5-point search found no rival, but that")
print("                      search was too small to mean anything, and the")
print("                      7-point search did not finish.")
