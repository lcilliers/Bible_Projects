# v3_0 Publication Pipeline — design

**Date:** 2026-05-27
**Status:** Design proposal, partial infrastructure in place
**Trigger:** Researcher direction — Session C re-reads what Phase 9 just had in memory; use the existing prose store; build for input → output (catch-up + revised publishing).

## §1. Pipeline overview

```
Phase 9 batch (per characteristic, AI session)
  ├─ Authors 189 prompt findings → cluster_finding
  ├─ Authors 8 tier-prose blocks → prose_section (sc_v2_tier_T0..T7, scope=characteristic)
  └─ Self-check
       ↓
Phase 9 synthesis batch (per cluster, AI session)
  ├─ Authors 189 cluster-scope findings → cluster_finding
  ├─ Authors 3 cluster-scope prose:
  │    sc_v2_synth_opening    (Ch1 cluster-wide)
  │    sc_v2_synth_divine_pattern (Ch3 cluster spine)
  │    sc_v2_synth_appendix   (free-form themes)
  └─ All → prose_section (scope=cluster)
       ↓
Phase 11 validation + Phase 12 closure (as now)
       ↓
Session C publication (mostly CC; optional researcher polish)
  ├─ CC: scripts/_assemble_cluster_publication_from_db_v1_*.py --cluster {CODE}
  │       reads prose_section by cluster → assembles combined Markdown
  ├─ Researcher reviews assembled markdown
  ├─ Researcher edits → scripts/_ingest_chapter_prose_v1_*.py
  │       ingests revisions → new prose_section version (supersession chain)
  └─ Final PDF/DOCX generation (existing combine_cluster_published_to_docx.py / markdown-pdf)

CATCH-UP for clusters not yet published (M02, M04-M09, M20, M26, M39, M46):
  Phase 9 already produced findings under the old per-cluster-scope model.
  CC: build inputs/ (already done for 11 of these via _build_complete_extract.py)
  AI: short Session C session per cluster producing ch1-ch7 (one-time legacy
       authoring under existing Session C model)
  CC: ingest each draft into prose_section via _ingest_chapter_prose_v1_*.py
  CC: assemble final via _assemble_cluster_publication_from_db_v1_*.py
```

## §2. Infrastructure (in place as of 2026-05-27)

### §2.1 Schema (M54, schema 3.27.0 → 3.28.0)

Extended `prose_section`:

| Column | Type | Purpose |
|---|---|---|
| cluster_code | TEXT NULL | Cluster scope (the canonical FK to `cluster`) |
| characteristic_id | INTEGER NULL | Characteristic-scope FK to `characteristic` |
| cluster_subgroup_id | INTEGER NULL | Sub-group-scope FK (for per-sub-group prose if needed) |

Indexes added:
- `idx_prose_section_cluster_code` (partial, WHERE cluster_code IS NOT NULL)
- `idx_prose_section_characteristic_id` (partial)
- `idx_prose_section_cluster_subgroup_id` (partial)

`prose_section_fts` rebuilt to include `cluster_code` + `characteristic_id` as UNINDEXED filter columns. FTS triggers (ai/au/ad) updated.

### §2.2 Section types registered (18 new sc_v2_* rows)

**Chapter prose** (per-cluster, 7 chapters):
- `sc_v2_ch1` What this study is
- `sc_v2_ch2` The characteristics in this study
- `sc_v2_ch3` The divine pattern
- `sc_v2_ch4` Where each characteristic lives in the person
- `sc_v2_ch5` How each characteristic works
- `sc_v2_ch6` How each characteristic relates to the others
- `sc_v2_ch7` The view from outside Scripture

**Tier publication prose** (per-characteristic, 8 tiers, authored during Phase 9 batch):
- `sc_v2_tier_T0` through `sc_v2_tier_T7`

