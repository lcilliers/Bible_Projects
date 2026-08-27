# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file becomes permanent provenance once imported (its archived path is -->
<!-- recorded as record_change_log.change_source, escalation #836) -- do not delete -->
<!-- by hand; the import step archives it automatically on success. -->
<!-- PROSE_EXPORT_SECTION_IDS: 22,23,24,25,26,27,28,70,30,31,66 -->

<!-- PROSE_SECTION_ID: 22 -->
<!-- PROSE_SECTION_TYPE: prog_data_database -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The database as the programme's working memory -->
<!-- PROSE_SORT_ORDER: 22 -->
<!-- PROSE_VERSION: 110 -->

## The database as the programme's working memory

The programme now runs on two SQLite databases, not one. `iba/app/db/iba.db` is the home for all project process control and base data — every table from STEP extraction through Strong's, verses, meaning, and lexical detail, and the `cfg_*` configuration store that governs how every script and module behaves. `database/bible_research.db` is the home for prose and findings — the analytical output built on top of the base data, and the DB-canonical prose store the programme's written account is authored into. This split was made explicit on 2026-08-15, correcting an earlier arrangement where `bible_research.db` alone carried both the base-data layer and the analytical layer; the base layer has since moved to `iba.db`, and `bible_research.db`'s own copies of the tables it superseded are retained but marked inactive (see the sub-sections below for which ones, and by how much).

`iba.db` is governed by its own `cfg_*` system — twenty tables, on the order of a thousand rows, that hold every rule the app's code obeys: which API may write which table, what a step's failure path is, what a controlled vocabulary's allowed values are, what a report's structure is. The principle is that the code decides nothing; every choice the code used to make in a literal is now a row a live check can read. This governing layer is itself part of the data architecture — not a separate concern bolted on afterward — because it is what makes the base-data layer's behaviour traceable and changeable without a code edit. Chapter 5 describes the governance mechanism itself in full; this chapter describes what the two databases hold.

Neither database is the primary source for the Hebrew, Greek, and Aramaic material the programme works with. STEP Bible, a peer-maintained scholarly resource, remains the source every Strong's number, gloss, meaning parse, and verse reference traces back to. `iba.db`'s base-data layer is the programme's verified, structured copy of what STEP returns — not a replacement for STEP, a working record built from it.

