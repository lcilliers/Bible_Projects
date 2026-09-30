# Storing Prose/Narrative Analysis in SQLite — Advice

| Field | Value |
|---|---|
| Filename | prose-in-sqlite-advice-v1-20260419.md |
| Status | **RESOLVED 2026-04-19** — researcher approved Option D; directed to fold infrastructure + routines into the DB-wide review. Follow-on design doc created. |
| Purpose | Respond to researcher question about storing Session B/C/D prose analysis in SQLite rather than `.md` files. Recommends an architecture and flags what must be decided before committing. |
| Resolution outcome | Option D adopted. Scope folded into DB review (not deferred as originally recommended). See `wa-prose-store-design-v1-20260419.md` for schema and round-trip tooling detail. |
| Relates to | `wa-global-database-review-design-v1-20260419.md` (updated 2026-04-19 PM with prose scope) · `wa-prose-store-design-v1-20260419.md` (new detailed design) |
| Produced | 2026-04-19 |

---

## 1. Top-Line Advice

**Yes, this is a sound direction — with one important caveat.** SQLite handles large text well; your stated goal (systematic cross-word edits) is exactly what relational storage enables. But the *editing and review workflow* is where files currently shine. The optimal architecture keeps the DB as canonical store while preserving `.md` round-tripping for edits and reviews.

Recommended architecture (detail in §4): **DB-canonical with file round-trip and FTS5 indexing**.

Caveat: adopting this adds meaningful scope to the DB-wide review work (new tables, new patch operations, new round-trip scripts). Do not adopt lightly — but if adopted, fold it into that instruction now rather than retrofitting later.

---

## 2. SQLite's Technical Fitness for Large Prose

Summary: **SQLite is well-suited to this.** The project already uses it. No external dependency needed.

| Concern | Reality | Notes |
|---|---|---|
| Column size limit | 1 GB default, 2 GB max per TEXT value | Prose chapters typical 2–20 KB — trivial |
| DB size growth | ~10 KB/section × 214 words × 6 sections × 3 versions ≈ 38 MB added | Current DB ~40 MB; total under 100 MB — no concern |
| Query performance on large TEXT | Indexed columns stay fast; TEXT body retrieved as needed | Store `word_count`, `section_type`, `status` as indexed columns; prose is payload |
| Full-text search | FTS5 virtual tables: excellent, mature, supports phrase/prefix/BM25 ranking | Built-in to SQLite; no extension install |
| Concurrent write safety | WAL mode (already enabled) handles single-writer/multi-reader | Adequate for this workflow |
| Backup cost | Proportional to size; backups remain fast | Already in rolling-10 strategy |
| Text encoding | UTF-8 native | Matches project standard |

**Non-issues often raised that do not apply here:**

- "SQLite isn't for blobs/documents" — folklore from document-DB marketing. TEXT columns up to GB scale are routine. SQLite is used by Chrome, iOS, Android, aircraft avionics.
- "Use PostgreSQL for full-text" — FTS5 is competitive for this corpus size. PostgreSQL would add infrastructure burden for zero programme benefit.
- "TEXT vs BLOB" — TEXT for UTF-8 narrative; BLOB only for binary (images, etc.). Use TEXT.

**Tunable for prose-heavy content:**

- `PRAGMA page_size = 8192;` — larger pages reduce overflow for typical prose. Apply only if audit shows overflow pressure; otherwise keep default 4096.
- `PRAGMA journal_mode = WAL;` — already in place.
- `PRAGMA synchronous = NORMAL;` — already reasonable; prose writes are not transactional-hot.

---

## 3. What You Gain, What You Lose

### Gain

| Capability | Enabled by | Programme value |
|---|---|---|
| "Update section X across all words" | SQL UPDATE with WHERE section_type | HIGH — your stated goal |
| "Compare how 'Theological' is framed across all words" | SELECT with JOIN on dimension | HIGH — analytical consistency |
| "Find all sections mentioning 'covenant'" | FTS5 MATCH query | HIGH — cross-word exploration |
| Version history per section | supersedes_id chain | HIGH — lifecycle management |
| Metrics: word counts, revision dates, author attribution | Direct columns | MEDIUM — quality audit |
| Cross-reference sections ↔ findings ↔ dimensions | FK joins | HIGH — coherence checks |
| Programmatic regeneration of word study outputs | SELECT → render | HIGH — publication pipeline |
| Single source of truth | Canonical store | HIGH — ends "which file has the latest" |

