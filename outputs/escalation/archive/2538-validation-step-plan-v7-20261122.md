# Validation after stage 4: principles and proposal

Escalation #2538, 2026-11-22. Not built. The researcher is still clearing the principles and will read the proposal as a whole afterwards. Sources: the researcher's instructions of 2026-11-22 (quoted on #2538), `cfg_method_rule` (IB-01 to IB-06, LR-03, LR-04, RS-02, RS-04, RW and RG rules), `cfg_behaviour_rule` B:130 to B:134, `iba/app/lib/observationrecord.py`, `iba/app/lib/layerinner.py`, and read-only queries of this session. **Proposed** marks my additions; **open** marks what is not settled.

## 1. Principles settled so far

1. **Scope.** All observations in the study related to the collection, excluding deleted observations and nodes: a) refers to the collection; b) refers to a verse in it; c) refers to a strong that is part of it (a member surface with its lettered Strong's code); d) its meaning relates to it. Nodes reaching into other collections and verses are included, because each observation and node must be verified as traceable; when the other collection is analysed, its validation includes all the observations related to it, these nodes among them.
2. **Repair first, delete last.** Restate so it is true and founded (a restatement that changes the meaning is validated against the base data); complete node columns where it can be done; consolidate duplicates; delete a node only when it cannot be referenced and another node gives the observation its context; delete an observation only when it is meaningless for the study and cannot be made true.
3. **Two markers only:** evidence (observations about the data) and inner being (observations about the working of the inner being, based on the evidence; building blocks of the stage 5 claims, not claims). The marker is not the node's role and not the observation's tag.
4. **The marker follows content and purpose, not stage.** The researcher agrees with B:132 in principle but the stored data is not consistent with it, so there is room for an observation that is not stage 4 to be marked inner being without rejecting it, as long as it has evidence traces.
5. **Every inner-being observation has trace nodes to its evidence**, and a rule sets this as an expectation.
6. **Every older observation is evaluated** and marked.
7. **Two validations, never concurrent** (evidence, then inner being), each with its own completeness check; an inner-being observation must not reference deleted evidence; what is expected and acceptable differs by layer.
8. **An orphaned trace node is deleted only after checking that a valid node stands in its place.**
9. **No older observation is discarded without a clear verification that it has been consumed** into a current observation.

## 2. The marker (proposed)

- **Name and home.** A column `nature` on `ib_observation`, governed by `cfg_enum ib_observation.nature` with two values: `evidence` and `inner_being`. Empty means not yet judged. It is not called layer or stage (both words are in use for other things) and not role (a node's role).
- **Who sets it and when.** Only the validation sets it, from reading the observation's wording against the base data and the observation rules. Each setting is recorded in `ib_observation_change` (column `nature`, old and new value, reason in words), the existing append-only record.
- **Completeness rule.** An observation in scope of a validated collection holds a value; an empty value fails that collection's completeness check.
- **The test that separates the two, applied to the wording:** *evidence* states what the data are or show: a word's sense, form and grain, the structure, the grouping, which words stand together, what a verse says in its setting. *Inner being* states how something works in the inner being: an operation or state, what it is directed at, who bears it, its route, its qualification, the relation between inner operations. An observation that states both is split (one finding per observation, RO11), each part marked.
- **Not a third class.** RS-04 allows an observation whose wording shows it is not verse understanding to be "left exactly as it is with the reason". Under two markers that outcome has no place. **Open:** what is done with such an observation (for example a recorded open question or a data error): consume it into one that is, or keep it without a marker.

## 3. The trace rule (proposed wording)

A new rule in `cfg_method_rule`, registered with the validation step and checked by its completeness check:

> **IB-07 inner-being-observations-trace-to-evidence.** Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, or is grounded in the data itself (see below). A traced node never points at a deleted observation. The rule applies to every stage and to the earlier pipeline. An inner-being observation without evidence is repaired first: the evidence is found and traced, or the observation is restated. It is deleted only when it cannot be made true, with the reason. An evidence observation is not required to trace.

**Inner-being observation with no obvious evidence (the researcher's second point).** Where the observation itself is the evidence because it refers to the verse and the word, my recommendation is that no evidence observation is created for the plain verse text, and one is created where the observation relies on a fact about the data beyond the verse text (a word's sense, its grain, its form, the structure, the grouping). Basis: B:131 and RW-04 forbid an observation that repeats the verse; an evidence observation of "the verse says X" would be that, and would be the noise the researcher is concerned about. The grounding is then the observation's own word nodes (each carries a `verse_lexical_id` for the occurrence), and the validation records in the observation's comment what base data it rests on. Where the observation relies on a data fact that no evidence observation states, that fact is written as an evidence observation and traced. The researcher's leaning is towards creating the evidence layer in these cases; this is the narrower form, for decision. **Open.**

## 4. How the older observations will be judged (proposed)

Each older observation in scope goes through five steps, in this order, recorded in `ib_observation_change`:

1. **Compliance with the observation rules** (RO11, RW-02 to RW-11, RS-08, B:131): one finding; founded in the verse and base data; not a restatement of the verse or the dictionary sense; concise and verse-specific; tied to verses and words with a node on each; parts, tag and basis valid; a role on each word node.
2. **Truth against the base data:** the verse, the lexicon's three meaning sources, the structure.
3. **Marker:** evidence or inner being, by the test in section 2.
4. **Consumption check.** Find the current-method observations whose nodes cover its occurrences and read whether they carry its meaning. Record what the old observation says, which current observation carries each part, and any part not carried. The outcome is one of:
   - consumed completely: it is deleted, with the carrying observations named;
   - consumed in part: the uncarried part is restated into an existing or a new observation (repair first), then the old one is deleted as consumed;
   - not consumed and valid: it is kept, marked, and traced if inner being;
   - not founded or not true: it is marked as such in its comment and deleted;
   - cannot be decided: held for the researcher with the evidence for the case.
5. **Verification before any consumed deletion.** A deletion for consumption is allowed only when a record exists naming the carrying observations and the mapping, and a check confirms: each carrying observation is live; every occurrence the old observation's nodes name is on a live node of a carrying observation, or the record states why that node is not carried. Nothing is deleted in bulk. The first run is a pilot on a sample, and the researcher sees the list of deletions with their mapping before the run is extended.

**A tool constraint to know.** The existing merge (`merge_observation`) refuses a merge unless the two texts are the same (`merge_same_text_only`); the older observations will mostly differ in wording from the current ones. A consumption deletion needs its own function that moves or confirms the nodes, writes the mapping record, and deletes only after the check in step 5. The mapping record is proposed as rows in `ib_observation_change` (column `consumed_by`, new value the carrying ids, reason the mapping), not a new table. **Open.**

**How large the candidate pool is for thought (structural indicator only, not a meaning test).** 615 older observations (every stage except lexical, layer-1, layer-2 and layer-3) have a live node on thought's 351 verses. For 272 of them every word node sits on an occurrence that a current-method observation already covers; for 175 some do; for 168 none do, or they have no word node. Whether their meaning is carried is decided only by reading. By stage (every word covered / some / none or no word node): prior-capture 168/158/93, strand-reading 53/7/19, engagement 29/9/22, verse-reading 16/1/10, char-answers 4/0/22, char-reading 1/0/2, char-subgroup 1/0/0.

## 5. What is expected and acceptable, by layer (proposed)

| aspect | evidence | inner being |
|---|---|---|
| what it states | what the data are or show; one finding; concise, verse-specific, never a restatement | how something works in the inner being, based on the evidence; a building block of a claim; one finding; never a restatement of the verse |
| true against | the base data | the evidence it traces, and the base data when read back or when a restatement changes the meaning |
| trace | not required | required by IB-07 |
| word nodes | verse_reference, verse_lexical_id, surface, strong, morph_code, role, collection_id; subgroup_id once the surface is placed, else empty with its reason | the same, with an inner-being role |
| acceptable missing | a column the data cannot give, with its reason in `disposition_note`; a recorded none with its reason where the item allows | a recorded not-used or not-gathered with its reason (IB-04) |
| coherence | with the other evidence of the same verse and word | with the other inner-being observations of the collection and the evidence under them |
| completeness check | every word of the collection by surface and lettered Strong's code has its stage 1 observations; every subgroup its stage 3 observations; every in-scope occurrence a node with a role; every in-scope observation marked; no live observation without a live node; no live node on a deleted observation; no two of one meaning | every inner-being observation traced to live evidence or recorded as grounded in the data; no reference to deleted evidence; every in-scope observation marked; no live node on a deleted observation; no two of one meaning; no consumed deletion without its verified record |

## 6. The dangling traces (principle 8, checked)

93 live traced nodes on 81 live observations point at 46 deleted observations, all from the earlier pipeline. For 79 of the 81 no valid traced node stands in place. Each is first marked (step 3 above). Evidence: the dead trace is dropped. Inner being: it is repaired by tracing to valid evidence, restated, or deleted as unfounded. Of the 46 deleted targets, 20 have a logged delete reason (out of scope, every node out of scope, withdrawn) and 26 have no delete record in `ib_observation_change`. **Open:** record a reason retroactively for those 26, or leave.

## 7. Order of work, one collection at a time

1. Evidence validation: structural tests for the whole scope; reading batched by verse; record; evidence completeness check.
2. Gate: the inner-being validation opens only when the evidence check passes.
3. Inner-being validation: marker, traces, reading, record, then its completeness check.
4. A later evidence change reopens only the inner-being rows it touches.
5. Registered in config as a routine of `Collection-Build.ps1`, tested on a copy under a named snapshot with counts predicted and checked; B:132 and B:133 amended for principle 4; documentation in GOVERNANCE.md, USER-GUIDE.md and BUILD.md (E:12). Pilot on thought.

## 8. Scope for thought (collection 56), read-only

a) 785 observations; b) 1,180 (contains a); c) 775 (inside a); d) by reading, unmeasured.

## 9. Points still open

1. What is done with an observation that is not verse understanding (section 2).
2. Whether an evidence observation is created where an inner-being observation is grounded in the data itself (section 3; my recommendation is the narrow form).
3. Where the consumption mapping record is held (section 4; proposed `ib_observation_change`).
4. The 26 deleted observations with no delete record (section 6).

## 10. Limits

Counts are from read-only queries in this session; d) is unmeasured; the coverage figures are structural and say nothing about meaning. The proposal is not for approval until the researcher has cleared the principles.
