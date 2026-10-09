# M18 verses shared with M47, M25 and M02: pull, cross-reference and test validation

**Date:** 2026-10-09 · **Escalation:** #1993 · **Status:** pull and cross-reference done; a test batch of 6 verses for your review. Nothing is changed in the narrative.

**Asked (researcher, verbatim):** *"M18 verse bind with M47, M25 and M92. All these verses should already be in the narrative. However their interpretation and meaning may be incomplete or too narrow and need review. so pull all these verses into a csv and then work through the these three cluster analysis already done to validate the interpretation and the placing of the verses in the narrative."*

**M92:** there is no M92 in `cluster`. I have taken **M02 Anger & Wrath** as meant: its analysis is done, it shares 59 verses with M18, and OT-19 holds exactly these verses "for when M18 is analysed". M72 Authority & Dominion (182 shared verses, no analysis yet) is carried as a flag column only. **Please confirm M02.**

**Files:**
- Pull: [`m18-shared-m47-m25-m02-pull-v1-20261009.py`](m18-shared-m47-m25-m02-pull-v1-20261009.py) → [`m18-shared-m47-m25-m02-verses-v1-20261009.csv`](m18-shared-m47-m25-m02-verses-v1-20261009.csv)
- Narrative and open-threads cross-reference: `verse-narrative-ot-crossref-v2-20261006.py` (M64 folder, reused unchanged) → `…-crossref-v1-20261009.csv`
- Analysis cross-reference: [`m18-shared-analysis-crossref-v1-20261009.py`](m18-shared-analysis-crossref-v1-20261009.py) → **[`m18-shared-m47-m25-m02-crossref-v2-20261009.csv`](m18-shared-m47-m25-m02-crossref-v2-20261009.csv)**. This is the working file: one row per verse, with the M18 words, the partner words, the delight-filter bucket, the narrative places, the open threads, every analysis file that cites the verse, and the ESV text.

## 1. The set

| | Verses |
| --- | --- |
| M18 × M47 | 208 |
| M18 × M25 | 111 |
| M18 × M02 | 59 |
| **Distinct verses** | **348** |

Overlaps: M47 + M25 22, M47 + M02 5, M25 + M02 3. M72 is flagged on 45 of the 348.

## 2. What the cross-reference shows

**Every verse was read in its partner's analysis. About two in three are not cited in the narrative.**

| Partner | Shared | In its analysis | Cited in the narrative | Analysed, not cited |
| --- | --- | --- | --- | --- |
| M47 | 208 | 208 | 63 | 145 |
| M25 | 111 | 111 | 43 | 68 |
| M02 | 59 | 59 | 27 | 32 |
| **All (distinct)** | **348** | **348** | **112** | **236** |

So the premise "all these verses should already be in the narrative" holds for 112 of the 348. The other 236 were read in a cluster analysis but did not reach the narrative.

