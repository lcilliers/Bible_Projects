# 2329: making the Phase 1 observations fit for purpose (design, 2026-10-30)

## The goal

The researcher's own words, chat 2026-10-30: to tease out the operation of a characteristic across its surfaces, for asking *"what is the state of mind before the act, what happens after the act, does it differ when the subject of asking changes"*; and *"you know exactly what is my goal ... So I leave to to you."* This design is my decision on how to meet that goal. It is one design, not a list.

## What the test showed

See `outputs/escalation/2320-asking-usefulness-test-v1-20261030.md` (the 39 verses, the three questions, the narrative). In short: who asks whom is only a sentence, what follows an asking is mostly in the next verse and not recorded, the state before is never asked for, and the sheet does not carry the meaning data (#2320 v29).

## The design (four changes to Phase 1, one trial)

1. **The meaning data on the Observe sheet.** For each surface of the verse the sheet carries what the tables hold for its code: the meaning tree rows (`strong_meaning_tree`), the sense head (`strong_sense`), the STEP gloss and the related words (`strong_related`); for Greek also the lexicon. One set-based query over the verse's codes (B:71). The data-quality flag about meaning sources is then written from what is held, not typed by hand.
2. **Two parts added to every observation of an inner-being surface** (the parts list in `reading.observation_parts`):
   - `before`: what the verse states of the prompt, state or purpose before the act, in words, or `{"none": "the verse does not say"}`.
   - `after`: what follows the act, the answer, result or response, in words, or `{"none": ...}`. The sheet already carries the passage around the verse (`passage_window` 2 in `reading.verse_loop`), so the next verse's text is in front of me at Observe; the part cites it by reference (for example Gen 37:16 for Gen 37:15). No verse enters the scope and no verse text is read twice (RO1).
3. **The party typed.** The party part gains the kind of the one who acts and of the one acted on, from the existing enum `party_kind` (divine, human, non_human), beside the sentence. Who-asks-whom then comes from a query.
4. **Nothing else in Phase 1 changes.** Which surfaces are recorded (inner-being only), the roles, the kinds and Record's checks stay as built. The narrative home for asking is not decided here: it belongs to the claims step when the claims are written (RN-05).
5. **The trial (RG-19).** After the build the 39 recorded verses are redone under the new parts by modifying their observations, with the reason (no duplicates, no deletions; RS-04). The researcher then checks five verses of their own choosing. **No further verse is run in bulk until that check is passed.** The test is the same three questions on asking, now answered from the record: the asker and the asked by query, `before` and `after` present or stated absent for every verse.

## How it is built

- A Developer Mode session (CLAUDE.md): config first (`reading.observation_parts`, the verse loop, the party enum use), then the code that reads it (`governance.rules_must_be_config_driven`), then spec 4.2, USER-GUIDE and BUILD.
- Time for the trial, from a measurement already taken: the timed batches ran at about 22 seconds a verse (`_analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking-batch-times-v1-20261028.md`), so 39 verses is in the order of a quarter of an hour of reading, plus the build.

## Approval sought

That this design (the four changes and the trial) is the change to Analysis_phase_1, and that I build it in a Developer Mode session and run the trial. Approval does not release further bulk batches of m21-asking: that waits for your check of the five verses.
