# What's actually in the DB — the per-term-in-verse record-set (orientation)

> Researcher (2026-06-15): *"Why did the sense/finding issue not come up when mode was updated? Am I visualising the record-set correctly? What is actually in the database?"* Verified answer below. Your mental model is right in spirit; three refinements.

## The analytical unit is the TERM-IN-VERSE, not the verse
A record-set hangs off **(verse_context_id, mti_term_id)** — one term as used in one verse. A verse containing 5 in-scope terms has **5** record-sets, not one.

## The 14 VE fields are stored in TWO different layers (this answers Q1)
| field kind | where it lives | examples | how updated |
|---|---|---|---|
| **Bedrock per-occurrence facts** | **COLUMNS** on `wa_verse_records` / `wa_verse_term_links` | **mode #4** = `morph_code`/`stem`; **span** = `span_strong_match`; **language**; **subgloss** = `step_subgloss_label` | direct column writes (e.g. the morph backfill) |
| **Interpretive fields** | **FINDINGS** (rows in `finding`, each linked to a catalogue question) | sense (Lexical), type (Kind), compound (Co-occurrence), mode-of-operation (Modes), location, faculty… | finding writes |

**This is why the sense issue didn't surface when mode was updated:** **mode (#4) is a COLUMN, not a finding** (verified: 0 findings link to a morphology question). The morph backfill touched `wa_verse_records.morph_code/stem` and never went near the finding model. **Sense (#1) is a FINDING** ('Lexical and Semantic Analysis'), so fixing it is a finding-model operation — a different layer entirely.

## What the finding record-set actually looks like (your model, refined)
Each finding = **one catalogue question (the KEY) + `finding_value` (the VALUE)** — your key/value picture is exactly right. But:
- the **keys** are the **173 tiered catalogue questions** (T0–T7), not literally "1–14"; the 14 VE fields are a *conceptual grouping* that maps into those questions;
- coverage is **partial and uneven by provenance**:

| provenance | term-in-verse units | findings / unit | what it is |
|---|---|---|---|
| **`l2_api`** (read; M01/M15) | 8,294 | **~22** | the fuller read field-set |
| **`l2_mechanical`** (bulk) | 23,154 | **~5** | only the mechanically-derivable fields (Lexical/sense, Kind/type, Modes, Co-occurrence, + location) |

- **30,224** distinct term-in-verse units have *any* VERSE finding, out of **42,704** active verse_context rows → **~12,500 units have none yet**.
- So "not all of the fields are completed" is correct, and more so than it looks: the bulk has only ~5 of the ~22 fields; the full set exists only for the read clusters.

## So, your three statements — scored
- ✅ "a record-set with a key and a value" — **right** (catalogue question + finding_value).
- ⚠️ "every **verse**" — it's per **term-in-verse**.
- ⚠️ "the **1–14** items" — the keys are the **173 catalogue questions**; mode #4 isn't among them (it's a column).
- ✅ "these add up to the **145,000** bulk" — **right** for `l2_mechanical` (23,154 units × ~5 ≈ 145,720) — but that's one provenance; `l2_api` adds another 186,455.

## Why this matters for the sense fix
Sense is the **'Lexical and Semantic Analysis'** finding, present on **every** l2_mechanical unit (23,154) but carrying the **uniform term gloss** instead of the per-occurrence subgloss. The fix operates **only on findings** (not columns) — replace that value with the per-occurrence `step_subgloss_label`, de-dup against `l2_api`, set `verse_context.sense_id`. See `wa-sense-operation-setup-v1-20260615.md`.
