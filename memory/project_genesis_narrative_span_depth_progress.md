---
name: project_genesis_narrative_span_depth_progress
description: "ACTIVE WORK (2026-07-05): reading the OT NARRATIVES for the inner being at SPAN DEPTH (verse-first, span-by-span, gate-checked). GENESIS 1-50 FULLY COMPLETE (69 readings ps 916-1004, 4 syntheses) - Joseph cycle (Gen 37-50) was the skipped section, now done. EXODUS Block 1 (1:1-15:21) COMPLETE (20 readings ps 968-987). NEXT: Exodus Block 2 (15:22-24 wilderness+Sinai; backfill Ex 16-24 first, STEP up)."
metadata: 
  node_type: memory
  type: project
  originSessionId: 92aed34e-8a28-44a4-8d9d-4bdf6df70a12
---

**Narrative inner-being reading at span depth** — the method the researcher confirmed 2026-07-04 (span-lexical is the unit not the plot; individual + INTERACTIVE operations; never lump repeated/same-gloss spans, never over-read genealogies; story instrumental). Full method: `verse-analysis/_methodology/wa-ot-narrative-inner-being-method-proposal-20260704.md` + worked example `wa-narrative-method-worked-example-gen3-20260704.md`. Governed by [[feedback_resist_grouping_preserve_distinctions]], [[project_passage_reading_checkback_gate]], [[feedback_each_chapter_first_principles_find_the_gems]].

**Progress (GENESIS 1-50 FULLY COMPLETE):**
- Primeval Gen 1-11: 15 passages GEN-01..15 (ps 916-930), synthesis filed.
- Abraham Gen 12-25:18: 18 passages ABR-01..18 (ps 931-948), synthesis filed.
- Jacob Gen 25:19-36: 19 passages JAC-01..19 (ps 949-967, `genesis-jacob-v1-20260704`), synthesis. Spine = grasp TRANSFIGURED (Peniel).
- Joseph Gen 37-50: 17 passages JOS-01..17 (ps 988-1004, `genesis-joseph-v1-20260705`), 0 gaps, synthesis. Spine = PROVIDENCE discerned + evil overruled ("you meant evil, God meant good" 50:20; chashav for both agencies <- machashavah 6:5 - Genesis's arc closes). Judah's transformation (seller->substitute->scepter); guilt-that-cannot-rest; Joseph's escalating weeping; deferred reckonings LAND at Gen 49 (Reuben/Bilhah, Simeon&Levi/Shechem - JAC-17/18 silences broken); bones-oath seams into Exodus. (Was the SKIPPED section - researcher caught it; done 2026-07-05.)
- 69 readings, ~106,000 words, type 108 `lexical_prose_passage`, every reading GATE-checked. 4 cross-passage syntheses.
- Genesis text fully backfilled (1533/1533). NOTE: cross-passage SYNTHESES are .md-only (git), NOT DB-filed; the per-passage READINGS are the DB record (type 108). Syntheses in `verse-analysis/genesis/_synthesis/`.

**Progress (EXODUS Block 1 COMPLETE, 2026-07-05):**
- Ex 1:1-15:21 (Bondage->Call->Deliverance): 20 passages EXO-01..20 (prose_section 968-987, provenance `exodus-deliverance-v1-20260705`), 0 non-T2 gaps, synthesis filed. ~32,950 words.
- Backfill needed (Ex was 793/1213; backfilled 1-15 via STEP). Exodus text NOT complete beyond ch15 - later blocks need backfill (STEP must be up).
- **Method additions this block (researcher-steered):** (1) **hardening-ledger** = an empirical per-motif trajectory analysis (`verse-analysis/exodus/_reports/wa-exodus-hardening-trajectory-analysis-20260705.md`) built BEFORE the readings, tabulating every occurrence's AGENT/verb/trigger - answered "why the hardening switched" (self->God at 9:12 AFTER settled self-hardening + counterfeit collapse; relief-triggers-hardening 8:15/9:34; confession-without-fear 9:27->30->34). Reusable pattern for any recurring motif. (2) **multi-interior lens** = read the ADVERSARY's IB (Pharaoh) and the protagonist people's IB (Israel) as DISTINCT contrary arcs, never merged (Pharaoh hardens->judgment; Israel groan->fear/faith->song). Both now standing method for narratives with an antagonist.
- Exodus block plan (5 blocks): 1 done (1-15:21); 2 wilderness+Sinai (15:22-24); 3 tabernacle-instructions THIN (25-31); 4 golden calf+renewal (32-34); 5 tabernacle-construction THIN (35-40). Block plan + density scan: `verse-analysis/exodus/_seg/wa-exodus-passage-set-block1-*` + `_reports/wa-exodus-density-readiness-scan-*`.

**Tooling (reusable, all built/proven this work):**
- Filer: `scripts/_apply_file_passage_lexical_prose_v1_20260704.py --book --unit-code --story --live --no-backup` (one reading per unit_code, type 108).
- Gate (MANDATORY): `scripts/_check_passage_reading_coverage_v1_20260704.py --unit-code=X [--story=path]`.
- Segmentation loader: `scripts/_apply_load_segmentation_v1_20260703.py --in <json> --live` (idempotent per provenance).
- Backfill (if a book lacks context verses): `scripts/_apply_backfill_chapter_verses_v1_20260702.py --book --chapter --live --no-backup`.

**NEXT (resume here): Exodus Block 2, Ex 15:22-24:18** (Marah/manna/water/Amalek/Jethro; Sinai theophany; the Decalogue; the Book of the Covenant; covenant ratified). GENESIS IS DONE (all 4 blocks incl. Joseph). Backfill Ex 16-24 first (STEP up - Exodus text was 793/1213, only ch1-15 backfilled so far). Watch: Israel's IB continues past the sea (the murmuring/testing arc - the song fades fast at Marah 15:24); the LAW as inner-being (coveting 20:17; "you know the heart of a sojourner" 23:9; the fear-of-God at Sinai). Then Exodus Block 4 (golden calf 32-34, narrative-rich) is the next gem after; Blocks 3+5 (tabernacle 25-31, 35-40) THIN. Exodus block plan in `verse-analysis/exodus/_seg/wa-exodus-passage-set-block1-*`.

Same workflow: density scan (scratchpad `exodus_readiness.py`/`exodus_spans.py` patterns) -> cast passages -> segmentation JSON -> load -> verify 0 gaps -> read with the gate (+ multi-interior lens where an antagonist exists; hardening-ledger-style motif analysis for recurring motifs) -> commit every 2-3 -> synthesis (.md). Reusable probe: `scripts/_probe_passage_material_v1_20260704.py --unit-code=X`.

**Related open loop:** [[project_prophets_wisdom_read_at_movement_depth_debt]] - the poetic/prophetic chapter readings need an additive span-depth pass later (parked).
