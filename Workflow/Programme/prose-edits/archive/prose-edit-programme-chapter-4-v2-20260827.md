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
<!-- PROSE_VERSION: 1209 -->

## The database as the programme's working memory

The programme runs on two SQLite databases. `iba/app/db/iba.db` is the home for all project process control and base data — every table from STEP extraction through Strong's, verses, meaning, and lexical detail, and the `cfg_*` configuration store that governs how every script and module behaves. `database/bible_research.db` is the home for prose and findings — the analytical output built on top of the base data, and the DB-canonical prose store the programme's written account is authored into.

`iba.db` is governed by its own `cfg_*` system — twenty tables, on the order of a thousand rows, that hold every rule the app's code obeys: which API may write which table, what a step's failure path is, what a controlled vocabulary's allowed values are, what a report's structure is. The principle is that the code decides nothing; every choice the code used to make in a literal is now a row a live check can read. This governing layer is itself part of the data architecture — not a separate concern bolted on afterward — because it is what makes the base-data layer's behaviour traceable and changeable without a code edit. Chapter 5 describes the governance mechanism itself in full; this chapter describes what the two databases hold.

Neither database is the primary source for the Hebrew, Greek, and Aramaic material the programme works with. STEP Bible, a peer-maintained scholarly resource, remains the source every Strong's number, gloss, meaning parse, and verse reference traces back to. `iba.db`'s base-data layer is the programme's verified, structured copy of what STEP returns — not a replacement for STEP, a working record built from it.