### Lose

| Capability | Lost when prose moves to DB | Mitigation |
|---|---|---|
| Git diffs on prose edits | DB rows are opaque to Git | Export to `.md` at milestones; commit those as snapshots |
| Branch-based review of prose | Can't checkout a branch of DB rows | Export-to-branch workflow; or markup the export `.md` |
| Editing in IDE / Obsidian / Typora | DB isn't a file | Round-trip tool: export section → edit `.md` → import |
| `grep`/ripgrep across prose | Searches miss DB content | FTS5 replaces; also optional export snapshot for grep |
| Portable without DB software | Need SQLite to read | Exports give portability at snapshot points |
| Claude AI's current output format | Claude AI writes `.md`, not DB rows | Claude AI continues to write `.md`; CC imports to DB via patch |

**The lose column is real. The mitigations work, but they are tooling that must be built.**

---

## 4. Four Architectural Options

### Option A — DB-canonical, DB-only

Prose lives in DB. Edits happen via SQL or via a custom editor. No file mirror.

- Pros: simplest data model; no sync concerns
- Cons: editing UX is poor without a custom tool; reviews are awkward; Git is blind to content

**Not recommended** — the editing friction will cause operational pain.

### Option B — Files canonical, DB as metadata index

Files remain source of truth. DB stores pointers + extracted metadata (word_count, section_type, last_modified).

- Pros: preserves current workflow; low migration cost
- Cons: no cross-word SQL on content; FTS requires indexing step; "update section X across words" still means editing 214 files

**Suitable as an interim step** — gains metadata queries without committing to DB-canonical.

### Option C — Files canonical, DB as materialised view

Files are source. A sync script parses `.md` into DB rows, kept in lockstep.

- Pros: edit in files; query in DB; FTS works; one-way flow is simple
- Cons: sync process to maintain; parse errors; DB writes are regeneration only (not authoring); still 214 files for programme-wide edits

**Suitable if you prefer a file-first workflow** — gains query power without committing to DB-authoring.

### Option D — DB canonical, file round-trip for editing ⭐ *Recommended*

DB is source of truth. Edits export to `.md`, are made in the file, then imported back as a new revision row.

- Pros: cross-word SQL operations are native; FTS native; "update section X across all 214 words" is one SQL statement (with approval gates); edit UX preserves file-based comfort; full version history retained
- Cons: requires round-trip tooling; research workflow must adapt to "DB is the truth, file is the scratchpad"; patch/directive vocabulary extended

**Recommended for your stated goal.** The cost is tooling (new scripts + schema); the benefit matches your operational need.

---

## 5. Recommended Schema (if Option D adopted)

### 5.1 Core table

```sql
CREATE TABLE prose_section (
  id INTEGER PRIMARY KEY,
  registry_id INTEGER NOT NULL REFERENCES word_registry(id),
  section_type_id INTEGER NOT NULL REFERENCES prose_section_type(id),
  chapter_no INTEGER,
  heading TEXT,
  body TEXT NOT NULL,
  word_count INTEGER NOT NULL,
  source TEXT NOT NULL,  -- session_b_stage2c / session_c_v1 / session_c_v2 / session_d / etc.
  status TEXT NOT NULL,  -- draft / in_review / approved / archived
  version INTEGER NOT NULL DEFAULT 1,
  supersedes_id INTEGER REFERENCES prose_section(id),
  author TEXT NOT NULL,  -- claude_ai / claude_code / researcher
  created_at TEXT NOT NULL,
  approved_at TEXT,
  approved_by TEXT,
  metadata_json TEXT,  -- e.g. {"dimension_ids": [12,15], "finding_ids": [234]}
  delete_flagged INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX idx_prose_registry_section
  ON prose_section(registry_id, section_type_id, status)
  WHERE delete_flagged = 0;

CREATE INDEX idx_prose_current
  ON prose_section(section_type_id, status)
  WHERE delete_flagged = 0 AND supersedes_id IS NULL;
```

### 5.2 Section type dictionary

