# Session C — Context MD Production
## Framework B Soul Word Analysis | Phase 1 | v3 Specification

---

## What this session produces

**One file only:** `WA-[registry-no]-[word]-context-[yyyy-mm-dd].md`

This is the narrative context file. It holds a structured record of the situational and narrative context of every CORE and EXTENDED verse in the word's verse set. It is a dataset, not an interpretation. It preserves the who, what, and what-happens in each verse's story — data that the JSON and Analysis MD cannot hold.

---

## Input files required for this session

Attach all three of the following before starting:

1. **The word source file** — the STEP markdown file for the word (e.g. `word_grief.md`)
2. **The completed JSON file from Session A** — `WA-[registry-no]-[word]-data-[yyyy-mm-dd].json`
3. **The v3 specification document** — `WA-Phase1-Specification-v3-2026-03-07.docx`

The JSON file defines which verses are CORE, EXTENDED, AMBIGUOUS, or PERIPHERAL. Context records are required for CORE and EXTENDED only. The source file provides the verse texts and surrounding context. Do not begin until both have been read in full.

---

## Process sequence — follow this order exactly

**Step 1 — Read the JSON verse_classifications array in full.** Extract every verse classified as CORE or EXTENDED. This is the complete list of verses requiring a context record. Note the term and bundling details for each.

**Step 2 — Read the source file in full.** For each CORE and EXTENDED verse, locate the verse text in the source file and note the surrounding passage context available there.

**Step 3 — Apply the bundling rule.** Where two or more CORE or EXTENDED verses under the same term show the same person in the same situation experiencing the same inner state, they may be combined into a single record. All references must be listed. Do not bundle verses from different books, different persons, or different situations — even if the inner-being function appears similar.

**Step 4 — Write one context record per CORE or EXTENDED verse or bundle.** Follow the record structure below exactly. Write records in term order (follow the order of terms in the JSON term_inventory).

**Step 5 — Write the Situation and Genre Summary** (after all records).

**Step 6 — Write the Peripheral Verse Flags section** (after the summary).

---

## Context MD file structure

### Filename
`WA-[registry-no]-[word]-context-[yyyy-mm-dd].md`

### Section 1 — Header
Word, registry ID, source list, date, version number. One sentence stating: (a) the total number of CORE and EXTENDED verse entries documented in this file, and (b) the literary genres represented across those entries.

### Section 2 — Verse Context Records

One structured record per CORE or EXTENDED verse or bundle. Write records in term order.

**Record format — use these field labels exactly:**

```
---
Reference:       [book chapter:verse — or list of references if bundled]
Term:            [transliteration and Strong's number]
Classification:  [CORE or EXTENDED — carried over from JSON exactly]
Genre:           [narrative / lament / prophecy / wisdom / epistle / apocalyptic / law / hymn]
Speaker/Subject: [who is speaking or acting; name the person if named in the text]
Situation:       [2–4 sentences describing what is happening in the surrounding passage when this verse occurs]
Inner-being moment: [one sentence stating precisely what the verse records about the inner state of the person; quote the key phrase using the English translation in the source file]
Response:        [one sentence stating what action, speech, prayer, or response follows from or accompanies the inner state; if none recorded, state: not recorded in the surrounding passage]
Bundling note:   [if bundled: one sentence stating why these verses were bundled; if single verse: single verse]
---
```

**Field rules:**

*Reference:* Use the same reference format as the source file (e.g. Psa 31:7, not Psalm 31:7).

*Genre:* Assign one genre label. Where a passage is formally a prayer within a narrative, assign the dominant form of the passage (usually lament or hymn). Prophecy covers both prophetic address and lament poetry in prophetic books (e.g. Jeremiah's confessions are lament; Jeremiah's oracles are prophecy — assign the dominant form for the specific passage). Wisdom covers Proverbs, Ecclesiastes, Job's wisdom speeches. Epistles cover NT letters. Apocalyptic covers Daniel and Revelation.

