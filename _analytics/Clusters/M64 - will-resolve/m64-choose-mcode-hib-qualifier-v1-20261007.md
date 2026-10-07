# M64 "choose": which co-occurring M-code words are inner-being characteristics, and which are qualifiers

**Date:** 2026-10-07 · **Escalation:** #1978 · **Status:** for the researcher's review. Nothing is woven.

**Asked (researcher, verbatim):** *"from this analysis isolate the M-code word that have a direct HIB impact, and the words that is that a qualifyer, that is more like one of the T-codes that a real characteristic that operates with choosing."*

**Sources:**
- input: [`m64-choose-mcode-cooccurrence-v1-20261007.csv`](m64-choose-mcode-cooccurrence-v1-20261007.csv), with its source rows in [`m64-choose-reading-v3-20261007.csv`](m64-choose-reading-v3-20261007.csv). This covers the 222 uncited verses.
- script: [`m64-choose-mcode-hib-qualifier-v1-20261007.py`](m64-choose-mcode-hib-qualifier-v1-20261007.py). It makes no DB query (rule 71).
- one row per word in its verse: [`m64-choose-mcode-hib-qualifier-v1-20261007.csv`](m64-choose-mcode-hib-qualifier-v1-20261007.csv). This has 462 rows, with the class, the relation or qualifier kind, whose activity it is, the nearest T-code, and the ESV text.
- one row per Strong's, with each of its faces: [`m64-choose-mcode-hib-qualifier-summary-v1-20261007.csv`](m64-choose-mcode-hib-qualifier-summary-v1-20261007.csv)

## 1. How each word was judged

The unit is **the word in its verse**, not the M-code. One M-code often carries both kinds of words. The same Strong's can also change face from verse to verse (#1919). Each word was read in the ESV text with its aligned surface and put in one of three classes:

| Class | Meaning | Rows |
| --- | --- | --- |
| **HIB** | The word names something going on in a person's inner being in this verse, such as knowing, liking, desiring, loving, fearing, rejoicing, refusing, being ashamed, repenting, believing, or the heart or soul itself. | **99** |
| **DIV** | The same kind of word, but it is God's or Jesus' own inner activity: his love, delight, pleasure, compassion, knowing or purpose. Under rule 72 this is route A (Ch 13.1). It is kept apart because it often gives the **ground** of God's choosing. | **28** |
| **QUAL** | A qualifier. It names who, what, where, which office, what status, what event, or an outward act. It places the choosing but does not operate in it. This is the T-code-like set. | **335** |

**The line between HIB and an outward act.** Speaking, calling, praying, crying out, serving, ministering, keeping (commandments), blessing and seeking are counted as **operations** (T3-like), because the verse shows them as outward acts. This holds even though several sit in clusters named for them (M42 Prayer, M36 Worship, M65 Speech). See judgement point J1.

**For HIB and DIV words, the verse's own relation to the choosing is recorded:**
- **ground:** why or how the choice is made
- **paired:** named alongside the choosing as a parallel act
- **object:** the inner thing that is itself chosen
- **purpose:** what the chosen are chosen for
- **trait:** a trait the verse gives the chosen
- **response:** follows the choosing
- **contrast:** set against the choosing
- **toward:** an inner movement toward what was chosen
- **setting:** happens at what was chosen
- **awareness:** knowing that a choice has been made
- **none:** in the same verse, but not bound to the choosing

**Whose:** for HIB words, "chooser" is the person doing the choosing, "chosen" is the one chosen, and "other" is anyone else.

## 2. The inner-being words that operate with choosing (HIB, 99 rows)

### 2a. In the chooser's own choosing (28 rows): the closest to "a characteristic that operates with choosing"

**Ground: why or how the choice is made (12)**
- Knowing:
  - Isa 7:15–16: *"when he knows how to refuse the evil and choose the good"*
  - Act 15:22, 25: *"it seemed good to us … to choose men"* (G1380)
- Liking or preference:
  - Deu 23:16: *"wherever it suits him"* (H2896A)
  - 2Sa 19:38: *"whatever seems good to you"* (H2896A)
  - Jos 24:15: *"if it is evil in your eyes to serve the Lord, choose this day"*
- Pleasure: Act 6:5, *"what they said pleased the whole gathering, and they chose Stephen"*
- Fear: Psa 25:12, *"the man who fears the Lord … the way that he should choose"*
- Not listening: Isa 65:12, *"when I spoke, you did not listen … and chose what I did not delight in"*
- Iniquity: Job 15:5, *"your iniquity teaches your mouth, and you choose the tongue of the crafty"*
- Eagerness: 2Cor 8:17, *"being himself very earnest he is going … of his own accord"*

