# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 23 -->
<!-- PROSE_SECTION_TYPE: prog_data_registry -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The registry -->
<!-- PROSE_SORT_ORDER: 23 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch4-obslog-v1_0-20260423.md -->

## The registry

The registry is the database's expression of the programme's scope. `word_registry` carries two hundred and fourteen rows, one for each English-language entry that the programme treats as in scope. Every layer described in the sub-sections that follow is anchored to the registry: a term belongs to a registry, a verse record is read through a term that belongs to a registry, a dimension is identified against a registry, a finding is raised against a registry. How the registry was composed — the four-stage construction from the inner-being definition — is described in the Chapter 2 sub-section on word selection.

A registry row carries what the programme knows about a word as an entry in the corpus. The core fields identify the word: `no` (the registry number assigned to it), `word` (the English headword), `source_list` (where it came from during registry construction), `category_hint`, `description`, `origin`, and `inference_note`. The processing fields track its passage through the programme's phases: `phase1_status`, `phase1_term_count`, `phase1_verse_count`, `verse_context_status`, `dim_review_status`, `dim_review_version`, `session_b_status`, and the automation-tracking fields (`automation_eligible`, `last_automation_run`, `automation_run_id`). The analytical fields accumulate what the work on the word has produced: `unique_term_count`, `shared_term_count`, `term_sharing_ratio`, `sb_classification`, `sb_classification_reasoning`, `carry_forward`, `word_synopsis`. A single row, read end-to-end, is a summary of a word's state in the programme at the moment the row is read.

The registry row is the atomic unit of research. The programme works word by word: a word is selected for a phase, the phase runs against that word, the row's phase fields update, the next phase opens against it. Every finding the programme produces is a finding about a word in the registry; every verse the programme classifies is classified through a term that belongs to a registry word. The registry is the seam at which the scope definition and the analytical work meet.

The registry carries an operational grouping in the `cluster_assignment` field. Values are drawn from the set C01 through C22 — the run-batch tranches the programme uses to schedule Verse Context processing across the registry. The tranches are administrative: they group words so that batches of manageable size can be run through the pipeline in sequence. They are not analytical. What the registry words analytically have in common — how their inner-being characteristics relate, what dimensional patterns they share, which words group together on the evidence — is not what `cluster_assignment` records. That work is the subject of the sub-section on dimensions; the dimensional evidence is where the programme's analytical grouping lives.

Alongside the registry, the database holds a per-word file index. `wa_file_index` carries two hundred and six rows that track the processing files produced against the registry: each row carries a filename, the owning registry (`registry_id` as FK to `word_registry.id`), the phase the file belongs to, the date produced, the translation used, and specification notes. Files are part-numbered where they are split, and the index records which parts exist and which are still to come. The file index is the record of what artefacts exist for a word on the file system that the database governs; it is how the programme keeps track of the physical outputs that each phase of work on a word produces.

The registry and the file index together hold the programme's answer to two questions about any word: is it in scope, and what state is it in. Everything the rest of this chapter describes is a layer that hangs from this one.

---
