# IBA config related to "prose" -- extract

Generated 2026-08-21 for escalation #784 v6. Source: `iba/app/db/iba.db`, all `cfg_*` tables, scanned column-by-column for the literal string "prose" (case-insensitive). Chapters 1-3 of the programme prose have been rewritten to the current methodology; this extract is the input for aligning chapter 4 (data architecture) against what IBA's config actually says. Companion reading: [`docs/prose-store-architecture.md`](../../docs/prose-store-architecture.md) (the DB-canonical prose store design) and the four retrieval/authoring scripts named in this item's context -- `scripts/build_programme_prose_extract.py`, `scripts/export_prose_chapter_edit.py`, `scripts/import_prose_chapter_edit.py`, `scripts/search_prose.py`.

Rows are split into **core** (config that governs the prose store, its chapter/concept registry, its tooling, or a governance rule naming prose specifically) and **incidental** (a `use`/description field that happens to use "prose" as an ordinary English word for free text, on a table unrelated to the prose store) at the end. Everything found is listed; nothing is dropped.

---

## 1. Headline finding

**All 15 `cfg_utility` rows for prose-related scripts are `inactive=1`** -- including all four scripts named in this escalation's context (`build_programme_prose_extract.py`, `export_prose_chapter_edit.py`, `import_prose_chapter_edit.py`, `search_prose.py`). Per escalation #729, most were set inactive on 2026-08-18 (zero `Cfg-method` call sites) as a researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than `config_exempt=1`; four others (`build_corpus_prose.py`, `build_programme_prose_extract.py`, `build_session_a_prose.py`, `search_prose.py`) additionally carry an open NON-COMPLIANT flag from escalation #648 (hardcoded constants that should be `cfg_setting`-driven). See §5 for the full table. This means the architecture doc's retrieval/authoring flow (§8 of `prose-store-architecture.md`) currently describes tooling the config system marks dormant.

## 2. Governance framing -- config vs. prose

Three `cfg_table.use` entries state the boundary between config (cfg_* rows) and prose (narrative text in `prose_section` / the programme-prose files) directly -- relevant to reconciling chapter 4 against IBA, since this is the line the researcher has drawn between the two:

| Table | `use` |
|---|---|
| `cfg_escalation` | One row per discrete, nameable rule governing the escalation utility itself -- config, not prose (researcher, 2026-08-16 iba-table-review reset). Parallel to cfg_method_rule but scoped to escalation.py, not the debate pipeline. |
| `cfg_method_rule` | One row per discrete, nameable analytical rule governing a debate-pipeline step -- config, not only prose docs (researcher, 2026-08-06). |

`governance.prose_canonical_authority` (§3 below) is the operative rule: the programme prose is canonical on *what the project is about*; `cfg_*` config is canonical on *how the system operates*. `cfg_prose_chapter` / `cfg_prose_concept` are the index bridging the two -- they point at prose, they do not duplicate it.

## 3. `cfg_prose_chapter` -- the chapter registry (7 rows, full)

The chapter-level registry for `governance.prose_canonical_authority` -- which programme-prose chapters exist, their review status, and which live extract file is their source. **Does not hold the prose text itself.**

| Ch | Title | Status | Source doc | Description |
|---:|---|---|---|---|
| 0 | Preamble | **reviewed** | `Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md` | Programme preamble -- what the study is, framed for a reader coming to it fresh. |
| 1 | Programme purpose | **reviewed** | `Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md` | Mission, scope, this inner-being programme, defining inner being, science and the Bible, expected outcome -- the project's governing question lives here. |
| 2 | Research methodology | **reviewed** | `Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md` | Research method overview, word selection/registry construction, programme flow, science in action, publishing, key methodological principles and constraints. |
| 3 | Research approach | **reviewed** | `Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md` | Traceability and evidential warrant, the two-AI division of responsibility, session continuity and memory discipline. |
| 4 | Data architecture | **not_yet_aligned** | `Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md` | Escalation pending (part (d), separate item) -- content not yet checked against the live iba.db/bible_research.db split this file itself documents (2026-08-15 architecture correction postdates this chapter's last prose revision). |
| 5 | Data integrity & governance | **not_yet_aligned** | `Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md` | Escalation pending (part (d)) -- likely superseded in places by iba/app/GOVERNANCE.md's live config-driven model. |
| 6 | Instruction corpus | **not_yet_aligned** | `Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md` | Escalation pending (part (d)) -- likely stale against the current Workflow/Instructions/ [current]-token document set. |

Chapters 0-3: `reviewed`. Chapters 4-6: `not_yet_aligned` -- chapter 4's own description row says outright: *"content not yet checked against the live iba.db/bible_research.db split this file itself documents (2026-08-15 architecture correction postdates this chapter's last prose revision)."* This is the exact gap this escalation's next step (chapter 4 rewrite) closes.

