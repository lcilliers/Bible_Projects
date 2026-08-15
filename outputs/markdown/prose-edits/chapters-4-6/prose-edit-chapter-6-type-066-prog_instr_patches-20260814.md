# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 41 -->
<!-- PROSE_SECTION_TYPE: prog_instr_patches -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Patches -->
<!-- PROSE_SORT_ORDER: 113 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch6-bodies-v1_0-20260423.md -->

## Patches

The patches instruction is the method instruction for one of the programme's two mechanisms for changing the database. A patch is a structured JSON object with a defined shape: a `_patch_meta` header carrying identity and provenance, an `operations` array of typed operations against named tables, and a `_patch_summary` footer recording operation counts. The instruction is the authoritative reference for the shape, the allowed operation types, the filename and patch-id conventions, the self-check Claude AI runs before submission, and the completion confirmation Claude Code returns on apply.

A patch is used when the change is fully specified in data terms: the affected fields are known, the foreign keys to match on are known, and the table structure accepts the operation as written. The patch captures everything the applicator needs to execute without further interpretation.

Operations cover the full range of analytical writes: verse-context classification, pre-analysis and analysis-complete updates for Session B, dimension assignments, catalogue population, prose section inserts and supersedes, rules and addenda updates, and the REPAIR operations for cascading resets. The instruction also covers failure-patch mechanics, the supersede-only discipline on narrative prose, and the physical-delete prohibition.

Patches are authored by Claude AI, reviewed by the researcher, and applied by Claude Code. No patch reaches the database without explicit researcher approval. The patches instruction sits alongside the directive instruction as the second of the two formal change channels.

---
