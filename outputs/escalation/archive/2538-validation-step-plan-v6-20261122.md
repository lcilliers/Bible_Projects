# Validation after stage 4: principles and proposal

Escalation #2538, 2026-11-22. Not built. The researcher is still clearing the principles and will read the proposal as a whole once they are settled (researcher, 2026-11-22). Sources: the researcher's instructions of 2026-11-22 (quoted on #2538), `cfg_method_rule` (IB-01 to IB-06, LR-03, LR-04, RS-02, RS-04, RW and RG rules), `cfg_behaviour_rule` B:130 to B:134, `iba/app/lib/layerinner.py`, and read-only queries of this session. **Proposed** marks my additions; **open** marks what the record does not settle.

## 1. Principles settled so far (the researcher's words, restated)

1. **Scope.** All observations in the study related to the collection, excluding deleted observations and nodes. Related: a) refers to the collection; b) refers to a verse in it; c) refers to a strong that is part of it (a member surface with its lettered Strong's code; not every verse of a strong); d) its meaning relates to it. The collection may reach into other collections and verses through nodes. Those observations and nodes are in the validation because each must be verified as traceable; when the other collection is analysed, its validation must include all the observations related to it, these nodes among them.
2. **Repair first, delete last.** Make an observation true and founded; a restatement that changes its meaning is validated against the base data. Complete node columns where it can be done. Consolidate duplicates (one kept, the others deleted with the reason). Delete a node only when it cannot be referenced and another node gives the observation its context. Delete an observation and its nodes when it is meaningless for the study and cannot be made true.
3. **Two markers only.** An observation is either **evidence** (observations about the data) or **inner being** (observations about the working of the inner being, based on the evidence). The inner-being observations are the building blocks of the claims generated in stage 5; they are not claims. The marker is distinct from a node's role (the role is the word's part in a finding) and from the observation's tag (its kind).
4. **The marker follows content and purpose, not stage.** An inner-being observation can arise at any tier and at stage 3 or stage 4; the stage is not its definition. This agrees with RS-04 ("the stage is never used to filter").
5. **Every older observation is evaluated** and marked evidence or inner being.
6. **Trace expectation.** Every inner-being observation has trace nodes tying it to its evidence. A rule must be in place that sets this as an expectation (proposed form in section 4).
7. **Two validations, never concurrent:** the evidence validation, then the inner-being validation; each ends with its own completeness check; an inner-being observation must not reference deleted evidence; what is expected and acceptable differs by layer.
8. **A trace node that is orphaned is deleted, but only after checking that a valid node stands in its place.**

## 2. What the record shows that bears on this

- **The marker has no home yet.** Nothing but the stage value separates the layers; status is draft on nearly all observations. So the marker is new (proposed: one governed value on the observation, set by the validation from its reading; name and values open).
- **B:132 conflicts with principle 4 as written.** B:132 says every observation of stages 1 to 3 states what the dictionary, the verses and the structure show, and none states what a word does for the inner being. Principle 4 allows an inner-being observation to arise at stage 3. B:132 (and B:133, which separates the lexical and inner-being analyses) would need amending if the principle stands; I have not changed either. **Open.**
- **Existing check.** `layerinner.py` already requires every stage 4 observation to hold at least one traced node on an observation the step may rest on, plus word nodes. For the earlier observations nothing requires a trace.
- **Thought stage 4 (stored as layer-3)** has 217 observations and 827 traced nodes, pointing at layer-1 66, layer-2 295, layer-3 449 and lexical 17; none points at a deleted observation.
- **Principle 8, checked for the dangling traced nodes.** 93 live traced nodes on 81 live observations point at 46 deleted observations. All belong to the earlier pipeline (verse-reading 73 observations, char-answers 8). For 79 of the 81 observations no valid traced node stands in place: every trace they hold points at a deleted observation. Two keep another traced node to a live observation. No delete record of the 46 names a merged survivor; 20 of the 46 have a logged delete reason (out of scope; every node out of scope; withdrawn); 26 have no delete record in `ib_observation_change`. So, by the researcher's test, the 79 are not simply deleted as orphans: each of those 81 observations must first be marked evidence or inner being. If evidence, a trace to another observation is not required and the dead trace is dropped. If inner being, it lacks its trace and is repaired (traced to valid evidence), restated or deleted as unfounded. For the 2, the dead trace is dropped.

