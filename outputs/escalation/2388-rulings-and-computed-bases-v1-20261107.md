# #2388 Researcher rulings and the computed-base question (v1, 2026-11-07)

> Inferential (B:4) wherever it says likely: my reading of each word against its derived words, not a judge answer and not confirmed. Read-only, nothing written.

## Rulings (verbatim, recorded on #2388)

- Decision 2: "are there any of the computed bases that is actually behaviour or state related - all the items in your examples should be re-assigned to 'other', they are wrongly classified."
- Decision 3: "the same goes for the non-state words, all need to be re-classified."
- Decision 4: "2385, and 2383 to be superseded into 2388"

## 1. To other (your ruling): 25 computed bases, the examples I listed

accustom, address, age, allot, annul, apostatize, appall, appoint, ash, astound, batter, begin, bend, blindfold, blunt, bowel, brawl, brother, bruise, catch, confound, control, cost, cripple, day

Note for you: appall, astound, confound, brawl and accustom read as inner-being words in their derived forms (appalled, astounded, confounded, brawler, accustomed). You said all the examples; I take that as final unless you say otherwise.

## 2. To other (your ruling): the 16 non-state words

all, life, much, forever, can, first, nothing, sight, whole, end, light, very, only, full, fruit, without

Note: this list came from a heuristic, so it is the 16 I showed you, not every non-state word among the 605. Heuristic limits are in section 4 of outputs/escalation/2388-unassigned-bases-seed-options-v1-20261107.md.

## 3. Your question: which of the other computed bases are behaviour or state

There are 78 computed bases left. Each has no group of its own; the group of its derived word (judged on the derived word alone) is not a reliable guide, since those judgements are the kind you found wrong.

**Likely behaviour or inner-being state (37), inferential:** err, heed, respond, shun, stare, rave, perplex, hearten, laze, grate, sate, parch, pang, infirmity, foreknow, opine, reckon, deem, peacemaker, joke, swell, stiff, stable, integrate, mature, genuineness, manage, object, treat, disable, debauch, regenerate, transfigure, guarantee, qualify, thorough, sway

**Likely other, not inner-being (41), inferential:** deed, dispose, divide, drag, draw, drown, earth, effect, feed, finish, fit, flow, former, fortify, hallow, imprison, impute, inherit, inward, kindle, limit, lodged, lower, occupy, overflow, plain, pluck, precept, rape, refine, single, squeeze, station, strip, touch, undo, veil, victor, withdraw, wrestle, write

Approve one of: (a) these two lists as they stand; (b) you amend them; (c) the group judge asks for the likely-state list only and the rest go to other.

## 4. What building the correction needs (design, B:105)

The group step has three actions: Status, Repoint, Judge. None sets a group by the researcher's ruling, so the corrections above cannot be made through the app. Writing surface_term by hand would bypass it (governance.project_change_rule). Proposed design, not built:
- A new action, Set, taking -Group other and a reviewed list of surfaces, refusing any surface not in the list.
- It writes surface_term.surface_group = other, group_state = confirmed, group_judged_by = researcher, group_reason = the ruling and escalation id, and one surface_event per change (the state before and after).
- Preview with -Check first; a second run changes nothing.
- A base moved to other leaves the in-scope set, so its base_state becomes out_of_scope on the next resolve run, and the repoint check must not move it back.
- Config: a step row group.set in the work package, a USER-GUIDE entry (8.11), a BUILD.md entry (governance.build_md_on_code_change).
