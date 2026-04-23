# Prose Store — Architecture and Stages of Development

**Purpose:** single-page architectural summary of how the programme's prose lives in the database — what tables hold it, how it is scoped, what stages of research it spans, how it is authored, and how it is retrieved.

**Canonical design source:** [wa-prose-store-design-v1-20260419.md](../outputs/investigations/wa-prose-store-design-v1-20260419.md). This doc summarises what was built and what is currently in use; the design doc contains the deeper reasoning, trade-offs, and researcher decisions.

---

## 1. At a glance

```
┌─ DB (canonical) ─────────────────────────────────────────┐
│                                                          │
│   prose_section_type  (dictionary of section handles)    │
│          │                                               │
│          ▼                                               │
│   prose_section  ───────►  prose_section_fts  (FTS5)     │
│     │        │                                           │
│     │        ├──►  prose_section_dimension_link          │
│     │        └──►  prose_section_finding_link            │
│     │                                                    │
│     └──►  supersedes_id / superseded_by_id (versioning)  │
│                                                          │
└──────────┬───────────────────────────▲───────────────────┘
           │                           │
   build_programme_                    │
   prose_extract.py              apply_session_patch.py
           │                           │
           ▼                           │
  data/exports/reference/        patch files (CATALOGUE_POPULATION + PROSE)
  outputs/docx/                        ▲
           │                           │
           ▼                           │
    .md / .docx for reading     .md drafts in data/imports/WA/Prose/
```

**Single working sentence:** the database is the authoritative memory of the programme's interpretation; `.md` and `.docx` are scratchpads for authoring and readable exports for humans.

---

## 2. Core concept — DB-canonical with file round-trip

Prose lives in relational rows, not in files. Every analytical paragraph written by the programme — governance prose, per-word analysis, cross-registry synthesis — is a row in `prose_section`. Files are:

- **Inputs** — draft `.md` authored by Claude AI, wrapped in a PROSE patch, applied to the DB through the standard applicator.
- **Outputs** — fresh extracts (JSON / MD / DOCX) produced from the DB on demand.

Consequences of this choice:

- Prose becomes queryable alongside the evidence it rests on. A question like _"show every observation about directional determination across all clusters"_ has an answer that does not depend on anyone remembering which session it came from.
- Prose carries provenance through its `section_type_id` (what section of the programme it is) and its `registry_id` (which word it concerns, or `NULL` for programme-wide).
- Synthesis becomes auditable. A finding can be traced back to a specific prose row keyed to specific evidence rather than to "a session log somewhere".

---

## 3. Schema — four tables and an FTS index

### 3.1 `prose_section_type` — the dictionary

One row per section-handle. A handle is a stable, named slot that prose can be written into (e.g. `prog_disc_traceability` = "Traceability and evidential warrant" in the programme chapter on disciplines).

Key columns:

| Column | Purpose |
|---|---|
| `code` | Stable machine identifier, globally unique (e.g. `prog_purp_mission`, `sb_ch2_meaning`, `sc_v2_ch4_exegesis`). |
| `label` | Human heading (used in extracts and renderings). |
| `source_stage` | Which research stage this section belongs to (see §5). |
| `lifecycle_tag` | For staged rewrites — e.g. `v1` / `v2` / `v3` for Session C's three-pass lifecycle; `NULL` otherwise. |
| `chapter_no` | Chapter number where applicable (programme prose, Session B, Session C). `NULL` for freeform or synthesis prose. |
| `description` | Short stub telling an authoring session what the prose under this handle should cover. |
| `expected_length_min` / `_max` | Optional word-count guide for the author. |
| `sort_order` | Render order inside a chapter. |

### 3.2 `prose_section` — the content

One row per authored prose body. Key columns:

| Column | Purpose |
|---|---|
| `section_type_id` | FK to the handle. Required. |
| `registry_id` | FK to `word_registry`. `NULL` → programme-wide; non-null → scoped to a single word. |
| `heading` | Rendered heading; overrides the type label where set. |
| `body` | The prose itself. UTF-8, markdown-compatible. |
| `word_count` | Derived at insert. |
| `status` | Lifecycle — `draft` / `in_review` / `approved` / `archived` (see §6). |
| `version` | Starts at 1; increments on supersede. |
| `supersedes_id` / `superseded_by_id` | Version chain — the revision history is in the rows, not in diffs. |
| `author` | `claude_ai` / `claude_code` / `researcher`. |
| `approved_at` / `approved_by` | Set by the `approve` op. |
| `source_file` | The `.md` draft the prose was authored in (provenance). |
| `metadata_json` | Free-form metadata (rarely needed). |
| `delete_flagged` | Soft delete. |

### 3.3 `prose_section_fts` — full-text search

Virtual FTS5 index over `prose_section` (shadow tables `_data` / `_idx` / `_content` / `_docsize` / `_config`). Kept in sync by triggers. Enables phrase and proximity search across every prose row the programme has authored.

### 3.4 Link tables — structural joins

- `prose_section_dimension_link` — a prose row `discusses` (or similar `link_type`) a dimension record. Lets dimensional syntheses pull every prose that engages a given dimension across the programme.
- `prose_section_finding_link` — a prose row `discusses` a Session B finding. Lets a finding surface the prose that elaborates it.

Both are simple junction tables with a `link_type` vocabulary and `created_at` stamp.

---

## 4. Scope — programme-wide vs registry-scoped

The `registry_id` field carries scope:

| `registry_id` | Meaning | Examples |
|---|---|---|
| `NULL` | Programme-wide: applies to the whole study, not a single word. | Programme chapters (purpose, method, research approach, data architecture, governance, instruction corpus). |
| Integer | Registry-scoped: applies to one word (registry_id = word_registry.id). | Session A extracts for a specific word; Session B analysis of "anger"; Session C word study of "love". |

This field was made nullable in directive `DIR-20260421-002` (schema enablement) to allow programme-wide prose. Prior to that change the programme-wide chapters could not be authored through the normal patch pipeline.

---

## 5. Stages of development — `source_stage`

Prose in the programme is authored at five distinct research stages. Each stage has its own set of section handles, its own authoring rules, and its own position in the programme workflow.

### 5.1 `programme` — governance and orientation

**Authored by:** Claude AI, with researcher direction.
**Scope:** `registry_id = NULL` (programme-wide).
**Structure:** organised into 6 macro chapters × ~45 sub-sections per the working structure design ([programme-prose-structure-design-v1-20260421.md](../outputs/investigations/programme-prose-structure-design-v1-20260421.md)):

| Ch | Macro area | Subject |
|---:|---|---|
| 1 | Programme purpose | Mission, scope, the inner-being frame, defining inner being, science and the Bible, expected outcome. |
| 2 | Research methodology | Research method, word selection and registry, programme flow, science in action, publishing, key principles, key constraints. |
| 3 | Research approach | Tool selection, STEP foundation, two-AI division, data management, process instructions, evidential principles, verse authority, analytics and question catalogue, memory management, inner-being filter. |
| 4 | Data architecture | Database, registry, terms, ownership and XREF, verse groups, anchor verse, dimensions, questions, inter-word relationships. |
| 5 | Data integrity and governance | Delete discipline, validation, backup, patch failure, finding references, STEP data provenance. |
| 6 | Instruction corpus | Global rules, referencing, authority, instruction versioning (`[current]`), update flow, directive vs patch, override protocol. |

Programme prose is where the database explains itself — the discipline, the architecture, the research method — in prose the programme can read back later and that survives any single session's recollection.

### 5.2 `session_a` — mechanical per-word extracts

**Authored by:** Claude Code (`author = 'claude_code'`).
**Scope:** per-registry (`registry_id` non-null).
**Semantics:** Session A prose is derived from structured data — the registry record, the extracted terms, the lexical layer. It is not analytical judgement; it is a prose view of data the database already holds. Section handles cover the standard sections of the per-word Session A extract (synopsis, term inventory summary, verse coverage overview, lexical notes, etc.).

Because Session A prose is mechanical and reproducible, it has a unique operation — `session_a_replace` — which permits in-place update by Claude Code. No other stage permits in-place updates.

