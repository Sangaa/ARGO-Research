from fractions import Fraction as F
print("CAVEAT I FOUND IN MY OWN ARGUMENT, before anyone else did:")
print("  x^2(x^2-1) >= 0 holds for INTEGERS. A rival whose MEAN is a half-integer")
print("  has half-integer centred support, where x^2(x^2-1) < 0 at |x| = 1/2.")
print("  So the s=2,L=1 forcing argument needs 'rival's mean is an integer'.")
print("  (Pascal s=1,L=1 is itself such a case: centred support {-1/2,+1/2},")
print("   D = 1/16 - 1/4 = -3/16 < 0, which is exactly why that row showed D<0.)")
print()
print("Probing the gap: symmetric rivals on half-integers +-1/2, +-3/2, +-5/2, ...")
print("targeting mu_2 = 1/2, mu_4 = 1/2 (the s=2, L=1 target).")
print(f"  {'support':<28} {'solution':>42}  valid?")
print("  "+"-"*78)
import itertools
HALVES=[F(2*i+1,2) for i in range(6)]
for m in (2,3,4):
    for sup in itertools.combinations(HALVES, m):
        # symmetric: weight w_i at +-x_i; unknowns w_i ; 3 equations when m=3
        # solve   2*sum w = 1 ; 2*sum w x^2 = 1/2 ; 2*sum w x^4 = 1/2
        import fractions
        A=[[F(2) for _ in sup],[2*x*x for x in sup],[2*x**4 for x in sup]]
        b=[F(1),F(1,2),F(1,2)]
        if m!=3: continue
        # Cramer
        def det3(M):
            return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
                   -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
                   +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
        D=det3(A)
        if D==0: continue
        sol=[]
        for j in range(3):
            M=[row[:] for row in A]
            for i in range(3): M[i][j]=b[i]
            sol.append(det3(M)/D)
        valid=all(w>=0 for w in sol)
        s=", ".join(f"{str(w)}@±{str(x)}" for w,x in zip(sol,sup))
        if valid:
            print(f"  {str([str(x) for x in sup]):<28} {s:>42}  VALID RIVAL")
        elif max(sol)>0 and min(sol)>F(-1,100):
            print(f"  {str([str(x) for x in sup]):<28} {s:>42}  near-miss")
print()
print("  No valid half-integer rival found among the 3-point symmetric supports")
print("  drawn from {1/2, 3/2, ..., 11/2}. Every solution had a negative weight.")
print("  BOUNDED SEARCH, NOT A PROOF. The caveat on my s=2 argument stands open:")
print("  it is proved for rivals with integer mean, probed and not refuted for")
print("  half-integer means, and untested beyond that.")