Where each partner read them:
- **M47:** [`M47-x-willing-desiring-batchC-v3-20260928.md`](../M47%20-%20inner-seat/M47-x-willing-desiring-batchC-v3-20260928.md) §1, "Desire and longing (M18)", §1.1–1.13. This is the M47 × M18 reading. Other M47 batches (D, E, H, G, F, B, A) and the depiction file also cite some of these verses. **Batch C is dated 2026-09-28.** That is before the narrative reset (#1912), the change-of-character rule (#1919), "let Scripture speak" (rule 69) and the weave rulings (#1918, #1930).
- **M25:** the observation ledgers, units 1–4 and Q2–Q4, with a face for each verse in the faces CSVs (unit 3: 54 verses; unit 2: 43). Most of these are in "Living before God" (unit 3) and "Dying and death" (unit 2).
- **M02:** the anger unit ledgers 1–5, the faces CSVs, and the cross-ledger overview §F (M18 row: 59 verses). All 59 verses are in OT-19.

Where the 112 cited verses are placed (citations, a verse can be in several places): 10.13 Anger 32, Ch 2 28, Ch 11 27, 10.6 Wanting 15, Ch 5 13, Ch 12 12, 10.7 11, 10.1 11, 10.4 8, Ch 4 8, and fewer elsewhere. **13.1 Divine has 3.**

## 3. The validation method

Each verse is read in its passage, with no framework (the M64 method from 2026-10-07). Then three things are set side by side:
1. **The analysis:** what the partner cluster's reading said about the verse.
2. **The narrative:** where the verse is placed, and what the narrative says it means there.
3. **The reading:** what the verse says in its passage, with the M18 word in view.

The result for each verse:
- **Interpretation:** sound, or incomplete, or too narrow, or misread. If it is not sound, the record says what is missing.
- **Placement:** confirmed, or to add, or to move, or not for the narrative (route C), with the place proposed.
- **Proposal:** the change. Nothing is applied until you approve it.

I suggest the 348 verses are worked partner by partner, M47 then M25 then M02, in batches by analysis section (for M47, batch C §1.1 to §1.13). Each verse in an overlap is done once, under the first partner.

## 4. Test batch: 6 verses

One cited and one uncited verse from each partner.

### 4.1 Pro 21:1 (M47; cited in Ch 4 and Ch 11)

> "The king's heart is a stream of water in the hand of the Lord; he turns it wherever he will." (21:2: "Every way of a man is right in his own eyes, but the Lord weighs the heart.")

- **M18 word:** "wherever he will" is *ḥāpēṣ* (H2654A, "to delight in"): wherever he pleases.
- **Analysis:** batch C §1.12, "Divine desire and delight", under "God's heart and will". This is right.
- **Narrative:**
  - Ch 4, "The heart feels" ¶2, uses it among the "materials" Scripture uses "to describe what state a heart is in", next to stone, wax and fat.
  - Ch 11 §1 has it as "God turns and puts things into hearts".
- **Reading:** the verse is not about the state the king's heart is in. It is about where it is directed: water channelled, turned where the Lord pleases. 21:2 sets it beside the Lord weighing the heart.
- **Interpretation:** **too narrow** in Ch 4; sound in Ch 11. In both places the M18 face, God's *pleasure* directing the heart, is not said.
- **Placement:**
  - **To add** in 13.1 *Willing*, as God's pleasure directing a human heart. 13.1 does not carry the verse now.
  - Ch 4: reword the clause so that the stream is a heart being directed, not a state.

### 4.2 Mat 5:28 (M47; not cited)

> 5:27–30: "'You shall not commit adultery.' But I say to you that everyone who looks at a woman with lustful intent has already committed adultery with her in his heart. If your right eye causes you to sin, tear it out …"

- **M18 word:** "with lustful intent" is *epithumeō* (G1937), "to desire", in the infinitive: he looks in order to desire her.
- **Analysis:** batch C §1.3, "Heart-desire toward sin". Its reading: "The heart is where desire is either consented to or governed. Mat 5:28 places the act itself in the heart before any deed." The second sentence is what the verse says. The first joins this verse to 1Co 7:37 into a statement neither verse makes.
- **Narrative:** not cited anywhere. Matthew 5 is cited only for anger (5:22, in 10.10 and 10.13).
- **Reading:** Jesus places the adultery "in his heart". The way in is the eye ("looks … to desire"), and 5:29 goes straight on to the eye that causes sin. The desire is counted as the act.
- **Interpretation:** the analysis is sound in its second sentence. The first is a join to drop.
- **Placement:** **to add** in 10.6 *Wanting*, where wrong desire is treated: desire in the heart, entered through the eye, counted as the deed. Also in Ch 4, "The heart feels", which already lists "desires" with Psa 37:4 only.

### 4.3 Jon 4:3 (M25; cited in Ch 2 and Ch 5)

> 4:1–4: "But it displeased Jonah exceedingly, and he was angry … 'for I knew that you are a gracious God and merciful … and relenting from disaster. Therefore now, O Lord, please take my life from me, for it is better for me to die than to live.' And the Lord said, 'Do you do well to be angry?'"

- **M18 word:** "better" is *ṭôb* (H2896A), Jonah's own weighing of death against life (the delight filter's "judged good by someone" kind).
- **Analysis:**
  - M25: D12 "wanting to die", L14 "life weighed from within", S03 "the soul … asks to die".
  - Batch C §1.7: "Life 'better' gone".
  - M02 notes the anger side through Jon 4:4 (AG-58) and holds the death side under OT-08.
- **Narrative:**
  - Ch 2, *Wanting to die*: listed with Elijah, Job and Saul. Further down, Ch 2 says "Jonah's wish came with his anger at God's mercy: 'angry enough to die' (Jonah 4:9)".
  - Ch 5, "Loving and hating one's own soul" ¶3: "a third kind of hating one's life, which is exhaustion rather than discipleship", with Job 10:1, Ecc 2:17 and Jon 4:3.
- **Reading:** in 4:3 the wish comes straight out of 4:1–2, from Jonah's displeasure and anger that God is gracious and relents. The "better" is his own judgement. God answers with a question about his anger (4:4). Only at 4:8 is he "faint" from the sun.
- **Interpretation:** **misread in Ch 5.** Jon 4:3 is not exhaustion; the passage gives anger at God's mercy as its ground. Ch 2 is sound.
- **Placement:** confirmed in Ch 2. **Ch 5: to correct.** Either take Jon 4:3 out of the "exhaustion" sentence or say what its ground is. Jon 4:8 fits "faint" better.

### 4.4 Psa 34:12 (M25; not cited, but its NT quotation is)

> 34:11–14: "Come, O children, listen to me; I will teach you the fear of the Lord. What man is there who desires life and loves many days, that he may see good? Keep your tongue from evil … Turn away from evil and do good; seek peace and pursue it."