The two databases are not symmetric in what they hold going forward. `iba.db` is primary for all base-data and process-control work; a handful of the analytical tables it currently carries — the book-by-book passage/phenomenon/debate pipeline described later in this chapter — are expected to migrate back into `research_db` once the analysis phase is properly under way (escalation #737, on hold). `bible_research.db` is primary for prose and findings, including the cluster/characteristic analytical model that is the current live successor to the retired per-word dimension-review layer.

The sub-sections that follow work through what is in each database, table by table: the registry (both copies, one live and one retained), the term/lexical substrate, the verse and passage layer, the anchor-verse mechanism as it exists today, the cluster/characteristic analytical grouping, the question catalogue and the finding store, the synthesis bridge, and the prose store. Each sub-section names plainly which of its tables are the live source of truth and which are retained history — the distinction the researcher has been most insistent on maintaining as the architecture has moved.

---

<!-- PROSE_SECTION_ID: 23 -->
<!-- PROSE_SECTION_TYPE: prog_data_registry -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The registry -->
<!-- PROSE_SORT_ORDER: 23 -->
<!-- PROSE_VERSION: 111 -->

## The registry

`word_registry` exists in both databases, and the two copies now play different roles. `iba.db`'s `word_registry` (180 rows) is the live registry — the scope of a new-word run, carrying `word`, `source`, `status`, and the timestamps a run needs. `bible_research.db`'s `word_registry` (222 rows) is the older, much richer registry the programme accumulated across the Session A/B/C/D era — carrying the word's definition, provenance, cluster assignment, and the per-stage status fields (`phase1_status`, `verse_context_status`, `dim_review_status`, `session_b_status`, and more) that drove that pipeline. It is now marked inactive in the project's own table register: retained for provenance, not the place new registry work is scoped from.

The row-count difference (180 live vs. 222 retained) is not yet reconciled and is not asserted here as a completed migration — it is a fact about where the two registries currently stand, left for whoever next works registry consolidation to account for.

The retained `bible_research.db` registry is worth reading, not discarding, because it is where the programme's phase-based history lives: which words were carried through Verse Context, Dimension Review, and Session B, and what those passes concluded. Its `cluster_assignment` field (C01 through C22) recorded the old run-batch tranches used to schedule Verse Context processing — an administrative grouping, not an analytical one, and distinct from the M-code `cluster` table described later in this chapter, which is the live analytical taxonomy.

The live `iba.db` registry is deliberately thin. It answers one question — is this English word in scope, and what is its onboarding status — and nothing more. The richer per-word analytical state that the old registry accreted over its lifetime is not being rebuilt onto the new registry wholesale; the current method builds its analytical record elsewhere, in the base-data and cluster tables the rest of this chapter describes, keyed off the Strong's code rather than off a registry row.

---

<!-- PROSE_SECTION_ID: 24 -->
<!-- PROSE_SECTION_TYPE: prog_data_terms -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Terms -->
<!-- PROSE_SORT_ORDER: 24 -->
<!-- PROSE_VERSION: 112 -->

## Terms

The term layer has moved to `iba.db` in full, and it is structured differently from the layer it replaced. Where the old architecture held one canonical term table (`mti_terms`) and one extraction-time inventory (`wa_term_inventory`) — both now inactive, retained in `bible_research.db` for provenance — the live architecture is a chain of small, single-purpose tables, each named for the processing layer it represents.

`word_strong` is the discovery record (L1): one row per (word, Strong's) pair that STEP's word-search returned, 4,874 rows. It carries the link only — no term detail — and is the starting point that determines which Strong's numbers a given English word's onboarding run will touch.

`strong` is the term's identity (L2): one row per Strong's number, unique and global to the whole study, 15,293 rows. Meaning is deliberately not carried on this row; it is normalised out into its own set of tables — `strong_sense`, `strong_meaning_tree`, `strong_lexicon`, `strong_lsj_parsed`, `strong_mounce_parsed` — mirroring the sense-hierarchy, LSJ, and Mounce enrichment the old `wa_meaning_parsed`/`wa_meaning_sense`/`wa_lsj_parsed` tables carried, rebuilt on the new identity table. `strong_related` (87,535 rows) carries the associative and root-family relationships the old `wa_term_related_words`/`wa_term_root_family` tables held.

`lemma_inventory` (11,781 rows) is the independent substrate the seed net runs over — imported from the old study, deliberately not derived from the registry, so that it functions as a genuine completeness control rather than a reflection of what the registry already expected to find. `candidate_seed` (2,087 rows) is the over-inclusive Axis-A candidate assessment built from it: a potential, not yet definite, decision about whether a lemma belongs in scope, with the lexical stage as the real test.

The verse-level lexical substrate is a further chain. `span` (391,417 rows) is the immutable source parse — one row per HTML `<span>` tag STEP's own interlinear presents for a verse, kept verbatim so the parse is re-derivable; a combined-unit tag (more than one Strong's or morph code on one `<span>`) is kept as one row, not split, after a 2026-07-25 correction found the earlier one-row-per-code model misattributed surface text. `span_candidate` (83,914 rows) is the L4b candidate stamp over a span — existence itself is the stamp, before the lexical stage tests it in context. `verse_lexical` (960,064 rows) is the derived, version-aware mechanical reading: the T1–T3 role classification, stem/voice-selected sense, and named-not-resolved ambiguity, one row per Strong's code within a span. It is read by `report.verse_lexical` and, downstream, never re-derived from `span`/`strong`/`strong_meaning_parsed` directly — the derivation happens once, and everything after it reads the derived row.

Every retired table in the old term layer — `mti_terms`, `wa_term_inventory`, `wa_file_index`, `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` — remains in `bible_research.db`, unaltered, as the historical record of the pre-2026-08-17 term architecture. None of them is where a current term question should be answered from.

---

<!-- PROSE_SECTION_ID: 25 -->
<!-- PROSE_SECTION_TYPE: prog_xref_architecture -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Ownership and cross-registry references -->
<!-- PROSE_SORT_ORDER: 25 -->
<!-- PROSE_VERSION: 113 -->

## Ownership and cross-registry references

The old architecture solved vocabulary overlap between registry words with an ownership rule: every Strong's number had exactly one OWNER registry (`mti_terms.owning_registry_fk`), and every other registry that found the term relevant carried it as an XREF, inheriting the OWNER's analytical record rather than duplicating it. That whole mechanism — `mti_terms.owning_registry_fk`, `wa_term_inventory.term_owner_type`, `mti_term_cross_refs`, the pure-XREF registry concept — is retired along with `mti_terms` and `wa_term_inventory` themselves. It is recorded here as history, not as a live rule to apply.

The live architecture answers a related but different question, and answers it more directly: does a Strong's code belong to a cluster (an M-code thematic grouping), and it answers this as a property of the Strong's code itself, with no dependency on any registry row at all. `cluster_strong` (7,609 rows) is the strong-to-cluster link, deliberately built with no foreign key to `word_registry` or to any term-ownership table. A Strong's code's cluster membership is decided directly, not inherited through which English word happened to introduce it.

This is a genuine architectural simplification, not merely a renaming of the old ownership rule. Where the old model needed an explicit OWNER/XREF distinction because a term's full analytical record (verses, groups, dimensions) lived under one registry's tables and had to be found from another registry's perspective, the live model keeps the term-level record (`verse_lexical`, `span`, `strong_related`) at the Strong's-code level from the start — every table in the term layer described in the previous sub-section is already keyed on the Strong's code or the span, never on a registry. There is no ownership question left to answer, because there is no registry-scoped copy of the term data to own.

`cluster_strong`'s allocation has happened in several distinct passes, each recorded by its own `source` value rather than overwriting a prior row in place: 2,801 rows carry `old-system-migration` (the 2026-08-11 migration from `bible_research.db`'s original `cluster` table), 1,612 carry `llm-allocation-v1_3-20260811`, 203 carry `llm-reassignment-v1_1-20260811`, 1,414 carry `auto-precedent`, 1,574 carry `manual-backfill-triage-20260813`, and 5 carry `manual-covenant-cluster-20260813`. The `manual-backfill-triage` batch followed a researcher correction (2026-08-13) that a bulk keyword-crossmatch allocation of the backfill Strong's codes into clusters was not an acceptable substitute for allocation grounded in actual verse-context analysis; the batch recorded under that source name is the analysis-grounded correction, not the automation it replaced.

