# ARGO — open research record

A working research house. Each lane gets a folder; each folder is a working record
rather than a finished paper: what was derived, what was measured, what was wrong,
and who corrected it.

Nothing here is peer-reviewed by a human mathematician. Every record states its own
evidence class — read the class before the claim.

---

## ده إيه (بالعربي)

ده السجل العام لأبحاث البيت. كل مسار بحثي له مجلد، وكل مجلد **دفتر معمل** مش ورقة
مكتملة: اللي اشتقناه، واللي قِسناه، واللي كان غلط، ومين صلّحه.

**الأغلاط مكتوبة جوه السجلات بنفس تفاصيل النتايج.** ده مقصود. شغل بحثي ماتشوفش فيه
غير النتايج اللي نجحت مينفعش يتراجع.

**القاعدة:** كل رقم في أي سجل ليه سكريبت بيطلّعه. مافيش رقم مكتوب بالإيد. السبب إن
ده حصل فعلًا — رقم اتكتب بالإيد (480 بدل 472) وصفر اتكتب بالإيد جوه جدول قياس،
والاتنين اتمسكوا من مراجعين. فالشهادة بقت بتطبع أعدادها بنفسها.

**مين عمل إيه:** التوجيه البحثي والتصحيحات الموضوعية من Human Authority. الاشتقاقات
والمراجعات من مقاعد نماذج مختلفة من **مزوّدين مختلفين**، فالمراجعة عبر-مزوّد — لكنها
**مش مراجعة أقران بشرية**، ومحدش من بره شافها لحد الآن.

---

## Lanes

### [`pascal-singmaster/`](pascal-singmaster/) — repeated values in Pascal's triangle

The **Singmaster conjecture**: is the number of times a value `> 1` can appear in
Pascal's triangle bounded by an absolute constant? `3003` appears eight times and
nobody knows whether anything appears nine.

Headline: an **effective** uniform quadratic bound — for `t >= 2`, `k >= 1`,
`n >= 2k + 3t`, every solution of `C(n,k) = C(n-t, k+t)` satisfies `n < 200 t²`.
Jenkins (arXiv:1411.4111) proves *finiteness* for `t_1 != t_2` by Siegel's theorem,
which is **ineffective** — it gives no searchable range. This bound is explicit, so
for each `t` the solution set is decidable by a finite search. Jenkins' §3 already
sketches finiteness at `t = 2`, so the honest contribution is two rows: **effectivity
is uniformly new; finiteness is new only for `t >= 3`.**

Six sub-lanes, three of them opened because another closed. Its own
[README](pascal-singmaster/README.md) is the route index.

*New lanes get a sibling folder here.*

---

## How a lane is added

A folder goes in when it can carry its own weight, not when it has a result:

1. **A README that is a route index**, not a file list — purpose, why the lane opened,
   what closed and by what measurement, what is still open.
2. **One certificate per claim.** `python3 -I`, no network, no external data, exits
   non-zero on failure, and **prints its own population sizes** rather than letting
   prose carry a hand-typed figure.
3. **Failures kept.** A superseded derivation stays beside its correction; the diff is
   the lesson. A first attempt that was wrong is not deleted.
4. **Every claim bound** by
   `WHAT WAS MEASURED → SCOPE → METHOD → EVIDENCE → LIMITATION → EVIDENCE CLASS`,
   with the class one of `MEASURED / DERIVED / BOUNDED_PROXY / UNAVAILABLE`.
   A `BOUNDED_PROXY` number was measured in one window with one parameter range and
   is not a theorem.
5. **Frozen results do not move.** Anything offered for external review is frozen;
   improvements become a *new* version with a change log, and the superseded file is
   never edited, so a referee holding an old copy can see exactly what differs.
   Editing a frozen file in place is itself a defect — see
   [`FREEZE_LOG.md`](pascal-singmaster/referee/FREEZE_LOG.md) for a leftover that was
   recorded rather than patched for exactly this reason.

## What is not here

The house also runs engineering, review and governance lanes which are **not
published**: their records carry third-party and operational material that does not
belong in a public repository, and stripping the sensitive parts would leave records
that no longer support their own claims.

Cross-references in these files to `Sangaa/ARGO-KOP` pull requests point at a
**private** repository and will not resolve for an outside reader. They are kept
because deleting a record's provenance to make it look self-contained is worse than
a dead link.

Two further research lanes exist in the house and are not here: a vision-science /
perception lane, and a method retrospective on how earlier answers were justified.
Both are entangled with personal material.

## Licence

Research records (`.md`) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/);
certificate scripts (`.py`) under MIT. See [`LICENSE`](LICENSE).
