# Validation after stage 4: principles and proposal (v9)

Escalation #2538, 2026-11-22. Not built. The researcher is still clearing the principles and will read the proposal as a whole afterwards. Sources: the researcher's instructions of 2026-11-22 (quoted on #2538), `cfg_method_rule` (IB-01 to IB-06, LR-03, LR-04, RS-02, RS-04, RW and RG rules), `cfg_behaviour_rule` B:130 to B:134, `iba/app/lib/observationrecord.py`, `iba/app/lib/layerinner.py`, read-only queries, and the two pilot reports (`2538-validation-pilot-pull-thought-v1-20261122.md`, `2538-validation-pilot-reading-1chr-28-9-v1-20261122.md`). **Proposed** marks my additions; **open** marks what is not settled. v8 is in `archive/`.

## 1. Principles settled

1. **Scope.** All observations in the study related to the collection, excluding deleted observations and nodes: a) refers to the collection; b) refers to a verse in it; c) refers to a strong that is part of it (a member surface with its lettered Strong's code); d) its meaning relates to it. Nodes reaching into other collections and verses are included, so each is verified traceable; when the other collection is analysed its validation includes every observation related to it, these among them.
2. **Repair first, delete last.** Restate so it is true and founded (a restatement that changes the meaning is validated against the base data); complete node columns; consolidate duplicates; delete a node only when it cannot be referenced and another node gives the observation its context; delete an observation only when it is meaningless for the study and cannot be made true (comment first, then deleted).
3. **Two markers only:** evidence (about the data) and inner being (about the working of the inner being, based on evidence; building blocks of the stage 5 claims, not claims). Not the node's role, not the tag.
4. **The marker follows content and purpose, not stage.** A non-stage-4 observation may be inner being as long as it has evidence traces.
5. **Evidence is verse-based by definition.** An observation that says something with inner-being implications is inner being and needs a trace.
6. **Every inner-being observation has trace nodes to its evidence;** a rule sets it (section 3).
7. **Every older observation is evaluated** and marked.
8. **Two validations, never concurrent** (evidence, then inner being), each with its own completeness check; an inner-being observation never references deleted evidence; expectations differ by layer (section 6).
9. **An orphaned trace node is deleted only after checking that a valid node stands in its place.**
10. **No older observation is discarded without verified consumption.** The mapping is held in `ib_observation_change`.
11. **A created evidence observation must earn its place** (section 4).
12. **The 26 deleted observations with no delete record stay deleted;** their notes are updated so they do not surface again (section 7).
13. **(New, 2026-11-22) An observation that is neither evidence nor inner being is deleted:** it contributes nothing to the purposes of the observations. Comment first, then deleted. There is no ruling state: the validation lists each one in its report with its reason, after checking that every verse fact it states is held by a live observation or is true of the verse.
14. **(New, 2026-11-22) Every finding is acted on.** The objective is to fix and re-align, not to leave issues standing. A finding stays open only when a named later validation will touch the observation (another collection owns its subject): then the observation carries a recorded deferral (the collection, the finding, the date) and the completeness check accepts it as deferred, not as failed. A finding with no named owner must be closed in this validation. A correction that is verified against the base data is made now even on an observation that is deferred; what is deferred is only what needs the owning collection's own evidence (consumption, completing that collection's nodes).

## 2. The marker (proposed)

- **Home.** A column `nature` on `ib_observation`, governed by `cfg_enum ib_observation.nature`: `evidence`, `inner_being`. Empty means not yet judged. The earlier holding value `for_ruling` is dropped (principle 13).
- **Who sets it.** Only the validation, from the wording against the base data. Each setting is logged in `ib_observation_change` (column `nature`, old and new value, reason).
- **Test.** Evidence states what the data are or show, tied to a verse. Inner being states how something works in the inner being: an operation or state, what it is directed at, who bears it, its route, its relation to other inner operations. One that states both is split (one finding per observation) and each part marked. One that states neither is deleted (principle 13). The pilot shows the test is workable: of 55 observations, 29 evidence, 20 inner being, 6 neither; the marker did not follow stage (prior-capture holds both kinds, four layer-3 observations are evidence by content because they report only word distances).

## 3. The trace rule (proposed wording)

