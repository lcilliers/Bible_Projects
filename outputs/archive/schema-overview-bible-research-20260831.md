# bible_research — schema overview

_Generated from the DBSchema register (`database/bible_research.db`, schema 3.40.0, register captured 2026-08-31). Escalation #1306._

**113 tables · 1,216 columns · 110 PK columns · 75 FKs · 11 checks · 168 indexes · 5 triggers · 2 views**

> ⚠ 3 table(s) and 45 column(s) still undescribed — see the flagged section at the end.

## Tables

| table | description | rows | cols | PK | FKs | idx |
|---|---|---:|---:|---|---:|---:|
| `book_code_variants` | Alias table mapping the many book abbreviation forms encountered in source data onto a single books row, so that '1Chr', '1Ki' and '1Kgs'... | 112 | 2 | code | 1 | 1 |
| `books` | The 66 books of the Bible as canonical reference data: name, testament, canonical order and several code forms used to parse and render v... | 66 | 9 | id | 0 | 4 |
| `characteristic` | The named characteristics belonging to each cluster — the distinct inner-being traits a cluster resolves into, each with a definition. 27... | 277 | 11 | id | 0 | 3 |
| `characteristic_subgroup` | The many-to-many join between a characteristic and the cluster sub-groups that carry it, recording why the pairing holds. In practice it ... | 146 | 9 | id | 2 | 3 |
| `cluster` | The 49 top-level thematic groupings of the study (47 M-codes plus FLAG and T2), each naming a domain of the inner life such as Anger, Wis... | 49 | 10 | cluster_code | 0 | 1 |
| `cluster_finding` | The catalogue-prompted findings layer: one row per observation question asked of a cluster (or of a characteristic, sub-group or verse-co... | 19,997 | 16 | id | 4 | 1 |
| `cluster_observation` | Write-on-discovery notes made while working a cluster — design rationales, verdicts, synthesis notes and carry-forwards — each addressed ... | 276 | 17 | id | 2 | 3 |
| `cluster_subgroup` | Sub-divisions of a cluster (for example M01-A, M01-BOUNDARY), each carrying a label and a core description that scopes which sense of the... | 175 | 13 | id | 1 | 2 |
| `engine_run_log` | One row per engine or patch execution (875 rows, March to July), recording mode, timing, outcome and roll-up counts of what was written. ... | 890 | 17 | id | 0 | 1 |
| `engine_stream_checkpoint` | Per-stream progress within a run (1,948 rows over 347 runs) — a stream is usually a single term, e.g. 'term:H8637'. It exists to allow re... | 1,948 | 11 | id | 1 | 0 |
| `finding` | The universal finding store: one row per typed analytical finding, at VERSE, CLUSTER or GLOBAL level, with VERSE dominating (over 430k of... | 458,096 | 20 | id | 0 | 5 |
| `finding_citation` | Extracted citations found inside cluster-level narrative text — the pointer that a given cluster_finding or cluster_observation quotes a ... | 51,148 | 8 | id | 0 | 3 |
| `finding_question_link` | Joins findings to the observation questions in wa_obs_question_catalogue that they answer — the mechanism by which the question catalogue... | 357,657 | 13 | id | 0 | 2 |
| `finding_revision` | Declared as a field-level audit trail for changes to findings — recording which field moved from what value to what, why, and by whom — b... | 0 | 9 | id | 0 | 1 |
| `finding_verse_index` | _(undescribed)_ | 475,790 | 6 | id | 0 | 0 |
| `finding_verse_link` | Links findings to the verses they rest on, distinguishing the anchor verse from supporting ones. The table is small and lopsided: 3,586 o... | 3,659 | 7 | id | 0 | 2 |
| `ib_characteristic` | The live meaning-keyed inner-being characteristic index: one row per distinct sense of a Hebrew term as read in a book, keyed on lemma pl... | 1,634 | 29 | id | 0 | 1 |
| `ib_characteristic_legacy` | The superseded 29-row inner-being characteristic registry from 2026-07-03, retained as a backup after ib_characteristic was rebuilt on a ... | 29 | 22 | — | 0 | 0 |
| `ib_observation` | A small transitional store of 81 observations from the fan-out reads of nine focus verses (chiefly Lev 25:43, Exo 1:13 and Gen 6:5), each... | 81 | 13 | id | 0 | 0 |
| `lemma_faculty_map` | Maps 1,717 Strong's lemmas to the inner-being faculty or faculties they engage (affect, cognition, volition, moral evaluation and combina... | 1,717 | 6 | strongs_number | 0 | 1 |
| `lexicon` | A flat reference lexicon of 11,666 Strong's entries harvested wholesale from STEP on 2026-06-16 — original-script lemma, transliteration,... | 11,666 | 9 | strong | 0 | 1 |
| `mti_term_cross_refs` | Records the registry words that reference a term other than its owning one — the XREF side of term ownership, held as a junction between ... | 462 | 7 | id | 2 | 3 |
| `mti_term_flags` | Junction attaching Phase 2 triage flags from phase2_flag_types to terms in mti_terms; 1,005 assignments across 785 terms. In practice it ... | 1,005 | 2 | mti_term_id, flag_id | 2 | 1 |
| `mti_term_subgroup` | The many-to-many placement of terms into cluster sub-groups, replacing the old single-valued column on mti_terms. 1,196 placements over 7... | 1,196 | 7 | id | 2 | 3 |
| `mti_terms` | The master term index: one row per Hebrew/Greek/Aramaic term drawn into the study, carrying the term's identity (Strong's, transliteratio... | 7,861 | 24 | id | 1 | 1 |
| `passage` | The passage register (4,296 rows): a passage is a maximal run of consecutive verses forming the reading unit, anchored on its first verse... | 4,296 | 13 | id | 0 | 0 |
| `phase2_flag_types` | Lookup of the 25 Phase 2 flag codes an analyst may raise against a term, each with a prose definition of when it applies — e.g. thin data... | 25 | 3 | id | 0 | 1 |
| `prose_section` | The DB-canonical store of authored prose: one row per titled section of narrative — chapter readings, cluster essays, synthesis passages ... | 949 | 18 | id | 2 | 5 |
| `prose_section_dimension_link` | Declared as a many-to-many link between prose sections and dimensions, with a link_type qualifying the relationship, but it holds 0 rows.... | 0 | 4 | prose_section_id, dimension_id, link_type | 1 | 1 |
| `prose_section_finding_link` | Declared as a many-to-many link between prose sections and findings, so that a passage could be traced to the evidence behind it, but it ... | 0 | 4 | prose_section_id, finding_id, link_type | 2 | 1 |
| `prose_section_fts` | An SQLite FTS5 virtual table providing full-text search over prose_section. Its columns mirror the source table one-for-one and hold no i... | 949 | 7 | — | 0 | 0 |
| `prose_section_fts_config` | An FTS5-managed shadow table holding the configuration of the prose_section_fts index as key/value pairs. It is internal machinery writte... | 1 | 2 | k | 0 | 1 |
| `prose_section_fts_content` | An FTS5-managed shadow table storing the raw column values of each indexed row, so the virtual table can return original text and support... | 949 | 8 | id | 0 | 0 |
| `prose_section_fts_data` | An FTS5-managed shadow table holding the inverted index itself as opaque binary segment blobs. It is SQLite internal machinery — the cont... | 1,097 | 2 | id | 0 | 0 |
| `prose_section_fts_docsize` | An FTS5-managed shadow table recording, per indexed document, the token count of each column in a packed binary form. FTS5 uses it for re... | 949 | 2 | id | 0 | 0 |
| `prose_section_fts_idx` | An FTS5-managed shadow table mapping index segments and term prefixes to the pages within prose_section_fts_data where their postings liv... | 845 | 3 | segid, term | 0 | 1 |
| `prose_section_type` | The controlled vocabulary of prose section kinds — 108 codes spanning programme documentation, per-session outputs, cluster findings and ... | 108 | 18 | id | 0 | 2 |
| `prose_section_verse_link` | _(undescribed)_ | 0 | 4 | prose_section_id, verse_reference, link_type | 1 | 1 |
| `record_change_log` | _(undescribed)_ | 1,242 | 10 | id | 0 | 1 |
| `reread_worklist` | The chapter-by-chapter worklist for the Psalms re-read, one row per chapter with the gate counts recorded at completion. It is single-pur... | 150 | 12 | id | 0 | 1 |
| `schema_version` | Migration ledger: one row per schema version applied to the database, each carrying the cumulative migration history as JSON. 16 rows spa... | 16 | 5 | id | 0 | 0 |
| `segment_unit` | Reading segments above the verse: 877 named units of text (a thread, discourse or scene) each summarised by the characteristics it carrie... | 877 | 13 | id | 0 | 1 |
| `segment_unit_verse` | The membership junction resolving each segment_unit to its verses (11,276 rows over 877 units and 10,330 distinct verses). Verses can bel... | 11,276 | 4 | unit_id, verse_id | 0 | 2 |
| `session_d_observations` | Declared and never used: 0 rows. Part of the four-table Session D scaffolding, intended to hold observations raised by a Session D run (t... | 0 | 11 | id | 0 | 1 |
| `session_d_runs` | Declared and never used: 0 rows. Intended as the header table for Session D runs (one row per run, with its cluster and registry scope), ... | 0 | 9 | id | 0 | 1 |
| `session_d_term_links` | Declared and never used: 0 rows. Intended to record the terms a Session D run implicated, together with a divergence marker between the t... | 0 | 8 | id | 0 | 0 |
| `session_d_verse_links` | Declared and never used: 0 rows. Intended to record verses where several Session D registries overlapped, with an overlap count tested ag... | 0 | 9 | id | 0 | 0 |
| `sources` | Declared to hold bibliographic sources keyed to Zotero, but it has 0 rows — it was created and never used. No secondary-literature citati... | 0 | 6 | id | 0 | 1 |
| `term_collection_lexical` | Holds collection-level lexical judgements about a term — properties asserted of the term across its whole verse set rather than in any on... | 1,081 | 11 | id | 0 | 0 |
| `term_fetch_log` | Per-Strong's-number record of STEP API fetches (2,377 rows), showing what was requested, what it resolved to, and how many verses came ba... | 2,377 | 14 | id | 1 | 0 |
| `themes` | Declared as a lookup of thematic labels but has 0 rows — created and never used. Nothing in the live model links to it; theme-like groupi... | 0 | 3 | id | 0 | 1 |
| `vcg_term` | The many-to-many link between verse-context groups and terms, replacing the old single mti_term_id column on verse_context_group. Notably... | 5,091 | 7 | id | 2 | 3 |
| `ve_dimension_scoreboard` | The rule-validation scoreboard for the 18 VE-lexical dimensions (ve_nr 101-118), holding each dimension's rule, its validation verdict an... | 18 | 8 | ve_nr | 0 | 0 |
| `ve_lexical` | The live lexical-analysis store: one row per analytical item read off a verse, keyed to a verse span and a dimension number (ve_nr 101-11... | 620,151 | 17 | id | 2 | 3 |
| `ve_lexical_divinv_pre_reverse_20260626` | A snapshot of 860 divine-involvement items (ve_nr 8, tier T0.1.2) produced by the divine_involvement_read_api pass on 2026-06-16, taken b... | 860 | 10 | — | 0 | 0 |
| `ve_lexical_divinv_roles_premap_20260626` | A snapshot of 5,187 divine-involvement items (ve_nr 8) taken before the 2026-06-26 remap collapsed them. Comparing it against ve_lexical_... | 5,187 | 10 | — | 0 | 0 |
| `ve_lexical_faculty_backup` | A snapshot of 29,031 faculty items (ve_nr 7, tier T3) as produced by the v2_engine_iter1 run and dated 2026-06-16, holding the engine's t... | 29,031 | 10 | — | 0 | 0 |
| `ve_lexical_faculty_pre_reset_20260626` | A snapshot of all 29,203 faculty items (ve_nr 7) as they stood immediately before the 2026-06-26 faculty reset. Every id still resolves i... | 29,203 | 10 | — | 0 | 0 |
| `ve_lexical_faculty_seat_reverse_20260626` | A snapshot of 1,492 faculty items created on 2026-06-26 by the inferred-seat rule, which assigned a faculty by reading faculty-words else... | 1,492 | 10 | — | 0 | 0 |
| `ve_lexical_legacy` | The previous generation of the lexical store, retired at the 2026-07-02 cutover and kept whole. 507,651 rows, ids 2351222 to 7123084 (no ... | 507,651 | 17 | id | 2 | 0 |
| `ve_lexical_objtype_premap_20260626` | A snapshot of 9,534 object-type items (ve_nr 16) taken before the 2026-06-26 remap. The comparison against ve_lexical_legacy is unambiguo... | 9,534 | 10 | — | 0 | 0 |
| `ve_lexical_origin_quarantine_20260626` | A snapshot of 3,623 origin items (ve_nr 6, tier T2.9.1) quarantined on 2026-06-26. Every row is identical: the value 'received-from-outsi... | 3,623 | 10 | — | 0 | 0 |
| `ve_lexical_overlay_reverse_20260626` | A snapshot of 1,387 items reversed on 2026-06-26, mixing two dimensions: object-type (ve_nr 16, 1,128 rows) and cause (ve_nr 17, 259 rows... | 1,387 | 10 | — | 0 | 0 |
| `ve_lexical_valence_quarantine_20260626` | A snapshot of 26,993 valence items (ve_nr 21, tier T0.3.1) quarantined on 2026-06-26 — the largest withdrawal recorded in this group. All... | 26,993 | 10 | — | 0 | 0 |
| `ve_lexical_verification` | A small manual verification log: 46 hand-checked ve_lexical items, all of dimension 101 (sense) and all checked on 2026-07-14, recording ... | 46 | 11 | id | 0 | 1 |
| `ve_verification_sample` | The drawn sampling frame for verifying the lexical layer: 3,332 (ve_nr, verse_span_id) pairs selected across 18 dimensions from Psalms (b... | 3,332 | 4 | ve_nr, verse_span_id | 0 | 1 |
| `verse` | The master verse table and the anchor of the whole verse layer: one row per verse of the ESV text (25,634 rows, all 66 books), each with ... | 25,634 | 13 | id | 0 | 4 |
| `verse_analysis_progress` | A 33-row scratch tracker for the fan-out reading of a small researcher-curated verse set (fear-of-God versus oppression of the dependent)... | 33 | 10 | id | 0 | 0 |
| `verse_context` | The term-in-verse classification record (55,775 rows): for one verse-record and one MTI term it holds whether that occurrence is relevant... | 55,775 | 24 | id | 4 | 3 |
| `verse_context_group` | The catalogue of verse-context groups (VCGs) — named groupings of term-in-verse occurrences that share a context, referenced by verse_con... | 4,155 | 5 | id | 0 | 1 |
| `verse_coverage` | A derived, materialised roll-up of study coverage per verse — how many spans, study terms and lexical units each verse carries, and wheth... | 23,593 | 11 | verse_id | 0 | 0 |
| `verse_coverage_morphology` | A per-word morphology extract for a narrow set of verses — 2,877 word rows covering only 326 distinct references, concentrated in Levitic... | 2,877 | 8 | id | 0 | 0 |
| `verse_evidence_index` | The fan-in index that answers 'what evidence is bound to this verse' — 804,805 rows mapping a verse to each piece of evidence held agains... | 804,805 | 5 | — | 0 | 2 |
| `verse_evidence_orphan` | The reject log of the verse_evidence_index build: 222 evidence rows that could not be bound to a verse. Every row has the same single cau... | 222 | 3 | — | 0 | 0 |
| `verse_morph_complexity` | A derived per-verse syntactic complexity profile counting content words, finite and non-finite verbs, conjunctions, prepositions and subo... | 23,593 | 10 | verse_id | 0 | 0 |
| `verse_morphology` | The morphological backbone of the layer: one row per word of every verse (325,507 rows), carrying the surface form, Strong's tag, morph_c... | 325,507 | 13 | id | 1 | 3 |
| `verse_morphology_raw` | The raw STEP HTML behind the parsed morphology — one row per verse (25,634, i.e. complete cover of the master verse table), kept so the p... | 25,634 | 3 | verse_id | 1 | 0 |
| `verse_span_index` | The working analytical surface over word spans (325,474 rows): it reproduces verse_morphology's columns almost exactly and adds the analy... | 325,474 | 22 | id | 0 | 2 |
| `verse_term_index` | A minimal derived lookup of which Strong's terms appear in which verse (275,593 rows, no primary key, indexed both ways). It is a de-dupl... | 275,593 | 2 | — | 0 | 2 |
| `wa_addendum_registry` | A one-off audit artefact: 22 observations from the April 2026 global-rules audit, each recording a problem with a rule and where its cont... | 22 | 15 | id | 0 | 2 |
| `wa_cross_registry_links` | 158 researcher-authored links between registry words, each naming the connecting Hebrew or Greek term and explaining the connection in pr... | 158 | 8 | id | 3 | 2 |
| `wa_crosslink_type` | The 11 kinds of relationship that may connect two registry words, e.g. shared root, semantic opposition, causative chain. It is the contr... | 11 | 3 | id | 0 | 1 |
| `wa_data_quality_flags` | Engine-derived data-quality evidence raised against a term in a word-study file (19,866 rows) — automated observations such as thin verse... | 0 | 9 | id | 1 | 0 |
| `wa_dim_review_cluster_log` | A completion log for the retired dimension review: one row per C-code cluster finished, six in all (C10, C13, C17, C20, C21, C22), record... | 6 | 9 | id | 0 | 1 |
| `wa_dimension_index` | The retired dimension-review layer: 3,509 rows, one per verse_context_group, recording which of 20 named dimensions the group was assigne... | 3,509 | 15 | id | 1 | 5 |
| `wa_file_index` | One row per input file (or engine onboarding stub) that supplied a registry word's data, with the file's provenance, split-part structure... | 308 | 20 | id | 1 | 3 |
| `wa_file_name_pattern` | The 23 registered filename conventions used across the programme, each given as a template such as 'wa-dim-{cluster}-extract-{YYYYMMDD}.j... | 23 | 10 | id | 0 | 1 |
| `wa_finding_catalogue_links` | The legacy mapping of Session B findings to catalogue questions, with a coverage judgement and a note on what the finding contributed. It... | 6,199 | 11 | id | 2 | 1 |
| `wa_finding_entity_links` | A legacy link from Session B findings to the verses or verse-context groups they attach to, superseded by finding_verse_link under the li... | 287 | 7 | id | 1 | 2 |
| `wa_flag_type_question_link` | Maps quality-flag types to the catalogue questions that a raised flag should prompt, so that a data-quality signal pulls in the right ana... | 12 | 6 | id | 2 | 3 |
| `wa_label_pattern` | The 11 registered identifier formats used for labels rather than filenames — finding ids, flag ids, patch ids, group codes — each mapped ... | 11 | 10 | id | 0 | 1 |
| `wa_lsj_parsed` | Structured parse of the Liddell-Scott-Jones classical Greek lexicon entry for a term, splitting the raw entry into gloss, domains, and ph... | 9 | 10 | id | 1 | 2 |
| `wa_meaning_parsed` | One header row per inventory term for its parsed definition, holding the counts and derived flags of the parse whose detail lives in wa_m... | 7,748 | 11 | id | 1 | 2 |
| `wa_meaning_sense` | The parsed sense hierarchy of a term's definition: 17,125 rows, one per numbered sense, keyed to wa_meaning_parsed and ordered by the sou... | 17,125 | 11 | id | 1 | 2 |
| `wa_meaning_stem` | Breaks a Hebrew verb's definition down by verbal stem (Qal, Piel, Hiphil and so on) with the sense each stem carries. Effectively unused:... | 13 | 6 | id | 1 | 1 |
| `wa_obs_question_catalogue` | The observation question catalogue: 424 prompts that drive analysis, organised by tier and component, each with its text, scope, provenan... | 424 | 17 | obs_id | 1 | 1 |
| `wa_patch_type_registry` | The 20 recognised JSON patch types, each naming the instruction that governs it and the tables it writes to — the reference-as-database r... | 20 | 10 | id | 0 | 1 |
| `wa_prose_section_citations` | Records which evidence a given prose section cites — a finding, a Q&A catalogue link, an SD pointer, or an observation sequence — togethe... | 562 | 10 | id | 4 | 4 |
| `wa_quality_flag_types` | Lookup of the 29 data-quality and research flag codes, grouped by kind and each defined in prose. Unlike phase2_flag_types it carries a d... | 3 | 8 | id | 0 | 1 |
| `wa_rule_registry` | The programme's global rules held as data: 59 rules with their text, rationale, application notes and supersession chain, all imported fr... | 59 | 19 | id | 0 | 2 |
| `wa_session_b_dimensions` | A near-empty remnant of the Session B per-word dimensional assessment: just 2 rows, for registries 112 and 182, raised on 27 and 28 March... | 2 | 13 | id | 0 | 0 |
| `wa_session_b_findings` | The superseded per-word Session B findings store: 2,883 findings raised April to May 2026 across 112 registries, since replaced by the un... | 2,883 | 27 | id | 1 | 1 |
| `wa_session_research_flags` | Researcher-facing pointers and findings raised during analysis (715 rows) — a working queue of things to return to, with routing (session... | 715 | 17 | id | 3 | 3 |
| `wa_term_inventory` | The per-registry term inventory: one row per term as held under a given English word's file, carrying the STEP-sourced identity, gloss, m... | 7,844 | 27 | id | 1 | 8 |
| `wa_term_phase2_flags` | Junction attaching Phase 2 triage flags from phase2_flag_types to inventory terms: 1,570 assignments over 883 terms, using 25 distinct fl... | 1,570 | 7 | term_inv_id, flag_id | 2 | 1 |
| `wa_term_related_words` | The related-word web: 103,944 rows attaching each inventory term to other lemmas STEP reports as related, by gloss, transliteration and S... | 103,944 | 7 | id | 1 | 1 |
| `wa_term_root_family` | Assigns inventory terms to a shared etymological root family by root code, so terms from one root (e.g. CHARAH, 'burn/anger') can be work... | 2,861 | 7 | id | 1 | 1 |
| `wa_verse_records` | The legacy per-term-in-verse occurrence store (247,046 rows) that predates the master verse table — one row per term found in a verse, wi... | 247,046 | 30 | id | 4 | 14 |
| `wa_verse_term_links` | The junction between a wa_verse_records occurrence and a wa_term_inventory term (237,531 rows), unique on (verse_id, term_inv_id) and car... | 237,531 | 8 | id | 2 | 3 |
| `wa_vocab_member` | The 39 permitted values across the 8 declared vocabularies, one row per value with its label, description and sort order. It has a full s... | 39 | 12 | id | 2 | 2 |
| `wa_vocab_set` | Declares 8 controlled vocabularies (dimension labels, dominant subject, confidence markers, Stage 2c outcomes), naming for each the DB co... | 8 | 10 | id | 0 | 2 |
| `word_registry` | The programme's lexical entry point: one row per English inner-life word (222 rows), carrying the word's definition, provenance, cluster ... | 222 | 32 | id | 0 | 4 |
| `word_run_state` | Per-word outcome of each engine run: which phase the word reached, what the audit concluded and why it stopped. 539 rows over 373 runs — ... | 539 | 11 | id | 1 | 0 |

## Undescribed tables

- `finding_verse_index` — 475,790 rows, 6 columns
- `prose_section_verse_link` — 0 rows, 4 columns
- `record_change_log` — 1,242 rows, 10 columns

---
_Rebuild the register with `python iba/scripts/build_dbschema.py --db bible_research --verify` before regenerating this report, if it may be stale._
