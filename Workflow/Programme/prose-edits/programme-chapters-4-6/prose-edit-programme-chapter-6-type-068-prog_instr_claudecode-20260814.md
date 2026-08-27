# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 43 -->
<!-- PROSE_SECTION_TYPE: prog_instr_claudecode -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Claude Code operating guide -->
<!-- PROSE_SORT_ORDER: 115 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch6-bodies-v1_0-20260423.md -->

## Claude Code operating guide

The Claude Code operating guide is the method instruction for Claude Code itself. It describes CC's role — executor of patches and directives, operator of the database, producer of extracts, runner of the engine and supporting scripts — and the operational routines CC performs across the pipeline.

The guide covers the data-foundation pipeline: the registration of new words, the extraction of STEP Bible data, the `audit_word` reconciliation step, and the JSON export workflow that produces the complete word data files Session B works from. It covers schema and implementation tasks, programme-state queries from CC's side, engine and script status reporting, Verse Context operations from CC's perspective including batch construction and anchor integrity, and the re-run mechanisms the programme uses when upstream data changes (the STALE_TERM mechanism and its companions). It also carries the running record of recurring anomaly resolutions.

Where the patches and directives instructions define what Claude AI asks CC to do, this guide defines what CC does with what it receives — how it validates, how it executes, how it reports back. The three documents together cover the CAI-to-CC interaction completely: patches and directives for the ask, this guide for the execution.

The guide does not restate the patch or directive format; it points to those documents. Its own authority is confined to CC's operational behaviour.

---
