# Prose Edit — Word Index and Glossary — Chapter 1

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file becomes permanent provenance once imported (its archived path is -->
<!-- recorded as record_change_log.change_source, escalation #836) -- do not delete -->
<!-- by hand; the import step archives it automatically on success. -->
<!-- PROSE_EXPORT_SECTION_IDS: 1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1067,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1066,1068 -->

<!-- PROSE_SECTION_ID: 1041 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## delete_flagged

[DEFINITION] Deleted in the project indicate that the item is soft-delete by setting the the delete column to 1 or 'delete' or 'inactive'.  As a general practice records are not removed, but soft-deleted. Column naming for the same behaviour varies: deleted, delete_flagged. These records should be excluded from usage

[BACKGROUND] The project's dominant deletion convention, used on most tables in both databases. Distinct from deleted (version-aware supersession) and deleted (folder state) below, and from inactive, the separate convention for retiring config registrations rather than data rows. wa_obs_question_catalogue.deleted currently disagrees with that table's own status column — a known, unreconciled inconsistency.

---

<!-- PROSE_SECTION_ID: 1042 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## inactive

[DEFINITION] inactive, used in cfg.* tables, is a alternative term to deleted and should be excluded for any operations.

[BACKGROUND] The config-system counterpart to delete_flagged: retires a config registration rather than project data. Used, for example, to retire the wa_vocab_set/wa_vocab_member tables once their content was migrated into this Glossary.

---

<!-- PROSE_SECTION_ID: 1043 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## M-Code cluster

[DEFINITION] An analytical grouping mechanism for Strong's terms, used to establish the collections. Each cluster carries an M-code (e.g. M01). M01 to M47 group Strong's terms by shared characteristics of the inner being. Two further codes extend the scheme: FLAG holds terms not yet decided into a characteristic grouping, and T2 holds supplementary terms that are not themselves inner-being terms. T3 is a related tier for action verbs and other terms not directly tied to an inner-being operation.

[BACKGROUND] Clusters have served their purpose in establishing the collections and play no part in nodes and observations; cluster_code on a node is history (researcher, 2026-11-13; behaviour rules 130 and 131). The code itself is cluster.cluster_code; the bare cluster columns are ib_characteristic.cluster, verse_span_index.cluster and file_manifest.cluster. See the other "cluster" entry below for an unrelated, retired scheme (C01 to C22).

---

<!-- PROSE_SECTION_ID: 1044 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## C-code

[DEFINITION] Dimension Reviews used C-code (C01–C22) to group strong terms. This grouping is distinguished from cluster (M-code).C-code allocations is completely redundant and no longer used.

[BACKGROUND] wa_dim_review_cluster_log.cluster carries this sense under the bare column name cluster — the one place in the schema where that bare name disagrees with every other table's M-code convention. Reading it as an M-code would be a real, silent misread.

---

<!-- PROSE_SECTION_ID: 1045 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## FLAG

[DEFINITION] FLAG is a specific type of Cluster of strong terms that have not been considered for Cluster allocation.

[BACKGROUND] Not the generic word "flag" — quality flags, research flags, term flags, and inference flags are each their own unrelated thing project-wide. Named distinctly here because a plain search for "flag" returns dozens of unrelated hits.

---

<!-- PROSE_SECTION_ID: 1046 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1261 -->

## T2

[DEFINITION] M-code cluster with code T2 consists of Strong's codes carrying no direct inner-being connotation. These terms may serve as a qualifier to enhance another inner being term. Their analytic value is closely tied to another term, never in isolation.

[BACKGROUND] T2 is a cluster_code value, like FLAG and T3, distinct from T3 (a tier for human operations and movements not tied to one cluster). Clusters play no part in nodes and observations; cluster_code on a node is history (researcher, 2026-11-13).

---

<!-- PROSE_SECTION_ID: 1047 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## characteristic

[DEFINITION] Characteristic (short form Char) is widely used to describe inner being behaviour. It is the foundation for the programme observations of how the inner being works or manifest. The composition and naming of specific characteristics are not predefined and is part of the subject matter of the program. The word_registry.word IS NOT a characteristic and the registry should never be used as the composition of a specific Characteristic. The lemma, gloss, sub gloss or surface word used in the lexical is not synonymous to a characteristic. A specific characteristic is likely to be associated with a group of like words; the study gathers them in collections of surfaces. On a node, characteristic is the role of the word the finding is about.

[BACKGROUND] Unlike the body that have a defined set of members (arms. fingers etc) , the inner being does NOT consist of a predefined list of characteristics. Characteristics cannot be measured and their structure and existence are only known by inference on the inner being behaviours. Characteristics is not a thing, it is likely to be something like a process, state, movement. The collection of behaviours, processes, actions, movements in the inner being give substance to a specific characteristic such as anger or love. Clusters and subgroups served to establish the collections and play no part in observations (researcher, 2026-11-13).

---

<!-- PROSE_SECTION_ID: 1048 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## operation

[DEFINITION] operation within the context of the inner being encapsulate or describe what and how a inner being activity is working or behaving. This includes from or to other objects outside of the inner being such as another inner being, non-inner being, or physical object.

[BACKGROUND] In an observation, the operation of a statement finding is an action description (who or what does what) with its mode: done, foreseen, commanded, negated or reported (cfg_setting reading.observation_items).

---

<!-- PROSE_SECTION_ID: 1049 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## family

[DEFINITION] family within the context of work related to characteristics is used as an alternative method to group terms together for analytical purposes.  A family of terms is a characteristic in the making.

[BACKGROUND] Distinct from family (root), which groups terms by shared etymology, not theme.

---

<!-- PROSE_SECTION_ID: 1050 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## family root

[DEFINITION] root or family root in entymological grouping that eminates from STEP

[BACKGROUND] An etymological grouping, unrelated to family (thematic) despite sharing the word "family."

---

<!-- PROSE_SECTION_ID: 1051 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## scope

[DEFINITION] scope within the context of the verse defines the verse or passage that collectively represent the data that is subject to analysis

[BACKGROUND] Convention only, no CHECK constraint. One of at least four unrelated live meanings of the bare column name scope — see the sibling entries below.

---

<!-- PROSE_SECTION_ID: 1052 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## scope

[DEFINITION] scope within the context of file naming (wa_file_name_pattern.scope) defines what a filename pattern is instantiated per — "per-cluster," "per-registry," "programme," plus per-group/per-batch/patch-id.

[BACKGROUND] Governs file-naming only; unrelated to the other scope senses.

---

<!-- PROSE_SECTION_ID: 1053 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## scope

[DEFINITION] scope within the context of the catalogue (wa_obs_question_catalogue.scope) create buckets based on what the question is related to (Word/term lexical, Characteristic/HIB behaviour, etc.) for the 126 live T-coded questions. This is an alternative grouping to the Tier classification for the catalogue questions.

[BACKGROUND] Recently repurposed from an older universal/Leviticus-marker meaning.

---

<!-- PROSE_SECTION_ID: 1054 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## scope

[DEFINITION] scope within the context of run-step processing (cfg_step.scope): what a run-step needs scoped to it to execute (a word, "none," etc.) — an IBA app run-parameter concept.

[BACKGROUND] Unrelated to any of the data-level scope senses above.

---

<!-- PROSE_SECTION_ID: 1055 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Dimension

[DEFINITION] The retired 11-value Dimension vocabulary: 01 Emotion-Positive, 02 Emotion-Negative, 03 Cognition, 04 Volition, 05 Moral Character, 06 Relational Disposition, 07 Vitality/Existence, 08 Transformation, 09 Agency/Power, 10 Dependence/Creatureliness, 11 Divine-Human Correspondence.

[BACKGROUND] Governed wa_dimension_index.dimension under the now-retired Dimension Review stage (researcher-ratified 2026-04-20). Superseded by the M-code cluster/characteristic model; data retained, not live.

---

<!-- PROSE_SECTION_ID: 1056 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## dominant subject

[DEFINITION] Retired Dimension Review vocabulary naming the primary agent in a verse-context group: HUMAN, GOD, OTHER_HUMAN, UNSEEN (rare), or NONE (genuinely dual — divine and human both explicit).

[BACKGROUND] Governed wa_dimension_index.dominant_subject. Retired with the Dimension Review stage.

---

<!-- PROSE_SECTION_ID: 1057 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## dimension confidence

[DEFINITION] Retired confidence marker for a dimension assignment: KEYWORD_WEAK / KEYWORD_STRONG (automated classifier, pending review) or CLAUDE_AI (post-review analyst assignment).

[BACKGROUND] Governed wa_dimension_index.dimension_confidence. Retired with the Dimension Review stage.

---

<!-- PROSE_SECTION_ID: 1058 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## QA_FLAG

[DEFINITION] Retired per-group quality outcome from Dimension Review's Phase B: QA-CLEAR, QA-TERMCENTRIC, QA-VAGUE, QA-BROAD, QA-EXTERNALISED, QA-REVIEW.

[BACKGROUND] Logged in observations, never a DB column. Retired with the Dimension Review stage.

---

<!-- PROSE_SECTION_ID: 1059 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## MANUAL_OVERRIDE

[DEFINITION] Retired lock flag: 1 = dimension locked by researcher review; 0 = open for reassignment (the expected post-completion state).

[BACKGROUND] Governed wa_dimension_index.manual_override. Retired with the Dimension Review stage.

---

<!-- PROSE_SECTION_ID: 1060 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Stage 2c Synthesis Outcome

[DEFINITION] Retired v1.8 outcome code: D = Described (substantive finding citing 2+ Q&A entries), F = Further research required, N = Not applicable.

[BACKGROUND] Governed wa_session_b_findings.synthesis_outcome under the retired Session B Stage 2c mechanism.

---

<!-- PROSE_SECTION_ID: 1061 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Stage 2c Synthesis Finding Type

[DEFINITION] Retired v1.8 finding_type values: SYNTHESIS_INTRA_TIER (single tier) and SYNTHESIS_INTER_TIER (tier-pair).

[BACKGROUND] Governed wa_session_b_findings.finding_type (synthesis subset) under the retired Session B Stage 2c mechanism.

---

<!-- PROSE_SECTION_ID: 1062 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Stage 2c Structural Relationship

[DEFINITION] Retired values naming the structural connection between two tiers on an inter-tier D-outcome: causal, enabling, sequential, constitutive, tension, parallel, N/A.

[BACKGROUND] Governed wa_session_b_findings.structural_relationship under the retired Session B Stage 2c mechanism. Last of the 8 migrated Dimension Review vocabularies.

---

<!-- PROSE_SECTION_ID: 1063 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## grain

[DEFINITION] The actual rollup unit for verse-analysis: a per-occurrence STEP sub-gloss, not the bare lemma/Strong's number. A polysemous lemma (e.g. abad = serve/minister/labour/burden) rolls up per grain, never aggregated across all its senses.

[BACKGROUND] Indexed by wa_verse_term_links (step_subgloss_code). mti_terms.owning_word is explicitly not authoritative for sense — the grain code is. Introduced in the 2026-07-02 verse-analysis method, superseding "lemma" as the unit of rollup.

---

<!-- PROSE_SECTION_ID: 1064 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Gate 1

[DEFINITION] In the index-driven lexical build, a span that is a tagged non-T2 term with a verse_context — lexicalised and linked via verse_context_id.

[BACKGROUND] One of two span-admission gates (see Gate 2 for the other). Function words (particle/preposition/conjunction/suffix/pronoun) are skipped entirely; T2 stays excluded from standalone analysis.

---

<!-- PROSE_SECTION_ID: 1065 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Gate 2

[DEFINITION] In the index-driven lexical build, a content word not yet tagged as a term — lexicalised anyway, keyed on verse_span_id (gate='2-relevant'), as a candidate for confirmation.

[BACKGROUND] One of two span-admission gates (see Gate 1 for the other). Distinct from "gate" used generically elsewhere in the project (e.g. the anchor-verse gate).

---

<!-- PROSE_SECTION_ID: 1067 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## oracle

[DEFINITION] For prophetic books, the processing unit in place of chapter or whole-book: a rhetorically-marked passage that routinely crosses chapter lines (e.g. Malachi's disputation form).

[BACKGROUND] Segmentation units can span chapters for this via the verse_refs field, filed under the oracle's anchor chapter.

---

<!-- PROSE_SECTION_ID: 1069 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1262 -->

## T3

[DEFINITION] T3 is a tier for Strong's terms describing an inner-being operation, action, or movement (often a verb) that is not tied to one specific cluster, or that applies broadly across many clusters. Unlike T2, T3 terms ARE inner-being-related: they describe an operation, not merely qualify one.

[BACKGROUND] T3 is a cluster_code value, like FLAG and T2. Clusters play no part in nodes and observations; cluster_code on a node is history (researcher, 2026-11-13).

---

<!-- PROSE_SECTION_ID: 1070 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Dimension

[DEFINITION] In the current verse-lexical method, a dimension (D1–D14, also 've_nr' 101–118+) is one structured field of information derived for a term-in-verse — e.g. sense, source, seat, bearer, manner, intensity, role. Each dimension is one column of the analytical read of a span, not a characteristic of the inner being itself.

[BACKGROUND] Distinct from the retired Dimension Review vocabulary (see the other "Dimension" entry) — that scheme classified whole verse-context groups into one of 11 broad areas; this one is the live per-term structured-field vocabulary in ve_lexical. Also distinct from characteristic (what the inner being does) — a dimension is a linguistic/analytical attribute recorded about a term's occurrence.

---

<!-- PROSE_SECTION_ID: 1071 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## term

[DEFINITION] Used loosely throughout the project for any of: a Strong's-coded lexical entry (a specific Hebrew/Greek word-sense), a word_registry study word, or a span occurrence in a verse. Context decides which is meant — the project has no single definition that fixes it.

[BACKGROUND] See grain for the project's actual, precise rollup unit where "term" would otherwise be ambiguous. Prefer grain, span, or Strong's number over the bare word "term" when precision matters.

---

<!-- PROSE_SECTION_ID: 1072 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## strong

[DEFINITION] A Strong's number is the standard Hebrew/Greek concordance numbering (e.g. H2734, G4710) used to identify a specific lexical entry across the whole Bible. The project's mti_terms table holds one row per Strong's number.

[BACKGROUND] H = Hebrew, G = Greek; suffix letters (e.g. H7965H) mark sub-entries. A single Strong's number can carry several distinct senses — see grain for how the project resolves which sense is meant in a given occurrence.

---

<!-- PROSE_SECTION_ID: 1073 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## lemma

[DEFINITION] The dictionary/citation form of a word — the base form a Strong's number or STEP entry is filed under, before inflection. In this project, the bare lemma is NOT treated as the unit of analysis for rollup — see grain.

[BACKGROUND] mti_terms.owning_word is explicitly documented as unreliable for sense discrimination on a polysemous lemma (e.g. "worship" mislabels the H5647G "to serve" grain) — the grain code, not the lemma, is authoritative for sense.

---

<!-- PROSE_SECTION_ID: 1074 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## surface

[DEFINITION] The literal, exact text of a word as it appears at one span in the verse (span.surface) — independent of which Strong's number or sense it resolves to.

[BACKGROUND] One of at least three different things a request for "all words of X" could mean — see grain and term for the other two; each gives a different result set for the same request.

---

<!-- PROSE_SECTION_ID: 1075 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## gloss

[DEFINITION] A short English translation equivalent for a Strong's number or grain, typically sourced from STEP — e.g. "anger" for a Hebrew root. Used throughout reports as the human-readable stand-in for a Strong's code.

[BACKGROUND] Distinct from sub gloss (a STEP-level finer sense distinction) and from surface (the literal text actually written in the verse).

---

<!-- PROSE_SECTION_ID: 1076 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## sub gloss

[DEFINITION] A STEP-provided finer sense distinction below the level of a bare gloss — the actual basis for the grain: wa_verse_term_links.step_subgloss_code records which sub-gloss a given occurrence carries.

[BACKGROUND] This is what makes grain-based rollup possible: a polysemous lemma's several sub-glosses are what let the project separate its senses without inventing a new coding scheme.

---

<!-- PROSE_SECTION_ID: 1077 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## lexical

[DEFINITION] Used adjectivally throughout the project for anything concerning a term's meaning/sense as opposed to its inner-being content — "the lexical," "lexicalise," "ve_lexical" all refer to the structured, per-term-in-verse analytical record.

[BACKGROUND] ve_lexical is the live table; "lexicalise" means to derive and write that structured record for a span.

---

<!-- PROSE_SECTION_ID: 1078 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## movement

[DEFINITION] The programme's general word for what the inner being DOES — an action, change, or process attributed to a HIB, as opposed to a static trait. Operationalised in iba.db as operation.

[BACKGROUND] Used informally in prose/method documents; operation is the actual registered database entity for a specific instance of movement.

---

<!-- PROSE_SECTION_ID: 1079 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## action

[DEFINITION] A general term for a verb-level inner-being movement — closely related to operation and to the T3 tier, which specifically holds action/verb terms not tied to one cluster.

[BACKGROUND] Not a distinct technical term with its own DB representation — see operation and T3 for the structured senses.

---

<!-- PROSE_SECTION_ID: 1080 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## STEM

[DEFINITION] A column recording a word's morphological stem (e.g. Hebrew binyan/verb stem, or a general inflectional-family classification), derived from morph_code.

[BACKGROUND] morph_code is the linguistic source of truth in this project; stem and language are both derived from it, not independently authoritative. Not to be confused with STEP (the Bible-lexicon tool this project ingests from) or root (an etymological grouping, see family root).

---

<!-- PROSE_SECTION_ID: 1081 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## XREF

[DEFINITION] A cross-reference registry entry: a Strong's number classified in a registry OTHER than its canonical OWNER registry, recording analytical relevance without duplicating classification.

[BACKGROUND] wa_term_inventory.term_owner_type = OWNER | XREF. mti_terms.owning_registry_fk names the canonical OWNER; mti_term_cross_refs holds the XREF rows. A pure-XREF registry (no OWNER terms) is a legitimate complete state. See owner term for a related but not-yet-reconciled use of "owner" in the verse-analysis method.

---

<!-- PROSE_SECTION_ID: 1082 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Session A

[DEFINITION] The first stage of the (now-superseded) per-word pipeline: initial STEP extraction and raw-data capture for a registry word, producing the Word Summary/Meaning/Verses/Terms/Pointers/Questions sections filed under this session in the Detail design prose book.

[BACKGROUND] Part of the pre-2026-08-15 base-layer pipeline, now owned by iba.db/iba/app. Retained here for provenance since Session A/B/C/D prose content is still live in bible_research.db.

---

<!-- PROSE_SECTION_ID: 1083 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Session B

[DEFINITION] The second stage of the (now-superseded) per-word pipeline: verse-context classification and characteristic/impact analysis, historically split into Stage 1 (readiness) and Stage 2 (analysis, including the retired Stage 2c synthesis).

[BACKGROUND] See Stage 2c Synthesis Outcome / Finding Type / Structural Relationship for the retired Stage 2c vocabulary this session produced.

---

<!-- PROSE_SECTION_ID: 1084 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Session C

[DEFINITION] The third stage of the (now-superseded) per-word pipeline: synopsis, description, and lexicon prose produced per word, later superseded by cluster-level publication.

[BACKGROUND] Session C's own per-word instruction was retired 2026-05-12 in favour of cluster-based publication (wa-sessionc-cluster-overview).

---

<!-- PROSE_SECTION_ID: 1085 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Session D

[DEFINITION] The fourth stage of the (now-superseded) per-word pipeline: cross-registry pointer clustering and cross-word synthesis, producing the Session D Cluster prose (Moral Character, Cognition, Volition, etc.).

[BACKGROUND] Referred to elsewhere as an abandoned workstream (SD_POINTER flag code) — session_d_* tables in bible_research.db carry 0 live rows.

---

<!-- PROSE_SECTION_ID: 1086 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## meaning

[DEFINITION] The parsed dictionary/lexicon meaning text for a Strong's number, structured into senses and stems (wa_meaning_parsed, wa_meaning_sense, wa_meaning_stem) — the raw lexical definition, not the project's own inner-being analysis of the term.

[BACKGROUND] Distinct from gloss (a short translation tag) and from the project's own characteristic/operation analysis, which interprets a term's inner-being content beyond its dictionary meaning.

---

<!-- PROSE_SECTION_ID: 1087 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## flag

[DEFINITION] A flag is a marker added to a record to signal something for follow-up, review, or classification — used generically across many unrelated mechanisms project-wide (quality flags, research flags, term flags, inference flags, the FLAG cluster code).

[BACKGROUND] Not one single mechanism — see FLAG (the cluster-code sense) for the one specific, unrelated Strong's-code meaning. Elsewhere, "flag" always refers to whichever specific flag table/column is under discussion; there is no single project-wide flag concept.

---

<!-- PROSE_SECTION_ID: 1088 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## HIB

[DEFINITION] Human Inner Being — a specific named or implicit human narrative subject within a book, registered in iba.db's hib table. A non-human being (e.g. God, an animal, an institution) can never be registered as a HIB.

[BACKGROUND] The debate pipeline's core subject entity — every phenomenon and operation is recorded against a HIB. Distinct from inner being (the whole field of study) and from inner-being characteristic (the registry's admission filter).

---

<!-- PROSE_SECTION_ID: 1089 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## inner being

[DEFINITION] The programme's whole subject of study: the human spirit, soul, and body as Scripture describes their characteristics, operations, and interrelationships. The programme's governing question is what Scripture reveals about it.

[BACKGROUND] Used at three different scales project-wide: the whole field of study (this sense), HIB (one specific narrative subject within a book), and inner-being characteristic (the registry's admission filter — what makes a word relevant to this study at all).

---

<!-- PROSE_SECTION_ID: 1090 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## non-inner being

[DEFINITION] A being, entity, or content that does NOT qualify as a human inner-being subject for this study — includes God, angels/demons, animals, institutions, and physical objects, and (for terms) content that is not about the inner being at all.

[BACKGROUND] The negative complement of HIB and of inner-being characteristic — used to explain why a term or entity is excluded from the study's registry or from HIB registration.

---

<!-- PROSE_SECTION_ID: 1091 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## root

[DEFINITION] The Hebrew/Greek etymological root a term derives from (e.g. CHARAH, tov) — the basis for the family root grouping, which collects terms sharing a common root regardless of their individual sense.

[BACKGROUND] Distinct from family (thematic), which groups by shared inner-being theme, not etymology. Root-family coding is inconsistent in the schema — some codes are bare romanised roots, others language-prefixed.

---

<!-- PROSE_SECTION_ID: 1092 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Tier

[DEFINITION] The T0–T7 scheme used throughout the observation-question catalogue to classify a question's depth/kind — distinct from a cluster, a component, or a Scope-focus bucket.

[BACKGROUND] Canonical range is T0–T7 (an earlier T1–T8 document is superseded) — this is the observation-catalogue's own depth/kind classification (wa_obs_question_catalogue.section). Do not confuse with T2/T3 as used for cluster-code/tier classification of Strong's terms (see T2, T3) — same T-number notation, two unrelated classification schemes.

---

<!-- PROSE_SECTION_ID: 1093 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Catalogue

[DEFINITION] Refers to the observation-question catalogue (wa_obs_question_catalogue): the ~189-question bank of standard observation questions asked of a term, cluster, or verse during analysis.

[BACKGROUND] Being refactored toward a two-layer VE/SYNTH structure (not yet applied to the DB). Each question carries a scope, tier, and section classification.

---

<!-- PROSE_SECTION_ID: 1094 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## Question

[DEFINITION] One row of the observation-question catalogue (wa_obs_question_catalogue) — a standard analytical prompt asked against a term, cluster, or verse, distinct from a researcher's own ad hoc question in chat or an escalation.

[BACKGROUND] Findings are typically recorded against the specific catalogue question that prompted them (finding_question_link).

---

<!-- PROSE_SECTION_ID: 1095 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## word

[DEFINITION] Used loosely for: (a) a registry study word (word_registry.word, the English words this whole programme studies), (b) the literal text at a span (see surface), or (c) any Strong's-coded lexical entry (see term). Context decides which.

[BACKGROUND] The programme's registry itself is keyed on sense (a); most technical DB work means (b) or (c) — prefer surface, grain, or Strong's number when precision matters.

---

<!-- PROSE_SECTION_ID: 1096 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## verse context

[DEFINITION] The classification record for one term's occurrence in one verse (bible_research.db's verse_context table) — carries the analysis note, keywords, relevance judgement, and (legacy) dimension/pole fields for that specific term-in-verse.

[BACKGROUND] Distinct from the Scope-focus bucket label of the same name (a catalogue classification, see scope), and from iba.db's own base-layer verse/measure tables, which don't use this name at all.

---

<!-- PROSE_SECTION_ID: 1097 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## verse context group (VCG)

[DEFINITION] A group of verse_context rows classified together (verse_context_group) — the unit that vcg_term links a term to, and that cluster_subgroup/characteristic_subgroup ultimately scope work against.

[BACKGROUND] Abbreviated VCG throughout the schema and prose (e.g. group_code "M38-G-VCG-08"). Heading corrected from the researcher's draft "vsg" to the actual live acronym VCG — flagged here, not silently changed.

---

<!-- PROSE_SECTION_ID: 1098 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## config (cfg)

[DEFINITION] The cfg_* table family in iba.db — the single source of truth for how the IBA app's tools, schema, and behaviour rules are governed. Includes cfg_table, cfg_column, cfg_enum, cfg_setting, cfg_step, cfg_behaviour_rule, and others.

[BACKGROUND] Changes to cfg_* content normally go through configmaint.propose (researcher-approval-gated) except in a declared Developer Mode session. This Glossary is itself part of the cfg_* governance model, cross-referenced from cfg_column.use.

---

<!-- PROSE_SECTION_ID: 1099 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## narration

[DEFINITION] The prose account of what a passage or term's evidence says about the inner being, written in the researcher's set voice (wa-narrative-style-instruction) — e.g. "the story" built from a term's collated verse-lexicals, or a chapter's Phase-2 reading.

[BACKGROUND] Used interchangeably with "narrative" and "story" throughout the verse-analysis method. NOTE: this definition is Claude's interpretation of a partially unclear instruction ("narration...describes the theme of the verses. Narration is used in the same context") — flagged for the researcher to confirm or correct, not asserted as certain.

---

<!-- PROSE_SECTION_ID: 1100 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## prose

[DEFINITION] The project's canonical narrative content, stored DB-side in prose_section/prose_section_type (bible_research.db) rather than as flat files. Organised into books (Programme, Detail design, Findings, Essays, Word Index and Glossary), each with chapters and sections.

[BACKGROUND] The programme prose specifically (book_label='Programme') is the canonical authority on what the project is about (governance.prose_canonical_authority). This Glossary is itself one of the prose books.

---

<!-- PROSE_SECTION_ID: 1101 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## programme

[DEFINITION] The whole research effort this project is: a structured study of English words for the human inner life, mapped to Hebrew/Greek terms via Strong's numbers, processed through the IBA app and captured in two SQLite databases (iba.db, bible_research.db).

[BACKGROUND] "The programme" and "Programme" (the prose book) are related but not identical — the book documents the programme; the programme is the actual research effort, which is broader than any one book.

---

<!-- PROSE_SECTION_ID: 1102 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## patch

[DEFINITION] A patch is a validated JSON file that specifies one or more database write operations (inserts/updates), submitted for researcher approval before Claude Code applies it under transactional control. Patch types include PREANALYSIS, SESSIONB, VERSECONTEXT, REPAIR, and others.

[BACKGROUND] Patch preparation, the self-check, and the REPAIR catalogue are governed by wa-patch-instruction [current]. Distinct from a directive (which specifies an operation by criteria rather than a literal write payload) and from a PROSE supersede patch (the specific patch type this Glossary's own edit cycle generates).

---

<!-- PROSE_SECTION_ID: 1103 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## directive

[DEFINITION] A directive is an instruction file specifying a database change by its five required elements (rather than a literal write payload) — used for cluster-process operations under the cluster model.

[BACKGROUND] Governed by wa-directive-instruction [current] §3; Claude Code validates the five required elements and rejects a directive missing any of them, reporting which. Distinct from a patch, which carries the write payload directly.

---

<!-- PROSE_SECTION_ID: 1104 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## anchor

[DEFINITION] The designated primary verse for a term (verse_context.is_anchor=1) or for a passage (passage.anchor_verse_id / verse_passage.is_anchor) — the verse a term's or passage's analysis is built from and cited against. A term with zero active anchors cannot proceed to Session B.

[BACKGROUND] Used at two different grains project-wide: the term-level anchor verse (this entry) and the passage-level anchor verse (a maximal run of consecutive verses' first verse). The programme prose also notes hib.first_verse_id "plays an analogous role" for a HIB without being named anchor in the schema — a drafting gap, not a misreading.

---

<!-- PROSE_SECTION_ID: 1105 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## registry

[DEFINITION] One row of word_registry: the record for one English study word, carrying its onboarding status, session_b_status, verse_context_status, and (legacy) cluster_assignment. The registry number ("no") is the word's permanent identifier used in file naming and cross-references.

[BACKGROUND] Two structurally different tables share this name across the two databases: bible_research.db's word_registry (heavy, phase-status-tracking, ~215 rows) and iba.db's word_registry (thin: word/source/status/timestamps, the current live scope list, ~180 rows). Confirm which database is meant before assuming a field exists.

---

<!-- PROSE_SECTION_ID: 1106 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## OWNER

[DEFINITION] wa_term_inventory.term_owner_type = OWNER means this registry is the canonical home for a Strong's number's classification. The alternative, XREF, records analytical relevance in another registry without duplicating classification.

[BACKGROUND] One mti_terms row exists per Strong's number project-wide; owning_registry_fk names its OWNER. NOT the same thing as owner term (the verse-analysis method's processing-order sense) — whether those two uses of "owner" coincide or genuinely differ is exactly the open question flagged on that entry.

---

<!-- PROSE_SECTION_ID: 1107 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## obslog

[DEFINITION] The comprehensive observation log Claude AI submits at the close of a per-word analysis session — a structured Markdown document (Q&A findings, SD pointers, observations, Stage 2c chapters, GAP questions, review notes, status update) that Claude Code's parser converts into a DB-write manifest.

[BACKGROUND] Part of the legacy per-word Architecture v2 pipeline (6 reset-registries only, superseded by the cluster model for all other words). Format drift between obslogs has required a format-variant fallback parser at least once.

---

<!-- PROSE_SECTION_ID: 1108 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1 -->

## supersede (prose)

[DEFINITION] The mechanism by which an edited prose_section row is replaced without deleting history: the prior version is retained (queryable, not live) and a fresh row/version carries the edit forward.

[BACKGROUND] The basis of this Glossary's own edit cycle (Prose.ps1 export → edit → import) and, historically, of the per-word obslog pipeline's chapter-revision mechanism. "PROSE supersede patch" is the specific patch type this produces.

---

<!-- PROSE_SECTION_ID: 1109 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1243 -->

## T1 (Verse Reading Technique)

[DEFINITION] [VRT] Work from the row, not the gloss -- step T1 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] The unit of analysis is the row (surface + strong + morph + full meaning_tree/stepGloss), not the English translation printed above the table. The translation orients the reader; it is not the evidence. Do not extract English clauses and match them against a keyword checklist; do not dilute or compromise reading quality; do not skip, ignore, or bypass rows; read each row in the context of the nearby rows, not in isolation. A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T1 (a different, characteristic-grain scheme -- see 'TT1 (Tier Catalogue)').

---

<!-- PROSE_SECTION_ID: 1110 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1244 -->

## T2 (Verse Reading Technique)

[DEFINITION] [VRT] Pull the full lexical range before assigning a sense -- step T2 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] Read the word's entire meaning_tree entry for its Strong's code(s), not just the stepGloss or the one sense the English translation happens to use. Record explicitly when a sense the English translation does not use is already a standing member of the word's own lexical range (stated via the lexicon, not inferred from metaphor/imagery), and when the range is genuinely ambiguous across senses that matter for this verse (name the live senses and reason which is operative, rather than silently picking one). A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T2 (a different, characteristic-grain scheme -- see 'TT2 (Tier Catalogue)'). Also distinct from the [CC] cluster_code T2 (a Strong's-code classification -- see the bare 'T2' entry).

