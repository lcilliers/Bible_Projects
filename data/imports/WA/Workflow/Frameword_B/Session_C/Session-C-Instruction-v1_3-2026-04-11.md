# Session C — Word Publication Layer
## Framework B Soul Word Analysis Programme
## Instruction v1.3 | 2026-04-11

---

## What This Session Is

Session C produces a single publication document for each word — a complete, reader-facing description of the word as a characteristic of the human inner life. It is written in plain, accessible language for an intelligent non-specialist reader. It draws directly from the word's data export (the complete JSON produced by Session A) and from the verse annotation and language annotation contributions provided by Session B.

Session C is the primary articulation layer of the programme. It does not summarise the technical analysis — it articulates what the word means, how it works, and where it connects, using the biblical evidence as its foundation. Session B subsequently deepens and corrects it. Session D findings will further inform it as cross-word patterns are established.

The document produced by Session C is a living document. It is updated to its annotated final form when Session B's verse and language annotations are incorporated. It is updated again when Session D establishes cross-word connections.

---

## Pipeline Position

```
Session A  →  data extraction (complete JSON)
Session C  →  primary word articulation (this session) — one document
Session B  →  analytical audit — verse annotations and language annotations 
               fed back into this document; database updated
Session D  →  cross-word synthesis — findings fed back into this document; 
               synergy publication layer produced separately
```

---

## What to Attach

**Session C v1 (initial document):**
- This instruction file
- The complete word data export from Session A: `wa-[nnn]-[word]-complete-[date].json`

**Session C v2 (Session B update — Stage 3 of Session B):**
- This instruction file
- The Session B v3 clean extract: `wa-[nnn]-[word]-complete-[date]-r3.json`
- The Session B observations log (highest-versioned file)
- The Session B analytical brief
- The existing word study: `wa-[nnn]-[word]-word-study-v1-[date].md`

**Session C v3 (Session D update):**
- This instruction file
- The Session D findings document for this word
- The existing word study: `wa-[nnn]-[word]-word-study-v2-[date].md`

Do not attach sub-process documents or extract files beyond what the current version requires.

---

## Output File

One Markdown file per word per version:

| Version | Filename pattern | Example |
|---|---|---|
| v1 — initial | `wa-[nnn]-[word]-word-study-v1-[date].md` | `wa-068-grace-word-study-v1-2026-04-09.md` |
| v2 — Session B update | `wa-[nnn]-[word]-word-study-v2-[date].md` | `wa-068-grace-word-study-v2-2026-04-10.md` |
| v3 — Session D update | `wa-[nnn]-[word]-word-study-v3-[date].md` | `wa-068-grace-word-study-v3-[date].md` |

All filenames lowercase. The previous version is retained on disk — do not overwrite.

**Note on existing files produced without version suffix:** Files produced before this convention was formalised (e.g. `wa-068-grace-word-study.md`) are treated as v1. They should be renamed to the v1 pattern when next handled in Session B Stage 3.

---

## Reading the JSON Before Writing

Session C reads the JSON in two passes. Do not collapse these into a single read — the two-pass structure keeps memory focused and prevents loading detail that is not yet needed.

---

### Pass 1 — Structural Read (before writing any section)

Read the following fields in order. After each field, note what it contributes to the overall orientation of the word. Do not read term lexical detail or verse text at this stage.

| Field | Purpose of this read |
|---|---|
| `registry.word`, `registry.no`, `registry.description` | Confirm the word and its programme definition — this is the conceptual anchor for the whole document |
| `registry.dimensions` | Note the dimension(s) assigned — primary and secondary where present |
| `registry.cluster_assignment` | Note the relational cluster — shapes the connections picture in Section 5 |
| `statistics` | Note term count, active term count, verse count, anchor count, testament distribution, sharing ratio — these numbers govern Sections 4 and 5 opening paragraphs |
| `verse_context.groups` — `context_description` fields only | Read every group description. These are the programme's own semantic map of the word's usage range. Read them all before writing Section 1 — they are the primary source for the characteristic summary. Do not read individual verse records at this stage. |
| `dimension_index` — `dimension` and `context_description` fields only | Note the dimension assigned to each group and confirm it matches the group description |
| `terms` — owner terms only, `gloss`, `god_as_subject`, `somatic_link`, `phase2_flags` fields only | Note each owner term's gloss, whether God is the primary actor, whether a somatic link is flagged, and what phase 2 flags are present. Do not read Mounce definitions, BDB senses, or related words lists at this stage. |

