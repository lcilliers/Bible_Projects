# Session Startup — New Word File Generator
## Framework B Soul Word Analysis | Phase 1 | v1 Specification

---

## What this session produces

**Two files:**

1. `word_[word].md` — the pre-populated source file ready for STEP data entry
2. `WA-MTI-framework-b-terms-[yyyy-mm-dd].json` — the MTI updated with the new word's terms marked as `pending`

---

## What you must provide at the start of this session

1. **Word and registry ID** — e.g. "sorrow, registry 154"
2. **Header text** — the brief description from the originating word list
3. **STEP term list** — the full list of terms as plain text, exactly as retrieved from STEP, one term per line in the format: `gloss (transliteration - script)`
4. **The current MTI file** — `WA-MTI-framework-b-terms-[yyyy-mm-dd].json` uploaded as an attachment
5. **Any exclude instructions** — terms flagged for exclusion from the word file

---

## Process sequence — follow this order exactly

**Step 1 — Parse the STEP term list.**
Extract the gloss, transliteration, and Strong's number for every term. If a Strong's number is not supplied with the list, derive it from the transliteration and gloss using the MTI. Flag any term where the Strong's number cannot be confirmed — do not guess.

**Step 2 — Run the MTI lookup.**
For every term in the list, check the Strong's number against the MTI.
- Match found → cross-reference term. Note: owning registry, owning word, owning part.
- No match found → new term. Needs full extraction in STEP.
- Flagged exclude → exclude. Remove from both lists.

**Step 3 — Produce the lookup report.**
State the counts: total terms | excluded | cross-reference | new. List all three categories clearly.

**Step 4 — Generate `word_[word].md`.**
Follow the file structure defined below exactly.

**Step 5 — Update the MTI.**
For every new term (not cross-reference, not exclude): add a record to the MTI with `status: "pending"`. Set `owning_registry` and `owning_word` from the new word's details. Do not add cross-reference terms again.
For every cross-reference term: add the new registry to the `also_used_in` array of the existing MTI record.
Save the updated MTI with today's date in the filename.

---

## word_[word].md file structure

### Line 1 — Registry header

```
### [word] registry [id]
```

### Line 2 — Source list

```
> **Source list:** `[source list name]`
```

### Lines 3–6 — Header block

The header text provided, formatted as plain prose. Include the Hebrew/Greek note lines and Conceptual Search Terms and STEP Bible Suggestion lines if provided.

### STEP verses section

```
STEP verses
```

Then the full STEP term list, one term per line, with inline tags applied:

- New terms: `- gloss (transliteration - script)` — no tag, plain entry
- Cross-reference terms: `- gloss (transliteration - script) [XREF: registry NNN word]`
- Excluded terms: omit entirely

### Divider

```
---
```

### New term blocks — one block per new term, in the order they appear in the STEP list

Each block:

```
### gloss (_transliteration_ - script)

Word analysis


[3 blank lines]

```

The heading uses the exact gloss and transliteration from the STEP list.
"Word analysis" is on the line immediately after the heading, followed by 3 blank lines.
This gives space to paste the STEP word analysis content and verses directly below.

### Cross-reference section — at the end of the file

```
---

<!-- CROSS-REFERENCE TERMS — analysis held in owning registry. No STEP extraction needed. -->

```

Then one line per cross-reference term:

```
- gloss (transliteration - script) [XREF: registry NNN word]
```

---

## Rules

- Do not include excluded terms anywhere in the output file
- Do not create word analysis blocks for cross-reference terms
- Do not add content to the word analysis blocks — leave them blank for the researcher to fill
- Transliteration only — no script characters in section headings
- File name: `word_[word].md` using underscore, lowercase

---

## MTI update rules

- New terms: add with `status: "pending"`. Do not mark as `extracted` — that is done at the end of Session A.
- Cross-reference terms: add new registry to `also_used_in` only. Do not change `owning_registry`.
- Save MTI with updated date in filename: `WA-MTI-framework-b-terms-[yyyy-mm-dd].json`
- Both the word file and the updated MTI must be delivered at the end of this session.
