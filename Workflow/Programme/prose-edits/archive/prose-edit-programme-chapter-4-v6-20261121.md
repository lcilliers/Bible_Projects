# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file becomes permanent provenance once imported (its archived path is -->
<!-- recorded as record_change_log.change_source, escalation #836) -- do not delete -->
<!-- by hand; the import step archives it automatically on success. -->
<!-- PROSE_EXPORT_SECTION_IDS: 22,23,24,25,26,27,28,70,30,31,66 -->

<!-- PROSE_SECTION_ID: 22 -->
<!-- PROSE_SECTION_TYPE: prog_data_database -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: The database as the programme's working memory -->
<!-- PROSE_SORT_ORDER: 22 -->
<!-- PROSE_VERSION: 1404 -->

## The database as the programme's working memory

The programme runs on two SQLite databases. `iba/app/db/iba.db` is the home for the project's process control and its working data: the base data (every table from the STEP extraction through the Strong's tables, the verses, meanings and the mechanical reading of each verse), the surfaces and collections, the observations and nodes, the claims and the narrative, the escalation record, and the `cfg_*` configuration store that governs how every step of the app behaves. `database/bible_research.db` is the home for the programme prose and its glossary, the store in which the programme's written account is authored.

The `cfg_*` store holds every rule the app's code obeys: which step may write which table, what a step's failure path is, what a controlled vocabulary's allowed values are, what a report's structure is. The principle is that the code decides nothing; every choice is a row that a live check can read. The configuration layer is part of the data architecture, not a separate concern, because it makes the behaviour of the base data and of the reading traceable and changeable without a code edit. Chapter 5 describes the governance mechanism in full; this chapter describes what the two databases hold. The record of what each table is for, and what each column holds, is kept in the database itself (`cfg_table` and `cfg_column`) and is read before a table is used.

Neither database is the primary source for the Hebrew, Greek and Aramaic material the programme works with. STEP Bible remains the source every Strong's number, gloss, meaning parse and verse reference traces back to. The base data in `iba.db` is the programme's verified, structured copy of what STEP returns, a working record built from it and not a replacement for it.

The sections that follow work through what each database holds: the registry of onboarded words and the surface and collection tables that hold the scope, the term and lexical substrate, the verse layer, the node, the observation tables, the question catalogue, the claims and narrative, and the prose store. A table this chapter does not name is not part of the current architecture, whatever its history. Tables kept only as the record of earlier methods are not read by the current study.

---

<!-- PROSE_SECTION_ID: 23 -->
<!-- PROSE_SECTION_TYPE: prog_data_registry -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: Surfaces, collections and the registry -->
<!-- PROSE_SORT_ORDER: 23 -->
<!-- PROSE_VERSION: 1405 -->

## Surfaces, collections and the registry

The scope of the study is held in the surface and collection tables of `iba.db`. `surface_term` holds each surface, the English word or phrase of the ESV, with its surface group (behaviour, inner_being_state, entity or other), the reason for it, who judged it and its state, together with its base. `surface_derivation` records how a derived form relates to its base, `surface_event` keeps every change to a surface with its state before and after, `surface_flag` holds the flags raised against surfaces, and `ai_call` keeps each call to the local model with the prompt version that gave it. What a model judged stays inferential until the researcher confirms it.

`collection` holds the collections: a name, a status (confirmed, merged or retired) and the core word it is formed around. `collection_link` places each surface as a member by tier (core, synonym, opposite, gathered or phrase), keeps the link a surface holds in its own right, and flags a link that is shared. `collection_listing` holds the listed candidates. A collection's members carry the verses. `collection_subgroup` and `collection_subgroup_surface` hold the subgroups of a collection and the index of its surfaces, each with its state: placed in a subgroup, set aside with a reason, or not yet placed.

`word_registry` is the entry point for onboarding a new word of the base data: a row carries the English headword, why it entered, and its onboarding state. It is deliberately thin and answers one question: whether this word is in an onboarding run, and where that run stands. The record of the study's scope is not the registry; it is the surfaces and collections above. A word's analytical record is not accreted onto a registry row; it is built in the tables the rest of this chapter describes, keyed on the Strong's code, the surface, the collection and the node.

---