---

<!-- PROSE_SECTION_ID: 1111 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1245 -->

## T3 (Verse Reading Technique)

[DEFINITION] [VRT] Let morph decide voice, person, and aspect -- step T3 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] Read the morph code for every verb before deciding tense or voice -- never the English word order or tense. Perfect vs. imperfect vs. participle carry different aspectual force (a passive participle is a durative/ongoing condition, not a future event) -- check this against the English translation's own tense and correct where they diverge. Person/number decides the actual grammatical subject, never inferred from an English pronoun alone. Voice decides whether the subject acts or is acted upon. A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T3 (a different, characteristic-grain scheme -- see 'TT3 (Tier Catalogue)'). Also distinct from the [CC] cluster_code T3 (a Strong's-code classification -- see the bare 'T3' entry).

---

<!-- PROSE_SECTION_ID: 1112 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1246 -->

## T4 (Verse Reading Technique)

[DEFINITION] [VRT] Referent cruxes -- step T4 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] When a pronoun or unnamed party is genuinely ambiguous (several readings all grammatically live), do not silently resolve it and do not default to the most obvious English reading: enumerate every grammatically/contextually live reading; give the textual grounds for each; adopt one explicitly, stating why and whether the choice is a directed/researcher call or this pass's own default; keep the rejected alternatives on record, not just the winner. A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T4 (a different, characteristic-grain scheme -- see 'TT4 (Tier Catalogue)').

