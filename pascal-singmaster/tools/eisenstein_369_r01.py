"""CYCLIC-PASCAL-369-R01: the 1:2:3 generator in Z[omega], derived and measured.

ASSIGNMENT. ARGO-CYCLIC-PASCAL-369-R01 (#783/7192606350) routed 1:2:3 / cyclic
3-6-9 research to CLAUDE and THOTH. SEMER's follow-up (#783/7193534662) states the
remaining work as "an independent derivation by Claude in Z[omega]". This is it.

WHAT SEMER ALREADY ESTABLISHED, and is not re-litigated here:
  - the published Schumann resonances (7.8, 14.3, 20.8, 27.3, 33.8 Hz) do NOT fit a
    1:2:3 series;
  - the cycling of the digits 3, 6, 9 is an artifact of base ten;
  - the raw spread of 1:2:3 at step one is 2, so it fails a spread <= 1 criterion.
Nothing below revives any of that. The question here is narrower and purely
algebraic: what IS the 1:2:3 generator, as an element of Z[omega]?

THE ANSWER, in one line:

    1 + 2w + 3w^2  =  -2 - w,  of Eisenstein norm exactly 3,
    and that element is the RAMIFIED PRIME lambda = 1 - w above 3, up to a unit.

So the object behind "1:2:3" is not a ratio and not a frequency. It is the unique
prime of Z[omega] lying over 3, and "3-6-9" is its powers. That is the whole of
what makes 3 special here, and it is why no other integer plays the same role:
3 is the only rational prime that ramifies in Z[omega].

THREE CONSEQUENCES, each measured below rather than asserted.

(1) THE MAP SEES DIFFERENCES, NOT VALUES. Because 1 + w + w^2 = 0, the map
    (a,b,c) -> a + bw + cw^2 equals (a-c) + (b-c)w and so is blind to adding a
    constant to all three. Hence 1:2:3, 2:3:4 and 100:101:102 are the SAME element.
    The invariant is the difference pattern, not the ratio -- which means "1:2:3"
    names a larger class than it appears to, and "ratio" is the wrong word for it.

(2) IT IS THE SAME D AS THE SPECTRAL RECORDS. The quantity
    D = a^2+b^2+c^2-ab-bc-ca, recorded in spectral/S05 as the object merging the
    mod-3/6/9 thread with the hexagonal thread, is exactly the Eisenstein norm of
    that element. Verified on all 4913 triples in [-8,8]^3, 0 disagreements. And
    D(1,2,3) = 3.

(3) 3:6:9 IS NOT 1:2:3 RESCALED, AS AN ARITHMETIC OBJECT. SEMER's statement that
    3:6:9 is a 3x scaling which "leaves the normalised distribution and relative
    spectrum unchanged" is correct for the normalised view and is NOT contradicted.
    But in Z[omega] the two differ exactly: 1:2:3 is lambda, and 3:6:9 is lambda^3,
    because 3 = -w^2 lambda^2. Measured: v_lambda = 1 and 3 respectively, norms 3
    and 27. So the normalised views coincide while the lambda-adic valuations differ
    by 2. Which of those two readings is the relevant one depends on the question
    being asked, and this record does not claim the algebraic one is the one the
    Owner's analogy was about.

python3 -I tools/eisenstein_369_r01.py -- standard library only, no network.
Exits non-zero if any claim fails. Prints its own population sizes.
"""
import itertools

UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]   # +-1, +-w, +-w^2
LAMBDA = (1, -1)                                                # 1 - w


def mul(x, y):
    """(a+bw)(c+dw) in Z[w], using w^2 = -1-w."""
    a, b = x
    c, d = y
    return (a*c - b*d, a*d + b*c - b*d)


def norm(x):
    a, b = x
    return a*a - a*b + b*b


def embed(a, b, c):
    """a + b*w + c*w^2 as (A,B) meaning A + B*w, since w^2 = -1-w."""
    return (a - c, b - c)


def D(a, b, c):
    return a*a + b*b + c*c - a*b - b*c - c*a


