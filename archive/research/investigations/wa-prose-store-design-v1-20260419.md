# wa-prose-store — Design Workings (v1)

| Field | Value |
|---|---|
| Filename | wa-prose-store-design-v1-20260419.md |
| Status | DRAFT — awaiting researcher markup |
| Purpose | Design workings for prose/narrative storage in SQLite (Option D — DB-canonical with file round-trip). Approved by researcher 2026-04-19; folded into the DB-wide review scope. |
| Decision reference | `outputs/investigations/prose-in-sqlite-advice-v1-20260419.md` — researcher approved Option D, requested DB review to include infrastructure + routines |
| Related design | `outputs/investigations/wa-global-database-review-design-v1-20260419.md` — updated to include prose scope |
| Related design | `outputs/investigations/wa-global-readiness-sweep-design-v1-20260419.md` — may gain a prose coverage phase |
| Produced | 2026-04-19 |

---

## 1. Decisions Already Made (researcher direction)

| # | Decision | Source |
|---|---|---|
| P1 | Adopt DB-canonical prose storage (Option D) | 2026-04-19 message |
| P2 | DB review prepares the infrastructure AND supporting routines | 2026-04-19 message |
| P3 | Work in `.md`, canonical is DB | 2026-04-19 message |
| P4 | CC prepares table structure | 2026-04-19 message |
| P5 | `.md` export can contain any number of sections in any order; import routes each to its correct DB row automatically | 2026-04-19 message |

**Open items that still need markup** are in §11 (narrower than before — most major decisions are made).

---

## 2. Architecture Recap

DB-canonical. Prose lives in relational rows. Editing happens in `.md` files via round-trip tooling. The DB is the source of truth; files are scratchpads.

```
  ┌─ DB (canonical) ────────────────────────────────┐
  │                                                 │
  │  prose_section  ──────> prose_section_fts (FTS5)│
  │      │                                          │
  │      ├──> prose_section_type (dictionary)       │
  │      ├──> prose_section_dimension_link          │
  │      └──> prose_section_finding_link            │
  │                                                 │
  └──────────┬──────────────────────────▲───────────┘
             │                          │
   export_prose.py               import_prose.py
             │                          │
             ▼                          │
  ┌─ .md scratchpad ──────────────────┐ │
  │  <!-- PROSE_SECTION id: 1234 -->  │ │
  │  ## Heading                       │ │
  │  prose body ...                   │ │
  │  <!-- PROSE_SECTION id: 1235 -->  │─┘
  │  ## Another heading                
  │  more prose ...                   
  └───────────────────────────────────┘
             │
             ▼
     render_prose.py
             │
             ▼
   outputs/markdown/ · outputs/docx/  (publication)
```

---

## 3. Table Schema — Full Specification

### 3.1 `prose_section_type` — dictionary

```sql
CREATE TABLE prose_section_type (
  id              INTEGER PRIMARY KEY,
  code            TEXT NOT NULL UNIQUE,     -- stable machine code: 'sb_ch2_meaning'
  label           TEXT NOT NULL,            -- human label: 'Session B Chapter 2 — Meaning'
  source_stage    TEXT NOT NULL,            -- 'session_b' | 'session_c' | 'session_d'
  lifecycle_tag   TEXT,                     -- 'v1' | 'v2' | 'v3' for Session C; NULL otherwise
  chapter_no      INTEGER,                  -- 1..6 for chaptered stages; NULL for synthesis
  description     TEXT,                     -- what this section is for
  expected_length_min  INTEGER,             -- optional: word count lower bound
  expected_length_max  INTEGER,             -- optional: word count upper bound
  sort_order      INTEGER NOT NULL,         -- for rendering order
  delete_flagged  INTEGER NOT NULL DEFAULT 0,
  created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE UNIQUE INDEX idx_pst_code ON prose_section_type(code) WHERE delete_flagged = 0;
CREATE INDEX idx_pst_stage_lifecycle ON prose_section_type(source_stage, lifecycle_tag) WHERE delete_flagged = 0;
```

