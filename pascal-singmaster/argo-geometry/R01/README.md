# ARGO geometry and inverse-observation record — archival round R01

Date: 2026-11-26. Seat: ARGO. The human research direction was to derive laws, test them, and design geometry rather than assume the traditional representation. This record preserves the available conversation artifacts; it is **not a claim of mathematical novelty, a solved conjecture, or a physical experiment**.

## Routes and scope

| Route | Evidence and restart point |
|---|---|
| Cyclic ternary arithmetic, 8/19 | [script](cyclic_8_19_check.py), [output](cyclic_8_19_check.log). Exact modular convolution, spectral polynomials, bounded checks. For weights (1,2,3), the principal/nonprincipal collision condition at primes p>3 is p dividing b²+bc+c²=19, derived by taking the norm of b(1−ω)+c(1−ω²); the scan is a check, not the proof. Scaling to (3,6,9) changes modular periods. No physical significance established. |
| Bells and signed Pascal differences | [R01 script](argo_bell_pascal_r01.py), [output](argo_bell_pascal_r01.log). Published measurements of alloys, not matched pure metals. Literal Hz matches are unit-dependent; negative result retained. Signed row four represents the square of a discrete second difference; a toy bending operator, not a full bell-shell model. |
| Inverse observations | [R02 script](argo_bell_inverse_r02.py), [output](argo_bell_inverse_r02.log). A restricted model f_j²=A j²+B j⁴ with A,B≥0 fails the two-frequency necessary bound f4/f2≤4 for the recorded bells. The held-out third mode also misses; not a prospective blind trial. Ternary generators with equal sum and spectral norm can differ in phase; the complex eigenvalue and sum recover ordered weights within this model. |
| Ternary lift | [R03 script](argo_pascal_ternary_r03.py), [output](argo_pascal_ternary_r03.log). Multiply a Pascal row by its outer binomial coefficient to obtain n!/(a!b!c!); project by b+2c mod 3 to recover ternary convolution. Covariance is a mathematical random-walk model, not a material measurement. |
| Square geometry | [R04 script](argo_square_geometry_r04.py), [output](argo_square_geometry_r04.log). F=a+bx+cy+dxy. Axial projections can agree while joint laws differ. ad−bc determines step covariance after normalization by S². A mixed moment identifies the remaining parameter for this fixed support. |
| Square Singmaster extension | [R05 script](argo_square_singmaster_sparse_r05.py), [output](argo_square_singmaster_sparse_r05.log). Equal-weight square layer B_n(i,j)=C(n,i)C(n,j). For t>1, Q(t)=4P(t)+I(t). Interior factors ≥n bound the row by sqrt(t); ordinary non-edge coefficients ≥C(n,2) bound their scan. The script is value-capped, not a universal bound. |
| Lattice octagon | [R06 script](argo_octagon_r06.py), [output](argo_octagon_r06.log). Integer steps (±2,±1),(±1,±2), not geometrically regular. Saturation at the value cap+1 preserves all smaller nonnegative counts. Independent exact early layers are checked. |
| Regular octagon | [R06 script](argo_regular_octagon_r06.py), [output](argo_regular_octagon_r06.log). Exact eighth-root endpoints represented by signed coordinate steps in Z⁴, not four physical dimensions. Enumeration groups absolute coordinates by symmetry. Independent early-layer checks do not replace proof of the tail bound. |

## Boundary theorem and open work

For a convex polygon with m extreme vertices used as equal unit-weight steps, the points on each edge of the n-fold convex hull arise only from that edge's two adjacent generator vertices. Thus for t>1, M(t)=m P(t)+I(t), I(t)≥0; vertex values 1 are excluded. In the octagons a mixed word has at least n permutations, so coefficients t>1 cannot occur at n>t. The regular-octagon script also uses a stronger tail reduction, which still merits independent scrutiny. See [Claude's independent review](../../reviews/REV_01_LIVING_REFERENCE_AND_OCTAGON_2026-11-26.md): the boundary corollary implies ordinary Singmaster if the generalized multiplicity is uniformly bounded, but the converse remains open. Extra geometry might supply leverage; no such proof has been established.

## Provenance and evidence

