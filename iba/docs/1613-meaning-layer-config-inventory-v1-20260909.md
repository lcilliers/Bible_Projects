# #1613 — Base-Data Meaning Layer: Full `cfg_*` Reference Inventory

**Escalation:** #1613, "Normalise meaning representation in base data"
**Date:** 2026-09-09
**Status:** input document — inventory only, no design decision made here. Scope of what
"normalising meaning" should produce is still open per #1613's own text.

> **★ CORRECTION (researcher, this session, after §15 v1 was written):** §15's original
> recommendation — `strong_meaning_parsed` as master truth — is **wrong** and is struck through
> below, left in place rather than deleted so the correction is visible. The researcher's own
> reasoning: **`strong` is the master truth table.** It is the only table in this layer that
> chains to `span`, which chains to `verse` — and `verse` is the actual foundation of the study.
> Every other table in this document is derived from `strong` in some way; none of them anchor to
> the verse text on their own. §15 is corrected below; §17 is the comprehensive completeness/quality
> audit of `strong` and every table that depends on it, run live for this correction.

## 1. Scope and method

**Table set.** #1613's own context names the "base-data meaning layer, as it actually exists
live" as exactly these 8 `iba.db` tables:

| Table | Role |
|---|---|
| `strong` | the Strong's code's identity row (L2 anchor) |
| `strong_sense` | one-line head/brief meaning per strong |
| `strong_meaning_tree` | raw STEP meaning data (sense tree, per lemma) |
| `strong_meaning_parsed` | parsed form of `strong_meaning_tree` |
| `strong_lexicon` | raw LSJ + Mounce text (Greek only) |
| `strong_lsj_parsed` | parsed form of `strong_lexicon.lsj` (classical Greek) |
| `strong_mounce_parsed` | parsed form of `strong_lexicon.mounce` |
| `strong_related` | STEP-fetched related-term links (not derived from any raw table) |

This document does not widen that set on its own judgement — it is exactly the set #1613 named.
(`strong_verse` and `word_strong` are the identity/verse-linkage layer around `strong`, not the
meaning layer, and are excluded; they appear below only where a config row happens to reference
them incidentally.)

**Method.** Every `cfg_*` table (43 of them, `iba.db`) was searched two ways:
(a) an exact match on any column literally named `table_name` (`cfg_column`, `cfg_index`,
`cfg_unique`, `cfg_write_grant`, `cfg_report_csv_table`, `cfg_table_purpose`, `cfg_table`), and
(b) a whole-word regex scan of every free-text column in every other `cfg_*` table for the 8 table
names. Every row that matched either way is included below in full (not paraphrased), grouped by
`cfg_*` table. `cfg_change_detail` (the migration audit trail) is summarised rather than dumped —
it recorded the same rows going in, not a distinct governing rule.

---

## 2. `cfg_table` — table-level grain/use