## 3. What is expected and acceptable, by layer (proposed; the researcher's corrections come first)

| aspect | evidence | inner being |
|---|---|---|
| what it states | what the data show: the dictionary, the verses, the stored structure; one finding per observation; concise, verse-specific, never a restatement | the working of the inner being based on the evidence; a building block of a claim, not a claim; one finding per observation; never a restatement of the verse |
| true against | the base data (verse text, the lexicon's three meaning sources, the structure) | the evidence it traces, and the base data when read back or when a restatement changes the meaning |
| trace | not required | required: at least one traced node on a live evidence observation (rule in section 4) |
| word nodes | verse_reference, verse_lexical_id, surface, strong, morph_code, role, collection_id; subgroup_id once the surface is placed, else empty with its reason | the same, with an inner-being role |
| acceptable missing | a column the data cannot give, with its reason in `disposition_note`; a recorded none with its reason where the item allows (LR-03) | a recorded not-used or not-gathered with its reason in words (IB-04) |
| coherence | with the other evidence of the same verse and word (one grain per lettered Strong's code) | with the other inner-being observations of the collection and the evidence under them |
| completeness check | every word of the collection by surface and lettered Strong's code has its stage 1 observations; every subgroup its stage 3 observations; every in-scope occurrence a node with a role; no live observation without a live node; no live node on a deleted observation; no two live observations of one meaning | every evidence observation of the subgroup rested on or declared not used; every inner-being observation traced to live evidence; no reference to deleted evidence; no live node on a deleted observation; no two of one meaning |

## 4. The trace rule (proposed form)

A rule in `cfg_method_rule` and its check: every live inner-being observation, of any stage and of the earlier pipeline, holds at least one live traced node on a live evidence observation. It is checked by the inner-being completeness check and refuses a validated state without it. Evidence observations are not required to trace. An inner-being observation that cannot be traced is repaired (the evidence found and traced), restated, or deleted as unfounded (repair first). Open: the rule's id and wording, and where it sits in the stage 4 ledger rows, which already require it.

## 5. Order of work, one collection at a time (unchanged in outline)

1. Evidence validation: structural tests for the whole scope, then reading batched by verse (each verse once with all its observations), then record, then the evidence completeness check.
2. Gate: the inner-being validation opens only when the evidence check passes.
3. Inner-being validation: marker set for every observation, traces checked, reading, record, then its completeness check.
4. A later evidence change reopens only the inner-being rows it touches.
5. Registered in config as a routine of `Collection-Build.ps1` (Pull, Record, Check for each validation), tested on a copy under a named snapshot with counts predicted and checked; documented in GOVERNANCE.md, USER-GUIDE.md and BUILD.md (E:12). Pilot on thought.

## 6. Scope for thought (collection 56), read-only

a) 785 observations; b) 1,180 (contains a); c) 775 (inside a); d) by reading, unmeasured. The verse set for b) is the 351 verses of nodes carrying the collection; per principle 1 it includes reached verses and collections.

## 7. Points still open

1. The marker's name, values and column; the amendment of B:132 and B:133 for principle 4.
2. The wording and place of the trace rule.
3. How the marker is judged for an older observation: by reading its wording (RS-04), with which test separating "about the data" from "about the working of the inner being".
4. The 26 deleted observations with no delete record, which still carry live traces: record the reason retroactively, or leave.

## 8. Limits

Counts are from read-only queries in this session; d) is unmeasured. The proposal is not for approval until the researcher has cleared the principles.
