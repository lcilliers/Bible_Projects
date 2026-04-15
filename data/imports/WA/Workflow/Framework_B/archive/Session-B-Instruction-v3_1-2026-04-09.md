# Session B — Analytical Composition and Database Update
## Framework B Soul Word Analysis Programme
## Instruction v3 | 2026-04-09

---

## What This Session Is

Session B is the full analytical composition session for each word. It performs a rigorous, multi-pass analysis of the word's complete data set, updates the programme database with analytical findings, and produces the technical layer that supports Session C's reader-facing documents and provides the input material for Session D's cross-word synthesis.

Session B reads the Session A data export and the Session C documents together. Its work has two equal outputs:

**Output 1 — Database updates.** Session B writes analytical findings back into the word's JSON: phase2 flag completions, somatic classifications, spirit-soul-body provisional assignments, and verse annotation tags. These updates make the database richer for every subsequent session.

**Output 2 — Session C enrichment.** Session B produces verse annotations and language annotations that are incorporated into the Session C documents, strengthening their accuracy and credibility. Session C documents are updated to their annotated final form using Session B's contributions.

Session B does not produce a separate publication. Its analytical findings live in the database and in the annotated versions of the Session C documents.

---

## Pipeline Position

```
Session A  (data extraction → complete JSON)
    ↓
Session C  (primary word articulation → five reader-facing documents 
            + Session C completion note)
    ↓
Session B  (analytical composition — this session)
    ├── updates JSON (database layer)
    ├── produces verse annotations → feeds back to Session C Document 3
    ├── produces language annotations → feeds back to Session C Document 4
    └── produces Session B handoff note → input for Session D
    ↓
Session D  (cross-word synthesis → feeds back to Session C and produces 
            synergy publication layer)
```

---

## What to Attach

- This instruction file
- The complete word data export: `wa-[registry]-[word]-complete-[date].json`
- The Session C combined document for this word: `wa-[registry]-[word]-word-study.md`

**Note:** The five Session C reader-facing sections (Sections 1–5) and the Session C completion note are produced as a single combined file. All references in this instruction to "Documents 1–5" and "Session C completion note" refer to the corresponding sections within that single file.

---

## What This Session Produces

| Output | Type | Description |
|---|---|---|
| Updated JSON | Database | Phase2 flags, somatic classifications, spirit-soul-body assignments, verse annotation tags written back |
| Verse annotation set | Session C input | Structured annotations for Document 3 — one per anchor verse, with additional verse flags |
| Language annotation set | Session C input | Structured annotations for Document 4 — correcting, deepening, or expanding the terms review |
| Session B analytical brief | Internal | Structured summary of all findings for Session D input |
| Session C Document 3 (v2) | Publication | Updated annotated summaries incorporating Session B verse annotations |
| Session C Document 4 (v2) | Publication | Updated terms review incorporating Session B language annotations |

---

## Pre-Analysis Validation

Before beginning analytical work, read the Session C completion note. Note:
- Which statements the Session C writer flagged as uncertain
- Which anchor verses were not used and why
- Which gaps the writer identified (somatic, spirit-soul-body, thin lexical data)
- The specific questions raised for Session B investigation

These become the priority items for each pass.

Then read the complete JSON — all sections. Do not begin Pass 1 until the full data set has been read. For large registries (over 300 active verses), read in the following order: registry block → statistics → term inventory → dimension index → verse context groups → verse records by term.

---

## Analysis Pipeline — Five Passes

### Pass 1 — Meaning and Semantic Range

**Purpose:** Establish a complete and accurate picture of what each core term means, how its meaning varies across its usage range, and where the boundaries of the word's semantic territory lie.

**Method:**
- For each owner term, read the full Mounce definition, all BDB senses, and the LSJ entry where available
- Read the context group descriptions for that term — these represent the programme's own semantic clustering of the verse evidence
- Identify the primary sense, any secondary senses, and any edge or boundary senses
- Note where the translation range (the variety of English words used to render the term) reveals semantic breadth that a single gloss obscures
- Note where different senses in the same term create internal tensions — places where the word can mean almost opposite things depending on context

**Database write-back:** For each term, confirm or update the `meaning_numbered` field if the sense structure can now be specified more precisely than the prose-only meaning block.

**Session C check:** Compare findings against Document 1 (Characteristic Summary) and Document 2 (Impact Description). Identify any statements that the meaning analysis confirms, complicates, or contradicts. Flag these for the verse annotation pass.

---

### Pass 2 — Divine Dimension and God-as-Subject Analysis

**Purpose:** Establish the pattern of divine involvement with this word — where God is the subject of the action, where the word describes a characteristic of God, and how the divine dimension shapes the human dimension.