---

<!-- PROSE_SECTION_ID: 1113 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1247 -->

## T5 (Verse Reading Technique)

[DEFINITION] [VRT] Genre-conventional elements -- step T5 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] Record the genre-conventional elements of the verse or passage as an observation -- including elements expected by the genre but textually absent. Do not pass over these elements silently. A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T5 (a different, characteristic-grain scheme -- see 'TT5 (Tier Catalogue)').

---

<!-- PROSE_SECTION_ID: 1114 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1248 -->

## T6 (Verse Reading Technique)

[DEFINITION] [VRT] Stamp human-being words (IB) -- step T6 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] Stamp every word that explicitly points to a human being with IB. Other non-human beings are more likely to be stamped Agent (T7) -- only human-being words are stamped IB. A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T6 (a different, characteristic-grain scheme -- see 'TT6 (Tier Catalogue)').

---

<!-- PROSE_SECTION_ID: 1115 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1249 -->

## T7 (Verse Reading Technique)

[DEFINITION] [VRT] Stamp causing-action words (Agent) -- step T7 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] Stamp every word (the noun) that is the causing action as Agent. Note that an IB (T6) can itself be an Agent for another IB. A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T7 (a different, characteristic-grain scheme -- see 'TT7 (Tier Catalogue)').

---

<!-- PROSE_SECTION_ID: 1116 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1250 -->

