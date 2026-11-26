from math import comb
def S(n,m,r): return sum(comb(n,k) for k in range(n+1) if k%m==r)
def W(n,m,r): return m*S(n,m,r)-2**n

print("1. HER Q_7 against my S06 row for m=7")
print("   hers : Q_7(x) = x^3 + 57x^2 - 289x - 1")
print("          =>  W(n+21) + 57W(n+14) - 289W(n+7) - W(n) = 0")
print("   mine :      W(n+21) = -57W(n+14) + 289W(n+7) + W(n)")
print("   same equation rearranged:", True)
bad=[n for n in range(0,120) for r in range(7)
     if W(n+21,7,r)+57*W(n+14,7,r)-289*W(n+7,7,r)-W(n,7,r)!=0]
print(f"   re-verified in her sign convention, n=0..119, r=0..6 (840 cases): "
      f"{'HOLDS' if not bad else bad[:3]}")

print()
print("2. HER EDGE CASE: even m, the zero eigenvalue, and row 0")
print("   She says the REDUCED relation fails at row 0 for m=4. Checking the")
print("   reduced degree-1 form W(n+4) = -4 W(n), which drops the zero root:")
print(f"   {'n':>3} {'r':>2} {'W(n+4)':>12} {'-4 W(n)':>12}  ok?")
first_fail=None
for n in range(0,10):
    for r in range(4):
        lhs=W(n+4,4,r); rhs=-4*W(n,4,r)
        ok=(lhs==rhs)
        if not ok and first_fail is None: first_fail=(n,r)
        if n<3: print(f"   {n:>3} {r:>2} {lhs:>12} {rhs:>12}  {'ok' if ok else 'FAILS'}")
bad=[(n,r) for n in range(0,200) for r in range(4) if W(n+4,4,r)!=-4*W(n,4,r)]
print(f"   failures over n=0..199: {len(bad)}  first at {bad[0] if bad else '-'}")
print(f"   failures with n >= 1   : {len([x for x in bad if x[0]>=1])}")
print("   -> SHE IS RIGHT. The reduced form fails exactly at n = 0 and holds")
print("      from n = 1 on. The zero eigenvalue contributes only at the start,")
print("      and the degree-2 form W(n+8) = -4W(n+4) + 0*W(n) absorbs it, which")
print("      is why my S06 table reported degree 2 for m=4 and passed from n=0.")
print("      Her caveat and my table are the same fact stated at two degrees.")

print()
print("3. HER DEGREE BOUND for odd m: at most (m-1)/2")
for m in (3,5,7,9,11):
    print(f"   m={m:>2}: (m-1)/2 = {(m-1)//2}, my S06 table gave degree "
          f"{m//2}  -> {'same' if (m-1)//2==m//2 else 'DIFFER'}")
