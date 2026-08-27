# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 24 -->
<!-- PROSE_SECTION_TYPE: prog_data_terms -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Terms -->
<!-- PROSE_SORT_ORDER: 24 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch4-obslog-v1_0-20260423.md -->

## Terms

The database's term layer holds the Hebrew, Greek, and Aramaic words that the programme's registry words are built from. Where a registry word is an English entry, a term is the original-language lexical unit: a Strong's number, a transliteration, a gloss, and the morphological and semantic detail that carries the term's meaning in Scripture.

Two tables hold the term data, and their relationship matters for how the rest of the architecture is read. `mti_terms` is the canonical term index — seven thousand five hundred and seventy-one rows, each a unique term identified as belonging to a registry word. Its core fields identify the term (`strongs_number`, `transliteration`, `gloss`, `language`) and anchor it to a registry (`owning_registry`, `owning_registry_fk` as FK to `word_registry.id`, `owning_word`, `owning_part`). The remaining fields carry the term's analytical state: `status` (the term's place in the lifecycle), `exclusion_reason` (where the term has been ruled out), `strongs_reconciled` (whether the Strong's number has been reviewed for suffix and spelling variants), `anchor_note` (where the term functions as an anchor for verse-context classification), `extraction_date`, `last_changed`, and `delete_flagged` for soft-delete. The owning-registry mechanism — one term, one owning registry — is the foundation for the cross-registry reference architecture described in the next sub-section.

`wa_term_inventory` is the extraction-time term record — seven thousand five hundred and fifty rows that capture what STEP Bible returned when the phase-1 extraction pipeline ran against each registry's processing file. Its fields record the raw lexical detail: `step_search_gloss` and `word_analysis_gloss` (the programme's two gloss captures), `occurrence_count` and `occurrence_count_qualifier`, `meaning` and `meaning_numbered`, `also_spelled`, `lsj_entry`, `testament`, `causative_form_present`, `short_def_mounce`, and a set of fields tracking how the term came into the inventory (`evidential_status`, `retention_note`, `term_owner_type`, `term_introduction_source`, `term_introduction_rationale`, `term_introduction_date`). The inventory is tied through `file_id` to the processing file that produced it; each extraction run against a registry's file creates or updates the inventory rows for that file's terms.

The two layers exist because they answer different questions. `mti_terms` answers "what are the canonical terms for this registry?" `wa_term_inventory` answers "what did STEP return when we extracted this file?" Both are carried in the database because the programme preserves the raw extraction record alongside the curated canonical record. Their counts are close but not identical.

STEP Bible is the primary source for every term in both layers. Strong's numbers, transliterations, glosses, meaning text, and verse references all originate in STEP, the peer-maintained scholarly tool for Hebrew and Greek biblical analysis. The programme extracts from STEP, stores the result, and treats the stored copy as the working reference — but every claim in the term layer traces back to STEP, and STEP remains the authority to which term records are verified.

The programme parses STEP's meaning text into a structured sense hierarchy. `wa_meaning_parsed` holds one row per parsed term inventory entry (seven thousand four hundred and forty-nine rows) with summary counts — how many top-level senses, how many stems, whether a causative stem is present, whether domain tags were found, parse version and warnings. `wa_meaning_sense` holds the sense-tree nodes — fifteen thousand nine hundred and fifty-six rows — each carrying a `level_code`, a `level_depth`, a `parent_level_code`, the sense text, a sort order, and optional stem-label or domain-tag attributes. The tree structure means a term's senses can be read as the hierarchical object STEP presents, not as flat text. `wa_meaning_stem` carries stem-labelled aggregations where a term has Hebrew binyanim or equivalent verbal stems, with one row per distinct stem recording its name, type, and top sense. For Greek terms that have LSJ enrichment, `wa_lsj_parsed` carries the Liddell-Scott-Jones extract — raw LSJ text, a gloss, domain tags, philosophical and etymological notes, and cognate forms.

The associative term data is held in two further tables. `wa_term_related_words` records the related-word associations the programme has captured for each inventory term — gloss, transliteration, Strong's number, and a relationship note, with one hundred and one thousand nine hundred and seventy rows across the corpus. `wa_term_root_family` records root-family membership — the root code, the root language, and the root gloss — with two thousand eight hundred and sixty-one rows across the corpus. Both tables are term-inventory-scoped and both carry soft-delete.

Term-level flags are held in a parallel pair of tables because of the two term layers. `mti_term_flags` is a simple many-to-many link between `mti_terms.id` and `phase2_flag_types.id` — one thousand and five rows. `wa_term_phase2_flags` is the extraction-layer equivalent linking `wa_term_inventory.id` to the same flag types, but it carries additional detail — a description, the source of the flag, a raised date, and an obsolete-reason field — with one thousand five hundred and seventy rows. `phase2_flag_types` is the flag vocabulary, holding twenty-five flag codes and their descriptions.

The extraction record itself is logged in `term_fetch_log` — two thousand three hundred and seventeen rows tracking every STEP extraction run against the registry. Each row records what was requested, what came back (verse counts fetched, stored, filtered), which Strong's numbers were resolved or needed suffix reconciliation, and any API warnings. The log is the extraction provenance — the record of how the term data in the two term layers arrived in the database.

Every table in the term layer carries `delete_flagged` for soft-delete. A term that is set aside is not removed; its row stays in the database with the flag set, and the chain of related rows (meanings, related words, root families, flags) is also flag-set where appropriate. The governance discipline for soft-delete is the subject of a later chapter; its consequence for the term layer is that the term history is preserved across revisions. A term ruled out in one pass can be read back in a later pass; its reasons for exclusion are held in `exclusion_reason`; its evidential state is held in `evidential_status`.

---