## 4. `cfg_prose_concept` -- concept-to-prose pointer index (full table)

A pointer index: "this concept is DEFINED at this chapter/section of the prose" -- not a copy of the definition. Direct replacement mechanism for `wa_rule_registry` rows (e.g. GR-PROG-001/002) that used to restate a definition as rule text.

| concept_key | Ch | Section hint | Description | Source |
|---|---:|---|---|---|
| `verse_primacy` | 1 | Defining Inner Being / This Inner-Being Programme sections | The verse is the primary unit of evidence; findings and dimensions emerge from verse evidence, never bent to fit a pre-existing category. Direct successor of wa_rule_registry GR-PROG-001 (obsolete 2026-08-17) -- this pointer replaces the rule's own restated text. | wa_rule_registry GR-PROG-001; escalation #714 |
| `inner_being_definition` | 1 | Defining Inner Being / This Inner-Being Programme sections | The programme's governing question: what does Scripture reveal about the characteristics, operations, and interrelationships of the human inner being (spirit, soul, body)? Supersedes wa_rule_registry GR-PROG-002 (obsolete 2026-08-17) per researcher decision 2026-08-18 -- GR-PROG-002 is retired as a rule; this pointer to the prose is now the canonical reference, not a restated rule text. | wa_rule_registry GR-PROG-002 (superseded); escalation #714 |

Two concepts are currently indexed, both anchored to chapter 1 (`verse_primacy`, `inner_being_definition`). Neither of these literally contains the word "prose" in its own text -- they are pulled in full here because the *table* is core, not because of a text match. No concept row yet exists for chapters 4-6 -- expected, since those chapters are `not_yet_aligned`.

## 5. `cfg_utility` -- prose-related scripts (15 rows, full)