```sql
CREATE TABLE prose_section_type (
  id INTEGER PRIMARY KEY,
  code TEXT UNIQUE NOT NULL,     -- e.g. 'sb_ch2_meaning', 'sc_v1_ch1_intro'
  label TEXT NOT NULL,            -- human-readable
  source_stage TEXT NOT NULL,     -- session_b / session_c / session_d
  lifecycle_version INTEGER,      -- for Session C: 1/2/3
  chapter_no INTEGER,
  description TEXT,
  delete_flagged INTEGER NOT NULL DEFAULT 0
);
```

This removes free-text drift in `section_type` strings.

### 5.3 FTS5 virtual table

```sql
CREATE VIRTUAL TABLE prose_section_fts USING fts5(
  body, heading,
  section_type UNINDEXED,
  registry_id UNINDEXED,
  content='prose_section',
  content_rowid='id',
  tokenize='porter unicode61'
);

-- Triggers for sync
CREATE TRIGGER prose_section_ai AFTER INSERT ON prose_section BEGIN
  INSERT INTO prose_section_fts(rowid, body, heading, section_type, registry_id)
    VALUES (new.id, new.body, new.heading, new.section_type_id, new.registry_id);
END;
-- Plus AU (update), AD (delete) triggers — standard FTS5 pattern.
```

Usage:
```sql
-- Find all sections mentioning 'covenant'
SELECT ps.registry_id, wr.word, pst.label, snippet(prose_section_fts, 0, '«', '»', '...', 16) AS ctx
FROM prose_section_fts
JOIN prose_section ps ON ps.id = prose_section_fts.rowid
JOIN word_registry wr ON wr.id = ps.registry_id
JOIN prose_section_type pst ON pst.id = ps.section_type_id
WHERE prose_section_fts MATCH 'covenant'
  AND ps.status = 'approved' AND ps.delete_flagged = 0
ORDER BY bm25(prose_section_fts);
```

### 5.4 Optional: section → dimension/finding link tables

```sql
CREATE TABLE prose_section_dimension_link (
  prose_section_id INTEGER NOT NULL REFERENCES prose_section(id),
  dimension_id INTEGER NOT NULL,  -- FK to wa_dimension_index (if retained)
  PRIMARY KEY (prose_section_id, dimension_id)
);

CREATE TABLE prose_section_finding_link (
  prose_section_id INTEGER NOT NULL REFERENCES prose_section(id),
  finding_id INTEGER NOT NULL REFERENCES wa_session_b_findings(id),
  PRIMARY KEY (prose_section_id, finding_id)
);
```

These let you ask: "Show me all Session B Stage 2c chapter 3 sections that reference finding X". Powerful for coherence audits.

---

## 6. Round-Trip Tooling (Option D)

Three scripts needed:

| Script | Purpose | Output |
|---|---|---|
| `scripts/export_prose.py` | Export a section (or batch) from DB to `.md` file for editing | `outputs/prose_edits/wa-{nnn}-{word}-{section_code}-v{n}-{date}.md` |
| `scripts/import_prose.py` | Import edited `.md` back into DB as a new version row (supersedes current) | DB row written; old row flagged superseded |
| `scripts/render_prose.py` | Regenerate publication `.md`/`.docx` from current approved sections | `outputs/markdown/` and `outputs/docx/` |

Round-trip discipline:
1. Export section → edit `.md` → import
2. Import creates a new row (`version = N+1`, `supersedes_id = old_id`)
3. Status transitions: `draft` → `in_review` → `approved`
4. On approve: render publication formats

### Round-trip safety

- Import requires the exported file to carry a machine-readable header (`<!-- prose_section_id: 1234; version: 2 -->`) so the target row is unambiguous.
- Edit-without-export is detected on import: if header is missing, import refuses.
- Conflict detection: if target row's version has changed since export, import halts with a merge prompt.

---

## 7. Patch System Implications

To integrate with existing patch discipline:

### 7.1 New operation types required

| Operation | Table | Purpose |
|---|---|---|
| `insert` on `prose_section` | Create new section | New Claude AI output |
| `update` on `prose_section` (via supersede) | Revise a section | Always insert-then-supersede, never in-place update |
| `approve` on `prose_section` | Status transition draft → approved | Gated, with approver |
| `bulk_supersede` on `prose_section` | Programme-wide edit | Your stated use case |

### 7.2 New patch type

**Proposed:** `PROSE` patch type — carries prose_section operations. Separate from analytical patches to keep approval reviews focused.

