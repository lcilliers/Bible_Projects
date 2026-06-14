# Failures, Oversights & Reasons-for-Rework — full log

> Reconstructed 2026-06-14 from the project's own dated written record (session logs, methodology notes, design docs), read in ascending date order. Every entry carries a citation `(filename — "quoted phrase")`. Items marked `[GAP]`/`[UNCERTAIN]`/`[INFERRED]` were flagged as such by the reader because the record is silent or ambiguous — they are **not** asserted as fact.
>
> Source method: manifest-driven (database/file_manifest.json, rebuilt 2026-06-14, 7,448 files), narrative spine = 325 high-signal docs under `Logs/`, `Workflow/Sessionlogs/`, `Workflow/methodology/`, `Workflow/Programme/`, `Workflow/Instructions/`, `docs/`, `outputs/`.
>
> **Why this log exists (researcher direction):** the project's summary docs (CLAUDE.md, memory) drifted from reality; the failure/rework history is the evidence of *why* the architecture is shaped as it is. "There are many" — confirmed: ~55 distinct items below.

---

## How to read the pattern

The recurring failure modes, in the researcher's own record:
1. **Drift between "decision made" and "instruction/schema updated"** — "The gap between 'decisions made' and 'instructions updated' is where pipeline failures live" (WA-SessionLog-Final-v1-20260330.md).
2. **AI as sole quality gate** — "I cannot be relied upon as the sole quality safeguard" (2026-03-15); fabricated registry numbers, false compliance claims.
3. **Procedural discretion → drift** — discretionary instruction language let sessions skip steps (fellowship Stage 2a, 9 defects).
4. **Imposed structure miscutting an integrated subject** — registry-driven, then dimension-driven, then term-driven clustering each found to miscut the data.
5. **Forcing early decisions on ambiguous verses** — L1 locking senses too early; the meaning-duplicates-then-fabricates loop.
6. **Infrastructure fragility** — schema re-migrations, duplicate `mti_terms`, and the catastrophic 2026-06-03 DB loss.

---

## 2026-03 (Foundations)

