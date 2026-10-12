# M72 × completed strands: did they consider the authority? (pull and test of 8, v2)

**Date:** 2026-10-12 · **Escalation:** #1998 · **Status:** v2. The test verdict on 1Sa 7:3 is corrected, and the full check is **deferred to the downstream re-read of each narrative segment** (researcher ruling, §4). Nothing was changed in the narrative or the ledgers. **Supersedes:** `archive/m72-completed-strand-check-test-v1-20261012.md`.

**Instruction (researcher, chat 2026-10-12, verbatim):** *"check if §5 - other M-Codes - where the primary M_code as already been completed (m25, M47, M18, M01, M02) appropriately considered the where the authority is coming from or the impact of the authority on the characteristic"*.

**Files:**
- Script: [`m72-completed-strand-check-pull-v1-20261012.py`](m72-completed-strand-check-pull-v1-20261012.py)
- Output: [`m72-completed-strand-check-v1-20261012.csv`](m72-completed-strand-check-v1-20261012.csv)

The CSV has one row per verse, with:
- the partner strands
- the M72 words with their group (all groups but B are qualifiers under the scope ruling)
- the partner words
- the narrative places
- a working aid, `authority_named_in_paragraph`: whether a citing paragraph holds any of the verse's M72 surface words. It is a pointer, not a decision. A paragraph can name the king as "Saul" or "Pharaoh".

## 1. The set

| Partner | Verses | Cited in the narrative | Citing paragraph names the authority | Hold a B word |
|---|---|---|---|---|
| M25 Life & Death | 294 | 49 | 40 | 16 |
| M47 Inner Seat | 238 | 97 | 73 | 28 |
| M18 Desire & Longing | 182 | 105 | 91 | 18 |
| M01 Fear & Awe | 129 | 40 | 27 | 10 |
| M02 Anger & Wrath | 100 | 44 | 31 | 4 |
| **All (distinct)** | **832** | **263** | **201** | **53** |

- **Not cited in the narrative: 569.** Each strand decided these in its own ledgers, as data, as a face, or as held.
- **By M72 group, at verse level:** A only 458, D only 97, E only 68, C only 67, B only 53, and the rest mixed.
- **The 53 B verses** are read with the B set. There the check is part of the reading.

## 2. Test: 8 verses (non-B), read in their passages beside the strand's own record

Four verses are cited where the paragraph does not name the authority; four are not cited. One of each kind per strand (M25, M47, M01, M02), drawn at random. M18 is left out of the test, because its 182 were all checked on 2026-10-12 (OT-98).

| Verse | Strand's record | What the passage gives about the authority | Verdict |
|---|---|---|---|
| **Mal 1:13** (M25 "snort") | 10.5: *"you snort at it"*, contempt breathed out | The next verse gives the ground: *"For I am a great King, says the Lord of hosts, and my name will be feared among the nations"* (1:14). The contempt is shown to the King's table. | **Gap.** The one despised is named as a great King. It widens the contempt reading (whom it is aimed at), and 13.1 takes *"I am a great King"* as God's character. |
| **1Sa 7:3** (M47 "heart") | 10.7 *Setting the heart*: *"direct your heart to the Lord"* | *"he will deliver you out of the hand of the Philistines"*. The return and the putting away of gods are joined to deliverance from oppression; 7:2 gives the twenty years of lament before it. | **Gap** (corrected in v2; v1 said "Considered"). The narrative keeps the directing of the heart and loses the outcome, deliverance from oppression. v1 judged the hand word "only the setting" because its role is qualifier. But the qualifier carried the outcome of the whole verse. The researcher's example of the deeper problem (§4). |
| **Mic 4:4** (M01 "make afraid") | Ch 14: *"no one shall make them afraid"*, a home held without threat | The verse ends *"for the mouth of the Lord of hosts has spoken"*. The narrative quotes up to "afraid" and stops. | **Gap.** The ground of the safety, whose word guarantees it, is left out. It is the source of the absence of fear. |
| **2Ki 3:27** (M02 "wrath") | Anger ledger AG-198: *"there came great wrath against Israel"*, held (AN-H4), source not named; 10.13 *Connections* | The king of Moab, *"when [he] saw that the battle was going against him"* (3:26), offered *"his oldest son who was to reign in his place"*. | **Considered.** The M72 word names who was given up (the heir). The anger strand held the verse for its own reason (the source of the wrath is not named). |
| **1Ki 22:35** (M25 "died") | M25 unit 2, face D01, death notices (data) | Ahab dies propped in his chariot. Before it, he had said of Micaiah *"I hate him"* (22:8), and Micaiah had said *"If you return in peace, the Lord has not spoken by me"* (22:28). | **Considered for M25** (a death notice). The passage's inner acts, hating the true word and the disguise (22:30), are not about authority, and they go with M06 and 10.11 when those are read. |
| **1Ki 1:2** (M47 "bosom") | M47 batch H: *"the king's failing body"* | The servants arrange for the king. | **Considered.** The king is the setting. |
| **Jer 15:4** (M01 "horror") | Fear unit 3, FE-86: a people made a horror. The reasons listed are the people's own deeds. | The verse gives a different cause: *"because of what Manasseh the son of Hezekiah, king of Judah, did in Jerusalem"*. | **Gap.** The cause named in this verse is a king's deeds bearing on a whole people. FE-86's "reasons given" leaves it out, and its summary ("the verses give the cause as their own deeds") does not hold for this verse. |
| **Judg 9:30** (M02 "anger") | Anger ledger AG-49, *"kindled by what is heard"*, listed under the face "The ruler's anger, and those beneath it" | Zebul is *"the ruler of the city"*. He hears Gaal stirring the city against Abimelech (9:31). | **Considered.** The ruler face holds it. |

