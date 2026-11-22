# Validation after stage 4: two validations, one for each layer

Escalation #2538, 2026-11-22. Not built; for the researcher's approval (B:17). Sources: the researcher's instructions of 2026-11-22 (quoted on #2538), `cfg_method_rule` (IB-01 to IB-06, LR-04, RS-02, RS-04, RW-01 to RW-11, RG rules), `cfg_behaviour_rule` B:130 to B:134, `iba/app/lib/layerinner.py`, and read-only queries of this session. Items marked **proposed** are mine; items marked **open** are not settled by the record.

## 1. What the researcher has set

1. **Scope.** All observations in the study related to the collection (a: refers to the collection; b: refers to a verse in it; c: refers to a strong that is part of it, meaning a member surface with its lettered Strong's code, the rule of stage 1, B:132; d: its meaning relates to it). Deleted observations and nodes are excluded. For thought: a 785, b 1,180 (contains a), c 775 (inside a); d is added by reading.
2. **Repair first, delete last.** Restate an observation so it is true and founded; a restatement that changes its meaning is validated against the base data. Complete node columns where they can be. Consolidate duplicates (one kept, one deleted with its reason). Delete a node only when it cannot be referenced and another node still gives the observation its context. Delete an observation (and its nodes) when it is meaningless for the study and cannot be made true.
3. **Two layers, two validations, never concurrent.** An evidence validation and a claim validation. Each has its own completeness check. A claim observation must never reference deleted evidence. What is expected and what is acceptable differ by layer (section 3).

## 2. The two layers (proposed definitions)

- **Evidence layer.** Observations that state what the dictionary, the verses and the stored structure show: stage 1 (lexical), stage 3 (layer-1 and layer-2) of the current method, and the earlier observations that pass the evidence validation. They carry no inner-being role or route (B:132). Their base is the base data.
- **Claim layer.** The stage 4 observations (stored as stage layer-3): the elements, behaviours and cross-collection working that the claims read. They make no claim themselves (stage 5 is undecided; IB-02, IB-04). Their base is the evidence observations they rest on, through traced nodes, with occasional reading back into the base data.
- **Background (proposed third class).** An earlier observation whose wording shows it is not verse understanding is left as it is with its reason (RS-04). It is neither evidence nor claim input.

Note: RS-04 says the stage "is never used to filter"; the nature of an observation is judged by its wording. So the class is a recorded value set by the validation from reading each observation, not inferred from the stage name. The stored stage names do not match the method's numbering (stage 4 is stored as layer-3), which is a further reason for an explicit value.

## 3. What is expected and acceptable, by layer

| aspect | evidence validation (first) | claim validation (second) |
|---|---|---|
| what the observation states | What the dictionary, the verses and the structure show; no inner-being role, route or claim (B:132). One finding per observation (RO11, RW-03); concise and verse-specific, never a restatement of the dictionary sense or the verse (RW-04, B:131). | A building block of the inner-being analysis: an element of a subgroup (3.1), a behaviour discovered in the collection (3.2), the working across collections (3.3). No claims (IB-02, IB-04). Never restates the verse. |
| what it is true against | The base data: the verse text, the lexicon's three meaning sources, the stored structure and the surface grouping. | The evidence observations it rests on (does it follow from them), and the base data only when read back or when a restatement changes its meaning. |
| nodes required | Word nodes: verse_reference, verse_lexical_id, surface, strong, morph_code, role, collection_id; subgroup_id once the surface is placed, otherwise empty with its reason. | The same word-node columns with a stage 4 role (a node with any other role is refused), plus at least one traced node on an observation the row may rest on. Word nodes lie within the occurrences the traced observations cover, or the read-back is recorded (IB-02, IB-06). |
| what is acceptable as missing | A column the data cannot give, stated in `disposition_note`; a recorded none with its reason where the item allows it (LR-03). | A recorded not-used or not-gathered with its reason in words (IB-04); no behaviour recorded as none with its reason. A traced node is never empty and never points at a deleted observation. |
| coherence | With the other evidence observations of the same verse and word (one word, two senses, one grain per lettered Strong's code, RG-21). | With the other claim observations of the collection and the evidence under them: 3.3 with 3.2 with 3.1; no two building blocks that say the same thing. |
| restating | Against the base data. | Against the evidence it traces; against the base data too when the meaning changes. |
| when evidence moves | Not applicable. | If the evidence validation deletes or restates an observation that a claim observation traces, the claim observation is repaired (rested on the restated or other evidence) or withdrawn if nothing true is left; the affected ledger rows reopen (B:134). |
| completeness check | Every word of the collection, by surface and lettered Strong's code, has its stage 1 observations; every subgroup has its stage 3 observations (1.1, 1.2, 2.1 ledger rows answered and validated); every in-scope occurrence has a node with a role; no live observation without a live node; no live node on a deleted observation; no two live observations of one meaning. | Every evidence observation of the subgroup is rested on or declared not used; every 3.1 observation is gathered into a behaviour or declared not gathered; at least one behaviour or a recorded none; every traced node on a live observation; no claim observation without live evidence; no live node on a deleted observation; no two of one meaning. |
| the existing check that applies | LayerCheck rows for steps S1, 1.1, 1.2, 2.1 (LR-04). | LayerCheck rows for steps 3.1, 3.2, 3.3 (IB-06). |

## 4. The earlier (legacy) observations

They are in the scope and go through the evidence validation (RS-04, IB-05): each is accepted, modified, deleted, merged, or left as it is with its reason, and nothing is physically deleted. Node columns by kind are as in the table; for the older stages a role that is empty is judged per observation and filled by reading, or the node is deleted under repair-first. The history columns cluster_code and cluster_subgroup_code are noise and are not completed. question_code is not verified as redundant.

## 5. Order of work, one collection at a time

1. Evidence validation: structural tests for the whole scope, then reading for truth and meaning batched by verse (each verse read once with all its observations). Record, then the evidence completeness check.
2. Gate: the claim validation opens only when the evidence completeness check passes.
3. Claim validation: re-derive the claim observations and their evidence links, read, record, then the claim completeness check.
4. The stage 4 ledger stays closed only when both checks pass. A later evidence change reopens only the rows it touches.
5. Registered in config as a routine of `Collection-Build.ps1` (Pull, Record, Check for each validation), tested on a copy under a named snapshot with counts predicted and checked; documented in GOVERNANCE.md, USER-GUIDE.md and BUILD.md (E:12). Pilot on thought.

## 6. Points that are open

1. **The marker.** A recorded role on each observation (evidence, claim input, background), set by the validation. Proposed; needs the researcher's decision.
2. **Do the claims read all of stage 4, or only 3.2 and 3.3,** with 3.1 reached by tracing down. 449 of thought's 827 traced nodes already point stage 4 at stage 4.
3. **A valid earlier observation that no stage 4 observation traces.** Kept as available evidence (stage 4 does not rest on it), or should stage 4 be re-run for the subgroups where such observations exist (IB-05 says shown, not demanded). Open.
4. **The verse set for b)** is the 351 verses of nodes carrying the collection, which includes verses reached through supporting words. Open whether that is the intended set.
5. **The 93 live traced nodes that point at deleted observations** belong to the older pipeline (char-answers and verse-reading source observations). They are dangling evidence links in the legacy layer; the evidence validation either repoints or deletes them.

## 7. Limits

Counts are from read-only queries in this session; d is unmeasured. The column text of question_code and reading_id was not checked in code. The per-layer table is a proposal drawn from the rules above; the researcher's corrections to it come first.