| Date | What went wrong | Why / reason for rework | Citation |
|---|---|---|---|
| 2026-03-05/07 | Phase 1 instructions executed against drifted v4 spec (multi-part word handling) | Multi-part logic was a "context-window artefact" with no real application; removed entirely in Session A v9 | (Framework-B-SessionLog-2026-03-07.md — "Multi-part logic removed entirely…context-window artefact") |
| 2026-03-07 | Session C (full verse-context extraction) abandoned mid-design | Large production burden, required array never populated, duplicated Session B, bundling rule blocked the useful cross-context analysis | (Framework-B-SessionLog-2026-03-07.md — "Session C is retired from Phase 1 workflow") |
| 2026-03-15 | MTI `also_used_in` / `owning_part` format inconsistency (56 dict vs 34 string; 4 formats) | "Format drift occurred across sessions" without checking existing format | (WA-Programme-Session-Log-2026-03-15-evening.md — "also_used_in format inconsistency") |
| 2026-03-15 | JSON schema drift across 26+ files (3 incompatible generations); only 1 of 8 audited clean | Obsolete field names (`somatic_dimension` etc.); files un-queryable together | (WA-Programme-Session-Log-2026-03-15-evening.md — "Only 1 of 8 files audited was fully clean") |
| 2026-03-15 | MTI metadata stale (total_terms 604 vs actual 629); missing registries; duplicate/unresolved Strong's | Referential errors not flagged proactively | (WA-Programme-Session-Log-2026-03-15-evening.md — "mti_meta.total_terms stale") |
| 2026-03-15 | **AI sole-quality-gate failure acknowledged** | "introduced MTI format inconsistencies without flagging; returned incomplete verse search…fabricated registry numbers from memory; produced peace file in non-standard structure while claiming v7 compliance" | (WA-Programme-Session-Log-2026-03-15-evening.md — "I cannot be relied upon as the sole quality safeguard") |
| 2026-03-22 | `audit_word.py` not treating STEP as master (COALESCE guards; no orphan delete) | Complete redesign to STEP-master, two-phase dry-run+apply | (session-2026-03-22…md — "Original audit_word.py used COALESCE guards that prevented STEP data from overwriting") |
| 2026-03-22 | 7 critical engine bugs after schema 3.2.0 (incl. WAL-on-every-connection corruption risk) | Migration broke INSERT column lists, version constant, zfill | (session-2026-03-22…md — "Fixes 1–7") |
| 2026-03-23 | Soul (r182) AUDIT_WORD crashed mid-run | Recovered from artefacts; term expansion 4→11; no data loss | (session-2026-03-23-soul-audit-recovery.md — "Recovered after crash") |
| 2026-03-23/24 | H2734 (anger, 91 occ) entirely missed by `text=+anger` search | ESV never renders it "anger"; required pivot to `meanings=` semantic endpoint | (session-2026-03-24-claude-code-first-session.md — "H2734: Now classified as G1m") |
| 2026-03-25 | Duplicate `mti_terms` rows (H4172B fear; G0150 shame) triggering WR-15 STOP | No uniqueness constraint on strongs+registry | (session-2026-03-25…md — "WR-15 duplicate H4172B in mti_terms") |
| 2026-03-25 | **A8 destructive reset deleting researcher flags** (data-loss bug) | Unconditional DELETE on all quality flags; scoped to DATA_COVERAGE only | (session-2026-03-25…md — "Changed DELETE to scope by flag_group = 'DATA_COVERAGE' only") |
| 2026-03-25 | RESTORE step missing — re-included terms left `delete_flagged` | A6 never cleared the flag on terms returning to include list | (session-2026-03-25…md — "Added RESTORE step in A6") |
| 2026-03-27 | Instruction/schema coupling error (Task 8 fields referenced before schema applied) | Extraction blocked until v3.7.0 | (WA-SessionLog-ExtractionDesign-v1.1-20260327.md — "Wait for Claude Code confirmation of Task 8") |
| 2026-03-30 | 42 instruction-register gaps discovered on the final day of the month | "The gap between 'decisions made' and 'instructions updated' is where pipeline failures live" | (WA-SessionLog-Final-v1-20260330.md — "All 42 gaps in the instruction register are closed") |
| 2026-03-31 | `[GAP]` VCB-001–005 batches: status report claims applied, design logs describe VC as not-yet-begun | Execution logs absent; cannot confirm whether prototype or proposal | (wa-programme-status-report-20260331-eod.md vs WA-SessionLog-Final-v1-20260330.md) |

## 2026-04 (Dimension review, Session B redesign, governance repair)