*Situation:* Describe what is happening at the point this verse occurs, using the surrounding verse texts available in the source file. Do not use the words "therefore," "this shows," or "this demonstrates." Permitted verbs: the text states / the narrative records / the person does / the speaker says / the verse records. If surrounding context is not available in the source file, state: surrounding context not available in source file.

*Inner-being moment:* One sentence. Quote the key phrase from the English translation in the source file. The phrase must be the specific expression of the inner state — not the outer event. Do not interpret what the inner state means.

*Response:* One sentence. Record what the person does with the inner state — prays, acts, speaks, continues suffering, is comforted, etc. If the surrounding passage does not record a response, state: not recorded in the surrounding passage.

*Bundling note:* If verses are bundled, state the specific reason — same person, same situation, same inner state. If a single verse, write: single verse.

### Section 3 — Situation and Genre Summary

After all verse context records. Maximum three paragraphs. Observe the following without drawing conclusions:
- Which literary genres the CORE verses are distributed across, and whether the inner-being usage of this word is concentrated in particular genres or spread broadly
- The range of human situations in which this inner state appears in the CORE verses — stated descriptively, not categorically
- Whether the word appears predominantly in the voice of the sufferer (first-person), in the voice of an observer naming another person's state (third-person), or in narrative description

### Section 4 — Peripheral Verse Flags

A brief note on PERIPHERAL verses that were excluded from the context records. For each PERIPHERAL verse that has situational features potentially relevant to Phase 2 beyond what the classification captures, state this in one sentence and flag it for Phase 2 attention. If no PERIPHERAL verses warrant flagging, state: No PERIPHERAL verses warrant Phase 2 flagging for this word.

---

## Scope boundary — what the Context MD must never contain

- The word "therefore"
- The phrases "this shows" or "this demonstrates"
- Framework B vocabulary (three-state typology, soul function labels, transformation stages)
- Conclusions about inner-being function or soul anatomy
- Cross-word synthesis
- Neuroscience, psychology, or behavioural science
- Speculation about what the inner state means or what it produces in the person
- Hebrew or Greek script characters — transliteration only
- Any verse record for an AMBIGUOUS or PERIPHERAL verse (those are excluded)

---

## Handling EXTENDED verses

EXTENDED verses show the inner-being state in a secondary or indirect register — cosmic mourning, national grief, land mourning, personified creation. Write the context record for these in full, but:
- In the *Inner-being moment* field, note that the inner state is expressed through a secondary register (e.g. the land, a personified nation, a cosmic event) and state what the indirect connection to the human inner state is
- Do not treat the EXTENDED classification as a reason to shorten or thin the record — EXTENDED verses still require full records

---

## Cross-reference requirement

Every CORE and EXTENDED verse reference in the JSON verse_classifications must appear in exactly one record in this file — either as the primary reference or within a bundle. Before finalising, cross-check the complete list of CORE and EXTENDED verses from the JSON against the records written. No verse may be omitted.

---

## Pre-submission checks for Session C

Before finalising:

- [ ] Every CORE and EXTENDED verse from the JSON appears in exactly one record
- [ ] Every record has all required fields populated
- [ ] No AMBIGUOUS or PERIPHERAL verses have records
- [ ] "Therefore," "this shows," and "this demonstrates" do not appear anywhere
- [ ] No Framework B vocabulary appears anywhere
- [ ] All bundled records state the bundling reason explicitly
- [ ] Surrounding context that is absent from the source file is stated as such — not fabricated
- [ ] The Situation and Genre Summary is written and does not draw conclusions
- [ ] The Peripheral Verse Flags section is written (even if it states no flags warranted)
- [ ] Transliteration only — no script characters
- [ ] Total CORE and EXTENDED entry count in the header matches the actual number of records

---

## Output

Produce the completed Context MD file. This file, together with the JSON from Session A and the Analysis MD from Session B, constitutes the complete Phase 1 record for this word.
