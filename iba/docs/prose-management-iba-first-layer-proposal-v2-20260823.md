# Prose management in IBA — first layer: proposal (escalation #829) — v2

**Supersedes v1** (`prose-management-iba-first-layer-proposal-v1-20260823.md`, left on disk for
history). v1 was a cross-check against Plan v4 — confirmed nothing had drifted, then reused v4's
content largely as-is. The researcher's review of v1 (2026-08-23) correctly identified that this
is not enough: *a proposal must be a complete capture of what exists and what needs to change for
every aspect of scope, not a cross-check that a prior document still fits* — and named specific,
real gaps v1 still had. §0 below maps every point of that review to where it's answered here.

**Stage:** plan/propose/design (in detail), per `cfg_behaviour_rule` class=`development`,
rule_key=`test-plan-per-module-utility` (escalation #828): *"plan/propose/design (in detail) →
approve → build per the plan → approve"*. Nothing in this document has been submitted to
`configmaint.propose` or built.

---

## 0. Compliance map — every review point, and where it's answered

| Review point (researcher, 2026-08-23) | Answered in |
|---|---|
| "Not just a cross check... a complete capture of what is there, and what needs to be updated/added for the scope" | Whole document restructured around existing/change tables — §1, §3, §4, §6 |
| "Previous proposal of this kind still missed items in the build because it was not properly stated" | §1.3/§6 name real, previously-missed structural facts (undocumented columns, an incomplete `book_stage_map`, dormant link tables) found by re-reading the live schema directly, not the design doc |
| Must state existing + change/new for every aspect, **incl. documentation and testing plan** | §8 (documentation), §9 (test plan) both now explicit existing/change |
| New **Governance** section — existing rules regulating prose, literal config wording, gaps, new wording | §2 |
| §0/§1 — check #784 for new columns suggested | §1.3 — found more than #784 named: 3 live undocumented columns on `prose_section` (§1.3a) plus #784's own `prose_section_verse_link` suggestion, routed in §6 D2 |
| Quality-flag incorporation + table-suitability assessment | §1.4, with a schema-grounded assessment (not narrative-only) |
| Start by stating storage tables in scope and their relationships | §1 opens the document |
| Include config definitions of all tables and columns | §1.2 (full `cfg_table`/`cfg_column` content, all 10 tables / 68 columns) |
| §3 — list the scripts involved | §3, all 15 `prose`-touching `cfg_utility` rows classified, not just the 4 |
| §5 — everything out of scope needs an escalation home or an in-proposal decision | §7 (registration table — every row has a home) |
| `docs/prose-store-architecture.md` is an input; its info must be captured in configs; it must be **superseded by the build, not updated** | §1/§2/§4/§5 fold in every rule the architecture doc states; §8.1 states the supersession as a build step |
| Every known postponed/parked item must be registered, or it gets lost | §6 (decisions, each with a stated home) + new escalation **#832** raised for the items this proposal doesn't resolve itself |

---

## 1. Storage tables in this scope, and how they relate

### 1.1 The table family and its relationships

```
prose_section_type  (dictionary — 108 codes, 16 columns)
      │  section_type_id (FK, required)
      ▼
prose_section  (content — 1,040 rows, 20 columns)
      │
      ├──► prose_section_fts (+ 5 FTS5 shadow tables) — SQLite-managed search index, auto-synced
      ├──► prose_section_dimension_link  — declared, 0 rows, dead (dimension review retired 2026-05-04)
      ├──► prose_section_finding_link    — declared, 0 rows, FK points at a retired table
      └──► supersedes_id / superseded_by_id (self-referential version chain, in-table)
```

`registry_id` (on `prose_section`) additionally scopes a row to one `word_registry` entry, or
`NULL` for programme/cluster-wide. `cluster_code`/`characteristic_id`/`cluster_subgroup_id`
(§1.3a) additionally scope a row to the M-code taxonomy — a second, independent scoping axis the
architecture doc never documents.

### 1.2 In / out of this build's scope, per table

| Table | Rows | Columns | This build (§4/§5) | Why |
|---|---:|---:|---|---|
| `prose_section_type` | 108 | 16 | **IN** | `source_stage`/`lifecycle_tag`/`book_label` get `cfg_enum` backing (currently uncontrolled — no CHECK constraint at all); 4 columns get real `cfg_column.use` text (currently blank, §1.3b) |
| `prose_section` | 1,040 | 20 | **IN** | `status`/`author` CHECK values get `cfg_enum` backing; write operations get `cfg_status_flow`/`cfg_behaviour_rule`/`cfg_write_grant` |
| `prose_section_fts` + 5 shadow tables | n/a (index) | 24 (all already catalogued, §1.2a) | **OUT — no action** | SQLite-managed, auto-synced by triggers, already fully catalogued in `cfg_table`/`cfg_column`; nothing here is config-governable |
| `prose_section_dimension_link` | 0 | 4 | **OUT of population — decision on retirement, §6 D4** | Dead concept (dimension review retired 2026-05-04); no `dimension_id` FK target was ever even named |
| `prose_section_finding_link` | 0 | 4 | **OUT of population — decision on FK fix, §6 D3** | FK points at the legacy `wa_session_b_findings`, not the live `finding` table |

*(§1.2a: the FTS5 machinery — `prose_section_fts`/`_data`/`_idx`/`_content`/`_docsize`/`_config` —
is omitted from the full column dump in §1.5 below for the same reason it needs no build action:
every column is SQLite-internal (opaque binary segments, positional `c0..c6` copies, term-prefix
keys), already described in `cfg_column`, and carries no project-authored meaning. Available on
request; adds no governance content.)*

### 1.3 Real gaps found by reading the live schema directly (not carried over from any prior doc)

**a) Three live columns on `prose_section` that `docs/prose-store-architecture.md` §3.2 does not
mention at all**, and that neither Plan v4 nor proposal v1 accounted for: `cluster_code` (TEXT,
free text, 192/1,040 rows populated), `characteristic_id` (INTEGER, 124/1,040 populated),
`cluster_subgroup_id` (INTEGER, declared + indexed, **0/1,040 populated — never used**). All 192
populated `cluster_code` values and all 124 `characteristic_id` values were checked live against
`cluster`/`characteristic` — **zero orphans**; the data is clean, only the formal FK constraint is
missing. Decisions: §6 D5/D6.

