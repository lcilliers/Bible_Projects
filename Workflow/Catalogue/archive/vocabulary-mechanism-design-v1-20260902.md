# Vocabulary/glossary mechanism — design proposal (v1)

**Date:** 2026-09-02 · **Escalation:** #1377 (all notes/links/process control for this build live
there, per researcher instruction). **Stage:** DESIGN / PROPOSE — not built. Per `cfg_behaviour_rule`
`decision-points-are-terminal-not-inline`, this is a genuine new decision (schema shape, a new
prose book, a new link table) and stops here for approval before any test-plan/build-plan/build
work starts, per the full cycle the researcher asked for this item to follow.

## 1. Objective (researcher, this chat, 2026-09-02, condensed)

Regulate the terms used in the project, especially where a term carries a special, loaded, or
confusable meaning. Record outdated terms. Handle a definition's lifecycle — reset, extend,
retract. `cfg_enum` plays a part, and various `cfg_*` tables will *use* a vocabulary term and
declare where it applies, but the term's actual *definition* lives elsewhere, cross-referenced
from those config tables. The vocabulary definition itself is judged **not** a config table but a
**data table with lifecycle** — and prose is a strong candidate to hold it, since it is already
authoritative elsewhere and already cross-referenced from configs.

## 2. Where #1377 already got to (recap, not re-derived)

- v3 (researcher, verbatim): *"I will work through this list. From I can see it all belongs in
  enums."* — first framing: everything into `cfg_enum`.
- v4 (researcher, verbatim): *"I see enum in its strict definition. that is fine. it is likely we
  need then a new cfg for it. but not now."* — corrected: `cfg_enum` stays strict (column-value
  vocabularies only); prose-level concept collisions (`characteristic`, `dimension`, `HIB`,
  `Phase 1/2`, `inner being`, etc.) need a separate mechanism.
- v5 (Claude, completeness check): found `cfg_prose_concept` already exists (escalation #714,
  2026-08-18) for exactly the v4 gap, currently 2 rows. Flagged as a live gap that the v4 "likely
  need a new cfg" judgement never checked for. Also flagged: the ~40-term seed list was never
  individually sorted into buckets.

This design proposal is the answer to both v5 gaps: what to do with `cfg_prose_concept`, and how
the sorting/cross-reference actually works mechanically — worked against real cases from
[`vocabulary-glossary-seed-v2-20260901.md`](vocabulary-glossary-seed-v2-20260901.md), not
abstractly.

## 3. What already exists that this should reuse, not duplicate