> **IB-07 inner-being-observations-trace-to-evidence.** Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, unless it is self-evidencing: it quotes its verse or verses in full and holds a word node for every word it relies on. A traced node never points at a deleted observation. The rule applies to every stage and to the earlier pipeline. A trace points first at an existing evidence observation; an evidence observation is created only when none states the fact. An inner-being observation without evidence is repaired first (evidence found and traced, or created and traced, or restated); it is deleted only when it cannot be made true, with the reason. An evidence observation is not required to trace; it is tied to a verse.

The pilot found 15 of 20 inner-being observations on 1Chr.28.9 without a trace; 5 (all layer-3) trace.

## 4. Created evidence observations: the noise test (pilot result)

An evidence observation is created only when it states a fact about the data that no existing evidence states and that the inner-being observation relies on, and that the nodes and the quotation do not already carry. Pilot, 1Chr.28.9:
- **Earns its place (3):** who does what to thoughts (subject, verb, object across Ps.139.2, 1Chr.28.9, Isa.66.18, Ps.94.11, 1Cor.3.20, Luke.5.22, Matt.9.4, Heb.4.12, with Ps.139.23 as a petition); seek before find, with 1Chr.28.9 a condition and Isa.65.1 the finding given to those who did not seek; the timing "before I have brought them" in Deut.31.21, tied to H3336. Each draft's quotations were verified verbatim in `verse`.
- **Noise (1):** #19501 (the whole verse quoted, a node for every word); it is self-evidencing and needs none.
- **Existing evidence suffices (1):** #20019 traces to #12412 (H3336 across verses).
The pilot report of each collection lists the evidence observations found and those created, with the inner-being observation each serves, so the researcher can judge noise from the list.

## 5. Judging the older observations (proposed, with pilot results)

