# #2538 — The validation built into the collection build: plan for approval (v1, 2026-11-24)

Researcher, 2026-11-24, in chat: "the next step of the build is to ensure that all the validation work you did previously are built into the collection build code to ensure that the validation steps are an integral part of the build, and not an after the fact corrective action." Nothing is built. This file states what I understood, what each piece of the validation becomes in the build, the increments, the tests and the points I need decided (rule B:17).

## 1. What I understood

Everything the validation after stage 4 does (`iba/app/lib/collectionvalidate.py`, `iba/app/lib/validationactions.py`, rules VA-01 to VA-06 and IB-07) is done as each row is recorded and as each step closes, so that a collection built by the steps comes out already valid. `ValidatePull`, `ValidateRecord` and `ValidateCheck` stay, but as a final audit that must find nothing, not as the place where observations are repaired. The marker and node columns at creation (done today) are the first piece of this.

## 2. What each piece of the validation becomes

"Mechanical" means a table test with no judgement; "reading" means a judgement that only a reading can make, so it is built as something the record demands an answer to, not as a computed pass.

| Validation piece | In the build today | Proposed in the build | Kind |
|---|---|---|---|
| Marker (VA-05) | set at creation (applied live today) | none further | mechanical, done |
| Word node columns, with the reason a gap stays (VA-02) | checked at creation (today) | none further | mechanical, done |
| Observation with no live node | by construction in layer steps | the record refuses a finding that would have none | mechanical |
| Trace to a deleted observation (IB-07) | refused at stage 4 only | refused at every step that writes a trace | mechanical |
| Inner-being observation traced to evidence marked as such (IB-07) | stage 4 accepts a trace to any stage 3 observation | the trace target must be marked evidence; an unmarked older target is accepted as pending, as IB-07 says; a target marked inner_being is refused | mechanical |
| Same text on two live observations (VA-02, RW-03) | only inside the file being recorded | the record refuses a text equal, after whitespace and case, to a live observation of the same collection scope, naming it; the filler gains a node on it instead (`existing` action `merge`) | mechanical |
| Two observations of one meaning | none | at record time the pull of each row already lists the older observations on its occurrences; the record demands an answer for each (section 3) | reading |
| Untrue or unfounded wording, a false quotation, a node on the wrong word (VA-02) | wording rules RW-04, B:131 (no copy of the verse), grounds for a read basis, the quote check against the ESV | no new computed test; the quote check and grounds test stay; "founded in the verse" stays a reading, done by me on the pull's verse text, with the verse text and positions in the pull | reading |
| Older observations on the collection's occurrences consumed, merged, restated or deleted as neither, never discarded without verified consumption (VA-03, VA-04) | stage 4 only, optional (IB-05); stage 1 `adopt` | the actions of section 3 are demanded for every older live observation with a node on an occurrence of the row, at every step | reading, demanded |
| Deferral of an older observation to a named collection's validation (VA-02) | none | the `existing` action `defer` names the collection and the finding; the record keeps it through `validationactions.defer`; the check accepts it as deferred | reading, recorded |
| Evidence layer passes before the inner-being layer is judged (VA-06) | stage 4 opens when stage 3 is closed | stage 4 also opens only when the evidence check (the mechanical tests above over the collection's scope) passes, so the two layers never run at once | mechanical gate |
| Final audit | `ValidatePull`, `ValidateRecord`, `ValidateCheck` run after stage 4 | `ValidateCheck` becomes the last gate of step 3.3: the step closes only when it passes; the other two remain for an old collection built before this change | mechanical gate |

## 3. The one design point: older observations met while building

Today the pull of a row shows the existing observations on its occurrences (`existing_observations`) but nothing demands an answer outside stage 4 (IB-05: "shown, not demanded"). The validation demanded one for each in its scope, with a verified consumption before any deletion (VA-03). My proposal:

- For each row of steps S1, 1.1, 1.2 and 2.1 the pull lists the older live observations with a node on an occurrence of the row, as it does now.
- The record demands, for each, one of: `keep` (it stands, with its marker set by the row's item or by reading), `restate` (new wording, checked against the base data), `merge` into a named observation (its nodes move, the duplicate is soft deleted), `consume` (live observations carry its meaning, stated in words, each occurrence of it on a live node or named as not carried, traces re-pointed), `delete_as_neither` (comment first, then deleted), or `defer` to a named collection with the finding. The actions are the existing functions of `validationactions.py`; no new action is written.
- An older observation left with no answer makes the record refuse the row, naming it.
- This applies only to older observations that are in the collection's scope by the validation's own scope definition (node on the collection, on a verse of it, or on a member surface with its own code).

## 4. Increments, each tested on a copy before the next

1. **Mechanical refusals** (section 2, "mechanical" rows): no node, trace to a deleted observation at every step, trace target marker, same text. Config: `layer.reading` keys; code in `lib/layerreading.py`, `lib/layerinner.py`, `lib/observationrecord.py`.
2. **Older observations answered at record** (section 3), reusing `validationactions.py`.
3. **Gates**: the evidence check before stage 4 opens; `ValidateCheck` as the closing gate of 3.3.
4. **Records**: rules amended (`collection-validation-follows-stage-4`, VA-01 to VA-06, IB-01, IB-05, IB-07, RW-12), `USER-GUIDE.md`, `BUILD.md`, one migration through `apply_logged`, a named snapshot before the live apply.

Tests (copy only, no live write): the 19 cases of `temp_2538_marker_at_creation_test_run.py` stay green; new cases for each refusal with a synthetic bad input and a good one; the stage 1 to 4 test collection taken through all steps with an older observation planted on each kind of occurrence and each of the six answers; the final gate refuses a collection with one planted defect and passes the clean one. The stale cases of `temp_2505_layers_test_run.py` (R3, G1) are repaired in the same unit, since they hide regressions.

## 5. Decisions I need from you

1. **Demanded or shown (section 3).** Your principle was "all observations that relate to the collection are included" and "under no circumstances discarded without a clear verification that they have been consumed". I propose the answer is demanded at every step. The cost: each row of thought's rerun carries the older observations on its occurrences and each needs an answer, which is the validation's reading work moved into the build, not removed.
2. **Same text: refuse or merge automatically.** I propose refuse, naming the existing observation, so the merge is a recorded decision. Automatic merge would be quicker and silently changes an older observation.
3. **The closing gate.** Is `ValidateCheck` passing the right condition to close step 3.3 and so to finish a collection's phase 1 to 4?
4. **Order against the thought rerun.** Build and test this first, then rerun thought, so the rerun runs on the final code. Confirm.
