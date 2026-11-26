import cmath
print("HER CORRECTION: the discriminant alone does not determine growth.")
print("Growth is |lambda|; oscillation is arg(lambda). Delta only says whether")
print("arg is 0/pi or not. Checking my S04 table against that.")
print()
print(f"{'(a,b)':>9} {'Delta':>7} {'|lambda|max':>12} {'arg(lambda)':>12}  {'S04 said':<22} {'actually':<26}")
print("-"*100)
S04={(2,-1):"polynomial (unipotent)",(1,1):"exponential",(2,1):"exponential",
     (1,2):"exponential",(1,-1):"oscillation",(0,-1):"oscillation",
     (3,-2):"exponential",(1,-2):"oscillation"}
wrong=[]
for (a,b),said in S04.items():
    D=a*a+4*b
    r1=(a+cmath.sqrt(D))/2; r2=(a-cmath.sqrt(D))/2
    mx=max(abs(r1),abs(r2))
    ang=max(abs(cmath.phase(r1)),abs(cmath.phase(r2)))
    if D<0:
        if   abs(mx-1)<1e-12: act="oscillation, CONSTANT amp"
        elif mx>1:            act="oscillation, GROWING amp"
        else:                 act="oscillation, DECAYING amp"
    elif D==0: act="polynomial (unipotent)" if abs(mx-1)<1e-12 else f"|l|={mx:.3f}, repeated"
    else:      act="exponential" if mx>1 else "decay"
    ok = (act.split(",")[0] in said) and ("GROWING" not in act or "oscillation" in said)
    flag = "" if act.startswith(said.split(" ")[0]) and "GROWING" not in act else "  <-- S04 HID THIS"
    if "GROWING" in act or "DECAYING" in act: wrong.append((a,b,act))
    print(f"{str((a,b)):>9} {D:>7} {mx:>12.6f} {ang:>12.6f}  {said:<22} {act:<26}{flag}")
print()
print(f"rows where S04's one-word label hid the amplitude: {len(wrong)}")
for a,b,act in wrong: print(f"   (a,b) = ({a},{b}) is {act}, S04 just said 'oscillation'")
print()
print("WHY my table looked right: for complex roots the product is -b, so")
print("|lambda|^2 = -b. With b = -1 that is 1 - CONSTANT amplitude. Her earlier")
print("family fixed b = -1, so on THAT SLICE the discriminant does determine")
print("everything. I generalised off the slice without re-deriving. She is right.")
print()
print("CORRECTED MAP - two axes, not one:")
print(f"  {'|lambda|':<14} {'arg(lambda)':<16} {'behaviour'}")
print("  "+"-"*56)
for m,g,beh in ((" < 1","any","decay"),(" = 1","0 or pi","bounded, non-oscillating"),
                (" = 1","other","oscillation, constant amplitude"),
                (" > 1","0 or pi","exponential growth"),
                (" > 1","other","oscillation with growing amplitude")):
    print(f"  {m:<14} {g:<16} {beh}")
print()
print("  |lambda|^2 = -b for complex roots, so the growth axis is b and the")
print("  oscillation axis is where a sits relative to 2*sqrt(-b). Delta = a^2+4b")
print("  is the BOUNDARY between the two arg regimes, nothing more.")