### 3.2 `prose_section` — canonical prose store

```sql
CREATE TABLE prose_section (
  id                INTEGER PRIMARY KEY,
  registry_id       INTEGER NOT NULL REFERENCES word_registry(id),
  section_type_id   INTEGER NOT NULL REFERENCES prose_section_type(id),
  heading           TEXT,                   -- section heading as written (may override type label)
  body              TEXT NOT NULL,          -- the prose itself (UTF-8, markdown-compatible)
  word_count        INTEGER NOT NULL,       -- computed on insert/update
  status            TEXT NOT NULL,          -- 'draft' | 'in_review' | 'approved' | 'archived'
  version           INTEGER NOT NULL DEFAULT 1,
  supersedes_id     INTEGER REFERENCES prose_section(id),
  superseded_by_id  INTEGER REFERENCES prose_section(id),
  author            TEXT NOT NULL,          -- 'claude_ai' | 'claude_code' | 'researcher'
  created_at        TEXT NOT NULL,
  approved_at       TEXT,
  approved_by       TEXT,
  metadata_json     TEXT,                   -- flexible extras: {"dimension_ids":[...], "finding_ids":[...]}
  source_file       TEXT,                   -- optional: path to .md that produced this version
  delete_flagged    INTEGER NOT NULL DEFAULT 0,

  CHECK (status IN ('draft','in_review','approved','archived')),
  CHECK (author IN ('claude_ai','claude_code','researcher')),
  CHECK (length(body) > 0),
  CHECK (word_count >= 0),
  -- Exactly one current version per (registry, section_type):
  -- enforced in application (import tool) rather than via partial UNIQUE
  -- because SQLite partial indexes have some limitations on triggers
);

CREATE INDEX idx_ps_registry_type_current
  ON prose_section(registry_id, section_type_id)
  WHERE delete_flagged = 0 AND superseded_by_id IS NULL;

CREATE INDEX idx_ps_status
  ON prose_section(status)
  WHERE delete_flagged = 0 AND superseded_by_id IS NULL;

CREATE INDEX idx_ps_supersedes
  ON prose_section(supersedes_id)
  WHERE supersedes_id IS NOT NULL;
```

**Design notes on the supersede chain:**
- New version = `INSERT` a new row. Old row's `superseded_by_id` is updated to the new row's id.
- `superseded_by_id IS NULL AND delete_flagged = 0` → current live version.
- `supersedes_id` walks backwards for full history.
- Never in-place UPDATE of `body` on an approved row. Drafts may be updated in place (saves churn). This is the "Option (c) hybrid" from the advice doc Q7.

### 3.3 `prose_section_fts` — full-text search

```sql
CREATE VIRTUAL TABLE prose_section_fts USING fts5(
  body,
  heading,
  section_type_code UNINDEXED,
  registry_id UNINDEXED,
  status UNINDEXED,
  content='prose_section',
  content_rowid='id',
  tokenize='porter unicode61 remove_diacritics 2'
);

-- Sync triggers
CREATE TRIGGER prose_section_ai AFTER INSERT ON prose_section
BEGIN
  INSERT INTO prose_section_fts(rowid, body, heading, section_type_code, registry_id, status)
  SELECT new.id, new.body, new.heading, pst.code, new.registry_id, new.status
  FROM prose_section_type pst WHERE pst.id = new.section_type_id;
END;

CREATE TRIGGER prose_section_au AFTER UPDATE ON prose_section
BEGIN
  INSERT INTO prose_section_fts(prose_section_fts, rowid, body, heading, section_type_code, registry_id, status)
  VALUES('delete', old.id, old.body, old.heading, '', old.registry_id, old.status);
  INSERT INTO prose_section_fts(rowid, body, heading, section_type_code, registry_id, status)
  SELECT new.id, new.body, new.heading, pst.code, new.registry_id, new.status
  FROM prose_section_type pst WHERE pst.id = new.section_type_id;
END;

CREATE TRIGGER prose_section_ad AFTER DELETE ON prose_section
BEGIN
  INSERT INTO prose_section_fts(prose_section_fts, rowid, body, heading, section_type_code, registry_id, status)
  VALUES('delete', old.id, old.body, old.heading, '', old.registry_id, old.status);
END;
```