**Paired: named alongside the choosing as a parallel act (10)**
- Refuse: Isa 7:15, Isa 7:16
- Reject: Job 34:33
- Know: Job 34:4 (*"Let us choose what is right; let us know among ourselves what is good"*), Job 34:33
- Envy: Pro 3:31 (*"Do not envy … and do not choose"*)
- Desire: Isa 1:29 (*"the oaks that you desired … the gardens that you have chosen"*)
- The soul's delight: Isa 66:3 (*"These have chosen their own ways, and their soul delights in their abominations"*)
- Hold fast: Isa 56:4 (*"who choose the things that please me and hold fast my covenant"*)
- Take care: Job 36:21

**Object: the inner thing that is itself chosen (4)**
- Faithfulness: Psa 119:30, *"I have chosen the way of faithfulness"*
- Knowledge: Pro 8:10
- Wisdom and understanding: Pro 16:16

**Response of the chooser (2)**
- Isa 1:29: *"they shall be ashamed … you shall blush for the gardens that you have chosen"*

### 2b. In those who are chosen (27 rows)

**Purpose: chosen so that … (9)**
- Isa 43:10: *"that you may know and believe me and understand"*
- Eph 1:4: *"that we should be holy and blameless before him. In love"*
- 2Th 2:13: belief
- Tit 1:1: knowledge
- Jam 2:5: *"rich in faith"*

**Trait: what the verse says of the chosen (11)**
- Act 6:5: *"full of faith"*
- Col 3:12: compassion, the inward parts, kindness, humility, meekness, patience
- Tit 1:1: faith, godliness
- Jam 2:5: *"those who love him"*
- Rev 17:14: *"called and chosen and faithful"*

**Response of the chosen (7)**
- Joy:
  - 2Sa 6:21: David, *"I will celebrate"*
  - Psa 105:43: *"his chosen ones with singing"*
  - Psa 106:5: gladness
- Psa 65:4: *"we shall be satisfied"*
- 1Ch 28:10: *"be strong"*
- Isa 44:2: *"Fear not … whom I have chosen"*
- 2Pe 1:10: *"be all the more diligent"*

### 2c. In others, around the choosing (44 rows)

**Toward what was chosen (14)**
- 1Ki 8:48, 2Ch 6:38: *"repent with all their heart and with all their soul … pray … toward the city that you have chosen"*
- Neh 1:9: return
- Deu 18:6: the Levite's soul-desire to come to the chosen place
- Psa 106:5: to rejoice and glory with the chosen
- 2Ti 2:10: *"I endure everything for the sake of the elect"*
- 1Pe 2:6: believing in the chosen stone
- Isa 66:3: soul

**Contrast: set against the choosing (8)**
- Despised and abhorred by people: Isa 49:7, Jer 33:24, 1Pe 2:4 (*"rejected by men but in the sight of God chosen"*)
- Rom 11:7: Israel's seeking, and the hardening
- Pro 10:20: *"the heart of the wicked is of little worth"*, set against "choice silver"
- Isa 45:4: *"though you do not know me"*

**Setting: happens at the chosen place (6)**
- Rejoice: Deu 12:18, Deu 16:11, Deu 16:15
- Desire: Deu 12:21
- *"Be careful to do"*: Deu 17:10

**Response of others (5)**
- 1Sa 20:30: Saul's anger and his "knowing" of Jonathan's choice
- Joh 15:19: *"the world would love you … therefore the world hates you"*

**Other relations (7)**
- Purpose: Deu 14:23, *"that you may learn to fear the Lord"*; Act 15:7, believe
- Object of God's choice: Isa 58:5, a person humbling his soul. Here the inner act is what God chooses.
- Awareness: Act 15:7, 1Th 1:4
- Ground: Num 17:5, the grumbling that God's choosing will end

**None: in the same verse, but not bound to the choosing (4)**
- Judg 20:34
- Isa 7:16, *"dread"*
- 2Jo 1, love and know

## 3. God's own inner activity in choosing (DIV, 28 rows)

**Ground (19)**
- Love:
  - Deu 4:37, Deu 10:15
  - Psa 47:4, Psa 78:68
  - Col 3:12, 1Th 1:4, 2Th 2:13 (*"beloved"*)
- *"Set his love / heart"* (H2836A): Deu 7:7, Deu 10:15
- Desire: Psa 132:13, *"he has desired it for his dwelling place"*
- Took pleasure: 1Ch 28:4
- Compassion: Isa 14:1
- Faithful: Isa 49:7
- Soul well pleased: Mat 12:18
- Knows the hearts: Act 1:24
- Purpose: Rom 9:11
- Grace: Rom 11:5
- Jesus' knowing: Joh 13:18, *"I know whom I have chosen"*

