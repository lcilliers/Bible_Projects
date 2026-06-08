# Session log — 2026-06-08 · L1 sweep launch (prototyping → all-clusters strategy)

> CC session log. Continues the V3_2 re-prototyping. Outcome: prototypes validated, L1/L2 architecture
> settled, and the strategy set to sweep **all 46 clusters through L1** before any synthesis.

## What happened

1. **T2 cleanup items 1–2 applied.** 106 never-co-occur Parked terms soft-deleted (reversible); T2 now
   **480 active** (those that co-occur with a characteristic — held for L2 disposition). §A characteristics
   already moved. `scripts/_apply_t2_soft_delete.py`.
2. **P2/L2 decision design** (`_assess_p2_verse_scenarios.py`, M01): 6-scenario taxonomy S0–S6; pure-L1
   settles only ~4%; **74% of verses are COMPOUND** → architecture is **type → modules → synthesise**, not
   three disjoint passes. Researcher agreed §6.1–6.3; §6.4 (qualifier span-attach) to be tested.
3. **Prototypes (read-only, all validated):**
   - **Morph backfill viable** — STEP HTML carries `morph=` per span; **100% coverage** on M01; Hebrew verb
     stems decode (ya.re Qal/Niphal/Piel). `_prototype_step_morph.py`.
   - **Meaning run** — morph→sense bridge is a parse of the BDB `(Qal)/(Niphal)/(Piel)` markers in
     `sense_text`. Morph resolves the **stem axis** (194/194 ya.re) but **not the within-stem shade**
     (fear↔reverence) → 190/194 shade-residue → L2. `_prototype_meaning_run.py`.
   - **P1 keywords** — whole-word + self-check, **85/85 PASS**; fixed book-abbrev leakage; flagged
     concatenation artifacts. `_prototype_p1_keywords.py`.
4. **Keyword-digestion methodology** — overlap→sub-group seeds · divergence→role flags · size→polysemy.
5. **L1/L2 architecture** — multi-angle **report-per-angle → review → synthesise → DB**; angles never write,
   synthesis is the only writer; iteration designed-in.
6. **Strategy: sweep ALL 46 clusters through L1 first** (researcher conviction; reframed to hold L2 synthesis
   until the cross-cluster roll-up is read, to avoid paying twice). In **batches and layers with review
   points** to guard against systemic failures.

## Launch scaffolding (this entry)

- **Backup:** `backups/bible_research_pre_l1_sweep_20260608.db`.
- **Fallback/rollback doc:** `research/investigations/wa-l1-sweep-prelaunch-state-and-rollback-v1-20260608.md`.
- **Matching key confirmed:** `wa_verse_records.reference` (e.g. `"Gen 43:32"`) == STEP `ref` → backfill
  matches on `(mti_term_id, reference)`.

## L0 morph backfill — COMPLETE (all 46 clusters)

`scripts/_apply_morph_backfill.py`, matched on `(mti_term_id, reference)`. Run in 4 batches with a
DB-side-coverage review point between each:
- Batch 1 M01: 1044/1044 · Batch 2 M02–M15: 12509/12512 · Batch 3 M16–M31: 10889/10891 ·
  Batch 4 M33–M46: 6664/6665.
- **Full corpus: 31106/31112 verse-rows (100.0%) carry morph.** 6 rows unmatched corpus-wide (negligible).
- Stem distribution (verbs): Qal 7168 · Hiphil 1816 · Piel 1694 · Niphal 870 · Hithpael 321 · Pual 81 ·
  Hophal 34. Two rare stems mapped after first pass (Tiphil ×3, Polpal ×2) — stem map fixed in all three
  scripts; the 5 rows corrected. 0 unmapped stems remain.

The sweep's **only structural write is done.** Everything from here (layers A–F) is read-only until synthesis.

## Full-day arc (after L0)

3. **Cross-cluster roll-up (read-only angles 1–5 + correlation).** 44% of verses cross-cluster; every cluster
   touches 40–45/45. Correlating co-occurrence (contextual) × keyword-Jaccard (semantic) → **three link
   classes**: SAME-ish (merge) · **RELATIONAL** (co-occur but differ — most strong links, e.g. Life↔Relational
   211/0.03; Sin→Repentance) · KIN (kin, rarely meet). Strength = connective backbone.
4. **Ontology reframe (governing).** The **cluster is not the real object**; the unit is **THING_A[type]
   —relationship[effect]→ THING_B[type]**, verse-anchored; the **differential of impact** is the prize. Things
   have **types** (status/action/quality, readable from morph). Evidence: Sin(status)←atonement(action);
   Fear×Strength one link → evocation/opposition/response.
5. **Corpus keyword map** (preliminary → typed + glue-filtered): 1660 terms, type dist STATUS 46/ACTION 34/
   QUALITY 18; type signatures read distinctly. **Registry grounding** diagnostic: ~86% of anchors grounded
   (lexical or cognate-synonym); ~26 genuinely termless (modern abstractions); 4 duplicate registry rows.
6. **Inner-man systems model** mapped to the data (morph **stem = "method A"**; produces/lacks/transitions =
   the typed edges). **Web analysis strategy:** the raw web is near-complete → **cover verses, don't chase
   edges**; the unit is the **verse** (*a finding for every verse*); cluster = entry-batch not boundary;
   meaningful-absence (KIN-not-met) read against coverage.
7. **Method checkpoint:** the L1 work does NOT point to a different approach — **build on V3_2, it evolves**;
   primary output moves to the **typed-relationship finding per verse**; cluster → work-batch + roll-up;
   relationship layer central. Open: do L2 sub-groups/L6 characteristic stay or become roll-ups — prove on Fear.
8. **First M01 verse-read (batch 1, 14 verses, read-only).** The typed-relationship finding **works**:
   differential live (Deu28:66 assurance-absent→dread vs Isa12:2 trust-present→no-fear); fear↔reverence shade
   resolved at the read; **sub-groups fell out as roll-ups, not imposed** (passes the checkpoint test).
9. **Scaling design proposal** (`wa-scaling-design-and-layers-v1`): **collapse VCG + pre-sub-group into
   roll-ups** (verse→finding→roll-up); pipeline **assemble(CC)→read(AI chat)→apply(CC)→roll-up(CC)**,
   term-batched, cross-cluster de-dup; minimal finding schema; **D1–D5 decisions** for markup.

## State at end of day

- DB: schema 3.29.0; **morph backfilled 100%** (31106/31112 rows); T2 480 active; **no analytical writes** —
  all afternoon work is read-only reports. All pushed (last commit `4f6b93a`).
- Backups: `bible_research_pre_l1_sweep_20260608.db` + NAS daily.

## Next (morning)

- Researcher to re-read `wa-scaling-design-and-layers-v1-20260608.md` and **mark up D1–D5**.
- **CC recommendation: validate on the hard case before building** — run the **`ya.re` slice (194 verses,
  multi-sense, cross-cluster-heavy)** to confirm the layer-collapse + finding format survive; *then* build the
  evolved pipeline (finding schema migration → assemble → chat-read → apply → roll-up).

## Key memories written

`feedback_l1_l2_is_multi_angle_report_then_synthesise` · `project_all_clusters_l1_sweep_first` ·
`project_p2_l2_decision_architecture` · `feedback_keyword_digestion_methodology` ·
`feedback_qualifier_routes_per_verse_occurrence` · `feedback_l1_must_be_verse_aware`.
