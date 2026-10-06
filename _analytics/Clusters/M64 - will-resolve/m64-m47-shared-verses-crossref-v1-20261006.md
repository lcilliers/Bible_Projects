# M64 × M47 shared verses: narrative and open-thread cross-reference

**Date:** 2026-10-06 · **Escalation:** #1978 · **Status:** data cross-reference only, no reading

**Sources:**
- the verse list: [`m64-m47-shared-verses-v2-20261006.csv`](m64-m47-shared-verses-v2-20261006.csv). It is v1 with four columns added: `narrative_n`, `narrative_refs`, `ot_refs`, `ot_pairing`. v1 is in `archive/`.
- the script: [`verse-narrative-ot-crossref-v2-20261006.py`](verse-narrative-ot-crossref-v2-20261006.py). It is read-only and works for any verse-list CSV.

## 1. How it was checked

- **Narrative:** the highest version of each chapter file in `inner-being-narrative/` (01 to 15, with 10.0 to 10.13). The `00-index` status file and `archive/` are excluded.
  - Each place is given as chapter · section heading · paragraph number within that section. "(opening)" is the text before the first section heading.
  - Citations are read in full names and short forms (Genesis 6:5, Gen 6:5), with ranges, comma verses, and a bare `8:21` after `Gen 6:5`. A bare reference takes the last book only when nothing but punctuation or "and / with / beside" lies between them, and it is marked "book carried". A verse inside a range, not named singly, is marked "in range".
  - A bare reference further away from its book is not picked up. For example, `(3:24)` after a sentence about `(Genesis 2:9)` is missed. So a zero here means "no citation found", not "not discussed".
- **Open threads register:** every column of every OT row (90 rows, 104 verse citations).
  - Also checked: the verse lists behind the M02 pairing threads OT-16 to OT-90, in `M02 - anger-wrath/wa-cluster-M02-mcode-face-combinations-v1-20261005.csv`.

## 2. Result

| Measure | Count |
| --- | --- |
| Verses | 56 |
| Cited in the narrative | 21 |
| Not cited | 35 |
| Cited in an open-threads row | 0 |
| In an OT pairing verse list | 0 |

**Narrative places, by chapter** (a verse cited twice in one chapter counts twice):

| Chapter | Places |
| --- | --- |
| 10.4 Thinking | 7 |
| 11. Patterns of the inner life | 5 |
| 12. When the inner being goes wrong | 5 |
| 6. The spirit | 3 |
| 9. Where the words part | 3 |
| 2. Life, breath and death | 3 |
| 10. The inner being at work | 2 |
| 4. The heart | 2 |
| 10.9 Relating to God | 2 |
| 10.13 Anger | 2 |
| 7. Flesh | 2 |
| 10.10 Relating to others | 1 |
| 14. Made new | 1 |
| 10.12 Fear | 1 |