After Pass 1, write Sections 1 and 2 in full. The structural read provides everything needed for these sections.

---

### Pass 2 — Section-by-Section Detailed Read (when writing each section)

Read detailed data only when writing the section that requires it. Do not pre-load.

**Before writing Section 3:**
- Extract all anchor verses from `verse_context.groups` — all context records where `is_anchor = 1`
- For OWNER terms: read anchor verse text in full
- For XREF terms: read the context group description only — do not read XREF anchor verse text (see XREF Anchor Verse Rule below)
- Read anchor verse records one group at a time — do not load all verse records simultaneously

**Before writing Section 4:**
- For each owner term in turn, read: full Mounce definition, all BDB senses, LSJ entry where available, occurrence count, related words list, `has_causative_stem`, root family data
- Read one term at a time — complete the term description before reading the next term
- For the somatic scan: read full verse records for owner terms only, scanning for body-part language, physical posture, and physiological expression

**Before writing Section 5:**
- Read `correlations` block: `xref_sharing`, `verse_cooccurrence`, `dimension_overlap`, `root_families`, `shared_anchor_verses`
- Read `status_note` fields on all terms
- Read `session_research_flags` for any flags with session_target = C

---

### XREF Anchor Verse Rule

XREF terms are terms whose ownership belongs to a different registry. Their verse classification and anchor designation was performed by their owning registry. This registry uses XREF terms' context group descriptions to inform Sections 1 and 2 — the descriptions name the semantic territory the XREF terms cover. However:

- Do not write Section 3 annotations for XREF anchor verses — those verses are annotated in the owning registry's word study
- Do not load XREF verse text
- Where the context group description of an XREF term contributes to the characteristic picture, that contribution is incorporated into prose in Sections 1 and 2 — not cited as a verse annotation in Section 3
- At the end of Section 3, note how many anchor verse records belong to XREF terms and state that they are handled in their owning registries

---

## Document Structure

The document has six sections followed by an internal completion note. All sections appear in the single file in the order below.

---

## Document Lifecycle

The word study is a living document with three defined versions. Each version is a distinct file — the previous version is never overwritten.

### v1 — Initial Document (this session)

**Trigger:** Session A complete for this word. No Session B analysis available yet.

**What it produces:** A complete, reader-facing description of the word drawn from the JSON structural read and anchor verse pass. Section 3 annotations are the writer's own reading of what each verse contributes. Section 5 connections are drawn from the correlations block and context group descriptions — marked as formal, linguistic, theological, or inferential as appropriate.

**What it does not include:** Session B verse annotations, Session B language annotations, spirit-soul-body classification, correlation-confirmed connection characterisations. These gaps are recorded honestly in Section 6.

**Extract used:** Session A complete export — `wa-[nnn]-[word]-complete-[date].json`

**Output:** `wa-[nnn]-[word]-word-study-v1-[date].md`

---

### v2 — Session B Update (Session B Stage 3)

**Trigger:** Session B Stage 2 complete. R3 extract available. Session B analytical brief complete. This update is conducted as Stage 3 of Session B — governed by the Session B instruction, not independently.

**What changes:** Every section is validated against the complete, corrected data. Session B verse annotations replace or deepen Section 3 annotations. Session B language annotations correct or deepen Section 4 term descriptions. Section 5 is rewritten to reflect correlation-confirmed connections — every connection confirmed by a correlation signal is named with its signal type; every inferential connection is explicitly labelled. The spirit-soul-body provisional classification from Pass 4 is incorporated. All errors, gaps, and unsupported statements from v1 are corrected.

**What does not change:** The reader-facing register — v2 is still a plain-language document. Internal programme references are removed in Stage 3b.

**Extract used:** Session B R3 extract — `wa-[nnn]-[word]-complete-[date]-r3.json`

**Input documents:** R3 extract, Session B observations log (highest-versioned), Session B analytical brief, existing v1 word study.

**Output:** `wa-[nnn]-[word]-word-study-v2-[date].md`

---

### v3 — Session D Update

**Trigger:** Session D cross-word synthesis complete for this word's connections. Session D findings document available.

**What changes:** Section 5 is updated to reflect the formally established cross-word connections from Session D synthesis. Questions that Session D has answered are replaced with findings. Questions that Session D has deepened or reframed are updated. New connections established by Session D are added.

**What does not change:** Sections 1–4. Section 5 structure is retained; content is updated.