`iba.db` is primary for all base-data and process-control work; a handful of the analytical tables it currently carries — the book-by-book passage/phenomenon/debate pipeline described later in this chapter — are expected to migrate back into `research_db` once the analysis phase is properly under way (escalation #737, on hold). `bible_research.db` is primary for prose and findings, including the cluster/characteristic analytical model that is the programme's current analytical grouping mechanism.

The sub-sections that follow work through what is live in each database, table by table: the registry, the term/lexical substrate, the verse and passage layer, the anchor-verse mechanism, the cluster/characteristic analytical grouping, the question catalogue and the finding store, the synthesis bridge, and the prose store. Each describes the architecture as it operates today — a data table this chapter does not name is not part of the current architecture, whatever its history.

---

<!-- PROSE_SECTION_ID: 23 -->
<!-- PROSE_SECTION_TYPE: prog_data_registry -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The registry -->
<!-- PROSE_SORT_ORDER: 23 -->
<!-- PROSE_VERSION: 1177 -->

## The registry

`iba.db`'s `word_registry` (180 rows) is the programme's live registry — the scope of a new-word onboarding run. A row carries `word` (the English headword), `source` (why it entered scope), `status` (its onboarding state), and the timestamps a run needs. It is deliberately thin: it answers one question — is this English word in scope, and what is its onboarding status — and nothing more.

The registry's analytical weight sits elsewhere. A word's actual lexical and analytical record is not accreted onto the registry row itself; it is built in the base-data and cluster tables the rest of this chapter describes, keyed off the Strong's code a word's onboarding run discovers, not off the registry row. The registry is the entry point and the scope list; it is not where the programme's findings about a word live.

---

<!-- PROSE_SECTION_ID: 24 -->
<!-- PROSE_SECTION_TYPE: prog_data_terms -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Terms -->
<!-- PROSE_SORT_ORDER: 24 -->
<!-- PROSE_VERSION: 1178 -->

## Terms

The term layer lives in `iba.db`, as a chain of small, single-purpose tables, each named for the processing layer it represents.

`word_strong` is the discovery record (L1): one row per (word, Strong's) pair that STEP's word-search returned, 4,874 rows. It carries the link only — no term detail — and is the starting point that determines which Strong's numbers a given English word's onboarding run will touch.

`strong` is the term's identity (L2): one row per Strong's number, unique and global to the whole study, 15,293 rows. Meaning is deliberately not carried on this row; it is normalised out into its own set of tables — `strong_sense`, `strong_meaning_tree`, `strong_lexicon`, `strong_lsj_parsed`, `strong_mounce_parsed` — the sense-hierarchy, LSJ, and Mounce enrichment for the term. `strong_related` (87,535 rows) carries the term's associative and root-family relationships.

`lemma_inventory` (11,781 rows) is the independent substrate the seed net runs over — imported from the old study, deliberately not derived from the registry, so that it functions as a genuine completeness control rather than a reflection of what the registry already expected to find. `candidate_seed` (2,087 rows) is the over-inclusive Axis-A candidate assessment built from it: a potential, not yet definite, decision about whether a lemma belongs in scope, with the lexical stage as the real test.

The verse-level lexical substrate is a further chain. `span` (391,417 rows) is the immutable source parse — one row per HTML `<span>` tag STEP's own interlinear presents for a verse, kept verbatim so the parse is re-derivable; a combined-unit tag (more than one Strong's or morph code on one `<span>`) is kept as one row, not split, after a 2026-07-25 correction found the earlier one-row-per-code model misattributed surface text. `span_candidate` (83,914 rows) is the L4b candidate stamp over a span — existence itself is the stamp, before the lexical stage tests it in context. `verse_lexical` (960,064 rows) is the derived, version-aware mechanical reading: the T1–T3 role classification, stem/voice-selected sense, and named-not-resolved ambiguity, one row per Strong's code within a span. It is read by `report.verse_lexical` and, downstream, never re-derived from `span`/`strong` directly — the derivation happens once, and everything after it reads the derived row.

---

<!-- PROSE_SECTION_ID: 25 -->
<!-- PROSE_SECTION_TYPE: prog_xref_architecture -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Ownership and cross-registry references -->
<!-- PROSE_SORT_ORDER: 25 -->
<!-- PROSE_VERSION: 1179 -->

## Ownership and cross-registry references

Inner-being vocabulary overlaps across registry words, and the architecture answers a direct question about that overlap: does a Strong's code belong to a cluster (an M-code thematic grouping)? It answers this as a property of the Strong's code itself, with no dependency on any registry row at all. `cluster_strong` (7,609 rows) is the strong-to-cluster link, deliberately built with no foreign key to `word_registry`. A Strong's code's cluster membership is decided directly, not inherited through which English word happened to introduce it.

Every table in the term layer described in the previous sub-section is already keyed on the Strong's code or the span, never on a registry. A term's analytical record — its lexical readings, its cluster membership — accumulates at the Strong's-code level from the start; there is no per-registry copy of that record to reconcile across words that share a term.

`cluster_strong`'s allocation has happened in several distinct passes, each recorded by its own `source` value rather than overwriting a prior row in place: 2,801 rows carry `old-system-migration` (the 2026-08-11 migration that seeded the table), 1,612 carry `llm-allocation-v1_3-20260811`, 203 carry `llm-reassignment-v1_1-20260811`, 1,414 carry `auto-precedent`, 1,574 carry `manual-backfill-triage-20260813`, and 5 carry `manual-covenant-cluster-20260813`. The `manual-backfill-triage` batch followed a researcher correction (2026-08-13) that a bulk keyword-crossmatch allocation of the backfill Strong's codes into clusters was not an acceptable substitute for allocation grounded in actual verse-context analysis; the batch recorded under that source name is the analysis-grounded correction, not the automation it replaced. That correction is the standing rule for how any further allocation work must proceed.

`word_strong` is a many-to-many link — a Strong's code can be discovered through more than one English word's onboarding run — but this does not create an ownership question, because the analytical record a Strong's code accumulates does not live under any one word's registry row.

---

<!-- PROSE_SECTION_ID: 26 -->
<!-- PROSE_SECTION_TYPE: prog_data_verses -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Verses and the context layer -->
<!-- PROSE_SORT_ORDER: 26 -->
<!-- PROSE_VERSION: 1180 -->

## Verses and the context layer

`iba.db`'s `verse` table (29,759 rows) carries the addressable identity of a verse — `osisId`, `reference`, and `preview` (the full interlinear HTML, kept verbatim so `span` is re-derivable).

The live passage layer sits above it: `verse_passage` (25,690 rows — passage membership, `is_anchor` flag per verse-in-passage) and `passage` (18,558 rows — the reading-frame register; a passage is a maximal run of consecutive verses, chapter-bounded in practice, anchored on its first verse via `anchor_verse_id`).

The book-by-book debate pipeline adds a further, distinctly analytical layer on top of the passage register: `hib` (63 rows — a Human Inner Being identified within a book's scope, recurring across many passages of that book), `phenomenon` (177 rows — one row per HIB per verse per passage, Step 3 of the debate digest), and `operation` (177 rows — the operation registered for a phenomenon, Step 4–5 output; a `phenomenon_id NOT NULL` constraint enforces that an operation always traces to a phenomenon). `passage_linkage`, `passage_insufficiency`, `passage_emergent_question`, and `passage_validation_note` carry the debate's supporting judgement calls, and `debate_change_detail` (242 rows) is the shared per-run CRUD audit trail across every debate writer (`hib.set`, `passage.build`, `phenomenon.set`, `operation.set`, `closing.set`).

The `passage` table's `debate_status` field shows exactly how far this analytical work has reached: of 18,558 passages spanning the whole Bible, only 49 currently carry a debate status (45 `filled`, 4 `complete`), concentrated in six books — Daniel, Jonah, Joel, Obadiah, Micah, and Hosea. The great majority of the passage register (18,504 rows, carrying `rule='char-continuity'`) exists as the reading-frame substrate the debate work will draw on as it proceeds; it is not itself evidence that those passages have been analytically read.

---

<!-- PROSE_SECTION_ID: 27 -->
<!-- PROSE_SECTION_TYPE: prog_anchor_verse -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The anchor verse -->
<!-- PROSE_SORT_ORDER: 27 -->
<!-- PROSE_VERSION: 1181 -->

## The anchor verse

`verse_passage.is_anchor` marks the verse chosen to represent its passage — the (passage × verse) row that carries the flag is the passage's anchor. `passage.anchor_verse_id` duplicates the same designation at the passage-row level, for direct lookup without a join.

`hib.first_verse_id` plays an analogous role for a Human Inner Being: the verse at which that HIB was first identified within its book's scope. Because a HIB recurs across many passages of the same book rather than being scoped to one passage, its first-verse designation gives the reader-facing account and the analytical writer a specific verse to point to at the HIB level, distinct from the passage-level anchor above it.

Both anchors are simple and coarse by design: one flagged verse per passage, one first-identified verse per HIB. Each exists to give a reader a specific piece of verse evidence to cite, not to arbitrate between competing candidate verses within a larger classification structure.

---

<!-- PROSE_SECTION_ID: 28 -->
<!-- PROSE_SECTION_TYPE: prog_data_dimensions -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Dimensions — the analytical grouping mechanism -->
<!-- PROSE_SORT_ORDER: 28 -->
<!-- PROSE_VERSION: 1182 -->

## Dimensions — the analytical grouping mechanism

The programme's analytical grouping mechanism is the M-code cluster model. `cluster` (49 rows: M01 through M46-numbered codes, plus FLAG and T2) names the top-level thematic groupings of the study — Anger, Wisdom, Peace, and so on — keyed on the M-code itself so the code is the stable identifier used everywhere else in the model. `characteristic` (277 rows across 35 of the 49 clusters) names the distinct inner-being traits a cluster resolves into, each with its own definition; the rows accumulated across several eras — 53 backfilled directly from sub-groups in May, 78 added in July as explicitly provisional top-down exemplars. `cluster_subgroup` (sub-divisions such as M01-A or M01-BOUNDARY) exists for only 17 of the 49 clusters, with 19 of its rows delete-flagged, so the table records the sub-group design's history as much as its current state.

`cluster_strong`'s allocation passes (described in the sub-section on ownership) are the live mechanism by which a Strong's code enters the M-code analytical model — and the 2026-08-13 correction recorded there (rejecting bulk keyword-crossmatch allocation in favour of allocation grounded in verse-context analysis) is the standing rule for how any further allocation work must proceed. A cluster's characteristics, and the Strong's codes assigned to it, are the current form the programme's analytical grouping takes.

---

<!-- PROSE_SECTION_ID: 70 -->
<!-- PROSE_SECTION_TYPE: prog_data_questions -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The question catalogue and findings -->
<!-- PROSE_SORT_ORDER: 29 -->
<!-- PROSE_VERSION: 1183 -->

## The question catalogue and findings

`wa_obs_question_catalogue` is a live table in `bible_research.db` — 424 prompts organised by tier and component, each with its text, scope, provenance, and lifecycle status — but its own state is worth stating plainly rather than glossing over: 243 of the 424 rows are marked `deleted` and only 239 are marked `active`, the residue of a v2 restructure that retired 159 questions as redundant. The two lifecycle markers (`deleted` and `status`) do not agree in count, which means the table's own bookkeeping of what is and isn't current is not fully self-consistent. A reader drawing questions from this catalogue should check both fields, not one.

`finding` is the programme's universal finding store — one row per typed analytical finding at VERSE, CLUSTER, or GLOBAL level, 438,000 rows in total, with VERSE dominating at over 430,000 of them. The fact that matters most about this table today is not its size but its state: roughly 92% of its rows carry `delete_flagged = 1`, leaving on the order of 35,000 live findings. A query against it should filter on `delete_flagged` deliberately, and a claim that findings "drive" current analysis should be checked against that 35,000-row live subset, not the 438,000-row total.

`wa_session_research_flags` is an actively populated table (715 rows), and its distribution shows where the live cross-registry and structural-observation work actually sits today: `SD_POINTER` (357 rows) is the largest single flag code, followed by `SB_FINDING` (203) and `VERSE_EVIDENCE_BREADTH_NOTE` (52); the remainder are smaller, specific markers accumulated across the programme's various analytical passes. This table is the bridge to the next sub-section: the SD pointer is the mechanism by which a single-registry observation is carried forward toward cross-registry synthesis.

---

<!-- PROSE_SECTION_ID: 30 -->
<!-- PROSE_SECTION_TYPE: prog_data_synthesis -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The synthesis bridge — from per-word records to cross-registry work -->
<!-- PROSE_SORT_ORDER: 30 -->
<!-- PROSE_VERSION: 1184 -->

## The synthesis bridge — from per-word records to cross-registry work

The SD pointer mechanism described in the previous sub-section — a `wa_session_research_flags` row with `flag_code = 'SD_POINTER'` — is the programme's standing bridge from a single registry's analytical observation to a cross-registry question worth investigating. 357 such pointers exist. `session_d_runs` and `session_d_observations` both hold zero rows: the pointer record has accumulated; the investigation it is meant to feed has not yet been declared.

The live cluster/characteristic model described earlier in this chapter is, in practice, doing a version of the cross-word synthesis work the SD pointer mechanism was built to feed — a cluster's characteristics group Strong's codes across whatever English registry words happen to touch them. The two mechanisms exist side by side in the database; they have not been formally reconciled with each other, and that reconciliation is not attempted here.

---

<!-- PROSE_SECTION_ID: 31 -->
<!-- PROSE_SECTION_TYPE: prog_data_prose_store -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The prose store — phase-bridge architecture -->
<!-- PROSE_SORT_ORDER: 31 -->
<!-- PROSE_VERSION: 1185 -->

## The prose store — phase-bridge architecture

The prose store is `bible_research.db`'s DB-canonical mechanism for authored narrative, and it is the most actively developed part of the architecture described in this chapter — this very chapter is being written through it. `prose_section_type` is the dictionary of stable named slots prose can be written into — 108 codes, spanning programme documentation, per-session outputs, cluster findings, and lexical prose, more than half of them belonging to the `programme` book rather than to any single analytical stage. `prose_section` is the content — one row per titled section, carrying its body, version, and lifecycle state. Nearly all of it is machine-authored (`claude_code` or `claude_ai`); at the time of writing, exactly one row is attributed directly to the researcher.

The store's lifecycle mechanism is Model A: system-versioned temporal tables (escalation #836, 2026-08-24). `apply_session_patch.py` mutates a superseded `prose_section` row in place rather than inserting a new row; the prior content is preserved automatically by SQLite's own temporal-versioning mechanism. The practical consequence for an author is that no edit is silently lost and the full history is queryable, guaranteed by the database engine's own versioning rather than application-level bookkeeping. `record_change_log` is a project-wide change-audit log, not a prose-specific one; prose edits are one of the kinds of change it records.

`prose_section_verse_link`, `prose_section_dimension_link`, and `prose_section_finding_link` are three link tables connecting a prose row to the specific verses, dimensions, and findings it discusses. Together they let a query start from a verse, a dimension, or a finding and find every prose passage that discusses it, or start from a prose passage and find the evidence it rests on.

The prose store also carries its own quality-flagging mechanism: a `PROSE_QUALITY` flag can be raised against the corpus generally (not tied to a specific `prose_section` row, since the section a flag concerns is found by search at fix time, not stored from raise time), a fix can be proposed by searching the active corpus for a literal match and previewing the replacement, and an approved fix is applied as a PROSE supersede patch — the same patch mechanism this chapter's own edit goes through.

`Prose.ps1` is the registered operational front door onto all of this: `Extract` (JSON/Markdown/DOCX programme-prose extracts), `Search` (FTS5 search across active sections), `ExportChapter`/`ImportChapter` (the editable-Markdown round trip this chapter's own revision used), `Flag`/`FlagFixPropose`/`FlagFixApply` (the quality-flag workflow just described), and `SetStatus` (setting or resetting a section's own review status directly, no body change). Every step reads its configuration — chapter names, the book/stage map, the search result limit, the edit-file directory — from `cfg_prose`, not from a hardcoded constant. The database remains the store's canonical form throughout: a draft Markdown file is the input, the PROSE patch reads it, `apply_session_patch.py` writes it to the database, and any extract is regenerated from the database afterward.

---

<!-- PROSE_SECTION_ID: 66 -->
<!-- PROSE_SECTION_TYPE: prog_data_obslog_pipeline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Obslog-to-DB capture pipeline -->
<!-- PROSE_SORT_ORDER: 32 -->
<!-- PROSE_VERSION: 1186 -->

## Programme — Obslog-to-DB capture pipeline

The programme's live capture mechanisms are three, each serving a different kind of work.

First, for programme and analytical prose: the `Prose.ps1` round trip described in the previous sub-section — export a chapter to editable Markdown, edit the body under each section's fixed heading, import to generate a PROSE supersede patch, apply the patch with `scripts/apply_session_patch.py`. No step in that chain writes to the database directly; the patch step is always a distinct, reviewable operation from the write step. This chapter's own revision is an instance of that pipeline.

Second, for the book-by-book debate work: `debate_change_detail` is the shared per-run CRUD audit trail across every debate writer — `hib.set`, `passage.build`, `phenomenon.set`, `operation.set`, and `closing.set` each log their inserts, updates, and soft-deletes to this one table (242 rows to date), giving the debate pipeline the same kind of write-provenance record the prose store gets from its own versioning. `passage.debate_sync` is the registered step that re-checks an already-written debate file for its fill-in-placeholder marker and updates `passage.debate_status` accordingly — a deliberately narrow, config-registered mechanism, built precisely because reconstructing a missing step from past output files is itself the signal that a required step is missing, not a puzzle to solve from precedent.

Third, for anomalies, judgement calls, and anything requiring a decision the running code cannot make on its own: the `escalation` table, described in full in the next chapter. The live mechanism raises a typed escalation with an explicit `resolution_kind` (decision-required or self-correctable) and a `next_action`, tracked to closure through `Escalation.ps1`.

What the three mechanisms share is the same underlying discipline: a write to the database is always a distinct, auditable step from the analytical or editorial work that produced it, and the record of that write — a patch, a `debate_change_detail` row, an escalation history row — outlives the session that made it.

---