**Cluster synthesis prose** (per-cluster, authored during Phase 9 synthesis batch):
- `sc_v2_synth_opening` (Ch1 cluster-wide)
- `sc_v2_synth_divine_pattern` (Ch3 spine)
- `sc_v2_synth_appendix` (free-form themes)

### §2.3 Tier → chapter mapping

| Source tier-prose | Consumed by chapter | Notes |
|---|---|---|
| sc_v2_tier_T0 (per char) | Ch1 (cluster intro), Ch3 (divine pattern per char) | T0 = Divine Image |
| sc_v2_synth_opening | Ch1 | Cluster-wide opening |
| sc_v2_synth_divine_pattern | Ch3 | Cluster-wide spine |
| sc_v2_tier_T1 (per char) | Ch1, Ch5 | T1 = Faculty in operation |
| sc_v2_tier_T2 (per char) | Ch4 | T2 = Constitutional location |
| sc_v2_tier_T3 (per char) | Ch4 | T3 = Faculties |
| sc_v2_tier_T4 (per char) | Ch5 | T4 = Relational interfaces |
| sc_v2_tier_T5 (per char) | Ch5 | T5 = Transformation |
| sc_v2_tier_T6 (per char) | Ch6 | T6 = Inter-characteristic |
| sc_v2_tier_T7 (per char) | Ch7 | T7 = View from outside Scripture |

Under v3_0, Session C's chapter assembly is a CC join over `prose_section`: gather tier-prose per characteristic + synthesis prose per cluster, concatenate per chapter mapping.

### §2.4 Scripts (in place)

| Script | Purpose |
|---|---|
| `_migrate_m54_prose_section_cluster_scope_20260527.py` | Schema migration (applied) |
| `_apply_v3_section_types_20260527.py` | Section type registration (applied) |
| `_backfill_published_clusters_to_prose_section_20260527.py` | Backfill M01/M03/M15 chapter drafts (applied — 36 rows loaded) |
| `_assemble_cluster_publication_from_db_v1_20260527.py` | Read prose_section → combined Markdown (works; M03 verified) |
| `_ingest_chapter_prose_v1_20260527.py` | Take input markdown → insert prose_section rows with supersession chain |

## §3. v3_0 Phase 9 batch instruction extension

Per characteristic batch, the AI's output structure extends:

```
For tier T{N}:
  1. Author the tier's N prompts as parser-safe findings (as v2_9)
  2. After all the tier's findings are written:
       Write a publication-ready prose summary of the tier's findings.
       Length: 200-500 words (see expected_length_min/max in
       prose_section_type for sc_v2_tier_T{N})
       Format: prose paragraphs (no bullet points, no headers)
       Use the sub-group/VCG/verse citation conventions of the findings.
       Mark the section with `**[TIER_PROSE_T{N}]**` opening marker.
  3. CC's loader writes the tier prose to prose_section as:
       cluster_code = {cluster}
       characteristic_id = {char.id}
       section_type_id = sc_v2_tier_T{N}.id
       version = 1
       status = 'draft'
       author = 'claude_ai'
```

Per synthesis batch:
- Same pattern for the 3 cluster-scope prose blocks
- `**[CLUSTER_OPENING]**`, `**[CLUSTER_DIVINE_PATTERN]**`, `**[CLUSTER_APPENDIX]**` markers
- Loader inserts with `cluster_code` set, `characteristic_id` NULL

## §4. v3_0 Session C reduction

Session C ceases to be an AI session. The CC assembly script (`_assemble_cluster_publication_from_db_v1_*.py`) becomes its primary engine:

1. **Resolve latest active version** for each chapter:
   `WHERE cluster_code=? AND section_type_id=? AND superseded_by_id IS NULL`
2. **For chapter prose authored directly** (sc_v2_ch{N} rows present): use as-is.
3. **For chapter prose derived from tier prose** (sc_v2_ch{N} missing, tier prose present): assemble by gathering tier prose blocks per the §2.3 mapping. Optional cluster-level voice polish via short AI session.
4. **Optional researcher review** of assembled markdown.
5. **Final output**: combined Markdown + PDF/DOCX via existing assemblers.