- **M18 word:** "desires" is *ḥāpēṣ* (H2655, "delighting"): the man who delights in life.
- **Analysis:** M25 unit 3, LD-101, face L09: "long life … with keeping, fearing, honouring".
- **Narrative:** not cited. Peter's quotation of it, 1Pe 3:10 ("Whoever desires to love life and see good days"), is in Ch 2 (long days) and 10.5 *Speaking*.
- **Reading:** the psalm sets the wish for life inside a lesson in "the fear of the Lord" (34:11). Its answer is a way of living: tongue, turning from evil, doing good, pursuing peace.
- **Interpretation:** sound in the M25 face. The M18 face, delighting in life as a want, is not said anywhere.
- **Placement:** covered by a parallel (1Pe 3:10) in Ch 2 and 10.5. **Possible add** in 10.6 *Wanting*, as the want for life itself and what the psalm sets to meet it. This is a low-priority judgement for you.

### 4.5 Pro 6:34 (M02; cited in 10.1, 10.13 and Ch 11)

> 6:32–35: "He who commits adultery lacks sense; he who does it destroys himself … For jealousy makes a man furious, and he will not spare when he takes revenge. He will accept no compensation; he will refuse though you multiply gifts."

- **M18 word:** "jealousy" is *qinʾāh* (H7068).
- **Analysis:** M02 AG-74, "The husband's fury" (face 2S). Setting Pro 6:20–35; jealousy "makes" the fury, and the fury refuses a gift. The F.5 note sets this beside Eze 16:38 and says no verse joins them.
- **Narrative:**
  - 10.1: "Grief makes it tender; jealousy makes it hard".
  - Ch 11: "Joined with jealousy, it 'will accept no compensation'".
  - 10.13 *Connections*: "jealousy with anger".
- **Reading:** in this verse jealousy is the cause ("makes … furious") and refusal is what it does. The setting is a marriage violated by another man.
- **Interpretation:** sound. "Hard" in 10.1 is a reading of "will not spare … will accept no compensation". It is fair, but it should be marked "I read".
- **Placement:** confirmed. Jealousy itself, its faces and why they differ (God's, a husband's, envy of the wicked), has no account yet. That is for the M18 jealousy words (overview §3D, 112 hits), not for this verse.

### 4.6 Psa 37:1 (M02; not cited, though Psa 37:3–8 is)

> 37:1–4: "Fret not yourself because of evildoers; be not envious of wrongdoers! For they will soon fade like the grass … Trust in the Lord, and do good … Delight yourself in the Lord, and he will give you the desires of your heart."

- **M18 word:** "be not envious" is *qānāʾ* (H7065). The M18 delight word (*ʿānag*, H6026) is in 37:4.
- **Analysis:** M02 AG-140, "'Fret not yourself': the burning verb turned on oneself" (face 3W). F.6 notes that envy is named beside the anger and is not to be read into it.
- **Narrative:**
  - 10.1 gives 37:8 and lists "Trust … Commit … Be still" (37:3, 5, 7) as what the psalm puts in place of the heat.
  - 10.6 opens with 37:4 on its own.
  - 37:1 is not cited, so envy is not named.
- **Reading:** the psalm's own first line pairs fretting with envy of wrongdoers. Its answers include "Delight yourself in the Lord" (37:4), which comes between "trust" (37:3) and "commit" (37:5).
- **Interpretation:** **incomplete.** The narrative splits Psalm 37: heat goes to 10.1, desire to 10.6. In 10.1 the list of what replaces the heat leaves out 37:4, and the envy of 37:1 is not named.
- **Placement:** **to add** 37:1 in 10.1 beside 37:8, with "Delight yourself in the Lord" (37:4) added to the psalm's list. This is the psalm's own order, not a join. 10.6 could point back to it.

## 5. What the test shows

Of the 6 verses:

| Verse | Interpretation | Placement |
| --- | --- | --- |
| Pro 21:1 | too narrow (Ch 4) | add 13.1; reword Ch 4 |
| Mat 5:28 | sound (one join to drop) | add 10.6 and Ch 4 |
| Jon 4:3 | misread (Ch 5) | correct Ch 5 |
| Psa 34:12 | sound | covered by a parallel; possible add in 10.6 |
| Pro 6:34 | sound ("I read" marker needed) | confirmed |
| Psa 37:1 | incomplete | add in 10.1 |

In five of the six, the **M18 face** of the verse (the pleasure, the desire, the judging "better", the envy) is what the partner reading did not carry. That is what you expected: the partner clusters read these verses for their own word.

Something to keep in view: 10.6 *Wanting* is a short chapter of 38 lines with no sections. The other key characteristics, fear (10.12) and anger (10.13), each got a full account of their own (#1961). M18's verses will add to 10.6 throughout this work. Whether 10.6 later becomes that kind of account is your call, and not part of this step.

## 6. For your direction

1. **Confirm M02** as the third partner (in place of "M92").
2. **The method and its result format** (§3, §4): approve, or adjust.
3. **The order:** M47 (batch C §1.1–1.13) first, then M25, then M02.
4. **The test-batch proposals** (§5): apply now, or hold all changes until a partner is finished.