### 5.3 `session_b` — analytical output per word

**Authored by:** Claude AI.
**Scope:** per-registry.
**Structure:** follows the Session B analytical-output chapters (6 chapters, per [current] `wa-sessionb-analysis-output`). Each chapter has its own section handle. Produced as part of the Type (b) SESSIONB patch at Session B completion.

Session B prose answers the standing catalogue of questions for a word, captures findings, and provides the narrative substrate for the per-word written study that follows.

### 5.4 `session_c` — reader-facing word study (v1 → v2 → v3 lifecycle)

**Authored by:** Claude AI.
**Scope:** per-registry.
**Structure:** 6 chapters, three lifecycle versions per chapter — `lifecycle_tag IN ('v1', 'v2', 'v3')`.

Session C is the publishable word study, produced in three passes:

- **v1** — initial draft drawn directly from Session B findings.
- **v2** — refinement after cross-registry context (Session D pointers raised in B may reshape framing).
- **v3** — final reader-facing version after researcher review.

The lifecycle is carried in `prose_section_type.lifecycle_tag` so that each pass is its own section handle. Rows do not supersede across versions — `v1` content stays; `v2` and `v3` are separate handles holding the successive passes.

### 5.5 `session_d` — cross-registry synthesis

**Authored by:** Claude AI.
**Scope:** typically `NULL` (cross-registry) or scoped to a synthesis registry where the programme has one.
**Structure:** synthesis-specific handles — clustering rationale, dimensional comparison, inter-word relationship commentary, cross-registry findings.

Session D prose is the layer where cross-word observations raised as SD pointers during Session B are elaborated into comparative analysis.

---

## 6. Lifecycle — draft, supersede, approve, archive

Status transitions for a `prose_section` row:

```
    draft ──────► in_review ──────► approved ──────► archived
      │                │                │                │
      └────────────────┴────────────────┴───► superseded (new row, supersedes_id linked)
                                                        │
                                             or delete_flagged = 1 (soft retire)
```

### 6.1 Supersede-only discipline for narrative prose

Narrative prose is immutable at the row level. A revision creates a new row with `version = old.version + 1`, `supersedes_id = old.id`, and the old row's `superseded_by_id = new.id`. The row history is queryable; no edit is ever silently lost.

Only Session A mechanical extracts permit in-place update, through the `session_a_replace` operation. That operation is gated on `author = 'claude_code'`.

### 6.2 Soft delete

`delete_flagged = 1` retires a row. No physical DELETE is supported by the applicator. This matches the programme's broader soft-delete discipline.

---

## 7. Authoring flow — the two-patch pattern

A new prose chapter (programme or otherwise) reaches the database in two patches, applied in order through the standard applicator [scripts/apply_session_patch.py](../scripts/apply_session_patch.py):

**Patch 1 — `CATALOGUE_POPULATION`.** One `insert` per new `prose_section_type` row. Creates the handles (section codes + labels + descriptions + chapter numbers + length guides) that the content will slot into. Uses `INSERT OR IGNORE` on `code` so a duplicate run is a no-op.

**Patch 2 — `PROSE`.** One `insert` per `prose_section` row. Each insert references its handle by `section_type_id_lookup: {"code": "..."}` so the content patch does not need the integer IDs assigned by Patch 1 — the applicator resolves the code at apply time.

Both patches are null-exempt for `session_b_status`. Both take pre-apply backups and are archived to `archive/patches/` on success.

Worked precedent now in the commit history:

- Chapter 0 + 1 seeded: commit `1301f81`.
- Chapter 2 seeded + preamble revised: commit `62c01ba`.
- Chapter 3 seeded: commit `8d14c83`.

### 7.1 Revisions

A revision follows the same shape but uses the `supersede` operation on `prose_section`. The applicator writes the new row, sets `supersedes_id` / `superseded_by_id`, and transfers any approval state per instruction.

### 7.2 Status transitions

- `approve` — sets status to `approved`, stamps `approved_at` + `approved_by`.
- `delete` — soft-retires (`delete_flagged = 1`).
- `bulk_supersede` — systematic rewrite using a target list + record template, for programme-wide refactors.

