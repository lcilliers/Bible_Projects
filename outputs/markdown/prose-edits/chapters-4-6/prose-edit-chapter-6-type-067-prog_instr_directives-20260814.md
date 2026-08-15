# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 42 -->
<!-- PROSE_SECTION_TYPE: prog_instr_directives -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Directives -->
<!-- PROSE_SORT_ORDER: 114 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch6-bodies-v1_0-20260423.md -->

## Directives

The directives instruction is the method instruction for the second mechanism for changing the database. A directive is a plain-language instruction with five required elements: a title and identifier, a statement of what is to be done and why, a specification of the operations the directive asks Claude Code to perform, a definition of the expected outcome, and the confirmation Claude Code is to return. The instruction covers the five-element format, the filename convention, the self-check before submission, and the completion confirmation protocol.

A directive is used when the change cannot be captured adequately in a JSON patch — typically because it requires reasoning, script execution, or schema preparation that a declarative operation list cannot express. Schema enablement sits here exclusively: before a class of patches can apply against a constraint the current schema does not permit (such as the `registry_id NOT NULL` relaxation that programme-wide prose required), a directive prepares the schema and a patch then carries the data.

The directives instruction and the patches instruction are equal peers: between them, they cover every database-change operation the programme uses. Either document is authoritative within its own scope; together they are the exhaustive set. Directives, like patches, are authored by Claude AI, reviewed by the researcher, and executed by Claude Code — no directive reaches the database without approval.

---
