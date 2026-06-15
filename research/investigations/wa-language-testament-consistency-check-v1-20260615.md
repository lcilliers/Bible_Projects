# Language & testament fields — consistency check

> Researcher request (2026-06-15): *"is the language field consistent with the mode, and the testament consistent with the books table."* Fields: `mti_terms.language` (per term), `wa_verse_records.testament` + `book_id`, `books.testament`. Mode = `morph_code` prefix (H=Hebrew · A=Aramaic · Greek = hyphenated `N-`/`V-`/`A-` or the all-caps indeclinables like `ADV`). Read-only.

## Verdict
- **Language vs mode — consistent.** No genuine conflicts. The only divergences are explained by a *granularity limit* of the language field, not an error.
- **Testament vs books — fully consistent.** 0 mismatches across 229,956 rows.

## CHECK A — term language vs mode (58,340 occurrences with morph)

| term language | morph language | count | reading |
|---|---|---|---|
| Hebrew | Hebrew | 46,751 | ✓ agree |
| Greek | Greek | 10,545 | ✓ agree |
| Hebrew | Aramaic | 866 | see (1) |
| "Greek" | "Aramaic" | 178 | see (2) — false alarm |

**57,296 agree directly.** The two divergence buckets:

1. **866 "Hebrew → Aramaic"** are all in **Daniel (738) · Ezra (123) · Jer (5)** — the genuinely Aramaic portions of the OT. They are **correctly Aramaic in morph**, but `mti_terms.language` carries them as **"Hebrew"** because **the language field has only two values — Hebrew and Greek, no "Aramaic"** (Biblical Aramaic words use H-Strong's numbers and are folded under Hebrew). This is a **granularity limitation, not an inconsistency**: the term-level field cannot express Aramaic; the morph-level mode can and does.
2. **178 "Greek → Aramaic"** were a **false alarm in the checker**, not the data — every one is the Greek morph code **`ADV` / `ADV-C`** (adverb), an all-caps Robinson indeclinable that my prefix test misread as `A`=Aramaic. They are correctly Greek.

**So:** language and mode agree everywhere they can.

## Resolution (2026-06-15) — fixed the classifier, deliberately NOT the data

**Fixed (code):** built one canonical classifier — `scripts/analytics/morph_util.py` (`morph_language` / `morph_category` / `morph_stem` / `morph_readable`) — so checks and the visual stop re-implementing (and re-bugging) the H / A / Greek discrimination. Re-run with it: term↔morph language now **57,788 direct agree · 866 Aramaic-folded-under-Hebrew (expected) · 0 `ADV` false-alarms**. The mode visual (`outputs/markdown/wa-mode-field-visual-20260615.md`) was regenerated and now labels `ADV`→Greek adverb, `AR`/`AC`→Aramaic preposition/conjunction correctly.

**Deliberately NOT done (data):** overwriting `mti_terms.language='Aramaic'` for the 866 would **create the very "noise later" it was meant to remove**, because the field is coupled to a Hebrew/Greek binary:
- `scripts/analytics/step_client.py:200` **derives** `language` from the Strong's prefix (`G…`→Greek, else Hebrew) on every term sync — so the next `audit_word` would **revert** any Aramaic override.
- `engine/meaning_parser.py:238` branches on `language == "Hebrew"` for Hebrew-style meaning parsing — Aramaic uses the same script/lexicon, so a relabel would make those terms **fall through and miss parsing**.

The Aramaic distinction is **already precise where it belongs — in the morph code** (the 866 are exactly the A-prefix Dan/Ezr/Jer occurrences). The term-level `language` field is, by design, "Hebrew-script vs Greek", with Aramaic subsumed under Hebrew. **Verdict: not an inconsistency — leave the field; the morph carries Aramaic.** If a *persistent, queryable* term-level Aramaic flag is ever wanted, the safe route is a **separate column** (e.g. `script_language`) derived from the morph — never overwriting the coupled `language`.

## CHECK B — verse testament vs books table

- **Mismatches (verse.testament ≠ books.testament via book_id): NONE.**
- **229,956** verse rows where the per-verse testament **agrees** with the book's testament.
- 0 rows with NULL testament; 0 orphan `book_id`s.
- **1** row with NULL `book_id`: `1Cor 12:31` (id 132805) — and it is **`delete_flagged=1`** (soft-deleted), `testament='NT'` still correct. Negligible; optionally set its `book_id` for tidiness.

**Testament is fully consistent with the books table.**
