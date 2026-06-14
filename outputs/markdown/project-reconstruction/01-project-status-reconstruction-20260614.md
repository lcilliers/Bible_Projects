# Project Status — reconstructed from the written record (ascending date order)

> Reconstructed 2026-06-14 from the project's own dated documents (manifest-driven, read oldest→newest). Every claim is cited to a source file. This **supersedes** the drifted summaries in CLAUDE.md (last refresh 2026-04-27) and the memory index. Where the record is silent, it says `[GAP]`.
>
> Companion files: `02-failures-oversights-rework-log-20260614.md` (the failure history) · `03-table-data-relevancy-map-20260614.md` (which tables/data are live, stale-relevant, or dead) · `00-spine-index-ascending-20260614.md` (the 523-doc reading list).

---

## The arc in one paragraph

The project began (March) as a **per-word STEP-extraction engine** producing JSON + analysis for ~214 inner-life words. It grew a **Verse-Context** stage (classify verses per term) and a **dimension-review** layer (April), then a heavy **per-word Session B/C/D** analytical pipeline. Through April–May the organising principle was found to **miscut the data three times over** — first registry, then dimension, then term-similarity clustering — driving a **pivot to a cluster + characteristic + finding model** (M-codes, May). May's v3_0 pipeline collapsed 14 phases to 6 and made the **finding** the unit. In June the team discovered the per-word analysis itself was unreliable and re-architected to an **L1/L2 "verse-read = meaning"** model where each verse is read once and emits ~14 tier findings per term — then traced a **4-month rework loop to a single tool defect** (the meaning paragraph duplicating the dimensions then fabricating), and adopted a **dimensions-primary, meaning-derived, column-wise** correction. A **catastrophic DB loss (2026-06-03)** cost ~6 weeks. The programme is now **accumulating verse-meaning across clusters before any synthesis/distillation**.

---

## March 2026 — foundations (schema → engine → STEP → first extractions)