### 3.4 Link tables (optional but recommended)

```sql
-- Links prose sections to the dimensions they discuss
CREATE TABLE prose_section_dimension_link (
  prose_section_id  INTEGER NOT NULL REFERENCES prose_section(id),
  dimension_id      INTEGER NOT NULL,   -- FK to wa_dimension_index.id (or its replacement post-DB-review)
  link_type         TEXT NOT NULL,      -- 'discusses' | 'references' | 'cites'
  created_at        TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (prose_section_id, dimension_id, link_type)
);

-- Links prose sections to the Session B findings they discuss
CREATE TABLE prose_section_finding_link (
  prose_section_id  INTEGER NOT NULL REFERENCES prose_section(id),
  finding_id        INTEGER NOT NULL REFERENCES wa_session_b_findings(id),
  link_type         TEXT NOT NULL,      -- 'discusses' | 'references' | 'cites'
  created_at        TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (prose_section_id, finding_id, link_type)
);
```

**Use case:** "Find all prose sections discussing finding X across all words" — useful for consistency audits post-systematic-edit.

---

## 4. Section Type Catalogue — Seed Data Proposal

**PROPOSED** seed values. Finalise once Session B/C/D chapter structures are confirmed.

| code | label | source_stage | lifecycle_tag | chapter_no |
|---|---|---|---|---|
| `sa_s1_d1` | Session A Step — 1 | session_a | Word Summary | 1 |
| `sa_s1_d2` | Session A Step — 1 | session_a | Meaning | 2 |
| `sa_s1_d3` | Session A Step — 1 | session_a | Verses | 3 |
| `sa_s1_d4` | Session A Step — 1 | session_a | Terms | 4 |
| `sa_s1_d5` | Session A Step — 1 | session_a | Pointers | 5 |
| `sa_s1_d6` | Session A Step — 1 | session_a | Questions | 6 |
| `sb_s2c_ch1` | Session B Stage 2c — Chapter 1 | session_b | Word Characteristic Summary | 1 |
| `sb_s2c_ch2` | Session B Stage 2c — Chapter 2 | session_b | Word Impact Description | 2 |
| `sb_s2c_ch3` | Session B Stage 2c — Chapter 3 | session_b | Annotated Verse Evidence | 3 |
| `sb_s2c_ch4` | Session B Stage 2c — Chapter 4 | session_b | 	Original Language Vocabulary | 4 |
| `sb_s2c_ch5` | Session B Stage 2c — Chapter 5 | session_b | Connections  | 5 |
| `sc_v1_ch1` | Session C v1 — Chapter 1 | session_c | synopsis | 1 |
| `sc_v1_ch2` | Session C v1 — Chapter 2 | session_c | Description | 2 |
| `sc_v1_ch3` | Session C v1 — Chapter 3 | session_c | Inner being at work | 3 |
| `sc_v1_ch4` | Session C v1 — Chapter 4 | session_c | At work in scripture | 4 |
| `sc_v1_ch5` | Session C v1 — Chapter 5 | session_c | Lexicon | 5 |
| `sd_synthesis_Cl1` | Session D — Cluster 1 | session_d | Moral Character | 1 |
| `sd_synthesis_Cl2` | Session D — Cluster 2 | session_d | Cognition |2 |
| `sd_synthesis_Cl3` | Session D — Cluster 3 | session_d | Volition | 3 |
| `sd_synthesis_Cl4` | Session D — Cluster 4 | session_d | Relational Disposition | 4 |
| `sd_synthesis_Cl5` | Session D — Cluster 5 | session_d | Divine-Human Correspondence | 5 |
| `sd_synthesis_Cl6` | Session D — Cluster 6 | session_d | Agency  | 6 |
| `sd_synthesis_Cl7` | Session D — Cluster 7 | session_d | Dependence  | 7 |
| `sd_synthesis_Cl8` | Session D — Cluster 8 | session_d | Emotion | 8 |
| `sd_synthesis_Cl9` | Session D — Cluster 9 | session_d | Vitality | 9 |
| `sd_synthesis_Cl10` | Session D — Cluster 10 | session_d | Transformation | 10 |