Filename: `wa-{nnn}-{word}-prose-v{n}-{date}.json` per registry; or `wa-global-prose-{descriptor}-v{n}-{date}.json` for programme-wide.

### 7.3 Approval discipline for programme-wide edits

"Update section X across all 214 words" is potentially destructive. Suggested protocol:
1. Claude AI drafts the change as a *pattern* (what to change, in what words)
2. CC generates a preview: shows N sample diffs + full impact list
3. Researcher approves the pattern
4. CC applies as a single `bulk_supersede` patch; each affected row gets a new version
5. Rollback: re-run supersede in reverse; old versions are still present

### 7.4 Extract implications

`build_complete_extract.py` and friends must include approved prose sections in their output for Claude AI to read. This is a schema-aware change but low risk (additive to extracts).

---

## 8. Migration Path — If Adopted Into DB-Wide Review

### 8.1 New migrations required

| Migration | Purpose | Risk |
|---|---|---|
| M19 (or later) — prose schema | `CREATE TABLE prose_section`, `prose_section_type`, FTS5, triggers | LOW — pure additive |
| M20 — link tables | Dimension / finding link tables | LOW — additive |
| M21 — seed section types | Populate `prose_section_type` with canonical Session B/C/D codes | LOW — data-only |
| M22 — import existing prose | Bulk-import current `.md` outputs into DB | MEDIUM — data migration; needs audit after |

### 8.2 New scripts required

- `scripts/export_prose.py`, `scripts/import_prose.py`, `scripts/render_prose.py` (round-trip)
- `scripts/migrate_prose_from_files.py` (one-off for M22)
- `scripts/apply_session_patch.py` updates (new operation types)

### 8.3 Governing document updates

- Session B analysis output instruction: add prose DB capture step
- Session C instruction: same
- Session D instruction: same
- Patch instruction: document `PROSE` type + operations
- CLAUDE.md §3 table groups: add "Table Group 17 — Prose"
- CC instruction: new responsibilities (prose round-trip, programme-wide edits)

### 8.4 Scope impact on DB-wide review

**If adopted:** adds ~4 migrations + 3 new scripts + 5 governing document edits. Not trivial but tractable. Clean fit with Phase C/D/F of the DB-wide review.

**If deferred:** no impact on current DB-wide review; can be added later as a separate M{n} migration sequence without re-opening the completed review.

---

## 9. Impact on Readiness Sweep

**Low to moderate.**

If adopted: the sweep gains a new Phase R.H (prose coverage) — per registry, check whether expected section types are present, word counts in range, status = approved. Adds one phase; mechanics are straightforward.

If deferred: no impact. Sweep proceeds as designed.

---

## 10. Honest Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Round-trip tool bugs cause silent edit loss | MEDIUM initially | HIGH | Header-based export/import; version conflict detection; always write new row, never overwrite |
| Programme-wide edits applied wrongly across 214 words | LOW if gated | VERY HIGH | Multi-step approval with preview + sample diffs; idempotent supersede (old versions retained) |
| Researcher workflow disruption during transition | MEDIUM | MEDIUM | Migration phased: start with new output (Session C going forward) rather than retrofitting Session B archives |
| Git history loses fidelity on prose evolution | HIGH | LOW-MEDIUM | Periodic exports committed to repo as snapshots; DB has its own version chain |
| Review workflow becomes DB-centric | MEDIUM | MEDIUM | Export to `.md` for review; reviewer marks up the file; import accepts markup |

---

## 11. Open Design Questions

Mark up inline.

### Q1 — Scope of prose types to move to DB

Options:
- (a) All Session B, C, D outputs
- (b) Only Session C (reader-facing word study) — the main publication surface
- (c) Only Session B Stage 2c chapters — where cross-word consistency matters most
- (d) Defer entirely; keep files for now

My recommendation: **(c) first**, then expand to (a) if the workflow settles in.

**Your answer:**  
 
---

### Q2 — Timing relative to DB-wide review

Options:
- (a) Fold into the current DB-wide review — extra scope, but clean
- (b) Separate follow-on review — DB review completes cleanly; prose adopted later
- (c) Not now — decide after DB review finishes and programme state is clearer

My recommendation: **(b)** — complete the core DB hygiene first; adopt prose store as a focused follow-on once tooling for it is scoped.

**Your answer:**  
 
---