---

## 8. Retrieval

### 8.1 Extracts

[scripts/build_programme_prose_extract.py](../scripts/build_programme_prose_extract.py) produces the programme-prose extract in three formats:

- **JSON** — machine-readable state; metadata always; bodies included with `--include-body`.
- **Markdown** — readable view grouped by chapter, bodies inline.
- **DOCX** — reader-facing Word document (for review in Drive).

Output paths: [data/exports/reference/](../data/exports/reference/) for JSON/MD; [outputs/docx/](../outputs/docx/) for DOCX.

### 8.2 FTS5 search

`prose_section_fts` supports phrase and proximity search across every prose row in the database. Useful for "show me every passage that mentions X across all stages".

### 8.3 Round-trip editing via `.md` markers

Per the design, `.md` scratchpads carry `<!-- PROSE_SECTION id: NNNN -->` markers that let an import routine route each section back to its DB row. An `.md` can hold any number of sections in any order; the import places each where it belongs. (Import tooling is part of the prose-store design; availability of the generic round-trip script is tracked separately from this architectural summary.)

---

## 9. Current state (as of 2026-04-23)

Verified by direct DB query:

| Stage | Section types seeded | Prose rows (active) |
|---|---:|---:|
| `programme` | 28 | 21 |
| `session_a` | 6 | 0 |
| `session_b` | 5 | 0 |
| `session_c` | 5 | 0 |
| `session_d` | 10 | 0 |
| **Total** | **54** | **21** |

Programme-prose chapter coverage:

| Chapter | Section types | Status |
|---|---:|---|
| ch 0 | 1 | seeded |
| ch 1 | 6 | seeded + populated |
| ch 2 | 7 | seeded + populated |
| ch 3 | 6 | seeded + populated |
| (no chapter assigned — legacy M34 seed) | 8 | pending rename into current structure |
| ch 4 – 6 | 0 | pending seed |

All 21 populated programme prose rows are at `status = 'draft'`. No rows have been moved to `in_review` or `approved` yet.

---

## 10. Why this matters (the working principle)

The prose store establishes the database as the programme's analytical memory, not just its evidentiary substrate. Claude AI does not live inside the database; Claude AI is an analytical instrument applied to snapshots drawn from it. Prose written to the database is prose written to survive a session boundary — self-contained, scoped, grounded in the evidence it rests on.

This principle is recorded in full in [WA-WorkingMemoryAndSnapshots-v1.0-2026-04-21.md](../data/imports/WA/Workflow/methodology_logs/WA-WorkingMemoryAndSnapshots-v1.0-2026-04-21.md). The prose store is that principle made operational: the database carries interpretation as well as evidence, and interpretation held in the database survives session boundaries the way evidence does.

---

## 11. References

| Doc | Purpose |
|---|---|
| [wa-prose-store-design-v1-20260419.md](../outputs/investigations/wa-prose-store-design-v1-20260419.md) | Full design workings, schema rationale, round-trip tooling design. |
| [prose-in-sqlite-advice-v1-20260419.md](../outputs/investigations/prose-in-sqlite-advice-v1-20260419.md) | Decision record: Option D (DB-canonical) adopted 2026-04-19. |
| [programme-prose-structure-design-v1-20260421.md](../outputs/investigations/programme-prose-structure-design-v1-20260421.md) | Proposed 6-chapter × 45-sub-section structure for programme prose. |
| [prose-instructions-compatibility-review-v1-20260421.md](../outputs/investigations/prose-instructions-compatibility-review-v1-20260421.md) | Gap analysis of patch + directive instructions vs prose lifecycle; fix plan that landed in commit `9ebcf7e`. |
| [WA-WorkingMemoryAndSnapshots-v1.0-2026-04-21.md](../data/imports/WA/Workflow/methodology_logs/WA-WorkingMemoryAndSnapshots-v1.0-2026-04-21.md) | Governing principle — database-as-memory, snapshot-as-first-class-research-act. |
| [CLAUDE.md §3 Table Group 17](../CLAUDE.md) | Schema summary entry in project reference. |

---

*Architectural summary produced 2026-04-23.*
