# #2510 Open questions: one list (v1, 2026-11-20)

This is the single list of Claude's open questions from the work of #2510. None is answered here (researcher's instruction, 2026-11-20): each is to be woven in at the stage it belongs to as the study proceeds through stages 3 and 4. A question states what is not settled, and where the evidence was searched it names the document. Documents named are working documents in `outputs/escalation/`; the answers belong in the database and the prose.

## Stage 1: the lexical analysis

| # | Question | Where it arises |
|---|---|---|
| 1 | How is stage 1 divided for volume? The order in which the 169 collections are taken, and how the word rows of one large collection are split across sessions (the pull and the record are whole-file; the ledger lets a step stay partly answered, as `thought` shows with 10 of 177 rows answered). No batch size or resume rule is configured. | stages document section 6 |
| 2 | What is done about the anomalies found in the `thought` stage 1 run: a stored surface on a code it does not seem to belong to (H1961 in Eze 19:10, G1161 in Rom 2:3, H0413 in Jer 40:4 and others)? | #2508 |

## Stage 2: the grouping of the surfaces

| # | Question | Where it arises |
|---|---|---|
| 3 | Do the 10 subgroups of `thought` stand, are they rolled back, or are they re-made? What did the run of 2026-11-15 get wrong: the method (dictionary meaning), the output, or the purpose the groups were built for? The comparison report `collection-groups-thought-v1-20261115` against the groups named at #2463 v16 has not been read in this work. | #2509 v6 and v7; stages document sections 3 and 4 |
| 4 | What are the subgroups for, in the researcher's own words, in stage 3 and in stage 4? The record gives the reasoning of #2463 v16 and v18 (a concept of like-meaning surfaces; one observation for the set; the verses travelling with it through the nodes), which was said before the stages were re-cut on 2026-11-15. | project map section 8 point 3; stages document section 4 |
| 5 | How does the subgroup relate to the `concept` and `concept_subgroup` tables, which hold a level above the collection? The record says only that "the DB already provides for it". | #2463 v18 (d) and v20 |
| 6 | The 69 surfaces with no surface group and the 56 not yet judged: are they in or out of the collections? | stages document section 7 |
| 7 | A surface set aside in stage 2 (its meaning is not the collection's): what is it read for afterward? In layer 2 its occurrences are skipped without a row, a record or a failed check, and the researcher's rule that a word is bound with its partner or excluded has no recorded step that excludes it with a record. | stages document section 7 |

## Stage 3: the verse-lexical observations

| # | Question | Where it arises |
|---|---|---|
| 8 | Is a pairing or relation of fewer than 3 shared verses meant to be unread? No row is demanded for it. | `layer.reading` thresholds; stages document section 7 |
| 9 | Does "stage 4 is not gated until all of stage 3 is completed" mean every step of stage 3 for the collection, or every collection? Read here as the first, and labelled inferential. | stage 3 draft v3 section 7 |
| 10 | Is stage 3 taken for a collection as a whole, or subgroup by subgroup? | stages document section 6 |
| 11 | Is the morph code, which every node already carries, sufficient as the evidence of the grammatical form of a word for stage 4? Labelled inferential. | stage 3 draft v3 section 6 |

## Stage 4: the inner-being analysis

| # | Question | Where it arises |
|---|---|---|
| 12 | Is stage 4 crafted as the stage 4 draft proposes: the working as one observation over several nodes, with new parts for the bearer, the form (act, state or movement), the effect and the context, and an item for the condition of a being? | stage 4 draft section 8, 1 |
| 13 | Which of the Analysis_phase_1 items, node roles and nuance rules carry over to stage 4, and which are retired? | stage 4 draft section 8, 2 |
| 14 | Are the interventions of the stage 4 draft section 4 steps of the read, and what is the standing of the by-role guide in stage 4? | stage 4 draft section 8, 3 |
| 15 | Does the three-phase order of the stage 4 draft section 5 apply? | stage 4 draft section 8, 4 |
| 16 | The stage 4 batch: its size, who judges, and how a failure is recorded. | stage 4 draft section 8, 5 |
| 17 | What is the role of the subgroup in stage 4? Inferred only: the unit at which the inner-being role is stated, bound with its partner. | stages document section 4 |

## Stage 5 and the account

| # | Question | Where it arises |
|---|---|---|
| 18 | How is the narrative structured against the collections? B:127 and B:129 say each collection becomes a chapter section; the researcher called 169 sub-chapters enormous and said the groupings should come from the claims, which would require those rules to be amended. | project map section 8 point 1; #2486 |
| 19 | How are claims formulated and assembled in stage 5, and how are the existing claims cross-linked to the collections and re-evaluated against the observations? | #2486; work index |
| 20 | How are the existing per-cluster science reviews (files under `Workflow/Sciences/science_files/`) used in the claims reading, given that loading them into a reading was never built? | project map section 3D |

## The prose and the record

| # | Question | Where it arises |
|---|---|---|
| 21 | The rewritten prose is in the database as draft. Which sections does the researcher approve, and which does the researcher correct? | this session |
| 22 | The pointers of `cfg_prose_concept` still name cluster-era terms and none points to collection, the layered reading, the node and observation model, or the narrative. They are configuration rows, changed through Propose. | gap list v2 section 3 |
| 23 | The section types of the old Session A to D slots keep their old codes (for example `prog_instr_session_a`); only the headings were changed. A new or renamed type needs the researcher's instruction (B:55). | gap list v2 section 3; B:55 |
| 24 | The round trip of `Prose.ps1 -Step ImportChapter` tags the author of an imported section as `researcher`. The sections rewritten in this work were reset to `claude_code`; earlier sections edited by the same route also carry `researcher` and their authorship has not been checked. | `prose_section.author` |
| 25 | The 87 draft entries of the programme glossary, and the entry `cluster`, which is defined only as the M-code cluster. | gap list v2 section 3 |
| 26 | The session-close check that keeps the project map current (the researcher's decision D3 on #2510) is not built; it needs its own design. | #2510 |
| 27 | The researcher's count of 56 versions of #2510 is not explained; the database holds 21. | #2510 v20 |

## Held escalations that carry decisions

#2448 (approve the change list and test plan for the final reading by collections, including the migration of the `reading` table's home cluster), #2486 (binding values, the claim work-up list, scope, evidence stance, the placement of planning in the skeleton), #2506 (configuration findings: an orphan, a drift, a glossary currency finding, an unresolved hedge phrase), #2507 (D1 to D4 of the lexical observations design), #2509 (approval of the grouping method). Their own records state what each needs.
