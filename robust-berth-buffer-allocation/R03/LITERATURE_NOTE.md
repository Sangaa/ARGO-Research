# Literature note — nonuniform buffer costs

Focused search date: 2026-11-27; not an exhaustive survey.

- Briskorn, Leung & Pinedo (2011), [“Robust scheduling on a single machine using time buffers”](https://doi.org/10.1080/0740817X.2010.505123), explicitly studies overall weighted buffer time and trade-offs between schedule performance and buffer allocation. Thus weighted buffer scheduling is established; R03 makes no novelty claim.
- Fulkerson & Gross (1965), [“Incidence matrices and interval graphs”](https://doi.org/10.2140/pjm.1965.15.835), develops the consecutive-ones structure for interval incidence matrices. The standard consecutive-ones total-unimodularity theorem then gives integrality of the R03 interval-covering primal for integral demands; see also Grötschel, Lovász & Schrijver's *Geometric Algorithms and Combinatorial Optimization* discussion of consecutive-ones matrices.

R03's narrow model fixes a vessel order and applies linear per-gap costs to R02's delay-cap interval constraints. The literature search does not determine whether this exact LP specialization has appeared. Novelty remains UNRESOLVED. The next search must compare full formulations and references for weighted buffer allocation, interval covering, and robust single-machine schedules.