**Method:**
- Read all verses where God is the named or implied subject of the term's action
- Identify the dominant pattern — does God primarily give this characteristic, model it, command it, withhold it, restore it, or pour it out?
- Note the relationship between the divine dimension and the human dimension — is the human characteristic derivative (received from God), responsive (answering to God's action), or parallel (operating by the same principle as God operates)?
- Note any eschatological dimension — is the full expression of this characteristic presented as a future gift rather than a present reality?

**Database write-back:** Update `god_as_subject` field for any term where this was not correctly set during extraction. Add FRAMEWORK_SIGNAL phase2 flag where the divine-human relationship has direct implications for the spirit-soul-body classification.

**Session C check:** Verify the statement in Documents 1 and 2 about the ultimate source of the characteristic. Confirm or correct it based on the verse evidence.

---

### Pass 3 — Verse Annotation

**Purpose:** Produce a complete, structured annotation for every anchor verse in the registry, ready for incorporation into Session C Document 3. This is the primary contribution of Session B to the published documents.

**Method:**
- Extract every anchor verse (all context records with `is_anchor = 1`) and their context group descriptions
- For each anchor verse, write an annotation of 3–6 sentences that:
  - Names what this verse does that the plain summary statement could not fully carry
  - Draws on the verse's specific language, grammar, or context to make a precise observation
  - Connects the verse to the word's broader semantic picture established in Pass 1
  - Notes anything surprising, complex, or theologically significant that a plain reading might pass over
  - Is written in accessible language — no technical notation, no Strong's numbers

**Additionally:** Read the full verse record set for each owner term. Flag any non-anchor verse that:
  - Contains a usage of the term that is not represented by any anchor verse (a missing register or sense)
  - Directly contradicts or complicates a statement made in Session C Documents 1 or 2
  - Contains significant somatic (body) language relevant to Pass 4

These flagged verses are candidates for addition to Document 3 as supplementary annotations.

**Output format for each verse annotation:**
```
REFERENCE: [book chapter:verse]
STRONG'S: [term identifier]
CONTEXT GROUP: [group code]
ANCHOR: yes / supplementary
ANNOTATION: [3–6 sentences]
SESSION C FLAG: [confirm / correct / deepen / add] — [brief note on which 
                statement in Documents 1-2 this annotation addresses]
```

**Database write-back:** Tag each anchor verse record with its annotation status. Add VERSE_ANNOTATION_COMPLETE flag to the registry record when all anchors are annotated.

---

### Pass 4 — Somatic Evidence and Spirit-Soul-Body Classification

**Purpose:** Establish the bodily dimension of the word — how it is expressed in or through the body, where it originates in the spirit-soul-body trichotomy, and what its relationship to the physical body is.

**Method:**

**4a — Somatic scan.** Read all verse records for owner terms. For each verse containing a body-part reference, physical posture, physiological reaction, or somatic expression, record:
- The verse reference
- The body part or somatic expression named
- The classification: origin (the body is where this word begins), expression (the body manifests it), instrument (the body performs it), or absence (the body is notably not involved — a purely interior state)

Body-part vocabulary to scan for includes but is not limited to: heart, soul, spirit, eye, face, mouth, lip, hand, knee, foot, breath, bowels, bones, flesh, skin, tears, weeping, posture terms (bowing, falling, prostrating).

**4b — Somatic pattern summary.** Having completed the scan, describe the somatic signature of this word:
- Which body parts are most associated with it?
- Is its somatic expression concentrated (one dominant organ or posture) or diffuse?
- Is the body the origin of the word's movement, or the expression of it?
- Does the somatic evidence suggest this word lives primarily at the spirit level, soul level, or body level — or at the intersection of levels?

**4c — Spirit-soul-body provisional classification.** Assign a provisional classification:
- **Spirit-primary:** The word names a state or movement that originates in the spirit — it is received from God rather than generated from within; it operates above the level of natural human capacity
- **Soul-primary:** The word names a characteristic of the inner life — emotion, disposition, relational orientation, desire, will — that is distinctively human and operates within the range of natural human experience
- **Body-primary:** The word names something that is primarily expressed through or triggered by the physical body
- **Spirit-soul interface:** The word moves between spirit and soul dimensions — received at the spirit level, expressed at the soul level
- **Soul-body interface:** The word moves between soul and body — felt inwardly, expressed outwardly through the body
- **Trichotomy-spanning:** The word operates across all three dimensions simultaneously

Provide brief reasoning for the classification drawn from the somatic evidence and the meaning analysis.

**Database write-back:** Update `somatic_link` field for any term where somatic evidence was found. Add SOMATIC_FLAG_RECOMMENDED, SPIRIT_SOUL_BOUNDARY, or BODY_SOUL_BOUNDARY phase2 flags as warranted. Write provisional spirit-soul-body classification to the registry's `sb_classification` field with reasoning in `sb_classification_reasoning`.

**Session C check:** Review Document 1 (Characteristic Summary) for any statements about origin or manner of the characteristic that the somatic evidence confirms, deepens, or needs to correct.

---

### Pass 5 — Language Annotation and Terms Review Audit

**Purpose:** Audit Document 4 (Critical Terms Review) for accuracy, completeness, and depth, and produce language annotations that strengthen it.

**Method:**

**5a — Accuracy audit.** Read Document 4 against the full lexical data in the JSON (Mounce definitions, BDB senses, LSJ entries, related words lists). Check:
- Are the stated senses accurate and complete?
- Are the occurrence counts correct?
- Are the related words correctly described?
- Are the root relationships correctly stated?
- Are any classical (pre-biblical) usages that would inform the terms review missing?
- Does the semantic arch or synthesis observation at the end hold up?

**5b — Completeness audit.** Check:
- Are all owner terms covered?
- Are the most significant associated words (non-proper-name glosses) described adequately?
- Are there entries in the related words lists that warrant more attention than Document 4 gave them?
- Are there semantic observations embedded in the LSJ entries that were not surfaced?

**5c — Language annotations.** For each significant correction, addition, or deepening, produce a structured language annotation:

```
TERM: [Strong's number and transliteration]
TYPE: correction / addition / deepening
ANNOTATION: [the specific observation, stated precisely]
SESSION C FLAG: [which statement or section of Document 4 this addresses]
```

**Database write-back:** No new database fields are updated in this pass. However, if the audit reveals a Strong's number error or an incorrect gloss in the MTI, flag it for researcher correction separately.

---

## Session B Analytical Brief (Handoff to Session D)

After completing all five passes, produce a structured analytical brief. This is an internal document, not reader-facing.

**Sections:**

**1. Registry summary** — word, registry number, term count, verse count, session B date

**2. Meaning findings** — the primary semantic picture that emerged, any significant tensions or surprises in the meaning analysis, any senses that were underrepresented or missing from Session C

**3. Divine dimension summary** — the dominant pattern of divine involvement, the divine-human relationship for this word, any eschatological dimension

**4. Somatic signature** — the body-part vocabulary associated with this word, the somatic classification summary, the provisional spirit-soul-body assignment with confidence level (high / medium / low)

**5. Spirit-soul-body provisional classification** — stated in one sentence with brief reasoning

**6. Session C corrections and additions** — list every place where Session B found a statement in Documents 1–5 that needs correction, addition, or deepening, with specific reference to which document and which statement

**7. Cross-word signals for Session D** — the strongest outbound connections identified during all five passes, including any signals not already in Document 5 (Research Pointers), with the specific verse or term evidence that generates each signal

**8. Open questions** — anything that the five passes raised but could not resolve from this registry's data alone — questions that require either cross-word analysis (Session D) or researcher review

---

## Analytical Principles

**The data is authoritative.** Every finding must be traceable to a specific verse record, term entry, or lexical source in the JSON. Do not import general theological knowledge to fill gaps in the data.

**Emergence, not imposition.** The spirit-soul-body classification, the somatic signature, and the semantic picture must emerge from the evidence. Do not assign a classification and then select evidence to support it.

**Session C documents are not sacred.** Session B exists to correct, deepen, and complete them. An accurate document that has been corrected is more valuable than an accessible document that contains errors. Make corrections clearly and specifically.

**Phase2 flags are recommendations, not conclusions.** They inform Session D but do not constitute final component assignments. Flag what the data warrants. Do not over-flag.

**Somatic evidence is observational, not interpretive.** Record what the verses say about bodily involvement before interpreting what it means. The scan comes before the pattern summary.

---

## Change Log

v3.1 (2026-04-09): "What to Attach" section updated — the five Session C reader-facing documents and the Session C completion note are produced and attached as a single combined file (`wa-[registry]-[word]-word-study.md`). All internal references to "Documents 1–5" and "Session C completion note" continue to refer to the corresponding sections within that file.

v3 (2026-04-09): Full redefinition of Session B's role and structure. Session B is now the analytical composition session that operates against Session C documents, updates the database, and produces the technical layer for Session D. Pass 3 (Verse Annotation) and Pass 5 (Language Annotation) are new passes providing direct feed-back into Session C Documents 3 and 4. Spirit-soul-body provisional classification formalised in Pass 4. Session B Analytical Brief replaces the previous prose analysis MD as the Session D handoff document. Somatic evidence protocol retained and expanded from v2.

v2 (2026-03-15): Added Pass 3 (Somatic Evidence) as a mandatory fifth analysis pass. Added Section 5 (Body-Soul Connection) as mandatory output section. Added somatic classification framework. Added SOMATIC_FLAG_RECOMMENDED, SPIRIT_SOUL_BOUNDARY, BODY_SOUL_BOUNDARY, and FRAMEWORK_SIGNAL phase2 flags.

v1 (prior): Original four-pass structure — meaning, divine dimension, verse patterns, cross-registry. No somatic protocol.