Five steps per observation, recorded in `ib_observation_change`: (1) compliance with the observation rules; (2) truth against the base data; (3) marker; (4) consumption check; (5) verification before any consumed deletion. Added from the pilot:
- **Split before anything else** when an observation holds more than one finding (4 on 1Chr.28.9: #17270, #20455, #20489, #20498).
- **Consumption is recorded (`consumed_by`) only when a live observation states every fact the old one states and the old one adds nothing the new one lacks.** On 1Chr.28.9 no older observation could yet be shown consumed by the thought build; their facts belong to other collections (search, intend, forsake, serve, desire). They stay live and marked, with a recorded deferral to the owning collection (principle 14). The expected "most are consumed" holds collection by collection.
- **Consolidating an observation that another traces** re-points the trace to the surviving observation's own sources; two pairs in layer-3 (#22524/#22604, #22525/#22608).
- **A claim stronger than its verse is restated to the verse** and checked (#7319, #7320, #12431, #17167, #20549); codes not in the verse are corrected (#5797).

**Tool constraints.** `merge_observation` accepts only same text. New functions are needed: consume (confirm or move nodes, write the `consumed_by` record, delete only after the check), split, consolidate with trace re-pointing, restate for any stage, annotate a deleted observation, and delete with comment first. Each is tested on a copy under a named snapshot (B:29, B:46).

## 6. What is expected, by layer (proposed)

| aspect | evidence | inner being |
|---|---|---|
| states | what the data are or show, tied to a verse; one finding; never a restatement | how something works in the inner being, based on evidence; one finding; a building block |
| true against | the base data | the evidence it traces, and the base data when a restatement changes meaning |
| trace | not required | IB-07 |
| word nodes | verse_reference, verse_lexical_id, surface, strong, morph_code, role, collection_id; subgroup_id once placed, else empty with its reason | the same, with an inner-being role |
| acceptable missing | a column the data cannot give, with its reason in `disposition_note` | a recorded not-used or not-gathered with its reason (IB-04) |
| coherence | with the other evidence of the verse and word | with the other inner-being observations and the evidence under them |
| completeness | every word has its stage 1 observations; every subgroup its stage 3; every in-scope occurrence a node with a role; every in-scope observation marked; no live observation without a live node; no live node on a deleted observation; no two of one meaning; every finding closed or deferred to a named collection | every inner-being observation traced to live evidence or self-evidencing; no reference to deleted evidence; every in-scope observation marked; no two of one meaning; no consumed deletion without its verified record; every finding closed or deferred |

## 7. Dangling traces and the 26 undocumented deletions

93 live traced nodes on 81 live observations point at 46 deleted observations, from the earlier pipeline (none in thought's own scope). For 79 of 81 no valid trace stands in place. Each is marked first; evidence: the dead trace is dropped; inner being: traced to valid evidence, restated, or deleted as unfounded (principle 2). Of the 46 deleted targets, 20 have a logged delete reason and 26 none; the 26 stay deleted and their notes are updated by a new function (none annotates a deleted observation today), wording: "Deleted before delete records were kept; the reason was not recorded. Confirmed by the researcher on 2026-11-22 to stay deleted. A trace that points here is handled by the validation." The 26 are found at run time (deleted target with no `deleted` row in `ib_observation_change`).

## 8. Action for each finding of the pilot (principle 14)

| finding (1Chr.28.9) | observations | action now | deferred to |
|---|---|---|---|
| neither evidence nor inner being | #19613, #19915, #20029, #20345, #20414, #20427 | comment with reason, then deleted (principle 13); first check that each verse fact stated is true and held by a live observation (all verified true; H5068 in 1Chr.29.17 of #20427 to be checked at run time) | none |
| untrue or stronger than the verse | #7319, #7320, #12431, #17167, #20549 | restate to the verse, check against the base data, log | none |
| codes not in the verse | #5797 | correct to M30 and M12 and M34 as the verse carries them; split the "spine" sentence into an inner-being observation traced to it | none |
| count and omission | #22623 | restate nine verses (ten occurrences), add 1Chr.28.9 "serve" 12 before | none |
| meaning duplicates | #22524 into #22604; #22525 into #22608 | consolidate; re-point the traces of #22604 and #22608 to the survivors' sources; record `consumed_by` | none |
| compound | #17270, #20455, #20489, #20498 | split; the "God and Jesus know thoughts" claim consumed into #12431 once restated and traced | the other claims go to their owning collections (below) |
| inner being without trace | 15 (section 3) | trace to existing evidence (#12412 for #20019); create the three evidence observations of section 4; #19501 self-evidencing; the rest restated or traced as their reading shows | none for thought's subjects |
| text without nodes | #7317, #21752, #19613, #20029 | add the nodes for the cited verses where the verse is in the collection's scope or restate to the nodes held | cited verses of other collections: that collection |
| node columns empty | role on 13 nodes, collection on 3 | complete from the reading of the observation; where the data cannot give it, the reason in `disposition_note` | none |
| older observations on other collections' subjects | seeking (H1875): #5793, #5797, #7091, #7303, #7317, #7319, #7320, #21752, #21757; plan H3336 (intend): #12412, #12413, #20019 trace; forsake: #17167, #19508; serve: #16318; willing (desire): #17012; heart: #17057, #17270, #17271 | corrections that are verified now (above); marker set; a recorded deferral on the observation | consumption and node completion by the collection that owns the subject: search (156), intend (78), forsake (47), serve (24), desire (9), heart (102) |

## 9. Order of work, one collection at a time

1. Evidence validation: structural tests for the whole scope; reading batched by verse; actions of section 8; record; evidence completeness check.
2. Gate: the inner-being validation opens only when the evidence check passes.
3. Inner-being validation: marker, traces, reading, actions, record, its completeness check.
4. A later evidence change reopens only the inner-being rows it touches.
5. Build: the functions of section 5; `nature` column and `cfg_enum`; rule IB-07; the deferral record; routine of `Collection-Build.ps1`, test plan with predicted counts on a copy under a named snapshot; amend B:132 and B:133 for principle 4; GOVERNANCE.md, USER-GUIDE.md, BUILD.md. Pilot on thought, extended to the whole scope only after the researcher has seen the 1Chr.28.9 actions applied on the copy.

## 10. Scope for thought (collection 56), read-only

a) 785 observations; b) 1,180 (contains a); c) 775 (inside a); d) by reading. Structure: 1,212 of 15,784 word nodes miss a required column (all but 11 in the older pipeline); 0 dead traces and 0 exact-text duplicates inside the scope; 9,577 nodes reach into 158 other collections (their observations are in scope, principle 1).

## 11. Points still open

None of principle. For the researcher's reading of the whole: the deferral record's form (a row in `ib_observation_change` with column `deferred_to`, or a column on the observation) and whether a deferral lapses when the owning collection is never run. I propose the change-record row, with a completeness line in each collection's report that lists deferrals addressed to it.

## 12. Limits

Only 1Chr.28.9 was read (my reading, inferential, B:4). The copy holds the marker and its log only: nothing was restated, split, consolidated, created or deleted, and none of the functions is built. Hebrew sense claims were not checked against the meaning tree. The proposal is not for approval until the researcher has read it as a whole.