| file_path | inactive | purpose |
|---|---:|---|
| `query_db.py` | 1 | prose_section_type joined to active current prose_section rows -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |
| `scripts/_apply_d6_capture_contributor_source.py` | 1 | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). D6 — capture a contributor source (Logos / AI-Chat) into prose_section, strip it |
| `scripts/_apply_file_chapter_lexical_prose_v1_20260702.py` | 1 | _apply_file_chapter_lexical_prose_v1_20260702.py |
| `scripts/_apply_file_passage_lexical_prose_v1_20260704.py` | 1 | _apply_file_passage_lexical_prose_v1_20260704.py |
| `scripts/_apply_file_ruthlessness_lexical_prose_20260702.py` | 1 | _apply_file_ruthlessness_lexical_prose_20260702.py |
| `scripts/_apply_file_synthesis_prose_v1_20260703.py` | 1 | File a cross-chapter SYNTHESIS document as a DB-canonical prose_section |
| `scripts/_apply_prose_programme_chapter01.py` | 1 | _apply_prose_programme_chapter01.py -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |
| `scripts/_export_prose_to_md_v1_20260703.py` | 1 | Regenerate folder .md documents FROM the DB corpus (prose_section is canonical), |
| `scripts/_probe_primary_span_prose_reference_v1_20260705.py` | 1 | _probe_primary_span_prose_reference_v1_20260705.py — per book: primary spans + how many are |
| `scripts/build_corpus_prose.py` | 1 | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_corpus_prose.py — Compile completed word-analysis chapters into a book. |
| `scripts/build_programme_prose_extract.py` | 1 | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). build_programme_prose_extract.py — Prose-book extract. |
| `scripts/build_session_a_prose.py` | 1 | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Render per-word Session A prose as a self-contained `.md` for Verse Context input. |
| `scripts/export_prose_chapter_edit.py` | 1 | Export one current prose chapter or section as a temporary editable Markdown file. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |
| `scripts/import_prose_chapter_edit.py` | 1 | Turn an edited prose chapter Markdown file into a PROSE supersede patch. -- INACTIVE 2026-08-18 (escalation #729): zero Cfg-method call sites, researcher decision ("set these 110 module to inactive; if the time arise when they need to be used, then the script can be updated to be fully compliant") rather than config_exempt=1. |
| `scripts/search_prose.py` | 1 | NON-COMPLIANT (escalation #648 -- hardcoded constant(s) that should be cfg_setting-driven; see iba/app/reports/hardcoded-constants-sweep-20260817.md). Search prose_section across all prose books. |

**15/15 rows are `inactive=1`.**

## 6. `cfg_setting` -- settings naming prose (5 rows, full)

| key | value | use |
|---|---|---|
| `database.bible_research.path` | "database/bible_research.db" | bible_research.db's file path, project-root-relative (aka research_db in prose elsewhere -- that alias isn't repeated here, see governance.project_databases). Structured counterpart, escalation #723. |
| `database.iba.path` | "iba/app/db/iba.db" | iba.db's file path, project-root-relative -- structured counterpart to governance.project_databases' prose, part of escalation #723's project_database enum + path settings. |
| `governance.prose_canonical_authority` | "The programme prose (Workflow/Programme/programme_prose/) is the canonical authority on what the project is about -- researcher, 2026-08-18. Chapters 0-3 are reviewed and final; chapters 4-6 are not yet aligned (escalation pending, part (d)). cfg_prose_chapter names each chapter and its status; cfg_prose_concept points a key project concept (e.g. verse primacy, the inner-being definition) at the prose section that defines it, rather than restating the definition as a separate rule. A methodology/approach change that touches a concept named in cfg_prose_concept should flag whether the prose needs updating (part (f) -- the flagging MECHANISM is not yet built, this states the principle only)." | entry-point anchor for the prose-as-canonical-authority work -- part (a) of escalation #714 |
| `governance.scope_research_db` | "The research_db (bible_research.db) is the home for prose and findings with all the related enabling tables." |  |
| `raw.meaning_tree_clean_pattern` | "^(?:[^<]\|<(?!(?i:br\\b))[^>]*>)*$" | a clean strong_meaning_tree.sense_text: any text plus complete <ref>...</ref> spans (STEP's own citation markup, tolerated -- BUILD.md notes Greek mediumDef is prose with <ref> tags); any OTHER leftover markup (<br>, <b>, ...) fails -- the same <br> parser bug as strong_sense.head, one level deeper |

## 7. `cfg_behaviour_rule` -- rules naming prose specifically (2 rows, core)

| id | class | rule_key | rule_text | source |
|---:|---|---|---|---|
| 13 | `sqlite` | `dont-assume-which-database` | Don't assume which database a table lives in. bible_research.db (prose + analytic findings) and iba.db (process control + the entire base data layer) have a defined split; a 'no such table' error usually means the wrong database was opened, not a typo. | Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md |
| 15 | `documentation` | `obsidian-copy-not-authoritative` | An Obsidian-edited copy of a DB-generated `.md` file is never authoritative. The database row is the source of truth for prose, findings, and config -- editing the file doesn't change the database, and a regenerated export overwrites the edit. | Workflow/Obsidian/obsidian-usage-guide-v1-20260815.md |

## 8. `cfg_content_index_exclude` -- prose excluded from content indexing (1 row)

| pattern | reason |
|---|---|
| `Workflow/Programme/programme_prose/` | "researcher, 2026-08-17: exclude programme prose from content_index -- generated analysis prose saturated with the very biblical vocabulary being indexed (one file alone produced ~597,000 hits). Covers both the live extract and its archive/ copy via folder-prefix match." |

## 9. `cfg_write_grant` -- who may write the prose config tables (2 rows, full)

| writer | table_name | database |
|---|---|---|
| `configmaint.propose` | `cfg_prose_chapter` | `iba` |
| `configmaint.propose` | `cfg_prose_concept` | `iba` |

Only `configmaint.propose` may write `cfg_prose_chapter` / `cfg_prose_concept` -- consistent with `governance.config_control` (every `cfg_*` row governed by the configmaint rules).

## 10. `cfg_enum` -- controlled vocabulary for prose (3 rows, full)

| enum name | value | ordinal |
|---|---|---:|
| `config_module` | `prose` | 22 |
| `prose_chapter_status` | `reviewed` | 0 |
| `prose_chapter_status` | `not_yet_aligned` | 1 |

## 11. `cfg_table` -- the prose_section family (bible_research.db, 11 rows, full)

| table | grain | use | inactive |
|---|---|---|---:|
| `prose_section` | one row per id | The DB-canonical store of authored prose: one row per titled section of narrative — chapter readings, cluster essays, synthesis passages and programme documentation — with its full body text, version lineage and approval state. Almost all of it is machine-authored (claude_code or claude_ai); exactly one row is attributed to the researcher. | 0 |
| `prose_section_dimension_link` | one row per (prose_section_id, dimension_id, link_type) | Declared as a many-to-many link between prose sections and dimensions, with a link_type qualifying the relationship, but it holds 0 rows. It was created, keyed and uniquely indexed, and never used — a plausible casualty of the dimension layer's retirement. | 0 |
| `prose_section_finding_link` | one row per (prose_section_id, finding_id, link_type) | Declared as a many-to-many link between prose sections and findings, so that a passage could be traced to the evidence behind it, but it holds 0 rows. Its FK points at the legacy wa_session_b_findings rather than the live finding table, so it was superseded before it was ever populated. | 0 |
| `prose_section_fts` | no declared primary key — see cfg_column for prose_section_fts's real columns | An SQLite FTS5 virtual table providing full-text search over prose_section. Its columns mirror the source table one-for-one and hold no independent data; the underlying storage lives in the prose_section_fts_data/idx/content/docsize/config shadow tables. Because FTS5 columns are untyped, every column reports as type '?'. | 0 |
| `prose_section_fts_config` | one row per k | An FTS5-managed shadow table holding the configuration of the prose_section_fts index as key/value pairs. It is internal machinery written by SQLite, not by the study; the single row records the FTS5 format version in use. | 0 |
| `prose_section_fts_content` | one row per id | An FTS5-managed shadow table storing the raw column values of each indexed row, so the virtual table can return original text and support content-requiring operations. It is SQLite's internal copy of prose_section's indexed columns, positionally numbered c0..c6, not a hand-designed table. | 0 |
| `prose_section_fts_data` | one row per id | An FTS5-managed shadow table holding the inverted index itself as opaque binary segment blobs. It is SQLite internal machinery — the contents are not human-readable and must never be written or interpreted directly; the index is maintained automatically as prose_section changes. | 0 |
| `prose_section_fts_docsize` | one row per id | An FTS5-managed shadow table recording, per indexed document, the token count of each column in a packed binary form. FTS5 uses it for relevance ranking; it is internal machinery with one row per prose_section row. | 0 |
| `prose_section_fts_idx` | one row per (segid, term) | An FTS5-managed shadow table mapping index segments and term prefixes to the pages within prose_section_fts_data where their postings live — the b-tree lookup layer of the index. Internal machinery; the 'term' values are binary prefix keys, not words from the prose. | 0 |
| `prose_section_type` | one row per id | The controlled vocabulary of prose section kinds — 108 codes spanning programme documentation, per-session outputs, cluster findings and lexical prose — each with a label, the stage that produces it, and expected length bounds. It is the only real enforcement behind prose_section.section_type_id, and it has grown by accretion: over half the types belong to 'programme' rather than to any analytical stage. | 0 |
| `wa_prose_section_citations` | one row per id | Records which evidence a given prose section cites — a finding, a Q&A catalogue link, an SD pointer, or an observation sequence — together with the citation marker as it appears in the text. It covers only 25 prose sections out of 1,039 and was written in five batches in late April 2026; all its FKs point at the legacy Session B evidence tables, so it documents the old citation model rather than the live finding store. | 0 |

Plus the two IBA-side registry tables (already shown in full in §3-4): `cfg_prose_chapter`, `cfg_prose_concept`.

## 12. `cfg_column` -- prose_section family column catalogue (bible_research.db)

Every column of every `prose_section*` table, as governed by `governance.table_columns`. Grouped by table; the full `use` text is kept verbatim.

### `prose_section` (20 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `id` | INTEGER | PK |  | Surrogate primary key for the prose section. |
| 1 | `registry_id` | INTEGER |  | word_registry.id | The word_registry entry the section is about, where it is word-scoped. 86% NULL, since most sections are chapter- or cluster-scoped rather than tied to a single registry word. |
| 2 | `section_type_id` | INTEGER |  | prose_section_type.id | The kind of section, referencing prose_section_type. Heavily skewed — one type (lexical prose at chapter level) accounts for roughly half of all rows. |
| 3 | `heading` | TEXT |  |  | The section's title, typically naming the scripture unit and the reading performed (for example 'Amo 1 - inner-being reading'). Not unique: some headings repeat across versions. |
| 4 | `body` | TEXT |  |  | The prose itself — the actual authored text, often several thousand characters of markdown. This is the payload the whole table exists to hold and the content mirrored into the FTS index. |
| 5 | `word_count` | INTEGER |  |  | Cached length of body in words. Some rows record 0 despite holding text, so the count is not reliably maintained; the maximum (over 74,000) shows a few sections are book-length. |
| 6 | `status` | TEXT |  |  | Editorial state, CHECK-constrained to draft, in_review, approved or archived. The great majority are approved; 'in_review' is permitted but never used. |
| 7 | `version` | INTEGER |  |  | Version of the section. Declared INTEGER but the contents contradict that — the column holds strings such as '1_0', '2_0' and 'v1' alongside plain integers, so different writers used different conventions and the column cannot be compared numerically. |
| 8 | `supersedes_id` | INTEGER |  | prose_section.id | The earlier prose_section this row replaces. Present on 90 rows, forming a self-referential revision chain within the table. |
| 9 | `superseded_by_id` | INTEGER |  | prose_section.id | The inverse pointer to the row that replaced this one, maintained symmetrically with supersedes_id on the same 90 rows. |
| 10 | `author` | TEXT |  |  | Who wrote the section, CHECK-constrained to claude_ai, claude_code or researcher. The distribution is the notable thing: only one row in 1,039 is researcher-authored. |
| 11 | `created_at` | TEXT |  |  | When the section was written, in ISO-8601 UTC. This column is consistently formatted, unlike its equivalents in the finding tables. |
| 12 | `approved_at` | TEXT |  |  | When the section was approved. 87% NULL even though 922 rows are marked approved, so the approval timestamp was not kept in step with the status column. |
| 13 | `approved_by` | TEXT |  |  | The approver — either claude_code or the value 'manual_backfill', which records that approval was applied retrospectively rather than by an actual reviewer. Null on most approved rows. |
| 14 | `metadata_json` | TEXT |  |  | A JSON blob of scope and provenance for the section: book, chapter and verse list for chapter readings, or term, cluster_code, source and verses for term-scoped prose. Structure varies by section type and is not schema-enforced. |
| 15 | `source_file` | TEXT |  |  | The markdown file the prose was ingested from, recording the path or filename it came in on. Near-universally populated, showing the store was built by importing files rather than authoring in place. |
| 16 | `delete_flagged` | INTEGER |  |  | Soft-delete marker; 59 sections are flagged out. |
| 17 | `cluster_code` | TEXT |  |  | The M-code cluster the section belongs to, where cluster-scoped. 82% NULL, and free text with no FK to the cluster table. |
| 18 | `characteristic_id` | INTEGER |  |  | The characteristic the section discusses, where characteristic-scoped. Populated on only 124 rows. |
| 19 | `cluster_subgroup_id` | INTEGER |  |  | Intended to scope a section to a cluster subgroup, and indexed for that, but 100% NULL — declared and never used. |

### `prose_section_type` (16 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `id` | INTEGER | PK |  | Surrogate primary key, referenced by prose_section.section_type_id. |
| 1 | `code` | TEXT |  |  | The short machine name for the section type (for example 'cluster_essay', 'lexical_prose', 'cf_char_synth'). Unique across the table and the value exposed through the FTS index as section_type_code. |
| 2 | `label` | TEXT |  |  | The human-readable name of the section type, usually stating both what it is and who it is for (for example 'Cluster Essay (general-reader prose product)'). Unique per row. |
| 3 | `source_stage` | TEXT |  |  | The programme stage that produces this kind of prose — 'programme' for documentation plus the session_a/b/c/d family. Uncontrolled: no CHECK or FK constrains the eleven values in use. |
| 4 | `lifecycle_tag` | TEXT |  |  | Marks the generation of the type, using values like 'v1', 'v2' and 'source'. 77% NULL, so most types carry no lifecycle marker at all and the tag distinguishes only the reworked ones. |
| 5 | `chapter_no` | INTEGER |  |  | For cluster-publication types, the chapter of the finished product the section belongs to, giving the assembly order across a seven-chapter structure. |
| 6 | `description` | TEXT |  |  | Prose explaining what the section type is for, what tier of evidence sources it, and what consumes it. Missing on 32 types. |
| 7 | `expected_length_min` | INTEGER |  |  | The lower word-count guide for a section of this type. Null on 44 types, which therefore have no length expectation; it is guidance, not a constraint — nothing validates prose_section.word_count against it. |
| 8 | `expected_length_max` | INTEGER |  |  | The upper word-count guide for the type, paired with expected_length_min and null on the same set of types. Advisory only. |
| 9 | `sort_order` | INTEGER |  |  | Ordering position for presenting types within their stage or chapter; values repeat across groups, so it orders within a group rather than globally. |
| 10 | `delete_flagged` | INTEGER |  |  | Soft-delete marker; no type has been retired this way — all 108 remain live. |
| 11 | `created_at` | TEXT |  |  | When the type was defined. Values cluster into about twenty batches from April and May 2026, tracing how the vocabulary was extended in waves; formats mix space-separated and ISO-8601 UTC. |
| 12 | `book_order` | INTEGER |  |  |  |
| 13 | `book_label` | TEXT |  |  |  |
| 14 | `section_order` | INTEGER |  |  |  |
| 15 | `section_label` | TEXT |  |  |  |

### `prose_section_dimension_link` (4 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `prose_section_id` | INTEGER |  | prose_section.id | Intended to identify the prose section, with an FK to prose_section. Never populated. |
| 1 | `dimension_id` | INTEGER |  |  | Intended to identify the dimension discussed. Never populated, and notably it carries no FK, so the target table was never even named. |
| 2 | `link_type` | TEXT |  |  | Intended to qualify how the section relates to the dimension, defaulting to 'discusses'. Never populated, so no other link type is attested. |
| 3 | `created_at` | TEXT |  |  | Intended insertion timestamp, defaulting to datetime('now'). Never populated. |

### `prose_section_finding_link` (4 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `prose_section_id` | INTEGER |  | prose_section.id | Intended to identify the prose section, with an FK to prose_section. Never populated. |
| 1 | `finding_id` | INTEGER |  | wa_session_b_findings.id | Intended to identify the cited finding, with an FK to the legacy wa_session_b_findings table — not the live finding store. Never populated. |
| 2 | `link_type` | TEXT |  |  | Intended to qualify the relationship, defaulting to 'discusses'. Never populated. |
| 3 | `created_at` | TEXT |  |  | Intended insertion timestamp, defaulting to datetime('now'). Never populated. |

### `prose_section_fts` (7 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `body` |  |  |  | The indexed copy of prose_section.body — the searchable prose text; this is the column the index exists to serve. |
| 1 | `heading` |  |  |  | The indexed copy of prose_section.heading, so searches can match on section titles. |
| 2 | `section_type_code` |  |  |  | The indexed prose_section_type.code, denormalised into the index so results can be filtered by section kind without a join; 'lexical_prose_chapter' dominates. |
| 3 | `registry_id` |  |  |  | The indexed copy of prose_section.registry_id, allowing search results to be narrowed to a registry word. Null for most rows, as in the source. |
| 4 | `cluster_code` |  |  |  | The indexed copy of prose_section.cluster_code, for narrowing results to an M-code cluster. Null for most rows. |
| 5 | `characteristic_id` |  |  |  | The indexed copy of prose_section.characteristic_id, for narrowing results to a characteristic. Null for most rows. |
| 6 | `status` |  |  |  | The indexed copy of prose_section.status, so draft and archived sections can be excluded from search results. |

### `prose_section_fts_config` (2 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `k` |  | PK |  | The configuration key. Only 'version' is present, which is the FTS5 default configuration set. |
| 1 | `v` |  |  |  | The value for the key — here the integer 4, the FTS5 on-disk format version. |

### `prose_section_fts_content` (8 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `id` | INTEGER | PK |  | The FTS5 rowid, matching prose_section.id one-for-one across all 1,039 rows. |
| 1 | `c0` |  |  |  | Stored value of the first indexed column, body — the prose text. |
| 2 | `c1` |  |  |  | Stored value of the second indexed column, heading. |
| 3 | `c2` |  |  |  | Stored value of the third indexed column, section_type_code. |
| 4 | `c3` |  |  |  | Stored value of the fourth indexed column, registry_id. |
| 5 | `c4` |  |  |  | Stored value of the fifth indexed column, cluster_code. |
| 6 | `c5` |  |  |  | Stored value of the sixth indexed column, characteristic_id. |
| 7 | `c6` |  |  |  | Stored value of the seventh indexed column, status. |

### `prose_section_fts_data` (2 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `id` | INTEGER | PK |  | FTS5-assigned block identifier. Values are not a dense sequence — they encode segment and level information, which is why the range runs into the trillions across only 1,059 rows. |
| 1 | `block` | BLOB |  |  | The opaque binary payload of an index segment (posting lists and structure records), written and read only by FTS5. |

### `prose_section_fts_docsize` (2 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `id` | INTEGER | PK |  | The FTS5 rowid of the document, corresponding to prose_section.id. |
| 1 | `sz` | BLOB |  |  | A varint-encoded blob of per-column token counts for that document, read only by FTS5's ranking functions. |

### `prose_section_fts_idx` (3 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `segid` |  |  |  | The FTS5 segment identifier; the eleven values in use reflect how the index has been merged into segments, not anything about the prose. |
| 1 | `term` |  |  |  | A binary term-prefix key used to locate the right page of postings. Stored as a blob and not meaningful as text. |
| 2 | `pgno` |  |  |  | The page number within prose_section_fts_data at which postings for that term prefix begin. |

### `wa_prose_section_citations` (10 columns)

| # | column | type | pk | fk | use |
|---:|---|---|:---:|---|---|
| 0 | `id` | INTEGER | PK |  | Surrogate primary key for the citation row. |
| 1 | `prose_section_id` | INTEGER |  | prose_section.id | The prose section doing the citing. Only 25 distinct sections appear, so citation tracking was piloted on a small set and never rolled out. |
| 2 | `cited_finding_id` | INTEGER |  | wa_session_b_findings.id | The cited finding, referencing the legacy wa_session_b_findings table rather than the live finding store. Null on 45% of rows, which cite something other than a finding. |
| 3 | `cited_qa_link_id` | INTEGER |  | wa_finding_catalogue_links.id | The cited wa_finding_catalogue_links row (a finding-to-question mapping). Present on only four rows — effectively unused. |
| 4 | `cited_sd_pointer_id` | INTEGER |  | wa_session_research_flags.id | The cited Session D research pointer in wa_session_research_flags. Present on 38 rows. |
| 5 | `cited_observation_seq` | TEXT |  |  | The cited observation as a textual sequence code (for example 'OBS-067-OBS-014'), used where the observation has no row to point at. |
| 6 | `citation_form` | TEXT |  |  | The citation marker exactly as it appears in the prose — 'Q001', 'DIM-067-SD002', 'SP-067-018' and similar. This is the only column populated on every row, and the several distinct prefix families show the citation notation was never standardised. |
| 7 | `paragraph_no` | INTEGER |  |  | The paragraph of the prose section in which the citation occurs. 96% NULL, so the position of a citation within its section was almost never recorded. |
| 8 | `delete_flagged` | INTEGER |  |  | Soft-delete marker; no row has been flagged. |
| 9 | `created_at` | TEXT |  |  | Insertion timestamp. Only five distinct values, confirming the table is the output of five batch runs on 27 and 28 April 2026. |

### `cfg_prose_chapter` / `cfg_prose_concept` (iba.db, already shown in full in §3-4)

**`cfg_prose_chapter`**

| # | column | type | pk | use | filled_by |
|---:|---|---|:---:|---|---|
| 0 | `chapter` | INTEGER | PK | the chapter number (0-6 currently) | migration/bootstrap_prose_authority_v1_20260818.py |
| 1 | `title` | TEXT |  | the chapter's title | migration/bootstrap_prose_authority_v1_20260818.py |
| 2 | `status` | TEXT |  | 'reviewed' (final, per researcher 2026-08-18) or 'not_yet_aligned' (per cfg_enum prose_chapter_status) -- NOT derived from the prose extract file's own per-section status metadata, which is known stale (still shows 'draft' everywhere as of 2026-08-14) | migration/bootstrap_prose_authority_v1_20260818.py |
| 3 | `source_doc` | TEXT |  | the live prose extract file this chapter's content comes from | migration/bootstrap_prose_authority_v1_20260818.py |
| 4 | `description` | TEXT |  | what this chapter covers | migration/bootstrap_prose_authority_v1_20260818.py |
| 5 | `added_at` | TEXT |  | when this chapter was registered | migration/bootstrap_prose_authority_v1_20260818.py |

**`cfg_prose_concept`**

| # | column | type | pk | use | filled_by |
|---:|---|---|:---:|---|---|
| 0 | `concept_key` | TEXT | PK | short kebab/snake-case identifier, e.g. 'verse_primacy' | migration/bootstrap_prose_authority_v1_20260818.py |
| 1 | `chapter` | INTEGER |  | which cfg_prose_chapter defines this concept | migration/bootstrap_prose_authority_v1_20260818.py |
| 2 | `section_hint` | TEXT |  | which section(s) within the chapter, in plain language (prose sections aren't independently keyed yet) | migration/bootstrap_prose_authority_v1_20260818.py |
| 3 | `description` | TEXT |  | a short gloss of the concept, for discoverability -- the prose itself remains authoritative for the full definition | migration/bootstrap_prose_authority_v1_20260818.py |
| 4 | `source` | TEXT |  | provenance -- which prior rule/decision this concept pointer replaces or derives from | migration/bootstrap_prose_authority_v1_20260818.py |
| 5 | `added_at` | TEXT |  | when this concept was registered | migration/bootstrap_prose_authority_v1_20260818.py |

## 13. `cfg_unique` -- prose_section link-table uniqueness (8 rows, full)

- **`prose_section_dimension_link`**: `prose_section_id`, `dimension_id`, `link_type`
- **`prose_section_finding_link`**: `prose_section_id`, `finding_id`, `link_type`
- **`prose_section_fts_idx`**: `segid`, `term`

## 14. `cfg_change_detail` -- change history touching prose config (2 relevant rows)

6 rows matched the raw scan; 4 are `raw.meaning_tree_clean_pattern` edits where "prose" appears only inside a `use` string describing STEP's Greek `mediumDef` markup (incidental, listed in §15). The 2 core rows:

| id | run_id | table | op | applied_at |
|---:|---|---|---|---|
| 277 | `RUN-20260817_145306_062-CONFIGMAINT` | `cfg_content_index_exclude` | insert | 2026-08-17T14:02:11Z |

## 15. Incidental matches -- "prose" used as an ordinary English word (noise, listed for completeness)

These rows matched the raw text search but are not prose-*store* configuration -- the word "prose" appears only as a plain-English descriptor of a free-text column on an unrelated table. Listed so nothing found is silently dropped.

**`cfg_column` rows (table/column only, not the prose store):**

`bible_research.characteristic.definition`, `bible_research.cluster.gloss`, `bible_research.cluster_finding.finding_text`, `bible_research.cluster_subgroup.core_description`, `bible_research.finding.finding_value`, `bible_research.ib_characteristic.ledger`, `bible_research.ib_observation.narrative`, `bible_research.mti_terms.transliteration`, `bible_research.mti_terms.anchor_note`, `bible_research.phase2_flag_types.description`, `bible_research.segment_unit.gist`, `bible_research.session_d_runs.run_summary`, `bible_research.themes.description`, `bible_research.ve_lexical.value`, `bible_research.ve_lexical.direction`, `bible_research.ve_lexical_overlay_reverse_20260626.value`, `bible_research.verse_context.set_aside_reason`, `bible_research.wa_cross_registry_links.note`, `bible_research.wa_dimension_index.notes`, `bible_research.wa_finding_catalogue_links.id`, `bible_research.wa_finding_catalogue_links.session_b_note`, `bible_research.wa_meaning_parsed.parse_warnings`, `bible_research.wa_obs_question_catalogue.review_note`, `bible_research.wa_patch_type_registry.type_code`, `bible_research.wa_quality_flag_types.description`, `bible_research.wa_session_b_dimensions.relational_environment_note`, `bible_research.wa_session_b_dimensions.spirit_soul_body_note`, `bible_research.wa_session_b_dimensions.inner_operations_note`, `bible_research.wa_session_b_dimensions.being_note`, `bible_research.wa_session_research_flags.description`, `bible_research.word_registry.description`, `bible_research.word_registry.sb_classification_reasoning`, `iba.passage.open_decisions_note`, `iba.strong_lsj_parsed.note`

**`cfg_table` rows (incidental):**

`bible_research.phase2_flag_types`, `bible_research.ve_lexical_overlay_reverse_20260626`, `bible_research.wa_cross_registry_links`, `bible_research.wa_quality_flag_types`, `bible_research.wa_session_b_dimensions`, `iba.cfg_behaviour_rule`

**`cfg_behaviour_rule` / `cfg_escalation` (incidental -- "chat prose" = plain text, not the DB store):**

- `cfg_behaviour_rule` id 21: `chat-items-become-escalations` (class `chat`)
- `cfg_escalation` id 5: `chat_routing`

**`cfg_change_detail` (incidental -- STEP `mediumDef` markup parsing, ids 21/23/24; governance rule insert, id 67):**

id 21 (`cfg_setting` insert), id 23 (`cfg_setting` update), id 24 (`cfg_setting` update), id 67 (`cfg_setting` insert)

---

*Extract produced by direct SQLite query against `iba/app/db/iba.db`'s `cfg_*` tables, 2026-08-21.*