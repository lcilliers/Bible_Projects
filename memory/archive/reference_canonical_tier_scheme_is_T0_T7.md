---
name: reference-canonical-tier-scheme-is-t0-t7
description: "Canonical tier scheme = DB T0-T7 (per 2026-06-11 restructure); the T1-T8 framework doc (v1_2, 2026-04-29) is SUPERSEDED"
metadata: 
  node_type: memory
  type: reference
  originSessionId: d51a2ae4-3564-40b3-84fd-2dc7fed902d8
---

REFERENCE (2026-06-17; refit applied 2026-06-19): the **canonical tier scheme is T0–T7**, held in `wa_obs_question_catalogue`. **Active count is now 126** (was 173) after the **v2_1 de-bias refit applied 2026-06-19** — 126 keep-codes rewritten + 47 obsolete soft-deleted (folded into a named primary; fold target in `review_note`; per-tier 9/18/6/33/18/9/13/20, T2 consolidated 28→6). No renumber, no hard delete. T0 Divine Image · T1 Definition · T2 Constitutional Location · T3 Inner Faculties · T4 Relational Interfaces · T5 Formative/Developmental · T6 Structural Relationships · T7 Evidential Foundation. `ve_lexical.related_tier` and the engine VE_MAP also use T0–T7. Refit mechanism: `apply_session_patch.py` now has an `update` handler for this table; regen-from-doc builder = `scripts/build_tier_catalogue_update_patch_20260619.py`.

**SUPERSEDED:** `WA-tier-framework-definitions-v1_2-2026-04-29.md` (T1–T8, no T0) — pre-restructure. Do NOT treat as current. Crosswalk old→new: T1→T1, T2→T2, T3→T3, T5→T4, T6→T5, T7→T6, T8→T7, and DB adds T0.

**Watch:** the M01-c1 analysis used the superseded T1–T8 labels — content sound, tier numbers must be remapped to T0–T7 before reconciling to the DB. The two-layer VE/SYNTH refit (VE-01..17) is approved-in-principle but NOT yet in the DB.

**Canonical docs (Workflow/Tiers/):** current state = `WA-tier-catalogue-current-state-v2-20260619.md` (generated from DB post-refit; regen `python scripts/export_tier_catalogue.py --md --version vN --asof YYYY-MM-DD`; v1-20260617 archived); refit instruction = `wa-tier-catalogue-cc-update-v1_0-20260619.md` + companion `wa-tier-catalogue-rewrite-v2_1-20260619.md`; pending design = `wa-tier-catalogue-restructured-v2-20260611.md` (VE/SYNTH, not in DB). Everything else (incl. the v1_2 T1–T8 framework) archived. Related: [[feedback_source_of_truth_is_written_record]], [[feedback_filing_is_first_class_governance]].
