from math import comb
from fractions import Fraction as F
import random
def C(a,b): return comb(a,b) if 0<=b<=a else 0

print("="*78)
print("MONITOR FINDING 1: the Krawtchouk row as a PER-CELL tool is UNSOUND")
print("="*78)
print("  His point: the involution is a property of the ROW, not the cell. Any")
print("  per-cell instantiation keys on n alone - e.g. the +1 multiplicity")
print("  ceil((n+1)/2). And every genuine repetition has n != m, so such a tool")
print("  falsely excludes almost all of them.")
print()
# the complete population of genuine repetitions under n < 600
seen={}
for n in range(4,600):
    for k in range(2,n//2+1): seen.setdefault(C(n,k),[]).append((n,k))
eq=[(p[i],p[j]) for v,p in seen.items() if len(p)>1
    for i in range(len(p)) for j in range(i+1,len(p))]
print(f"  complete population of genuine repetitions, 4<=n<600: {len(eq)} pairs")
inv_kraw = lambda n,k: -(-(n+1)//2)        # ceil((n+1)/2), a function of n alone
false_ex=[(a,b) for a,b in eq if inv_kraw(*a)!=inv_kraw(*b)]
print(f"  falsely excluded by ceil((n+1)/2): {len(false_ex)} / {len(eq)}")
survivor=[(a,b) for a,b in eq if inv_kraw(*a)==inv_kraw(*b)]
print(f"  survivors: {survivor}")
for a,b in survivor:
    print(f"     -> C{a} = C{b} = {C(*a)};  ceil((n+1)/2) = "
          f"{inv_kraw(*a)} for both - the 3003 pair, a collision not a reason")
random.seed(7)
cells=[(n,k) for n in range(4,400) for k in range(2,n//2+1)]
pairs=[]
while len(pairs)<20000:
    x=random.choice(cells); y=random.choice(cells)
    if x!=y: pairs.append((x,y))
ne=[(x,y) for x,y in pairs if C(*x)!=C(*y)]
ruled=sum(1 for x,y in ne if inv_kraw(*x)!=inv_kraw(*y))
print(f"  its exclusion rate on unequal pairs: {ruled}/{len(ne)} = {ruled/len(ne):.2%}")
print()
print("  HE IS RIGHT. High exclusion power AND unsound. And my S02 table reported")
print("  'false exclusions: 0' for that row because the sample had ZERO genuine")
print("  equal pairs - the column was computed over an empty set and could not")
print("  have seen this. In S03 I quietly DROPPED the row instead of fixing it.")
print("  Dropping a row is not the same as reporting that it was unsound.")
