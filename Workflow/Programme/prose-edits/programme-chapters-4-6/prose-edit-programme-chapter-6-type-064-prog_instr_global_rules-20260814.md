# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 39 -->
<!-- PROSE_SECTION_TYPE: prog_instr_global_rules -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Global rules -->
<!-- PROSE_SORT_ORDER: 111 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch6-bodies-v1_0-20260423.md -->

## Global rules

The global rules document is the single file of programme-wide binding rules. It carries every rule that applies across sessions, phases, and instructions — file naming, cadence discipline, observations-log conduct, cross-document referencing, the two-AI division of responsibility, help-forward bounds, data-discipline requirements, and the rules governing session startup itself. Rules are identified by stable codes (GR-LOAD-001, GR-REF-001, GR-OBS-001, and so on) and are cited by code throughout the rest of the instruction corpus rather than restated.

The rules are held in the database in `wa_rule_registry`, with companion guidance in `wa_addendum_registry`. The working form is a JSON extract — `wa-global-rules-extract-{YYYYMMDD}.json` — regenerated from the database whenever rules change. A parallel markdown view is produced alongside the JSON for reading. Neither extract is itself the rules: the database is canonical.

The document is read in full at the start of every session before any other instruction, extract, or data file. This is the load gate that opens every piece of work the programme does; it is described in the rules themselves and not expanded on here. The rules extract is also the compliance reference point during work: any instruction's behaviour that conflicts with a rule resolves to the rule.

The global rules are the only document in the corpus that binds every other instruction; every other document in this chapter is governed by it.

---
