---
name: project_l1l2_field_reliability_direction
description: "ACTIVE direction (2026-06-14) - L1/L2 verse meaning = 14 mechanically-derived fields that COMPOSE a templated, traceable meaning sentence; sense is mostly mechanical"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8a5e10ea-2d9d-4bb9-8ca3-fb979500309e
---

ACTIVE working direction (2026-06-14) — the resolution of the L1/L2 "verse-read = meaning" impasse. Canonical design: `research/investigations/wa-l1l2-field-reliability-measures-v1-20260614.md` (§1a–1f). Session log: `Workflow/Sessionlogs/wa-sessionlog-20260614-l1l2-field-reliability-and-morph-backfill-v1.md`.

**The fix to the impasse:** stop narrating meaning (un-traceable). Instead DERIVE the 14 verse-fields mechanically, each as a traceable finding, then COMPOSE a templated sentence from them → meaning is back-trackable by construction and searchable. The sentence is a deterministic VIEW of findings, not a new artefact. Supersedes/refines [[project_meaning_duplicates_then_fabricates]].

**Reliability strata** — fields are mechanical to differing degrees, with 3 terminal states each: **resolved** · **indeterminate** (verse genuinely unclear = a real finding) · **pending** (`UNRESOLVED` = backtrack worklist, distinct from `NONE`).
- **Mode (#4) = bedrock** — the morph, parsed (Hebrew stem = the operative mode). Per-occurrence + mechanical. DONE assessing.
- **Sense (#1) = mostly mechanical** — 79% of occ are mono-sense (1 STEP subgloss → assign it); poly-sense use STEP's **per-occurrence subgloss** (a field-lookup, not a read — *nephesh* splits 9 ways per verse). Only the coarse-ceiling residue (*pneuma* "spirit" = Holy-Spirit+human+wind) needs a signal-rule or read. **Impasse correction: the old "pneuma=wind/breath for all 312" used the term UNIFORM GLOSS, not STEP's per-occurrence subgloss.**
- **5 signal-driven fields** (location/origin/faculty/attributed-to-God/relational) need a signal-LIST (vocabulary) + signal-RULES (decision logic) + states. See [[feedback_characteristic_is_typed_term_in_verse]].

**Traceability chain (proven live):** `wa_verse_records.id` → `verse_context.verse_record_id` (FK) → `finding.verse_context_id`. Morph/subgloss are SOURCE columns; mode/sense FINDINGS are emitted from + cite them (keeps "all analysis in findings" true — [[feedback_all_study_work_in_db]]).

**Morph backfill DONE 2026-06-14:** the gap was programme-wide (69 content terms across 14 clusters + all T2, root = created after the 06-08 batches), now closed via `_apply_morph_backfill.py` (+40,697 rows; 69→0 fully-unmorphed). `verse_context.sense_id` still NULL everywhere (`step_meaning_applied` is the populated sense source).

**Tomorrow's sequence (researcher-set):** sense → type → refine the 5 signal-lists → solve fields 9–12 (purpose/typology/response/produces) → #14 literary falls away for verse work → templated narration last.
