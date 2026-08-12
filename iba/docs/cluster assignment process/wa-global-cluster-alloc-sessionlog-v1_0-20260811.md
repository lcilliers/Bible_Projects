# WA — Cluster Allocation of Unallocated Strongs — SESSION LOG (v1.0)

- **filename:** wa-global-cluster-alloc-sessionlog-v1_0-20260811.md
- **date timestamp:** 2026-08-11
- **version:** v1.0 (new)
- **author:** le Roux Cilliers
- **previous outputs referenced:** obslog `wa-obslog-global-cluster-alloc-v1-20260811.md`; deliverables `wa-global-cluster-alloc-final-v1_3-20260811.json`, `wa-global-t3-cluster-record-v1_0-20260811.json`, `wa-global-prior-reassignments-v1_1-20260811.json`, `wa-global-cluster-alloc-low-review-v1_2-20260811.md`, `wa-global-t2-likeness-review-v1_0-20260811.md`.
- **purpose:** Preserve the full process, debate, and decisions of the cluster-allocation exercise so the method can be re-run on future allocation passes.

---

## 1. Objective & scope

Allocate **1,612 previously-unallocated Strong's numbers** (809 Hebrew, 803 Greek) to the programme's clusters, and produce a JSON assignment report for Claude Code (CC) to apply. Inputs: `cluster.csv` (49 clusters), `cluster_strong.csv` (2,801 already-allocated strongs — reference on prior approach, **not** for reassignment except where later authorised), `strong_without_cluster.csv` (the 1,612 to allocate). Evidence per strong was **stepGloss + transliteration + count only** — no verse layer.

Governing rules for T2 and FLAG (from the researcher): **T2 (Supplementary)** = strongs with no inner-being (IB) relation; **FLAG** = IB-related but fitting no cluster (rare).

## 2. Process narrative (the debate)

**Startup gate (GR-LOAD-001).** Global rules loaded (34 across 12 categories), obslog initialised, cadence discipline active, before any analysis.

**Data understanding + a named insufficiency.** The only evidence is a short gloss; the prior `old-system-migration` allocation almost certainly used richer STEP/verse data we do not have. Gloss-only allocation is sound for clear cases and weak for abstract glosses — flagged up front, and confidence was carried on every item.

**Forks surfaced before bulk work (F1–F5):** evidence basis; the IB/T2 boundary + T2 default; output schema; FLAG threshold; filename/prefix. Researcher resolved all: proceed on gloss with confidence; **T2 for anything not denoting IB**; schema accepted; FLAG rare; global-rules filename style, prefix `wa`.

**Why HIGH rests on precedent, not statistics.** The 2,801 prior allocations were treated as a labelled precedent set. Three precedent signals: **P1** exact gloss in prior labels, **P2** exact gloss in a cluster.csv gloss list, **P3** transliteration in a cluster.csv gloss list. A TF-IDF "profile" scorer was tried and **rejected for HIGH** — it mis-fired badly on short glosses (wanted "brother" → Deceit) and buried obvious items ("to sanctify" had no token overlap). HIGH was therefore restricted to **single-cluster gloss precedent (P1/P2)**; **translit-only (P3) matches were demoted** to review because of Hebrew/Greek homograph collisions. Profile scores were kept only as a *sorting aid* for the medium pile.

**Tiers:** HIGH (precedent, no decision needed) · MEDIUM (precedent-conflict / profile suggestion / T2-hint, grouped for trend-spotting) · LOW (no precedent, weak/no signal).

**T3 "Operations" — a new cross-cutting grouping.** The researcher observed that action words (see, give, make, take, bow, look…) sitting in T2/FLAG describe a human operation and aren't tied to one cluster. A new cluster **T3** was created for these. Scope was then **expanded to the whole corpus** (prior allocations included) and the short name set to **"Operations."**

**The edge rule (evolved through debate).** An initial reading — tag *all* IB-cluster operation-verbs with T3 (edge) — was **corrected by the researcher**: a verb with a **direct meaning-relation to a cluster stays in that cluster** (to love → M05, not T3). **T3 is only for operations whose cluster cannot reasonably be determined, or that apply to many clusters.** Edge (T3 + one cluster) is **rare, not a default.** Consequence: the ~795 specific-verb operations already in IB clusters stayed put; only generic-verb operations were reassessed.

**Generic-verb disposition (75 items).** Applying the edge rule: 39 STAY (direct relation), 24 → T3 (bare/applies-to-many), 8 RECLUSTER (sense ties elsewhere). The reclusters were the expected find — the Hebrew *nasa* ("to lift") senses had all pooled into M19 Trust and were split to their real homes (forgive→M11, guilt→M10, vow→M21, kindness→M05); plus make peace→M33. Researcher confirmed both.

**Medium accepted.** The researcher judged the medium suggestions "near enough… a likely bucket, not a final decision" and accepted them as suggested.

**Low review (semantic pass).** 574 items: operations → their cluster if directly related else T3; non-operations → an IB cluster only where the gloss denotes IB (a transparent stem lexicon) else **T2 (F2 default)**. Result: T2 362 · T3 127 · IB-cluster pulls 85.

