# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 40 -->
<!-- PROSE_SECTION_TYPE: prog_instr_reference -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Reference -->
<!-- PROSE_SORT_ORDER: 112 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch6-bodies-v1_0-20260423.md -->

## Reference

The reference is the programme's dictionary. It holds the controlled vocabularies that the database and the instructions use — dimension labels, confidence tiers, status values, resolution paths, patch types, classification outcomes — together with the schema field definitions, file-naming rule extensions, and cross-cutting lookups that the rest of the corpus points to when a vocabulary question arises.

The content lives in the database: vocabulary in `wa_vocab_set` and `wa_vocab_member`; schema definitions in the schema tables themselves; naming extensions alongside the file-naming rules. The working form is a JSON snapshot — `wa-reference-snapshot-{YYYYMMDD}.json` — regenerated when any of the underlying tables change. As with the rules, the database is canonical and the snapshot is the live read.

Any controlled-vocabulary value, any field definition, any file-naming clarification that an instruction needs is pointed at the reference rather than restated in the referring instruction. This concentration keeps vocabulary drift impossible: when a dimension label is revised, the change happens in one place and every instruction that uses the label resolves to the revised value without any document-by-document update.

The reference is loaded at session start after the rules. Together, the rules and the reference are the two documents that define what the programme's instructions mean; the rest of the corpus is written on the assumption that both are available and current.

---
