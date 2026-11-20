# #2510 Stage 3, the verse-lexical observations (draft v2, 2026-11-19)

Status: DRAFT by Claude for the researcher to scrutinise. It describes stage 3 as built (B:132, B:133, B:134; `cfg_setting layer.reading`, steps 1.2 and 2.1; `iba/app/lib/layerreading.py`; USER-GUIDE, the layered reading of a collection) and corrects v1 against the researcher's review of 2026-11-19 (#2510 v18). What is built is stated as built; what the researcher's review settled is stated as settled; any inference is labelled (B:4). Nothing is built or changed.

## 1. What stage 3 is for

Stage 3 records the **words' context**: what the other words of the verse, and the verse's stored structure, show with each group of surfaces. It answers "what do the words used say here", is checkable against the text, and never states what a word does for the inner being (B:132, B:133). It is the evidence base for stage 4, the inner-being analysis made from the stage 3 observations. Stage 3 and stage 4 observations are different observations, not one observation read two ways (researcher, 2026-11-19).

## 2. The outcome of stage 3 for a collection

Stage 3 is complete for a collection when every aspect the data demands is answered by an observation with its nodes, or by a recorded none with its reason where the item allows it, and each answer is validated by `LayerCheck` (B:134). Concretely, the collection then holds:

| Aspect (ledger item) | Step | One row for each | Present when |
|---|---|---|---|
| strong-enrichment | 1.2 | surface group | always (a none is not allowed) |
| pairing | 2.1 | surface group and partner collection | they share at least 3 verses (`pair_min_verses`) |
| qualifier | 2.1 | surface group | a qualifier stands with the group in its verses |
| entity | 2.1 | surface group | an entity is named or referred to in its verses |
| direction | 2.1 | surface group | the group has entities (the direction the text states) |
| group-relation | 2.1 | pair of groups | they share at least 3 verses (`relation_min_verses`) |
| double-meaning | 2.1 | surface of a group | the surface carries two or more Strong's codes |

