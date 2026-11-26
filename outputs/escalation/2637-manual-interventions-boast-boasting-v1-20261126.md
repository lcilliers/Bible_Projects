# #2637 Manual interventions on boast, subgroup boasting (v1, 2026-11-26)

Every place where Claude had to act outside the package's own commands while running the loop of
subgroup boasting (#2620), so that the methods can be updated to carry it. Each item says what
happened, where (run id or escalation), and what the package would need. Nothing here is built
(B:105); it is the input to the design for developer mode.

All database writes went through `Collection-Build.ps1` Read*/Record* commands. The interventions
are in the work between a pull and a record, and in the follow-up after a refusal.

## A. Across every step

| # | Intervention | Evidence | What the package would need |
|---|---|---|---|
| A1 | Packages are too large to read whole (S1 49-55k chars, 2.1 up to 77k, 3.1 158k). Claude wrote compact viewers (`show.py` to `show5.py` in the scratchpad) to print each word, occurrence, verse and older observation on one line. | every Read* of #2620 | A compact view of each package, from the package command itself. |
| A2 | Claude wrote its answers into the answer file with scratch Python (`fill_s1a/b/c.py`, `fill_senses.py`, `fill_enrich.py`, `fill_dm.py`, `fill_rows.py`, `fill_byref.py`, `fill_ev.py`, `build_elems.py`) and JSON specs (`spec_*.json`). | every Record* of #2620 | A way to give the judgement only (text, basis, grounds, the observations or verses it rests on, the disposition of each older observation) and have the package build the answer file. |
| A3 | Claude's scripts checked coverage before recording (every occurrence in exactly one reading, every older observation answered once, every observation to take up rested on or declared). The recorder checks the same, but only at record, one fault list per attempt. | assertions in the fill scripts | A pre-check that lists all coverage gaps before the record. |
| A4 | Each refused answer file raised a self-correctable escalation automatically (14: #2622-#2627, #2629-#2636). Claude closed each by hand with ResolveSelfCorrectable, using a loop script (`resolve.ps1`). | #2622-#2636 | A refusal of a read answer belongs to the run, not the escalation table. It could be logged on the ledger row and cleared when the same row records. If it stays an escalation, it could close by itself when the row later validates. |
| A5 | The rules that refused files were found by failing; several are not in the package instruction (see C1, C3, C4, F2, G3, G4, G5). | the 14 refusals | Every rule the recorder enforces stated in the package instruction, with its exact form. |
| A6 | Read-only checks of the database were written as scratch Python files (`q1.py` to `q15.py`). Inline `python -c` fails under PowerShell's quoting. | this session | A read-only query entry point for ad-hoc checks, or the needed facts in the packages (see G1). |
| A7 | The point-of-use rules hook refuses the first use of each operation and the whole chained command. On one occasion a fill step in the same command did not run, and the record was previewed on the empty template (#2632). | #2632 | Not a method fault. Noted so that fills and records are not chained with a first use. |

## B. Grouping (GroupPull, GroupRecord)

| # | Intervention | Evidence | What the package would need |
|---|---|---|---|
| B1 | The grouping file was filled by editing the JSON in PowerShell: placeholders replaced (`decided \| uncertain`), the seed group names renamed to the chosen subgroups, definitions written. | RUN-20261126_103335_978 | A grouping answer form: surface, subgroup, reason, certainty; the groups list built from it. |
| B2 | Rule conflict decided ad hoc. The pull says a surface with no pair is a subgroup of its own; the seed rule says a word family stays together. boastful (base boast, in WordNet, no pair in the collection) was placed alone and marked uncertain. | #2620 v4 | The precedence between the two rules stated in config (a decision for the researcher). |
| B3 | After GroupRecord, Claude ran Manifest-Rebuild by hand, because the output says to run it to register the scrutiny report. | RUN-20261126_103344_253 | Registration done by GroupRecord itself. |
| B4 | LayerNext named step 3.2 for the collection before it was grouped. Claude found the true state by querying the tables. | #2621, RUN-20261126_103059_757 | The fix of #2621. |

## C. S1, the words (ReadWords, RecordWords)

| # | Intervention | Evidence | What the package would need |
|---|---|---|---|
| C1 | Verse references had to be in the package's own form (Zep, Psa, Jam, 1Th, Obd); Zeph, Ps, Jas and 1Thess were refused as not naming the verse. | #2622 | The form stated in the instruction, or common forms accepted. |
| C2 | A text copying more than 7 consecutive verse words was refused, five times in S1. | #2624 | A pre-check of the copy limit on each text before the record. |
| C3 | Grounds of a read observation must be one unbroken run of the words of one verse: no morph code, no lexicon words, no two phrases joined by a semicolon. This is not stated. | #2622, #2625; `iba/app/lib/layerreading.py` lines 863-873 | Stated in the instruction; the check message to say one unbroken phrase of one verse. |
| C4 | Merge was refused because the texts differ. The instruction says merge is for an observation saying the same; the code takes only identical text. Claude used consume instead. | #2623 | The instruction and the code to agree: merge for the same meaning, or the instruction to say identical text. |
| C5 | A consume naming an uncarried occurrence never matches on the words path (string keys not converted). Claude used carry to 1.1 instead. | #2626, #2627, #2628 | The fix of #2628. |
| C6 | A consume must cover the older observation's occurrences in later packages of the same subgroup, which have no nodes yet. Observation 15200 could not be consumed in S1, so it was carried to 1.1. | #2626, #2627 | The answer to an older observation held until all its occurrences in the subgroup are read, or carriers allowed from the whole subgroup. |
| C7 | Older observations were judged into recurring classes by hand: process notes ("batch 3", "read in batch"), pointer notes (chapter or section numbers, cluster codes, thread ids), count notes (hits, verses), table fragments, a bare label with a quote, a heading. Each was deleted as neither or consumed, and each case was reasoned afresh. | S1 and 2.1 answers of #2620 (for example 15282, 15201, 15323, 15263, 16693, 17336, 15290, 18958) | The classes named in config, with the action each takes, and the package marking the candidates of each class. |
| C8 | A data error (Psa 10:3, the surface boasts stored also on H3588A, the conjunction for) could only be named in the text at S1 and 2.1; the flag item exists only at 3.1. | 23708, 3.1 finding f18 | A data-quality flag available at S1. |

## D. 1.1 and 1.2 (ReadSenses, RecordSenses, ReadEnrichment, RecordEnrichment)

| # | Intervention | Evidence | What the package would need |
|---|---|---|---|
| D1 | The partition of 52 S1 observations into senses, with a check that each is carried once and every occurrence placed, was done in a scratch script. | RUN-20261126_104809_837 | The coverage pre-check of A3. |
| D2 | The lexicon of the rarer codes (H3588A, H8597, H6286A and others) was printed separately, because the package cuts each entry. | RUN-20261126_104810_936 | The full sense head and meaning range of each code in a compact block. |

## E. 2.1, the structure (ReadStructure, RecordStructure)

| # | Intervention | Evidence | What the package would need |
|---|---|---|---|
| E1 | The row asks for side and distance; the package gives one structure line per word. Claude computed positions of the boast word and the partner word with a script (`show5.py`) for all 69 pairing rows. | pairing packages of #2620 | The position, side and distance of each partner occurrence from the subgroup's word, in the package. |
| E2 | Findings must name every occurrence of the row once. Claude mapped verse references to occurrence ids with a script (`fill_byref.py`). | 2.1 records of #2620 | The coverage pre-check of A3, and verse references accepted per finding (the instruction allows them). |
| E3 | The copy limit refused a pairing text again. | #2629 | As C2. |
| E4 | Partner words of a collection used only grammatically (order in "in order to", will as a future, return in "in return for", presence) were written as pairing findings, then declared not used at 3.1. | 23740, 23750, 23827 | A form-only disposition at 2.1. |

## F. Sweep and evidence validation (ReadSweep, ReadEvidence, RecordEvidence)

| # | Intervention | Evidence | What the package would need |
|---|---|---|---|
| F1 | The sweep with nothing to read exits with code 3 and raises an escalation, though it answers its row; Claude resolved it as not a fault. | #2630 | Exit 0 and no escalation when the sweep is empty. |
| F2 | The restate action was refused for a `nature` parameter; its parameters are not listed in the instruction. | #2631 | The parameters of each validation action listed in the package. |
| F3 | Claude caught an unchecked superlative (15197, "most frequent", B:36) and a universal claim wider than the verses read (15298). The code has no check for them. | RUN-20261126_110000_236 | A check that flags superlatives and universal words (most, never, no verse, always) for the reader to confirm. |
| F4 | 262 observations were read in 7 batches of 40, each verdict written by hand into a spec file. | RecordEvidence runs of #2620 | The answer form of A2. |

## G. 3.1, the elements (ReadElements, RecordElements)

| # | Intervention | Evidence | What the package would need |
|---|---|---|---|
| G1 | The package does not say which of the subgroup's occurrences each observation covers. Claude queried `ib_node` directly (`occmap.py`) to know where a finding may put occurrence nodes. | RUN-20261126_110008_622 | The covered occurrences of each observation in the package. |
| G2 | Nodes were assembled by script (`build_elems.py`): the occurrences of the traced observations, each with its role, then the traced nodes. | RUN-20261126_110334_762 | The answer form of A2: the finding names what it rests on and the role, and the package builds the nodes. |
| G3 | A finding of kind qualification needs a node with the role qualifier. The row may name only the subgroup's own occurrences, so the qualifier words (partners) cannot be named. Claude wrote the three role findings as statements. This is a conflict between RG-04 (qualification applies to the qualifier and the characteristic) and the 3.1 occurrence rule. | #2633, #2634, #2635 | A design decision for the researcher: partner occurrences allowed in 3.1 for a qualification, or qualification removed from the 3.1 kinds. |
| G4 | A finding whose nodes all bear on an act (all enactment) is refused. This is not stated; the enactment item practically needs a characteristic node. | #2636 | Stated in the instruction. |
| G5 | The polarity values and the route values (A, B, C) are not in the answer template. Claude guessed pursuit and chose the routes. | 3.1 answer of #2620 | The allowed values in the template. |
| G6 | A finding must carry at least one occurrence node, and the item kinds, modes and flag types come from `reading.observation_items`. Claude read that setting directly. | scratchpad q13.py | The item parts in the package `uses` block (it gives kinds and bases only). |

## H. After the loop

| # | Intervention | Evidence | What the package would need |
|---|---|---|---|
| H1 | The summary of the loop (ledger counts, senses, elements, repairs, open items) was written by a scratch script (`mkreport.py`). | outputs/escalation/2620-boast-boasting-loop-v1-20261126.md | A loop report per subgroup from the package. |
| H2 | The escalations raised by refusals were found by querying the table by date. | scratchpad q14.py, q15.py | Covered by A4. |
