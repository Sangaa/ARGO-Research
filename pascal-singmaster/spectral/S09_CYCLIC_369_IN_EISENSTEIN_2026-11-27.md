# S09 — `CYCLIC-PASCAL-369-R01`: what the 1:2:3 generator actually is

Date: 2026-11-27 · Seat: CLAUDE / ANALYSIS
Assignment: `ARGO-CYCLIC-PASCAL-369-R01` (`#783/7192606350`), whose remaining item per
SEMER's follow-up (`#783/7193534662`) is **"an independent derivation by Claude in `ℤ[ω]`"**
Status: `DERIVED + MEASURED / ALGEBRAIC IDENTIFICATION ONLY / NO PHYSICAL CLAIM`

---

## 0. What is already settled and is not re-opened here

SEMER's audit established, and this record does not revive any of it:

- the published Schumann resonances (7.8, 14.3, 20.8, 27.3, 33.8 Hz) **do not fit** a
  1:2:3 series;
- the cycling of the digits 3, 6, 9 is **an artifact of base ten**;
- the raw spread of 1:2:3 at step one is 2, so it **fails** a spread ≤ 1 criterion.

The question here is narrower and purely algebraic: **what is the 1:2:3 generator, as an
element of `ℤ[ω]`?**

## 1. The answer

```
1 + 2ω + 3ω²  =  −2 − ω,   of Eisenstein norm exactly 3
```

and that element **is the ramified prime `λ = 1 − ω` above 3, up to a unit** — measured:
`(−1 − ω)·λ = −2 − ω`, exactly, and it is the only unit that does it.

So the object behind "1:2:3" is **not a ratio and not a frequency. It is the unique prime of
`ℤ[ω]` lying over 3**, and "3, 6, 9" is its powers.

**And that is the whole of why 3 is special here.** `3 = −ω²λ²` — verified: `(1+ω)λ² = 3`
exactly. **3 is the only rational prime that ramifies in `ℤ[ω]`.** No other integer can play
this role, not because of numerology but because ramification happens at the discriminant
and the discriminant is `−3`.

## 2. Three consequences, each measured

### (1) The map sees **differences**, not values

Because `1 + ω + ω² = 0`, the map `(a,b,c) ↦ a + bω + cω²` equals `(a−c) + (b−c)ω` and is
therefore **blind to adding a constant to all three entries**. Measured: 351 shifted pairs,
**0 changed image**. And

```
(0,1,2)  (1,2,3)  (2,3,4)  (5,6,7)  (100,101,102)   →   all map to  −2 − ω
```

**So "1:2:3" names a much larger class than it appears to, and "ratio" is the wrong word for
it.** `100:101:102` is not in ratio 1:2:3 by any reading, and it is the same element. The
invariant is the **difference pattern**.

Pushed further: the triples of norm 3 in `[0,6]³` are **30**, and their difference patterns
`(b−a, c−b)` are **exactly six**:

```
(1,1)  (−1,−1)  (1,−2)  (−1,2)  (2,−1)  (−2,1)
```

which is **one orbit under the six units** of `ℤ[ω]` — and every one of those 30 triples
embeds to an associate of `λ`, with **0 exceptions**. So "norm 3" is a finite set of
difference patterns, not a statement about the numerals 1, 2 and 3.

*(The first version of this paragraph described that set from memory as
"`(1,1), (0,1), (1,0)` or a sign flip". The measurement disagreed. The certificate now
prints the set and checks its size and its orbit property, rather than letting prose carry
it.)*

### (2) It is the same `D` as the spectral records

`spectral/S05` recorded `D = a² + b² + c² − ab − bc − ca = |a + bω + cω²|²` as the object
that merged the mod-3/6/9 thread and the hexagonal-lattice thread into `ℤ[ω]`. That is
**exactly the Eisenstein norm** of the element above. Verified on **all 4913** triples in
`[−8,8]³`, **0 disagreements**. And `D(1,2,3) = 3`.

So this record and S05 are describing one object, and the assignment's `ℤ[ω]` framing was
the right one.

### (3) `3:6:9` is **not** `1:2:3` rescaled, as an arithmetic object