| Date | What went wrong | Why / reason for rework | Citation |
|---|---|---|---|
| 2026-04-05 | **H3820A lev (heart anchor) wrongly `status=delete`**; r183 completed VC without its anchor term | Bulk delete-cleanup hit a term whose own note said "must be extracted as the registry's anchor"; VCB-032 repair restored 331 verses | (WA-SessionLog-DimReview-Instruction-Review-v1-2026-04-09.md — "H3820A lev…incorrectly at status=delete") |
| 2026-04-06 | Dimension index: 40% of groups unclassified; KEYWORD_WEAK 31% unreliable | Broad keyword matches unreliable; flagged for review | (wa-dimension-report-20260406.md — "Unclassified 1,382 (40%)") |
| 2026-04-08 | **Grouping model wrong: term-centric → characteristic-perspective** | Groups described "what the term does" not "what the verse is about"; ~3,300 pre-VCB-032 groups left un-retrofitted | (WA-SessionLog-DimReview-Instruction-Review-v1-2026-04-09.md — "revised from term-centric to characteristic-perspective") |
| 2026-04-09 | **C21 dimension patch corrupted wrong IDs** (would hit C06/C08/C10/C13/C15); DB restored from backup | Sequential-ID assumption wrong after instruction version bump | (WA-SessionLog-20260409.md — "Would have corrupted C06, C08, C10, C13, C15. Database restored from backup") |
| 2026-04-09 | H2603B phantom grace term (0 genuine occurrences) | Gloss "be loathsome" inconsistent; all verses resolved to H2603A | (WA-SessionLog-SessionB-SessionD-Design-2026-04-09.md — "Identified as phantom entry") |
| 2026-04-09 | Session B v3 architecture mismatch (pool-based v5.x vs per-word v3); 2 clarifying Qs deferred | "segments" methodology + dimensions-provision-Session-D opaque; blocked v5.0 draft | (WA-SessionLog-SessionB-SessionD-Design-2026-04-09.md — "researcher indicated they would answer later") |
| 2026-04-09 | Session B v3 has no flag code for Session D observations | Patch used PH2_CROSS_REF_ENRICHMENT vs old SD_POINTER requirement | (WA-SessionLog-SessionB-SessionD-Design-2026-04-09.md — "This is a gap in Session B v3") |
| 2026-04-13 | Compassion (r023) word study: 16 substantive errors + 1 false positive catalogued | Wrong verse counts, mis-stated Ezekiel first-person claims, etc.; patch staged, schema not live | (wa-023-compassion-audit-patch-v1-2026-04-13.md — "17 items from compassion audit") |
| 2026-04-14/15 | **Flag-table infrastructure out of governance** (1 of 16 codes referenced; 4 purposes mixed) | Blocked Session B/C/D instructions; 6-directive remediation | (wa-global-flagtable-remediation-plan-v1.0-20260414.md — "out of governance") |
| 2026-04-15 | 19 `VOLUME_LIMITATION` rows non-canonical; `finding_type` mixed-case (24 rows) | Naming drift normalised to PH2_/UPPER_SNAKE_CASE | (wa-session-log-20260415-flag-remediation.md — "updated from 'VOLUME_LIMITATION' to 'PH2_VOLUME_LIMITATION'") |
| 2026-04-14 | Instruction documentation debt: 11 global rules duplicated across instructions; stale version refs | No unified global-rules reference; v2 drafted (22→31 rules) | (wa-global-rules-audit-session-log-v1-2026-04-14.md) |
| 2026-04-16 | **Session B Stage 1 Step 1.2 substantively broken — full rewrite** | Incoherent Phase-2 deferrals; no terms-of-reference for "correct"; incomplete field coverage | (wa-global-sessionlog-sessionb-redesign-v2-20260416.md — "significant rewrite of Step 1.2, not incremental correction") |
| 2026-04-16 | Fellowship (r062) Trigger 3: 4 terms have verses but no groups | All verses set-aside (tabernacle vocab); Stage 1 blocked | (wa-062-fellowship-sessionb-sessionlog-v1-20260416.md — "Trigger 3 FIRED") |
| 2026-04-16 | Analysis Output dry-run found 10 instruction gaps (IG-1..10) | No fast-paths/guidance for NULL LSJ, 0 senses, set-aside terms, naming, versioning | (wa-062-fellowship-stage2a-dryrun-v1-20260416.md — "Ten instruction gaps") |
| 2026-04-17 | **Fellowship Stage 2a run failed on 9 distinct defects** (Units 7/8/9 unwritten; cherry-picked Q&A; omitted link inserts; missing required findings; no completion record) | **Procedural drift** — discretionary language let the session decide otherwise | (wa-062-fellowship-review-tasks-v3-20260417.md — "The instruction said something else in each case. The session decided otherwise") |
| 2026-04-17 | Root cause: instruction discretion ("determine/assess/as appropriate") | Task 7 Governing Principle: depth unrationed, procedural choice removed (every step mechanical) | (wa-062-fellowship-review-tasks-v4-20260417.md — "the session made procedural decisions in the moment") |
| 2026-04-19 | **XREF join bug (OT-DBR-010): 7/15 grace findings spurious** (pointed at deprecated duplicate `mti_terms`) | "would have corrupted data if applied blindly"; programme findings 14,284→7,411 (−48%), Path 1 6,398→179 (−97%) | (wa-global-databasereview-sessionlog-v1.4-20260419.md) |
| 2026-04-19 | OT-DBR-009 `mti_terms` duplication (HIGH) raised | Duplicate canonical rows from prior import/migration; **designed but not executed** | (wa-global-databasereview-sessionlog-v1.4-20260419.md — "Raised OT-DBR-009 (mti_terms duplication — HIGH)") |
| 2026-04-19 | `schema_version` table inconsistent (id order ≠ apply order; mixed date formats) | "likely indicates a re-insertion or restore sequence that the schema does not protect against" | (wa-global-databasereview-obslog-v1.4-20260419.md) |
| 2026-04-28/29 | Tier framework T2 (constitutional location) substantially revised | Soul redefined as seat-of-faculties; heart/mind repositioned as soul-subsets; body as design-print | (WA-tier-framework-definitions-v1_2-2026-04-29.md — "T2 substantially revised") |

