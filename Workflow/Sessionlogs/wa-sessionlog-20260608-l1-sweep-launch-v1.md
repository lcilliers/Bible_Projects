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

## Next (this session / next)

- **Read-only angle layers A–F** across all clusters → the **cross-cluster roll-up** (qualifier map ·
  cross-cluster co-occurrence matrix · shared-term/homonym index · scenario-type distribution).
- Read the roll-up together → decide the synthesis/synergy frame.

## Key memories written

`feedback_l1_l2_is_multi_angle_report_then_synthesise` · `project_all_clusters_l1_sweep_first` ·
`project_p2_l2_decision_architecture` · `feedback_keyword_digestion_methodology` ·
`feedback_qualifier_routes_per_verse_occurrence` · `feedback_l1_must_be_verse_aware`.
