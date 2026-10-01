# Candidate next strand — Fear (from the M01 extract)

**Date:** 2026-10-01 · **Version:** v2 (adds §3A, surface forms; corrects §3.1; v1 in `archive/`) · **Status:** strand **approved** 2026-10-01 (#1927) · **Source:** iba.db (read-only), the researcher's M01 extract query

## 1. What was run

- **Query as given.** The `other_m_hits` filter is `cs.cluster_code = 'M01'`, so it pairs M01 words only with **other M01 words in the same verse**, including each word with itself (distance 0).
  - Result: 1,303 rows over **916 verses**.
  - **100 verses** hold two or more fear words.
  - Output: not kept (superseded by the variant, decision 1 below).
- **Variant `<> 'M01'`.** The same query with one change, so that M01 words are paired with every **other** cluster in the verse. This is what shows the strand's links to the rest of the web.
  - Result: 19,955 rows over the same 916 verses.
  - Output: `fear-web-pull-v1-20261001.csv`; query: `fear-web-pull-query-v1-20261001.sql`.

Both files are in this folder.

## 2. M01 vocabulary (hits in the 916 verses)

| Strong | Gloss | Hits |
| --- | --- | --- |
| H3372G | to fear | 204 |
| H3372H | to fear: revere | 110 |
| G5399 | to fear | 94 |
| H3373 | afraid | 65 |
| H6343 | dread | 49 |
| G5401 | fear | 46 |
| H3374 | fear | 45 |
| H7264 | to tremble | 41 |
| H2729 | to tremble | 39 |
| H6342 | to dread | 25 |
| H8047G/H | horror (destroyed / appalled) | 22 / 17 |

The remaining 80+ Strong's numbers have 17 hits or fewer each: terror, trembling, shuddering, horror, agony, timidity, reverence, and others.

## 3. What the data shows (counts only, no reading yet)

### 3.1 One word, two faces: STEP splits H3372 — but the surface does not follow the split

| Strong | Verses | LORD/God within 5 words | Negated ("not" within 2 words before) |
| --- | --- | --- | --- |
| H3372G to fear | 200 | 62 | **67** |
| H3372H to fear: revere | 107 | **75** | 8 |
| H3374 fear (noun) | 45 | 30 | 2 |
| G5399 to fear | 91 | 22 | 26 |
| H6343 dread | 48 | 18 | 1 |

- **"Do not fear":** a negator falls within 2 words before a fear word in **128 verses**.
- **Correction (v2, after the researcher pointed to surface):** the G/H suffix is not a reliable guide to the face. The surface shows this (§3A.1):
  - the surface "fear" occurs 88 times under H3372G and 55 times under H3372H
  - "awesome" occurs under both
  - "terrifying" occurs under both

  The face has to be read from the surface and the verse, not from the suffix or the gloss.

### 3.2 Links to other clusters (verses; "near" = within 3 words)

| Cluster | Verses | Near | Commonest near pairs |
| --- | --- | --- | --- |
| T7 Party-Divine | 407 | 248 | LORD, God |
| T14 Body-Parts | 208 | 117 | mostly H6440 "face: before" (largely prepositional; check before use), hand 26 |
| M47 Inner Seat | 97 | 50 | fear + heart 11; tremble / dread / revere + heart 4 each |
| M24 Faintness & Despair | 90 | **56** | fear + be dismayed 11 (1Ch 22:13, 28:20, 2Ch 20:15, 20:17, 32:7) |
| M23 Strength & Courage | 79 | 38 | fear + strengthen 13 (Deu 31:6, Dan 10:19, 2Ti 1:7) |
| M19 Trust & Refuge | 35 | 26 | tremble + security; fear + trust (Isa 12:2, Jer 17:17, Jam 2:19) |
| M33 Rest & Peace | 38 | 20 | tremble + rest; fear + peace (Isa 7:4, Hab 3:16, Jer 30:10) |
| M55 Destruction & Ruin | 33 | 19 | dread + devastation; shudder + appalled (Ezekiel, Jeremiah) |
| M02 Anger & Wrath | 35 | 12 | Deu 9:19, Psa 90:11, Psa 88:16, Heb 11:27 |
| M20 Doubt & Discouragement | 16 | 8 | fear + hide (Gen 3:10, Exo 3:6, Mat 25:25) |
| M48 Astonishment & Wonder | 13 | 7 | revere + wonder (Exo 15:11, Psa 139:14, Mar 16:8) |
| M51 Love & Devotion | 10 | 5 | 1Jo 4:18, 1Pe 2:17 |

The full table for all clusters is in `fear-web-pull-v1-20261001.csv`.

## 3A. Surface forms: how the English renders each root

Surface (`verse_lexical.surface`) is the English word or phrase that stands for the Strong's in that verse. The gloss gives one label per root. The surface shows the different ways the root is taken in different verses, so it is the first signal of a change of character (#1919).

- **1,032 M01 hits** carry **144 distinct surfaces**.
- These are renderings only. Each is a pointer to a verse to read, not a meaning.

### 3A.1 One root, several renderings (selected; full list in the data)

**H3372H "to fear: revere" (110 hits)**
- fear (55) · feared (13)
- **awesome (20)**: Deu 7:21, Deu 10:17, Neh 1:5, Psa 66:3, Psa 99:3, Gen 28:17 …
- awesome deeds / things / thing (7): Psa 145:6, Isa 64:3, Exo 34:10
- stood in awe (2): Jos 4:14, 1Ki 3:28
- reverence (2): Lev 19:30, 26:2
- terrifying: Deu 10:21
- awe-inspiring: Eze 1:22
- afraid: Gen 28:17

In the "awesome" verses the word is set on God or His deeds, not on the one who fears.

**H3372G "to fear" (204 hits)**
- afraid (89) · fear (88) · feared (17)
- frighten: 2Ch 32:18, Neh 6:9
- terrifying: Deu 1:19, 8:15
- awesome: Joe 2:31, Mal 4:5
- fearsome: Hab 1:7

**H3373 "afraid" (65 hits)**
- fear (36) · fears (10)
- **shuns**: Ecc 9:2
- **cautious**: Pro 14:16
- **reveres**: Pro 13:13

**G5401 / G5399 fear (Greek)**
- fear / afraid (most hits)
- **respect**: Rom 13:7, 1Pe 2:18, 3:15
- **respectful**: 1Pe 3:2
- **respects**: Eph 5:33
- **reverence**: Eph 5:21
- **awe**: Luk 5:26, Act 2:43, Mat 27:54
- **filled [with great fear]**: Mar 4:41
- terror: Rom 13:3

Fear is rendered as respect only toward people.

**H7264 rāgaz "to tremble" (41 hits)**
- tremble / trembled / trembles (17)
- **raging / raged / enraged** (5): 2Ki 19:27–28, Isa 37:28–29, Eze 16:43
- **quarrel**: Gen 45:24
- **disturbed**: 1Sa 28:15, 2Sa 7:10, 1Ch 17:9
- **deeply moved**: 2Sa 18:33
- **stirred up**: Isa 14:9
- quaked: 1Sa 14:15, Isa 5:25
- shudder: Isa 32:10–11

One root covers trembling and rage. **This links directly to the anger strand.**

**H6342 "to dread" (24 hits)**
- fear / afraid (13)
- **thrill**: Isa 60:5 ("your heart shall thrill")
- **awe**: Psa 119:161
- feel [dread]: Deu 28:67

**H2729 "to tremble" (39 hits)**
- tremble / trembling (15)
- **"no one shall make them afraid"** (5; wording per Mic 4:4): Mic 4:4, Zep 3:13, Eze 34:28, 39:26, Isa 17:2
- **come trembling**: Hos 11:11
- trembled violently: Gen 27:33
- taken [all this trouble]: 2Ki 4:13

**H1481C "to dread" (10 hits)**
- **awe**: Psa 22:23, 33:8
- **fearful awe**: 1Sa 18:15
- **intimidated**: Deu 1:17

**H6343 "dread" (49 hits)**
- fear (17) · terror (17) · dread (10)
- "in **great** terror": Psa 14:5, 53:5
- "the **thing** I fear": Job 3:25

### 3A.2 One English word, many roots

The surface hides root differences in the other direction too:

| Surface | Strong's numbers behind it |
| --- | --- |
| fear | 20 |
| terror | 15 |
| afraid | 14 |
| trembling | 11 |
| tremble | 10 |
| awe | 7 |

Reading by English word alone would merge roots that the Hebrew and Greek keep apart. Reading by root alone would merge faces that the English keeps apart. **Both are needed.**

### 3A.3 Surfaces where the English renders no fear at all

These hits are tagged M01, but the English shows another face.

| Strong | Surface | Verses |
| --- | --- | --- |
| H8047G | desolation / waste (18) | Jer 25:11, 25:18, Isa 24:12, Joe 1:7 … |
| H4288 | ruin | Pro 10:14, 10:15, 13:3, 18:7 |
| H4656 | [abominable] image | 1Ki 15:13, 2Ch 15:16 |
| H4867 | waves / breakers | 2Sa 22:5, Psa 42:7, 88:7, 93:4 |
| H8175B | tempest | Psa 50:3 |
| H2427A | pain / pangs | Jer 6:24, 22:23, 50:43, Mic 4:9 |
| H2866 | calamity | Job 6:21 |
| H6125 | oppression | Psa 55:3 |
| H0367 | idols | Jer 50:38 |
| H4035 | barn | Hag 2:19 |
| H6178 | gullies | Job 30:6 |
| H3374 | commandment | Isa 29:13 ("their fear of me is a commandment taught by men") |
| H3374 | exceedingly | Jon 1:10, 1:16 (fear in the Hebrew, intensity in the English) |

- Under the rule that a cluster tag shows one face only (#1919), these are **read, not dropped**.
- Re-allocating them is not proposed. Clusters are anchors, and re-allocation is low priority.
- Some are faces of fear carried into a place, an object or a body (desolation, waves, pangs). Whether each is a face of fear is for the verse to show.

## 4. Where fear stands in the narrative now

Fear appears only in passing. The places are:

- 10.1 Feeling: the heart's range; Psa 112:7; 2Sa 6:8–9
- Ch 11: the tender heart; Deu 20:8; Mat 25:24–25
- the "e.g." list in the index: fear is named there as a possible later strand

**No section traces fear the way the anger strand traced anger.**

## 5. Candidate

**Next strand: Fear.** It would be woven by activity, as anger was (#1920), and not given a chapter of its own.

Why this strand, from the data:

1. **Size.** 916 verses and about 90 Strong's numbers. Like anger before #1920, it is almost absent from the narrative.
2. **Change of character is already visible in the data.** STEP's own split of H3372 into "fear" and "revere" is visible before any reading (§3.1). #1919 asks for exactly this kind of record: the faces, the circumstances that differ, and why.
3. **It connects to strands already woven:**
   - inner seat (M47, 97 verses)
   - anger (M02, 35 verses, including Psa 90:11, "the power of your anger … your wrath according to the fear of you")
   - the origin of thought / hiding (M20)
4. **It opens the next nodes of the web without a whole-scope task.** Dismay (M24), strength and courage (M23), trust (M19) and rest (M33) come in only as far as fear's verses reach them.

**Suggested reading order (a strand, not a cluster pass):**

1. The H3372 pair and H3373/H3374, **grouped by surface, not by suffix**: afraid · fear · awesome · awe / reverence · respect (Greek). The 128 "do not fear" verses are one group within this.
2. Fear in the heart and body: M47 seats; trembling and shuddering words, **including H7264's rage / disturbed / deeply moved surfaces** (anger link); the hand and face only where they are not prepositional.
3. Fear's near neighbours, as the verses lead: dismay, strength, trust, rest, hiding.
4. Fear before God's acts and judgments (the M55 / M02 verses), in step with Ch 13, with the §3A.3 desolation / waste / waves / pangs surfaces read alongside.

**Chapters likely touched (to be confirmed by the reading, not assumed):** 10.1, 10.9, 10.10, 11 §4, 12, 13, 14.

**Alternative, if fear is held back:** M24 Faintness & Despair. It has the most near co-occurrences with fear of any M-cluster (56 verses), but it is smaller and would mostly arrive through fear anyway.

## 6. Decisions (researcher, 2026-10-01, #1927)

Researcher, verbatim: *"1 - accept your correct as <> 2- yes 3 - _analytics/cross-cluster-web/fear/"*

1. The extract filter is **`<> 'M01'`** (fear with the rest of the web).
2. **Fear is approved as the next strand.**
3. Strand files are filed in **`_analytics/cross-cluster-web/fear/`**.