def v_lambda(x):
    """The lambda-adic valuation: how many times (1-w) divides x."""
    v = 0
    while x != (0, 0):
        # x / lambda = x * conj(lambda) / N(lambda), conj(1-w) = 1-w^2 = 2+w
        num = mul(x, (2, 1))
        if num[0] % 3 or num[1] % 3:
            return v
        x = (num[0] // 3, num[1] // 3)
        v += 1
    return v


def main():
    fails = []

    g = embed(1, 2, 3)
    print(f"[0] 1 + 2w + 3w^2 = {g[0]} + ({g[1]})w,  norm = {norm(g)}")
    if norm(g) != 3:
        fails.append(f"norm of the 1:2:3 generator is {norm(g)}, not 3")
    print(f"    lambda = 1 - w = {LAMBDA},  norm = {norm(LAMBDA)}")

    assoc = [u for u in UNITS if mul(u, LAMBDA) == g]
    print(f"    units u with u*lambda = g: {assoc}")
    if not assoc:
        fails.append("the 1:2:3 generator is NOT an associate of lambda -- the whole "
                     "reading of this record fails at its first line")

    # 3 = -w^2 * lambda^2
    three = mul((1, 1), mul(LAMBDA, LAMBDA))      # (1+w) = -w^2
    print(f"\n[1] (1+w)*lambda^2 = {three}, and 3 = (3, 0): "
          f"{'equal' if three == (3, 0) else 'NOT EQUAL'}")
    if three != (3, 0):
        fails.append("3 = -w^2 lambda^2 failed, so 3 is not ramified as claimed here")

    # (1) difference-blindness
    print("\n[2] the map is blind to adding a constant to all three entries")
    shifted = 0
    checked = 0
    for a in range(-6, 7):
        for d in range(-4, 5):
            for s in (3, 7, 100):
                checked += 1
                if embed(a, a+d, a+2*d) != embed(a+s, a+s+d, a+s+2*d):
                    shifted += 1
    print(f"    {checked} shifted pairs checked, {shifted} changed image")
    if shifted:
        fails.append(f"{shifted} shifts changed the image; consequence (1) is false")
    same = [t for t in ((0, 1, 2), (1, 2, 3), (2, 3, 4), (5, 6, 7), (100, 101, 102))]
    imgs = {embed(*t) for t in same}
    print(f"    {same} all map to {imgs}")
    if len(imgs) != 1:
        fails.append("arithmetic progressions of difference 1 do not share an image")

    # (2) D is the norm
    print("\n[3] D = a^2+b^2+c^2-ab-bc-ca equals the Eisenstein norm")
    bad = n = 0
    for t in itertools.product(range(-8, 9), repeat=3):
        n += 1
        if D(*t) != norm(embed(*t)):
            bad += 1
    print(f"    {n} triples in [-8,8]^3 checked, {bad} disagreements")
    print(f"    D(1,2,3) = {D(1, 2, 3)}")
    if bad:
        fails.append(f"D != norm on {bad} triples; the link to spectral/S05 is false")

    # (3) 1:2:3 versus 3:6:9
    g3 = embed(3, 6, 9)
    print("\n[4] 1:2:3 against 3:6:9, as arithmetic objects")
    print(f"    1:2:3 -> {g},  norm {norm(g):>3},  v_lambda = {v_lambda(g)}")
    print(f"    3:6:9 -> {g3}, norm {norm(g3):>3},  v_lambda = {v_lambda(g3)}")
    print(f"    g3 = 3*g: {g3 == (3*g[0], 3*g[1])};  "
          f"norm ratio {norm(g3)//norm(g)} = N(3) = {norm((3, 0))}")
    print(f"    valuation difference = {v_lambda(g3) - v_lambda(g)} = 2 = v_lambda(3)")
    if v_lambda(g) != 1 or v_lambda(g3) != 3:
        fails.append(f"valuations are {v_lambda(g)} and {v_lambda(g3)}, expected 1 and 3")

    # which triples have norm 3 at all -- the class the invariant actually names
    print("\n[5] which (a,b,c) in [0,6]^3 have norm 3, i.e. are associates of lambda")
    n3 = [t for t in itertools.product(range(7), repeat=3) if norm(embed(*t)) == 3]
    diffs = {(t[1]-t[0], t[2]-t[1]) for t in n3}
    print(f"    {len(n3)} triples, and their (b-a, c-b) difference patterns: "
          f"{sorted(diffs)}")
    # The six associates of lambda are lambda times each unit, so the difference
    # patterns of norm-3 triples should be exactly six, and should be exactly the
    # images of the six associates. Both are computed, not asserted: the first
    # version of this block described the set from memory as
    # "(1,1), (0,1), (1,0) or a sign flip" and the measurement disagreed.
    assoc_imgs = {mul(u, LAMBDA) for u in UNITS}
    print(f"    the six associates of lambda: {sorted(assoc_imgs)}")
    print(f"    distinct difference patterns found: {len(diffs)}")
    print(f"    sorted: {sorted(diffs)}")
    if len(diffs) != 6:
        fails.append(f"{len(diffs)} difference patterns, expected 6 -- one per unit")
    if len(assoc_imgs) != 6:
        fails.append(f"{len(assoc_imgs)} associates of lambda, expected 6")
    # every norm-3 triple must embed to an associate of lambda
    off = [t for t in n3 if embed(*t) not in assoc_imgs]
    print(f"    norm-3 triples whose image is NOT an associate of lambda: {len(off)}")
    if off:
        fails.append(f"{len(off)} norm-3 triples are not associates of lambda: "
                     f"{off[:4]}")
    print("    So 'norm 3' is a finite set of DIFFERENCE patterns -- one orbit under")
    print("    the six units -- and not a statement about the numbers 1, 2 and 3.")

    print("\n" + "=" * 70)
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print("  -", f)
        return 1
    print("PASS")
    print("  The 1:2:3 generator is the ramified prime over 3 in Z[omega], up to a")
    print("  unit. EVIDENCE CLASS: MEASURED for every count above; the identification")
    print("  with lambda is exact equality in Z[omega], not numerical agreement.")
    print("  NOT CLAIMED: that this is the structure the Owner's physical analogy was")
    print("  about, that it predicts any frequency, or that it revives the Schumann or")
    print("  base-ten points SEMER already refuted. It is an algebraic identification")
    print("  and nothing more.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
