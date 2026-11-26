from math import comb
def C(a,b): return comb(a,b) if 0 <= b <= a else 0

def carries(k, m, p):           # Kummer: v_p(C(k+m,k)) = carries adding k+m in base p
    c = 0; carry = 0
    while k or m or carry:
        d = (k % p) + (m % p) + carry
        carry = 1 if d >= p else 0
        c += carry
        k //= p; m //= p
    return c

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37]
N = 400
print("Candidate set: every interior pair (n,k),(m,j) that an EQUALITY TEST must")
print("rule out. Built the honest way - all pairs with the same value are real")
print("repetitions, so the candidates are pairs we must NOT wrongly exclude, and")
print("the measure is how many NON-equal pairs a tool can rule out cheaply.")
print()
# sample random non-equal pairs and ask: does the tool separate them?
import random
random.seed(7)
cells = [(n,k) for n in range(4, N) for k in range(2, n//2+1)]
pairs = []
while len(pairs) < 20000:
    a = random.choice(cells); b = random.choice(cells)
    if a == b: continue
    pairs.append((a,b))
eq = [(a,b) for a,b in pairs if C(*a) == C(*b)]
ne = [(a,b) for a,b in pairs if C(*a) != C(*b)]
print(f"sampled pairs: {len(pairs)}   genuinely equal: {len(eq)}   unequal: {len(ne)}")
print()
print(f"{'tool':<42} {'unequal pairs ruled out':>24} {'rate':>8}  false?")
print("-"*86)

# tool A: an identity valid at every cell -- the hexagon / heat kernel class
ruled = 0
for (n,k),(m,j) in ne:
    # heat-kernel statement: both satisfy u_{n+1}=(u_n(x-1)+u_n(x+1))/2. always true.
    pass
print(f"{'identity true at every cell (hex, heat, 2cos)':<42} {0:>24} {0.0:>7.2%}  no")

# tool B: parity of the row sum / Krawtchouk involution eigenvalue -- also an identity
print(f"{'Krawtchouk involution (spectral)':<42} {0:>24} {0.0:>7.2%}  no")

# tool C: Kummer p-adic valuation vector  -- NOT an identity: it is a FUNCTION
for P in ([2], [2,3], [2,3,5], PRIMES[:6], PRIMES):
    ruled = 0; false_excl = 0
    for (n,k),(m,j) in ne:
        va = tuple(carries(k, n-k, p) for p in P)
        vb = tuple(carries(j, m-j, p) for p in P)
        if va != vb: ruled += 1
    for (n,k),(m,j) in eq:
        va = tuple(carries(k, n-k, p) for p in P)
        vb = tuple(carries(j, m-j, p) for p in P)
        if va != vb: false_excl += 1
    name = f"Kummer valuations, p in {P if len(P)<=3 else str(P[:3])[:-1]+', ...]'}"
    print(f"{name:<42} {ruled:>24} {ruled/len(ne):>7.2%}  "
          f"{'FALSE EXCLUSIONS: '+str(false_excl) if false_excl else 'no'}")
print()
print("Kummer is a FUNCTION of the cell, not an identity satisfied by every cell.")
print("Two cells can disagree on it. That is the entire difference, and it is why")
print("it excludes and the other three do not.")