## T8 (Verse Reading Technique)

[DEFINITION] [VRT] Stamp inner-being-related words (Process) -- step T8 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] Stamp every word that relates to any IB in the verse with Process -- including state/condition/faculty words tied to an IB. A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T8 (a different, characteristic-grain scheme -- see 'TT8 (Tier Catalogue)').

---

<!-- PROSE_SECTION_ID: 1117 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1251 -->

## T9 (Verse Reading Technique)

[DEFINITION] [VRT] Stamp action-verb words (Action) -- step T9 of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique).

[BACKGROUND] Stamp every action word (the verb) with Action. A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, not conclusive -- they do not determine which IB is affected by which Agent, or how it relates to a Process (that follows later in the study). Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. Distinct from the [TC] tier-catalogue T9 (a different, characteristic-grain scheme -- see 'TT9 (Tier Catalogue)').

---

<!-- PROSE_SECTION_ID: 1118 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1252 -->

## T0 (Tier Catalogue)

[DEFINITION] [TC] Divine Image and Created Design -- tier T0 of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions).

[BACKGROUND] God-relation (is the characteristic predicated of God, in what relation), created purpose (what it leads the person to be/do/become), image-bearer expression (what aspect of divine likeness it instantiates), typological significance. Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (checked live 2026-09-04, escalation #1447: its own header names it the authoritative current question list, its obs_ids match wa_obs_question_catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md). Distinct from the [VRT] Verse Reading Technique T0 -- see 'TT0 (Verse Reading Technique)'.

---

<!-- PROSE_SECTION_ID: 1119 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1253 -->

## T1 (Tier Catalogue)

[DEFINITION] [TC] Definition -- tier T1 of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions).