SEMER wrote that 3:6:9 is a 3× scaling which *"leaves the normalised distribution and
relative spectrum unchanged."* **That is correct for the normalised view and is not
contradicted here.** But in `ℤ[ω]` the two differ exactly:

| | element | norm | `v_λ` |
| --- | --- | --- | --- |
| `1:2:3` | `−2 − ω` | **3** | **1** |
| `3:6:9` | `−6 − 3ω` | **27** | **3** |

`v_λ(3:6:9) − v_λ(1:2:3) = 2 = v_λ(3)`, because `3 = −ω²λ²`. So **`1:2:3` is `λ` and
`3:6:9` is `λ³`** up to units.

The normalised views coincide while the **λ-adic valuations differ by 2**. Which of the two
readings is the relevant one depends on the question being asked, and **this record does not
claim the algebraic one is the one the Owner's analogy was about.**

## 3. Why `m = 3` and not another `m` — the link to the spectral lane

`spectral/S05` measured that residue spread mod `m` grows at rate `2cos(π/m)`, and is bounded
**iff `2cos(π/m) ≤ 1` iff `m ≤ 3`**. This record says `3` is the unique ramified prime of
`ℤ[ω]`.

**These are two faces of the same fact, and that is the closest thing here to an answer to
the Owner's question about why 3 keeps appearing:** `ℤ[ω]` is the ring of the cube roots of
unity, `m = 3` is the largest modulus with bounded spread, and `3` is the one prime where
that ring ramifies. The number 3 is not special because of its digits; it is special because
it is the discriminant's prime.

`SCOPE / LIMITATION:` the identification is exact and the counts are measured. The *link*
between the `2cos(π/m)` boundary and ramification is stated here as a **structural
observation, not a proved equivalence** — `EVIDENCE CLASS: DERIVED`. Nobody has shown the
`m ≤ 3` bound *follows from* ramification, and this record does not.

## 4. What is NOT claimed

- **No physical claim whatsoever.** Nothing here predicts a frequency, an optimum, or a
  resonance, and nothing revives the Schumann or base-ten points SEMER refuted.
- **No novelty.** That `3` is the unique ramified prime of `ℤ[ω]`, and that `1 − ω` generates
  the prime above it, is standard algebraic number theory. What is new here is only the
  *identification* of the house's 1:2:3 object with that prime, and the difference-blindness
  consequence.
- **No bearing on Singmaster.** This is the `369` assignment, not the bound.

## Evidence

`tools/eisenstein_369_r01.py` — exit 0, standard library, no network, prints every count.

| claim | class |
| --- | --- |
| `1 + 2ω + 3ω² = −2 − ω`, norm 3, associate of `λ` | **MEASURED**, exact equality in `ℤ[ω]` |
| `3 = −ω²λ²` | **MEASURED**, exact |
| difference-blindness, 351 pairs | **MEASURED**, 0 changes |
| `D` = Eisenstein norm, 4913 triples | **MEASURED**, 0 disagreements |
| 6 difference patterns = one unit orbit, 30 triples, 0 exceptions | **MEASURED** |
| `v_λ` = 1 and 3 | **MEASURED** |
| `2cos(π/m)` boundary ↔ ramification | **DERIVED** — observation, not proof |

## Sources

- Assignment: [`#783/7192606350`](https://github.com/Sangaa/ARGO-KOP/issues/783#issuecomment-7192606350) · SEMER's follow-up: [`#783/7193534662`](https://github.com/Sangaa/ARGO-KOP/issues/783#issuecomment-7193534662) · CLAUDE's ACK: [`#915/7200327193`](https://github.com/Sangaa/ARGO-KOP/pull/915#issuecomment-7200327193)
- Both are in the **private** `Sangaa/ARGO-KOP` and will not resolve for an outside reader.
- [`spectral/S05 — Three is 2cos(π/3)`](S05_THREE_IS_2COS_PI_OVER_3_2026-11-26.md) — it carries **both** `D` and the `2cos(π/m)` boundary, which is itself the point: the two faces of 3 were already in one record before this one connected them to ramification.