**Result of the test (v2):** 4 considered, 4 with a gap. Three are of one kind, **where the authority comes from**:
- the one despised is a great King (Mal 1:14)
- the safety rests on the word of the Lord of hosts (Mic 4:4)
- a king's deeds bring horror on his people (Jer 15:4)

The fourth, 1Sa 7:3, is an **outcome lost**: the reading kept the strand's own clause and dropped what the verse joins to it.

None of the four needs the M72 word read as a characteristic. In each, the qualifier carries a ground, a cause or an outcome that the strand's reading passed over. Of the five verses still marked "considered", two (2Ki 3:27, 1Ki 22:35) were judged by whether the strand had a record, not by a full reading of the passage. They are not a reliable "considered".

## 3. How far to take the check (as put to the researcher in v1)

The test suggests that gaps are present but not the rule (3 of 8). Options:
1. **All 832,** strand by strand, beside each strand's record. This is the full check. It is the largest piece of reading in M72.
2. **The cited 263 first** (the narrative is where an omission shows), then the not-cited ones only where the strand placed the verse as an observation, not as data.
3. **By the kind of gap the test found:** first the verses where the M72 word gives a ground or a cause. In the text these show as "for", "because of", "by the word of", or as a title in the same or the next verse. Then the rest.

My recommendation is **2**. The narrative is the place where a missing ground does harm. In data rows the M72 word is mostly a death notice or a court setting.

For each gap found, the correction would be made in the narrative where the verse is cited (with a version bump), and the strand's ledger row would get a dated note. Nothing will be changed until you approve the method.

## 4. Ruling: the full check is deferred to the segment re-read

**Researcher, chat 2026-10-12, verbatim:** *"the triage of completed strands is pointing towards the existence of a deeper problem in the narrative - largely related to verse reading being fragmented accross different reading sessions. The results of this is evident - take one simple example I Sam 7:3 10.7 narrowly in 'directing the heart' but the outcome ' delivery from oppression' is lost. No doubt this calls for deeper reading, but I am not sure what the timing of this deeper reading should be. Downstream I will introduce a reread in any case of each segment of the narrative, because this is not the only problem in the narrative, and it may be better to re-assess these complex context reading scenarios at that stage. You must do better with your reading work; I can see how you are just chasing tick boxes and lists with narrow goals, and failing on many fronts, but I really don't know how to fix it, and would rather focus on the main task of working through all the strands to at least have a half baked result than nothing."*

What follows from the ruling:
- **The 832-verse check is not run now.** The CSV and this test are kept as an input to the downstream re-read of each narrative segment (OT-99).
- **The problem the test shows:**
  - The readings are fragmented across sessions.
  - Each strand kept the clause that held its own word.
  - What the verse joins to that clause (a ground, a cause, an outcome) was lost.

  The four gaps above are examples, not a count.
- **The main task continues:** work through the strands. For M72, that is group B.
