# TOTO | Research Sparks / دفتر الشرارات

A working notebook for independent exploration, failed ideas reconsidered under new information, and small mathematical experiments. Not a claim of novelty or peer review.

## Route index

- [R01 — moment identifiability, finite differences, and observation phases](R01/TOTO_RESEARCH_SPARKS_R01.md). DERIVED: sharp consecutive raw-moment threshold for binomial distributions on the integer lattice, constructive rival distributions, persistence under convolution, corrected common-phase criterion. MEASURED: bounded exact-arithmetic checks in [certificate](R01/toto_moment_probe.py) and [stdout](R01/toto_moment_probe.log). Open: multidimensional projections, noise, literature and independent review.
- Source: TOTO research session, 2026-11-26; research direction and request to revisit failed ideas from Human Authority. Public publication requested explicitly. The notebook's internal workspace URL is omitted in this public copy; private GitHub source references remain provenance as described in the repository README. No changes to the original notebook, script or historical log. On publication the script was rerun with `python3 -I` and stdout matched the original log byte for byte.

Reproduce from `R01/`: `python3 -I toto_moment_probe.py`. No network or third-party packages. New rounds get their own subfolder; preserve old claims and corrections.

Status: SESSION-DERIVED / NON-CANONICAL / REQUIRES VALIDATION.

## Subsequent rounds

- [R02 — joint moment and cyclic observation kernel](R02/TOTO_RESEARCH_SPARKS_R02.md): sharp finite-window degree obstruction; exact construction and certificate.
- [R03 — two coprime circles and an unbounded lattice](R03/TOTO_RESEARCH_SPARKS_R03.md): quadratic-periodic witness; sharp threshold and explicit counterexamples. [Certificate](R03/probe.py) · [stdout](R03/probe.log).
- [R04 — shared divisors](R04/TOTO_RESEARCH_SPARKS_R04.md): sharp threshold a+b-gcd(a,b), including noncoprime, nested and equal circles. [Certificate](R04/probe.py) · [stdout](R04/probe.log).
