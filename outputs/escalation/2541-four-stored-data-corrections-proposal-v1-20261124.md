# #2541 — Proposed corrections to the four stored-data errors of thought stage 1 (from #2533)

Raised by Claude, 2026-11-24, on the researcher's option A of #2533 v3. Nothing in the database was changed. Every value below was read from `iba/app/db/iba.db` on 2026-11-24.

## What the researcher is asked to decide

Approve, change or reject each of the four corrections (section 2), and rule on the one question that blocks three of them: how a correction to the source spine is held (section 1).

## 1. The blocking question: no procedure exists yet for correcting these tables

- `verse_lexical` is a derived layer: `cfg_table.use` says it is the mechanical reading of `span` and is rebuilt by `iba/app/lib/lexical.py` (`write_readings_for_span`, which updates and deletes rows). A hand edit of a `verse_lexical` row is overwritten by the next rebuild of that verse.
- `span` is recorded as "SOURCE, immutable" (`cfg_table.use`): a parse of STEP's own verse text. No override table, correction table or procedure for it is registered (searched `cfg_table`, `cfg_setting` and `iba/app/USER-GUIDE.md`).
- Rule B:105 forbids me to design and build a mechanism in the same pass, and B:44 makes a new decision point terminal. So I propose the corrections and the options for holding them, and build nothing.

Options for holding a correction that survives a rebuild:

- **A (recommended).** A small correction table keyed on `span_id` and `code_ordinal` (field, stored value, corrected value, reason, escalation), read by `lexical.py` when it writes a row, with each application recorded in `cfg_change_detail`. It keeps `span` immutable and survives rebuilds. This is new schema, so it comes back to you as a design on its own escalation before any build, then a test on a copy and a BUILD entry.
- **B.** Correct the `verse_lexical` row directly and leave a note in the observation. Simple, but a rebuild of the verse undoes it, so the observation text and the table disagree again.
- **C.** Leave all four as flagged in the observation texts (RG-16) and correct nothing in the tables.

Case 2.3 is different: it sits in two lemma tables, not in `span`, and needs no new mechanism.

## 2. The four cases

### 2.1 1Cor 2:11, `verse_lexical` 1484168 (span 904504, G3588): empty morph code

- Stored: `strong` G3588, `morph_code` NULL on the row and `''` on the span; `surface` `thoughts`; `unit_role` sole; `role` ["T2"].
- Verse (ESV): "…no one comprehends the thoughts of God except the Spirit of God." The neighbouring spans carry morph codes (G2316 N-GSM-T, G3762 A-NSM, G6063 V-RAI-3S); the G3588 span alone has none.
- Finding: G3588 is the article. Its morph is empty on the span, which is the source layer, so the gap is not made by our derivation.
- Proposed correction: none to the value of `strong`. Record the empty morph as a known source gap on this row (a correction row under option A) and keep reading it as the article standing for the omitted noun in the genitive phrase, as the observation already says. I do not propose inventing a morph code that the source does not give.
- Not checked: STEP's current answer for this verse (STEP was not queried).

### 2.2 Eze 19:10, `verse_lexical` 1369520 (span 818297, H1961): copula aligned into `reason`

- Stored: H1961, morph HVqp3fs, `surface` `reason`, `unit_size` 1, `unit_role` sole. Neighbours: `by` is H9006, `abundant` H7227A, `water` H4325G.
- Verse (ESV): "Your mother was like a vine in a vineyard…, fruitful and full of branches by reason of abundant water." H1961 in the form stored (qal perfect 3fs) is the copula of the first clause, "was"; ESV's "by reason of" is built on H9006 and the noun after it.
- Finding: the copula H1961 is aligned to the English word `reason` at position 10, so the unit reads "reason" where it should read the clause copula "was".
- Proposed correction: set the surface of this occurrence to `was` (the first clause's copula) and leave `reason` to the unit of H9006. Before it is applied I must locate the position of "was" in `span` for this verse; I have not.
- Not checked: STEP's alignment for this verse.

### 2.3 Pro 5:21, H6424: the stored sense head reads "to envy"

- Stored: `strong_sense` row for H6424 (`head` "to envy", `is_own_lemma` 1) and `lemma_inventory` id 15848 (`lemma_key` H6424, `gloss` "to envy", source `lemma-inventory-master-2026`). The same gloss "to envy" is stored for G5354 (id 21237), the Greek word.
- Evidence: the parsed lexicon from STEP, `strong_meaning_parsed` ids 5210538 to 5210540 for H6424, reads "(Piel) to weigh, make level, balance", "to weigh out", "to make level or smooth". The verse (ESV): "he ponders all his paths", which fits "weigh".
- Finding: the H6424 inventory gloss equals the G5354 gloss and contradicts the lexicon line. It reads as a copy from the Greek row; I have not proven how it got there. `strong_sense.head` is defined as the first line of the lexicon's mediumDef, which for H6424 is "to weigh, make level, balance".
- Proposed correction: set `lemma_inventory` 15848 `gloss` and `strong_sense` H6424 `head` to "to weigh, make level, balance", with the old value kept in the change record. These are two non-source tables and the change needs your approval, not a new mechanism. Every occurrence of H6424 reads the same head, so it repairs them all.
- Not checked: whether any other H-code carries a Greek gloss. It is a one-query test I can run on approval, and it would turn this single correction into a class.

### 2.4 Rom 4:19, `verse_lexical` 1478906 (span 831566, G3756): negator inside the unit "considered"

- Stored: span 831566 `surface` `considered`, `strong_variant` "G2657 G3756", morph "V-AAI-3S PRT-N"; both rows have `unit_surface` `considered`, `unit_size` 2, `unit_role` content_part; row 1478906 has `is_negator` 1, `role` ["T5"]. Neighbours: position 2 `weaken` G0770G, position 3 `faith` G4102G.
- Verse (ESV): "He did not weaken in faith when he considered his own body…". The source aligns the negator PRT-N to the word `considered`, while in the English the negation bears on "weaken in faith".
- Finding: this is the source alignment, stored as given. Read as a negation of the considering it gives the wrong sense; the observation already says so.
- Proposed correction: none to the code or the text. Keep the row and record on it that its negation bears on the unit of G0770G (`weaken`, span 831564), so a reader of the row, not only of the observation, is not led to read "did not consider". Under option A this is a correction row; under option B nothing can be held beyond the observation text.
- Not checked: the Greek word order against the source alignment.

## 3. What each option leaves

| Case | Option A | Option B | Option C |
|---|---|---|---|
| 2.1 1Cor 2:11 | gap recorded on the row | edit lost on rebuild | left flagged |
| 2.2 Eze 19:10 | surface corrected, survives | edit lost on rebuild | left flagged |
| 2.3 Pro 5:21 | corrected in two lemma tables, no new schema | same | left flagged |
| 2.4 Rom 4:19 | negation target recorded | edit lost on rebuild | left flagged |

## 4. Recommendation

Approve 2.3 now as a data correction of two lemma-table rows. Approve option A in principle for 2.1, 2.2 and 2.4, on the condition that its schema comes back to you as a design on a new escalation before it is built.
