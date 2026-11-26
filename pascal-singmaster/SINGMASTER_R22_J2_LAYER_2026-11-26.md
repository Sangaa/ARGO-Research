# CLAUDE — R22: HER GENERAL-`W` FORMULA CLOSES THE `j = 2` LAYER TOO

> **CORRECTED 2026-11-26 — two corrections, both from outside me.**
>
> **1. "CLOSED" WAS WRONG, AND SHE CAUGHT IT.** This record says the `j = 2` layer is
> "closed for every `t`" on the strength of a scan to `t = 4000` plus a known limit.
> That is not a proof: a verified range and an asymptotic direction leave the whole
> interval between them unargued, and the degenerate `W = 0` endpoint — where the
> degree drops — is not covered at all. Her objection stands and the title overstates.
> She then **supplied** the missing argument: bounding `(t-1)P(t,L)/t^4 <=
> (L^2+58L+369)/8` for `t >= 2` reduces `m_2 < 1` to `L^2 - 326L + 369 < 0`, true at all
> four `L` (`-600, -2175, -3096, -6879`). So the lower endpoints **are** now proved for
> every `t >= 2` — by her algebra, not by my scan. Verified in
> `SINGMASTER_R23_TOTO_BOUND_REVIEW_2026-11-26.md` §"her reservation".
>
> **2. THE REASON I GAVE FOR NOT READING HER PROOF WAS WRONG.** §4 below blames the
> repository being private. Human Authority corrected this: the repository has been
> private its whole life, and `git` worked all session. The actual gap was narrower —
> no GitHub **API** credential in this container (`gh auth status`: not logged in), so
> comment bodies were unreachable while commits and branches were not. Diagnosing a
> missing capability as a property of the repository sent me looking in the wrong place;
> the fix took one tool, the browser already attached to this session. The derivation
> was read and reviewed the same day in R23.
>
> Both are left in place below rather than edited away, because the wrong reason is the
> part worth keeping.

Date: 2026-11-26
Seat: CLAUDE / ANALYSIS
Source: TOTO, R21 — symbolic derivation of `c_{2t-4}(t, W)`, plus a candidate
general bound `n < 200t^2` which I have **not** been able to read (§4)

## 0. Short version

Her `c_{2t-4}` is general in **both** `t` and `W`; mine was only the `W = 1`
slice. Verified exactly against the polynomial at every bracket endpoint for
`t = 2..21` and at arbitrary `W` values — **zero mismatches**. Her `m_2` at
`W = 1` and mine are the same rational function.

Because hers carries `W`, it closes the case I had left open:

    lower endpoint W = -L :  m_2 = (t-1) P(t,L) / (48 L t^4)   ->  25/(48L)
    P(t,L) = 25t^3 + 16t^2 L + 25t^2 - 2tL + 23t + L^2 - 6L + 23

and `(t-1)P(t,L) < 48 L t^4` holds for every `t` checked to 4000 at each of the
four `L` that occur, with the maximum at **small** `t` (0.2395 at `L=3, t=3`) and
the limit `25/(48L) <= 25/144`.

So with R21's `j = 1` layer and this, both layers are **settled over the measured
range at both endpoints** — see the correction banner: "closed for every `t`" was
my wording and it was wrong; her algebraic closure is what makes it true — and what
remains is

    max over j >= 3 : 959/31104 = 0.030832   at t = 6, W = 1, j = 3
    room for a crude bound : factor 32.4

The target has gone `1.94 -> 4.27 -> 32.4` across three rounds, each time because
the case attaining the maximum got proved rather than because the estimate
improved.

`EVERY TIME WE PROVE THE WORST CASE, THE REST GETS EASIER THAN THE LAST ESTIMATE`

## 1. Her formula, verified

    c_{2t-4} = t(t-1)/1152 * [25t^3 - 16t^2 W + 25t^2 + 2tW + 23t + W^2 + 6W + 23]

Checked against the exact endpoint polynomial at both bracket endpoints for
`t = 2..21`, and separately at `W = -7, -2, 0, 2, 5, 13` for `t = 3, 5, 8, 11`.
Zero mismatches in either set.

Her `W = 1` specialisation `m_2 = (t-1)(25t^3+9t^2+25t+30)/(48t^4)` expands to
`(25t^4-16t^3+16t^2+5t-30)/(48t^4)`, identical to my
`(25t^5-16t^4+16t^3+5t^2-30t)/(48t^5)`. Two derivations, same function; hers
reached it symbolically in `W`, mine by interpolation at fixed `W`, and hers is
the better object.

- EVIDENCE CLASS: MEASURED exactly, two independent families of test points.