**Extract used:** Not required unless Session D identifies data corrections. Where corrections arise, the Session D process governs.

**Output:** `wa-[nnn]-[word]-word-study-v3-[date].md`

---

## Section 1 — Word Characteristic Summary

**Purpose:** Describe what this word means as a characteristic of a human being — what it looks like, how it feels, how it shows up in life.

**Length:** 230–270 words.

**Register:** Plain English. No Strong's numbers, no transliterations, no linguistic notation. Write as if explaining to a thoughtful reader with no biblical studies background.

**What to take into account:**
- Draw on the `registry.description` and the `context_description` fields of the verse context groups as conceptual anchors — but rewrite everything in your own words
- The owner term glosses and Mounce definitions reveal the range of English translations — use this range to show the breadth of the concept rather than flattening it to one word
- The `god_as_subject` flags indicate where God is the primary actor for this term — this shapes how the characteristic is described at its source level
- Where the `dimension_index` assigns both a primary and secondary dimension (e.g. Relational Disposition and Cognition), reflect both — the characteristic may operate on more than one level
- End with a statement about where this characteristic comes from in a human being — whether it is self-generated, received, developed through experience, or some combination

**Constraints:**
- Do not list — write in flowing prose
- Do not quote verse references in the body text (these come in Section 3)
- Let what the data says come through — do not impose a pre-existing theological framework

---

## Section 2 — Word Impact Description

**Purpose:** Describe the living dynamic of the word — what feeds it, what opposes it, what it produces, and where it ultimately comes from.

**Length:** 230–270 words.

**Register:** Same as Section 1 — plain, accessible prose.

**Required coverage — every impact description must address these six dynamics:**
1. The opposite of this characteristic — its natural enemy or negation
2. What feeds or strengthens it in a person
3. What diminishes or blocks it
4. What it produces in the person who has it
5. What it produces in others or in relationships
6. Where it ultimately comes from — self-generated or received

**What to take into account:**
- The verse context group descriptions often name causal relationships — what produces this word's state and what it produces in others. Read these carefully before writing
- The `phase2_flags` on individual terms carry signals about relational direction, semantic breadth, and eschatological usage — these shape the impact picture
- Where a term has a causative stem (noted in the parsed meaning senses), this indicates the word can be both experienced and caused in another — note this dynamic
- The cross-registry status notes in the MTI data (where terms carry `status_note` text) often name the adjacent characteristic that this word resolves into or depends upon — these are impact pointers
- The somatic evidence (body-part language in the verse records) often reveals how the characteristic is experienced physically — weeping, lifted hands, prostration, a heart response — and this belongs in the impact description as the embodied dimension of the characteristic

**Constraints:**
- The six coverage points should flow naturally through the prose — they are not subheadings
- The final statement about ultimate source should feel like a conclusion, not an appendix
- Do not use programme-internal vocabulary (registry, XREF, phase2 flag, etc.)

---

## Section 3 — Annotated Verse Evidence

**Purpose:** Ground the plain summaries in Sections 1 and 2 with the biblical text. Every significant claim should be traceable to a verse. The annotations explain what each verse adds — what it confirms, sharpens, complicates, or deepens.

**Method:**
- Extract all anchor verses from the `verse_context.groups` data (all context records with `is_anchor = 1`) for OWNER terms only
- Re-present Sections 1 and 2 in full
- After each significant statement or paragraph, insert the relevant anchor verse(s) as a block quotation followed by an annotation

**XREF anchor verses:** Anchor verses belonging to XREF terms are not annotated in this document. They are handled in their owning registry's word study. Where an XREF term's context group description has contributed to the characteristic picture in Sections 1 and 2, that contribution is already present in the prose — no verse annotation is added here. At the end of this section, record how many anchor verse records belong to XREF terms and state that they are handled in their owning registries.

**Initial pass (before Session B):** Use the owner term anchor verses as extracted from the data. Write annotations based on your own reading of what each verse contributes.

**After Session B (v2 update):** Replace or supplement initial annotations with Session B's structured verse annotations, which will be more precise. Add any supplementary verses Session B has flagged as representing missing registers or senses.

**Format of each verse block:**
```
> **[Reference]** — *[Verse text, ESV]*
>
> [Annotation — 3–6 sentences. Name what this verse does that the plain 
> statement could not fully carry. Draw on the verse's specific language 
> or context. Note anything surprising, complex, or significant that a 
> plain reading might pass over. Written in accessible language — no 
> Strong's numbers or transliterations.]
```