`word_strong` remains a many-to-many link in its own right — a Strong's code can be discovered through more than one English word's onboarding run — but this no longer creates an ownership question the way it once did, because the analytical record a Strong's code accumulates (its lexical readings, its cluster membership) does not live under any one word's registry row.

---

<!-- PROSE_SECTION_ID: 26 -->
<!-- PROSE_SECTION_TYPE: prog_data_verses -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Verses and the context layer -->
<!-- PROSE_SORT_ORDER: 26 -->
<!-- PROSE_VERSION: 114 -->

## Verses and the context layer

The verse layer has been rebuilt in `iba.db`, and it is considerably simpler than the classification grid it replaced. `iba.db`'s `verse` table (29,759 rows) carries only the addressable identity of a verse — `osisId`, `reference`, and `preview` (the full interlinear HTML, kept verbatim so `span` is re-derivable) — with no relevance flag, no anchor flag, no group membership, and no genre or process-stage column. `bible_research.db`'s own `verse` table (25,634 rows, all 66 books, carrying `passage_id`, `is_passage_anchor`, `process_marker`, and `genre` columns) is the substrate of the July-2026 verse-first/genre-aware lexical method — the method a live reading test (Jonah 3) judged failed on 2026-08-03; that table is marked inactive in the project's own register, retained as the record of that attempt, not the live verse table.

`verse_context` and `verse_context_group` — the relevance/anchor/related classification grid and the context-group table the old architecture built its Session B analysis on — do not exist in `iba.db` at all. They are not superseded by a like-for-like replacement; the classification work they did is now split across two different live mechanisms described in the sub-sections that follow: `verse_lexical`'s mechanical T1–T3 reading (a per-Strong's-code classification, not a per-term-per-group one), and the book-by-book passage/phenomenon/debate pipeline (a per-passage, per-Human-Inner-Being classification). Anyone looking for the old `verse_context` table's descendant should look at both, not at a single direct replacement.