**Open threads.** None of the 56 verses is cited in the register, and none is in an M02 pairing list. So none of them also carries an anger word. Three threads name M64 or M47 as their trigger, so they bear on this set as a whole, not on any one verse:
- **OT-09** "gold nuggets" pass (open). Its trigger is *"at a point the researcher chooses; candidates are … before the M12 / M64 strands"*.
- **OT-62** Anger (M02) and Will & Resolve (M64) (open). Its 7 verses are 1Sa 20:30, 1Ti 2:8, Act 5:33, Deu 29:20, Eze 20:8, Psa 106:23 and Zec 8:14. None of them has an M47 word.
- **OT-18** Anger (M02) and Inner Seat (M47) (resolved, #1974).

## 3. Verses cited in the narrative

| Verse | M64 word | M47 word | Narrative places |
| --- | --- | --- | --- |
| Gen 6:5 | H3336 intention "intention" | H3820A heart "heart" | 10. The inner being at work · Where I am answerable · ¶2<br>10.4 Thinking · The inclination: a shaped thing · ¶1<br>10.4 Thinking · The inclination: a shaped thing · ¶2<br>11. Patterns of the inner life · 1. The inner being is acted upon as much as it acts · ¶2<br>12. When the inner being goes wrong · The heart as the source · ¶1<br>12. When the inner being goes wrong · The heart as the source · ¶2 |
| Gen 8:21 | H3336 intention "intention" | H3820A heart "heart"; H3820A heart "heart" | 4. The heart · The heart speaks to itself · ¶6<br>11. Patterns of the inner life · 8. God has a heart and a soul · ¶5<br>12. When the inner being goes wrong · The heart as the source · ¶2 |
| Exo 35:35 | H2803G to devise: design "designer"; H2803G to devise: design "skilled" | H3820A heart "them" | 10.4 Thinking · Where thoughts come from · ¶3<br>10.4 Thinking · What thinking does · ¶2<br>11. Patterns of the inner life · 1. The inner being is acted upon as much as it acts · ¶2 |
| Deu 2:30 | H0014 be willing "would" | H7307G spirit "spirit"; H3824 heart "heart" | 6. The spirit · The human spirit · ¶10<br>9. Where the words part · Lines that are often drawn, but that I cannot find · ¶2<br>11. Patterns of the inner life · 1. The inner being is acted upon as much as it acts · ¶2 |
| 2Sa 14:14 | H2803G to devise: design "devises" | H5315H soul: life "life" | 2. Life, breath and death · What death is · ¶4<br>10.4 Thinking · Small, passing, and wholly seen · ¶4 |
| 2Sa 19:19 | H2803H to devise: count "hold" | H3820A heart "heart" | 10.10 Relating to others · (opening) · ¶3 |
| 1Ch 28:9 | H3336 intention "plan" | H3820A heart "heart"; H5315G soul "mind"; H3824 heart "hearts" | 10.4 Thinking · Small, passing, and wholly seen · ¶2<br>10.9 Relating to God · (opening) · ¶2 |
| 1Ch 29:18 | H3336 intention "purposes" | H3824 heart "hearts"; H3824 heart "hearts" | 14. Made new · Thoughts taken captive · ¶2 |
| Job 7:15 | H0977 to choose "choose" | H5315I soul: myself "I" | 2. Life, breath and death · Wanting to die · ¶1 |
| Psa 31:13 | H2161 to plan "plot" | H5315H soul: life "life" | 10.12 Fear · Dread laid on others · ¶4 |
| Psa 32:2 | H2803H to devise: count "counts" | H7307G spirit "spirit" | 6. The spirit · The human spirit · ¶6<br>9. Where the words part · Lines that are often drawn, but that I cannot find · ¶2 |
| Psa 51:12 | H5081G noble: willing "willing" | H7307G spirit "spirit" | 6. The spirit · The human spirit · ¶11 |
| Psa 140:2 | H2803I to devise: devise "plan" | H3820A heart "heart" | 12. When the inner being goes wrong · The heart deceives its owner · ¶2 |
| Pro 16:9 | H2803I to devise: devise "plans" | H3820A heart "heart" | 4. The heart · The heart thinks, attends and remembers · ¶2<br>10.4 Thinking · Where thoughts come from · ¶1 |
| Isa 10:7 | H2803I to devise: devise "think" | H3824 heart "heart"; H3824 heart "heart" | 10.13 Anger · Those who carry it out · ¶1<br>10.13 Anger · What changes it · ¶1 |
| Isa 42:1 | H0972 chosen "chosen" | H5315G soul "soul"; H7307G spirit "Spirit" | 9. Where the words part · Lines that are often drawn, but that I cannot find · ¶6<br>11. Patterns of the inner life · 8. God has a heart and a soul · ¶2 |
| Zec 7:10 | H2803I to devise: devise "devise" | H3824 heart "heart" | 10. The inner being at work · Where I am answerable · ¶1 |
| Rom 8:6 | G5427 purpose "mind on"; G5427 purpose "mind on" | G4561 flesh "flesh"; G4151G spirit/breath: spirit "Spirit" | 2. Life, breath and death · Death in the living · ¶1<br>7. Flesh · Flesh in the New Testament: one word, several values · ¶4 |
| Rom 8:7 | G5427 purpose "mind" | G4561 flesh "flesh" | 12. When the inner being goes wrong · Flesh as an orientation · ¶1 |
| Rom 8:27 | G5427 purpose "mind" | G2588 heart "hearts"; G4151G spirit/breath: spirit "Spirit" | 10.9 Relating to God · (opening) · ¶2 (in range Romans 8:26–27) |
| Phili 1:22 | G0138 to choose "choose" | G4561 flesh "flesh" | 7. Flesh · Flesh in the New Testament: one word, several values · ¶2 |

## 4. Verses not cited in the narrative

| Verse | M64 word | M47 word |
| --- | --- | --- |
| Exo 10:27 | H0014 be willing "he would" | H3820A heart "heart" |
| Exo 35:5 | H5081G noble: willing "generous" | H3820A heart "heart" |
| Exo 35:22 | H5081G noble: willing "willing" | H3820A heart "heart" |
| Exo 36:8 | H2803G to devise: design "skillfully" | H3820A heart "craftsmen" |
| Lev 7:18 | H2803H to devise: count "credited" | H1320 flesh "flesh"; H5315I soul: myself "he" |
| Deu 12:21 | H0977 to choose "choose" | H5315I soul: myself "you" |
| Deu 18:6 | H0977 to choose "choose" | H5315L soul: appetite "desires" |
| 2Sa 23:17 | H0014 be willing "he would" | H5315H soul: life "lives" |
| 1Ki 8:48 | H0977 to choose "chosen" | H3824 heart "heart"; H5315G soul "soul" |
| 1Ki 12:33 | H0908 to devise "devised" | H3820A heart "from" |
| 1Ch 11:19 | H0014 be willing "he would" | H5315H soul: life "risk"; H5315H soul: life "lives" |
| 2Ch 6:38 | H0977 to choose "chosen" | H3820A heart "heart"; H5315G soul "soul" |
| 2Ch 7:16 | H0977 to choose "chosen" | H3820A heart "heart" |
| 2Ch 29:31 | H5081G noble: willing "willing" | H3820A heart "heart" |
| Neh 6:8 | H0908 to devise "inventing" | H3820A heart "mind" |
| Psa 17:3 | H2161 to plan "purposed" | H3820A heart "heart" |
| Psa 35:4 | H2803I to devise: devise "devise" | H5315H soul: life "life" |
| Pro 10:20 | H0977 to choose "choice" | H3820A heart "heart" |
| Isa 49:7 | H0977 to choose "chosen" | H5315J soul: person "one" |
| Isa 58:5 | H0977 to choose "choose" | H5315I soul: myself "himself" |
| Isa 66:3 | H0977 to choose "chosen" | H5315G soul "soul" |
| Eze 3:7 | H0014 be willing "willing"; H0014 be willing "willing" | H3820A heart "heart" |
| Eze 14:7 | H5144A to dedicate "separates" | H3820A heart "heart" |
| Eze 38:10 | H2803I to devise: devise "devise" | H3824 heart "mind" |
| Dan 5:21 | H6634 to will "he will" | H3825 heart "mind" |
| Dan 6:3 | H6246 to plan "planned" | H7308 spirit "spirit" |
| Dan 11:25 | H2803I to devise: devise "devised" | H3824 heart "heart" |
| Jon 1:4 | H2803I to devise: devise "threatened" | H7307H spirit: breath "wind" |
| Zec 8:17 | H2803I to devise: devise "devise" | H3824 heart "hearts" |
| Mat 12:18 | G0140 to choose "chosen" | G5590G soul "soul"; G4151G spirit/breath: spirit "Spirit" |
| Act 11:23 | G4286 purpose "steadfast" | G2588 heart "purpose" |
| 1Cor 4:5 | G1012 plan "purposes" | G2588 heart "heart" |
| 1Cor 12:11 | G1014 to plan "wills" | G4151G spirit/breath: spirit "Spirit" |
| 2Cor 1:17 | G1011 to plan "wanted"; G1011 to plan "make"; G1011 to plan "plans" | G4561 flesh "flesh" |
| 2Th 2:13 | G0138 to choose "chose" | G4151G spirit/breath: spirit "Spirit" |
