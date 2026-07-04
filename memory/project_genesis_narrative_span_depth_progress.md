---
name: project_genesis_narrative_span_depth_progress
description: "ACTIVE WORK (2026-07-04): reading the OT NARRATIVES for the inner being at SPAN DEPTH (verse-first, span-by-span, gate-checked) - the new narrative/passage-driven method. Genesis 1-25 COMPLETE (primeval 15 + Abraham 18 = 33 readings, prose_section 916-948 type 108, 0 non-T2 gaps, 2 syntheses). NEXT: the Jacob cycle, Gen 25:19+."
metadata: 
  node_type: memory
  type: project
  originSessionId: 92aed34e-8a28-44a4-8d9d-4bdf6df70a12
---

**Narrative inner-being reading at span depth** — the method the researcher confirmed 2026-07-04 (span-lexical is the unit not the plot; individual + INTERACTIVE operations; never lump repeated/same-gloss spans, never over-read genealogies; story instrumental). Full method: `verse-analysis/_methodology/wa-ot-narrative-inner-being-method-proposal-20260704.md` + worked example `wa-narrative-method-worked-example-gen3-20260704.md`. Governed by [[feedback_resist_grouping_preserve_distinctions]], [[project_passage_reading_checkback_gate]], [[feedback_each_chapter_first_principles_find_the_gems]].

**Progress (Genesis 1-25 COMPLETE):**
- Primeval Gen 1-11: 15 passages GEN-01..15 (prose_section 916-930), 0 non-T2 gaps, synthesis filed.
- Abraham Gen 12-25:18: 18 passages ABR-01..18 (prose_section 931-948), 0 non-T2 gaps, synthesis filed.
- 33 readings, ~44,200 words, type 108 `lexical_prose_passage`, every reading GATE-checked.
- Genesis text fully backfilled (1533/1533); Jacob chapters (25:19-37) present, NO backfill needed.

**Tooling (reusable, all built/proven this work):**
- Filer: `scripts/_apply_file_passage_lexical_prose_v1_20260704.py --book --unit-code --story --live --no-backup` (one reading per unit_code, type 108).
- Gate (MANDATORY): `scripts/_check_passage_reading_coverage_v1_20260704.py --unit-code=X [--story=path]`.
- Segmentation loader: `scripts/_apply_load_segmentation_v1_20260703.py --in <json> --live` (idempotent per provenance).
- Backfill (if a book lacks context verses): `scripts/_apply_backfill_chapter_verses_v1_20260702.py --book --chapter --live --no-backup`.

**NEXT (resume here):** the **Jacob cycle, Gen 25:19-35:29** (+ Gen 36 Esau's line thin). Workflow: cast passages by operation-web -> segmentation JSON (provenance `genesis-jacob-v1-<date>`) -> load -> verify 0 non-T2 gaps -> read passage-by-passage with the gate -> commit every 2-3 -> synthesis. Watch (let emerge): the supplanter/grasping interior (aqav) vs transformation (Jacob->Israel, Peniel); blessing GRASPED (vs Abraham's RECEIVED); deceiver deceived; Bethel's vow; "I will not let you go unless you bless me". Full resumption guide: `verse-analysis/_reports/wa-session-log-20260704-genesis-narrative-span-depth.md`.

**Related open loop:** [[project_prophets_wisdom_read_at_movement_depth_debt]] - the poetic/prophetic chapter readings need an additive span-depth pass later (parked).
