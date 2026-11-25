# #2542 — The partner words stored in thought pairings, checked against their collections (from #2536)

Raised by Claude, 2026-11-24, on the researcher's option A of #2536 v3. Nothing in the database was changed. Every value was read from `iba/app/db/iba.db` on 2026-11-24 (tables `surface_term`, `collection`, `collection_subgroup_surface`, `verse_lexical`, `verse`).

## What the researcher is asked to decide

Whether the three regroupings and one index-row removal of section 2 are made, and the one placement of section 2.2 that I cannot decide from meaning. The two cases of section 3 need no move.

## 1. Method

For each word of #2536 I read its stored group, base and collection, the member list of that collection, and the ESV text and stored Strong's code at each verse the pairing cited. A word is judged against what its collection gathers (rule B:129), by what it means in the verse. The sample for each word is every verse cited in #2536; I did not count the word's other occurrences.

## 2. Words that are not of their collection's meaning

### 2.1 `surely` in the collection `hear` (collection 60; term 46, base `sure`)

- `hear` gathers 31 surfaces of hearing, heeding and obeying (hear, listen, heed, obey, attention, deaf, ignore…); `surely` is the only member that is not.
- At Exo 2:14 (H0403), 1Sa 16:6 (H0389), 1Sa 20:26 (H3588A and H1931 in one unit) and 2Ki 5:11 (H3318G and H0413 in one unit) `surely` is an adverb of assertion, "Surely the thing is known". It has nothing to do with hearing. (Jdg 3:24, also cited in #2536, has no stored row for the surface `surely` and I did not resolve why.)
- Precedent in the same table: `certainly` (term 683) and `indeed` (term 309) are group `other`.
- Proposed: group `surely` to `other` (rule B:129: a generic evaluative or speech word is regrouped to other and is not a surface of a collection). Its placement row in `hear` is removed by that regrouping.
- Its base `sure` (term 65, inner_being_state, collection `loyalty`) is a separate question, not examined here.

### 2.2 `unworthy` in the collection `reward` (collection 218; term 5792, base `worth`)

- `reward` gathers 11 surfaces (reward, pay, repay, deserts, deserving, due reward, bestowed, punishment, worth, unworthy, pay attention): what is due to a person.
- At Deu 15:9 (H1100I, unit `unworthy` head) the phrase is "an unworthy thought in your heart": the noun H1100I, worthlessness, used of a base thought. It does not mean "not deserving a reward".
- Proposed: move `unworthy` out of `reward`. The surface `worthless` (term 944, inner_being_state) is stored in the collection `pride`, which sits oddly with its meaning, so I cannot decide the destination from meaning without first settling where `worthless` belongs. Decision for the researcher: place `unworthy` with `worthless` wherever that stands, or give the pair a place of their own.
- `worth` stays in `reward`.

### 2.3 `presence` and `present` in the collection `offer` (collection 219)

- `offer` gathers 20 surfaces of offering and dealing (offer, offered, presented, freely offered, deal…).
- `presence` (term 4831, base `present`, group `other`, state `corrected`) at Rut 4:4: "in the presence of those sitting here" (H5048), a locative phrase, not an offering. Its group is already `other`; its row in `offer` has state `unplaced`, reason `index fill`, and `collection_state` `untouched`, so it is an index artefact, not a placement of the study. Proposed: remove that index row. Its base `present` is wrong for it: the base of `presence` is not the verb "present" of offering.
- `present` (term 2037, group inner_being_state, state `judged`) at 1Cor 7:26: "the present distress" (G1764), an adjective meaning current. The same surface text also stands for the verb "present" that `offer` is about, so a surface-level move would be wrong for the verb senses. Proposed: no collection move; treat 1Cor 7:26 at the occurrence level (section 3).

## 3. Words that stay in their collection, with a note at the occurrence

### 3.1 `will` in the collection `desire` (collection 9; term 34, base `will`)

- At 2Sa 14:17 (H4994 with H1961, a three-word unit) and 2Ki 7:12 (H4994) `will` is the future auxiliary, "will set me at rest", "I will tell you". It is not desire.
- The surface `will` as the noun of wishing and the verb "wills" (both members of `desire`) is correct. The collection is not changed.
- Proposed: record the two verses as occurrences that do not hold the sense of the collection, in the observations of `desire` at the stage 1 reading, as the researcher said of #2536 ("it must be recorded in the observations to ensure that it would be picked up when the partner collection is analysed"). I have not written those observations: they are made by a reading (RW-01), and `desire` has not been read.

### 3.2 `present` at 1Cor 7:26

Same treatment: record 1Cor 7:26 in the observations of `offer` when that collection is read.

## 4. How the changes would be made

- `surely` and `presence`: `iba/app/ps/Surface-Group.ps1 -Action Set -Group other -Surface surely -Reason "<your ruling, quoted> (#2542)" -Check` previews it; the tool requires a quoted researcher's ruling as the reason, so I wait for your approval before running it. It writes a `surface_event` and a second run changes nothing.
- B:129 requires a change to collections to be made class by class, tried on a copy, under a named snapshot, with counts predicted and checked, links set deleted and never removed, and recorded in BUILD. I will do that when you approve; the counts are one placement row each for `surely`, `presence` and (when its destination is decided) `unworthy`.
- After the change, `Surface-Structure.ps1 -Action Match` is run (USER-GUIDE section 8.11).

## 5. Summary

| Word | Stored in | Verdict | Proposed |
|---|---|---|---|
| surely | hear | not of hear | group other |
| unworthy | reward | not of reward | move; destination for the researcher |
| presence | offer | index artefact, group already other | remove index row |
| present | offer | right for the verb senses, wrong at 1Cor 7:26 | note at occurrence |
| will | desire | right; auxiliary at 2Sa 14:17 and 2Ki 7:12 | note at occurrence |
