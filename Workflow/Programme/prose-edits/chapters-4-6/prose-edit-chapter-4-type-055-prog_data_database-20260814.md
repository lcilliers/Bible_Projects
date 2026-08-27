# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 22 -->
<!-- PROSE_SECTION_TYPE: prog_data_database -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The database as the programme's working memory -->
<!-- PROSE_SORT_ORDER: 22 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch4-obslog-v1_0-20260423.md -->

## The database as the programme's working memory

The Soul Word Analysis Programme is built on a single SQLite database, `bible_research.db`. The database holds every structured artefact the programme produces — the registry, the extracted terms, the verse records, the classification of each term in each verse, the dimensional evidence, the question catalogue, the findings, the synthesis pointers, and the programme's own prose. Schema v3.14.0 carries this in sixty-two tables, organised by the architectural layers described in the rest of this chapter.

The database is the programme's **working memory**. Analytical work written to the database survives session boundaries in the way evidence does — a finding recorded against a term in a specific verse can be read back in a later session exactly as it was recorded, without depending on any session's memory or any intermediary file. This is the DB-canonical principle: the database is the authoritative record of the programme's interpretation, not only of its evidentiary substrate.

The database is not the primary source for the lexical and verse data the programme works with. Hebrew and Greek term data — Strong's numbers, glosses, meaning parses, verse references — originate in STEP Bible, a peer-maintained scholarly resource for biblical-language analysis. The extraction pipeline reads STEP and writes the programme's copy into the DB; STEP remains the primary source to which every term record and verse reference traces back. The database holds what the programme has verified, classified, and analysed; it does not replace the source it draws from.

The database is not the programme's runtime log. Operational state — engine runs, checkpoints, per-word run history — lives in separate tables (`engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log`) that record how processing proceeded, not what the programme found. The data architecture described in this chapter concerns what the programme knows, not what the programme did operationally.

Shared types across the data architecture are held in controlled-vocabulary tables. `wa_vocab_set` names each set (phase codes, status values, crosslink types, and the others); `wa_vocab_member` carries the allowed values within each set. Columns elsewhere in the schema reference these values so that a term's status, a finding's lifecycle, or a link's type is drawn from a fixed controlled list rather than free text. The controlled-vocabulary layer is the scaffolding that keeps meaning consistent across tables that are otherwise structurally independent.

The sub-sections that follow describe what is in the database. Each sub-section takes one layer of the architecture — the registry, the terms, the verses, the context layer, the anchor-verse mechanism, the dimensional evidence, the question catalogue and findings, the synthesis bridge, and the prose store — and states what the layer holds and how its tables are related. The reader who finishes this chapter has the full vocabulary to read the programme's database state at any point and understand what each row means.

---
