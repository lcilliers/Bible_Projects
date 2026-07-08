# Session C Cluster — Appendices Instruction (A, B, C)

**Document type:** Combined instruction covering all three appendices of a cluster's published study.
**Audience:** Claude AI (the writer)
**Version:** v1.0
**Date:** 2026-05-12
**Loads alongside:** `wa-sessionc-cluster-style-method-v1_1-20260512.md` (shared)
**Reads (three separate input files):**

- `wa-cluster-{CLUSTER}-appa-input-v1-{YYYYMMDD}.md` (Terms)
- `wa-cluster-{CLUSTER}-appb-input-v1-{YYYYMMDD}.md` (Key verses)
- `wa-cluster-{CLUSTER}-appc-input-v1-{YYYYMMDD}.md` (Method note)

**Writes (three separate draft files):**

- `wa-cluster-{CLUSTER}-appa-draft-v1-{YYYYMMDD}.md`
- `wa-cluster-{CLUSTER}-appb-draft-v1-{YYYYMMDD}.md`
- `wa-cluster-{CLUSTER}-appc-draft-v1-{YYYYMMDD}.md`

---

## 1. What this instruction covers

The three appendices of the published study close the book with reference material the reader can return to:

- **Appendix A — Terms.** A two-layer term inventory: the **key terms** for each characteristic (those placed under the characteristic in the analytical record) and the **supportive terms** across the study (those that appear in the verse evidence but do not themselves carry a core characteristic).
- **Appendix B — Key verses.** A single table covering every key verse cited in the chapters above, with a "meaning of the term in this study" column that gives the per-verse contextual reading.
- **Appendix C — Method note.** A short paragraph in plain English acknowledging the analytical method and the evidential basis of the study.

The appendices are written **as a single AI run** — you read all three inputs together, write into the AI-WRITE zones in each, and return three draft files. The volume of AI work across all three is small (~1000–1500 words total) — about the size of a single chapter section.

---

## 2. Voice and citation expectations

The appendices match the chapters in voice and audience (per shared style §1–§4) but with two adjustments:

- **Citation density is lighter.** Appendix A and Appendix C make no per-claim verse citations — they are reference / methodology material. Appendix B *is* a verse table, so every row carries a verse; the AI-fill cells are short per-verse contextual readings, not claims requiring secondary anchoring.
- **Length is constrained.** Each appendix is short by design. Do not pad. A 60-word commentary that says it well is better than a 120-word commentary that pads to fill the range.

The shared style document's avoid-list (§3) still applies. The thematic lens names (§5) and the silence principle (§6) also apply where relevant.

---

## 3. Appendix A — what to write

### A.opening (~30 words, one sentence)

A single framing sentence at the top of Appendix A, naming the appendix as the term inventory underlying the study. Plain English. Do not list the characteristics by code or number.

### A.{n} commentary, one per non-BOUNDARY characteristic (~60–120 words each)

After each characteristic's key-terms table (provided in the input), write a short commentary paragraph that characterises what these terms *together* reveal about the characteristic. Focus on:

- **The substantive sense the terms collectively carry** — what kind of inner-life material these terms name as a group. (E.g. for M15-A: "These ten terms together name wisdom as both attribute and quality — the noun forms hold wisdom as something possessed, the adjectival forms hold it as a constituted character of the person, and the verbal forms name its exercise.")
- **Notable Hebrew / Greek distributions.** Where the split between Hebrew and Greek terms is itself a finding — for example, where a characteristic is carried almost entirely by Hebrew vocabulary (suggesting OT prominence), or where the Greek vocabulary brings in distinctions the Hebrew lacks, or where a Greek term consolidates several Hebrew terms — name the pattern. Where the distribution is unremarkable, do not comment.
- **The relationship between the terms.** Where the terms are clearly related (verb/noun pairs from the same root; cognates; person-type terms paired with quality terms), name the relationship briefly. The reader who scans the table should leave the commentary with a working sense of *why* these terms are grouped together.

Do **not**:

- List the terms again. The table is right above the commentary; the reader has just read it.
- Cite specific verses. The commentary characterises the vocabulary, not its uses; verses appear in Appendix B and throughout the chapters.
- Pad to fill 120 words if 70 says it well.

### Supportive terms section (no AI commentary required)

The supportive-terms (BOUNDARY) section is a pure table — no AI prose is required there. Leave the table as the generator produced it.

---

## 4. Appendix B — what to write

