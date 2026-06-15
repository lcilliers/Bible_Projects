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

**So:** language and mode agree everywhere they can. If you want the field to *distinguish* Aramaic, the clean fix is to add an "Aramaic" value (or derive language from the morph prefix) for the 866 Dan/Ezr/Jer occurrences — optional; nothing is currently wrong.

> Note: the same all-caps-indeclinable case mislabels Greek adverbs/particles in the readable column of `outputs/markdown/wa-mode-field-visual-20260615.md` (e.g. `ADV` shown as "Aramaic adverb"). The stored `morph_code` is correct; only that display label is affected. Low priority.

## CHECK B — verse testament vs books table

- **Mismatches (verse.testament ≠ books.testament via book_id): NONE.**
- **229,956** verse rows where the per-verse testament **agrees** with the book's testament.
- 0 rows with NULL testament; 0 orphan `book_id`s.
- **1** row with NULL `book_id`: `1Cor 12:31` (id 132805) — and it is **`delete_flagged=1`** (soft-deleted), `testament='NT'` still correct. Negligible; optionally set its `book_id` for tidiness.

**Testament is fully consistent with the books table.**