| Mechanism | Where | Shape | Verdict |
|---|---|---|---|
| `cfg_enum` | iba.db | `name / value / ordinal / inactive` only | Correct for strict column-value vocabularies (unchanged, per v4's own decision). No room for a definition, a loaded-term warning, or a supersedes pointer — confirms v4's own read was right. |
| `cfg_prose_concept` | iba.db | `concept_key / chapter / section_hint / description / source / added_at`, 2 rows | Right *idea*, wrong *shape* for what's now being asked: no `status`, no `aliases` (the 4-way delete-marker spelling problem needs this), no `superseded_by`, and it duplicates definition text inline instead of pointing at the authoritative prose. **Proposed: superseded by `cfg_vocabulary_index` below, not kept alongside it** — same purpose, richer shape, one mechanism not two. |
| `prose_section` (+ `prose_section_type`) | bible_research.db | `heading / body / status / version / approved_by / approved_at / metadata_json`, existing books (`Programme`, `Detail design`, `Findings`, `Essays`), FTS5 search, existing link tables (`prose_section_verse_link`, `prose_section_finding_link`, `prose_section_dimension_link`) | This is the researcher's own instinct confirmed live: prose already has the versioning + approval + search machinery a definition-with-lifecycle needs. No new content-storage mechanism needs building — a new **book** (`book_label`) is the natural extension point, exactly like `Essays` or `Findings` already are. |
| `cfg_column.database` | iba.db | discriminator column (`'iba'`\|`'bible_research'`) already unifying config for both live databases in one place | Confirms `cfg_*` tables are the right home for the cross-reference/index layer even though the definitions themselves live in the other database — this pattern (config in iba.db pointing at content in bible_research.db) is already established, not new. |

## 4. Proposed architecture — two tiers, not one

**Tier 1 — `cfg_enum` (unchanged).** Strict column-value vocabularies stay exactly as they are.
No schema change to this table. Where an enum's *values* need a fuller definition than "the value
is `X`" (e.g. why four delete-marker spellings exist and which is canonical), the enum's row(s)
carry a pointer into Tier 2 (see §6) — the enum table itself is not where that text lives.

**Tier 2 — a new vocabulary index (iba.db) + a new prose book (bible_research.db).**

- **`cfg_vocabulary_index`** (iba.db, new table, supersedes `cfg_prose_concept`) — the
  cross-reference/lifecycle layer. One row per *distinct sense* of a term (see §7 on why sense,
  not word).
- **A new prose book, `book_label = 'Vocabulary'`** (bible_research.db, reuses `prose_section` /
  `prose_section_type`) — the actual definition text, disambiguation, examples, and lifecycle
  narrative. One `prose_section` row per vocabulary entry, linked from the index row above.
- **`cfg_vocabulary_usage`** (iba.db, new link table) — records every place elsewhere in the
  config system that *depends on* a given vocabulary term, so a redefinition/retraction can show
  its full blast radius before it's approved. This is the "conflicts and fallouts" mechanism
  named in the objective — a query, not a manual hunt.

## 5. Proposed schema

### `cfg_vocabulary_index` (iba.db)

| Column | Type | Notes |
|---|---|---|
| `term_key` | TEXT, PK | Stable slug. One per **sense**, not per word — e.g. `cluster.mcode`, `cluster.ccode`, not one row for `cluster` covering both (see §7). |
| `display_term` | TEXT | The human word/phrase as written, e.g. `cluster`. |
| `status` | TEXT | `active` \| `deprecated` \| `retracted` \| `superseded` — itself a `cfg_enum` row (`name='vocab_term_status'`), since this vocabulary is exactly the kind of small, closed, stable set `cfg_enum` was already agreed to own. |
| `superseded_by` | TEXT, NULL | Another `term_key`, when `status='superseded'`. |
| `aliases` | TEXT (JSON array), NULL | Other spellings/old names folded into this sense — e.g. `delete_flagged`'s index row carries `["deleted", "delete_flag", "deprecated"]` for the four-way spelling split Part 4 of the seed found. |
| `prose_section_id` | INTEGER | Points to the `prose_section` row (bible_research.db) holding the actual definition. Cross-database logical pointer, same convention already used for `mti_terms.owning_registry_fk` and similar — not an enforceable SQLite FK, documented as one. |
| `source` | TEXT | Provenance, same convention as `cfg_prose_concept.source` today. |
| `added_at` / `updated_at` | TEXT | Standard. |

### New prose book: `Vocabulary`

- One new `prose_section_type` row (or a small handful, if separating e.g. "term entries" from a
  front-matter "how to read this book" section) with `book_label = 'Vocabulary'`.
- One `prose_section` row per vocabulary entry: `heading` = the term_key's display form (e.g.
  "cluster — M-code sense"), `body` = the full definition/disambiguation/lifecycle narrative.
  Existing `status`/`version`/`approved_by`/`approved_at` columns handle the reset/extend/retract
  lifecycle with **no new versioning mechanism needed** — a redefinition is an ordinary prose edit
  through the existing `prosestore.py` import/export cycle, which already archives a supersede
  patch on import (the audit trail the objective asks for, already built).
- `cfg_prose.book_stage_map` / `cfg_prose.book_output_dir` (both already keyed by `book_label`)
  get a `Vocabulary` entry alongside `Programme`/`Detail design`/`Findings`/`Essays` — a data
  addition to existing config content, not a schema change.

### `cfg_vocabulary_usage` (iba.db, new link table)

| Column | Type | Notes |
|---|---|---|
| `term_key` | TEXT | FK-by-convention to `cfg_vocabulary_index.term_key`. |
| `database` | TEXT | `'iba'` \| `'bible_research'` — which DB the dependent thing lives in. |
| `table_name` | TEXT, NULL | The `cfg_table`/`cfg_enum`/`cfg_column` (etc.) row that depends on this term, when applicable. |
| `column_name` | TEXT, NULL | Narrows to a specific column, when applicable. |
| `enum_name` | TEXT, NULL | Narrows to a specific `cfg_enum.name` group, when the dependency is an enum value rather than a column. |
| `note` | TEXT, NULL | Free text — why this thing depends on this sense of the term. |
| `added_at` | TEXT | |

This is a generic junction, not a bespoke column bolted onto `cfg_enum`/`cfg_column`/`cfg_setting`
individually — one mechanism instead of a schema change cascading across every table that might
someday reference a vocabulary term (`root-fix-not-one-off` / `simple-steps-not-engineered-designs`).

**How the fallout check works in practice:** before approving a `status` change on
`cfg_vocabulary_index` (deprecating/retracting/superseding a sense), run
`SELECT * FROM cfg_vocabulary_usage WHERE term_key = ?` — every row is a place that will need a
look before the change is safe. No separate detection mechanism to build; it's a query against
data that's already being kept current as vocabulary terms get adopted elsewhere.

## 6. How Tier 1 and Tier 2 connect

