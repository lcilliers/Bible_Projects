# #2507 The observation rules against the recorders: audit (v1, 2026-11-15)

Asked by the researcher (2026-11-15): "can you confirm that the observation rules have been built into the process and agrees with the rules we spent such a long time to design previously (both for lexical and inner being)". Answer after reading the rules (B:130, B:131, RW-01 to RW-11, RG-17 to RG-22, RS-04, RS-08, RS-10, `reading.observation_rules`, `reading.observation_items`) and the code of both writers: the shared pipeline `lib/observationrecord.py` (used by the readings and Engagement, the inner-being side) and `lib/layerreading.py` (the layered reading, the lexical and the layer steps). **Not confirmed as first built; the gaps found are listed and the mechanical ones are closed in this build (BUILD 538).**

| Rule | Lexical and layer steps (`layerreading.py`) | Inner being (`observationrecord.py` through the readings, Engagement) |
|---|---|---|
| B:130 node: occurrence, collection, role, group | enforced: nodes are built from the data, never typed | enforced (check, write, Node-Check) |
| B:130 a node does not exist without a live observation | **was broken** for a re-recorded single observation (nodes stayed live); fixed, tested | node deletion is its own act (RS-04); reported by Node-Check |
| B:131 not a repeat of the verse text (`max_verse_words_copied` 7) | **was enforced for S1 only; now for every layer item**; caught two real restatements in the pilot | enforced |
| B:131 tied to its verses | by nodes for every item; the text must also name them for the lexical item (`tie_to_verse`) | by nodes |
| B:131 interprets what its verse says, founded in it | **not mechanical**: a reading judgement; failed once (dictionary restatement), found by the researcher | not mechanical |
| B:131 the same wording never two observations | enforced (exact text) | enforced (exact text) |
| RW-01 changes only by a reading, with the reason | enforced (`ib_observation_change`) | enforced |
| RW-02 the eight kinds and the structured parts | the lexical kinds term and face are two of the eight; the layer kinds group, enrichment, pairing, relation are outside the eight by the researcher's G4 ruling; `parts` is `item`, `step`, `word`, `grounds`, not the nine items | enforced (`check_item_parts`, the nine items) |
| RW-03 one observation, a node for each variant | enforced | enforced |
| RW-04 concise, verse-specific, never the dictionary sense, a transliteration never without its gloss | verse-specific enforced; **dictionary restatement and the gloss are not mechanical**: the item text says it and the pilot was re-recorded with every transliteration glossed | same |
| RW-05 span-grounded | enforced (the occurrence) | enforced |
| RW-06 references resolved fresh | enforced | enforced |
| RW-08 several readings, each its own observation | enforced for S1 (one observation for each sense, covering every occurrence) | by reading |
| RW-09 a re-read sees what is recorded | **S1 only; now every pull shows the existing observations on the occurrences** | enforced |
| RS-08 a read observation names its grounds in the words of the verse | **was missing; now enforced** (`grounds` is required for basis read, and must be words of the verses the observation is tied to) | enforced |
| Quotations are the ESV's wording | **was missing; now enforced** (the quote check of the readings) | enforced |
| RG-17 a prompt that does not apply is not answered | prompts are given by catalogue code; none is forced | by reading |
| RG-21 grain, RG-22 function words | enforced (a word is a surface and lettered code; function-word-only words are no row, a negator stays) | RG-21 by reading |
| RW-11 missing data is named as a gap | not built for the lexical items | RO4, by reading |
| RG-20 read back against the verse | not mechanical (a procedure) | not mechanical |
| RS-08, RS-10 the nine items, one observation for each, the verse always has an operation | not applicable to the lexical stage | enforced for Analysis_phase_1 |
| The inner-being analysis from the lexical observations (stage 4) | **not built**: no recorder, no items, no rules for it yet | n/a |

What stays judgement and is therefore the reader's to hold (and the researcher's to scrutinise): that an observation interprets what its verse says and is not the dictionary range; that a transliteration is glossed; the read-back. The tests that carry the mechanical rules are `temp_2505_layers_test_run.py` (47 of 47) and `temp_2507_alignment_test_run.py` (11 of 11).
