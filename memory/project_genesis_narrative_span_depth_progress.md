---
name: project_genesis_narrative_span_depth_progress
description: "ACTIVE WORK (2026-07-04): reading the OT NARRATIVES for the inner being at SPAN DEPTH (verse-first, span-by-span, gate-checked) - the new narrative/passage-driven method. GENESIS 1-36 COMPLETE (primeval 15 + Abraham 18 + Jacob 19 = 52 readings, prose_section 916-967 type 108, 0 non-T2 gaps, 3 syntheses). NEXT: the Joseph cycle, Gen 37-50."
metadata: 
  node_type: memory
  type: project
  originSessionId: 92aed34e-8a28-44a4-8d9d-4bdf6df70a12
---

**Narrative inner-being reading at span depth** — the method the researcher confirmed 2026-07-04 (span-lexical is the unit not the plot; individual + INTERACTIVE operations; never lump repeated/same-gloss spans, never over-read genealogies; story instrumental). Full method: `verse-analysis/_methodology/wa-ot-narrative-inner-being-method-proposal-20260704.md` + worked example `wa-narrative-method-worked-example-gen3-20260704.md`. Governed by [[feedback_resist_grouping_preserve_distinctions]], [[project_passage_reading_checkback_gate]], [[feedback_each_chapter_first_principles_find_the_gems]].

**Progress (Genesis 1-36 COMPLETE):**
- Primeval Gen 1-11: 15 passages GEN-01..15 (prose_section 916-930), 0 non-T2 gaps, synthesis filed.
- Abraham Gen 12-25:18: 18 passages ABR-01..18 (prose_section 931-948), 0 non-T2 gaps, synthesis filed.
- Jacob Gen 25:19-36: 19 passages JAC-01..19 (prose_section 949-967, provenance `genesis-jacob-v1-20260704`), 0 non-T2 gaps, synthesis filed. Spine = grasp TRANSFIGURED into faith (Peniel, Jacob->Israel), deceiver deceived, blessing grasped->given-through-brokenness. Gems: JAC-05 (8x barakh theft), JAC-10 (12 birth-namings kept distinct), JAC-15 (Peniel).
- 52 readings, ~77,300 words, type 108 `lexical_prose_passage`, every reading GATE-checked.
- Genesis text fully backfilled (1533/1533). NOTE: cross-passage SYNTHESES are .md-only (git), NOT DB-filed (per primeval/Abraham precedent); the per-passage READINGS are the DB record (type 108). Syntheses in `verse-analysis/genesis/_synthesis/`.

**Tooling (reusable, all built/proven this work):**
- Filer: `scripts/_apply_file_passage_lexical_prose_v1_20260704.py --book --unit-code --story --live --no-backup` (one reading per unit_code, type 108).
- Gate (MANDATORY): `scripts/_check_passage_reading_coverage_v1_20260704.py --unit-code=X [--story=path]`.
- Segmentation loader: `scripts/_apply_load_segmentation_v1_20260703.py --in <json> --live` (idempotent per provenance).
- Backfill (if a book lacks context verses): `scripts/_apply_backfill_chapter_verses_v1_20260702.py --book --chapter --live --no-backup`.

**NEXT (resume here):** the **Joseph cycle, Gen 37-50** (Joseph sold, Judah/Tamar ch38, Potiphar, dreams/prison, the reconciliation, Jacob's blessing of the sons ch49, the deaths). Same workflow: per-chapter non-T2 density scan (`scripts/_probe...` / the density script pattern in scratchpad) -> cast passages by operation-web -> segmentation JSON (provenance `genesis-joseph-v1-<date>`) -> load -> verify 0 non-T2 gaps -> read passage-by-passage with the gate -> commit every 2-3 -> synthesis (.md). Watch (let emerge): the DEFERRED RECKONINGS land in Gen 49 (Jacob's deathbed words on Reuben/Simeon/Levi ← the silences JAC-17/18); Judah's transformation (ch38 -> ch44 the substitute); Joseph's providence-reading ("you meant evil, God meant good" 50:20 - the natan/God-gave theology matured); dreams; forgiveness. Reusable probe: `scripts/_probe_passage_material_v1_20260704.py --unit-code=X`. Full resumption guide: `verse-analysis/genesis/_reports/wa-session-log-20260704-genesis-narrative-span-depth.md` (update it for Joseph).

**Related open loop:** [[project_prophets_wisdom_read_at_movement_depth_debt]] - the poetic/prophetic chapter readings need an additive span-depth pass later (parked).