[BACKGROUND] Name and naming, kind (act/disposition/condition/quality), boundary (structural opposite, what it excludes), modes of operation, immediate response, sustained effect, conditions of reception. Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (checked live 2026-09-04, escalation #1447: its own header names it the authoritative current question list, its obs_ids match wa_obs_question_catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md). Distinct from the [VRT] Verse Reading Technique T1 -- see 'TT1 (Verse Reading Technique)'.

---

<!-- PROSE_SECTION_ID: 1120 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1254 -->

## T2 (Tier Catalogue)

[DEFINITION] [TC] Constitutional Location and Boundaries -- tier T2 of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions).

[BACKGROUND] Spirit-level location (spirit/soul/heart/mind/body), body-direction where a body link exists, origin/source, constitutional movement across levels. Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (checked live 2026-09-04, escalation #1447: its own header names it the authoritative current question list, its obs_ids match wa_obs_question_catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md). Distinct from the [VRT] Verse Reading Technique T2 -- see 'TT2 (Verse Reading Technique)'. Also distinct from the [CC] cluster_code T2 -- see the bare 'T2' entry.

---

<!-- PROSE_SECTION_ID: 1121 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1255 -->

## T3 (Tier Catalogue)

[DEFINITION] [TC] The Inner Faculties -- tier T3 of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions).

