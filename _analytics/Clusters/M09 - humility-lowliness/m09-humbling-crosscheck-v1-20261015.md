# M09 humbling fan-out: cross-check against the narrative, the claims register, M08 Pride and M47

**Date:** 2026-10-15 · **Escalation:** #2148 · **Status:** check only. Nothing in the narrative or register is changed. The corrections found are listed for the researcher (§5).

**Instruction (researcher, chat 2026-10-15, verbatim):** *"proceed with the comparison, and the cross check"*.

The scope (§3) set three checks: against M08 Pride, against M47 (#1979, dropped placements by word), and against the narrative. This file also checks against the claims register, under rule 77: the register keeps the narrative honest (no claim without basis, no fitting, no dropped verses).

**Data.** Script [`m09-humbling-crosscheck-pull-v1-20261015.py`](m09-humbling-crosscheck-pull-v1-20261015.py) → [`m09-humbling-crosscheck-v1-20261015.csv`](m09-humbling-crosscheck-v1-20261015.csv). It covers 183 verses: every verse decided read or carried in batches 1–5.

For each verse the CSV gives:
- where the narrative cites it now, and whether the citing paragraph uses a humbling word
- its claims-register links
- whether it shares M08 or M47
- its inner-seat words (heart, spirit, soul, mind), and whether it is cited in a faculty chapter (Ch 3–9)

**Note on the tool.** `narrative_citation.passage_id` is empty for 6,513 of 6,540 current citations, because `narrative_passage` holds only the register's 121 passages. So the script finds the citing paragraph in the current chapter file instead. "Uses a humbling word" is a crude aid: the word is often only in the quoted verse. The judgments in §2 and §5 come from reading the paragraphs.

## 1. Figures

| Measure | Count |
| --- | --- |
| Verses checked | 183 |
| Cited in the narrative now | 55 (30%), in 23 chapters/sections. Most: Ch 11 (13), 10.13 (10), 10.7 (10), 10.1 (8), Ch 4 (7), 13.1 (7) |
| Not cited anywhere | 128 |
| Sources in the claims register | 5 (2Ch 7:14 → 10-5; Pro 17:22 → 2-9, withdrawn; Psa 34:18 and Psa 51:17 → 1-1; Phili 2:8 → C-160) |
| Sharing M08 Pride | 29, of which 1 is in Ch 12 *Pride and the lifted-up heart and spirit* (Pro 16:19) |
| Holding an inner-seat word | 49, of which 16 are in a faculty chapter (Ch 3–9) |

**The humbling angle has no home.** The 55 cited verses are placed for other reasons:
- anger in 10.13
- fear in 10.1, 10.9 and 10.12
- choosing and willing in 10.7
- the heart in Ch 4, the spirit in Ch 6
- death in Ch 2
- jealousy in 13.1 and Ch 11
- authority in Ch 11 and 10.10

Read for what they say there, most of these placements are sound. Exceptions are in §5. The point is that no paragraph anywhere tells humbling as itself. That is what 10.14 *Humility* will do (decided 2026-10-15).

## 2. Against the narrative: how the cited verses are carried

**Placements that carry the humbling, in another chapter's frame (sound; to point to 10.14 at the weave):**
- **10.13 *Anger*.** Humbling oneself turns wrath: 2Ch 12:7, 12:12, 32:26, 33:12; 2Ki 22:19; Zep 2:3; and Ahaz and Manasseh in distress. This matches batch 1 group I.
- **Ch 6 *The human spirit*.** *"It is lowly or proud, and it is judged"*, with Pro 16:18, Mat 5:3, Isa 57:15 and Isa 66:2. Also *"It is crushed, and it faints"*, with Pro 15:13, 18:14 and Exo 6:9 (*"A broken spirit can keep a person from even hearing good news"*). This matches batch 3 groups II and III.
- **Ch 14 *Revived, restored, renewed*.** Isa 57:15 with 57:16.
- **Ch 11.** Psa 51:17, *"Offered to God, a crushed spirit is the very sacrifice he wants"*. Batch 3 group I.
- **10.7 *Put on*.** Col 3:12.

**Placements where the verse's humbling side is not told** (not errors; the angle is for 10.14 and the weave):
- **Isa 66:2** in 10.1, 10.9 and 10.12 is carried for *"trembles at my word"*. Its *"humble and contrite in spirit"* is told only in Ch 6's list.
- **Phili 2:8** is in Ch 2 only, for the death Christ *"went to … himself"* (claim C-160). His humbling is told nowhere. 13.1 has no paragraph on Jesus humbling himself, emptying himself or being lowly in heart.
- **Luk 2:51** is in Ch 4 for Mary's heart. The Son *"was submissive to them"* is not told.
- **Mat 11:29** is in Ch 11 *Inner states pass between people*, for rest. *"gentle and lowly in heart"* is not taken up for itself.
- **Dan 4:37, Dan 5:19 and Dan 5:22** are in 13.1, Ch 4 and 10.7 *Willing*, for God's will and the heart. Belshazzar's *"have not humbled your heart, though you knew all this"* is not told as humbling refused.
- **Exo 6:9** in 10.2 opening is for hearing. The broken spirit is told in Ch 6. This is sound.

## 3. Against M08 Pride (29 shared verses)

Only **Pro 16:19** is in Ch 12 *Pride and the lifted-up heart and spirit*. The other 28 humble/proud verses are not in the pride section:

- **Isaiah:** 2:11, 2:12, 2:17, 5:15, 10:33, 13:11, 25:11, 26:5
- **Ezekiel:** 17:24, 21:26
- **Job:** 5:11, 22:29, 40:11, 40:12
- **Proverbs:** 3:34, 11:2, 18:12, 29:23
- **Psalms:** 34:2, 138:6
- **2Ch 32:26** (Hezekiah *"humbled himself for the pride of his heart"*)
- **Dan 4:37** (*"those who walk in pride he is able to humble"*)
- **Isa 57:15**
- **1Pe 5:5, Jam 4:6** (*"God opposes the proud"*)
- **Rom 12:16** (*"Do not be haughty"*)
- **Col 2:18** (*"puffed up"*)
- **Jam 1:9**

**What Ch 12 holds:**
- Deu 8:14, Pro 16:5, Pro 16:18–19, Dan 5:20, Isa 14:13–14, Eze 28, Eze 31, Psa 50:21, Luk 1:51, Esther 6, Dan 4:30–31 and Isa 14:10–11. It tells pride's seat (heart and spirit), its false likeness, its growth from a given beauty, and its fall.
- It tells pride's fall but not its counterpart. The humble raised, the proud brought low *"and the Lord alone will be exalted"*, is told nowhere.

**At the weave:**
- 10.14 tells the humbling.
- Ch 12 gains pointers.
- Hezekiah's turn from the pride of his heart (2Ch 32:25–26) and Belshazzar's refusal (Dan 5:22) are the two direct joins. Ch 12 already has the next verse in each case (Dan 5:20).

M08 has not been read as a strand. This is the humility side only.

## 4. Against M47 (#1979: dropped placements, by word)

Of the 49 verses with an inner-seat word, 16 are in a faculty chapter (Ch 3–9). The other 33 are not:

| Seat | Verses not in a faculty chapter | Faculty chapter to receive them at the weave |
| --- | --- | --- |
| **heart** | Lev 26:41 (*"uncircumcised heart is humbled"*); Deu 8:2 (*"to know what was in your heart"*); 2Ch 34:27 (*"your heart was tender"*); Dan 10:12 (*"set your heart to understand and humbled yourself"*); Psa 107:12 (*"he bowed their hearts down"*); Pro 18:12 (*"a man's heart is haughty"*); Mat 11:29 (*"lowly in heart"*); Psa 38:8; Psa 69:20; Psa 109:22 (*"my heart is stricken"*); Jer 23:9; Eze 6:9 (God over *"their whoring heart"*); 1Pe 3:15 | Ch 4 *The heart* (Eze 6:9 and Mat 11:29 also to 13.1) |
| **brokenhearted** | Psa 147:3; Psa 109:16; Isa 61:1 | Ch 4 / Ch 6 |
| **spirit** | Pro 16:19, Pro 29:23 (*"lowly in spirit"*); Job 17:1 (*"My spirit is broken"*); Gal 6:1, 1Cor 4:21 (*"a spirit of gentleness"*); 1Cor 14:32 (*"the spirits of prophets are subject to prophets"*); Heb 12:9 (*"the Father of spirits"*) | Ch 6 *The spirit* (Heb 12:9 also to 13.1) |
| **soul** | Psa 34:2 (*"My soul makes its boast in the Lord"*); Jam 1:21 (*"able to save your souls"*); Heb 13:17 (*"keeping watch over your souls"*); Mat 11:29 (*"rest for your souls"*) | Ch 5 *The soul* |
| **mind** | Col 2:18 (*"puffed up … by his sensuous mind"*); Rom 8:7 (*"the mind that is set on the flesh"*, cited in 10.7 and Ch 12) | Ch 3 / Ch 7 *Flesh* |
| **other surfaces** | Isa 58:3, 58:5 (*"ourselves"*, *"himself"*, from *nephesh*); Isa 11:4 (*"breath"*); Luk 10:20 (*"spirits"*, other beings, 13.3); Col 2:23 | these words name the self or other beings; no faculty placement is needed |

Under #1979 (*"I will tackle them as we move through the clusters"*), these are the M09 strand's dropped placements by word. They are for the weave, chapter by chapter, by what each verse says of that seat.

## 5. Narrative statements to correct (rule 77: the register keeps the narrative honest)

Found while reading the citing paragraphs. Each is a statement that goes beyond its verses or fits a verse to a line it does not carry. **None is changed.** Under #1982 D3, an existing reading is reset only on the researcher's instruction.

| # | Where | Statement | What the verse says | Proposed |
| --- | --- | --- | --- | --- |
| 1 | Ch 12 *Pride and the lifted-up heart and spirit* | *"Pride and humility are where the spirit is weighed most"* | the verses cited (Pro 16:18–19; Mat 5:3) place pride and lowliness in the spirit. None says "most", and no count was made | remove "most": *"Pride and humility are where the spirit is weighed: haughty or lowly, proud or poor in spirit."* (`feedback_avoid_unsubstantiated_superlatives`) |
| 2 | 10.8 *Right and wrong* (opening) and 10.13 *How it is provoked* | Mic 6:8 cited for *"Wrong done to the weak draws God's anger as surely as idols do"* | Mic 6:8 names what the Lord requires: *"to do justice, and to love kindness, and to walk humbly with your God"*. It names neither anger nor the weak. Exo 22:23–24, cited beside it, does | drop Mic 6:8 from the anger statement and keep Exo 22:23–24. Place Mic 6:8 for what it says (10.14; 10.8 for justice and kindness) |
| 3 | Ch 11 *Inner states pass between people* | *"Jesus offers rest that passes from his heart to ours"* | *"learn from me, for I am gentle and lowly in heart, and you will find rest for your souls"*. Rest is found in learning from him; the verse does not say it passes from his heart | restate as the verse has it, or mark **I read** |
| 4 | Ch 14 *Held — not yet re-examined*; claim **10-5** (Held) | *"The seven conditions for the Spirit's work (2 Chronicles 7:14). This belongs to the companion study of the Holy Spirit."* | *"if my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land"*. It names no Spirit, and the count of seven is not in the verse | now read (batch 1 group I): take it out of *Held* into 10.14 (and Ch 14 if wanted) for what it says, and restate or withdraw claim 10-5 |
| 5 | claim **1-1** (*"Soul and spirit in synonymous parallel"*, verdict Widened) | the sources include Psa 51:17 and Psa 34:18 | both pair **heart** and **spirit**, not soul and spirit. Ch 3 lists them correctly under *"Heart and spirit"* | check whether 1-1 was widened to cover heart and spirit. If not, the two sources belong to a heart-and-spirit claim (compare #2146, register source rows) |

## 6. Summary for the weave

1. **10.14 *Humility*** tells the whole: the readings, the OT/NT comparison and Jesus' role (`m09-humbling-ot-nt-and-jesus-v1-20261015.md`).
2. **The angles go to their chapters in context** (placement decision): 10.9, 10.7, 10.10, 10.2, 10.13 (already there), Ch 6/Ch 11, Ch 12, 13.1. Add §4's faculty placements: Ch 4, Ch 5, Ch 6.
3. **13.1** gains *Lowering himself*: God's lowering, and the Son's (comparison §4).
4. **Ch 12** gains the humbling counterpart's pointers and the two direct joins (§3).
5. **§5's five corrections**, on the researcher's word.
6. **Claims register:** a weave record (`Narrative-Register.ps1 -Action Record`) with the new claims and tellings, as for every weave since #2110.
