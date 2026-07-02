---
name: project_lexical_prose_endpoint_and_ve_lexical_phase1
description: "STATE (2026-07-02): the single-term pipeline ENDPOINT = the accepted first-tier story filed to prose_section under new type 'lexical_prose' (one per owner term). AND ve_lexical Phase 1 optimisation (M63, schema 3.37.0): 507k legacy rows archived to ve_lexical_legacy so the live table = live model only (~1,990 rows)."
metadata:
  node_type: memory
  type: project
  originSessionId: bf6ef2d7-5b5c-4775-88f2-f2ca15223daa
---

**Two things landed 2026-07-02, after the ruthlessness (perek H6531) first-tier story was accepted.** Builds on [[project_term_driven_genre_aware_lexical_method]] and the architecture review `verse-analysis/_reports/wa-ve-lexical-architecture-review-v1-20260702.md`.

**1. Pipeline ENDPOINT = story filed to prose.** The single-term story (lexicals-only, cited) is filed into `prose_section` under a NEW section type **`lexical_prose`** (`prose_section_type.code='lexical_prose'`, id 103) — "Lexical Prose (single-term story)", **one per owner term**. Ruthlessness = `prose_section` id **398** (registry_id 216, cluster_code M06, v1, status approved, author `claude_code`; verse list + `source:lexical-model-2026` in `metadata_json`; verses cited INLINE in the body — the finding-centric `wa_prose_section_citations` table does NOT fit lexical prose so it's unused). FTS (`prose_section_fts`) auto-populates via triggers. Script: `scripts/_apply_file_ruthlessness_lexical_prose_20260702.py`. This is the last step of the per-term pipeline (anchor lexical → all verses → sanity-check → synthesis → story → **prose**).

**2. ve_lexical Phase 1 optimisation (M63, schema → 3.37.0).** The researcher's "huge duplication" impression was correct but it was **legacy accretion, not the live model**: `ve_lexical` held 509,641 rows of which only ~1,990 were live (`source_provenance='lexical-model-2026'`, all delete-flags). Phase 1 (approved a+b): **archived 507,651 non-live rows to `ve_lexical_legacy`** (retained per catalogue §7, NOT deleted); **dropped the duplicate index `ix_velex_vc`** (was identical to `ix_ve_lexical_vc`); VACUUM reclaimed 129 MB (DB 769.7 → 640.5 MB). `ve_lexical` is now the live model only. Script: `scripts/_apply_ve_lexical_phase1_archive_legacy_20260702.py`. Engine constant `EXPECTED_SCHEMA_VERSION=3.37.0`.

**Phase 2 HELD** (researcher agreed to defer): normalise the live EAV into `span_lexical` (1/span) + `span_pair` (N/span) and FK-ise `from_span`/`to_span` (currently TEXT like `H6973@Exo 1:12`, un-joinable — the cross-term/cohabitation layer will need real span FKs). Revisit after ~10 terms across genres so the item set stabilises first (avoid rework). Cf. [[project_ve_lexical_normalisation_and_groundings]] (now stale/pre-reset).
