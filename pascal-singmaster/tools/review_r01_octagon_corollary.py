from math import comb
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def P(t):
    """full multiplicity of t in Pascal's triangle, all entries > 1"""
    hits=[]
    for k in range(1,60):
        n=2*k
        while C(n,k)<=t:
            if C(n,k)==t: hits.append((n,k))
            n+=1
        if C(2*k,k)>t: break
    out=[]
    for n,k in hits:
        out.append((n,k))
        if n-k!=k: out.append((n,n-k))
    return len(out), sorted(out)

print("THEIR P(t) COLUMN, recomputed independently")
THEIRS={2:1,3:2,6:3,8:2,9:2,19:2,36:4,56:4,63:2,64:2,65:2,120:6,210:6}
print(f"  {'t':>5} {'their P':>8} {'mine':>6}  cells")
ok=True
for t in sorted(THEIRS):
    p,cells=P(t)
    m=(p==THEIRS[t]); ok&=m
    print(f"  {t:>5} {THEIRS[t]:>8} {p:>6}  {'ok' if m else 'DIFFER'}  {cells}")
print(f"  whole column reproduces: {ok}")

print()
print("="*78)
print("THE COROLLARY OF THEIR OWN BOUNDARY THEOREM")
print("="*78)
print("  They prove: for a convex polygon with m extreme vertices and equal unit")
print("  weights, M(t) = m*P(t) + I(t) with I(t) >= 0.")
print()
print("  Immediately:  M(t) >= m*P(t) >= P(t)   for every m >= 1.")
print()
print("  So for EVERY polygon in the family:")
print("     M bounded  =>  P bounded  =>  SINGMASTER.")
print()
print("  That is not a remark about the square or the octagon. It is a theorem")
print("  about the whole geometric programme, and it follows in one line from")
print("  the theorem they just proved:")
print()
print("     NO POLYGON IN THIS FAMILY GIVES A STATEMENT WEAKER THAN SINGMASTER.")
print()
print("  Checked on their own data (m=8 for both octagons):")
print(f"  {'t':>5} {'P':>3} {'8P':>4} {'A':>5} {'I_A':>5} {'B':>5} {'I_B':>5}")
A={2:24,3:24,6:48,8:21,9:24,19:16,36:32,56:40,63:16,64:16,65:16,120:56,210:64}
B={2:24,3:48,6:104,8:49,9:48,19:48,36:96,56:192,63:48,64:48,65:56,120:208,210:400}
bad=[]
for t in sorted(THEIRS):
    p=THEIRS[t]
    ia=A[t]-8*p; ib=B[t]-8*p
    if ia<0 or ib<0: bad.append(t)
    print(f"  {t:>5} {p:>3} {8*p:>4} {A[t]:>5} {ia:>5} {B[t]:>5} {ib:>5}")
print(f"  I >= 0 in every case: {not bad}   {'' if not bad else bad}")
print(f"  their t=210 note 'boundary 48, interiors A16/B352': "
      f"8*P(210) = {8*6}, I_A = {A[210]-48}, I_B = {B[210]-48}  -> MATCHES")