**What to take into account:**
- Somatic verses (those containing body-part language or physical posture) deserve particular attention in annotation — the body's involvement often reveals the depth or urgency of the inner state
- Verses where God is the subject of the term's action are theologically significant — the annotation should name what this reveals about the divine-human dimension of the characteristic
- Verses that represent the eschatological dimension (flagged by `ESCHATOLOGICAL_USAGE` phase2 flag) should be annotated to show what the future-oriented expression of the characteristic reveals about its present form
- Not every anchor verse needs to annotate the same passage — distribute annotations across both Section 1 and Section 2 material
- Where an anchor verse creates tension with something said in Sections 1 or 2, do not suppress the tension — name it in the annotation. Complexity is not a problem; unacknowledged complexity is

**Constraints:**
- Every owner term anchor verse must appear somewhere in this section
- XREF anchor verses are not annotated here — they are handled in their owning registry
- Annotations may introduce new insight the plain summaries did not carry, as long as it comes genuinely from the verse
- End this section with a closing line in this format: *"Section 3 draws on [n] anchor verses from owner terms, [translation]. Anchor verses for XREF terms ([list term identifiers]) are handled in their respective owning registries."*

---

## Section 4 — Original Language Vocabulary

**Purpose:** Describe the original language vocabulary the research identified — what the key words are, what they mean, how they relate to each other, and what the full family of associated words reveals about the concept.

**Structure:**

**Opening paragraph:** Name the language families and root relationships. State how many terms were identified, how many are core to this word, and how many are shared with adjacent word studies. Note what the sharing ratio signals about the word's connectivity.

**For each core term:** (in order — Greek terms first if present, then Hebrew)
- Name the word in plain English with its transliteration and Strong's number in parentheses
- State its occurrence count and testament range
- Describe the range of English translations it receives — this reveals its semantic breadth
- Describe its core meaning and sub-senses drawn from the lexical data (Mounce, BDB), in plain language
- For Greek terms, note any significant classical (pre-biblical) usage where it illuminates the NT meaning
- Name what this specific term contributes that the others do not

**What to take into account:**
- The `somatic_link` field on each term indicates whether it has a documented bodily dimension — where set, this should be reflected in the term's description
- Where a term's meaning block carries `has_causative_stem = 1`, note that the word has both a passive and an active form — it can name both the experience and the causing of the state
- The related words list for each term is extensive. Filter out proper names (personal and place names) and focus on the meaningful semantic vocabulary. Organise the associated glosses thematically rather than by Strong's number
- The negative semantic twin of a term (a word from the same root that means the opposite) is worth naming — it defines the word by contrast
- After Session B, incorporate Session B's language annotations where they correct, add to, or deepen any term description

**Synthesis observation:** After covering the individual terms, close with a paragraph that describes what the complete vocabulary reveals as a whole — the semantic arch from source to expression, or the conceptual territory the full word family covers together.

**Length:** 700–1100 words depending on the richness of the term inventory.

**Register:** This section carries more technical weight than Sections 1–3. Transliterations and Strong's numbers in parentheses are appropriate. However, technical notation should serve clarity — a non-specialist should be able to read this section and learn something.

---

## Section 5 — Connections and Research Pointers

**Purpose:** Map all the outbound connections from this word — every other characteristic, concept, or word study that the research signals as related, overlapping, or dependent. This is the interface between the individual word study and the cross-word synthesis work of Session D.

**Opening:** State the word's connectivity — its sharing ratio, and what that ratio indicates about whether this is a self-contained characteristic or a highly relational one.

**For each outbound connection:**
- Name the connected characteristic in plain English
- State the nature of the connection precisely:
  - *Formal* — documented in the research data (shared term, explicit cross-reference in the programme notes)
  - *Linguistic* — shared vocabulary or root family
  - *Theological* — concepts that travel together in Scripture without necessarily sharing vocabulary
  - *Inferential* — a connection the research suggests but does not formally establish
- Name the key question this connection raises for further research — phrased as a question the reader can hold
- State the priority: High / Medium / Lower

**What to take into account:**
- The `status_note` fields on MTI terms often name adjacent characteristics explicitly — these are formal connections
- Terms whose owning registry is a different word study are shared vocabulary — name the word study and the nature of the overlap
- The verse context group descriptions often name what this word is a response to, or what it produces — these are causal pointers to adjacent characteristics
- The eschatological anchor verses point toward hope, repentance, and restoration — these are theological connections
- The somatic evidence may point toward body-oriented word studies (weeping, strength, flesh) that would benefit from cross-referencing
- After Session D, this section will be updated with the formally established cross-word connections

