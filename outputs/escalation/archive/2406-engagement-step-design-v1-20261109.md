# #2406 — design of the step before narration: what is engaged in the inner being (v1, for decision)

A design for the researcher to decide; nothing is built (B:105). It rests on the exploration in `outputs/escalation/2406-aloud-collection-split-and-surfaces-v1-20261109.md`. Table facts below were read from the live `cfg_table` / `cfg_column` meanings and the code (B:123); the proposals are mine and inferential (B:4).

## What the researcher directed (verbatim, 2026-11-09, chat)

> "a) this step should reset the draft surface_group for each surface, as it now become an assessment based on context. b) the one liner by surface is very helpful, and must be captured, probably in the ib_observations. I would suggest that it would have an observation for each separate surface assessment and a node for each verse where it is true. c) the final step of this assessment is to review the verses in the collection that was not included to check if there are something missed. This may give an outcome, to be recorded in the observations, that the verse has no inner being bearing."

## The step as I understand it, in order

1. **Scope:** one collection (first `aloud`, id 138): its member surfaces and their verses.
2. **Assess each surface from its verses** (not from the bare word): read every verse the surface has in the collection and write what the surface does for the inner being, as one sentence (the sentence of part b of the exploration file).
3. **Record** each assessment as one observation, and one node for each verse where it is true.
4. **Replace the draft group** of the surface by the result of the assessment (item a).
5. **Review the verses of the collection that no surface assessment included**, and record what was missed, or that the verse has no inner-being bearing (item c).

## How it fits the tables (read from the live meanings)

- **`ib_observation`** is "one finding: a distinct description … applied through `ib_node` to every verse and word it covers", written by `reading.record`. It has the columns this needs: `obs_text` (the self-standing sentence), `setting`, `meaning`, `implication`, `parts` (JSON, including `sense` and `circumstance`), `tag`, `route`. So one observation per surface assessment fits its stated grain.
- **`ib_node`** is "one row per verse, word … the finding applies to", with `verse_reference`, `surface`, `role`, `disposition` (told, claim, held, data, context, withdrawn) and `disposition_note`. One node per verse where the sentence is true fits.
- **No bearing already has a place:** `ib_observation.route` has the value C, "no bearing" (held "on a party or link finding", per its column meaning); whether it can be used for a verse with no inner-being bearing is part of decision D4.
- **The entry point exists:** the reading process (`iba/app/ps/Reading.ps1`, study status in `governance.study_status`) writes observations and nodes; the collation (`Verse-Collate.ps1`) lists what the project already holds for a scope of verses so that work is not repeated.

## Facts that bear on the group reset (item a)

`surface_group` is also the gate of the surface cycle, not only a label. Read from the code:
- `iba/app/lib/collectionask.py` takes candidate words only where `surface_group IN (the in-scope groups)`;
- `iba/app/lib/surfacestructure.py` and `iba/app/lib/surfaceresolve.py` take only surfaces with `surface_group IS NOT NULL`;
- `base_state` `out_of_scope` is "the group is entity or other, or the surface is not yet judged into the study".

So a plain reset to NULL would take the 8 surfaces out of the structure, resolve and ask steps, and the collection links already made would stay while their words fall out of scope. Also, one surface can behave both ways by context (quiet: "be quiet" is an act; the quiet of a land is a state), so a single value may not fit what the assessment finds.

## Decisions for the researcher

**D1. How the draft group is reset.**
- **A (recommended):** the draft is replaced in one write by the assessment's result, with the old value kept in `surface_event` (as the existing `set_group` and `correct` actions do), so the surface never sits at NULL.
- **B:** reset to NULL with `group_state` unjudged, and accept that the surface leaves the structure, resolve and ask steps until the assessment writes its value.
- **C:** keep the draft and mark it as to be reassessed; no value is discarded until replaced. (This needs a new `group_state` value, a config change.)

**D2. What the group holds after the assessment.**
- **A (recommended):** the surface's group stays one value, taken from the assessment; where the verses split between act and state, the group is set from the assessment's sentence and the split is stated in the observation's `parts` (a new group value `mixed` is not introduced).
- **B:** a new group value for a surface that is both, which changes `cfg_enum surface_term.surface_group` and the in-scope lists named above.
- **C:** the group moves to the verse (on the node), and the surface keeps no group.

**D3. The unit of an observation.** One observation per surface per collection (recommended, as you suggested), or one per surface across all collections where it is a member. A surface that is a member of two collections (`shared`) is the case that decides it.

**D4. The verses nobody included (item c).** The sentence per surface covers the verses of its own surface. The review reads the collection's other verses (the export lists member surfaces only, so these are the verses of the collection's core words and set-aside or associated words that the assessments left out; I have not yet counted them for `aloud`). A verse with no inner-being bearing is recorded as an observation with a node. Options for how: (A, recommended) a single observation per collection saying "no inner-being bearing", with one node per such verse and `disposition` `data` or `context`, and with the reason in `disposition_note`; (B) `route` C on one observation per verse; (C) a new tag. Which is yours.

**D5. Who writes the sentence.** Claude reading the verses in the session (what I did for `aloud`), or the AI client (`qwen3:30b`) with the verses in the request. The exploration shows the bare-word call was the weak point, so a verse-fed call is possible, but its answers are inferential and need your review either way (B:4). My recommendation is Claude reading, one collection at a time, until you have seen the sentences for two or three collections.

## What is not designed yet

The test plan (B:46), the exact `Reading.ps1` calls, the config rows, and the effect on `collection_state` and the `check` step are left until D1 to D5 are decided. Nothing was written to any table.