**Contrast (4)**
- God rejects or casts off: 2Ki 23:27, Psa 78:67, Isa 41:9 (*"not cast you off"*), Jer 33:24

**Object (3)**
- What God delights in or accepts is set as the measure of the human choice: Isa 56:4, Isa 58:5, Isa 65:12

**Other (2)**
- 2Ch 7:16: *"my heart will be there"*
- Luk 18:7: *"will he delay long"*

## 4. The qualifiers (QUAL, 335 rows): T-code-like

| Qualifier kind | Nearest T-code | Rows | Main words |
| --- | --- | --- | --- |
| outward act (operation) | T3 Operations | 102 | speak, call, pray, cry out, minister, serve, seek, bless, keep (commandments), declare, help, save, swear, hear (God hears) |
| office or rank | T8 Party-Human | 37 | king (17), ruler, reign, leader, head |
| object | T12 Objects-Artifacts | 29 | idol, truth, inheritance, offerings, word, gold, sign, throne |
| status given | none | 24 | holy (a people holy to the Lord), blessed, called, beloved friend, weak, lowly, poor, rich, foolish, wise |
| human party | T8 Party-Human | 19 | enemy, flesh ("human being"), false prophets, orphan, the righteous, the wicked |
| event or setting | none | 17 | battle (11), strife, a legal case, a feast |
| outcome | none | 16 | save, salvation, shame (as a fate), glory, death, fall |
| moral value chosen | none | 15 | the good, the evil, what is right, justice, wickedness, violence |
| attribute of the chosen men | none | 12 | able, valour, mighty, new (gods), inexperienced |
| divine party | T7 Party-Divine | 11 | the Holy One, the (Holy) Spirit, Lord of hosts |
| place or realm | T10 Places | 8 | kingdom, palace, holy land, holiness of the temple |
| circumstance | none | 7 | affliction, distress, means |
| law, covenant, word | none | 6 | commandments, instruction, covenant, rules |
| value comparison | none | 6 | "better than" (H2896A, 4), riches, favour |
| course of conduct | none | 5 | way (M76) |
| natural world | T13 Natural-World | 5 | the thicket of the Jordan, perennial (pasture), beasts |
| verdict on a party | none | 3 | perverse, rebellious, abomination |
| body | T14 Body-Parts | 3 | hand (power), uplifted (arm) |
| divine attribute | T7 | 2 | power, excellencies |
| time | none | 2 | all the days of his life, the foundation of the world |
| corporate | T11 Corporate-Collective | 2 | assembly, church |
| function word | none | 2 | "against" (H7122H, M37) |
| quality that draws the choice | none | 1 | Gen 6:2, "attractive" |

- **ESV elisions:** some surfaces are function words, such as "of" and "and" (H8269), "to" (H6310I) and "another" (H1779). The Hebrew repeats the word and the ESV leaves it out. These are real occurrences, not mis-tags.
- **No existing T-code fits 13 of the kinds.** These are status, event or setting, outcome, moral value, attribute, circumstance, law, value comparison, course of conduct, verdict, time, function word, and the quality that draws the choice. They come to 116 rows. See judgement point J3.

## 5. By M-code

Of the 68 M-codes:
- 33 have only qualifier rows
- 8 have no qualifier rows
- 27 are mixed. The main ones are below, and all the counts are in the summary CSV.

**M-codes whose words are only qualifiers in these verses (33):**
- M10 Violence (battle)
- M14 Deceit (false prophets, devil)
- M22 Praise
- M25 Life & Death
- M26 Judgment
- M32 Covenant
- M33 Rest
- M36 Worship & Service
- M37 Firstborn
- M42 Prayer
- M43 Prophecy
- M44 Fellowship
- M46 Wealth
- M54 Torah
- M55 Destruction (idol)
- M65 Speech
- M72 Authority (51 rows, the largest)
- M76 Walk
- M79 Salvation
- M80 Blessing
- and 13 M-codes with one or two rows each: M03, M48, M49, M52, M57, M70, M71, M73, M77, M78, M81, M82, M84

**M-codes with no qualifier rows (8).** Each row is human (HIB), God's (DIV), or both:
- M01 Fear
- M02 Anger
- M04 Joy
- M19 Trust
- M20 Doubt (grumble, 1 row)
- M50 Grace & Mercy (3 HIB, 2 DIV)
- M64 Will (*"God's purpose of election"*, 1 DIV)
- M69 Eagerness

**Mostly inner-being, with some qualifier rows (6):**

