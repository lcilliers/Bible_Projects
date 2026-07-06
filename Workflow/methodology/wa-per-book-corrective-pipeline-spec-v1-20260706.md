# Per-book corrective pipeline — SPECIFICATION (v1)

> The explicit, repeatable specification for correcting each book's verse-record completeness. Written after the Psalms pilot (where the steps were discovered ad-hoc) so the remaining books follow a documented process, not improvisation. Applies to all 66 books; ~27 were "read" under the old method that added **zero** verse-records. Date: 2026-07-06.

## Purpose
The book-reading phase added no `wa_verse_records`, and the old coverage gate was circular. The authoritative full-text index (`verse_span_index`, one row per word-occurrence with `primary_strong`, `morph_code`, `verse_id`) is complete; the verse-record + role layers are not. This pipeline reconciles each book to the master index.

## The six steps (mechanical = script; analytical = reading)

| # | Step | Type | Tool / method | Output | Validation |
|---|------|------|---------------|--------|------------|
| a | Scope the book | mechanical | pick `book_id` | — | — |
| b | Reading units + linkages | mechanical | confirm `verse_span_index` present; ensure verse-records carry `verse_span_id` | linked FKs | spans>0 |
| c | **Role reassessment** | **ANALYTICAL** | read every real-strong span in context → `characteristic / qualifier / standalone` (decided by meaning-in-context, never a term list); write `ve_lexical` ve_nr=115, `source_provenance='role-reassess-2026'` | per-span role | every span roled; prior roles NOT trusted (Psalms: only 43% survived) |
| d | Gate-1 completeness | mixed | from step-c characteristic spans, find strongs with no registered OWNER → **registry assignment (analytical)** → `audit_word --registry=N --extract-file=<curated> --add-terms` (isolated file; curate the `terms` array; NOT `--fetch-step`) → finishing fields → `_apply_create_vc_for_onboarded` | onboarded terms | every characteristic strong registered |
| e | Master-index backfill + validate | mechanical | `_apply_master_index_backfill_v1 --book N --with-ambiguous` (fully-scaffolded records from the index: term_inv_id+word_registry_fk+mti_term_id+verse_span_id) | verse-records | characteristic-span MISS = 0; integrity snapshot/compare shows only expected deltas, no new invariant breach |

## Per-book state assessment (run first)
```sql
-- master-index spans (must be >0)
SELECT COUNT(*) FROM verse_span_index WHERE verse_id IN (SELECT id FROM verse WHERE book_id=?);
-- role reassessment done? (ve_nr=115, role-reassess-2026)
SELECT COUNT(*) FROM ve_lexical vl JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id
  JOIN verse v ON v.id=vsi.verse_id WHERE v.book_id=? AND vl.ve_nr=115 AND vl.source_provenance='role-reassess-2026';
-- verse-record gap: registered-OWNER spans lacking a record (see _apply_master_index_backfill --dry-run)
```

## Governance / safety (every book)
- **Integrity gate:** backup DB → `_check_integrity_controls --snapshot` pre → writes → snapshot post → `--compare`. Expect only intended deltas; **no new invariant breach** (baseline `dup_owner_strong=1` G0150, `velex_orphan_vc` are pre-existing). Restore on unexpected deltas.
- **Audit framework** for term onboarding: stamp new mti `anchor_note='gate1-onboard-2026'`; `_audit_gate1_additions` reconciliation + collateral detector (existing terms must be preserved, delta +0).
- All workings filed to `.md`; commit incrementally.

## Known limitations (fix forward)
- Backfill owner-join is **exact-strong**; base-vs-sub-entry mismatches (e.g. Psalms H7307 *ruach*, OWNER inventory `H7307H/I` vs mti base `H7307`) need a targeted fix or a base-matching owner resolver (v2 TODO).
- Ambiguous multi-sub-entry bases resolved by **dominant sense** (OWNER sub-entry with most existing records) — imperfect; validated per book.
- Onboarding into a populated registry uses `--add-terms` (isolated file, no whole-registry re-audit). Reused-mti terms need `mti_term_id` verse backfill (Group-A pattern).

## Status
- **Psalms (book 19): (a)–(e) COMPLETE** — characteristic-span MISS 0; 124 orphan terms onboarded (97 + 27); ~3,486 backfilled records. (Steps b–c were done in a prior session; d–e this session.)
- **Proverbs (book 20): step (e) mechanical backfill DONE** (+1,231 registered-term records, integrity clean). **BUT step (c) role reassessment = NOT done** (0 `role-reassess-2026`; 45,921 legacy ve_lexical whose roles are unreliable). Therefore **(d) gate-1 orphan identification is blocked** — characteristic orphans can't be identified without the role layer.

## ⚠ The scaling bottleneck (needs a decision)
Step (c) **role reassessment is analytical reading**, per span, per book. Psalms' was 150 chapters read in a prior session. Across ~27 books this is the dominant cost. Options to decide before mass rollout:
1. Do the full analytical role reassessment per book (highest fidelity, highest cost).
2. Run only the **mechanical backfill** (step e) across all books now — closes the verse-record gap for *registered* terms immediately — and schedule the role reassessment + gate-1 as a separate analytical pass.
3. Hybrid per book as capacity allows.

*Filed 2026-07-06. This spec is the reference for every remaining book.*