**T2 likeness review + descriptors.** The full T2 set (542) was grouped by likeness (particles, people, objects, body, colours, numbers, etc.). The large "Other/abstract" bucket surfaced ~64 items that read as IB (beauty, courage, mockery, comfort, perverseness…). The researcher framed these as **descriptors** — qualifiers that pair with something else and are rarely analysed alone. Decision: descriptors **stay in T2** (T2's definition is precisely "supplementary"); only descriptors with a **direct single-cluster relation** are pulled (20 pulled); **no separate T4 bucket** — verse-level analysis pulls descriptors in automatically.

**Consolidation.** All decisions folded into the final allocation.

## 3. Decisions register

| id | decision | rationale |
|---|---|---|
| F1 | gloss-only evidence, carry confidence | no verse layer available; be honest about strength |
| F2 | T2 for anything not denoting IB | clean default; keeps IB clusters clean |
| F3 | schema w/ confidence, operation, alt_clusters, review_flag, rationale | auditable, review-ready |
| F4 | FLAG rare; never from cluster.csv FLAG gloss list | that list is an uncertainty bag, not an assignment signal |
| F5 | global-rules filename style, prefix `wa` | corpus consistency |
| T3 | new cluster "Operations" | operations analysable as movements; pair to a cluster at verse level |
| edge | direct relation → cluster (not T3); T3 only if undetermined/many; edge rare | avoids general spreading; keeps T3 meaningful |
| MED | mediums accepted as suggested | likely bucket for verse-level assessment, not final meaning |
| DESC | descriptors stay T2; pull only directly-tied; no T4 | descriptors pair and are rarely analysed alone; T2 = supplementary |

## 4. Reusable method (recipe for future passes)

1. Complete the startup gate; declare reference; initialise obslog.
2. Load cluster taxonomy, prior labelled allocations, and the unallocated list.
3. Build precedent signals: P1 exact gloss in prior labels; P2 exact gloss in cluster.csv gloss lists; P3 transliteration in cluster.csv gloss lists. **Exclude FLAG from P2/P3 votes.**
4. Tier: **HIGH** = single-cluster gloss precedent (P1/P2). **Demote translit-only (P3) singles** to review. **MEDIUM** = precedent-conflict / profile suggestion / non-IB-hint. **LOW** = no precedent.
5. **Operations carve-out → T3** under the edge rule: T2/FLAG operations → T3; generic ops in IB clusters reassessed (STAY / T3 / recluster); specific IB verbs stay.
6. **LOW semantic pass:** operation → cluster-or-T3; non-operation → IB cluster via a transparent stem lexicon, else **T2 (F2)**.
7. **T2 likeness review**; handle **descriptors** = stay T2 unless directly cluster-tied; no new bucket unless the verse tooling needs the tag.
8. Consolidate the final allocation; keep **prior reassignments** in a separate report; add the **T3 cluster record**.
9. All outputs are **reports for researcher review**; CC applies via patch (GR-PROC-004). Profile scores inform, never decide; counts inform, never decide.

## 5. Pitfalls encountered (avoid on reuse)

- **cluster.csv FLAG gloss list is an uncertainty bag** — matching it must not vote "assign FLAG." Exclude from P2/P3.
- **TF-IDF profile scoring is too noisy for confident assignment** on 1–4 word glosses (brother→Deceit). Use it only to sort, never to decide HIGH.
- **Transliteration-only matches collide on homographs** (Hebrew *nasa* → many senses). Demote to review.
- **Multi-cluster prior rows:** the same strong appears under >1 cluster. Building a dict keyed by strong number **drops instances** (lost 21). Iterate per (strong, cluster) instance.
- **Substring keyword matching creates false positives** ("ill" in k**ill**/f**ill**; "sin" in his**sin**g). Use **token/stem matching with word boundaries.**
- **Seat words** (heart/soul/spirit/mind/flesh/conscience) → **M47**, never T2.

## 6. Outputs produced

| file | purpose |
|---|---|
| `wa-global-cluster-alloc-final-v1_3-20260811.json` | **FINAL** allocation of all 1,612 unallocated strongs |
| `wa-global-t3-cluster-record-v1_0-20260811.json` | new **T3 "Operations"** cluster record to add |
| `wa-global-prior-reassignments-v1_1-20260811.json` | **218** prior-allocation changes (211 T2/FLAG→T3, 6 generic→T3, 1 recluster) |
| `wa-global-operations-corpus-v1_0-20260811.json` | corpus-wide operations instrument (1,372) |
| `wa-global-generic-op-disposition-v1_0-20260811.json` | 75 generic-verb ops STAY/T3/recluster |
| `wa-global-cluster-alloc-low-review-v1_2-20260811.{md,json}` | LOW semantic dispositions |
| `wa-global-t2-likeness-review-v1_0-20260811.{md,json}` | T2 grouped by likeness + IB-flag |
| `wa-obslog-global-cluster-alloc-v1-20260811.md` | working obslog (full trail) |
| (superseded) `…-high/medium/low-v1_0/1_1/1_2` | tier snapshots retained for provenance |

## 7. Final results

- 1,612 allocated: **T2 522 · T3 291 · IB clusters 790 · FLAG 9.**
- Largest IB clusters: M24 Weakness 52 · M10 Sin 46 · M15 Wisdom 44 · M05 Love 43 · M03 Grief 42 · M06 Hate 39 · M02 Anger 35.
- Prior reassignments: 218 (separate report).

## 8. Next steps

- CC to apply, after researcher review (GR-PROC-004): (1) add T3 cluster record; (2) apply final allocation; (3) apply prior reassignments — each via patch, with confirmation output.
- `review_flag=true`, all `low`, and all descriptor-pull items are the primary review subset.
- Buckets are provisional homes for **verse-level analysis**, which will confirm or refine each assignment (and resolve descriptor/operation pairings automatically).

## 9. Caveat

Evidence was gloss + transliteration + count only. The allocation is an analytical scaffold — a likely bucket for verse-level work — not a final judgement on meaning. Clusters remain a convenience of arrangement, not a claim about the inner-being system.