<!-- PROSE_SECTION_ID: 24 -->
<!-- PROSE_SECTION_TYPE: prog_data_terms -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: Terms -->
<!-- PROSE_SORT_ORDER: 24 -->
<!-- PROSE_VERSION: 1406 -->

## Terms

The term layer lives in `iba.db`, as a chain of small, single-purpose tables, each named for the processing layer it represents.

`word_strong` is the discovery record: one row for each pair of an English word and a Strong's code that STEP's word search returned. It carries the link only, with no term detail, and determines which Strong's codes an onboarding run touches.

`strong` is the term's identity: one row for each Strong's code, unique and global to the whole study. Meaning is deliberately not carried on this row; it is normalised into its own tables, `strong_sense`, `strong_meaning_tree`, `strong_lexicon`, `strong_lsj_parsed` and `strong_mounce_parsed`, which hold the sense hierarchy and the LSJ and Mounce enrichment. `strong_related` carries the associative and root-family relationships between codes and is keyed on the exact lettered code, never on the base code.

`lemma_inventory` is the independent substrate over which the seed net runs, imported from the earlier study and deliberately not derived from the registry, so that it works as a completeness control. `candidate_seed` is the over-inclusive candidate assessment built from it, a potential and not a definite decision about whether a lemma belongs in scope, with the lexical stage as the real test.

The verse-level lexical substrate is a further chain. `span` is the immutable source parse, one row for each tag of STEP's own interlinear presentation of a verse, kept verbatim so the parse can be re-derived; a combined-unit tag is kept as one row and is not split. `span_candidate` is the candidate stamp over a span. `verse_lexical` is the derived mechanical reading of the verse: one row for each Strong's code within a span, with the cluster codes of the Strong's code in its `role` column (an association copied onto the occurrence, and not the role a word has in a finding, which is set out under the node), the sense selected by stem and voice, and any ambiguity named and not resolved. It records the verse's structural composition and says nothing of what a word does for the inner being. It is derived once from the span and read from there; everything after it reads the derived row and does not derive again from `span` or `strong`.

---

<!-- PROSE_SECTION_ID: 25 -->
<!-- PROSE_SECTION_TYPE: prog_xref_architecture -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: Ownership and cross-registry references -->
<!-- PROSE_SORT_ORDER: 25 -->
<!-- PROSE_VERSION: 1436 -->

## Ownership and cross-registry references

Inner-being vocabulary overlaps, and the architecture answers the question of overlap at the level of the surface and the collection. Each surface of the scope is a member of exactly one collection. A surface carries the collection of its own link where it has one, and otherwise the collection of its base: a derived form is a surface with a link of its own, so it is read by that link. A node carries the one collection of its surface by this rule.

Every table of the term layer is keyed on the Strong's code or the span, never on a registry row. A term's record accumulates at the Strong's-code level from the start, so there is no per-word copy of that record to reconcile across words that share a term. `word_strong` is a many-to-many link, because a Strong's code can be discovered through more than one English word, but this raises no question of ownership: the record a Strong's code accumulates does not live under any one word.

An English surface relates to the original text through its Strong's codes, and a surface that carries more than one sense in the verses is read by the code of each sense. `strong_related` is keyed on the exact lettered code. The base of a surface is an instrument for gathering like words into a collection and never the member of a collection itself.

---

<!-- PROSE_SECTION_ID: 26 -->
<!-- PROSE_SECTION_TYPE: prog_data_verses -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: Verses and the context layer -->
<!-- PROSE_SORT_ORDER: 26 -->
<!-- PROSE_VERSION: 1437 -->

## Verses and the context layer

`iba.db`'s `verse` table carries the addressable identity of a verse: its `osisId`, its reference, and the full interlinear HTML of STEP kept verbatim so that `span` can be re-derived. Every verse of the Bible is held, and each has its mechanical reading in `verse_lexical` (the previous section).

A verse is in the study's scope when it holds an occurrence of a member surface of a live collection. The entity and other surfaces of an in-scope verse are in scope as nodes of the observation that covers them; a verse that holds only entity or other surfaces is out of scope and is not touched. The scope is read from the tables: an analysis reads tables and never a working file.

The verse is the place where every observation is tied to the text. Each observation is applied to its verses, words and surfaces by nodes (the section on the node), and a reading of a verse begins with the verse itself, read in its passage with all the observations already recorded for it.

---

