# Candidate next strand — Fear (from the M01 extract)

**Date:** 2026-10-01 · **Status:** **approved** 2026-10-01 (#1927) · **Source:** iba.db (read-only), the researcher's M01 extract query

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

### 3.1 One word, two faces: STEP itself splits H3372

The pattern below was counted only. The verses are not read yet.

| Strong | Verses | LORD/God within 5 words | Negated ("not" within 2 words before) |
| --- | --- | --- | --- |
| H3372G to fear | 200 | 62 | **67** |
| H3372H to fear: revere | 107 | **75** | 8 |
| H3374 fear (noun) | 45 | 30 | 2 |
| G5399 to fear | 91 | 22 | 26 |
| H6343 dread | 48 | 18 | 1 |

- **"Do not fear":** a negator falls within 2 words before a fear word in **128 verses**.
- In this data, the "revere" face of H3372 sits next to God much more often than it is negated. The "fear" face is negated much more often.
- This bears directly on the change-of-character discovery (#1919). It is a reason to read these verses, not a finding.

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

1. The H3372 pair: afraid vs revere, with the 128 "do not fear" verses as a group.
2. Fear in the heart and body: M47 seats; trembling and shuddering words; the hand and face only where they are not prepositional.
3. Fear's near neighbours, as the verses lead: dismay, strength, trust, rest, hiding.
4. Fear before God's acts and judgments (the M55 / M02 verses), in step with Ch 13.

**Chapters likely touched (to be confirmed by the reading, not assumed):** 10.1, 10.9, 10.10, 11 §4, 12, 13, 14.

**Alternative, if fear is held back:** M24 Faintness & Despair. It has the most near co-occurrences with fear of any M-cluster (56 verses), but it is smaller and would mostly arrive through fear anyway.

## 6. Decisions (researcher, 2026-10-01, #1927)

Researcher, verbatim: *"1 - accept your correct as <> 2- yes 3 - _analytics/cross-cluster-web/fear/"*

1. The extract filter is **`<> 'M01'`** (fear with the rest of the web).
2. **Fear is approved as the next strand.**
3. Strand files are filed in **`_analytics/cross-cluster-web/fear/`**.
