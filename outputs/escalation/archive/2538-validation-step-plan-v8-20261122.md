# Validation after stage 4: principles and proposal

Escalation #2538, 2026-11-22. Not built. The researcher is still clearing the principles and will read the proposal as a whole afterwards. Sources: the researcher's instructions of 2026-11-22 (quoted on #2538), `cfg_method_rule` (IB-01 to IB-06, LR-03, LR-04, RS-02, RS-04, RW and RG rules), `cfg_behaviour_rule` B:130 to B:134, `iba/app/lib/observationrecord.py`, `iba/app/lib/layerinner.py`, and read-only queries of this session. **Proposed** marks my additions; **open** marks what is not settled.

## 1. Principles settled so far

1. **Scope.** All observations in the study related to the collection, excluding deleted observations and nodes: a) refers to the collection; b) refers to a verse in it; c) refers to a strong that is part of it (a member surface with its lettered Strong's code); d) its meaning relates to it. Nodes reaching into other collections and verses are included, because each observation and node must be verified as traceable; when the other collection is analysed, its validation includes all the observations related to it, these nodes among them.
2. **Repair first, delete last.** Restate so it is true and founded (a restatement that changes the meaning is validated against the base data); complete node columns where it can be done; consolidate duplicates; delete a node only when it cannot be referenced and another node gives the observation its context; delete an observation only when it is meaningless for the study and cannot be made true.
3. **Two markers only:** evidence (observations about the data) and inner being (observations about the working of the inner being, based on the evidence; building blocks of the stage 5 claims, not claims). The marker is not the node's role and not the observation's tag.
4. **The marker follows content and purpose, not stage.** The stored data is not consistent with B:132, so an observation that is not stage 4 may be marked inner being, without rejecting it, as long as it has evidence traces.
5. **Evidence is verse-based by definition.** An observation without a verse cannot be evidence. If it says something with inner-being implications it is inner being and needs a trace to something that supports it. An observation that is neither is highlighted for the researcher's separate ruling.
6. **Every inner-being observation has trace nodes to its evidence**, and a rule sets this as an expectation.
7. **Every older observation is evaluated** and marked.
8. **Two validations, never concurrent** (evidence, then inner being), each with its own completeness check; an inner-being observation must not reference deleted evidence; what is expected and acceptable differs by layer.
9. **An orphaned trace node is deleted only after checking that a valid node stands in its place.**
10. **No older observation is discarded without a clear verification that it has been consumed** into a current observation. The mapping record is held in `ib_observation_change` (agreed).
11. **Where an inner-being observation is grounded in the data itself, the evidence observation is created** (the researcher's suggestion), provided it is not noise: the researcher needs to understand what these observations contribute (section 4).
12. **The 26 deleted observations with no delete record stay deleted;** their observation notes are updated so they do not surface again (section 7).

## 2. The marker (proposed)

- **Name and home.** A column `nature` on `ib_observation`, governed by `cfg_enum ib_observation.nature`: `evidence` and `inner_being`. Empty means not yet judged. It is not called layer or stage (both words are in use) and not role.
- **Who sets it.** Only the validation, from reading the wording against the base data and the observation rules. Each setting is recorded in `ib_observation_change` (column `nature`, old and new value, the reason in words).
- **The neither case (principle 5).** An observation that cannot be evidence (no verse, or it states nothing about the data) and says nothing of the inner being is not given a marker. The validation lists it with its wording and its reason in a ruling list for the researcher (proposed: a recorded state `for_ruling` that holds the empty value and appears in the validation's report until the researcher rules). The completeness check treats an empty marker with no ruling state as a failure, and a `for_ruling` observation as pending, not failed.
- **The separating test, applied to the wording.** Evidence states what the data are or show, tied to a verse: a word's sense, form and grain in it, the structure, the grouping, which words stand together, what the verse says in its setting. Inner being states how something works in the inner being: an operation or state, what it is directed at, who bears it, its route, its qualification, the relation between inner operations. An observation that states both is split (one finding per observation, RO11) and each part marked.

## 3. The trace rule (proposed wording)

> **IB-07 inner-being-observations-trace-to-evidence.** Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence. A traced node never points at a deleted observation. The rule applies to every stage and to the earlier pipeline. An inner-being observation without evidence is repaired first: the evidence is found and traced, or written as an evidence observation and traced, or the observation is restated. It is deleted only when it cannot be made true, with the reason. An evidence observation is not required to trace; it is tied to a verse.

Under principle 11 the earlier option "grounded in the data itself without an evidence observation" is dropped: the evidence observation is created.

## 4. Are the created evidence observations noise? (the researcher's question)

**What a created evidence observation must contribute (proposed test).** It states a fact about the data that is not stated anywhere else in the evidence and that the inner-being observation relies on: a word's sense or grain in this verse, a form, a structure, a grouping, a relation between words. It is tied to its verse and words, one finding, and never repeats the verse or the dictionary sense (B:131, RW-04). If any of that fails it is not created: the existing evidence is traced, or the inner-being observation is restated onto what the evidence does state.

**Guards against noise (proposed).**
1. Find first: the stage 1 and stage 3 observations already state the sense, grain and grouping of every word of the collection (for thought, 177 sense rows and 7 groups). The trace goes to those when they carry the fact. A new evidence observation is made only when none does.
2. The duplicate test (B:131) applies to it as to every observation.
3. The pilot reports, for each collection, how many evidence observations were found and how many were created, with the list of the created ones and the inner-being observation each serves. The researcher judges the noise from that list, not from my description.

**An illustration, not a finding.** I read 14 of the older observations on 1Chr.28.9 (prior-capture, engagement) and judged each by wording only; this is my reading, inferential (B:4), on one verse, and not validated.
- Most prior-capture rows are sections of the earlier document that quote several verses as support (for example "4.1 Serving with all the heart and all the soul", "10.7 Choosing and setting direction"). They are neither tied to this verse nor one finding, and read as inner-being themes. By section 5 they are candidates to be consumed by the current inner-being observations, or split.
- A few are about this verse alone and say something inner-being (for example 17167, God's rejection of the one who forsakes; 20019, God sees the intention). They are inner being and need a trace: for forsake the stage 1 evidence of its collection is the first place to look.
- Some are working notes: 19915 ("Carried since #1986") and 17271 ("[Claude reading] The translators move between heart, soul, spirit and mind...") state nothing about this verse's data or its inner being. These would go on the ruling list.
- The two engagement rows (21752 'searches', 21757 'seek') classify the word's use in the verse. 'seek' says the seeking is the inner operation (inner being); 'searches' says it bears on the inner being without being the operation, which is a statement about the word's role. Both need the marker judged and are the kind of case the evidence layer must carry.
- In this sample I would not expect many new evidence observations to be needed, because the thought build already holds evidence for every word of the collection. I cannot say that for the whole scope until the marking is done.

## 5. How the older observations will be judged (proposed)

Each older observation in scope goes through five steps, recorded in `ib_observation_change`:
1. **Compliance with the observation rules** (RO11, RW-02 to RW-11, RS-08, B:131): one finding; founded in the verse and base data; not a restatement of the verse or the dictionary sense; concise and verse-specific; tied to verses and words with a node on each; parts, tag and basis valid; a role on each word node.
2. **Truth against the base data:** the verse, the lexicon's three meaning sources, the structure.
3. **Marker:** evidence, inner being, or neither (the ruling list), by the test in section 2.
4. **Consumption check.** Find the current-method observations whose nodes cover its occurrences and read whether they carry its meaning. Record what the old observation says, which current observation carries each part, and any part not carried. The outcome is one of: consumed completely (deleted, with the carrying observations named); consumed in part (the uncarried part is restated into an existing or new observation, then the old one deleted as consumed); not consumed and valid (kept, marked, traced if inner being); not founded or not true (marked in its comment and deleted); cannot be decided (held for the researcher with the evidence).
5. **Verification before any consumed deletion.** A deletion for consumption is allowed only when a record exists naming the carrying observations and the mapping, and a check confirms each carrying observation is live and every occurrence the old observation's nodes name is on a live node of a carrying observation, or the record states why that node is not carried. Nothing is deleted in bulk. The first run is a pilot on a sample, and the researcher sees the deletions with their mapping before the run is extended.

**A tool constraint.** `merge_observation` refuses a merge unless the two texts are the same (`merge_same_text_only`). A consumption deletion needs its own function that confirms or moves the nodes, writes the mapping record (`ib_observation_change`, column `consumed_by`, new value the carrying ids, the mapping as the reason), and deletes only after the check in step 5.

**Candidate pool for thought (structural only, not a meaning test).** 615 older observations (every stage except lexical, layer-1, layer-2 and layer-3) have a live node on thought's 351 verses. For 272 every word node sits on an occurrence a current-method observation already covers; for 175 some do; for 168 none do or they have no word node. By stage (every word covered / some / none or no word node): prior-capture 168/158/93, strand-reading 53/7/19, engagement 29/9/22, verse-reading 16/1/10, char-answers 4/0/22, char-reading 1/0/2, char-subgroup 1/0/0.

## 6. What is expected and acceptable, by layer (proposed)

| aspect | evidence | inner being |
|---|---|---|
| what it states | what the data are or show, tied to a verse; one finding; concise, verse-specific, never a restatement | how something works in the inner being, based on the evidence; a building block of a claim; one finding; never a restatement of the verse |
| true against | the base data | the evidence it traces, and the base data when read back or when a restatement changes the meaning |
| trace | not required | required by IB-07 |
| word nodes | verse_reference, verse_lexical_id, surface, strong, morph_code, role, collection_id; subgroup_id once the surface is placed, else empty with its reason | the same, with an inner-being role |
| acceptable missing | a column the data cannot give, with its reason in `disposition_note`; a recorded none with its reason where the item allows | a recorded not-used or not-gathered with its reason (IB-04) |
| coherence | with the other evidence of the same verse and word | with the other inner-being observations of the collection and the evidence under them |
| completeness check | every word of the collection by surface and lettered Strong's code has its stage 1 observations; every subgroup its stage 3 observations; every in-scope occurrence a node with a role; every in-scope observation marked or on the ruling list; no live observation without a live node; no live node on a deleted observation; no two of one meaning | every inner-being observation traced to live evidence; no reference to deleted evidence; every in-scope observation marked or on the ruling list; no live node on a deleted observation; no two of one meaning; no consumed deletion without its verified record |

## 7. The dangling traces and the 26 undocumented deletions

93 live traced nodes on 81 live observations point at 46 deleted observations, all from the earlier pipeline. For 79 of the 81 no valid traced node stands in place. Each is first marked (section 5, step 3). Evidence: the dead trace is dropped. Inner being: it is repaired by tracing to valid evidence, restated, or deleted as unfounded.

Of the 46 deleted targets, 20 have a logged delete reason and 26 have none. The 26 stay deleted (principle 12). Their notes are updated so they do not surface again. **Tool gap:** `modify_observation` refuses an observation that is already deleted, and no function annotates one, so the update needs a function in the validation build (tested on a copy, under a named snapshot), not a direct write; I have not touched the data. Proposed note wording for each, as a new `revisit_note` on the deleted observation and a record in `ib_observation_change`: "Deleted before delete records were kept; the reason was not recorded. Confirmed by the researcher on 2026-11-22 to stay deleted. A trace that points here is handled by the validation." The ids are the 26 whose deleted target has no `deleted` row in `ib_observation_change` (all verse-reading), listed by the check at run time. The wording does not state a reason that was not recorded.

## 8. Order of work, one collection at a time

1. Evidence validation: structural tests for the whole scope; reading batched by verse; record; evidence completeness check.
2. Gate: the inner-being validation opens only when the evidence check passes.
3. Inner-being validation: marker, traces, reading, record, then its completeness check.
4. A later evidence change reopens only the inner-being rows it touches.
5. Registered in config as a routine of `Collection-Build.ps1`, tested on a copy under a named snapshot with counts predicted and checked; B:132 and B:133 amended for principle 4; documentation in GOVERNANCE.md, USER-GUIDE.md and BUILD.md (E:12). Pilot on thought.

## 9. Scope for thought (collection 56), read-only

a) 785 observations; b) 1,180 (contains a); c) 775 (inside a); d) by reading, unmeasured.

## 10. Points still open

1. The `for_ruling` state for an observation that is neither (section 2): the name, and whether the ruling list is a report or a recorded state.
2. The test for a created evidence observation (section 4) and the pilot report that lets the researcher judge the noise.
3. The wording of the note on the 26 deleted observations (section 7).

## 11. Limits

Counts are from read-only queries in this session; d) is unmeasured; the coverage figures are structural and say nothing about meaning. The illustration in section 4 is one verse, my reading, unvalidated. The proposal is not for approval until the researcher has cleared the principles.
