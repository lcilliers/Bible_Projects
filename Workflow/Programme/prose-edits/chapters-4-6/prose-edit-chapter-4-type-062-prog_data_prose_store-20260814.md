# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 31 -->
<!-- PROSE_SECTION_TYPE: prog_data_prose_store -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The prose store — phase-bridge architecture -->
<!-- PROSE_SORT_ORDER: 31 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch4-obslog-v1_0-20260423.md -->

## The prose store — phase-bridge architecture

The prose store is the programme's phase-bridge architecture. Each phase of the research has its own prose store — a set of records carrying the authoritative truth of that phase. When a word at any phase is reset and reworked, the prior phase's store remains as the record of what the truth was at that point; the new work produces a fresh store entry that supersedes or sits alongside the old. The programme's final reader-facing prose is produced from the last phase store, drawing on the accumulated truth of every phase that preceded it. This is the mechanism by which any word, at any phase, can be revisited without losing what the earlier work established.

The store is implemented on two tables and a small set of supporting structures. `prose_section_type` is the dictionary — thirty-four rows, each a stable named slot that prose can be written into. A row carries the `code` (the machine identifier, globally unique across all stages and chapters), a `label`, the `source_stage` it belongs to, an optional `lifecycle_tag` for staged rewrites, an optional `chapter_no`, a `description` telling the authoring session what the prose under this handle should cover, and optional expected-length guides (`expected_length_min`, `expected_length_max`). `sort_order` controls render order within a chapter or grouping.

`prose_section` is the content. Twenty rows are currently populated (preamble plus the three chapters of the programme corpus that have been drafted so far). Each row carries its `section_type_id` (the handle), a `registry_id` (NULL for programme-wide prose, an integer FK to `word_registry` for word-scoped prose), a `heading`, the `body` as the prose itself, a `word_count` derived at insert, and the lifecycle fields: `status`, `version`, `supersedes_id`, `superseded_by_id`, `author`, `created_at`, `approved_at`, `approved_by`, `metadata_json`, `source_file`, `delete_flagged`.

Five `source_stage` values partition the store into the five phase-stores the programme maintains. The `programme` stage holds the governance and orientation prose — the chapters of this corpus — scoped to `registry_id = NULL` because the prose is programme-wide. The `session_a` stage holds mechanical per-word extracts (synopsis, term inventory summary, verse coverage overview, lexical notes) authored by the operational agent from the structured data the database already contains. The `session_b` stage holds per-word analytical output — the six chapters of Session B Analysis for each registry word. The `session_c` stage holds reader-facing word studies in a three-version lifecycle: `v1` is the initial draft drawn from Session B findings, `v2` is the refinement after cross-registry context becomes available, `v3` is the final reader-facing version after researcher review. The `session_d` stage holds cross-registry synthesis prose — the synthesis documents that Session D runs produce, and which the programme's final account will draw from when the programme-level synthesis pass is declared.

The lifecycle discipline is supersede-only for narrative prose. Status moves through `draft`, `in_review`, `approved`, `archived`; a revision does not edit the existing row but creates a new row with `version = old.version + 1`, `supersedes_id = old.id`, and the old row's `superseded_by_id = new.id`. The row history is queryable end-to-end; no edit is ever silently lost. This is what makes the phase-bridge reset work: a word whose Session B is re-done does not overwrite the prior Session B prose — it produces a new `session_b` row that supersedes the old, and the old remains as the record of what Session B's answer was before the re-run. The one exception is the `session_a_replace` operation, which permits in-place update for mechanical Session A extracts because they are reproducible from the underlying data. Every other operation creates a new row.

Full-text search across the entire prose corpus is provided by `prose_section_fts`, an FTS5 virtual index kept in sync with `prose_section` by triggers. Phrase and proximity search runs across every row in every stage — a query for every passage that mentions a particular concept returns results from governance prose, Session B analyses, Session C word studies, and Session D syntheses in the same result set.

Two link tables connect the prose back to the evidence and the analytical output it rests on. `prose_section_dimension_link` records that a prose row discusses a dimension (a row in `wa_dimension_index`). This lets a dimensional synthesis pull every prose passage across the corpus that engages a given dimension, regardless of which stage the passage is in. `prose_section_finding_link` records that a prose row discusses a Session B finding. This lets a finding be traced to the prose that elaborates it — or a prose passage back to the findings it rests on. Both tables carry a `link_type` vocabulary.

The database is the prose store's canonical form. Files — markdown drafts for authoring, extracts in JSON / markdown / DOCX for reading — round-trip through the database but are not the authoritative source. A draft `.md` is the input; the PROSE patch reads it; the applicator writes it to the database; the extract is regenerated from the database. Between those endpoints, the database holds the truth. The principle that operationalises this architecture is the one recorded across the rest of this chapter: the database is the programme's analytical memory, not only its evidentiary substrate. The prose store is the piece that makes the interpretation survive session boundaries the way the evidence does.

At present the programme stage holds twenty-one populated prose rows across the preamble and the first three chapters; the four research-stage stores have their section types defined but no populated content yet. Session A prose will accumulate as the programme's mechanical per-word extracts are authored; Session B prose will accumulate as each registry completes its analysis; Session C prose will accumulate as the word studies are produced; Session D prose will accumulate when Session D runs execute. When the programme reaches its final synthesis pass, the prose store will hold the full accumulated truth of every phase for every word, and the reader-facing account the programme produces will draw on all of it.

---
