from math import comb
def C(a,b): return comb(a,b) if 0<=b<=a else 0
# C(n,k)=3003 with k<=n/2 forces small k, since C(n,k) >= C(2k,k) grows fast
hits=[]
for k in range(1,15):
    n=2*k
    while C(n,k)<=3003:
        if C(n,k)==3003: hits.append((n,k))
        n+=1
print(f"P(3003): left-half solutions {hits}  -> with mirrors, P = {2*len(hits)}")
print()
print("THEIR d-AXIS FORMULA  R_d(t) = d * 2^(d-1) * P(t), with P(3003) = 8:")
theirs={1:8,2:32,3:96,4:256,5:640,6:1536}
ok=all(d*2**(d-1)*8==theirs[d] for d in theirs)
for d in sorted(theirs):
    print(f"   d={d}: formula {d*2**(d-1)*8:>5}   their table {theirs[d]:>5}")
print(f"   internally consistent: {ok}")
print()
print("   BUT THE FORMULA ITSELF IS UNVERIFIED HERE. It depends on their")
print("   geometry, described in words, whose code was attached to that")
print("   conversation and not to this one. A table agreeing with the formula")
print("   that produced it is arithmetic, not evidence.")
print()
print("="*76)
print("THE LOGICAL CLAIM, which I CAN check, and it is the one that matters")
print("="*76)
print("  They state Q(t) = 4P(t) + I(t) with I >= 0, and separately that a")
print("  bound in the quadrinomial pyramid WOULD IMPLY Singmaster but not")
print("  conversely.")
print()
print("  The implication is CORRECT and immediate from their own relation:")
print("  Q >= 4P, so Q bounded => P bounded => Singmaster.")
print()
print("  AND THAT IS THE PROBLEM, NOT THE SELLING POINT.")
print("  Anything that IMPLIES Singmaster is AT LEAST AS HARD as Singmaster.")
print("  They present it as 'we added a new problem' - true - but the arrow's")
print("  direction means the generalisation cannot be a ROUTE to Singmaster.")
print("  Generalising upward is a legitimate move and sometimes the extra")
print("  symmetry gives leverage. That has to be ARGUED, and the argument is")
print("  absent. As written, the quadrinomial programme is strictly harder")
print("  than the thing it came from.")
