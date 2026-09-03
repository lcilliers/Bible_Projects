# Vocabulary/glossary — seed list

> Escalation #1377. v2 supersedes
> [`1377-vocabulary-glossary-seed-v1-20260901.md`](archive/1377-vocabulary-glossary-seed-v1-20260901.md)
> (archived) — v1 seeded from #1007/#1376's own documents only; v2 adds two more passes per
> researcher instruction (2026-09-01): a full read of the current programme prose
> (`Workflow/Programme/programme_prose/wa-programme-prose-extract-20260827.md`) and a scan of
> every column name in both live databases via `cfg_column` (1,799 rows: 1,224 `bible_research` +
> 575 `iba`). This is still a candidate list, not definitions — the `cfg_enum`-vs-separate
> question from v1 is still open and unresolved here.

## Part 1 — terms already given a working definition (from v1, unchanged)

Carried forward from #1376's own "Terminology (growing list)" section in
[`1376-characteristic-tables-cross-db-inventory-v2-20260901.md`](1376-characteristic-tables-cross-db-inventory-v2-20260901.md):

| Term | As used in that study |
|---|---|
| **inner-being characteristic** | The programme's own filter-concept — what qualifies a word for the registry at all. |
| **HIB** | Human Inner Being — a named or implicit *human* narrative subject (`iba.db hib`). A non-human being can never be registered as a HIB. |
| **phenomenon** | IBA's live term for a characteristic *in operation* — one HIB's state/disposition, evidenced in one verse (`iba.db phenomenon`). A per-occurrence reading, not a catalog entry. |
| **operation** | The movement/behaviour registered against one phenomenon (`iba.db operation`). |
| **cluster** | A top-level thematic grouping, keyed on an M-code (or T2/T3/FLAG) — but see Part 3 below, the column-name scan found this word is not as settled as it looks. |
| **cluster_code** | The stable string key for a cluster (e.g. `M04`, `T3`, `FLAG`). |
| **characteristic** (Model A sense) | A named, hand-defined trait belonging to a cluster — an abstract catalog entry, not tied to a verse (`bible_research.db characteristic`). |
| **family** (Model B sense) | `ib_characteristic`'s own grouping concept, derived by book, not by cluster. |
| **cluster_subgroup / characteristic_subgroup** | An abandoned sub-division attempt — built on lemma, not span. |
| **T2 (Supplementary)** | Strong's codes assigned to a cluster process but carrying no inner-being relation. |
| **T3 (Operations)** | Strong's codes for a human operation/movement not tied to one cluster, or applying across many. |
| **FLAG** | Flagged for review — deliberately rare. |
| **HIGH / MEDIUM / LOW** | Confidence tiers from the Model A cluster-allocation process. |
| **descriptor** | A T2 item reading as inner-being content but rarely analysed alone. |

## Part 2 — candidate terms from #1007 with no settled definition (from v1, unchanged)

| Term | Where it came up | Why it needs a definition |
|---|---|---|
| **scope** (`wa_obs_question_catalogue.scope`) | #1007, #1374/#1375 | Just repurposed from an old universal/Leviticus-marker meaning to the Scope-focus bucket meaning. See Part 3 below — the column-name scan found the word "scope" has *four* unrelated meanings project-wide, not two. |
| **Scope focus** (the 8 buckets) | `1007-tier-catalogue-scope-focus-v3-20260831.md` | Word/term (lexical), Characteristic (HIB behaviour), Characteristic relational, Characteristic (what it is) [proposed, unconfirmed], The HIB, Verse-context, Other non-human beings, The verse, Science. |
| **source** (`wa_obs_question_catalogue.source`) | `1007-word-term-lexical-source-v1-20260831.md` | New column, distinct from `scope`. |
| **tier / T-code** | Whole catalogue (T0–T7) | Used throughout without one canonical statement of what a "tier" *is* as opposed to a cluster, a component, or a bucket. |
| **span** | `span` table, `verse_lexical.span_id` | One verse-position's row — distinct from "term" and from "surface." |
| **surface** | `span.surface` | The literal word/phrase text at a span — distinct from the Strong's-coded term it resolves to. |
| **term** | Used everywhere, loosely | Sometimes a Strong's-coded lexical entry, sometimes `word_registry.word`, sometimes used for "word" or "span." |
| **word** (as distinct from span/term) | Throughout | Same ambiguity as "term." |
| **content / function** (`verse_lexical.role`) | Live schema | A linguistic classification — easy to mistake for an inner-being-relatedness judgment, which it is NOT. |
| **resolved / unregistered / content_resolved** (`verse_lexical.status`) | Live schema | Whether a span is lexically matched/onboarded — again not an IB-relevance judgment. |
| **inner-being-related (IB-related)** | This session's discussion | No field anywhere represents it — confirmed gap. |
| **Layer A / Layer B** | `1007-tier-catalogue-iba-raw-data-mapping-v2-20260831.md` Part 2 | Layer A = base lexical layer; Layer B = debate/phenomenology layer. |
| **Phase 1 / Phase 2** | This session's chat only | Phase 1 = surface/word-level; Phase 2 = characteristic-rollup, verse-context. Coined live, not written up durably yet. |
| **verse-context** | Ambiguous across two databases | (a) a Scope-focus bucket label vs (b) `bible_research.db`'s actual `verse_context`/`verse_context_group` tables. |
| **model** (Model A/B/C/D) | `1376-characteristic-tables-cross-db-inventory-v2` | Informal document-local labels, not project-standard names. |