**OPEN — Q4 below:** please confirm the canonical chapter labels per Session B Stage 2c and per Session C lifecycle version. Current instructions reference "6 chapters" but the specific section names are the naming authority for `label`.

---

### Reviewer observations on researcher edits (2026-04-19 PM)

Flagging items for when you return to this table. Not blocking — corrections to apply in the next pass.

**Column alignment:** The table header defines columns as `code | label | source_stage | lifecycle_tag | chapter_no`. Your edits have placed chapter/section names (e.g. "Word Summary", "Meaning", "Moral Character") in the **`lifecycle_tag`** column, but per schema §3.1 `lifecycle_tag` is intended for 'v1' / 'v2' / 'v3' (Session C lifecycle version). The chapter name should live in **`label`**. Recommend refactoring the table to something like:

```text
| code | label | source_stage | lifecycle_tag | chapter_no |
| sa_s1_d1 | Session A — Word Summary | session_a | NULL | 1 |
| sb_s2c_ch1 | Session B Stage 2c — Word Characteristic Summary | session_b | NULL | 1 |
| sc_v1_ch1 | Session C v1 — Synopsis | session_c | v1 | 1 |
| sd_cl1_moral | Session D Cluster — Moral Character | session_d | NULL | 1 |
```

**Session A codes:** Your `sa_s1_d1` … `sa_s1_d6` work. The advice doc used descriptive codes (`sa_summary`, `sa_meaning`, `sa_terms`, `sa_verses`, `sa_pointers`, `sa_questions`). Either works — pick one style and keep consistent.

**Session A ordering:** Your order is Summary → Meaning → Verses → Terms → Pointers → Questions. The advice doc proposed Summary → Meaning → Terms → Verses → Pointers → Questions. Minor — which flows better is a readability judgement.

**Session B Stage 2c labels:** Confirmed from question catalogue extract (194 questions grouped into 5 catalogue sections). Your 5 chapters match the catalogue §1–§5.

**Session C:** Only `v1` listed. v2 and v3 lifecycle versions can be added when their chapter structure is defined, or noted as deferred.

**Session D — four concerns:**

1. Code contains a space: `sd_synthesis Cl1`. Codes should be identifier-safe (no spaces). Recommend `sd_cl1_moral_character`, `sd_cl2_cognition`, etc.
2. All labels say "Cluster 1" (copy-paste from first row). Each should be unique: "Cluster 1" / "Cluster 2" / …
3. Dimension **Transformation** is missing. From the dimensions extract, it has 115 uses across 56 words — a real programme-wide dimension. Add as `sd_cl10_transformation` (or equivalent).
4. Optional: consider whether legacy dimensions (Identity / Selfhood; Somatic / Embodied) deserve their own Session D cluster sections or fold into the 9 above after vocabulary normalisation (per dimensions extract §6).

---

## 5. Multi-Section `.md` Round-Trip — The Key Spec

This section answers your question: *"an md export can include any number of sections in any order. and when the MD is added back, it will automatically know which section should go where in the database."*

### 5.1 Marker format

Each section is prefixed by an HTML-comment marker block. HTML comments render invisibly in markdown previewers, so they do not pollute the reading experience.

```markdown
<!-- PROSE_SECTION
id: 1234
type: sb_s2c_ch2
registry: 68
version: 2
status: draft
author: claude_ai
-->

## Chapter 2 — Meaning

Lorem ipsum dolor sit amet...

(any standard markdown here: headings, lists, code, quotes)

<!-- PROSE_SECTION
id: 1287
type: sb_s2c_ch3
registry: 68
version: 1
status: approved
author: claude_ai
-->

## Chapter 3 — Use in Context

Another section, any order...
```