Appendix B is a single large table. Most rows are fully populated by the generator. The AI work is:

### Filling the "Meaning of the term in this study" column for verses where it reads `_AI to fill from meaning-group context_`

These are verses whose `verse_context.analysis_note` is empty in the DB. For each such row:

- Read the verse text in the row.
- Read the meaning-group description in the row (the "Meaning-group" column).
- Write a tight one-line entry (≤20 words) capturing what the term carries **in this specific verse** within the context of the study.
- The format should match the rows that the generator filled from `analysis_note`: short, often a verbatim fragment of the verse text in quotation marks followed by a brief gloss. (E.g. `"let the word of Christ dwell in you richly" — logos as the indwelling instructive word`.)

Do **not** invent meaning that goes beyond what the verse text and the meaning-group context support. If the verse offers thin evidence for what the term carries here, give the lightest reading that the verse honestly supports.

### Closing note (~40 words, optional)

A short one-sentence closing for the table — e.g. noting the total verse count and pointing the reader toward Appendix A for terms. The closing-note AI-WRITE zone is in the input file. If it adds nothing, you may leave it as a minimal one-liner; do not pad.

Do **not**:

- Rewrite or overwrite cells that the generator filled from `analysis_note`. Those are the researcher's per-verse readings as recorded in the DB.
- Add columns or change the table structure.

---

## 5. Appendix C — what to write

### Method note (~150 words)

A single plain-English paragraph acknowledging the analytical method behind the study. The paragraph should:

- State that the study draws from a structured analytical record covering the verse evidence for each characteristic.
- Note that key verses were selected as the evidential foundation for each meaning group.
- State plainly that **no claim in the chapters above is made without specific verse evidence behind it**.
- Briefly acknowledge the cluster status and the version of the analytical record (drawn from the metadata block in the input). The reader does not need the dates; they need to know the study reflects a defined snapshot.

Do **not**:

- Use the words *cluster*, *tier*, *finding*, *sub-group*, or any other jargon (per shared style §3).
- Describe the technical pipeline (catalogue prompts, Phase 8, the database). The method note is for the reader, not for the researcher.
- Go beyond ~150 words. The method note is brief by design.

---

## 6. How to read the three inputs together

You receive three input files. Read all three before writing anything — the appendices reference each other (e.g. App B's closing may point the reader to App A; App A's opening should be calibrated against the rest of the appendix). Once you have the shape of all three in mind, write into the zones in any order; the three drafts can be returned together.

---

## 7. Output

For each appendix, return its input file with prose written into every AI-WRITE zone:

- Replace each `<!-- AI WRITE: … -->` marker block AND the placeholder underneath it with the finished prose. Remove the marker block entirely.
- Leave each `<!-- EVIDENCE: … -->` block exactly as it is.
- For Appendix B, leave generator-filled rows untouched; only fill the `_AI to fill from meaning-group context_` cells.
- Keep the appendix title and all section headers intact.
- Save your outputs as the three draft filenames listed in this instruction's header.

---

## 8. Quality bar

The appendices pass the quality bar when:

1. **Appendix A** has a one-sentence opening, a commentary paragraph for every non-BOUNDARY characteristic, and the supportive-terms section is left as a pure table.
2. **Appendix A** commentaries characterise the term group without re-listing the terms.
3. **Appendix B** has every `_AI to fill from meaning-group context_` cell filled with a one-line per-verse reading consistent in shape with the generator-filled cells.
4. **Appendix B** has the closing note written (or kept minimal) — generator-filled rows are untouched.
5. **Appendix C** has a single ~150w plain-English method-note paragraph that states the verse-evidence basis without jargon.
6. No appendix exceeds its length guidance materially.
7. No jargon from the shared instruction's avoid-list appears.

---

## 9. Completion procedure

Per shared style §12, on completion you:

1. **Write** all three appendices.
2. **Reverse audit** (shared §10): for App A, confirm every characteristic has its commentary. For App B, confirm every `_AI to fill_` placeholder has been replaced with a real one-line reading (none left behind). For App C, confirm the method note acknowledges the verse-evidence basis.
3. **Self-review pass** (shared §11): repetition → overreach → padding → tonal drift → structural drift. Appendices are particularly prone to **padding to fill a length range** — read with a sharp eye and pull anything that adds no content. The 30-word opening sentence should be one sentence; if it's two, one is filler.
4. **Return** the three finished appendix files.