## Part 3 — NEW: found in the programme prose (2026-08-27 extract)

The prose is the canonical account of the whole programme (`governance.prose_canonical_authority`),
so this pass reads differently from #1007's — it's not catalogue-question wording, it's the
programme's own self-description, and it surfaces terminology collisions the catalogue work never
touched.

### 3a. Same word, genuinely different things (the dangerous kind)

| Term | Sense 1 | Sense 2 | Sense 3 (if any) | The risk |
|---|---|---|---|---|
| **cluster** | `cluster` table (M-code, "analytical" per the prose's own Ch.4 framing) | `word_registry.cluster_assignment` — **C-codes** (C01–C22), explicitly called "administrative" by the same chapter, a leftover run-batch tranching field from the retired Dimension Review stage | — | The prose itself states these are architecturally distinct ("dimensions (analytical) and C01-C22 clusters (administrative)") — yet both are called "cluster." Confirmed live in the DB (Part 4 below): one column literally named `cluster` holds a C-code where every other `cluster` column holds an M-code. |
| **characteristic** | Chapter 1's foundational *concept* — the working definition that decides whether an English word is in scope at all (`prog_purp_defining_inner_being`) | Model A's `characteristic` *table* — a hand-defined trait belonging to a cluster, one level below cluster in the M-code hierarchy | Model B's `ib_characteristic` — a "family" grouping derived by book | The prose uses "characteristic" for the programme's entire subject matter (Ch.1) AND for one specific mid-tier table (Ch.4) AND that table has a same-named cousin in a different model with a different grain. Three distinct grains, one word. |
| **dimension** | Chapter 4's section is literally *titled* "Dimensions — the analytical grouping mechanism" | The section's own body then states the *actual* live mechanism is the M-code `cluster`/`characteristic` model, not dimensions — `wa_dimension_index` is a retired mechanism (eliminated per earlier programme history) | — | The prose's own chapter heading has not caught up with its own body text — a residual naming holdover inside the canonical document itself, not just a DB artefact. |
| **inner being** | The programme's whole subject (Ch.1: "the human inner being") | **HIB** = *Human Inner Being*, one specific named/implicit narrative subject within a book (`iba.db hib`, Model C) | "inner-being characteristic" / "inner-being word" — the registry-admission concept | Same root phrase used at three different scales: the whole field of study, one specific analytical entity within the debate pipeline, and the registry's admission filter. |
| **anchor** | `verse_passage.is_anchor`/`passage.anchor_verse_id` — the passage-level anchor verse | `hib.first_verse_id` — the prose explicitly says this "plays an analogous role" for a HIB, but it is **not** named `anchor` in the schema | — | The prose itself flags the parallel without the schema naming it consistently — a real drafting gap, not a misreading. |
| **registry** | `iba.db`'s live `word_registry` (Ch.4: thin, 4 real fields — `word`/`source`/`status`/timestamps, 180 rows, current scope list) | `bible_research.db`'s (older/legacy) `word_registry`-keyed apparatus described in `CLAUDE.md` — `session_b_status`, `verse_context_status`, `cluster_assignment`, 215 registries, phase-status fields | — | Two structurally unrelated things share the table name `word_registry` across the two databases — one a thin scope list, one a heavy legacy phase-tracking table. `CLAUDE.md` itself documents the legacy one; the live prose documents the thin one. Worth confirming whether this is a genuinely reconciled single table or two same-named tables in two databases. |
| **passage** | `iba.db`'s `passage`/`verse_passage` (Ch.4: a maximal run of consecutive verses, chapter-bounded, `anchor_verse_id`) | The still-cited (per `CLAUDE.md`'s live-method banner) `verse.passage_id` from the 2026-07-02 verse-first method, `bible_research.db`-side | — | Same definition in words ("a maximal run of consecutive verses, anchor = first verse") stated independently in two places against two different databases — not yet confirmed whether one migrated from the other or both are live in parallel. |

### 3b. Heavily overloaded generic terms (lower individual risk, but worth naming as a category)

Not necessarily wrong — `cfg_column.use` already documents each instance — but the same word
recurring across many unrelated tables with unrelated meanings is exactly the pattern that makes
prose and conversation ambiguous even when the schema itself is fine.