**Marker fields:**

| Field | Required | Purpose |
|---|---|---|
| `id` | For updates — YES. For new sections — NO (stub). | Points to the existing `prose_section.id` row |
| `type` | Always | Section type code (maps to `prose_section_type.code`) |
| `registry` | Always | Registry `no` (word_registry.no) |
| `version` | For updates — YES | Detect edit conflicts if DB has moved on |
| `status` | Always | Desired status on import: `draft` / `in_review` / `approved` |
| `author` | Always | Attribution |
| `supersedes` | Derived | Set by import to the pre-import current row's id |
| `delete` | Optional | If `true`, mark the row `delete_flagged=1` and skip body |

### 5.2 Parsing algorithm (import)

```
Read file.
Find all lines matching '<!-- PROSE_SECTION' (start markers).
For each start marker:
  marker_meta = parse YAML-like payload until '-->'
  body = text from line after '-->' to (next start marker | EOF)
  yield (marker_meta, body)

For each (meta, body):
  validate marker: required fields present
  route:
    if meta.id is present:
      row = DB lookup by id
      if row.version != meta.version and meta.delete not true:
        conflict error: halt
      if meta.delete == true:
        soft-delete; continue
      else:
        create new row supersedeing row:
          insert new prose_section with version = row.version + 1,
          supersedes_id = row.id, body = body
        update row.superseded_by_id = new_id
    else:  # new section, no id
      validate type + registry + status
      insert new prose_section with version = 1, supersedes_id = NULL
      record new id in import log
```

### 5.3 Order independence — confirmed

The parser processes markers in file order for determinism, but the OUTCOME does not depend on file order: each marker carries full routing information (id or type+registry), so sections can appear in any sequence. You can reorder freely when editing; write a new section above an old one; move sections around — all fine.

### 5.4 Partial file semantics

A `.md` file may contain only SOME of a word's sections. Sections NOT in the file are left untouched in the DB. This is the default. To explicitly delete, use `delete: true` in the marker.

### 5.5 New sections

To add a new section that does not yet exist in the DB:
- Omit the `id` field (or set `id: new`)
- Supply `type`, `registry`, `status`, `author`
- On import, a new row is created
- The import report lists the new `id` so you know what was created

To help: `export_prose.py --with-new-stubs=sb_s2c_ch4,sb_s2c_ch5` appends empty marker stubs for types not yet populated for the registry, so you can fill them in.

### 5.6 Orphan content

Text OUTSIDE any marker block:

- Content BEFORE the first marker → treated as file preamble; ignored on import (may contain editor notes, review comments)
- Content BETWEEN end of one section body and the next marker → the next marker defines where the preceding section ends, so the "gap" is implicit — import interprets as "all text up to next marker is the current section's body"
- Content AFTER the last marker → continues that section to EOF

**Import tool reports orphan content explicitly** so you know what it included/excluded.

### 5.7 Conflict detection

If DB row version advanced since export (another session edited it), import halts with:

```
CONFLICT: section id 1234 was version 2 at export; DB now at version 3.
  Export file version: 2
  DB version: 3
  Options:
    --force-overwrite: override (creates new version 4 superseding 3)
    --rebase: re-export current DB row, merge manually
    --skip: leave DB row alone
```

Researcher decides; CC does not silently override.

### 5.8 Round-trip marker examples

**Update existing section:**
```
<!-- PROSE_SECTION
id: 1234
type: sb_s2c_ch2
registry: 68
version: 2
status: in_review
author: researcher
-->
```

**Create new section:**
```
<!-- PROSE_SECTION
type: sb_s2c_ch4
registry: 68
status: draft
author: researcher
-->
```

**Delete section:**
```
<!-- PROSE_SECTION
id: 1234
version: 2
delete: true
-->
```

(Body after a delete marker is ignored. Soft-delete preserves history.)

---

## 6. Tooling Scripts

### 6.1 `scripts/export_prose.py`