| M-code | HIB | DIV | QUAL |
| --- | --- | --- | --- |
| M15 Knowing | 17 | 1 | 2 |
| M18 Desire | 7 | 7 | 6 |
| M47 Inner seat | 9 | 3 | 7 |
| M51 Love | 4 | 7 | 1 |
| M30 Rejection | 6 | 4 | 3 |
| M13 Faith | 7 | 1 | 5 |

**Mostly qualifier, with a few inner-being rows (the largest of the mixed M-codes):**

| M-code | HIB rows | QUAL rows |
| --- | --- | --- |
| M23 Strength | 2 | 17 |
| M61 Holiness | 1 | 14 |
| M58 Wickedness | 1 | 11 |
| M45 Renewal | 1 | 11 |
| M12 Righteousness | 1 | 8 |
| M24 Faintness | 1 | 7 |
| M16 Wisdom | 1 | 7 |
| M07 Shame | 2 | 5 |

## 6. Words that change face (#1919): 28 Strong's

The full list is in the summary CSV (`face_count` > 1). These are the ones that matter most for choosing:

- **H2896A *ṭôb* "good, pleasant"** (M18) has four faces:
  - the chooser's own liking: *"wherever it suits him"*, *"whatever seems good to you"*
  - the quality that draws the choice: Gen 6:2, *"attractive"*
  - the moral good that is chosen: Job 34:4
  - "better than", a value comparison: Psa 84:10, Pro 8:19, Pro 16:16, Pro 22:1
- **H3045 *yādaʿ* "know"** (M15) has six faces:
  - the ground of choosing: Isa 7:15–16
  - paired with choosing: Job 34
  - the purpose of being chosen: Isa 43:10
  - a response: 1Sa 20:30
  - a contrast: Isa 45:4
  - God making himself known, an operation: Num 16:5, Eze 20:5
- **H3988A *māʾas* "reject"** (M30):
  - human refusing, paired with choosing: Isa 7:15–16, Job 34:33
  - God's rejecting, set against his choosing: Psa 78:67, 2Ki 23:27, Isa 41:9, Jer 33:24
- **H2654A *ḥāpēṣ* "delight"** (M18):
  - God's delight as the measure of what is chosen: Isa 56:4, Isa 65:12
  - the human soul delighting: Isa 66:3
- **H6918G / G0040G "holy"** (M61):
  - mostly a status given to the chosen, or the divine name (the Holy One, the Holy Spirit)
  - once the purpose of being chosen: Eph 1:4, *"that we should be holy and blameless"*

## 7. Judgement points for the researcher

- **J1. Prayer, speech and service as operations.**
  - M42 Prayer (25 rows), M36 Worship & Service (13) and M65 Speech (13) are all counted as outward acts (T3-like).
  - In these verses they are the acts done at or toward what was chosen. One example is praying toward the chosen city.
  - Jos 24:15 and 22 (*"choose this day whom you will serve"*) make serving **what is chosen**. It is still counted as an operation.
  - Should prayer and serving count as operations here, or as inner-being words?
- **J2. Moral values as the thing chosen.** "The good", "the evil", "what is right" and "wickedness" (15 rows) are counted as qualifiers: they name the moral quality of what is chosen. Inner possessions that are chosen are counted as HIB. These are wisdom, understanding, knowledge and faithfulness (4 rows). Is this line right?
- **J3. Qualifier kinds with no T-code.** 116 qualifier rows fall in 13 kinds that have no existing T-code (§4). They are recorded descriptively. No new code is proposed.
- **J4. Status given by God.** "Holy", "beloved", "blessed" and "called", said of the chosen, are counted as a status (a qualifier). Traits the chosen live out are counted as HIB. These are faith, kindness, patience and humility (Col 3:12, Act 6:5, Rev 17:14). Col 3:12 has both kinds in one verse.
- **J5. Single-reading calls.** These rows rest on one reading of the verse and are open to correction:
  - Eph 1:4, *"In love"*: whose love it is. It is taken as the purpose of the chosen.
  - Job 15:5, iniquity as the ground of the choosing
  - Num 17:5, grumbling as the ground of God's choosing
  - Isa 41:8, *"Abraham, my friend"*, taken as a status

## 8. What this gives the strand

- The **HIB set of 99 rows** in §2 is the working list for "what operates with choosing" in the uncited verses.
- Of these, **28 rows are in the chooser's own choosing (§2a)**:
  - ground: knowing, liking, pleasure, fear, not listening, iniquity, eagerness
  - paired: refuse, reject, envy, desire, delight, hold fast, take care
  - object: wisdom, knowledge, faithfulness
  - response: shame
- The **DIV set (§3)** is the ground of God's choosing, for route A and Ch 13.1.
- The **qualifier set** places the verses: who, where, which office, and what event. It stays in the data. Under rule 72 and #1930 it is not material for the narrative in its own right.
