# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 30 -->
<!-- PROSE_SECTION_TYPE: prog_data_synthesis -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: The synthesis bridge — from per-word records to cross-registry work -->
<!-- PROSE_SORT_ORDER: 30 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch4-obslog-v1_0-20260423.md -->

## The synthesis bridge — from per-word records to cross-registry work

The architecture holds two mechanisms for crossing registry boundaries. The first is explicit cross-word relationships — records in `wa_cross_registry_links` that name the connection between two registry words. The second is the SD pointer mechanism — cross-registry observations raised during Session B that cannot be resolved within a single registry and are carried forward to Session D for investigation. Together they are the bridge from the programme's per-word analytical work to cross-registry synthesis.

`wa_cross_registry_links` carries one hundred and fifty-eight rows, each recording an identified cross-word relationship. Fields: the `file_id` that originated the link, the linked word and its registry (`linked_word`, `linked_registry_id`), the type of connection (`connection_type_id` as FK to `wa_crosslink_type`), the connecting term that expresses the relationship, a free-form note, and a last-changed timestamp. The connection-type vocabulary is held in `wa_crosslink_type` — eleven types with unique codes and descriptions. The connection types are the programme's controlled set of answer categories to the question "how is this word related to that word" — shared term, root family, semantic adjacency, and the other relationships the programme has identified in the work to date.

The principal bridge from per-word Session B work to cross-registry Session D work is the SD pointer. An SD pointer is a row in `wa_session_research_flags` with `flag_code = 'SD_POINTER'`. Each pointer names a specific cross-registry observation that arose during Session B analysis for a registry word — a verse-level co-occurrence with another registry that suggests a structural inner-being relationship, a root-family connection that crosses a registry boundary, a dimensional pattern appearing in an unexpected cross-cluster combination, or a researcher-identified structural observation. The row records the registry that raised the pointer (`registry_id`), the partner registry where determinable (`cross_registry_id`), the pointer's priority (`HIGH` / `MEDIUM` / `LOW`), a flag label in the form `DIM-[nnn]-SD[nnn]`, the full analytical description, the Session B instruction version that produced it, and the raised date. `resolved` is 0 until Session D investigates and closes the pointer; `resolved_date` and `resolved_note` are populated when it does.

SD pointers are questions, not answers. Session B raises the pointer with precision but does not resolve it, because the data required to resolve it is not in a single registry's record. Session D begins with the accumulated pointer record, groups the pointers by theme and partner registry, formulates the investigation questions they pose, requests the cross-registry data those questions require, and produces the synthesis findings that answer them. The boundary is absolute: Session B does not answer cross-registry questions, and Session D does not raise them without a pointer.

The current pointer state concentrates in one cluster. As of April 2026, ninety-four SD pointers have been raised across the compassion, mercy, and grace registries — forty-three at `HIGH` priority, forty at `MEDIUM`, eleven at `LOW`. No other cluster yet has pointer density sufficient to support a meaningful Session D investigation. The threshold is not programme completion; Session D can run against a thematic cluster as soon as three to five of its registries have reached analytical completeness with HIGH-priority pointers accumulated against them, and the researcher declares the run.

Four further tables hold the programme's design intent for Session D output. `session_d_runs` will record each Session D investigation — its run identifier, date, cluster reference, registries in scope, registries that had reached completion at the time of the run, the Session B sources read, a run summary, and a JSON filename. `session_d_observations` will carry the structural observations the run produces — observation identifier, observation type, registries and terms implicated, structural note, source references, and a gate marker that records the evidential threshold the observation meets. `session_d_term_links` will record term-level cross-registry links identified during the run; `session_d_verse_links` will record verse-level cross-registry links, with the overlap count and a threshold-met flag for patterns that meet a significance criterion. All four tables are currently empty. They hold the schema for Session D output; the output itself begins to accumulate when the first Session D run executes.

Session D synthesis does not produce the cross-registry answer as a single finding. It produces a synthesis document, an accumulation of observations, and a set of cross-registry links that together name the patterns the investigation found. The synthesis document itself is prose — and that prose lives in the prose store described in the next sub-section, under the `session_d` source stage.

---