```
Usage: python scripts/export_prose.py [options] > out.md

Scope options (one required):
  --registry=N                   Export one word's sections
  --registry-range=M,N           Export a range
  --section-type=CODE            Export one section type across all words
  --section-type-filter=PATTERN  Wildcard: sb_s2c_* etc.
  --word-filter=PATTERN          By word spelling

Filter options:
  --status=approved|draft|in_review|all   Default: approved
  --current-only                          Only latest version (default true)
  --include-history                       Include superseded versions

Stub options:
  --with-new-stubs=TYPE[,TYPE]    Emit empty markers for unpopulated types
  --stub-only                     Emit stubs for missing sections, no existing

Output options:
  --output=FILE                   Write to file instead of stdout
  --split-by=word|section_type    Split output into multiple files
```

### 6.2 `scripts/import_prose.py`

```
Usage: python scripts/import_prose.py [options] <file.md>

Modes:
  --dry-run           Parse and plan; report without writing
  --apply             Execute the plan (default false — requires explicit flag)

Conflict handling:
  --on-conflict=halt|skip|force-overwrite  Default: halt

Safety:
  --require-approval    Will not apply; writes a plan file awaiting approval marker
  --transaction=single|per-section  Wrap all imports in one TX or per-section TXs

Output:
  --report=FILE          Write import report (JSON + human summary)
```

Import report fields per section:
- marker meta (id, type, registry, version)
- action taken (insert_new | supersede | delete | skip | conflict_halt)
- new row id (if applicable)
- word count before/after
- status before/after

### 6.3 `scripts/render_prose.py`

```
Usage: python scripts/render_prose.py [options]

Scope:
  --registry=N               One word
  --section-type=CODE        One type across all words (for systematic review)
  --all                      Entire programme

Format:
  --format=md|docx|pdf       Default md
  --include-markers          Include PROSE_SECTION markers in output (default: no)
  --chapter-ordered          Order sections by chapter_no (default true)

Output:
  --output-dir=DIR           Default outputs/markdown/ or outputs/docx/
```

---

## 7. Patch System Integration

### 7.1 New patch type

`PROSE` — carries prose operations. Separate from analytical patches for focused approval.

### 7.2 Patch filenames

| Scope | Filename |
|---|---|
| Per registry | `wa-{nnn}-{word}-prose-v{n}-{YYYYMMDD}.json` |
| Programme-wide | `wa-global-prose-{descriptor}-v{n}-{YYYYMMDD}.json` |

### 7.3 Operations supported

| Operation | Table | Purpose |
|---|---|---|
| `insert` | prose_section | New section (new v1 row) |
| `supersede` | prose_section | Replace current row with new version |
| `delete` | prose_section | Soft-delete (sets delete_flagged=1) |
| `approve` | prose_section | Status transition: draft|in_review → approved; sets approved_at, approved_by |
| `bulk_supersede` | prose_section | Programme-wide edit across many registries |
| `insert` | prose_section_type | New section type (seed expansion) |
| `insert` | prose_section_dimension_link | Link section to dimension |
| `insert` | prose_section_finding_link | Link section to finding |

### 7.4 `bulk_supersede` safety protocol

For programme-wide edits ("update section X across all 214 words"):

1. Claude AI drafts the pattern: "For all sections of type=`sb_s2c_ch3` where registry cluster=C17, replace paragraph matching regex X with text Y."
2. CC generates a **preview file**: `outputs/previews/wa-global-prose-{descriptor}-preview-{date}.md` containing:
    - Total affected rows
    - N sample diffs (first 5, middle 5, last 5)
    - Full list of affected (registry, section_type, current_version)
3. Researcher reviews preview; marks `PREVIEW APPROVED` inline
4. CC produces the full `bulk_supersede` patch
5. Researcher approves the patch (standard patch approval)
6. CC applies in a single transaction; each affected row gets a new supersede version
7. Rollback: all old versions retained (supersede chain); undo is a reverse `bulk_supersede`

### 7.5 Applicator extensions required

`scripts/apply_session_patch.py` gains:

- `PROSE` patch type handler
- `insert` on `prose_section` (straightforward)
- `supersede` on `prose_section` (compound: insert new + update old.superseded_by_id)
- `delete` on `prose_section` (soft-delete)
- `approve` on `prose_section` (status update + approval metadata)
- `bulk_supersede` on `prose_section` (batch, transactional)

Plus the operations on link tables and type table.

---

## 8. Migration Sequence (folded into DB-wide review Phase C)

Migration numbers assume M19+ are DB-hygiene migrations per the DB review design. Prose migrations follow.

| Mig | Description | Risk |
|---|---|---|
| M_P1 | `CREATE TABLE prose_section_type` + indexes | LOW |
| M_P2 | `CREATE TABLE prose_section` + indexes | LOW |
| M_P3 | `CREATE VIRTUAL TABLE prose_section_fts` + triggers | LOW |
| M_P4 | `CREATE TABLE prose_section_dimension_link` | LOW |
| M_P5 | `CREATE TABLE prose_section_finding_link` | LOW |
| M_P6 | Seed `prose_section_type` with initial catalogue | LOW |

Each migration follows DB review Phase C discipline: pre-check, post-check, backup, approval gate G3.

**Optional M_P7** — import existing `.md` prose as historical v1 rows. **PROPOSED:** deferred per earlier advice (new work only). If later desired, a separate migration + one-off import tool.

---

## 9. Supporting Routines (CC to build in DB review Phase D)

| Script | Purpose | Coordination with existing |
|---|---|---|
| `scripts/export_prose.py` | Round-trip export | New script |
| `scripts/import_prose.py` | Round-trip import | New script |
| `scripts/render_prose.py` | Publication output | Replaces manual markdown/docx assembly for sections-in-DB |
| `scripts/apply_session_patch.py` | Gains PROSE operations | Updated |
| `scripts/build_complete_extract.py` | Includes current approved prose sections in extract | Updated |
| `scripts/build_file_manifest.py` | Tracks prose export files | No change (file-aware already) |
| `scripts/export_database_schema.py` | Includes prose tables in schema doc | Auto via SQL introspection |

### 9.1 Import-tool testing harness

A small test harness `scripts/_test_prose_roundtrip.py`:
- Generates a fixture `.md` with N sections
- Imports (dry-run)
- Verifies plan matches expectation
- Imports (apply)
- Re-exports
- Asserts round-trip is byte-identical (modulo marker metadata updates)

Run as part of DB review Phase E verification.

---

## 10. Coordination With Other Design Docs

### 10.1 DB-wide review design

**Adds to Phase C scope:** migrations M_P1 through M_P6 (+ optional M_P7).
**Adds to Phase D scope:** new scripts (export/import/render), applicator updates.
**Adds to Phase E scope:** round-trip test harness.
**Adds to Phase F scope:** prose-aware schema JSON, CLAUDE.md §3 Table Group 17.

An update to the DB-wide review design doc carries these additions.

### 10.2 Readiness sweep design

**Proposed addition:** Phase R.H becomes "Prose coverage" — per registry, check:
- Are expected section types present for this registry's stage?
- Any approved sections with `word_count` outside expected range?
- Any draft sections older than N days (stale drafts)?
- Any sections with `superseded_by_id IS NULL AND status = 'archived'` (broken chain)?

Mechanical checks; adds ~15 minutes per registry pass.

**Action:** Update the sweep design doc after this design is approved.

### 10.3 Session B/C/D instructions

**Downstream updates** (not blocking for DB review — can land in their own session):
- Session B analysis output instruction: Stage 2c chapters are captured to DB via `.md` import
- Session C instruction: chapters produced in `.md`, imported to DB
- Session D instruction: synthesis narrative captured to DB

These instruction updates happen AFTER prose infrastructure lands, governed by standard instruction-update discipline.

---

## 11. Open Questions

Narrower now that Option D is accepted. Please answer inline.

### Q1 — Marker format: HTML comment vs fenced block

