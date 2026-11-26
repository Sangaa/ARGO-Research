from math import comb, cos, pi
import cmath
print("="*76)
print("3. THE m=5 ROW IS FIBONACCI, AND THAT CLOSES A LOOP WITH THIS MORNING")
print("="*76)
print("   The spread's growth rate is 2cos(pi/m). At m=5:")
print(f"     2cos(pi/5) = {2*cos(pi/5):.10f}")
print(f"     phi        = {(1+5**0.5)/2:.10f}")
print(f"     equal to 1e-12? {abs(2*cos(pi/5)-(1+5**0.5)/2) < 1e-12}")
print("   And the measured m=5 spreads were 1,2,3,5,8,13,21,34,55,89 - Fibonacci.")
print()
print("   This is the SAME PARAMETER as S04. There her family was")
print("     P_n = a P_(n-1) + b P_(n-2),  with the wave branch a = 2cos(theta).")
print("   Here the residue-spread of Pascal mod m grows at rate a = 2cos(pi/m).")
print("   phi is not 'appearing again'. phi IS 2cos(pi/5), and the m=5 residue")
print("   system is the a = phi point of the same one-parameter law.")
print()
print(f"   {'m':>3} {'a = 2cos(pi/m)':>16} {'what that a is':<34}")
print("   "+"-"*60)
NAMES={2:"0 - degenerate, spread exactly 0",3:"1 - the boundary, spread bounded",
       4:"sqrt(2)",5:"phi, the golden ratio",6:"sqrt(3)",
       10:"phi again, via 2cos(pi/10)=sqrt(2+phi)"}
for m in (2,3,4,5,6,10):
    print(f"   {m:>3} {2*cos(pi/m):>16.10f} {NAMES[m]:<34}")

print()
print("="*76)
print("4. HER CRITERION D = a^2+b^2+c^2-ab-bc-ca IS THE EISENSTEIN NORM")
print("="*76)
w=cmath.exp(2j*pi/3)
print("   Claim: D(a,b,c) = |a + b*w + c*w^2|^2 for w a primitive cube root of 1.")
bad=[]
for a in range(-6,7):
    for b in range(-6,7):
        for c in range(-6,7):
            D=a*a+b*b+c*c-a*b-b*c-c*a
            z=a+b*w+c*w*w
            if abs(abs(z)**2 - D) > 1e-9: bad.append((a,b,c))
print(f"   verified over all (a,b,c) in [-6,6]^3  ({13**3} triples): "
      f"{'IDENTITY HOLDS' if not bad else bad[:3]}")
print()
print("   Her table, recomputed:")
for t in ((1,1,1),(1,1,0),(2,2,1),(1,2,3),(3,6,9)):
    a,b,c=t
    print(f"     {str(t):>10} -> D = {a*a+b*b+c*c-a*b-b*c-c*a}")
print()
print("   SO THE 3/6/9 THREAD AND THE HEXAGONAL-LATTICE THREAD ARE ONE OBJECT.")
print("   D is the norm form of Z[w], the EISENSTEIN INTEGERS, whose geometry IS")
print("   the triangular/hexagonal lattice. The monitor lane's R10 hexagonal work")
print("   on #883 and this 3-fold periodicity are the same ring, not two leads.")
print("   D = 0 iff a = b = c (the balanced generator); D = 1 iff the triple is")
print("   a unit times a generator of Z[w] - which is why (1,1,0) and (2,2,1)")
print("   both give 1 and behave alike, as her table observed without the reason.")
print()
print("   And (3,6,9) = 3*(1,2,3), so D scales by 9: 3 -> 27. The '3,6,9' triple")
print("   carries NO structure beyond (1,2,3) - it is the same Eisenstein point")
print("   scaled by 3. Her own table shows this and it is worth saying plainly.")