**Closing summary table:**

| Connected Characteristic | Nature | Priority |
|---|---|---|
| [name] | [formal / linguistic / theological / inferential] | [High / Medium / Lower] |

**Constraint:** Every connection listed must be traceable to something in the data. If a connection is inferential, say so. Do not speculate beyond what the evidence supports.

---

## Section 6 — Internal Completion Note

**Purpose:** A brief internal record within the document itself — not reader-facing, but preserved as part of the study record.

**Format:**
```
---
## Internal — Session C Completion Note

Word: [word]  
Registry: [number]  
Session C date: [date]  
Specification: Session C Instruction v[governing version]

### What was available from the data
[Brief note on what the JSON provided — was the data rich or thin, 
were anchor verses plentiful or sparse, were the context group 
descriptions detailed or minimal. Note how many anchor verse records 
belonged to XREF terms and were therefore not annotated here.]

### What Session C could not address
[Specifically: somatic evidence not yet fully surfaced, spirit-soul-body 
classification not yet assigned, any terms where lexical data was thin, 
any owner term anchor verses that were not used and why, any XREF group 
descriptions used for prose but whose verse annotations are in other registries]

### Questions for Session B
[Specific questions that arose during writing that Session B should 
investigate — statements the writer is uncertain about, tensions that 
need resolution, verses that seemed important but were hard to interpret]

### Version log
- v1: [date] — initial document, Session C Instruction v[n]
- v2: [date] — updated with Session B annotations, Session B Instruction v[n] — [brief note on what changed]
- v3: [date] — updated with Session D findings — [brief note on what changed]
---
```

---

## Quality Principles

**Accuracy over accessibility.** If the data does not support a statement, do not make it in order to produce a cleaner narrative. A gap honestly acknowledged is better than a gap filled with inference.

**Emergence over imposition.** The character of each word should emerge from what the data says. Do not read a pre-existing theological framework onto the material. Conclusions must be derivable from the evidence independently.

**Plain language is not shallow language.** Depth of insight and accessibility of language are not opposites. The reader should finish each section knowing more than when they started.

**The verse annotations are not decoration.** Every annotation in Section 3 should say something that the plain summary could not say without it. If it merely repeats what was already said, it does not belong.

**The terms review is not a glossary.** Section 4 should tell a story about the word through its vocabulary — not simply list definitions.

**The research pointers are not speculation.** Section 5 is only as valuable as it is honest about what is established versus what is inferred.

**Somatic evidence belongs throughout.** Where the body is involved in the expression or experience of a characteristic — through body-part language, physical posture, or physiological response in the verse texts — this should appear naturally in Sections 1, 2, and 3, not only in Section 4. The body is part of the story, not a technical footnote.

---

## Change Log

v1.3 (2026-04-11): Five additions. (1) **XREF anchor verse ownership rule** formalised — XREF anchor verses are handled in their owning registry only; this registry uses XREF context group descriptions to inform Sections 1 and 2 but does not write XREF anchor verse annotations in Section 3. This rule was applied in practice during the grace word study (2026-04-09) but was not previously saved as an instruction update. (2) **Two-pass JSON reading procedure** replacing the flat reading list — a structural read covers orientation fields first; a section-by-section detailed read covers term and verse data only when writing the relevant section. This prevents memory overload on large registries. (3) **Output filename convention updated** — all Session C documents carry version number and date from v1: `wa-[nnn]-[word]-word-study-v1-[date].md`. No version-less filenames. Aligned with Session B v4.7 naming conventions. (4) **Document lifecycle section added** — formally defines the v1 (initial), v2 (Session B update), and v3 (Session D update) versions: what triggers each, what to attach, which JSON extract to use, and what the output is. (5) **Completion note template updated** — version string made dynamic (`Session C Instruction v[governing version]`); v2 and v3 update entries added to the version log within the note.

v1.2 (2026-04-09): Restructured from six separate documents to a single document per word. Somatic evidence, spirit-soul-body awareness, god-as-subject signals, causative stem indicators, phase2 flag awareness, and eschatological dimension incorporated as explicit guidance within each section. Session B annotation inputs defined formally. Internal completion note added as Section 6 within the document.

v1.1 (2026-04-09): Initial specification as six separate documents — superseded by v1.2.