- **Schema** climbed v2.2 → **v3.8.0** across ~10 migrations; added engine-control tables (`engine_run_log`, `word_run_state`, `term_fetch_log`, `schema_version`, `engine_stream_checkpoint`) and span-filter columns (`target_word`, `span_strong_match`, `context_before/after`). (session-2026-03-18-engine-build.md — "All 10 schema migrations (M01–M10) applied…v2.2 to v3.0.0"; WA-SessionLog-Final-v1-20260330.md — "Schema v3.8.0")
- **Session A engine** (v9, 16 modules) signed off 2026-03-18 with three modes (NEW_WORD, AUDIT_WORD, GAP_FILL); multi-part logic removed as a context-window artefact; **span-based verse filtering** (store only verses where the Strong's appears in a STEP `<span>`). (Session-A-v9-Architecture-v4-Final-20260318.md)
- **STEP API** reverse-engineered (localhost:8989); critical discovery that `meanings={word}` semantic search finds terms literal text-search misses (e.g. H2734 anger). (session-2026-03-17-step-api-exploration.md; session-2026-03-24…md)
- **Pivot to pool-based simultaneous analysis** + a new **Verse-Context** stage to cut verse-reading volume (classify ANCHOR/RELATED/SET_ASIDE per term); Session D's inter-word work pulled forward into Session B. (WA-SessionLog-VerseContextDesign-v3-20260329.md)
- **End-of-March state:** ~34/181 registries Phase-1 complete; ~3,807 active terms; ~85k verses; VCB-001..005 applied (12,436 verse_context rows). `[GAP]` whether those VCB batches were a prototype or production. (wa-programme-status-report-20260331-eod.md)

## April 2026 — verse context complete, dimension review, governance repair

- **Verse Context complete for all 181 active registries** by mid-April; 3,469 contextual meaning groups across 22 clusters **C01–C22**. (WA-SessionLog-20260405-20260408.md)
- **Dimension Review** ran on the C-clusters; 10-dimension vocabulary locked; "verse-first, data-derived, never preset" principle. ~40% of groups unclassified at one point (KEYWORD_WEAK unreliable). (WA-SessionLog-20260409.md; wa-dimension-report-20260406.md)
- **Grouping model corrected** term-centric → **characteristic-perspective** (2026-04-08); ~3,300 earlier groups left un-retrofitted. (WA-SessionLog-DimReview-Instruction-Review-v1-2026-04-09.md)
- **Schema → v3.10.0**; observation-question catalogue created (`wa_obs_question_catalogue`, 194 Qs) + `wa_finding_catalogue_links`; flag tables brought into governance (6 directives, 2026-04-15); `wa_finding_entity_links` created. (wa-global-dir-20260416-001-schema-catalogue-v1-20260416.md; wa-session-log-20260415-flag-remediation.md)
- **Session B redesign** exposed as procedurally fragile (Step 1.2 rewrite; fellowship Stage 2a failed on 9 counts) → **Task 7 Governing Principle**: depth unrationed, procedural choice removed. (wa-062-fellowship-review-tasks-v4-20260417.md)
- **DB-wide review** (2026-04-19) fixed an XREF join bug that had inflated findings 14,284→7,411 (−48%); raised OT-DBR-009 (mti_terms dup). **Reference-as-DB** migration (M32) moved 5 vocabularies into the DB as single source of truth. (wa-global-databasereview-sessionlog-v1.4-20260419.md; ref-migration-m32-doc-sweep-20260420.md)
- **End-of-April state:** schema v3.10.0; all registries scored on readiness v2 (5 BANKED, 17 near-clean, 154 needing work); tier framework T1–T7 finalised (T2 constitutional-location major revision). (WA-tier-framework-definitions-v1_2-2026-04-29.md)

## May 2026 — the cluster/characteristic/finding pivot (the decisive month)

- **2026-05-04 — three things dropped at once:** registry as grouping driver (dominance only 50.6%), **dimension review entirely** ("created noise, built on wrong assumptions"), and VCGs as a clustering input. Replaced by **term-similarity clustering** → 88 leaf clusters → **45 thematic M-clusters** (M01 Fear … M46). (wa-sessionlog-term-anchor-reset-v1-20260504.md)
- **Characteristic model added** (schema M42–M52 / ~v3.27): new tables `characteristic`, `characteristic_subgroup`, `cluster_observation`, plus `cluster_subgroup`, `mti_term_subgroup`, `vcg_term`. Hierarchy: **Cluster → Characteristic(s) → Sub-group(s) → VCG(s) → Verses**. (WA-characteristic-and-observation-schema-proposal-v1-20260518.md; WA-structural-terms-clarification-v1-20260518.md)
- **2026-05-17 — scope-bias correction:** inner-being = the *whole* human inner life (no spiritualisation filter); BOUNDARY-pending ruled an invalid resolution; cross-cluster co-occurrence must be assessed *before* routing. M01–M03 declared only "transitionally closed." (wa-sessionlog-20260517-methodology-pivot-end-of-session-v1.md)
- **2026-05-26 — the "Type 1/2/3 cluster" insight:** M11 parked because term-similarity clustering scatters a characteristic's "legs" across clusters; raises the open question whether the inner being is too integrated to force into structures. (wa-sessionlog-20260526-cluster-architecture-question-v1.md)
- **2026-05-27 — v3_0 pipeline frozen:** 14 phases → **6 (A–F)**; two governing principles (GP-1 verse-meaning rules all analytics; GP-2 record every observation, no bias-screening). **Session C retired** (re-read verse corpus 7×); Phase E authors prose from the **`cluster_finding`** table; publication = CC assembly from `prose_section`. (wa-sessionb-cluster-instruction-v3_0-20260527.md; wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md)
- **End-of-May state:** schema ~v3.28; 8 clusters fully closed; M10c done; M11/M38 structurally ready/parked; M04 paused; first v3_0 test (M38) produced sound findings but poor prose + 177 hygiene items. (wa-v3_0-final-review-v1-20260527.md; wa-v3_0-refinement-0-index-v1-20260529.md)

## June 2026 — verse-read = meaning, DB loss, root-cause diagnosis (current)

- **2026-06-03 — DATABASE LOSS:** live DB truncated to 0 bytes (Drive sync corruption); recovered to a **2026-05-28** copy → ~6 weeks of work lost, June 1–2 handler work unrecoverable. Project moved off Drive to `C:\Bible_study_projects` with NAS + git backups. (wa-db-loss-incident-20260603.md; wa-db-recovery-assessment-20260603.md; CLAUDE.md §13)
- **2026-06-04 — foundations reset:** the prior "remediation/audit-to-zero" frame declared the *wrong* frame; study re-grounded on (a) focus = vocabulary + inner life + relationships, (b) raw-data completeness inventory (science extracts noted as a gap), (c) verse-meaning rules all analytics / every finding anchored / no guessing, (d) end point. (wa-study-foundations.md)
- **2026-06-07 — V3_2 redesign:** old manual L1/L2 (VCG + sub-group iteration) abandoned (~40 days/cluster, cascading rework). New **L1–L8 rollup** design; `wa-cluster-rollup-design.md` is the authoritative spec. (wa-cluster-rollup-design.md)
- **2026-06-08/09 — L1/L2 "verse-read = meaning" goes live:** morph backfilled 100% (all 46 clusters); **L2 reads each verse once and emits ~14 tier findings per in-scope term (`l2_api`) + a meaning paragraph (`l2_meaning`)**, routed to each term's cluster; Sonnet 4.6, engine-logged, resumable. **M01 (Fear) and M15 (Wisdom) 100% complete.** (wa-sessionlog-20260609-verse-read-meaning-M01-M15-v1.md; memory project_l2_verse_read_meaning_live)
- **2026-06-10/11 — root-cause diagnosis + correction:** the 4-month rework loop traced to a **tool defect** — the meaning paragraph duplicated the 14 dimensions then fabricated, and the audit only checked field→paragraph. Fix: **dimensions PRIMARY (disciplined, option-list, silence-valid, column-wise) / meaning DERIVED (cannot invent)**; tier catalogue restructured to **two layers** (15 VE fields rolling up into SYNTH); 189 old T-questions dispositioned (16 DROP soft-deleted). (wa-sessionlog-20260611-ve-exploration-and-meaning-diagnosis-v1.md; wa-tier-catalogue-restructured-v2-20260611.md)
- **M47 "Constitution" cluster** created (2026-06-10): the inner-being seats/faculties (heart, soul, spirit, mind, flesh, conscience); "exactly where a single mechanical lexical sense is meaningless and the read matters most." (memory project_constitution_cluster_and_flag_resolution)

### Current state (2026-06-14)

| Dimension | State |
|---|---|
| **Live schema** | **3.31.0** (2026-06-10) — *not* the v3.11/v3.17 in CLAUDE.md |
| **Organising model** | Cluster (M-codes, `cluster` table, 49) → Characteristic (128) → Sub-group (175) → VCG → Verse; **finding** is the unit |
| **Live pipeline** | L1 (mechanical) + **L2 verse-read = meaning** (API); L3–L8 synthesis/distillation **parked** until more clusters accumulate |
| **Findings** | `finding` 343,434 (L2 verse-read store, written to 2026-06-10); `cluster_finding` 19,996 (catalogue-prompted, to 2026-06-11) |
| **Clusters done** | M01 + M15 verse-read 100%; ~13 "Analysis Completed"; M02–M46 in progress; 30 not-started but morph-backfilled |
| **Registry** | 215 rows; **lexical entry point + C-code dimension-review anchor**, now scaffolding under the M-code cluster model (both coexist) |
| **Active standing risks** | OT-DBR-009 mti_terms dedup (unfixed); science extracts not in DB; volume-vs-value of per-verse findings; publication parked |

> Key correction to CLAUDE.md: it still presents `word_registry` as "*the* 214-word anchor" and omits the `finding`/`cluster`/`characteristic` architecture entirely. The live primary object is the **finding** (typed term-in-verse); the registry is the lexical entry point and the C-code (dimension-review) anchor — a *parallel* live layer to the M-code clusters, not a dead one.
