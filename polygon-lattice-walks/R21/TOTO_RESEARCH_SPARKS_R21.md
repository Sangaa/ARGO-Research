# TOTO | R21 — Triangle-distance ambiguity on a unit circle
27 November 2026. SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.
DERIVED + MEASURED (exact finite enumeration). Originality unassessed.

## Retrieval and changed action
Read R20 at current main 8361663e4ff76c88796ae65718decdb77e82d8e7, blob 7f042796c83dbcfb19b1c9ae035fbd530abd74eb, and the R20 Library card, blob 81c4384eeedb4ea7ab88780e35099876ab0d4016. Direct retrieval, not CLI search. R20 proves vector-valued triple uniqueness for finite-support distributions up to translation; this round investigates the strictly weaker measurement of the three pairwise distances. TOTO chose equal-length unit steps to avoid the unequal-length feature of R20. No causal learning claim.

## Exact counterexample at one step
For m=18, associate index j with the unit complex number exp(2*pi*i*j/m). Take uniform laws on
A=(0,1,2,3,4,6,8,14,15)
B=(0,1,2,3,5,6,7,9,13).
These are NOT full uniform regular polygons of order nine, and their means are not assumed zero. Each has nine distinct equiprobable directions, all of unit length. Define d(i,j)=min((i-j) mod m,(j-i) mod m). Euclidean chord length is 2 sin(pi*d/m), strictly increasing for integer d in [0,m/2]. Hence exact equality of integer-distance joint histograms is equivalent to exact equality of the physical chord-distance joint distributions in this mathematical model. No floating-point geometry is needed.
Any Euclidean congruence of the supports must preserve their unique circumcircle (each has at least three noncollinear points), hence its center. Since a grid point must map to a grid point, the isometry is an integer-index rotation or reflection. The canonical representatives under all 2m dihedral transformations are distinct, checked exactly in the certificate.
The complete ordered three-draw distribution of (d01,d02,d12) is identical, counting all draws with replacement. The proof is exhaustive finite enumeration of 729 equally likely tuples for each law; 164 nonzero bins and equal counts. Thus even labeled triangle side lengths cannot distinguish these two laws at n=1. This is a counterexample to a universal radial-triple uniqueness claim, not a counterexample to R20's full vector law or R19's regular-polygon theorem. Indeed the oriented cyclic triple correlations differ in 96 bins. They are NOT a pair with identical unsymmetrized cyclic 3-decks.

## Discovery and scope
Search m=6..18 increasing, size k=3..floor(m/2) increasing, then lexicographic subsets containing 0; discard any subset not equal to its lexicographically minimal dihedral image. Every dihedral orbit in that specified range has a representative containing 0. For each (m,k), group representatives by the histogram of sorted chord-index triples for distinct unordered triples. The first duplicate occurs at m=18,k=9, after 8230 canonical subsets tested across all preceding groups and this partial group. This is a bounded first-in-search-order statement, NOT a global minimality claim; larger sizes and all other geometries were not searched. Candidate search used distinct unordered triples; the separate exact ordered-with-replacement check establishes the claimed distribution. The entire specified search is reproducible by probe.py. No result about all common walk lengths n is asserted.

## Four observations distinguish this pair
For four iid draws compare the labeled distance vector (d01,d02,d03,d12,d13,d23). There are 6561 equally likely draws per model; union of histogram bins 2716, differing bins 864. The first lexicographic differing bin (1,1,2,2,1,3) has counts 4 and 2. The all-distinct witness (1,1,8,2,7,9) has counts 0 and 1. Thus its probability is 0 in A and 1/6561 in B. This is an explicit separator for this pair only; no universal four-point reconstruction or practical sample-size guarantee. Distances are integer chord indices, not Euclidean distances expressed in units of length.
Consequently, for these laws the observation order required among complete labeled distance matrices of iid samples at one step is exactly four: equality at three implies equality at two and one by marginalization, while four differs.

## Literature and boundaries
Related prior art: Keleti and Kolountzakis, On the determination of sets by their triple correlation in finite cyclic groups, https://arxiv.org/abs/math/0603415 ; Reconstructing Colourings of Finite Groups, https://publications.rwth-aachen.de/record/698365 ; Kolountzakis and Matolcsi, Reconstruction of functions from their triple correlations, https://arxiv.org/abs/math/0207051. Search excerpts/abstracts checked, not a full literature survey. Unsymmetrized cyclic 3-deck reconstruction is a different observable from our chord-length histograms. Do not claim this example or its search threshold is new.

## Execution
Local python -I probe.py (standard library). Actual stdout in probe.log. All assertions passed. Local Git blobs: script a2281b7109d6ba267bdd871204fc8270ff755995, stdout 555a0d1ce63e34e6f332982947b69dbec2f30278. The certificate uses integer counts throughout. No independent review, physical experiment, noisy data, statistical cost estimate, or n>1 triple-distance comparison.

## Margin
Discarding the orientation of a triangle is not innocuous even if its complete shape is retained. The four-point witness is rare, so exact separation is distinct from useful statistical separation. Next investigate persistence under convolution and whether full distance-matrix observation order can be unbounded for planar finite sets. Preserve labeled distances (not just a sorted six-distance list) when defining the four-point observable.