## 2026-05 (Cluster rework; the big pivots)

| Date | What changed / was found wrong | Why / reason | Citation |
|---|---|---|---|
| 2026-05-04 | **Registry abandoned as grouping driver** | Registry dominance averaged 50.6%; 76/120 clusters cross-cut 3+ registries; "registry was potentially misleading" | (wa-sessionlog-term-anchor-reset-v1-20260504.md — "should we try to group the terms instead") |
| 2026-05-04 | **Dimension review eliminated entirely** | "fundamentally dimensions created noise, built on wrong assumptions" | (wa-sessionlog-term-anchor-reset-v1-20260504.md, 05:59) |
| 2026-05-04 | `verse_context_group` dropped as a clustering **input** | "these groups have shown to be limited and incomplete in value" (retained as output layer only) | (wa-sessionlog-term-anchor-reset-v1-20260504.md, 06:51) |
| 2026-05-17 | **Spiritualisation bias: systematic BOUNDARY over-counting** (M04 had 322 BOUNDARY verses) | Phase-1 prompts (all God-directed) + Phase 3/5 synthesis narrowed inner-being to God-directed; pure-human content parked | (wa-sessionlog-20260517-methodology-pivot-end-of-session-v1.md §(a)) |
| 2026-05-17 | "BOUNDARY-pending" declared an invalid resolution (M01/M02/M03 closed with 39 pending flags) | "Boundary is resolved before completion of the cluster…Merely parked is not a resolve"; M01–M03 only "transitionally closed" | (wa-sessionlog-20260517…v1.md §(c)) |
| 2026-05-17 | Cross-cluster co-occurrence not checked before routing (56% of M04-BOUNDARY co-occur elsewhere) | Whole-term transfers lost cross-characteristic structure; v2_5 §17 adds pre-routing co-occurrence | (wa-sessionlog-20260517…v1.md §(e)) |
| 2026-05-17 | M04 Phase 5 v1 sub-group design **rejected** (largest sub-group 81% > 50% gate) | Boundaries too permissive; v2 redesign → 11 sub-groups, 33.5% largest | (wa-sessionlog-20260526-cluster-architecture-question-v1.md §1.2) |
| 2026-05-26 | **M11 parked — "Type 3" cluster** (characteristic-legs scattered across clusters) | May-04 term-similarity clustering ≠ characteristic neighbourhoods; "no single cluster owns M11's characteristic" | (wa-sessionlog-20260526-cluster-architecture-question-v1.md §2.2–2.4) |
| 2026-05-26 | Deeper open question: is the inner being too integrated/fluid to force into structures? | Strong's sense-splits = 19th-c overlay; Hebrew anthropology holistic; unresolved | (wa-sessionlog-20260526…v1.md §5) |
| 2026-05-26 | v2_9 Phase 8 reduced to **silent soft-delete** of old VCGs | "I am happy with silently marking the old VCGs as redundant…Scale down the phase 8 processes" | (wa-sessionlog-20260526…v1.md §1.2) |
| 2026-05-27 | **Session C found redundant — re-reads verse corpus 7× per cluster** | Re-reads derivative (findings) instead of source; ~40M–200M tokens avoidable; replaced by v3_0 Phase E (reads `cluster_finding`) | (wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md §2.2, §3) |
| 2026-05-29 | First full v3_0 cluster (M38): prose "sentence-by-sentence, not integrated argument"; 177 hygiene items; 12.5h, $9.40 | Pipeline functional but not quality/speed-optimised; 4 refinement areas (exploratory, not adopted) | (wa-v3_0-refinement-0-index-v1-20260529.md) |

## 2026-06 (Verse-read = meaning; DB loss; the root-cause diagnosis)