| Term | Sample of distinct senses found |
|---|---|
| **flag** | quality flags (`wa_quality_flag_types`/`wa_data_quality_flags`), research flags (`wa_session_research_flags`, e.g. `SD_POINTER`), term flags (`mti_term_flags`, e.g. somatic/god_as_subject), registry-construction inference flags (*Inferred*/*Partial*/*Absent*, Ch.2), the `FLAG` cluster code itself, `PROSE_QUALITY` flags, `verse_context`'s "three flags." |
| **status** | `word_registry.status` (onboarding state), `mti_terms.status` (extracted/candidate_delete/etc., legacy), `passage.debate_status`, `verse_lexical.status` (resolved/unregistered/etc.), `escalation.state`, `prose_section` lifecycle status, plus the legacy `session_b_status`/`verse_context_status`. |
| **source** | `word_registry.source` ("why it entered scope"), `wa_obs_question_catalogue.source` (the new catalogue column), `cluster_strong.source` (allocation-pass provenance, e.g. `manual-backfill-triage-20260813`), STEP Bible as "the source" in the general-English sense, `cfg_column.source`/`filled_by`. |
| **scope** | See Part 3c — four distinct column-level meanings found live, plus the general-English "programme scope"/"registry scope" sense (Ch.1) and the AI-operating-discipline "scope integrity"/"help-forward, not scope-extended" sense (Ch.3). At least six senses total. |
| **resolved / resolution** | `verse_lexical.status = 'resolved'` (lexical match found), `escalation.resolution`/`resolution_kind`, `candidate_seed`'s "not yet definite" pre-resolution state, `verse_lexical.ambiguity_note`'s "named-not-resolved ambiguity." |

## Part 4 — NEW: confirmed live in the schema (from the `cfg_column` scan)

Ran a scan of all 1,799 `cfg_column` rows across both databases (1,224 `bible_research`, 575
`iba`) for column names shared across both DBs and for internally inconsistent naming within one
DB. Two concrete, evidenced findings:

**The soft-delete marker has at least four different spellings for the same concept**, confirmed
via `cfg_column.use` text, not inferred:

| Spelling | Where | Notes |
|---|---|---|
| `delete_flagged` | `bible_research.db`, ~38 tables | The dominant convention in that database. |
| `deleted` | `bible_research.db`, **one** table only: `wa_obs_question_catalogue` | The odd one out in its own database — and its own `use` text confirms it disagrees with the table's `status` column on row counts (243 vs 185), a live inconsistency the prose's Ch.4 also names independently. |
| `delete_flag` | `bible_research.db`, **one** table only: `wa_session_b_findings` | A third spelling, singular not plural. |
| `deleted` | `iba.db`, uniformly, all tables | The whole-database convention there — but not one behaviour: most tables are plain soft-delete, while `hib`/`phenomenon`/`operation`/`verse_lexical`/several `passage_*` tables are explicitly "**version-aware** soft-delete" (a superseded row is flipped, not just flagged) — same column name, two different delete semantics. |
| `deprecated` | `bible_research.db`, historical | `wa_quality_flag_types.delete_flagged`'s own `use` text records that this column is "replacing the retired deprecated column (a rename, not a new concept)" — a fourth, now-retired name for the same thing. |

**The column named `cluster` (not `cluster_code`) does not hold one consistent kind of value.**
Four tables carry a bare `cluster` column; three hold an M-code, one holds a C-code:

| Table.column | Holds | Per its own `cfg_column.use` |
|---|---|---|
| `ib_characteristic.cluster` | M-code | "The single primary M-code cluster this characteristic maps to" |
| `verse_span_index.cluster` | M-code | "The M-code cluster (e.g. 'M47', 'M15') the span belongs to" |
| `file_manifest.cluster` | M-code | "M-code cluster extracted from the filename" |
| `wa_dim_review_cluster_log.cluster` | **C-code** | "The C-code completed, unique per row" |

This is a concrete instance of the exact risk this escalation exists to catch: one column name,
used inconsistently, across two genuinely different code systems the programme itself treats as
architecturally distinct elsewhere (`cluster_assignment` = C-codes/administrative vs the `cluster`
table = M-codes/analytical). Anyone querying or reading `wa_dim_review_cluster_log.cluster` by name
alone would reasonably assume an M-code.

**`scope` as a bare column name has four unrelated live meanings**, not the two this thread has
mostly discussed:

| Table.column | Meaning |
|---|---|
| `verse_coverage.scope` | Derived verse-level band: in-scope / T2-only / etc. |
| `wa_file_name_pattern.scope` | File-naming granularity: per-cluster / per-registry / programme / etc. |
| `wa_obs_question_catalogue.scope` | The catalogue's Scope-focus bucket (#1007's work). |
| `cfg_step.scope` | What a run-step needs scoped to it to execute (a word, `'none'`, etc.) — a run-parameter concept, unrelated to the other three. |

## What this pass does not do

It does not resolve the `cfg_enum`-vs-separate-mechanism question from v1 — if anything, the
`cluster`/`scope` findings above make the case stronger that *some* of these are column-value
vocabularies `cfg_enum` could plausibly own, while others (`characteristic`, `dimension`, `HIB`,
`Phase 1/2`) are prose-level concepts no enum row would fit. That split is still yours to decide.
It also does not attempt the `status`/`source`/`flag`/`resolved` overload list exhaustively — Part
3b samples each to show the pattern is real, not a complete inventory of every table that uses
these words.