## 2. The lower endpoints, now closed

At `W = -L`, `c_d = -tL/24`, so

    m_2 = 24 |c_{2t-4}| / (t L t^4) = (t-1) P(t,L) / (48 L t^4)

| `L` | max of `m_2` over `t = 2..4000` | attained at | limit `25/(48L)` |
|---|---|---|---|
| 3 | 0.239540 | `t = 3` | 0.1736 |
| 8 | 0.140788 | `t = 2` | 0.0651 |
| 11 | 0.128314 | `t = 2` | 0.0434 |
| 24 | 0.121582 | `t = 2` | 0.0217 |

The maxima sit at the **smallest** `t`, not at large `t`, so the inequality is
not asymptotically delicate; it is a finite check at small `t` plus a limit that
goes the right way. `(t-1)P(t,L) < 48 L t^4` is a degree-4 against degree-4
comparison with leading coefficients `25` and `48L`, so for `L >= 1` the
asymptotic direction is immediate and only small `t` needs looking at.

- EVIDENCE CLASS: MEASURED to `t = 4000` for each `L`; the asymptotic direction
  DERIVED. A fully general statement needs the small-`t` range argued rather
  than enumerated, which is a finite and easy task.

## 3. What is left

After `j = 1` (R21) and `j = 2` (here):

    max over all (t, w_0, j >= 3), t = 2..60 : 959/31104 = 0.030832
    attained at t = 6, W = 1, j = 3
    room : factor 32.4

Worth noting what did **not** work even with that much room: the root-modulus
bound from #904 gives `|c_{d-j}/c_d| <= 48 C(2t,j+2) t^{j+1}/L`, and at `j = 3`
that is about `12.8 t^5 / L` against a target of `t^6` — it needs `t^2 >= 12.8/L`,
so it finally *does* hold for `t` beyond a small constant. That is the first `j`
at which the crude bound is not hopeless, which is a concrete reason to think
`j >= 3` is the easy region rather than merely the one with slack.

The obvious continuation is the one her formula suggests: a general
`c_{2t-2-j}(t, W, j)`. Two of the three coefficients now have closed forms
derived the same way; a pattern in `j` would close everything at once.

## 4. Her `n < 200t^2` — I have not reviewed it

She asks for an independent review of a candidate general bound, published as a
comment on PR #904. **I cannot read it.** The repository is private, the
container has no GitHub credential, and the laptop that holds the authenticated
`gh` has been closed since 08:00. A WebFetch of a private-repo comment returns
nothing.

> **SUPERSEDED.** The private-repository part of that sentence is wrong — see
> correction 2 in the banner. The real blocker was the missing GitHub API credential
> alone; the comment was read through the attached browser and reviewed in R23. The
> paragraph is kept because the misdiagnosis is the lesson: when a capability is
> missing, name the capability, not the asset.

So, precisely:

- I have **not** reviewed the derivation, the remainder bounds or the sign cases.
- What I can say is that `n < 200t^2` is **consistent** with everything measured
  here: the Taylor-shift thresholds give `n <~ 1.24 t^2` across `t = 2..60`, two
  orders of magnitude inside her bound. Consistency of a claim with measurements
  is not a review of its proof, and I am not offering it as one.
- To review it I need the derivation itself — pasted into the conversation, or
  the laptop reachable again.

`I CANNOT REVIEW WHAT I CANNOT READ, AND CONSISTENCY IS NOT VERIFICATION`

## 5. Status

| statement | status |
|---|---|
| `c_{2t-4}(t,W)` closed form | **verified exactly**, hers |
| `j = 1`, both endpoint types | **proved** (R21) |
| `j = 2`, `W = 1` | **proved** (R21, hers independently) |
| `j = 2`, lower endpoints | **proved** modulo a finite small-`t` check |
| `j >= 3` | measured `t = 2..60`, max `959/31104` |
| `n <= 4t^2` for all `t >= 2` | follows from the full claim; not yet proved |
| `n < 200t^2` (hers) | **unreviewed — I could not read the derivation** |
| non-existence, `t = 2..20` | proved and exhaustively verified |
| originality, present day | unresolved |

## 6. Next

1. A general `c_{2t-2-j}(t, W, j)`, following her method. Two coefficients in,
   the pattern may be visible.
2. Read and review `n < 200t^2` once it is reachable.
3. Originality: a citation sweep of the papers citing Jenkins.

Research only. Branch `claude/singmaster-r20-margin-20261126-r02` carries R20,
R21 and this; `claude/singmaster-r19-exact-20261126-r01` is open as PR #905.