**b) Four columns on `prose_section_type` with blank `cfg_column.use` text** —
`book_order`/`book_label`/`section_order`/`section_label` — a live violation of
`governance.table_columns` ("each column ... must be listed in cfg_column **with a proper use
text**"). Not a judgement call, a standard to fix (`feedback_fix_standard_violations_dont_ask`) —
real `use` text for all 4 is in §5.

**c) `prose.book_stage_map`'s proposed value (v1, carried from Plan v4) is factually wrong against
live data — and so is the *code's own hardcoded default it was copied from*.** `prose_section_type.
source_stage` has **11** live distinct values, not the 5 the architecture doc names:
`contributor`(2) / `essay`(1) / `findings`(3) / `programme`(52) / `session_a`(6) / `session_b`(5) /
`session_b_phase9`(11) / `session_c`(12) / `session_d`(10) / `synthesis`(3) / `verse-analysis`(3).
Cross-tabbed against `book_label`: **`contributor` and `findings` are both entirely unbooked**
(`book_label IS NULL` on all 5 of those rows) — `book_stage_map`'s proposed value omits both
stages, and `prosestore.py`'s own `_DEFAULT_BOOK_STAGE_MAP` fallback constant has the identical
gap (confirmed by reading the code, not assumed). The `findings`-stage gap is the *same* finding
already named at #784 §4 ("3 'Cluster Findings' types that logically belonged under `Findings` but
were never tagged") — identified there, never turned into an actual config/data fix until now.
Corrected value in §5.

### 1.4 Adjacent tables relevant to future prose work — named, assessed, not in this build

`wa_quality_flag_types`/`wa_data_quality_flags` were named at #784 §7 as the likely shape to reuse
for the prose-change-flag idea (already claimed as **#831**'s scope, not repeated here). Schema
checked directly (not re-narrated from #784): `wa_data_quality_flags.file_id` is a hard FK to
`wa_file_index` — a *term-file* entity, not a row-generic target; there is no `raised`/`resolved`
lifecycle field, only `last_changed`; 19,866 existing rows are all term-scoped. **Confirms #784
§7's own assessment with schema evidence**: reusing this shape for `prose_section` needs either a
polymorphic-target redesign or a parallel table, and a lifecycle field — a real design task, not a
config addition, correctly out of #829's scope. Home: **#831**.

### 1.5 Full config definitions — `prose_section` and `prose_section_type`

Every column, exactly as `cfg_column` states it today (built from live-data profiling, not
hand-typed) — this is what "captured in the configs" already means for the schema layer;
`governance.table_columns` is satisfied for both tables already. Included in full per the review
request, not summarised:

**`prose_section`** (`cfg_table.use`: *"The DB-canonical store of authored prose: one row per
titled section of narrative — chapter readings, cluster essays, synthesis passages and programme
documentation — with its full body text, version lineage and approval state."*)

| Column | Type | `cfg_column.use` |
|---|---|---|
| `id` | INTEGER PK | Surrogate primary key for the prose section. |
| `registry_id` | INTEGER | The `word_registry` entry the section is about, where word-scoped. 86% NULL — most sections are chapter- or cluster-scoped rather than word-scoped. |
| `section_type_id` | INTEGER NOT NULL | The kind of section, referencing `prose_section_type`. Heavily skewed — one type (lexical prose at chapter level) accounts for roughly half of all rows. |
| `heading` | TEXT | The section's title. Not unique. |
| `body` | TEXT NOT NULL | The prose itself — the payload the table exists to hold. |
| `word_count` | INTEGER NOT NULL DEFAULT 0 | Cached length of `body` in words. **Not reliably maintained** — some rows record 0 despite holding text (escalation #832). |
| `status` | TEXT NOT NULL, CHECK | Editorial state — `draft`/`in_review`/`approved`/`archived`. Great majority `approved`. |
| `version` | INTEGER NOT NULL DEFAULT 1 | Declared INTEGER but **live data contradicts the type** — holds strings like `'1_0'`/`'v1'`/`'v2'` alongside real integers (escalation #832). |
| `supersedes_id` | INTEGER | The earlier `prose_section` row this replaces. Present on 90 rows, forming a self-referential revision chain. |
| `superseded_by_id` | INTEGER | Inverse of `supersedes_id`, maintained symmetrically. |
| `author` | TEXT NOT NULL, CHECK | Who wrote it — `claude_ai`/`claude_code`/`researcher`. Only 2 of 1,040 rows are `researcher`. |
| `created_at` | TEXT NOT NULL | ISO-8601 UTC, consistently formatted. |
| `approved_at` | TEXT | 87% NULL even though 922 rows are `approved` — not kept in step with `status` (escalation #832). |
| `approved_by` | TEXT | `claude_code`, or `'manual_backfill'` for retrospective approval. |
| `metadata_json` | TEXT | Free-form scope/provenance JSON — book/chapter/verse list, term, `cluster_code`, source, version. |
| `source_file` | TEXT | The markdown file the prose was ingested from. Near-universally populated. |
| `delete_flagged` | INTEGER NOT NULL DEFAULT 0 | Soft-delete marker; 59 rows flagged out. |
| `cluster_code` | TEXT | The M-code cluster the section belongs to, where cluster-scoped (§1.3a). 82% NULL, free text, **no FK to `cluster`** (0 orphans live — §6 D5). |
| `characteristic_id` | INTEGER | The characteristic the section discusses, where characteristic-scoped. Populated on 124/1,040 rows. |
| `cluster_subgroup_id` | INTEGER | Declared and indexed to scope a section to a cluster subgroup. **100% NULL — never used** (§6 D6). |

**`prose_section_type`** (`cfg_table.use`: *"The controlled vocabulary of prose section kinds — 108
codes spanning programme documentation, per-session outputs, cluster findings and lexical prose —
each with a label, the stage that produces it, and expected length bounds. The only real
enforcement behind `prose_section.section_type_id`."*)

| Column | Type | `cfg_column.use` |
|---|---|---|
| `id` | INTEGER PK | Surrogate primary key, referenced by `prose_section.section_type_id`. |
| `code` | TEXT NOT NULL UNIQUE | Short machine name (e.g. `cluster_essay`, `lexical_prose`, `cf_char_synth`). |
| `label` | TEXT NOT NULL | Human-readable name, usually stating what it is and who it's for. |
| `source_stage` | TEXT NOT NULL | The programme stage producing this type. **Uncontrolled — no CHECK constraint.** 11 live values (§1.3c), not the 5 the architecture doc names. |
| `lifecycle_tag` | TEXT | Generation marker — `v1`/`v2`/`source`. 77% NULL. `v3` (architecture doc's own third pass) has **0 live rows**. |
| `chapter_no` | INTEGER | For cluster-publication types, the chapter of the finished product. |
| `description` | TEXT | What the type is for. Missing on 32 types. |
| `expected_length_min`/`_max` | INTEGER | Word-count guide; advisory only, NULL on 44 types. |
| `sort_order` | INTEGER NOT NULL DEFAULT 0 | Presentation order within a stage/chapter; repeats across groups. |
| `delete_flagged` | INTEGER NOT NULL DEFAULT 0 | Soft-delete; no type retired this way, all 108 live. |
| `created_at` | TEXT NOT NULL | Clusters into ~20 batches, April–May 2026. |
| `book_order` | INTEGER | **(§1.3b — blank `use`, fixed in §5.)** Display order of the 4 books: 1=Programme, 2=Detail design, 3=Findings, 4=Essays. |
| `book_label` | TEXT | **(§1.3b.)** Which of the 4 live books this type belongs to. NULL on 5 types (the `contributor` pair + 3 unbooked `findings`-stage types, §1.3c). Uncontrolled — no CHECK constraint. |
| `section_order` | INTEGER | **(§1.3b.)** Ordering of the named groupings within a book (e.g. `Session A`=1, `Session B`=2 inside Detail design). |
| `section_label` | TEXT | **(§1.3b.)** The named grouping itself (e.g. `Session A`, `Verse analysis`, `Observation framework`) — a third level between book and chapter. |

`prose_section_dimension_link` and `prose_section_finding_link` (4 columns each, all currently
`use`="Intended... Never populated") are reproduced in full in §6 D3/D4 alongside their retirement
decisions, not repeated here.

---

## 2. Governance — what already regulates prose behaviour today

### 2.1 Existing rules, literal wording

| Setting / rule | Literal content | What it actually governs | What it does *not* cover |
|---|---|---|---|
| `governance.prose_canonical_authority` (`cfg_setting`) | *"The programme prose (Workflow/Programme/programme_prose/) is the canonical authority on what the project is about — researcher, 2026-08-18. Chapters 0-3 are reviewed and final; chapters 4-6 are not yet aligned (escalation pending, part (d)). `cfg_prose_chapter` names each chapter and its status; `cfg_prose_concept` points a key project concept ... at the prose section that defines it, rather than restating the definition as a separate rule. A methodology/approach change that touches a concept named in `cfg_prose_concept` should flag whether the prose needs updating (part (f) — the flagging MECHANISM is not yet built, this states the principle only)."* | The **Programme book's** own chapter-alignment status and canonicity — a governance-of-content rule | Nothing about `prose_section`'s mechanics (write ops, status lifecycle, enum backing), and nothing about the other 3 books |
| `cfg_prose_chapter` (7 rows) | `chapter 0–6`, `title`, `status` (`reviewed` ×4 / `not_yet_aligned` ×3), `source_doc`, `description` | Which Programme chapters are settled vs. pending (chs. 4–6 tracked at escalation **#739**) | Not a `cfg_prose` module-settings table (different name, different shape) — do not confuse with §4's new `cfg_prose` |
| `cfg_prose_concept` (2 rows: `verse_primacy`, `inner_being_definition`) | Points a concept key at its defining prose chapter/section, e.g. *"The verse is the primary unit of evidence; findings and dimensions emerge from verse evidence, never bent to fit a pre-existing category."* | Two named project concepts' canonical prose location | Not a general concept-registry; only 2 entries exist |
| `governance.programme_stages` (`cfg_setting`) | *"The research programme has three main stages: Base_data (STEP through lexical); Analysis (deriving understanding of the inner being); Publishing (essays and output for the results). Previously referred to as Session A (base data), Session B/D (analytics), Session C (publishing)..."* | A **coarse, 3-stage** process-terminology mapping, old→new | Does **not** map onto the 11 live `source_stage` values (§1.3c) — different altitude, not a conflict (§6 D9) |
| `governance.rules_must_be_config_driven`, `governance.module.config`, `governance.table_columns`, `governance.tables` | (Project-wide, quoted in full in CLAUDE.md §12/GOVERNANCE.md — not reproduced here) | Generic requirements this whole proposal exists to satisfy for prose specifically | Nothing prose-specific — that's the gap |

### 2.2 The gap, confirmed live today (2026-08-23)

**Zero** `cfg_behaviour_rule`, `cfg_enum`, `cfg_status_flow`, `cfg_write_grant`, `cfg_work_package`,
or `cfg_step` row exists anywhere naming `prose_section`, `prose_section_type`, or any `prose.*`
operation. Every rule the architecture doc states about how `prose_section` actually behaves — the
`session_a_replace` author gate, supersede-only immutability, the two-patch ordering, which
operation sets which status — exists **only** in that Markdown file and in code, not in a single
`cfg_*` row. This is the gap `governance.rules_must_be_config_driven` names directly: *"no
operational or process rule may exist only in ... memory [or a document] without a referenced
`cfg_*` row."*

### 2.3 New governance wording this proposal adds

Summarised here; literal payloads in §5 (not duplicated). Three new `cfg_behaviour_rule` rows
(class=`sqlite`) state the session_a_replace gate, supersede-only discipline, and two-patch
ordering as real config rows for the first time. Two new `cfg_enum` groups back `status`/`author`.
Two *additional* new `cfg_enum` groups (beyond v1's proposal — added this revision, §1.3c/§5) back
`source_stage` and `lifecycle_tag`, since those are just as uncontrolled as `status`/`author` but
were missed in v1. A `cfg_prose` module table replaces the informational-only architecture doc for
the three tool settings, corrected against live data (§1.3c). Once built, this proposal's own
existence is what closes `governance.rules_must_be_config_driven`'s gap for prose — stated here so
the researcher can evaluate the actual wording before it's written, not after.

---

## 3. Scripts and code involved

### 3.1 Operational surface — in scope, changes

| File | Current state | Change in this build |
|---|---|---|
| `iba/app/lib/prosestore.py` | `cfg_utility`, `inactive=0`, already the incorporated logic | `CHAPTER_EDIT_OUT_DIR` hardcode → `cfg.module_setting('cfg_prose', 'prose.edit_file_dir')`; `_DEFAULT_BOOK_STAGE_MAP` corrected to match §1.3c (still the fallback when `cfg_prose` is inactive/absent) |
| `iba/app/handlers/prose.py` | **Not** in `cfg_utility` (confirmed live — matches the project convention: handler files are registered via `cfg_step`, not `cfg_utility`; `handlers/passage.py` follows the identical pattern) | Registered via the new `cfg_work_package`/`cfg_step` rows, component II |
| `iba/app/ps/Prose.ps1` | Same — not in `cfg_utility`, same convention as `Passage.ps1` | Same — dispatcher-wired via `cfg_step`, no separate `cfg_utility` row needed |
| `scripts/build_programme_prose_extract.py` | `cfg_utility`, `inactive=1`, `NON-COMPLIANT (#648)` | Reactivate, superseded-pointer `purpose` text |
| `scripts/export_prose_chapter_edit.py` | `cfg_utility`, `inactive=1`, `INACTIVE 2026-08-18 (#729)` | Reactivate, superseded-pointer `purpose` text |
| `scripts/import_prose_chapter_edit.py` | `cfg_utility`, `inactive=1`, `INACTIVE 2026-08-18 (#729)` | Reactivate, superseded-pointer `purpose` text |
| `scripts/search_prose.py` | `cfg_utility`, `inactive=1`, `NON-COMPLIANT (#648)` | Reactivate, superseded-pointer `purpose` text |

### 3.2 Dormant historical scripts touching prose — documented, unchanged, no action

9 more `cfg_utility` rows match `%prose%`, none part of this build. Listed here so nothing is
silently missing from the inventory (the review's own complaint about v1):

| File | `purpose` (as stored) | Disposition |
|---|---|---|
| `scripts/_apply_file_chapter_lexical_prose_v1_20260702.py` | One-off lexical-prose file applier | Historical, `inactive=1` per escalation #729's own precedent ("set to inactive; update only if needed again"). Unchanged here. |
| `scripts/_apply_file_passage_lexical_prose_v1_20260704.py` | Same shape, passage-scoped | Same |
| `scripts/_apply_file_ruthlessness_lexical_prose_20260702.py` | Same shape, one cluster | Same |
| `scripts/_apply_file_synthesis_prose_v1_20260703.py` | File a cross-chapter SYNTHESIS document | Same |
| `scripts/_apply_prose_programme_chapter01.py` | One-off Programme ch.1 applier | Same |
| `scripts/_export_prose_to_md_v1_20260703.py` | Regenerate folder `.md` from the DB corpus | Functionally superseded by `prosestore.py`'s extract; same `inactive=1` precedent, not reactivated as a duplicate |
| `scripts/_probe_primary_span_prose_reference_v1_20260705.py` | Diagnostic probe, per-book primary spans | Same |
| `scripts/build_corpus_prose.py` | Compile completed word-analysis chapters into a book | Part of the **old per-word Session A/B/C pipeline** — its disposition (keep as history vs. dead weight) is the still-open question at #784 §9 about the `Detail design` book, not decided here |
| `scripts/build_session_a_prose.py` | Render per-word Session A prose for Verse Context input | Same — old per-word pipeline, #784 §9 |

None of these are prefixed `temp_` despite being genuinely one-off (a minor, pre-existing deviation
from `governance.scripts_and_routines`'s letter — flagged, not fixed here; escalation #729 already
made the "leave inactive, don't force compliance until reused" call project-wide, which this
proposal doesn't reopen).

### 3.3 `apply_session_patch.py` — write side, narrow scope

Not in `cfg_utility` at all (project-wide script, not prose-specific). Only its 6 `prose_section`
operations (`insert`/`supersede`/`delete`/`approve`/`session_a_replace`/`bulk_supersede`, read at
lines 1662–1850) get governance rows in this build (§4 component III) — the script itself is
explicitly not rearchitected (§7).

---

## 4. Full scope — five components

**I. Read/report layer.** Code already built and tested. Config missing (§2.2).

**II. Dispatcher registration.** `prose` as a `cfg_work_package` + 4 `cfg_step` rows, `kind='utility'`.

**III. Write-layer governance.** `cfg_enum` for `status`/`author`; `cfg_status_flow` (4 rows);
`cfg_behaviour_rule` (3 rows, `session_a_replace` gate / supersede-only / two-patch ordering);
`cfg_write_grant` (2 rows, `database='bible_research'`).

**IV. `cfg_prose` — dedicated per-module table, 4 keys** (was 3 in v1; `edit_file_dir` unchanged
from v1, `book_stage_map`'s *value* now corrected per §1.3c).

**V. `prose_section_type` column governance — new this revision.** `cfg_enum` for `source_stage`
(11 values), `lifecycle_tag` (4 values incl. unused `v3`), `book_label` (4 values); real `use` text
for the 4 blank columns (§1.3b).

**VI. Storage-integrity decisions — new this revision.** §6 D3–D6: `prose_section_finding_link`'s
FK, `prose_section_dimension_link`'s retirement, `cluster_code`'s FK, `cluster_subgroup_id`'s
disposition. Each is a genuine decision, not a default — none built without an explicit answer.

**Test plan.** §9, required up front (governance rule 46 / escalation #828).

---

## 5. Detailed build spec — literal payloads

### IV. `cfg_prose` — new table + 4 rows

```sql
CREATE TABLE cfg_prose (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    use TEXT NOT NULL,
    inactive INTEGER NOT NULL DEFAULT 0
);
```

| key | value | use |
|---|---|---|
| `prose.chapter_names` | `{"0":"Preamble","1":"Programme purpose","2":"Research methodology","3":"Research approach","4":"Data architecture","5":"Data integrity & governance","6":"Instruction corpus"}` | Chapter-number → readable-name lookup for the extract's Markdown/Word output. Read by `prosestore.py:chapter_names(cfg)`. Fixes `build_programme_prose_extract.py`'s `NON-COMPLIANT (#648)` flag. |
| `prose.book_stage_map` | `{"Programme":["programme"],"Detail design":["session_a","session_b","session_b_phase9","session_c","session_d"],"Findings":["synthesis","verse-analysis","findings"],"Essays":["essay"]}` | **Corrected per §1.3c** (v1's value and the code's own hardcoded default both omitted the `findings` stage — closes the same gap #784 §4 already named). `contributor` (2 types) is *deliberately* left out — its own `label` text says "capture once → route many," i.e. it is explicitly a staging area, not a book; documented here rather than silently absent. Allowed `--book` values + validation set for `prose.extract`/`Prose.ps1`. Read by `prosestore.py:book_stage_map(cfg)`. |
| `prose.search_default_limit` | `100` | Default result cap for `search_prose.py`/`prose.search`. Read by `prosestore.py:search_default_limit(cfg)`. Fixes `search_prose.py`'s `#648` flag. |
| `prose.edit_file_dir` | `"outputs/markdown/prose-edits"` | Directory `export_chapter` writes editable `.md` into, and `import_chapter` archives from (`{value}/archive/`) on success. Replaces the hardcoded `CHAPTER_EDIT_OUT_DIR` constant. Closes #784 §6's open location question — same NON-COMPLIANT-hardcoded-constant shape already fixed elsewhere under #648, a standard fix not a fresh decision. |

### I/III — `cfg_enum` groups (status/author — unchanged from v1)

| name | value | ordinal |
|---|---|---|
| `prose_section_status` | `draft` | 0 |
| `prose_section_status` | `in_review` | 1 |
| `prose_section_status` | `approved` | 2 |
| `prose_section_status` | `archived` | 3 |
| `prose_section_author` | `claude_ai` | 0 |
| `prose_section_author` | `claude_code` | 1 |
| `prose_section_author` | `researcher` | 2 |

### V — `cfg_enum` groups — **new this revision** (§1.3c/§4 component V)

| name | value | ordinal |
|---|---|---|
| `prose_section_type_source_stage` | `programme` | 0 |
| `prose_section_type_source_stage` | `session_a` | 1 |
| `prose_section_type_source_stage` | `session_b` | 2 |
| `prose_section_type_source_stage` | `session_b_phase9` | 3 |
| `prose_section_type_source_stage` | `session_c` | 4 |
| `prose_section_type_source_stage` | `session_d` | 5 |
| `prose_section_type_source_stage` | `synthesis` | 6 |
| `prose_section_type_source_stage` | `verse-analysis` | 7 |
| `prose_section_type_source_stage` | `findings` | 8 |
| `prose_section_type_source_stage` | `essay` | 9 |
| `prose_section_type_source_stage` | `contributor` | 10 |
| `prose_section_type_lifecycle_tag` | `source` | 0 |
| `prose_section_type_lifecycle_tag` | `v1` | 1 |
| `prose_section_type_lifecycle_tag` | `v2` | 2 |
| `prose_section_type_lifecycle_tag` | `v3` | 3 |
| `prose_section_type_book_label` | `Programme` | 0 |
| `prose_section_type_book_label` | `Detail design` | 1 |
| `prose_section_type_book_label` | `Findings` | 2 |
| `prose_section_type_book_label` | `Essays` | 3 |

(`v3` and the 5 unbooked types, §1.3c, are enumerated as *valid targets*, not asserted as currently
correct — the enum documents the domain, it doesn't retroactively populate NULLs.)

### V — `cfg_column` — 4 blank `use` values filled (§1.3b)

| table | column | new `use` |
|---|---|---|
| `prose_section_type` | `book_order` | "Display order of the 4 live books: 1=Programme, 2=Detail design, 3=Findings, 4=Essays. Paired 1:1 with `book_label`." |
| `prose_section_type` | `book_label` | "Which of the 4 live books this type belongs to — see `cfg_enum` group `prose_section_type_book_label`. NULL on 5 types (`contributor` pair + the 3 unbooked `findings`-stage types, escalation #832)." |
| `prose_section_type` | `section_order` | "Ordering of the named sub-groupings within a book (e.g. within `Detail design`: `Session A`=1, `Session B`=2, ... `Session B Phase 9`=5, `Observation framework`=6) — a level between book and chapter." |
| `prose_section_type` | `section_label` | "The named sub-grouping itself (e.g. `Session A`, `Verse analysis`, `Synthesis`, `Observation framework`) — human label for `section_order`'s position." |

### III — `cfg_status_flow` rows, `entity='prose_section'` (unchanged from v1)

| status | set_by | ordinal |
|---|---|---|
| `draft` | `apply_session_patch.py: prose_section insert/supersede/bulk_supersede (caller-supplied, the default when omitted)` | 0 |
| `in_review` | `apply_session_patch.py: prose_section insert/supersede (caller-supplied status — no dedicated transition op exists; 0 rows currently at this status)` | 1 |
| `approved` | `apply_session_patch.py: prose_section approve (the one dedicated transition op — also stamps approved_at/approved_by)` | 2 |
| `archived` | `apply_session_patch.py: prose_section insert (caller-supplied status only — 11 existing rows were archived at insert time, not via a transition op)` | 3 |

### III — `cfg_behaviour_rule` rows, `class='sqlite'` (unchanged content from v1; `source`/`enforced_by` now stated explicitly, matching the project's own style convention)

| rule_key | rule_text | source | enforced_by |
|---|---|---|---|
| `prose-section-session-a-replace-author-gate` | "The `session_a_replace` operation is the one exception to `prose_section`'s supersede-only immutability — it updates a row in place. Code-gated on `author='claude_code'`; permitted only for Session A mechanical extracts, because they are reproducible from structured data rather than analytical judgement." | `docs/prose-store-architecture.md` §5.2/§6.1; escalation #784/#829 | `apply_session_patch.py`'s `UPDATE ... WHERE id=? AND author='claude_code'` clause |
| `prose-section-supersede-only-discipline` | "Narrative `prose_section` rows are immutable once written, outside the one exception above. A revision creates a new row (`version = old.version + 1`, `supersedes_id = old.id`); the predecessor's `superseded_by_id` is set to point forward. No `UPDATE` of `body` on an existing narrative row is a sanctioned operation." | `docs/prose-store-architecture.md` §6.1; escalation #784/#829 | `apply_session_patch.py`'s `supersede` operation shape; not yet mechanically checked against direct DB access |
| `prose-section-two-patch-ordering` | "A new prose chapter reaches the database in two ordered patches: `CATALOGUE_POPULATION` first (creates `prose_section_type` handles), then `PROSE` (content, referencing handles by `section_type_id_lookup: {code}`). Applying `PROSE` before its `CATALOGUE_POPULATION` fails at the code lookup, by design." | `docs/prose-store-architecture.md` §7; escalation #784/#829 | `apply_session_patch.py`'s `section_type_id_lookup` resolution — fails loudly, not silently, if violated |

### III — `cfg_write_grant` rows, `database='bible_research'` (unchanged from v1; §6 D1 still standing)

| writer | table_name |
|---|---|
| `apply_session_patch` | `prose_section` |
| `apply_session_patch` | `prose_section_type` |

### II — `cfg_work_package` + 4 `cfg_step` rows (unchanged from v1)

`cfg_work_package`: `name='prose'`, `ps_script='iba/app/ps/Prose.ps1'`, `runs_over='none'`, `chained=0`.

| ordinal | step | handler | kind | does |
|---|---|---|---|---|
| 0 | `prose.extract` | `iba.app.handlers.prose:extract` | utility | Programme-prose extract (JSON/MD/DOCX) |
| 1 | `prose.search` | `iba.app.handlers.prose:search` | utility | FTS/plain search over `prose_section` |
| 2 | `prose.export_chapter` | `iba.app.handlers.prose:export_chapter` | utility | Export a chapter to editable `.md` |
| 3 | `prose.import_chapter` | `iba.app.handlers.prose:import_chapter` | utility | Turn an edited `.md` into a patch file (writes no DB row itself) |

### I — reactivate the 4 original scripts (`cfg_utility`) (unchanged from v1)

Same 4 rows (§3.1), same superseded-pointer `purpose` text, `inactive: 1 → 0`.

---

## 6. Decisions needed — consolidated

Every item below is a genuine judgement call, not a default this proposal silently picked. Each
states a recommendation and, if the researcher defers it, its registered home — **escalation
#832**, raised while writing this revision specifically to hold whatever isn't decided here.

| # | Decision | Recommendation | If deferred, home |
|---|---|---|---|
| **D1** | `cfg_write_grant`: one `apply_session_patch` writer identity vs. six per-operation identities | One writer (carried from v1) — nothing downstream distinguishes the six operations yet | n/a — build proceeds with the recommendation unless told otherwise |
| **D2** | `prose_section_verse_link` (new table, #784 §13's verse-grounding gap) — build now as part of this storage layer, or defer? | **Defer.** New schema needing its own shape decision (verse ref? span? chapter-level?) not yet designed; verse-linking naturally happens *at add/edit time*, which is #831's territory, not this storage-governance layer | **#831** |
| **D3** | `prose_section_finding_link`'s FK — fix now (point at live `finding`, not legacy `wa_session_b_findings`) or defer? | **Fix now.** 0 rows, zero data-migration risk, purely a schema-correctness fix independent of when/whether the link mechanism gets populated (`feedback_fix_standard_violations_dont_ask`) | **#832**, if not approved now |
| **D4** | `prose_section_dimension_link` — the dimension-review concept it targets was retired 2026-05-04; `dimension_id` has no FK target at all. Formally retire (`cfg_table.inactive=1` + a note) now, or leave dormant? | **Retire now** (cheap, correct, zero data/schema risk — table stays declared, just marked inactive in the catalogue) | **#832**, if not approved now |
| **D5** | `cluster_code` — add a real FK to `cluster(cluster_code)` via table-rebuild migration (0 live orphans, confirmed) | **Include in this build.** Data is already 100% clean; this is the moment to lock it before drift is possible. Heavier than the config-only steps (a real DDL migration), flagged explicitly rather than bundled silently | **#832**, if not approved now |
| **D6** | `cluster_subgroup_id` — 100% NULL, never used. Drop the column, leave it declared-but-dead, or something else? | **Leave as-is.** Dropping a column is a heavier, harder-to-reverse migration for no live benefit; the fact is now documented (§1.5) so it won't be mistaken for populated data | **#832** — registered either way, in case cluster-subgroup-level prose scoping becomes wanted later |
| **D7** | `prose_section.version` — declared INTEGER, live data holds mixed integer/string values (escalation #832) | **Not fixed here.** Needs its own decision on what "version" should mean (strict ordinal vs. free-form edit tag) before any cleanup is safe against ~1,040 rows | **#832** |
| **D8** | `word_count`/`approved_at` reliability (not consistently maintained) | **Not fixed here.** Low-urgency data hygiene, no functional blocker on this build | **#832** |
| **D9** | `governance.programme_stages` (3-stage abstraction) vs. the new `prose_section_type_source_stage` enum (11 concrete values) — reconcile, or keep both? | **Keep both — not actually a conflict.** Different altitude: one is the programme's own high-level stage narrative, the other is the ground-truth column domain. No change to `governance.programme_stages` proposed. | n/a |

---

## 7. Explicitly out of scope — every item registered

| Item | Home |
|---|---|
| Migrating the full `wa_patch_type_registry` into `cfg_enum` | No escalation yet — genuinely project-wide (~20+ patch types spanning every patch, not just prose), larger than any single module's build; flagged so it isn't silently forgotten, raise when `apply_session_patch.py` as a whole comes under IBA |
| Rearchitecting `apply_session_patch.py` into an IBA dispatcher module | Same — no escalation yet, same reason |
| Widening `find_unknown_write_grant_writers` to validate `database='bible_research'` grants too | No escalation yet — small, `configmaint.validate`-mechanism-only change, not blocking this build |
| `docs/prose-store-architecture.md` §9 stale current-state table | Superseded outright by this build (§8.1), not fixed in place |
| Generic `.md`-marker round-trip import tool (architecture doc §8.3) | Already deferred by the architecture doc itself — carried forward unchanged |
| Programme Prose Chapter 4 rewrite | **#786** |
| `cfg_prose_chapter` `not_yet_aligned` chapters 4–6 | **#739** |
| The prose-change-flag mechanism | **#831** |
| Chapter-rewrite assistance (downstream of change-flag) | **#831** |
| `prose_section_verse_link` | **#831** (§6 D2) |
| Quality-flag table suitability for prose (design/build) | **#831** (§1.4) |
| The Concordance (5th book) | Still at **#784** — two sub-problems named there, not yet split into their own item; the already-buildable "base concordance" half is a real, separate opportunity not yet raised as its own escalation — flagged, not actioned |
| Raw-material-visibility for writing | Still at **#784** — connected to but not merged with the chapter-rewrite-assist idea; no separate escalation yet |
| Book-2/book-3 boundary question | Still at **#784** — a live content sample already shows the current line doesn't hold; needs its own design pass before it can be a build item |
| "Delete a section from an edit file" — silent no-op vs. refuse/warn/retire | Still at **#784** §6 — a behavior decision, not a config-governance gap |
| `prose_section.version`/`word_count`/`approved_at` data hygiene | **#832** (§6 D7/D8) |
| `prose_section_finding_link`/`dimension_link` fixes, if not approved in this build | **#832** (§6 D3/D4) |

---

## 8. Documentation updates

**8.1 `docs/prose-store-architecture.md` — SUPERSEDED, not updated.** Per instruction: once this
build (§9 sequencing) completes and passes its test plan (§10), the file's content is replaced with
a short superseded-pointer banner (matching the project's own convention for superseded documents
elsewhere) naming the new canonical sources: `cfg_prose`/`cfg_enum`/`cfg_status_flow`/
`cfg_behaviour_rule`/`cfg_write_grant` (mechanics), the new GOVERNANCE.md section (§8.2), `cfg_table`/
`cfg_column` (schema — already live, §1.5), and `iba/app/USER-GUIDE.md` (usage, §8.4). This is a
build step (§9), not a separate future task — it happens in the same unit of work per the shape of
`governance.build_md_on_code_change`. The doc's own §11 references (`wa-prose-store-design-v1-...`,
the Option-D decision record, the structure-design doc) are **not** superseded — they're historical
design rationale, not operative rules, and stay as provenance, cited from the new GOVERNANCE.md
section rather than rewritten.

**8.2 `GOVERNANCE.md`** — new section (next `§`), documenting this design and quoting the new
`cfg_behaviour_rule` rows verbatim, matching the existing pattern (§48–§50).

**8.3 `BUILD.md`** — new section, build record across all stages, gaps found/fixed named
individually (matching the existing pattern), including the D3–D6 decisions' actual outcomes.

**8.4 `USER-GUIDE.md`** — new "Prose module" section: the 4 dispatcher steps, the `cfg_prose`
settings, and the reactivated scripts' CLI usage (superseding the architecture doc's §8 as the live
command reference).

---

## 9. Sequencing (the "build per the plan" stage)

1. `cfg_prose` table creation + 4 rows (§5, component IV).
2. `cfg_column` — fill the 4 blank `use` values (§5, component V).
3. `cfg_enum` — `prose_section_status`(4) + `prose_section_author`(3) + `prose_section_type_source_stage`(11) + `prose_section_type_lifecycle_tag`(4) + `prose_section_type_book_label`(4).
4. `cfg_status_flow` — 4 rows, `entity='prose_section'`.
5. `cfg_behaviour_rule` — 3 rows, `class='sqlite'`.
6. `cfg_write_grant` — 2 rows, `database='bible_research'`.
7. `cfg_work_package` `prose` + 4 `cfg_step` rows.
8. `cfg_utility` — reactivate the 4 original scripts.
9. Code: `prosestore.py`'s `CHAPTER_EDIT_OUT_DIR` hardcode → `cfg.module_setting`; `_DEFAULT_BOOK_STAGE_MAP` corrected.
10. **Only if D3/D4/D5 approved:** `prose_section_finding_link`'s FK rebuild (point at `finding`); `prose_section_dimension_link` → `cfg_table.inactive=1`; `cluster_code` FK rebuild against `cluster`.
11. `docs/prose-store-architecture.md` → superseded banner (§8.1).
12. GOVERNANCE.md/BUILD.md/USER-GUIDE.md updates (§8.2–8.4).

---

## 10. Test plan (required up front, results go in the resolution)

v1's 22 cases (unchanged — reproduced by reference, not repeated here to keep this section legible:
extract/search/export/import behavior incl. the corrected refuse-on-unedited-reimport and
auto-archive cases, all 6 `apply_session_patch.py` operations, dispatcher wiring, `cfg_write_grant`
read) **plus**, new this revision:

| # | Function / operation | Test case | Expected |
|---|---|---|---|
| 23 | `prose.extract --book Findings` | after `book_stage_map` correction | Includes the 3 `findings`-stage types once they're re-tagged (or a clean, explicit note that they remain untagged if D-decisions leave them as-is — not a silent omission) |
| 24 | `prose.extract --book contributor` | invalid — `contributor` deliberately excluded from `book_stage_map` | Clean error listing the 4 real book choices, not a crash |
| 25 | `cfg.module_setting('cfg_prose', 'prose.edit_file_dir')` | read | Returns `"outputs/markdown/prose-edits"` |
| 26 | *(only if D5 approved)* insert a `prose_section` row with a `cluster_code` not present in `cluster` | FK violation, insert refused | Confirms the new constraint is real, not just documented |
| 27 | *(only if D3 approved)* `prose_section_finding_link` schema | `PRAGMA foreign_key_list` | FK now references `finding`, not `wa_session_b_findings` |
| 28 | `configmaint.validate` full run | after all proposals + code changes applied | Clean — no new structural violations |

---

## 11. What I need from you

Same one-decision structure as v1, widened to cover this revision's additions:

1. **Approve as written** — I submit §5's proposals in §9's order, make the code changes, resolve
   D1–D9 per the stated recommendations (unless told otherwise below), run the full test plan
   (v1's 22 + this revision's 6), and bring results back in one resolution against #829.
2. **Or answer D1–D9 individually** where a recommendation doesn't hold, and/or flag anything in §7's
   registration table that should get its own escalation now rather than staying parked.