Session C reduces from ~10 AI sessions to ~0-1 (the optional polish).

## §5. Catch-up routine

For the 11 closed clusters with `inputs/` but no chapter drafts (M02, M04, M05, M06, M07, M08, M09, M20, M26, M39, M46) and the 3 with no inputs at all (M10, M10b, M10c):

```
Per cluster:
  1. CC: ensure inputs/ folder exists (build_complete_extract.py if missing)
  2. AI: run legacy Session C model — 7 chapter sessions, ~30 min each, writes
     chapter drafts to /published/
  3. CC: _ingest_chapter_prose_v1_*.py --cluster {CODE} --multi --input <combined draft>
     (or per-chapter ingest)
  4. CC: _assemble_cluster_publication_from_db_v1_*.py --cluster {CODE}
  5. CC: combine_cluster_published_to_docx.py for final PDF/DOCX

This is one-time legacy authoring under v2_x Session C. v3_0 publication
pipeline doesn't try to retroactively produce tier prose for these clusters
(they have findings only, no tier prose — the prose store still holds the
chapter outputs which is all Session C consumers need).
```

## §6. Revised publishing routine

For clusters already published where the researcher wants revisions:

```
1. Researcher edits the chapter markdown file (e.g. revised ch3 prose)
2. CC: _ingest_chapter_prose_v1_*.py --cluster {CODE} --ch 3 --input <revised.md>
   - New version inserted; old version becomes superseded
   - Supersession chain preserved in DB
3. CC: _assemble_cluster_publication_from_db_v1_*.py --cluster {CODE}
   - Picks up latest active version automatically
4. CC: regenerate PDF/DOCX
```

Idempotency: if the input body matches the current latest version's body
(hash-compared), no new row is inserted.

## §7. The backfilled M01/M03/M15 state

| Cluster | Chapters loaded | Versions | Status |
|---|---:|---|---|
| M01 | 7 | v1, v2 (each ch) | draft |
| M03 | 7 | v1 (each ch) | approved |
| M15 | 7 | v1, v2, ch4 also v3 | draft |

36 rows total, with 15 supersession chain links. FTS indexed. Verified by running the assembler on M03 (38,515 words assembled successfully).

## §8. Files written today

- `scripts/_migrate_m54_prose_section_cluster_scope_20260527.py`
- `scripts/_apply_v3_section_types_20260527.py`
- `scripts/_backfill_published_clusters_to_prose_section_20260527.py`
- `scripts/_assemble_cluster_publication_from_db_v1_20260527.py`
- `scripts/_ingest_chapter_prose_v1_20260527.py`
- `Workflow/Instructions/wa-v3-publication-pipeline-design-v1-20260527.md` (this doc)

## §9. Outstanding for v3_0

1. **Phase 9 batch builder extension** — when v3_0 governs new cluster work, the per-characteristic and synthesis batch builders need to extend the AI prompt to request tier prose alongside findings. The loader needs to parse `[TIER_PROSE_T{N}]` markers and insert into prose_section.
2. **PDF/DOCX assembly from DB** — currently combine_cluster_published_to_docx.py reads from files. A DB-driven version would close the loop (read prose_section → emit DOCX).
3. **`prose_section_finding_link` population** — when ingesting tier prose, the loader could automatically link the prose section to the cluster_finding rows it synthesises (the tier's 21-33 findings). This makes the "which findings does this prose summarise?" question queryable.
4. **Researcher approval workflow** — `prose_section.status` and `approved_at`/`approved_by` fields exist. A `_approve_prose_section.py` script would let researcher mark sections approved after review, advancing the publication state.

These are forward extensions, not blockers for the v3_0 design itself.

---

*Design v1 — 2026-05-27. Infrastructure in place; awaits v3_0 Phase 9 instruction integration.*