The scripts and logs below are recovered conversation attachments, not newly reconstructed historical files. All eight scripts were re-executed locally with python -I; exit status zero and stdout byte-for-byte identical to their paired original logs. NumPy and SymPy are required by some original scripts; they are preserved as-is, **not** mislabelled as stdlib-only certificates. No network or physical experiment was involved in this replay. This checks reproduction, not every assumption, data transcription, proof, or novelty. The output files, rather than manually copied counts, are the numeric record.

Public source references for the bell data: https://pmc.ncbi.nlm.nih.gov/articles/PMC7764211/ (Cekus et al., table 5); https://doi.org/10.1186/s40494-021-00620-2 (Carvalho et al.); https://www.hibberts.co.uk/identifying-bell-partials/ . The replay uses recorded numeric inputs, not a new source audit. Preserve the failed restricted model and literal-number comparison.

Unrecovered: original standalone triangle-count program/log and the dedicated Fe/Cu isotope control script/log, and the dense R05 census attachment. The full living reference contains additional contributions and historical entries not exported here. Do not invent artifacts or treat missing evidence as a pass. The public index links only existing public records. Source provenance for this round is the original research conversation and its R01–R06 reports; private operational content is not published.

Evidence classes: algebraic claims DERIVED within stated models; script outputs MEASURED (computational replay), value-window and physical proxies BOUNDED_PROXY; missing artifacts UNAVAILABLE. No human peer review or canonical promotion.

## Artifact manifest

Git blob identifiers measured on the mounted original attachments:

| File | Git blob SHA-1 |
|---|---|
| [cyclic_8_19_check.py](cyclic_8_19_check.py) | `475ffb9854d9daced79d2fdf0be447d4b50e257c` |
| [cyclic_8_19_check.log](cyclic_8_19_check.log) | `334848a2c24fb23ee526187a6a34584647f90fd4` |
| [argo_bell_pascal_r01.py](argo_bell_pascal_r01.py) | `62733ee41b4bcd44f6e8742ed4e5bb4d244e180a` |
| [argo_bell_pascal_r01.log](argo_bell_pascal_r01.log) | `c34dd416badadc7f9ae0bad62af9abe8c6cb162d` |
| [argo_bell_inverse_r02.py](argo_bell_inverse_r02.py) | `58f2b2819e53d9d333cce66aa9faf624c62fc946` |
| [argo_bell_inverse_r02.log](argo_bell_inverse_r02.log) | `91b2b7f0542fb30fa2db4a6f8a9a602cd6c0e934` |
| [argo_pascal_ternary_r03.py](argo_pascal_ternary_r03.py) | `7f03922aa6338e9a2966607127ce9125de0c56f8` |
| [argo_pascal_ternary_r03.log](argo_pascal_ternary_r03.log) | `3252802d84243ac1d764425ff7f825672c67e853` |
| [argo_square_geometry_r04.py](argo_square_geometry_r04.py) | `b909aa64f3186798750d5bffc346da48ccdf30f9` |
| [argo_square_geometry_r04.log](argo_square_geometry_r04.log) | `60754bf543341c220c1f565bc962eee23fd977e9` |
| [argo_square_singmaster_sparse_r05.py](argo_square_singmaster_sparse_r05.py) | `7daa44c8224147b289494c92657352fc799430a3` |
| [argo_square_singmaster_sparse_r05.log](argo_square_singmaster_sparse_r05.log) | `1622a9e586af19d3f3f3a58a2dbe7b0fe23d9fa5` |
| [argo_octagon_r06.py](argo_octagon_r06.py) | `ea04320ffb8e48a896c007ad30ea406bcfc1e0a5` |
| [argo_octagon_r06.log](argo_octagon_r06.log) | `ba4c12b4d1db05a9f050a392696c8b4c00115429` |
| [argo_regular_octagon_r06.py](argo_regular_octagon_r06.py) | `f7f98d0f95d019d81deff2c66520beb72132a11c` |
| [argo_regular_octagon_r06.log](argo_regular_octagon_r06.log) | `b562c1fc9187c876ca768c7c416a69a04ffac68a` |

Reproduce from this directory: `python -I argo_octagon_r06.py` (and likewise the other scripts); compare stdout with the matching .log file. The original scripts were intentionally not edited. New portable certificates and corrected claims belong in a new round.