Source: `layerreading.derive`, lines 139 to 196. Each observation carries nodes: the occurrences it holds for (the group's occurrences in its verses, and for a pairing the partner words in the shared verses), each with its verse reference, surface, Strong's code, morph code, collection and subgroup. Because the nodes are built from the data, the set of observations and nodes of stage 3 is the complete verse-lexical account of the collection, and stage 4 reads it.

What stage 4 is handed: for every verse of every group, the group's meaning and codes (1.2); the words standing with it, with side and distance (pairing); the qualifiers and the word each reaches; the entities named; the direction the text states; the relation to the other groups; the faces. A stage 4 reading that finds a stage 3 observation wrong does not correct it in place: it returns the case to stage 3 (the move and re-answer rules of B:134: a re-answered row withdraws its earlier observation with the reason).

## 3. The unit of reading for stage 3

The unit is the **surface group** of one collection, read through the verses in which its surfaces stand. Every stage 3 row is keyed by (item, group, subject) (`collection_layer_item`): the group is the unit, and the subject is the partner collection (pairing), the other group (relation) or the surface (double meaning). A row is read over the group's occurrences, verse by verse, in the shared verses for pairings and relations. The reading is by Claude from the evidence in the working file, with the researcher scrutinising (B:127); no bulk or templated writing is a substitute (B:127).

The unit is not the word (stage 1: the surface with its lettered Strong's code), not the collection as a whole (the gate), and not the cluster (retired from nodes and observations, #2495). A group's observations are found through the subgroup on its nodes (`ib_node.subgroup_id`).

## 4. How the surface groups are generated, and what they are for in stage 3

**Generation (stage 2, built).** The surfaces of a collection are grouped by their dictionary meaning, judged from the Strong's meaning of the words: a group is the surfaces that mean the same or the same kind of thing, named for that meaning. `Collection-Build.ps1 -Action GroupPull` writes a working file with one row for each live index row (surface, each Strong's code with its lexicon evidence, the occurrences, the link tier); Claude judges each surface and fills the group, reason, certainty and, for a surface with more than one sense, a group for each code; `GroupRecord` validates the whole file and writes the groups and placements in one transaction with a scrutiny report for the researcher (method rules GP-01 to GP-04; `lib/collectiongroup.py`). A surface whose meaning is not the collection's is set aside with its reason. Nothing in the grouping judges what a word does for the inner being (B:132).

**Purpose for stage 3.**
1. The group is the unit every stage 3 row is keyed on (section 3); without the grouping, stage 3 does not open (`grouping_gate`: every surface placed or isolated, every group holding a surface).
2. The group's meaning is what makes a pairing, a qualifier or a direction comparable: the words that stand with the group are read against one meaning, not against a scatter of surfaces.
3. Step 1.2 validates the grouping against the Strong's codes of its members. A surface found wrongly placed is moved by the collection change procedure (B:129, B:134), the step reopens and the ledger rows the new grouping demands are added.

## 5. How the observations and nodes are written (built)

1. **Open.** `LayerOpen -Collection <name> -Step 1.2|2.1`: refuses until stage 1 is closed and the grouping is finished and the previous step is closed; derives the ledger rows from the data (a second open changes nothing; an aspect the data no longer demands is retired).
2. **Pull.** `LayerPull -Collection <name> -Step <step>`: writes the working file with each open row's evidence (the occurrences, the partners, the stored structure, the lexicon) and an empty fill, up to 80 nodes shown for each row.
3. **Read and fill (Claude, in the session).** For each row either `disposition observed` with `obs_text` of at least 40 characters, and `basis` (`stated`: the data states it, or `read`: read from the verse), or `none` with a `reason` of at least 10 characters where the item allows it (not for an enrichment). The text states what the lexicon, the verses and the stored structure show: it names its verses by reference, does not copy more than the verse-words limit (`reading.observation_items max_verse_words_copied`), does not restate the dictionary range, states for a qualifier the word it reaches ("adjacency is not scope") and, for an entity, who is named and how the text refers to them; it says nothing of what a word does for the inner being (B:131, B:132).
4. **Record.** `LayerRecord -File <file> [-Check]`: checks the whole file (a problem anywhere refuses all) and writes in one transaction the observations (stage `layer-2` for 2.1, `layer-1` for 1.2; kinds `enrichment`, `pairing`, `relation`, `face`), their nodes and the ledger answers. Nodes are built from the data, never typed: the group's occurrences (role `member`, default `lexical`) and the partners in the shared verses (role `partner`), each with verse reference, `verse_lexical_id`, surface, Strong's code, morph code, collection and subgroup (B:130). A row answered again withdraws its earlier observation with the reason (soft delete, `ib_observation_change`).
5. **Check.** `LayerCheck -Collection <name>` validates every answered row against the tables (stage, kind, nodes equal to the demanded occurrences, roles, collection, every Strong's code of an enrichment), sets `validated` and writes a versioned report naming the gates, what is open, what failed, and what the data demands that has no row. A step is closed when every row is answered and validated.

## 6. What the outcome says about the additions v1 proposed

v1 section 4 listed candidates. Read against the outcome in section 2 (the researcher: define the outcome and what is to be adopted follows):

| v1 candidate | Result | Basis |
|---|---|---|
| 1 Grammatical form of each word (stem, tense, voice, number) | Already carried: the morph code is on every node and in the working file; it is evidence read within the qualifier, pairing and direction observations, not a new item. Whether the observation text must state it is for the item's question to say; nothing new to build. | `layerreading._word_row` reads `morph_code`; `ib_node.morph_code` (inference: the sufficiency of the morph code for stage 4 is labelled inferential until stage 4 is defined) |
| 2 Grammatical function of each word in its clause | Already carried as side and distance in the pairing and as the word a qualifier reaches; no separate item. | `layer.reading` items `pairing`, `qualifier` |
| 3 Rendering check against the original | Belongs to stage 1 (the word read from the lexicon and the verses), not to stage 3. | `word-sense` item, step S1 |
| 4 Passage and genre of each verse | Dropped. The passage register is retired (project map, section 2); the verse-bounded reading stands. | Project map section 2; B:116 |
| 5 Stage 3 closes before stage 4 opens | Adopted, as settled below. | Researcher, 2026-11-19 |

## 7. Settled by the researcher's review (2026-11-19)

1. **Stage 3's closure is a gate for the collection.** A collection's stage 3 is closed only when every row of steps 1.2 and 2.1 is answered and validated.
2. **Stage 4 is not gated until all of stage 3 is completed.** Stage 4 does not open until stage 3 is complete. (Inferential reading, B:4: that "all of stage 3" means every step of stage 3 for the collection, following the collection as the unit of B:132 and B:127. If the researcher means every collection, the check is the same applied to all collections; the config will carry whichever is stated when stage 4 is built under its own design, B:105.)
3. **Stage 3 and stage 4 observations are separate and usually different**: the grammatical qualifier is a stage 3 observation; what it gives the characteristic in place is a stage 4 observation.

## 8. What is not decided

Stage 4 is not built and not defined in config; stage 5 is not decided (`governance.programme_stages`). Where this draft says what stage 3 hands to stage 4, it is the record of stage 3's side only.