[BACKGROUND] Perception, cognition, memory, affect, creativity, volition, agency, moral evaluation, conscience, conscientiousness, relational capacity -- does the characteristic engage each faculty, and how. Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (checked live 2026-09-04, escalation #1447: its own header names it the authoritative current question list, its obs_ids match wa_obs_question_catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md). Distinct from the [VRT] Verse Reading Technique T3 -- see 'TT3 (Verse Reading Technique)'. Also distinct from the [CC] cluster_code T3 -- see the bare 'T3' entry.

---

<!-- PROSE_SECTION_ID: 1122 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1256 -->

## T4 (Tier Catalogue)

[DEFINITION] [TC] Relational Interfaces -- tier T4 of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions).

[BACKGROUND] Divine interface both directions (God-to-human, human-to-God), human interface (giving/receiving/boundaries), spiritual-beings interface (angelic/adversarial). Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (checked live 2026-09-04, escalation #1447: its own header names it the authoritative current question list, its obs_ids match wa_obs_question_catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md). Distinct from the [VRT] Verse Reading Technique T4 -- see 'TT4 (Verse Reading Technique)'.

---

<!-- PROSE_SECTION_ID: 1123 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1257 -->

## T5 (Tier Catalogue)

[DEFINITION] [TC] Formative and Developmental Dimension -- tier T5 of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions).