### Q3 — Current `.md` corpus migration

If adopted: what happens to the existing `outputs/markdown/`, `outputs/docx/`, analysis outputs in `data/imports/WA/Session_B_Analysis/`, etc.?

Options:
- (a) Migrate all existing prose into DB as historical v1 rows
- (b) Leave existing; only new prose goes into DB
- (c) Migrate selectively — Session C-ready words only

My recommendation: **(b) then (c) on demand** — new work uses DB; historical `.md` remains where it is; per-word migration triggered by re-opening a word for revision.

**Your answer:**  
 
---

### Q4 — Review workflow preservation

How do you currently review Claude AI's prose outputs? (In IDE markdown preview? In Obsidian? Exported to PDF?)

This is important input for round-trip tool design. If your review is markdown-preview-in-IDE, the export `.md` format should preserve your heading style, admonition blocks, etc.

**Your answer:**  
 
---

### Q5 — Programme-wide edits — appetite

How often do you envision needing to update "the same section across all words"?
- A few times per year at milestone consolidations?
- Routinely during development as conventions evolve?
- Rarely — goal is cross-word *query*, not cross-word *edit*?

Answer shapes how much investment goes into the `bulk_supersede` approval pipeline.

**Your answer:**  
 
---

### Q6 — FTS priority

Full-text search across all prose is a headline benefit of this architecture. Is cross-word search:
- Core to the workflow (FTS5 from day one)
- Useful but not urgent (add after core tables in place)
- Not a priority (may defer)

**Your answer:**  
 
---

### Q7 — Versioning granularity

Options for version semantics:
- (a) Every import creates a new version row (fine-grained; DB grows faster)
- (b) Only status transitions create new versions (draft → approved = new row; draft → draft = overwrite)
- (c) Hybrid: drafts overwrite; approved always creates new

My recommendation: **(c)** — drafts are cheap; approved is the artefact of record and must be immutable.

**Your answer:**  
 
---

### Q8 — Claude AI author workflow

Currently Claude AI writes `.md` files as part of Session B/C outputs. In the DB-canonical model, the flow becomes:
- Claude AI writes `.md` file (as today)
- CC imports `.md` into DB as a new row
- Researcher reviews in DB (via export round-trip)

This preserves Claude AI's writing pattern while moving the source of truth.

Alternative: Claude AI writes directly into DB via patch operations.

My recommendation: **Preserve `.md` writing; CC imports** — least disruption to Claude AI's successful pattern.

**Your answer:**  
 
---

## 12. Summary Recommendation

| Topic | Recommendation |
|---|---|
| Adopt DB storage for prose? | **Yes** — technical fit is strong; stated goal genuinely wants it |
| Architecture | **Option D — DB-canonical with file round-trip + FTS5** |
| Timing | **Defer to follow-on after DB-wide review completes** — keep scope focused |
| Initial scope | **Session B Stage 2c chapters first** — most consistency-critical surface |
| Migration of existing prose | **New work only; historical on demand** |
| Round-trip tooling | **Build before enabling** — don't rely on raw SQL editing |
| Programme-wide edits | **Gated via preview + multi-step approval** — power tool needs safety |
| Schema pre-commit | Use schema shown in §5 as starting point; refine in the follow-on review |

---

## 13. Relationship to Current Design Docs

- The DB-wide review (v1) does **not** currently include prose storage. Recommend keeping it that way — finish DB hygiene first.
- The readiness sweep (v1) does **not** currently include prose coverage checks. Can be added later as a new phase when prose adoption lands.
- A third design doc would be produced at adoption time: `wa-prose-store-design-v1-{date}.md`.

---

## 14. Approval

No approval needed on this advice doc itself. It exists to inform your decision on Q1–Q8. Mark up your answers when ready; if you want to proceed, I will:
1. Produce `wa-prose-store-design-v1-{date}.md` (separate design doc)
2. Update the DB-wide review design to note the follow-on work
3. Produce the actual instruction artefacts after both design docs are approved

Status: [ ] ADVICE ACCEPTED — PRODUCE PROSE DESIGN DOC  [ ] ADVICE ACCEPTED — DEFER PROSE ADOPTION  [ ] REVISIONS REQUESTED

Date:  
Reviewer: le Roux Cilliers
Notes:  

---

*End of advice v1 — 2026-04-19*