The live passage layer is `verse_passage` (25,690 rows — passage membership, `is_anchor` flag per verse-in-passage) and `passage` (18,558 rows — the reading-frame register; a passage is a maximal run of consecutive verses, chapter-bounded in practice, anchored on its first verse via `anchor_verse_id`). Both are `iba.db` tables and both are actively written by the book-by-book debate pipeline, not retained history.

The book-by-book debate pipeline itself adds a further, distinctly analytical layer on top of the passage register: `hib` (63 rows — a Human Inner Being identified within a book's scope, recurring across many passages of that book), `phenomenon` (177 rows — one row per HIB per verse per passage, Step 3 of the debate digest), and `operation` (177 rows — the operation registered for a phenomenon, Step 4–5 output; a `phenomenon_id NOT NULL` constraint enforces that an operation always traces to a phenomenon). `passage_linkage`, `passage_insufficiency`, `passage_emergent_question`, and `passage_validation_note` carry the debate's supporting judgement calls, and `debate_change_detail` (242 rows) is the shared per-run CRUD audit trail across every debate writer (`hib.set`, `passage.build`, `phenomenon.set`, `operation.set`, `closing.set`).

The `passage` table's `debate_status` field shows exactly how far this live analytical work has reached: of 18,558 passages spanning the whole Bible, only 49 currently carry a debate status (45 `filled`, 4 `complete`), concentrated in six books — Daniel, Jonah, Joel, Obadiah, Micah, and Hosea. The great majority of the passage register (18,504 rows, carrying `rule='char-continuity'`) exists as the reading-frame substrate the debate work will draw on as it proceeds; it is not itself evidence that those passages have been analytically read.

---

<!-- PROSE_SECTION_ID: 27 -->
<!-- PROSE_SECTION_TYPE: prog_anchor_verse -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The anchor verse -->
<!-- PROSE_SORT_ORDER: 27 -->
<!-- PROSE_VERSION: 115 -->

## The anchor verse

The anchor concept survives the architecture change, but it now attaches to a passage rather than to a term-in-group classification. `verse_passage.is_anchor` marks the verse chosen to represent its passage — the (passage × verse) row that carries the flag is the passage's anchor, in the same spirit as the old `verse_context.is_anchor` flag marked a group's canonical citation, but scoped to the passage register rather than to a term-specific context group. `passage.anchor_verse_id` duplicates the same designation at the passage-row level, for direct lookup without a join.

`hib.first_verse_id` plays an analogous role for a Human Inner Being: the verse at which that HIB was first identified within its book's scope. Because a HIB recurs across many passages of the same book rather than being scoped to one passage, its first-verse designation is the closest live equivalent to the old architecture's "canonical citation" idea, applied at the HIB level rather than the group level.

What the anchor no longer is: a per-term, per-context-group designation chosen from among a term's classified verses, with the one-or-two-anchors-per-group convention, the no-clear-anchor fallback, and the promotion/demotion discipline the old `verse_context` architecture built around it. That whole apparatus depended on the classification grid described in the previous sub-section, and it does not exist in the live schema. The live anchor is simpler and coarser: one flagged verse per passage, one first-identified verse per HIB, both serving the same underlying purpose — giving the reader-facing account and the analytical writer a specific verse to point to — without the group-level machinery the earlier method built to manage competing candidate anchors.

---

<!-- PROSE_SECTION_ID: 28 -->
<!-- PROSE_SECTION_TYPE: prog_data_dimensions -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Dimensions — the analytical grouping mechanism -->
<!-- PROSE_SORT_ORDER: 28 -->
<!-- PROSE_VERSION: 116 -->

## Dimensions — the analytical grouping mechanism

The programme's live analytical grouping mechanism is the M-code cluster model, not the dimension-review layer the earlier architecture built. `cluster` (49 rows: M01 through M46-numbered codes, plus FLAG and T2) names the top-level thematic groupings of the study — Anger, Wisdom, Peace, and so on — keyed on the M-code itself so the code is the stable identifier used everywhere else in the model. `characteristic` (277 rows across 35 of the 49 clusters) names the distinct inner-being traits a cluster resolves into, each with its own definition; the rows accumulated across several eras — 53 backfilled directly from sub-groups in May, 78 added in July as explicitly provisional top-down exemplars — and `cluster_subgroup` (sub-divisions such as M01-A or M01-BOUNDARY) exists for only 17 of the 49 clusters, with 19 of its rows delete-flagged, so the table records the sub-group design's history as much as its current state.

`wa_dimension_index` (3,509 rows) — the old per-`verse_context_group` dimension-review layer, assigning each group one of eleven working dimension labels (Emotion — Positive/Negative, Cognition, Volition, Moral Character, and the others) — is explicitly retired. It is retained in `bible_research.db`, not deleted, because it is a genuine record of the analytical work that era of the programme produced; it is not where a current dimensional question is answered from, and it has no live successor performing the same per-group classification. The cluster/characteristic model that replaced it works at a different grain — the Strong's code and the cluster, not the verse-context group — and does not attempt a like-for-like migration of the old dimension labels onto the new structure.

`cluster_strong`'s allocation passes (described in the sub-section on ownership) are the live mechanism by which a Strong's code enters the M-code analytical model — and the 2026-08-13 correction recorded there (rejecting bulk keyword-crossmatch allocation in favour of allocation grounded in verse-context analysis) is the standing rule for how any further allocation work must proceed. A cluster's characteristics, and the Strong's codes assigned to it, are the current form the programme's analytical grouping takes; the dimension vocabulary of the earlier era is history the current model does not carry forward.

---

<!-- PROSE_SECTION_ID: 70 -->
<!-- PROSE_SECTION_TYPE: prog_data_questions -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The question catalogue and findings -->
<!-- PROSE_SORT_ORDER: 29 -->
<!-- PROSE_VERSION: 1160 -->

## The question catalogue and findings

`wa_obs_question_catalogue` remains a live table — 424 prompts organised by tier and component, each with its text, scope, provenance, and lifecycle status — but its own state is worth stating plainly rather than glossing over: 243 of the 424 rows are marked `deleted` and only 239 are marked `active`, the residue of a v2 restructure that retired 159 questions as redundant. The two lifecycle markers (`deleted` and `status`) do not agree in count, which means the table's own bookkeeping of what is and isn't current is not fully self-consistent. A reader drawing questions from this catalogue should check both fields, not one.

`finding` is the universal finding store the architecture consolidated per-word findings into — one row per typed analytical finding at VERSE, CLUSTER, or GLOBAL level, 438,000 rows in total, with VERSE dominating at over 430,000 of them. The fact that matters most about this table today is not its size but its state: roughly 92% of its rows carry `delete_flagged = 1` — every `l2_api` and `l2_mechanical` row, and most `l2_meaning` rows, are soft-deleted — leaving on the order of 35,000 live findings. `finding` is, at present, mostly a retained legacy substrate rather than an active corpus; a query against it should filter on `delete_flagged` deliberately, and a claim that findings "drive" current analysis should be checked against that 35,000-row live subset, not the 438,000-row total.

`wa_session_b_findings` (2,883 findings, raised April to May 2026 across 112 registries) is the superseded per-word findings store `finding` replaced. It is retained, with its own audit trail, rather than live — a further layer of the same consolidation `finding` represents, one step further back in the programme's history.

`wa_session_research_flags` is still an actively populated table (715 rows), and its distribution shows where the live cross-registry and structural-observation work actually sits today: `SD_POINTER` (357 rows) is the largest single flag code, followed by `SB_FINDING` (203) and `VERSE_EVIDENCE_BREADTH_NOTE` (52); the remainder — `BOUNDARY_DECISION_PENDING`, the `PH2_*` codes, `DIMREVIEW_SESSION_D`, `RESEARCHER_DECISION`, and others — are smaller, specific markers accumulated across the programme's various analytical passes. This table is the bridge to the next sub-section: the SD pointer is the mechanism by which a single-registry observation is carried forward toward cross-registry synthesis.

---

<!-- PROSE_SECTION_ID: 30 -->
<!-- PROSE_SECTION_TYPE: prog_data_synthesis -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The synthesis bridge — from per-word records to cross-registry work -->
<!-- PROSE_SORT_ORDER: 30 -->
<!-- PROSE_VERSION: 117 -->

## The synthesis bridge — from per-word records to cross-registry work

The SD pointer mechanism described in the previous sub-section — a `wa_session_research_flags` row with `flag_code = 'SD_POINTER'` — remains the programme's standing bridge from a single registry's analytical observation to a cross-registry question worth investigating. 357 such pointers exist. What has not changed since the previous version of this chapter is that Session D itself has never run: `session_d_runs` and `session_d_observations` both hold zero rows. The pointer record has accumulated; the investigation it is meant to feed has not yet been declared.

`wa_cross_registry_links` (158 rows, keyed through `wa_crosslink_type`'s eleven connection types) remains the other cross-word relationship mechanism the old architecture built — shared term, root family, semantic adjacency, and the other categories the programme identified before the method reset. It, like the SD pointer backlog, is retained but has not been extended or superseded by a new cross-registry mechanism; the live cluster/characteristic model described earlier in this chapter is, in practice, now doing a version of the cross-word grouping work these tables were built to support — a cluster's characteristics group Strong's codes across whatever English registry words happen to touch them, which is closer to the synthesis these tables were reaching for than either table was designed to deliver on its own.

The honest state of this sub-section, stated plainly rather than as a pending-but-imminent milestone: the cross-registry synthesis layer the earlier architecture designed (SD pointers accumulating toward a Session D run) has not executed, and the live analytical work of the programme — the book-by-book debate pipeline, the cluster/characteristic allocation — has not been built as a direct continuation of that specific design. Both exist in the database; neither has been formally reconciled with the other, and that reconciliation is not attempted here.

---

<!-- PROSE_SECTION_ID: 31 -->
<!-- PROSE_SECTION_TYPE: prog_data_prose_store -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The prose store — phase-bridge architecture -->
<!-- PROSE_SORT_ORDER: 31 -->
<!-- PROSE_VERSION: 118 -->

## The prose store — phase-bridge architecture

The prose store remains `bible_research.db`'s DB-canonical mechanism for authored narrative, and it is the most actively developed part of the architecture described in this chapter — this very chapter is being written through it. `prose_section_type` is the dictionary of stable named slots prose can be written into; it has grown to 108 codes (from 34 at the time this chapter was last drafted), spanning programme documentation, per-session outputs, cluster findings, and lexical prose, more than half of them now belonging to the `programme` book rather than to any single analytical stage. `prose_section` is the content — one row per titled section, carrying its body, version, and lifecycle state. Nearly all of it is machine-authored (`claude_code` or `claude_ai`); at the time of writing, exactly one row is attributed directly to the researcher.

The lifecycle mechanism changed on 2026-08-24 (escalation #836). The earlier append-only supersede model — a revision creates a new row, the old row's `superseded_by_id` points forward — has been rebuilt onto Model A: system-versioned temporal tables. `apply_session_patch.py` now mutates a superseded `prose_section` row in place rather than inserting a new row; the prior content is preserved automatically by SQLite's own temporal-versioning mechanism rather than by a hand-maintained `supersedes_id`/`superseded_by_id` chain. The practical consequence for an author is the same as before — no edit is silently lost, the full history is queryable — but the mechanism that guarantees it is now the database engine's own versioning, not application-level bookkeeping. `record_change_log`, introduced the same day, is a project-wide change-audit log, not a prose-specific one; prose edits are one of the kinds of change it records.

`prose_section_verse_link` (added with the 2026-08-26 prose add/edit rules, escalation #890) is a further link table connecting a prose row to the specific verses it discusses, alongside the existing `prose_section_dimension_link` and `prose_section_finding_link`. Together the three link tables let a query start from a verse, a dimension, or a finding and find every prose passage that discusses it, or start from a prose passage and find the evidence it rests on.

The prose store also now carries its own quality-flagging mechanism, repurposed from the old `wa_quality_flag_types`/`wa_data_quality_flags` tables (escalation #833): a `PROSE_QUALITY` flag can be raised against the corpus generally (not tied to a specific `prose_section` row, since the section a flag concerns is found by search at fix time, not stored from raise time), a fix can be proposed by searching the active corpus for a literal match and previewing the replacement, and an approved fix is applied as a PROSE supersede patch — the same patch mechanism this chapter's own edit goes through.

`Prose.ps1` is the registered operational front door onto all of this: `Extract` (JSON/Markdown/DOCX programme-prose extracts), `Search` (FTS5 search across active sections), `ExportChapter`/`ImportChapter` (the editable-Markdown round trip this chapter's own revision used), and `Flag`/`FlagFixPropose`/`FlagFixApply` (the quality-flag workflow just described). Every step reads its configuration — chapter names, the book/stage map, the search result limit, the edit-file directory — from `cfg_prose`, not from a hardcoded constant. The database remains the store's canonical form throughout: a draft Markdown file is the input, the PROSE patch reads it, `apply_session_patch.py` writes it to the database, and any extract is regenerated from the database afterward. The principle this whole mechanism serves is unchanged from the previous version of this chapter — the database is the programme's analytical memory, not only its evidentiary substrate — but the machinery that delivers on it has been substantially rebuilt since.

---

<!-- PROSE_SECTION_ID: 66 -->
<!-- PROSE_SECTION_TYPE: prog_data_obslog_pipeline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Obslog-to-DB capture pipeline -->
<!-- PROSE_SORT_ORDER: 32 -->
<!-- PROSE_VERSION: 1156 -->

## Programme — Obslog-to-DB capture pipeline

The obslog-to-DB pipeline this section previously described — a comprehensive Session B analytical `.md` parsed into a structured manifest and dispatched into `wa_session_b_findings`, `wa_finding_catalogue_links`, and versioned `prose_section` chapters — belonged to Architecture v2 (2026-04-27) and does not operate today. Session B itself, and the obslog format it read from, are retired along with the per-word analytical pipeline described in earlier sub-sections; the tables it wrote to (`wa_session_b_findings`, `wa_finding_catalogue_links`) are retained as history, not live capture targets.

The live capture mechanisms are three, each serving a different kind of work, and none of them resembles the single obslog-parse-and-dispatch design this section used to describe. First, for programme and analytical prose: the `Prose.ps1` round trip described in the previous sub-section — export a chapter to editable Markdown, edit the body under each section's fixed heading, import to generate a PROSE supersede patch, apply the patch with `scripts/apply_session_patch.py`. No step in that chain writes to the database directly; the patch step is always a distinct, reviewable operation from the write step. This chapter's own revision is an instance of that pipeline.

Second, for the book-by-book debate work: `debate_change_detail` is the shared per-run CRUD audit trail across every debate writer — `hib.set`, `passage.build`, `phenomenon.set`, `operation.set`, and `closing.set` each log their inserts, updates, and soft-deletes to this one table (242 rows to date), giving the debate pipeline the same kind of write-provenance record the prose store gets from its own versioning, without needing a bespoke obslog format of its own. `passage.debate_sync` (built 2026-07-30 in response to a gap found live while debating Micah) is the registered step that re-checks an already-written debate file for its fill-in-placeholder marker and updates `passage.debate_status` accordingly — a deliberately narrow, config-registered mechanism, built precisely because reconstructing "how did the prior book's debate get marked filled" from `BUILD.md` history and archived output files was recognised as itself the signal that a required step was missing, not a puzzle to solve from precedent.

Third, for anomalies, judgement calls, and anything requiring a decision the running code cannot make on its own: the `escalation` table, described in full in the next chapter. Where the old pipeline surfaced `DATA_ANOMALY_*` findings into the next analytical session's queue, the live mechanism raises a typed escalation with an explicit `resolution_kind` (decision-required or self-correctable) and a `next_action`, tracked to closure through `Escalation.ps1` rather than through a narrative obslog section.

What the three mechanisms share, and what the retired obslog pipeline shared with them, is the same underlying discipline: a write to the database is always a distinct, auditable step from the analytical or editorial work that produced it, and the record of that write — a patch, a `debate_change_detail` row, an escalation history row — outlives the session that made it.

---