[BACKGROUND] Nature of transformation, sequence of inner states, mechanism of change, suffering/affliction, formation/sanctification, eschatological trajectory. Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (checked live 2026-09-04, escalation #1447: its own header names it the authoritative current question list, its obs_ids match wa_obs_question_catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md). Distinct from the [VRT] Verse Reading Technique T5 -- see 'TT5 (Verse Reading Technique)'.

---

<!-- PROSE_SECTION_ID: 1124 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1258 -->

## T6 (Tier Catalogue)

[DEFINITION] [TC] Structural Relationships with Other Characteristics -- tier T6 of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions).

[BACKGROUND] Co-occurrence, sequential relationships, causal/constitutive relationships, vocabulary/root sharing, distinctions from the nearest neighbouring characteristic. Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (checked live 2026-09-04, escalation #1447: its own header names it the authoritative current question list, its obs_ids match wa_obs_question_catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md). Distinct from the [VRT] Verse Reading Technique T6 -- see 'TT6 (Verse Reading Technique)'.

---

<!-- PROSE_SECTION_ID: 1125 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1259 -->

## T7 (Tier Catalogue)

[DEFINITION] [TC] Evidential and Methodological Foundation -- tier T7 of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions).

[BACKGROUND] Lexical and semantic analysis (primary terms, grammatical/semantic range, vocabulary arc), verse and literary interpretation (sentence/argument function, genre). Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (checked live 2026-09-04, escalation #1447: its own header names it the authoritative current question list, its obs_ids match wa_obs_question_catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md). Distinct from the [VRT] Verse Reading Technique T7 -- see 'TT7 (Verse Reading Technique)'.

---

<!-- PROSE_SECTION_ID: 1126 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1263 -->

## T1

[DEFINITION] Ambiguous on its own -- T1 has no [CC] cluster_code meaning (checked live 2026-09-05: T2/T3/T4 exist in that scheme, not T1). Two real, unrelated meanings exist: see 'T1 (Verse Reading Technique)' (work from the row, not the gloss) and 'T1 (Tier Catalogue)' (Definition, characteristic-grain).

[BACKGROUND] Added per escalation #1447's own finding (v2/v3): a reader hitting bare 'T1' anywhere in the project's docs had no glossary entry to check at all, unlike T2/T3 which already had (cluster_code) entries even before this build. This entry exists to be found by that search, not to declare a third meaning. The [CC] cluster_code scheme is no longer fixed at T2/T3 -- see 'T4' and the M-Code cluster entry's own background note (2026-09-05 revision) for the incremental finer-bucket series now underway.

---

<!-- PROSE_SECTION_ID: 1127 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1264 -->

## T4

[DEFINITION] T4 is the first of an incremental series of finer-grained cluster codes now being split out of T2's own rough catch-all, per the researcher's own criterion: a new bucket is justified when it serves real analytical benefit (e.g. supporting a specific tier/catalogue question efficiently) and shares one common relation across its members, at the same grain as an ordinary M-cluster (e.g. M15/Wisdom) -- not a bucket per minute distinction. T4 groups Strong's codes referring to the adversarial spiritual party -- Satan/the Devil -- a referent-identity classification, distinct from the topic-driven M-code axis: a code can carry both an M-cluster assignment and a T4 tag.

[BACKGROUND] Added 2026-09-05, correcting an earlier same-week attempt (escalation #1383) to do this kind of classification in a cfg_* table (cfg_lexical_code_class) instead — researcher's own verdict, verbatim: "assigning a special status to a strong is to use a cluster for it... this is not cfg territory." Currently 3 codes, reallocated from T2 (not newly discovered): H7854 (satan), G4567 (satanas), G1228G (diabolos). G1228H ("slanderous", the adjective sense) stays at its existing M14/Deceit assignment, a different sense. Further finer buckets (negator, connective, party-kinds) are expected to follow the same pattern as analytics identifies them -- see escalations #1499-1502.

---

<!-- PROSE_SECTION_ID: 1128 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1288 -->

## base

[DEFINITION] A base is the English word a surface text is an inflected or derived form of, when the two share the same root meaning (sought: seek; wonderful: wonder). It is itself a surface text: a base is a row of the same table as the surface that points to it, and a word with no base is its own base. A base is where surfaces of one root meaning are gathered before they are placed in collections.

[BACKGROUND] Named 'base form' in the AI question. Held in surface_term (base_id), with the evidence in surface_derivation. Everything a model decided about a base is inferential until its state is confirmed.

---

<!-- PROSE_SECTION_ID: 1129 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1289 -->

## inflection

[DEFINITION] The relation of a surface to its base when only the grammatical ending changes: tense, plural, participle, comparative, including irregular forms (wept: weep; grew: grow).

[BACKGROUND] One of three allowed base relations (inflection, derivation, none). The relation 'none' is used when the word has no base, is only an opposite or look-alike of a candidate base, or its meaning has moved away from it.

---

<!-- PROSE_SECTION_ID: 1130 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1290 -->

## derivation

[DEFINITION] The relation of a surface to its base when a different word form is made with a suffix or prefix, such as a noun from a verb or an adjective, and the core meaning stays the same (wonderful: wonder; strife: strive).

[BACKGROUND] Contrast inflection, where only the grammatical ending changes. A derived form with a changed meaning is not a derivation here (undoing is not undo).

---

<!-- PROSE_SECTION_ID: 1131 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1296 -->

## surface group

[DEFINITION] The first sorting of a surface text by what it names, as the ESV uses it: behaviour (something a person does or undergoes, an act, feeling, thought, speech or choice), inner_being_state (a standing condition or characteristic of a person or of the inner being: righteous, proud, humble, weak), entity (a thing that exists: a human, a plant or animal, God in all forms, an unseen power, or a part of any of these), or other (everything else, and any word that definitely belongs in none of the other three).

[BACKGROUND] Held in surface_term.surface_group and judged by a model, so it is inferential until confirmed. A word that says what an entity does, is like or has undergone is not an entity, even when it describes one. The surface group is not the cluster or the concept.

---

<!-- PROSE_SECTION_ID: 1132 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1292 -->

## subgroup

[DEFINITION] A subdivision of an M-code cluster that carries a label and a core description of which sense of the cluster theme it covers (for example M01-A). A (Strong's code, surface) pair was allocated to a subgroup at the clustering stage; the allocation is provisional, never a finding.

[BACKGROUND] Held in cluster_subgroup; the allocation of a pair is surface_subgroup. Subgroups served to establish the collections and play no part in nodes and observations; cluster_subgroup_code on a node is history (researcher, 2026-11-13; behaviour rules 130 and 131).

---

<!-- PROSE_SECTION_ID: 1133 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1293 -->

## collection

[DEFINITION] A set of surfaces (words and phrases) of like meaning, gathered and named for the concept they share. Every surface in scope (a word or phrase of the groups behaviour and inner_being_state that has a verse) is a member of exactly one collection; a surface is in more than one only in very rare circumstances and by the researcher's ruling. A collection is made by putting like words together: synonyms, opposites, gathered. The base is only an instrument for gathering like words, never the member; a derived form is a surface with a link of its own; a phrase is one concept, placed in one collection. The collection is the unit of study: its observations, claims and narration follow it, and each collection becomes a chapter of the narration (behaviour rules 127 and 129).

[BACKGROUND] Held in collection and collection_link; the members are surface_term rows placed by tier (core, synonym, opposite, gathered, phrase). A node carries the one collection of its surface (its own link, else through its base). Everything a model proposed for a collection is inferential until its status is confirmed.

---

<!-- PROSE_SECTION_ID: 1134 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1294 -->

## concept

[DEFINITION] A sub-chapter of a concept domain, named for what its subgroups share; the first grouping of the subgroups, a link from the base data to the narrative.

[BACKGROUND] Held in concept and concept_subgroup; a collection carries collection.concept_id. Since 2026-11-12 the narrative chapters follow collections (researcher; behaviour rule 129), so a concept is a first grouping, not a finding.

---

<!-- PROSE_SECTION_ID: 1135 -->
<!-- PROSE_SECTION_TYPE: glossary_programme -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Programme glossary -->
<!-- PROSE_SORT_ORDER: 1 -->
<!-- PROSE_VERSION: 1295 -->

## concept domain

[DEFINITION] A domain of the concept grouping: the basis the researcher ruled on 2026-10-31 for the narrative, with domains as chapters and concepts as sub-chapters.

[BACKGROUND] Held in concept_domain, loaded from the v1 specification iba/docs/concept-mapping-spec-v1-20261031.json by grouping the existing subgroups. Since 2026-11-12 the narrative chapters follow collections (researcher; behaviour rule 129); the domains are a first grouping, not a finding.

---

<!-- PROSE_SECTION_ID: 1066 -->
<!-- PROSE_SECTION_TYPE: glossary_contentious -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Contentious glossary -->
<!-- PROSE_SORT_ORDER: 2 -->
<!-- PROSE_VERSION: 1 -->

## role

[DEFINITION] The role of a word in an observation: what the word is for that finding, judged from its verse and never from a cluster tag. On a node the roles are characteristic and qualifier (relevant to the inner being), object, relational_target and enactment (they bear on the finding), and standalone, which records that the word was recognised and has no inner-being role (cfg_setting reading.node_roles; behaviour rule 130).

[BACKGROUND] Held in ib_node.role. It is a different column from verse_span_index.role, an older linguistic classification with an overlapping vocabulary. This entry is in the contentious glossary: the researcher settles it.

---

<!-- PROSE_SECTION_ID: 1068 -->
<!-- PROSE_SECTION_TYPE: glossary_contentious -->
<!-- PROSE_BOOK: Word Index and Glossary -->
<!-- PROSE_CHAPTER: Glossary -->
<!-- PROSE_CHAPTER_NO: 1 -->
<!-- PROSE_SECTION_TITLE: Contentious glossary -->
<!-- PROSE_SORT_ORDER: 2 -->
<!-- PROSE_VERSION: 1 -->

## owner term

[DEFINITION] In the term-driven verse-analysis method: the term currently being worked through its full processing order (its anchor verse's passage first, then every one of its verses).

[BACKGROUND] A processing-order concept. CLAUDE.md's XREF architecture separately defines OWNER (wa_term_inventory.term_owner_type) as which registry canonically holds a Strong's number's classification, as opposed to an XREF copy. To resolve: check whether an XREF-classified term is ever batch-processed this way in practice — if XREF terms are never processed as an "owner term," the two concepts likely coincide and could merge into one sense; if they are, they're genuinely different and need distinct names.

---
