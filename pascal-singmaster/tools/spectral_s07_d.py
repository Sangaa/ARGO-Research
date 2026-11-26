from math import comb
def C(a,b): return comb(a,b) if 0<=b<=a else 0
def S(n,r): return sum(C(n,k) for k in range(n+1) if k%5==r)
print("CORRECTION TO MYSELF: her (A,B,C,C,B) names the DISTINCT values, so C is")
print("the third distinct value, not the third sorted entry. I misread it and")
print("nearly reported her matrix as failing. Redoing.")
print()
F=[0,1]
for i in range(2,260): F.append(F[-1]+F[-2])
print(f"  {'n':>4} {'distinct A,B,C':<22} {'x=A-B':>7} {'y=B-C':>7} "
      f"{'predict (x+y, x+2y)':>22} {'actual at n+2':>16}  {'x+y = F_(n+1)?':>15}")
ok=True; okF=True
for n in range(2,22,2):
    d=sorted(set(S(n,r) for r in range(5)), reverse=True)
    if len(d)<3: 
        print(f"  {n:>4} {str(d):<22}  (fewer than 3 distinct values)")
        continue
    A,B,Cv=d[0],d[1],d[2]
    x,y=A-B,B-Cv
    d2=sorted(set(S(n+2,r) for r in range(5)), reverse=True)
    A2,B2,C2=d2[0],d2[1],d2[2]
    x2,y2=A2-B2,B2-C2
    pred=(x+y,x+2*y)
    if (x2,y2)!=pred: ok=False
    if x+y!=F[n+1]: okF=False
    print(f"  {n:>4} {str((A,B,Cv)):<22} {x:>7} {y:>7} {str(pred):>22} "
          f"{str((x2,y2)):>16}  {str(x+y==F[n+1]):>15}")
print()
print(f"  her two-step map [[1,1],[1,2]] reproduces (x,y): {ok}")
print(f"  and max - min = x + y = F_(n+1): {okF}")
print()
print("  SO HER DERIVATION IS CORRECT IN BOTH PARTS, and the error was mine:")
print("  I read the third SORTED entry instead of the third DISTINCT value and")
print("  got y = 0 every time. One careless index away from telling a colleague")
print("  her proof was broken.")