Options:
- (a) HTML comment (`<!-- PROSE_SECTION ... -->`) — invisible in markdown renderers, cleanest reading
- (b) Fenced code block (```prose-section ... ```) — visible but explicit
- (c) YAML frontmatter-style (`---\nprose_section:\n  id: 1234\n---`) — familiar pattern

My recommendation: **(a) HTML comment**. Invisible in preview; standard round-trip metadata pattern; survives most markdown processors.

**Your answer:**  
 
---

### Q2 — Migration import of existing prose (M_P7)

Should the migration sequence include importing the existing `.md` prose outputs from `outputs/markdown/`, `data/imports/WA/Session_B_Analysis/`, etc. as historical v1 rows?

Options:
- (a) Yes — import everything historical at adoption time
- (b) Selective — import only approved Session C outputs for the 6 completed words
- (c) No — new work only; historical `.md` remains on disk

My recommendation: **(c) No** — aligns with earlier advice (less risk, less scope). Historical files remain where they are. If a historical word is re-opened for revision, a one-off import can be run for just that word.

**Your answer:**  
 
---

### Q3 — Status vocabulary

Proposed statuses: `draft`, `in_review`, `approved`, `archived`.

Confirm or override?

My recommendation: keep the four as proposed.

**Your answer:**  
 
---

### Q4 — Section type catalogue seed

The seed in §4 is a skeleton. Please confirm the canonical Session B Stage 2c chapter structure (6 chapters — what are they named?) and Session C chapter structure (6 chapters × 3 lifecycle versions — v1/v2/v3 naming?).

Alternatively, mark this as "fill in later, once instructions are finalised" — seed can be populated incrementally.

**Your answer:**  
 
---

### Q5 — Conflict handling default

On import, if DB version has advanced since export:
- (a) HALT (safest — no silent overwrites)
- (b) PROMPT (ask per section)
- (c) FORCE-OVERWRITE (overrides silently — dangerous)

My recommendation: **(a) HALT by default**, with explicit `--on-conflict=force-overwrite` flag available for deliberate overrides.

**Your answer:**  
 
---

### Q6 — Per-section vs per-file transactions

On bulk import, wrap:
- (a) All sections in one transaction — atomic; one failure rolls back all
- (b) Each section in its own transaction — partial success possible
- (c) Configurable — default (a), flag for (b)

My recommendation: **(c) Configurable; default (a)**.

**Your answer:**  
 
---

### Q7 — Link tables

`prose_section_dimension_link` and `prose_section_finding_link` are proposed. They enable "show all prose about finding X" queries. Useful now, or defer?

My recommendation: **Include from start (M_P4, M_P5)**. Low cost; high future value; uses confirmed analytical links.

**Your answer:**  
 
---

### Q8 — Publication rendering

`render_prose.py` produces `.md`/`.docx` outputs for publication. Target location:
- (a) `outputs/markdown/` and `outputs/docx/` (current convention)
- (b) New locations `outputs/prose_md/` and `outputs/prose_docx/`
- (c) Configurable

My recommendation: **(a)** — use existing output locations; file manifest tracks them.

**Your answer:**  
 
---

## 12. Summary of Commitments If Approved

Upon approval of this design and the updated DB-wide review design:

1. DB-wide review instruction v1.0 produced; includes prose migrations in Phase C
2. Migrations M_P1–M_P6 designed, dry-run, applied under Phase E approval gates
3. Round-trip scripts produced: `export_prose.py`, `import_prose.py`, `render_prose.py`
4. Applicator updated for `PROSE` patch type and operations
5. Test harness `_test_prose_roundtrip.py` exercised in Phase E
6. Schema JSON + CLAUDE.md updated in Phase F
7. Session B/C/D instructions updated in subsequent sessions (not blocking DB review)
8. Readiness sweep design updated to include optional prose coverage phase

---

## 13. Approval

**Researcher approval — write below:**

Status: [ X] APPROVED — PROCEED  [ ] REVISIONS REQUESTED — see markup

Date:  
Reviewer: le Roux Cilliers
Notes:  

---

*End of design workings v1 — 2026-04-19*