<!-- PROSE_SECTION_ID: 27 -->
<!-- PROSE_SECTION_TYPE: prog_anchor_verse -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: The node -->
<!-- PROSE_SORT_ORDER: 27 -->
<!-- PROSE_VERSION: 1409 -->

## The node

The programme anchors a finding to a specific piece of verse evidence by the **node**. A node applies one observation to one verse, one word and one surface: it carries the verse reference, the `verse_lexical` row of the occurrence (which fixes the surface, the Strong's code and the morph code), the collection and subgroup of the surface, the role the word has in the finding, and the stage that produced it. The node is how the study finds things: the observations of a collection are found through the collection on the node, and those of a subgroup through its subgroup.

Where an observation refers to several variants, such as verses, surfaces or Strong's codes, it has a node for each variant. A live observation has at least one live node, and a node cannot exist without a live observation. Two live nodes of one observation whose indexing columns are all the same are either incomplete or a duplicate: an incomplete node is completed, and a duplicate is withdrawn with its reason. A node is withdrawn, never physically deleted.

The role of a node is what the word is for the finding the observation states, and it is judged by reading the verse. It is judged for each occurrence, against what the verse is about, the inner-being operation it carries, and never taken from the cluster tag, from the collection the surface is in, from the word's other occurrences or from the part the word usually plays. The same surface can therefore be a characteristic in one verse and a qualifier in another. Each role is its own observation, applied by its nodes to the verses where that role holds, and the difference between the verses is carried by those observations and not by the surface's group.

The roles fall into four sets. Two are relevant to the inner being. A **characteristic** is a word that behaves as a characteristic of the inner being: it carries the main inner-being operation of the verse, and it is the word the finding is about. A **qualifier** binds to a characteristic and gives it value or context in place: its manner, measure, strengthening, ground, cause, object or setting, or the negator that makes an act a refusal, and there is no fixed list. The observation of a qualifier states what it gives the characteristic; the word has no account of its own from that verse, and it is carried as a face of the word and as an interrelationship. In 'I cried aloud to the Lord', *cried* is the characteristic and *aloud* a qualifier giving volume, unless the verse treats the loudness as a purpose or effect of its own, in which case it is part of the characteristic. A word that only qualifies, or that has no inner-being role of its own, is not analysed by itself: it is bound to the characteristic it qualifies, or excluded. Three roles bear on the finding without being its characteristic or qualifier: the **object** (what the act is directed at, or its content), the **relational target** (the party the act engages) and the **enactment** (the outward act the inner act produces). `standalone` records that the word was recognised and has no inner-being role on any other surface of the verse. `lexical` records that the word was read lexically and that its inner-being role has not been assessed; the nodes of stages 1 to 3 carry it, because those stages state nothing of the inner being.

A party's role is an observation and not a field of the node. 'An evil spirit acting towards the inner being' is one observation, applied by its nodes to every verse and word it affects; the programme keeps no table of parties. A role is never a verdict: a verse is not closed as 'only a qualifier' or 'no bearing', and what is recorded is what the verse is (Chapter 2, the inner-being layer).

The study's earlier method named three roles, characteristic, qualifier (or process-element) and standalone, and they remain the core. The node adds the object, the relational target and the enactment for the words that bear on a finding, and `lexical` for the words not yet assessed. Two other columns are also called role and are not the role of a node: `verse_lexical.role` holds the cluster codes of the word's Strong's code copied onto each occurrence, an association with no reading of the verse in it, and `verse_span_index.role` in `bible_research.db` holds an older analytic role set by earlier campaigns, on part of the spans and with a vocabulary that grew by use. Neither is read as the role of a word in a finding.

The role is required on a node that names a word, but it is not yet set on every node. On 2026-11-21, of the 68,426 live nodes, 14,065 had no role. Setting them has been handed to the collection reading, which has not yet reached it, and a role found wrong on an earlier-method node is corrected there.

---

<!-- PROSE_SECTION_ID: 28 -->
<!-- PROSE_SECTION_TYPE: prog_data_dimensions -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: The analytical grouping: collections and subgroups -->
<!-- PROSE_SORT_ORDER: 28 -->
<!-- PROSE_VERSION: 1450 -->

## The analytical grouping: collections and subgroups

The programme's analytical grouping is the collection and, within it, the subgroup. A collection gathers surfaces of like or related behaviour (Chapter 2). A subgroup is a group of the surfaces of one collection, made so that the collection can be read in units: the subgroup is the unit of reading, and its surfaces are read together in each layer. The verses of a subgroup's surfaces travel with it through the nodes, so that an observation made for the subgroup is found for each of its verses. The concept tables of an earlier method are retired and the collection takes their place. The method that grouped the surfaces of the first collection did not serve the purpose the subgroups are for and is withdrawn; the subgroups are formed again when collection processing starts.

The readings of a collection are recorded in the observation tables. `ib_observation` holds one finding, with its stage, its kind (for example term, face, group, enrichment, pairing or relation), its text and its status. `ib_node` holds the occurrences the observation applies to (the previous section). `ib_observation_change` keeps every change to an observation with its reason, so that a withdrawal is a soft delete that can be explained. `collection_layer_item` is the ledger of the layered reading: one row for each aspect a step of the reading demands for a collection, which is closed by an observation with its nodes or by a recorded none with its reason, and is then validated by the check.

The values of the stage of an observation are `lexical` (stage 1), `layer-1` and `layer-2` (stage 3). The observations of stage 4, the inner-being analysis, are not yet defined. Observations made by earlier methods are kept as the history of those methods; a live observation must comply with the rules of the observation and the node, and one that cannot be revived to comply is retired with its nodes as a soft delete with its reason.

The reading process of the app (`Reading.ps1`) takes a reading of one scope through three gates (recorded, synergised, published) and is being aligned to collections.

---

<!-- PROSE_SECTION_ID: 70 -->
<!-- PROSE_SECTION_TYPE: prog_data_questions -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: The question catalogue and findings -->
<!-- PROSE_SORT_ORDER: 29 -->
<!-- PROSE_VERSION: 1411 -->

## The question catalogue and findings

The standing catalogue of questions is `wa_obs_question_catalogue` in `iba.db`. Its questions are prompts that direct the reading toward what a word's occurrences may show; they are never answers to force, and a prompt that does not apply to a word is not answered. Step S1 of the layered reading draws on its prompts of the meaning window when a word is read in its verses. A reader must check which table a piece of work queries and must not assume that a table name alone identifies it, because a table of the same name exists in the other database as the record of an earlier method.

The findings of the programme are the observations of the previous section. Each is tied to its verses by nodes and is founded in the verse. An observation never repeats the verse text, beyond the number of consecutive verse words the configuration allows, and the same wording and meaning is never held as two observations: a second live observation with the same text is a duplicate and is withdrawn with its nodes moved to the first.

Observations of earlier methods are kept as the record of those methods. Their kinds, tags and parts need not be consistent or a full read, provided they comply with the rules of the observation and the node. The collections are read again, in the stages of Chapter 2, to enhance them. The researcher's earlier instructions and answers, and the reasons for each change, are in the escalation record and the observation change log, and are read there before a question is put.

The universal finding store and the flags of earlier methods are kept as history and are not read by the current study.

---

<!-- PROSE_SECTION_ID: 30 -->
<!-- PROSE_SECTION_TYPE: prog_data_synthesis -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: Claims and the narrative -->
<!-- PROSE_SORT_ORDER: 30 -->
<!-- PROSE_VERSION: 1412 -->

## Claims and the narrative

The account of the programme is built from the observations upward through two tables of claims and a narrative, all in `iba.db`. `narrative_claim` holds each **claim**: a statement derived from sources, the verses and, later, the science reading, that goes beyond their mere text, held in its own plain wording. A quotation is not a claim. `narrative_claim_source` holds the sources of each claim and its verdict against the wording of the original essay: stands, restated, widened, corrected or new. `narrative_claim_telling` records how the narrative tells each claim: in full, in part or by pointer. Each claim is therefore traceable to its sources and to the place in the narrative where it is told.

`narrative_chapter` is the authority for which chapters exist, their order and their purpose. `narrative_section` holds the sections of each chapter, whose text is a block; `narrative_citation` holds the citations and `narrative_update` the record of updates to the narrative. The chapter files are exports from the database; the database is the home of the narrative.

The claims are formulated from the observations in stage 5 of the reading, which is not yet decided. What is established is that a claim is bound to the observations and nodes that found it, and that the claims of a collection are formulated after its inner-being analysis (stage 4), which is itself still being defined. The existing claims come from an earlier method and are not yet cross-linked to the collections; that cross-linking, and the re-evaluation of each claim against the observations, belongs to the work of stages 4 and 5. Larger claims are not made before the smaller claims on which they rest.

---

<!-- PROSE_SECTION_ID: 31 -->
<!-- PROSE_SECTION_TYPE: prog_data_prose_store -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: The prose store -->
<!-- PROSE_SORT_ORDER: 31 -->
<!-- PROSE_VERSION: 1413 -->

## The prose store

The prose store is `bible_research.db`'s database-canonical mechanism for authored narrative and for the programme prose, including this chapter. `prose_section_type` is the dictionary of stable named slots prose can be written into, and it is controlled vocabulary: a new type is created only on the researcher's instruction naming its code and its place in the book. `prose_section` is the content, one row for each titled section, carrying its body, its version and its status (draft, in review, approved or archived). The programme glossary and the contentious glossary are kept in the same store, as sections of their own types; Claude keeps the programme glossary up to date and its entries enter as draft, while an entry in the contentious glossary is the researcher's to settle.

The store's lifecycle is system-versioned: a section that is superseded is updated in place, and its prior content is kept in `record_change_log`, whose payload holds what a change overwrote and whose row is pointed to by the section's version. No edit is silently lost and the full history is queryable. `record_change_log` is a project-wide change-audit log, and a prose write produces its log row in the same transaction as the write.

`prose_section_verse_link`, `prose_section_dimension_link` and `prose_section_finding_link` connect a prose row to the verses, dimensions and findings it discusses, so that a query can start from the evidence and find the prose that discusses it, or the reverse.

The store carries its own quality-flagging mechanism. A flag raised against the corpus is followed by a proposal that searches the active corpus for a literal match and previews the replacement, and an approved fix is applied as a patch, the same mechanism that carries every other prose change.

`Prose.ps1` is the registered front door onto the store: `Extract` for programme-prose extracts, `Search` for a search of the active sections, `ExportChapter` and `ImportChapter` for the editable-Markdown round trip, `Flag`, `FlagFixPropose` and `FlagFixApply` for the quality workflow, `SetStatus` for the review status of a section, and `ApplyPatch`, which applies a reviewed patch in one transaction or not at all and is run as a dry run first. Every step reads its configuration from `cfg_prose` and not from a constant. The database remains canonical: a draft file is the input, the patch reads it, the patch step writes it, and any extract is regenerated from the database afterward.

---

<!-- PROSE_SECTION_ID: 66 -->
<!-- PROSE_SECTION_TYPE: prog_data_obslog_pipeline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data architecture -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_SECTION_TITLE: Capture mechanisms -->
<!-- PROSE_SORT_ORDER: 32 -->
<!-- PROSE_VERSION: 1414 -->

## Capture mechanisms

The programme's capture mechanisms are three, each serving a different kind of work, and they share one discipline: a write to a database is always a distinct, auditable step from the work that produced it, and the record of that write outlives the session that made it.

First, for programme prose and the glossary: the `Prose.ps1` round trip described in the previous section. A chapter is exported to editable Markdown, the body under each section's fixed heading is edited, the import generates a patch, and the patch is applied through the dry run first and then the live apply. No step in that chain writes to the database directly.

Second, for the observations of the reading: each step of the layered reading is run through the app. A working file is pulled for the open rows of the ledger with their evidence, Claude reads and fills each row, and the record step checks the whole file (a problem anywhere refuses all) and writes the observations, their nodes and the ledger answers in one transaction. The check then validates every answered row against the tables. A row answered again withdraws its earlier observation with its reason in `ib_observation_change`. The grouping of the surfaces is run in the same way, with its own validation and a scrutiny report for the researcher.

Third, for anomalies, judgement calls and anything requiring a decision that the running code cannot make on its own: the `escalation` table, described in the next chapter. An item is raised with the researcher's own words quoted verbatim, an explicit resolution kind and a next action, and is tracked to closure through `Escalation.ps1`.

Where a step that a routine needs is not registered in the app, reconstructing it from past output files is itself the signal that a required step is missing and is not a puzzle to solve from precedent; the missing step is registered and built first.

---
