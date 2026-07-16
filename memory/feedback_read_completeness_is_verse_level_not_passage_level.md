---
name: feedback_read_completeness_is_verse_level_not_passage_level
description: A book read is complete only when every VERSE is covered, not every passage; guard against passage_id-orphan verses.
metadata:
  type: feedback
---

A passage-driven lexical read (pull passages by id, read char-by-char) can **silently exclude verses that have no `passage_id`**. In the Proverbs reread (2026-07-14 book-close) this was real: **116 of 915 verses had `passage_id = NULL`** and were never pulled; 24 carried genuine inner-being content (e.g. Agur's contentment prayer 30:7-8, faintheartedness 24:10, several sluggard verses). The read was "701/701 passages" complete yet only **87% of verses**. The gap was not caught until the book-close audit because per-cycle conformance was passage-range-scoped.

**Why:** "complete" was measured as passages-read; passage ids also don't track verse order, so a "resume at max id + 1" high-water mark can't see orphan verses.

**How to apply:**
- Define **"book complete" as verse-level coverage**, never passage-level.
- Run a **verse-coverage pre-flight** at book-start (in `_check_book_lexical_readiness`): assert every verse ∈ a passage OR an explicit skip-list; block the read until totals reconcile (verses-in-passages + orphans = book total).
- Add a cheap **book-wide verse-coverage assertion each cycle**, not only a passage-range conformance check.
- The apply/conformance tooling being **span-id-based** (not passage-based) is what let the gap be closed later without restructuring passages — keep tooling span-id-first.

Related: [[project_passage_reading_checkback_gate]], [[project_book_lexical_readiness_assessment]], [[project_reread_success_gates_and_scored_audit]], [[feedback_no_stats_trends_review_fabricated_data]].
