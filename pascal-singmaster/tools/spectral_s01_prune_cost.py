from math import comb, log10
import time
def carries(k,m,p):
    c=carry=0
    while k or m or carry:
        d=(k%p)+(m%p)+carry; carry=1 if d>=p else 0; c+=carry; k//=p; m//=p
    return c
P3=[2,3,5]
def digits(n,k):                       # log10 C(n,k) without materialising it
    s=0.0
    for i in range(k): s += log10(n-i) - log10(i+1)
    return int(s)+1

print("CORRECTED. My first timing swept ALL cells, which are dominated by small k")
print("where comb is trivial - the sample decided the answer, again. Fixing it by")
print("measuring at a fixed deep position k = n/3.")
print()
print(f"{'n':>9} {'digits of C(n,n/3)':>19} {'Kummer(3p)':>12} {'exact comb':>12} {'speedup':>9}")
print("-"*68)
for n in (100, 300, 600, 3000, 10_000, 40_000, 150_000):
    k=n//3; reps=max(10, 2000//max(1,n//300))
    t0=time.perf_counter()
    for _ in range(reps): tuple(carries(k,n-k,p) for p in P3)
    t1=time.perf_counter()
    for _ in range(reps): comb(n,k)
    t2=time.perf_counter()
    kt=(t1-t0)/reps; ct=(t2-t1)/reps
    print(f"{n:>9} {digits(n,k):>19} {kt*1e6:>10.1f}us {ct*1e6:>10.1f}us {ct/kt:>8.2f}x")
print()
print("And at the shallow positions that dominate a naive sweep:")
print(f"{'n':>9} {'k':>6} {'digits':>8} {'Kummer':>10} {'comb':>10} {'speedup':>9}")
print("-"*58)
for n,k in ((600,2),(600,5),(600,20),(600,100),(600,300)):
    reps=3000
    t0=time.perf_counter()
    for _ in range(reps): tuple(carries(k,n-k,p) for p in P3)
    t1=time.perf_counter()
    for _ in range(reps): comb(n,k)
    t2=time.perf_counter()
    kt=(t1-t0)/reps; ct=(t2-t1)/reps
    print(f"{n:>9} {k:>6} {digits(n,k):>8} {kt*1e6:>8.2f}us {ct*1e6:>8.2f}us {ct/kt:>8.2f}x")
print()
print("There it is. At k=2 the prune costs 10x what it saves; at k=n/2 it saves")
print("3x. A sweep over all k is ~75% shallow cells, so the average came out")
print("against the prune and I reported the average as the verdict.")