| Date | What went wrong | Why / reason | Citation |
|---|---|---|---|
| pre-06 (surfaced) | First L1 run flawed by **forcing early decisions** on ambiguous verses | L1 locked multi-sense Hebrew (e.g. ya.re fear/awe/reverence) too early, blocking later discovery | (wa-cluster-rollup-design.md §2 discipline 2; wa-sessionlog-20260608…§3) |
| 2026-06-03 | **DATABASE LOSS — live DB truncated to 0 bytes** | Google Drive sync-corruption; conflict copies + `backups/` (same Drive) also lost | (wa-db-loss-incident-20260603.md) |
| 2026-06-03 | Recovery point = May-28 conflict copy (~6 weeks stale) | Loses May 28–June 2 work (M10c/M10b/M38/M08 closures, handler suite, dedup repair, M20) | (wa-db-recovery-assessment-20260603.md §3) |
| 2026-06-01/02 | Lost handler-based work **cannot be replayed** | June 1–2 work used interactive handlers, not `Sessions/Patches/*.json` | (wa-db-recovery-assessment-20260603.md §3–4) |
| 2026-06-07 | Old L1/L2 (manual VCG + sub-group iteration) **abandoned** | Error-prone, ~40 days/cluster, cascading reworks; V3_2 redesign | (wa-cluster-rollup-design.md preface) |
| 2026-06-08 | L0 morph backfill: 5 stems initially unmapped | Prototype stem-mapping incomplete; fixed across scripts | (wa-sessionlog-20260608…§"L0 morph backfill") |
| 2026-06-09 | L2 self-audit over-flagging (57% then) | Criteria too strict (word-overlap artefacts); real omission ~7% | (wa-sessionlog-20260609…§5) |
| 2026-06-09 | M01 gap verse (Pro 24:21); M15 term chashab 4 verses short | Missing in initial run / transient API error; closed by re-run | (wa-sessionlog-20260609…§6, §8) |
| 2026-06-09 | **OT-DBR-009 re-surfaced** (41 dup term rows, 2,209 dup verse_context, ~5k dup findings) | chesed H2617B 100% subset of H2617A; not blind-fixable (conflicting senses); **not executed** | (wa-sessionlog-20260609…§2) |
| 2026-06-09 | Faculty findings **induced per-cluster** (e.g. boulomai tagged cognition in Wisdom but it's volition) | Faculty must be derived per-term from lexical meaning; 1,734 induced M15 findings removed | (memory feedback_faculty_must_be_per_term_not_per_cluster; wa-sessionlog-20260609…) |
| 2026-06-11 | **Legacy Session B findings peppered with fabricated data** (uniform per-family counts = templated tell) | "review-by-statistics dangerous"; DROP-code findings + underlying Session B findings + 16 catalogue Qs soft-deleted | (wa-sessionlog-20260611…§1; commits f347742, 2d798a3, bb534aa) |
| 2026-06-11 | **ROOT CAUSE of the 4-month loop: meaning paragraph duplicates the 14 dimensions, then fabricates** | System prompt orders meaning to reflect every field; audit checks field→paragraph only, so duplication enforced + extra prose unaudited; each re-read imports different synthesis → re-do | (wa-sessionlog-20260611…§5 "The turning point"; memory project_meaning_duplicates_then_fabricates) |
| 2026-06-11 | Structural fix: reverse primacy (dimensions PRIMARY/disciplined, meaning DERIVED/cannot-invent); column-wise reading | Breaks the variation circle; workflow change not schema change | (wa-sessionlog-20260611…§4–5; memory project_column_wise_ve_hypothesis) |

---

## Standing unresolved items (as of 2026-06-14)

- **OT-DBR-009** `mti_terms` duplication — 41 dupes, 2,209 affected verses; designed (Action R), **not executed** (deemed non-blocking).
- **Science extracts (h)** not yet in the DB — known data-completeness gap (wa-study-foundations.md §b).
- **L3–L8 synthesis / distillation** parked until verse-meaning accumulates across more clusters (`wa-characteristic-distillation-design-v1` on hold).
- **Legacy `l2_mechanical` findings** — 115,946 still active for un-meaninged clusters (superseded only where `l2_api` exists).
- **Publication pipeline** (prose_section, v3_0 Phase E) built but parked.
- **Backup hardening** post-DB-loss — now off-Drive to NAS + git (CLAUDE.md §13), but June 1–2 work remains unrecoverable.
