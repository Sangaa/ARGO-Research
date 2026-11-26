from math import comb, cos, pi
print("My first attempt was a bad demonstration - 7 loose predicates, 0 singletons.")
print("It showed nothing. The real knob is not the predicate, it is the TOLERANCE.")
print()
primes=[p for p in range(5,1000) if all(p%d for d in range(2,int(p**.5)+1))]
def q(p):                       # a generic spectral quantity, nothing special
    return 2*cos(pi/p)*2*cos(2*pi/p)
# for each prime, find a tolerance window that isolates it on this one quantity
print("Same quantity for every prime. Tuning only the window, I can isolate:")
print(f"   {'target':>7} {'window on |q(p) - q(target)|':>32} {'how many primes inside':>24}")
import bisect
vals=sorted((q(p),p) for p in primes)
for target in (7,11,19,23,31,101):
    qt=q(target)
    d=sorted(abs(q(p)-qt) for p in primes if p!=target)
    eps=d[0]/2
    inside=[p for p in primes if abs(q(p)-qt)<eps]
    print(f"   {target:>7} {'< '+format(eps,'.3e'):>32} {len(inside):>24}  -> {inside}")
print()
print("Every prime is the unique one, for a window chosen after looking.")
print("That is the whole problem with 'it holds only at 19 among 166 primes':")
print("the claim is about the SEARCH, not about 19, until the search is stated.")
print()
print("WHAT WOULD MAKE IT A RESULT, concretely:")
print("  1. the condition written down BEFORE the scan, not fitted to the hit;")
print("  2. the number of conditions tried, and the tolerance, both reported;")
print("  3. a reason the condition matters - i.e. it forces something downstream,")
print("     the way 2cos(pi/m) <= 1 forces bounded spread at m <= 3;")
print("  4. and ideally it should predict a SECOND value, then be checked there.")
print()
print("Point 3 is the one that separates S05 from this. '3 is special' survived")
print("because 2cos(pi/3) = 1 CAUSES the boundedness - it is not a coincidence")
print("noticed at 3, it is the mechanism. If the 19 condition has a downstream")
print("consequence, it is a result. If it is a coincidence that survived a scan,")
print("it is 1 in 166 and 166 scans were available.")
