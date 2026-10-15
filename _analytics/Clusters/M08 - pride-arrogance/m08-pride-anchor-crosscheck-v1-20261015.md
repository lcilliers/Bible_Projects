# M08 pride: is the narrative anchored in the claims register for these words?

**Date:** 2026-10-15 · **Escalation:** #2156 · **Register update:** 143, with follow-up claims C-243 and C-244 and 12 tellings

**Instruction (researcher, verbatim):** *"... cross checking that the narrative is anchored in the claims register for this group of words"*

**Scope (rule 77 as amended, #2154):** the concept in focus is pride, with presumption, boasting and mocking. Every passage in the whole narrative that uses a word of this group was read against the register. The word list is in [`m08-pride-anchor-scan-v1-20261015.py`](m08-pride-anchor-scan-v1-20261015.py). It covers pride, proud, arrogant, haughty, boast, mock, scoff, scorn, conceit, presume, insolent, lofty, lifted up, puffed, majesty, derision, jeer, and exalts himself. A passage is split as the register splits it (`parse_chapter`).

## 1. Counts

| Point | Passages with the words | Telling no claim |
| --- | --- | --- |
| Before the weave | 151 | 110 |
| After update 143 | 210 | 104 |
| After the follow-up (C-243, C-244 and 12 tellings) | 210 | 93 |

Scans: [`…-scan-before-v1-20261015.csv`](m08-pride-anchor-scan-before-v1-20261015.csv), [`…-scan-after-v1-20261015.csv`](m08-pride-anchor-scan-after-v1-20261015.csv), [`…-scan-final-v1-20261015.csv`](m08-pride-anchor-scan-final-v1-20261015.csv).

## 2. What was done

**New text (10.15 and the woven sections).** Every statement that goes beyond its verses has a claim:
- C-212 to C-242 were added in update 143. They have 73 tellings, including links on older passages.
- C-243 (boast and rejoice are one Greek word) and C-244 (the plan that presumes on tomorrow) were added afterwards.
- All 33 new claims are told in at least one passage. The register's own `Check` lists none of them as untold.

**Older passages on pride that told no claim** are now told, by new claims or by existing ones:

| Passage | Told by |
| --- | --- |
| Ch 4 *The heart and anger*: Uzziah's heart lifted up | C-214 (given, then held as one's own) |
| Ch 4 and 10.4: Eliab's "presumption"; 10.14 *Reading another's fall* | C-237 (pride can be named wrongly) |
| Ch 5 *Rest for the soul*: the soul boasts in the Lord, not in itself | C-182 (the boast moved) |
| Ch 9: the spirit "haughty" before a fall | 2-2 |
| 10.1 *How a feeling rises* and Ch 11 *Thresholds*: Uzziah lifted up when strong | C-214 |
| 10.2: the word scorned (Jer 6:10); God opens the ear to conceal pride (Job 33:17) | C-222, C-224 |
| 10.3: "against the pride of having"; 10.4: Uzziah strong, then proud; 10.6: the giver forgotten (Neh 9) | C-214 |
| 10.5 *Speech before words*; Ch 11 *God's delight in a person*; 13.1 *His delight in people's mouths*: the mockers' taunt | C-233 (mocking takes trust as its target) |
| 10.6: the envy and the pride of the tree | C-209 |
| 10.7 *Others around a choice*; 10.9 *Kept from what would rule*: presumption | C-223 |
| 10.12: fear set against pride (Rom 11:20) | C-225 |
| 10.13 *Those who carry it out*; Ch 11 *Authority as a standing*; Ch 12, the boast of Dan 4:30 | C-215 (pride credits its own hand) |
| 10.14 *Pride brings its own fall* | C-235 |
| Ch 11 *Likening* | C-208 |
| Ch 11 *Overflow* (one word for anger's and pride's overflow) | C-242, a lexical claim: H5678 in Job 40:11 and Pro 21:24 |

**Two passages changed by the weave keep their claims.** The 10.14 opening still tells C-168, and the Ch 12 *Pride is placed in the heart and in the spirit* passage still tells C-207. Both were read again and still hold.

## 3. The 93 passages that still tell no claim

Each one was read: [`m08-pride-anchor-classify-v1-20261015.csv`](m08-pride-anchor-classify-v1-20261015.csv), built by [`…-classify-v1-20261015.py`](m08-pride-anchor-classify-v1-20261015.py).

| Decision | Passages | Why no claim is added now |
| --- | --- | --- |
| quote or pointer | 29 | They only quote verses with the word, or point to another section. Nothing is said about pride beyond the verse. Examples: the Ch 12 bullets under *Pride is placed in the heart*, the 10.14 lists, and the Connections lists. |
| other concept | 64 | They use a pride word, but what they say beyond the verses is about another concept. Under rule 77 as amended, they are reconciled when that concept's strand touches them. By chapter: 10.6 desire, envy, jealousy 10; 10.7 choosing and willing 7; Ch 11 7; 10.13 anger 6; 10.10 4; 13.1 God's delight and jealousy 4; and 1 to 3 each in Ch 2, 4, 6, 7, 10.1, 10.2, 10.4, 10.5, 10.9, 10.11, 10.12, 10.14 and 13.2. |

## 4. What is not done here

- **No statement was restated or removed.** None of the older pride passages read had a statement that the verses do not carry.
- **Two references to Job 40:13** (13.1 *Majesty* and C-239's source) are a verse gap by design. They are raised as #2158 with the same answer as #2151.
- **The register's own `Check` lists 51 findings** (`outputs/narrative-register/narrative-register-check-v9-20261015.md`). 49 are the older untold claims carried from before update 143. The other 2 are the Job 40:13 references. None concerns a pride claim.