| Table | Grain | Use |
|---|---|---|
| `strong` | one row per strong — unique, global to the study | L2 — the strong's identity. The meaning is normalised out (O4): it lives in `strong_sense` / `strong_meaning_tree` / `strong_lexicon`. |
| `strong_sense` | one row per strong — the sense HEAD | the span's meaning, read constantly. The head is the first line of `mediumDef` (the sense); `is_own_lemma` marks a code that is its own lemma, where the gloss carries the sense. |
| `strong_meaning_tree` | one row per sense-node of a LEMMA's definition tree | the lemma's full range — read rarely, only when the broader context is needed. Keyed on the lemma (shared across its senses, which the prototype proved). |
| `strong_meaning_parsed` | one row per gloss segment of a `strong_meaning_tree` lemma (2026-07-25 corrected parse) | L2b — the parsed meaning layer over `strong_meaning_tree` (raw). Segment-scoped: refs/note belong to the exact `<b>` span they followed, not pooled across the whole source row (the original extract's bug, fixed before this table existed). Comma/semicolon are NOT sense separators here — only a literal line break splits a gloss further. |
| `strong_lexicon` | one row per strong that has LSJ/Mounce (Greek) | the large lexicon text — separate because rarely scanned |
| `strong_lsj_parsed` | one row per LSJ sense of a `strong_lexicon.lsj` entry (2026-07-25 corrected parse) | L2b — the parsed classical-Greek lexicon layer over `strong_lexicon.lsj` (raw). Sense blocks split on LSJ's own `<LevelN>`/`<br>` structure; gloss kept whole within a block, not exploded on internal commas. |
| `strong_mounce_parsed` | one row per Mounce sense of a `strong_lexicon.mounce` entry (2026-07-25 corrected parse) | L2b — the parsed Greek lexicon layer over `strong_lexicon.mounce` (raw). Split ONLY on `<br>` (the source's real line breaks); comma/semicolon within one line are punctuation inside a sense, not sense separators. |
| `strong_related` | one row per (strong, related strong) pair STEP's `getInfo` returned (fetched 2026-07-25) | L2b — NOT derived from any raw table; fetched live from STEP per full strong code (`lib.stepapi.Step.call2_getInfo`, `vocabInfos[0].relatedNos`) since no raw table captures this. `related_strong` is unconstrained — STEP can name a code this app has never onboarded via `raw.detail`. |

All 8 rows: `database='iba'`, `category='data'`, `inactive=0`.

---

## 3. `cfg_column` — full column catalogue, all 8 tables

### `strong` (10 columns)
| Column | PK | FK | Use | Source |
|---|---|---|---|---|
| `strongNumber` | ✓ | — | the resolved Strong's code — the key | `call2.vocabInfos[0].strongNumber` |
| `accentedUnicode` | | — | the actual Hebrew/Greek word | `call2.vocabInfos[0].accentedUnicode` |
| `stepGloss` | | — | short English sense | `call2.vocabInfos[0].stepGloss` |
| `stepTransliteration` | | — | romanised form; never shown without the gloss | `call2.vocabInfos[0].stepTransliteration` |
| `language` | | — | Hebrew/Greek from the code prefix | `derived:call2.strongNumber` |
| `count` | | — | STEP token frequency — NOT a verse count, may be capped | `call2.vocabInfos[0].count` |
| `freqList` | | — | raw frequency distribution | `call2.vocabInfos[0].freqList` |
| `created_at` | | — | when first fetched | filled by `raw.detail` |
| `deleted` | | — | soft delete | — |
| `origin` | | — | `'word'` = deliberately onboarded for a registry word (`raw.discover` → `word_strong` → `raw.detail`); must carry the full raw-data-integrity chain. `'backfill'` = onboarded by `raw.backfill_meaning`'s book-scoped completeness sweep, independent of any word; not in scope for cluster/meaning-relevance mapping, used only to support lexical resolution. Sticky: an upgrade `backfill`→`word` can happen; never downgraded. | migrated one-time classification, then stamped by `detail_one()` going forward; filled by `raw.detail_one` |

### `strong_sense` (4 columns)
| Column | PK | FK | Use | Source |
|---|---|---|---|---|
| `strong` | ✓ | `strong.strongNumber` | the strong | — |
| `head` | | — | the sense — THE SPAN'S MEANING | `derived:call2.mediumDef.head` (expectation: `nohtml`) |
| `is_own_lemma` | | — | 1 = no ': ' head; the code is its own lemma and the gloss is the sense | `derived:call2.mediumDef` |
| `deleted` | | — | soft delete | — |

### `strong_meaning_tree` (7 columns)
| Column | PK | FK | Use | Source |
|---|---|---|---|---|
| `id` | ✓ | — | surrogate key | — |
| `lemma_key` | | — | the base code the tree belongs to | `derived:call2.strongNumber.base` |
| `sense_code` | | — | the tree position: `1)`, `1a)`, `1b1)` | `derived:call2.mediumDef.tree` |
| `sense_text` | | — | the sense line | `derived:call2.mediumDef.tree`; expectation: `pattern:raw.meaning_tree_clean_pattern` |
| `sort` | | — | order within the tree | `derived:call2.mediumDef.tree` |
| `deleted` | | — | soft delete | — |
| `strong_variant` | | `strong.strongNumber` | (no `use` text recorded — see §9 finding) | — |

### `strong_meaning_parsed` (10 columns)
| Column | PK | FK | Use | Source |
|---|---|---|---|---|
| `id` | ✓ | — | surrogate key | — |
| `lemma_key` | | — | the base code this parsed sense belongs to (never a sub-entry letter) | `derived:strong_meaning_tree.lemma_key` |
| `sort` | | — | order within the source sense tree | `parsed:strong_meaning_tree.sort` |
| `sense_code` | | — | the tree position, e.g. `1a1a)` — or the `sense_code` column value verbatim | `parsed:strong_meaning_tree.sense_code` |
| `gloss` | | — | one exploded gloss term, kept whole (no comma/semicolon splitting) | `parsed:strong_meaning_tree.sense_text`; expectation `notblank` |
| `verse_refs` | | — | verse citations scoped to this gloss's own `<b>` span, semicolon-joined | `parsed:strong_meaning_tree.sense_text` |
| `note` | | — | commentary scoped to this gloss's own segment, not pooled across the row | `parsed:strong_meaning_tree.sense_text` |
| `row_type` | | — | lookup / description / not applicable — `lexicon_split_common.classify_row()` | `derived:gloss` |
| `deleted` | | — | soft delete | — |
| `strong_variant` | | `strong.strongNumber` | (no `use` text recorded — see §9 finding) | — |

### `strong_lexicon` (4 columns)
| Column | PK | FK | Use | Source |
|---|---|---|---|---|
| `strong` | ✓ | `strong.strongNumber` | the strong | — |
| `lsj` | | — | LSJ entry (Greek) | `call2.vocabInfos[0].lsjDefs` |
| `mounce` | | — | Mounce short def (Greek) | `call2.vocabInfos[0].shortDefMounce` |
| `deleted` | | — | soft delete | — |

### `strong_lsj_parsed` (7 columns)
| Column | PK | FK | Use | Source |
|---|---|---|---|---|
| `id` | ✓ | — | surrogate key | — |
| `strong` | | `strong.strongNumber` | the full strong code this LSJ sense belongs to | `derived:strong_lexicon.strong`; `notnull` |
| `sense_label` | | — | LSJ sense position, e.g. `I` / `I.2` / `II.2.b`, or `'headword'` | `parsed:strong_lexicon.lsj` |
| `gloss` | | — | the sense's bold-span gloss text, kept whole (no comma splitting); may legitimately be blank when a block carries only dialect/citation notes | `parsed:strong_lexicon.lsj` |
| `note` | | — | dialect/grammar labels, connective prose — everything in the block but the gloss | `parsed:strong_lexicon.lsj` |
| `row_type` | | — | `headword` for the entry's own headword row(s), `lookup` for every sense row | `derived:sense_label` |
| `deleted` | | — | soft delete | — |

### `strong_mounce_parsed` (5 columns)
| Column | PK | FK | Use | Source |
|---|---|---|---|---|
| `id` | ✓ | — | surrogate key | — |
| `strong` | | `strong.strongNumber` | the full strong code this Mounce line belongs to | `derived:strong_lexicon.strong`; `notnull` |
| `mounce_parsed` | | — | one `<br>`-delimited line of Mounce's entry, kept whole (no comma splitting) | `parsed:strong_lexicon.mounce` |
| `row_type` | | — | lookup / description — `lexicon_split_common.classify_row()` | `derived:mounce_parsed` |
| `deleted` | | — | soft delete | — |

### `strong_related` (7 columns)
| Column | PK | FK | Use | Source |
|---|---|---|---|---|
| `id` | ✓ | — | surrogate key | — |
| `strong` | | `strong.strongNumber` | the full code of the SOURCE term STEP was asked about | `fetched:STEP.getInfo`; `notnull` |
| `related_strong` | | — (unconstrained) | the full code of the RELATED term — may have no `strong` row of its own yet | `fetched:STEP.getInfo.relatedNos.strongNumber`; `notnull` |
| `related_form` | | — | the related term's native-script form | `fetched:STEP.getInfo.relatedNos.matchingForm` |
| `related_transliteration` | | — | the related term's transliteration | `fetched:STEP.getInfo.relatedNos.stepTransliteration` |
| `related_gloss` | | — | the related term's own short gloss | `fetched:STEP.getInfo.relatedNos.gloss` |
| `deleted` | | — | soft delete | — |

**Note (both `strong_variant` columns):** the `strong_meaning_tree.strong_variant` and
`strong_meaning_parsed.strong_variant` columns each carry an FK to `strong.strongNumber` but have
`type=NULL` and no `use` text in `cfg_column` — see §9 finding.

---

## 4. `cfg_index` / `cfg_unique` — indexing

| Table | Index name | Columns |
|---|---|---|
| `strong_lexicon` | `idx_strong_lexicon_strong` | `strong`, `deleted` |
| `strong_lsj_parsed` | `idx_strong_lsj_parsed_strong` | `strong`, `deleted` |
| `strong_meaning_parsed` | `idx_strong_meaning_parsed_strong_variant` | `strong_variant`, `deleted` |
| `strong_meaning_tree` | `idx_strong_meaning_tree_strong_variant` | `strong_variant`, `deleted` |
| `strong_mounce_parsed` | `idx_strong_mounce_parsed_strong` | `strong`, `deleted` |
| `strong_related` | `idx_strong_related_strong` | `strong`, `deleted` |
| `strong_sense` | `idx_strong_sense_strong` | `strong`, `deleted` |

`strong` itself has no `cfg_index` row (its PK, `strongNumber`, is already indexed by being the
primary key) and no `cfg_unique` row among the 8. (For comparison, `strong_verse.strong` and
`word_strong.strong` do carry `cfg_unique` rows — outside this 8-table scope, listed here only
because they matched the free-text/column search.)

No `cfg_index` row exists on `strong_meaning_tree.lemma_key` or `strong_meaning_parsed.lemma_key`
— the two tables' actual shared join key — only on `strong_variant`. Confirmed absent, not just
unlisted here.

---

## 5. `cfg_write_grant` — who is allowed to write each table

| Table | Writer |
|---|---|
| `strong` | `call2_getInfo`, `strong.reconcile` |
| `strong_sense` | `call2_getInfo` |
| `strong_meaning_tree` | `call2_getInfo` |
| `strong_lexicon` | `call2_getInfo` |
| `strong_meaning_parsed` | `lexicon.parse` |
| `strong_lsj_parsed` | `lexicon.parse` |
| `strong_mounce_parsed` | `lexicon.parse` |
| `strong_related` | `lexicon.related` |

All 8 grants: `database='iba'`, `inactive=0`. This is a clean single-writer picture per table — no
table in this layer has more than one live writer.

---

## 6. `cfg_api` — the STEP calls behind the raw layer

| Name | Route | Input |
|---|---|---|
| `call2_getInfo` | `rest/module/getInfo/{version}//{strong}//` | a strong |
| `call3_strong` | `rest/search/masterSearch/strong={strong}\|version={version}` | a strong |

`call2_getInfo` is the one source for `strong` + `strong_sense` + `strong_meaning_tree` +
`strong_lexicon` (`raw.detail`) and, separately, for `strong_related` (`lexicon.related`, one live
call per row via `relatedNos`). `call3_strong` is the verse-linkage call (`strong_verse`/`verse`/
`span`) — outside the meaning layer proper.

---

## 7. `cfg_step` — every process step that touches these tables

| Step | Work package | Kind | Inactive | Does |
|---|---|---|---|---|
| `raw.detail` | `new-word` | operations | 0 | CALL 2 `getInfo` per strong → strong + sense + tree + lexicon (the meaning) |
| `raw.verses` | `new-word` | operations | 0 | CALL 3 per strong → `strong_verse` + `verse` + `span` (span parsed from preview) |
| `raw.backfill_meaning` | `raw-backfill` | operations | 0 | for a book (optionally narrowed to one chapter's verse range via `-Range C:V-V`), find every distinct strong its spans reference that has no `strong` row yet, and pull ONLY the meaning (STEP `getInfo` → strong/strong_sense/strong_meaning_tree/strong_lexicon) — not verses. Reuses `raw.detail_one()` unchanged. Progressive, passage-driven DB coverage growth, not a full-Bible bulk pull. |
| `lexicon.parse` | `lexicon-parse` | operations | 0 | `strong_meaning_tree` + `strong_lexicon` → `strong_meaning_parsed`/`strong_lsj_parsed`/`strong_mounce_parsed` (corrected 2026-07-25 parse); no network, deterministic, clears and rebuilds |
| `lexicon.related` | `lexicon-parse` | operations | 0 | `strong` → `strong_related`; one live STEP `getInfo` call per row (`relatedNos`) |
| `lexicon.validate` | `lexicon-parse` | operations | 0 | read-only coverage + value-quality check **"across all 4 tables"** (verbatim); persists `lexicon.quality_report_path` every run; escalates only if findings exist — see §9 finding on this wording vs. its actual 6-table `cfg_report_csv_table` wiring |
| `candidate.set` *(inactive)* | `set-candidates` | operations | 1 | stamp `span_candidate` on the book's spans whose base-strong is a candidate |
| `candidate.validate` *(inactive)* | `candidate-quality` | operations | 1 | read-only quality check: `candidate_tag` null/format, `lemma_key`/`strong` resolution — one escalation per invocation, standalone |
| `report.strong_meaning` | `strong-meaning-report` | utility | 0 | meaning-parse layer coverage — `strong`/`strong_sense`/`strong_meaning_tree`/`strong_lexicon` gap list, sense-count distribution, lexicon completeness |
| `report.registry` | `registry-report` | utility | 0 | evaluate/review `word_registry` — summary, join to `strong`, sense report grouped by gloss |
| `report.word_registry_span` | `word-registry-span-report` | utility | 0 | `word_registry` : `word_strong` : `strong` : `strong_meaning_parsed` : `verse_lexical` : span analysis, for one registry word — every linked Strong's with its parse-meaning breakdown and unique surface-span applications — read-only |
| `report.strong_verse` | `strong-verse-report` | utility | 0 | on-demand verse restatement for one Strongs reference (`verse_lexical.strong` exact match, whole Bible) in the context of a registry word |
| `report.cluster` | `cluster-report` | utility | 0 | evaluate/review the cluster taxonomy and `cluster_strong` assignment coverage, scoped to `strong.origin=word` |
| `cluster.assign` | `cluster-assign` | operations | 0 | DB-wide sweep: `lib.strongreconcile.reconcile()` per strong — mechanical HIGH-precedent classification + backfill-to-word promotion cascade |
| `strong.reconcile` | `new-word` | operations | 0 | cluster-classify and, where warranted, promote every one of the word's own codes — runs last in `new-word`, after verses/spans are validated |
| `lexical.build` | `verse-lexical` | operations | 0 | mechanical T1-T3 engine: stem/voice-selects the operative sense **from `strong_meaning_parsed` via `morph_code`** (not the whole six-stem/voice paradigm) — this is `resolved_sense`'s actual, single-source derivation |
| `lexical.enrich` | `verse-lexical` | operations | 0 | Stage 1 Layer 2 — JSON-payload-driven; every content-role code gets a full `strong_related` pull as `note_type='related_word'` rows (per `cfg_method_rule` #52, §8) |
| `lexical.run` | `verse-lexical` | operations | 0 | Window 1 front door; resolves a selector to a verse-list, then runs Layer 1/2 over it |
| `report.lexical_extract` | `verse-lexical` | operations | 0 | multi-filter JSON extract over `verse_lexical`/`verse_lexical_note` |

**Pipeline wiring note:** `lexicon-parse` (`lexicon.parse` → `lexicon.related` → `lexicon.validate`)
is its own `cfg_work_package` row with `chained=0`, `runs_over='none'` — a standalone, manually
invoked package. It is **not** a step inside `new-word`'s chain (which stops at `strong.reconcile`,
ordinal 7) and **not** inside `raw-backfill`'s chain (`raw.backfill_meaning` alone). Both of the
latter two write straight into `strong_meaning_tree`/`strong_lexicon` (the raw tables) but never
themselves trigger `lexicon.parse`/`lexicon.related` to catch the parsed/related tables back up.
See §14.

---

## 8. `cfg_method_rule` — the only two documented rules

These are the **only** `cfg_method_rule` rows anywhere that mention any of the 8 tables:

- **#44 `language-testament-derivation`** (step `lexical.build`): "language and testament are
  denormalized onto `verse_lexical` unconditionally, at build time — `language` = `strong.language`
  (verbatim copy); testament = 'OT' if `cfg_book_order.ordinal<=38` else 'NT'. Both mechanical, no
  judgement, run on every row." (`source_doc`: design doc §5.1/§3.E)
- **#52 `related-word-pull-total-sorting-manual`** (step `lexical.enrich`): "Every content-role code
  gets a full, unconditional `strong_related` pull as `note_type='related_word'` rows. The pull is
  mechanical/total; same-concept-vs-coincidental sorting is Layer 2,
  `resolution_status='unclassified'` until sorted." (`source_doc`: checklist doc; design doc §3.F)

Neither rule touches the `strong_meaning_tree`→`strong_meaning_parsed` completeness question, the
lsj/mounce-vs-meaning_parsed coverage divergence, or a routing principle for which of the 3 parse
tables to consult for a given code. This is a direct, first-hand confirmation of #1613's own claim
("NO cfg_method_rule documents the completeness principle").

---

## 9. `cfg_on_fail` — failure handling

- `raw.detail`: "a strong returned no vocab from STEP — missing lexical data, worth a decision, not
  a silent continue."
- `report.strong_verse`, condition `strong-not-linked`: "the requested Strongs code is not linked
  to this registry word (`word_strong`)" — `path: report-stop`, `route: terminal`.

Neither addresses a strong that resolves in `strong_lexicon`/lsj/mounce but not in
`strong_meaning_tree`/`strong_meaning_parsed` (or vice versa) — the exact 45-strong gap #1613
describes has no defined failure-handling row.

---

## 10. `cfg_report` / `cfg_report_section` / `cfg_report_csv_table` — how this layer is reported

**`cfg_report`:**
- `report.strong_meaning` — no title captured in this scan's direct hits, wired via `cfg_report_csv_table` (below).
- `lexicon.validate` — title "Lexicon-parse quality report", `output_kind: md+csv`, 3 sections (`summary`, `coverage`, `value_quality`).
- `report.strong_verse` — title `"{word} -- {strong} -- verse restatement by Strongs reference"`.
- `report.cluster` — title "Cluster taxonomy and strong-assignment coverage".

**`cfg_report_csv_table` — the actual per-report table wiring:**

| Step | Tables (from this scope) | Join note |
|---|---|---|
| `report.strong_meaning` | `strong` | "the raw table this report analyzes for lexicon-completeness/gap-list sections" |
| `report.strong_meaning` | `strong_lexicon` | "the raw table this report analyzes for lexicon-completeness sections" |
| `report.strong_meaning` | `strong_meaning_tree` | "joined to `strong.stepGloss` via `lemma_key`" |
| `report.strong_meaning` | `strong_sense` | "joined to `strong.stepGloss`" |
| `lexicon.validate` | `strong` | "the raw table this report analyzes for its coverage check" |
| `lexicon.validate` | `strong_lexicon` | "the raw table this report analyzes for lexicon-detail coverage" |
| `lexicon.validate` | `strong_lsj_parsed` | — |
| `lexicon.validate` | `strong_meaning_parsed` | — |
| `lexicon.validate` | `strong_mounce_parsed` | — |
| `lexicon.validate` | `strong_related` | — |
| `report.registry` | `word_registry_strong_pairing` *(virtual)* | "joined to `word_strong`/`strong`/`strong_sense`" |

**Finding:** `lexicon.validate`'s own `cfg_step.does` text says it checks "across all 4 tables",
but its live `cfg_report_csv_table` wiring lists **6** tables (`strong`, `strong_lexicon`,
`strong_lsj_parsed`, `strong_meaning_parsed`, `strong_mounce_parsed`, `strong_related`). Flagged as
a discrepancy in the config text itself, not resolved here — either the "4" undercounts what the
report actually reads, or "4" meant something narrower (e.g. the 4 *parsed/related* output tables,
excluding the 2 *raw* source tables `strong`/`strong_lexicon`) that the `does` text never spells
out. Either way, it does not change #1613's underlying finding: none of these rows, by table name
alone, establish that `lexicon.validate` checks `strong_meaning_tree`→`strong_meaning_parsed`
**row-level** coverage (as opposed to `strong_lexicon`→lsj/mounce coverage) — confirming that
question needs a code read, which is out of scope for a config inventory.

**`cfg_report_section`** headings that name these tables: `candidate.validate` → "Lemmas with no
strong entry yet (by frequency)"; `report.strong_meaning` → "strong rows with no strong_sense yet
(by usage count)" and "Sense-count distribution (strong_meaning_tree)"; `report.registry` →
"Registry word joined to strong"; `lexicon.validate` → "Coverage — strong_lexicon/strong rows with
no parsed/related output"; `report.cluster` → "Word-origin strong count per cluster".

---

## 11. `cfg_setting` — parameters governing this layer

| Key | Module | Value | Use |
|---|---|---|---|
| `language.greek_prefix` | `raw` | — | "a strong starting with this is Greek; else Hebrew" |
| `report.strong_fields` | `report` | — | "which columns the L1→L2 strong table shows" |
| `step.span_html` | `step` | `<span(?: var='[^']*')?(?: morph='([^']*)')? strong='([^']*)'>([^<]*)</span>` | "how STEP formats an interlinear span in a verse preview: (morph, strong, surface). The forward-walk and the span parse read it." |
| `raw.meaning_tree_clean_pattern` | `raw` | `^(?:[^<]\|<ref[^>]*>[^<]*</ref>)*$` | "a clean `strong_meaning_tree.sense_text`: any text plus complete `<ref>...</ref>` spans (STEP's own citation markup, tolerated); any OTHER leftover markup (`<br>`, `<b>`, ...) fails — the same `<br>` parser bug as `strong_sense.head`, one level deeper" |
| `report.strong_meaning_path` | `report` | `"research/discovery/strong-meaning.md"` | where `report.strong_meaning` persists its output |
| `report.auto_backfill_before_render` | `report` | `true` | "`report.verse_span_meaning` auto-runs `raw.backfill_meaning_for()` for any span whose strong is not yet registered ... researcher direct 2026-07-26 instruction (do not leave partial-coverage reports as a silent manual follow-up step)" |
| `lexicon.outline_code_pattern` | `lexicon` | `^(\d+[a-zA-Z0-9]*\))\s*(.*)$` | "`strong_meaning_tree.sense_text`: matches a leading outline code ... when `sense_code` itself is empty, splitting it from the remaining gloss text" |
| `lexicon.linebreak_pattern` | `lexicon` | `[\r\n]+` | "the only recognised sense-separator in `strong_meaning_tree.sense_text`/`strong_lexicon.lsj`/`mounce` — commas/semicolons/colons are NOT separators" |
| `lexicon.bracket_pairs` | `lexicon` | `{"(": ")", "[": "]", "{": "}"}` | classify_row/strip_bracketed bracket nesting |
| `lexicon.classify_lookup_max_words` | `lexicon` | `3` | classify_row lookup-vs-description word-count threshold |
| `lexicon.lsj_level_tags` | `lexicon` | `["level1","level2","level3","level4"]` | LSJ outline-level HTML tag names |
| `lexicon.lsj_sublabel_pattern` | `lexicon` | `^\d+[a-z]*$` | LSJ sublabel shape |
| `lexicon.lsj_top_level_label_pattern` | `lexicon` | `^[IVXLCDM]+$` | LSJ top-level Roman-numeral shape |
| `lexicon.non_latin_script_pattern` | `lexicon` | `[Ͱ-Ͽἀ-῿֐-׿]` | forces `row_type='description'` on Greek/Hebrew script |
| `lexicon.quality_report_path` | `lexicon` | `"research/discovery/lexicon-parse.md"` | where `lexicon.validate` persists its findings |
| `lexicon.ref_tag_pattern` | `lexicon` | `<ref=['"]([^'"]*)['"]>` | matches STEP's malformed `<ref='...'>` markup for pre-parse rewriting |
| `report.strong_verse_output_dir` | `report` | `"iba/app/verse-analysis/word_registry"` | base folder for `report.strong_verse` output |
| `cluster.assign.word_optional_clusters` | `cluster` | `["T2","T3"]` | cluster codes exempt from the needs-a-`word_registry`-link rule |

No `cfg_setting` row exists for a routing/priority order between `strong_meaning_parsed`,
`strong_lsj_parsed`, and `strong_mounce_parsed` — confirming, from the settings side, the same "no
index/routing table" gap #1613 names.

---

## 12. `cfg_utility` — code modules

| Module | File | Inactive | Purpose (verbatim) |
|---|---|---|---|
| `lexiconparse` | `iba/app/lib/lexiconparse.py` | 0 | "lexiconparse.py — the governed parse of the raw lexicon layer (strong_meaning_tree.sense_text," *(cut off — see §13 finding)* |
| `registryreport` | `iba/app/lib/registryreport.py` | 0 | "registryreport.py — evaluate/review the `word_registry`: a summary, its join to `strong` (via" *(cut off)* |
| `strongreport` | `iba/app/lib/strongreport.py` | 0 | "strongreport.py — analysis of the meaning-parse layer (`strong` + `strong_lexicon` +" *(cut off)* |
| `wordregistryspanreport` *(inactive)* | `iba/app/lib/wordregistryspanreport.py` | 1 | "NON-COMPLIANT (escalation #648 — hardcoded constant(s) that should be cfg_setting-driven) ... word_registry -> word_strong -> strong -> parse-meaning -> unique" *(cut off)* |
| `strongreconcile` | `iba/app/lib/strongreconcile.py` | 0 | "strong reconciliation utility" |
| `contentindex` | `iba/app/lib/contentindex.py` | 0 | "file-content concordance search over .md files, keyed on Strong's numbers/glosses/words sourced from strong/word_registry." |
| `lexicalscope` | `iba/app/lib/lexicalscope.py` | 0 | "Selector-to-verse-id resolution for lexical.run (escalation #1549 rework) — cluster/word/strong-list/verse-list all converge to a verse-id list via `span.strong_variant` (exact-token match), never `strong_verse` (verified undercounting)." |
| `clusterfamilyscan` | `iba/app/lib/clusterfamilyscan.py` | 0 | "candidate-generation via `strong_related` lexical-family data instead of gloss-keyword matching, with proper-noun filtering." |
| `lexical` | `iba/app/lib/lexical.py` | 0 | "the lexical (`verse_lexical`) engine: T1-T3 ... also computes position/surface/language/testament/is_negator/narrative_morph/gloss_consistent_in_verse/party_kind" |
| `lexicalenrichgenerate` | `iba/app/lib/lexicalenrichgenerate.py` | 0 | "The LLM-calling half of lexical.run Layer 2 ... Config-driven from the start (module lexical)" |
| `scripts_apply_finding_verse_term_index_v1_20260829` *(inactive, one-off)* | `scripts/_apply_finding_verse_term_index_v1_20260829.py` | 1 | "backfills `finding.strong_number` via `mti_terms.strongs_number` -> `iba.strong.strongNumber`" — the one live cross-database bridge from `bible_research.db` into this layer. Run and verified 2026-08-29; one-off, not reusable. |

---

## 13. Findings surfaced by this inventory pass

1. **No routing/completeness rule exists anywhere in `cfg_*`.** Confirmed independently across
   `cfg_method_rule` (§8), `cfg_setting` (§11), `cfg_on_fail` (§9), and `cfg_behaviour_rule` (a
   full free-text scan of its 66 rows returned zero hits on any of the 8 table names). This is a
   direct, first-hand confirmation of #1613's central claim, not an assumption carried over from
   it.
2. **`strong_meaning_tree.strong_variant` and `strong_meaning_parsed.strong_variant` have no `use`
   text and no `type`** in `cfg_column`, despite carrying the FK actually joined on. Both are also
   the join key their own `cfg_index` rows are built on (§4) — the column governance for this
   layer's real join path is thinner than the rest of the layer's column documentation.
3. **`lexicon.validate`'s `cfg_step.does` says "4 tables"; its `cfg_report_csv_table` wiring lists
   6.** Discrepancy noted (§10), not resolved — needs either a `does`-text correction or an
   explanation of which 4 are meant.
4. **Three `cfg_utility.purpose` fields are truncated mid-sentence in the live data**
   (`lexiconparse`, `registryreport`, `strongreport` — §12, confirmed by raw string length, not a
   display artefact). If this document is meant to reflect config "in detail," those three rows
   are themselves incomplete at the source and would need the researcher's or Claude's own
   completion, not just re-quoting.
5. **`resolved_sense` (`verse_lexical`, the layer's actual downstream consumer) has no `fk` and no
   named source table in `cfg_column`** — its `use` text ("stem/voice-selected sense text ...") does
   not state that only `strong_meaning_parsed` is consulted, never `strong_lsj_parsed`/
   `strong_mounce_parsed`. This is the exact gap #1613 traces to the 45-strong divergence; the
   config-level evidence for it is that `resolved_sense`'s `cfg_column` row is silent on source,
   not that it states a rule which turns out to be incomplete.
6. **One near-miss excluded from this inventory as out of scope:** `cfg_behaviour_rule` #66
   (`cluster-label-must-track-membership`) matched the free-text scan on the word "strong" but is
   about `cluster`/`cluster_strong` label maintenance, not the meaning layer — noted here only for
   transparency of method, not included in §8.

---

## 14. Completeness and cross-table integrity — what would actually have to be checked

None of the checks catalogued above, taken together, currently let anyone assert that this 8-table
layer is complete and internally consistent — they answer three narrower questions that get
conflated with "is it complete." First, **single-table row-presence coverage** — does every `strong`
have a `strong_sense` row, does every `strong_lexicon` row have an lsj/mounce parse — is what
`report.strong_meaning` and `lexicon.validate`'s coverage section actually check, and they do it
well; the live `run` history (§7) shows this has genuinely been run and tracked over time (e.g. run
`RUN-20260811_172851_742-LEXICON-PARSE`: "2 strong_lexicon row(s) with no lsj parse, 2 with no
mounce parse, 2 strong row(s) with no related fetch, 0 value-quality violation(s) — researcher
confirmed known/acceptable"). Second, **cross-table coverage divergence** — whether
`strong_meaning_parsed`, `strong_lsj_parsed`, and `strong_mounce_parsed` agree on which Greek codes
they cover — is exactly the question #1613 raised and no check anywhere runs it; it requires
comparing three `DISTINCT strong` sets against each other, not against a fixed target. Third,
**referential/FK-level integrity** — whether a `strong_variant`/`lemma_key`/`related_strong` value
actually resolves to a live row on the table it's declared to FK against — has no standing check at
all; `cfg_column.fk` is a documentation field, not an enforced SQLite constraint on these tables. An
ad-hoc version of that third check was run for this document (not registered as a `cfg_step`, not
repeatable via any PS script): of `strong_meaning_tree`'s 40,315 live rows, 2,182 (347 distinct
`strong_variant` codes, e.g. `G0039`, `G0165`) point to a code with no live `strong` row at all —
which, reassuringly, lands exactly on the "347 base-lemma-only rows with no individual `strong` row
of their own" #1613's own context already named, not a new defect; `strong_related.related_strong`
separately shows 14,954 such non-resolving rows, which is *by design* per `strong_related`'s own
`cfg_table.use` text (§2) rather than an integrity gap. Fourth, and least visible: **pipeline
staleness**. Because `lexicon-parse` runs standalone rather than chained after `new-word`/
`raw-backfill` (§7), a `strong`/`strong_meaning_tree` row can exist for a while with no
corresponding `strong_meaning_parsed` row purely because nobody has re-run `lexicon.parse` since —
not because of any genuine source-data gap. The `run` table records that each invocation happened
and what it found, but nothing compares `strong.created_at`/`strong_meaning_tree` row counts against
the timestamp of the last `lexicon-parse` run to say whether the layer is currently *current*; nor
does the live `strong_meaning_tree` (13,206 distinct `lemma_key`) vs. `strong_meaning_parsed`
(13,204) count — a 2-lemma gap, checked live for this paragraph — distinguish a staleness lag from a
real parse failure. **In short: to actually establish completeness and cross-table integrity for
this layer, three things would need to be built and registered as standing, repeatable
`cfg_step`/`cfg_quality_check` rows (not answered ad hoc, as they were for this paragraph) —**
a cross-parse-table coverage-divergence check, an FK-orphan check scoped to catch genuine anomalies
without re-flagging the known 347/14,954 by-design cases, and a staleness check comparing raw-table
freshness against the parse pipeline's last run — none of which exist today.

---

## 15. ~~Recommendation — which table is master truth for meaning~~ CORRECTED

**Struck through, not deleted — this was wrong.** The researcher's correction: **`strong` is the
master truth table**, not `strong_meaning_parsed`. Reasoning (theirs, not a rediscovery of mine):
`strong` is the only table in this layer that chains to `span`, and `span` chains to `verse` —
`verse` is the actual foundation of the whole study (verse primacy, `governance.prose_canonical_authority`).
Every table below §2-§12 is derived from `strong` in some way (by FK, or by the fetch that
populated it), but none of them independently anchor to the verse text — they answer "what does
this code mean," not "is this code actually grounded in Scripture." Meaning-content richness
(§15 v1's whole argument) is a real property of `strong_meaning_parsed`, but it's a property of a
*satellite*, not a claim to being the anchor. §17 is the completeness/quality audit this correction
required, run live against `strong` and everything that depends on it.

**A second reason §15 v1 needs retracting, not just re-ranking:** point 3 below claimed
`resolved_sense` is "already built from `strong_meaning_parsed` alone" as evidence for
`strong_meaning_parsed`'s primacy. §17 found that claim is now **false** — as of escalation #1575
(2026-09-08, researcher-directed), `resolved_sense` is written for **zero** live rows (confirmed:
0 of 544,013 `status='resolved'` rows carry a non-NULL `resolved_sense`; see §17). The `cfg_column.use`
text quoted below was accurate when #1613's own context was written days earlier, then the code
changed under it without the config text being updated — exactly the kind of drift §17 was built to
catch, and a second reason this recommendation could not have stood even on its original terms.

**Original v1 text, left for the record:**

**`strong_meaning_parsed` (backed by `strong_meaning_tree`) is the master truth table for meaning.**
Three reasons, in order of weight:

1. **It's the only source that covers both languages.** `strong_lexicon`→lsj/mounce is Greek-only by
   definition (`strong_lexicon`'s own grain: "one row per strong that has LSJ/Mounce (Greek)", §2).
   A table that structurally cannot speak to Hebrew cannot be "master" for a bilingual layer — at
   best it can be master *for the Greek subset*. `strong_meaning_tree`/`strong_meaning_parsed`
   covers both: 9,173 Hebrew + 5,592 Greek strongs, plus 347 base-lemma-only rows (#1613 context).

2. **`strong_sense` and `strong_meaning_tree` are not competing sources — they're the same source at
   two granularities.** Per §3's `cfg_column.source` values: `strong_sense.head` is
   `derived:call2.mediumDef.head`; `strong_meaning_tree.sense_text` is `derived:call2.mediumDef.tree`.
   Same STEP field (`mediumDef`), same single `call2_getInfo` call (§5's `cfg_write_grant` shows one
   writer — `call2_getInfo` — populating `strong`, `strong_sense`, `strong_meaning_tree`, *and*
   `strong_lexicon` together). So the real fork isn't `strong_sense` vs. `strong_meaning_tree` vs.
   `strong_lexicon` as three independent claims about meaning — it's `mediumDef` (STEP's own
   dictionary-style definition, feeding `strong_sense` + `strong_meaning_tree`/`_parsed`) vs.
   `lsjDefs`/`shortDefMounce` (two separate third-party reference lexicons STEP also happens to
   carry, feeding `strong_lexicon`→lsj/mounce). `mediumDef` is STEP's own primary definition field;
   lsj/mounce are supplementary scholarly lexicons layered on top. That framing, not table-counting,
   is why `strong_meaning_parsed` reads as primary and lsj/mounce as secondary, rather than three
   co-equal sources.

3. **It's already the live, settled design for the actual consumer-facing meaning field.**
   `verse_lexical.resolved_sense` — the field every downstream reader (`report.verse_lexical`,
   T4-T9) treats as "the meaning of this code in this verse" — is already built from
   `strong_meaning_parsed` alone (§7, `lexical.build`; #1605 §9.1/9.3). Naming it master formalises
   a choice the pipeline has already made, rather than introducing a new one.

**What this does not resolve on its own:** the 45-strong gap (real lsj/mounce data, no
`strong_meaning_parsed` row) still needs handling, and naming `strong_meaning_parsed` master doesn't
make lsj/mounce irrelevant — it argues for a **layered/fallback model** (master first, lsj/mounce
consulted only when master is silent) over a **dual-master model** (either table wins depending on
which has data), because a fallback keeps exactly one authoritative answer per code and makes the
45-strong cases visibly the exception they are, rather than quietly doubling the number of "correct"
answers a code can have. Whether that fallback is worth building, and what happens to `strong_sense`
and the raw layer's own review, are separate open items #16 still leaves open.

---

## 17. Comprehensive completeness & quality audit — `strong` and every table below it

Per the researcher's correction (§15): `strong` is the anchor, everything else in this document is
a satellite of it. This section audits `strong` against its own real foundation (`span`/`verse`),
then every table that FK's to `strong` anywhere in `iba.db` (found by a live `cfg_column.fk LIKE
'strong.%'` sweep — 12 data tables, one more than the 8 the original §1 scope covered: `word_strong`,
`strong_verse`, `cluster_strong`, `candidate_seed` were outside §1's meaning-layer framing but are
squarely "below `strong`"). Every number below was queried live against `iba.db` for this section,
read-only, 2026-09-09.

### 17.1 `strong` itself — completeness against its real foundation

`strong`'s own claim to being "in scope of the project" rests on matching real verse text via
`span`, not on carrying rich meaning content. Checked directly:

- **378,149** live `span` rows carry a non-blank `strong_variant`, naming **15,452** distinct
  Strong's codes across the live text (a `span` row can name more than one code when STEP combines
  them on one HTML tag).
- **15,293** live `strong` rows exist.
- **409** of the 15,452 codes actually appearing in live verse text have **no live `strong` row at
  all** — 555 individual `span` occurrences, spread across **38 of the 66 books** (heaviest: 1Chr
  198, Matt 71, Num 50, Acts 31, Gen 28, Luke 24 — not confined to unworked genealogy-heavy books,
  so this does not read as simple "not yet backfilled" backlog; it is scattered through
  heavily-worked NT and OT narrative books alike). `raw.detail`'s own `cfg_on_fail` row ("a strong
  returned no vocab from STEP — missing lexical data, worth a decision, not a silent continue", §9)
  suggests at least some of this is STEP genuinely returning nothing for a code that was actually
  attempted, rather than the code never having been tried — but that distinction cannot be settled
  from config/data alone; it needs a code-level check of whether these 409 codes have ever been
  passed to `raw.detail_one()` and failed, versus never attempted.
- **250** live `strong` rows are never referenced by any live `span` at all — 248 of them
  `origin='word'` (deliberately onboarded because a registry word's STEP search returned the code),
  2 `origin='backfill'`. A `strong` row with `origin='word'` implies a real registry word claimed
  it, yet no verse in the live corpus contains it — worth a decision on whether that's an expected
  by-product of the verse-gap-by-design ruling (`governance.verse_gap_by_design`, a missing verse
  could hide the only occurrence) or a genuine anomaly.

**Verdict: `strong`'s coverage of its own foundation is close but not complete — 409/15,452 (2.6%)
of codes actually in the text have no identity row.** This is the number that actually answers "is
the master table itself complete," and no existing `cfg_step`/`cfg_quality_check` computes it
today — it was built ad hoc for this audit.

### 17.2 The 12 satellite tables — what each does and how complete it is

| Table | What it does (§2-§12 detail, condensed) | Completeness finding (live, this audit) |
|---|---|---|
| `word_strong` | L1 discovery record: which strongs a word's STEP search returned (`raw.discover`) | 4,874 rows, 3,494 distinct codes. **29 orphans** (reference a `strong` code that does not exist at all — not even soft-deleted). More significant: **1,311 of 4,776 `origin='word'` `strong` rows (27%) have NO `word_strong` row at all** — the discovery provenance for over a quarter of "deliberately onboarded for a word" codes is missing. Plausible mechanism, not confirmed from config alone: `strong.origin`'s own `cfg_column.use` (§3) documents a `backfill`→`word` promotion path ("a later word legitimately claims the code... sticky... never downgraded") that may update `origin` without inserting a `word_strong` row — needs a code check to confirm, not asserted here as settled. |
| `strong_verse` | Verse-linkage index (`strong`, `verse`), "the source's assertion this strong is in this verse" (`raw.verses`/CALL 3) | 132,718 rows, but only **4,509 of 15,293 live strong codes (29.5%) have any row at all** — **10,784 codes have zero.** Cleanly explained for **10,517** of those: every single `origin='backfill'` `strong` row (10,517 of them) has zero `strong_verse` coverage, because `raw.backfill_meaning` explicitly does not run `raw.verses` ("pull ONLY the meaning... not verses", §7) — by design, not a defect. The remaining **267 are `origin='word'` rows missing `strong_verse` despite having gone through the `new-word` chain**, which does run `raw.verses` (§7, ordinal 4) — this subset is the real anomaly, not the 10,517. This is also the table `lexicalscope.py`'s own `cfg_utility.purpose` already calls out as "verified undercounting" (§12) — this audit is the first live quantification of how large that undercount actually is. |
| `strong_sense` | One-line sense HEAD per strong, "read constantly" | **Fully complete**: all 15,293 live `strong` rows have exactly one live `strong_sense` row, no duplicates, zero blank/null `head` values. Clean. |
| `strong_meaning_tree` → `strong_meaning_parsed` | Raw STEP sense tree → parsed gloss segments | Base-lemma coverage clean (§13 finding #2's 347-code gap reconfirmed live, unchanged). New this audit: **12,237 of 40,315 live `strong_meaning_tree.sense_text` rows (30%) fail the table's own declared `raw.meaning_tree_clean_pattern` expectation** — they carry `<b>`, `<i>` or other non-`<ref>` markup the pattern says should not survive (sample: `<b>to do good, confer benefits,</b> <ref='Act.14.17'>Acts 14:17;</ref>...`). No `cfg_quality_check` row currently tests this expectation — it is declared in `cfg_column.expectation` (§3) and never enforced. Whether this is tolerated-by-design (raw table, cleaned downstream in `strong_meaning_parsed`, which passed its own `notblank` check with 0 violations) or an unmet invariant is a judgement call, not resolved here — but the number is real and large. |
| `strong_lexicon` → `strong_lsj_parsed`/`strong_mounce_parsed` | Raw + parsed LSJ/Mounce lexicons, Greek-only | **Fully complete at the raw level**: exactly the 5,639 live Greek `strong` rows have a `strong_lexicon` row, no orphans either direction. Parse-level gap unchanged from the last `lexicon-parse` run (§7's `run` history): 2 lsj-text rows and 2 mounce-text rows still have no parsed output — stable, not drifting. The cross-parse-table divergence #1613 raised (lsj/mounce vs. `strong_meaning_parsed`) was re-run live at the correct grain (base lemma, not full sub-lettered code) and **confirms exactly 45 sub-lettered Greek variants** (e.g. `G0039G`, `G0039H`) with real lsj/mounce data but no `strong_meaning_tree` row of their own — matching #1613's original figure precisely, and now precisely characterised: **the gap is at the sub-entry-letter grain, not the base-lemma grain** — every one of those 45 codes' base lemma does have a `strong_meaning_parsed` entry (0 base-level gap, confirmed live). |
| `strong_related` | STEP-fetched related-term links, not derived from any raw table | **Essentially fully attempted**: 15,291 of 15,293 live strong codes have at least one live `strong_related` row (or a documented zero-relation outcome is indistinguishable from "row exists with 0 related" — see §13 finding, the table's grain gives no way to tell "fetched, found none" from "never fetched"). Only 2 live codes have zero rows, and separately 2 `strong_related` source codes (`H3673`, `H3674`) reference a `strong` that no longer exists live — small, isolated, not a systemic gap. |
| `cluster_strong` | Strong↔cluster taxonomy assignment | 17,300 rows. **411 orphans** — reference a `strong` code that does not exist at all (not soft-deleted; genuinely absent). Coverage the other direction is clean: every `origin='word'` `strong` row has a `cluster_strong` row (0 gap), consistent with `strong.reconcile` running last in the `new-word` chain (§7). |
| `candidate_seed` | Candidate-tagging pipeline for verse analysis | 2,087 rows, **217 orphans** (10.4% — a `strong_variant` value with no live `strong` row). Lower priority: its owning work packages (`set-candidates`, `candidate-quality`) are both `inactive=1` (§7) — this looks like a parked pipeline, not a live one, and the orphan rate should be read in that light. |
| `verse_lexical` | Layer 1 (T1-T3) derived engine output — role, resolved sense, per span-code | Row-presence coverage against `span` is nearly complete: of 544,649 individual strong-code tokens across live spans, only **55 live `span` rows have zero corresponding live `verse_lexical` rows.** Status split: 544,013 `resolved`, 559 `unregistered` (matches `strong`'s own 409-code gap roughly in shape). **The material finding is not row-presence, it's `resolved_sense` itself: 0 of 544,013 `status='resolved'` rows carry a non-NULL `resolved_sense` — every single one is NULL.** Confirmed via direct row sampling, not just aggregate count (§17 method). This is not a newly discovered defect — it is escalation **#1575** (2026-09-08, researcher instruction "remove it from the column for all the lexicals"), applied live: `resolve_code()` no longer writes `resolved_sense` at all. What **is** a live finding: `verse_lexical.resolved_sense`'s own `cfg_column.use` text (§3, quoted in the now-struck §15) and `lexical.build`'s own `cfg_step.does` text (§7, "stem/voice-selects the operative sense from `strong_meaning_parsed`") were **not updated** when #1575 was applied — both still describe the pre-#1575 behaviour. This is a live, present-tense config/code drift, not a historical note. |

### 17.3 Summary verdict

Three tables are clean by this audit: `strong_sense` (100%, zero defects), `strong_lexicon` (100%
raw coverage), and `strong_related` (99.99% attempted). Everything else below `strong` carries a
real, now-quantified gap: `strong`'s own match to `span`/`verse` is 97.4% not 100%; `word_strong`
is missing for 27% of word-origin codes; `strong_verse` structurally covers under a third of live
codes (mostly by design, but with a 267-code anomaly inside the by-design majority);
`strong_meaning_tree` carries a 30% rate of undeclared-but-checked markup violations; `word_strong`/
`cluster_strong`/`candidate_seed` each carry a nonzero pure-orphan rate (references to `strong`
codes that were never soft-deleted, just never existed); and `verse_lexical.resolved_sense` — the
one field every downstream consumer actually reads as "the meaning" — is current-state empty for
100% of resolved rows, with the config that describes it not yet caught up to that fact. None of
this was visible from `cfg_*` text alone (§1-§14's method); it took running the checks against live
data, which is itself the headline finding: **the "how would you know" question from §14 was not
rhetorical — running the checks surfaces materially different answers than reading the config does.**

---

## 18a. Outcome — the spine ruling captured live (2026-09-10)

§15/§17 asked "which table is master truth" and "how would you know completeness." The researcher
answered directly, in chat: `strong` is master (the anchor to `span`/`verse`, not the richest
content), verse→span→strong must sync (desync fatal), extended meaning has an accepted anomaly
(T2/T3-T15/backfill) but a strong→meaning→parse break is always fatal, and the pull-through
mechanism is trigger-on-discovery, not a proactive sweep — adjusted once more (escalations
#1622-1624) to make the trigger explicit before applying. **Captured live 2026-09-10:**
`governance.base_data_spine` + 4 `cfg_method_rule` rows (escalations #1620-1624), plus
`candidate_seed`'s retirement completed for real (escalations #1614-1618 — two live dependents this
audit found, now both inactive). Full record: `iba/app/GOVERNANCE.md` §73; memory
`project_base_data_spine_verse_span_strong_parse`. The 409-code desync itself is **not** fixed by
this pass — the rule now exists and says it's fatal; the actual remediation is separate, still open
below.

## 18. What this document does not do

Per #1613's own stated scope, this is inventory (§1-§14) plus one corrected recommendation (§15)
plus one live completeness/quality audit (§17) plus the spine ruling now captured in config (§18a)
— the ruling is captured; most of what it governs is not yet fixed. Still open, pending the
researcher: whether the 409-code `strong`/`span` gap and the 267-code `strong_verse` anomaly need a
remediation pass or are acceptable as-is; whether the 1,311-code `word_strong` gap's cause (the
hypothesised `backfill`→`word` promotion path) should be confirmed by a code read and, if confirmed,
whether that's acceptable or needs `word_strong` backfilled retroactively; whether the 411/217/29
pure-orphan rows across `cluster_strong`/`candidate_seed`/`word_strong` should be cleaned up or left;
whether the 12,237-row `strong_meaning_tree` markup-pattern violation is tolerated-by-design or a
real defect worth a `cfg_quality_check`; whether `verse_lexical.resolved_sense`'s `cfg_column.use`
and `lexical.build`'s `cfg_step.does` should be corrected now to match #1575's live behaviour (this
one reads as a straightforward config-text fix, not a new design decision, but is left for the
researcher to confirm rather than self-applied); and everything §16 (now folded into this list)
already listed about the meaning-parse layer specifically.