`cfg_enum` itself gains **no new column** in this proposal — adding one would be a schema change
to a table already agreed stable in its strict shape (v4). Instead, the connection is via
`cfg_vocabulary_usage` pointing *at* the enum: e.g. a term_key `delete_marker` (status: active,
aliases: `["deleted","delete_flag","deprecated"]`) gets a `cfg_vocabulary_usage` row with
`database='bible_research', enum_name=NULL, table_name='wa_quality_flag_types', column_name='delete_flagged'`
(and similarly one row per table carrying a variant spelling) — recording "this column's naming
choice is governed by this vocabulary decision," discoverable by term without touching `cfg_enum`
at all. If a *future* case genuinely needs an enum row to carry a vocabulary pointer directly
(rather than being found via the usage table), that is its own small schema change, to be raised
against `cfg_enum` specifically when a real case demands it — not spent here speculatively.

## 7. Why one index row per SENSE, not per WORD

The seed list's Part 3a is the direct evidence for this: `cluster` (M-code vs C-code),
`characteristic` (three distinct grains), `dimension` (heading vs body disagreeing in the prose
itself), `inner being` (three scales) are exactly the "same word, genuinely different things" case
the whole mechanism exists to catch. A single index row keyed on the bare word `cluster` cannot
represent "this word means two incompatible things depending on context" — it would just be
another ambiguous artifact of the same kind the mechanism is meant to fix. Keying on `term_key`
as a disambiguated slug (`cluster.mcode`, `cluster.ccode`) and keeping `display_term='cluster'`
as a separate, non-unique column lets a lookup by the bare word surface *all* its senses at once
(exactly the disambiguation the objective asks for), while each sense gets its own lifecycle,
aliases, and usage list independently.

## 8. Worked examples against the hardest real cases

| Case (from the seed) | `term_key`(s) | `aliases` | Notes |
|---|---|---|---|
| 4-way delete-marker spelling | `delete_marker` (one sense — the concept is the same, only spelling differs) | `["deleted","delete_flag","deprecated"]` (canonical: `delete_flagged`) | Single sense, spelling variance is exactly what `aliases` is for. `wa_obs_question_catalogue.deleted` disagreeing with its own `status` column is a **usage-table** finding (two `cfg_vocabulary_usage` rows on the same table with conflicting implications), not a new vocabulary concept. |
| `cluster` column (M-code vs C-code) | `cluster.mcode`, `cluster.ccode` | none | Two senses, per §7. `wa_dim_review_cluster_log.cluster` gets a `cfg_vocabulary_usage` row against `cluster.ccode` — the one place the bare column name disagrees with its own table's usual sense — surfacing the exact risk the seed named. |
| `characteristic` (3 grains) | `characteristic.programme_concept` (Ch.1), `characteristic.model_a_table`, `characteristic.ib_family` (Model B) | none | Three senses, three prose entries, one shared `display_term`. |
| `scope` (4+ column meanings) | `scope.verse_coverage_band`, `scope.file_naming_granularity`, `scope.catalogue_bucket`, `scope.run_step_param` | none | Four senses — this is the clearest case for why per-sense keys are necessary; a single `scope` entry would just restate the ambiguity. |

## 9. What this design deliberately leaves open (for you to decide, not assumed)

1. **Book name** — `Vocabulary` vs `Glossary` vs something else. Used `Vocabulary` above only
   because that's #1377's own short_description; not a considered choice.
2. **Migration of `cfg_prose_concept`'s 2 existing rows** (`verse_primacy`,
   `inner_being_definition`) into the new mechanism — straightforward (2 rows), but is a real data
   move, not implied automatically by approving the schema.
3. **Whether the seed list's ~40 candidate terms get sorted into this mechanism as part of this
   build's own test/build-plan work**, or that sorting is separate follow-on work once the
   mechanism exists. Recommend: sort a *small representative subset* (the §8 worked examples plus
   2–3 more) as the build's own test cases, leave the full ~40-term sort as explicit follow-on
   work tracked under #1377, not silently folded into "done."
4. **Whether `cfg_vocabulary_index.status`'s enum (`active/deprecated/retracted/superseded`)
   is the right vocabulary** — proposed by analogy to `escalation.state`-style lifecycles
   elsewhere in the project, not independently derived.

## 10. Next steps (pending your approval of this design)

Per the cycle you asked for: this document is the **design/propose** stage. On approval, next is
a **test plan** (per `cfg_behaviour_rule` `test-plan-per-module-utility`) covering: creating a
fresh term, aliasing an old spelling into an existing term, extending a definition (new prose
version), retracting a term with existing `cfg_vocabulary_usage` rows (does it block, warn, or
just surface the list?), and looking up all senses of an ambiguous bare word — then a **build
plan**, then the build cycle itself. None of that starts until this document is approved or
corrected.
